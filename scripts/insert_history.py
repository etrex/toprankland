#!/usr/bin/env python3
"""Insert/replace a single dated history entry into a ranking JSON file.

Usage: python3 insert_history.py <target.json> <entry.json>
- Removes any existing history entry with the same date, then appends the new one.
- Validates: required keys, unique ranks, score keys subset of scoreFactors, bilingual i18n.
- Writes back with ensure_ascii=False, indent=2.
"""
import json
import sys


def main():
    target_path, entry_path = sys.argv[1], sys.argv[2]
    with open(target_path, encoding="utf-8") as f:
        data = json.load(f)
    with open(entry_path, encoding="utf-8") as f:
        entry = json.load(f)

    slug = data.get("slug", target_path)
    factor_keys = set(data.get("scoreFactors", {}).keys())

    # --- validate entry shape ---
    for k in ("date", "rankings", "references", "i18n"):
        if k not in entry:
            sys.exit(f"ERROR {slug}: entry missing key '{k}'")

    ranks = [r["rank"] for r in entry["rankings"]]
    if len(ranks) != len(set(ranks)):
        sys.exit(f"ERROR {slug}: duplicate ranks {sorted(ranks)}")

    valid_ids = {c["id"] for c in data.get("competitors", [])}
    for r in entry["rankings"]:
        if "id" not in r or "rank" not in r or "score" not in r:
            sys.exit(f"ERROR {slug}: ranking item missing id/rank/score: {r}")
        if valid_ids and r["id"] not in valid_ids:
            sys.exit(f"ERROR {slug}: unknown competitor id '{r['id']}'")
        if not (1.0 <= float(r["score"]) <= 10.0):
            sys.exit(f"ERROR {slug}: score out of range for {r['id']}: {r['score']}")
        bad = set(r.get("scores", {}).keys()) - factor_keys
        if bad:
            sys.exit(f"ERROR {slug}: unknown score keys {bad} for {r['id']}")

    for lang in ("en", "zh-tw"):
        if lang not in entry["i18n"]:
            sys.exit(f"ERROR {slug}: i18n missing '{lang}'")
        node = entry["i18n"][lang]
        if not node.get("commentary"):
            sys.exit(f"ERROR {slug}: {lang} commentary empty")
        hl = node.get("highlights", [])
        if not (3 <= len(hl) <= 5):
            sys.exit(f"ERROR {slug}: {lang} needs 3-5 highlights, got {len(hl)}")
        for h in hl:
            if not h.get("title") or not h.get("body"):
                sys.exit(f"ERROR {slug}: {lang} highlight needs title+body: {h}")
        # ban em dashes
        blob = node["commentary"] + " ".join(h["title"] + h["body"] for h in hl)
        if "—" in blob or "——" in blob:
            sys.exit(f"ERROR {slug}: {lang} contains em dash; use comma/period")

    # --- merge ---
    history = data.setdefault("history", [])
    history[:] = [h for h in history if h.get("date") != entry["date"]]
    history.append(entry)

    with open(target_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"OK {slug}")


if __name__ == "__main__":
    main()
