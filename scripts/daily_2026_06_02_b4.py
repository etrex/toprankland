"""2026-06-02 daily update — Batch 4: Home/Outdoor cleaning & climate (7 files)"""
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


def build_air_purifiers():
    d, p = load("best-air-purifiers.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Canada wildfire smoke reignites U.S. air quality concerns", "url": "https://www.accuweather.com/en/weather-forecasts/canada-wildfire-smoke-reignites-u-s-air-quality-concerns/1779212", "source": "AccuWeather"},
            {"title": "Best air purifiers for wildfire smoke", "url": "https://www.iqair.com/us/air-purifiers-for-wildfire-smoke", "source": "IQAir"},
            {"title": "Best Air Purifier for Wildfire Smoke (2026)", "url": "https://www.airpurifierreport.com/guides/best-air-purifier-wildfire-smoke", "source": "Air Purifier Report"},
        ],
        "i18n": {
            "en": {
                "commentary": "Wildfire smoke is the story this week, and it changes how you should think about buying an air purifier right now. Canadian wildfire smoke pushed air quality to unhealthy levels across North Dakota, Montana, Minnesota and South Dakota on June 1, and by June 3 parts of Michigan and Minnesota hit very unhealthy readings. Smoke even reached as far south as Florida. This is exactly the scenario where the IQAir HealthPro Plus at the top of our list earns its premium. It carries roughly 5 pounds of granular activated carbon, which is what actually removes the VOCs and odor that ride along with fine smoke particles, and its HyperHEPA filtration captures ultrafine particles down well below the standard HEPA threshold. During an active smoke event, that carbon mass is the difference between cleaner air and air that just smells slightly less smoky.\n\nThe Coway Airmega 400S at rank 2 remains the smartest large-room value in the category. With a smoke CADR around 350 CFM it clears a 400 square foot room at six air changes per hour, which is the rate you want during a smoke advisory, not the relaxed two changes most spec sheets quote. It is the purifier I recommend for open-concept living rooms and kitchens.\n\nThe Blueair HealthProtect 7470i at rank 3 holds its spot on the strength of its HEPASilent dual filtration, which lets it move a lot of air quietly, a real advantage when you run it overnight through a smoke event. The Rabbit Air MinusA3 at rank 4 stays appealing for its wall-mountable design and customizable filter, and the Coway Airmega ProX at rank 5 rounds out the list for very large spaces. With British Columbia facing the highest sustained fire risk this summer and smoke season just beginning, buying now means you are protected before the next plume arrives, not scrambling after it.",
                "highlights": [
                    {"title": "IQAir HealthPro Plus Is Built for Active Smoke Events", "body": "Its roughly 5 pounds of granular activated carbon and HyperHEPA filtration target the VOCs and ultrafine particles that define wildfire smoke. During the June 1 to 4 smoke event across the Upper Midwest, this carbon mass is what separates genuinely clean air from air that merely smells less smoky."},
                    {"title": "Coway Airmega 400S Clears Large Rooms Fast", "body": "A smoke CADR near 350 CFM delivers six air changes per hour in a 400 square foot room, the rate you actually want during a smoke advisory. It is the best large-room value for open living spaces and the purifier I recommend most for households on a budget."},
                    {"title": "Smoke Season Is Starting Early This Year", "body": "Canadian wildfire smoke already pushed Minnesota to very unhealthy air on June 3, and British Columbia faces the highest sustained fire risk through summer. Buying a purifier now means protection is in place before the next plume, not after."},
                ],
            },
            "zh-tw": {
                "commentary": "這週的重點是野火煙霾，而且它直接影響你現在該怎麼挑空氣清淨機。加拿大野火的煙在 6 月 1 日把北達科他、蒙大拿、明尼蘇達一帶的空氣品質推到不健康等級，6 月 3 日密西根和明尼蘇達部分地區甚至飆到非常不健康，煙甚至飄到南邊的佛羅里達。這種情境下，榜首的 IQAir HealthPro Plus 才真正體現它的價值。它配了大約 5 磅的顆粒活性碳，這個碳量才是真的能把跟著煙塵一起來的揮發性有機物和臭味抓掉的關鍵，HyperHEPA 濾網更能濾到遠低於一般 HEPA 標準的超細顆粒。煙害發生的當下，碳量的多寡就是「空氣真的乾淨」和「只是聞起來沒那麼嗆」的差別。\n\n第二名的 Coway Airmega 400S，依然是大坪數空間最聰明的選擇。它的煙塵 CADR 大約 350 CFM，能在約 11 坪的房間做到每小時六次換氣，這才是煙害警報時你需要的換氣速度，而不是規格表上輕鬆寫的兩次。開放式客廳、廚房連在一起的格局，我最推這台。\n\n第三名的 Blueair HealthProtect 7470i，靠 HEPASilent 雙重過濾撐住排名，風量大又安靜，煙害期間整晚開著也不吵，這點很實用。第四名的 Rabbit Air MinusA3 主打可壁掛設計和客製化濾網，第五名的 Coway Airmega ProX 則補上超大空間的需求。今年夏天卑詩省的火災風險最高也最持久，煙害季才剛開始，現在入手代表下一波煙來之前你已經有防護，而不是煙來了才手忙腳亂搶貨。",
                "highlights": [
                    {"title": "IQAir HealthPro Plus 為煙害當下而生", "body": "約 5 磅顆粒活性碳加上 HyperHEPA 濾網，專門對付野火煙霾裡的揮發性有機物和超細顆粒。6 月 1 到 4 日中西部上游的煙害事件中，這個碳量就是「空氣真乾淨」和「只是沒那麼嗆」的分水嶺。"},
                    {"title": "Coway Airmega 400S 大空間快速淨化", "body": "煙塵 CADR 接近 350 CFM，能在約 11 坪房間做到每小時六次換氣，這才是煙害警報時真正需要的速度。開放式空間最佳性價比之選，預算有限的家庭我也最推這台。"},
                    {"title": "煙害季今年提早報到", "body": "加拿大野火煙已在 6 月 3 日把明尼蘇達空氣推到非常不健康，卑詩省整個夏天面臨最高且最持久的火災風險。現在入手代表下一波煙來前防護就位，不是事後才補救。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK air-purifiers")


def build_portable_air_conditioners():
    d, p = load("best-portable-air-conditioners.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Summer forecast 2026: Heat, severe storms to shape the season as El Nino develops", "url": "https://www.accuweather.com/en/weather-forecasts/summer-forecast-2026-heat-severe-storms-to-shape-the-season-as-el-ni%C3%B1o-develops-strengthens/1884851", "source": "AccuWeather"},
            {"title": "Midea Duo Smart Inverter MAP12S1TBL Review | Tested", "url": "https://www.techgearlab.com/reviews/electronics/portable-air-conditioner/midea-duo-smart-inverter-map12s1tbl", "source": "TechGearLab"},
            {"title": "Midea Duo Review | Test Results", "url": "https://www.consumeranalysis.com/guides/portable-ac/midea-duo-review/", "source": "Consumer Analysis"},
        ],
        "i18n": {
            "en": {
                "commentary": "A hot summer is forecast across nearly the entire contiguous United States in 2026, with almost no region expected to land below its historical average. That is the backdrop for buying a portable air conditioner right now, and it is why the Midea Duo holds the top spot with conviction. Its patented hose-in-hose design functions as a true dual-hose system in a single condensed unit, which solves the negative-pressure problem that makes most single-hose portables waste their cooling. The practical result is that the Duo cools faster and holds temperature in genuinely challenging high-heat, high-humidity rooms. It runs on R-32 refrigerant with inverter technology that cuts energy use over 40 percent against the federal standard, and it drops to a near-silent 42 dB on its lowest setting, which matters when it is running through a heat advisory overnight.\n\nThe Whynter NEX ARC-1230WN at rank 2 covers rooms up to 600 square feet with 12,000 BTU SACC and earned best-of recognition from both Forbes and U.S. News last year. It is the pick for larger spaces where the Duo's coverage runs thin. The LG LP1419IVSM at rank 3 brings LG's dual-inverter quiet operation and reliable smart controls, a strong choice for bedrooms where noise is the priority.\n\nThe Hisense HAP0824TWD at rank 4 and the Whynter Elite ARC-122DS at rank 5 round out the list as solid value options for medium rooms. With energy demand and electric bills set to climb under this summer's heat, the inverter efficiency that the Duo and the LG deliver is no longer a luxury feature, it is what keeps your cooling costs from spiraling. If your space runs hot and humid, the Midea Duo is the unit I would put my money on before the peak of the season arrives.",
                "highlights": [
                    {"title": "Midea Duo Solves the Single-Hose Efficiency Problem", "body": "Its hose-in-hose design works as a true dual-hose system, eliminating the negative pressure that wastes cooling in ordinary portables. The result is faster cooling and steady temperatures in high-heat, high-humidity rooms, backed by R-32 inverter efficiency over 40 percent better than the federal standard."},
                    {"title": "A Hot Summer Forecast Raises the Stakes", "body": "Nearly every region of the contiguous US is forecast above its historical average this summer, driving up energy demand and electric bills. The Duo's inverter efficiency and 42 dB quiet floor make it the unit that cools hard without spiking your power bill."},
                    {"title": "Whynter ARC-1230WN Owns the Large-Room Tier", "body": "With 12,000 BTU SACC and coverage up to 600 square feet, the Whynter NEX is the pick for spaces where the Midea Duo runs thin. Forbes and U.S. News both named it a best portable AC last year, and it remains the large-room workhorse."},
                ],
            },
            "zh-tw": {
                "commentary": "2026 年幾乎整個美國本土都預測會是個酷暑，幾乎沒有地區會低於歷史平均溫度。這就是你現在該買移動式冷氣的大背景，也是 Midea Duo 穩坐榜首的理由。它專利的「管中管」設計，用一個整合機身做到真正的雙軟管系統，解決了大多數單軟管移動式冷氣那個讓冷氣白白浪費掉的負壓問題。實際的好處就是，Duo 降溫更快，在又熱又濕的硬底子房間裡也能穩住溫度。它用 R-32 冷媒搭配變頻技術，比聯邦標準省電超過 40%，最低段運轉只有接近無聲的 42 分貝，高溫警報的夜裡整晚開著也不吵，這點很重要。\n\n第二名的 Whynter NEX ARC-1230WN，12,000 BTU SACC 可覆蓋約 17 坪空間，去年同時拿下 Forbes 和 U.S. News 的最佳推薦。空間比較大、Duo 覆蓋吃力的時候，就選這台。第三名的 LG LP1419IVSM 帶來 LG 的雙變頻靜音和穩定的智慧控制，臥室裡最在意噪音的人很適合。\n\n第四名的 Hisense HAP0824TWD 和第五名的 Whynter Elite ARC-122DS 補上中型空間的高性價比選項。今年夏天用電需求和電費都會往上爬，Duo 和 LG 的變頻效率正好幫你把電費守住，這已經是夏天選機的必備條件。如果你家又熱又濕，旺季高峰來之前，我會直接押 Midea Duo。",
                "highlights": [
                    {"title": "Midea Duo 解決單軟管的效率痛點", "body": "管中管設計做到真正的雙軟管系統，消除了一般移動式冷氣浪費冷氣的負壓問題。又熱又濕的房間降溫更快、溫度更穩，搭配 R-32 變頻比聯邦標準省電超過 40%。"},
                    {"title": "酷暑預測讓選機更關鍵", "body": "今年夏天美國本土幾乎每個地區都預測高於歷史均溫，用電需求和電費跟著上升。Duo 的變頻效率加上 42 分貝靜音底線，讓它降溫夠猛又不會把電費衝爆。"},
                    {"title": "Whynter ARC-1230WN 稱霸大空間級距", "body": "12,000 BTU SACC、覆蓋達約 17 坪，是 Midea Duo 覆蓋吃力時的最佳選擇。去年 Forbes 和 U.S. News 都把它列為最佳移動式冷氣，大空間的主力機種。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK portable-air-conditioners")


def build_cordless_vacuums():
    d, p = load("best-cordless-vacuums.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Shark PowerDetect Cordless vs Dyson Gen5detect: which is better?", "url": "https://www.techradar.com/home/vacuums/dyson-gen5detect-vs-shark-powerdetect-cordless-vacuum", "source": "TechRadar"},
            {"title": "The 5 Best Cordless Vacuums of 2026", "url": "https://www.rtings.com/vacuum/reviews/best/cordless", "source": "RTINGS"},
            {"title": "Top 10 Best Cordless Vacuums of 2026", "url": "https://vacuumwars.com/vacuum-wars-best-cordless-vacuums/", "source": "Vacuum Wars"},
        ],
        "i18n": {
            "en": {
                "commentary": "The cordless vacuum race in 2026 comes down to a clear question: do you want the best value or the most raw power? The Shark PowerDetect holds our top spot because it answers that question for the most people. It pairs a redesigned DuoClean floorhead with class-leading suction, a flexible MultiFLEX wand, and a self-emptying dock that genuinely cuts down on the chore of maintenance. In direct head-to-head testing, the PowerDetect actually pulled pet hair through high-pile carpet faster than the Dyson Gen5detect, and it does that at a price hundreds of dollars below the flagship. Add the removable battery delivering up to 40 minutes of runtime and you have the vacuum I recommend to most households without hesitation.\n\nThe Dyson Gen5detect at rank 2 remains the performance benchmark, and it earned best-performance and best-battery-life honors in 2025 testing for good reason. Its fifth-generation Hyperdymium motor, onboard particle sensor, and green-laser Fluffy Optic head that reveals hidden dust in real time give it the edge on low-pile carpet and hard floors. If outright cleaning power on hard surfaces is your priority and budget is not the constraint, this is the one.\n\nThe Dyson V15 Detect at rank 3 stays relevant as the more accessible Dyson with the same laser dust-detection party trick. The Tineco Pure One A90S at rank 4 brings smart iLoop sensing at a friendlier price, and the Samsung Bespoke Jet AI at rank 5 rounds out the list with its all-in-one Clean Station and slick design. The takeaway heading into summer is simple: the Shark PowerDetect gives you flagship-tier cleaning where it counts at a mid-tier price, which is why it sits at number one.",
                "highlights": [
                    {"title": "Shark PowerDetect Beats Flagships on Value", "body": "It pulls pet hair through high-pile carpet faster than the Dyson Gen5detect in head-to-head testing, pairs a DuoClean floorhead with a self-emptying dock, and does it for hundreds less than flagship rivals. For most households, it is the clearest recommendation in the category."},
                    {"title": "Dyson Gen5detect Sets the Power Benchmark", "body": "Its fifth-generation Hyperdymium motor, onboard particle sensor, and green-laser Fluffy Optic head took best-performance and best-battery honors in 2025 testing. For maximum cleaning power on hard floors and low-pile carpet, nothing else matches it."},
                    {"title": "Removable Batteries Define the Top Tier", "body": "Both the PowerDetect with up to 40 minutes of runtime and the Gen5detect offer swappable batteries, the feature that turns a cordless vacuum into a whole-home tool rather than a one-room sprint. It is now the dividing line between flagship and budget models."},
                ],
            },
            "zh-tw": {
                "commentary": "2026 年無線吸塵器的競爭，說穿了就是一個選擇：你要最高性價比，還是最猛的純吸力。Shark PowerDetect 穩坐榜首，因為它替最多人回答了這個問題。它把重新設計的 DuoClean 吸頭、class-leading 吸力、可彎折的 MultiFLEX 軟管，加上一個真的能省下倒垃圾麻煩的自動集塵座結合在一起。在直接對決測試裡，PowerDetect 在長毛地毯上把寵物毛吸起來的速度，其實比 Dyson Gen5detect 還快，而且價格便宜了好幾百美元。再加上可拆換電池、續航最長 40 分鐘，這就是我會毫不猶豫推給大多數家庭的那一台。\n\n第二名的 Dyson Gen5detect 仍然是性能標竿，2025 年測試拿下最佳性能和最佳續航是有道理的。它的第五代 Hyperdymium 馬達、機身內建顆粒感測器，還有那顆綠雷射 Fluffy Optic 吸頭能即時照出隱形灰塵，在短毛地毯和硬地板上佔優勢。如果你最在意硬地板的純清潔力、預算又不是問題，就選這台。\n\n第三名的 Dyson V15 Detect 依然有戲，是價格比較親民、又保留同樣雷射偵塵看家本領的 Dyson。第四名的 Tineco Pure One A90S 用更友善的價格帶來智慧 iLoop 感測，第五名的 Samsung Bespoke Jet AI 靠全合一 Clean Station 和漂亮設計補上榜尾。夏天的結論很簡單：Shark PowerDetect 用中階價格給你旗艦級的清潔力，這就是它排第一的原因。",
                "highlights": [
                    {"title": "Shark PowerDetect 性價比擊敗旗艦", "body": "對決測試中，它在長毛地毯吸寵物毛的速度比 Dyson Gen5detect 還快，DuoClean 吸頭搭配自動集塵座，價格卻便宜旗艦好幾百美元。對大多數家庭來說，這是品類裡最明確的推薦。"},
                    {"title": "Dyson Gen5detect 立下吸力標竿", "body": "第五代 Hyperdymium 馬達、機身顆粒感測器、綠雷射 Fluffy Optic 吸頭，2025 年測試拿下最佳性能與最佳續航。硬地板和短毛地毯要最強清潔力，沒有對手。"},
                    {"title": "可拆換電池是頂規分水嶺", "body": "PowerDetect 續航最長 40 分鐘、Gen5detect 同樣支援可換電池，這個功能讓無線吸塵器從只能掃一間房，變成能打掃全家的工具，如今已是旗艦與平價機種的分界線。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK cordless-vacuums")


def build_robot_vacuums():
    d, p = load("best-robot-vacuums.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Roborock Saros 20 vs Dreame X60 Max Ultra: Which 2026 Flagship Wins?", "url": "https://www.bestrobovacuums.com/comparisons/roborock-saros-20-vs-dreame-x60-max-ultra", "source": "Best Robot Vacuums"},
            {"title": "Best (May 2026) Robot Vacuums", "url": "https://vacuumwars.com/best-may-2026-robot-vacuums/", "source": "Vacuum Wars"},
            {"title": "Best Robot Vacuum Cleaners This Summer 2026", "url": "https://the-gadgeteer.com/2026/05/06/best-robot-vacuums-summer-2026/", "source": "The Gadgeteer"},
        ],
        "i18n": {
            "en": {
                "commentary": "The Dreame X60 Max Ultra holds our top spot, and the latest testing confirms why it keeps winning the all-around title. Vacuum Wars currently rates it the best overall robot vacuum for the season, and it earns that by cleaning better than anything else in the field. In their lab it posted an 89 percent carpet deep-clean score and a rare 100 percent in flattened pet-hair pickup, which is the result that separates a great robovac from a merely good one. The hardware backs it up: a slim 3.13-inch retractable-LiDAR profile, 51 mm threshold climbing, 35,000 Pa of suction, and the HyperStream Duo Divide anti-tangle brush that keeps long hair from binding up the roller. Despite a wave of new releases from Dyson and Shark, the X60 stays the most consistent performer tested.\n\nThe Roborock Saros 20 at rank 2 is the one to watch if your home has obstacles the rest of the field cannot handle. Its AdaptiLift Chassis 3.0 crosses double-layer thresholds up to 3.46 inches, which covers raised bathroom tiles, thick transition strips, and even small steps between rooms. The honest summary is that the Dreame cleans better while the Roborock navigates better, and at current pricing the X60 delivers more cleaning performance per dollar.\n\nThe Dreame L50 Ultra at rank 3 brings flagship features down to a more reachable price, the Roborock Saros Z70 at rank 4 carries the mechanical arm that picks up small clutter, and the Roborock Qrevo CurvX at rank 5 rounds out the list with strong mopping. For most homes heading into summer, the X60 Max Ultra remains the safest pick, it simply cleans floors and carpet better than the competition.",
                "highlights": [
                    {"title": "Dreame X60 Max Ultra Wins on Cleaning Performance", "body": "It posted an 89 percent carpet deep-clean score and a perfect 100 percent in flattened pet-hair pickup in Vacuum Wars testing, the best all-around results in the field. With 35,000 Pa suction and the HyperStream Duo Divide anti-tangle brush, it stays the most consistent performer despite new Dyson and Shark releases."},
                    {"title": "Roborock Saros 20 Crosses Thresholds Nothing Else Can", "body": "Its AdaptiLift Chassis 3.0 climbs double-layer thresholds up to 3.46 inches, clearing raised bathroom tiles, thick transition strips, and small steps between rooms. If navigation through a complex floor plan is your main obstacle, it is the bot to buy."},
                    {"title": "X60 Delivers More Cleaning Per Dollar", "body": "At current pricing the Dreame X60 Max Ultra offers more cleaning performance per dollar than the Roborock Saros 20. The honest split is simple: the Dreame cleans better, the Roborock navigates better, and most homes are better served by cleaning."},
                ],
            },
            "zh-tw": {
                "commentary": "Dreame X60 Max Ultra 穩坐我們的榜首，最新測試也再次證明它為什麼能一直拿下全能冠軍。Vacuum Wars 目前把它評為本季最佳全能掃地機器人，靠的就是它比場上任何對手都掃得乾淨。在他們的實驗室裡，它拿下 89% 的地毯深層清潔分數，還有罕見的 100% 壓平寵物毛拾取率，這個成績就是把頂級掃地機和「還不錯」拉開差距的關鍵。硬體也撐得起來：3.13 吋的可伸縮 LiDAR 薄身、51mm 越障能力、35,000 Pa 吸力，加上 HyperStream Duo Divide 防纏繞滾刷，長頭髮不會把滾筒卡死。即使 Dyson 和 Shark 推了一波新機，X60 仍然是測過最穩定的那台。\n\n第二名的 Roborock Saros 20，如果你家有那些別人過不去的障礙，它就是該關注的對象。它的 AdaptiLift Chassis 3.0 能跨越最高 3.46 吋的雙層門檻，浴室墊高磁磚、厚的過門條、甚至房間之間的小台階都能搞定。老實說就是：Dreame 掃得比較乾淨，Roborock 走位比較強，而以目前定價，X60 每塊錢買到的清潔力更多。\n\n第三名的 Dreame L50 Ultra 把旗艦功能下放到更好入手的價位，第四名的 Roborock Saros Z70 帶著能撿小雜物的機械手臂，第五名的 Roborock Qrevo CurvX 靠強悍拖地補上榜尾。夏天對大多數家庭來說，X60 Max Ultra 仍然是最穩的選擇，它就是把地板和地毯掃得比對手乾淨。",
                "highlights": [
                    {"title": "Dreame X60 Max Ultra 清潔力封王", "body": "Vacuum Wars 測試中拿下 89% 地毯深層清潔分數、100% 壓平寵物毛拾取率，是場上最佳全能成績。35,000 Pa 吸力加上 HyperStream Duo Divide 防纏繞滾刷，即使 Dyson、Shark 推新機，它仍是最穩定的那台。"},
                    {"title": "Roborock Saros 20 越障能力無人能及", "body": "AdaptiLift Chassis 3.0 能跨越最高 3.46 吋的雙層門檻，墊高浴室磁磚、厚過門條、房間小台階都不是問題。如果你家複雜格局的走位是主要難題，就選這台。"},
                    {"title": "X60 每塊錢買到更多清潔力", "body": "以目前定價，Dreame X60 Max Ultra 每塊錢買到的清潔力勝過 Roborock Saros 20。老實說就是 Dreame 掃得乾淨、Roborock 走位強，而多數家庭更需要的是把地掃乾淨。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK robot-vacuums")


def build_robotic_pool_cleaners():
    d, p = load("best-robotic-pool-cleaners.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Beatbot AquaSense X Review: The AstroRinse Station Is a Breakthrough", "url": "https://the-gadgeteer.com/2026/04/13/beatbot-aquasense-x-review-the-astrorinse-station-is-a-breakthrough-in-pool-cleaning/", "source": "The Gadgeteer"},
            {"title": "The Best Robotic Pool Cleaners for 2026, Tested and Reviewed", "url": "https://www.poolbots.com/best-robotic-pool-cleaners", "source": "Poolbots"},
            {"title": "Robotic Pool Cleaner Reviews | 32+ Tested (2026)", "url": "https://www.thepoolnerd.com/robotic-pool-cleaner-reviews", "source": "The Pool Nerd"},
        ],
        "i18n": {
            "en": {
                "commentary": "Pool season is here, and with a hot summer forecast across most of the country, the pool is about to get a lot of use. That makes now the moment to lock in a robotic cleaner so you spend the season swimming, not skimming. The Dolphin Premier holds our top spot, and the reasoning is durability and proven results. After 32-plus head-to-head tests, independent reviewers and USA Today both name the Premier the best robotic pool cleaner for 2026. Its triple commercial-grade motors, swappable filtration media, and reliable navigation mean it cleans floor, walls, and waterline without drama, season after season. For an in-ground pool owner who wants one cleaner that simply works for years, this is the safe and smart buy.\n\nThe Beatbot AquaSense 2 Ultra at rank 2 is the AI-forward flagship for owners who want the cutting edge. Beatbot's newer AquaSense X, a CES 2026 Innovation Award honoree, raises the bar even further with its AstroRinse station, the first fully automatic filter-cleaning system that rinses the filter, empties the debris tank, and recharges the robot in about three minutes. That technology trajectory is exactly why Beatbot keeps its premium position in our rankings.\n\nThe Dolphin Nautilus CC Plus WiFi at rank 3 stays the value champion, delivering CleverClean smart scanning and dual scrubbing brushes at a price that makes robotic cleaning accessible. The Aiper Scuba S1 at rank 4 leads the cordless category for above-ground and smaller pools, and the Beatbot AquaSense 2 Pro at rank 5 rounds out the list with strong surface skimming. Heading into the heart of pool season, the Dolphin Premier remains the cleaner I trust to handle a full summer of daily swimming.",
                "highlights": [
                    {"title": "Dolphin Premier Is the Proven Season-Long Workhorse", "body": "Named best robotic pool cleaner for 2026 by USA Today and ranked first after 32-plus head-to-head tests, the Premier pairs triple commercial-grade motors with swappable filtration and reliable navigation. For an in-ground pool you swim all summer, it is the durable, no-drama choice."},
                    {"title": "Beatbot AquaSense X Brings Hands-Free Maintenance", "body": "The CES 2026 Innovation Award honoree introduced the AstroRinse station, the first fully automatic filter-cleaning system, which rinses the filter, empties the bin, and recharges the robot in about three minutes. That trajectory keeps Beatbot's flagship at the premium tier of our rankings."},
                    {"title": "Pool Season Plus a Hot Summer Means Buy Now", "body": "With a hot summer forecast nearly nationwide, pools will see heavy use this year. Locking in a robotic cleaner now means you spend the season swimming instead of skimming, and the Dolphin Nautilus CC Plus makes that affordable for value buyers."},
                ],
            },
            "zh-tw": {
                "commentary": "泳池季到了，加上今年全國大多地區都預測是酷暑，泳池接下來會被用得很兇。這代表現在就是把泳池機器人定下來的時機，讓你整季都在游泳，而不是在撈葉子。Dolphin Premier 穩坐我們的榜首，理由是耐用度和經過驗證的成績。經過 32 次以上的對決測試，獨立評測者和 USA Today 都把 Premier 評為 2026 年最佳泳池機器人。它三顆商業級馬達、可更換的濾材、加上可靠的導航，意味著它能年復一年把池底、池壁、水線都清乾淨，不出狀況。對地下式泳池的屋主來說，想要一台用很多年都好用的清潔機，這就是又安全又聰明的選擇。\n\n第二名的 Beatbot AquaSense 2 Ultra，是給想要最前沿科技的人準備的 AI 旗艦。Beatbot 更新的 AquaSense X 拿下 CES 2026 創新獎，它的 AstroRinse 基座把標準又拉高，這是第一個全自動濾網清潔系統，大約三分鐘就能沖洗濾網、倒掉集塵、再幫機器人充電。正是這個技術走向，讓 Beatbot 持續穩居我們榜單的高階位置。\n\n第三名的 Dolphin Nautilus CC Plus WiFi 依然是性價比冠軍，CleverClean 智慧掃描加上雙刷頭，用親民價格讓泳池機器人變得人人買得起。第四名的 Aiper Scuba S1 主打無線，適合地上式和小型泳池，第五名的 Beatbot AquaSense 2 Pro 靠出色的水面撈污補上榜尾。泳池季正熱，Dolphin Premier 仍然是我信得過、能撐過一整個夏天天天游泳的那台。",
                "highlights": [
                    {"title": "Dolphin Premier 是驗證過的整季主力", "body": "被 USA Today 評為 2026 年最佳泳池機器人，32 次以上對決測試排名第一。三顆商業級馬達搭配可換濾材和可靠導航，地下式泳池整個夏天天天游，它就是耐用又不出包的選擇。"},
                    {"title": "Beatbot AquaSense X 帶來免手動保養", "body": "這台 CES 2026 創新獎得主推出 AstroRinse 基座，是第一個全自動濾網清潔系統，約三分鐘就能沖洗濾網、倒集塵、再充電。這個技術走向讓 Beatbot 旗艦穩居榜單高階位置。"},
                    {"title": "泳池季加酷暑就是現在入手的理由", "body": "今年全國大多地區預測酷暑，泳池使用率會很高。現在把泳池機器人定下來，整季都在游泳而不是撈污，Dolphin Nautilus CC Plus 更讓預算型買家負擔得起。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK robotic-pool-cleaners")


def build_robot_lawn_mowers():
    d, p = load("best-robot-lawn-mowers.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Mammotion LUBA 3 AWD 3000 robot lawn mower review", "url": "https://www.techradar.com/home/small-appliances/mammotion-luba-3-awd-3000-review", "source": "TechRadar"},
            {"title": "Best Robot Lawn Mower 2026 (Tested & Reviewed for U.S. Lawns)", "url": "https://us.mammotion.com/blogs/news/best-robot-lawn-mower-2026", "source": "Mammotion"},
            {"title": "9 Best Robot Lawn Mowers of 2026 - Reviewed", "url": "https://www.reviewed.com/home-outdoors/best-right-now/best-robot-lawn-mowers", "source": "Reviewed"},
        ],
        "i18n": {
            "en": {
                "commentary": "Mowing season is in full swing, and the Mammotion Luba 3 AWD 5000 holds our top spot because it strikes the best balance of precision navigation, terrain adaptability, and total automation for the mid-to-large U.S. lawns most buyers actually have. Its Tri-Fusion system combines LiDAR, RTK, and AI vision so it maps and follows your yard without burying boundary wire, and the all-wheel-drive system gives it real traction on slopes up to 80 percent, which is the difference between a mower that handles a hilly yard and one that gets stuck on it. Dual cutting discs driven by 165W motors deliver a 400mm cutting width that chews through a full lawn faster than single-blade designs. It is also the only robot mower to win the SEAL Sustainable Product Award 2026, a credential that reflects genuine engineering, not marketing.\n\nThe Ecovacs Goat A3000 LiDAR Pro at rank 2 and the standard A3000 LiDAR at rank 3 are the picks for owners who prize precision and automated edge trimming. The LiDAR Pro series uses AI-guided trimming-string technology to mow right up to the edge, a real step toward eliminating the manual edging that every robot mower owner used to dread.\n\nThe Ecovacs Goat A2000 LiDAR Pro at rank 4 brings that same wire-free precision to smaller yards at a friendlier price, and the Navimow X315 at rank 5 rounds out the list with reliable RTK navigation. With summer here and grass growing fast, the value of a robot mower is at its peak right now, every week it runs is a week you are not pushing a mower in the heat. For larger and more complex properties, the Luba 3 AWD 5000 is the one I would buy.",
                "highlights": [
                    {"title": "Mammotion Luba 3 AWD 5000 Conquers Difficult Terrain", "body": "Its Tri-Fusion navigation pairs LiDAR, RTK, and AI vision while all-wheel drive grips slopes up to 80 percent, and dual 165W motors deliver a 400mm cutting width. As the only robot mower to win the SEAL Sustainable Product Award 2026, it is the clear pick for mid-to-large and hilly lawns."},
                    {"title": "Ecovacs Goat LiDAR Pro Automates Edge Trimming", "body": "The A3000 LiDAR Pro series uses AI-guided trimming-string technology to mow right up to the lawn's edge, a genuine step toward eliminating the manual edging robot mowers historically left behind. For precision-focused owners, it is the standout."},
                    {"title": "Peak Mowing Season Makes the Value Obvious", "body": "With summer here and grass growing fast, every week a robot mower runs is a week you skip pushing a mower in the heat. The wire-free setup of the Ecovacs Goat line and the all-terrain Luba 3 both pay back the investment fastest right now."},
                ],
            },
            "zh-tw": {
                "commentary": "割草季正旺，Mammotion Luba 3 AWD 5000 穩坐我們的榜首，因為它在精準導航、地形適應力、完全自動化之間取得最好的平衡，正好對應大多數買家真正擁有的中到大型草坪。它的 Tri-Fusion 系統結合 LiDAR、RTK 和 AI 視覺，不用埋邊界線就能把你的院子畫圖、跟著走，而四輪驅動讓它在最高 80% 的斜坡上有真正的抓地力，這就是「能搞定坡地草坪」和「卡在坡上動不了」的差別。雙切割盤由 165W 馬達驅動，400mm 切割寬度，把整片草坪割完的速度比單刀設計快。它還是唯一拿下 SEAL Sustainable Product Award 2026 的機器割草機，這個認證反映的是真功夫，不是行銷。\n\n第二名的 Ecovacs Goat A3000 LiDAR Pro 和第三名的標準版 A3000 LiDAR，是給重視精準和自動修邊的人。LiDAR Pro 系列用 AI 導引的修邊線技術，能一路割到草坪邊緣，這是朝「省掉手動修邊」邁出的實在一步，每個機器割草機用戶以前都很怕手動修邊。\n\n第四名的 Ecovacs Goat A2000 LiDAR Pro 用更友善的價格，把同樣的免線精準帶到小院子，第五名的 Navimow X315 靠可靠的 RTK 導航補上榜尾。夏天到了草長得快，機器割草機的價值現在正處於高峰，它每跑一週，就是你少在大熱天推一週的割草機。對較大、較複雜的庭園來說，Luba 3 AWD 5000 就是我會買的那台。",
                "highlights": [
                    {"title": "Mammotion Luba 3 AWD 5000 征服難搞地形", "body": "Tri-Fusion 導航結合 LiDAR、RTK 和 AI 視覺，四輪驅動爬最高 80% 斜坡，雙 165W 馬達帶來 400mm 切割寬度。身為唯一拿下 SEAL Sustainable Product Award 2026 的機器割草機，中大型和坡地草坪的明確首選。"},
                    {"title": "Ecovacs Goat LiDAR Pro 自動修邊", "body": "A3000 LiDAR Pro 系列用 AI 導引修邊線技術，能一路割到草坪邊緣，朝著省掉手動修邊邁出實在一步。對重視精準的屋主來說，它是最突出的選擇。"},
                    {"title": "割草旺季讓價值一目了然", "body": "夏天到了草長得快，機器割草機每跑一週，就是你少在大熱天推一週草機。Ecovacs Goat 系列的免線安裝和 Luba 3 的全地形能力，現在回本最快。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK robot-lawn-mowers")


def build_smart_pet_feeders():
    d, p = load("best-smart-pet-feeders.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Best Smart Pet Feeders and Cameras 2026", "url": "https://www.smarthomeexplorer.com/guides/best-automated-smart-pet-feeders-cameras-2026", "source": "Smart Home Explorer"},
            {"title": "Granary Automatic Cat Feeder with Camera | PETLIBRO", "url": "https://petlibro.com/products/petlibro-granary-automatic-pet-feeder-with-camera", "source": "Petlibro"},
            {"title": "Petlibro Granary Automatic Pet Feeder with Camera Review", "url": "https://cats.com/petlibro-granary-automatic-feeder-with-camera-review", "source": "Cats.com"},
        ],
        "i18n": {
            "en": {
                "commentary": "A smart pet feeder lives or dies on one thing: does it feed when it is supposed to, every single time? The Petlibro Granary Camera holds our top spot because it answers that question better than anything else, and it is exactly the reassurance you want with summer travel season arriving and more households leaving pets home for weekend trips. PCMag and Wirecutter both named it a best automatic pet feeder for the same reason we do, reliability. Its twin-turbine motor is documented by PCMag as four times more jam-resistant than the single-auger designs that cause the top failure mode in verified reviews, so the food actually drops. Around that core it layers the features that matter: a 1080P camera with a 145-degree wide-angle lens and IR night vision so you can watch your pet eat, two-way audio to comfort them with your voice, scheduling for up to 10 meals a day, and instant app alerts for low food, low battery, and jams. The sealed hopper keeps kibble fresh and the stainless steel bowl resists bacteria.\n\nThe Petkit Yumshare Dual-Hopper 2 at rank 2 is the pick for multi-pet or mixed-diet homes, with two separate hoppers and a camera in one unit. The Petlibro Polar Wet Food feeder at rank 3 solves the hardest problem in the category, keeping wet food fresh with thermoelectric cooling, which makes it the standout for cats on a wet diet.\n\nThe Wopet Heritage View Dual-Bowl at rank 4 brings camera monitoring and a two-bowl design at a friendly price, and the Petlibro One RFID at rank 5 rounds out the list with RFID tags that stop one pet from eating another's portion. Heading into summer travel, the Granary Camera is the feeder I trust to keep a pet fed and visible while you are away.",
                "highlights": [
                    {"title": "Petlibro Granary Camera Wins on Reliability", "body": "Its twin-turbine motor is documented by PCMag as four times more jam-resistant than single-auger designs, the top failure mode in verified reviews. Named a best automatic feeder by PCMag and Wirecutter, it feeds when it is supposed to, which is the entire job."},
                    {"title": "Camera and Two-Way Audio Keep You Connected", "body": "A 1080P camera with a 145-degree lens and IR night vision lets you watch your pet eat, while two-way audio comforts them with your voice. With summer travel here, that remote visibility is the feature that turns a feeder into peace of mind."},
                    {"title": "Petlibro Polar Solves the Wet-Food Problem", "body": "Its thermoelectric cooling keeps wet food fresh on a schedule, the hardest challenge in this category. For cats on a wet diet, the Polar is the standout that lets you automate feeding without sacrificing the food they actually need."},
                ],
            },
            "zh-tw": {
                "commentary": "智慧餵食器成敗只看一件事：它有沒有每一次都準時把飯給出來？Petlibro Granary Camera 穩坐我們的榜首，因為它把這個問題回答得比誰都好，而這正是暑假出遊季到來、越來越多家庭週末把寵物留在家時，你最想要的那份安心。PCMag 和 Wirecutter 都把它選為最佳自動餵食器，理由跟我們一樣，就是可靠。它的雙渦輪馬達被 PCMag 記錄為比單螺桿設計防卡四倍，而單螺桿正是驗證評論裡最常見的故障模式，所以這台是真的會把飯掉下來。圍繞這個核心，它疊上真正重要的功能：1080P 鏡頭搭配 145 度廣角和紅外線夜視，讓你看著寵物吃飯，雙向語音能用你的聲音安撫牠，可排程一天最多 10 餐，還有缺糧、低電量、卡糧的即時 App 通知。密封糧倉讓飼料保持新鮮，不鏽鋼碗則抗菌。\n\n第二名的 Petkit Yumshare 雙糧倉 2，是多寵物或混合飲食家庭的選擇，一台機器有兩個獨立糧倉加鏡頭。第三名的 Petlibro Polar 濕食餵食器，解決了這個品類最難的問題，用半導體製冷讓濕食保鮮，是吃濕食貓咪的最佳選擇。\n\n第四名的 Wopet Heritage View 雙碗，用親民價格帶來鏡頭監看和雙碗設計，第五名的 Petlibro One RFID 靠 RFID 標籤防止一隻寵物偷吃另一隻的份補上榜尾。暑假出遊在即，Granary Camera 就是我信得過、能在你不在家時把寵物餵飽又看得見的那台。",
                "highlights": [
                    {"title": "Petlibro Granary Camera 以可靠取勝", "body": "雙渦輪馬達被 PCMag 記錄為比單螺桿設計防卡四倍，而單螺桿是驗證評論裡最常見的故障模式。獲 PCMag 和 Wirecutter 選為最佳自動餵食器，它就是會準時給飯，這正是餵食器的全部工作。"},
                    {"title": "鏡頭加雙向語音讓你隨時連線", "body": "1080P 鏡頭搭配 145 度廣角和紅外線夜視，讓你看著寵物吃飯，雙向語音能用你的聲音安撫牠。暑假出遊在即，這份遠端可見度就是讓餵食器變成安心感的關鍵功能。"},
                    {"title": "Petlibro Polar 解決濕食難題", "body": "半導體製冷讓濕食按時保鮮，這是品類裡最難的挑戰。對吃濕食的貓咪來說，Polar 是讓你能自動餵食又不犧牲牠真正需要食物的突出選擇。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK smart-pet-feeders")


if __name__ == "__main__":
    build_air_purifiers()
    build_portable_air_conditioners()
    build_cordless_vacuums()
    build_robot_vacuums()
    build_robotic_pool_cleaners()
    build_robot_lawn_mowers()
    build_smart_pet_feeders()
    print("Batch 4 complete")
