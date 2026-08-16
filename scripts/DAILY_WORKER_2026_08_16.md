# Daily Ranking Update — Worker Procedure (2026-08-16)

You update a batch of ranking JSON files in `/Users/etrexkuo/toprankland/src/content/rankings/`.
For EACH assigned slug, add ONE new `history` entry dated **2026-08-16** (bilingual). Do not touch other files.

Working dir: `/Users/etrexkuo/toprankland`
Scratchpad: `/private/tmp/claude-501/-Users-etrexkuo-toprankland/64d7a33b-f9f1-4c42-8ebf-c392e4c0fb2d/scratchpad`

The ranking JSON files are HUGE (up to 900KB). NEVER Read them with the Read tool. Always inspect with python one-liners.

## Steps per slug

1. **Inspect**:
```bash
cd /Users/etrexkuo/toprankland && python3 -c "
import json
d=json.load(open('src/content/rankings/SLUG.json'))
print('scoreFactors:', json.dumps(d['scoreFactors'], ensure_ascii=False))
print('last date:', d['history'][-1]['date'])
print('last rankings:', json.dumps(d['history'][-1]['rankings'], ensure_ascii=False))
print('names:', json.dumps({c['id']: c['name'] for c in d['competitors']}, ensure_ascii=False))
"
```

2. **WebSearch** for news from the past 7 days about this product category (e.g. "best wireless earbuds August 2026", "<category> new launch August 2026"). 1–2 searches is enough. Note 2–3 real article references (title, url, source) that came back in the search results. Do NOT invent URLs. If nothing notable turned up, keep rankings identical and omit `references` (the merge script then reuses the previous entry's references).

3. **Rankings**: they are copied forward automatically by the merge script. Only supply an `adjust` map when a genuine market event justifies it: adjust a score by ±0.1–0.2, or swap two ADJACENT ranks (you must then list BOTH ids with their new ranks, and update their `score` so the ordering stays consistent). Most slugs on most days need no `adjust` at all — that is fine and expected. Never duplicate a rank.

4. **Write bilingual content** following the style rules below. Even when rankings are unchanged, the commentary must be fresh for today and reflect what you found in search.

5. **Save**: write ONE payload file for your whole batch to a UNIQUE scratchpad filename
`payload_<yourbatchname>.json` (e.g. `payload_batch3.json` — never share a filename with another worker), shaped:

```json
{
  "best-example-slug": {
    "references": [ { "title": "...", "url": "https://...", "source": "..." } ],
    "adjust": { "comp-id-a": { "rank": 2, "score": 9.1 }, "comp-id-b": { "rank": 1, "score": 9.2 } },
    "i18n": {
      "en": { "commentary": "...", "highlights": [ { "title": "...", "body": "..." } ] },
      "zh-tw": { "commentary": "...", "highlights": [ { "title": "...", "body": "..." } ] }
    }
  }
}
```
`references` and `adjust` are both optional. `i18n` is required.

Then run:
```bash
cd /Users/etrexkuo/toprankland && python3 scripts/daily_2026_08_16.py /private/tmp/claude-501/-Users-etrexkuo-toprankland/64d7a33b-f9f1-4c42-8ebf-c392e4c0fb2d/scratchpad/payload_<yourbatchname>.json
```

The script is idempotent (replaces any existing 2026-08-16 entry), reloads each file at write time, and validates rank/highlight structure. If it raises, fix the payload and re-run.

- `commentary`: 200–400 words / 字, opinionated first-person.
- `highlights`: 3–5 objects, each exactly {title, body}.

## EN style
Confident, opinionated expert reviewer with clear convictions backed by data and experience. State what you believe and why; lead with the verdict and the reason. Describe products by what they are and do — positive framing. In prose, focus on what makes a product worth recommending; leave out how bad other options are. First person. Ground every judgment in something specific: a measurement, a market event, a real usage observation. NO em dashes — use commas or periods.

## ZH-TW style
語氣是台灣 3C 論壇資深網友的評測心得，第一人稱，觀點鮮明，像在跟讀者說話。句子完整，資訊說清楚，需要更多字才能說清楚的地方就用更多字，每個字都有意義。段落簡短，適當換行。每個判斷都要有具體理由，語氣口語但觀點鋒利。
禁止「不是⋯⋯而是」及所有否定對比句型（同一句話同時肯定某件事又否定另一件事）：直接說某產品哪裡好，不需要說較差選項有多差。描述屬性時直接說它是什麼、有什麼，用正面描述。
禁止破折號（——、—），改用逗號或句號。適當加入表達說話者態度的口語轉折詞（表達對自己判斷有把握的信心、坦誠承認某個事實、或直接邀請讀者進入對話）。價格用台灣讀者直覺感受表達。引用情境優先選台灣讀者熟悉的日常場景。

## Validation
After running the merge, verify every slug in your batch:
```bash
cd /Users/etrexkuo/toprankland && python3 -c "
import json,sys
for s in 'slug-a slug-b'.split():
    d=json.load(open(f'src/content/rankings/{s}.json'))
    assert d['history'][-1]['date']=='2026-08-16', s
    print('OK', s)
"
```
Report which slugs you updated and any ranking changes you made.
