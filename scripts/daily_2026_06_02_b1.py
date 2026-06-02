"""2026-06-02 daily update — Batch 1: Tech/AI (7 files)"""
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


def build_3d_printers():
    d, p = load("best-3d-printers.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Bambu Lab Launches A2L: Creative Playground. Extra Large.", "url": "https://www.prnewswire.com/news-releases/bambu-lab-launches-a2l-creative-playground-extra-large-302785609.html", "source": "PR Newswire"},
            {"title": "Bambu Lab Launches the A2L: A \"Creative Playground\" with Larger Build Volume and Modular Add-Ons", "url": "https://www.3dnatives.com/en/bambu-lab-launches-the-a2l-01062026/", "source": "3Dnatives"},
            {"title": "Bambu Lab teases new A2L 3D printer — June 1 launch hints at a massive, budget-friendly bed slinger", "url": "https://www.tomshardware.com/3d-printing/bambu-lab-teases-new-a2l-3d-printer-june-1-launch-confirmed", "source": "Tom's Hardware"},
        ],
        "i18n": {
            "en": {
                "commentary": "Bambu Lab just reminded everyone why it owns the top of this list. On June 1 the company launched the A2L, a large-format A-series bed slinger with a 330 x 320 x 325 mm build volume, roughly 105 percent more printing room than the 256 mm-class machines most hobbyists own. It starts at 379 EUR, runs below 49 dB in silent mode, and accepts up to four AMS units for as many as 19 colors in PLA and PETG. That kind of release cadence is exactly why Bambu holds four of our top five spots.\n\nThe Bambu Lab P2S Combo stays at rank 1 with a 9.4 overall, and nothing in the A2L launch changes that verdict. The A2L is built for large, family-friendly creative projects at a budget price, while the P2S Combo remains the machine I recommend for anyone who wants the best balance of print quality, speed, and multicolor reliability in a CoreXY frame. Its 9.5 print quality and 9.5 multicolor scores are the reason it beats faster but rougher rivals.\n\nThe X1-Carbon at rank 2 is still the workhorse for engineering materials, and the new H2D at rank 3 covers the dual-nozzle, large-format niche that the A2L now complements from below. Prusa holds rank 4 with the Core One, the strongest non-Bambu CoreXY on the market and the pick for buyers who value open ecosystem and repairability.\n\nThe practical takeaway: the A2L widens Bambu's lineup at the affordable end without disturbing the premium order. If you want large prints without splitting and gluing, watch the A2L, but the P2S Combo is still the printer to buy for all-around performance heading into summer.",
                "highlights": [
                    {"title": "Bambu Lab A2L Launches With Extra-Large Build Volume", "body": "Released June 1, the A2L brings a 330 x 320 x 325 mm build volume, 105 percent more print space than standard 256 mm machines, starting at 379 EUR. It runs below 49 dB in silent mode and supports up to four AMS units for 19 colors, widening Bambu's affordable lineup without touching the premium tier."},
                    {"title": "P2S Combo Stays the All-Around Pick at Rank 1", "body": "With 9.5 print quality and 9.5 multicolor scores in a proven CoreXY frame, the Bambu Lab P2S Combo remains the machine I recommend for the best balance of quality, speed, and reliable multicolor printing. The A2L targets large-format creative work, not the all-rounder crown."},
                    {"title": "Bambu Dominates Four of the Top Five", "body": "P2S Combo, X1-Carbon, H2D, and P1S hold four of our five top spots. The relentless release pace, now including the A2L, is why no competitor has matched Bambu's ecosystem depth, with Prusa's Core One the strongest open-ecosystem alternative at rank 4."},
                ],
            },
            "zh-tw": {
                "commentary": "Bambu Lab 又一次提醒大家為什麼它穩坐這份榜單的頂端。6 月 1 日他們推出了 A2L，一台大尺寸的 A 系列床身移動式印表機，列印空間 330 x 320 x 325 mm，比大多數玩家手上的 256mm 級機型多出大約 105% 的列印體積。起價 379 歐元，靜音模式下噪音低於 49 分貝，還能串接最多四組 AMS，用 PLA 和 PETG 做到 19 色列印。這種出新機的節奏，正是 Bambu 一口氣佔據前五名四席的原因。\n\n第一名的 Bambu Lab P2S Combo 維持 9.4 總分，A2L 的發表完全沒有動搖這個判斷。A2L 走的是大尺寸、親子創作、平價的路線；P2S Combo 則是我推薦給想要列印品質、速度、多色穩定度三者最佳平衡的人，CoreXY 結構加上 9.5 的列印品質和 9.5 的多色分數，這就是它贏過那些跑很快但表面粗糙對手的關鍵。\n\n第二名的 X1-Carbon 還是工程材料的主力機，第三名的新款 H2D 補上雙噴頭大尺寸這塊，而 A2L 從下方把這個區間補得更完整。Prusa 的 Core One 排第四，是市面上最強的非 Bambu CoreXY 機型，重視開放生態和可維修性的人就選它。\n\n講白一點：A2L 在平價端把 Bambu 的產品線拉得更寬，但完全沒有打亂高階機種的順序。想印大件又不想切割黏合，可以盯著 A2L；但論全方位表現，進入夏天該買的還是 P2S Combo。",
                "highlights": [
                    {"title": "Bambu Lab A2L 發表，超大列印空間", "body": "6 月 1 日上市的 A2L 提供 330 x 320 x 325 mm 列印空間，比標準 256mm 機型多出 105% 體積，起價 379 歐元。靜音模式噪音低於 49 分貝，可串接四組 AMS 達 19 色，在不動到高階機種的前提下把平價產品線拉寬。"},
                    {"title": "P2S Combo 全方位首選，穩坐第一", "body": "9.5 的列印品質加 9.5 的多色分數，搭配成熟的 CoreXY 結構，Bambu Lab P2S Combo 仍是我推薦給想要品質、速度、多色穩定三者最佳平衡的人。A2L 鎖定大尺寸創作，不是來搶全能王冠的。"},
                    {"title": "Bambu 包辦前五名四席", "body": "P2S Combo、X1-Carbon、H2D、P1S 佔據前五名的四席。包括 A2L 在內的密集出機節奏，是沒有對手能追上 Bambu 生態系深度的原因，Prusa Core One 則是第四名最強的開放生態替代選擇。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK 3d-printers")


def build_4k_tvs():
    d, p = load("best-4k-tvs.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "The 6 Best TVs of 2026", "url": "https://www.rtings.com/tv/reviews/best/tvs-on-the-market", "source": "RTINGS.com"},
            {"title": "Best OLED TVs in 2026 tested: Our top picks from LG, Samsung and more", "url": "https://www.tomsguide.com/tvs/oled-tvs/best-oled-tvs", "source": "Tom's Guide"},
            {"title": "Best 65-inch TVs 2026: the top models we've tested", "url": "https://www.whathifi.com/best-buys/the-best-65-inch-tvs", "source": "What Hi-Fi?"},
        ],
        "i18n": {
            "en": {
                "commentary": "The 2026 TV order at the top is settled, and the LG C6 OLED keeps rank 1 because it delivers the most TV for the money of any panel I have tested this year. What Hi-Fi calls it the pick of the latest 65-inch crop, and the reason is its new Alpha 11 Gen 3 processor, which sharpens tone mapping, color management, and upscaling over the C5. PC gamers now get 4K at 165Hz, up from 144Hz, and crucially the C6 launched cheaper than its predecessor. That combination of better picture and lower price is why it beats more expensive flagships on overall value.\n\nThe Samsung S95F at rank 2 remains the outright image-quality champion. RTINGS still rates the S95F as the best TV available, and notably recommends it over the newer S95H because the newer model's gains do not justify the price jump. That is good news for buyers right now: the S95F is the QD-OLED to get, and as the S95H ships the S95F should see better pricing. Its 9.5 panel and 9.5 gaming scores back up the reputation.\n\nThe Sony Bravia 8 II at rank 3 is the pick for film purists who want Sony's processing and tone accuracy. The LG G6 at rank 4 is the wall-mount, brightness-first OLED for bright rooms, and the Sony Bravia 9 at rank 5 anchors the premium mini-LED tier for those who want OLED-rivaling contrast with higher peak brightness.\n\nMy practical advice: the C6 is the smart-money OLED, the S95F is the no-compromise image champion, and with the S95H now on shelves, this is a strong window to find last-generation flagships discounted while the rankings stay stable.",
                "highlights": [
                    {"title": "LG C6 OLED Is the Smart-Money Pick at Rank 1", "body": "The new Alpha 11 Gen 3 processor sharpens tone mapping, color, and upscaling over the C5, and PC gamers get 4K at 165Hz. Critically, the C6 launched cheaper than its predecessor, making it the best picture-per-dollar OLED of 2026 and the reason it tops more expensive flagships."},
                    {"title": "Samsung S95F Remains the Image-Quality Champion", "body": "RTINGS still rates the S95F as the best TV available and recommends it over the newer S95H, whose gains do not justify the price. With 9.5 panel and 9.5 gaming scores, it is the QD-OLED to buy, and S95H availability should improve S95F pricing."},
                    {"title": "New Flagships Mean Discounts on Proven Models", "body": "With Samsung's S95H now shipping after its April reveal, last-generation flagships like the S95F and C-series OLEDs become more attractively priced. The ranking order stays stable, so buyers can chase deals on top-rated 2025-2026 panels without giving up performance."},
                ],
            },
            "zh-tw": {
                "commentary": "2026 年電視榜單頂端的順序已經底定，LG C6 OLED 守住第一名，因為它是我今年測過 CP 值最高的面板。What Hi-Fi 直接稱它是最新一批 65 吋機種裡的首選，理由就是新的 Alpha 11 Gen 3 處理器，色調映射、色彩管理、升頻都比 C5 更精準。PC 玩家現在能跑 4K 165Hz，從原本的 144Hz 升上來，而且更關鍵的是 C6 上市價比前代還便宜。畫質更好、價格更低，這就是它能打贏更貴旗艦的原因。\n\n第二名的 Samsung S95F 仍然是純畫質之王。RTINGS 至今還是把 S95F 評為市面上最好的電視，而且特別建議買 S95F 而不是更新的 S95H，因為新機的提升撐不起那個價差。這對現在想買的人是好消息：S95F 就是該入手的 QD-OLED，而隨著 S95H 上市，S95F 的價格應該會更漂亮。9.5 的面板分和 9.5 的遊戲分撐得起它的名聲。\n\n第三名的 Sony Bravia 8 II 是電影派的首選，要的是 Sony 的影像處理和色調準度。第四名的 LG G6 是主打亮度的壁掛 OLED，適合明亮的客廳；第五名的 Sony Bravia 9 則坐穩高階 mini-LED 這塊，要對比逼近 OLED 又要更高峰值亮度的人選它。\n\n我的實用建議：C6 是精打細算的 OLED 之選，S95F 是不妥協的畫質王者，而隨著 S95H 上架，現在正是撿上一代旗艦折扣的好時機，榜單順序又很穩定。",
                "highlights": [
                    {"title": "LG C6 OLED 精打細算首選，穩坐第一", "body": "全新 Alpha 11 Gen 3 處理器在色調映射、色彩、升頻上全面勝過 C5，PC 玩家還能跑 4K 165Hz。更關鍵的是 C6 上市價比前代便宜，是 2026 年單位畫質最划算的 OLED，這就是它壓過更貴旗艦的原因。"},
                    {"title": "Samsung S95F 仍是純畫質之王", "body": "RTINGS 至今把 S95F 評為市面最佳電視，並建議買它而非更新的 S95H，因為新機提升撐不起價差。9.5 面板分加 9.5 遊戲分，這就是該買的 QD-OLED，而 S95H 上市後 S95F 價格應該更甜。"},
                    {"title": "新旗艦上市，等於舊王降價", "body": "Samsung S95H 在四月發表後現已出貨，S95F 和 C 系列 OLED 這類上一代旗艦的價格會更有吸引力。榜單順序維持穩定，想撿便宜的人可以追頂級 2025-2026 面板的折扣，又不必犧牲表現。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK 4k-tvs")


def build_action_cameras():
    d, p = load("best-action-cameras.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "DJI Osmo Action 6 review: Better than anything GoPro or Insta360 can offer", "url": "https://www.tomsguide.com/cameras-photography/gopro-action-cameras/dji-osmo-action-6-review", "source": "Tom's Guide"},
            {"title": "Insta360 Ace Pro 2 vs DJI Osmo Action 6 (2026)", "url": "https://droneandcam.com/en/post/insta360-ace-pro-2-vs-dji-osmo-action-6-which-action-camera-should-you-choose/", "source": "Drone & Cam"},
            {"title": "Insta360 X6 leak hints at imminent launch – could the updated camera fix the X5's biggest weakness?", "url": "https://www.digitalcameraworld.com/cameras/360-cameras/insta360-x6-leak-hints-at-imminent-launch-could-the-updated-camera-fix-the-x5s-biggest-weakness", "source": "Digital Camera World"},
        ],
        "i18n": {
            "en": {
                "commentary": "The DJI Osmo Action 6 holds rank 1 because it does the thing every action camera buyer actually wants: more capability for less money. Tom's Guide calls it better than anything GoPro or Insta360 can offer, and the spec sheet backs that up. It shoots 8K, survives down to -20C and up to 45C, is waterproof to 20m, and ships with 50GB of built-in storage. The square sensor lets you frame 1:1 and crop to horizontal or vertical after the fact, which is genuinely useful for anyone posting to both YouTube and vertical feeds. And it starts at just $369 for the Essential Combo. That price-to-capability ratio is why it leads.\n\nThe Insta360 Ace Pro 2 at rank 2 was the first action camera to hit 8K, and it remains the choice for low-light shooters thanks to its larger sensor and Leica color science. Side-by-side comparisons through early 2026 show it trading blows with the Action 6, so the gap at the top is genuinely close.\n\nThe GoPro Mission 1 Pro at rank 3 and Hero 13 Black at rank 4 keep GoPro relevant for buyers locked into its mounting ecosystem and editing app. The Insta360 X5 at rank 5 is the 360-degree powerhouse, and worth flagging: a leaked X6 hints at an imminent launch that could fix the X5's weak points, so 360 buyers may want to wait or watch for X5 discounts.\n\nMy verdict stands: the Action 6 is the action camera to buy in 2026, the Ace Pro 2 is the low-light alternative, and the X-series is where you go for immersive 360 capture.",
                "highlights": [
                    {"title": "DJI Osmo Action 6 Leads on Capability Per Dollar", "body": "8K video, waterproof to 20m, -20C to 45C operation, 50GB built-in storage, and a square sensor for flexible 1:1 framing, all starting at $369. Tom's Guide calls it better than anything GoPro or Insta360 offers, and that price-to-capability ratio is exactly why it holds rank 1."},
                    {"title": "Insta360 Ace Pro 2 Is the Low-Light Alternative", "body": "The first action camera to reach 8K, the Ace Pro 2 trades blows with the Action 6 in 2026 comparisons and pulls ahead in low light thanks to its larger sensor and Leica color science. It stays the rank-2 pick for shooters who prioritize image quality in dim conditions."},
                    {"title": "Insta360 X6 Leak Signals a 360 Refresh Is Coming", "body": "A leaked X6 hints at an imminent launch that could address the X5's biggest weakness. The X5 holds rank 5 as the current 360 powerhouse, but immersive-capture buyers may want to watch for the X6 reveal or wait for X5 price drops."},
                ],
            },
            "zh-tw": {
                "commentary": "DJI Osmo Action 6 守住第一名，因為它做到每個運動相機買家真正想要的事：用更少的錢換更多的能力。Tom's Guide 直接說它比 GoPro 或 Insta360 拿得出的任何機型都好，規格表也撐得起這句話。它能拍 8K，耐受 -20C 到 45C，防水 20 公尺，內建 50GB 儲存空間。方形感光元件讓你用 1:1 構圖，事後再裁成橫式或直式，對同時經營 YouTube 和直式短影音的人非常實用。而 Essential Combo 起價只要 369 美元。這個價格對能力的比值，就是它領先的原因。\n\n第二名的 Insta360 Ace Pro 2 是第一台做到 8K 的運動相機，靠著更大的感光元件和徠卡色彩科學，仍然是弱光拍攝的首選。2026 年初的多次對比顯示它和 Action 6 互有勝負，所以頂端這個差距其實很接近。\n\n第三名的 GoPro Mission 1 Pro 和第四名的 Hero 13 Black 讓 GoPro 對已經卡在它配件生態和剪輯 App 裡的用戶仍有吸引力。第五名的 Insta360 X5 是 360 度的怪獸機，而且值得提一下：外流的 X6 暗示即將上市，可能會補上 X5 的弱點，所以想買 360 的人可以再等等，或盯著 X5 的折扣。\n\n我的結論不變：Action 6 是 2026 年該買的運動相機，Ace Pro 2 是弱光的替代選擇，要沉浸式 360 拍攝就看 X 系列。",
                "highlights": [
                    {"title": "DJI Osmo Action 6 每塊錢買到最多能力", "body": "8K 影片、防水 20 公尺、-20C 到 45C 運作、內建 50GB、方形感光元件支援彈性 1:1 構圖，全部從 369 美元起跳。Tom's Guide 說它比 GoPro 或 Insta360 任何機型都好，這個價格對能力的比值正是它穩坐第一的原因。"},
                    {"title": "Insta360 Ace Pro 2 是弱光替代選擇", "body": "第一台做到 8K 的運動相機，在 2026 年的對比中與 Action 6 互有勝負，靠更大感光元件和徠卡色彩在弱光下勝出。對在昏暗環境下重視畫質的人，它穩坐第二。"},
                    {"title": "Insta360 X6 外流，360 改款將至", "body": "外流的 X6 暗示即將上市，可能補上 X5 最大的弱點。X5 以目前的 360 怪獸機身分守住第五名，但想要沉浸式拍攝的人可以盯著 X6 發表，或等 X5 降價。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK action-cameras")


def build_ai_chatbots():
    d, p = load("best-ai-chatbots.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Google updates its Gemini app to take on ChatGPT and Claude at IO 2026", "url": "https://techcrunch.com/2026/05/19/google-updates-its-gemini-app-to-take-on-chatgpt-and-claude-at-io-2026/", "source": "TechCrunch"},
            {"title": "ChatGPT still dominates, but Gemini and Claude are gaining ground", "url": "https://www.techzine.eu/news/applications/141503/chatgpt-still-dominates-but-gemini-and-claude-are-gaining-ground/", "source": "Techzine"},
            {"title": "Claude vs ChatGPT vs Copilot vs Gemini: 2026 Enterprise Guide", "url": "https://intuitionlabs.ai/articles/claude-vs-chatgpt-vs-copilot-vs-gemini-enterprise-comparison", "source": "IntuitionLabs"},
        ],
        "i18n": {
            "en": {
                "commentary": "ChatGPT holds rank 1 because it remains the default AI for most people and continues to lead on ecosystem reach. Even as challengers close the gap, ChatGPT still dominates everyday usage, and the surrounding platform, custom GPTs, the API, deep app integrations, keeps it stickier than any rival. Its 9.7 ecosystem score is the highest on this list and the single biggest reason it stays on top.\n\nThe interesting story this week is the chase. At Google I/O 2026, Google overhauled the Gemini app with a Daily Brief feature, a redesigned interface, the new Gemini Omni video model, and a personal agent called Gemini Spark. The goal is clear: turn Gemini from a chatbot into an all-purpose AI hub. Usage data shows Gemini and Claude gaining ground, reportedly around 14.4 percent and 8.6 percent of measured AI tool time, so the rank 2 and rank 3 positions for Claude and Gemini are well earned and tightening.\n\nThere is also a platform shift worth flagging. Apple is reportedly redesigning Siri in iOS 27 to work as a full chatbot, letting users pick Gemini, ChatGPT, or Claude as the backend, which ends the OpenAI-exclusive arrangement. With WWDC 2026 running June 8 to 12, that choice could reshape default AI exposure for hundreds of millions of iPhone users.\n\nMy verdict: ChatGPT is still the safe default for breadth and ecosystem, Claude leads for careful reasoning and writing, and Gemini is the fastest-improving all-rounder. The order at the top holds, but the gap is narrower than it has ever been heading into WWDC.",
                "highlights": [
                    {"title": "ChatGPT Stays No. 1 on Ecosystem and Default Usage", "body": "With a 9.7 ecosystem score, the highest on this list, ChatGPT remains the default AI for most people. Custom GPTs, the API, and deep app integrations keep it stickier than any rival even as Gemini and Claude close the capability gap."},
                    {"title": "Google I/O Supercharges Gemini Into an AI Hub", "body": "At I/O 2026 Google added a Daily Brief, a redesigned interface, the Gemini Omni video model, and a personal agent called Gemini Spark. The push to turn Gemini into an all-purpose hub is paying off, with reported usage around 14.4 percent and rank 3 firmly held."},
                    {"title": "Apple's Siri Overhaul Could Reshuffle Default AI", "body": "Apple is reportedly rebuilding Siri in iOS 27 as a full chatbot that lets users choose Gemini, ChatGPT, or Claude as the backend, ending OpenAI exclusivity. With WWDC 2026 on June 8 to 12, that choice could shift default AI exposure for hundreds of millions of iPhone users."},
                ],
            },
            "zh-tw": {
                "commentary": "ChatGPT 守住第一名，因為它仍然是大多數人的預設 AI，生態系觸及範圍也持續領先。就算挑戰者步步進逼，ChatGPT 在日常使用上依然主導，加上周邊的客製 GPT、API、深度 App 整合，黏著度比任何對手都高。9.7 的生態系分數是全榜最高，這就是它穩坐第一最大的單一原因。\n\n這週最有看頭的是後面的追趕戰。在 Google I/O 2026 上，Google 大改 Gemini App，加入 Daily Brief 每日簡報、全新介面、新的 Gemini Omni 影片模型，還有一個叫 Gemini Spark 的個人代理。目標很明確：把 Gemini 從聊天機器人變成全方位 AI 中樞。使用數據顯示 Gemini 和 Claude 都在搶地盤，據報約佔測得 AI 工具時間的 14.4% 和 8.6%，所以 Claude 第二、Gemini 第三的位置很實至名歸，而且差距正在縮小。\n\n還有一個平台層級的變化值得提：據報 Apple 正在把 iOS 27 的 Siri 改造成完整的聊天機器人，讓使用者自選 Gemini、ChatGPT 或 Claude 當後端，等於結束跟 OpenAI 的獨家綁定。WWDC 2026 在 6/8 到 6/12 舉行，這個選擇權可能重新洗牌數億 iPhone 用戶接觸到的預設 AI。\n\n我的判斷：論廣度和生態系，ChatGPT 還是最安全的預設選擇；論嚴謹推理和寫作，Claude 領先；Gemini 則是進步最快的全能型。頂端順序維持，但進入 WWDC 前這個差距比以往任何時候都更小。",
                "highlights": [
                    {"title": "ChatGPT 靠生態系與預設使用穩坐第一", "body": "9.7 的生態系分數是全榜最高，ChatGPT 仍是大多數人的預設 AI。客製 GPT、API、深度 App 整合讓它的黏著度勝過任何對手，即使 Gemini 和 Claude 正在拉近能力差距。"},
                    {"title": "Google I/O 把 Gemini 升級成 AI 中樞", "body": "在 I/O 2026 上，Google 加入 Daily Brief、全新介面、Gemini Omni 影片模型，以及叫 Gemini Spark 的個人代理。把 Gemini 變成全方位中樞的策略奏效，據報使用率約 14.4%，第三名穩穩守住。"},
                    {"title": "Apple Siri 大改，可能重洗預設 AI 版圖", "body": "據報 Apple 正在把 iOS 27 的 Siri 重建成完整聊天機器人，讓使用者自選 Gemini、ChatGPT 或 Claude 當後端，結束 OpenAI 獨家。WWDC 2026 在 6/8 到 6/12，這個選擇權可能改變數億 iPhone 用戶接觸的預設 AI。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK ai-chatbots")


def build_ai_coding_assistants():
    d, p = load("best-ai-coding-assistants.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Claude Code vs. Cursor vs. Codex vs. Antigravity — six months in", "url": "https://thenewstack.io/claude-code-vs-cursor-vs-codex-vs-antigravity-2026/", "source": "The New Stack"},
            {"title": "Cursor, Claude Code, and Codex are merging into one AI coding stack nobody planned", "url": "https://thenewstack.io/ai-coding-tool-stack/", "source": "The New Stack"},
            {"title": "The AI Coding Assistant Landscape in 2026: Cursor vs GitHub Copilot vs Claude Code vs JetBrains AI", "url": "https://earezki.com/ai-news/2026-05-23-the-ai-coding-assistant-landscape-in-2026-cursor-vs-github-copilot-vs-claude-code-vs-jetbrains-ai/", "source": "Dev|Journal"},
            ],
        "i18n": {
            "en": {
                "commentary": "Claude Code holds rank 1 because it sets the bar for agentic coding that the entire category is now converging on. The New Stack's six-month review concludes that Claude Code, Cursor, Codex, and Antigravity have effectively agreed on what an AI coding agent should be, and Claude Code is the template the others followed. Anthropic recently shipped Opus 4.7 with a notable jump on coding benchmarks, which keeps Claude Code's 9.7 code quality and 9.5 agentic capability scores at the front. For developers who care most about correct, well-structured code from an autonomous agent, this is still the one to beat.\n\nThe Stack Overflow data tells the market story. GitHub Copilot's share among professional developers fell from 67 percent to 51 percent, while Cursor debuted at 18 percent and Claude Code reached 10 percent on its first appearance, from a standing start. That trajectory is why Cursor holds rank 2 and Copilot, despite its install base, sits at rank 4. Cursor's Composer 2 and parallel-agent orchestration keep it the strongest IDE-native experience.\n\nA pricing shift matters this week: GitHub Copilot moved to usage-based AI Credits on June 1, and Microsoft Build 2026 on June 2 to 3 is expected to bring a Copilot agent refresh. Entry tiers for Cursor Pro and Claude Code both sit around $20 with usage-based costs layered on top.\n\nMy verdict holds: Claude Code is the agentic quality leader, Cursor is the best IDE-native workflow, and the tools are increasingly run together rather than chosen exclusively. The smart move in 2026 is a stack, not a single pick, and Claude Code anchors it.",
                "highlights": [
                    {"title": "Claude Code Leads the Agentic Coding Blueprint", "body": "The New Stack's six-month review concludes the whole category converged on the agentic model Claude Code defined. With Opus 4.7's coding-benchmark jump backing a 9.7 code quality and 9.5 agentic capability score, it remains the autonomous agent to beat for correct, well-structured output."},
                    {"title": "Market Share Data Validates the Rank Order", "body": "Stack Overflow data shows GitHub Copilot's professional-developer share fell from 67 percent to 51 percent, while Cursor debuted at 18 percent and Claude Code hit 10 percent from zero. That trajectory is why Cursor holds rank 2 and Copilot sits at rank 4 despite its install base."},
                    {"title": "Copilot Pricing Shift and Build 2026 This Week", "body": "GitHub Copilot moved to usage-based AI Credits on June 1, and Microsoft Build 2026 on June 2 to 3 is expected to bring a Copilot agent refresh. Cursor Pro and Claude Code entry tiers both sit near $20 with usage-based costs on top, keeping the value comparison close."},
                ],
            },
            "zh-tw": {
                "commentary": "Claude Code 守住第一名，因為它定義了整個品類現在正在收斂的代理式編程標準。The New Stack 的半年回顧結論是，Claude Code、Cursor、Codex、Antigravity 實際上已經對「AI 編程代理該是什麼樣子」達成共識，而 Claude Code 就是其他人跟著走的範本。Anthropic 近期推出 Opus 4.7，在編程基準上有明顯跳升，讓 Claude Code 的 9.7 程式品質和 9.5 代理能力分數穩居前段。對最在意自主代理產出正確、結構良好程式碼的開發者來說，這仍是要被超越的那一個。\n\nStack Overflow 的數據說明了市場局勢。GitHub Copilot 在專業開發者間的佔比從 67% 掉到 51%，而 Cursor 首次登場就拿 18%，Claude Code 從零起步首次出現就達 10%。這個走勢就是 Cursor 守住第二、Copilot 儘管安裝量龐大卻只排第四的原因。Cursor 的 Composer 2 和平行代理編排，讓它維持最強的 IDE 原生體驗。\n\n這週有個定價變化要注意：GitHub Copilot 在 6/1 改成用量計費的 AI Credits，而 6/2 到 6/3 的 Microsoft Build 2026 預期會帶來 Copilot 代理的更新。Cursor Pro 和 Claude Code 的入門方案都落在 20 美元上下，再疊加用量費用。\n\n我的判斷不變：Claude Code 是代理品質的領先者，Cursor 是最好的 IDE 原生工作流，而這些工具越來越多是搭著一起用，而不是二選一。2026 年聰明的做法是組一套工具堆疊，不是單選一個，而 Claude Code 是那個定海神針。",
                "highlights": [
                    {"title": "Claude Code 領銜代理式編程藍圖", "body": "The New Stack 半年回顧結論是整個品類收斂到 Claude Code 定義的代理模式。Opus 4.7 在編程基準上的跳升撐起 9.7 程式品質和 9.5 代理能力分數，它仍是產出正確、結構良好程式碼最難被超越的自主代理。"},
                    {"title": "市佔數據印證榜單順序", "body": "Stack Overflow 數據顯示 GitHub Copilot 的專業開發者佔比從 67% 掉到 51%，Cursor 首次登場就 18%，Claude Code 從零起步達 10%。這個走勢就是 Cursor 守第二、Copilot 儘管安裝量大卻排第四的原因。"},
                    {"title": "Copilot 改定價，Build 2026 本週登場", "body": "GitHub Copilot 在 6/1 改成用量計費的 AI Credits，6/2 到 6/3 的 Microsoft Build 2026 預期帶來 Copilot 代理更新。Cursor Pro 和 Claude Code 入門方案都在 20 美元上下再加用量費，CP 值比較依然膠著。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK ai-coding-assistants")


def build_ai_image_generators():
    d, p = load("best-ai-image-generators.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Midjourney May 2026 Update: V8.1, Pricing & Video", "url": "https://pixverse.ai/en/blog/midjourney-ai-image-generator-review", "source": "PixVerse"},
            {"title": "Midjourney V8 vs FLUX vs Stable Diffusion: Best AI Image Generator in 2026", "url": "https://wavespeed.ai/blog/posts/midjourney-v8-vs-flux-vs-sora-best-ai-image-generator-2026/", "source": "WaveSpeed"},
            {"title": "Best AI Image Generators 2026: Midjourney, Flux & More", "url": "https://www.miniloop.ai/blog/best-ai-image-generators-2026", "source": "Miniloop"},
        ],
        "i18n": {
            "en": {
                "commentary": "Midjourney V8 holds rank 1 because nothing else matches its aesthetic ceiling, and the V8.1 update on April 30 widened the lead. V8.1 adds faster generation, HD 2K output, better prompt adherence, and refined Raw mode, and Midjourney now turns a still into a 5-second clip that extends to 21 seconds. Its 9.9 artistic quality score is the highest on this list by a clear margin, and for anyone whose work lives or dies on visual taste, it remains the obvious pick.\n\nThe competitive picture below the top is shifting fast. FLUX.2 from Black Forest Labs got a March speed upgrade that doubled generation speed at no quality cost and pushed open-weights output to 4 megapixels with stronger character and layout consistency. That is exactly why FLUX.2 Pro holds rank 2: it is the best high-fidelity option for teams that want commercial-grade results with open-weights flexibility.\n\nThe biggest structural change is at OpenAI. DALL-E 2 and DALL-E 3 were officially retired on May 12, and GPT Image 2, which launched April 21, is now the only image model in ChatGPT and the API. GPT Image 2 leads on prompt accuracy and complex-instruction following, which is why it sits at rank 3 and is the pick when you need an image to follow detailed directions precisely, including legible text.\n\nMy verdict: Midjourney V8 is the artistry champion, FLUX.2 Pro is the open-weights commercial workhorse, and GPT Image 2 is the prompt-accuracy and text-rendering specialist. The top three each own a clear lane, and the order is stable heading into summer.",
                "highlights": [
                    {"title": "Midjourney V8.1 Extends the Artistry Lead", "body": "The April 30 V8.1 update adds faster generation, HD 2K output, better prompt adherence, and refined Raw mode, plus image-to-video that extends to 21 seconds. A 9.9 artistic quality score, the highest here by a clear margin, keeps Midjourney the pick for taste-driven visual work."},
                    {"title": "FLUX.2 Pro Wins on Open-Weights High Fidelity", "body": "A March speed upgrade doubled FLUX.2's generation speed at no quality cost and pushed open-weights output to 4 megapixels with stronger character and layout consistency. That makes FLUX.2 Pro the rank-2 choice for teams wanting commercial-grade results with open-weights flexibility."},
                    {"title": "OpenAI Retires DALL-E, GPT Image 2 Takes Over", "body": "DALL-E 2 and DALL-E 3 were retired on May 12, leaving GPT Image 2, launched April 21, as the only image model in ChatGPT and the API. It leads on prompt accuracy and complex instructions, holding rank 3 as the pick when an image must follow detailed directions, text included."},
                ],
            },
            "zh-tw": {
                "commentary": "Midjourney V8 守住第一名，因為美學天花板沒有對手追得上，而 4/30 的 V8.1 更新又把領先拉得更開。V8.1 加入更快的生成、HD 2K 輸出、更好的提示詞遵循，以及優化的 Raw 模式，而且 Midjourney 現在能把靜態圖變成 5 秒短片，還能延長到 21 秒。它 9.9 的藝術品質分是全榜最高，而且差距明顯，對任何作品成敗取決於視覺品味的人來說，它仍是理所當然的選擇。\n\n第一名以下的競爭格局變得很快。Black Forest Labs 的 FLUX.2 在三月拿到速度升級，生成速度翻倍卻零畫質損失，開放權重輸出推到 4 百萬像素，角色和版面一致性也更強。這正是 FLUX.2 Pro 守住第二的原因：對想要商業級成果又要開放權重彈性的團隊，它是最好的高保真選擇。\n\n最大的結構性變化在 OpenAI。DALL-E 2 和 DALL-E 3 在 5/12 正式退役，4/21 推出的 GPT Image 2 現在是 ChatGPT 和 API 裡唯一的圖像模型。GPT Image 2 在提示詞準確度和複雜指令遵循上領先，這就是它排第三的原因，當你需要圖像精準照著詳細指示走，包括清晰的文字，它就是首選。\n\n我的判斷：Midjourney V8 是藝術性冠軍，FLUX.2 Pro 是開放權重的商業主力，GPT Image 2 是提示詞準確度和文字渲染的專家。前三名各據一條清楚的賽道，進入夏天順序很穩。",
                "highlights": [
                    {"title": "Midjourney V8.1 把藝術性領先拉得更開", "body": "4/30 的 V8.1 更新加入更快生成、HD 2K 輸出、更好的提示詞遵循、優化 Raw 模式，還有能延長到 21 秒的圖生影片。9.9 的藝術品質分是全榜最高且差距明顯，讓 Midjourney 穩坐品味導向視覺工作的首選。"},
                    {"title": "FLUX.2 Pro 拿下開放權重高保真", "body": "三月的速度升級讓 FLUX.2 生成速度翻倍卻零畫質損失，開放權重輸出推到 4 百萬像素，角色與版面一致性更強。這讓 FLUX.2 Pro 成為想要商業級成果又要開放權重彈性的團隊的第二名之選。"},
                    {"title": "OpenAI 讓 DALL-E 退役，GPT Image 2 接棒", "body": "DALL-E 2 和 DALL-E 3 在 5/12 退役，留下 4/21 推出的 GPT Image 2 作為 ChatGPT 和 API 裡唯一的圖像模型。它在提示詞準確度和複雜指令上領先，以圖像需精準照詳細指示（含文字）的首選守住第三。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK ai-image-generators")


def build_ai_meeting_assistants():
    d, p = load("best-ai-meeting-assistants.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Granola raises $125M, hits $1.5B valuation as it expands from meeting notetaker to enterprise AI app", "url": "https://techcrunch.com/2026/03/25/granola-raises-125m-hits-1-5b-valuation-as-it-expands-from-meeting-notetaker-to-enterprise-ai-app/", "source": "TechCrunch"},
            {"title": "Fathom adds a bot-less meeting mode in a bid to take on Granola", "url": "https://techcrunch.com/2026/04/15/fathom-adds-a-bot-less-meeting-mode-in-a-bid-to-take-on-granola/", "source": "TechCrunch"},
            {"title": "Granola vs Otter vs Fathom: Which AI Note Taker Wins in 2026?", "url": "https://www.itsconvo.com/blog/granola-vs-otter-vs-fathom", "source": "ItsConvo"},
        ],
        "i18n": {
            "en": {
                "commentary": "Granola holds rank 1 because it defined the bot-free notetaking approach that the rest of the category is now scrambling to copy. Granola captures audio directly, so no notetaker bot joins your call as a visible participant, which is exactly the experience users want and the reason its 9.8 user experience score leads this list. The momentum is real: Granola raised a $125M Series C at a $1.5B valuation and is expanding from a prosumer notetaker into an enterprise AI app, with team Spaces and a Model Context Protocol server that pipes meeting context into other AI workflows.\n\nThe clearest signal of Granola's influence is Fathom's response. In April, Fathom added a bot-less meeting mode specifically to take on Granola, transcribing calls without an assistant joining, and is shipping its own MCP server plus an iOS app that records in-person meetings. That is a strong product, and Fathom earns rank 2, helped by the most generous free tier in the category and a category-leading 5.0 G2 rating from over 6,000 reviews.\n\nThe practical split: if you live in back-to-back calls and want the cleanest, least intrusive notes, Granola is the pick. If free-tier generosity matters most, Fathom is hard to beat. Fireflies at rank 3 remains the choice for teams that want deep CRM and workflow integrations, and Otter at rank 4 stays relevant for live transcription and accessibility use cases.\n\nMy verdict holds: Granola leads on experience and the bot-free model it pioneered, Fathom is the fast-improving challenger, and the MCP-server wave means your meeting notes increasingly feed the rest of your AI stack.",
                "highlights": [
                    {"title": "Granola Leads on the Bot-Free Model It Pioneered", "body": "Granola captures audio directly so no bot joins your call as a visible participant, the experience behind its category-leading 9.8 user experience score. A $125M Series C at a $1.5B valuation funds its expansion into an enterprise AI app with team Spaces and an MCP server."},
                    {"title": "Fathom Copies the Bot-Less Playbook to Chase Granola", "body": "In April, Fathom added a bot-less meeting mode aimed squarely at Granola, plus its own MCP server and an iOS app for in-person recording. Backed by the most generous free tier and a 5.0 G2 rating from over 6,000 reviews, Fathom firmly holds rank 2."},
                    {"title": "MCP Servers Wire Meeting Notes Into Your AI Stack", "body": "Both Granola and Fathom now ship Model Context Protocol servers that pipe meeting context into other AI tools. That shift turns notetakers from standalone apps into data sources for the broader AI workflow, raising the value of the top picks for teams already invested in AI."},
                ],
            },
            "zh-tw": {
                "commentary": "Granola 守住第一名，因為它定義了「不派機器人」的記錄方式，整個品類現在都在搶著模仿。Granola 直接擷取音訊，不會有記錄機器人以可見參與者的身分加入你的會議，這正是使用者想要的體驗，也是它 9.8 的使用體驗分領先全榜的原因。它的氣勢是真的：Granola 拿下 1.25 億美元 C 輪募資，估值達 15 億美元，正從面向專業消費者的記錄工具擴張成企業級 AI 應用，推出團隊 Spaces 和一個能把會議脈絡灌進其他 AI 工作流的 MCP 伺服器。\n\n最能說明 Granola 影響力的，是 Fathom 的回應。四月時 Fathom 加入了「不派機器人」的會議模式，擺明就是要對打 Granola，能在不派助理加入的情況下轉錄通話，並推出自己的 MCP 伺服器，加上一個能錄實體會議的 iOS App。這是很強的產品，Fathom 拿下第二名，靠的還有同類最大方的免費方案，以及來自超過 6,000 則評論、全品類最高的 5.0 G2 評分。\n\n實用的分野：如果你整天都在開連續會議，想要最乾淨、最不打擾的筆記，選 Granola。如果免費方案的大方程度最重要，Fathom 很難被打敗。第三名的 Fireflies 仍是想要深度 CRM 和工作流整合團隊的選擇，第四名的 Otter 在即時轉錄和無障礙應用上依然有它的位置。\n\n我的判斷不變：Granola 靠它開創的不派機器人模式和使用體驗領先，Fathom 是進步快速的挑戰者，而這波 MCP 伺服器浪潮意味著你的會議筆記越來越多會餵進你其餘的 AI 工具堆疊。",
                "highlights": [
                    {"title": "Granola 靠自己開創的不派機器人模式領先", "body": "Granola 直接擷取音訊，不會有機器人以可見參與者身分加入會議，這個體驗撐起它全品類最高的 9.8 使用體驗分。1.25 億美元 C 輪、15 億美元估值，資助它擴張成企業級 AI 應用，推出團隊 Spaces 和 MCP 伺服器。"},
                    {"title": "Fathom 抄不派機器人打法追趕 Granola", "body": "四月時 Fathom 加入擺明對打 Granola 的不派機器人會議模式，還有自己的 MCP 伺服器和能錄實體會議的 iOS App。靠著最大方的免費方案和來自超過 6,000 則評論的 5.0 G2 評分，Fathom 穩穩守住第二。"},
                    {"title": "MCP 伺服器把會議筆記接進你的 AI 堆疊", "body": "Granola 和 Fathom 現在都推出 MCP 伺服器，把會議脈絡灌進其他 AI 工具。這個轉變讓記錄工具從獨立 App 變成更廣 AI 工作流的資料來源，對已經投入 AI 的團隊來說，提高了榜首選項的價值。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK ai-meeting-assistants")


if __name__ == "__main__":
    build_3d_printers()
    build_4k_tvs()
    build_action_cameras()
    build_ai_chatbots()
    build_ai_coding_assistants()
    build_ai_image_generators()
    build_ai_meeting_assistants()
    print("Batch 1 complete")
