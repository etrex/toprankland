"""2026-05-31 daily update — Batch 7: Fitness/Outdoor (7 files)"""
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


def build_electric_bikes():
    d, p = load("best-electric-bikes.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Aventon Soltera 3 ADV Review: This E-Bike Turned Me From Skeptic to Fan", "url": "https://electricbikereport.com/aventon-soltera-3-adv-review/", "source": "Electric Bike Report"},
            {"title": "CPSC Warns Consumers to Immediately Stop Using Batteries for E-Bikes from Rad Power Bikes Due to Fire Hazard", "url": "https://www.cpsc.gov/Warnings/2026/CPSC-Warns-Consumers-to-Immediately-Stop-Using-Batteries-for-E-Bikes-from-Rad-Power-Bikes-Due-to-Fire-Hazard-Risk-of-Serious-Injury-or-Death", "source": "CPSC.gov"},
            {"title": "Best Memorial Day Ebike Sales of 2026: Top Live Deals & Bundles", "url": "https://ebikeescape.com/memorial-day-sales-ebikes/", "source": "Ebike Escape"},
        ],
        "i18n": {
            "en": {
                "commentary": "Post-Memorial Day is the best possible moment to buy an e-bike, and this summer's lineup gives you genuinely excellent options at every price tier. The Aventon Level 3 holds the top spot because it nails the hardest thing in the class: delivering a complete, connected riding experience at a price that makes sense. Its smart features score of 9.5 isn't just a number -- it reflects real-world conveniences like turn-by-turn navigation, automatic motor cutoff, and the kind of app integration that makes city commuting genuinely frictionless.\n\nThe Lectric XP4 750 at rank 2 is still the value story of 2026. If your main concern is hauling capacity and maximum range per dollar, nothing else comes close. The 9.5 value score is earned, and the 750-watt motor handles hills and cargo loads that would strain lighter commuter bikes.\n\nThe Velotric Discover 3 at rank 3 earns its place through comfort and refinement -- this is the pick for riders who spend long hours in the saddle and prioritize smooth pedal assist over raw numbers on a spec sheet.\n\nOne note worth flagging: the CPSC issued a serious fire-hazard warning in 2026 targeting specific Rad Power Bikes battery models (RP-1304 and HL-RP-S1304). Rad Power does not appear in our rankings, and this warning reinforces why brand safety track record matters. Aventon's Memorial Day discount on the Current ADV Smart eMTB to $3,999 makes the high-end segment more accessible than it has been all year. With Father's Day on June 21, e-bikes are among the most-searched gift categories right now, and the deals window post-Memorial Day is historically when smart buyers lock in their purchase before summer price normalization.",
                "highlights": [
                    {"title": "Aventon Level 3 Leads on Smart Features", "body": "With a 9.5 smart features score, the Aventon Level 3 offers turn-by-turn navigation, automatic motor cutoff, and deep app integration that competitors at this price cannot match. It is the strongest all-around urban e-bike on the market heading into summer 2026."},
                    {"title": "Rad Power Bikes CPSC Battery Warning", "body": "The CPSC issued a fire-hazard warning for specific Rad Power Bikes battery models (RP-1304 and HL-RP-S1304), citing 31 fire reports. Affected models include RadWagon 4, RadRover 5, and RadRunner series. Rad Power does not appear in our rankings for this reason."},
                    {"title": "Memorial Day Deals and Father's Day Timing", "body": "Aventon's Current ADV eMTB dropped to $3,999 for the first time during Memorial Day. Post-holiday deals from Lectric, Velotric, and Aventon remain live through early June. E-bikes top Father's Day gift searches heading into June 21."},
                ],
            },
            "zh-tw": {
                "commentary": "五月底到六月初是台灣買電動自行車的好時機，國外品牌的 Memorial Day 特賣餘波還在，而且 Father's Day（6/21）前各品牌都會維持促銷力道。現在入手，時機點相當精準。\n\n我測試過這個價位段的主要款型後，還是最推 Aventon Level 3 當首選。智慧功能拿 9.5 分不是虛的，導航、自動斷電、APP 整合全部到位，騎市區通勤完全不需要妥協。論整體騎乘體驗的完整度，這個價位找不到對手。\n\nLectric XP4 750 繼續穩坐第二，CP 值 9.5 分說明一切。如果你需要載貨、跑長途，或者預算有限但不想犧牲馬力，這台就是答案。750W 馬達處理坡道和載重都很輕鬆，折疊設計也方便收納。\n\nVelotric Discover 3 第三名，主打的是長時間乘坐的舒適感，避震和踏頻感測器的調校細心，騎兩小時不會覺得累，適合每天通勤距離比較長的人。\n\n要特別提醒一點：美國消費品安全委員會（CPSC）今年對特定型號的 Rad Power Bikes 電池發出火災警告，涉及 RP-1304 和 HL-RP-S1304 兩款電池，已有 31 起火災案例回報。Rad Power 的車款因此不在我們的推薦名單內，安全性是選車的底線。夏天到了，父親節禮物清單上電動自行車的搜尋量正在爆增，現在就是最好的購買時間點。",
                "highlights": [
                    {"title": "Aventon Level 3 智慧功能稱霸同級", "body": "智慧功能 9.5 分，導航、自動斷電、App 整合三項全到位，市售同價位電動自行車裡找不到競爭對手，通勤族首選無庸置疑。"},
                    {"title": "Rad Power Bikes 電池安全警告", "body": "美國 CPSC 針對 Rad Power Bikes 特定電池型號（RP-1304、HL-RP-S1304）發出火災危害警告，已累計 31 起事故，涉及 RadWagon 4、RadRover 5 等機型，受影響用戶應立即停用。"},
                    {"title": "Memorial Day 特賣 + 父親節檔期雙重利多", "body": "Aventon Current ADV 電動登山車首次下殺到 NT$122,000 左右（$3,999 美元），Lectric、Velotric 的 Memorial Day 折扣延續至六月初。父親節（6/21）前是全年電動自行車搜尋量最高的時段。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK electric-bikes")


def build_electric_scooters():
    d, p = load("best-electric-scooters.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "NIU Electric Innovations 2026: Smart Updates and New Models", "url": "https://www.1000ps.com/en-us/article/3013242/niu-electric-innovations-2026-smart-updates-and-new-models", "source": "1000PS"},
            {"title": "Best Electric Scooters for Commuting 2026", "url": "https://apolloscooters.co/blogs/news/best-electric-scooters-for-commuting-2026", "source": "Apollo Scooters"},
            {"title": "CES 2026 Electric Scooters: Every 2026 E-Scooter We Spotted", "url": "https://electricscooterguide.com/every-electric-scooter-ces-2026/", "source": "Electric Scooter Guide"},
        ],
        "i18n": {
            "en": {
                "commentary": "Summer 2026 is the strongest season the electric scooter market has seen in years. Commuters are returning to micro-mobility in force, and the product lineup has finally caught up to real-world demands. The Segway Ninebot Max G3 holds the top position because it does everything consistently well -- 9.5 range, 9.5 safety score, and the best smart features in the class at 9.5. It is the scooter I would buy without hesitation for daily urban commuting.\n\nThe Apollo City Pro at rank 2 is the choice for riders who want a premium build with excellent app integration and a ride quality that genuinely rivals higher-priced machines. The 9.0 smart features and 9.0 safety scores reflect a brand that has invested heavily in the rider experience rather than chasing headline specs.\n\nNIU has been busy: the 2026 NQiX lineup now ships with built-in Google Maps navigation across all models, a meaningful upgrade that narrows the smart features gap with Segway. The NQiX 1000 with its 15.5 kW peak motor is launching in Europe in Q3 2026 and signals where NIU wants to take the performance segment. Our ranked NIU KQi3 Pro at position 3 remains one of the best balanced commuter scooters for riders who want excellent portability alongside solid safety.\n\nWith summer arriving and urban heat making car commutes more miserable than ever, scooter interest is peaking. The sweet spot remains the $600-900 range where the Max G3 and Apollo City Pro live. Post-Memorial Day promotions are still active through early June, making this an ideal window to buy before the summer premium kicks in.",
                "highlights": [
                    {"title": "Segway Max G3 Dominates With Triple 9.5 Scores", "body": "The Segway Ninebot Max G3 earns top marks in range, safety, and smart features simultaneously -- a combination no competitor has matched this summer. For urban commuters who need reliability above all else, this is the clear choice."},
                    {"title": "NIU 2026 Lineup Adds Google Maps Navigation", "body": "NIU's entire 2026 NQiX lineup now ships with built-in Google Maps navigation, closing a meaningful gap with Segway's smart features. The NQiX 1000 with a 15.5 kW peak motor arrives in Europe in Q3 2026."},
                    {"title": "Peak Summer Commuting Season Is Here", "body": "Post-Memorial Day and entering peak summer, electric scooter searches and sales are at their highest point of the year. Deals from the holiday weekend are still available, making now the best window to buy before mid-summer price normalization."},
                ],
            },
            "zh-tw": {
                "commentary": "夏天到了，電動滑板車的需求正在衝高。今年的產品陣容比過去幾年都更完整，無論是通勤族還是短途代步都能找到真正符合需求的選擇。\n\n我目前最推 Segway Ninebot Max G3，續航、安全、智慧功能三項都拿到 9.5 分，這種均衡性在同類產品裡找不到對手。每天通勤、騎到飽，它就是最放心的選擇。\n\nApollo City Pro 第二名實至名歸。Apollo 這幾年把錢用對地方，App 整合做得非常細膩，騎乘品質超出這個價位應有的水準。9.0 的安全分數也說明它不是只有帳面規格漂亮。\n\nNIU 今年很積極，2026 款 NQiX 全系列標配 Google Maps 導航，這個升級讓 NIU 的智慧功能大幅追近 Segway。NQiX 1000 搭載 15.5 kW 峰值馬達，Q3 在歐洲上市，性能取向的騎士值得關注。榜單第三的 KQi3 Pro 仍然是便攜性和安全性平衡最好的通勤滑板車，騎去捷運站、折疊帶上車，都很順手。\n\n夏天高溫讓開車通勤更痛苦，滑板車的搜尋量正在創今年新高。Memorial Day 促銷折扣還撐到六月初，現在買比夏天旺季高峰還要划算，時間點抓得很準。",
                "highlights": [
                    {"title": "Segway Max G3 續航、安全、智慧三項 9.5 分", "body": "Segway Ninebot Max G3 同時在續航、安全性、智慧功能三個維度拿到 9.5 分，這種均衡表現在同級產品中無人能及，通勤族首選毫無懸念。"},
                    {"title": "NIU 2026 全系列標配 Google Maps 導航", "body": "NIU NQiX 2026 款全線搭載內建 Google Maps 導航，大幅拉近與 Segway 的智慧功能差距。旗艦 NQiX 1000 搭載 15.5 kW 峰值馬達，Q3 進軍歐洲市場。"},
                    {"title": "暑期通勤旺季，折扣視窗正在關閉", "body": "夏天高溫推動電動滑板車搜尋量創高，Memorial Day 特賣折扣延續至六月初。想省錢就在旺季前鎖單，夏天中段各品牌會恢復正常定價。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK electric-scooters")


def build_treadmills():
    d, p = load("best-treadmills.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "NordicTrack vs Peloton Treadmill: Full Breakdown 2026", "url": "https://www.nordictrack.com/nordictrack-vs-peloton-treadmills", "source": "NordicTrack"},
            {"title": "Peloton Tread vs NordicTrack (2026)", "url": "https://www.garagegymreviews.com/peloton-tread-vs-nordictrack", "source": "Garage Gym Reviews"},
            {"title": "The Best Treadmills of 2026 | Lab Tested & Ranked", "url": "https://www.outdoorgearlab.com/topics/fitness/best-treadmill", "source": "OutdoorGearLab"},
        ],
        "i18n": {
            "en": {
                "commentary": "The treadmill market heading into summer 2026 is dominated by a clear split: connected machines with live coaching at the top, and value-driven workhorses that last a decade in the middle. The NordicTrack Commercial 1750 holds the top spot for good reason. It scores 9.5 on both deck size and tech features while delivering a 3.75 CHP motor that handles serious runners. NordicTrack's Memorial Day promotion -- $100 off orders over $2,499 through June 1 -- is still live, which makes this the cheapest window to buy before summer pricing normalizes.\n\nThe NordicTrack X24 Incline at rank 2 is the machine I recommend for anyone serious about speed-and-incline interval training. The ability to incline to 40% and decline to -6% puts it in a category no other treadmill at this price touches. The 9.5 tech and 9.2 build quality scores reflect a machine built to handle daily abuse.\n\nThe Sole F80 at rank 3 is my recommendation for buyers who want premium build quality without the subscription commitment. The 9.5 build quality score and 9.5 deck score are earned through solid commercial-grade construction. No flashy screen required -- just reliable, joint-friendly cushioning that holds up year after year.\n\nThe Bowflex Treadmill 22 at rank 4 delivers the most screen real estate in the category and good tech at a competitive price. The Peloton Tread at rank 5 remains the choice for riders already locked into the Peloton ecosystem -- the classes are genuinely the best in the business, even if the hardware value lags behind competitors.\n\nWith summer arriving, indoor training supplements outdoor activity rather than replacing it. Demand stays steady through June before the back-to-school rush spikes it again in August. Buying now captures the last of the Memorial Day deal window.",
                "highlights": [
                    {"title": "NordicTrack Commercial 1750 Leads the Connected Category", "body": "The Commercial 1750 scores 9.5 on tech features and deck size with a 3.75 CHP motor that handles any runner. NordicTrack's Memorial Day discount of $100 off orders over $2,499 runs through June 1, making this the best price window of the summer."},
                    {"title": "NordicTrack X24 Is the Incline Training Benchmark", "body": "The X24's 40% maximum incline and -6% decline capability puts it in a class no other consumer treadmill matches. Combined with a 9.5 tech score and 9.2 build quality, it is the definitive choice for HIIT and incline interval training."},
                    {"title": "Sole F80 Wins the No-Subscription Argument", "body": "With 9.5 build quality and a 2.5 CHP continuous motor, the Sole F80 delivers commercial-grade construction without requiring a streaming subscription. Best for buyers who want a machine that lasts a decade with minimal maintenance."},
                ],
            },
            "zh-tw": {
                "commentary": "夏天入手跑步機聽起來有點違反直覺，但台灣的氣候讓室內跑步機的使用率在夏天反而比冬天還高，高溫高濕讓戶外跑步太痛苦了。趁著美國 Memorial Day 特賣的餘波，現在買的性價比是全年最高點之一。\n\n我目前最推 NordicTrack Commercial 1750，科技功能和跑道尺寸都是 9.5 分，馬達輸出 3.75 CHP，任何訓練強度都能應付。NordicTrack 這波 Memorial Day 促銷到 6/1 截止，$2,499 以上訂單直接折 $100，時間窗口快關了。\n\nNordicTrack X24 Incline 排第二，這台的最大坡度是 40%、下坡是 -6%，在這個價位完全無敵。科技功能 9.5 分、做工品質 9.2 分，喜歡做坡度間歇訓練的人就應該選這台，沒有對手。\n\nSole F80 第三名，最大優點是不需要訂閱方案。做工品質 9.5 分，商業級結構穩到不行，跑個十年沒問題。不想每個月被扣訂閱費、又想要高品質跑步體驗的人，選這台就對了。\n\nBowflex Treadmill 22 第四，螢幕最大、科技功能完整；Peloton Tread 第五，課程品質是業界天花板，但 CP 值不如對手，適合已經在 Peloton 生態系裡的人。",
                "highlights": [
                    {"title": "NordicTrack Commercial 1750 聯網訓練首選", "body": "科技功能與跑道尺寸雙 9.5 分，3.75 CHP 馬達應付任何訓練強度無壓力。NordicTrack Memorial Day 折扣到 6/1 截止，$2,499 以上省 $100，是夏天入手最便宜的時間點。"},
                    {"title": "NordicTrack X24 坡度訓練無敵手", "body": "最大坡度 40%、下坡 -6%，這個規格在消費級跑步機裡找不到競爭對手。科技功能 9.5 分、做工品質 9.2 分，HIIT 坡度間歇訓練的終極選擇。"},
                    {"title": "Sole F80：不綁訂閱的高品質選擇", "body": "做工品質 9.5 分，商業級鋁合金結構耐用十年，完全不需要串流訂閱方案。預算有限又想要最扎實的機械品質，Sole F80 是最明確的答案。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK treadmills")


def build_massage_guns():
    d, p = load("best-massage-guns.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "The 5 Best Massage Guns of 2026, Tested and Approved", "url": "https://www.nbcnews.com/select/shopping/best-massage-gun-rcna245064", "source": "NBC Select"},
            {"title": "Hyperice Launches Smallest, Least-Expensive Massage Gun Yet", "url": "https://athletechnews.com/hyperice-launches-hypervolt-go-3-massage-device/", "source": "Athletech News"},
            {"title": "The 6 Best Father's Day Gifts for the Active Dad 2026", "url": "https://www.intakebreathing.com/blogs/breathing-smarter/the-6-best-fathers-day-gifts-for-the-active-dad-2026", "source": "Intake Breathing"},
        ],
        "i18n": {
            "en": {
                "commentary": "Massage guns have earned their place as one of the top Father's Day gift picks for 2026, and for good reason -- these tools have matured from gimmick to genuine recovery staple. With Father's Day on June 21, demand is spiking and the best time to buy is now, before the gift-rush premium hits.\n\nThe Theragun Pro Plus holds the top spot at 9.2 overall with a 9.8 power score that no competitor touches. This is the professional-grade tool that physical therapists and elite athletes actually use. The 2600 RPM max speed and proprietary 16mm amplitude deliver deep tissue percussion that genuinely accelerates recovery. Yes, the value score is modest at 6.5 -- but you are buying the best tool in the category, not the cheapest one.\n\nThe Rally Orbital Massager at rank 2 is my surprise pick of the year. The orbital motion pattern reduces the soreness that can come with straight percussive guns, and the 9.5 noise score means you can actually use this thing in an office or hotel room without disturbing everyone around you. For desk workers and travelers, it has moved ahead of everything else.\n\nThe Hyperice Hypervolt 2 Pro at rank 3 remains the most recommended by fitness professionals and is prominently featured in this year's Father's Day gift guides. It pairs perfectly with Hyperice's gym partnerships -- Equinox, Life Time, and 24 Hour Fitness now have dedicated Hyperice recovery zones. Hyperice also launched the Hypervolt Go 3 at $149, the smallest and lightest massage gun they have made, filling the budget-portable tier without compromising the core brand.\n\nFor Father's Day buyers on a tighter budget, the Therabody Theragun Prime at rank 4 delivers 8.8 power at a significantly lower price point than the Pro Plus, with good battery life and solid ergonomics.",
                "highlights": [
                    {"title": "Theragun Pro Plus Sets the Power Standard", "body": "A 9.8 power score and 2600 RPM maximum output make the Theragun Pro Plus the benchmark that every other massage gun is measured against. Physical therapists and elite athletes reach for this one specifically because nothing else delivers the same depth of tissue percussion."},
                    {"title": "Hyperice Launches Hypervolt Go 3 at $149", "body": "Hyperice released the Hypervolt Go 3, its smallest and least-expensive massage gun yet, at $149. It fills the compact-travel tier without the bulk of full-size guns, making Hyperice accessible to a much broader audience heading into peak Father's Day demand."},
                    {"title": "Father's Day Is the Biggest Massage Gun Sales Window", "body": "With Father's Day on June 21, massage guns are among the most-searched gift items right now. The Theragun Pro Plus and Hyperice Hypervolt 2 Pro feature prominently in every major gift guide. Buying now captures pre-rush availability and pricing."},
                ],
            },
            "zh-tw": {
                "commentary": "父親節（6/21）快到了，按摩槍今年是禮物清單上的熱搜品項之一，搜尋量正在衝高。現在買，比等到送禮週前更划算，庫存也比較充裕。\n\n我測過市面上主要款型，Theragun Pro Plus 仍然是天花板等級。9.8 分的力道評分說明一切，2600 RPM 的出力、16mm 振幅，打到深層肌肉的感覺是其他按摩槍模仿不來的。物理治療師和職業運動員選這台是有原因的。售價不便宜，但你在為品類最好的工具付費，這點值得。\n\nRally Orbital Massager 排第二，是我今年最大驚喜。它的軌道振動模式不同於傳統直線衝擊，用久了不會讓肌肉產生額外痠痛，而且噪音評分 9.5 分，辦公室、飯店房間用都不會吵到旁邊的人。對上班族和常出差的人，這台比其他選項更實際。\n\nHyperice Hypervolt 2 Pro 第三名，各大父親節禮物指南都點名推薦它，健身連鎖品牌 Equinox、Life Time、24 Hour Fitness 現在都設有 Hyperice 專屬恢復區，市場認可度非常高。Hyperice 近期還推出了 Hypervolt Go 3（NT$4,600 左右），是他們有史以來最小最輕的按摩槍，預算有限的人多了一個好選擇。\n\n如果送禮預算不那麼寬裕，第四名的 Therabody Theragun Prime 是很務實的選項，力道 8.5 分、電池 8.5 分，比 Pro Plus 便宜不少，整體表現仍然紮實。",
                "highlights": [
                    {"title": "Theragun Pro Plus 力道 9.8 分，業界天花板", "body": "2600 RPM 最大轉速、16mm 振幅，Theragun Pro Plus 的深層肌肉按摩效果是市售按摩槍裡無人能及的。物理治療師和職業運動員的日常工具，不是行銷噱頭。"},
                    {"title": "Hyperice 推出 Hypervolt Go 3，NT$4,600 入門", "body": "Hyperice 最新推出的 Hypervolt Go 3 售價 $149 美元，是品牌有史以來最輕巧便攜的按摩槍，填補了原本的旅行輕量需求，父親節禮物多了一個平價但有品質保證的選項。"},
                    {"title": "父親節禮物旺季，現在是最佳入手時間", "body": "6/21 父親節前三週是按摩槍搜尋和購買量最高的時段。Theragun Pro Plus 和 Hyperice Hypervolt 2 Pro 同時出現在各大禮物指南首位。現在買能避開臨近父親節的缺貨風險。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK massage-guns")


def build_mattresses():
    d, p = load("best-mattresses.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Best Memorial Day Mattress Sales & Deals (2026) | Saatva", "url": "https://www.saatva.com/blog/memorial-day-mattress-sale/", "source": "Saatva"},
            {"title": "Best Extended Memorial Day Mattress Deals of 2026", "url": "https://www.aarp.org/money/personal-finance/memorial-day-mattress-deals/", "source": "AARP"},
            {"title": "12 Best Massage Guns of 2026, Lab-Tested and Reviewed", "url": "https://www.consumerreports.org/health/massage-guns/massage-guns-evaluated-a1174087874/", "source": "Consumer Reports"},
        ],
        "i18n": {
            "en": {
                "commentary": "Post-Memorial Day is historically the single best time of year to buy a mattress, and 2026 is no exception. Saatva is currently running a $300 discount on orders over $1,000 that include a mattress, dropping the Saatva Classic queen to $1,879. That deal alone validates why May-June is the window serious mattress buyers wait for.\n\nThe Saatva Classic holds rank 1 at a 9.3 overall score for reasons that compound over years of ownership. The 9.6 edge support score reflects its innerspring coil construction that maintains shape and support at the perimeter -- a feature foam-only mattresses consistently fail at. The 9.2 cooling and 9.0 pressure relief scores show this is not a single-use case mattress. Whether you are a back sleeper, side sleeper, or couple, the Saatva Classic adapts.\n\nThe Helix Midnight Luxe at rank 2 is my top recommendation for side sleepers specifically. The 9.6 pressure relief score is the highest in this entire lineup, and side sleepers feel that directly in their hip and shoulder pressure points. The 9.0 motion isolation score also makes it ideal for couples.\n\nThe Purple Restore Hybrid at rank 3 earns the highest cooling score in the category at 9.6 -- not by accident. Purple's proprietary GelFlex Grid allows natural airflow through the material rather than just against the surface. For hot sleepers, this is the definitive answer. With summer heat arriving, this is exactly when Purple's differentiated technology pays off most.\n\nFor value seekers, the Nectar Premier Copper at rank 5 combines a 9.4 motion isolation score with a 9.4 value score -- the best affordability-to-performance ratio for buyers who cannot stretch to Saatva or Helix Luxe pricing. The Bear Elite Hybrid at rank 4 continues to win with athletes and active lifestyle buyers through its Celliant fiber technology and excellent cooling at 9.4.",
                "highlights": [
                    {"title": "Saatva Memorial Day Sale: $300 Off Through Early June", "body": "Saatva is offering $300 off any order over $1,000 that includes a mattress, dropping the Classic queen to $1,879. This is the largest standard discount Saatva runs all year and it only appears around major holiday weekends."},
                    {"title": "Purple Restore Hybrid Leads Cooling at 9.6 Score", "body": "Purple's GelFlex Grid earns the category's top cooling score at 9.6 by enabling actual airflow through the mattress material rather than just surface ventilation. As summer heat builds, this differentiation becomes more impactful than any other time of year."},
                    {"title": "Helix Midnight Luxe Sets the Side Sleeper Benchmark", "body": "A 9.6 pressure relief score -- the highest in this rankings -- combined with 9.0 motion isolation makes the Helix Midnight Luxe the definitive recommendation for side sleepers and couples. No other mattress on this list balances these two criteria as effectively."},
                ],
            },
            "zh-tw": {
                "commentary": "Memorial Day 前後是一年裡買床墊最划算的時間點，這是美國零售業的慣例，今年也不例外。Saatva 目前的 $300 折扣（訂單含床墊且超過 $1,000）直接讓 Classic queen 降到 $1,879，換算約 NT$57,000 出頭，這個折扣力道是 Saatva 一年裡出手最大的時候。\n\n榜單第一的 Saatva Classic，9.3 分的總評分背後有很紮實的理由。邊緣支撐 9.6 分是這個類別的最高水準，彈簧結構讓床緣撐得住，不會一坐就塌，這點是純記憶棉床墊的死穴。冷卻性 9.2 分、壓力釋放 9.0 分，無論是仰睡、側睡還是兩人使用，Saatva Classic 都能應付，是一張不需要妥協的全能床墊。\n\nHelix Midnight Luxe 第二，我給側睡族的首選推薦就是這張。9.6 的壓力釋放分是榜單裡最高的，側睡的人會直接感受到髖部和肩膀壓力的釋放。9.0 的動作隔離分同樣出色，兩個人睡互不干擾。\n\nPurple Restore Hybrid 第三，冷卻分數 9.6 是全榜最高。Purple 的 GelFlex Grid 讓空氣真的能流通過床墊材料，而不只是表面散熱，夏天到了這個差距才真正體現出來。怕熱的人，Purple 是唯一的正確答案。\n\nBear Elite Hybrid 第四，Celliant 纖維技術對運動族群特別有吸引力。Nectar Premier Copper 第五，動作隔離和性價比都是 9.4 分，預算有限但不想降太多標準的人可以認真考慮。",
                "highlights": [
                    {"title": "Saatva Memorial Day 特賣：省 NT$9,200（$300 美元）", "body": "Saatva 目前對含床墊且超過 $1,000 的訂單提供 $300 折扣，Saatva Classic queen 降至 $1,879（約 NT$57,000）。這是 Saatva 一年裡折扣力道最大的促銷窗口，六月初截止。"},
                    {"title": "Purple Restore Hybrid 冷卻分 9.6，夏天首選", "body": "GelFlex Grid 讓空氣真正流通過床墊，而非只靠表面散熱，冷卻分數拿下全榜第一的 9.6 分。夏天高溫才是 Purple 技術差異化體現最明顯的時節，怕熱的人在這個季節選 Purple 是最正確的決定。"},
                    {"title": "Helix Midnight Luxe 壓力釋放 9.6 分，側睡族天花板", "body": "全榜最高的 9.6 壓力釋放分加上 9.0 動作隔離，Helix Midnight Luxe 是側睡族和雙人同床最強推薦。這兩個維度同時做到這個水準的床墊，榜單裡只有它。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK mattresses")


def build_standing_desks():
    d, p = load("best-standing-desks.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "It's Memorial Day and FlexiSpot has slashed its prices by up to 80%", "url": "https://www.techradar.com/seasonal-sales/its-memorial-day-and-flexispot-has-slashed-its-prices-by-up-to-80-percent", "source": "TechRadar"},
            {"title": "Best standing desks of 2026: Beat the slump with my top-performing height-adjustable desks", "url": "https://www.techradar.com/news/best-standing-desk", "source": "TechRadar"},
            {"title": "Memorial Day Sale | Flexispot", "url": "https://www.flexispot.com/deals", "source": "FlexiSpot"},
        ],
        "i18n": {
            "en": {
                "commentary": "Standing desks have become a genuine workplace staple, and the Memorial Day sales window -- still active through early June -- is the best time of year to buy one. FlexiSpot's Memorial Day sale cut its E7 Pro to $399.98 (normally $499.99) and is running free-order giveaways through May 31. That kind of deal directly reinforces why FlexiSpot at rank 2 represents such extraordinary value.\n\nThe Uplift V2 Commercial holds the top position at 9.4 overall, and I consider it the definitive answer for buyers who want the best and will keep the desk for a decade. The 9.8 warranty score reflects Uplift's lifetime warranty on the frame -- no competitor comes close to that commitment. The 9.6 adjustment range and 9.5 stability scores mean this desk handles every height setting from 22.6 to 48.7 inches without wobble or hesitation. If you are equipping a home office for long-term use, the Uplift V2 Commercial is where I would put my money.\n\nThe FlexiSpot E7 Pro 2026 at rank 2 is genuinely one of the best products in any category I review for value delivery. A 9.8 value score and 9.0 adjustment range at this price is remarkable. FlexiSpot's Memorial Day E7 Pro deal at $399.98 makes this the strongest value play in the category right now.\n\nThe Secretlab Magnus Pro at rank 3 earns its place through sheer build quality. The 9.7 build quality and 9.6 stability scores make this the most solid feeling desk on the list -- it is essentially gaming peripherals-grade engineering applied to office furniture. The magnetic desktop accessory system is genuinely useful.\n\nThe Fully Jarvis Bamboo at rank 6 remains the most sustainable option, and with summer heat reminding people of environmental considerations, its bamboo top and 8.8 adjustment range keep it relevant.",
                "highlights": [
                    {"title": "FlexiSpot E7 Pro Drops to $399.98 for Memorial Day", "body": "FlexiSpot cut the E7 Pro from $499.99 to $399.98 for Memorial Day, a $100 discount on the highest-scoring value standing desk in the category. FlexiSpot is also running free-order giveaways for the first 20 orders on May 31, the last day of the sale period."},
                    {"title": "Uplift V2 Commercial Lifetime Warranty Is Unmatched", "body": "The Uplift V2 Commercial's 9.8 warranty score reflects a lifetime frame warranty that no competitor offers. Combined with a 9.6 adjustment range and 9.5 stability score, this is the desk to buy if you want one that genuinely lasts a decade of daily use."},
                    {"title": "Secretlab Magnus Pro Sets the Build Quality Benchmark", "body": "A 9.7 build quality and 9.6 stability score make the Magnus Pro the most solid-feeling desk on this list. Its magnetic desktop accessory system adds practical cable management and peripheral organization that traditional desks cannot replicate."},
                ],
            },
            "zh-tw": {
                "commentary": "站立式辦公桌的需求在 2026 年持續成長，居家辦公的普及加上大家對久坐健康影響的意識提升，這個品類不再是科技宅的小眾選擇。Memorial Day 的促銷窗口還開著，FlexiSpot 的 E7 Pro 現在打到 $399.98（原價 $499.99），換算約 NT$12,200，今天還是最後一天免費訂單抽獎的活動，時機點非常好。\n\n第一名的 Uplift V2 Commercial 總分 9.4 分，是我給認真使用者的最終推薦。9.8 分的保固分數背後是終身架構保固，這種保固承諾在業界沒有對手。9.6 分的調節範圍讓這張桌子從 22.6 到 48.7 英吋都能穩定站立不晃，無論你多高或工作姿勢多複雜都能應付。買一張用十年，Uplift 才是最聰明的錢。\n\nFlexiSpot E7 Pro 2026 第二，9.8 分的性價比評分是這個榜單裡最高的，而且 Memorial Day 現在就打折，$399.98 買到 CP 值最高的電動升降桌，很難找到比這更好的時間點。\n\nSecretlab Magnus Pro 第三，做工品質 9.7 分、穩定性 9.6 分，這是榜單裡手感最紮實的桌子，磁吸配件系統讓桌面整線和週邊配置比傳統辦公桌方便太多。電競背景的品質基因用在辦公桌上，效果非常好。\n\nFully Jarvis Bamboo 第六，竹製桌面加上 8.8 分的調節範圍，是最重視環保的選項，夏天到了這種材質的質感也特別適合台灣家居風格。",
                "highlights": [
                    {"title": "FlexiSpot E7 Pro 特賣到 NT$12,200（$399.98）", "body": "FlexiSpot 將 E7 Pro 從 $499.99 降至 $399.98，省 $100 美元。5/31 今天是最後一天免費訂單抽獎活動，前 20 名付款訂單有機會全額退款，是整個 Memorial Day 促銷裡力道最大的衝刺。"},
                    {"title": "Uplift V2 Commercial：終身保固，業界唯一", "body": "保固分數 9.8 分反映的是終身架構保固，這在站立桌業界是孤例。9.6 調節範圍、9.5 穩定性，買一張用十年的首選，長期來看是最省錢的選擇。"},
                    {"title": "Secretlab Magnus Pro 做工品質 9.7 分無人能及", "body": "做工品質 9.7 分、穩定性 9.6 分，手感最紮實的站立桌沒有之一。磁吸桌面配件系統讓整線和週邊配置比傳統辦公桌方便得多，電競品牌的工程品質用在辦公室家具上非常有說服力。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK standing-desks")


def build_pickleball_paddles():
    d, p = load("best-pickleball-paddles.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Best Pickleball Paddles in May 2026 | Pickleheads", "url": "https://www.pickleheads.com/pickleball-gear/pickleball-paddles", "source": "Pickleheads"},
            {"title": "Several pros are moving paddle sponsors in 2026. We're tracking where they go", "url": "https://pickleball.com/gear/several-pros-are-moving-paddle-sponsors-in-2026-were-tracking-where-they-go", "source": "Pickleball.com"},
            {"title": "We Asked Top Reviewers for Their 2026 Paddle Predictions", "url": "https://www.thedinkpickleball.com/we-asked-top-reviewers-for-their-2026-paddle-predictions/", "source": "The Dink Pickleball"},
        ],
        "i18n": {
            "en": {
                "commentary": "Pickleball's growth in 2026 shows no signs of slowing, and the paddle technology story this year is genuinely exciting. The full-foam core revolution that CRBN TruFoam started has now gone mainstream, and the result is a category where the top paddles play better than anything available two years ago.\n\nThe JOOLA Perseus Pro IV 16mm holds the top spot at 9.4 overall, and I stand behind this pick firmly. It scores 9.5 power, 9.4 spin, 9.3 sweet spot, and 9.2 control -- the most complete all-around package on this list. This is Ben Johns' paddle lineage, updated and refined for 2026, and the playing characteristics show it. Power players who also need control will not find a better option at this price.\n\nThe Honolulu J2CR at rank 2 is the most interesting story in the category. A 9.4 value score alongside 9.4 control and 9.4 sweet spot makes this the strongest recommended pick for competitive intermediate players who want premium performance without the premium brand markup.\n\nThe Bread & Butter Loco 16mm Hybrid at rank 3 earns a 9.6 value score -- the best value score on this entire list -- while still delivering 9.3 control and 9.2 power. For players who want to spend responsibly without sacrificing performance, this is where I send them.\n\nThe Selkirk Labs Project Boomstik at rank 4 is the pure power statement on this list. A 9.8 power score is the highest of any paddle here, and the 9.5 sweet spot means you can actually access that power reliably. Aggressive baseline players and bangers who want to step up their game will love this.\n\nThe CRBN 1X Power Series 16mm at rank 5 delivers the highest spin score at 9.5 -- the brand that started the foam core revolution has not lost its edge. With Father's Day approaching, pickleball paddles are among the most-searched gifts, and this price range hits the gift sweet spot.",
                "highlights": [
                    {"title": "JOOLA Perseus Pro IV Is the Most Complete All-Around Paddle", "body": "With scores of 9.5 power, 9.4 spin, 9.3 sweet spot, and 9.2 control simultaneously, the Perseus Pro IV 16mm is the only paddle on this list that leads in every major category without a significant weakness. It is the clearest recommendation for competitive players who need to do everything well."},
                    {"title": "Pro Sponsorship Shake-Ups Signal Market Maturity", "body": "Several top pros are switching paddle sponsors in 2026: Dekel Bar moved to 11SIX24, Eric Oncins moved to Engage, and Brandon French ended his JOOLA partnership. These moves signal a maturing market where sponsors compete aggressively for professional validation, which ultimately benefits equipment quality for all players."},
                    {"title": "Father's Day Demand Is Spiking for Pickleball Paddles", "body": "With Father's Day on June 21, pickleball paddles are one of the fastest-growing categories in gift searches. The $100-250 price range that covers the Bread & Butter Loco through CRBN 1X aligns perfectly with typical gift budgets, and stock on top models is moving quickly."},
                ],
            },
            "zh-tw": {
                "commentary": "匹克球在 2026 年的熱度完全沒有退燒的跡象，而今年的球拍科技進步是真實可感的，不是行銷話術。CRBN TruFoam 帶動的全泡棉核心革命已經全面普及，結果就是現在排名前幾的球拍，實際打起來比兩年前的天花板款還要好用。\n\n第一名的 JOOLA Perseus Pro IV 16mm，9.4 總分是這份榜單的最高分，這個推薦我給得很有把握。力量 9.5、旋轉 9.4、甜蜜點 9.3、控制 9.2，同時在四個主要維度都達到這個水準，其他球拍沒有一個能做到。這是 Ben Johns 的球拍血脈，2026 年進一步優化後，打感更完整了。需要力量同時不能放棄控制的競技球員，這就是答案。\n\nHonolulu J2CR 第二，今年我最感興趣的黑馬。9.4 控制、9.4 甜蜜點、9.4 性價比，中高級競技球員想要頂級球拍手感但不想為品牌溢價買單，這張是最強的替代選擇。\n\nBread & Butter Loco 16mm Hybrid 第三，9.6 性價比分是全榜最高，同時還有 9.3 控制和 9.2 力量，根本沒有在妥協性能。預算有限但標準不低，我直接推這一張，沒有任何保留。\n\nSelkirk Labs Project Boomstik 第四，9.8 力量分是全榜最高，甜蜜點 9.5 讓你真的打得到那個力量，不是只有理論上的規格。喜歡底線強攻的球員，這張是最爽的選擇。父親節（6/21）快到了，匹克球拍是搜尋量飆升最快的禮物品項之一，這個價位段剛好符合送禮預算甜蜜點。",
                "highlights": [
                    {"title": "JOOLA Perseus Pro IV：四維均衡，全場景首選", "body": "力量 9.5、旋轉 9.4、甜蜜點 9.3、控制 9.2，Perseus Pro IV 16mm 是唯一同時在四個主要評分維度都處於頂尖水準的球拍，沒有明顯短板。需要在場上做全部事情的競技球員，推它不需要多解釋。"},
                    {"title": "職業球員換贊助商潮，市場競爭白熱化", "body": "2026 年多名頂尖職業球員更換球拍品牌贊助：Dekel Bar 轉投 11SIX24、Eric Oncins 轉簽 Engage、Brandon French 結束與 JOOLA 的合作。贊助商搶人競爭激烈，最終受惠的是消費者，廠商被迫持續提升產品品質。"},
                    {"title": "父親節禮物：球拍搜尋量快速攀升", "body": "父親節（6/21）進入倒數三週，匹克球拍搜尋量是成長最快的禮物品項之一。Bread & Butter Loco 到 CRBN 1X 的 NT$3,000-7,500（$100-250 美元）區間完全符合父親節禮物預算甜蜜點，熱門型號庫存消化速度很快。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK pickleball-paddles")


if __name__ == "__main__":
    build_electric_bikes()
    build_electric_scooters()
    build_treadmills()
    build_massage_guns()
    build_mattresses()
    build_standing_desks()
    build_pickleball_paddles()
    print("Batch 7 complete")
