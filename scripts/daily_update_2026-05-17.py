#!/usr/bin/env python3
"""Apply 2026-05-17 history entries to all 48 ranking JSONs.

Loads content from batch{1..6}_2026-05-17.py and appends/updates today's
history entry on each ranking. Rankings array is copied from the most recent
history entry (no rank changes unless content authors say so).
"""
import importlib.util
import json
from pathlib import Path

DATE = "2026-05-17"
RANKINGS_DIR = Path("/Users/etrexkuo/toprankland/src/content/rankings")
SCRIPTS_DIR = Path("/Users/etrexkuo/toprankland/scripts")


def load_batch(n):
    path = SCRIPTS_DIR / f"batch{n}_2026-05-17.py"
    spec = importlib.util.spec_from_file_location(f"batch{n}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.CONTENT


def merge_all():
    merged = {}
    for n in range(1, 7):
        batch = load_batch(n)
        for slug, content in batch.items():
            if slug in merged:
                raise ValueError(f"Duplicate slug across batches: {slug}")
            merged[slug] = content
    return merged


def build_history_entry(slug, content):
    fpath = RANKINGS_DIR / f"{slug}.json"
    data = json.load(open(fpath))
    last = data["history"][-1]
    # Copy yesterday's rankings unchanged
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
    return entry, data, fpath


def apply_update(slug, content):
    entry, data, fpath = build_history_entry(slug, content)
    found = False
    for i, h in enumerate(data["history"]):
        if h["date"] == DATE:
            data["history"][i] = entry
            found = True
            break
    if not found:
        data["history"].append(entry)
    json.dump(data, open(fpath, "w"), indent=2, ensure_ascii=False)
    print(f"{'UPDATED' if found else 'ADDED'}: {slug}")
    return True


if __name__ == "__main__":
    content_map = merge_all()
    print(f"Loaded {len(content_map)} slugs across 6 batches")

    # Check every ranking JSON gets covered
    all_jsons = {p.stem for p in RANKINGS_DIR.glob("*.json")}
    missing = all_jsons - set(content_map.keys())
    extra = set(content_map.keys()) - all_jsons
    if missing:
        print(f"WARNING: ranking JSONs without content: {sorted(missing)}")
    if extra:
        print(f"WARNING: content for non-existent slugs: {sorted(extra)}")

    updated = 0
    for slug, content in content_map.items():
        if slug in extra:
            continue
        if apply_update(slug, content):
            updated += 1
    print(f"\nDone. {updated} files updated.")
