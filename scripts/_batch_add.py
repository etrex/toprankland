#!/usr/bin/env python3
"""Batch helper: read a JSON array of payloads from stdin and apply each.

Each payload follows the same shape as _add_today.py.
"""
import json
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src", "content", "rankings")

def apply_one(payload):
    slug = payload["slug"]
    date = payload["date"]
    path = os.path.join(ROOT, f"{slug}.json")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    history = data.get("history", [])
    history_sorted = sorted(history, key=lambda x: x.get("date", ""))
    if not history_sorted:
        print(f"ERROR: no history in {slug}", file=sys.stderr)
        return
    last = history_sorted[-1]
    rankings = payload.get("rankings_override", last["rankings"])
    references = payload.get("references_override", last.get("references", []))
    new_entry = {
        "date": date,
        "rankings": rankings,
        "references": references,
        "i18n": payload["i18n"],
    }
    replaced = False
    for i, h in enumerate(history):
        if h.get("date") == date:
            history[i] = new_entry
            replaced = True
            break
    if not replaced:
        history.append(new_entry)
    data["history"] = history
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"OK: {slug} ({'replaced' if replaced else 'appended'} {date})")

def main():
    payloads = json.load(sys.stdin)
    for p in payloads:
        apply_one(p)

if __name__ == "__main__":
    main()
