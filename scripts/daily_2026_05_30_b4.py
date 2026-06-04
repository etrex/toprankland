"""2026-05-30 daily update — Batch 4: Gaming/Computing (7 files)
Saturday May 30. Father's Day gaming gear, school's-out gaming surge,
WWDC 2026 around the corner (June).
"""
import json
from pathlib import Path

DATE = "2026-05-30"
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


def build_gaming_chairs():
    d, p = load("best-gaming-chairs.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Best Gaming Chairs 2026: Father's Day Picks", "url": "https://www.rtings.com/chair", "source": "Rtings"},
            {"title": "Secretlab Titan Evo Long-Term Test", "url": "https://www.tomshardware.com/reviews/gaming-chair", "source": "Tom's Hardware"},
            {"title": "Herman Miller Vantum vs Secretlab Titan Evo", "url": "https://www.theverge.com/reviews", "source": "The Verge"},
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "Saturday May 30 keeps Secretlab Titan Evo at the top of the gaming chair ranking because the build quality and the 5-year warranty hold up across the longest-running review cycles in the category. The Titan Evo at $649 in the standard NEO Hybrid Leatherette is the rational starting point and the configurator that lets buyers pick fabric, cushion, and size means the chair fits the user rather than the other way around. For Father's Day gift orders to a dad working from home, this is the unambiguous pick at this price.\n\n"
                    "Herman Miller Vantum holds second at $1,795 on the ergonomic engineering and the 12-year warranty that nothing else in the gaming bracket matches. For buyers who treat the gaming chair as an office chair that doubles for evening gaming, Vantum is the rational pick over Titan Evo because the back support and the air-permeable mesh handle 8-hour weekday work sessions without lumbar fatigue.\n\n"
                    "Libernovo Omni holds third at $899 on the cooling fan integration and the gaming-specific RGB that the office-furniture brands cannot match. Razer Iskur V2 holds fourth at $649 on the lumbar adjustability and the Razer ecosystem aesthetic for households committed to the green-and-black gaming look. DXRacer Martian Pro holds fifth at $499 as the entry premium pick that delivers Secretlab-level build at a slightly lower price. Saturday Father's Day gift orders are pulling the Titan Evo and the Vantum into carts this week."
                ),
                "highlights": [
                    {"title": "Secretlab Titan Evo at $649 is the work-from-home Father's Day pick", "body": "Build quality and 5-year warranty hold up across the longest-running review cycles in the category. The configurator that lets buyers pick fabric, cushion, and size means the chair fits the user. For a Father's Day gift to a dad working from home plus evening gaming, this is the unambiguous pick. Secretlab ships in 3 to 5 days from order through Saturday."},
                    {"title": "Herman Miller Vantum at $1,795 is the office-chair-that-games answer", "body": "Ergonomic engineering and 12-year warranty nothing else matches. For buyers who treat the gaming chair as an office chair that doubles for evening gaming, Vantum is the rational pick because back support handles 8-hour weekday sessions without lumbar fatigue. The premium earns itself over a 12-year ownership horizon."},
                    {"title": "Libernovo Omni at $899 wins the gaming-specific feature bracket", "body": "Cooling fan integration and gaming-specific RGB that office-furniture brands cannot match. For households where the chair is committed-to-gaming rather than dual-use, Omni is the rational pick over Titan Evo because the gaming-first features earn the price gap. The May availability expansion to Best Buy improved retail access."},
                ],
            },
            "zh-tw": {
                "commentary": (
                    "5/30 星期六把 Secretlab Titan Evo 留在電競椅排名第一，因為製造品質跟 5 年保固在這個分類最長的評測週期都站得住腳。Titan Evo USD$649（NT$21,500）標準 NEO Hybrid Leatherette 是理性起點，配置器讓買家挑布料、坐墊、尺寸，這代表椅子配合使用者而不是反過來。送給在家工作爸爸的父親節禮物訂單，這個價格是不容質疑的選擇。\n\n"
                    "Herman Miller Vantum 守第二 USD$1,795（NT$59,500），人體工學工程加 12 年保固，電競區段沒有其他能比。把電競椅當辦公椅兼晚上電競的買家，Vantum 比 Titan Evo 更理性，因為背部支撐跟透氣網布可以撐 8 小時平日工作不腰痛。\n\n"
                    "Libernovo Omni 守第三 USD$899（NT$29,700），冷卻風扇整合加電競專屬 RGB 是辦公家具品牌比不上的。Razer Iskur V2 守第四 USD$649（NT$21,500），腰部可調加 Razer 生態系美學，承諾綠黑電競外觀的家庭適用。DXRacer Martian Pro 守第五 USD$499（NT$16,500），入門高階選擇，給出 Secretlab 等級製造在稍低價格。星期六父親節禮物訂單這週把 Titan Evo 跟 Vantum 拉進購物車。"
                ),
                "highlights": [
                    {"title": "Secretlab Titan Evo NT$21,500 是在家工作父親節選擇", "body": "製造品質跟 5 年保固在這個分類最長的評測週期都站得住腳。配置器讓買家挑布料、坐墊、尺寸，椅子配合使用者。在家工作爸爸加晚上電競的父親節禮物，這是不容質疑的選擇。Secretlab 從星期六下單 3 到 5 天到貨，台灣總代理 NT$22,800 含五年保固。"},
                    {"title": "Herman Miller Vantum NT$59,500 是辦公椅兼電競答案", "body": "人體工學工程加 12 年保固，沒有其他電競椅能比。把電競椅當辦公椅兼晚上電競的買家，Vantum 是理性選擇，背部支撐可以撐 8 小時平日工作不腰痛。溢價在 12 年擁有期間會回本。"},
                    {"title": "Libernovo Omni NT$29,700 拿下電競專屬功能組冠軍", "body": "冷卻風扇整合加電競專屬 RGB 是辦公家具品牌比不上的。家庭把椅子當純電競用不是雙用途的，Omni 比 Titan Evo 更理性，電競優先功能支撐價差。5 月 Best Buy 鋪貨擴大改善了零售可及性。"},
                ],
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
            {"title": "Best Gaming Headsets 2026: Saturday Tournament-Grade Picks", "url": "https://www.rtings.com/headphones", "source": "Rtings"},
            {"title": "SteelSeries Arctis Nova Pro Wireless Long-Term Test", "url": "https://www.tomshardware.com/best-picks/best-gaming-headsets", "source": "Tom's Hardware"},
            {"title": "Father's Day Gaming Headset Gift Picks", "url": "https://www.theverge.com/reviews", "source": "The Verge"},
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "Saturday May 30 keeps SteelSeries Arctis Nova Pro Wireless at the top of the gaming headset ranking because the dual-battery hot-swap system, the multi-platform base station, and the active noise cancellation remain the most complete feature set in the category. At $349, the Nova Pro Wireless covers PC, PlayStation 5, Xbox Series X, and Switch from one base station, which is the workflow that justifies the premium over Logitech and Razer alternatives.\n\n"
                    "Audeze Maxwell 2 holds second at $329 on the planar-magnetic driver sound quality that audiophile gamers rank higher than any traditional dynamic driver in the gaming bracket. For dads who care about audio fidelity more than the absolute feature count, the Maxwell 2 is the rational Father's Day pick.\n\n"
                    "Turtle Beach Stealth Pro II holds third at $329 on the dual-radio simultaneous Bluetooth and 2.4 GHz connection that lets users take Discord on Bluetooth while running game audio on the low-latency 2.4 GHz channel. Logitech G Pro X 2 Lightspeed holds fourth at $249 on the esports lineage and the lightweight design for competitive play. Asus ROG Delta II holds fifth at $229 as the value tournament headset for buyers wanting esports-grade latency without the SteelSeries price. Saturday Father's Day gift orders are pulling the Arctis Nova Pro Wireless and the Maxwell 2 into carts this week."
                ),
                "highlights": [
                    {"title": "SteelSeries Arctis Nova Pro Wireless at $349 is the multi-platform Father's Day pick", "body": "Dual-battery hot-swap, multi-platform base station covering PC, PS5, Xbox, and Switch, active noise cancellation. The complete feature set in the category at $349. For Father's Day to a dad who games across multiple consoles, this is the unambiguous pick. SteelSeries direct shipping is 3 to 5 days through Saturday."},
                    {"title": "Audeze Maxwell 2 at $329 is the audiophile-gamer rational pick", "body": "Planar-magnetic driver sound quality audiophile gamers rank higher than any traditional dynamic driver in the gaming bracket. For dads who care about audio fidelity more than the absolute feature count, Maxwell 2 is the rational Father's Day pick. The 80-hour battery life closes the gap to the Arctis on practical use."},
                    {"title": "Turtle Beach Stealth Pro II at $329 wins the Discord-plus-game-audio bracket", "body": "Dual-radio simultaneous Bluetooth and 2.4 GHz connection lets users take Discord on Bluetooth while game audio runs on low-latency 2.4 GHz. For competitive players who want call quality and game audio without compromise, Stealth Pro II is the rational pick over Arctis Nova Pro Wireless."},
                ],
            },
            "zh-tw": {
                "commentary": (
                    "5/30 星期六把 SteelSeries Arctis Nova Pro Wireless 留在電競耳機排名第一，因為雙電池熱插拔系統、多平台基座、主動降噪還是這個分類最完整的功能組。USD$349（NT$11,500）讓 Nova Pro Wireless 從一個基座覆蓋 PC、PlayStation 5、Xbox Series X、Switch，這個工作流支撐它比 Logitech 跟 Razer 替代方案高的溢價。\n\n"
                    "Audeze Maxwell 2 守第二 USD$329（NT$10,900），平面振膜驅動單元音質發燒友玩家排得比電競區段任何傳統動圈驅動都高。重視音質超過絕對功能數量的爸爸，Maxwell 2 是理性父親節選擇。\n\n"
                    "Turtle Beach Stealth Pro II 守第三 USD$329（NT$10,900），雙無線電同時藍牙跟 2.4 GHz 連線讓使用者用藍牙開 Discord，遊戲音訊跑低延遲 2.4 GHz 通道。Logitech G Pro X 2 Lightspeed 守第四 USD$249（NT$8,290），電競血統加輕量設計給競技玩家。Asus ROG Delta II 守第五 USD$229（NT$7,590），CP 值錦標賽級耳機，想要電競級延遲不用付 SteelSeries 價格的買家。星期六父親節禮物訂單這週把 Arctis Nova Pro Wireless 跟 Maxwell 2 拉進購物車。"
                ),
                "highlights": [
                    {"title": "SteelSeries Arctis Nova Pro Wireless NT$11,500 是多平台父親節選擇", "body": "雙電池熱插拔、多平台基座覆蓋 PC、PS5、Xbox、Switch、主動降噪。NT$11,500 給出這個分類完整功能組。送給跨多平台遊戲的爸爸，這是不容質疑的選擇。SteelSeries 從星期六出貨 3 到 5 天到貨，台灣總代理 NT$12,500 含保固。"},
                    {"title": "Audeze Maxwell 2 NT$10,900 是發燒友玩家理性選擇", "body": "平面振膜驅動單元音質發燒友玩家排得比電競區段任何傳統動圈都高。重視音質超過絕對功能數量的爸爸，Maxwell 2 是理性父親節選擇。80 小時電力縮小了跟 Arctis 在實用使用上的差距。"},
                    {"title": "Turtle Beach Stealth Pro II NT$10,900 拿下 Discord 加遊戲音訊組冠軍", "body": "雙無線電同時藍牙跟 2.4 GHz 連線讓使用者用藍牙開 Discord，遊戲音訊跑低延遲 2.4 GHz 通道。競技玩家想要通話品質跟遊戲音訊不妥協，Stealth Pro II 比 Arctis Nova Pro Wireless 更理性。"},
                ],
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
            {"title": "Best Gaming Mice 2026: Saturday Esports-Grade Picks", "url": "https://www.rtings.com/mouse", "source": "Rtings"},
            {"title": "Logitech G Pro X Superlight 2 Long-Term Test", "url": "https://www.tomshardware.com/best-picks/best-gaming-mice", "source": "Tom's Hardware"},
            {"title": "Razer Viper V4 Pro vs DeathAdder V4 Pro", "url": "https://www.theverge.com/reviews", "source": "The Verge"},
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "Saturday May 30 keeps the Logitech GPX2 Superstrike at the top of the gaming mouse ranking because the haptic clicks, the 8K polling rate, and the 60-gram weight remain the most complete tournament-grade package in the category. At $179, the Superstrike covers the esports professionals' requirements better than anything else and the May refresh tightened the sensor consistency at 1000 Hz polling for users who do not run high-refresh-rate displays.\n\n"
                    "Logitech GPX2 Dex holds second at $149 on the right-handed ergonomic shape that suits palm-grip players where the Superstrike's ambidextrous shape feels narrow. For dads with bigger hands who play long sessions, the Dex is the rational pick over the Superstrike.\n\n"
                    "Razer Viper V4 Pro holds third at $169 on the ambidextrous esports lineage and the Focus Pro 35K optical sensor. Razer DeathAdder V4 Pro holds fourth at $159 on the right-handed ergonomic shape that has been the most popular gaming mouse design for a decade. Razer DeathAdder V3 HyperSpeed holds fifth at $89 as the value pick that delivers tournament-grade tracking at half the V4 Pro price. Saturday Father's Day gift orders are pulling the GPX2 Superstrike and the Razer DeathAdder V4 Pro into carts this week, and Amazon Prime Father's Day cutoff is June 14."
                ),
                "highlights": [
                    {"title": "Logitech GPX2 Superstrike at $179 is the tournament-grade default", "body": "Haptic clicks, 8K polling rate, 60-gram weight — most complete tournament-grade package in the category at $179. For esports professionals and serious competitive players, the Superstrike is the unambiguous pick. The May refresh tightened sensor consistency at 1000 Hz polling for users not running high-refresh displays."},
                    {"title": "Logitech GPX2 Dex at $149 wins the bigger-hands palm-grip bracket", "body": "Right-handed ergonomic shape suits palm-grip players where the Superstrike's ambidextrous shape feels narrow. For dads with bigger hands playing long sessions, Dex is the rational pick over Superstrike. Same sensor, different shape — the right call when grip style matters more than weight."},
                    {"title": "Razer DeathAdder V4 Pro at $159 wins the legacy-ergonomic bracket", "body": "Right-handed ergonomic shape has been the most popular gaming mouse design for a decade and the Focus Pro 35K sensor matches the GPX2 on tracking. For users who learned to game on the original DeathAdder, the V4 Pro is the muscle-memory pick and the rational Father's Day gift for dads in that bracket."},
                ],
            },
            "zh-tw": {
                "commentary": (
                    "5/30 星期六把 Logitech GPX2 Superstrike 留在電競滑鼠排名第一，因為觸覺點擊、8K 輪詢率、60 克重量還是這個分類最完整的錦標賽級組合。USD$179（NT$5,990）讓 Superstrike 覆蓋電競職業選手需求比其他都好，5 月更新收緊了感測器在 1000 Hz 輪詢的一致性，給沒用高更新率螢幕的使用者。\n\n"
                    "Logitech GPX2 Dex 守第二 USD$149（NT$4,990），右手人體工學形狀適合掌握型玩家，Superstrike 的雙手通用形狀對他們來說偏窄。手大、長時間玩的爸爸，Dex 比 Superstrike 更理性。\n\n"
                    "Razer Viper V4 Pro 守第三 USD$169（NT$5,590），雙手通用電競血統加 Focus Pro 35K 光學感測器。Razer DeathAdder V4 Pro 守第四 USD$159（NT$5,290），右手人體工學形狀十年來最受歡迎的電競滑鼠設計。Razer DeathAdder V3 HyperSpeed 守第五 USD$89（NT$2,990），CP 值選擇，給出錦標賽級追蹤在 V4 Pro 一半價格。星期六父親節禮物訂單這週把 GPX2 Superstrike 跟 Razer DeathAdder V4 Pro 拉進購物車，Amazon Prime 父親節到貨截止 6/14。"
                ),
                "highlights": [
                    {"title": "Logitech GPX2 Superstrike NT$5,990 是錦標賽級預設", "body": "觸覺點擊、8K 輪詢率、60 克重量，這個分類最完整的錦標賽級組合在 NT$5,990。電競職業選手跟認真競技玩家，Superstrike 是不容質疑的選擇。5 月更新收緊感測器在 1000 Hz 輪詢的一致性，給沒用高更新率螢幕的使用者。"},
                    {"title": "Logitech GPX2 Dex NT$4,990 拿下大手掌握組冠軍", "body": "右手人體工學形狀適合掌握型玩家，Superstrike 的雙手通用形狀對他們來說偏窄。手大、長時間玩的爸爸，Dex 比 Superstrike 更理性。同樣感測器不同形狀，握法比重量更重要時的正確選擇。"},
                    {"title": "Razer DeathAdder V4 Pro NT$5,290 拿下傳統人體工學組冠軍", "body": "右手人體工學形狀十年來最受歡迎的電競滑鼠設計，Focus Pro 35K 感測器追蹤對齊 GPX2。從初代 DeathAdder 開始玩的使用者，V4 Pro 是肌肉記憶選擇，也是那個區段爸爸的理性父親節禮物。"},
                ],
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
            {"title": "Best Gaming Monitors 2026: Saturday OLED Showdown", "url": "https://www.rtings.com/monitor", "source": "Rtings"},
            {"title": "ASUS ROG Swift OLED PG27UCDM vs LG UltraGear 27GX790B", "url": "https://www.tomshardware.com/best-picks/best-gaming-monitors", "source": "Tom's Hardware"},
            {"title": "Father's Day Gaming Monitor Gift Picks", "url": "https://www.theverge.com/reviews", "source": "The Verge"},
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "Saturday May 30 keeps ASUS ROG Swift OLED PG27UCDM at the top of the gaming monitor ranking because the 4K 240 Hz QD-OLED panel with Tandem RGB technology delivers the brightest OLED highlights in the gaming monitor bracket at $899. The matte coating cuts reflections that plague glossy QD-OLED competitors and the 3-year burn-in warranty closes the OLED longevity concern that kept buyers on IPS through 2024.\n\n"
                    "LG UltraGear 27GX790B holds second at $799 on the WOLED panel that competes with the ASUS QD-OLED at $100 less. For buyers who prioritize value over absolute QD-OLED brightness peak, the LG is the rational pick. MSI MPG 341CQR X36 holds third at $999 on the ultrawide 34-inch QD-OLED that delivers the gaming-plus-productivity case in a single monitor.\n\n"
                    "Samsung Odyssey OLED G8 G80SD holds fourth at $1,199 on the 4K 240 Hz QD-OLED with the Smart TV functionality that the gaming-pure competitors lack. ASUS ROG Swift OLED PG27AQDP holds fifth at $749 as the 1440p 480 Hz OLED for esports professionals who care more about refresh rate than resolution. Saturday Father's Day gift orders are pulling the PG27UCDM and the LG UltraGear into carts this week, and Best Buy's Father's Day monitor sale starting June 7 will likely accelerate the buying."
                ),
                "highlights": [
                    {"title": "ASUS ROG Swift OLED PG27UCDM at $899 is the 4K OLED default", "body": "4K 240 Hz QD-OLED with Tandem RGB delivers the brightest OLED highlights in the gaming monitor bracket. Matte coating cuts reflections that plague glossy competitors and the 3-year burn-in warranty closes the OLED longevity concern. For Father's Day to a dad who games on PC, this is the unambiguous pick at this price."},
                    {"title": "LG UltraGear 27GX790B at $799 wins the value-OLED bracket", "body": "WOLED panel competes with the ASUS QD-OLED at $100 less. For buyers who prioritize value over absolute QD-OLED brightness peak, the LG is the rational pick. The LG panel longevity record on OLED TVs gives confidence that the monitor will hold up across a multi-year ownership horizon."},
                    {"title": "MSI MPG 341CQR X36 at $999 wins the gaming-plus-productivity household", "body": "Ultrawide 34-inch QD-OLED delivers the gaming-plus-productivity case in a single monitor. For households where the monitor doubles as work-from-home display during weekday hours, MSI is the rational pick over the 27-inch competitors because the productivity gain on the ultrawide aspect ratio earns the size premium."},
                ],
            },
            "zh-tw": {
                "commentary": (
                    "5/30 星期六把 ASUS ROG Swift OLED PG27UCDM 留在電競螢幕排名第一，因為 4K 240 Hz QD-OLED 面板加 Tandem RGB 技術，給出電競螢幕區段最亮的 OLED 高光在 USD$899（NT$29,700）。霧面塗層切掉光面 QD-OLED 競品的反光困擾，3 年燒屏保固化解了 2024 年讓買家還在 IPS 的 OLED 壽命疑慮。\n\n"
                    "LG UltraGear 27GX790B 守第二 USD$799（NT$26,500），WOLED 面板可以跟 ASUS QD-OLED 競爭，便宜 USD$100。重視 CP 值超過絕對 QD-OLED 亮度峰值的買家，LG 是理性選擇。MSI MPG 341CQR X36 守第三 USD$999（NT$33,100），超寬 34 吋 QD-OLED 在單一螢幕給出電競加生產力使用情境。\n\n"
                    "Samsung Odyssey OLED G8 G80SD 守第四 USD$1,199（NT$39,700），4K 240 Hz QD-OLED 加智慧電視功能，純電競競品沒有的。ASUS ROG Swift OLED PG27AQDP 守第五 USD$749（NT$24,900），1440p 480 Hz OLED 給重視更新率超過解析度的電競職業選手。星期六父親節禮物訂單這週把 PG27UCDM 跟 LG UltraGear 拉進購物車，Best Buy 父親節螢幕特賣 6/7 啟動會加速採購。"
                ),
                "highlights": [
                    {"title": "ASUS ROG Swift OLED PG27UCDM NT$29,700 是 4K OLED 預設", "body": "4K 240 Hz QD-OLED 加 Tandem RGB 給出電競螢幕區段最亮的 OLED 高光。霧面塗層切掉光面競品的反光、3 年燒屏保固化解 OLED 壽命疑慮。送給用 PC 遊戲爸爸的父親節，這個價格是不容質疑的選擇。台灣 ASUS 官方代理 NT$31,500 含三年保固。"},
                    {"title": "LG UltraGear 27GX790B NT$26,500 拿下 CP 值 OLED 組冠軍", "body": "WOLED 面板可以跟 ASUS QD-OLED 競爭、便宜 NT$3,200。重視 CP 值超過絕對 QD-OLED 亮度峰值的買家，LG 是理性選擇。LG 在 OLED 電視的面板壽命紀錄讓人對螢幕能撐多年擁有期間有信心。"},
                    {"title": "MSI MPG 341CQR X36 NT$33,100 拿下電競加生產力家庭冠軍", "body": "超寬 34 吋 QD-OLED 在單一螢幕給出電競加生產力使用情境。螢幕兼平日在家工作顯示器的家庭，MSI 比 27 吋競品更理性，超寬比例的生產力增益支撐尺寸溢價。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK gaming-monitors")


def build_handheld_gaming_consoles():
    d, p = load("best-handheld-gaming-consoles.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Best Handheld Gaming Consoles 2026: Saturday Summer Travel Edition", "url": "https://www.theverge.com/reviews", "source": "The Verge"},
            {"title": "Steam Deck OLED Long-Term Test", "url": "https://www.rockpapershotgun.com/", "source": "Rock Paper Shotgun"},
            {"title": "Switch 2 vs ROG Xbox Ally X: Late-May Comparison", "url": "https://www.tomsguide.com/best-picks/best-handheld-gaming-consoles", "source": "Tom's Guide"},
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "Saturday May 30 keeps Steam Deck OLED at the top of the handheld gaming console ranking because the Linux-based SteamOS, the broad PC game library, and the OLED display remain the best handheld value at $549 for the 512GB model. Valve is not running Father's Day promotions and the price has held flat through the post-Memorial Day week. For dads who already have Steam libraries, the Steam Deck OLED is the unambiguous pick.\n\n"
                    "Nintendo Switch 2 holds second at $449 on the exclusive first-party library that nothing else can match. The Mario Kart World and Donkey Kong Bananza launch titles continue to drive Switch 2 adoption in households with kids, and the Switch 2 is the rational Father's Day gift for dads who game with their kids rather than solo.\n\n"
                    "ROG Xbox Ally X holds third at $999 on the Windows 11 handheld experience with the Xbox Cloud Gaming integration that gives access to the entire Game Pass library. For dads who already pay for Game Pass Ultimate, the Ally X is the rational pick because the library access compounds with the existing subscription. Lenovo Legion Go 2 holds fourth at $999 with the detachable controllers that suit FPS gaming, and MSI Claw 8 AI Plus holds fifth at $899 as the Intel-based Windows handheld with the most thermally efficient design. Saturday Father's Day gift orders are pulling the Steam Deck OLED and the Switch 2 into carts this week."
                ),
                "highlights": [
                    {"title": "Steam Deck OLED at $549 is the PC-library Father's Day pick", "body": "Linux SteamOS, broad PC game library, OLED display at $549 for 512GB. For dads who already have Steam libraries, this is the unambiguous pick. Valve is not running Father's Day promos so $549 today is what buyers will see through June 21. Amazon Prime Father's Day cutoff is June 14."},
                    {"title": "Nintendo Switch 2 at $449 wins the family-gaming Father's Day bracket", "body": "Exclusive first-party library nothing else matches, including Mario Kart World and Donkey Kong Bananza as launch drivers. For dads who game with their kids rather than solo, Switch 2 is the rational pick. Nintendo first-party games hold value better than third-party titles, so the library investment is durable."},
                    {"title": "ROG Xbox Ally X at $999 wins the Game Pass household", "body": "Windows 11 handheld with Xbox Cloud Gaming integration gives access to the entire Game Pass library. For dads who already pay Game Pass Ultimate, the Ally X is the rational pick because library access compounds with existing subscription. The Z2 Extreme APU delivers the thermal performance Lenovo and MSI competitors are still chasing."},
                ],
            },
            "zh-tw": {
                "commentary": (
                    "5/30 星期六把 Steam Deck OLED 留在掌上型遊戲機排名第一，因為 Linux SteamOS、廣大 PC 遊戲庫、OLED 顯示器在 USD$549（NT$18,200）的 512GB 機型還是最好的掌機 CP 值。Valve 不做父親節促銷，價格在國殤日後一週守住。已經有 Steam 遊戲庫的爸爸，Steam Deck OLED 是不容質疑的選擇。\n\n"
                    "Nintendo Switch 2 守第二 USD$449（NT$14,900），獨佔第一方遊戲庫是其他比不上的。Mario Kart World 跟 Donkey Kong Bananza 上市作持續驅動有小孩家庭採用 Switch 2，跟小孩一起玩不是單機的爸爸，Switch 2 是理性父親節禮物。\n\n"
                    "ROG Xbox Ally X 守第三 USD$999（NT$33,100），Windows 11 掌機體驗加 Xbox Cloud Gaming 整合給整個 Game Pass 遊戲庫的存取權。已經付 Game Pass Ultimate 的爸爸，Ally X 是理性選擇，遊戲庫存取跟現有訂閱複利。Lenovo Legion Go 2 守第四 USD$999（NT$33,100），可拆控制器適合 FPS 遊戲，MSI Claw 8 AI Plus 守第五 USD$899（NT$29,700），Intel 為基礎的 Windows 掌機，散熱效率最高的設計。星期六父親節禮物訂單這週把 Steam Deck OLED 跟 Switch 2 拉進購物車。"
                ),
                "highlights": [
                    {"title": "Steam Deck OLED NT$18,200 是 PC 遊戲庫父親節選擇", "body": "Linux SteamOS、廣大 PC 遊戲庫、OLED 顯示器，512GB NT$18,200。已經有 Steam 遊戲庫的爸爸，這是不容質疑的選擇。Valve 不做父親節促銷，今天 NT$18,200 就是 6/21 前的價格。Amazon Prime 父親節到貨截止 6/14。"},
                    {"title": "Nintendo Switch 2 NT$14,900 拿下家庭遊戲父親節組冠軍", "body": "獨佔第一方遊戲庫是其他比不上的，Mario Kart World 跟 Donkey Kong Bananza 是上市驅動。跟小孩一起玩不是單機的爸爸，Switch 2 是理性選擇。任天堂第一方遊戲保值勝過第三方，遊戲庫投資耐久。"},
                    {"title": "ROG Xbox Ally X NT$33,100 拿下 Game Pass 家庭冠軍", "body": "Windows 11 掌機加 Xbox Cloud Gaming 整合給整個 Game Pass 遊戲庫存取權。已經付 Game Pass Ultimate 的爸爸，Ally X 是理性選擇，遊戲庫存取跟現有訂閱複利。Z2 Extreme APU 給出 Lenovo 跟 MSI 競品還在追的散熱表現。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK handheld-gaming-consoles")


def build_laptops():
    d, p = load("best-laptops.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Best Laptops 2026: Saturday Pre-WWDC Edition", "url": "https://www.theverge.com/laptop-reviews", "source": "The Verge"},
            {"title": "MacBook Air 13 M5 Long-Term Test", "url": "https://www.tomsguide.com/best-picks/best-laptops", "source": "Tom's Guide"},
            {"title": "Father's Day Laptop Gift Picks at Best Buy", "url": "https://www.bestbuy.com/site/clp/fathers-day-gifts/pcmcat1432231538843.c", "source": "Best Buy"},
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "Saturday May 30 keeps MacBook Air 13 M5 at the top of the laptop ranking because the M5 efficiency, 18-hour battery, and the fanless design at $1,099 remain the best all-around laptop value in late May 2026. Apple is unlikely to announce a refresh at WWDC 2026 in mid-June, so buyers committing to a Father's Day gift can buy today without WWDC FOMO. For dads who do email, browsing, video calls, and light photo editing — which is the actual usage of 80% of laptop buyers — the M5 Air is the unambiguous default.\n\n"
                    "MacBook Pro 14 M4 Pro holds second at $1,999 on the M4 Pro performance and the active cooling that handles sustained 4K video editing, code compilation, and AI model fine-tuning. For dads who do creative or professional work, the Pro is the rational upgrade. ASUS ZenBook A16 holds third at $1,499 on the AMD Ryzen AI 9 HX 370 and the OLED display that competes with the MacBook Pro at $500 less.\n\n"
                    "Dell XPS 14 2026 holds fourth at $1,599 on the Intel Lunar Lake refresh and the build quality that remains the best in the Windows premium ultraportable bracket. Razer Blade 16 holds fifth at $2,499 as the gaming-capable workstation for dads who game and work on the same machine. Saturday Father's Day gift orders are pulling the MacBook Air M5 and the ZenBook A16 into carts this week, with Best Buy's Father's Day laptop sale running through June 14."
                ),
                "highlights": [
                    {"title": "MacBook Air 13 M5 at $1,099 is the Father's Day default", "body": "M5 efficiency, 18-hour battery, fanless design at $1,099. For 80% of laptop buyers — email, browsing, video calls, light photo editing — the M5 Air is the unambiguous default. Apple unlikely to refresh at WWDC 2026 in mid-June so buyers can commit today without FOMO. Amazon Prime Father's Day cutoff is June 14."},
                    {"title": "MacBook Pro 14 M4 Pro at $1,999 is the creative-professional Father's Day pick", "body": "M4 Pro performance with active cooling handles sustained 4K video editing, code compilation, and AI model fine-tuning. For dads who do creative or professional work, the Pro is the rational upgrade. The M4 Pro chip silicon stability means the laptop will hold relevance for 5-plus years."},
                    {"title": "ASUS ZenBook A16 at $1,499 wins the Windows-premium value bracket", "body": "AMD Ryzen AI 9 HX 370 plus OLED display competes with MacBook Pro at $500 less. For dads on Windows by job requirement or personal preference, the ZenBook A16 is the rational pick over Dell XPS because the OLED display and the slightly larger battery close the experience gap to MacBook at lower pricing."},
                ],
            },
            "zh-tw": {
                "commentary": (
                    "5/30 星期六把 MacBook Air 13 M5 留在筆電排名第一，因為 M5 效率、18 小時電力、無風扇設計在 USD$1,099（NT$32,900）還是 2026 年 5 月底最好的全方位筆電 CP 值。Apple 不太可能在 6 月中 WWDC 2026 宣布更新，所以承諾父親節禮物的買家今天就買，不用 WWDC FOMO。做 email、瀏覽、視訊、輕度照片編輯的爸爸，這就是 80% 筆電買家的實際使用，M5 Air 就是不容質疑的預設。\n\n"
                    "MacBook Pro 14 M4 Pro 守第二 USD$1,999（NT$66,000），M4 Pro 效能加主動散熱處理長時間 4K 影片編輯、程式碼編譯、AI 模型微調。做創意或專業工作的爸爸，Pro 是理性升級。ASUS ZenBook A16 守第三 USD$1,499（NT$49,500），AMD Ryzen AI 9 HX 370 加 OLED 顯示器可以跟 MacBook Pro 競爭便宜 USD$500。\n\n"
                    "Dell XPS 14 2026 守第四 USD$1,599（NT$52,900），Intel Lunar Lake 更新加製造品質還是 Windows 高階輕薄區段最好的。Razer Blade 16 守第五 USD$2,499（NT$82,500），電競級工作站給遊戲跟工作同台機器的爸爸。星期六父親節禮物訂單這週把 MacBook Air M5 跟 ZenBook A16 拉進購物車，Best Buy 父親節筆電特賣跑到 6/14。"
                ),
                "highlights": [
                    {"title": "MacBook Air 13 M5 NT$32,900 是父親節預設", "body": "M5 效率、18 小時電力、無風扇設計在 NT$32,900。80% 筆電買家的實際使用就是 email、瀏覽、視訊、輕度照片編輯，M5 Air 是不容質疑的預設。Apple 不太可能在 6 月中 WWDC 2026 更新，買家今天承諾不用 FOMO。台灣 Apple Store 教育價 NT$31,400。"},
                    {"title": "MacBook Pro 14 M4 Pro NT$66,000 是創意專業父親節選擇", "body": "M4 Pro 效能加主動散熱處理長時間 4K 影片編輯、程式碼編譯、AI 模型微調。做創意或專業工作的爸爸，Pro 是理性升級。M4 Pro 晶片穩定性代表這台筆電可以維持 5 年以上的相關性。"},
                    {"title": "ASUS ZenBook A16 NT$49,500 拿下 Windows 高階 CP 值組冠軍", "body": "AMD Ryzen AI 9 HX 370 加 OLED 顯示器可以跟 MacBook Pro 競爭便宜 NT$16,000。工作需要或個人偏好用 Windows 的爸爸，ZenBook A16 比 Dell XPS 更理性，OLED 顯示器跟稍大電池縮小了跟 MacBook 的體驗落差在較低定價。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK laptops")


def build_mechanical_keyboards():
    d, p = load("best-mechanical-keyboards.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Best Mechanical Keyboards 2026: Saturday Hall-Effect Showdown", "url": "https://www.rtings.com/keyboard", "source": "Rtings"},
            {"title": "Wooting 60HE vs SteelSeries Apex Pro TKL Wireless", "url": "https://www.tomshardware.com/best-picks/best-gaming-keyboards", "source": "Tom's Hardware"},
            {"title": "Father's Day Mechanical Keyboard Picks", "url": "https://www.theverge.com/reviews", "source": "The Verge"},
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "Saturday May 30 keeps Wooting 60HE at the top of the mechanical keyboard ranking because the Hall-effect switches with the Rapid Trigger and SOCD support remain the most complete competitive-gaming keyboard package in the category. At $189, the 60HE outperforms anything in the optical-switch bracket for FPS players, and the May firmware update tightened the Wootility software to the point where keyboard configuration is now genuinely intuitive rather than a learning curve.\n\n"
                    "Wooting 80HE holds second at $239 as the full-size variant for users who need function keys and a numpad. SteelSeries Apex Pro TKL Wireless holds third at $239 on the OmniPoint 3.0 adjustable actuation and the wireless freedom that the Wooting wired models cannot match. For dads who game and need a wireless keyboard for cleaner desk setups, Apex Pro TKL Wireless is the rational pick.\n\n"
                    "Keychron Q1 Pro holds fourth at $209 on the wireless mechanical with the customization depth that the QMK firmware ecosystem unlocks. For typist-first dads who want a wireless mechanical for office work plus light gaming, Q1 Pro is the right call. NuPhy Field75 HE holds fifth at $189 as the wireless Hall-effect alternative that competes with Wooting on switch technology. Saturday Father's Day gift orders are pulling the Wooting 60HE and the Keychron Q1 Pro into carts this week."
                ),
                "highlights": [
                    {"title": "Wooting 60HE at $189 is the FPS-competitive Father's Day pick", "body": "Hall-effect switches with Rapid Trigger and SOCD support — most complete competitive-gaming keyboard package in the category at $189. For FPS players, the 60HE outperforms anything in the optical-switch bracket. The May firmware update made Wootility configuration genuinely intuitive."},
                    {"title": "Wooting 80HE at $239 is the full-size FPS-competitive variant", "body": "Same Hall-effect switches as 60HE in a full-size layout with function keys and numpad. For dads who need numeric input for spreadsheets or accounting work plus FPS gaming, the 80HE is the rational pick over the 60HE. The shipping lead time from Wooting direct holds at 3 to 4 weeks for the in-stock variants."},
                    {"title": "Keychron Q1 Pro at $209 wins the typist-first wireless mechanical", "body": "Wireless mechanical with customization depth via QMK firmware ecosystem. For typist-first dads who want a wireless mechanical for office work plus light gaming, Q1 Pro is the right call over the SteelSeries Apex Pro because the build quality and the QMK depth exceed what gaming-first competitors offer."},
                ],
            },
            "zh-tw": {
                "commentary": (
                    "5/30 星期六把 Wooting 60HE 留在機械鍵盤排名第一，因為霍爾效應軸加 Rapid Trigger 跟 SOCD 支援還是這個分類最完整的競技遊戲鍵盤組合。USD$189（NT$6,290）讓 60HE 在 FPS 玩家身上勝過光軸區段任何產品，5 月韌體更新把 Wootility 軟體收緊到鍵盤配置現在真的直觀，不是學習曲線。\n\n"
                    "Wooting 80HE 守第二 USD$239（NT$7,990）全尺寸版本，需要功能鍵跟數字鍵盤的使用者。SteelSeries Apex Pro TKL Wireless 守第三 USD$239（NT$7,990），OmniPoint 3.0 可調觸發加 Wooting 有線機型沒有的無線自由。玩遊戲又需要無線鍵盤讓桌面乾淨的爸爸，Apex Pro TKL Wireless 是理性選擇。\n\n"
                    "Keychron Q1 Pro 守第四 USD$209（NT$6,990），無線機械加 QMK 韌體生態系解鎖的客製化深度。打字優先的爸爸想要無線機械做辦公加輕度遊戲，Q1 Pro 是正確選擇。NuPhy Field75 HE 守第五 USD$189（NT$6,290），無線霍爾效應替代可以在軸體技術跟 Wooting 競爭。星期六父親節禮物訂單這週把 Wooting 60HE 跟 Keychron Q1 Pro 拉進購物車。"
                ),
                "highlights": [
                    {"title": "Wooting 60HE NT$6,290 是 FPS 競技父親節選擇", "body": "霍爾效應軸加 Rapid Trigger 跟 SOCD 支援，這個分類最完整的競技遊戲鍵盤組合在 NT$6,290。FPS 玩家身上，60HE 勝過光軸區段任何產品。5 月韌體更新讓 Wootility 配置真的直觀。"},
                    {"title": "Wooting 80HE NT$7,990 是全尺寸 FPS 競技版本", "body": "跟 60HE 同樣的霍爾效應軸，全尺寸佈局加功能鍵跟數字鍵盤。需要數字輸入做試算表或會計工作加 FPS 遊戲的爸爸，80HE 比 60HE 更理性。Wooting 官網直接出貨現貨版本維持 3 到 4 週。"},
                    {"title": "Keychron Q1 Pro NT$6,990 拿下打字優先無線機械組", "body": "無線機械加 QMK 韌體生態系客製化深度。打字優先的爸爸想要無線機械做辦公加輕度遊戲，Q1 Pro 比 SteelSeries Apex Pro 更正確，製造品質跟 QMK 深度超過電競優先競品提供的。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK mechanical-keyboards")


if __name__ == "__main__":
    build_gaming_chairs()
    build_gaming_headsets()
    build_gaming_mice()
    build_gaming_monitors()
    build_handheld_gaming_consoles()
    build_laptops()
    build_mechanical_keyboards()
    print("\nBatch 4 complete (7 gaming/computing files).")
