# Daily Update Task — Shared Instructions (2026-06-10)

You are appending ONE new history entry dated **2026-06-10** to each ranking JSON file assigned to you, in BOTH English (`en`) and Traditional Chinese (`zh-tw`). Work autonomously.

## Process per file
1. Read the JSON file at `/Users/etrexkuo/toprankland/src/content/rankings/<slug>.json`.
2. Look at the LAST entry in `history` to get the existing `rankings` array (ids, ranks, scores).
3. Run 1–2 `WebSearch` queries for news in the **past 7 days** about this category (e.g. "best <category> 2026", "<category> new release June 2026"). Use real article URLs from results for `references`.
4. Append a NEW history entry dated `2026-06-10`. If a `2026-06-10` entry already exists, UPDATE it instead of adding a duplicate.
5. Write the file back. **Use Python (via Bash) to load/modify/dump the JSON** — these files are large; do NOT hand-edit JSON with the Edit tool. Preserve `ensure_ascii=False`, `indent=2`.

## Ranking rules
- Be CONSERVATIVE. Carry forward the previous entry's `rankings` (same ids, ranks, scores) unless a genuine major market event justifies a change. Minor score tweaks (±0.1) are fine.
- `rankings` must have same structure: `{ "id", "rank", "score", "scores": {...} }`. Ranks start at 1, no duplicates. Reuse the ids and scoreFactor keys already present.

## New history entry shape (root level holds ONLY date, rankings, references, i18n)
```json
{
  "date": "2026-06-10",
  "rankings": [ { "id": "...", "rank": 1, "score": 9.2, "scores": { "<factorKey>": 9.0 } } ],
  "references": [ { "title": "Article Title", "url": "https://...", "source": "Source Name" } ],
  "i18n": {
    "en": {
      "commentary": "200-400 word opinionated first-person analysis",
      "highlights": [ { "title": "Bold verdict heading", "body": "Paragraph defending it with specifics" } ]
    },
    "zh-tw": {
      "commentary": "200-400字 台灣論壇語氣分析",
      "highlights": [ { "title": "觀點強烈的子標題", "body": "支持判斷的中文段落" } ]
    }
  }
}
```
- `highlights`: 3–5 objects, each `{title, body}`. Both languages required.
- `references`: 2–4 real, verified URLs from your searches.

## English writing style
Confident, opinionated expert reviewer with clear convictions backed by data and experience. State what you believe and why; lead with the verdict. Positive framing — describe what a product IS and DOES, not what others are not. Do not describe how bad inferior options are (exception: structured comparison tables). Write first person, ground every judgment in something specific (a measurement, a market event, a real usage observation). Avoid em dashes; use a comma or period.

## 中文 writing style (zh-tw)
台灣 3C 論壇資深網友的評測心得，第一人稱，觀點鮮明，像在跟讀者說話。句子完整、資訊說清楚，每個字有意義。段落簡短。每個判斷要有具體理由。
禁止「不是⋯⋯而是」否定對比句型：直接說產品是什麼、有什麼，用正面描述。可以說某產品勝出，但散文只說推薦產品的優點，不用強調差的選項多差（比較表格例外）。
禁止破折號（——、—），改用逗號或句號。適當加入表達態度的口語轉折詞，讓文字有說話節奏。價格用台灣讀者直覺感受表達。引用情境優先選台灣讀者熟悉的場景。

## Competitor data
Only touch `competitors` if a clearly newsworthy price/product change warrants it. priceRange lives inside `competitors[].i18n.<lang>.priceRange`. zh-tw rule: official TW price → `NT$X,XXX`; no official TW channel / import only → `約 NT$X,XXX`.

## After editing, validate
Run `python3 -c "import json; json.load(open('<path>'))"` for each file to confirm valid JSON. Report which files you updated and any that failed.
