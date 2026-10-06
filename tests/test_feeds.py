"""Feed-Auswertung und Archivabgleich ohne Netzwerkzugriffe."""

import importlib.util
from pathlib import Path
from datetime import datetime, timezone
import re
import sys
from unittest.mock import patch

import pytest


ROOT = Path(__file__).resolve().parents[1]
for name in ("ingest_source", "themen", "feeds"):
    spec = importlib.util.spec_from_file_location(name, ROOT / "70_Scripts" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
feeds = sys.modules["feeds"]


def test_rss_sorts_unsorted_entries_and_deduplicates_tracking():
    xml = b'''<rss version="2.0"><channel><title>Example</title><link>https://example.org</link>
    <item><title>Alt</title><link>/old</link><pubDate>Mon, 01 Jun 2026 12:00:00 GMT</pubDate></item>
    <item><title>Neu</title><link>/new?utm_source=mail</link><pubDate>Mon, 05 Oct 2026 12:00:00 GMT</pubDate></item>
    <item><title>Dublette</title><link>/new</link></item>
    <item><title>Unbekannt</title><link>/unknown</link><pubDate>kein Datum</pubDate></item>
    <item><title>Ohne Link</title></item>
    <item><link>javascript:alert(1)</link></item>
    </channel></rss>'''
    title, website, format_name, entries = feeds.parse_feed(xml, "https://example.org/rss.xml")
    assert (title, website, format_name) == ("Example", "https://example.org", "rss")
    assert [i.titel for i in entries] == ["Neu", "Alt", "Unbekannt"]
    assert entries[0].url == "https://example.org/new?utm_source=mail"
    assert entries[-1].datum is None


def test_atom_uses_article_link_and_publication_date():
    xml = b'''<feed xmlns="http://www.w3.org/2005/Atom"><title>Atom</title>
    <link rel="self" href="/atom.xml"/><link href="/"/>
    <entry><title>Article</title><link rel="self" href="/entry.xml"/>
    <link href="/article"/><published>2026-10-01T11:00:00+02:00</published>
    <updated>2026-10-05T11:00:00Z</updated></entry></feed>'''
    _, website, format_name, entries = feeds.parse_feed(xml, "https://example.org/atom.xml")
    assert website == "https://example.org/"
    assert format_name == "atom"
    assert entries[0].url == "https://example.org/article"
    assert entries[0].datum.isoformat() == "2026-10-01T11:00:00+02:00"


def test_archived_urls_include_sources_and_ignored_inbox_entries(tmp_path):
    inbox = tmp_path / "00_Inbox/Quellen/URL"
    sources = tmp_path / "80_Knowledge/Sources"
    inbox.mkdir(parents=True)
    sources.mkdir(parents=True)
    (inbox / "ignored.md").write_text(
        '---\nurl: "https://www.example.org/old/?utm_source=mail"\nstatus: ignoriert\n---\n', encoding="utf-8")
    (sources / "known.md").write_text('---\nurl: https://example.org/new\n---\n', encoding="utf-8")
    (inbox / "README.md").write_text('url: https://example.org/not-a-source\n', encoding="utf-8")
    with patch.object(feeds, "ROOT", tmp_path):
        assert feeds.bekannte_urls() == {"https://example.org/old", "https://example.org/new"}


def test_invalid_feed_does_not_create_register(tmp_path):
    register = tmp_path / "feeds.yaml"
    with patch.object(feeds, "REGISTER", register), patch.object(feeds, "abrufen", side_effect=ValueError("kein Feed")):
        assert feeds.main(["add", "https://example.org/rss.xml"]) == 1
    assert not register.exists()


def test_duplicate_feed_does_not_fetch_or_rewrite(tmp_path):
    register = tmp_path / "feeds.yaml"
    original = "feeds:\n  - name: Beispiel\n    url: https://example.org/rss.xml\n"
    register.write_text(original, encoding="utf-8")
    with patch.object(feeds, "REGISTER", register), patch.object(feeds, "abrufen") as fetch:
        assert feeds.main(["add", "https://www.example.org/rss.xml?utm_source=mail"]) == 0
    fetch.assert_not_called()
    assert register.read_text(encoding="utf-8") == original


def test_check_continues_after_failed_feed_without_importing(tmp_path, capsys):
    register = tmp_path / "feeds.yaml"
    register.write_text("feeds:\n  - url: https://example.org/bad\n  - url: https://example.org/good\n", encoding="utf-8")
    original = register.read_bytes()
    entries = [feeds.Eintrag("Bekannt", "https://example.org/known", None),
               feeds.Eintrag("Offen", "https://example.org/new", None)]
    with patch.object(feeds, "REGISTER", register), patch.object(feeds, "ROOT", tmp_path), \
         patch.object(feeds, "bekannte_urls", return_value={"https://example.org/known"}), \
         patch.object(feeds, "abrufen", side_effect=[OSError("Abruf fehlgeschlagen"), ("Good", "", "rss", entries)]):
        assert feeds.main(["check", "--limit", "1", "--alle"]) == 1
    output = capsys.readouterr()
    assert "Offen" in output.out and "Bekannt" not in output.out
    assert "Datum unbekannt" in output.out
    assert "Abruf fehlgeschlagen" in output.err
    assert register.read_bytes() == original
    assert not (tmp_path / "00_Inbox/Quellen").exists()


def test_non_feed_xml_is_rejected():
    with pytest.raises(ValueError, match="Kein unterstützter Feed"):
        feeds.parse_feed(b"<html><body>Not a feed</body></html>", "https://example.org")


def test_verified_url_alias_is_known_only_with_archived_original():
    feed = {"url_aliases": {"https://example.org/article": "https://example.org/skills/article"}}
    assert feeds.bekannte_feed_urls(feed, set()) == set()
    assert feeds.bekannte_feed_urls(feed, {"https://example.org/skills/article"}) == {
        "https://example.org/article", "https://example.org/skills/article"}
    assert "https://example.org/other/article" not in feeds.bekannte_feed_urls(
        feed, {"https://example.org/skills/article"})


def regeln():
    return {"verifikation": [("tdd", 3, re.compile(r"\btdd\b"))],
            "planung": [("plan mode", 3, re.compile(r"\bplan mode\b"))]}


def test_feed_descriptions_are_read_as_plain_text():
    xml = b'''<rss><channel><item><title>Example</title><link>https://example.org/a</link>
    <description>&lt;p&gt;Use &lt;b&gt;TDD&lt;/b&gt; &amp;amp; tests.&lt;/p&gt;
    &lt;script&gt;unrelated keywords&lt;/script&gt;</description></item></channel></rss>'''
    entries = feeds.parse_feed(xml, "https://example.org/rss.xml")[3]
    assert entries[0].beschreibung == "Use TDD & tests."
    assert feeds.bewerte_eintrag(entries[0], {}, regeln()).cluster == []
    # Ein einzelner Begriff nur in der Beschreibung reicht hier nicht zur Empfehlung.
    assert feeds.vorauswahl(entries, {}, regeln(), 10)[1] == 0


def test_atom_xhtml_summary_is_not_lost():
    xml = b'''<feed xmlns="http://www.w3.org/2005/Atom"><entry><title>TDD</title>
    <link href="https://example.org/a"/><summary type="xhtml"><div xmlns="http://www.w3.org/1999/xhtml">
    Use <b>TDD</b> before code.</div></summary></entry></feed>'''
    entries = feeds.parse_feed(xml, "https://example.org/atom.xml")[3]
    assert entries[0].beschreibung == "Use TDD before code."


def test_topic_relevance_outweighs_recent_irrelevant_entry():
    today = datetime(2026, 10, 5, tzinfo=timezone.utc)
    older = datetime(2026, 9, 1, tzinfo=timezone.utc)
    entries = [feeds.Eintrag("News", "https://example.org/news", today),
               feeds.Eintrag("TDD guide", "https://example.org/tdd", older)]
    selected, count, excluded = feeds.vorauswahl(entries, {}, regeln(), 10)
    assert [e.eintrag.titel for e in selected] == ["TDD guide"]
    assert count == 1 and excluded == 0
    assert "tdd" in selected[0].gruende[0]


def test_course_landing_page_is_visible_only_in_full_list():
    feed = {"auswahl": {"ausschliessen_pfade": ["/workshops/*"]}}
    entries = [feeds.Eintrag("TDD guide", "https://example.org/workshops/tdd", None)]
    selected, count, excluded = feeds.vorauswahl(entries, feed, regeln(), 10)
    assert selected == [] and count == 0 and excluded == 1
    selected, _, _ = feeds.vorauswahl(entries, feed, regeln(), 10, alle=True)
    assert selected[0].ausschluss == "Auswahlregel: /workshops/*"


def test_shortlist_covers_other_topics_without_losing_newest_articles():
    entries = [feeds.Eintrag("TDD", f"https://example.org/tdd-{day}", datetime(2026, 10, day, tzinfo=timezone.utc))
               for day in [5, 4, 3]]
    entries.append(feeds.Eintrag("Plan Mode", "https://example.org/plan", datetime(2026, 10, 2, tzinfo=timezone.utc)))
    selected, _, _ = feeds.vorauswahl(entries, {}, regeln(), 3)
    assert [e.eintrag.url for e in selected] == ["https://example.org/tdd-5", "https://example.org/tdd-4", "https://example.org/plan"]
    selected, _, _ = feeds.vorauswahl(entries, {}, regeln(), 3, thema="verifikation")
    assert len(selected) == 3 and all(e.cluster == ["verifikation"] for e in selected)


def test_feed_specific_keywords_use_word_boundaries():
    feed = {"auswahl": {"themen_keywords": {"verifikation": ["/pr", "pull request"]}}}
    selected, _, _ = feeds.vorauswahl(
        [feeds.Eintrag("The /pr Skill", "https://example.org/pr", None, "Write a pull request body.")], feed, regeln(), 10)
    assert selected[0].cluster == ["verifikation"]
    selected, _, _ = feeds.vorauswahl([feeds.Eintrag("The /price Skill", "https://example.org/price", None)], feed, regeln(), 10)
    assert selected == []


def test_selection_report_is_a_draft_and_does_not_archive(tmp_path):
    register = tmp_path / "feeds.yaml"
    register.write_text("feeds:\n  - name: Beispiel\n    url: https://example.org/rss.xml\n", encoding="utf-8")
    report = tmp_path / "Auswahl.md"
    original = register.read_bytes()
    entries = [feeds.Eintrag("TDD guide", "https://example.org/tdd", None)]
    with patch.object(feeds, "REGISTER", register), patch.object(feeds, "ROOT", tmp_path), \
         patch.object(feeds, "themen_regeln", return_value=({"verifikation": {"name": "Tests"}, "planung": {"name": "Planung"}}, regeln())), \
         patch.object(feeds, "abrufen", return_value=("Example", "", "rss", entries)):
        assert feeds.main(["check", "--ausgabe", str(report)]) == 0
    text = report.read_text(encoding="utf-8")
    assert "Vorauswahl" in text and "kein Qualitätsnachweis" in text and "TDD guide" in text
    assert register.read_bytes() == original
    assert not (tmp_path / "00_Inbox/Quellen").exists()
