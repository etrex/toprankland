#!/usr/bin/env python3
"""Add a 2026-05-23 history entry to a single ranking JSON file.

Usage: pass a JSON payload via stdin describing the new entry. Carries forward
yesterday's rankings unless `rankings_override` is provided.
"""
import json
import sys
from pathlib import Path

TODAY = "2026-05-23"
RANKINGS_DIR = Path(__file__).resolve().parent.parent / "src" / "content" / "rankings"


def add_entry(slug: str, payload: dict) -> str:
    path = RANKINGS_DIR / f"{slug}.json"
    with path.open() as f:
        data = json.load(f)

    history = data["history"]
    last = history[-1]

    rankings = payload.get("rankings_override") or last["rankings"]
    references = payload["references"]
    en_commentary = payload["en_commentary"]
    en_highlights = payload["en_highlights"]
    zh_commentary = payload["zh_commentary"]
    zh_highlights = payload["zh_highlights"]

    new_entry = {
        "date": TODAY,
        "rankings": rankings,
        "references": references,
        "i18n": {
            "en": {
                "commentary": en_commentary,
                "highlights": en_highlights,
            },
            "zh-tw": {
                "commentary": zh_commentary,
                "highlights": zh_highlights,
            },
        },
    }

    if history and history[-1]["date"] == TODAY:
        history[-1] = new_entry
        action = "updated"
    else:
        history.append(new_entry)
        action = "added"

    with path.open("w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    return f"{slug}: {action}"


def main():
    payload = json.load(sys.stdin)
    for slug, entry in payload.items():
        print(add_entry(slug, entry))


if __name__ == "__main__":
    main()
