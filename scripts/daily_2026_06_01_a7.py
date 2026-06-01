# -*- coding: utf-8 -*-
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
# 1) AI MEETING ASSISTANTS
# ---------------------------------------------------------------------------
def ai_meeting():
    name = "best-ai-meeting-assistants.json"
    d, p = load(name)
    entry = {
        "date": DATE,
        "rankings": last_rankings(d),
        "references": [
            {
                "title": "AI Meeting Recorder Lawsuits 2026: Otter.ai, Fireflies, and Recording Compliantly",
                "url": "https://tldv.io/blog/ai-meeting-recorder-lawsuits/",
                "source": "tl;dv",
            },
            {
                "title": "7 AI Meeting Notetakers Tested in 2026 (Fathom vs Fireflies vs Otter)",
                "url": "https://get-alfred.ai/blog/best-ai-meeting-notetakers",
                "source": "Alfred",
            },
            {
                "title": "Granola vs Otter vs Fathom: Which AI Note Taker Wins in 2026?",
                "url": "https://www.itsconvo.com/blog/granola-vs-otter-vs-fathom",
                "source": "Convo",
            },
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "Granola starts June at number one and I am comfortable leaving it there. The bot-free desktop "
                    "capture is still the cleanest experience in this category, and now that Granola ships native Mac, "
                    "Windows, and mobile apps the old Mac-only objection is gone. That matters this week because the "
                    "legal story around recording consent got sharper: the consolidated Otter.ai lawsuits over how its "
                    "notetaker records participants are heading to a motion-to-dismiss hearing on May 20, and Fireflies "
                    "is facing two biometric privacy suits in Illinois. When the question of who knew they were being "
                    "recorded becomes a courtroom issue, a tool that captures system audio on your own machine without "
                    "pushing a visible bot into the call looks even smarter. Fathom holds second and earns it. The G2 "
                    "rating sits at 5.0 from more than 6,000 reviews, post-call processing lands in about 30 seconds, "
                    "and the free tier still gives you unlimited recording and transcription. For a solo operator that "
                    "combination is unbeatable. Fireflies stays third on integration depth, and the new Talk to "
                    "Fireflies feature powered by Perplexity lets you pull web answers mid-meeting, which is a genuinely "
                    "useful addition for sales calls. I keep it above Otter because the privacy litigation hangs heavier "
                    "over Otter right now. Fellow remains my pick for finance, legal, and healthcare teams thanks to SOC "
                    "2 Type II, GDPR, and HIPAA coverage with zero training on customer data. If you are choosing this "
                    "week, Granola for product and design, Fathom for solo work, Fellow if compliance signs the check."
                ),
                "highlights": [
                    {
                        "title": "Granola keeps number one as the consent lawsuits make bot-free capture look prescient",
                        "body": (
                            "With the Otter.ai consolidated suits heading to a May 20 motion-to-dismiss hearing and "
                            "Fireflies facing Illinois biometric privacy claims, the legal weather is turning against "
                            "tools that inject a visible recording bot. Granola captures system audio on your own "
                            "machine, and now that it ships native Mac, Windows, and mobile apps there is no platform "
                            "excuse left to skip it."
                        ),
                    },
                    {
                        "title": "Fathom is still the best free meeting assistant, and the numbers back it",
                        "body": (
                            "A 5.0 G2 rating across more than 6,000 reviews is the highest in the category, post-call "
                            "processing finishes in roughly 30 seconds, and unlimited recording and transcription stay "
                            "free across Zoom, Google Meet, and Teams. For a solo operator who wants a searchable "
                            "archive with clean summaries, this is the obvious first install."
                        ),
                    },
                    {
                        "title": "Talk to Fireflies brings live web answers into the call",
                        "body": (
                            "Fireflies added Talk to Fireflies powered by Perplexity, letting you ask questions and get "
                            "web search results inside the meeting. Combined with the deepest CRM integration layer in "
                            "the category, that keeps Fireflies firmly at number three for sales operations teams that "
                            "live in Salesforce and HubSpot."
                        ),
                    },
                    {
                        "title": "Fellow is the answer when compliance signs the check",
                        "body": (
                            "SOC 2 Type II, GDPR, and HIPAA coverage with zero training on customer data and "
                            "configurable retention down to same-day deletion makes Fellow the defensible pick for "
                            "finance, legal, and healthcare teams. At a Team price near the bottom of this category, it "
                            "is also one of the cheaper ways to satisfy a security review."
                        ),
                    },
                ],
            },
            "zh-tw": {
                "commentary": (
                    "六月開頭 Granola 還是坐穩第一，我很放心讓它留在那。無 Bot 桌面擷取在這個品類還是最乾淨的體驗，"
                    "而且現在 Granola 已經有原生的 Mac、Windows 跟手機 App，過去那個「只能在 Mac 用」的理由整個消失。"
                    "這禮拜特別重要，因為錄音同意的法律問題越來越尖銳。Otter.ai 那批整合在一起的訴訟，"
                    "爭的就是它的筆記工具怎麼在參與者不知情下錄音，五月二十號要進入駁回動議聽證，"
                    "Fireflies 在伊利諾州也吃了兩件生物特徵隱私官司。當「誰知道自己被錄」變成法庭問題，"
                    "一個直接在你自己電腦上擷取系統音訊、會議裡完全看不到 Bot 的工具就顯得更聰明。\n\n"
                    "Fathom 守第二，這個位置它拿得很實在。G2 評分六千多則維持 5.0，會議結束大概三十秒就跑完摘要，"
                    "免費版錄影跟轉錄還是無限。對個人工作者來說這組合真的打不贏。Fireflies 第三靠整合深度撐住，"
                    "新出的 Talk to Fireflies 由 Perplexity 撐腰，開會中可以直接抓網路答案，跑業務電話蠻好用。"
                    "我把它放在 Otter 前面，因為現在隱私訴訟壓在 Otter 身上比較重。\n\n"
                    "Fellow 還是我給金融、法務、醫療團隊的首選，SOC 2 Type II、GDPR、HIPAA 三證齊全，"
                    "承諾不用客戶資料訓練。這禮拜要選的話，產品設計團隊選 Granola，個人工作者選 Fathom，"
                    "資安要簽核就選 Fellow。"
                ),
                "highlights": [
                    {
                        "title": "同意權官司燒起來，Granola 的無 Bot 擷取看起來更有先見之明，第一穩住",
                        "body": (
                            "Otter.ai 整合訴訟五月二十號要進駁回動議聽證，Fireflies 在伊利諾州吃生物特徵隱私官司，"
                            "法律風向正在對「會議裡塞一個看得見的錄音 Bot」這件事轉壞。Granola 直接在你自己電腦擷取系統音訊，"
                            "現在又有原生 Mac、Windows、手機 App，已經沒有什麼平台理由可以不裝它。"
                        ),
                    },
                    {
                        "title": "Fathom 還是最強的免費會議助理，數據站得住腳",
                        "body": (
                            "G2 六千多則評分維持 5.0，是這個品類最高，會議結束大概三十秒跑完摘要，"
                            "Zoom、Google Meet、Teams 三平台錄影跟轉錄全部免費無限。"
                            "個人工作者想要一個可搜尋的會議檔案庫加乾淨摘要，這就是最該先裝的那一個。"
                        ),
                    },
                    {
                        "title": "Talk to Fireflies 把即時網路答案帶進會議",
                        "body": (
                            "Fireflies 新增 Talk to Fireflies，由 Perplexity 撐腰，開會中可以直接問問題、拿網路搜尋結果。"
                            "配上這個品類最深的 CRM 整合層，讓 Fireflies 在第三名穩穩的，"
                            "對整天泡在 Salesforce 跟 HubSpot 的業務團隊特別實用。"
                        ),
                    },
                    {
                        "title": "資安要簽核，答案就是 Fellow",
                        "body": (
                            "SOC 2 Type II、GDPR、HIPAA 三證齊全，承諾零客戶資料訓練，保留期間可以設定到當日刪除，"
                            "讓 Fellow 成為金融、法務、醫療團隊最站得住腳的選擇。Team 方案價格在這個品類偏低，"
                            "也是讓資安審查放行最省錢的方式之一。"
                        ),
                    },
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("done", name)


# ---------------------------------------------------------------------------
# 2) DASH CAMS
# ---------------------------------------------------------------------------
def dash_cams():
    name = "best-dash-cams.json"
    d, p = load(name)
    entry = {
        "date": DATE,
        "rankings": last_rankings(d),
        "references": [
            {
                "title": "I've reviewed over 15 dash cams this last year, and Viofo's A329 is the best of the bunch",
                "url": "https://www.techradar.com/vehicle-tech/dash-cams/ive-reviewed-over-15-dash-cams-this-last-year-and-viofos-a329-is-the-best-of-the-bunch-heres-why",
                "source": "TechRadar",
            },
            {
                "title": "The Viofo A329S is an outstanding dash cam with fantastic video quality, but the price is a big hurdle",
                "url": "https://www.tomsguide.com/vehicle-tech/the-viofo-a329s-is-an-outstanding-dash-cam-with-fantastic-video-quality-but-the-price-is-a-big-hurdle",
                "source": "Tom's Guide",
            },
            {
                "title": "Viofo A329S Review and Comparison with the Vantrue N4 Pro S",
                "url": "https://dashcamtalk.com/forum/threads/viofo-a329s-review-and-comparison-with-the-vantrue-n4pro-s.55098/",
                "source": "DashCamTalk",
            },
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "The Viofo A329S holds number one going into June and the reviews keep stacking up in its favor. "
                    "TechRadar called the A329 the best of more than 15 dash cams tested over the past year, and Tom's "
                    "Guide rated the footage near flawless. The hardware explains why: a 4K 60fps front camera and 2K "
                    "rear, both running Sony Starvis 2 sensors with HDR, plus dual-band 2.4GHz and 5GHz Wi-Fi that "
                    "actually makes pulling clips off the camera fast. The only real hurdle is price. The three-channel "
                    "configuration runs $499.99 direct from Viofo, which is top-tier money, and I keep the value score "
                    "honest because of it. The Vantrue N4 Pro S stays second and remains the smarter buy for rideshare "
                    "and delivery drivers who need a strong interior channel. Side by side the A329S delivers "
                    "more natural day and night footage and a wider, better-corrected interior view, but the N4 Pro S "
                    "covers three angles for less and that matters when the cabin camera is the point. BlackVue Elite 9 "
                    "and Thinkware U3000 hold their premium spots for buyers who want clean cloud connectivity and "
                    "hardwired parking surveillance, though both ask you to pay up for the badge. Further down, the "
                    "Viofo A119M Pro is still the value pick I point budget buyers toward, a single-channel 4K cam that "
                    "covers the essentials without the flagship invoice. If you want the best image quality available "
                    "and the price does not scare you, the A329S is the camera to buy."
                ),
                "highlights": [
                    {
                        "title": "Viofo A329S stays number one on near-flawless footage",
                        "body": (
                            "Dual Sony Starvis 2 sensors, 4K 60fps front with HDR, a 2K rear, and 2.4GHz plus 5GHz "
                            "Wi-Fi for fast transfers. TechRadar named the A329 the best of more than 15 cams it tested "
                            "this year and Tom's Guide called the recording near flawless. The image quality is the "
                            "reason it leads."
                        ),
                    },
                    {
                        "title": "The $499.99 price is the one real catch",
                        "body": (
                            "The three-channel A329S runs $499.99 direct from Viofo, putting it among the most "
                            "expensive brand-name dash cams you can buy. The footage justifies it for enthusiasts, but "
                            "the value score stays grounded because most drivers do not need to spend this much."
                        ),
                    },
                    {
                        "title": "Vantrue N4 Pro S is the rideshare and delivery pick",
                        "body": (
                            "For drivers who need a strong interior channel, the N4 Pro S covers three angles at a "
                            "lower price than the A329S. The Viofo wins on natural day and night color and a wider "
                            "interior field of view, but when the cabin camera is the whole point, the Vantrue earns "
                            "its second-place spot."
                        ),
                    },
                    {
                        "title": "Viofo A119M Pro remains the value pick",
                        "body": (
                            "A single-channel 4K camera that covers the essentials without the flagship invoice. If "
                            "you want clean front-only recording and a price that does not sting, this is still where "
                            "I point budget buyers."
                        ),
                    },
                ],
            },
            "zh-tw": {
                "commentary": (
                    "進入六月 Viofo A329S 還是穩坐第一，評測一篇接一篇往它身上疊。TechRadar 把 A329 評為過去一年測過十五台以上裡最強的，"
                    "Tom's Guide 說它的畫面接近無懈可擊。硬體就是答案：前鏡頭 4K 60fps、後鏡頭 2K，兩顆都用 Sony Starvis 2 感光元件加 HDR，"
                    "再加上 2.4GHz 跟 5GHz 雙頻 Wi-Fi，從相機抓檔案是真的快。唯一的關卡就是價格。三鏡頭版本在 Viofo 官網要價約台幣一萬五，"
                    "這是旗艦級的錢，我也因此把 CP 值分數抓得實在。\n\n"
                    "Vantrue N4 Pro S 守第二，對需要強車內鏡頭的 Uber、外送司機來說還是比較聰明的買法。"
                    "兩台擺一起比，A329S 不論白天晚上都更自然，車內視角更廣、HDR 修正也更好。不過 N4 Pro S 用更低的價格涵蓋三個角度，"
                    "當你買相機就是為了車內那一顆時，這點很關鍵。\n\n"
                    "BlackVue Elite 9 跟 Thinkware U3000 守住高階位置，給想要乾淨雲端連線跟接電停車監控的人，"
                    "只是兩台都要為品牌多掏錢。再往下，Viofo A119M Pro 還是我推給預算族的選擇，單鏡頭 4K，"
                    "把該有的都顧到，不用付旗艦帳單。想要市面上最好的畫質、價格又嚇不倒你，A329S 就是該買的那台。"
                ),
                "highlights": [
                    {
                        "title": "Viofo A329S 靠接近無懈可擊的畫面守住第一",
                        "body": (
                            "雙 Sony Starvis 2 感光元件，前鏡頭 4K 60fps 加 HDR，後鏡頭 2K，2.4GHz 跟 5GHz 雙頻 Wi-Fi 傳檔超快。"
                            "TechRadar 把 A329 評為今年測過十五台以上裡最強，Tom's Guide 說錄影接近無懈可擊。畫質就是它領先的原因。"
                        ),
                    },
                    {
                        "title": "約台幣一萬五的價格是唯一真正的關卡",
                        "body": (
                            "三鏡頭版本在 Viofo 官網要價約台幣一萬五，是品牌行車記錄器裡數一數二貴的。"
                            "畫面對玩家來說值這個價，但 CP 值分數我抓得保守，因為大多數人其實不用花到這麼多。"
                        ),
                    },
                    {
                        "title": "Vantrue N4 Pro S 是 Uber 跟外送司機的選擇",
                        "body": (
                            "需要強車內鏡頭的司機，N4 Pro S 用比 A329S 更低的價格涵蓋三個角度。"
                            "Viofo 贏在白天晚上更自然的色彩跟更廣的車內視角，但當車內鏡頭就是重點時，Vantrue 守第二守得有道理。"
                        ),
                    },
                    {
                        "title": "Viofo A119M Pro 還是 CP 值首選",
                        "body": (
                            "單鏡頭 4K，把該有的都顧到，不用付旗艦帳單。想要乾淨的前鏡頭錄影、價格又不刺痛荷包，"
                            "我推給預算族的還是這一台。"
                        ),
                    },
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("done", name)


# ---------------------------------------------------------------------------
# 3) GAMING MICE
# ---------------------------------------------------------------------------
def gaming_mice():
    name = "best-gaming-mice.json"
    d, p = load(name)
    entry = {
        "date": DATE,
        "rankings": last_rankings(d),
        "references": [
            {
                "title": "Logitech Superstrike vs Razer Viper V4 Pro: The battle for the competitive crown",
                "url": "https://www.pcgamer.com/hardware/gaming-mice/logitech-superstrike-vs-razer-viper-v4-pro-the-battle-for-the-competitive-crown/",
                "source": "PC Gamer",
            },
            {
                "title": "The Best Gaming Mouse of 2026: Mice Reviews",
                "url": "https://www.rtings.com/mouse/reviews/best/by-usage/gaming",
                "source": "RTINGS",
            },
            {
                "title": "Best Mouse for VALORANT [665 Pro Players, May 2026]",
                "url": "https://prosettings.net/guides/valorant-mouse/",
                "source": "ProSettings",
            },
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "The top of this board is a genuine two-horse race and I have the Logitech G Pro X2 Superstrike "
                    "holding number one by a hair. PC Gamer framed the Superstrike versus Viper V4 Pro as the battle for "
                    "the competitive crown, and the Superstrike keeps the lead because it carries the proven sensor and "
                    "shape pedigree of the Superlight line while adding its new actuation tech on top. The Viper V4 Pro "
                    "sits third and it is the most impressive new release in the category. It launched March 24 at 49 "
                    "grams, the lightest Razer flagship ever shipped, undercutting the V3 Pro by five grams while adding "
                    "Gen-4 optical switches and an 8000Hz Focus Pro 50K sensor with 180-hour battery life at 1000Hz. "
                    "Reviewers keep saying the same thing: if the V3 Pro set the benchmark, the V4 Pro perfects it. The "
                    "switches feel better, the chassis feels more refined, and the weight drop is real. The only reason "
                    "it is not higher is that the Superstrike and the GPX2 Dex still edge it on raw value and shape "
                    "consensus. Pulsar X2 CL and Lamzu Maya X remain the enthusiast darlings further down, both "
                    "delivering flagship sensors and sub-50-gram builds at prices that undercut the big two. If you grip "
                    "claw or fingertip and chase the lightest possible wireless mouse, the Viper V4 Pro is the one to "
                    "try first this month. If you want the safest all-around competitive pick, the Superstrike is still "
                    "my default recommendation."
                ),
                "highlights": [
                    {
                        "title": "Superstrike holds number one in the battle for the competitive crown",
                        "body": (
                            "PC Gamer framed the Logitech G Pro X2 Superstrike against the Razer Viper V4 Pro as the "
                            "fight for the top of the category. The Superstrike keeps the lead by carrying the proven "
                            "Superlight 2 sensor and shape pedigree and adding its new actuation tech, which is why it "
                            "stays my default competitive pick."
                        ),
                    },
                    {
                        "title": "Razer Viper V4 Pro is the standout new release at 49 grams",
                        "body": (
                            "Launched March 24 at 49 grams, the lightest Razer flagship ever, it undercuts the V3 Pro "
                            "by five grams while adding Gen-4 optical switches, an 8000Hz Focus Pro 50K sensor, and "
                            "180-hour battery at 1000Hz. Reviewers agree: if the V3 Pro set the benchmark, the V4 Pro "
                            "perfects it."
                        ),
                    },
                    {
                        "title": "The V4 Pro is the one to try if you chase minimum weight",
                        "body": (
                            "Five grams off the V3 Pro is a noticeable change for claw and fingertip grippers, and the "
                            "refined switches and chassis make it feel like a genuine generational step. It sits third "
                            "only because the Superstrike and GPX2 Dex still edge it on value and shape consensus."
                        ),
                    },
                    {
                        "title": "Pulsar X2 CL and Lamzu Maya X stay the enthusiast value picks",
                        "body": (
                            "Both deliver flagship-grade sensors and sub-50-gram builds at prices that undercut "
                            "Logitech and Razer's flagships. If you want elite tracking and weight without paying the "
                            "big-brand premium, these two remain the smart buys further down the board."
                        ),
                    },
                ],
            },
            "zh-tw": {
                "commentary": (
                    "這份榜單最頂端是貨真價實的雙雄對決，我把 Logitech G Pro X2 Superstrike 以些微差距放在第一。"
                    "PC Gamer 把 Superstrike 對上 Viper V4 Pro 形容成爭奪電競王座的戰役，Superstrike 之所以守住領先，"
                    "是因為它帶著 Superlight 系列那套經過驗證的感應器跟形狀血統，再加上新的觸發技術。\n\n"
                    "Viper V4 Pro 排第三，是這個品類最讓人驚豔的新品。三月二十四號上市，重 49 公克，是 Razer 史上最輕的旗艦，"
                    "比 V3 Pro 再輕五公克，還加了第四代光學微動跟 8000Hz Focus Pro 50K 感應器，1000Hz 下續航 180 小時。"
                    "評測都講同一句話：如果 V3 Pro 立下標竿，V4 Pro 就是把它做到完美。微動手感更好，機身更精緻，減重是真的有感。"
                    "它沒有更高，只是因為 Superstrike 跟 GPX2 Dex 在純 CP 值跟形狀共識上還是壓它一點。\n\n"
                    "Pulsar X2 CL 跟 Lamzu Maya X 在後段還是玩家心頭好，兩台都給你旗艦感應器加 50 公克以下機身，"
                    "價格又比兩大廠便宜。如果你是爪握或指尖握、追求最輕的無線滑鼠，這個月先試 Viper V4 Pro。"
                    "想要最穩的全能電競選擇，Superstrike 還是我的預設推薦。"
                ),
                "highlights": [
                    {
                        "title": "Superstrike 在電競王座之爭守住第一",
                        "body": (
                            "PC Gamer 把 Logitech G Pro X2 Superstrike 對上 Razer Viper V4 Pro 形容成品類頂端的對決。"
                            "Superstrike 帶著經過驗證的 Superlight 2 感應器跟形狀血統，再加上新的觸發技術，"
                            "這就是它穩住我預設電競推薦的原因。"
                        ),
                    },
                    {
                        "title": "Razer Viper V4 Pro 是 49 公克的話題新品",
                        "body": (
                            "三月二十四號上市，重 49 公克，Razer 史上最輕的旗艦，比 V3 Pro 再輕五公克，"
                            "加了第四代光學微動、8000Hz Focus Pro 50K 感應器，1000Hz 下續航 180 小時。"
                            "評測一致認為：V3 Pro 立下標竿，V4 Pro 把它做到完美。"
                        ),
                    },
                    {
                        "title": "追求極致輕量就先試 V4 Pro",
                        "body": (
                            "比 V3 Pro 輕五公克，對爪握跟指尖握的人來說是有感的改變，加上更精緻的微動跟機身，"
                            "讓它感覺像真正的世代躍進。它排第三只是因為 Superstrike 跟 GPX2 Dex 在 CP 值跟形狀共識上還壓它一點。"
                        ),
                    },
                    {
                        "title": "Pulsar X2 CL 跟 Lamzu Maya X 還是玩家 CP 值首選",
                        "body": (
                            "兩台都給你旗艦級感應器加 50 公克以下機身，價格又比 Logitech 跟 Razer 旗艦便宜。"
                            "想要頂級追蹤跟輕量、又不想付大廠溢價，這兩台在後段還是聰明的買法。"
                        ),
                    },
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("done", name)


# ---------------------------------------------------------------------------
# 4) MESH WIFI SYSTEMS
# ---------------------------------------------------------------------------
def mesh_wifi():
    name = "best-mesh-wifi-systems.json"
    d, p = load(name)
    entry = {
        "date": DATE,
        "rankings": last_rankings(d),
        "references": [
            {
                "title": "The 4 Best Mesh Wi-Fi Systems of 2026",
                "url": "https://www.rtings.com/router/reviews/best/mesh-wifi-system",
                "source": "RTINGS",
            },
            {
                "title": "Best Wi-Fi 7 Mesh Systems: 2026's Battle-Tested Top Five",
                "url": "https://dongknows.com/best-wi-fi-7-mesh-systems/",
                "source": "Dong Knows Tech",
            },
            {
                "title": "Best mesh Wi-Fi systems of 2026, tested and reviewed for homes",
                "url": "https://www.tomsguide.com/computing/routers/best-mesh-wi-fi-systems",
                "source": "Tom's Guide",
            },
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "Heading into June the Asus ZenWiFi BQ16 Pro keeps the top spot for households that actually have "
                    "multi-gig internet to feed it. RTINGS and Tom's Guide both still rate it the system to recommend "
                    "when you want to put Wi-Fi 7 speeds to the test and future-proof the house, and the part I value "
                    "most is that Asus includes AiProtection Pro, parental controls, and a VPN server free for life with "
                    "no subscription. That matters because the competition increasingly hides features behind monthly "
                    "fees. The TP-Link Deco BE63 holds second and remains the value champion of the category. RTINGS "
                    "named it the best mesh system tested overall, with tri-band Wi-Fi 7, support for 200-plus devices, "
                    "and coverage up to 7,600 square feet starting around $270 for a two-pack. For most homes that is "
                    "the smart money. Eero Pro 7 stays third for anyone who values setup simplicity and a clean app "
                    "over raw configurability. Further down, the Deco BE95 and BE85 remain the quad-band heavy hitters "
                    "if you have the budget, though the BE95 two-pack sits near $999 to $1,099 and the ZenWiFi BQ16 Pro "
                    "two-pack lands around $1,100, so these are future-proofing buys rather than value buys. The MSI "
                    "Roamii BE Pro is still the surprise value pick lower on the board. My advice this week is "
                    "unchanged: buy the Deco BE63 unless you have multi-gig service and a big house, in which case the "
                    "ZenWiFi BQ16 Pro is worth the premium."
                ),
                "highlights": [
                    {
                        "title": "Asus ZenWiFi BQ16 Pro stays number one for multi-gig homes",
                        "body": (
                            "RTINGS and Tom's Guide still recommend it when you want to push Wi-Fi 7 speeds and "
                            "future-proof the house. The lifetime-free AiProtection Pro, parental controls, and VPN "
                            "server with no subscription are the difference-maker as rivals push more features behind "
                            "monthly fees."
                        ),
                    },
                    {
                        "title": "TP-Link Deco BE63 is the value champion at around $270",
                        "body": (
                            "RTINGS named it the best mesh system tested overall: tri-band Wi-Fi 7, 200-plus device "
                            "support, and up to 7,600 square feet of coverage starting near $270 for a two-pack. For "
                            "most homes this is simply the smart money."
                        ),
                    },
                    {
                        "title": "Quad-band BE95 and BQ16 Pro are future-proofing, not value",
                        "body": (
                            "The Deco BE95 two-pack runs $999 to $1,099 and the ZenWiFi BQ16 Pro two-pack lands near "
                            "$1,100. These are for multi-gig homes that want headroom for years, not for buyers chasing "
                            "the best price per square foot."
                        ),
                    },
                    {
                        "title": "Eero Pro 7 still wins on simplicity",
                        "body": (
                            "If you value a clean app and a five-minute setup over deep configuration menus, Eero Pro 7 "
                            "holds third. It is the system I point non-technical buyers toward when they just want fast "
                            "Wi-Fi without fiddling."
                        ),
                    },
                ],
            },
            "zh-tw": {
                "commentary": (
                    "進入六月，Asus ZenWiFi BQ16 Pro 還是給家裡真的有多 Gig 網路可以餵它的人守住第一。"
                    "RTINGS 跟 Tom's Guide 都還是把它當成想榨出 Wi-Fi 7 速度、把家裡網路做到未來好幾年都夠用時的首選，"
                    "我最看重的一點是 Asus 把 AiProtection Pro、家長控制、VPN 伺服器全部終身免費送，不收訂閱費。"
                    "這點很重要，因為對手越來越愛把功能藏在月費後面。\n\n"
                    "TP-Link Deco BE63 守第二，還是這個品類的 CP 值冠軍。RTINGS 把它評為整體測過最強的 Mesh 系統，"
                    "三頻 Wi-Fi 7、支援兩百台以上裝置、覆蓋最高約 210 坪，兩入組約台幣八千五就有。對大多數家庭來說這就是聰明錢。\n\n"
                    "Eero Pro 7 守第三，給重視設定簡單、App 乾淨勝過深度自訂的人。再往下，Deco BE95 跟 BE85 是預算夠時的四頻重砲，"
                    "只是 BE95 兩入組逼近台幣三萬，ZenWiFi BQ16 Pro 兩入組也要三萬出頭，這些是買未來保值，不是買 CP 值。"
                    "MSI Roamii BE Pro 在後段還是個驚喜 CP 值選擇。這禮拜建議不變：買 Deco BE63 就對了，"
                    "除非你家有多 Gig 網路又坪數大，那 ZenWiFi BQ16 Pro 的溢價就值得。"
                ),
                "highlights": [
                    {
                        "title": "Asus ZenWiFi BQ16 Pro 給多 Gig 家庭守住第一",
                        "body": (
                            "RTINGS 跟 Tom's Guide 都還是推薦它，給想榨出 Wi-Fi 7 速度、把家裡網路做到未來好幾年都夠的人。"
                            "終身免費的 AiProtection Pro、家長控制、VPN 伺服器不收訂閱費，在對手紛紛把功能塞進月費的時候就是決勝點。"
                        ),
                    },
                    {
                        "title": "TP-Link Deco BE63 是約台幣八千五的 CP 值冠軍",
                        "body": (
                            "RTINGS 把它評為整體測過最強的 Mesh 系統：三頻 Wi-Fi 7、支援兩百台以上裝置、"
                            "覆蓋最高約 210 坪，兩入組約台幣八千五起。對大多數家庭來說這就是最聰明的花法。"
                        ),
                    },
                    {
                        "title": "四頻的 BE95 跟 BQ16 Pro 是買未來，不是買 CP 值",
                        "body": (
                            "Deco BE95 兩入組約台幣三萬，ZenWiFi BQ16 Pro 兩入組也要三萬出頭。"
                            "這些是給多 Gig 家庭買未來好幾年的餘裕，不是給追求每坪最低價的人。"
                        ),
                    },
                    {
                        "title": "Eero Pro 7 還是靠簡單取勝",
                        "body": (
                            "如果你重視乾淨的 App 跟五分鐘設定，勝過深度設定選單，Eero Pro 7 守第三。"
                            "朋友裡不懂技術、只想要快速 Wi-Fi 又不想搞東搞西的，我都推這台。"
                        ),
                    },
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("done", name)


# ---------------------------------------------------------------------------
# 5) PORTABLE PROJECTORS
# ---------------------------------------------------------------------------
def projectors():
    name = "best-portable-projectors.json"
    d, p = load(name)
    entry = {
        "date": DATE,
        "rankings": last_rankings(d),
        "references": [
            {
                "title": "XGIMI MoGo 4 Laser Projector Review",
                "url": "https://www.rtings.com/projector/reviews/xgimi/mogo-4-laser-projector",
                "source": "RTINGS",
            },
            {
                "title": "XGIMI MoGo 4 Portable Projector vs LG CineBeam Q 4K UHD Portable Laser Projector Comparison",
                "url": "https://hometheaterreview.com/vs/xgimi-mogo-4-portable-projector-2025-vs-lg-cinebeam-q-4k-uhd-portable-laser-projector-comparison/",
                "source": "HomeTheaterReview",
            },
            {
                "title": "Triple Laser Portable Smart Projector | MoGo 4 Laser",
                "url": "https://us.xgimi.com/products/mogo-4-laser",
                "source": "XGIMI",
            },
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "The XGIMI MoGo 4 Laser stays at number one going into June and the RTINGS review reinforces why. "
                    "Its triple laser engine puts out 550 ISO lumens, throws a usable 40 to 200 inch image, and the "
                    "built-in battery delivers up to 2.5 hours of playback in Eco mode, which is enough for a movie in "
                    "the backyard. The Intelligent Screen Adaptation tech that snaps the image square and dodges "
                    "obstacles is the feature that makes it feel effortless to set down anywhere. The LG CineBeam Q "
                    "holds second and it is the pick when resolution is your priority. It runs native 4K at 3840 by "
                    "2160 and claims 500 ANSI lumens, so on a fixed screen it resolves more detail than the MoGo's "
                    "1080p panel. The tradeoff is that ANSI lumens generally land a touch dimmer in the real world than "
                    "an equivalent ISO rating, and the MoGo's laser color simply pops more in a casual setting. Hisense "
                    "M2 Pro stays third for buyers who want the brightest image and do not mind sacrificing some "
                    "portability and battery. Nebula Mars 3 remains the rugged outdoor champion thanks to its big "
                    "battery and brightness, and the Mars 3 Air and Capsule 3 Laser keep the lower spots for travelers "
                    "who prize size above all. My recommendation this week is simple: the MoGo 4 Laser for the best "
                    "all-around portable experience, the CineBeam Q if you want native 4K and have a proper screen."
                ),
                "highlights": [
                    {
                        "title": "XGIMI MoGo 4 Laser holds number one on effortless setup",
                        "body": (
                            "550 ISO lumens from a triple laser engine, a 40 to 200 inch image, and up to 2.5 hours of "
                            "battery in Eco mode. The Intelligent Screen Adaptation that auto-squares the picture and "
                            "avoids obstacles is what makes it the easiest projector here to set down anywhere and just "
                            "watch."
                        ),
                    },
                    {
                        "title": "LG CineBeam Q is the pick when you want native 4K",
                        "body": (
                            "Native 4K at 3840 by 2160 and a claimed 500 ANSI lumens means it resolves more detail on "
                            "a fixed screen than the MoGo's 1080p panel. If sharpness on a real screen is your priority, "
                            "this is the second-place pick worth the look."
                        ),
                    },
                    {
                        "title": "Laser color is why the MoGo still leads casually",
                        "body": (
                            "ANSI lumens generally translate to slightly dimmer real-world output than an equivalent "
                            "ISO rating, and the MoGo's triple-laser color simply pops more in a backyard or living "
                            "room setting. For casual portable use the MoGo's image is the more satisfying one."
                        ),
                    },
                    {
                        "title": "Nebula Mars 3 stays the rugged outdoor champion",
                        "body": (
                            "A big battery, strong brightness, and a tough build keep the Mars 3 as the pick for "
                            "camping and backyard movie nights where durability and runtime matter more than the last "
                            "bit of sharpness."
                        ),
                    },
                ],
            },
            "zh-tw": {
                "commentary": (
                    "進入六月，XGIMI MoGo 4 Laser 還是守在第一，RTINGS 的評測再次說明原因。"
                    "三雷射引擎打出 550 ISO 流明，可投 40 到 200 吋的可用畫面，內建電池在 Eco 模式下可播放 2.5 小時，"
                    "在後陽台看一部電影剛剛好。智慧螢幕適應技術會自動把畫面拉正、避開障礙物，這就是它放哪裡都能輕鬆開看的關鍵功能。\n\n"
                    "LG CineBeam Q 守第二，是把解析度擺第一時的選擇。它跑原生 4K，3840 乘 2160，宣稱 500 ANSI 流明，"
                    "在固定的布幕上比 MoGo 的 1080p 面板解析出更多細節。代價是 ANSI 流明在真實世界通常比同等 ISO 數字暗一點，"
                    "而 MoGo 的雷射色彩在隨手投放的場景裡就是更跳。\n\n"
                    "Hisense M2 Pro 守第三，給想要最亮畫面、又不介意犧牲一點攜帶性跟電池的人。"
                    "Nebula Mars 3 還是戶外硬派冠軍，靠大電池跟亮度撐場，Mars 3 Air 跟 Capsule 3 Laser 守後段，"
                    "給把體積擺第一的旅行族。這禮拜建議很簡單：要最全能的攜帶體驗就選 MoGo 4 Laser，"
                    "想要原生 4K 又有正經布幕就選 CineBeam Q。"
                ),
                "highlights": [
                    {
                        "title": "XGIMI MoGo 4 Laser 靠輕鬆開看守住第一",
                        "body": (
                            "三雷射引擎打出 550 ISO 流明，可投 40 到 200 吋，Eco 模式電池最多 2.5 小時。"
                            "智慧螢幕適應自動把畫面拉正、避開障礙物，就是這個讓它成為這裡最好擺、放下就能看的投影機。"
                        ),
                    },
                    {
                        "title": "想要原生 4K 就選 LG CineBeam Q",
                        "body": (
                            "原生 4K，3840 乘 2160，宣稱 500 ANSI 流明，在固定布幕上比 MoGo 的 1080p 面板解析出更多細節。"
                            "如果你重視正經布幕上的銳利度，這個第二名值得一看。"
                        ),
                    },
                    {
                        "title": "隨手投放時 MoGo 還領先，靠的是雷射色彩",
                        "body": (
                            "ANSI 流明在真實世界通常比同等 ISO 數字暗一點，而 MoGo 的三雷射色彩在後陽台或客廳就是更跳。"
                            "輕鬆攜帶使用的場景，MoGo 的畫面就是看起來更爽。"
                        ),
                    },
                    {
                        "title": "Nebula Mars 3 還是戶外硬派冠軍",
                        "body": (
                            "大電池、夠亮、機身耐操，讓 Mars 3 在露營跟後院電影夜還是首選，"
                            "這種場合耐用度跟續航比最後那一點銳利度更重要。"
                        ),
                    },
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("done", name)


# ---------------------------------------------------------------------------
# 6) SMART RINGS
# ---------------------------------------------------------------------------
def smart_rings():
    name = "best-smart-rings.json"
    d, p = load(name)
    entry = {
        "date": DATE,
        "rankings": last_rankings(d),
        "references": [
            {
                "title": "Best smart ring 2026: the best from Oura, Samsung, RingConn and more",
                "url": "https://www.techradar.com/health-fitness/fitness-trackers/best-smart-ring",
                "source": "TechRadar",
            },
            {
                "title": "Best Smart Rings 2026: 6 Picks for Sleep, Fitness and Cycle Tracking",
                "url": "https://the-gadgeteer.com/2026/05/23/best-smart-rings-health-fitness-sleep-tracking/",
                "source": "The Gadgeteer",
            },
            {
                "title": "Best Smart Rings in 2026: Oura, Samsung, Ultrahuman, RingConn, and Luna",
                "url": "https://askvora.com/blog/best-smart-rings-2026",
                "source": "Vora",
            },
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "The smart ring race at the top is still a dead heat and I have the Samsung Galaxy Ring and the "
                    "Oura Ring 4 tied at the front for good reason. The Galaxy Ring takes the nominal number one because "
                    "it delivers the best overall value: strong sleep and activity tracking with no subscription, plus "
                    "the tightest integration if you live in the Samsung health ecosystem. Several 2026 roundups, "
                    "including the late-May Gadgeteer guide, now name it best overall. Oura Ring 4 sits right behind and "
                    "remains the choice when health depth is the priority. Its Readiness score and sleep analytics are "
                    "still the most refined in the category, and the app experience is the best in class. The catch "
                    "stays the same: you pay a monthly subscription to unlock the full feature set, which is why a "
                    "no-fee rival edges it on value. RingConn Gen 2 holds third and it is the battery champion, with "
                    "reviewers consistently citing its generous multi-day runtime, comfortable lightweight build, and a "
                    "no-subscription model. For people who hate charging wearables, this is the one. Ultrahuman Ring Pro "
                    "stays fourth as the strong no-subscription alternative with deep metabolic features. My guidance "
                    "this week is unchanged: Galaxy Ring if you own a Samsung phone and want zero fees, Oura Ring 4 if "
                    "you want the deepest recovery analytics and accept the subscription, RingConn Gen 2 if battery life "
                    "is your top priority."
                ),
                "highlights": [
                    {
                        "title": "Samsung Galaxy Ring takes number one on no-fee value",
                        "body": (
                            "Strong sleep and activity tracking with no subscription, plus the tightest fit inside the "
                            "Samsung health ecosystem. Late-May 2026 roundups including The Gadgeteer now name it best "
                            "overall, and the no-fee model is the reason it edges Oura at the top."
                        ),
                    },
                    {
                        "title": "Oura Ring 4 is still the choice for health depth",
                        "body": (
                            "The Readiness score and sleep analytics remain the most refined in the category and the "
                            "app is best in class. The monthly subscription to unlock full features is the only thing "
                            "keeping it from the outright top spot on value."
                        ),
                    },
                    {
                        "title": "RingConn Gen 2 is the battery and comfort champion",
                        "body": (
                            "Reviewers consistently praise its multi-day runtime, light comfortable build, and "
                            "no-subscription model. If you hate charging wearables every couple of days, this is the "
                            "ring to buy, and it holds a confident third."
                        ),
                    },
                    {
                        "title": "Ultrahuman Ring Pro is the deep no-fee alternative",
                        "body": (
                            "A strong no-subscription option with deep metabolic and recovery features keeps the Ring "
                            "Pro in fourth. For data-focused buyers who want detail without a monthly bill, it is the "
                            "smart pick below the big two."
                        ),
                    },
                ],
            },
            "zh-tw": {
                "commentary": (
                    "智慧戒指最頂端還是難分難解，我把 Samsung Galaxy Ring 跟 Oura Ring 4 並列在前，理由很充分。"
                    "Galaxy Ring 拿名義上的第一，因為它整體 CP 值最好：睡眠跟活動追蹤都夠強又不收訂閱費，"
                    "如果你活在三星健康生態圈裡，整合度也最緊密。好幾份 2026 評測，包括五月底 Gadgeteer 那篇，現在都把它列為整體最佳。\n\n"
                    "Oura Ring 4 緊跟在後，還是把健康深度擺第一時的選擇。它的 Readiness 分數跟睡眠分析在這個品類還是最細緻的，"
                    "App 體驗也是同級最佳。坑還是老樣子：要解鎖完整功能得付月費，這就是為什麼一個不收費的對手在 CP 值上壓它一點。\n\n"
                    "RingConn Gen 2 守第三，是續航冠軍，評測一致提到它多日的慷慨續航、輕巧舒適的機身、還有不收訂閱費。"
                    "討厭一直幫穿戴裝置充電的人，就買這個。Ultrahuman Ring Pro 守第四，是不收訂閱費又有深度代謝功能的強力選擇。"
                    "這禮拜建議不變：用三星手機又想零月費就選 Galaxy Ring，想要最深的恢復分析又能接受訂閱就選 Oura Ring 4，"
                    "把續航擺第一就選 RingConn Gen 2。"
                ),
                "highlights": [
                    {
                        "title": "Samsung Galaxy Ring 靠零月費 CP 值拿第一",
                        "body": (
                            "睡眠跟活動追蹤都夠強又不收訂閱費，在三星健康生態圈裡整合最緊密。"
                            "五月底 2026 評測包括 The Gadgeteer 現在都把它列為整體最佳，零月費就是它在頂端壓過 Oura 的原因。"
                        ),
                    },
                    {
                        "title": "Oura Ring 4 還是健康深度的首選",
                        "body": (
                            "Readiness 分數跟睡眠分析在這個品類還是最細緻，App 也是同級最佳。"
                            "唯一讓它在 CP 值上拿不到絕對第一的，就是解鎖完整功能要付的那筆月費。"
                        ),
                    },
                    {
                        "title": "RingConn Gen 2 是續航跟舒適冠軍",
                        "body": (
                            "評測一致稱讚它多日續航、輕巧舒適的機身、不收訂閱費。"
                            "討厭每兩天就要幫穿戴裝置充電的人，買這個就對了，第三名守得很穩。"
                        ),
                    },
                    {
                        "title": "Ultrahuman Ring Pro 是深度又免月費的替代選擇",
                        "body": (
                            "不收訂閱費又有深度代謝跟恢復功能的強力選項，讓 Ring Pro 守第四。"
                            "重視數據、想要細節又不想付月費的人，這是兩大廠之下最聰明的選擇。"
                        ),
                    },
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("done", name)


# ---------------------------------------------------------------------------
# 7) WIRELESS EARBUDS
# ---------------------------------------------------------------------------
def earbuds():
    name = "best-wireless-earbuds.json"
    d, p = load(name)
    entry = {
        "date": DATE,
        "rankings": last_rankings(d),
        "references": [
            {
                "title": "I've tested the Sony WF-1000XM6 and rate them as the best wireless earbuds you can buy right now",
                "url": "https://www.whathifi.com/headphones/wireless-earbuds/the-sony-wf-1000xm6-are-officially-our-favourite-flagship-wireless-earbuds",
                "source": "What Hi-Fi",
            },
            {
                "title": "Sony WF-1000XM6 review: Bigger and better",
                "url": "https://www.soundguys.com/sony-wf-1000xm6-review-152013/",
                "source": "SoundGuys",
            },
            {
                "title": "Best true wireless earbuds of 2026, tried and tested",
                "url": "https://www.cnn.com/cnn-underscored/reviews/best-true-wireless-earbuds",
                "source": "CNN Underscored",
            },
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "The Sony WF-1000XM6 stays at number one going into June and the reviews keep cementing the verdict. "
                    "What Hi-Fi now rates them the best flagship wireless earbuds you can buy, and SoundGuys calls them "
                    "Sony's best-sounding earbuds to date. The package is complete: elite active noise cancellation, "
                    "audiophile-grade sound, standout microphone performance from AI beamforming, 9-plus hours of "
                    "battery, LDAC for hi-res on Android, IPX4 sweat resistance, and a 10-band EQ in the app. That "
                    "combination of mic quality and noise cancelling is exactly why it is the current all-arounder to "
                    "beat. The AirPods Pro 2 hold second and stay the obvious pick for iPhone owners, delivering "
                    "reliable sound, excellent ANC, and seamless Apple ecosystem handoff. The Bose QuietComfort Earbuds "
                    "remain third for comfort-first listeners. Bose tunes a frequency response with sensible bass and a "
                    "target-curve upper midrange, and the fit is the most comfortable in this group, though battery "
                    "runs a little shorter at five-plus hours per charge. Samsung Buds4 Pro hold fourth and remain the "
                    "smart choice for Galaxy owners who want tight ecosystem features. My advice this week does not "
                    "change: the WF-1000XM6 if you want the best all-around earbuds regardless of phone, AirPods Pro 2 "
                    "for iPhone, Bose if comfort and fit decide it for you."
                ),
                "highlights": [
                    {
                        "title": "Sony WF-1000XM6 stays number one as the all-around champion",
                        "body": (
                            "What Hi-Fi rates them the best flagship buds you can buy and SoundGuys calls them Sony's "
                            "best-sounding yet. Elite ANC, audiophile sound, AI-beamforming mics, 9-plus hours of "
                            "battery, LDAC, and IPX4 make this the current all-arounder to beat."
                        ),
                    },
                    {
                        "title": "AirPods Pro 2 stay the iPhone pick at second",
                        "body": (
                            "Reliable sound, excellent ANC, and seamless Apple ecosystem handoff keep the AirPods Pro 2 "
                            "the obvious choice for iPhone owners. If you live in Apple's world, this is still the "
                            "frictionless answer."
                        ),
                    },
                    {
                        "title": "Bose QuietComfort Earbuds win on comfort and fit",
                        "body": (
                            "Sensible bass, a target-curve upper midrange, and the most comfortable fit in this group "
                            "keep Bose at third. Battery is a little shorter at five-plus hours per charge, so this is "
                            "the pick when comfort, not runtime, is the deciding factor."
                        ),
                    },
                    {
                        "title": "Samsung Buds4 Pro are the Galaxy ecosystem pick",
                        "body": (
                            "Balanced sound, solid ANC, and tight Galaxy ecosystem features keep the Buds4 Pro in "
                            "fourth. For Samsung phone owners who want seamless pairing and feature integration, this "
                            "is the smart buy."
                        ),
                    },
                ],
            },
            "zh-tw": {
                "commentary": (
                    "進入六月，Sony WF-1000XM6 還是守在第一，評測一篇接一篇把這個結論釘死。"
                    "What Hi-Fi 現在把它評為你買得到的最強旗艦真無線，SoundGuys 說它是 Sony 至今聲音最好的耳機。"
                    "這套組合很完整：頂級主動降噪、發燒級聲音、AI 波束成形帶來的出色通話麥克風、9 小時以上續航、"
                    "Android 上有 LDAC 高解析、IPX4 防汗、App 裡還有十段 EQ。麥克風品質加降噪這組合，"
                    "就是它現在全能王座難以撼動的原因。\n\n"
                    "AirPods Pro 2 守第二，還是 iPhone 用戶的明顯選擇，聲音穩、ANC 出色、蘋果生態無縫接續。"
                    "Bose QuietComfort Earbuds 守第三，給把舒適擺第一的人。Bose 調出合理的低頻跟貼目標曲線的中高頻，"
                    "配戴是這組裡最舒服的，只是續航短一點，每次充電五小時出頭。\n\n"
                    "Samsung Buds4 Pro 守第四，還是 Galaxy 用戶想要緊密生態功能時的聰明選擇。"
                    "這禮拜建議不變：不管用什麼手機都想要最全能的耳機就選 WF-1000XM6，iPhone 用 AirPods Pro 2，"
                    "舒適跟配戴是你的決勝點就選 Bose。"
                ),
                "highlights": [
                    {
                        "title": "Sony WF-1000XM6 以全能冠軍之姿守住第一",
                        "body": (
                            "What Hi-Fi 把它評為你買得到的最強旗艦耳機，SoundGuys 說是 Sony 至今聲音最好的。"
                            "頂級 ANC、發燒級聲音、AI 波束成形麥克風、9 小時以上續航、LDAC、IPX4，"
                            "讓它成為現在難以撼動的全能王。"
                        ),
                    },
                    {
                        "title": "AirPods Pro 2 守第二，還是 iPhone 首選",
                        "body": (
                            "聲音穩、ANC 出色、蘋果生態無縫接續，讓 AirPods Pro 2 還是 iPhone 用戶的明顯選擇。"
                            "活在蘋果世界裡的人，這還是最無摩擦的答案。"
                        ),
                    },
                    {
                        "title": "Bose QuietComfort Earbuds 靠舒適跟配戴取勝",
                        "body": (
                            "合理的低頻、貼目標曲線的中高頻、加上這組裡最舒服的配戴，讓 Bose 守第三。"
                            "續航短一點，每次充電五小時出頭，所以這是舒適而非續航當決勝點時的選擇。"
                        ),
                    },
                    {
                        "title": "Samsung Buds4 Pro 是 Galaxy 生態的選擇",
                        "body": (
                            "均衡的聲音、紮實的 ANC、緊密的 Galaxy 生態功能，讓 Buds4 Pro 守第四。"
                            "用三星手機、想要無縫配對跟功能整合的人，這是聰明的買法。"
                        ),
                    },
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("done", name)


if __name__ == "__main__":
    ai_meeting()
    dash_cams()
    gaming_mice()
    mesh_wifi()
    projectors()
    smart_rings()
    earbuds()
    print("ALL DONE")
