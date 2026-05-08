#!/usr/bin/env python3
"""Helper: append today's history entry to a ranking JSON file.

Usage: pipe a JSON object on stdin matching:
{
  "slug": "best-laptops",
  "date": "2026-05-02",
  "rankings_override": [...]  // optional; if absent, copies latest entry's rankings
  "references_override": [...]  // optional; if absent, copies latest entry's references
  "i18n": {
    "en": {"commentary": "...", "highlights": [{"title": "...", "body": "..."}]},
    "zh-tw": {"commentary": "...", "highlights": [{"title": "...", "body": "..."}]}
  }
}
"""
import json
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src", "content", "rankings")

def main():
    payload = json.load(sys.stdin)
    slug = payload["slug"]
    date = payload["date"]
    path = os.path.join(ROOT, f"{slug}.json")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    history = data.get("history", [])
    history_sorted = sorted(history, key=lambda x: x.get("date", ""))
    if not history_sorted:
        print(f"ERROR: no history in {slug}", file=sys.stderr)
        sys.exit(1)
    last = history_sorted[-1]
    rankings = payload.get("rankings_override", last["rankings"])
    references = payload.get("references_override", last.get("references", []))
    new_entry = {
        "date": date,
        "rankings": rankings,
        "references": references,
        "i18n": payload["i18n"],
    }
    # Replace if today's date already exists, else append
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

if __name__ == "__main__":
    main()
