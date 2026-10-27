"""Kuratierte Factory-Aussagen prüfen, verknüpfen und als Kontext bereitstellen.

Liest den begrenzten semantischen Pilot direkt aus Markdown/JSON. Aktiviert keine
Skills, führt keine Quellprogramme aus und benötigt keinen Volltext-Index.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = Path("80_Knowledge/Factory/pilot.json")
TYPES = {"quellenaussage", "statisch-nachgelesen", "eigene-ableitung", "eigene-regel"}
RELATIONS = {"ergaenzt", "setzt-voraus", "steht-in-spannung", "implementiert"}
STOPWORDS = set("wie was welche welcher welches wir unser unsere unsere fuer für und oder die der das ein eine einem einer den dem von mit zur zum im in ist sind soll sollen kann koennen können bitte moechte möchte ich du es als auf bei aus zu des an am man besser factory software agent agenten system".split())


def resolve(root: Path, relative: str) -> Path:
    path = Path(relative)
    if path.is_absolute() or ".." in path.parts or not relative:
        raise ValueError(f"Ungültiger relativer Wissenspfad: {relative}")
    result = (root / path).resolve()
    if not result.is_relative_to(root.resolve()):
        raise ValueError(f"Wissenspfad verlässt das Repository: {relative}")
    return result


def keyed(items: list, label: str) -> dict:
    if not isinstance(items, list):
        raise ValueError(f"{label}: Liste erwartet")
    result = {}
    for item in items:
        if not isinstance(item, dict) or not isinstance(item.get("id"), str) or not re.fullmatch(r"[a-z0-9][a-z0-9-]*", item["id"]):
            raise ValueError(f"{label}: gültige ID fehlt")
        if item["id"] in result:
            raise ValueError(f"{label}: doppelte ID {item['id']}")
        result[item["id"]] = item
    return result


def require_refs(ids: list, objects: dict, label: str) -> None:
    if not isinstance(ids, list) or any(not isinstance(i, str) or i not in objects for i in ids):
        raise ValueError(f"{label}: unbekannte Referenz")
    if len(ids) != len(set(ids)):
        raise ValueError(f"{label}: doppelte Referenz")


def dependencies(data: dict) -> dict[str, set[str]]:
    result = {claim["id"]: set(claim.get("aus", [])) for claim in data["aussagen"]}
    for relation in data["beziehungen"]:
        if relation["typ"] == "setzt-voraus":
            result[relation["von"]].add(relation["nach"])
    return result


def load(root: Path) -> dict:
    data = json.loads(resolve(root, REGISTRY.as_posix()).read_text(encoding="utf-8"))
    validate(data, root)
    return data


def validate(data: dict, root: Path) -> None:
    if not isinstance(data, dict) or data.get("schema_version") != 1 or data.get("status") != "semantischer-pilot":
        raise ValueError("Nicht unterstützte Pilot-Registry")
    groups = {name: keyed(data.get(name), name) for name in ("belege", "aussagen", "synthesen", "faehigkeiten", "beziehungen")}
    ids = [i for group in groups.values() for i in group]
    if len(ids) != len(set(ids)):
        raise ValueError("IDs müssen über alle Objekttypen eindeutig sein")
    for evidence in groups["belege"].values():
        resolve(root, evidence["pfad"])
        if not isinstance(evidence.get("familie"), str) or not evidence["familie"]:
            raise ValueError(f"{evidence['id']}: Herkunftsfamilie fehlt")
        for field in ("sha256", "bereich_sha256"):
            if not re.fullmatch(r"[a-f0-9]{64}", evidence.get(field, "")):
                raise ValueError(f"{evidence['id']}: ungültiger Hash")
        if type(evidence.get("von")) is not int or type(evidence.get("bis")) is not int or not 1 <= evidence["von"] <= evidence["bis"]:
            raise ValueError(f"{evidence['id']}: ungültiger Zeilenbereich")
        if evidence.get("repo"):
            resolve(root, evidence["repo"])
            if not evidence["pfad"].startswith(evidence["repo"].rstrip("/") + "/") or not re.fullmatch(r"[a-f0-9]{40,64}", evidence.get("revision", "")):
                raise ValueError(f"{evidence['id']}: Repo und Revision passen nicht zum Beleg")
    for claim in groups["aussagen"].values():
        for field in ("aussage", "grenze"):
            if not isinstance(claim.get(field), str) or not claim[field].strip():
                raise ValueError(f"{claim['id']}: {field} fehlt")
        if claim.get("nachweisart") not in TYPES:
            raise ValueError(f"{claim['id']}: unbekannte Nachweisart")
        require_refs(claim.get("beleg_ids", []), groups["belege"], claim["id"])
        require_refs(claim.get("aus", []), groups["aussagen"], claim["id"])
        if not claim.get("beleg_ids") and not claim.get("aus"):
            raise ValueError(f"{claim['id']}: Herkunft fehlt")
    for group in ("synthesen", "faehigkeiten"):
        for item in groups[group].values():
            resolve(root, item["pfad"])
            prefix = "80_Knowledge/Faehigkeiten/" if group == "faehigkeiten" else "80_Knowledge/Vergleiche/"
            if not item["pfad"].startswith(prefix) or not item["pfad"].endswith(".md"):
                raise ValueError(f"{item['id']}: Ansicht liegt außerhalb des vorgesehenen Bereichs")
            for field in ("titel", "zweck", "experiment") if group == "faehigkeiten" else ("titel", "kurzfassung"):
                if not isinstance(item.get(field), str) or not item[field].strip():
                    raise ValueError(f"{item['id']}: {field} fehlt")
            require_refs(item.get("aussage_ids"), groups["aussagen"], item["id"])
            if not item["aussage_ids"]:
                raise ValueError(f"{item['id']}: Aussagen fehlen")
            if group == "faehigkeiten":
                if item.get("status") != "kandidat":
                    raise ValueError(f"{item['id']}: der Pilot unterstützt nur Kandidaten")
                for field in ("eingaben", "ausgaben", "voraussetzungen", "vorgehen", "pruefung", "stop", "laufzeit", "grenzen"):
                    if not isinstance(item.get(field), list) or not item[field] or any(not isinstance(v, str) or not v.strip() for v in item[field]):
                        raise ValueError(f"{item['id']}: {field} fehlt")
            else:
                require_refs(item.get("faehigkeit_ids", []), groups["faehigkeiten"], item["id"])
    nodes = groups["aussagen"] | groups["synthesen"] | groups["faehigkeiten"]
    destinations = [item["pfad"] for name in ("synthesen", "faehigkeiten") for item in data[name]]
    if len(destinations) != len(set(destinations)):
        raise ValueError("Mehrere Ansichten verwenden denselben Pfad")
    for relation in groups["beziehungen"].values():
        if relation.get("typ") not in RELATIONS or not relation.get("begruendung"):
            raise ValueError(f"{relation['id']}: Beziehungstyp/Begründung fehlt")
        require_refs([relation.get("von"), relation.get("nach")], nodes, relation["id"])
        if relation["typ"] == "setzt-voraus" and (relation["von"] not in groups["aussagen"] or relation["nach"] not in groups["aussagen"]):
            raise ValueError(f"{relation['id']}: Voraussetzungen müssen Aussagen verbinden")
    parents = dependencies(data)
    completed = set()
    def visit(key, visiting):
        if key in visiting:
            raise ValueError(f"Zyklische Aussagenableitung: {key}")
        if key not in completed:
            for parent in parents[key]:
                visit(parent, visiting | {key})
            completed.add(key)
    for key in groups["aussagen"]:
        visit(key, set())


def revision(root: Path, path: str) -> str:
    result = subprocess.run(["git", "-C", str(resolve(root, path)), "rev-parse", "HEAD"], capture_output=True, check=False, timeout=15)
    if result.returncode:
        return ""
    return result.stdout.decode("ascii").strip()


def render_card(card: dict, data: dict, root: Path) -> str:
    claims = keyed(data["aussagen"], "aussagen")
    lines = ["<!-- Generiert aus 80_Knowledge/Factory/pilot.json mit wissen karten. -->", f"# Fähigkeitskandidat: {card['titel']}", "", f"**Stand:** {data['stand']} · **ID:** `{card['id']}` · **Status:** Kandidat, nicht aktiviert", "", card["zweck"], ""]
    for field, heading in (("eingaben", "Eingaben"), ("ausgaben", "Prüfbare Ausgaben"), ("voraussetzungen", "Einsatzbedingungen"), ("vorgehen", "Vorgehen als Entwurf"), ("pruefung", "Abnahme"), ("stop", "Stop und Eskalation"), ("laufzeit", "Laufzeit und Wirkungen"), ("grenzen", "Grenzen und Gegenargumente")):
        lines.extend([f"## {heading}", "", *[f"- {value}" for value in card[field]], ""])
    lines.extend(["## Aussagen und Belege", "", "Die IDs verweisen auf die versionierten Belegbereiche in [pilot.json](../Factory/pilot.json). Mehrere Stellen derselben Herkunftsfamilie sind keine unabhängigen Bestätigungen.", ""])
    for key in card["aussage_ids"]:
        lines.append(f"- `{key}` — {claims[key]['aussage']}")
    lines.extend(["", "## Kleinster Versuch", "", card["experiment"], "", "Der Versuch ist vorbereitet. Eine praktische Wirksamkeitsmessung und produktive Übernahme stehen aus. Die bestehende Skill-Registry und die Repo-Freigaberegeln bleiben maßgeblich.", ""])
    return "\n".join(lines)


def cards(root: Path, data: dict, check: bool = False) -> dict:
    validate(data, root)
    mismatches = []
    for card in data["faehigkeiten"]:
        path = resolve(root, card["pfad"])
        expected = render_card(card, data, root)
        if check:
            if not path.is_file() or path.read_text(encoding="utf-8") != expected:
                mismatches.append(card["pfad"])
        else:
            if path.exists() and not path.read_text(encoding="utf-8").startswith("<!-- Generiert aus 80_Knowledge/Factory/pilot.json"):
                raise ValueError(f"Vorhandene fremde Datei wird nicht überschrieben: {card['pfad']}")
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(expected, encoding="utf-8", newline="\n")
    return {"aktuell": not mismatches, "karten": len(data["faehigkeiten"]), "abweichungen": mismatches}


def audit(root: Path, data: dict, views: bool = True) -> dict:
    validate(data, root)
    repo_revisions = {repo: revision(root, repo) for repo in {e.get("repo") for e in data["belege"] if e.get("repo")}}
    evidence_states = {}
    for evidence in data["belege"]:
        state = "aktuell"
        path = resolve(root, evidence["pfad"])
        try:
            content = path.read_bytes()
            lines = content.decode("utf-8-sig").splitlines(keepends=True)
            span = "".join(lines[evidence["von"] - 1:evidence["bis"]])
            if evidence["bis"] > len(lines) or hashlib.sha256(content).hexdigest() != evidence["sha256"] or hashlib.sha256(span.encode("utf-8")).hexdigest() != evidence["bereich_sha256"]:
                state = "datei-geaendert"
        except (OSError, UnicodeError):
            state = "nicht-aufloesbar"
        if state == "aktuell" and evidence.get("repo") and repo_revisions[evidence["repo"]] != evidence["revision"]:
            state = "repo-revision-geaendert"
        evidence_states[evidence["id"]] = {"id": evidence["id"], "status": state, "pfad": evidence["pfad"], "familie": evidence["familie"]}
    claims = keyed(data["aussagen"], "aussagen")
    parents = dependencies(data)
    claim_states = {}
    def evaluate(key):
        if key not in claim_states:
            claim = claims[key]
            ids = set(claim.get("beleg_ids", []))
            for parent in parents[key]:
                ids.update(evaluate(parent)["aufgeloeste_beleg_ids"])
            problems = sorted(i for i in ids if evidence_states[i]["status"] != "aktuell")
            families = sorted({evidence_states[i]["familie"] for i in ids})
            claim_states[key] = {"id": key, "status": "pruefbedarf" if problems else "aktuell", "aufgeloeste_beleg_ids": sorted(ids), "herkunftsfamilien": families, "familienzahl": len(families), "problem_belege": problems}
        return claim_states[key]
    for key in claims:
        evaluate(key)
    node_states = {}
    for item in data["synthesen"] + data["faehigkeiten"]:
        problems = sorted({e for key in item["aussage_ids"] for e in claim_states[key]["problem_belege"]})
        node_states[item["id"]] = {"id": item["id"], "status": "pruefbedarf" if problems else "aktuell", "problem_belege": problems}
    errors = []
    if views:
        errors += cards(root, data, check=True)["abweichungen"]
        for synthesis in data["synthesen"]:
            path = resolve(root, synthesis["pfad"])
            if not path.is_file() or not set(synthesis["aussage_ids"]) <= set(re.findall(r"\bc\d{2}\b", path.read_text(encoding="utf-8"))):
                errors.append(synthesis["pfad"])
    return {"status": "pruefbedarf" if errors or any(e["status"] != "aktuell" for e in evidence_states.values()) else "aktuell", "graph_revision": hashlib.sha256(json.dumps(data, ensure_ascii=False, sort_keys=True).encode()).hexdigest(),
            "scope": "Kuratierter semantischer Pilot; keine vollständige Analyse des Repos und keine Wirksamkeitsmessung.",
            "vollanalyse": False, "wirksamkeit_gemessen": False,
            "anzahl": {"aussagen": len(claims), "belege": len(evidence_states), "herkunftsfamilien": len({e["familie"] for e in data["belege"]}), "synthesen": len(data["synthesen"]), "faehigkeiten": len(data["faehigkeiten"]), "beziehungen": len(data["beziehungen"])},
            "belege": list(evidence_states.values()), "aussagen": list(claim_states.values()), "ableitungen": list(node_states.values()), "ansicht_fehler": errors}


def tokens(text: str) -> set[str]:
    return {w for w in re.findall(r"[\wäöüß-]+", text.lower()) if len(w) > 2 and w not in STOPWORDS}


def context(root: Path, data: dict, question: str, topic: str | None = None) -> dict:
    report = audit(root, data)
    if report["ansicht_fehler"]:
        raise ValueError("Pilot-Ansichten fehlen oder weichen ab: " + ", ".join(report["ansicht_fehler"]))
    words = tokens(question)
    scored = [(len(words & tokens(" ".join([s["titel"], *s["tags"]]))), s) for s in data["synthesen"]]
    if topic:
        selected = [s for s in data["synthesen"] if s["id"] == topic]
        if not selected:
            raise ValueError(f"Unbekannte Synthese: {topic}")
    else:
        selected = [s for score, s in scored if score > 0] or data["synthesen"]
    claims = keyed(data["aussagen"], "aussagen")
    parents = dependencies(data)
    ids = {key for s in selected for key in s["aussage_ids"]}
    seed = set(ids)
    for relation in data["beziehungen"]:
        if relation["typ"] in {"steht-in-spannung", "setzt-voraus"} and (relation["von"] in seed or relation["nach"] in seed):
            ids.update((relation["von"], relation["nach"]))
    ids &= claims.keys()
    def expand(key):
        for parent in parents[key]:
            if parent not in ids:
                ids.add(parent)
                expand(parent)
    for key in list(ids):
        expand(key)
    card_ids = {key for synthesis in selected for key in synthesis.get("faehigkeit_ids", [])}
    selected_cards = [c for c in data["faehigkeiten"] if c["id"] in card_ids]
    for card in selected_cards:
        ids.update(card["aussage_ids"])
    for key in list(ids):
        expand(key)
    checked = keyed(report["aussagen"], "aussagen")
    checked_evidence = keyed(report["belege"], "belege")
    evidence_ids = {e for key in ids for e in checked[key]["aufgeloeste_beleg_ids"]}
    blocked = [checked[key] for key in sorted(ids) if checked[key]["status"] != "aktuell"]
    node_ids = ids | {s["id"] for s in selected} | {c["id"] for c in selected_cards}
    return {"frage": question, "status": "belege-pruefen" if blocked else "bereit", "graph_revision": report["graph_revision"], "scope": report["scope"],
            "vollanalyse": False, "wirksamkeit_gemessen": False, "bereit_fuer": "lesenden-pilot-abruf",
            "auswahl": "explizites-thema" if topic else "schlagworttreffer" if any(n for n, _ in scored) else "pilot-gesamtueberblick",
            "synthesen": [{**({key: s[key] for key in ("id", "titel", "pfad")} if blocked else s), "status": "pruefbedarf" if blocked else "aktuell"} for s in selected],
            "aussagen": [] if blocked else [{**claims[key], **checked[key]} for key in sorted(ids)],
            "beziehungen": [] if blocked else [r for r in data["beziehungen"] if r["von"] in node_ids and r["nach"] in node_ids],
            "faehigkeiten": [] if blocked else selected_cards,
            "belege": [{**e, **checked_evidence[e["id"]]} for e in data["belege"] if e["id"] in evidence_ids], "gesperrte_aussagen": blocked,
            "offene_fragen": data["offene_fragen"], "aktivierung": "keine; bestehende Registry bleibt maßgeblich"}


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help=argparse.SUPPRESS)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("pilot-check", help="Belege, Ableitungen und Kartenansichten prüfen")
    build = sub.add_parser("karten", help="Lesbare Kandidatenkarten aus der Registry erzeugen")
    build.add_argument("--check", action="store_true")
    query = sub.add_parser("kontext", help="Belegte Aussagen, Spannungen und Kandidaten zum Pilot abrufen")
    query.add_argument("frage")
    query.add_argument("--thema")
    args = parser.parse_args(argv)
    try:
        root = args.root.resolve()
        data = load(root)
        if args.command == "karten":
            result = cards(root, data, args.check)
            success = result["aktuell"]
        elif args.command == "pilot-check":
            result = audit(root, data)
            success = result["status"] == "aktuell"
        else:
            result = context(root, data, args.frage, args.thema)
            success = result["status"] == "bereit"
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0 if success else 1
    except (ValueError, OSError, KeyError, TypeError, subprocess.TimeoutExpired) as error:
        print(f"Wissenspilot: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
