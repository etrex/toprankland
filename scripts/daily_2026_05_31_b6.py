"""2026-05-31 daily update — Batch 6: Wearables/Mobile (8 files)"""
import json
from pathlib import Path

DATE = "2026-05-31"
ROOT = Path("/Users/etrexkuo/toprankland/src/content/rankings")

def load(name):
    p = ROOT / name
    return json.loads(p.read_text(encoding="utf-8")), p

def save(p, data):
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

def upsert(data, entry):
    for i, h in enumerate(data["history"]):
        if h["date"] == entry["date"]:
            data["history"][i] = entry
            return
    data["history"].append(entry)

def last_rankings(d):
    return d["history"][-1]["rankings"]


def build_smart_watches():
    d, p = load("best-smart-watches.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {
                "title": "The best smartwatch 2026: Wearables and fitness watches to buy",
                "url": "https://www.techradar.com/news/wearables/best-smart-watches-what-s-the-best-wearable-tech-for-you-1154074",
                "source": "TechRadar",
            },
            {
                "title": "The best smartwatches in 2026: Options for every budget",
                "url": "https://www.wareable.com/smartwatches/best-smartwatch-reviews-compared-8286",
                "source": "Wareable",
            },
            {
                "title": "Smartwatch Buying Guide 2026: Best Apple, Samsung, Garmin",
                "url": "https://gadgetschamp.com/smartwatches/smartwatch-buying-guide/",
                "source": "GadgetsChamp",
            },
        ],
        "i18n": {
            "en": {
                "commentary": "With Father's Day approaching on June 21 and WWDC 2026 just around the corner, the smartwatch market is moving fast — and right now, the Apple Watch Ultra 3 is the clearest recommendation I can make for anyone who wants the absolute best. At 9.4 out of 10, it earns that score with blood glucose trend monitoring, a titanium build rated to 100m, and Siri integrations that will only deepen after WWDC. For Android users or those who want premium multi-sport GPS without the Apple ecosystem lock-in, the Garmin Fenix 8 remains unmatched — Body Battery, Training Readiness, dual-frequency GNSS, and up to 18 days of battery. Samsung's Galaxy Watch 8 Ultra holds its own on the Android side with 100ATM water resistance and comprehensive health sensors, and I'd pick it over the standard Galaxy Watch 8 every time if budget allows. The Apple Watch Series 11 hits the sweet spot for most iPhone users: non-invasive blood glucose trend monitoring and a refined slim chassis at a price that won't break the bank. Garmin's Venu X1 rounds out my top picks as the best smartwatch for sport-first buyers who still want a stylish daily driver. Bottom line: buy before Father's Day when deals are live, and don't wait for WWDC — no new Apple Watch hardware is expected until fall.",
                "highlights": [
                    {
                        "title": "Apple Watch Ultra 3 still leads the pack",
                        "body": "With blood glucose trend monitoring and titanium durability, the Ultra 3 scores 9.4 and remains our top overall pick heading into summer 2026.",
                    },
                    {
                        "title": "Garmin Fenix 8 for serious athletes",
                        "body": "Dual-frequency GNSS, up to 18-day battery, and Garmin's deep Training Readiness ecosystem make the Fenix 8 the gold standard for endurance athletes.",
                    },
                    {
                        "title": "Father's Day buying window is now open",
                        "body": "Post-Memorial Day deals are live across Apple, Samsung, and Garmin. Father's Day falls June 21 — order by mid-June for safe delivery.",
                    },
                ],
            },
            "zh-tw": {
                "commentary": "父親節快到了（6月21日），加上 WWDC 2026 六月登場，現在買智慧型手錶的時機其實很好。我直接說結論：Apple Watch Ultra 3 是目前市場上最值得買的旗艦，評分 9.4，血糖趨勢監測、鈦金屬錶殼、100米防水，對熱愛戶外活動的爸爸來說幾乎沒有對手。Android 陣營的話，Garmin Fenix 8 依然是我最推薦的，訓練準備度評分、雙頻 GPS、18 天長效電池，認真跑步或登山的人用了就不會想換回去。Samsung Galaxy Watch 8 Ultra 在三星陣營表現穩健，100ATM 防水加上完整健康感測器，比標準版 GW8 更值得加價升級。Apple Watch Series 11 則是 iPhone 用戶的最佳平衡點，血糖趨勢監測加上更輕薄的設計，NT$14,900 左右的定價相當合理。另外，Garmin Venu X1 是兼顧運動與日常美感的好選擇，不想要 Fenix 那麼「硬派」外觀的人可以認真考慮。WWDC 不會有新 Apple Watch 硬體，秋天才會發布，所以現在是入手時機，別等了。",
                "highlights": [
                    {
                        "title": "Apple Watch Ultra 3 旗艦地位穩固",
                        "body": "血糖趨勢監測加上鈦金屬錶殼，Ultra 3 評分 9.4，是父親節送禮首選，WWDC 前入手不用等到秋天。",
                    },
                    {
                        "title": "Garmin Fenix 8 專業運動首選",
                        "body": "雙頻 GPS、18 天電池、訓練準備度評分，認真跑步或登山的用戶選它就對了，三星和蘋果都追不上這種電池續航。",
                    },
                    {
                        "title": "父親節促銷檔期現在開跑",
                        "body": "美國連假後各品牌折扣開始，父親節 6 月 21 日，建議 6 月中前下單確保準時到貨。",
                    },
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK smart-watches")


def build_smart_rings():
    d, p = load("best-smart-rings.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {
                "title": "Samsung Galaxy Ring 2 shelved? Oura patent dispute casts doubt on future",
                "url": "https://www.techradar.com/health-fitness/samsung-galaxy-ring-2-shelved-an-oura-patent-dispute-and-reported-underwhelming-sales-casts-doubt-on-the-smart-rings-future",
                "source": "TechRadar",
            },
            {
                "title": "Galaxy Ring 2 remains in limbo as Samsung fights Oura again",
                "url": "https://www.sammobile.com/news/galaxy-ring-2-remains-in-limbo-as-samsung-fights-oura-again/",
                "source": "SamMobile",
            },
            {
                "title": "Best smart rings 2026: Oura and top alternatives tested",
                "url": "https://www.wareable.com/fashion/best-smart-rings-1340",
                "source": "Wareable",
            },
        ],
        "i18n": {
            "en": {
                "commentary": "The smart ring market just got more interesting — and more complicated. Samsung Galaxy Ring 2 is effectively shelved until early 2027 due to an ongoing ITC patent dispute with Oura, and reportedly underwhelming sales of the original Galaxy Ring. That's big news because it removes the most anticipated hardware competition from the near-term horizon, which indirectly strengthens Oura's position as the category's innovation leader. Right now I'd call it a genuine tie at the top between the Samsung Galaxy Ring (gen 1, score 8.9) and Oura Ring 4 (score 8.9) — the Galaxy Ring wins on no-subscription hardware integration with One UI, while the Oura Ring 4 wins on health analytics depth and its new blood pressure trend monitoring. With Father's Day approaching, both are excellent gifts in the NT$15,000–20,000 range. If budget is a concern, the RingConn Gen 2 at 8.7 delivers serious health tracking without a monthly subscription and is my top value pick. Ultrahuman Ring Pro rounds out the upper tier with strong metabolic insights for fitness-focused users. The Circular Ring 2 and Amazfit Helio Ring remain competent but not compelling enough to unseat the top three. With Samsung's next ring pushed to 2027, expect Oura to push meaningful software updates over the next six months.",
                "highlights": [
                    {
                        "title": "Galaxy Ring 2 delayed to 2027",
                        "body": "An ITC patent dispute with Oura and reported slow sales mean Samsung's next smart ring won't arrive until early 2027, leaving the current Galaxy Ring gen 1 to carry the flag.",
                    },
                    {
                        "title": "Oura Ring 4 strengthens its lead",
                        "body": "With Samsung hardware paused, Oura Ring 4's blood pressure trend monitoring and deep health analytics make it the category's most capable ring right now.",
                    },
                    {
                        "title": "RingConn Gen 2 is the no-subscription value winner",
                        "body": "At a lower price and with no monthly fees, RingConn Gen 2 scores 8.7 and is our top pick for buyers who refuse to pay subscription costs.",
                    },
                ],
            },
            "zh-tw": {
                "commentary": "智慧戒指市場最近最大的新聞是：Samsung Galaxy Ring 2 基本上確定要延到 2027 年初才會推出，原因是和 Oura 之間的 ITC 專利糾紛還沒解決，加上初代 Galaxy Ring 銷售表現不如預期。這個消息對市場格局影響滿大的，因為少了三星的競品壓力，Oura 短期內更能鞏固自己的技術領先地位。目前排名第一的三星 Galaxy Ring 和 Oura Ring 4 都拿到 8.9 分，算是真正的並列。我個人覺得如果你用 Samsung 手機，Galaxy Ring 的無訂閱費整合非常方便；但如果更在意健康數據的深度，Oura Ring 4 的血壓趨勢監測和睡眠分析還是業界最強。父親節禮物的話，這兩款都是 NT$15,000 上下的好選擇。預算有限的話，RingConn Gen 2 評分 8.7 而且完全不用訂閱費，超推。Ultrahuman Ring Pro 代謝洞察不錯，適合認真健身的族群。Oura 接下來幾個月應該會持續推軟體更新，三星則要等到 2027 年了。",
                "highlights": [
                    {
                        "title": "Galaxy Ring 2 確定延至 2027",
                        "body": "與 Oura 的 ITC 專利訴訟加上銷售不理想，三星下一代智慧戒指要等 2027 年初，現在買初代 Galaxy Ring 依然是三星生態的最佳選擇。",
                    },
                    {
                        "title": "Oura Ring 4 趁機鞏固領先優勢",
                        "body": "三星新品暫停，Oura Ring 4 憑血壓趨勢監測和深度睡眠分析繼續領跑，是目前健康追蹤最完整的智慧戒指。",
                    },
                    {
                        "title": "RingConn Gen 2 是無訂閱費首選",
                        "body": "評分 8.7、不收月費，對不想綁訂閱的用戶來說 RingConn Gen 2 是性價比最高的選擇，不用猶豫。",
                    },
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK smart-rings")


def build_smart_glasses():
    d, p = load("best-smart-glasses.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {
                "title": "Meta launches two new Ray-Ban glasses designed for prescription wearers",
                "url": "https://techcrunch.com/2026/03/31/meta-launches-two-new-ray-ban-glasses-designed-for-prescription-wearers/",
                "source": "TechCrunch",
            },
            {
                "title": "7 Smart Glasses Stories That Defined 2026 So Far",
                "url": "https://the-gadgeteer.com/2026/05/08/smart-glasses-2026-stories-so-far/",
                "source": "The Gadgeteer",
            },
            {
                "title": "Meta Ray-Ban Display updates and international availability delay",
                "url": "https://www.androidcentral.com/apps-software/meta/meta-ray-ban-display-updates-ces-2026",
                "source": "Android Central",
            },
        ],
        "i18n": {
            "en": {
                "commentary": "Smart glasses had a genuinely big spring. Meta expanded Ray-Ban prescription support in late March — Blayzer and Scriber frames starting at $499, available from April 14 at optical retailers — and in May rolled out pedestrian navigation to every U.S. city, delivering turn-by-turn directions right in the lens. EssilorLuxottica tripled Ray-Ban Meta sales to over 7 million pairs in 2025, and that momentum is carrying into 2026. The Ray-Ban Meta Gen 2 remains my top pick at 9.3: it does more useful things in a lighter package than any XR headset costs ten times as much. The Oakley Meta HSTN at 9.0 is the sport-first alternative with the same Meta AI engine in a performance frame. If you want a display, the Ray-Ban Meta Display at 8.7 now supports teleprompter mode and EMG handwriting — it's still U.S.-focused and international rollout is delayed, but the software stack is maturing fast. For XR viewing, XREAL One Pro scores 8.6 and offers the sharpest micro-OLED experience in its class. The Even Realities G2 at 8.5 rounds out the upper tier with its clean prescription-friendly design. Google AI Glasses are generating buzz as the next comparison target but aren't shipping yet — this remains Meta's category to lose.",
                "highlights": [
                    {
                        "title": "Ray-Ban Meta now supports nearly all prescriptions",
                        "body": "Starting April 14, the Blayzer and Scriber frames ($499+) bring prescription support to virtually all wearers, massively expanding the addressable market for AI-enabled smart glasses.",
                    },
                    {
                        "title": "Pedestrian navigation expands to all U.S. cities in May",
                        "body": "Turn-by-turn directions in the lens are now available across every U.S. city, making Ray-Ban Meta the most practically useful smart glasses for everyday navigation.",
                    },
                    {
                        "title": "7 million pairs sold proves mass-market viability",
                        "body": "EssilorLuxottica's tripled 2025 sales figure confirms smart glasses are crossing from niche to mainstream — the form factor has arrived.",
                    },
                ],
            },
            "zh-tw": {
                "commentary": "今年春天對智慧眼鏡來說真的是大爆發。Meta 在三月底推出 Ray-Ban 處方鏡片版本，Blayzer 和 Scriber 兩款鏡框從 499 美元起，4 月 14 日開始在光學店販售，幾乎支援所有度數，這對習慣戴眼鏡的使用者來說是很重要的進展。五月又把行人導航推廣到美國全部城市，鏡片裡就能看到轉彎提示，真的很實用。EssilorLuxottica 在 2025 年賣出超過 700 萬副 Ray-Ban Meta，業績三倍成長，動能延續到 2026 年。Ray-Ban Meta Gen 2 評分 9.3，我的首選不變，日常佩戴輕鬆、Meta AI 功能完整，比大多數 XR 頭顯便宜太多了。Oakley Meta HSTN 評分 9.0 是戶外運動版的最佳替代，同樣的 AI 引擎搭上更運動的外型。有螢幕顯示需求的話，Ray-Ban Meta Display 支援提詞機模式和 EMG 手寫，軟體進步速度很快，雖然現在還是主打美國市場。XREAL One Pro 評分 8.6，是這個價位最清晰的 Micro-OLED XR 體驗。Even Realities G2 評分 8.5，設計簡潔且支援處方鏡片，值得一提。Google AI Glasses 雖然引發討論，但尚未出貨，目前還是 Meta 的天下。",
                "highlights": [
                    {
                        "title": "Ray-Ban Meta 處方版 4 月上市",
                        "body": "Blayzer 和 Scriber 鏡框支援幾乎所有度數，從 NT$16,000 起，戴眼鏡的用戶終於有正式選擇了。",
                    },
                    {
                        "title": "行人導航五月擴展至美國所有城市",
                        "body": "鏡片內轉彎提示現在覆蓋全美，Ray-Ban Meta 的實用性大幅提升，日常通勤或觀光都能派上用場。",
                    },
                    {
                        "title": "700 萬副銷量驗證大眾市場潛力",
                        "body": "EssilorLuxottica 2025 年銷售量三倍成長，智慧眼鏡已從小眾走向主流，這個品類的時機到了。",
                    },
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK smart-glasses")


def build_foldable_smartphones():
    d, p = load("best-foldable-smartphones.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {
                "title": "Samsung brings May 2026 update to Galaxy Z Fold 7 and Flip 7 globally",
                "url": "https://www.sammyfans.com/2026/05/25/samsung-brings-may-2026-update-to-galaxy-z-fold-7-and-flip-7-globally/",
                "source": "Sammy Fans",
            },
            {
                "title": "Galaxy Z Fold 7 and Z Flip 7 quietly get a new update — two critical fixes included",
                "url": "https://www.androidheadlines.com/2026/05/galaxy-z-fold-7-and-z-flip-7-quietly-get-a-new-update-two-critical-fixes-included.html",
                "source": "Android Headlines",
            },
            {
                "title": "Galaxy Z Fold 7, Z Flip 7 May 2026 security update goes global",
                "url": "https://www.sammobile.com/news/galaxy-z-fold-7-z-flip-7-may-2026-security-update-reaches-more-regions",
                "source": "SamMobile",
            },
        ],
        "i18n": {
            "en": {
                "commentary": "The Galaxy Z Fold 7 continues to lead this category with a 9.4 score and for good reason: it's the most refined book-style foldable ever made, and Samsung's May 2026 One UI 8.5 security patch — fixing 36 vulnerabilities and two critical bugs — shows exactly the kind of post-launch software discipline that makes a premium purchase feel justified. The Pixel 10 Pro Fold at 9.3 is the best alternative for those who want cleaner Android and seven years of guaranteed updates, a commitment no other Android OEM matches. For anyone in the Chinese market or buying gray-market, the OPPO Find N5 at 9.0 is genuinely the thinnest book-style foldable available and earns its score. The Motorola Razr Fold at 9.2 deserves a closer look — it's a new premium entry that competes directly with the Galaxy Z Fold 7 at a potentially lower price. On the flip side, the Galaxy Z Flip 7 at 8.6 remains the best compact foldable for everyday carry, and the Galaxy Z Flip 7 FE at 7.9 makes the clamshell form factor accessible for budget-conscious buyers. Both devices have been rolling out their May 2026 security patch globally through late May, and One UI 9.0 eligibility is confirmed for later this year — meaning the software story is far from over.",
                "highlights": [
                    {
                        "title": "Galaxy Z Fold 7 and Flip 7 receive May 2026 security update",
                        "body": "The One UI 8.5-based patch fixes 36 security issues plus two critical bugs and is rolling out globally — buyers can expect a more secure and stable experience right now.",
                    },
                    {
                        "title": "One UI 9.0 confirmed for Fold 7 and Flip 7",
                        "body": "Both devices are eligible for One UI 9.0 later in 2026, extending the software value proposition for new buyers today.",
                    },
                    {
                        "title": "Motorola Razr Fold enters premium tier at 9.2",
                        "body": "The Motorola Razr Fold is the highest-rated new entrant this cycle, offering a compelling alternative to the Galaxy Z Fold 7 for buyers open to the Motorola ecosystem.",
                    },
                ],
            },
            "zh-tw": {
                "commentary": "Galaxy Z Fold 7 評分 9.4 穩守第一，這不是白給的。三星這週把 5 月 2026 安全更新推給全球用戶，One UI 8.5 修復了 36 個安全漏洞加兩個嚴重 bug，這種買完還在認真維護的態度是旗艦機應有的樣子。Pixel 10 Pro Fold 評分 9.3 是最適合想要純淨 Android 體驗的選擇，七年更新承諾在 Android 陣營無人能敵，值得認真考慮。OPPO Find N5 評分 9.0，是目前最薄的書本式摺疊機，台灣用戶要透過平行輸入管道才能買到，但確實是設計上的領先者。Motorola Razr Fold 評分 9.2 是這個週期的新亮點，直接和 Galaxy Z Fold 7 競爭，定價可能更友善，喜歡 Motorola 生態的人可以多比較。翻蓋式的話，Galaxy Z Flip 7 評分 8.6 仍是日常攜帶最平衡的選擇，Galaxy Z Flip 7 FE 評分 7.9 則讓翻蓋摺疊機的門檻降低，有預算限制的人可以考慮。One UI 9.0 已確認這兩款都有資格升級，軟體生命週期還很長。",
                "highlights": [
                    {
                        "title": "Galaxy Z Fold 7 和 Flip 7 完成五月安全更新",
                        "body": "One UI 8.5 修復 36 個安全問題和兩個嚴重漏洞，目前全球滾動更新中，現有用戶可以立即升級享受更穩定的體驗。",
                    },
                    {
                        "title": "One UI 9.0 更新資格已確認",
                        "body": "Fold 7 和 Flip 7 都在 One UI 9.0 升級名單內，2026 年稍晚就會推出，現在買依然划算。",
                    },
                    {
                        "title": "Motorola Razr Fold 以 9.2 分殺入旗艦區",
                        "body": "這個週期最值得關注的新進者，和 Galaxy Z Fold 7 直接競爭，對 Motorola 生態有好感的用戶可以認真評估。",
                    },
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK foldable-smartphones")


def build_portable_chargers():
    d, p = load("best-portable-chargers.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {
                "title": "Best Power Bank 2026: 5 New Chargers That Raised the Bar",
                "url": "https://the-gadgeteer.com/2026/05/06/best-power-bank-2026-five-new-chargers/",
                "source": "The Gadgeteer",
            },
            {
                "title": "The best power banks and portable chargers for every device in 2026",
                "url": "https://www.engadget.com/computing/accessories/best-power-bank-143048526.html",
                "source": "Engadget",
            },
            {
                "title": "The Best Power Banks of 2026 — GearJunkie Tested",
                "url": "https://gearjunkie.com/technology/best-power-bank",
                "source": "GearJunkie",
            },
        ],
        "i18n": {
            "en": {
                "commentary": "Summer travel season is here and the Anker Prime 26K 300W is the power bank I'd take on any trip without hesitation — 9.6 out of 10, 300W total output across two USB-C and one USB-A port, and enough capacity to charge a 16-inch MacBook Pro at full speed while simultaneously topping off a phone and tablet. The 250W dual-port input recharges it to 50% in just 13 minutes. That's desktop-replacement power in a carry-on bag. For most travelers who don't need the full 300W ceiling, the Anker Prime 27650 250W at 9.4 is a slightly smaller but still exceptional unit that covers laptops, phones, and earbuds without breaking a sweat. The Anker 737 PowerCore 24K and UGREEN Nexode 25000mAh 200W both score 9.1 and deserve serious consideration for anyone comparison shopping in the $80–120 range. For ultra-compact needs, the Anker Nano Power Bank 10K at 8.7 is the Men's Journal 2026 Travel Award winner — built-in USB-C cable, 30W output, pocketable size. GearJunkie's May 2026 guide refresh added the Anker Laptop Power Bank 25,000mAh as a new pick, confirming Anker continues to dominate the category across all capacity tiers.",
                "highlights": [
                    {
                        "title": "Anker Prime 26K 300W is the summer travel champion",
                        "body": "300W total output and 50% recharge in 13 minutes makes this the definitive laptop-capable power bank for travel season — no other portable charger matches its combination of speed and capacity.",
                    },
                    {
                        "title": "Anker Nano 10K wins 2026 Travel Award",
                        "body": "Men's Journal named the Anker Nano Power Bank 30W with built-in USB-C cable as the best travel power bank of 2026 — it's the pick for minimalist packers.",
                    },
                    {
                        "title": "GearJunkie refreshes picks for summer 2026",
                        "body": "The May 2026 guide update added the Anker Laptop Power Bank 25,000mAh and compact iWALK 4,500mAh, reflecting the expanding range of use cases power bank buyers now have.",
                    },
                ],
            },
            "zh-tw": {
                "commentary": "夏天旅遊旺季來了，行動電源的選擇這時候特別重要。我的首選是 Anker Prime 26K 300W，評分 9.6，300W 總輸出、兩個 USB-C 加一個 USB-A，帶一個電源供應器的概念就能搞定 MacBook Pro、手機和平板同時充電。更厲害的是 250W 雙口輸入，讓自身充電到 50% 只要 13 分鐘，這個速度在同級產品裡找不到對手。如果不需要到 300W，Anker Prime 27650 250W 評分 9.4，稍微小一點但依然處理筆電、手機沒問題，是出差族的好幫手。Anker 737 PowerCore 24K 和 UGREEN Nexode 25000mAh 200W 都拿到 9.1 分，NT$2,500 至 3,500 區間是值得比較的兩款。需要超輕便的話，Anker Nano Power Bank 10K 評分 8.7，附內建 USB-C 線，30W 輸出，可以塞進褲子口袋，是《Men's Journal》2026 旅遊獎得主。GearJunkie 在 5 月更新指南時又新增 Anker Laptop Power Bank 25,000mAh，確認 Anker 在各個容量區間都是領先者。",
                "highlights": [
                    {
                        "title": "Anker Prime 26K 300W 是夏季旅行首選",
                        "body": "300W 輸出、13 分鐘充到 50%，筆電手機平板同時充不是問題，是目前市場上速度和容量都最全面的行動電源。",
                    },
                    {
                        "title": "Anker Nano 10K 獲 2026 旅遊獎",
                        "body": "Men's Journal 評選為 2026 年最佳旅行行動電源，內建 USB-C 線加上口袋尺寸，輕裝出遊的最佳搭檔。",
                    },
                    {
                        "title": "GearJunkie 五月更新推薦名單",
                        "body": "5 月最新指南新增 Anker Laptop Power Bank 25,000mAh 和超輕便 iWALK 4,500mAh，反映市場需求越來越多元化。",
                    },
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK portable-chargers")


def build_portable_power_stations():
    d, p = load("best-portable-power-stations.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {
                "title": "The Best Power Stations of 2026 — Lab Tested & Ranked",
                "url": "https://www.outdoorgearlab.com/topics/camping-and-hiking/best-power-station",
                "source": "OutdoorGearLab",
            },
            {
                "title": "The Best Portable Power Stations of 2026 — Tested by GearJunkie",
                "url": "https://gearjunkie.com/technology/best-portable-power-stations",
                "source": "GearJunkie",
            },
            {
                "title": "The Best Portable Power Stations and Solar Generators of 2026",
                "url": "https://www.nbcnews.com/select/shopping/best-portable-power-station-rcna242425",
                "source": "NBC News Select",
            },
        ],
        "i18n": {
            "en": {
                "commentary": "Summer camping season and the post-Memorial Day surge in outdoor activity make right now the best time to buy a portable power station — and the EcoFlow Delta 3 Plus at 9.1 is my clear top recommendation. It delivers the best balance of power, portability, and expandability for most campers and home-backup users. The BLUETTI Elite 200 V2 at 9.0 is the best choice for buyers who want maximum raw capacity without spending EcoFlow Delta Pro money. The Anker Solix C2000 Gen 2 at 8.9 rounds out the top three with higher-than-average surge output and Anker's now-updated C1000 Gen 2 — highlighted in GearJunkie's May 21 refresh — is the pick for those who want a future-proof unit in the 1kWh class. The EcoFlow Delta Pro 3 remains the go-to for serious home backup: 4,000W output and 4,096Wh capacity with expansion options up to 48kWh. LFP battery chemistry is now the standard across reputable brands at every price point, meaning longer cycle life and greater safety compared to earlier NMC cells. DJI Power 2000, Jackery Explorer 1500 Ultra, and Anker Solix C1000 Gen 2 all deserve mention in the 1,500–2,000Wh range for camping and van life buyers looking at the summer window.",
                "highlights": [
                    {
                        "title": "EcoFlow Delta 3 Plus leads for summer camping",
                        "body": "At 9.1 and with the best expandability in its class, the Delta 3 Plus is the top choice for post-Memorial Day camping season — buy now before summer price spikes.",
                    },
                    {
                        "title": "Anker Solix C1000 Gen 2 updated as top compact pick",
                        "body": "GearJunkie's May 21 2026 guide refresh added the updated Anker Solix C1000 V2 for its higher-than-average surge output — the best option for users who want future-proof 1kWh-class power.",
                    },
                    {
                        "title": "LFP chemistry is now the baseline standard",
                        "body": "As of 2026, all reputable portable power station brands use LFP batteries for longer cycle life and safer chemistry — buyers no longer need to specifically seek out LFP-labeled models.",
                    },
                ],
            },
            "zh-tw": {
                "commentary": "美國連假後戶外活動旺季正式開始，露營和應急備電需求同步上升，現在是買攜帶式電源站的好時機。我的首選是 EcoFlow Delta 3 Plus，評分 9.1，對大多數露營和家庭備電用戶來說，它的輸出功率、攜帶便利性和可擴充性是市場上最均衡的組合。BLUETTI Elite 200 V2 評分 9.0，預算有限但需要大容量的話是最好的選擇，不用花 EcoFlow Delta Pro 的錢就能有接近的容量。Anker Solix C2000 Gen 2 評分 8.9，突波輸出優異，完成前三名組合。GearJunkie 在 5 月 21 日更新推薦名單時特別加入升級版 Anker Solix C1000 Gen 2，對 1kWh 等級有需求的人可以認真考慮。EcoFlow Delta Pro 3 依然是認真家庭備電的最強選擇，4,000W 輸出加上最高可擴充到 48kWh，應付停電完全不成問題。LFP 磷酸鐵鋰電池現在是各大品牌的標準配備，循環壽命更長、安全性更高，買的時候不用再特別找有標 LFP 的型號了。露營、廂型車生活的朋友，DJI Power 2000 和 Jackery Explorer 1500 Ultra 在 1,500–2,000Wh 這個區間也很值得比較。",
                "highlights": [
                    {
                        "title": "EcoFlow Delta 3 Plus 夏季露營首選",
                        "body": "評分 9.1 加上同級最佳擴充彈性，連假後露營旺季現在買是最好時機，建議在夏季漲價前入手。",
                    },
                    {
                        "title": "Anker Solix C1000 Gen 2 五月更新為緊湊型首選",
                        "body": "GearJunkie 5 月 21 日更新推薦名單時加入升級版，突波輸出優異，是 1kWh 等級最值得考慮的未來保值選擇。",
                    },
                    {
                        "title": "LFP 電池已成市場標準",
                        "body": "2026 年起各主流品牌全面採用磷酸鐵鋰電池，循環壽命和安全性大幅提升，消費者買的時候不用再特別挑選了。",
                    },
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK portable-power-stations")


def build_dash_cams():
    d, p = load("best-dash-cams.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {
                "title": "Best Dash Cams for 2026: Tested & Ranked by Vortex Radar",
                "url": "https://www.vortexradar.com/best-dashcams/",
                "source": "Vortex Radar",
            },
            {
                "title": "Best Dash Cams of 2026 — VIOFO Top Picks and Buyer's Guide",
                "url": "https://www.viofo.com/blogs/viofo-car-dash-camera-guide-faq-and-news/the-best-dash-cams-of-2026-our-top-picks-and-whats-new",
                "source": "VIOFO",
            },
            {
                "title": "The 7 Best Dash Cams of 2026: Tested Head-to-Head",
                "url": "https://drivegearlab.blog/the-7-best-dash-cams-of-2026/",
                "source": "DriveGearLab",
            },
        ],
        "i18n": {
            "en": {
                "commentary": "Summer road trips make this the peak season for dash cam purchases, and the VIOFO A329S at 9.1 is the camera I recommend without reservation. Vortex Radar tested 13 models head-to-head in 2026 and the A329S came out on top — and The New York Times Wirecutter independently reached the same conclusion. Sharp 4K front video, flexible rear and interior camera configurations, and Sony STARVIS 2 sensors across every channel make this the most capable all-around system you can buy. VIOFO also pushed major V2.0 firmware updates to the A329S, A229 series, and A119M Pro via the VIOFO App — no more SD card gymnastics for OTA updates. The Vantrue N4 Pro S at 8.8 is my pick for three-channel recording with the best interior camera, ideal for rideshare drivers. The Blackvue Elite 9 at 8.6 is the go-to for cloud-connected parking alerts and remote viewing — Blackvue's cloud ecosystem remains unmatched for remote monitoring. Thinkware U3000 at 8.4 holds the premium spot for built-in safety and ADAS features. For budget-conscious buyers, the VIOFO A119M Pro at 8.0 is the 2026 single-camera upgrade with true 4K and no compromise on image quality. Summer travel is peak dash cam season — buy now before inventory tightens.",
                "highlights": [
                    {
                        "title": "VIOFO A329S wins head-to-head test against 13 rivals",
                        "body": "Both Vortex Radar and Wirecutter independently named the A329S the best dash cam of 2026 — the most validated consensus pick in the category this year.",
                    },
                    {
                        "title": "VIOFO V2.0 firmware brings OTA updates via app",
                        "body": "Major firmware V2.0 rolled out to the A329S, A229 series, and A119M Pro — over-the-air updates now push through the VIOFO App instead of requiring SD card downloads.",
                    },
                    {
                        "title": "Blackvue Elite 9 leads for cloud parking monitoring",
                        "body": "For drivers who want remote viewing and parking alerts via cloud, the Blackvue Elite 9 offers the most mature cloud ecosystem in the dash cam market.",
                    },
                ],
            },
            "zh-tw": {
                "commentary": "夏季公路旅行旺季是買行車記錄器的最好時機，而我的首選還是 VIOFO A329S，評分 9.1。Vortex Radar 今年測試了 13 款同類產品，A329S 排名第一；《紐約時報》旗下的 Wirecutter 也獨立得出同樣結論。4K 前鏡頭畫質清晰，後鏡、車內鏡配置靈活，每個通道都用 Sony STARVIS 2 感光元件，是目前最全面的行車記錄系統。VIOFO 最近還幫 A329S、A229 系列和 A119M Pro 推了 V2.0 韌體大更新，現在可以直接透過 APP 空中更新，不用再拔記憶卡了，這個改進很實用。Vantrue N4 Pro S 評分 8.8，三鏡頭加最好的車內鏡，是 Uber/Lyft 司機的最佳選擇。Blackvue Elite 9 評分 8.6，雲端停車監控和遠端查看是它最強的地方，Blackvue 的雲端生態系在這個品類裡最成熟，愛車黨推薦。Thinkware U3000 評分 8.4，內建安全輔助駕駛 ADAS 功能，是高端買家的穩健選擇。預算有限的話，VIOFO A119M Pro 評分 8.0，真 4K 單鏡頭升級版，畫質沒有妥協。夏天旺季庫存容易吃緊，建議及早下單。",
                "highlights": [
                    {
                        "title": "VIOFO A329S 在 13 款實測中奪冠",
                        "body": "Vortex Radar 和 Wirecutter 各自獨立測試後都選出 A329S 為 2026 最佳行車記錄器，是今年最具公信力的雙重認證。",
                    },
                    {
                        "title": "VIOFO V2.0 韌體支援 APP 空中更新",
                        "body": "A329S、A229 系列和 A119M Pro 全面升級 V2.0，透過 VIOFO APP 就能直接推送更新，不用再拔記憶卡操作了。",
                    },
                    {
                        "title": "Blackvue Elite 9 雲端停車監控最強",
                        "body": "雲端遠端查看和停車警報通知，Blackvue 的雲端生態系在這個品類最成熟，愛車族需要遠端監控首選它。",
                    },
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK dash-cams")


def build_air_purifiers():
    d, p = load("best-air-purifiers.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {
                "title": "Best Air Purifiers 2026 — 95 Models Objectively Tested",
                "url": "https://moderncastle.com/air-purifiers/best-air-purifier/",
                "source": "Modern Castle",
            },
            {
                "title": "The Best Air Purifiers of 2026: Tried and Reviewed by NBC Select",
                "url": "https://www.nbcnews.com/select/shopping/best-air-purifiers-rcna206778",
                "source": "NBC News Select",
            },
            {
                "title": "The best air purifiers you can buy in 2026",
                "url": "https://housefresh.com/best-air-purifiers-we-tested/",
                "source": "HouseFresh",
            },
        ],
        "i18n": {
            "en": {
                "commentary": "Summer air quality concerns — wildfire smoke, pollen, and increased ozone — make this the most important time of year to have a quality air purifier. The IQAir HealthPro Plus at 9.5 remains the reference standard for a reason: it reduces PM2.5 down to 0.1 microns and PM10 down to 0.2 microns with its HyperHEPA filtration, a performance level no other consumer air purifier reliably matches. It is expensive, but for allergy sufferers or anyone in wildfire smoke territory, no other unit provides the same peace of mind. The Coway Airmega 400S at 9.1 is my top recommendation for the overwhelming majority of buyers — it combines a high CADR, smart app control, and long-lasting filters at a price that makes sense for living rooms and large open-plan spaces. The Blueair HealthProtect 7470i at 8.9 is the best choice for buyers who want Swedish HEPA Glass filtration with a sleek design that doesn't look like lab equipment. For mid-size rooms, the Rabbit Air MinusA3 at 8.6 and Coway Airmega ProX at 8.6 are both excellent — the MinusA3 for quiet operation and customizable panels, the ProX for maximum CADR in its size class. Tests confirm the Airmega ProX outperformed the $1,400 IQAir Atem X, which is a meaningful data point. Levoit Core 600S at 8.4 and Vital 200S at 8.3 are the value picks for budget-focused buyers who still want smart features.",
                "highlights": [
                    {
                        "title": "IQAir HealthPro Plus is the gold standard for serious air quality",
                        "body": "At 9.5, the HealthPro Plus filters PM2.5 down to 0.1 microns — the most demanding filtration performance of any consumer air purifier and the only real choice for wildfire smoke or severe allergies.",
                    },
                    {
                        "title": "Coway Airmega 400S is the best buy for most homes",
                        "body": "High CADR, smart connectivity, and durable filters at a fraction of IQAir's price — the 400S is the workhorse recommendation for living rooms and open-plan spaces in 2026.",
                    },
                    {
                        "title": "Summer wildfire season makes air purifiers essential",
                        "body": "Post-Memorial Day marks the start of peak wildfire and high-pollen season across much of North America — a strong HEPA air purifier is no longer optional for sensitive households.",
                    },
                ],
            },
            "zh-tw": {
                "commentary": "夏季是空氣品質最需要注意的時候，野火煙霧、花粉、臭氧濃度都在升高，空氣清淨機的需求在這個時節特別高。我的首選是 IQAir HealthPro Plus，評分 9.5，HyperHEPA 濾網可以過濾 PM2.5 細至 0.1 微米、PM10 細至 0.2 微米，這個規格在消費級市場找不到對手。價格確實偏高，但對過敏族或居住在野火煙霧地區的人來說，沒有其他選擇能帶來同等程度的安心感。大多數家庭的首選我推 Coway Airmega 400S，評分 9.1，CADR 表現優異、APP 智慧控制、濾網壽命長，適合客廳或大空間使用，性價比是同級最好的。Blueair HealthProtect 7470i 評分 8.9，瑞典 HEPA Glass 濾網加上設計感強的外型，不像實驗室設備，放客廳很好看。中型房間的話，Rabbit Air MinusA3 和 Coway Airmega ProX 都拿到 8.6 分，MinusA3 靜音且可換面板很有個性，Airmega ProX 的 CADR 是同尺寸裡最強的，測試中甚至擊敗了售價 NT$45,000 的 IQAir Atem X。Levoit Core 600S 和 Vital 200S 評分分別為 8.4 和 8.3，有 App 連接但預算有限的首選。",
                "highlights": [
                    {
                        "title": "IQAir HealthPro Plus 是最高規格空氣清淨機",
                        "body": "評分 9.5，PM2.5 過濾細至 0.1 微米，是消費級市場最頂級的過濾性能，野火煙霧或嚴重過敏的家庭唯一選擇。",
                    },
                    {
                        "title": "Coway Airmega 400S 是最多家庭的最佳買點",
                        "body": "高 CADR、智慧 App、濾網耐用，價格只有 IQAir 的一小部分，是 2026 年客廳和大空間的標準推薦款。",
                    },
                    {
                        "title": "夏季野火和花粉季讓空氣清淨機成必需品",
                        "body": "美國連假後進入野火和高花粉季節，北美敏感體質家庭這時候裝一台好的 HEPA 空氣清淨機已經不是選配，是必要配備。",
                    },
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK air-purifiers")


if __name__ == "__main__":
    build_smart_watches()
    build_smart_rings()
    build_smart_glasses()
    build_foldable_smartphones()
    build_portable_chargers()
    build_portable_power_stations()
    build_dash_cams()
    build_air_purifiers()
    print("Batch 6 complete")
