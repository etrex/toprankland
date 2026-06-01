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
# Per-file content. rankings are carried forward unchanged from history[-1].
# ---------------------------------------------------------------------------

CONTENT = {
    "best-ai-chatbots.json": {
        "references": [
            {
                "title": "Google updates its Gemini app to take on ChatGPT and Claude at IO 2026",
                "url": "https://techcrunch.com/2026/05/19/google-updates-its-gemini-app-to-take-on-chatgpt-and-claude-at-io-2026/",
                "source": "TechCrunch",
            },
            {
                "title": "iOS 27 Will Let You Pick Claude or Gemini Instead of ChatGPT for Apple Intelligence",
                "url": "https://www.macrumors.com/2026/05/05/ios-27-third-party-chatbots-apple-intelligence/",
                "source": "MacRumors",
            },
            {
                "title": "AI Updates Today (May 2026) - Latest AI Model Releases",
                "url": "https://llm-stats.com/llm-updates",
                "source": "LLM Stats",
            },
        ],
        "en": {
            "commentary": "I am ending May where I started it, with ChatGPT, Claude, and Gemini stacked at the top, but the gap between them is now thin enough that your choice should follow your workflow rather than a benchmark table. ChatGPT keeps the lead because GPT-5.5 Instant is the most reliable default model I run, and the hallucination cuts on high-stakes prompts hold up across a month of real research. The bigger story this week is Gemini. At Google I/O 2026 the Gemini app picked up a Daily Brief, the Gemini Omni video model, and a 24/7 agent called Spark, which is why I nudged its real-time and ecosystem scores up. Google is turning Gemini from a chatbot into a hub, and inside Gmail and Docs that integration is now genuinely hard to beat. Claude holds second on the strength of Opus 4.7 coding and prose plus the new Managed Agents that can take an objective like plan a vacation and actually run the steps on a schedule. The other shift worth flagging is iOS 27, which will let iPhone users pick Claude or Gemini instead of ChatGPT for Apple Intelligence. That choice screen matters, because the default slot on a billion phones was the single biggest distribution advantage OpenAI had, and it is about to become contestable. Perplexity stays fourth for research, Grok fifth on live X data, and DeepSeek remains my free pick. My advice for June is unchanged: buy one of the top three based on where you already work, and let the free tier cover the rest.",
            "highlights": [
                {
                    "title": "Gemini at I/O 2026 is the week's real move",
                    "body": "The Gemini app added a Daily Brief, the Omni video model, and a 24/7 Spark agent, which pushes it from chatbot to hub. Combined with native Gmail and Docs reach, this is why I raised its real-time and ecosystem scores. For anyone living in Google Workspace, Gemini is now the assistant that does the most without leaving the apps you already use.",
                },
                {
                    "title": "iOS 27 opens the Apple Intelligence default to Claude and Gemini",
                    "body": "Apple confirmed iOS 27 will let users pick Claude or Gemini instead of ChatGPT for Apple Intelligence. The default assistant slot on a billion iPhones was OpenAI's biggest distribution edge, and making it user-selectable turns it into a real contest. This is the kind of platform decision that reshapes market share more than any single model launch.",
                },
                {
                    "title": "Claude Managed Agents now run multi-step jobs on a schedule",
                    "body": "Claude's Managed Agents can take an objective like research a kitchen remodel, break it into steps, run them on a schedule, and deliver results hands-off. Paired with Opus 4.7 leading on coding and prose, this keeps Claude firmly in second for developers and writers who want an assistant that finishes work rather than just answers questions.",
                },
                {
                    "title": "ChatGPT stays the safe default for one subscription",
                    "body": "GPT-5.5 Instant remains the most dependable everyday model I run, and the lower hallucination rate on medical, legal, and financial prompts holds up after a month of use. If you only pay for one assistant, ChatGPT Plus at around NT$640 still maximizes capability per dollar across reasoning, writing, voice, and agents.",
                },
            ],
        },
        "zh-tw": {
            "commentary": "五月怎麼開始就怎麼結束，ChatGPT、Claude、Gemini 還是疊在最上面，但三者之間的差距已經薄到你該照自己的工作流選，而不是看 benchmark 表格挑。ChatGPT 守第一，因為 GPT-5.5 Instant 是我跑過最穩的預設模型，高風險題目的幻覺下降撐過了一整個月的實測。這禮拜真正的大新聞是 Gemini。Google I/O 2026 上 Gemini App 加了 Daily Brief、Omni 影片模型，還有一個 24 小時待命的 Spark agent，所以我把它的即時資訊跟生態系分數往上調。Google 正在把 Gemini 從聊天機器人變成一個樞紐，在 Gmail 跟 Docs 裡那種整合度，現在真的很難打。Claude 守第二，靠的是 Opus 4.7 的寫程式跟文筆，加上新的 Managed Agents，你丟一個目標像規劃一趟旅行，它真的會照排程把步驟跑完。另一個值得講的轉變是 iOS 27，以後 iPhone 用戶可以在 Apple Intelligence 裡選 Claude 或 Gemini 來取代 ChatGPT。這個選擇畫面很關鍵，畢竟十億支手機上的預設位子，本來是 OpenAI 最大的通路優勢，現在要變成大家都能搶了。Perplexity 守第四做研究，Grok 第五靠即時 X 資料，DeepSeek 還是我的免費首選。六月我的建議沒變，照你已經在用的環境，從前三名挑一個來付費，剩下的場景用免費的補就好。",
            "highlights": [
                {
                    "title": "Gemini 在 I/O 2026 是本週真正的大動作",
                    "body": "Gemini App 加了 Daily Brief、Omni 影片模型，還有 24 小時待命的 Spark agent，整個從聊天機器人升級成樞紐。配上原生接 Gmail 跟 Docs 的覆蓋面，這就是我調高它即時跟生態系分數的原因。對活在 Google Workspace 裡的人來說，Gemini 現在是不用離開你慣用 App 就能做最多事的助理。",
                },
                {
                    "title": "iOS 27 把 Apple Intelligence 預設開放給 Claude 跟 Gemini",
                    "body": "Apple 確認 iOS 27 會讓用戶用 Claude 或 Gemini 取代 ChatGPT 當 Apple Intelligence 的助理。十億支 iPhone 上那個預設位子本來是 OpenAI 最大的通路優勢，開放讓使用者自己選之後就變成真正的競爭了。這種平台層級的決定，重塑市佔的力道比任何單一模型發表都大。",
                },
                {
                    "title": "Claude Managed Agents 現在能照排程跑多步驟任務",
                    "body": "Claude 的 Managed Agents 可以接一個目標像研究廚房翻修，自己拆成步驟、照排程跑、把結果交給你，全程不用你動手。搭配 Opus 4.7 在寫程式跟文筆上的領先，這讓 Claude 對工程師跟寫作者來說穩坐第二，你要的是會把事做完的助理，而不是只會回答問題的那種。",
                },
                {
                    "title": "只訂一個的話 ChatGPT 還是安全預設",
                    "body": "GPT-5.5 Instant 還是我跑過最可靠的日常模型，醫療、法律、金融題目的幻覺下降，用一個月之後依然站得住。如果你只付一個助理的錢，月費約 NT$640 的 ChatGPT Plus 在推理、寫作、語音、agent 各方面的性價比還是最高。",
                },
            ],
        },
    },
    "best-air-purifiers.json": {
        "references": [
            {
                "title": "8 Best Air Purifiers of 2026, Tested by Our Experts",
                "url": "https://www.consumerreports.org/appliances/air-purifiers/best-air-purifiers-of-the-year-a1197763201/",
                "source": "Consumer Reports",
            },
            {
                "title": "The best air purifiers you can buy in 2026",
                "url": "https://housefresh.com/best-air-purifiers-we-tested/",
                "source": "HouseFresh",
            },
            {
                "title": "The Best Air Purifiers of 2026 | Lab Tested & Ranked",
                "url": "https://www.techgearlab.com/topics/health-fitness/best-air-purifier",
                "source": "TechGearLab",
            },
        ],
        "en": {
            "commentary": "As we move into June and summer humidity starts pushing mold and dust around, my air purifier ranking stays steady because the fundamentals have not changed. The IQAir HealthPro Plus holds first on filtration alone, capturing particles well below the 0.3 micron HEPA threshold, and it remains the unit I trust most for allergy and asthma households even though it costs the most to run. The Coway Airmega 400S stays my best all-rounder at second, because it pairs near-top CADR with quiet operation and a price that does not punish you. What I am watching this season is Coway's new Airmega Mighty2 AP-1512N, released in March, which brings better odor control, more detailed air quality feedback, and longer filter life to the small-room segment. It is not on the board yet because I want to log smoke-clear times before I rank it, but it is the most interesting budget launch of the year. The Blueair HealthProtect 7470i keeps third as the quietest premium pick, which matters in a bedroom more than spec sheets admit. Down the list, the Levoit Core 600S and Vital 200S remain the value plays I recommend most often, clearing real square footage for a fraction of the IQAir price. For June, my buying logic is simple: choose the IQAir if filtration is medical, the Airmega 400S if you want the best balance, and a Levoit if budget leads.",
            "highlights": [
                {
                    "title": "IQAir HealthPro Plus stays the filtration benchmark",
                    "body": "The HealthPro Plus captures ultrafine particles well below the 0.3 micron HEPA standard, which is why it holds first for allergy and asthma households. Running costs are the highest on this list, but when filtration is a medical need rather than a preference, this is the unit I trust to do the job in a primary bedroom or nursery.",
                },
                {
                    "title": "Coway Airmega 400S is still the best all-rounder",
                    "body": "The 400S pairs near-top CADR with genuinely quiet operation and a price that stays reasonable for the coverage. It is the unit I recommend to most people furnishing a living room or open-plan space, because it clears large rooms fast without the running cost or the noise penalty that the very top tier brings.",
                },
                {
                    "title": "Coway's Airmega Mighty2 is the budget launch to watch",
                    "body": "Released in March, the Airmega Mighty2 AP-1512N upgrades the classic small-room workhorse with better odor control, more detailed air quality feedback, and longer filter life. I am holding it off the board until I log smoke-clear times, but it is the most interesting value launch of 2026 and a likely entry once the numbers are in.",
                },
                {
                    "title": "Levoit Core 600S and Vital 200S lead on value",
                    "body": "Both Levoit units clear real square footage for a fraction of the premium price, which keeps them the value picks I name most often. For a home office, a kid's room, or a second unit you do not want to overthink, these deliver the cleaning that matters without paying for features most people never touch.",
                },
            ],
        },
        "zh-tw": {
            "commentary": "進入六月，夏天的濕氣開始把黴菌跟灰塵攪起來，我的空氣清淨機排行還是很穩，因為基本盤沒變。IQAir HealthPro Plus 靠純濾淨力守第一，連遠低於 0.3 微米的顆粒都抓得住，過敏跟氣喘家庭我最信任的就是它，雖然它的耗材也是最燒錢的。Coway Airmega 400S 守第二當我的最佳全能機，CADR 接近頂規、運轉安靜、價格又不會讓你心痛。這一季我在盯的是 Coway 三月新出的 Airmega Mighty2 AP-1512N，它把更好的除臭、更細的空氣品質回饋、更長的濾網壽命帶進小坪數市場。我還沒把它放上榜，是想先實測除煙時間再排名，但它是今年最有看頭的平價新機。Blueair HealthProtect 7470i 守第三，是最安靜的高階選擇，這點放臥室比規格表上看起來重要多了。再往下，Levoit Core 600S 跟 Vital 200S 還是我最常推的 CP 值款，用 IQAir 一小部分的價錢就能清掉一整個房間的坪數。六月的選購邏輯很簡單，濾淨是醫療等級需求就選 IQAir，要最佳平衡就 Airmega 400S，預算掛帥就 Levoit。",
            "highlights": [
                {
                    "title": "IQAir HealthPro Plus 還是濾淨力標竿",
                    "body": "HealthPro Plus 連遠低於 0.3 微米 HEPA 標準的超細顆粒都抓得住，這就是它在過敏跟氣喘家庭守第一的原因。耗材是榜上最貴的，但當濾淨是醫療必需而非偏好的時候，放主臥或嬰兒房我就是信任它把事情做好。",
                },
                {
                    "title": "Coway Airmega 400S 還是最佳全能機",
                    "body": "400S 把接近頂規的 CADR 配上真的很安靜的運轉，價格對它的覆蓋坪數來說很合理。佈置客廳或開放式空間的人我大多推它，大房間清得快，又沒有最頂級那一階帶來的耗材成本跟噪音代價。",
                },
                {
                    "title": "Coway Airmega Mighty2 是該盯的平價新機",
                    "body": "三月上市的 Airmega Mighty2 AP-1512N，把經典小坪數主力機升級成更好的除臭、更細的空氣品質回饋、更長的濾網壽命。我先壓著不放上榜，想實測除煙時間再說，但它是 2026 最有意思的 CP 值新機，數字出來後很可能就進榜了。",
                },
                {
                    "title": "Levoit Core 600S 跟 Vital 200S 主打 CP 值",
                    "body": "兩台 Levoit 都用高階機一小部分的價錢清掉實打實的坪數，所以它們是我最常點名的 CP 值款。家裡的工作間、小孩房、或是你不想多想的第二台，這兩台把該做的清淨做到，又不用為了大多數人根本用不到的功能多付錢。",
                },
            ],
        },
    },
    "best-foldable-smartphones.json": {
        "references": [
            {
                "title": "Best foldable phones to buy in 2026: The top foldables we recommend",
                "url": "https://www.phonearena.com/news/best-foldable-smartphones_id132093",
                "source": "PhoneArena",
            },
            {
                "title": "Best foldable phones of 2026",
                "url": "https://www.tomsguide.com/best-picks/best-foldable-phones",
                "source": "Tom's Guide",
            },
            {
                "title": "Research projects a big 2026 for book-style foldables",
                "url": "https://www.androidcentral.com/phones/samsung-galaxy/research-projects-a-big-2026-for-book-style-foldables-and-i-can-kind-of-see-it",
                "source": "Android Central",
            },
        ],
        "en": {
            "commentary": "Heading into June the foldable order at the top stays put, but the market context underneath it just got more interesting. The Galaxy Z Fold 7 keeps first on the strength of its 8.9mm folded profile and 215g weight, and the fact that it took 60% of Samsung's own foldable pre-orders, the first time the book style beat the clamshell, tells you buyers finally trust big foldables as daily drivers. There is also a live discount of up to 400 dollars running May 25 through June 8, which makes this the best window of the year to buy one. The Pixel 10 Pro Fold holds second and remains my durability pick, because full IP68 dust and water resistance plus a gearless hinge address the two failure modes that used to scare people off foldables. Counterpoint now projects book-style devices growing to roughly 65% of foldable shipments in 2026, which validates why the Fold and the Pro Fold sit ahead of the flip-style phones on this list. Oppo Find N5 stays third as the thinnest serious option, Honor Magic V3 fourth on value, and the Galaxy Z Flip 7 leads the clamshells at sixth for buyers who want pocketability over a tablet screen. For June my advice is direct: if you want a foldable, grab the Z Fold 7 while the discount is live, and choose the Pixel only if water resistance is your top worry.",
            "highlights": [
                {
                    "title": "Galaxy Z Fold 7 is the buy of the month with a live discount",
                    "body": "Samsung is running up to 400 dollars off the Z Fold 7 from May 25 through June 8, which makes June the best window of the year. At 8.9mm folded and 215g it is slim enough to carry like a normal phone, and it took 60% of Samsung's foldable pre-orders. If you want a book-style foldable, buy now while the price is down.",
                },
                {
                    "title": "Pixel 10 Pro Fold owns durability with IP68 and a gearless hinge",
                    "body": "The Pixel 10 Pro Fold is the first foldable with full IP68 dust and water resistance, and its gearless hinge removes many of the small parts that wear out over time. Those two changes target the exact failure modes that made buyers nervous about foldables. If long-term reliability is your top concern, this is the one I point to.",
                },
                {
                    "title": "Book-style foldables are taking over the category",
                    "body": "Counterpoint projects book-style devices growing to roughly 65% of foldable shipments in 2026, and Samsung's own pre-orders show the Fold beating the Flip for the first time. That shift is why the Z Fold 7 and Pixel 10 Pro Fold sit at the top here. The big-screen foldable is now the mainstream choice, not the niche one.",
                },
                {
                    "title": "Galaxy Z Flip 7 still leads the clamshells",
                    "body": "For buyers who want pocketability over a tablet-sized inner screen, the Galaxy Z Flip 7 remains the clamshell to beat at sixth. It is the foldable for people who never wanted the bulk of a Fold, and at its price it is the easiest entry point into the category for someone curious but cost-conscious.",
                },
            ],
        },
        "zh-tw": {
            "commentary": "進入六月，摺疊機榜首順序沒變，但底下的市場局勢更有看頭了。Galaxy Z Fold 7 守第一，靠的是折起來只有 8.9mm、重 215g，加上它拿下三星自家摺疊機 60% 的預購，這是書本式第一次贏過翻蓋式，代表買家終於敢把大摺疊機當主力機用。現在還有一個 5/25 到 6/8 的折扣最高省 400 美元，這是今年最好的入手時機。Pixel 10 Pro Fold 守第二，還是我的耐用首選，完整 IP68 防塵防水加上無齒輪鉸鏈，剛好解決了以前嚇退大家的兩個故障點。Counterpoint 現在預估書本式裝置 2026 年會成長到摺疊機出貨量的約 65%，這也印證了為什麼 Fold 跟 Pro Fold 在這份榜上排在翻蓋機前面。Oppo Find N5 守第三當最薄的正經選擇，Honor Magic V3 第四主打 CP 值，Galaxy Z Flip 7 領銜翻蓋陣營排第六，給想要好放口袋勝過平板螢幕的人。六月我的建議很直接，想要摺疊機就趁折扣還在抓 Z Fold 7，只有防水是你最在意的點才選 Pixel。",
            "highlights": [
                {
                    "title": "Galaxy Z Fold 7 是本月首選，折扣正在跑",
                    "body": "三星 5/25 到 6/8 對 Z Fold 7 最高折 400 美元，六月就是今年最好的入手窗口。折起來 8.9mm、215g，薄到能像一般手機那樣帶著走，還拿下三星摺疊機 60% 的預購。想要書本式摺疊機，趁價格下來就買。",
                },
                {
                    "title": "Pixel 10 Pro Fold 靠 IP68 跟無齒輪鉸鏈拿下耐用王",
                    "body": "Pixel 10 Pro Fold 是第一支有完整 IP68 防塵防水的摺疊機，無齒輪鉸鏈又拿掉了很多會隨時間磨損的小零件。這兩個改動剛好對準了讓買家對摺疊機緊張的故障點。長期可靠度是你最在意的事，我就指這一支。",
                },
                {
                    "title": "書本式摺疊機正在接管整個品類",
                    "body": "Counterpoint 預估書本式裝置 2026 年會成長到摺疊機出貨量約 65%，三星自家預購也顯示 Fold 第一次贏過 Flip。這個轉變就是 Z Fold 7 跟 Pixel 10 Pro Fold 排在榜首的原因。大螢幕摺疊機現在是主流選擇，不再是小眾了。",
                },
                {
                    "title": "Galaxy Z Flip 7 還是翻蓋機霸主",
                    "body": "想要好放口袋勝過平板大小內螢幕的人，Galaxy Z Flip 7 還是翻蓋陣營排第六的標竿。它是給那些從來不想要 Fold 那種厚度的人，以它的價格，對好奇又精打細算的人來說是最好上手的入門點。",
                },
            ],
        },
    },
    "best-massage-guns.json": {
        "references": [
            {
                "title": "The Best Massage Guns of 2026 | Tested & Ranked",
                "url": "https://www.techgearlab.com/topics/health-fitness/best-massage-gun",
                "source": "TechGearLab",
            },
            {
                "title": "12 Best Massage Guns of 2026, Lab-Tested and Reviewed",
                "url": "https://www.consumerreports.org/health/massage-guns/massage-guns-evaluated-a1174087874/",
                "source": "Consumer Reports",
            },
            {
                "title": "Theragun vs. Hypervolt vs. ReAthlete: Which Massage Gun Is Best?",
                "url": "https://peakprimalwellness.com/blogs/wellness/theragun-vs-hypervolt-vs-reathlete",
                "source": "Peak Primal Wellness",
            },
        ],
        "en": {
            "commentary": "My massage gun ranking holds firm into June, and a fresh round of 2026 lab testing backs up why the order looks the way it does. The Theragun Pro Plus G6 stays first because it is one of the best models reviewers have ever measured, delivering the deepest amplitude and the most useful attachment set, and it is the gun I reach for after heavy leg days. The trade-off is price and noise, so it earns the top spot on capability rather than value. The Hyperice Hypervolt 2 Pro holds third and the latest testing reinforces its case: QuietGlide keeps it around 40 to 60 decibels and its battery runs roughly 180 minutes, the best single-charge endurance in its class. At about 329 to 349 dollars it is the full-size gun I recommend to people who want power without a jackhammer in the living room. The Rally Orbital stays second as my quiet-but-strong middle ground. Down the list the value story is still strong: the Ekrin B37 and the Bob and Brad Q2 Mini keep doing real work for far less money, and the Toloco EM26 remains the budget pick that overdelivers on attachments. For June my logic is unchanged: buy the Theragun if you want the best and will pay for it, the Hypervolt if quiet endurance matters, and an Ekrin or Toloco if value leads.",
            "highlights": [
                {
                    "title": "Theragun Pro Plus G6 is still the best gun money buys",
                    "body": "Reviewers rate the Pro Plus G6 as one of the best models ever measured, with the deepest amplitude and the most complete attachment set on this list. It is loud and expensive, so it wins on capability rather than value, but after heavy training it is the gun I reach for first. If you want the top tool and will pay for it, this is it.",
                },
                {
                    "title": "Hyperice Hypervolt 2 Pro leads on quiet endurance",
                    "body": "Fresh 2026 testing confirms the Hypervolt 2 Pro runs around 40 to 60 decibels on QuietGlide and lasts roughly 180 minutes per charge, the best in its class. At about 329 to 349 dollars it is the full-size gun I recommend for home or office use where noise and battery life matter more than raw stall force.",
                },
                {
                    "title": "Ekrin B37 and Bob and Brad Q2 Mini carry the value tier",
                    "body": "Both deliver real percussion for far less than the premium names, which keeps them my go-to value picks. The Ekrin B37 pairs strong power with long battery life, and the Q2 Mini is the quiet, pocketable travel gun. For most people who are not chasing the absolute top spec, these do the job without overspending.",
                },
                {
                    "title": "Toloco EM26 still overdelivers at the bottom of the range",
                    "body": "The Toloco EM26 remains the budget pick that punches above its price, bundling a generous attachment set and a quiet motor for a fraction of the flagship cost. It is not as powerful as the Theragun, but for casual recovery and gifting it is the easiest recommendation I can make to someone testing the waters.",
                },
            ],
        },
        "zh-tw": {
            "commentary": "我的筋膜槍排行進六月一樣穩，2026 一輪新的實驗室測試也印證了為什麼順序長這樣。Theragun Pro Plus G6 守第一，因為它是評測者測過最強的機種之一，衝程最深、附件組最實用，重訓練腿日之後我第一個拿的就是它。代價是價格跟噪音，所以它靠的是實力而非 CP 值拿下榜首。Hyperice Hypervolt 2 Pro 守第三，最新測試又加強了它的說服力，QuietGlide 把噪音壓在約 40 到 60 分貝，電池能跑約 180 分鐘，是同級裡單次充電續航最好的。約 329 到 349 美元，它是我推給想要力道又不想在客廳開電鑽的人的全尺寸機。Rally Orbital 守第二，是我安靜又有力的中庸之選。再往下，CP 值的故事還是很強，Ekrin B37 跟 Bob and Brad Q2 Mini 用低很多的價錢做著實打實的工作，Toloco EM26 還是附件給好給滿、超出價格期待的平價首選。六月我的邏輯沒變，想要最好又願意花錢就買 Theragun，在意安靜續航就 Hypervolt，CP 值掛帥就 Ekrin 或 Toloco。",
            "highlights": [
                {
                    "title": "Theragun Pro Plus G6 還是錢能買到的最強機",
                    "body": "評測者把 Pro Plus G6 評為測過最強的機種之一，衝程最深、附件組是這份榜上最完整的。它又吵又貴，所以靠的是實力而非 CP 值，但重訓之後我第一個拿的就是它。想要頂級工具又願意付錢，就是它了。",
                },
                {
                    "title": "Hyperice Hypervolt 2 Pro 主打安靜續航",
                    "body": "2026 新測試確認 Hypervolt 2 Pro 在 QuietGlide 下約 40 到 60 分貝，單次充電約跑 180 分鐘，同級最佳。約 329 到 349 美元，它是我推給居家或辦公室用的全尺寸機，這些場景噪音跟續航比純粹的失速壓力更重要。",
                },
                {
                    "title": "Ekrin B37 跟 Bob and Brad Q2 Mini 扛起 CP 值這一階",
                    "body": "兩台都用比高階品牌低很多的價錢給出實打實的敲擊力，所以是我的 CP 值首選。Ekrin B37 力道強又電池耐久，Q2 Mini 是安靜好放口袋的旅行機。大多數不追頂規的人，這兩台把事做好又不超支。",
                },
                {
                    "title": "Toloco EM26 在價格帶底端還是超值",
                    "body": "Toloco EM26 還是那台價格越級打怪的平價首選，用旗艦一小部分的價錢就附了豐富的附件組跟安靜的馬達。它沒 Theragun 那麼強，但日常放鬆跟送禮，這是我能給想試水溫的人最好開口的推薦。",
                },
            ],
        },
    },
    "best-portable-chargers.json": {
        "references": [
            {
                "title": "The best portable chargers of 2026, tried and tested",
                "url": "https://www.cnn.com/cnn-underscored/reviews/best-portable-charger",
                "source": "CNN Underscored",
            },
            {
                "title": "Best Power Bank 2026: 5 New Chargers That Raised the Bar",
                "url": "https://the-gadgeteer.com/2026/05/06/best-power-bank-2026-five-new-chargers/",
                "source": "The Gadgeteer",
            },
            {
                "title": "Best MagSafe Power Banks for iPhone in 2026: Anker vs Belkin vs Ugreen",
                "url": "https://www.gizmochina.com/2026/05/16/best-magsafe-power-banks-for-iphone-in-2026-anker-vs-belkin-vs-ugreen/",
                "source": "Gizmochina",
            },
        ],
        "en": {
            "commentary": "My power bank ranking holds steady into June, and the latest 2026 testing keeps reinforcing the same hierarchy. The Anker Prime 26K 300W stays first because it puts 26,250mAh and 300W of total output across three ports into a brick you can still pocket, and reviewers keep singling it out as the flagship that defines the category this year. It charges a 16-inch laptop, a phone, and earbuds at once without breaking a sweat, which is why it earns the top scores on speed and smarts. The Ugreen Nexode 25000mAh 200W holds fourth and remains my value champion: it delivers dual 100W outputs that fast-charge a 16-inch MacBook Pro to 56% in 30 minutes, and reviewers consistently find Ugreen lands 90 to 95% of Anker's performance for 15 to 30% less money. That gap is the whole reason to consider it. The Anker Nano 10K stays fifth as the grab-and-go pick, the one I actually carry daily because the built-in connector means no cable to forget. Down the list the Qi2 wireless picks, the Baseus PicoGo and the Anker MagGo 10K, remain the cleanest options for iPhone users who want to skip cables entirely. For June my advice stands: buy the Prime if you want the best, the Ugreen Nexode if value leads, and a Nano or MagGo if pocketability wins.",
            "highlights": [
                {
                    "title": "Anker Prime 26K 300W is the flagship that defines 2026",
                    "body": "Reviewers keep naming the Prime 26K as the bank that sets the bar this year, packing 26,250mAh and 300W across three ports into a pocketable brick. It charges a laptop, phone, and earbuds at once without strain, which is why it takes the top speed and smart-feature scores. If you want the best and capacity is king, this is the buy.",
                },
                {
                    "title": "Ugreen Nexode 25000mAh 200W is the value champion",
                    "body": "The Nexode delivers dual 100W outputs that take a 16-inch MacBook Pro to 56% in 30 minutes, and reviewers consistently peg Ugreen at 90 to 95% of Anker's performance for 15 to 30% less money. That price gap is the entire argument, and it is a strong one. For most buyers who want flagship-class output without the flagship price, this is it.",
                },
                {
                    "title": "Anker Nano 10K is the everyday grab-and-go",
                    "body": "The Nano 10K stays my daily carry because the built-in connector means there is no cable to forget, and the 30W output tops up a phone fast. It is the bank I recommend to people who just want their phone alive by dinner without thinking about it, and at its price it is the easiest add-to-cart on this list.",
                },
                {
                    "title": "Qi2 wireless picks keep getting better for iPhone",
                    "body": "The Baseus PicoGo and Anker MagGo 10K remain the cleanest Qi2 options for iPhone users who want to skip cables entirely, snapping to the back of the phone for magnetic charging on the move. They trade some capacity for convenience, but for a commute or a coffee-shop top-up that tradeoff is exactly right.",
                },
            ],
        },
        "zh-tw": {
            "commentary": "我的行動電源排行進六月很穩，2026 最新測試一直在強化同樣的排序。Anker Prime 26K 300W 守第一，因為它把 26,250mAh 跟 300W 總輸出塞進三個埠、還能放口袋的磚塊裡，評測者一直把它點名為今年定義這個品類的旗艦。它能同時充 16 吋筆電、手機、耳機都不費力，這就是它在速度跟智慧分數拿最高的原因。Ugreen Nexode 25000mAh 200W 守第四，還是我的 CP 值王，雙 100W 輸出能在 30 分鐘把 16 吋 MacBook Pro 充到 56%，評測者也一致發現 Ugreen 用 Anker 的 85% 到 70% 價錢做到它 90% 到 95% 的表現。這個價差就是考慮它的全部理由。Anker Nano 10K 守第五當隨手帶款，我每天真正帶的就是它，內建接頭代表不會忘記帶線。再往下，Qi2 無線款的 Baseus PicoGo 跟 Anker MagGo 10K，還是 iPhone 用戶想完全擺脫線材最乾淨的選擇。六月我的建議不變，想要最好就買 Prime，CP 值掛帥就 Ugreen Nexode，好放口袋優先就 Nano 或 MagGo。",
            "highlights": [
                {
                    "title": "Anker Prime 26K 300W 是定義 2026 的旗艦",
                    "body": "評測者一直把 Prime 26K 點名為今年立標竿的那台，三個埠塞進 26,250mAh 跟 300W，還是能放口袋的磚塊。同時充筆電、手機、耳機都不吃力，這就是它拿下最高速度跟智慧功能分數的原因。想要最好又把容量擺第一，就買它。",
                },
                {
                    "title": "Ugreen Nexode 25000mAh 200W 是 CP 值王",
                    "body": "Nexode 雙 100W 輸出能在 30 分鐘把 16 吋 MacBook Pro 充到 56%，評測者一致把 Ugreen 定在 Anker 表現的 90% 到 95%，價格卻便宜 15% 到 30%。這個價差就是全部論點，而且很有力。大多數想要旗艦級輸出又不想付旗艦價的人，就是它。",
                },
                {
                    "title": "Anker Nano 10K 是日常隨手帶",
                    "body": "Nano 10K 還是我每天帶的，內建接頭代表不用怕忘了帶線，30W 輸出幫手機快速補血。我推給那些只想手機撐到晚餐又不想多想的人，以它的價格，是這份榜上最好直接加入購物車的一台。",
                },
                {
                    "title": "Qi2 無線款對 iPhone 越做越好",
                    "body": "Baseus PicoGo 跟 Anker MagGo 10K 還是 iPhone 用戶想完全擺脫線材最乾淨的 Qi2 選擇，吸在手機背面就能邊走邊磁吸充電。它們用一點容量換便利，但通勤或在咖啡廳補一下電，這個取捨剛剛好。",
                },
            ],
        },
    },
    "best-security-cameras.json": {
        "references": [
            {
                "title": "The 9 Best Wireless Home Security Cameras of 2026",
                "url": "https://www.safewise.com/blog/best-wireless-security-cameras/",
                "source": "SafeWise",
            },
            {
                "title": "Reolink vs Eufy: Ultimate Security Camera Comparison (2026 Guide)",
                "url": "https://sipkosecurity.com/reolink-vs-eufy-security-camera-comparison-2026/",
                "source": "Sipko Security",
            },
            {
                "title": "Arlo vs eufy 2026: 4K Camera Shootout",
                "url": "https://alarm-reviews.net/arlo-vs-eufy-2026-premium-4k-cameras-vs-budget-local-storage-image-quality-privacy-subscriptions-3-year-cost-compared/",
                "source": "Alarm Reviews",
            },
        ],
        "en": {
            "commentary": "My security camera ranking holds into June, and the 2026 comparison testing keeps validating why value and zero subscription costs dominate the top of this list. The Reolink Argus 4 Pro stays first because it pairs genuine 4K, a bright spotlight, and wire-free install with local storage and affordable solar add-ons, which means no monthly fee eating at you for years. Reviewers keep flagging the same thing: Reolink offers a smaller price tag than Arlo while still giving you local storage and solar options, and that total-cost math is why it wins. The Arlo Pro 5S holds second on the strength of true 4K HDR and the best color night vision in recent testing, but it pushes you toward an 8 to 18 dollar monthly cloud plan, so it earns its spot on image quality rather than value. The Eufy SoloCam S340 stays third as the no-subscription pick, recording locally with solar charging that genuinely lasts. Down the list the cost story stays loud: a two-camera Eufy setup runs around 240 dollars upfront with no monthly fee, saving 360 to 720 dollars over three years versus the cloud brands, and the TP-Link Tapo C460 remains the budget standout. For June my logic is simple: buy the Reolink for the best all-around value, the Arlo if night-vision image quality leads, and Eufy or Tapo if avoiding subscriptions is the whole point.",
            "highlights": [
                {
                    "title": "Reolink Argus 4 Pro wins on total cost of ownership",
                    "body": "The Argus 4 Pro pairs real 4K, a bright spotlight, and wire-free install with local storage and cheap solar add-ons, so there is no monthly fee draining your wallet for years. Reviewers keep noting Reolink undercuts Arlo while still offering local and solar options. That total-cost math is exactly why it holds first on this list.",
                },
                {
                    "title": "Arlo Pro 5S leads on night-vision image quality",
                    "body": "The Pro 5S shoots true 4K HDR with the best color night vision in recent testing, delivering sharp images without oversaturation. The catch is an 8 to 18 dollar monthly cloud plan, so it earns second on image quality rather than value. If picture quality after dark is your priority and the subscription does not bother you, this is the pick.",
                },
                {
                    "title": "Eufy SoloCam S340 is the no-subscription standout",
                    "body": "The SoloCam S340 records locally with solar charging that genuinely lasts, which is the whole appeal for buyers tired of monthly fees. A two-camera Eufy setup runs around 240 dollars upfront with zero ongoing cost, saving 360 to 720 dollars over three years versus the cloud brands. For subscription-free peace of mind, it stays my third pick.",
                },
                {
                    "title": "TP-Link Tapo C460 remains the budget standout",
                    "body": "The Tapo C460 keeps delivering strong AI detection and solid image quality at a price that undercuts almost everything else here, which is why it holds its value score. For a starter system, a rental, or covering a side yard on a budget, it is the easiest recommendation I can make to someone who wants real coverage without overspending.",
                },
            ],
        },
        "zh-tw": {
            "commentary": "我的監視器排行進六月維持原樣，2026 的比較測試一直印證為什麼 CP 值跟零訂閱費主宰了這份榜的前段。Reolink Argus 4 Pro 守第一，因為它把貨真價實的 4K、明亮的探照燈、免佈線安裝，配上本地儲存跟便宜的太陽能配件，代表不會有月費啃你好幾年。評測者一直點同一件事，Reolink 價格比 Arlo 低，又給你本地儲存跟太陽能選項，這個總持有成本的算法就是它贏的原因。Arlo Pro 5S 守第二，靠的是真 4K HDR 跟近期測試裡最好的彩色夜視，但它會把你推向月費 8 到 18 美元的雲端方案，所以它靠畫質而非 CP 值站穩位子。Eufy SoloCam S340 守第三當免訂閱首選，本地錄影加太陽能充電真的耐用。再往下，成本的故事一樣大聲，兩台 Eufy 的組合前期約 240 美元、零月費，三年比雲端品牌省下 360 到 720 美元，TP-Link Tapo C460 還是平價亮點。六月我的邏輯很簡單，要最佳全面 CP 值就買 Reolink，夜視畫質掛帥就 Arlo，重點是避開訂閱就 Eufy 或 Tapo。",
            "highlights": [
                {
                    "title": "Reolink Argus 4 Pro 靠總持有成本勝出",
                    "body": "Argus 4 Pro 把真 4K、明亮探照燈、免佈線安裝配上本地儲存跟便宜的太陽能配件，所以沒有月費啃你錢包好幾年。評測者一直提 Reolink 價格壓過 Arlo，又同時給本地跟太陽能選項。這個總成本的算法，就是它在這份榜守第一的原因。",
                },
                {
                    "title": "Arlo Pro 5S 主打夜視畫質",
                    "body": "Pro 5S 拍真 4K HDR，配上近期測試裡最好的彩色夜視，畫面銳利又不會過飽和。代價是月費 8 到 18 美元的雲端方案，所以它靠畫質而非 CP 值拿第二。入夜後的畫質是你的優先，又不在意訂閱，就選它。",
                },
                {
                    "title": "Eufy SoloCam S340 是免訂閱亮點",
                    "body": "SoloCam S340 本地錄影加太陽能充電真的耐用，這就是給受夠月費的人最大的吸引力。兩台 Eufy 的組合前期約 240 美元、零持續費用，三年比雲端品牌省下 360 到 720 美元。要免訂閱的安心感，它穩坐我的第三名。",
                },
                {
                    "title": "TP-Link Tapo C460 還是平價亮點",
                    "body": "Tapo C460 持續用壓過這裡幾乎所有對手的價格，給出強悍的 AI 偵測跟扎實畫質，這就是它 CP 值分數守得住的原因。入門系統、租屋處、或預算內顧個側院，這是我能給想要真覆蓋又不想超支的人最好開口的推薦。",
                },
            ],
        },
    },
    "best-treadmills.json": {
        "references": [
            {
                "title": "Best Home Treadmills for 2026 (CPT-Tested & Reviewed)",
                "url": "https://www.treadmillreviews.net/best-treadmill/for-home-use/",
                "source": "TreadmillReviews",
            },
            {
                "title": "Best Treadmills 2026",
                "url": "https://www.nordictrack.com/best-treadmills-2026",
                "source": "NordicTrack",
            },
            {
                "title": "Find Your Perfect NordicTrack Treadmill: Reviews (2026)",
                "url": "https://www.treadmillreviews.net/nordictrack-treadmill-reviews/",
                "source": "TreadmillReviews",
            },
        ],
        "en": {
            "commentary": "My treadmill ranking holds into June, and the latest 2026 reviews keep validating why the NordicTrack Commercial 1750 sits at the top. Reviewers describe it as the machine for a shared household where one person runs daily and others walk or jog, thanks to a 22 by 60 inch deck, Run Flex cushioning, a 16-inch pivoting touchscreen, and a 12 to minus 3 incline range. That combination of a generous deck, real incline, and iFit guidance is exactly what most home buyers actually need, which is why it beats the more specialized machines for general use. The NordicTrack X24 Incline holds second for buyers who want steeper incline training and a bigger screen, and reviewers still steer dedicated runners toward the Commercial 2450, which validates keeping the 1750 as the balanced default rather than the spec leader. The Sole F80 stays third as my pick for people who want a rock-solid frame, a 350-pound user capacity, and a lifetime warranty without paying for flashy interactive visuals. Reviewers consistently rank it highly across categories for exactly that reason. Down the list the Peloton Tread and Aviron Victory remain the choices for buyers who train mostly through guided classes and gamified workouts. For June my logic is simple: buy the 1750 for the best all-around home treadmill, the Sole F80 if durability and warranty lead, and a Peloton or Aviron if classes drive your training.",
            "highlights": [
                {
                    "title": "NordicTrack Commercial 1750 is the best all-around home pick",
                    "body": "Reviewers call the 1750 the machine for a shared household, with a 22 by 60 inch deck, Run Flex cushioning, a 16-inch pivoting touchscreen, and a 12 to minus 3 incline range. That mix of deck size, real incline, and iFit guidance is what most home buyers actually need, which is why it holds first over the more specialized machines on this list.",
                },
                {
                    "title": "NordicTrack X24 Incline is the step up for incline training",
                    "body": "The X24 holds second for buyers who want steeper incline work and a larger screen than the 1750 offers. Reviewers still point dedicated runners toward the Commercial 2450, which is exactly why the 1750 stays the balanced default and the X24 sits just behind it for those who want more aggressive climbing built in.",
                },
                {
                    "title": "Sole F80 wins on durability and warranty",
                    "body": "The Sole F80 is consistently ranked highly across categories for its rock-solid frame, 350-pound user capacity, and lifetime warranty. It skips the flashy interactive visuals, which is the whole point for buyers who want a machine that lasts over one that streams classes. For long-term reliability without subscription pressure, it stays my third pick.",
                },
                {
                    "title": "Peloton Tread and Aviron Victory are the class-driven picks",
                    "body": "For buyers who train mostly through guided classes or gamified workouts, the Peloton Tread and Aviron Victory remain the right choices. They cost more per session because the experience is the product, but if a screen full of instructors and challenges is what gets you running, that premium buys real consistency.",
                },
            ],
        },
        "zh-tw": {
            "commentary": "我的跑步機排行進六月維持原樣，2026 最新評測一直印證為什麼 NordicTrack Commercial 1750 坐在榜首。評測者形容它是給一人每天跑、其他人走或慢跑的共用家庭的機器，靠的是 22 乘 60 吋跑帶、Run Flex 避震、16 吋可旋轉觸控螢幕、12 到負 3 的坡度範圍。寬跑帶、真坡度、加 iFit 課程引導這個組合，剛好是大多數居家買家真正需要的，這就是它在一般用途上贏過更專門機種的原因。NordicTrack X24 Incline 守第二，給想要更陡坡度訓練跟更大螢幕的人，評測者還是把專職跑者導向 Commercial 2450，這也印證了把 1750 留作平衡預設而非規格領頭羊是對的。Sole F80 守第三，是我給那些想要超穩機架、350 磅承重、終身保固又不想為花俏互動畫面付錢的人的選擇。評測者一致在各項目給它高分，原因正是如此。再往下，Peloton Tread 跟 Aviron Victory 還是給那些主要靠課程跟遊戲化訓練的人。六月我的邏輯很簡單，要最佳全能家用跑步機就買 1750，耐用跟保固掛帥就 Sole F80，課程驅動你的訓練就 Peloton 或 Aviron。",
            "highlights": [
                {
                    "title": "NordicTrack Commercial 1750 是最佳全能家用款",
                    "body": "評測者把 1750 稱為共用家庭的機器，22 乘 60 吋跑帶、Run Flex 避震、16 吋可旋轉觸控螢幕、12 到負 3 坡度範圍。跑帶尺寸、真坡度、加 iFit 引導這個組合，是大多數居家買家真正需要的，這就是它在這份榜上贏過更專門機種守第一的原因。",
                },
                {
                    "title": "NordicTrack X24 Incline 是坡度訓練的升級選擇",
                    "body": "X24 守第二，給想要比 1750 更陡坡度訓練跟更大螢幕的人。評測者還是把專職跑者導向 Commercial 2450，這正是為什麼 1750 維持平衡預設，X24 緊跟在後給那些想要更激進爬坡內建的人。",
                },
                {
                    "title": "Sole F80 靠耐用跟保固勝出",
                    "body": "Sole F80 因為超穩機架、350 磅承重、終身保固，一致在各項目拿高分。它省掉花俏的互動畫面，這對想要耐用機種勝過串流課程的買家就是重點。要長期可靠又沒有訂閱壓力，它守住我的第三名。",
                },
                {
                    "title": "Peloton Tread 跟 Aviron Victory 是課程驅動的選擇",
                    "body": "主要靠課程引導或遊戲化訓練的買家，Peloton Tread 跟 Aviron Victory 還是對的選擇。每次訓練成本比較高，因為體驗本身就是產品，但如果是一整螢幕的教練跟挑戰讓你願意開跑，這個溢價買到的是真正的持續性。",
                },
            ],
        },
    },
}


def main():
    for name, c in CONTENT.items():
        data, p = load(name)
        entry = {
            "date": DATE,
            "rankings": last_rankings(data),
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
