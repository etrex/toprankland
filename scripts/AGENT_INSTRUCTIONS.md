# TopRankLand — Agent Instructions

## 網站概述
- **URL**: toprankland.com
- **定位**: 消費決策排行榜 — 實體商品、虛擬商品、人（當人想購買/選擇時參考的排行榜）
- **技術**: Astro (Static) + Tailwind CSS + Chart.js
- **部署**: Cloudflare Pages（從 GitHub 自動部署）
- **專案路徑**: /Users/etrexkuo/toprankland

---

## 資料架構

排行榜資料位於 `src/content/rankings/*.json`，格式如下：

```json
{
  "slug": "best-wireless-earbuds",
  "title": "Best Wireless Earbuds",
  "category": "Electronics",
  "description": "一句話說明",
  "scoreFactors": {
    "key1": "Factor Label",
    "key2": "Factor Label"
  },
  "competitors": [
    {
      "id": "unique-id",
      "name": "Product Name",
      "brand": "Brand",
      "url": "https://...",
      "priceRange": "$249",
      "description": "一句話介紹"
    }
  ],
  "history": [
    {
      "date": "YYYY-MM-DD",
      "rankings": [
        {
          "id": "unique-id",
          "rank": 1,
          "score": 9.2,
          "scores": { "key1": 9.0, "key2": 8.5 }
        }
      ],
      "commentary": "今日分析（200-400字），客觀說明排名變化原因",
      "highlights": ["重點摘要1", "重點摘要2"],
      "references": [
        { "title": "文章標題", "url": "https://...", "source": "來源名稱" }
      ]
    }
  ]
}
```

**重要規則**:
- `competitors` 最多 100 個
- 每天只新增一個 history 項目（date 為當天 YYYY-MM-DD）
- 如果今天已有該日期的 history，**更新**而非新增
- score 範圍 1.0–10.0，保留一位小數
- rank 從 1 開始，不能重複

---

## 現有排行榜

| 檔案 | 主題 | 類別 |
|------|------|------|
| best-wireless-earbuds.json | Best Wireless Earbuds | Electronics |
| best-gaming-mice.json | Best Gaming Mice | Gaming |
| best-vpn-services.json | Best VPN Services | Software |
| best-smart-watches.json | Best Smart Watches | Wearables |

---

## 每日更新任務（Daily Ranking Update）

**步驟**:

### 1. 研究最新資訊
針對每個排行榜，用 WebSearch 搜尋最新評測、新聞、使用者評價：
- 新型號發布？重大韌體更新？價格變動？重大缺陷？
- 參考來源優先級：rtings.com > wirecutter > techradar > theverge > reddit

### 2. 重新評估排名
- **不要每天大幅變動**（市場穩定，除非有重大事件）
- 新品發布或重大更新才需大幅調整（rank 移動 3+）
- 小幅口碑累積可調整 0.1–0.2 分
- 理由要具體、客觀，引用實際事件

### 3. 新增今日 history 條目
在每個 JSON 的 `history` 陣列末尾新增今天的完整條目。

### 4. 建置並部署
```bash
cd /Users/etrexkuo/toprankland
npm run build
CLOUDFLARE_ACCOUNT_ID=8c4a53bddc1c11f46aa4709db491265d npx wrangler pages deploy dist --project-name toprankland --branch master
git add src/content/rankings/
git commit -m "content: daily update $(date +%Y-%m-%d)"
git push
```

---

## 新增排行榜任務（Add New Ranking）

**執行時機**: 每次執行時評估，每週至少新增一個

**選題原則**:
- 消費者購買前會主動搜尋的類別
- 有明確可比較競品（至少 8 個）
- 市場活躍（會有變化）
- SEO 潛力高

**好的主題**:
- 實體: 無線耳機、遊戲滑鼠、機械鍵盤、掃地機器人、藍牙喇叭、顯示器、電動牙刷、筆電
- 虛擬: VPN、密碼管理器、串流平台、雲端儲存、生產力 SaaS
- 人: 依領域定義，需客觀、有公開可查的指標

---

## 內容品質原則

1. **客觀**: 分析要有具體理由，引用事件或數據
2. **一致**: 同類產品評分標準要一致
3. **即時**: 重大新聞要反映在排名中
4. **公正**: 不偏袒特定品牌，以使用者利益為優先
5. **簡潔**: commentary 200–400 字，highlights 3–5 條
