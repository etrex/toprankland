# Daily Update — Shared Subagent Instructions

You are adding ONE new history entry dated **2026-06-11** to each ranking JSON file assigned to you.

## Procedure per file (path: src/content/rankings/<slug>.json)

1. Load the file with Python. Read `slug`, `scoreFactors`, the competitor `id`s, and the **last** history entry (`history[-1]`).
2. Run ONE `WebSearch` for recent (past ~7 days) news about this product category (e.g. "best <category> June 2026 review ranking"). Skim for any major launches, price drops, or recalls.
3. Build a new history entry for date `2026-06-11`:
   - `rankings`: COPY the previous entry's rankings array (same ids, ranks, scores). Only change ranks/scores if your search surfaced a genuine major market event. Be conservative — stability is the norm. Keep ranks unique starting at 1, scores 1.0–10.0 one decimal.
   - `references`: 2–4 items `{title, url, source}`. Prefer reusing/refreshing the previous entry's references or citing reputable sources you actually found (TechRadar, Tom's Guide, Wirecutter, Rtings, The Verge, etc.). Do NOT invent fake URLs — if unsure, reuse the previous entry's references.
   - `i18n.en` and `i18n.zh-tw`, each with `commentary` (200–400 words / 字) and `highlights` (3–5 objects of `{title, body}`).
4. Insert it using the helper (see below) — DO NOT rewrite the whole file by hand.

## Writing style — English (en)

Confident, opinionated expert reviewer with clear convictions backed by real data. First person. Lead with the verdict and the reason. State what a product IS and does — positive framing. Do not describe how bad other options are (except inside comparison tables, which we don't use here). Ground every judgment in something specific: a measurement, a market event, a real usage observation. **No em dashes** — use a comma or period.

## Writing style — Chinese (zh-tw)

語氣是台灣 3C 論壇資深網友的評測心得，第一人稱，觀點鮮明，像在跟讀者說話。句子完整，資訊說清楚，但每個字都有意義。段落簡短，適當換行。每個判斷都要有具體理由。**禁止「不是…而是」這類否定對比句型** — 直接說產品是什麼、好在哪。**禁止破折號（——、—）** — 用逗號或句號。適當加入表達說話者態度的口語轉折詞（像是「老實說」「講白了」「說真的」）。價格用台灣讀者直覺的金額感受。引用情境優先選台灣讀者熟悉的日常場景。

## New entry shape

```json
{
  "date": "2026-06-11",
  "rankings": [ { "id": "...", "rank": 1, "score": 9.4, "scores": { "<factorKey>": 9.0 } } ],
  "references": [ { "title": "...", "url": "https://...", "source": "..." } ],
  "i18n": {
    "en":    { "commentary": "...", "highlights": [ { "title": "...", "body": "..." } ] },
    "zh-tw": { "commentary": "...", "highlights": [ { "title": "...", "body": "..." } ] }
  }
}
```

The `scores` object keys MUST match the file's `scoreFactors` keys exactly (copy from previous entry).

## Safe insertion helper

Write your new entry to a temp JSON file, then merge with the helper. Example:

```bash
cat > /tmp/entry_<slug>.json <<'EOF'
{ ...your full entry object... }
EOF
python3 scripts/insert_history.py src/content/rankings/<slug>.json /tmp/entry_<slug>.json
```

The helper loads the target, removes any existing 2026-06-11 entry (so re-runs update rather than duplicate), appends the new one, and writes back with `ensure_ascii=False, indent=2`. It validates ranks are unique and score keys match `scoreFactors`. If it prints an error, fix your entry and retry.

## Important
- Do NOT run build/deploy/git — the orchestrator does that once at the end.
- Each commentary must be genuinely written, bilingual, opinionated. Vary wording per product; do not template.
- Verify the helper printed `OK <slug>` for every file before finishing.
