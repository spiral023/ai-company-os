"""Exportlogik mit kleinen Fixtures testen, ohne private Kursvolltexte in Git."""
from pathlib import Path
import sys
import unittest

from bs4 import BeautifulSoup
from markdown_it import MarkdownIt

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import build_downloads as builder


FIXTURE = """<html><head><style>body{color:#123}</style></head><body><div class="wrap">
<header class="mast"><h1>Course</h1></header>
<article class="chapter" id="first"><header class="chapter-head"><h1>First<a class="anchor" href="#first">#</a></h1></header>
<p>A <strong>precise</strong> explanation with <code>some_code</code>.</p>
<div class="video-local"><a href="videos/001.mp4">Video</a></div><video src="private.mp4"></video>
<figure><button class="shot"><img src="medien/001.png" alt="Illustration"></button><figcaption>Image caption</figcaption></figure>
<pre><code>line_one\n```nested\n\tline_two\n</code></pre><pre><code></code></pre>
<ul><li><label class="task"><input type="checkbox">Do <code>one_thing</code></label></li><li><label class="task"><input type="checkbox">Do another thing</label></li></ul>
<article class="q" data-correct="b"><p class="q-text">Which answer?</p><div class="choices"><button class="choice" data-choice="a"><span class="key">A</span><span class="label">First choice</span></button><button class="choice" data-choice="b"><span class="key">B</span><span class="label">Second choice</span></button></div><div class="explain" hidden><p>The full explanation.</p></div></article>
<nav class="pager">Next</nav></article><article class="chapter" id="second" hidden><h1>Second</h1><p>Final content.</p></article>
<footer class="colophon">Progress<button>Reset</button></footer><script>window.sideEffect = true</script></div></body></html>"""
IMAGE = {"nr": 1, "url": "https://res.cloudinary.com/example/image.png", "breite": 100, "hoehe": 50}
ENCODED = {1: "data:image/png;base64,cG5n"}


class DownloadBuildTests(unittest.TestCase):
    def test_removes_video_and_controls_but_keeps_image_and_every_chapter(self):
        content = builder.prepare_content(FIXTURE, "de")
        self.assertEqual(len(content.select("article.chapter")), 2)
        self.assertEqual(len(content.select("img")), 1)
        self.assertFalse(content.select("button, script, video, .video-local, .pager, .colophon, [hidden]"))
        self.assertIn("Final content.", content.get_text())
        self.assertIn("Richtige Antwort: B", content.get_text())
        self.assertEqual(content.select_one(".choice.correct .label").get_text(), "Second choice")
        self.assertIn("The full explanation.", content.get_text())

    def test_html_is_standalone_with_embedded_image_and_original_code(self):
        content = builder.prepare_content(FIXTURE, "en")
        builder.configure_images(content, [IMAGE], "embedded", ENCODED)
        result = BeautifulSoup(builder.html_export(FIXTURE, content, "en", "html-embedded-md-links"), "html.parser")
        self.assertEqual(result.html["lang"], "en")
        self.assertEqual(result.img["src"], ENCODED[1])
        self.assertEqual(result.img["loading"], "lazy")
        self.assertEqual(len(result.select(".export-toc a")), 2)
        self.assertEqual(result.pre.get_text(), "line_one\n```nested\n\tline_two\n")
        self.assertFalse(result.select("script, video, iframe, link[href]"))
        self.assertIn("Correct answer: B", result.get_text())

    def test_markdown_keeps_nested_fences_empty_code_tasks_answers_and_links(self):
        content = builder.prepare_content(FIXTURE, "de")
        builder.configure_images(content, [IMAGE], "links", ENCODED)
        markdown = builder.markdown_export(content, "de", "html-embedded-md-links")
        builder.validate_markdown(content, markdown)
        self.assertIn("- [ ] Do `one_thing`", markdown)
        self.assertNotIn("- - [ ]", markdown)
        self.assertIn(IMAGE["url"], markdown)
        self.assertIn("Richtige Antwort: B", markdown)
        code = [token.content.rstrip("\n") for token in MarkdownIt().parse(markdown) if token.type == "fence"]
        self.assertEqual(code, ["line_one\n```nested\n\tline_two", ""])

    def test_missing_images_and_changed_image_order_are_rejected(self):
        content = builder.prepare_content(FIXTURE, "de")
        with self.assertRaises(ValueError):
            builder.configure_images(content, [], "embedded", ENCODED)
        with self.assertRaises(ValueError):
            builder.configure_images(content, [{**IMAGE, "nr": 2}], "links", ENCODED)

    def test_text_only_mode_preserves_image_description(self):
        content = builder.prepare_content(FIXTURE, "en")
        builder.configure_images(content, [IMAGE], "none", {})
        self.assertFalse(content.select("img"))
        self.assertIn("Illustration", content.get_text())
        markdown = builder.markdown_export(content, "en", "text-only")
        builder.validate_markdown(content, markdown)


if __name__ == "__main__":
    unittest.main()
