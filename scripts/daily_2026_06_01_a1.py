import json
from pathlib import Path

DATE = "2026-06-01"
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


# ---------------------------------------------------------------------------
# 1. 3D PRINTERS
# ---------------------------------------------------------------------------
def build_3d_printers():
    d, p = load("best-3d-printers.json")
    entry = {
        "date": DATE,
        "rankings": last_rankings(d),
        "references": [
            {
                "title": "Bambu Lab teases new A2L 3D printer — June 1 launch hints at a massive, budget-friendly bed slinger",
                "url": "https://www.tomshardware.com/3d-printing/bambu-lab-teases-new-a2l-3d-printer-june-1-launch-confirmed",
                "source": "Tom's Hardware",
            },
            {
                "title": "New Bambu Lab X2D 3D printer adds nozzle-switching system",
                "url": "https://develop3d.com/3d-printing/bambu-lab-x2d/",
                "source": "DEVELOP3D",
            },
            {
                "title": "The X1-series is EOL - the standard it set will remain forever",
                "url": "https://blog.bambulab.com/the-x1-series-is-eol-the-standard-it-set-will-remain-forever/",
                "source": "Bambu Lab",
            },
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "Today is a pivot day for the FDM market and I want my readers to see it coming. Bambu Lab has "
                    "confirmed a June 1 launch for the A2L, teased as 'a BIG one,' and the 'L' points squarely at a "
                    "large-format bed slinger meant to replace the aging A1 line. That matters for this ranking because "
                    "the A1 family was the gateway most beginners used, and a roomier, value-priced successor reshapes "
                    "the bottom of every buyer's shortlist. At the same time Bambu has formally retired the X1 series "
                    "as end of life and is steering buyers toward the X2D, which adds a mechanical nozzle-switching "
                    "system and the AI thermal management borrowed from the H series. I am holding my order steady "
                    "today because none of these machines have shipped into independent hands yet, and I never reorder "
                    "on a teaser. My P2S Combo stays at the top: it is the printer I recommend to anyone who wants "
                    "multicolor done right with the least fuss, and at its current price it is the most complete "
                    "package you can buy. The X1 Carbon remains my quality benchmark even in EOL status, because the "
                    "hardware does not get worse the day a press release goes out, and the resale and parts ecosystem "
                    "is enormous. Prusa's Core One keeps my trust for anyone who values open firmware and serviceability "
                    "over raw speed. If you have been waiting, the smart move this week is patience. Watch the A2L "
                    "reviews land, watch X2D street pricing settle, then buy. I will revisit these standings the moment "
                    "real test prints exist, and I expect movement in the entry tier within a month."
                ),
                "highlights": [
                    {
                        "title": "A2L launches June 1",
                        "body": "Bambu Lab confirmed a June 1 reveal for the A2L, teased as a large-format bed slinger positioned to succeed the A1 line. It could reshape the value end of this list once units ship.",
                    },
                    {
                        "title": "X1 series is officially EOL",
                        "body": "Bambu retired the X1 series as end of life, but the X1 Carbon hardware still prints beautifully and its parts ecosystem is deep, so I keep it at rank 2 today.",
                    },
                    {
                        "title": "X2D brings nozzle switching",
                        "body": "The new X2D adds a mechanical nozzle-switching dual-extrusion system plus H-series AI thermal management. Promising, but I wait for independent prints before moving it onto the board.",
                    },
                    {
                        "title": "P2S Combo holds the crown",
                        "body": "For hassle-free multicolor at a sane price, the P2S Combo is still the printer I hand to friends. Nothing announced this week changes that recommendation.",
                    },
                    {
                        "title": "My advice: wait a week",
                        "body": "With the A2L hours away and X2D pricing unsettled, patience is the value play. I reorder on test prints, never on teasers.",
                    },
                ],
            },
            "zh-tw": {
                "commentary": (
                    "今天是 FDM 市場的轉折點，我得先幫大家把風向講清楚。Bambu Lab 已經確認 6 月 1 日要發表 A2L，官方自己預告"
                    "「這台很大」，名字裡的 L 幾乎就是在講大列印尺寸的床身移動式機型，目標就是接替已經有點年紀的 A1 系列。"
                    "這對排行榜影響很大，因為 A1 一直是新手入門的第一台，現在出個空間更大又主打性價比的接班人，整個入門價位帶的"
                    "購買清單都要重新洗牌。同一時間 Bambu 也正式把 X1 系列列為停產 EOL，把買家導向 X2D，這台多了機械式換噴頭"
                    "系統，還把 H 系列那套 AI 溫控搬過來。老實說我今天不動排名，因為這幾台都還沒到獨立評測者手上，我從不靠一張"
                    "預告圖就改榜。P2S Combo 繼續坐穩第一，這台就是我會直接推給想玩多色又怕麻煩的人，以現在的售價來看，它是"
                    "整體最完整的一台。X1 Carbon 就算停產了還是我心中的畫質標竿，發新聞稿那天硬體又不會變差，二手跟零件生態也"
                    "夠龐大。Prusa Core One 對於看重開源韌體跟好維修的人，依然值得信賴。如果你最近在觀望，這禮拜最聰明的做法"
                    "就是再等一下。等 A2L 評測出爐，等 X2D 實際街價穩定，再出手。等真正的測試列印件出現，我會立刻重新檢視榜單，"
                    "我預期一個月內入門級距會有變化。"
                ),
                "highlights": [
                    {
                        "title": "A2L 6 月 1 日登場",
                        "body": "Bambu Lab 確認 6 月 1 日揭曉 A2L，預告是大尺寸床身移動式機型，擺明要接班 A1。等實機鋪貨後，入門價位帶很可能洗牌。",
                    },
                    {
                        "title": "X1 系列正式停產",
                        "body": "Bambu 把 X1 系列列為 EOL，但 X1 Carbon 的硬體照樣印得漂亮，零件生態又深，所以我今天還是把它放在第二名。",
                    },
                    {
                        "title": "X2D 帶來機械換噴頭",
                        "body": "新的 X2D 多了機械式換噴頭雙擠出系統，加上 H 系列的 AI 溫控。看起來很香，可是我要等獨立評測列印件才會把它放上榜。",
                    },
                    {
                        "title": "P2S Combo 穩坐第一",
                        "body": "想要省事的多色列印又不想花大錢，P2S Combo 還是我會直接推給朋友的那台。這禮拜的消息都動搖不了它。",
                    },
                    {
                        "title": "我的建議：再等一週",
                        "body": "A2L 幾小時後就揭曉，X2D 價格也還沒穩，這時候耐心才是真正划算的選擇。我只看測試列印件改榜，不看預告圖。",
                    },
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)


# ---------------------------------------------------------------------------
# 2. AI VIDEO GENERATORS
# ---------------------------------------------------------------------------
def build_ai_video():
    d, p = load("best-ai-video-generators.json")
    entry = {
        "date": DATE,
        "rankings": last_rankings(d),
        "references": [
            {
                "title": "Best AI Video Generator in 2026: Runway, Veo, Seedance, Kling & More",
                "url": "https://pixflow.net/blog/best-ai-video-generator/",
                "source": "Pixflow",
            },
            {
                "title": "Kling AI, Runway, Vidu: The AI Video Generators Set to Replace OpenAI's Sora",
                "url": "https://www.bloomberg.com/news/articles/2026-04-01/kling-ai-runway-vidu-the-ai-video-generators-set-to-replace-openai-s-sora",
                "source": "Bloomberg",
            },
            {
                "title": "Veo 3.1 vs Runway vs Kling: AI Video Tools 2026",
                "url": "https://www.ud.hk/insight/article/2026-05-04-ai-video-tools-comparison",
                "source": "UD.HK",
            },
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "The post-Sora landscape has settled into a shape I am comfortable ranking around, and this week's "
                    "benchmarks reinforce my order rather than upend it. Pixflow's May 2026 testing put Google Veo 3.1 "
                    "at 87 percent prompt-adherence accuracy, ahead of Runway Gen-4.5 at 72 percent and Kling 3.0 at 68 "
                    "percent. That single number captures why Veo stays at the top for me: it does what you ask, in 4K, "
                    "in both landscape and portrait, with native audio that actually lines up with the action. For "
                    "narrative shots and establishing scenes it is the most reliable tool I can hand to a working "
                    "creator. Runway Gen-4.5 keeps second because it owns the controls professionals actually fight "
                    "with daily. Its motion brush, camera-move precision, and reference-driven character consistency are "
                    "the best in the field, so when you must keep one face identical across a dozen shots, Runway wins. "
                    "Kling 3.0 holds third on value and cinematic motion. It renders hair, fabric, and liquids with "
                    "real conviction and adds a multi-shot storyboard mode with audio sync across cuts, all at a price "
                    "that undercuts the Western leaders. The bigger story Bloomberg framed in April still drives this "
                    "market: OpenAI pulling the Sora app did not slow consumer video, it accelerated four distinct "
                    "bets, Runway on quality, Kling on cost, Veo on ecosystem, Seedance on open weights. I am keeping "
                    "every position steady today because the leaderboard moved in degrees, not leaps, and my top three "
                    "still answer three clear use cases."
                ),
                "highlights": [
                    {
                        "title": "Veo 3.1 leads on prompt accuracy",
                        "body": "Pixflow's May benchmark clocked Veo 3.1 at 87 percent prompt adherence versus 72 for Runway and 68 for Kling. With 4K and synced native audio, it stays my pick for narrative work.",
                    },
                    {
                        "title": "Runway owns pro controls",
                        "body": "Motion brush, precise camera moves, and reference-driven character consistency keep Runway Gen-4.5 at rank 2. If a face must stay identical across shots, this is the tool.",
                    },
                    {
                        "title": "Kling 3.0 is the value champion",
                        "body": "Convincing hair, fabric, and liquids plus a multi-shot storyboard mode with audio sync, all under the Western price ceiling, hold Kling firmly at third.",
                    },
                    {
                        "title": "The post-Sora market matured",
                        "body": "Bloomberg framed it well: Sora's app shutdown accelerated four bets, quality, cost, ecosystem, and open weights. That diversity is exactly why this list now has clear lanes.",
                    },
                    {
                        "title": "Order held, no leaps this week",
                        "body": "The leaderboard shifted in degrees, not jumps. My top three each answer a distinct use case, so every position stays put today.",
                    },
                ],
            },
            "zh-tw": {
                "commentary": (
                    "後 Sora 時代的格局終於穩下來了，這週的跑分也是在加強我的排序，而不是把它翻盤。Pixflow 五月的測試把 Google "
                    "Veo 3.1 的提示遵循度做到 87%，領先 Runway Gen-4.5 的 72% 跟 Kling 3.0 的 68%。光這個數字就說明了 Veo "
                    "為什麼穩坐我心中第一，你叫它做什麼它就做什麼，還是 4K，橫的直的都行，原生音訊真的對得上畫面動作。要做敘事鏡頭"
                    "跟場景定場，它是我敢直接交給接案者用的最穩工具。Runway Gen-4.5 守住第二，因為它掌握了專業者每天在搏鬥的那些"
                    "控制項。動態筆刷、運鏡精度、靠參考圖鎖角色一致性，全場最強，所以當你得讓同一張臉在十幾個鏡頭裡保持一樣，Runway "
                    "就是贏家。Kling 3.0 靠性價比跟電影感運動穩在第三。它把頭髮、布料、液體渲染得很有說服力，還加了多鏡頭分鏡模式，"
                    "切換之間音訊也能同步，而且價格硬是壓在歐美對手底下。Bloomberg 四月講的大方向到現在還在主導市場，OpenAI 把 "
                    "Sora app 收掉並沒有讓消費級影片變慢，反而加速了四種路線，Runway 拚品質、Kling 拚成本、Veo 拚生態、Seedance "
                    "拚開源權重。我今天每個名次都不動，因為榜單是微幅移動，不是大跳，我的前三名依然分別對應三種很清楚的需求。"
                ),
                "highlights": [
                    {
                        "title": "Veo 3.1 提示遵循度最高",
                        "body": "Pixflow 五月跑分 Veo 3.1 達 87% 提示遵循度，Runway 72%、Kling 68%。加上 4K 跟同步原生音訊，敘事工作我還是選它。",
                    },
                    {
                        "title": "Runway 掌握專業控制",
                        "body": "動態筆刷、精準運鏡、靠參考圖鎖角色一致性，讓 Runway Gen-4.5 穩居第二。要讓同一張臉跨鏡頭都一樣，就靠它。",
                    },
                    {
                        "title": "Kling 3.0 是性價比王",
                        "body": "頭髮、布料、液體都渲染得很有說服力，還有多鏡頭分鏡跟切換音訊同步，價格又壓在歐美對手底下，第三名穩穩的。",
                    },
                    {
                        "title": "後 Sora 市場成熟了",
                        "body": "Bloomberg 講得好，Sora app 收掉反而加速四種路線，品質、成本、生態、開源權重。這種分化正是這份榜單現在分工這麼清楚的原因。",
                    },
                    {
                        "title": "排序維持，本週無大跳",
                        "body": "榜單是微幅移動，不是大跳。前三名各自對應一種明確需求，所以今天每個位置都不動。",
                    },
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)


# ---------------------------------------------------------------------------
# 3. E-READERS
# ---------------------------------------------------------------------------
def build_ereaders():
    d, p = load("best-e-readers.json")
    entry = {
        "date": DATE,
        "rankings": last_rankings(d),
        "references": [
            {
                "title": "Best ereaders in 2026: 9 top ebook readers from Kindle, Kobo and more tested",
                "url": "https://www.techradar.com/best/best-ereader",
                "source": "TechRadar",
            },
            {
                "title": "What new e-readers will Kobo release in 2026?",
                "url": "https://goodereader.com/blog/kobo-ereader-news/what-new-e-readers-will-kobo-release-in-2026",
                "source": "Good e-Reader",
            },
            {
                "title": "Amazon Kindle Vs. Kobo: Which E-Reader Is Right For You?",
                "url": "https://www.bgr.com/2173418/amazon-kindle-vs-kobo-which-e-reader-best-for-you/",
                "source": "BGR",
            },
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "The e-reader debate in 2026 has finally moved past pixels, and that shift is the single most useful "
                    "thing I can tell a buyer this week. Screen quality across Kindle, Kobo, and Boox is now close "
                    "enough that the real divider is software philosophy. Kindle stays tightly optimized for Amazon's "
                    "store, while Kobo leans into native format support, deep typography controls, and seamless public "
                    "library borrowing. That framing is exactly why my top two hold. The Kindle Paperwhite 2025 keeps "
                    "rank one because it nails the fundamentals readers feel every night, a fast crisp display, "
                    "multi-week battery, and the smoothest store-to-page pipeline in the category. For most people who "
                    "just want to read, it is the easiest recommendation I can make. The Kobo Libra Colour stays at "
                    "rank two and remains my pick for the per-dollar value crowd, because its format flexibility and "
                    "library integration give you genuine control over your own reading life. I am noting one piece of "
                    "housekeeping news this week: the Boox Palma 2 has been discontinued. It still sits on my board on "
                    "current stock, but I would not chase a fresh unit at inflated pricing now that supply is drying up. "
                    "Kobo has also signaled that color is its future, with a refreshed Clara Colour and BW generation "
                    "expected, so anyone eyeing a long hold might wait to see those land. I am keeping the full order "
                    "steady today. Nothing this week beats the Paperwhite on reliability or the Libra Colour on value, "
                    "and those two anchors still define the smart buy."
                ),
                "highlights": [
                    {
                        "title": "Software, not screens, divides 2026",
                        "body": "Panel quality has converged, so the real choice is philosophy: Kindle's store optimization versus Kobo's format freedom and library borrowing. That is the lens I rank by now.",
                    },
                    {
                        "title": "Paperwhite 2025 holds rank one",
                        "body": "Fast crisp display, multi-week battery, and the smoothest store-to-page experience make it the easiest recommendation for anyone who simply wants to read.",
                    },
                    {
                        "title": "Libra Colour is the value pick",
                        "body": "Format flexibility plus seamless library integration keep the Kobo Libra Colour at rank two as the best per-dollar choice for readers who want control.",
                    },
                    {
                        "title": "Boox Palma 2 discontinued",
                        "body": "The pocketable Palma 2 has been discontinued. It stays on my list on current stock, but I would not pay inflated prices chasing fresh units now.",
                    },
                    {
                        "title": "Kobo is going all-in on color",
                        "body": "Kobo has signaled a refreshed Clara Colour and BW generation ahead. Long-hold buyers may want to wait for those to land before committing.",
                    },
                ],
            },
            "zh-tw": {
                "commentary": (
                    "2026 年的電子閱讀器之爭，終於不再糾結在像素上，這個轉變是我這週最想先講給買家聽的事。Kindle、Kobo、Boox "
                    "之間的螢幕素質已經接近到，真正的分水嶺變成軟體哲學。Kindle 緊緊綁著 Amazon 書店優化，Kobo 則主打原生格式"
                    "支援、深度排版控制，還有順暢到不行的公共圖書館借閱。這個框架剛好解釋了我前兩名為什麼不動。Kindle Paperwhite "
                    "2025 守住第一，因為它把讀者每晚都會有感的基本功做好了，螢幕快又清晰，續航好幾週，從書店到頁面那條動線是這"
                    "類別最順的。對大多數只想好好看書的人，它就是我最好開口推薦的那台。Kobo Libra Colour 守在第二，依然是我推給"
                    "看重每塊錢價值那群人的首選，因為它的格式彈性跟圖書館整合，讓你真正掌握自己的閱讀生活。這週我也要記一筆消息："
                    "Boox Palma 2 已經停產。靠現有庫存它還留在榜上，但供貨開始乾的現在，我不會去追加價的全新機。Kobo 也放話"
                    "彩色才是它的未來，預期會有改版的 Clara Colour 跟 BW 世代，所以打算長期持有的人，或許可以等那幾台先落地。"
                    "我今天整份排序維持不動。這週沒有任何機種在可靠度上贏 Paperwhite，也沒有在性價比上贏 Libra Colour，這兩個"
                    "定錨依然界定了聰明的買點。"
                ),
                "highlights": [
                    {
                        "title": "2026 看軟體不看螢幕",
                        "body": "面板素質已經收斂，真正的選擇變成哲學之爭：Kindle 的書店優化 對上 Kobo 的格式自由跟圖書館借閱。我現在就用這個角度排名。",
                    },
                    {
                        "title": "Paperwhite 2025 守住第一",
                        "body": "螢幕快又清晰、續航好幾週、書店到頁面最順，對只想好好看書的人來說，這是我最好開口的推薦。",
                    },
                    {
                        "title": "Libra Colour 是性價比首選",
                        "body": "格式彈性加上順暢的圖書館整合，讓 Kobo Libra Colour 穩居第二，是想掌握自己閱讀生活那群人最划算的選擇。",
                    },
                    {
                        "title": "Boox Palma 2 停產",
                        "body": "口袋型的 Palma 2 已經停產。靠現有庫存它還在榜上，但我不會為了追全新機去付加價的錢。",
                    },
                    {
                        "title": "Kobo 全面押注彩色",
                        "body": "Kobo 已經放話會有改版的 Clara Colour 跟 BW 世代。打算長期持有的買家，或許可以等那幾台落地再決定。",
                    },
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)


# ---------------------------------------------------------------------------
# 4. GAS GRILLS
# ---------------------------------------------------------------------------
def build_gas_grills():
    d, p = load("best-gas-grills.json")
    entry = {
        "date": DATE,
        "rankings": last_rankings(d),
        "references": [
            {
                "title": "The Best Weber Grills of 2026, Tested and Reviewed",
                "url": "https://www.bobvila.com/reviews/best-weber-grill/",
                "source": "Bob Vila",
            },
            {
                "title": "BarbecueBible's Grill Guide for 2026",
                "url": "https://barbecuebible.com/2026/04/24/grill-guide-2026/",
                "source": "Barbecuebible.com",
            },
            {
                "title": "Best BBQ Grills of 2026 for Every Budget Fully Tested & Reviewed",
                "url": "https://testedgearhub.com/best-bbq-grills-of-2026-for-every-budget-fully-tested-reviewed/",
                "source": "Tested Gear Hub",
            },
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "We are heading into peak grilling season and the 2026 reviews are landing in a way that validates "
                    "the top of my list rather than shaking it. The reinvented Weber Spirit E-425C is getting "
                    "deserved attention this spring: it gives you four burners, room to cook for a crew, and two Boost "
                    "Burners that deliver 40 percent more power in the sear zone. That combination of capacity, even "
                    "heat, and a genuine searing punch at a mainstream price is exactly why the Spirit E-425 sits at "
                    "rank one for me. It is the grill I tell most families to buy and stop overthinking. The Genesis "
                    "E-325 holds second as the upgrade pick, with thicker build quality and the most even grates Weber "
                    "makes in this class, and the new Genesis SX-335 smart variant shows where Weber is pushing premium "
                    "buyers who want connected cooking. Napoleon's Prestige 500 RSIB keeps third on raw cooking power "
                    "and that signature infrared rear and side burner combo, which is still the setup I reach for when "
                    "I want rotisserie and high-heat searing in one cart. Nothing in the spring 2026 review cycle "
                    "displaces these anchors. Weber's durability and consistent heat keep showing up across "
                    "independent tests, and the Spirit line in particular keeps winning the value argument. I am "
                    "holding the full order steady today. If you are buying for this summer, the Spirit E-425 is the "
                    "safe, high-confidence pick, and the timing right now is good before peak-season demand tightens "
                    "stock on the popular models."
                ),
                "highlights": [
                    {
                        "title": "Spirit E-425C earns rank one",
                        "body": "Four burners, crew-sized capacity, and two Boost Burners delivering 40 percent more sear-zone power at a mainstream price. This is the grill I tell most families to just buy.",
                    },
                    {
                        "title": "Genesis E-325 is the upgrade",
                        "body": "Thicker build and the most even grates Weber makes in this class keep the Genesis at rank two for buyers who want to step up.",
                    },
                    {
                        "title": "Genesis SX-335 brings smart cooking",
                        "body": "Weber's new smart Genesis variant shows where premium connected grilling is heading, a sign the brand is investing at the top.",
                    },
                    {
                        "title": "Napoleon Prestige 500 for power",
                        "body": "Raw output plus infrared rear and side burners hold the Prestige 500 RSIB at third. Still my reach-for grill when I want rotisserie and high-heat searing together.",
                    },
                    {
                        "title": "Buy before peak season tightens stock",
                        "body": "Independent 2026 tests keep crowning Weber on durability and even heat. With summer demand rising, now is a good time to lock in the popular Spirit and Genesis models.",
                    },
                ],
            },
            "zh-tw": {
                "commentary": (
                    "燒烤旺季要來了，2026 的評測一篇篇出爐，剛好是在幫我榜單頂端背書，而不是把它搖動。改款的 Weber Spirit "
                    "E-425C 這個春天受到應得的關注，四口爐、空間夠大可以一次烤給一桌人，還有兩個 Boost Burner 在搶火區多給"
                    "你 40% 火力。容量、均熱、加上真正夠猛的搶火能力，又落在主流價位，這就是 Spirit E-425 在我這裡坐第一的"
                    "原因。這台就是我會叫大多數家庭直接買、別再想太多的那台。在台灣它落在 NT$25,000 上下這個帶，CP 值很實在。"
                    "Genesis E-325 守第二，是進階首選，用料更厚，烤網均熱是 Weber 這級距做得最好的，新的 Genesis SX-335 "
                    "智慧版則點出 Weber 想往哪推那些要連網烤肉的高階買家。Napoleon Prestige 500 RSIB 靠純火力跟它招牌的"
                    "紅外線後燒與側燒組合守第三，想要一台車上同時搞定旋轉烤跟高溫搶火，我還是會伸手拿它。2026 春季這輪評測沒有"
                    "任何一台撼動這幾個定錨。Weber 的耐用度跟穩定均熱在各家獨立測試裡一直出現，Spirit 系列在性價比這題上也一直"
                    "贏。我今天整份排序維持不動。如果你是為這個夏天買，Spirit E-425 就是安全又高信心的選擇，而且現在時機不錯，"
                    "趁旺季需求把熱門型號的庫存吃緊之前先下手。"
                ),
                "highlights": [
                    {
                        "title": "Spirit E-425C 拿下第一",
                        "body": "四口爐、一桌人份的容量、兩個 Boost Burner 在搶火區多給 40% 火力，又落在主流價位。這就是我會叫大多數家庭直接買的那台。",
                    },
                    {
                        "title": "Genesis E-325 是進階款",
                        "body": "用料更厚、烤網均熱是 Weber 這級距最好的，讓 Genesis 守在第二，給想升級的買家。",
                    },
                    {
                        "title": "Genesis SX-335 帶來智慧烤肉",
                        "body": "Weber 新的智慧版 Genesis 點出高階連網烤肉要往哪走，也代表這品牌在頂端持續投資。",
                    },
                    {
                        "title": "要火力就看 Napoleon Prestige 500",
                        "body": "純火力加上紅外線後燒與側燒，讓 Prestige 500 RSIB 守第三。想一台車同時搞定旋轉烤跟高溫搶火，我還是拿它。",
                    },
                    {
                        "title": "趁旺季庫存吃緊前先買",
                        "body": "2026 獨立測試持續把 Weber 推上耐用與均熱寶座。夏天需求升溫，現在正好趁熱門的 Spirit 跟 Genesis 缺貨前鎖定。",
                    },
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)


# ---------------------------------------------------------------------------
# 5. OUTDOOR GRIDDLES
# ---------------------------------------------------------------------------
def build_griddles():
    d, p = load("best-outdoor-griddles.json")
    entry = {
        "date": DATE,
        "rankings": last_rankings(d),
        "references": [
            {
                "title": "Fire it up! 5 outdoor griddles you need for this year's barbecue season",
                "url": "https://www.t3.com/home-living/barbeque/outdoor-griddles",
                "source": "T3",
            },
            {
                "title": "The Best Outdoor Griddle for 2026",
                "url": "https://thebarbecuelab.com/best-outdoor-griddle/",
                "source": "The Barbecue Lab",
            },
            {
                "title": "Meet the Standout Winners From Our 2026 Grilling Awards",
                "url": "https://www.mensjournal.com/gear/best-grills",
                "source": "Men's Journal",
            },
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "Griddles are the fastest-growing barbecue trend of 2026, and the season's reviews are crowning the "
                    "machines I already have near the top of this list. The big story is the Weber Slate 36, repeatedly "
                    "called the griddle to beat in the $799 to $1,049 range. Its rust-resistant, porcelain-enamelled "
                    "cooktop is a genuine differentiator in humid conditions, it heats to 260C, and three "
                    "independently controlled burners give you real multi-zone cooking. That is a serious flat-top, and "
                    "it earns its rank four placement comfortably. So why do I still hold Camp Chef's Gridiron 36 at "
                    "number one? Because when I weigh heat control, build quality, and grease management together, the "
                    "Gridiron is the most complete cook I have used, and grease handling is where flat-tops live or die "
                    "for me. The Blackstone Original 36 Omnivore stays at rank two as the value workhorse, the griddle "
                    "I recommend to anyone who wants the most cooking surface per dollar and a massive accessory "
                    "ecosystem. Traeger's Flatrock 3-Zone holds third on its excellent zoned heat control. The Weber "
                    "Slate's porcelain enamel is a real selling point if you live somewhere humid and dread seasoning "
                    "maintenance, and I would not blame anyone in the Gulf Coast or the Pacific Northwest for "
                    "prioritizing it. I am keeping the order steady today because the Slate's strengths were already "
                    "priced into my board. If you are buying for summer cookouts, the Gridiron is my no-regrets pick, "
                    "and the Slate is the smart choice when rust resistance tops your list."
                ),
                "highlights": [
                    {
                        "title": "Griddles are 2026's hottest trend",
                        "body": "Flat-top cooking is the fastest-growing barbecue category this year, with breakfasts, smash burgers, seafood, and stir-fries all moving outdoors. The competition has never been deeper.",
                    },
                    {
                        "title": "Weber Slate 36 is the griddle to beat",
                        "body": "Reviewers crown the Slate in the $799 to $1,049 range. Its rust-resistant porcelain cooktop, 260C heat, and three-zone control make it a serious flat-top at rank four.",
                    },
                    {
                        "title": "Gridiron 36 holds number one",
                        "body": "Weighing heat control, build, and grease management together, Camp Chef's Gridiron is the most complete cook I have used. Grease handling is where flat-tops win or lose for me.",
                    },
                    {
                        "title": "Blackstone Omnivore is the value king",
                        "body": "Most cooking surface per dollar plus a massive accessory ecosystem keep the Original 36 Omnivore at rank two for budget-minded buyers.",
                    },
                    {
                        "title": "Rust resistance is the Slate's edge",
                        "body": "If you live somewhere humid and hate seasoning upkeep, the Slate's porcelain enamel is a real advantage worth prioritizing.",
                    },
                ],
            },
            "zh-tw": {
                "commentary": (
                    "鐵板燒是 2026 成長最快的烤肉趨勢，這季的評測也把我榜單頂端那幾台機器一一捧上來。最大的話題是 Weber Slate "
                    "36，被一再點名是 $799 到 $1,049 這個帶裡最難打的那台。它防鏽的琺瑯瓷鐵板面，在潮濕環境是真正的差異化"
                    "賣點，能加熱到 260 度，三個獨立控火爐口給你真正的多區烹調。這是一台很認真的鐵板，穩穩拿下第四名沒問題。"
                    "那為什麼我還是把 Camp Chef Gridiron 36 放第一？因為把控火、用料、排油一起秤，Gridiron 是我用過最完整"
                    "的一台，而排油正是鐵板的生死線。Blackstone Original 36 Omnivore 守第二，是性價比的工作馬，想要每塊錢"
                    "換到最多烹調面積、又想要龐大配件生態的人，我就推這台。Traeger Flatrock 3-Zone 靠優秀的分區控火守第三。"
                    "Weber Slate 的琺瑯瓷對住在潮濕地方、又怕養面保養的人是真賣點，在台灣這種濕度，光是不用一直擔心生鏽就很"
                    "加分，南部跟東部沿海的朋友把它擺前面我完全不會怪你。我今天排序維持不動，因為 Slate 的強項本來就已經反映"
                    "在我的榜上了。如果你是為夏天聚餐買，Gridiron 是我不後悔的選擇，而當防鏽是你清單第一順位時，Slate 就是"
                    "聰明解。"
                ),
                "highlights": [
                    {
                        "title": "鐵板是 2026 最夯趨勢",
                        "body": "鐵板燒是今年成長最快的烤肉類別，早餐、爆漿漢堡、海鮮、熱炒全都搬到戶外。競爭從沒這麼激烈過。",
                    },
                    {
                        "title": "Weber Slate 36 最難打",
                        "body": "評測把 Slate 捧在 $799 到 $1,049 帶。防鏽琺瑯瓷面、260 度高溫、三區控火，讓它在第四名就是一台很認真的鐵板。",
                    },
                    {
                        "title": "Gridiron 36 守住第一",
                        "body": "把控火、用料、排油一起秤，Camp Chef Gridiron 是我用過最完整的一台。排油正是鐵板的生死線。",
                    },
                    {
                        "title": "Blackstone Omnivore 是性價比王",
                        "body": "每塊錢換到最多烹調面積，再加上龐大配件生態，讓 Original 36 Omnivore 守第二，給精打細算的買家。",
                    },
                    {
                        "title": "防鏽是 Slate 的優勢",
                        "body": "住在潮濕地方又懶得養面的人，Slate 的琺瑯瓷是真正的優勢，值得放前面。",
                    },
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)


# ---------------------------------------------------------------------------
# 6. ROBOT LAWN MOWERS
# ---------------------------------------------------------------------------
def build_mowers():
    d, p = load("best-robot-lawn-mowers.json")
    entry = {
        "date": DATE,
        "rankings": last_rankings(d),
        "references": [
            {
                "title": "5 new robot lawnmowers from CES 2026 that show the future of smart gardening this year",
                "url": "https://www.t3.com/home-living/garden/5-new-robot-lawnmowers-from-ces-2026",
                "source": "T3",
            },
            {
                "title": "Of all the new 2026 robot lawn mowers, these are the 3 I'm most excited to try out",
                "url": "https://www.techradar.com/home/smart-home/of-all-the-new-2026-robot-lawn-mowers-these-are-the-3-im-most-excited-to-try-out",
                "source": "TechRadar",
            },
            {
                "title": "Best Robot Lawn Mowers of 2026: The Ultimate Guide",
                "url": "https://robohorizon.com/en-us/magazine/2026/03/best-robot-lawn-mowers-of-2026-the-ultimate-guide-to-your-lawns-new-overlords/",
                "source": "RoboHorizon",
            },
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "The 2026 robot mower class that debuted at CES is now reaching reviewers, and the news this week "
                    "reinforces exactly why my top three sit where they do. Mammotion's Luba 3 AWD took home a CES 2026 "
                    "Innovation Award on the strength of its Tri-Fusion positioning, which fuses 360-degree LiDAR, "
                    "NetRTK satellite correction, and dual-camera AI vision. The all-wheel-drive system climbs slopes "
                    "up to 80 percent and its AI recognizes more than 300 obstacle types. That is the most capable "
                    "terrain package in the category, and it keeps the Luba 3 AWD at rank one for anyone with a hilly "
                    "or complex yard. Ecovacs is pushing hard right behind it with the new HoloScope 360 dual-LiDAR "
                    "navigation, which can cut setup to under a minute and map down to two-centimeter accuracy, paired "
                    "with a TruEdge trimmer for cleaner edges along fences and paths. That is precisely the navigation "
                    "and automation strength that holds the Goat A3000 line at ranks two through four. Segway unveiled "
                    "nine new Navimow models across five series using a cloud NRTK system that drops the local antenna, "
                    "and the X-series stays my pick for owners who want wire-free setup without fuss. I am holding the "
                    "order steady today because these are announcements and early units, not finished long-term tests, "
                    "and I never reorder a mower before it has survived a full mowing cycle in real grass. If you are "
                    "buying now, the Luba 3 AWD is the no-compromise terrain pick, and the Navimow i2 remains the value "
                    "sweet spot for flatter lawns."
                ),
                "highlights": [
                    {
                        "title": "Luba 3 AWD wins CES innovation",
                        "body": "Tri-Fusion positioning fuses 360-degree LiDAR, NetRTK satellite correction, and dual-camera AI vision. With 80 percent slope climbing and 300-plus obstacle types, it holds rank one for tough yards.",
                    },
                    {
                        "title": "Ecovacs HoloScope 360 speeds setup",
                        "body": "The new dual-LiDAR system maps to two-centimeter accuracy and cuts install to under a minute, with a TruEdge trimmer for cleaner edges. This keeps the Goat A3000 line strong.",
                    },
                    {
                        "title": "Segway floods the lineup",
                        "body": "Nine new Navimow models across five series use a cloud NRTK system that drops the local antenna. The X-series stays my wire-free pick for fuss-free setup.",
                    },
                    {
                        "title": "Order held until real testing",
                        "body": "These are announcements and early units, not finished long-term reviews. I never reorder a mower before it survives a full cycle in real grass.",
                    },
                    {
                        "title": "Navimow i2 is the value sweet spot",
                        "body": "For flatter lawns, the Navimow i2 LiDAR remains the smart-money buy, balancing strong navigation and automation against a friendlier price.",
                    },
                ],
            },
            "zh-tw": {
                "commentary": (
                    "CES 亮相的 2026 割草機世代現在陸續到評測者手上，這週的消息正好強化了我前三名為什麼站在這些位置。Mammotion "
                    "Luba 3 AWD 靠它的 Tri-Fusion 定位拿下 CES 2026 創新獎，這套系統把 360 度光達、NetRTK 衛星校正、雙鏡頭"
                    "AI 視覺融在一起。四輪驅動能爬 80% 的坡，AI 能辨識超過 300 種障礙物。這是這個類別裡最強的地形套件，也讓 "
                    "Luba 3 AWD 在第一名穩住，給院子有坡度或地形複雜的人。Ecovacs 緊追在後，主打新的 HoloScope 360 雙光達"
                    "導航，能把安裝壓到一分鐘以內，建圖精度到兩公分，再配上 TruEdge 修邊器，沿著圍籬跟步道把邊修得更乾淨。這正是"
                    "撐住 Goat A3000 系列二到四名的導航與自動化實力。Segway 一口氣端出橫跨五個系列的九款新 Navimow，用雲端 "
                    "NRTK 系統省掉本地天線，X 系列依然是我推給想要免布線、又怕麻煩的人的選擇。我今天排序維持不動，因為這些都還是"
                    "發表跟早期機，不是跑完的長期測試，而割草機沒在真草地撐過一整個割草週期之前，我從不改它的排名。如果你現在要買，"
                    "Luba 3 AWD 是不妥協的地形之選，Navimow i2 則依然是平坦草坪的性價比甜蜜點。"
                ),
                "highlights": [
                    {
                        "title": "Luba 3 AWD 拿下 CES 創新獎",
                        "body": "Tri-Fusion 定位融合 360 度光達、NetRTK 衛星校正、雙鏡頭 AI 視覺。能爬 80% 坡、辨識 300 多種障礙，難搞的院子第一名就是它。",
                    },
                    {
                        "title": "Ecovacs HoloScope 360 加速安裝",
                        "body": "新雙光達系統建圖精度到兩公分，安裝壓到一分鐘以內，還有 TruEdge 修邊器把邊修乾淨。這撐住了 Goat A3000 系列。",
                    },
                    {
                        "title": "Segway 一口氣灌滿產品線",
                        "body": "橫跨五系列的九款新 Navimow 用雲端 NRTK 省掉本地天線。X 系列依然是我推給想免布線、怕麻煩的人的選擇。",
                    },
                    {
                        "title": "排序維持，等真測試",
                        "body": "這些都還是發表跟早期機，不是跑完的長期評測。割草機沒在真草地撐過一整個週期前，我從不改排名。",
                    },
                    {
                        "title": "Navimow i2 是性價比甜蜜點",
                        "body": "平坦草坪上，Navimow i2 光達版依然是精明之選，導航與自動化夠強，價格又比較親民。",
                    },
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)


# ---------------------------------------------------------------------------
# 7. SMART THERMOSTATS
# ---------------------------------------------------------------------------
def build_thermostats():
    d, p = load("best-smart-thermostats.json")
    entry = {
        "date": DATE,
        "rankings": last_rankings(d),
        "references": [
            {
                "title": "Ecobee and Nest lead 2026 smart thermostat rankings",
                "url": "https://www.msn.com/en-us/news/other/ecobee-and-nest-lead-2026-smart-thermostat-rankings/gm-GM9F89B1BC",
                "source": "MSN",
            },
            {
                "title": "Ecobee vs Nest Thermostat (2026): Which Smart Thermostat Is Right for You?",
                "url": "https://www.smarthomeexplorer.com/guides/ecobee-vs-nest-thermostat-2026",
                "source": "Smart Home Explorer",
            },
            {
                "title": "Nest $280 vs Ecobee $250 vs Honeywell $200 — Saves More 2026?",
                "url": "https://clearflowguide.com/articles/nest-vs-ecobee-smart-thermostat-2026",
                "source": "Clearflow Guide",
            },
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "As summer cooling season ramps up, the 2026 thermostat reviews keep landing on the same two "
                    "champions I already have at the top, and the reasoning is sound enough that I am holding my order "
                    "steady. Independent tests and expert roundups put Ecobee's Smart Thermostat Premium and Google's "
                    "Nest Learning Thermostat 4th Gen as the clear market leaders. The Ecobee earns rank one for me "
                    "because at $249 it bundles a room sensor, built-in air quality monitoring, and compatibility with "
                    "Alexa, Google, Siri, and HomeKit, all with no subscription. For a household that wants whole-home "
                    "comfort across every ecosystem, that is the most complete value in the category. The Nest 4th Gen "
                    "holds rank two on the strength of its learning engine. CNET's 2026 review confirmed the schedule "
                    "learns in seven to ten days and needs no manual input afterward, and PCMag called it the "
                    "best-designed thermostat money can buy. The story that matters most this season is time-of-use "
                    "optimization. Both units now talk to your utility, pre-cooling when power is cheap and easing off "
                    "when afternoon prices spike, and that is where the real savings show up on a summer bill. Honeywell's "
                    "T9 keeps third on its excellent multi-room sensor support. I would note the Ecobee promotion that "
                    "ran with prices as low as $59.99 ended May 27, so the deep discounts have passed for now. I am "
                    "keeping the full order steady today. If you are buying before the heat peaks, the Ecobee Premium is "
                    "my no-subscription value pick, and the Nest is the choice when hands-off learning matters most."
                ),
                "highlights": [
                    {
                        "title": "Ecobee Premium holds rank one",
                        "body": "At $249 it bundles a room sensor, air quality monitoring, and Alexa, Google, Siri, and HomeKit support with no subscription. That is the most complete value here.",
                    },
                    {
                        "title": "Nest 4th Gen learns in 7 to 10 days",
                        "body": "CNET confirmed the schedule learns in a week to ten days with no manual input, and PCMag called it the best-designed thermostat money can buy. It stays at rank two.",
                    },
                    {
                        "title": "Time-of-use is the 2026 savings story",
                        "body": "Both leaders talk to your utility, pre-cooling when power is cheap and easing off during afternoon price spikes. That is where summer bills actually drop.",
                    },
                    {
                        "title": "Honeywell T9 owns multi-room",
                        "body": "Excellent multi-room sensor support keeps the Honeywell T9 at rank three for homes that need to balance temperature across many rooms.",
                    },
                    {
                        "title": "Ecobee's deep discount has ended",
                        "body": "The promotion with prices as low as $59.99 ran only through May 27, so the steepest deals have passed. Buy on current pricing, not on a sale that closed.",
                    },
                ],
            },
            "zh-tw": {
                "commentary": (
                    "夏天冷氣季開始升溫，2026 的恆溫器評測一篇篇都落在我本來就放榜首的那兩位冠軍身上，理由夠扎實，所以我排序維持"
                    "不動。獨立測試跟專家彙整都把 Ecobee Smart Thermostat Premium 跟 Google Nest Learning Thermostat "
                    "第四代列為明確的市場領頭羊。Ecobee 在我這裡拿第一，因為 249 美元就把房間感測器、內建空氣品質監測，加上"
                    "Alexa、Google、Siri、HomeKit 全相容通通包進去，而且完全免訂閱。對一個想要全屋舒適、又橫跨各家生態的"
                    "家庭，這就是這個類別裡最完整的價值。Nest 第四代守第二，靠的是它的學習引擎。CNET 2026 評測證實它七到十天"
                    "就學會排程，之後不用再手動，PCMag 更稱它是花錢買得到設計最好的恆溫器。這季最重要的話題是時間電價優化。"
                    "兩台現在都能跟你的電力公司對話，電便宜時先把屋子預冷，下午電價飆高時收力道，這正是夏季帳單真正省下來的地方。"
                    "Honeywell T9 靠優秀的多房間感測器支援守第三。要提醒一下，Ecobee 那檔最低 59.99 美元的促銷 5 月 27 日"
                    "已經結束，深折扣這陣子先過去了。我今天整份排序維持不動。如果你要趕在最熱之前買，Ecobee Premium 是我"
                    "免訂閱的價值之選，而當你最在意免動腦的自動學習，Nest 就是答案。"
                ),
                "highlights": [
                    {
                        "title": "Ecobee Premium 守住第一",
                        "body": "249 美元就把房間感測器、空氣品質監測，加上 Alexa、Google、Siri、HomeKit 全包進去，還免訂閱。這是這裡最完整的價值。",
                    },
                    {
                        "title": "Nest 第四代七到十天學會",
                        "body": "CNET 證實它一週到十天就學會排程，之後免手動，PCMag 稱它是花錢買得到設計最好的恆溫器。它守在第二。",
                    },
                    {
                        "title": "時間電價是 2026 省錢重點",
                        "body": "兩台領頭羊都能跟電力公司對話，電便宜時預冷，下午電價飆高時收力道。夏季帳單真正省的地方就在這。",
                    },
                    {
                        "title": "Honeywell T9 主打多房間",
                        "body": "優秀的多房間感測器支援，讓 Honeywell T9 守第三，給需要在多個房間之間平衡溫度的家庭。",
                    },
                    {
                        "title": "Ecobee 深折扣已結束",
                        "body": "最低 59.99 美元的促銷只到 5 月 27 日，最猛的折扣先過去了。請看現價買，別等已經收掉的特價。",
                    },
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)


if __name__ == "__main__":
    build_3d_printers()
    build_ai_video()
    build_ereaders()
    build_gas_grills()
    build_griddles()
    build_mowers()
    build_thermostats()
    print("All 7 files updated for", DATE)
