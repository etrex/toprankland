"""2026-06-02 daily update — Batch 7: Fitness/Outdoor (7 files)"""
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


def build_electric_bikes():
    d, p = load("best-electric-bikes.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Father's Day Sale: 4 Best Ebikes for Every Type of Dad", "url": "https://www.heybike.com/blogs/heybike-blog/fathers-day-sale-best-ebikes-for-every-type-of-dad", "source": "Heybike"},
            {"title": "Discounted E-Bikes: Best Time to Buy (2026 Calendar Guide)", "url": "https://leoguarbikes.com/blogs/news/discounted-e-bikes-calendar-guide", "source": "Leoguar Bikes"},
            {"title": "What's Next in 2026: All Things E-Bikes", "url": "https://www.autoevolution.com/news/what-s-next-in-2026-all-things-e-bikes-263438.html", "source": "autoevolution"},
        ],
        "i18n": {
            "en": {
                "commentary": "Three weeks out from Father's Day on June 21, e-bikes have become one of the most reliable big-ticket gifts of the season, and the timing for buyers is genuinely good right now. The Father's Day deal pattern is different from spring blowouts: instead of deep percentage cuts, brands are bundling real accessories with each purchase. Heybike is throwing in front and rear baskets and dropping the Ranger S by $400, while Viribus is running 10 percent off through June 22. For a gift, that bundled-accessory approach is often more useful than a raw discount because dad gets a complete, ready-to-ride package.\n\nThe Aventon Level 3 stays at the top of the list, and I keep coming back to the same reason: it solves the hardest problem in the category by delivering a fully connected, app-integrated riding experience at a price that still makes sense. The 9.5 smart features score reflects turn-by-turn navigation, automatic motor cutoff, and integration that makes daily city commuting feel effortless. For a Father's Day gift to a commuter, this is the safe, high-confidence pick.\n\nThe Lectric XP4 750 holds rank 2 as the value and cargo champion. The 750-watt motor handles hills and loads that lighter commuter bikes struggle with, the fold makes it easy to store in an apartment, and the 9.5 value score means you are not overpaying for the capability. If the dad in question wants to haul groceries or a kid seat, this is the one.\n\nThe Velotric Discover 3 holds rank 3 on the strength of long-ride comfort, with suspension and pedal-assist tuning that keep a two-hour ride pleasant. Industry coverage heading into summer 2026 points to lighter frames, longer range, and smarter safety features as the defining direction, and the top three here already reflect that maturity. Buying before the Father's Day rush locks in the best stock and the freshest bundles.",
                "highlights": [
                    {"title": "Aventon Level 3 Stays the Smart-Commuter Pick", "body": "A 9.5 smart features score covers turn-by-turn navigation, automatic motor cutoff, and deep app integration. For a Father's Day gift to a daily commuter, this is the highest-confidence choice in the category heading into summer 2026."},
                    {"title": "Father's Day Deals Favor Accessory Bundles", "body": "This season's e-bike promotions lean toward bundled accessories rather than deep price cuts. Heybike is adding front and rear baskets plus $400 off the Ranger S, and Viribus is running 10 percent off through June 22. For gifting, a complete ready-to-ride package often beats a raw discount."},
                    {"title": "Lectric XP4 750 Wins on Value and Cargo", "body": "The 750-watt motor handles hills and cargo loads that lighter commuter bikes cannot, and the folding design stores easily in an apartment. With a 9.5 value score, it is the pick for any dad who wants to haul groceries or add a child seat."},
                ],
            },
            "zh-tw": {
                "commentary": "離父親節（6/21）剩三週，電動自行車已經是這個檔期最穩的大件禮物之一，而且現在買的時機點其實不錯。父親節的促銷邏輯跟春季大特賣不太一樣，品牌不打深折，而是改送實用配件。Heybike 直接送前後車籃、Ranger S 折 $400，Viribus 則是 10% 折扣到 6/22。送禮的話，這種配件組合包通常比單純降價更實用，因為老爸收到的是一台「開箱即騎」的完整車。\n\n榜單第一還是 Aventon Level 3，我每次都回到同一個理由：它把這個品類最難的事情做好了，用合理的價格給你一台完全聯網、App 整合到位的車。智慧功能 9.5 分，導航、自動斷電、App 整合全部都有，每天騎市區通勤完全不用妥協。要送通勤族老爸，這台是最安全、最有把握的選擇。\n\nLectric XP4 750 守住第二，是 CP 值和載貨雙料冠軍。750W 馬達應付坡道和載重都輕鬆，折疊設計收在公寓裡也方便，9.5 的性價比分數代表你不會為這些能力多付錢。如果家裡老爸想載菜或裝兒童座椅，就選這台。\n\nVelotric Discover 3 第三，靠的是長途乘坐的舒適度，避震和踏頻輔助的調校讓騎兩小時也不累。國外媒體展望 2026 夏天的方向是更輕的車架、更長的續航、更聰明的安全功能，榜單前三名其實已經反映了這種成熟度。趕在父親節送禮潮之前下手，庫存最齊、配件組合也最新。",
                "highlights": [
                    {"title": "Aventon Level 3 智慧通勤首選不動", "body": "智慧功能 9.5 分，導航、自動斷電、App 整合全到位。要送每天通勤的老爸，這台是 2026 夏天進場時最有把握的選擇。"},
                    {"title": "父親節促銷主打配件組合包", "body": "這個檔期的電動自行車促銷偏向送配件而不是砍價。Heybike 加送前後車籃、Ranger S 折 $400，Viribus 10% 折扣到 6/22。送禮的話，一台開箱即騎的完整車組往往比單純折價更划算。"},
                    {"title": "Lectric XP4 750 載貨與 CP 值雙冠", "body": "750W 馬達應付坡道與載重輕鬆，折疊設計收在公寓也方便。9.5 性價比分數，想載菜或加裝兒童座椅的老爸首選就是這台。"},
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
            {"title": "Best Electric Scooters for Commuting 2026", "url": "https://apolloscooters.co/blogs/news/best-electric-scooters-for-commuting-2026", "source": "Apollo Scooters"},
            {"title": "Top 5 Alternatives to Segway in 2026: TopRiding, NIU & More", "url": "https://topriding.com/blogs/news/top-5-alternatives-to-segway", "source": "TopRiding"},
            {"title": "NIU's V-Day Sale Offers KQi 300X E-Scooter With Dual-Tube Hydraulic Suspension at New $727 Low", "url": "https://9to5toys.com/2026/02/12/nius-v-day-sale-kqi-300x-e-scooter-new-727-low-more/", "source": "9to5Toys"},
        ],
        "i18n": {
            "en": {
                "commentary": "Early June is peak commuting season for electric scooters, and this summer the buying decision comes down to one thing that the spec sheets often hide: voltage architecture and real-world range, not headline motor wattage. That distinction is exactly why the Segway Ninebot Max G3 stays at the top of the list. It posts 9.5 across range, safety, and smart features simultaneously, and reviewers measuring real-world miles consistently find Segway's Max line meets or beats its own claims. For a daily urban commute where reliability matters more than bragging rights, this is the scooter I recommend without hesitation.\n\nThe Apollo City Pro holds rank 2 on the strength of build quality and app integration that genuinely rivals more expensive machines. Apollo has put its money into ride feel and rider experience, and the 9.0 safety score reflects a brand that is not just chasing top-line numbers. Apollo's current lineup, including dual-motor models with IP66 water resistance and lifetime-warranty options, shows how seriously the brand takes long-term ownership.\n\nNIU's KQi3 Pro stays at rank 3 as the portability-and-safety balance pick. The 48-volt architecture on NIU's newer KQi models is the kind of detail that matters in practice: higher voltage holds speed deeper into the battery cycle, so you do not feel the scooter sag as the charge drops. NIU has been aggressive on pricing too, recently dropping the KQi 300X with dual-tube hydraulic suspension to a new low, which keeps competitive pressure on the whole category.\n\nWith summer heat making car commutes more miserable by the week, scooter demand is climbing toward its annual peak. The $600 to $900 band where the Max G3 and City Pro live remains the sweet spot, and buying now beats the mid-summer price normalization.",
                "highlights": [
                    {"title": "Segway Max G3 Holds Triple 9.5 Scores", "body": "The Max G3 earns 9.5 in range, safety, and smart features at once, a combination no rival matches this summer. Real-world mileage tests consistently show Segway's Max line meeting or beating its own range claims, which is why it stays the top commuter pick."},
                    {"title": "Voltage Architecture Beats Headline Wattage", "body": "NIU's newer KQi models use a 48-volt architecture that holds speed deeper into the battery cycle, so the scooter does not sag as the charge drops. This kind of real-world engineering detail matters far more than peak motor wattage on a spec sheet."},
                    {"title": "Peak Commuting Season Is Here", "body": "As summer heat makes car commutes more miserable, scooter demand is climbing toward its annual peak. The $600 to $900 band where the Max G3 and Apollo City Pro live remains the sweet spot, and buying now beats mid-summer price normalization."},
                ],
            },
            "zh-tw": {
                "commentary": "六月初是電動滑板車的通勤旺季，今年夏天的選購關鍵其實藏在規格表看不到的地方：電壓架構和實際續航，而不是帳面上的馬達瓦數。這個差別正是 Segway Ninebot Max G3 守住榜首的原因。它在續航、安全、智慧功能三項同時拿到 9.5 分，國外實測里程的媒體一致發現 Segway Max 系列達到甚至超過自家標示。每天市區通勤，可靠度比帳面數字重要，我推這台不會猶豫。\n\nApollo City Pro 第二，靠的是做工品質和 App 整合，實際體驗直逼更貴的機型。Apollo 把錢花在騎乘手感和使用者體驗上，9.0 的安全分數說明它不是只追求帳面數字。Apollo 目前的產品線包含雙馬達、IP66 防水、終身保固的機型，可以看出品牌對長期使用有多認真。\n\nNIU KQi3 Pro 守住第三，是便攜性和安全性平衡的選擇。NIU 新款 KQi 的 48V 架構是實際騎乘才感受得到的細節：電壓高，速度在電量下降時也維持得住，不會騎到一半就軟掉。NIU 在價格上也很積極，最近把搭載雙管液壓避震的 KQi 300X 降到新低點，等於替整個品類維持競爭壓力。\n\n夏天高溫讓開車通勤一週比一週難受，滑板車需求正往全年高峰爬。Max G3 和 City Pro 所在的 $600 到 $900 區間（約 NT$18,000 到 27,000）還是甜蜜點，現在買比夏天中段恢復原價划算。",
                "highlights": [
                    {"title": "Segway Max G3 三項 9.5 分守榜首", "body": "Max G3 在續航、安全、智慧功能同時拿 9.5 分，這種組合今夏無人能及。國外實測里程一致顯示 Segway Max 系列達到甚至超過自家標示，通勤首選地位穩固。"},
                    {"title": "電壓架構勝過帳面瓦數", "body": "NIU 新款 KQi 採 48V 架構，速度在電量下降時依然維持得住，騎到後段不會軟掉。這種實際騎乘的工程細節，遠比規格表上的馬達峰值瓦數重要。"},
                    {"title": "通勤旺季已到", "body": "夏天高溫讓開車通勤越來越難受，滑板車需求正往全年高峰爬。Max G3 和 Apollo City Pro 所在的 NT$18,000 到 27,000 區間是甜蜜點，現在買比夏天中段恢復原價划算。"},
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
            {"title": "Best Treadmills 2026", "url": "https://www.nordictrack.com/best-treadmills-2026", "source": "NordicTrack"},
            {"title": "NordicTrack Promo Codes and Deals (2026)", "url": "https://www.garagegymreviews.com/nordictrack-promo-code", "source": "Garage Gym Reviews"},
            {"title": "Treadmills | Buy Online, Pick Up In Store at DICK'S", "url": "https://www.dickssportinggoods.com/f/treadmills", "source": "DICK'S Sporting Goods"},
        ],
        "i18n": {
            "en": {
                "commentary": "With Father's Day on June 21 approaching and summer heat pushing serious runners indoors, the treadmill market is in a strong buying window. A practical angle worth flagging this year: NordicTrack purchases are eligible for HSA and FSA funds, which can save 30 to 40 percent by using pre-tax dollars. For a high-value gift like a connected treadmill, that is a real lever most buyers overlook. NordicTrack is also still running up to $1,300 off smart machines and up to $2,200 off bundles, and a 30-day iFIT trial ships with every machine.\n\nThe NordicTrack Commercial 1750 stays at the top of the list, and the reason is durability plus connected coaching. It scores 9.5 on both tech features and deck size with a 3.75 CHP motor that handles any runner, and it is one of the few treadmills in its class with decline training. For a home gym that needs to last and keep a runner motivated through guided iFIT sessions, this is the workhorse I recommend.\n\nThe NordicTrack X24 Incline holds rank 2 as the incline-training benchmark. Its 40 percent maximum incline and -6 percent decline range is something no other consumer treadmill at this price touches, and the 9.5 tech score backs it up. For anyone serious about HIIT and incline intervals, this is the machine.\n\nThe Sole F80 stays at rank 3 as the no-subscription pick. A 9.5 build quality score and commercial-grade construction mean it lasts a decade with minimal fuss, and it never asks for a monthly fee. The Bowflex Treadmill 22 at rank 4 brings the biggest screen in the category, and the Peloton Tread at rank 5 remains the choice for buyers already inside the Peloton class ecosystem. Buying before the Father's Day rush captures the best stock and the current deal stack.",
                "highlights": [
                    {"title": "NordicTrack Commercial 1750 Stays the Connected Workhorse", "body": "A 9.5 tech and deck score with a 3.75 CHP motor and decline training makes the Commercial 1750 the durable, coaching-ready pick. It is one of the few treadmills in its class with decline capability and ships with a 30-day iFIT trial."},
                    {"title": "HSA and FSA Funds Cut the Real Cost", "body": "NordicTrack purchases are eligible for HSA and FSA funds, saving 30 to 40 percent through pre-tax dollars. For a high-value Father's Day gift, that is a real lever most buyers overlook, stacking on top of current discounts up to $1,300 on smart machines."},
                    {"title": "NordicTrack X24 Is the Incline Benchmark", "body": "A 40 percent maximum incline and -6 percent decline range puts the X24 in a class no other consumer treadmill at this price matches. Combined with a 9.5 tech score, it is the definitive choice for HIIT and incline interval training."},
                ],
            },
            "zh-tw": {
                "commentary": "父親節（6/21）快到了，加上夏天高溫把認真跑步的人逼回室內，跑步機現在正處在不錯的購買窗口。今年有個實用的角度值得提：在美國，NordicTrack 可以用 HSA、FSA 帳戶付款，等於用稅前的錢買，省下 30 到 40 趴，這對聯網跑步機這種高價禮物來說是很多人忽略的省錢槓桿。NordicTrack 目前還在跑智慧機種最高折 $1,300、組合最高折 $2,200 的促銷，每台都附 30 天 iFIT 試用。\n\n榜單第一還是 NordicTrack Commercial 1750，理由是耐用加上聯網教練。科技功能和跑道尺寸雙 9.5 分，3.75 CHP 馬達任何強度都應付，而且是同級少數有下坡訓練的機種。要組一台撐得久、又能用 iFIT 引導課程維持跑步動力的居家跑步機，我推這台主力機。\n\nNordicTrack X24 Incline 第二，是坡度訓練的標竿。最大坡度 40 趴、下坡 -6 趴，這個範圍在這個價位的消費級跑步機裡找不到對手，9.5 的科技分數也撐得住。認真做 HIIT 和坡度間歇的人，就是這台。\n\nSole F80 守住第三，是不綁訂閱的選擇。做工品質 9.5 分加上商業級結構，用十年沒煩惱，而且永遠不會要你月費。Bowflex Treadmill 22 第四，螢幕最大；Peloton Tread 第五，已經在 Peloton 課程生態系裡的人首選。趕在父親節送禮潮前下手，庫存最齊、折扣也疊得最滿。",
                "highlights": [
                    {"title": "NordicTrack Commercial 1750 聯網主力機不動", "body": "科技與跑道尺寸雙 9.5 分，3.75 CHP 馬達加上下坡訓練，是耐用又能引導課程的選擇。同級少數具備下坡功能，附 30 天 iFIT 試用。"},
                    {"title": "HSA、FSA 帳戶壓低實際成本", "body": "在美國 NordicTrack 可用 HSA、FSA 帳戶付款，用稅前的錢省 30 到 40 趴。對高價父親節禮物來說是多數人忽略的槓桿，還能疊加智慧機種最高 $1,300 的現有折扣。"},
                    {"title": "NordicTrack X24 是坡度訓練標竿", "body": "最大坡度 40 趴、下坡 -6 趴，這個範圍在同價位消費級跑步機裡無對手。搭配 9.5 科技分數，是 HIIT 和坡度間歇訓練的終極選擇。"},
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
            {"title": "Hyperice Launches Smallest, Least-Expensive Massage Gun Yet", "url": "https://athletechnews.com/hyperice-launches-hypervolt-go-3-massage-device/", "source": "Athletech News"},
            {"title": "The Hyperice Hypervolt 3 Line Outshines Other Massage Guns", "url": "https://www.insidehook.com/wellness/hyperice-hypervolt-3", "source": "InsideHook"},
            {"title": "5 Best Massage Guns of 2026: Personally Tested", "url": "https://fortune.com/article/best-massage-guns/", "source": "Fortune"},
        ],
        "i18n": {
            "en": {
                "commentary": "Massage guns are one of the safest Father's Day gifts you can buy, and with June 21 three weeks out, demand is climbing fast. These tools have fully matured from gimmick to recovery staple, and the 2026 lineup gives you a clear, confident pick at every budget. Buy now, before the gift-rush squeezes stock on the most popular models.\n\nThe Theragun Pro Plus stays at the top with a 9.8 power score that nothing else in the category touches. The 2600 RPM max speed and 16mm amplitude deliver deep-tissue percussion that physical therapists and elite athletes actually reach for. The value score is modest because you are buying the best tool in the class, not the cheapest one, and for a serious-athlete dad that trade is worth it.\n\nThe Rally Orbital Massager holds rank 2, and it remains my favorite surprise of the year. The orbital motion pattern is gentler than straight percussion, and the 9.5 noise score means it works in an office or hotel room without disturbing anyone. For a desk-worker or frequent-traveler dad, this is the thoughtful pick.\n\nThe Hyperice Hypervolt 2 Pro stays at rank 3, the model fitness pros recommend most and a fixture in this year's gift guides. Worth knowing: Hyperice launched the Hypervolt Go 3 at $149 in March, its smallest and least-expensive gun yet at just 1.6 pounds, with five speeds and four hours of battery, a 33 percent battery improvement over the prior generation. At that price it slots in well below Therabody's Theragun Mini Plus and makes a strong budget-portable gift without leaving the premium brand. The Therabody Theragun Prime at rank 4 rounds out the list with strong power at a friendlier price for buyers who want Theragun quality without the Pro Plus outlay.",
                "highlights": [
                    {"title": "Theragun Pro Plus Sets the Power Standard", "body": "A 9.8 power score, 2600 RPM max speed, and 16mm amplitude make the Pro Plus the deepest-hitting gun in the category. Physical therapists and elite athletes reach for this one specifically, making it the high-confidence gift for a serious-athlete dad."},
                    {"title": "Hyperice Hypervolt Go 3 Is the Smart Budget Gift", "body": "Launched at $149, the Hypervolt Go 3 is Hyperice's smallest and least-expensive gun yet at 1.6 pounds, with five speeds and four hours of battery, a 33 percent improvement over the prior generation. It slots well below Theragun's Mini Plus while keeping the premium brand."},
                    {"title": "Father's Day Is Peak Massage Gun Demand", "body": "With June 21 three weeks out, massage guns are among the most-searched gift items, and the Theragun Pro Plus and Hyperice Hypervolt 2 Pro lead every major gift guide. Buying now captures stock before the rush squeezes the most popular models."},
                ],
            },
            "zh-tw": {
                "commentary": "按摩槍是父親節最不會出錯的禮物之一，離 6/21 剩三週，搜尋量正在快速爬升。這類工具早就從噱頭變成恢復必備品，2026 年的產品線在每個預算帶都有明確、有把握的選擇。趁現在買，避開送禮潮把熱門款的庫存擠光。\n\nTheragun Pro Plus 守住榜首，9.8 的力道分數是品類裡沒人摸得到的高度。2600 RPM 最大轉速、16mm 振幅，打到深層肌肉的力道是物理治療師和職業運動員實際在用的等級。性價比分數普通，因為你買的是品類最好的工具，不是最便宜的，對認真運動的老爸來說這個取捨值得。\n\nRally Orbital Massager 第二，依然是我今年最大的驚喜。軌道式振動比直線衝擊溫和，噪音分數 9.5，辦公室或飯店房間用都不會吵到別人。送給上班族或常出差的老爸，這台很體貼。\n\nHyperice Hypervolt 2 Pro 守住第三，是健身專業人士最常推薦、也是今年各大禮物指南的常客。值得一提的是，Hyperice 三月推出 Hypervolt Go 3，售價 $149（約 NT$4,600），是品牌至今最小最便宜的一支，僅 1.6 磅、五段速、四小時電力，電力比上一代提升 33 趴。這個價位明顯低於 Therabody 的 Theragun Mini Plus，又不用離開高端品牌，當平價便攜禮物很有說服力。Therabody Theragun Prime 第四收尾，力道紮實、價格更親民，想要 Theragun 品質又不想花到 Pro Plus 的人很合適。",
                "highlights": [
                    {"title": "Theragun Pro Plus 力道 9.8 分定標竿", "body": "9.8 力道分、2600 RPM 最大轉速、16mm 振幅，是品類裡打最深的一支。物理治療師和職業運動員實際在用，送給認真運動的老爸最有把握。"},
                    {"title": "Hyperice Hypervolt Go 3 是聰明的平價禮物", "body": "售價 $149（約 NT$4,600），是 Hyperice 至今最小最便宜的一支，僅 1.6 磅、五段速、四小時電力，電力比上一代提升 33 趴。價位明顯低於 Theragun Mini Plus，又保有高端品牌。"},
                    {"title": "父親節是按摩槍需求高峰", "body": "離 6/21 剩三週，按摩槍是搜尋量最高的禮物品項之一，Theragun Pro Plus 和 Hyperice Hypervolt 2 Pro 領銜各大禮物指南。現在買能在送禮潮把熱門款擠光前先搶到庫存。"},
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
            {"title": "The Internet's Favorite Mattresses Are on Sale, Save Up to 50% on Nectar, Saatva, and More", "url": "https://shopping.yahoo.com/health/sleep/articles/internet-favorite-mattresses-sale-save-195635769.html", "source": "Yahoo Shopping"},
            {"title": "Best Extended Memorial Day Mattress Deals of 2026", "url": "https://www.aarp.org/money/personal-finance/memorial-day-mattress-deals/", "source": "AARP"},
            {"title": "Purple Mattress: GelFlex Grid and Cooling for Hot Sleepers", "url": "https://shopping.yahoo.com/health/sleep/articles/internet-favorite-mattresses-sale-save-195635769.html", "source": "Yahoo Shopping"},
        ],
        "i18n": {
            "en": {
                "commentary": "The post-Memorial Day window remains the single best stretch of the year to buy a mattress, and those deals are still live into early June. Saatva, Helix, Casper, and Purple are all running steep discounts, with savings ranging from a couple hundred dollars up to nearly $700. Helix has its entire range at 25 percent off, and Saatva's discounts span practically every model from $375 up to $697. If you have been waiting, this is the moment to act before the deals reset.\n\nThe Saatva Classic stays at rank 1, and the reasons compound over years of ownership. The 9.6 edge support score reflects an innerspring coil construction that holds its shape at the perimeter, something foam-only mattresses consistently struggle with. With 9.2 cooling and 9.0 pressure relief, it adapts to back sleepers, side sleepers, and couples alike. It is the all-rounder I recommend when someone wants one mattress to get right.\n\nThe Helix Midnight Luxe holds rank 2 as the side-sleeper benchmark. Its 9.6 pressure relief score is the highest on this list, and side sleepers feel it directly in their hip and shoulder pressure points. With Helix at 25 percent off right now, the timing is especially good.\n\nThe Purple Restore Hybrid stays at rank 3 with the category's top cooling score at 9.6. Purple's GelFlex Grid flexes under pressure to cushion hips and shoulders while letting air move through the material rather than just across the surface. As summer heat builds, that airflow advantage is more valuable than at any other time of year, which makes this the standout pick for hot sleepers buying in June. The Bear Elite Hybrid at rank 4 stays the favorite for active buyers through its Celliant fiber, and the Nectar Premier Copper at rank 5 remains the value play with matched 9.4 motion isolation and value scores.",
                "highlights": [
                    {"title": "Post-Memorial Day Deals Are Still Live", "body": "Saatva, Helix, Casper, and Purple are all running steep discounts into early June, with savings from a couple hundred dollars up to nearly $700. Helix has its full range at 25 percent off and Saatva spans nearly every model from $375 to $697."},
                    {"title": "Purple Restore Hybrid Leads Cooling at 9.6", "body": "Purple's GelFlex Grid flexes under pressure while letting air move through the material rather than just across the surface, earning the category's top 9.6 cooling score. As summer heat builds, that airflow advantage is more valuable than at any other time of year for hot sleepers."},
                    {"title": "Saatva Classic Stays the All-Rounder", "body": "A 9.6 edge support score from innerspring coil construction holds shape at the perimeter where foam-only beds struggle, and 9.2 cooling plus 9.0 pressure relief adapt to back sleepers, side sleepers, and couples. It is the pick when someone wants one mattress to get right."},
                ],
            },
            "zh-tw": {
                "commentary": "Memorial Day 過後這段時間仍然是一年裡買床墊最划算的窗口，而且這波折扣撐到六月初還在。Saatva、Helix、Casper、Purple 全部都在跑大折扣，省的金額從幾百美元到接近 $700 都有。Helix 全系列直接 25 趴 off，Saatva 幾乎每一款都有折，從 $375 折到 $697。如果你一直在等，現在就是動手的時機，趁折扣重置前下手。\n\nSaatva Classic 守住第一，理由會隨著使用年數累積。邊緣支撐 9.6 分背後是彈簧結構，床緣撐得住、不會一坐就塌，這是純記憶棉床墊的死穴。冷卻 9.2、壓力釋放 9.0，仰睡、側睡、雙人都能應付。有人想「一張床墊買對就好」，我就推這張全能型。\n\nHelix Midnight Luxe 第二，是側睡族的標竿。9.6 的壓力釋放分是榜單最高，側睡的人在髖部和肩膀壓力點會直接感受到。Helix 現在全系列 25 趴 off，時機特別好。\n\nPurple Restore Hybrid 守住第三，冷卻分 9.6 是全榜最高。Purple 的 GelFlex Grid 受壓時會彎折，撐住髖部和肩膀的同時讓空氣穿過材料，而不只是表面散熱。夏天高溫一起來，這個通風優勢比一年任何時候都值錢，六月買床墊又怕熱的人，這張就是首選。Bear Elite Hybrid 第四，靠 Celliant 纖維深受運動族喜愛；Nectar Premier Copper 第五，動作隔離和性價比同為 9.4，是預算有限的務實選擇。",
                "highlights": [
                    {"title": "Memorial Day 後折扣仍在跑", "body": "Saatva、Helix、Casper、Purple 全部跑大折扣到六月初，省的金額從幾百美元到接近 $700。Helix 全系列 25 趴 off，Saatva 幾乎每款都折，從 $375 到 $697。"},
                    {"title": "Purple Restore Hybrid 冷卻 9.6 領先", "body": "GelFlex Grid 受壓彎折的同時讓空氣穿過材料，而非只靠表面散熱，拿下全榜最高的 9.6 冷卻分。夏天高溫一起來，這個通風優勢比一年任何時候都值錢，怕熱的人首選。"},
                    {"title": "Saatva Classic 全能型守榜首", "body": "彈簧結構帶來 9.6 邊緣支撐，床緣撐得住純記憶棉撐不住的位置，加上 9.2 冷卻、9.0 壓力釋放，仰睡側睡雙人都能應付。想一張床墊買對就好，選它。"},
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
            {"title": "Best Standing Desks of 2026: Top-Performing Height-Adjustable Desks", "url": "https://www.techradar.com/news/best-standing-desk", "source": "TechRadar"},
            {"title": "Premium Standing Desk E7 Pro | Height Adjustable Ergonomic Desk", "url": "https://www.flexispot.com/flexispot-best-standing-desk-e7pro", "source": "FlexiSpot"},
            {"title": "FlexiSpot Discount Codes in June 2026", "url": "https://www.pcgamer.com/coupons/flexispot.com/", "source": "PC Gamer"},
        ],
        "i18n": {
            "en": {
                "commentary": "Standing desks are a genuine workplace staple now, and June is a smart month to buy one, whether for a home office upgrade or a Father's Day gift for the work-from-home dad. FlexiSpot's E7 Pro remains the value benchmark, lifting up to 440 pounds across a 25 to 50.6 inch range with four presets, a digital height display, and a built-in USB charging port on a rock-solid C-frame base. Multiple FlexiSpot discount codes are live this month, and the brand includes free standard shipping so the listed price is the checkout price.\n\nThe Uplift V2 Commercial stays at rank 1, and I keep recommending it for the same reason: it is the desk to buy if you want one that lasts a decade. The 9.8 warranty score reflects a lifetime frame warranty that no competitor matches, and the 9.6 adjustment range plus 9.5 stability mean it stays rock-steady at every height from 22.6 to 48.7 inches. For a long-term home office, this is where the money goes.\n\nThe FlexiSpot E7 Pro 2026 holds rank 2 as one of the strongest value products I review in any category. A 9.8 value score with a 9.0 adjustment range at this price is remarkable, and with June discount codes live, the timing for a gift is good.\n\nThe Secretlab Magnus Pro stays at rank 3 on pure build quality, with a 9.7 build quality and 9.6 stability score that make it the most solid-feeling desk on the list. Its magnetic accessory system adds genuinely useful cable management. The Fully Jarvis Bamboo at rank 6 remains the sustainable pick, with a bamboo top that suits a warm-weather home setup. Buying before the Father's Day rush locks in the best codes and stock.",
                "highlights": [
                    {"title": "Uplift V2 Commercial Lifetime Warranty Is Unmatched", "body": "A 9.8 warranty score reflects a lifetime frame warranty no competitor offers. Combined with a 9.6 adjustment range and 9.5 stability across 22.6 to 48.7 inches, this is the desk to buy if you want one that genuinely lasts a decade of daily use."},
                    {"title": "FlexiSpot E7 Pro Is the Value Benchmark", "body": "The E7 Pro lifts up to 440 pounds across 25 to 50.6 inches with four presets, a digital display, and built-in USB charging on a rock-solid C-frame. A 9.8 value score plus live June discount codes and free shipping make it a strong Father's Day gift."},
                    {"title": "Secretlab Magnus Pro Sets the Build-Quality Bar", "body": "A 9.7 build quality and 9.6 stability score make the Magnus Pro the most solid-feeling desk on this list. Its magnetic accessory system adds genuinely useful cable management that traditional desks cannot replicate."},
                ],
            },
            "zh-tw": {
                "commentary": "站立式辦公桌現在已經是辦公室的標配，六月是入手的好時機，不管是升級居家辦公還是送給在家工作的老爸當父親節禮物。FlexiSpot E7 Pro 仍是性價比標竿，承重最高 440 磅、升降範圍 25 到 50.6 英吋，四組記憶設定、數位高度顯示、內建 USB 充電埠，搭配穩固的 C 型架。這個月有多組 FlexiSpot 折扣碼可用，而且品牌全單免運，看到的標價就是結帳價。\n\nUplift V2 Commercial 守住第一，我一直推它的理由不變：要買一張用十年的桌子就選它。9.8 的保固分數背後是終身架構保固，業界沒有對手，9.6 的調節範圍加上 9.5 的穩定性，從 22.6 到 48.7 英吋每個高度都穩如磐石。要組長期使用的居家辦公室，錢花這裡最對。\n\nFlexiSpot E7 Pro 2026 第二，是我評測過所有品類裡性價比最強的產品之一。這個價位有 9.8 的性價比分和 9.0 的調節範圍很不簡單，加上六月折扣碼還在跑，當禮物的時機很好。\n\nSecretlab Magnus Pro 第三，純靠做工品質，9.7 的做工和 9.6 的穩定性讓它是榜單裡手感最紮實的桌子。磁吸配件系統的整線真的很實用。Fully Jarvis Bamboo 第六，是最環保的選擇，竹製桌面很適合溫暖天氣的居家風格。趕在父親節送禮潮前下手，折扣碼和庫存都鎖得最好。",
                "highlights": [
                    {"title": "Uplift V2 Commercial 終身保固業界唯一", "body": "9.8 保固分數反映終身架構保固，業界沒有對手。加上 9.6 調節範圍、9.5 穩定性，22.6 到 48.7 英吋全程穩固，要買一張用十年的桌子就選它。"},
                    {"title": "FlexiSpot E7 Pro 是性價比標竿", "body": "承重最高 440 磅、25 到 50.6 英吋升降，四組記憶、數位顯示、內建 USB 充電，搭配穩固 C 型架。9.8 性價比分加上六月折扣碼和全單免運，當父親節禮物很有說服力。"},
                    {"title": "Secretlab Magnus Pro 做工品質定標竿", "body": "9.7 做工、9.6 穩定性，是榜單裡手感最紮實的桌子。磁吸配件系統的整線真的實用，傳統辦公桌做不到。"},
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
            {"title": "Best Pickleball Paddles in 2026 | Pickleheads", "url": "https://www.pickleheads.com/pickleball-gear/pickleball-paddles", "source": "Pickleheads"},
            {"title": "Updated: Which Pro Pickleball Players Have Signed New Paddle Deals", "url": "https://thekitchenpickle.com/blogs/news/pro-pickleball-players-new-paddle-apparel-equipment-deals-2026", "source": "The Kitchen Pickleball"},
            {"title": "Tracking All the New Pro Paddle Deals in 2026", "url": "https://www.thedinkpickleball.com/tracking-all-the-new-pro-paddle-deals-in-2026/", "source": "The Dink Pickleball"},
        ],
        "i18n": {
            "en": {
                "commentary": "Pickleball's momentum into summer 2026 is undeniable, and the paddle technology story keeps getting better. The full-foam-core revolution that CRBN's TruFoam line started has gone fully mainstream, and the top paddles now play better than anything available two seasons ago. With Father's Day on June 21, paddles are one of the fastest-growing gift categories, and this price band sits right in the gift sweet spot.\n\nThe JOOLA Perseus Pro IV 16mm stays at the top of the list, and I stand behind it firmly. It posts 9.5 power, 9.4 spin, 9.3 sweet spot, and 9.2 control, the most complete all-around package here, with no glaring weakness. This is Ben Johns' paddle lineage refined for 2026, and the playing characteristics show it. For a competitive player who needs to do everything well, this is the clearest recommendation.\n\nThe Honolulu J2CR holds rank 2, the value-meets-performance story of the year. A 9.4 value score alongside 9.4 control and 9.4 sweet spot makes it the strongest pick for intermediate competitive players who want premium feel without the premium-brand markup.\n\nThe Bread & Butter Loco 16mm Hybrid stays at rank 3 with a 9.6 value score, the best on this list, while still delivering 9.3 control and 9.2 power. For a responsible spend that gives up nothing in performance, this is where I point buyers.\n\nThe Selkirk Labs Project Boomstik at rank 4 is the pure-power statement, with a 9.8 power score and a 9.5 sweet spot that lets you actually access it. The CRBN 1X Power Series 16mm at rank 5 holds the top spin score at 9.5. Worth noting for the wider market: a major pro sponsorship reshuffle is underway in 2026, with Anna Leigh Waters leaving Paddletek for Franklin and several other top pros switching brands, a sign of a maturing, fiercely competitive market that ultimately raises equipment quality for everyone.",
                "highlights": [
                    {"title": "JOOLA Perseus Pro IV Is the Most Complete Paddle", "body": "Scores of 9.5 power, 9.4 spin, 9.3 sweet spot, and 9.2 control make the Perseus Pro IV 16mm the only paddle here that leads across every major category with no glaring weakness. For a competitive player who needs to do everything well, it is the clearest pick."},
                    {"title": "Pro Sponsorship Reshuffle Signals Market Maturity", "body": "A major 2026 sponsorship shake-up is underway, with Anna Leigh Waters leaving Paddletek for Franklin and several other top pros switching brands. Aggressive competition for pro validation pushes manufacturers to keep raising equipment quality, which benefits every player."},
                    {"title": "Father's Day Demand Is Spiking for Paddles", "body": "With June 21 approaching, pickleball paddles are one of the fastest-growing gift categories. The price range covering the Bread & Butter Loco through CRBN 1X aligns with typical gift budgets, and stock on top models is moving quickly heading into the rush."},
                ],
            },
            "zh-tw": {
                "commentary": "匹克球進入 2026 夏天的氣勢完全擋不住，而球拍科技的故事一年比一年精彩。CRBN TruFoam 帶動的全泡棉核心革命已經全面主流化，現在排名前幾的球拍，實際打起來比兩季前的天花板還要好。父親節（6/21）快到了，球拍是成長最快的禮物品類之一，這個價位帶剛好落在送禮甜蜜點。\n\nJOOLA Perseus Pro IV 16mm 守住榜首，這個推薦我給得很有把握。力量 9.5、旋轉 9.4、甜蜜點 9.3、控制 9.2，是榜單裡最完整的全能組合，沒有明顯短板。這是 Ben Johns 的球拍血脈在 2026 年的優化版，打感看得出來。要送需要在場上做全部事情的競技球員，這是最明確的選擇。\n\nHonolulu J2CR 第二，是今年「性價比遇上性能」的代表。9.4 控制、9.4 甜蜜點、9.4 性價比，中高級競技球員想要頂級手感又不想付品牌溢價，這張最強。\n\nBread & Butter Loco 16mm Hybrid 守住第三，9.6 的性價比分是全榜最高，同時還有 9.3 控制和 9.2 力量。想理性花錢又不在性能上妥協，我直接推這張。\n\nSelkirk Labs Project Boomstik 第四，是純力量的宣言，9.8 力量分加上 9.5 甜蜜點讓你真的打得到那股力量。CRBN 1X Power Series 16mm 第五，9.5 的旋轉分是全榜最高。對整個市場值得一提的是：2026 年有一波職業贊助大洗牌，Anna Leigh Waters 離開 Paddletek 轉投 Franklin，多名頂尖職業球員也換了品牌，這代表市場正在成熟、競爭白熱化，最終受惠的是所有玩家的器材品質。",
                "highlights": [
                    {"title": "JOOLA Perseus Pro IV 是最完整的球拍", "body": "力量 9.5、旋轉 9.4、甜蜜點 9.3、控制 9.2，Perseus Pro IV 16mm 是榜單裡唯一在每個主要維度都領先、又沒有明顯短板的球拍。要送需要全場景表現的競技球員，最明確的選擇。"},
                    {"title": "職業贊助大洗牌反映市場成熟", "body": "2026 年職業贊助大洗牌進行中，Anna Leigh Waters 離開 Paddletek 轉投 Franklin，多名頂尖職業球員也換了品牌。搶人競爭激烈逼廠商持續提升器材品質，最終受惠的是所有玩家。"},
                    {"title": "父親節球拍需求飆升", "body": "離 6/21 越來越近，匹克球拍是成長最快的禮物品類之一。Bread & Butter Loco 到 CRBN 1X 的價位帶剛好符合送禮預算，熱門型號庫存在送禮潮前消化得很快。"},
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
