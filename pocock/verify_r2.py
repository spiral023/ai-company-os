"""R2-Upload nur lesend gegen das lokale Release-Manifest prüfen."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import sys
from urllib.error import HTTPError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen


def verify(manifest_file: Path) -> dict:
    manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
    account = os.environ["CLOUDFLARE_ACCOUNT_ID"]
    token = os.environ["CLOUDFLARE_API_TOKEN"]
    endpoint = f"https://api.cloudflare.com/client/v4/accounts/{quote(account, safe='')}/r2/buckets/{quote(manifest['bucket'], safe='')}/objects"
    objects, cursor, seen = {}, None, set()
    while True:
        params = {"prefix": "kurs/", "per_page": 1000}
        if cursor:
            params["cursor"] = cursor
        request = Request(endpoint + "?" + urlencode(params), headers={"Authorization": "Bearer " + token})
        with urlopen(request, timeout=60) as response:
            page = json.load(response)
        if not page.get("success"):
            raise ValueError("Cloudflare hat die lesende Bestandsabfrage abgelehnt.")
        objects.update({entry["key"]: entry for entry in page["result"]})
        info = page.get("result_info", {})
        if not info.get("is_truncated"):
            break
        cursor = info.get("cursor")
        if not cursor or cursor in seen:
            raise ValueError("Unvollständige oder wiederholte R2-Paginierung.")
        seen.add(cursor)
    missing, different = [], []
    for expected in manifest["objects"]:
        actual = objects.get(expected["key"])
        if actual is None:
            missing.append(expected["key"])
        elif actual.get("size") != expected["bytes"] or actual.get("etag", "").strip('"') != expected["md5"]:
            different.append(expected["key"])
    return {"release": manifest["release"], "erwartete_objekte": len(manifest["objects"]),
            "gepruefte_bytes": sum(entry["bytes"] for entry in manifest["objects"]),
            "vorhandene_objekte": len(objects), "fehlend": missing, "abweichend": different,
            "erfolgreich": not missing and not different}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=Path(__file__).parent / "_site/upload-manifest.json")
    parser.add_argument("--output", type=Path, help="Optionaler lokaler Prüfbericht ohne Zugangsdaten")
    args = parser.parse_args()
    try:
        result = verify(args.manifest)
    except (KeyError, ValueError, OSError, HTTPError) as error:
        # Keine Request-Header, Tokens oder API-Antwortkörper ausgeben.
        print("R2-Prüfung fehlgeschlagen: " + type(error).__name__, file=sys.stderr)
        sys.exit(1)
    encoded = json.dumps(result, ensure_ascii=False, indent=2)
    print(encoded)
    if args.output:
        args.output.write_text(encoded + "\n", encoding="utf-8")
    sys.exit(0 if result["erfolgreich"] else 1)
