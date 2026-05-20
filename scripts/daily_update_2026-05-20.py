#!/usr/bin/env python3
"""Apply 2026-05-20 history entries to all ranking JSONs by importing batch files."""
import json
import sys
from pathlib import Path

DATE = "2026-05-20"
RANKINGS_DIR = Path("/Users/etrexkuo/toprankland/src/content/rankings")
SCRIPTS_DIR = Path("/Users/etrexkuo/toprankland/scripts")

sys.path.insert(0, str(SCRIPTS_DIR))

CONTENT = {}
for i in range(1, 7):
    mod = __import__(f"batch{i}_2026_05_20")
    CONTENT.update(mod.CONTENT)


def apply_update(slug, content):
    fpath = RANKINGS_DIR / f"{slug}.json"
    data = json.load(open(fpath))
    last = data["history"][-1]
    rankings = json.loads(json.dumps(last["rankings"]))
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": content["references"],
        "i18n": {
            "en": {
                "commentary": content["en_commentary"],
                "highlights": content["en_highlights"],
            },
            "zh-tw": {
                "commentary": content["zh_commentary"],
                "highlights": content["zh_highlights"],
            },
        },
    }
    found = False
    for i, h in enumerate(data["history"]):
        if h["date"] == DATE:
            data["history"][i] = entry
            found = True
            break
    if not found:
        data["history"].append(entry)
    json.dump(data, open(fpath, "w"), indent=2, ensure_ascii=False)
    return found


if __name__ == "__main__":
    all_jsons = {p.stem for p in RANKINGS_DIR.glob("*.json")}
    missing = all_jsons - set(CONTENT.keys())
    extra = set(CONTENT.keys()) - all_jsons
    if missing:
        print(f"MISSING: {sorted(missing)}")
    if extra:
        print(f"EXTRA: {sorted(extra)}")
    updated = 0
    for slug, content in CONTENT.items():
        if slug in extra:
            continue
        found = apply_update(slug, content)
        print(f"{'UPDATED' if found else 'ADDED'}: {slug}")
        updated += 1
    print(f"\nTotal: {updated}")
