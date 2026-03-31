# TopRankLand — Agent Instructions

## 網站概述
- **URL**: toprankland.com
- **定位**: 消費決策排行榜 — 實體商品、虛擬商品、人（當人想購買/選擇時參考的排行榜）
- **技術**: Astro (Static) + Tailwind CSS + Chart.js
- **部署**: Cloudflare Pages（從 GitHub 自動部署）
- **專案路徑**: /Users/etrexkuo/toprankland
- **語系**: 雙語（English `/en/` + 繁體中文 `/zh-tw/`），未來擴展到 10+ 語系

---

## 資料架構（i18n 結構）

排行榜資料位於 `src/content/rankings/*.json`，**必須使用以下 i18n 格式**：

```json
{
  "slug": "best-wireless-earbuds",
  "category": "Electronics",
  "scoreFactors": {
    "key1": "English Factor Label",
    "key2": "English Factor Label"
  },
  "i18n": {
    "en": {
      "title": "Best Wireless Earbuds 2026",
      "description": "One-sentence English description"
    },
    "zh-tw": {
      "title": "最佳無線耳機 2026",
      "description": "一句話中文說明"
    }
  },
  "competitors": [
    {
      "id": "unique-kebab-id",
      "name": "Product Name",
      "brand": "Brand",
      "url": "https://verified-url",
      "priceRange": "$249",
      "i18n": {
        "en": { "description": "English one-liner" },
        "zh-tw": { "description": "中文一句話介紹" }
      }
    }
  ],
  "history": [
    {
      "date": "YYYY-MM-DD",
      "rankings": [
        { "id": "unique-id", "rank": 1, "score": 9.2, "scores": { "key1": 9.0, "key2": 8.5 } }
      ],
      "references": [
        { "title": "Article Title", "url": "https://...", "source": "Source Name" }
      ],
      "i18n": {
        "en": {
          "commentary": "200-400 word English analysis",
          "highlights": ["English point 1", "English point 2"]
        },
        "zh-tw": {
          "commentary": "200-400字中文分析",
          "highlights": ["中文重點1", "中文重點2"]
        }
      }
    }
  ]
}
```

**⚠️ 禁止使用的舊欄位**（會造成頁面渲染錯誤）：
- 根層級的 `title`, `description` — 必須放在 `i18n.en` / `i18n.zh-tw`
- `competitors[].description` — 必須放在 `competitors[].i18n.en.description`
- `history[].commentary`, `history[].highlights` — 必須放在 `history[].i18n.en` / `history[].i18n.zh-tw`

**重要規則**:
- `competitors` 最多 100 個
- 每天只新增一個 history 項目（date 為當天 YYYY-MM-DD）
- 如果今天已有該日期的 history，**更新**而非新增
- score 範圍 1.0–10.0，保留一位小數
- rank 從 1 開始，不能重複
- 所有外部 URL 必須驗證（curl 確認非 404）

---

## URL 結構

- 首頁: `/en/` 和 `/zh-tw/`
- 排行榜: `/en/rankings/{slug}` 和 `/zh-tw/rankings/{slug}`
- 舊 URL `/rankings/{slug}` 會自動 301 redirect 到 `/en/rankings/{slug}`

---

## 現有排行榜

讀取 `src/content/rankings/` 目錄取得最新清單。

---

## 建置並部署

```bash
cd /Users/etrexkuo/toprankland
npm run build
CLOUDFLARE_ACCOUNT_ID=8c4a53bddc1c11f46aa4709db491265d npx wrangler pages deploy dist --project-name toprankland --branch master --commit-dirty=true
git add -A
git commit -m "content: [描述]"
git push
```

---

## 內容品質原則

1. **雙語完整**: `i18n.en` 和 `i18n.zh-tw` 都要填寫，不能只寫一種語言
2. **客觀**: 分析要有具體理由，引用事件或數據
3. **一致**: 同類產品評分標準要一致
4. **即時**: 重大新聞要反映在排名中
5. **URL 驗證**: 所有新增的外部連結必須 curl 確認有效
6. **簡潔**: commentary 200–400 字，highlights 3–5 條
