# TopRankLand Agent Instructions

## 網站說明
- 網站：toprankland.com
- 技術：Astro (Static) + Tailwind CSS
- 部署：Cloudflare Pages（從 GitHub repo 自動部署）
- 專案路徑：/Users/etrexkuo/toprankland

## 內容架構
- 排行榜資料：`src/content/rankings/*.json`
- 每個 JSON 檔案對應一個排行榜頁面（自動生成路由）

## JSON 格式規範
```json
{
  "slug": "kebab-case-url-friendly",
  "title": "完整標題（含年份）",
  "description": "一句話說明這個排行榜",
  "category": "類別名稱（AI Tools / Developer Tools / Productivity / etc.）",
  "tags": ["tag1", "tag2"],
  "updatedAt": "YYYY-MM-DD",
  "items": [
    {
      "rank": 1,
      "name": "產品名稱",
      "tagline": "一句話介紹",
      "url": "https://...",
      "score": 9.5,
      "pros": ["優點1", "優點2", "優點3"],
      "cons": ["缺點1"],
      "pricing": "免費 / $XX/mo / etc."
    }
  ]
}
```

## 部署流程
建立或更新排行榜後，執行：
```bash
cd /Users/etrexkuo/toprankland
npm run build
git add src/content/rankings/
git commit -m "content: add/update [ranking name]"
git push
```
Cloudflare Pages 會自動偵測 push 並部署。

## 排行榜主題方向
優先考慮：
- AI 工具類（高搜尋量）
- 開發者工具類
- 生產力工具類
- SaaS 產品比較
- 熱門 App 排名

SEO 原則：
- 標題要包含年份（如 2026）
- 瞄準長尾關鍵字（"best X for Y"）
- 每個排行榜至少 5 個條目，最多 15 個
