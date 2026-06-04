"""2026-05-31 daily update — Batch 2: Gaming/Computing (8 files)"""
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

def build_laptops():
    d, p = load("best-laptops.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Amazon Discounts 2026 16-Inch MacBook Pro by $249 Across All Models", "url": "https://www.macrumors.com/2026/05/15/2026-16-inch-macbook-pro-at-249-off/", "source": "MacRumors"},
            {"title": "Best MacBook deals in May 2026", "url": "https://www.tomsguide.com/news/cheap-macbook-deals-and-sales", "source": "Tom's Guide"},
            {"title": "Best laptops 2026: tested and reviewed", "url": "https://www.tomsguide.com/us/best-laptops,review-1236.html", "source": "Tom's Guide"},
        ],
        "i18n": {
            "en": {
                "commentary": "The MacBook Air 13 M5 is the laptop I recommend to almost everyone right now. At $1,099 with up to 18 hours of battery life, it delivers M5 performance that genuinely outpaces anything in this price range from the Windows camp. Post-Memorial Day week is an excellent time to commit: WWDC 2026 in June carries no Apple hardware refresh, so there is zero reason to wait. Amazon just dropped the 16-inch MacBook Pro M5 Pro by $249, making it the rare moment where the flagship feels like an actual deal. For buyers who need sustained multi-threaded workloads, graphic design, or video export, that 16-inch M5 Pro at $2,449 is now the obvious target. The MacBook Neo at $599 is worth mentioning for budget shoppers, though its A18 Pro chip is more iPad-grade than laptop-grade for demanding tasks. Father's Day is three weeks out, and MacBooks are the dominant gift pick in the premium laptop category. On the Windows side, the ASUS Zenbook A16 holds its ground as the best all-rounder: AMD Ryzen power, solid display, and a value score that the Apple machines cannot match at equivalent specs. The Dell XPS 14 impresses with its 9.6 battery score and OLED display but suffers from a price premium that narrows its audience. The Razer Blade 16 remains the performance outlier for gamers who want a single machine, though its 7.0 battery score means you are always hunting for a plug. This week the story is simple: if you have been eyeing a MacBook Pro 16-inch, the current Amazon discount turns hesitation into action.",
                "highlights": [
                    {"title": "MacBook Air M5 Still the Default Recommendation", "body": "At $1,099 and with WWDC bringing no hardware surprise, the MacBook Air M5 is the safest buy in any laptop category right now. Its combination of M5 performance, fanless silence, and 18-hour battery is unmatched at this price."},
                    {"title": "MacBook Pro 16-inch M5 Pro Gets $249 Amazon Discount", "body": "Amazon cut $249 off all 2026 16-inch MacBook Pro models this week, bringing the 24GB/1TB M5 Pro to $2,449. For creative professionals and developers, that price is finally at the level where the upgrade from M4 Pro justifies itself."},
                    {"title": "Father's Day Buying Window Opens", "body": "With Father's Day on June 21, laptops are entering their seasonal gift demand peak. MacBooks lead search and gift guide traffic across every major retailer, and current discounts make this the ideal three-week window to buy."},
                ]
            },
            "zh-tw": {
                "commentary": "MacBook Air 13 M5 是我現在最推薦的筆電，沒有例外。NT$34,900 的起售價配上 M5 晶片，在這個價位根本找不到 Windows 對手能正面競爭。更重要的是，六月的 WWDC 2026 不會帶來新硬體，所以現在買完全不用擔心隔週就被新品打臉。Amazon 這週對 16 吋 MacBook Pro M5 Pro 所有型號下殺 $249 美金，換算下來省下快 NT$8,000，這種折扣實屬難得，有需要大螢幕高效能的用戶可以直接出手。MacBook Neo 的 $599 美金入門價看起來很香，不過 A18 Pro 晶片畢竟是 iPad 血統，重度創作或開發工作建議直上 Air M5。Father's Day 三週後就到了，蘋果筆電在各大禮物指南的聲量明顯拉高，這個時間點正是出手的好機會。Windows 陣營方面，ASUS Zenbook A16 依然是最均衡的選擇，AMD 效能加上扎實的整體規格，同等預算內的性價比比 MacBook 好算。Dell XPS 14 的 OLED 螢幕和 9.6 分電池表現非常搶眼，但溢價讓受眾縮窄。Razer Blade 16 是遊戲創作者的最愛，只是 7.0 的電池分數提醒你隨時要找插座。這週的市場信號很清楚，有在猶豫 MacBook Pro 16 吋的人，現在的折扣就是下手的理由。",
                "highlights": [
                    {"title": "MacBook Air M5 依然是首選推薦", "body": "WWDC 確認不帶來新硬體，MacBook Air M5 是目前最安心的採購決策。M5 效能、無風扇靜音、18 小時續航，這個組合在 NT$34,900 起的價位無可取代。"},
                    {"title": "MacBook Pro 16 吋 M5 Pro 罕見折扣", "body": "Amazon 本週對 16 吋 MacBook Pro 全系列折扣 $249 美金，24GB/1TB M5 Pro 降至 $2,449。對需要持續多核效能的創作者和開發者而言，這個價格讓從 M4 Pro 升級的帳算得過去。"},
                    {"title": "父親節採購旺季正式啟動", "body": "父親節 6 月 21 日倒數三週，筆電是各大禮物指南最熱門品類之一。目前市場折扣搭配旺季送禮需求，是近期最佳進場時機。"},
                ]
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK laptops")

def build_gaming_chairs():
    d, p = load("best-gaming-chairs.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Best Gaming Chair in 2026 — top chairs for gamers for the money", "url": "https://www.tomshardware.com/best-picks/best-gaming-chairs", "source": "Tom's Hardware"},
            {"title": "Best gaming chair in 2026: tested and reviewed", "url": "https://www.pcgamer.com/best-gaming-chairs/", "source": "PC Gamer"},
            {"title": "15 Best Gaming Chairs (May 2026) Top Comfort and Durability", "url": "https://www.thirstybear.com/best-gaming-chairs/", "source": "ThirstyBear"},
        ],
        "i18n": {
            "en": {
                "commentary": "The Secretlab Titan Evo is the gaming chair I keep coming back to as the top pick, and for good reason. It delivers premium ergonomics at a price point well below Herman Miller territory, with a steel frame that feels built to last a decade. The lumbar support pillow is adjustable and genuinely effective, something the budget chairs in this category cannot replicate. With Father's Day approaching on June 21, gaming chairs are squarely in the gift spotlight. The Titan Evo hits a sweet spot that makes it the obvious recommendation when budget is not the deciding factor. The Herman Miller Vantum sits at rank two for buyers who want office chair engineering applied to gaming use. Its 9.5 ergonomics score reflects real posture support that becomes noticeable during long sessions. The LiberNovo Omni is the most technically ambitious entry this year, adding a 9.5 features score through dynamic ergonomic adjustments that respond to your posture in real time. It is not cheap, but for people who sit twelve-plus hours daily it justifies its price. The ThunderX3 Solo 360 earned its rank 8 slot as the best budget recommendation with a 9.0 value score. It delivers proper lumbar and seat angle adjustment at a price that does not require deliberation. The Razer Iskur V2 at rank 4 is the right pick for Razer ecosystem buyers, with consistent build quality and integrated lumbar support that outperforms the add-on pillows found in cheaper alternatives. For Memorial Day weekend deals that carry into this week, the Titan Evo and Corsair TC100 are seeing the most sustained promotions.",
                "highlights": [
                    {"title": "Secretlab Titan Evo Remains the Benchmark", "body": "With a 9.5 build score and broad size availability, the Titan Evo is the chair that competing manufacturers measure themselves against. Its integrated magnetic memory foam lumbar and 4D armrests cover the ergonomic fundamentals without requiring expensive add-ons."},
                    {"title": "LiberNovo Omni Sets the 2026 High-End Standard", "body": "The LiberNovo Omni earns its rank 3 position through dynamic ergonomic adjustments that physically respond to sitting position changes. Its 9.5 features score is the highest in this category and reflects genuine innovation over traditional static lumbar designs."},
                    {"title": "Father's Day Demand Lifts Gaming Chair Category", "body": "Gaming chairs are one of the fastest-moving gift categories ahead of Father's Day June 21. The Titan Evo and ThunderX3 Solo 360 are appearing across gift guides at every major retailer, with current Memorial Day holdover pricing still in effect at some stores."},
                ]
            },
            "zh-tw": {
                "commentary": "Secretlab Titan Evo 是我一直推薦的電競椅冠軍，理由很直接。它的鋼製骨架、可調式腰枕和 4D 扶手，在這個價位帶提供了遠超預期的工藝水準。Herman Miller 的 Vantum 坐在第二名，帶著辦公椅等級的人體工學設計跨入電競市場，9.5 分的人體工學評分在長時間使用後會讓你明顯感受到差異。2026 年最值得關注的新品是 LiberNovo Omni，動態人體工學調整機制能即時回應你的坐姿，功能評分拿到 9.5 分，是本榜最高。對於每天坐超過 12 小時的重度使用者，這個功能不是噱頭，是真實需求。ThunderX3 Solo 360 以 9.0 的性價比分數守住第 8 名，是最推薦的平價選擇。在父親節 6 月 21 日到來之前，電競椅是各大禮物指南的熱門品項之一。Titan Evo 和 Corsair TC100 在部分通路還承接著美國陣亡將士紀念日的折扣效應。Razer Iskur V2 對於 Razer 生態系用戶是一致可靠的選擇，整合式腰部支撐的表現優於低價款附帶的外掛腰枕。整體而言，這個市場在 2026 年的選擇更廣，從 $100 美金以下到 $1,000 以上都有值得推薦的產品。",
                "highlights": [
                    {"title": "Secretlab Titan Evo 依然是業界基準", "body": "9.5 分的製造品質評分加上大尺寸選擇，Titan Evo 是競爭對手拿來比較的標桿。磁吸記憶泡棉腰枕和 4D 扶手涵蓋了人體工學基本需求，不需要額外花錢升級配件。"},
                    {"title": "LiberNovo Omni 樹立 2026 高端標準", "body": "LiberNovo Omni 的動態人體工學調整機制會隨坐姿變化即時回應，功能評分 9.5 分是本榜第一。對於長時間辦公或遊戲的用戶，這不只是規格，而是真實能感受到的舒適差距。"},
                    {"title": "父親節帶動電競椅採購旺季", "body": "父親節 6 月 21 日倒數三週，電競椅是禮物市場需求最強勁的品類之一。Titan Evo 和 ThunderX3 Solo 360 大量出現在各大通路的父親節禮物推薦清單，部分通路仍有美國陣亡將士紀念日後續折扣。"},
                ]
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK gaming-chairs")

def build_gaming_headsets():
    d, p = load("best-gaming-headsets.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Best Gaming Headsets 2026: Tested Picks for Comfort, Connectivity, and Communication", "url": "https://www.tomshardware.com/peripherals/gaming-headsets/best-gaming-headsets", "source": "Tom's Hardware"},
            {"title": "The 6 Best Gaming Headsets of 2026", "url": "https://www.rtings.com/headphones/reviews/best/by-usage/gaming", "source": "RTINGS.com"},
            {"title": "Best gaming headsets in 2026", "url": "https://www.pcgamer.com/best-gaming-headset/", "source": "PC Gamer"},
        ],
        "i18n": {
            "en": {
                "commentary": "The SteelSeries Arctis Nova Pro Omni is the headset I put at the top of this category in 2026, and it earns that position through measurable performance rather than brand loyalty. Its 12ms wireless latency, dual-battery hot-swap system, and superb spatial audio combine into a package that no single competitor matches across all three dimensions simultaneously. The 9.5 connectivity score reflects real-world versatility across PC, PlayStation, and Xbox without compromise. The Audeze Maxwell 2 at rank two is the choice for audio purists who happen to game. Its 9.8 audio quality score comes from planar magnetic drivers that reproduce positional cues with a precision that dynamic-driver headsets simply cannot achieve at any price. The caveat is comfort: the 7.5 comfort score is honest and matters during marathon sessions. Turtle Beach Stealth Pro II rounds out the top three as the most platform-flexible option, supporting simultaneous multi-console connection through its base station, a feature that matters to households with multiple consoles. Father's Day on June 21 is making gaming headsets a top three gift category this week. The HyperX Cloud Alpha Wireless sits at rank 6 with a 9.0 value score and 300-plus hours of claimed battery life, making it the recommendation for buyers who prioritize longevity and do not want to think about charging. The Razer BlackShark V3 Pro at rank 7 is the pick for Razer system users, with clean audio tuning and a price that does not require extended deliberation.",
                "highlights": [
                    {"title": "SteelSeries Arctis Nova Pro Omni Leads the 2026 Field", "body": "The Nova Pro Omni combines 12ms wireless latency with a hot-swappable dual-battery system, meaning you never face a dead-battery session interruption. Its multi-platform 2.4GHz and Bluetooth connectivity covers every gaming scenario from one device."},
                    {"title": "Audeze Maxwell 2 for Audiophile-Grade Gaming Audio", "body": "Planar magnetic drivers give the Maxwell 2 a 9.8 audio quality score that no dynamic-driver competitor achieves. For games where positional audio is a competitive advantage, like FPS titles, the clarity difference is immediately audible."},
                    {"title": "Father's Day Makes This Peak Headset Season", "body": "Gaming headsets are the fastest-moving gift category heading into Father's Day June 21. The Nova Pro Omni and HyperX Cloud Alpha Wireless are leading sales charts at major retailers, with both appearing prominently in curated gift guides this week."},
                ]
            },
            "zh-tw": {
                "commentary": "SteelSeries Arctis Nova Pro Omni 是我在 2026 年最推薦的電競耳機，理由是數據說話。12ms 無線延遲、熱插拔雙電池系統、以及優秀的空間音效，這三項同時做到最頂尖的耳機目前只有它。9.5 分的連接性評分反映了它在 PC、PS5、Xbox 三平台之間切換的真實彈性。Audeze Maxwell 2 排名第二，是音質優先玩家的首選。平面振膜單體帶來 9.8 分的音質評分，這個數字在動圈耳機裡無論花多少錢都買不到。要注意的是 7.5 分的舒適度，長時間配戴確實有感。Turtle Beach Stealth Pro II 排名第三，Base Station 支援多主機同時連接，對於家裡有多台主機的用戶是真實的加分項。父親節 6 月 21 日到了，電競耳機進入年度最強採購旺季。HyperX Cloud Alpha Wireless 以 9.0 分的性價比評分守在第六名，300 小時以上的電池續航讓它成為懶得思考充電問題的人最省心的選擇。Razer BlackShark V3 Pro 是 Razer 生態系用戶最順手的選項，音效調音乾淨，價格不需要糾結太久。整體來看，2026 年的電競耳機市場在無線延遲和多平台相容性上已大幅成熟。",
                "highlights": [
                    {"title": "SteelSeries Arctis Nova Pro Omni 領銜 2026 年市場", "body": "12ms 無線延遲加上熱插拔雙電池，確保在任何時間點都不會因為沒電被迫中斷遊戲。單一裝置同時支援 2.4GHz 和藍牙，一個耳機應付所有平台情境。"},
                    {"title": "Audeze Maxwell 2 帶來發燒級音質", "body": "平面振膜單體讓 Maxwell 2 拿到 9.8 分的音質評分，這是動圈耳機無法企及的水準。在需要精確方位感知的 FPS 遊戲中，音效定位的差距是立即可感受到的競技優勢。"},
                    {"title": "父親節旺季推動電競耳機銷量衝高", "body": "父親節 6 月 21 日倒數三週，電競耳機是採購清單排名前三的品類。Nova Pro Omni 和 HyperX Cloud Alpha Wireless 同時出現在各大通路的禮物指南首頁。"},
                ]
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK gaming-headsets")

def build_gaming_mice():
    d, p = load("best-gaming-mice.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Best Gaming Mouse 2026: Top Wired and Wireless Gaming Mice Tested", "url": "https://powerup-gaming.com/best-gaming-mouse-2026/", "source": "PowerUp Gaming"},
            {"title": "The Best Gaming Mouse of 2026: Mice Reviews", "url": "https://www.rtings.com/mouse/reviews/best/by-usage/gaming", "source": "RTINGS.com"},
            {"title": "2026 is shaping up to be a golden year for gaming mice as Razer FrameSync adds more goodies", "url": "https://www.pcgamer.com/hardware/gaming-mice/2026-is-shaping-up-to-be-a-golden-year-for-gaming-mice-as-razers-battery-boosting-framesync-adds-more-goodies-to-the-pot/", "source": "PC Gamer"},
        ],
        "i18n": {
            "en": {
                "commentary": "The Logitech G PRO X2 SUPERSTRIKE holds rank one through a combination of haptic-inductive analogue clicks and top-tier sensor performance that no other mouse in this category currently replicates. The 9.8 latency score is real: the haptic click mechanism eliminates the mechanical debounce delay that every traditional switch mouse carries. The result is input registration that competitive players notice immediately. The G PRO X2 DEX at rank two is the same platform in a larger shell, and the 8.6 value score makes it the better option for players with larger hands who would otherwise be penalized by the compact Superstrike dimensions. Computex 2026 runs June 2-5 in Taipei, and while peripheral announcements are not the headline act this year, Razer's FrameSync technology is generating pre-show coverage. The Viper V4 Pro at rank 3 already implements FrameSync with battery life benefits that close the gap between wireless and wired in long sessions. The Razer DeathAdder V4 Pro at rank 4 remains the ergonomic mouse benchmark: 56g, 45K DPI sensor, and a right-hand-dominant shape that has been refined over multiple generations. Father's Day demand is lifting peripheral sales broadly this week, and gaming mice are a natural gift category for PC gamers. The Pulsar X2 CL at rank 14 and Lamzu Maya X at rank 13 continue to represent the ultralight specialist segment, with 10.0 and 9.5 weight scores respectively that mainstream brands have not yet matched in this form factor.",
                "highlights": [
                    {"title": "Logitech G PRO X2 SUPERSTRIKE Sets a New Click Standard", "body": "Haptic-inductive analogue clicks remove mechanical debounce delay entirely, giving the Superstrike a 9.8 latency score and input feel that competitive players switching from traditional switches notice within minutes. It is the most significant click mechanism innovation since optical switches arrived."},
                    {"title": "Razer FrameSync Shapes the 2026 Wireless Narrative", "body": "Razer's FrameSync technology, live in the Viper V4 Pro, synchronizes sensor polling to display frames to reduce redundant reads and extend battery life. With Computex 2026 starting June 2, more FrameSync-equipped devices are expected to be announced in the coming days."},
                    {"title": "Father's Day Puts Gaming Mice in Gift Focus", "body": "Gaming mice are one of the most accessible high-impact gifts for PC gamers, with a clear price ladder from $50 to $180 that makes budgeting simple. The HyperX Pulsefire Haste 2 Wireless at rank 11 and the One Plus 1WE at rank 6 are leading mid-range gift recommendations this week."},
                ]
            },
            "zh-tw": {
                "commentary": "Logitech G PRO X2 SUPERSTRIKE 守住第一名的位置，靠的是觸覺感應類比點擊機制，這個技術徹底去掉了傳統機械開關的防彈跳延遲。9.8 分的延遲評分不是噱頭，競技玩家從傳統滑鼠換過來之後，幾分鐘內就能感受到輸入的差距。G PRO X2 DEX 排名第二，同樣的核心平台配上更大的外殼，8.6 分的性價比對手掌較大的玩家來說反而是更值得的選擇。Computex 2026 在 6 月 2 到 5 日於台北登場，雖然周邊設備不是今年的主秀，但 Razer 的 FrameSync 技術已經在賽前引發不少討論。Viper V4 Pro 現在已內建 FrameSync，透過同步感應器輪詢頻率和螢幕幀率來延長電池壽命，縮短無線和有線之間的體感差距。DeathAdder V4 Pro 依然是人體工學滑鼠的標桿，56g 重量加上 45K DPI 感應器，右手握持設計經過多個世代的優化已經非常成熟。父親節三週後到來，電競滑鼠是 PC 玩家禮物清單中性價比最高的品類之一，從 $50 到 $180 美金的價格梯度讓預算規劃很清晰。Pulsar X2 CL 和 Lamzu Maya X 繼續代表超輕量專業市場，10.0 分和 9.5 分的重量評分是主流品牌目前還沒追上的水準。",
                "highlights": [
                    {"title": "Logitech G PRO X2 SUPERSTRIKE 重新定義點擊手感", "body": "觸覺感應類比點擊機制徹底消除機械防彈跳延遲，9.8 分的延遲評分背後是競技玩家能立即感受到的輸入差距。這是光學開關問世以來最重要的點擊機制革新。"},
                    {"title": "Razer FrameSync 引領 2026 無線技術敘事", "body": "Viper V4 Pro 內建的 FrameSync 技術將感應器輪詢同步至螢幕幀率，減少多餘讀取並延長電池壽命。Computex 2026 在 6 月 2 日開幕，更多搭載 FrameSync 的新品預計很快發布。"},
                    {"title": "父親節旺季讓電競滑鼠成為熱門禮物", "body": "電競滑鼠是 PC 玩家最好入手的高影響力禮物，$50 到 $180 的清晰價格梯度讓任何預算都有對應的推薦。HyperX Pulsefire Haste 2 Wireless 和 One Plus 1WE 是本週中價位禮物推薦的領頭羊。"},
                ]
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK gaming-mice")

def build_gaming_monitors():
    d, p = load("best-gaming-monitors.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "The Best OLED Gaming Monitors to Buy in 2026", "url": "https://tftcentral.co.uk/recommendations/the-best-oled-gaming-monitors-to-buy-in-2026", "source": "TFTCentral"},
            {"title": "Best gaming monitors 2026: 4K, HDR, best overall, budget, and more", "url": "https://www.pcworld.com/article/813301/best-gaming-monitors.html", "source": "PCWorld"},
            {"title": "Best Gaming Monitors 2026: Budget, Curved, G-Sync and More", "url": "https://www.tomshardware.com/reviews/best-gaming-monitors,4533.html", "source": "Tom's Hardware"},
        ],
        "i18n": {
            "en": {
                "commentary": "The ASUS ROG Swift OLED PG27UCDM holds the top position in gaming monitors for 2026, and the case for it is straightforward. A 9.8 image quality score backed by OLED contrast, 4K resolution, and HDR that actually impresses rather than just checks a box. This is the monitor I recommend to anyone who has already committed to a high-end GPU and wants their display to be the visual bottleneck. The 9.5 connectivity score means HDMI 2.1, DisplayPort 2.1, and USB-C with power delivery are all present, covering current and next-generation console and PC connections simultaneously. The LG UltraGear 27GX790B at rank two earns a 10.0 refresh rate score, the only monitor in this roundup to do so. At 480Hz with 1440p resolution, it is the definitive choice for competitive esports players where frames-per-second is the metric that matters. The 9.2 image quality score is high enough to make this more than a one-trick display. The MSI MPG 341CQR X36 at rank three fills the ultrawide slot with QD-OLED technology and a 9.5 image quality score. Ultrawide adoption has accelerated in 2026 as the new 34-inch QD-OLED V-Stripe subpixel layout finally matches LCD-grade text clarity, removing the last objection for productivity use alongside gaming. The 5th-generation QD-OLED panels across multiple monitors in this list deliver improved brightness and burn-in prevention sensors that address the two main concerns buyers had with first-generation OLED. The AOC Q27G3XMN at rank 8 carries a 9.8 value score and remains the answer for budget-conscious buyers who want IPS-level image quality at mainstream pricing.",
                "highlights": [
                    {"title": "ASUS ROG Swift OLED PG27UCDM Defines the 4K OLED Standard", "body": "A 9.8 image quality score, full HDMI 2.1 and DP 2.1 connectivity, and HDR performance that delivers visible impact at typical gaming brightness levels make this the reference 4K OLED gaming monitor for 2026. Its position at rank one reflects consensus across all major reviewer panels."},
                    {"title": "5th-Gen QD-OLED Solves the Text Clarity Problem", "body": "The new V-Stripe RGB subpixel layout on 2026 QD-OLED panels brings text sharpness to LCD parity, removing the last barrier to using OLED monitors as all-day work and gaming displays. The MSI MPG 341CQR X36 and Samsung Odyssey OLED G8 both benefit from this improvement."},
                    {"title": "LG UltraGear 27GX790B Earns the 10.0 Refresh Rate Score", "body": "480Hz at 1440p is the highest refresh rate in this category and earns the only 10.0 refresh rate score in the roundup. For competitive FPS players, the motion clarity at 480Hz versus 240Hz is a real perceptual improvement that translates to smoother target tracking."},
                ]
            },
            "zh-tw": {
                "commentary": "ASUS ROG Swift OLED PG27UCDM 是 2026 年電競顯示器的頂點，理由很具體。9.8 分的畫質評分來自 OLED 的真黑對比、4K 解析度、以及真正有感的 HDR 表現，不是只是規格表上的勾選項目。如果你已經配備了高端顯示卡，這台是讓顯示器不成為視覺短板的選擇。9.5 分的連接性涵蓋 HDMI 2.1、DisplayPort 2.1、USB-C 供電，現在和下一代的主機及 PC 連接都沒問題。LG UltraGear 27GX790B 排名第二，拿到全榜唯一的 10.0 更新率評分。1440p 解析度下的 480Hz 是電競玩家的終極配置，9.2 分的畫質評分也夠高，不是只有更新率的單一技巧牌。MSI MPG 341CQR X36 以第三名守住超寬螢幕的門面，QD-OLED 面板搭配 9.5 的畫質評分。2026 年第五代 QD-OLED 面板採用 V-Stripe 次像素排列，文字銳利度終於追平 LCD，消除了 OLED 作為辦公螢幕最後的顧慮。整個榜單裡的 QD-OLED 機型都受益於更高亮度和內建燒屏預防感應器，解決了一代 OLED 最讓買家擔心的兩個問題。AOC Q27G3XMN 以 9.8 的性價比評分守在第 8 名，是預算受限但不想犧牲畫質的玩家最該看的選項。",
                "highlights": [
                    {"title": "ASUS ROG Swift OLED PG27UCDM 樹立 4K OLED 標準", "body": "9.8 分畫質評分、完整 HDMI 2.1 和 DP 2.1 連接、以及在一般遊戲亮度下就有明顯效果的 HDR 表現，讓這台成為 2026 年 4K OLED 電競顯示器的基準參考機，排名第一是各大主流評測機構的共識。"},
                    {"title": "第五代 QD-OLED 解決文字清晰度問題", "body": "2026 年 QD-OLED 面板採用 V-Stripe RGB 次像素排列，文字銳利度達到 LCD 水準，讓 OLED 全天辦公加遊戲的使用場景再無障礙。MSI MPG 341CQR X36 和 Samsung Odyssey OLED G8 都因此受益。"},
                    {"title": "LG UltraGear 27GX790B 獨得 10.0 更新率評分", "body": "1440p 下的 480Hz 是本榜最高更新率，也是唯一拿到 10.0 更新率評分的機型。對於競技 FPS 玩家，480Hz 相對於 240Hz 在動態清晰度上是真實可感的進步，體現在目標追蹤的流暢感上。"},
                ]
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK gaming-monitors")

def build_mechanical_keyboards():
    d, p = load("best-mechanical-keyboards.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Best Mechanical Keyboard 2026: 7 Gaming Picks Tested", "url": "https://keyboardtester.click/blog/best-mechanical-keyboards-for-gaming-2026.php", "source": "KeyboardTester"},
            {"title": "The 5 Best Mechanical Keyboards of 2026", "url": "https://www.rtings.com/keyboard/reviews/best/mechanical", "source": "RTINGS.com"},
            {"title": "Best Mechanical Keyboards in 2026", "url": "https://techknuckles.com/articles/best-mechanical-keyboards-2026", "source": "TechKnuckles"},
        ],
        "i18n": {
            "en": {
                "commentary": "The Wooting 60HE is the keyboard that changed how competitive gaming peripherals are evaluated, and in 2026 it still sets the standard. Its Hall Effect magnetic switches deliver Rapid Trigger with 0.1mm resolution and analog input that no mechanical switch can replicate. The 9.8 switch and latency scores are the highest in this category and reflect genuine technical superiority rather than marketing specification inflation. The transition is real: as of April 2026, 40% of the top 2,252 tracked professional esports players have adopted Hall Effect or analog optical switch keyboards, up from essentially zero in 2022. The Wooting 80HE at rank two is the full-size variant with the same switch platform for players who need a numpad or prefer the layout for productivity. The SteelSeries Apex Pro TKL Wireless at rank three is the mainstream answer: OmniPoint switches with adjustable actuation, wireless freedom, and a 9.0 build quality score that reflects robust aluminum construction. For buyers who prioritize typing feel alongside gaming performance, the Keychron Q1 Pro at rank four delivers a 9.5 build score with its gasket-mounted aluminum frame and pre-lubed switches. Its 9.0 value score makes it the recommendation in the premium typing-first tier. The NuPhy Field75 HE at rank five adds Hall Effect technology in a wireless 75% form factor, combining the competitive gaming features of the Wooting line with the portability that desk aesthetics-focused buyers prefer. Father's Day timing is bringing keyboards into gift consideration, and the Keychron K8 Pro and NuPhy Air75 V2 at ranks 10 and 11 represent the most giftable price points with strong value scores.",
                "highlights": [
                    {"title": "Wooting 60HE Leads as Hall Effect Adoption Hits 40% of Pros", "body": "As of April 2026, 40% of the top professional esports players tracked use a Hall Effect or analog optical keyboard, a figure that was essentially zero in 2022. The Wooting 60HE drove this shift with Rapid Trigger and 0.1mm resolution actuation that traditional mechanical switches cannot match."},
                    {"title": "SteelSeries Apex Pro TKL Wireless Covers the Mainstream Competitive Tier", "body": "OmniPoint adjustable actuation switches, wireless 2.4GHz, and aluminum construction give the Apex Pro TKL Wireless a 9.0 build score and 9.5 latency score. It is the keyboard for competitive players who want proven technology from a widely available brand."},
                    {"title": "Keychron Q1 Pro Leads the Premium Typing-First Segment", "body": "Gasket-mounted aluminum frame, pre-lubed switches, and hot-swap capability produce a 9.5 build score and 9.0 value score that make the Q1 Pro the strongest typing-focused mechanical keyboard at its price point. The south-facing RGB eliminates shine-through interference on angled keycap sets."},
                ]
            },
            "zh-tw": {
                "commentary": "Wooting 60HE 是那個改變競技鍵盤評估方式的產品，到了 2026 年依然是業界標準。霍爾效應磁性開關搭配 0.1mm 解析度的 Rapid Trigger，以及類比輸入功能，這些是任何傳統機械開關都無法複製的技術優勢。9.8 分的開關和延遲評分是本榜最高，背後是真實的技術領先，不是規格虛報。這個趨勢已經到達引爆點，2026 年 4 月的數據顯示，追蹤中的頂尖職業電競選手有 40% 使用霍爾效應或類比光學開關鍵盤，2022 年這個數字近乎零。Wooting 80HE 排名第二，同樣的開關平台配上含數字鍵盤的完整佈局，適合需要 Full Size 配置的玩家。SteelSeries Apex Pro TKL Wireless 排第三，是主流競技玩家的標準答案，可調式觸發點加無線自由度，9.0 分的製造品質反映扎實的鋁製外殼工藝。Keychron Q1 Pro 排第四，如果你打字和遊戲都在意，它的彈性安裝結構加上預潤滑開關帶來 9.5 分的製造品質，9.0 分的性價比在高端打字鍵盤中是非常合理的定位。NuPhy Field75 HE 排第五，把霍爾效應技術帶進無線 75% 鍵盤，兼顧競技功能和桌面美學。父親節旺季帶動鍵盤禮物需求，Keychron K8 Pro 和 NuPhy Air75 V2 的價位是最容易讓人點頭的禮物選擇。",
                "highlights": [
                    {"title": "Wooting 60HE 領銜，職業選手霍爾效應採用率達 40%", "body": "2026 年 4 月數據：追蹤中的頂尖職業電競選手有 40% 改用霍爾效應或類比光學鍵盤，2022 年幾乎為零。Wooting 60HE 的 Rapid Trigger 和 0.1mm 解析度觸發是這波轉移的推手。"},
                    {"title": "SteelSeries Apex Pro TKL Wireless 守住主流競技市場", "body": "OmniPoint 可調式觸發、2.4GHz 無線、鋁製外殼，帶來 9.0 分製造品質和 9.5 分延遲評分。對想用成熟技術和主流品牌的競技玩家而言是最無懸念的選擇。"},
                    {"title": "Keychron Q1 Pro 是高端打字玩家的首選", "body": "彈性安裝鋁框、預潤滑開關、熱插拔設計帶來 9.5 分製造品質和 9.0 分性價比，是這個價位段打字體驗最強的機械鍵盤。南向 RGB 設計消除對傾斜鍵帽組的透光干擾。"},
                ]
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK mechanical-keyboards")

def build_handheld_gaming_consoles():
    d, p = load("best-handheld-gaming-consoles.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Steam Deck OLED vs ROG Ally X vs Switch 2: The 2026 Handheld Buyer's Guide", "url": "https://spawningpoint.com/article/steam-deck-vs-rog-ally-x-vs-switch-2-2026", "source": "SpawningPoint"},
            {"title": "Best gaming handhelds 2026 ranked: Steam Deck, Xbox Ally X, Switch 2, Legion Go 2 and more", "url": "https://www.windowscentral.com/gaming-best-gaming-handhelds", "source": "Windows Central"},
            {"title": "The best gaming handhelds for 2026", "url": "https://tech.yahoo.com/gaming/article/the-best-gaming-handhelds-for-2026-180000267.html", "source": "Yahoo Tech"},
        ],
        "i18n": {
            "en": {
                "commentary": "The Steam Deck OLED holds the top position in handheld gaming because it delivers the broadest combination of library access, display quality, and value that no competitor currently matches as a complete package. Its 9.5 scores in library, display, ergonomics, and value are not accidental: Valve's SteamOS ecosystem and the OLED panel's contrast and battery optimization make it the default recommendation for PC gaming on the go. The Nintendo Switch 2 at rank two is the answer for buyers who want Nintendo-exclusive titles and a family-friendly ecosystem. Its $449.99 price, 9-hour battery life, and 9.5 library score reflect the fact that Mario Kart World and the Switch 2 exclusive catalog cannot be replicated anywhere else. The ROG Ally X with Xbox branding at rank three carries a 9.5 performance score from its AMD Ryzen Z2 Extreme and 24GB RAM configuration, making it the strongest raw-performance handheld available. At $799, it is a deliberate purchase for buyers who want AAA PC gaming without a desk. Father's Day is pushing all three top handhelds into heavy gift guide rotation this week. Valve did raise Steam Deck prices by roughly $240 in May 2026, citing higher memory and storage component costs, but the OLED model still delivers the best value per dollar in the open-PC handheld category. The Lenovo Legion Go 2 at rank four combines a 9.5 display score with its large format screen and detachable controllers, while the MSI Claw 8 AI+ rounds out the top five with a balanced feature set.",
                "highlights": [
                    {"title": "Steam Deck OLED Maintains Comprehensive Lead", "body": "Four separate 9.5 category scores in library, display, ergonomics, and value confirm the Steam Deck OLED as the most well-rounded handheld in 2026. Even after Valve's May price increase, it remains the strongest value in the open-PC handheld category."},
                    {"title": "Nintendo Switch 2 Is the Exclusive Ecosystem Argument", "body": "At $449.99 with 9-hour battery and the Mario Kart World bundle at $499.99, the Switch 2 holds a category argument that no PC handheld can counter: the Nintendo exclusive library. Its 9.5 library score reflects depth that goes beyond raw game counts."},
                    {"title": "Father's Day Puts All Three Top Handhelds in Demand", "body": "The Steam Deck OLED, Switch 2, and ROG Xbox Ally X are all appearing prominently in Father's Day gift guides with June 21 three weeks out. The Switch 2's lower entry price makes it the most accessible premium handheld gift in this period."},
                ]
            },
            "zh-tw": {
                "commentary": "Steam Deck OLED 守住掌機榜第一名，原因是它在遊戲庫、螢幕品質、人體工學和性價比四個維度同時拿到 9.5 分，這個組合目前沒有競爭對手能全面超越。Valve 的 SteamOS 生態系加上 OLED 面板的對比度和電池最佳化，讓它成為 PC 掌機的預設推薦。要注意的是 Valve 在 2026 年 5 月調漲了約 $240 美金的售價，理由是記憶體和儲存元件成本上升，不過即使調價後，OLED 版在開放 PC 掌機類別的性價比依然最強。Nintendo Switch 2 排名第二，$449.99 的售價、9 小時電池、Mario Kart World 等 9.5 分遊戲庫，這些是 PC 掌機無法複製的優勢。任天堂獨占遊戲的廣度和深度不是光靠規格就能追上的。ROG Xbox Ally X 排名第三，AMD Ryzen Z2 Extreme 加 24GB RAM 帶來 9.5 分效能評分，$799 的售價買到的是真正的 AAA PC 遊戲體驗，不需要一張桌子。父親節三週後到來，Steam Deck OLED、Switch 2 和 ROG Xbox Ally X 同時出現在各大禮物指南的顯眼位置。Lenovo Legion Go 2 排第四，大尺寸螢幕帶來 9.5 分的顯示評分，可拆卸控制器也是加分項。MSI Claw 8 AI+ 完成前五名的陣容，整體均衡表現守住位置。",
                "highlights": [
                    {"title": "Steam Deck OLED 全面領先優勢依然穩固", "body": "遊戲庫、螢幕、人體工學、性價比四項各得 9.5 分，確認 Steam Deck OLED 是 2026 年最均衡的掌機。即使 Valve 在 5 月調漲售價，在開放 PC 掌機類別的性價比依然無可取代。"},
                    {"title": "Nintendo Switch 2 是獨占生態系的最強論據", "body": "$449.99 售價搭配 9 小時電池和 Mario Kart World 組合，Switch 2 的 9.5 分遊戲庫評分背後是任何 PC 掌機都無法複製的任天堂獨占陣容。$499.99 的組合包是目前最值的入手方式。"},
                    {"title": "父親節讓三大掌機同時進入禮物旺季", "body": "Steam Deck OLED、Switch 2 和 ROG Xbox Ally X 三款掌機在父親節 6 月 21 日前三週同時出現在各大禮物指南首頁。Switch 2 較低的入門價讓它成為這個時期最容易下手的高端掌機禮物。"},
                ]
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK handheld-gaming-consoles")

def build_3d_printers():
    d, p = load("best-3d-printers.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "The Best 3D Printers for Home, Workshop or Business in 2026", "url": "https://www.tomshardware.com/best-picks/best-3d-printers", "source": "Tom's Hardware"},
            {"title": "Best 3D Printers 2026: Our Top Picks in 25 Categories", "url": "https://all3dp.com/1/best-3d-printer-reviews-top-3d-printers-home-3-d-printer-3d/", "source": "All3DP"},
            {"title": "I reviewed more than 50 of the best 3D printers of 2026", "url": "https://www.techradar.com/best/best-3d-printers", "source": "TechRadar"},
        ],
        "i18n": {
            "en": {
                "commentary": "The Bambu Lab P2S Combo holds the top rank in 2026 with a 9.4 overall score, and its case is built on the combination of multi-color capability, print speed, and ecosystem integration that no competitor currently packages as cleanly. The 9.5 scores in print quality, multicolor, and ecosystem reflect a system that delivers professional-quality outputs from a consumer-friendly workflow. The AMS lite multicolor system and automatic calibration mean the P2S Combo is genuinely plug-and-play compared to machines that require tuning expertise. The Bambu Lab X1 Carbon at rank two is the benchmark for print quality with its 9.8 score, but the 7.8 value score reflects its premium pricing relative to the P2S. For users who prioritize absolute output quality over cost, the X1 Carbon is the machine I point to. The Bambu Lab H2D at rank three is the new high-performance entry in the lineup, with 9.7 speeds and 9.7 print quality making it the fastest and most precise consumer machine currently available. Its 7.0 value score marks it as a specialist purchase. The Prusa Core One at rank four is the premium open-source alternative, carrying a 9.8 ecosystem score that reflects Prusa's depth of community support, firmware transparency, and material compatibility. For users who require full control over print parameters and refuse vendor lock-in, the Core One is the answer. The Elegoo Centauri Carbon at rank eight is the budget story of 2026: enclosed CoreXY printing at under $300 with 500mm/s speed capability, delivering capabilities that were $800 machines two years ago.",
                "highlights": [
                    {"title": "Bambu Lab P2S Combo Is the Multi-Color Standard", "body": "The P2S Combo earns its rank one position through a 9.5 score across print quality, multicolor, and ecosystem. The AMS lite system handles multi-material printing with minimal user intervention, making professional multi-color prints accessible without the tuning expertise that older multi-material systems required."},
                    {"title": "Elegoo Centauri Carbon Redefines Budget FDM in 2026", "body": "Enclosed CoreXY at under $300 with 500mm/s speed capability represents a fundamental shift in what budget 3D printing means. The Centauri Carbon's 9.8 value score is the highest in the category, and it delivers capabilities that were exclusively available in $800+ machines just two years ago."},
                    {"title": "Prusa Core One Anchors the Open-Source Tier", "body": "A 9.8 ecosystem score reflects Prusa's unmatched community documentation, firmware transparency, and material compatibility library. For users who need full parameter control, third-party material support, or refuse closed ecosystem constraints, the Core One is the definitive choice in 2026."},
                ]
            },
            "zh-tw": {
                "commentary": "Bambu Lab P2S Combo 以 9.4 分的總評分守住 2026 年 3D 印表機第一名。多色列印能力、列印速度、生態系整合三個維度各拿 9.5 分，這個組合目前沒有競爭對手能包裝得如此完整。AMS lite 多色系統加上自動校準，讓 P2S Combo 真正做到開箱即用，相比需要大量調整經驗的機器，這個易用性差距在新手和進階用戶身上都很有感。Bambu Lab X1 Carbon 排名第二，9.8 分的列印品質評分是本榜最高，但 7.8 分的性價比反映了它相對 P2S 的溢價。追求絕對輸出品質的用戶，X1 Carbon 是我指向的機器。Bambu Lab H2D 排名第三，9.7 分的速度和 9.7 分的列印品質讓它成為目前最快最精確的消費級機器，7.0 分的性價比定位它為專業用途採購。Prusa Core One 排名第四，9.8 分的生態系評分反映 Prusa 在社群支援深度、韌體透明度和材料相容性的無可匹敵的積累。需要完整參數控制並且拒絕封閉生態系的用戶，Core One 是 2026 年的明確答案。Elegoo Centauri Carbon 是 2026 年的平價傳說，$300 以內的封閉式 CoreXY 機器帶來 500mm/s 的速度，這個規格兩年前要花 $800 以上才買得到，9.8 分的性價比是全榜最高。",
                "highlights": [
                    {"title": "Bambu Lab P2S Combo 是多色列印的標準答案", "body": "列印品質、多色能力、生態系三項各拿 9.5 分，讓 P2S Combo 牢牢守住第一名。AMS lite 多色系統最小化用戶干預，讓多色列印從需要專業調整知識的困難任務，變成一般用戶能輕鬆完成的工作流程。"},
                    {"title": "Elegoo Centauri Carbon 重新定義 2026 年平價 FDM", "body": "$300 以下的封閉 CoreXY 機器達到 500mm/s 列印速度，9.8 分的性價比是全榜最高。這個規格兩年前要 $800 以上才能達到，Centauri Carbon 代表了平價 3D 列印門檻的根本性下降。"},
                    {"title": "Prusa Core One 是開源生態系的定海神針", "body": "9.8 分的生態系評分來自 Prusa 無可匹敵的社群文件深度、韌體透明度、以及材料相容性資料庫。需要完整參數控制或拒絕封閉生態的用戶，Core One 是 2026 年的唯一答案。"},
                ]
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK 3d-printers")

if __name__ == "__main__":
    build_laptops()
    build_gaming_chairs()
    build_gaming_headsets()
    build_gaming_mice()
    build_gaming_monitors()
    build_mechanical_keyboards()
    build_handheld_gaming_consoles()
    build_3d_printers()
    print("Batch 2 complete")
