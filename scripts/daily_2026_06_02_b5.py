"""2026-06-02 daily update — Batch 5: Gaming/Computing peripherals & devices (7 files)"""
import copy
import json
from pathlib import Path

DATE = "2026-06-02"
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
            {"title": "Secretlab Titan Evo NanoGen Review: The Next Generation", "url": "https://www.tomshardware.com/peripherals/gaming-chairs/secretlab-titan-evo-nanogen-review", "source": "Tom's Hardware"},
            {"title": "Best gaming chair: top seats that we've tested, and expert buying advice", "url": "https://www.techradar.com/gaming/best-gaming-chairs", "source": "TechRadar"},
            {"title": "Secretlab expands 2026 lineup with chairs for every gamer", "url": "https://www.msn.com/en-us/news/insight/secretlab-expands-2026-lineup-with-chairs-for-every-gamer/gm-GMD62F61CF", "source": "MSN"},
        ],
        "i18n": {
            "en": {
                "commentary": "The Secretlab Titan Evo stays at the top of this list, and the launch of the new Titan Evo NanoGen Edition only reinforces why Secretlab owns this category. The NanoGen layers in a new hybrid leatherette that Secretlab rates at 14x the durability of standard PU leather, plus a NanoFoam composite that is the most supportive foam they have shipped. At $799.99 it sits above the standard Titan Evo, but the regular Titan Evo at roughly $549 is still the chair I point most people toward. Its two-knob internal lumbar system, adjustable for both height and firmness, remains the single best built-in back support in any gaming chair, and the 9.5 build score reflects how well these chairs hold up over years of daily use.\n\nThe Herman Miller x Logitech G Vantum holds rank 2 as the premium ergonomic answer. The adaptive plates that support your lumbar and upper back, paired with a 12-year warranty, make this the chair for people who treat seating as a long-term health investment rather than a gaming accessory. It costs considerably more, and the value score of the category leaders reflects that, but the ergonomic pedigree is real.\n\nThe Libernovo Omni at rank 3 continues to impress as the dynamic-ergonomics pick, and the Razer Iskur V2 at rank 4 remains the strongest choice for players who want lumbar support baked into the frame rather than added as a pillow. With Father's Day on June 21 driving gift searches, gaming chairs are moving fast right now. The standard Titan Evo at its current price is the safest recommendation I can give, and Secretlab's expanded 2026 lineup means there is now a Titan variant for nearly every body type and budget.",
                "highlights": [
                    {"title": "Secretlab Titan Evo Is Still the Default Recommendation", "body": "The standard Titan Evo at around $549 delivers the best built-in lumbar system in any gaming chair, with a two-knob adjustment for height and firmness. Its 9.5 build score reflects construction that survives years of daily use, which is why it stays at rank 1."},
                    {"title": "NanoGen Edition Raises the Premium Ceiling", "body": "The new Titan Evo NanoGen at $799.99 adds hybrid leatherette rated at 14x the durability of standard PU and Secretlab's most supportive NanoFoam composite. It is the flagship that shows where Secretlab is pushing the category, even if the standard Evo remains the value pick."},
                    {"title": "Herman Miller Vantum Owns the Ergonomic Tier", "body": "The Herman Miller x Logitech G Vantum at rank 2 pairs adaptive lumbar and upper-back plates with a 12-year warranty. For buyers treating seating as a long-term health decision, this is the chair worth the premium."},
                ],
            },
            "zh-tw": {
                "commentary": "Secretlab Titan Evo 繼續穩坐這份榜單第一，新款 Titan Evo NanoGen 的上市更是把這個地位坐得更穩。NanoGen 用上了全新的混合皮革，Secretlab 標榜耐用度是一般 PU 皮的 14 倍，再加上他們有史以來最支撐的 NanoFoam 複合泡棉。NanoGen 售價 $799.99，比標準款貴一截，但老實說，標準版 Titan Evo（約 $549，台幣兩萬出頭）才是我最常推薦的那一張。它的雙旋鈕內建腰靠可以同時調高度和軟硬度，這套系統到現在還是所有電競椅裡最好的內建腰部支撐，做工 9.5 分也說明這張椅子天天坐好幾年都不會垮。\n\nHerman Miller x Logitech G Vantum 排第二，是高階人體工學的答案。自適應支撐板會貼合你的腰部和上背，再配上 12 年保固，這張椅子適合把坐姿當成長期健康投資的人，不只是電競配件。價格確實貴不少，但人體工學的底子是真材實料。\n\nLibernovo Omni 第三名，動態人體工學的表現依然亮眼；Razer Iskur V2 第四，腰靠直接做進椅背而不是外掛一顆枕頭，喜歡這種設計的人選它就對了。父親節（6/21）快到了，電競椅的搜尋量正在往上衝，標準版 Titan Evo 以現在的價格是我能給的最穩推薦。Secretlab 2026 產品線變得更齊全，幾乎每種體型和預算都能找到對應的 Titan 款式。",
                "highlights": [
                    {"title": "Secretlab Titan Evo 仍是最穩的預設推薦", "body": "標準版 Titan Evo 約 $549（台幣兩萬出頭），雙旋鈕內建腰靠可同時調高度和軟硬度，是電競椅裡最好的內建腰部支撐。做工 9.5 分，天天坐好幾年都不垮，第一名實至名歸。"},
                    {"title": "NanoGen 版把高階天花板拉高", "body": "新款 Titan Evo NanoGen 售價 $799.99，混合皮革耐用度標榜是一般 PU 的 14 倍，搭配 Secretlab 最支撐的 NanoFoam 泡棉。這是展示品牌方向的旗艦款，但標準版 Evo 仍是 CP 值首選。"},
                    {"title": "Herman Miller Vantum 穩坐人體工學頂級", "body": "Herman Miller x Logitech G Vantum 排第二，自適應腰部與上背支撐板加上 12 年保固。把坐姿當長期健康投資的人，這張椅子值得那個價差。"},
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
            {"title": "SteelSeries Unveils Arctis Nova Pro Omni with Hi-Res Wireless and OmniPlay", "url": "https://hothardware.com/news/steelseries-unveils-arctis-nova-pro-omni", "source": "HotHardware"},
            {"title": "I tested Reddit's favorite gaming headsets and there's a clear winner", "url": "https://www.tomsguide.com/gaming/gaming-peripherals/i-tested-reddits-favorite-high-end-gaming-headsets-and-theres-a-clear-winner-but-its-not-the-one-i-expected", "source": "Tom's Guide"},
            {"title": "SteelSeries Arctis Nova Pro Omni Launches at $399: Hi-Res Audio Without the Premium Price Tag", "url": "https://finance.biggo.com/news/202605061224_SteelSeries_Arctis_Nova_Pro_Omni_399_USD_launch", "source": "BigGo Finance"},
        ],
        "i18n": {
            "en": {
                "commentary": "The SteelSeries Arctis Nova Pro Wireless holds the top spot, and SteelSeries just made the case for itself even stronger. The brand's 25th-anniversary release, the Arctis Nova Pro Omni, launched May 5 at $399.99 with Hi-Res Wireless certification, 96kHz/24-bit audio, and OmniPlay multi-device mixing that connects up to five devices and mixes four audio sources at once. The dual-battery hot-swap system means you never stop to charge. It is the natural successor to the Nova Pro Wireless that already sits at rank 1, and it confirms SteelSeries owns the all-rounder crown in 2026.\n\nThe Audeze Maxwell 2 at rank 2 is the audiophile answer, and it earns it. In head-to-head testing it came out ahead of the field on raw sound quality, and its 80-hour battery life genuinely outlasts everything else in the category. At $299 it costs roughly half what some flagship rivals ask while delivering comparable or better audio. If your priority is the best sound regardless of feature count, this is the headset.\n\nThe Turtle Beach Stealth Pro II at rank 3 remains the most complete console-focused wireless option, and the Logitech G Pro X 2 Lightspeed at rank 4 stays the esports staple for players who want proven reliability and a light, comfortable fit for long sessions. The 9.5 feature-set and 9.5 connectivity scores on the Nova Pro Wireless are the reason it holds the lead: it does everything well, with a swappable-battery base station that no competitor matches at its price. With Father's Day approaching, premium headsets are a top gift category, and the Nova Pro family is the safest pick for buyers who want audio that works across PC, PlayStation, and Xbox without compromise.",
                "highlights": [
                    {"title": "Arctis Nova Pro Wireless Stays the Best All-Rounder", "body": "With a 9.5 feature-set and 9.5 connectivity score, the Nova Pro Wireless does everything well, anchored by a swappable-battery base station that no rival matches at the price. It holds rank 1 heading into summer 2026."},
                    {"title": "SteelSeries Nova Pro Omni Extends the Lead", "body": "The 25th-anniversary Arctis Nova Pro Omni launched May 5 at $399.99 with Hi-Res Wireless, 96kHz/24-bit audio, and OmniPlay mixing across five devices. Its dual-battery hot-swap design means uninterrupted play, confirming SteelSeries owns the all-rounder tier."},
                    {"title": "Audeze Maxwell 2 Wins on Pure Sound", "body": "At rank 2, the Maxwell 2 led head-to-head sound-quality testing and delivers 80 hours of battery, the longest in the category. At $299 it costs about half of some flagship rivals while matching or beating them on audio."},
                ],
            },
            "zh-tw": {
                "commentary": "SteelSeries Arctis Nova Pro Wireless 繼續坐穩第一，而 SteelSeries 最近把自己的理由講得更硬了。品牌 25 週年推出的 Arctis Nova Pro Omni 在 5/5 上市，售價 $399.99，拿到 Hi-Res 無線認證、96kHz/24-bit 音質，還有 OmniPlay 多裝置混音，可以同時連五台裝置、混四個音源。雙電池熱插拔設計讓你完全不用停下來充電。這台是榜首 Nova Pro Wireless 的自然接班人，等於再次確認 SteelSeries 在 2026 年握有全能王的位子。\n\nAudeze Maxwell 2 排第二，是發燒友的答案，而且當之無愧。在直接對比測試裡，它的純音質贏過一票對手，80 小時的續航也是同類產品裡真的撐最久的。售價 $299，大約是某些旗艦對手的一半，音質卻不輸甚至更好。如果你只在乎聲音夠不夠頂、不太管功能多不多，這支耳機就是答案。\n\nTurtle Beach Stealth Pro II 第三，是主機向最完整的無線選擇；Logitech G Pro X 2 Lightspeed 第四，電競老將，輕量又舒適，長時間戴不累，要穩定可靠就選它。Nova Pro Wireless 功能 9.5、連線 9.5，這就是它領先的原因，可換電池基座在這個價位沒有對手。父親節快到了，高階耳機是熱門禮物，想要一支橫跨 PC、PS、Xbox 都不妥協的，Nova Pro 家族是最穩的選擇。",
                "highlights": [
                    {"title": "Arctis Nova Pro Wireless 仍是最強全能王", "body": "功能 9.5、連線 9.5，Nova Pro Wireless 樣樣都做得好，核心是可換電池基座，這個價位沒有對手能比。進入 2026 夏季穩坐第一。"},
                    {"title": "SteelSeries Nova Pro Omni 把領先拉得更開", "body": "25 週年款 Arctis Nova Pro Omni 在 5/5 上市，售價 $399.99，配 Hi-Res 無線、96kHz/24-bit 音質、可同時連五台的 OmniPlay 混音。雙電池熱插拔讓遊戲不中斷，再次確認 SteelSeries 的全能地位。"},
                    {"title": "Audeze Maxwell 2 純音質取勝", "body": "排第二，Maxwell 2 在直接對比測試裡音質領先，續航 80 小時是同類最長。售價 $299，約是某些旗艦對手的一半，聲音卻不輸甚至更好。"},
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
            {"title": "Logitech Superstrike vs Razer Viper V4 Pro: The battle for the competitive crown", "url": "https://www.pcgamer.com/hardware/gaming-mice/logitech-superstrike-vs-razer-viper-v4-pro-the-battle-for-the-competitive-crown/", "source": "PC Gamer"},
            {"title": "Razer Viper V4 Pro review: superior to the Logitech G Pro X2 Superstrike in almost every way", "url": "https://www.theshortcut.com/p/razer-viper-v4-pro-review", "source": "The Shortcut"},
            {"title": "The Best Wireless Gaming Mouse of 2026: Mice Reviews", "url": "https://www.rtings.com/mouse/reviews/best/wireless-gaming", "source": "RTINGS.com"},
        ],
        "i18n": {
            "en": {
                "commentary": "The Logitech G Pro X2 Superstrike holds rank 1, and the reason is a genuine first in the category: it is the first gaming mouse with proper analog switches under the main buttons. That means clicks respond to the slightest touch, or to whatever actuation force you dial in, and for tactical-shooter players it shaves real time off the gap between starting to press and the in-game weapon firing. With a 9.8 latency score and 9.5 sensor score, it is the sharpest competitive tool on this list for players who want that edge and are happy paying around $180 for it.\n\nThat said, the Razer Viper V4 Pro at rank 2 is the mouse I steer most people toward, and the head-to-head reviews back that up. It weighs roughly 20% less than the Superstrike, its sensor is excellent, and battery life is in another league: around 180 hours at 1000Hz versus the Superstrike's 90 hours, which drops closer to 30 once you enable analog Rapid Trigger features. The buttons are tactile with near-zero pre-travel and the skates glide cleanly. For the vast majority of players, the Viper V4 Pro is the more practical flagship.\n\nThe Razer DeathAdder V4 Pro at rank 4 stays the top ergonomic-shape pick for palm-grip players, and the Pulsar X2 and Lamzu Maya X further down the list continue to give enthusiast buyers lightweight, high-value alternatives. The takeaway for summer 2026 is simple: if you grind tactical shooters and want the absolute lowest click latency, the Superstrike's analog switches justify rank 1. For everyone else, the Viper V4 Pro's weight, battery, and feel make it the smarter buy.",
                "highlights": [
                    {"title": "Superstrike's Analog Switches Are a Category First", "body": "The Logitech G Pro X2 Superstrike is the first gaming mouse with proper analog switches under the main buttons, letting clicks respond to the slightest touch or a custom actuation force. With a 9.8 latency score, it is the sharpest tool for tactical-shooter players, holding rank 1."},
                    {"title": "Viper V4 Pro Is the Smarter Buy for Most", "body": "At rank 2, the Razer Viper V4 Pro weighs about 20% less than the Superstrike and lasts roughly 180 hours at 1000Hz versus 90. With a top sensor and near-zero pre-travel buttons, it is the more practical flagship for the majority of players."},
                    {"title": "Battery Life Separates the Two Flagships", "body": "The Viper V4 Pro's 180-hour battery dwarfs the Superstrike's 90 hours, which can drop to around 30 hours once analog Rapid Trigger is active. For players who hate charging, that gap alone settles the decision."},
                ],
            },
            "zh-tw": {
                "commentary": "Logitech G Pro X2 Superstrike 坐穩第一，理由是品類裡真正的首創：它是第一支主按鍵採用類比微動的滑鼠。意思是點擊可以對最輕微的觸碰反應，或者你自己設定觸發力道，對打戰術射擊的玩家來說，這實際縮短了從開始按到遊戲裡開火之間的時間。延遲 9.8 分、感測器 9.5 分，是這份榜單上最銳利的競技工具，想要那點優勢、又願意花約 $180（台幣五千多）的人，它就是答案。\n\n話說回來，第二名的 Razer Viper V4 Pro 才是我最常推給一般人的那支，直接對比的評測也是這個結論。它比 Superstrike 輕大約 20%，感測器一樣頂，而續航根本是另一個檔次：1000Hz 下約 180 小時，Superstrike 只有 90 小時，開了類比 Rapid Trigger 之後更掉到接近 30 小時。按鍵紮實、預行程接近零，腳貼滑得很順。對絕大多數玩家來說，Viper V4 Pro 是更實際的旗艦。\n\nRazer DeathAdder V4 Pro 第四，趴握玩家的人體工學首選；榜單後段的 Pulsar X2、Lamzu Maya X 也持續給玩家輕量又划算的選擇。2026 夏天的結論很簡單：如果你每天泡在戰術射擊、要最低點擊延遲，Superstrike 的類比微動撐得起第一名。其他人，Viper V4 Pro 的重量、續航和手感讓它成為更聰明的選擇。",
                "highlights": [
                    {"title": "Superstrike 類比微動是品類首創", "body": "Logitech G Pro X2 Superstrike 是第一支主按鍵採類比微動的滑鼠，點擊能對最輕觸碰反應或自訂觸發力道。延遲 9.8 分，是戰術射擊玩家最銳利的工具，穩坐第一。"},
                    {"title": "Viper V4 Pro 對多數人是更聰明的選擇", "body": "排第二，Razer Viper V4 Pro 比 Superstrike 輕約 20%，1000Hz 下續航約 180 小時對上 90 小時。頂級感測器加上接近零預行程的按鍵，對多數玩家是更實際的旗艦。"},
                    {"title": "續航是兩支旗艦的分水嶺", "body": "Viper V4 Pro 的 180 小時電力遠勝 Superstrike 的 90 小時，後者開啟類比 Rapid Trigger 後甚至掉到約 30 小時。討厭充電的人，光這一點就能拍板。"},
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
            {"title": "Asus ROG Swift PG27UCDM 4K 240 Hz QD-OLED gaming monitor review: High-end in every way", "url": "https://www.tomshardware.com/monitors/gaming-monitors/asus-rog-swift-pg27ucdm-4k-240-hz-qd-oled-gaming-monitor-review", "source": "Tom's Hardware"},
            {"title": "ASUS ROG Swift OLED PG27UCDM Monitor Review", "url": "https://www.rtings.com/monitor/reviews/asus/rog-swift-oled-pg27ucdm", "source": "RTINGS.com"},
            {"title": "ASUS Republic of Gamers Announces Next-Gen RGB OLED Technology at CES 2026", "url": "https://press.asus.com/news/press-releases/rog-rgb-oled-ces-2026/", "source": "ASUS Pressroom"},
        ],
        "i18n": {
            "en": {
                "commentary": "The ASUS ROG Swift OLED PG27UCDM holds rank 1 with a 9.5 overall, and it has earned the position by being a genuine flagship in every dimension. It is the first 27-inch 4K OLED gaming monitor to pair that resolution with a 240Hz refresh rate, and at 166ppi the text clarity and image sharpness are a clear step beyond previous-generation panels. The 0.03ms response time, fourth-gen QD-OLED panel, and DisplayPort 2.1a UHBR20 with up to 80Gbps of uncompressed bandwidth make it as future-proof as a display gets in 2026. Its 9.8 image-quality and 9.7 HDR scores are the highest on this list, which is exactly why it leads.\n\nWhat makes this monitor a smart long-term buy is the ROG OLED Care Pro suite. The new Neo Proximity Sensor drops the panel to a black screen when no user is detected, which directly addresses the burn-in anxiety that has held some buyers back from OLED. At around $1,200 it is not cheap, but for 4K gaming at high refresh it is the definitive choice.\n\nThe LG UltraGear 27GX790B at rank 2 remains the answer for players who prioritize raw speed, and the MSI MPG 341CQR-X36 at rank 3 stays the pick for ultrawide immersion. Looking ahead, ASUS used CES 2026 to announce next-gen RGB OLED technology, which signals even brighter, more color-accurate panels are coming. For now, though, the PG27UCDM is the best 4K OLED gaming monitor you can buy, and nothing on the market dethrones it heading into summer.",
                "highlights": [
                    {"title": "PG27UCDM Leads on Image Quality and HDR", "body": "With a 9.8 image-quality and 9.7 HDR score, the ASUS ROG Swift OLED PG27UCDM is the first 27-inch 4K OLED to hit 240Hz. At 166ppi with 0.03ms response, it is the sharpest, fastest 4K OLED on this list, holding rank 1."},
                    {"title": "Neo Proximity Sensor Tackles Burn-In Anxiety", "body": "The ROG OLED Care Pro suite adds a Neo Proximity Sensor that blacks out the panel when no user is detected. For buyers hesitant about OLED longevity, this directly addresses the biggest concern and makes the PG27UCDM a confident long-term purchase."},
                    {"title": "DisplayPort 2.1a Makes It Future-Proof", "body": "Four-lane DisplayPort 2.1a UHBR20 delivers up to 80Gbps of uncompressed bandwidth, ensuring the PG27UCDM can drive 4K at 240Hz without compression. Paired with a fourth-gen QD-OLED panel, it is as future-proof as displays get in 2026."},
                ],
            },
            "zh-tw": {
                "commentary": "ASUS ROG Swift OLED PG27UCDM 以 9.5 總分坐穩第一，它能站在這個位置，是因為每個面向都是貨真價實的旗艦。它是第一台把 4K 解析度和 240Hz 刷新率結合的 27 吋 OLED 電競螢幕，166ppi 的文字清晰度和畫面銳利度，明顯比上一代面板更上一層。0.03ms 反應時間、第四代 QD-OLED 面板、DisplayPort 2.1a UHBR20 提供最高 80Gbps 的無壓縮頻寬，在 2026 年是最不怕過時的顯示器。畫質 9.8、HDR 9.7 都是全榜最高，這就是它領先的原因。\n\n讓這台螢幕成為聰明長期投資的，是 ROG OLED Care Pro 套件。新的 Neo 接近感測器會在偵測不到使用者時把面板切成全黑，直接化解了一些人對 OLED 燒屏的焦慮。售價約 $1,200（台幣三萬多）不算便宜，但要在 4K 高刷下打遊戲，它就是那個答案。\n\nLG UltraGear 27GX790B 第二，純速度取向的玩家選它；MSI MPG 341CQR-X36 第三，要超寬螢幕沉浸感就看它。展望未來，ASUS 在 CES 2026 發表了次世代 RGB OLED 技術，預告更亮、色彩更準的面板即將登場。不過就現在來說，PG27UCDM 是你買得到最好的 4K OLED 電競螢幕，進入夏天沒有對手能把它拉下來。",
                "highlights": [
                    {"title": "PG27UCDM 畫質與 HDR 雙料領先", "body": "畫質 9.8、HDR 9.7，ASUS ROG Swift OLED PG27UCDM 是第一台 240Hz 的 27 吋 4K OLED。166ppi 加 0.03ms 反應，是全榜最銳利、最快的 4K OLED，穩坐第一。"},
                    {"title": "Neo 接近感測器化解燒屏焦慮", "body": "ROG OLED Care Pro 套件加入 Neo 接近感測器，偵測不到使用者就把面板切黑。對擔心 OLED 壽命的人，這直接解決了最大顧慮，讓 PG27UCDM 成為可以放心的長期投資。"},
                    {"title": "DisplayPort 2.1a 讓它不怕過時", "body": "四通道 DisplayPort 2.1a UHBR20 提供最高 80Gbps 無壓縮頻寬，確保 PG27UCDM 能無壓縮推動 4K 240Hz。配上第四代 QD-OLED 面板，是 2026 年最不怕過時的顯示器。"},
                ],
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
            {"title": "Wooting 60HE+ | the 60% rapid trigger keyboard", "url": "https://wooting.io/wooting-60he", "source": "Wooting"},
            {"title": "Best Hall Effect Keyboards for Gaming (2026): 7 Rapid Trigger Picks", "url": "https://gamerhardware.org/best-hall-effect-keyboard/", "source": "Gamer Hardware"},
            {"title": "Wooting Keyboards Review 2026: Every Model Tested & Compared", "url": "https://gamingpcguru.com/wooting-keyboards-review/", "source": "Gaming PC Guru"},
        ],
        "i18n": {
            "en": {
                "commentary": "The Wooting 60HE holds rank 1, and the arrival of the 60HE v2 only strengthens the case for Wooting's dominance of competitive gaming keyboards. The original 60HE earned its reputation on pioneering rapid trigger firmware that the community keeps refining, delivering the fastest, most precise key response on the market, which is exactly what the 9.8 latency and 9.8 switch scores reflect. The v2 is a ground-up redesign: new closed-bottom Lekker Tikken Hall Effect switches give a full 4mm travel with a more tactile, satisfying keystroke, an aluminum case is now standard where the original shipped in plastic, and 8KHz Tachyon Mode polling jumps up from the 1KHz of the original 60HE+. Plastic-case versions began shipping in April 2026, so the v2 is now widely available.\n\nThe Wooting 80HE at rank 2 stays the pick for players who want rapid trigger in a more complete layout with arrow keys and a function row, and many reviewers still call it the single safest gaming keyboard recommendation for most people. The SteelSeries Apex Pro TKL Wireless at rank 3 remains the strongest mainstream-brand Hall Effect option for buyers who want wireless and OmniPoint adjustability from a household name.\n\nFurther down, the Keychron Q1 Pro at rank 4 stays the enthusiast custom-feel pick, and the NuPhy Field75 HE at rank 5 continues to blend Hall Effect performance with a more playful design language. The throughline for summer 2026 is that Hall Effect and rapid trigger are now the default expectation for competitive boards, and Wooting still sets the standard. If you play ranked FPS, the 60HE remains the keyboard to beat, and the v2 refresh keeps it firmly at the front.",
                "highlights": [
                    {"title": "Wooting 60HE Stays the Competitive Standard", "body": "With 9.8 latency and 9.8 switch scores, the Wooting 60HE delivers the fastest, most precise rapid trigger response on the market, refined continuously by its community. It remains the keyboard to beat for ranked FPS, holding rank 1."},
                    {"title": "60HE v2 Is a Ground-Up Redesign", "body": "The v2 adds closed-bottom Lekker Tikken switches with a full 4mm tactile travel, a standard aluminum case, and 8KHz Tachyon Mode polling up from 1KHz. Plastic-case versions began shipping in April 2026, making the refreshed board widely available."},
                    {"title": "Wooting 80HE Is the Safest All-Round Pick", "body": "At rank 2, the Wooting 80HE brings rapid trigger to a fuller layout with arrow keys and a function row. Many reviewers still call it the single safest gaming keyboard recommendation for most players."},
                ],
            },
            "zh-tw": {
                "commentary": "Wooting 60HE 坐穩第一，而 60HE v2 的登場更是把 Wooting 在競技鍵盤的主導地位坐得更穩。初代 60HE 靠著開創性的 rapid trigger 韌體建立名聲，社群還持續精進，給出市場上最快、最精準的按鍵反應，這正是延遲 9.8、軸體 9.8 分所反映的。v2 是從頭重新設計：新的封底 Lekker Tikken 霍爾軸給你完整 4mm 行程，敲擊更有段落感也更扎實，鋁合金外殼現在是標配，初代用的是塑膠，8KHz Tachyon 模式回報率也從初代 60HE+ 的 1KHz 大幅提升。塑膠殼版本 4 月開始出貨，所以 v2 現在已經買得到了。\n\nWooting 80HE 排第二，想要 rapid trigger 又要方向鍵和功能列的人選它，很多評測還是把它當成最穩的大眾首選。SteelSeries Apex Pro TKL Wireless 第三，想要大廠牌、無線又有 OmniPoint 可調行程的人，這是最強的主流選擇。\n\n再往下，Keychron Q1 Pro 第四，玩家向客製手感的代表；NuPhy Field75 HE 第五，把霍爾軸效能和更活潑的設計語言結合得很好。2026 夏天的主軸是，霍爾軸和 rapid trigger 現在已經是競技鍵盤的預設標配，而 Wooting 仍然在定標準。打排位 FPS 的話，60HE 還是那把要被超越的標竿，v2 改款讓它穩穩待在最前面。",
                "highlights": [
                    {"title": "Wooting 60HE 仍是競技標準", "body": "延遲 9.8、軸體 9.8，Wooting 60HE 給出市場上最快、最精準的 rapid trigger 反應，社群持續精進。打排位 FPS 它還是那把要被超越的標竿，穩坐第一。"},
                    {"title": "60HE v2 從頭重新設計", "body": "v2 加入封底 Lekker Tikken 軸，完整 4mm 段落行程，鋁合金外殼變標配，8KHz Tachyon 回報率從 1KHz 大幅提升。塑膠殼版本 4 月開始出貨，改款已經買得到。"},
                    {"title": "Wooting 80HE 是最穩的全能首選", "body": "排第二，Wooting 80HE 把 rapid trigger 帶進有方向鍵和功能列的完整配列。很多評測還是把它當成最穩的大眾遊戲鍵盤推薦。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK mechanical-keyboards")


def build_handheld_consoles():
    d, p = load("best-handheld-gaming-consoles.json")
    # MAJOR MARKET EVENT: Valve raised Steam Deck OLED prices on 2026-05-27
    # (512GB $549 -> $789, 1TB $649 -> $949). Steam Deck OLED held #1 largely on
    # its 9.5 value score; that score no longer holds. Switch 2 (unaffected, 9.2)
    # moves to #1. Steam Deck OLED drops to #2 with value adjusted down.
    rankings = copy.deepcopy(last_rankings(d))
    by_id = {r["id"]: r for r in rankings}
    sd = by_id["steam-deck-oled"]
    sw = by_id["nintendo-switch-2"]
    # Adjust Steam Deck OLED value down for the ~44% price hike and recompute.
    sd["scores"]["value"] = 8.3
    sd["score"] = 9.0
    sd["rank"] = 2
    sw["rank"] = 1
    # Reorder list and renumber the rest by their existing relative order.
    rankings.sort(key=lambda r: (0 if r["id"] == "nintendo-switch-2" else
                                 1 if r["id"] == "steam-deck-oled" else 2,
                                 r["rank"]))
    for i, r in enumerate(rankings, start=1):
        r["rank"] = i
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Valve hikes Steam Deck OLED prices — 512GB is now $789, while 1TB climbs to $949", "url": "https://www.tomshardware.com/video-games/handheld-gaming/valve-hikes-steam-deck-oled-prices-512gb-is-now-usd789-while-1tb-climbs-to-usd949", "source": "Tom's Hardware"},
            {"title": "Valve jacks up Steam Deck prices by as much as $300", "url": "https://www.engadget.com/2182286/valve-jacks-up-steam-deck-prices-by-as-much-as-300/", "source": "Engadget"},
            {"title": "Best gaming handhelds 2026 ranked: Steam Deck, Xbox Ally X, Switch 2, Legion Go 2, MSI Claw 8 AI+, and more", "url": "https://www.windowscentral.com/gaming-best-gaming-handhelds", "source": "Windows Central"},
        ],
        "i18n": {
            "en": {
                "commentary": "A genuine market event reshuffles the top of this list. On May 27, Valve raised Steam Deck OLED prices significantly, the 512GB model jumping from $549 to $789 and the 1TB from $649 to $949, citing the RAM and NAND flash shortage driven by AI data-center demand. The Steam Deck OLED held the top spot largely on an unbeatable value score, and at nearly 44% more expensive that argument no longer holds. It is still a superb handheld with its 7.4-inch HDR OLED screen, vast verified library, and excellent ergonomics, so it drops only to rank 2 rather than falling out of contention.\n\nThe Nintendo Switch 2 takes over rank 1 as a result. Its pricing is unaffected by this swing, and it is the definitive way to play Nintendo games in 2026. The 7.9-inch LCD supports HDR and runs up to 120fps, and docked it outputs 4K to compatible TVs. With the value calculus shifting, the Switch 2's combination of a stable price, a first-party library nothing else can match, and a polished hardware experience makes it the new front-runner.\n\nThe ASUS ROG Xbox Ally X holds rank 3 as the most powerful handheld PC option, with its Ryzen Z2 Extreme chip, 24GB of RAM, and up to 35W when plugged in, though its $1,000 price keeps it a premium pick. The Lenovo Legion Go 2 at rank 4 and MSI Claw 8 AI+ at rank 5 round out the high-performance Windows tier. The bigger story is that the RAM and NAND shortage is now hitting handheld pricing directly, and buyers should expect this pressure to persist through summer 2026. If you want a Steam Deck OLED, the value proposition has changed, and weighing it against the steady-priced Switch 2 is now the right move.",
                "highlights": [
                    {"title": "Switch 2 Takes Rank 1 After Steam Deck Price Hike", "body": "With Valve raising Steam Deck OLED prices on May 27, the Nintendo Switch 2 moves to rank 1. Its pricing is unaffected, and its unmatched first-party library plus a 7.9-inch HDR display running up to 120fps make it the new front-runner."},
                    {"title": "Steam Deck OLED Drops to Rank 2 on Value", "body": "The 512GB Steam Deck OLED jumped from $549 to $789 and the 1TB from $649 to $949, a near-44% increase. The hardware is still excellent, but its value score no longer leads, so it slips to rank 2 with an adjusted 9.0 overall."},
                    {"title": "RAM and NAND Shortage Hits Handheld Pricing", "body": "Valve attributed the increase to surging memory and storage costs driven by AI data-center demand. This pressure is now reaching consumer handheld pricing directly, and buyers should expect it to persist through summer 2026."},
                ],
            },
            "zh-tw": {
                "commentary": "一個真正的市場事件改寫了這份榜單的頂端。5/27 Valve 大幅調漲 Steam Deck OLED 價格，512GB 從 $549 跳到 $789，1TB 從 $649 漲到 $949，理由是 AI 資料中心需求帶動的 RAM 和 NAND 快閃記憶體短缺。Steam Deck OLED 原本主要靠無敵的 CP 值坐第一，現在貴了將近 44%，這個論點就站不住了。它仍是一台很棒的掌機，7.4 吋 HDR OLED 螢幕、龐大的已驗證遊戲庫、優秀的人體工學都在，所以它只掉到第二，沒有退出競爭。\n\n於是 Nintendo Switch 2 接手第一。它的定價沒受這波影響，而且是 2026 年玩任天堂遊戲最對的選擇。7.9 吋 LCD 支援 HDR，最高跑 120fps，接上底座還能輸出 4K 到相容電視。當 CP 值的算式整個變了，Switch 2 穩定的價格、無人能及的第一方遊戲庫，加上成熟的硬體體驗，讓它成為新的領頭羊。\n\nASUS ROG Xbox Ally X 守住第三，是最強的 Windows 掌機，搭 Ryzen Z2 Extreme、24GB RAM、插電可達 35W，不過 $1,000 的價格讓它維持在高階定位。Lenovo Legion Go 2 第四、MSI Claw 8 AI+ 第五，補齊高效能 Windows 陣容。更大的訊號是，RAM 和 NAND 短缺現在直接打到掌機定價，這個壓力預期會延續整個 2026 夏天。如果你想要 Steam Deck OLED，CP 值的故事已經變了，拿它跟定價穩定的 Switch 2 比一比，現在才是對的做法。",
                "highlights": [
                    {"title": "Steam Deck 漲價後 Switch 2 升上第一", "body": "Valve 5/27 調漲 Steam Deck OLED 價格，Nintendo Switch 2 升上第一。它的定價沒受影響，無人能及的第一方遊戲庫加上 7.9 吋 HDR、最高 120fps 的螢幕，讓它成為新的領頭羊。"},
                    {"title": "Steam Deck OLED 因 CP 值掉到第二", "body": "512GB Steam Deck OLED 從 $549 漲到 $789，1TB 從 $649 漲到 $949，漲幅接近 44%。硬體還是很棒，但 CP 值不再領先，所以滑到第二，總分調整為 9.0。"},
                    {"title": "RAM 與 NAND 短缺打到掌機定價", "body": "Valve 把漲價歸因於 AI 資料中心需求推高的記憶體與儲存成本。這個壓力現在直接觸及消費級掌機定價，預期會延續整個 2026 夏天。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK handheld-gaming-consoles (RANK CHANGE: Switch 2 -> #1, Steam Deck OLED -> #2)")


def build_laptops():
    d, p = load("best-laptops.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "The best MacBooks in 2026: I ranked the 5 best Apple laptops for every need", "url": "https://www.tomsguide.com/best-picks/best-macbook", "source": "Tom's Guide"},
            {"title": "Best Laptops 2026: Our benchmarked picks for productivity, portability, and battery life", "url": "https://www.tomshardware.com/laptops/best-laptops", "source": "Tom's Hardware"},
            {"title": "Best Ultrabooks in 2026: Thin, Light, and Powerful Laptops Ranked", "url": "https://buyingnerd.com/best-ultrabooks-2026/", "source": "Buying Nerd"},
        ],
        "i18n": {
            "en": {
                "commentary": "The MacBook Air M5 holds rank 1, and it remains the benchmark every other laptop is measured against for performance-per-watt and battery life. Apple bumped the starting storage to 512GB, added Wi-Fi 7, and squeezes roughly 18 hours of real-world battery from the M5 chip, with the 13-inch starting at $1,099. For the vast majority of people who want a thin, silent, all-day laptop that simply works, this is the safest recommendation on the market. Its 9.5 performance, 9.5 battery, and 9.5 portability scores explain why it leads.\n\nWhat is genuinely new in 2026 is how close Windows has finally come. The Dell XPS 14 line, running Intel's latest Lunar Lake silicon, delivers battery life that approaches 24 hours in video playback, rivalling Apple for the first time in Windows history. That is why the Dell XPS 14 2026 holds rank 4, and it is the strongest Windows pick for anyone who needs x86 compatibility without sacrificing endurance.\n\nThe MacBook Pro 14 M4 Pro at rank 2 stays the choice for creators who need sustained multi-core performance and a brighter display, while the ASUS Zenbook A16 at rank 3 is the standout ARM-based ultrabook, pairing a 16-inch 2.8K OLED, up to 48GB of RAM, and a 1.2kg chassis with over 21 hours of battery from the Snapdragon X2 Elite Extreme. The Razer Blade 16 at rank 5 remains the pick for players who want gaming power in a premium thin-and-light shell. With the RAM and NAND shortage pushing component costs up across the industry, locking in a configuration now, before further price pressure, is the smart move heading into summer 2026.",
                "highlights": [
                    {"title": "MacBook Air M5 Stays the Default Laptop", "body": "With 9.5 performance, 9.5 battery, and 9.5 portability, the MacBook Air M5 is the benchmark for performance-per-watt. A 512GB base, Wi-Fi 7, and around 18 hours of battery from $1,099 make it the safest pick for most buyers, holding rank 1."},
                    {"title": "Windows Finally Rivals Apple on Battery", "body": "The Dell XPS 14 2026 with Intel Lunar Lake delivers nearly 24 hours of video playback, matching Apple for the first time in Windows history. At rank 4, it is the strongest Windows pick for buyers who need x86 compatibility with all-day endurance."},
                    {"title": "ASUS Zenbook A16 Leads ARM Ultrabooks", "body": "At rank 3, the Zenbook A16 pairs a 16-inch 2.8K OLED, up to 48GB of RAM, and a 1.2kg chassis with over 21 hours of battery from the Snapdragon X2 Elite Extreme. It is the standout big-screen ARM ultrabook of 2026."},
                ],
            },
            "zh-tw": {
                "commentary": "MacBook Air M5 坐穩第一，論每瓦效能和續航，它仍是其他所有筆電被拿來比較的標竿。Apple 把起跳容量拉到 512GB，加入 Wi-Fi 7，M5 晶片在實際使用下能榨出大約 18 小時電力，13 吋從 $1,099（台幣三萬五左右）起跳。對絕大多數想要一台又薄又安靜、一整天都能用、開機就能順順工作的人來說，這是市場上最穩的推薦。效能 9.5、續航 9.5、便攜 9.5，這就是它領先的原因。\n\n2026 年真正的新鮮事，是 Windows 終於追到這麼近。Dell XPS 14 系列搭 Intel 最新的 Lunar Lake 平台，影片播放續航逼近 24 小時，在 Windows 歷史上第一次能跟 Apple 正面拚續航。這就是 Dell XPS 14 2026 守在第四的原因，也是需要 x86 相容性又不想犧牲續航的人最強的 Windows 選擇。\n\nMacBook Pro 14 M4 Pro 第二，需要持續多核效能和更亮螢幕的創作者選它；ASUS Zenbook A16 第三，是最亮眼的 ARM 超輕薄筆電，16 吋 2.8K OLED、最高 48GB RAM、1.2 公斤機身，搭 Snapdragon X2 Elite Extreme 跑出 21 小時以上續航。Razer Blade 16 第五，想要遊戲效能又要薄型高質感外殼的人選它。RAM 和 NAND 短缺正在推高整個產業的零件成本，趁進一步漲價前先把規格鎖定下來，是進入 2026 夏天聰明的做法。",
                "highlights": [
                    {"title": "MacBook Air M5 仍是預設筆電", "body": "效能 9.5、續航 9.5、便攜 9.5，MacBook Air M5 是每瓦效能的標竿。512GB 起跳、Wi-Fi 7、約 18 小時續航，$1,099 起，是多數人最穩的選擇，穩坐第一。"},
                    {"title": "Windows 終於在續航上追平 Apple", "body": "Dell XPS 14 2026 搭 Intel Lunar Lake，影片播放逼近 24 小時，Windows 史上第一次追平 Apple。排第四，是需要 x86 相容又要整天續航的人最強 Windows 選擇。"},
                    {"title": "ASUS Zenbook A16 領銜 ARM 超輕薄", "body": "排第三，Zenbook A16 配 16 吋 2.8K OLED、最高 48GB RAM、1.2 公斤機身，搭 Snapdragon X2 Elite Extreme 跑出 21 小時以上續航。是 2026 最亮眼的大螢幕 ARM 超輕薄筆電。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK laptops")


if __name__ == "__main__":
    build_gaming_chairs()
    build_gaming_headsets()
    build_gaming_mice()
    build_gaming_monitors()
    build_mechanical_keyboards()
    build_handheld_consoles()
    build_laptops()
    print("Batch 5 complete")
