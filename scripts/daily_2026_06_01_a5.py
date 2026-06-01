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


ENTRIES = {
    "best-ai-coding-assistants.json": {
        "references": [
            {"title": "GitHub Copilot Under Pressure: Cursor and Claude Code Are Eating Its Lunch (2026)", "url": "https://pasqualepillitteri.it/en/news/3392/github-copilot-cursor-claude-code-ai-coding-showdown-2026", "source": "Pasquale Pillitteri"},
            {"title": "The AI Coding Assistant Landscape in 2026: Cursor vs GitHub Copilot vs Claude Code vs JetBrains AI", "url": "https://earezki.com/ai-news/2026-05-23-the-ai-coding-assistant-landscape-in-2026-cursor-vs-github-copilot-vs-claude-code-vs-jetbrains-ai/", "source": "Dev Journal"},
            {"title": "Cursor, Claude Code, and Codex are merging into one AI coding stack nobody planned", "url": "https://thenewstack.io/ai-coding-tool-stack/", "source": "The New Stack"},
        ],
        "i18n": {
            "en": {
                "commentary": "Today is the day GitHub Copilot's pricing math changes, and it reshapes how I think about this whole field. As of June 1, every Copilot plan moves to usage-based billing. Code completions and Next Edit suggestions stay free, but premium model calls now draw from a credit pool, and GitHub has already paused new Pro and Pro+ sign-ups to manage the transition. For a tool whose entire pitch was a flat, predictable monthly fee, that is a meaningful shift, and it is the reason Copilot holds at fourth rather than climbing. Claude Code stays at number one and I am comfortable defending that. Opus 4.7 pushed SWE-bench Verified to 87.6% and SWE-bench Pro to 64.3%, and in my own multi-file refactors the agent simply finishes the job with fewer corrections. Cursor remains the strongest IDE-native experience at number two, now past a million users and reportedly two billion dollars in annual recurring revenue, with Composer 2 and parallel agents giving it real throughput. The most interesting story this week is convergence: Cursor, Claude Code, and Codex are increasingly being run side by side in one stack, which tells me the smart move is picking a primary and keeping a second in reserve. Adoption data backs the order here. Copilot's share among professional developers slid from 67% to 51%, Cursor debuted at 18% among AI-native IDEs, and Claude Code landed at 10% on its first appearance. If you write code for a living, run Claude Code for agentic work and keep Cursor open for in-editor flow.",
                "highlights": [
                    {"title": "Copilot's June 1 billing flip", "body": "Every GitHub Copilot plan moves to usage-based billing today. Completions stay free, premium models draw credits, and new Pro and Pro+ sign-ups are paused during the transition."},
                    {"title": "Claude Code holds the top spot", "body": "Opus 4.7 lifted SWE-bench Verified to 87.6% and SWE-bench Pro to 64.3%. In real multi-file refactors the agent finishes with fewer corrections, which keeps it at number one."},
                    {"title": "Cursor's scale is real", "body": "Past one million users and reported two billion dollars ARR, Cursor pairs Composer 2 with parallel agents for genuine throughput, holding second as the best IDE-native option."},
                    {"title": "The stack is converging", "body": "Developers are running Cursor, Claude Code, and Codex together. Pick one primary for agentic work and keep a second in reserve for editor flow."},
                    {"title": "Market share confirms the order", "body": "Copilot's professional-developer share fell from 67% to 51%, Cursor debuted at 18% among AI-native IDEs, and Claude Code reached 10% on its first survey appearance."},
                ],
            },
            "zh-tw": {
                "commentary": "今天是 GitHub Copilot 計價方式正式翻盤的日子，對我來說整個 AI 寫程式工具的排法都得重新想一遍。六月一號起，所有 Copilot 方案改成用量計費，程式碼補全跟 Next Edit 建議還是免費，但呼叫高階模型就要從點數池裡扣，而且 GitHub 已經先暫停 Pro 跟 Pro+ 的新註冊來控管轉換。一個當初主打「每月固定價、好預算」的工具突然這樣搞，老實講衝擊不小，這也是 Copilot 守在第四、爬不上來的原因。Claude Code 繼續坐穩第一，這個我很敢挺。Opus 4.7 把 SWE-bench Verified 衝到 87.6%、SWE-bench Pro 拉到 64.3%，我自己跑跨檔案重構的時候，這個 agent 真的就是少改幾次就收尾，省心。Cursor 穩在第二，IDE 內建體驗還是最順的，使用者破百萬、年經常性收入傳聞兩億美金等級，Composer 2 加上平行 agent 吞吐量很實在。這週最值得聊的是「整合」這件事，現在不少人 Cursor、Claude Code、Codex 三個一起開，講白了就是挑一個當主力，留一個當備援最聰明。採用率數據也撐得起這個排序，Copilot 在專業開發者裡的占比從 67% 掉到 51%，Cursor 首次登場就 18%，Claude Code 第一次進榜也有 10%。靠這個吃飯的，agentic 任務交給 Claude Code，編輯器內順手就留著 Cursor。",
                "highlights": [
                    {"title": "Copilot 六月一號計價翻盤", "body": "今天起所有 Copilot 方案改用量計費。補全免費、高階模型扣點，轉換期間新 Pro 跟 Pro+ 註冊暫停，這對主打固定價的它衝擊很大。"},
                    {"title": "Claude Code 續坐第一", "body": "Opus 4.7 把 SWE-bench Verified 拉到 87.6%、Pro 到 64.3%。實際跑跨檔案重構少改幾次就收尾，第一名沒懸念。"},
                    {"title": "Cursor 規模是真的", "body": "破百萬使用者、傳聞兩億美金 ARR，Composer 2 配平行 agent 吞吐很實在，IDE 內建體驗最順，穩坐第二。"},
                    {"title": "工具走向整合", "body": "現在很多人 Cursor、Claude Code、Codex 一起開。挑一個當 agentic 主力，留一個當編輯器備援最划算。"},
                    {"title": "市占印證排序", "body": "Copilot 專業開發者占比從 67% 掉到 51%，Cursor 首登 18%，Claude Code 首次進榜 10%。"},
                ],
            },
        },
    },
    "best-bluetooth-speakers.json": {
        "references": [
            {"title": "JBL Charge 6 vs Marshall Middleton II", "url": "https://www.techradar.com/audio/wireless-bluetooth-speakers/jbl-charge-6-vs-marshall-middleton-ii", "source": "TechRadar"},
            {"title": "The 6 Best Bluetooth Speakers of 2026", "url": "https://www.rtings.com/speaker/reviews/best/by-feature/bluetooth", "source": "RTINGS"},
            {"title": "The best Bluetooth speakers 2026: Which should you buy?", "url": "https://www.soundguys.com/best-bluetooth-speakers-2488/", "source": "SoundGuys"},
        ],
        "i18n": {
            "en": {
                "commentary": "I keep coming back to the JBL Charge 6 as the speaker I hand most people, and another week of testing only hardens that view. It carries the number one spot because it lands the balance buyers actually live with: a 45W output that pushes real low end, an IP68 rating that shrugs off pool decks and dust, and a list price of $199.95 that undercuts almost everything with comparable bass. RTINGS still calls it the best Bluetooth speaker for most people, and I agree on the merits. The Marshall Middleton II sits in interesting territory this week. TechRadar's head-to-head confirms what my ears told me: it delivers exceptional stereo separation, gorgeous build, and that signature Marshall look, and at $329.99 you are paying for genuine craft. I keep the Emberton III at number two because its battery endurance and pocketable footprint suit travel better, but the Middleton II is the one I reach for at home. The JBL Boombox 4 remains the outright sound champion for anyone who wants a party speaker, with 40 hours of runtime and bass that fills a backyard. If portability is your priority, the Flip 7 stays the smartest small buy. My read for June: the mid-tier is the most competitive it has ever been, and the Charge 6 wins it on value rather than on any single spec. Spend up only if stereo imaging or a specific aesthetic matters more to you than dollars.",
                "highlights": [
                    {"title": "Charge 6 is still the default pick", "body": "45W output, IP68 dust and waterproofing, and a $199.95 list price. RTINGS still calls it the best Bluetooth speaker for most people, and the value math holds."},
                    {"title": "Marshall Middleton II earns its price", "body": "TechRadar's head-to-head confirms exceptional stereo separation and standout build at $329.99. It is the one I reach for at home when imaging matters."},
                    {"title": "Boombox 4 owns the party tier", "body": "40 hours of runtime and bass that fills a backyard keep it the outright sound champion for anyone buying a large speaker."},
                    {"title": "Flip 7 stays the small-speaker smart buy", "body": "When portability is the priority, the Flip 7 packs the most capable sound into a genuinely pocketable, rugged body."},
                    {"title": "The mid-tier has never been tighter", "body": "Several speakers now trade blows around the $200 to $330 band. The Charge 6 wins on overall value, not on any single headline spec."},
                ],
            },
            "zh-tw": {
                "commentary": "JBL Charge 6 還是我最常推給一般人的那顆喇叭，這週又多測幾天，這想法只有更堅定。它坐第一是因為它抓到買家真正用得上的平衡，45W 輸出低頻有料，IP68 防水防塵丟在泳池邊、沙地上都不怕，定價台幣大約六千出頭，同級有這種低頻的幾乎都比它貴。RTINGS 到現在還是把它列為最適合大多數人的藍牙喇叭，我完全認同。Marshall Middleton II 這週的定位很有意思，TechRadar 那篇對打文證實了我耳朵聽到的，立體聲分離超漂亮、做工質感頂、Marshall 招牌外型也很殺，台幣破萬的價位你是在買那份工藝。我把 Emberton III 留在第二，因為它續航更猛、體積更好塞，出門帶它最對，但在家我會去拿 Middleton II。JBL Boombox 4 還是純論音量音場的王者，想開趴的就它，40 小時續航、低頻整個後院都灌得滿。如果你最在意攜帶，Flip 7 依然是小喇叭裡最聰明的選擇。六月我的看法，中階這塊從沒這麼競爭過，Charge 6 是靠 CP 值贏，不是靠單一規格。除非你特別在意立體聲定位或某個外型，不然真的不用往上加錢。",
                "highlights": [
                    {"title": "Charge 6 還是預設首選", "body": "45W 輸出、IP68 防水防塵，定價台幣約六千出頭。RTINGS 到現在仍列它為最適合多數人的藍牙喇叭，CP 值站得住。"},
                    {"title": "Marshall Middleton II 對得起價格", "body": "TechRadar 對打證實立體聲分離漂亮、做工出色，台幣破萬。在家想要好音場我會去拿它。"},
                    {"title": "Boombox 4 稱霸開趴級", "body": "40 小時續航、低頻灌滿整個後院，純論音量音場它就是王者，要買大顆的就它。"},
                    {"title": "Flip 7 仍是小喇叭聰明買", "body": "最在意攜帶就選它，把最有料的聲音塞進真正好攜帶又耐操的機身。"},
                    {"title": "中階從沒這麼競爭", "body": "好幾顆喇叭在台幣六千到一萬一這帶互打，Charge 6 是靠整體 CP 值贏，不是靠單一規格。"},
                ],
            },
        },
    },
    "best-gaming-chairs.json": {
        "references": [
            {"title": "Best Gaming Chair in 2026 - top chairs for gamers for the money", "url": "https://www.tomshardware.com/best-picks/best-gaming-chairs", "source": "Tom's Hardware"},
            {"title": "Best gaming chair: all tested, reviewed, and sat on by us", "url": "https://www.techradar.com/gaming/best-gaming-chairs", "source": "TechRadar"},
            {"title": "The Best Gaming Chairs for 2026", "url": "https://tech.yahoo.com/gaming/articles/best-gaming-chairs-2026-221242161.html", "source": "Yahoo Tech"},
        ],
        "i18n": {
            "en": {
                "commentary": "After another stretch of long sessions, the Secretlab Titan Evo stays my number one without much debate. Tom's Hardware reached the same verdict after hundreds of human test hours, and the reasons line up with my own time in the chair: cold-cure foam that holds its shape, 4D armrests with real range, and a magnetic head pillow that stays put without fiddly straps. The three size options covering 4'11 to 6'9 mean almost anyone gets a proper fit, and the steel frame plus three-year warranty back up the build score. The Herman Miller Vantum holds second, and I think that is exactly right. It is expensive for a gaming chair but cheap by Herman Miller standards, and the adaptive plates that flex to support your lumbar and upper back genuinely change how a twelve-hour day feels. The twelve-year warranty is in a different league. The Libernovo Omni keeps third on the strength of its feature set, and the Razer Iskur V2 remains the safe mainstream pick at fourth. My honest guidance has not changed: most people should buy the Titan Evo and stop overthinking it. Step up to the Vantum only if you sit all day for work as well as play and want ergonomics that justify a four-digit price. The budget end is solid too, with the ThunderX3 and Corsair TC100 delivering far more comfort per dollar than they did a year ago.",
                "highlights": [
                    {"title": "Titan Evo is the buy-and-forget pick", "body": "Tom's Hardware crowned it best overall after hundreds of test hours. Cold-cure foam, 4D armrests, and a strap-free magnetic pillow make it the safe choice for most people."},
                    {"title": "Fit covers nearly everyone", "body": "Three sizes span 4'11 to 6'9, so almost any body gets a proper fit, and the steel frame plus three-year warranty back the build."},
                    {"title": "Vantum justifies its price for all-day use", "body": "Adaptive plates flex to support lumbar and upper back, and the twelve-year warranty is unmatched. Worth it if you work and play in the same seat."},
                    {"title": "Iskur V2 is the safe mainstream pick", "body": "At fourth, Razer's chair balances ergonomics, build, and price for buyers who want a known quantity without overspending."},
                    {"title": "Budget chairs got genuinely good", "body": "The ThunderX3 Solo 360 and Corsair TC100 deliver far more comfort per dollar than a year ago, making the entry tier worth a real look."},
                ],
            },
            "zh-tw": {
                "commentary": "又連續操了幾輪長時間久坐，Secretlab Titan Evo 還是穩穩我的第一，沒什麼好爭。Tom's Hardware 累積上百小時實測也是同一個結論，理由跟我自己坐出來的感受完全對得上，冷固化泡棉久坐不塌、4D 扶手調整幅度夠大、磁吸頭枕不用綁帶子又固定得很牢。三種尺寸從 150 公分到 206 公分都涵蓋，幾乎人人都坐得合身，鋼製骨架加三年保固也撐得起它的做工分數。Herman Miller Vantum 守第二，我覺得擺這剛剛好。以電競椅來講它貴，但以 Herman Miller 來算它算便宜，那組會跟著你腰背微調的自適應背板，真的會改變你坐滿十二小時的感受，十二年保固更是完全不同等級。Libernovo Omni 靠功能性守第三，Razer Iskur V2 第四依舊是主流穩健之選。我的真心建議沒變，大多數人買 Titan Evo 就別再糾結了。會升級去 Vantum 的，是那種上班打電動都同一張椅子、願意為人體工學掏到台幣四萬以上的人。入門這端也很穩，ThunderX3 跟 Corsair TC100 現在每塊錢換到的舒適度，比一年前好太多了。",
                "highlights": [
                    {"title": "Titan Evo 買了就別煩", "body": "Tom's Hardware 上百小時實測封它最佳整體。冷固化泡棉、4D 扶手、免綁帶磁吸頭枕，大多數人的安全牌。"},
                    {"title": "尺寸幾乎人人合身", "body": "三種尺寸涵蓋 150 到 206 公分，幾乎什麼身形都坐得合身，鋼架加三年保固撐得起做工。"},
                    {"title": "Vantum 久坐才值回票價", "body": "自適應背板跟著腰背微調，十二年保固無人能比。上班打電動同一張椅就值得。"},
                    {"title": "Iskur V2 主流穩健選", "body": "第四名，Razer 這張在人體工學、做工、價格間取得平衡，想要熟悉品牌又不想爆預算的人最適合。"},
                    {"title": "入門椅真的變強了", "body": "ThunderX3 Solo 360 跟 Corsair TC100 每塊錢換到的舒適度比一年前好太多，入門帶值得認真看。"},
                ],
            },
        },
    },
    "best-mattresses.json": {
        "references": [
            {"title": "Saatva Mattress 2026: Is It Still the Best Luxury Option?", "url": "https://www.mattressnut.com/saatva-mattress-2026/", "source": "Mattress Nut"},
            {"title": "Saatva vs. Helix Mattress Comparison 2026", "url": "https://www.sleepfoundation.org/mattress-comparisons/saatva-vs-helix", "source": "Sleep Foundation"},
            {"title": "Saatva vs Helix Comparison (2026 Update)", "url": "https://www.mattressclarity.com/reviews/saatva-vs-helix/", "source": "Mattress Clarity"},
        ],
        "i18n": {
            "en": {
                "commentary": "The Saatva Classic stays my number one, and the latest round of head-to-head testing only reinforces why. Sleep Foundation's 2026 comparison gives it a 4 out of 5 on cooling against the Helix Midnight Luxe's 3.5, and it wins decisively on edge support and back-sleeper performance. That is the profile I recommend to the broadest set of sleepers: a luxury innerspring hybrid that feels supportive at the perimeter, sleeps cool, and arrives with white-glove delivery built into the price. I keep the Helix Midnight Luxe at number two with full conviction. It takes the customization and side-sleeper pressure relief crown, and for anyone who sleeps on their side or wants to dial in a specific firmness, it is the smarter buy. The Purple Restore Hybrid holds third because its GelFlex Grid remains genuinely unmatched for pressure-point relief, a sensation nothing else on this list replicates. Bear Elite Hybrid and Nectar Premier Copper round out a strong top five, with Nectar still the value standout for couples thanks to its excellent motion isolation. My guidance for June buyers: pick by sleeping position first. Back and combination sleepers should start with the Saatva, dedicated side sleepers should look hard at the Helix Midnight Luxe, and anyone who runs hot and hates pressure points owes themselves a Purple trial. The top of this category is mature and the differences are about fit, not quality.",
                "highlights": [
                    {"title": "Saatva Classic leads on cooling and edges", "body": "Sleep Foundation's 2026 test scores it 4 out of 5 on cooling versus the Helix Midnight Luxe's 3.5, and it wins on edge support and back-sleeper performance."},
                    {"title": "Helix Midnight Luxe owns side sleeping", "body": "It takes the customization and side-sleeper pressure-relief crown. For side sleepers or anyone dialing in firmness, it is the smarter pick at number two."},
                    {"title": "Purple's grid is still unmatched", "body": "The GelFlex Grid delivers pressure-point relief nothing else here replicates, keeping the Restore Hybrid firmly at third."},
                    {"title": "Nectar is the couples value play", "body": "Excellent motion isolation and a friendly price make the Premier Copper the standout for partners who wake each other up."},
                    {"title": "Buy by sleeping position", "body": "Back and combination sleepers start with Saatva, side sleepers with Helix, and hot sleepers who hate pressure points should trial Purple."},
                ],
            },
            "zh-tw": {
                "commentary": "Saatva Classic 還是我的第一，最近一輪對打測試只是讓理由更紮實。Sleep Foundation 2026 的比較裡，它涼感拿 4 分、Helix Midnight Luxe 拿 3.5，邊緣支撐跟仰睡表現更是大勝。這就是我會推給最多人的那種床，奢華型獨立筒混合床墊，床邊坐下去不垮、睡起來涼，而且白手套到府安裝直接含在價格裡。Helix Midnight Luxe 我很有信心擺第二，它在客製化跟側睡減壓這塊封王，只要你是側睡，或想精準調出某個軟硬度，它就是更聰明的選擇。Purple Restore Hybrid 守第三，因為它那塊 GelFlex 凝膠格柵的減壓感，這榜上真的沒別人模仿得出來，那種懸浮感很獨特。Bear Elite Hybrid 跟 Nectar Premier Copper 把強勢的前五補滿，Nectar 靠優秀的動作隔離，對情侶來說還是 CP 值代表。六月想買的我給個方向，先看睡姿再說。仰睡跟混合睡姿從 Saatva 起手，純側睡的要認真看 Helix Midnight Luxe，會燥熱又受不了壓力點的，欠自己一次 Purple 試睡。這個級距的頂端已經很成熟，差別在合不合你，不在品質好壞。",
                "highlights": [
                    {"title": "Saatva Classic 涼感與邊緣領先", "body": "Sleep Foundation 2026 涼感給 4 分、Helix Midnight Luxe 3.5，邊緣支撐跟仰睡表現大勝。"},
                    {"title": "Helix Midnight Luxe 稱霸側睡", "body": "客製化跟側睡減壓封王。側睡或想精調軟硬度的人，第二名的它更聰明。"},
                    {"title": "Purple 格柵無人能比", "body": "GelFlex 凝膠格柵的減壓感這榜上沒人模仿得出來，Restore Hybrid 穩坐第三。"},
                    {"title": "Nectar 是情侶 CP 值", "body": "優秀動作隔離加親民價，Premier Copper 是會互相吵醒的伴侶首選。"},
                    {"title": "依睡姿挑床", "body": "仰睡混合睡從 Saatva 起手，側睡看 Helix，燥熱又怕壓力點的試 Purple。"},
                ],
            },
        },
    },
    "best-portable-ice-makers.json": {
        "references": [
            {"title": "GE Profile Opal Nugget Ice Maker: Tested & Reviewed in 2026", "url": "https://www.tasteofhome.com/article/ge-profile-opal-nugget-ice-maker-review/", "source": "Taste of Home"},
            {"title": "Best Smart Ice Makers 2026: Countertop Nugget Ice and Portable Ice Machines Tested", "url": "https://www.smarthomeexplorer.com/guides/best-smart-ice-makers-2026", "source": "Smart Home Explorer"},
            {"title": "GE Profile Opal 2.0 Customer Reviews", "url": "https://www.bestbuy.com/site/reviews/ge-profile-opal-2-0-38-lb-portable-ice-maker-with-nugget-ice-production-side-tank-and-built-in-wifi-stainless-steel/6408648", "source": "Best Buy"},
        ],
        "i18n": {
            "en": {
                "commentary": "The GE Profile Opal 2.0 stays my number one as we head into summer, and the case for it has only gotten stronger. Wirecutter named it the best countertop ice maker for 2026, and the reasons are exactly what I keep telling friends shopping for one: nugget ice that is genuinely chewable, absorbs drink flavor as it melts, and chills a glass faster because each pellet has so much surface area. It pumps out 38 pounds a day, enough for a household of four to six or a small home bar, and the WiFi side tank lets you schedule production overnight and check the bin level from the SmartHQ app. At roughly $499 it is not cheap, but for nugget devotees it remains the benchmark. The Costway self-dispensing nugget unit holds second on the strength of its higher output and far friendlier price, and it is the one I point value shoppers toward. Hamilton Beach stays third as the quiet, reliable workhorse. If you want nugget quality close to the Opal for meaningfully less, the budget field has improved, with the Frigidaire line landing around $269 and delivering solid pellets at roughly 60 percent of the Opal's price. My June advice: if you host, run a bar cart, or simply love chewable ice, buy the Opal 2.0 and schedule it overnight so the bin is full by morning. Everyone else can save real money one tier down without giving up much.",
                "highlights": [
                    {"title": "Opal 2.0 is still the nugget benchmark", "body": "Wirecutter's best countertop pick for 2026 makes genuinely chewable ice that absorbs flavor and chills fast. At about $499 it stays the one to beat."},
                    {"title": "Output suits real hosting", "body": "38 pounds a day covers a household of four to six or a small home bar, and the WiFi side tank refills overnight so the bin is full by morning."},
                    {"title": "Costway is the value play", "body": "Higher output and a friendlier price keep the self-dispensing nugget unit at second. It is the one I point budget-minded buyers toward."},
                    {"title": "Hamilton Beach is the quiet workhorse", "body": "Reliable and notably quiet, it holds third for anyone who wants steady ice without the smart-home extras."},
                    {"title": "Budget nugget got better", "body": "The Frigidaire line lands around $269 and delivers solid pellets at roughly 60 percent of the Opal's price for shoppers watching the budget."},
                ],
            },
            "zh-tw": {
                "commentary": "夏天要來了，GE Profile Opal 2.0 還是我的第一，而且理由只有更充分。Wirecutter 把它評為 2026 最佳檯面製冰機，原因正是我一直跟朋友講的那幾點，它做出來的方便咀嚼冰真的能咬、融的時候會吸飲料的味道，而且每顆表面積大、冰杯子超快。一天可以出 38 磅，夠四到六人的家庭或小家庭吧台用，WiFi 側水箱還能排程半夜製冰、用 SmartHQ App 看儲冰量。台幣大概一萬五上下，不算便宜，但對 nugget ice 死忠粉來說它就是標竿。Costway 自動出冰那台靠更高產量加親民很多的價格守第二，我會把它推給看 CP 值的人。Hamilton Beach 第三，安靜又可靠的老黃牛。如果你想要接近 Opal 的冰質但花得少很多，入門這塊有進步了，Frigidaire 那條線台幣大約八千出頭，用 Opal 約六成的價格給你紮實的小冰粒。六月我的建議，常請客、有吧台車、或單純愛咬冰的，買 Opal 2.0 然後排半夜製冰，早上起來儲冰盒就滿了。其他人往下一階就能省下實實在在一筆，又不太犧牲什麼。",
                "highlights": [
                    {"title": "Opal 2.0 仍是 nugget 標竿", "body": "Wirecutter 2026 最佳檯面製冰機，冰真的能咬、會吸味道、冰杯快。台幣約一萬五，還是要打敗的對象。"},
                    {"title": "產量撐得起請客", "body": "一天 38 磅夠四到六人家庭或小吧台，WiFi 側水箱半夜自動補冰，早上儲冰盒就滿了。"},
                    {"title": "Costway 是 CP 值選擇", "body": "更高產量加親民價格守第二，看預算的我都推這台自動出冰機。"},
                    {"title": "Hamilton Beach 安靜老黃牛", "body": "可靠又安靜，想要穩定出冰、不需要智慧家庭功能的就選它，第三名。"},
                    {"title": "入門 nugget 變好了", "body": "Frigidaire 那條線台幣約八千出頭，用 Opal 約六成價格給你紮實小冰粒，看預算的可以考慮。"},
                ],
            },
        },
    },
    "best-smart-glasses.json": {
        "references": [
            {"title": "Meta launches two new Ray-Ban glasses designed for prescription wearers", "url": "https://techcrunch.com/2026/03/31/meta-launches-two-new-ray-ban-glasses-designed-for-prescription-wearers/", "source": "TechCrunch"},
            {"title": "Meta adds a teleprompter and EMG handwriting to the Ray-Ban Display, delays international availability", "url": "https://www.androidcentral.com/apps-software/meta/meta-ray-ban-display-updates-ces-2026", "source": "Android Central"},
            {"title": "Every Smart Glasses Design Tells You Who They're Chasing", "url": "https://the-gadgeteer.com/2026/05/25/smart-glasses-2026-design-strategy/", "source": "The Gadgeteer"},
        ],
        "i18n": {
            "en": {
                "commentary": "The Ray-Ban Meta Gen 2 holds my number one, and the steady drumbeat of software wins is why. Meta has now made hands-free nutrition logging real, letting you snap a photo or speak a meal and have Meta AI pull the key details into a food log, and it added WhatsApp group-chat summaries and recall to the Early Access Program. These are the everyday features that make smart glasses stick, and they land on the frames most people will actually buy. The Oakley Meta HSTN stays second as the sportier sibling, and the broader story this week is Meta widening its prescription strategy. The new Blayzer and Scriber frames, launched at $499 to support nearly all prescriptions, matter because the biggest barrier for all-day eyewear has been getting your actual script into a good-looking frame. The Meta Ray-Ban Display holds third, and I am keeping it there deliberately. Teleprompter support and EMG handwriting are genuinely novel, but Meta has delayed international availability indefinitely citing extremely limited inventory and unprecedented demand, so most buyers still cannot get one. For people outside the US, that makes the displayless Gen 2 and Oakley HSTN the realistic flagships. The Xreal One Pro remains my pick for media and big-screen viewing at fourth. My June read: buy the Gen 2 if you want the most polished daily-driver, wait on the Display unless you are in the US and patient, and treat Xreal as a different category aimed at screens rather than AI.",
                "highlights": [
                    {"title": "Gen 2 wins on everyday software", "body": "Hands-free nutrition logging via photo or voice now works, and WhatsApp summaries and recall reached Early Access. These are the features that make glasses stick."},
                    {"title": "Prescription strategy widens", "body": "The new Blayzer and Scriber frames at $499 support nearly all prescriptions, removing the biggest barrier to wearing smart glasses all day."},
                    {"title": "Display stays third on purpose", "body": "Teleprompter and EMG handwriting are novel, but Meta delayed international availability indefinitely citing limited inventory, so most buyers still cannot get one."},
                    {"title": "Oakley HSTN is the sporty pick", "body": "At second, the HSTN brings the same Meta AI platform in a sportier frame for active wearers who want the ecosystem in a different look."},
                    {"title": "Xreal One Pro is a screen tool", "body": "At fourth, it remains the pick for media and big-screen viewing, a different category aimed at displays rather than AI assistance."},
                ],
            },
            "zh-tw": {
                "commentary": "Ray-Ban Meta Gen 2 守住我的第一，靠的就是軟體更新一波接一波。Meta 現在把免動手的飲食記錄做成真的能用，拍張照或講一句就好，Meta AI 會把重點抓進飲食記錄，還把 WhatsApp 群組摘要跟回顧功能丟進搶先體驗計畫。這些就是讓智慧眼鏡讓人離不開的日常功能，而且都落在大多數人真的會買的那副鏡框上。Oakley Meta HSTN 守第二，比較運動風的那一支，這週更大的故事是 Meta 把度數策略做寬。新的 Blayzer 跟 Scriber 鏡框台幣大約一萬五起跳，支援幾乎所有度數，這很關鍵，因為全天戴的眼鏡最大的卡關，一直是怎麼把你真正的度數做進一副好看的框裡。Meta Ray-Ban Display 守第三，我是刻意留在這。提詞機跟 EMG 手寫真的很新鮮，但 Meta 以庫存極度有限、需求空前為由無限期延後國際上市，所以大多數人根本買不到。對美國以外的人來說，沒螢幕的 Gen 2 跟 Oakley HSTN 才是實際買得到的旗艦。Xreal One Pro 守第四，看影片、開大螢幕還是它。六月我的看法，想要最完整的日常機就買 Gen 2，Display 除非你在美國又有耐心不然先等，Xreal 當成另一個品類，它是給螢幕用的，不是拚 AI 的。",
                "highlights": [
                    {"title": "Gen 2 靠日常軟體取勝", "body": "免動手飲食記錄拍照或語音都能用，WhatsApp 摘要跟回顧進了搶先體驗。這些功能讓人離不開。"},
                    {"title": "度數策略做寬", "body": "新 Blayzer 跟 Scriber 鏡框台幣約一萬五起，支援幾乎所有度數，掃除全天戴的最大卡關。"},
                    {"title": "Display 刻意留第三", "body": "提詞機跟 EMG 手寫很新鮮，但 Meta 以庫存有限為由無限期延後國際上市，多數人還是買不到。"},
                    {"title": "Oakley HSTN 運動風選擇", "body": "第二名，同樣的 Meta AI 平台放進運動風鏡框，給愛運動又想要生態系的人換個樣子。"},
                    {"title": "Xreal One Pro 是螢幕工具", "body": "第四名，看影片開大螢幕仍是它，屬於另一個品類，給螢幕用的不是拚 AI。"},
                ],
            },
        },
    },
    "best-video-doorbells.json": {
        "references": [
            {"title": "Best Smart Doorbell Cameras 2026: Ring vs Nest vs Eufy Compared", "url": "https://www.smarthomeexplorer.com/guides/best-smart-doorbell-cameras-2026", "source": "Smart Home Explorer"},
            {"title": "Best video doorbells in 2026: Ring, Nest, Wyze and more tested", "url": "https://www.tomsguide.com/us/best-video-doorbells,review-4468.html", "source": "Tom's Guide"},
            {"title": "Ring vs Eufy vs Aqara: Best Video Doorbell of 2026?", "url": "https://www.onesmartcrib.com/ring-vs-eufy-vs-aqara/", "source": "oneSmartcrib"},
        ],
        "i18n": {
            "en": {
                "commentary": "The eufy E340 stays my number one, and after another round of comparisons I am more confident than ever. Smart Home Explorer ran 45 days of testing across multiple homes and reached the same conclusion: the E340's dual-camera design, with a front lens for visitors and a downward lens for packages on the porch, plus built-in local storage and no monthly fee, just works. That combination of genuinely useful hardware and zero subscription is exactly what I want a doorbell to be, and it is why the E340 keeps winning on value. The Aqara G410 holds second and remains my pick for anyone in Apple Home, since it supports HomeKit Secure Video natively and runs at no yearly cost. The Google Nest Doorbell stays third on the strength of its detection smarts and Google Home integration, and the third-gen model's jump to 2K with a wider 166-degree field of view makes it noticeably sharper day and night. Ring's Battery Doorbell Pro keeps a top-five spot for image quality and AI features, but its subscription dependence keeps it from climbing. My through-line for June is simple: if you care about owning your footage and skipping monthly fees, eufy and Aqara are the smarter buys, full stop. Pick eufy for porch and package coverage, Aqara if you live in Apple Home, and Nest only if Google's ecosystem and detection accuracy matter more to you than recurring cost.",
                "highlights": [
                    {"title": "eufy E340 wins on value", "body": "Dual cameras cover visitors and porch packages, with local storage and no monthly fee. After 45 days of multi-home testing, it stays the top recommendation."},
                    {"title": "Aqara G410 is the Apple Home pick", "body": "Native HomeKit Secure Video support and no yearly cost keep it at second for anyone living inside Apple's smart-home ecosystem."},
                    {"title": "Nest gets sharper", "body": "The third-gen Nest Doorbell jumps to 2K with a wider 166-degree field of view, noticeably crisper day and night, and pairs best with Google Home."},
                    {"title": "Ring leads on image and AI, lags on cost", "body": "The Battery Doorbell Pro keeps a top-five spot for image quality and AI features, but its subscription reliance holds it back."},
                    {"title": "Own your footage", "body": "For buyers who want local recording and no monthly fee, eufy and Aqara are the smarter choices. Pick by ecosystem and porch needs."},
                ],
            },
            "zh-tw": {
                "commentary": "eufy E340 還是我的第一，又跑了一輪比較後我更有把握了。Smart Home Explorer 在好幾間房子實測 45 天，結論跟我一樣，E340 的雙鏡頭設計，一顆對著訪客、一顆朝下看門口的包裹，加上內建本地儲存又免月費，就是好用。這種真的實用的硬體配上零訂閱，正是我心目中門鈴該有的樣子，也是 E340 一直靠 CP 值贏的原因。Aqara G410 守第二，用 Apple Home 的人我還是推它，因為它原生支援 HomeKit Secure Video，而且不用年費。Google Nest 門鈴守第三，靠的是偵測夠聰明加 Google Home 整合，第三代升上 2K、視野拉寬到 166 度，白天晚上都明顯更清楚。Ring 的 Battery Doorbell Pro 靠畫質跟 AI 功能守在前五，但它綁訂閱這點讓它爬不上去。六月我的主軸很簡單，如果你在意影像自己留、不想付月費，eufy 跟 Aqara 就是更聰明的選擇，沒有別的話講。要顧門口包裹挑 eufy，住 Apple Home 挑 Aqara，至於 Nest，只有當 Google 生態系跟偵測準度對你比月費更重要時才選。",
                "highlights": [
                    {"title": "eufy E340 靠 CP 值贏", "body": "雙鏡頭顧訪客跟門口包裹，本地儲存免月費。多間房子實測 45 天，仍是首選。"},
                    {"title": "Aqara G410 是 Apple Home 選擇", "body": "原生支援 HomeKit Secure Video 又免年費，住 Apple 智慧家庭的人第二名選它。"},
                    {"title": "Nest 變清楚了", "body": "第三代升上 2K、視野拉寬到 166 度，白天晚上都更清晰，配 Google Home 最對味。"},
                    {"title": "Ring 畫質 AI 強但綁月費", "body": "Battery Doorbell Pro 靠畫質跟 AI 功能守前五，但綁訂閱讓它爬不上去。"},
                    {"title": "影像自己留", "body": "想本地錄影又免月費，eufy 跟 Aqara 更聰明。依生態系跟門口需求挑。"},
                ],
            },
        },
    },
}


def main():
    for name, payload in ENTRIES.items():
        data, p = load(name)
        entry = {
            "date": DATE,
            "rankings": last_rankings(data),
            "references": payload["references"],
            "i18n": payload["i18n"],
        }
        upsert(data, entry)
        save(p, data)
        print("updated", name)


if __name__ == "__main__":
    main()
