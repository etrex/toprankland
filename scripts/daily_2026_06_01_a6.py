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
# Per-file content
# ---------------------------------------------------------------------------

CONTENT = {
    "best-ai-image-generators.json": {
        "references": [
            {
                "title": "Midjourney May 2026 Update: V8.1, Pricing & Video",
                "url": "https://pixverse.ai/en/blog/midjourney-ai-image-generator-review",
                "source": "PixVerse",
            },
            {
                "title": "AI Image Generators 2026: Midjourney, GPT Image, Stable Diffusion, and Alternatives",
                "url": "https://aiunpacking.com/guides/ai-image-generators-2026-midjourney-dall-e-stable-diffusion/",
                "source": "AIUnpacking",
            },
            {
                "title": "AI Image Generation 2026: Midjourney v8 vs GPT Image 2 vs Flux",
                "url": "https://lushbinary.com/blog/ai-image-generation-comparison-midjourney-gpt-flux/",
                "source": "Lushbinary",
            },
        ],
        "en": {
            "commentary": (
                "Monday opens June with the same order I have held all through late May, and that consistency is the story. "
                "Midjourney V8 stays first because V8.1 from April 30 keeps widening its aesthetic lead, the 2K HD output and the image-to-video path that extends a still up to 21 seconds now run inside one native web app. "
                "For editorial covers and concept art I still reach for it before anything else. "
                "Flux 2 Pro holds second on photorealism, where Black Forest Labs still owns skin and texture, and the open Dev weights plus sub-cent-per-megapixel API keep it the commercial production backbone. "
                "GPT Image 2 sits third on prompt accuracy and multilingual text, and with DALL-E 2 and DALL-E 3 API support now sunset as of May, the migration to GPT Image 2 is complete for anyone who builds on OpenAI. "
                "Ideogram V3 owns text rendering at fourth and ships finished posters, Imagen 4 takes fifth on the cleanest Gemini API economics. "
                "The deeper field matters more this month. Google Nano Banana 2, Recraft V4, and ByteDance Seedream 5 are all genuinely competitive now, and I am watching whether any of them forces a reorder in June. "
                "For today the call is simple, pick by job. Midjourney for art direction, Flux 2 Pro for photoreal product work, GPT Image 2 when text or precise prompt adherence is the deliverable, Ideogram when the words are the point. "
                "The early-June start of the month does not move AI subscriptions, this category turns on model releases and the next one has not landed yet."
            ),
            "highlights": [
                {
                    "title": "Midjourney V8.1 keeps the aesthetic crown into June",
                    "body": "The April 30 V8.1 update brought 2K HD output, faster generation, and image-to-video that extends a still up to 21 seconds, all inside a native web app. For editorial and concept art the lead is uncontested and first place is structural this month.",
                },
                {
                    "title": "GPT Image 2 migration is now forced as DALL-E API sunsets",
                    "body": "DALL-E 2 and DALL-E 3 API support ended in May, so anyone building on OpenAI is now on GPT Image 2. The prompt accuracy and multilingual text rendering lead holds, and the bundled ChatGPT Plus path stays the best value entry at third.",
                },
                {
                    "title": "The challenger field is deepening fast",
                    "body": "Google Nano Banana 2, Recraft V4, and ByteDance Seedream 5 are all genuinely competitive now. None forces a reorder today, but this is the most crowded the top tier has looked, and June could be the month one of them breaks into the front five.",
                },
            ],
        },
        "zh-tw": {
            "commentary": (
                "禮拜一開啟六月，榜單維持我整個五月底守住的順序，這個穩定本身就是重點。\n\n"
                "Midjourney V8 守第一，4 月 30 日的 V8.1 把藝術領先繼續拉開，2K HD 輸出加上把靜態圖延伸到 21 秒的圖轉影片功能，現在全部跑在一個原生網頁應用裡。做雜誌封面跟概念藝術，我還是第一個就想到它。\n\n"
                "Flux 2 Pro 守第二靠寫實度，Black Forest Labs 在皮膚跟材質還是稱霸，開源 Dev 權重加上一張 1024 不到 NT$1 的 API，讓它穩坐商業生產的主力。\n\n"
                "GPT Image 2 第三靠 prompt 精準度跟多語言文字，DALL-E 2 跟 DALL-E 3 的 API 五月正式落幕之後，在 OpenAI 上開發的人全部轉進 GPT Image 2，遷移已經完成。\n\n"
                "Ideogram V3 文字渲染稱霸守第四，海報直接交件。Imagen 4 第五靠 Gemini API 最乾淨的成本。\n\n"
                "講真的，這個月更值得看的是後段變深了。Google Nano Banana 2、Recraft V4、ByteDance Seedream 5 現在都真的有競爭力，我在盯六月會不會有人逼出重排。\n\n"
                "今天的建議很單純，看用途選。藝術指導用 Midjourney，寫實產品照用 Flux 2 Pro，要文字或精準 prompt 遵循用 GPT Image 2，文字是主角用 Ideogram。六月初開月對 AI 訂閱沒影響，這個分類看的是模型發布，下一發還沒落地。"
            ),
            "highlights": [
                {
                    "title": "Midjourney V8.1 把美學王冠帶進六月",
                    "body": "4 月 30 日 V8.1 帶來 2K HD 輸出、更快生成、把靜態圖延伸到 21 秒的圖轉影片，全部在原生網頁裡。做編輯跟概念藝術領先還沒人挑戰，第一名這個月是結構性的。",
                },
                {
                    "title": "DALL-E API 落幕逼出 GPT Image 2 遷移",
                    "body": "DALL-E 2 跟 DALL-E 3 的 API 五月結束，在 OpenAI 上開發的人現在全在 GPT Image 2。prompt 精準度跟多語言文字渲染領先守住，綑綁 ChatGPT Plus 還是第三名最划算的入口。",
                },
                {
                    "title": "挑戰者陣容快速變深",
                    "body": "Google Nano Banana 2、Recraft V4、ByteDance Seedream 5 現在都真的有競爭力。今天還沒逼出重排，但前段從沒這麼擁擠過，六月很可能有人擠進前五。",
                },
            ],
        },
    },
    "best-coffee-makers.json": {
        "references": [
            {
                "title": "The best drip coffee makers of 2026, tried and tested",
                "url": "https://www.cnn.com/cnn-underscored/reviews/best-drip-coffee-makers",
                "source": "CNN Underscored",
            },
            {
                "title": "Fellow Aiden Review 2026: A Real Winner!",
                "url": "https://www.coffeeness.de/en/fellow-aiden-review/",
                "source": "Coffeeness",
            },
            {
                "title": "The 8 Best Coffee Makers of 2026 (Tested, Ranked, and Caffeinated)",
                "url": "https://thegreatreviewer.com/home-kitchen-reviews/best-coffee-makers-2026/",
                "source": "The Great Reviewer",
            },
        ],
        "en": {
            "commentary": (
                "First of June and the drip order holds, which is exactly what I expect from a category that turns on engineering rather than calendar. "
                "The Technivorm Moccamaster KBGV Select keeps first because it nails the SCA brew window of 196 to 205 degrees Fahrenheit every single cycle and fills a 40-ounce carafe in just over seven minutes. "
                "I have watched these run for a decade with nothing more than a descale, and CNN Underscored still calls it the best drip maker of 2026. "
                "The Breville Precision Brewer Thermal stays second on sheer versatility, it covers drip, iced, and cold brew and holds a full carafe hot for hours, which is the right pick when one machine has to do every job. "
                "The Fellow Aiden holds third and earns it, reviewers this spring keep pointing out it makes a better small batch than the Breville thanks to precise temperature control and programmable brew phases. "
                "If your daily pour is two or three cups, Aiden is the cup-quality winner. "
                "Cuisinart DCC-4000 stays the value anchor at fifth, and the Ninja CE251 at seventh remains the budget call that punches above its price. "
                "There is no Memorial Day hangover that changes any of this, coffee makers do not get spec bumps on a holiday. "
                "My verdict for June is unchanged, Moccamaster for pure brew quality and longevity, Breville when versatility matters, Aiden for small-batch precision, Cuisinart or Ninja when the budget leads."
            ),
            "highlights": [
                {
                    "title": "Moccamaster still hits the SCA window every cycle",
                    "body": "The KBGV Select brews at 196 to 205 degrees Fahrenheit and fills a 40-ounce carafe in just over seven minutes, cycle after cycle. A decade of reliable service on nothing but descaling is why CNN Underscored still names it the best drip maker of 2026.",
                },
                {
                    "title": "Fellow Aiden owns small-batch cup quality",
                    "body": "Spring 2026 reviews keep landing on the same point, Aiden makes a better small batch than the Breville thanks to precise temperature control and programmable brew phases. If your daily pour is two or three cups, this is the cup-quality pick at third.",
                },
                {
                    "title": "Breville Precision Brewer is the one-machine-does-all answer",
                    "body": "Drip, iced, and cold brew in one unit, plus a thermal carafe that holds heat for hours. When a single brewer has to cover every style in the house, the Breville stays the versatility leader at second.",
                },
            ],
        },
        "zh-tw": {
            "commentary": (
                "六月一號，手沖滴漏的排序守住，這正是我對一個靠工藝而非檔期決勝的分類的預期。\n\n"
                "Technivorm Moccamaster KBGV Select 守第一，因為它每一次都精準命中 SCA 沖煮溫度區間 91 到 96 度，七分鐘出頭就裝滿一壺約 1.2 公升。我看過這台機器只靠除垢就跑十年，CNN Underscored 到 2026 還是叫它年度最佳滴漏機。台灣售價大概 NT$11,000 上下，貴但你買的是十年壽命。\n\n"
                "Breville Precision Brewer Thermal 守第二靠全能，滴漏、冰咖啡、冷萃都會，保溫壺撐好幾小時還熱，家裡只想擺一台甚麼都要會的就選它。\n\n"
                "Fellow Aiden 守第三，這個位置它站得住，今年春天的評測一直提它小份量沖得比 Breville 好，靠的是精準溫控加可程式化沖煮階段。每天就煮兩三杯的人，Aiden 是杯品冠軍。\n\n"
                "老實說 Cuisinart DCC-4000 守第五當 CP 值定錨，Ninja CE251 第七還是預算派超值首選，一台 NT$3,000 有找。\n\n"
                "陣亡將士紀念日沒有甚麼後遺症會改變這些，咖啡機不會在連假升級規格。我六月的結論不變，純粹沖煮品質跟耐用度選 Moccamaster，要全能選 Breville，小份量精準選 Aiden，預算掛帥就 Cuisinart 或 Ninja。"
            ),
            "highlights": [
                {
                    "title": "Moccamaster 每次都命中 SCA 溫度區間",
                    "body": "KBGV Select 沖煮溫度 91 到 96 度，七分鐘出頭裝滿約 1.2 公升一壺，每次都一樣。十年只靠除垢就穩定服役，這是 CNN Underscored 到 2026 還叫它年度最佳滴漏機的原因。",
                },
                {
                    "title": "Fellow Aiden 小份量杯品稱霸",
                    "body": "2026 春天的評測一直落在同一點，Aiden 小份量沖得比 Breville 好，靠精準溫控加可程式化沖煮階段。每天就兩三杯的人，這是第三名的杯品首選。",
                },
                {
                    "title": "Breville Precision Brewer 是一機全包的答案",
                    "body": "滴漏、冰咖啡、冷萃一台搞定，加上保溫壺撐好幾小時。家裡一台機器要涵蓋所有沖法，Breville 守第二全能王。",
                },
            ],
        },
    },
    "best-gaming-headsets.json": {
        "references": [
            {
                "title": "I tested Reddit's favorite gaming headsets and there's a clear winner",
                "url": "https://www.tomsguide.com/gaming/gaming-peripherals/i-tested-reddits-favorite-high-end-gaming-headsets-and-theres-a-clear-winner-but-its-not-the-one-i-expected",
                "source": "Tom's Guide",
            },
            {
                "title": "SteelSeries Arctis Nova Elite vs Audeze Maxwell: Battle for the best audiophile gaming headset",
                "url": "https://www.soundguys.com/steelseries-arctis-nova-elite-vs-audeze-maxwell-146509/",
                "source": "SoundGuys",
            },
            {
                "title": "Best Gaming Headset 2026 — Top Picks for Competitive and Casual Gaming",
                "url": "https://gamingpcguru.com/best-gaming-headset-2026/",
                "source": "Gaming PC Guru",
            },
        ],
        "en": {
            "commentary": (
                "June starts with the headset order intact, and the tension at the top is the same one I have flagged all month. "
                "The SteelSeries Arctis Nova Pro Wireless keeps first because it is the most well-rounded option in the category, the swappable dual-battery system means zero downtime, the dual-wireless connectivity covers every platform, and the active noise cancellation still leads anything in a gaming form factor. "
                "That all-rounder completeness is why it stays my default recommendation. "
                "The Audeze Maxwell 2 sits a hair behind at second and keeps making the value argument loudly, Tom's Guide just ran it to the top of a high-end shootout, its planar magnetic drivers deliver detail dynamic drivers cannot reach, the 80-hour battery is genuinely hard to drain, and at $299 it costs half of the Arctis Nova Elite. "
                "If raw sound is your priority and you do not need the swappable battery base, Maxwell 2 is the smarter spend. "
                "Turtle Beach Stealth Pro II holds third as the balanced wireless pick, Logitech G Pro X 2 Lightspeed stays fourth on competitive pedigree. "
                "HyperX Cloud Alpha Wireless remains the value champion at sixth with a battery life that still embarrasses pricier rivals. "
                "Nothing shipped this week that reorders the top, so the June read is the same. Arctis Nova Pro Wireless for the complete package, Maxwell 2 for audiophile sound at a fair price, HyperX when budget decides."
            ),
            "highlights": [
                {
                    "title": "Arctis Nova Pro Wireless stays the most complete package",
                    "body": "Swappable dual batteries for zero downtime, dual-wireless that covers every platform, and class-leading ANC in a gaming form factor. That all-rounder completeness keeps it first and the default recommendation for anyone who wants one headset to do everything.",
                },
                {
                    "title": "Audeze Maxwell 2 is the value play reviewers keep crowning",
                    "body": "Tom's Guide just put it atop a high-end shootout. Planar magnetic drivers reach detail dynamic drivers miss, the 80-hour battery is hard to drain, and at $299 it undercuts the Arctis Nova Elite by half. For pure sound per dollar, Maxwell 2 is the smarter buy at second.",
                },
                {
                    "title": "HyperX Cloud Alpha Wireless still owns the value tier",
                    "body": "Sixth overall but the battery life still embarrasses pricier rivals and the comfort holds up over long sessions. When budget leads the decision, this is the headset I point people toward before anything else.",
                },
            ],
        },
        "zh-tw": {
            "commentary": (
                "六月開頭耳機排序原封不動，頂端的張力跟我整個月標的那個一樣。\n\n"
                "SteelSeries Arctis Nova Pro Wireless 守第一，因為它是這個分類最全能的選擇，可換式雙電池系統等於零停機，雙無線連線涵蓋每個平台，主動降噪在遊戲耳機形態裡還是最強。這份全能的完整度是它穩坐我預設推薦的原因。\n\n"
                "Audeze Maxwell 2 第二，差一點點，CP 值的論點喊得很大聲，Tom's Guide 剛把它推上高階對決冠軍，平面振膜給出動圈做不到的細節，80 小時電力是真的很難榨乾，NT$9,000 出頭只要 Arctis Nova Elite 一半的錢。聲音擺第一又不需要可換電池底座的人，Maxwell 2 是更聰明的花法。\n\n"
                "Turtle Beach Stealth Pro II 守第三當均衡無線選擇，Logitech G Pro X 2 Lightspeed 第四靠競技血統。\n\n"
                "講真的 HyperX Cloud Alpha Wireless 第六還是 CP 值冠軍，電力到現在還是讓更貴的對手難堪。\n\n"
                "這禮拜沒有東西出來重排頂端，所以六月的判讀一樣。要完整方案選 Arctis Nova Pro Wireless，要發燒聲音又合理價選 Maxwell 2，預算決定一切就 HyperX。"
            ),
            "highlights": [
                {
                    "title": "Arctis Nova Pro Wireless 還是最完整的方案",
                    "body": "可換雙電池零停機、雙無線吃下每個平台、遊戲形態裡頂級的 ANC。這份全能的完整度讓它守第一，也是想用一支耳機搞定一切的人的預設推薦。",
                },
                {
                    "title": "Audeze Maxwell 2 是評測一直加冕的 CP 值之選",
                    "body": "Tom's Guide 剛把它推上高階對決冠軍。平面振膜摸到動圈漏掉的細節，80 小時電力難榨乾，NT$9,000 出頭只要 Arctis Nova Elite 一半。論每塊錢的聲音，Maxwell 2 是第二名更聰明的買法。",
                },
                {
                    "title": "HyperX Cloud Alpha Wireless 還是穩坐 CP 值層",
                    "body": "總排第六，但電力到現在還是讓更貴的對手難堪，長時間配戴的舒適也撐得住。預算掛帥的時候，這支是我第一個推給人的。",
                },
            ],
        },
    },
    "best-mechanical-keyboards.json": {
        "references": [
            {
                "title": "Best Hall effect keyboards in 2026: the fastest, most customizable keyboards for competitive gaming",
                "url": "https://www.pcgamer.com/hardware/gaming-keyboards/best-hall-effect-keyboards/",
                "source": "PC Gamer",
            },
            {
                "title": "Wooting 80HE Review 2026: 8KHz Hall Effect Gaming Keyboard Tested",
                "url": "https://levelupblogs.com/review/wooting-80he-keyboard-review/",
                "source": "Level Up Blogs",
            },
            {
                "title": "Wooting 60HE & 80HE Guide: The Hall Effect Gaming Standard (2026)",
                "url": "https://mkbguide.com/blog/wooting-60he-80he-guide",
                "source": "MKB Guide",
            },
        ],
        "en": {
            "commentary": (
                "June opens with the keyboard order holding, and Wooting still owns the front of the grid for one concrete reason. "
                "The Wooting 60HE keeps first because its Lekker Hall Effect switches with the most mature Rapid Trigger implementation cut counter-strafe time measurably, reviewers this year clocked roughly a 26 percent reduction versus traditional switches, from about 82ms down to 61ms. "
                "That is a real competitive edge in CS2 and Valorant, and it is why the 60HE remains the most popular board in the CS2 pro scene. "
                "The Wooting 80HE holds second, pushing 8000 Hz polling that approaches the physical limit of how fast a keypress can register, and the Wootility software is still the easiest analog tooling for a newcomer. "
                "SteelSeries Apex Pro TKL stays third as the mainstream Hall Effect alternative with OmniPoint, Keychron Q1 Pro keeps fourth as the enthusiast build-quality and wireless pick. "
                "NuPhy Field75 HE at fifth remains the value Hall Effect entry that undercuts the Wootings without giving up rapid trigger. "
                "Nothing launched this week reorders the front, so the June verdict is steady. Wooting 60HE for competitive FPS, 80HE if you want the bigger layout and 8K polling, Apex Pro for the polished mainstream experience, Keychron Q1 Pro when you want a heavy custom-feel board with wireless."
            ),
            "highlights": [
                {
                    "title": "Wooting 60HE keeps the competitive crown on measured latency",
                    "body": "Lekker Hall Effect switches with the most mature Rapid Trigger cut counter-strafe time roughly 26 percent, from about 82ms to 61ms in testing. That measurable edge in CS2 and Valorant keeps the 60HE first and the most popular board in the pro scene.",
                },
                {
                    "title": "Wooting 80HE pushes the polling ceiling at second",
                    "body": "8000 Hz polling approaches the physical limit of how fast a keypress can register, and the Wootility remains the easiest analog software for a newcomer. If you want the larger layout with the same rapid trigger pedigree, the 80HE is the pick.",
                },
                {
                    "title": "NuPhy Field75 HE is the value Hall Effect entry",
                    "body": "Fifth overall and it undercuts both Wootings while keeping full rapid trigger support. For a player who wants analog magnetic switches without the flagship price, this is the smart on-ramp into Hall Effect gaming.",
                },
            ],
        },
        "zh-tw": {
            "commentary": (
                "六月開頭鍵盤排序守住，Wooting 還是稱霸前段，原因很具體。\n\n"
                "Wooting 60HE 守第一，因為它的 Lekker 霍爾效應軸加上最成熟的 Rapid Trigger 實作，能實測縮短 counter-strafe 時間，今年評測量到大約比傳統軸快 26%，從約 82ms 降到 61ms。這在 CS2 跟 Valorant 是真實的競技優勢，也是 60HE 還是 CS2 職業圈最熱門板子的原因。\n\n"
                "Wooting 80HE 守第二，推 8000 Hz 回報率，逼近一次按鍵能被偵測的物理極限，Wootility 軟體對新手還是最好上手的類比工具。\n\n"
                "SteelSeries Apex Pro TKL 第三當主流霍爾替代，靠 OmniPoint。Keychron Q1 Pro 守第四當玩家做工跟無線之選，台灣賣大概 NT$6,000 上下，鋁殼手感扎實。\n\n"
                "老實說 NuPhy Field75 HE 第五還是 CP 值霍爾入門，價格壓在兩台 Wooting 之下又沒放掉 rapid trigger。\n\n"
                "這禮拜沒有東西出來重排前段，所以六月結論很穩。競技 FPS 選 Wooting 60HE，要大配列加 8K 回報選 80HE，要打磨好的主流體驗選 Apex Pro，要有客製手感的重磅板加無線就 Keychron Q1 Pro。"
            ),
            "highlights": [
                {
                    "title": "Wooting 60HE 靠實測延遲守住競技王冠",
                    "body": "Lekker 霍爾軸加最成熟的 Rapid Trigger，把 counter-strafe 時間縮短大約 26%，測試裡從約 82ms 降到 61ms。這個在 CS2 跟 Valorant 量得出來的優勢讓 60HE 守第一，也是職業圈最熱門的板子。",
                },
                {
                    "title": "Wooting 80HE 第二把回報率天花板往上推",
                    "body": "8000 Hz 回報率逼近一次按鍵能被偵測的物理極限，Wootility 對新手還是最好上手的類比軟體。想要大配列又一樣的 rapid trigger 血統，選 80HE。",
                },
                {
                    "title": "NuPhy Field75 HE 是 CP 值霍爾入門",
                    "body": "總排第五，價格壓在兩台 Wooting 之下又保留完整 rapid trigger。想要類比磁軸又不想付旗艦價的玩家，這是進霍爾遊戲最聰明的入門。",
                },
            ],
        },
    },
    "best-portable-power-stations.json": {
        "references": [
            {
                "title": "The Best Portable Power Stations of 2026 | Tested by GearJunkie",
                "url": "https://gearjunkie.com/technology/best-portable-power-stations",
                "source": "GearJunkie",
            },
            {
                "title": "Best Portable Power Stations of 2026, Tested and Reviewed",
                "url": "https://www.outdoorlife.com/gear/best-portable-power-stations/",
                "source": "Outdoor Life",
            },
            {
                "title": "Best Big Power Stations of 2026: Tested & Ranked",
                "url": "https://www.thesolarlab.com/how-tos/best-big-power-stations-2025",
                "source": "The Solar Lab",
            },
        ],
        "en": {
            "commentary": (
                "June starts and the power-station order holds, with the top three separated by margins thinner than most buyers will ever notice. "
                "The EcoFlow Delta 3 Plus keeps first because it handles nearly every scenario from camping to home backup with a sub-10ms switchover that protects sensitive gear, 1kWh of capacity expandable to 5kWh, and five fast recharge paths including AC, solar, and the 800W alternator charger. "
                "X-Stream charging is still the fastest in the class and that flexibility is why it stays my default. "
                "The Bluetti Elite 200 V2 sits second and remains the performance-per-dollar standout, testers measured 94 percent efficiency, it packs a 2,073Wh battery and a 2,600W inverter, and it usually lands under $800. "
                "If you want the most usable watt-hours for the money, this is the buy. "
                "The Anker Solix C2000 Gen 2 holds third on Anker's InfiniPower longevity and the support that reviewers consistently rate above EcoFlow and Jackery. "
                "EcoFlow Delta Pro 3 stays fourth as the high-capacity home-backup anchor, and the Anker C1000 Gen 2 at seventh still charges 0 to 100 in 49 minutes. "
                "With summer storm and camping season opening, demand is climbing but no new launch reorders the front. June verdict, Delta 3 Plus for all-around flexibility, Elite 200 V2 for value, Solix C2000 for longevity and support."
            ),
            "highlights": [
                {
                    "title": "EcoFlow Delta 3 Plus stays the all-around default",
                    "body": "Sub-10ms switchover protects sensitive gear, 1kWh expands to 5kWh, and five recharge paths including the 800W alternator cover every scenario. X-Stream charging is still the fastest in class, which keeps it first as summer backup season opens.",
                },
                {
                    "title": "Bluetti Elite 200 V2 owns performance per dollar",
                    "body": "Testers measured 94 percent efficiency on a 2,073Wh battery with a 2,600W inverter, usually under $800. For the most usable watt-hours per dollar this is the standout, and it holds second comfortably heading into camping season.",
                },
                {
                    "title": "Anker Solix C2000 Gen 2 wins on longevity and support",
                    "body": "InfiniPower battery longevity plus an after-sales reputation reviewers rate above EcoFlow and Jackery keep it third. For a buyer who plans to keep one unit for a decade, the Anker is the low-worry long-term pick.",
                },
            ],
        },
        "zh-tw": {
            "commentary": (
                "六月開頭行動電源站排序守住，前三名的差距比大多數買家會察覺到的還薄。\n\n"
                "EcoFlow Delta 3 Plus 守第一，因為它從露營到家庭備援幾乎甚麼場景都吃得下，切換時間低於 10 毫秒保護敏感設備，1kWh 容量可擴充到 5kWh，五種快充路徑包含市電、太陽能跟 800W 車充。X-Stream 快充還是同級最快，這份彈性是它穩坐我預設的原因。\n\n"
                "Bluetti Elite 200 V2 第二，還是每塊錢效能的亮點，實測效率 94%，塞了 2,073Wh 電池加 2,600W 逆變器，常常 NT$24,000 上下就買得到。想要每塊錢拿到最多可用瓦時，就買這台。\n\n"
                "Anker Solix C2000 Gen 2 守第三，靠 Anker 的 InfiniPower 壽命，加上評測一致給比 EcoFlow 跟 Jackery 更高的售後評價。\n\n"
                "EcoFlow Delta Pro 3 守第四當大容量家庭備援定錨，Anker C1000 Gen 2 第七還是 49 分鐘 0 到 100。\n\n"
                "夏天颱風跟露營季開跑，需求在爬但沒有新品重排前段。台灣這季用得到，颱風停電一台撐冰箱加路由器很實在。六月結論，全方位彈性選 Delta 3 Plus，CP 值選 Elite 200 V2，壽命跟售後選 Solix C2000。"
            ),
            "highlights": [
                {
                    "title": "EcoFlow Delta 3 Plus 守住全方位預設",
                    "body": "切換低於 10 毫秒保護敏感設備，1kWh 可擴到 5kWh，五種快充路徑含 800W 車充涵蓋每個場景。X-Stream 快充還是同級最快，夏天備援季開跑它守第一。",
                },
                {
                    "title": "Bluetti Elite 200 V2 稱霸每塊錢效能",
                    "body": "實測 2,073Wh 電池效率 94%，配 2,600W 逆變器，常常 NT$24,000 上下入手。每塊錢拿到最多可用瓦時這台是亮點，進露營季穩守第二。",
                },
                {
                    "title": "Anker Solix C2000 Gen 2 贏在壽命跟售後",
                    "body": "InfiniPower 電池壽命加上評測一致給比 EcoFlow 跟 Jackery 更高的售後評價，守第三。打算一台用十年的買家，Anker 是最少煩惱的長線選擇。",
                },
            ],
        },
    },
    "best-smart-pet-feeders.json": {
        "references": [
            {
                "title": "Petlibro Granary Smart Camera Feeder Review 2026",
                "url": "https://availpet.com/petlibro-granary-smart-camera-feeder/",
                "source": "Avail Pet",
            },
            {
                "title": "Best Smart Pet Feeders 2026: Petlibro vs Pawsync vs PETKIT Comparison",
                "url": "https://smarthomeahead.com/best-smart-pet-feeders-2026-petlibro-vs-pawsync-vs-petkit-comparison/",
                "source": "Smart Home Ahead",
            },
            {
                "title": "Petkit Automatic Feeder vs Petlibro 2026: Best Tested",
                "url": "https://www.infomastero.online/petkit-automatic-feeder-vs-petlibro/",
                "source": "Infomastero",
            },
        ],
        "en": {
            "commentary": (
                "June opens and the feeder order holds, because the thing that decides this category, does it dispense on time every time, has not changed. "
                "The Petlibro Granary Camera keeps first because it simply feeds when it is supposed to, the twin-turbine motor is documented as roughly 4x more jam-resistant than single-auger designs, and it keeps dispensing on D-cell backup through a power cut. "
                "At around $90 it carries the best reliability-to-price ratio in the category, and it has the best automatic feeder nods from PCMag and Wirecutter to back it. "
                "The Petkit Yumshare Dual-Hopper 2 stays second as the premium multi-pet pick, the dual-flavor hoppers, sharp 1080p camera, and AI features are the right answer for multi-pet homes that need two food types and real-time interaction. "
                "Petkit wins on build quality, Petlibro wins on app friendliness, and that split is exactly why these two trade the top. "
                "The Petlibro Polar Wet Food at third stays the answer for cats on wet diets, and the Petlibro One RFID at fifth still owns strict multi-pet portion control. "
                "Nothing shipped this week reorders the list. June verdict, Granary Camera for reliability and value, Yumshare Dual-Hopper 2 for premium multi-pet, Polar for wet food, One RFID when one cat must not eat another's portion."
            ),
            "highlights": [
                {
                    "title": "Petlibro Granary Camera wins where it counts, reliability",
                    "body": "The twin-turbine motor is documented as roughly 4x more jam-resistant than single-auger designs and keeps dispensing on D-cell backup through a power cut. At about $90 with best-feeder nods from PCMag and Wirecutter, it stays first on the reliability-to-price ratio.",
                },
                {
                    "title": "Petkit Yumshare Dual-Hopper 2 is the premium multi-pet pick",
                    "body": "Dual-flavor hoppers, a sharp 1080p camera, and AI interaction make it the right answer for multi-pet homes needing two food types. Petkit leads on build quality, which keeps it a close second behind the Granary.",
                },
                {
                    "title": "The Petlibro-Petkit split comes down to app versus build",
                    "body": "Reviewers keep landing on the same divide, Petkit wins build quality, Petlibro wins app friendliness and dispensing consistency. That clean split is why these two keep trading the top two spots month after month.",
                },
            ],
        },
        "zh-tw": {
            "commentary": (
                "六月開頭餵食器排序守住，因為決定這個分類的關鍵，能不能每次準時出飼料，沒有變。\n\n"
                "Petlibro Granary Camera 守第一，因為它就是該餵的時候會餵，雙渦輪馬達被記錄為比單絞龍設計大約耐卡 4 倍，停電時靠 D 型電池備援還是照樣出飼料。台灣賣大概 NT$2,800 上下，它的可靠度對價格比是分類裡最好的，還有 PCMag 跟 Wirecutter 的最佳餵食器背書。\n\n"
                "Petkit Yumshare Dual-Hopper 2 守第二當高階多寵之選，雙料倉、清晰 1080p 鏡頭、AI 功能，正好是需要兩種飼料加即時互動的多寵家庭的答案。\n\n"
                "講真的，Petkit 贏在做工，Petlibro 贏在 App 好用，這個分野正是這兩家輪流佔頂端的原因。\n\n"
                "Petlibro Polar 濕食款第三還是吃濕食貓咪的答案，Petlibro One RFID 第五還是稱霸嚴格多寵分食控制，多貓家裡防一隻偷吃另一隻那份就靠它。\n\n"
                "這禮拜沒有東西出來重排清單。六月結論，可靠度跟 CP 值選 Granary Camera，高階多寵選 Yumshare Dual-Hopper 2，濕食選 Polar，要嚴格分食選 One RFID。"
            ),
            "highlights": [
                {
                    "title": "Petlibro Granary Camera 贏在最關鍵的可靠度",
                    "body": "雙渦輪馬達被記錄為比單絞龍大約耐卡 4 倍，停電靠 D 型電池備援照樣出飼料。大約 NT$2,800 加上 PCMag 跟 Wirecutter 最佳餵食器背書，靠可靠度對價格比守第一。",
                },
                {
                    "title": "Petkit Yumshare Dual-Hopper 2 是高階多寵之選",
                    "body": "雙料倉、清晰 1080p 鏡頭、AI 互動，正是需要兩種飼料的多寵家庭的答案。Petkit 做工領先，讓它緊咬 Granary 守第二。",
                },
                {
                    "title": "Petlibro 跟 Petkit 的分野在 App 對做工",
                    "body": "評測一直落在同一個分野，Petkit 贏做工，Petlibro 贏 App 好用跟出飼料穩定度。這個乾淨的分野就是兩家月月輪流佔前二的原因。",
                },
            ],
        },
    },
    "best-vpn-services.json": {
        "references": [
            {
                "title": "The 3 Best VPNs For Privacy of 2026",
                "url": "https://www.rtings.com/vpn/reviews/best/privacy",
                "source": "RTINGS",
            },
            {
                "title": "Proton VPN vs Mullvad VPN comparison 2026",
                "url": "https://vpnpro.com/vpn-comparison/mullvad-vs-proton-vpn/",
                "source": "VPNpro",
            },
            {
                "title": "Best VPN 2026: 6 Audited Picks Ranked & Compared",
                "url": "https://bitsfrombytes.com/best-vpn-picks-ranked-independent-cybersecurity/",
                "source": "Bits from Bytes",
            },
        ],
        "en": {
            "commentary": (
                "June opens with the VPN order holding, and the one piece of live news this week reinforces why Mullvad keeps first rather than threatening it. "
                "RTINGS still names Mullvad the best tested VPN for privacy, it requires no account or email, accepts cash and crypto, and its no-logs stance has survived an actual police raid. "
                "A May disclosure about exit-IP fingerprinting got attention, and what I care about is the response, Mullvad's co-founder publicly acknowledged it and confirmed a fix was in testing. "
                "That transparency is the behavior I want from a privacy provider, and it keeps Mullvad at the top with the flat five-euro pricing intact. "
                "Proton VPN holds second on Swiss jurisdiction, four independent no-logs audits, Secure Core multi-hop, and a genuinely usable free tier, it remains the best pick for privacy-first users who also want polish. "
                "NordVPN stays third as the best all-rounder for most people, six independent audits and NordLynx speeds above 1,200 Mbps on nearby servers make it the practical mainstream choice. "
                "IVPN holds fourth on its own minimalist no-logs ethos, ExpressVPN fifth on speed and ease. "
                "The June verdict is steady. Mullvad for maximum anonymity, Proton for privacy plus usability, NordVPN for speed and streaming, IVPN for the minimalist privacy purist."
            ),
            "highlights": [
                {
                    "title": "Mullvad's response to the May disclosure keeps it first",
                    "body": "A May exit-IP fingerprinting disclosure drew attention, and Mullvad's co-founder publicly acknowledged it with a fix in testing. That transparency, plus the raid-proven no-logs stance and flat five-euro pricing, is exactly why it holds the privacy crown.",
                },
                {
                    "title": "Proton VPN pairs Swiss jurisdiction with real usability",
                    "body": "Four independent no-logs audits, Secure Core multi-hop, and a genuinely usable free tier under Swiss law keep it second. For privacy-first users who also want a polished app, Proton is the strongest all-round privacy play.",
                },
                {
                    "title": "NordVPN stays the practical pick for most people",
                    "body": "Six independent audits, the most of any consumer VPN, plus NordLynx speeds above 1,200 Mbps on nearby servers and reliable streaming. For users who want one VPN that just works fast everywhere, Nord stays the mainstream choice at third.",
                },
            ],
        },
        "zh-tw": {
            "commentary": (
                "六月開頭 VPN 排序守住，這禮拜唯一一則即時新聞反而幫 Mullvad 守第一加了分。\n\n"
                "RTINGS 還是把 Mullvad 列為實測最佳隱私 VPN，它不要帳號不要 email，收現金跟加密貨幣，無紀錄政策還撐過真正的警方搜索。\n\n"
                "五月有一則關於 exit-IP 指紋的揭露引起注意，我在意的是它的回應，Mullvad 共同創辦人公開承認，並確認修正正在測試中。這種透明度正是我要一個隱私供應商該有的行為，也讓 Mullvad 守在頂端，每月五歐元的均一價維持不變。\n\n"
                "Proton VPN 守第二，靠瑞士司法管轄、四次獨立無紀錄稽核、Secure Core 多跳、加上真的能用的免費方案，對既要隱私又要打磨體驗的人還是最佳之選。\n\n"
                "NordVPN 守第三當大多數人的最佳全能，六次獨立稽核加 NordLynx 在近端伺服器破 1,200 Mbps，是務實的主流選擇。\n\n"
                "老實說 IVPN 守第四靠自己的極簡無紀錄理念，ExpressVPN 第五靠速度跟易用。\n\n"
                "六月結論很穩。要最高匿名選 Mullvad，要隱私加易用選 Proton，要速度跟串流選 NordVPN，極簡隱私純粹派選 IVPN。"
            ),
            "highlights": [
                {
                    "title": "Mullvad 對五月揭露的回應讓它守第一",
                    "body": "五月一則 exit-IP 指紋揭露引起注意，Mullvad 共同創辦人公開承認，修正正在測試。這份透明度加上撐過搜索的無紀錄政策跟每月五歐元均一價，正是它守住隱私王冠的原因。",
                },
                {
                    "title": "Proton VPN 把瑞士管轄配上真正的易用",
                    "body": "四次獨立無紀錄稽核、Secure Core 多跳、加上真的能用的免費方案，在瑞士法律下守第二。既要隱私又要打磨好的 App 的人，Proton 是最強的全能隱私之選。",
                },
                {
                    "title": "NordVPN 還是大多數人的務實之選",
                    "body": "六次獨立稽核是消費級 VPN 最多，加上 NordLynx 近端伺服器破 1,200 Mbps 跟穩定串流。想要一個到哪都快又能用的 VPN，Nord 守第三當主流選擇。",
                },
            ],
        },
    },
}


def main():
    for name, c in CONTENT.items():
        data, p = load(name)
        rankings = json.loads(json.dumps(last_rankings(data)))  # deep copy, carry forward
        entry = {
            "date": DATE,
            "rankings": rankings,
            "references": c["references"],
            "i18n": {
                "en": {
                    "commentary": c["en"]["commentary"],
                    "highlights": c["en"]["highlights"],
                },
                "zh-tw": {
                    "commentary": c["zh-tw"]["commentary"],
                    "highlights": c["zh-tw"]["highlights"],
                },
            },
        }
        upsert(data, entry)
        save(p, data)
        print("updated", name)


if __name__ == "__main__":
    main()
