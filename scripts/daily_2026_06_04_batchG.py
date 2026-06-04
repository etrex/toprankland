import sys
sys.path.insert(0, "/Users/etrexkuo/toprankland/scripts")
from daily_helper import load, save, upsert, last_rankings, DATE

entries = {}

# ----------------------------------------------------------------------------
# best-portable-chargers.json
# ----------------------------------------------------------------------------
entries["best-portable-chargers.json"] = {
    "references": [
        {"title": "Best Power Bank 2026: 5 New Chargers That Raised the Bar", "url": "https://the-gadgeteer.com/2026/05/06/best-power-bank-2026-five-new-chargers/", "source": "The Gadgeteer"},
        {"title": "The best power banks and portable chargers for every device in 2026", "url": "https://www.engadget.com/computing/accessories/best-power-bank-143048526.html", "source": "Engadget"},
    ],
    "en": {
        "commentary": "Heading into June 2026 the Anker Prime 26K 300W stays my number one, and nothing this week gives me a reason to move it. It still does the rare thing of running a 16 inch MacBook Pro at full speed from a brick that fits a jacket pocket, 26,250mAh and 300W across two USB-C and one USB-A, with a 250W dual port input that puts roughly half the charge back in about 13 minutes. The interesting story right now is the wave of semi solid state pocket banks arriving in titanium shells with Qi2 wireless, the first real safety and density shift in this category in over a decade. I am watching those closely, but until I have field reliability data they stay off the podium and my proven leaders hold. The Prime 27650 250W keeps second for buyers who value reserve capacity over peak wattage, and Ugreen's Nexode 25000mAh remains the value heavyweight that delivers genuine laptop charging for clearly less money. For phone first carry, the Anker Nano 10K with its built in cable and the MagGo 10K Qi2 are still the easy picks that disappear into everyday bags, while the Baseus PicoGo and Belkin BoostCharge Pro cover magnetic Qi2 for iPhone owners who want to drop cables entirely. The INIU 20000mAh 45W stays the budget hero on value. The list is specialization by design, so match the brick to how you actually charge and you will not go wrong.",
        "highlights": [
            {"title": "Anker Prime 26K 300W still leads", "body": "It runs a 16 inch MacBook Pro at full speed from a pocketable 26,250mAh brick pushing 300W across three ports, and its 250W input refills roughly half in about 13 minutes. For laptop carriers it remains the one to buy."},
            {"title": "Semi solid state banks are the trend to watch", "body": "New pocket banks with titanium shells, semi solid state cells and Qi2 wireless are landing in 2026, the biggest density and safety shift in years. I want field reliability before ranking them, so proven units hold the podium for now."},
            {"title": "Ugreen Nexode 25000mAh is the value heavyweight", "body": "It delivers real laptop capable capacity and high wattage output for noticeably less than the Prime tier. If you want to power a laptop on the go without flagship pricing, this is the smart buy."},
        ],
    },
    "zh-tw": {
        "commentary": "進入 2026 年 6 月，Anker Prime 26K 300W 還是我的第一名，這週也沒有任何消息讓我想動它。它做到一件很難的事，用一個塞得進外套口袋的磚塊，就能讓 16 吋 MacBook Pro 全速充電，26,250mAh、兩個 USB-C 加一個 USB-A 合計 300W，配上 250W 雙孔輸入，大約 13 分鐘就能充回一半。現在比較有看頭的是一波半固態電芯的口袋行充，鈦合金外殼加 Qi2 無線，這是這個品類十幾年來第一次在安全跟密度上真的有突破。我會盯著看，但在還沒有實測的長期可靠度數據之前，它們先不上頒獎台，我這幾台久經考驗的還是穩坐前段。Prime 27650 250W 守住第二，適合重視電量儲備勝過最高瓦數的人，Ugreen Nexode 25000mAh 還是性價比重量級，能餵筆電卻便宜一截。手機族日常帶出門，Anker Nano 10K 內建線材跟 MagGo 10K Qi2 還是好推薦，塞進通勤包就不見了，Baseus PicoGo 跟 Belkin BoostCharge Pro 則服務想完全擺脫線材的 iPhone 磁吸 Qi2 族群。INIU 20000mAh 45W 還是預算族的性價比英雄。這份清單本來就是按用途分工，看你實際怎麼充來配，就不會選錯。",
        "highlights": [
            {"title": "Anker Prime 26K 300W 還是領頭羊", "body": "用可放口袋的 26,250mAh 磚塊讓 16 吋 MacBook Pro 全速跑，三孔合計 300W，250W 輸入約 13 分鐘充回一半。帶筆電的人，這台依然是首選。"},
            {"title": "半固態行充是值得盯的趨勢", "body": "2026 年出現一批鈦合金外殼、半固態電芯加 Qi2 無線的口袋行充，是近年最大的密度跟安全突破。我想先看實測長期可靠度再排名，所以目前頒獎台還是給久經考驗的機型。"},
            {"title": "Ugreen Nexode 25000mAh 是性價比重量級", "body": "能餵筆電的容量跟高瓦數輸出，價格卻比 Prime 等級便宜明顯一截。想在外面充筆電又不想花旗艦價，這台最聰明。"},
        ],
    },
}

# ----------------------------------------------------------------------------
# best-portable-power-stations.json
# ----------------------------------------------------------------------------
entries["best-portable-power-stations.json"] = {
    "references": [
        {"title": "The Best Portable Power Stations of 2026, Tested by GearJunkie", "url": "https://gearjunkie.com/technology/best-portable-power-stations", "source": "GearJunkie"},
        {"title": "EcoFlow vs. Jackery vs. Bluetti vs. Anker Solix: Which Solar Generator", "url": "https://powergenstore.com/blogs/news/ecoflow-vs-jackery-vs-bluetti-vs-anker-solix-which-solar-generator-is-best", "source": "PowerGen Store"},
    ],
    "en": {
        "commentary": "My ranking holds steady this first week of June 2026, and the EcoFlow Delta 3 Plus keeps the top spot for the same reason it earned it, it is the most well rounded mid size station you can buy. EcoFlow remains the industry leader in software and smart home integration, and that ecosystem edge, smart panels and EV to home interfaces, is exactly what keeps it ahead when the raw battery specs across brands have largely converged on LiFePO4. The Bluetti Elite 200 V2 stays second because it does the practical things right, it charges faster from the wall than comparable models and takes up less space, which is what most camping and home backup buyers actually feel. Anker's Solix C2000 Gen2 holds third as the dependable all rounder, and the Delta Pro 3 remains the pick when you need serious capacity and 240V capable output for whole home backup. The notable launch worth flagging is Anker's Solix C300 DC at $249, which drops AC entirely to stay light and USB focused, a smart niche play for campers who only charge phones, laptops and small gear. It does not change my main list, which is built around versatile AC stations, but it is the kind of specialization I expect more of this year. For most buyers the Delta 3 Plus remains the confident default.",
        "highlights": [
            {"title": "EcoFlow Delta 3 Plus stays the all rounder to beat", "body": "Its software and smart home integration lead the field, with smart panel and EV to home support that rivals cannot match. With battery chemistry converged on LiFePO4 across brands, that ecosystem edge is what keeps it at number one."},
            {"title": "Bluetti Elite 200 V2 wins on practical speed", "body": "It charges faster from the wall than comparable units and takes up less space, which is what camping and home backup buyers feel day to day. That real world convenience keeps it firmly in second."},
            {"title": "Anker Solix C300 DC is the niche launch to note", "body": "At $249 it ditches AC to stay light and USB focused, a smart pick for campers charging only phones, laptops and small gear. It does not reorder the AC station list but signals more specialization this year."},
        ],
    },
    "zh-tw": {
        "commentary": "6 月第一週我的排名穩住，EcoFlow Delta 3 Plus 守住冠軍，理由跟當初一樣，它是現在最全能的中型電源站。EcoFlow 在軟體跟智慧家庭整合上還是業界第一，這個生態系優勢，智慧電盤、電動車對家供電介面，正是在各品牌電芯規格大多都收斂到 LiFePO4 之後，它還能領先的關鍵。Bluetti Elite 200 V2 排第二，因為它把實用的事做對了，市電充電比同級快，體積又更小，這正是大多數露營跟居家備電的人實際感受到的。Anker Solix C2000 Gen2 守第三，當可靠的全能選手，Delta Pro 3 則是需要大容量加 240V 輸出做全屋備電時的首選。值得一提的新品是 Anker Solix C300 DC，售價 249 美元，乾脆拿掉 AC 輸出，專攻輕量跟 USB，這是聰明的利基打法，給只充手機、筆電跟小裝備的露營族。它沒有動到我主清單，因為主清單是以全能 AC 電源站為主，但這種專業分工我預期今年會更多。對大多數人來說，Delta 3 Plus 還是最有底氣的預設選擇。",
        "highlights": [
            {"title": "EcoFlow Delta 3 Plus 還是全能標竿", "body": "軟體跟智慧家庭整合領先全場，智慧電盤跟電動車對家供電的支援是對手追不上的。在各品牌電芯都收斂到 LiFePO4 之後，這個生態系優勢就是它穩坐第一的原因。"},
            {"title": "Bluetti Elite 200 V2 贏在實用充電速度", "body": "市電充電比同級快，體積又更小，這是露營跟居家備電的人每天真正感受到的。這種實戰便利讓它穩坐第二。"},
            {"title": "Anker Solix C300 DC 是值得注意的利基新品", "body": "售價 249 美元，拿掉 AC 專攻輕量跟 USB，適合只充手機、筆電跟小裝備的露營族。它沒有動到 AC 電源站清單，卻預告今年會有更多專業分工。"},
        ],
    },
}

# ----------------------------------------------------------------------------
# best-electric-bikes.json
# ----------------------------------------------------------------------------
entries["best-electric-bikes.json"] = {
    "references": [
        {"title": "Best Electric Bikes 2026 - Don't Buy Until You Read This", "url": "https://electricbikereport.com/best-electric-bikes/", "source": "Electric Bike Report"},
        {"title": "2026 Aventon Current ADV Review: $5,999 Carbon Fiber eMTB", "url": "https://freshlycharged.com/reviews/395/2026-aventon-current-adv-review", "source": "Freshly Charged"},
    ],
    "en": {
        "commentary": "My top of June 2026 e-bike order stands, and the Aventon Level 3 keeps the crown as the smartest commuter you can buy right now. Aventon's integrated ACU module with 4G connectivity is the reason, it lets you manage security, speed settings and motor output from the app, and that connected layer is where the category is genuinely advancing in 2026. The Lectric XP4 750 holds second as the people's champ, a folding go anywhere bike with the practical features and aggressive price that keep it the easiest recommendation for new riders. Velotric Discover 3 stays third on comfort and a balanced ride, and the Segway xyber and the rest of the field hold their positions. The headline this week is Aventon's Current ADV, a $5,999 carbon fiber eMTB with 120Nm of torque from the Ultra X mid drive and RockShox suspension. It is a serious trail machine and a sign of where Aventon's ambition is heading, but at that price and purpose it sits outside my commuter and value focused list rather than reordering it. For everyday riders who want range, comfort and genuinely useful smart features, the Level 3 remains my confident pick, with the XP4 the value answer right behind it.",
        "highlights": [
            {"title": "Aventon Level 3 stays the smartest commuter", "body": "Its integrated ACU module with 4G lets you control security, speed and motor output from the app, and that connected layer is where 2026 e-bikes are advancing. For everyday riders it remains the top pick."},
            {"title": "Lectric XP4 750 is still the people's champ", "body": "A folding, go anywhere bike with practical features and an aggressive price, it is the easiest recommendation for new riders. Solid range and power keep it firmly in second."},
            {"title": "Aventon Current ADV signals bigger ambition", "body": "The new $5,999 carbon fiber eMTB packs 120Nm from the Ultra X mid drive and RockShox suspension. It is a serious trail machine but sits outside the commuter and value list rather than reordering it."},
        ],
    },
    "zh-tw": {
        "commentary": "2026 年 6 月初我的電輔車排名站穩，Aventon Level 3 守住冠軍，是現在最聰明的通勤電輔車。關鍵就是 Aventon 內建的 ACU 模組加 4G 連線，讓你直接用 App 管理防盜、速度設定跟馬達輸出，而這個連網層正是 2026 年這個品類真正在進步的地方。Lectric XP4 750 排第二，當之無愧的庶民冠軍，可折疊、哪都能騎，實用配備加上殺很大的價格，對新手來說最好推薦。Velotric Discover 3 守第三，靠舒適跟均衡的騎乘感，Segway xyber 跟其他車款也守住位置。這週的頭條是 Aventon 的 Current ADV，一台要價 5,999 美元的碳纖維電動登山車，Ultra X 中置馬達給到 120Nm 扭力，配 RockShox 避震。這是認真的越野機器，也看得出 Aventon 的野心往哪走，但以這個價格跟定位，它在我這份以通勤跟性價比為主的清單之外，不會動到排名。對想要續航、舒適跟真正好用智慧功能的日常騎士，Level 3 還是我有底氣的首選，XP4 則是緊跟在後的性價比解答。",
        "highlights": [
            {"title": "Aventon Level 3 還是最聰明的通勤車", "body": "內建 ACU 模組加 4G，能用 App 控防盜、速度跟馬達輸出，這個連網層正是 2026 電輔車進步的方向。對日常騎士來說仍是首選。"},
            {"title": "Lectric XP4 750 還是庶民冠軍", "body": "可折疊、哪都能騎，實用配備加殺很大的價格，對新手最好推薦。續航跟動力夠扎實，穩坐第二。"},
            {"title": "Aventon Current ADV 透露更大野心", "body": "全新 5,999 美元碳纖維電動登山車，Ultra X 中置馬達 120Nm 加 RockShox 避震。是認真的越野機器，但落在通勤與性價比清單之外，不動排名。"},
        ],
    },
}

# ----------------------------------------------------------------------------
# best-electric-scooters.json
# ----------------------------------------------------------------------------
entries["best-electric-scooters.json"] = {
    "references": [
        {"title": "Segway Ninebot Max G3 Electric Scooter Review In 2026", "url": "https://www.voltridehub.com/segway-ninebot-max-g3-review/", "source": "VoltRideHub"},
        {"title": "Segway MAX G3 Premium Performance eKickscooter", "url": "https://store.segway.com/ninebot-kickscooter-max-g3", "source": "Segway"},
    ],
    "en": {
        "commentary": "The Segway Ninebot Max G3 holds my number one spot into June 2026, and the reviews this season only reinforce why, it is the set it and forget it commuter that remains the standard to beat. It pairs a 2000W peak motor, a 28 mph top speed and up to 50 miles of range with the kind of reliability that built the Max line's reputation. The features are where it pulls ahead, dual hydraulic damped suspension front and rear, the SegRide stability system, 11 inch self sealing tires with Dynamic Traction Control and an anti lock braking system, plus a built in 3A fast charger that finally kills the bulky external brick. That traction control genuinely matters for riders crossing wet manhole covers and painted lines, and it is the kind of safety upgrade I weight heavily. The Apollo City Pro keeps second as the premium ride quality pick, and the Niu KQi3 Pro holds third as the value commuter that punches above its price. Nothing in the last week reorders the field, the G3 simply remains the most complete commuter scooter you can buy, and for most riders who want range, safety and zero fuss, it is the easy recommendation.",
        "highlights": [
            {"title": "Segway Max G3 is the set and forget commuter", "body": "A 2000W peak motor, 28 mph top speed and up to 50 miles of range meet the reliability the Max line is known for. It remains the standard to beat in 2026."},
            {"title": "Traction control is the safety upgrade that matters", "body": "Dynamic Traction Control and an anti lock braking system keep the G3 planted on wet manhole covers and painted lines. Combined with dual hydraulic suspension, it is the most confident ride in the class."},
            {"title": "Built in fast charger ends the brick", "body": "An internal 3A fast charger means no more bulky external power brick to carry or lose. It is a small thing that makes daily ownership noticeably cleaner."},
        ],
    },
    "zh-tw": {
        "commentary": "Segway Ninebot Max G3 守住我 2026 年 6 月的第一名，這季的評測只是更印證了原因，它就是那種設定好就不用管的通勤車，仍是大家要超越的標竿。它把 2000W 峰值馬達、最高時速約 45 公里、續航最多約 80 公里，跟撐起整個 Max 系列名聲的可靠度綁在一起。真正拉開差距的是它的配備，前後雙液壓阻尼避震、SegRide 穩定系統、11 吋自我修補輪胎加上動態循跡控制跟防鎖死煞車，還有內建 3A 快充，終於擺脫那塊笨重的外接充電磚。那個循跡控制對台灣機車族很有感，過濕滑的人孔蓋跟路面標線時特別實在，這種安全升級我看得很重。Apollo City Pro 守第二，當高級騎乘質感的選擇，Niu KQi3 Pro 守第三，是越級打怪的性價比通勤車。過去一週沒有消息動到排名，G3 就是現在最完整的通勤滑板車，對大多數想要續航、安全又不想煩惱的人，它最好推薦。",
        "highlights": [
            {"title": "Segway Max G3 是設定好就不用管的通勤車", "body": "2000W 峰值馬達、最高時速約 45 公里、續航最多約 80 公里，加上 Max 系列著稱的可靠度。它仍是 2026 年要被超越的標竿。"},
            {"title": "循跡控制是最有感的安全升級", "body": "動態循跡控制加防鎖死煞車，讓 G3 過濕滑人孔蓋跟路面標線時穩穩抓地。配上前後雙液壓避震，是同級最有信心的騎乘。"},
            {"title": "內建快充終結充電磚", "body": "內建 3A 快充代表不用再帶那塊笨重的外接電源磚，也不怕弄丟。小細節卻讓每天用起來明顯清爽。"},
        ],
    },
}

# ----------------------------------------------------------------------------
# best-dash-cams.json
# ----------------------------------------------------------------------------
entries["best-dash-cams.json"] = {
    "references": [
        {"title": "The Viofo A329S is an outstanding dash cam with fantastic video quality", "url": "https://www.tomsguide.com/vehicle-tech/the-viofo-a329s-is-an-outstanding-dash-cam-with-fantastic-video-quality-but-the-price-is-a-big-hurdle", "source": "Tom's Guide"},
        {"title": "I've reviewed over 15 dash cams, and Viofo's A329 is the best of the bunch", "url": "https://www.techradar.com/vehicle-tech/dash-cams/ive-reviewed-over-15-dash-cams-this-last-year-and-viofos-a329-is-the-best-of-the-bunch-heres-why", "source": "TechRadar"},
    ],
    "en": {
        "commentary": "The Viofo A329S stays my top dash cam into June 2026, and the latest reviews land exactly where I do, it delivers the most natural looking footage day and night and the best in cabin image in its class. The hardware is the reason, a 4K 60fps front camera with Sony Starvis 2 sensors and HDR, paired with a 2K rear and a 210 degree cabin view, plus Wi-Fi 6 for genuinely fast offloads. Reviewers keep flagging the same single caveat, the three channel version at $499.99 is a real price hurdle, but Viofo offers dual and single channel versions at $429.99 and $359.99 for drivers who do not need all three feeds. If image quality is your priority, this is the buy. The Vantrue N4 Pro S holds second and runs the A329S close, it looks slightly brighter at night, which suits drivers who weight low light heavily. BlackVue Elite 9 keeps third for its parking mode and cloud ecosystem, and Thinkware U3000 holds its spot. Nothing this week reorders the list, the A329S is simply the most capable dash cam you can buy right now, and unless the price genuinely stings, it is my confident pick.",
        "highlights": [
            {"title": "Viofo A329S has the best image in its class", "body": "A 4K 60fps front camera with Sony Starvis 2 sensors and HDR delivers the most natural day and night footage, and its cabin view is the best around. Wi-Fi 6 makes offloading clips genuinely fast."},
            {"title": "Price is the one real caveat", "body": "The three channel A329S is $499.99, which reviewers flag as a hurdle. Viofo offers dual and single channel versions at $429.99 and $359.99 for drivers who do not need every feed."},
            {"title": "Vantrue N4 Pro S runs it close at night", "body": "It looks slightly brighter than the A329S after dark, which suits drivers who weight low light performance heavily. That keeps it a strong second and the alternative worth considering."},
        ],
    },
    "zh-tw": {
        "commentary": "Viofo A329S 守住我 2026 年 6 月的行車記錄器冠軍，最新評測的結論跟我一樣，它日夜畫面都最自然，車內鏡頭畫質也是同級最好。硬體是主因，前鏡頭 4K 60fps 配 Sony Starvis 2 感光元件加 HDR，搭 2K 後鏡頭跟 210 度車內視角，還有 Wi-Fi 6 讓備份檔案真的快。評測一直點出同一個唯一缺點，三鏡頭版要 499.99 美元，價格確實是門檻，但 Viofo 也有雙鏡頭跟單鏡頭版，分別 429.99 跟 359.99 美元，給不需要三路畫面的車主。如果你最在意畫質，就是這台。Vantrue N4 Pro S 守第二，咬得很緊，夜間看起來稍亮一點，適合特別重視低光的車主。BlackVue Elite 9 守第三，靠停車模式跟雲端生態系，Thinkware U3000 也守住位置。這週沒有消息動排名，A329S 就是現在最能打的行車記錄器，只要價格不會讓你太心痛，它就是我有底氣的首選。",
        "highlights": [
            {"title": "Viofo A329S 同級畫質最好", "body": "前鏡頭 4K 60fps 配 Sony Starvis 2 感光元件加 HDR，日夜畫面最自然，車內視角也是同級最佳。Wi-Fi 6 讓備份影片真的快。"},
            {"title": "價格是唯一真缺點", "body": "三鏡頭 A329S 要 499.99 美元，評測都點名是門檻。Viofo 也提供雙鏡頭跟單鏡頭版，429.99 跟 359.99 美元，給不需要每路畫面的車主。"},
            {"title": "Vantrue N4 Pro S 夜間咬得很緊", "body": "入夜後看起來比 A329S 稍亮，適合特別重視低光表現的車主。這讓它穩坐第二，是值得考慮的替代選擇。"},
        ],
    },
}

# ----------------------------------------------------------------------------
# best-3d-printers.json
# ----------------------------------------------------------------------------
entries["best-3d-printers.json"] = {
    "references": [
        {"title": "Bambu Lab P2S review: Refreshing a best seller", "url": "https://www.tomshardware.com/3d-printing/bambu-lab-p2s-review", "source": "Tom's Hardware"},
        {"title": "The Best 3D Printers for Home, Workshop or Business in 2026", "url": "https://www.tomshardware.com/best-picks/best-3d-printers", "source": "Tom's Hardware"},
    ],
    "en": {
        "commentary": "The Bambu Lab P2S Combo holds my number one into June 2026, and Tom's Hardware's review confirms exactly why, it refreshes a best seller without breaking the formula. The P2S keeps everything that made the P1S the default workshop printer and adds a 5 inch color touchscreen, AI powered error detection that catches spaghetti, nozzle clumping and purge jams, a 50C actively regulated chamber, a 300C nozzle, a 70 percent stronger extruder and quieter operation. The decisive part is the price, $549 standalone and $799 for the combo, only $50 more than the machine it replaces, which makes it the best value in serious multicolor printing right now. The X1 Carbon holds second as the proven flagship and the H2D stays third as the dual nozzle workhorse with a bigger build volume, both still worth it if you need their specific strengths, but the P2S simply offers more printer per dollar for most makers. Prusa Core One keeps fourth on its ecosystem and reliability. Nothing this week reorders the leaders, the P2S is the printer I would put in front of almost anyone moving up from a starter machine, and its AMS combo remains the most sensible buy in the lineup.",
        "highlights": [
            {"title": "Bambu Lab P2S refreshes the best seller right", "body": "It keeps the P1S formula and adds a 5 inch touchscreen, AI error detection, a 50C regulated chamber, a 300C nozzle and a 70 percent stronger extruder. The upgrades land where they matter for everyday printing."},
            {"title": "The price is what seals number one", "body": "At $549 standalone and $799 for the combo, it costs only $50 more than the P1S it replaces. That makes it the best value in serious multicolor printing right now."},
            {"title": "H2D stays the dual nozzle workhorse", "body": "Its bigger build volume, multi material support and dual nozzle setup keep it in third for makers who need that capability. From $1,899 it is the step up when the P2S is not enough."},
        ],
    },
    "zh-tw": {
        "commentary": "Bambu Lab P2S Combo 守住我 2026 年 6 月的第一名，Tom's Hardware 的評測完全印證原因，它把暢銷機改款改得剛剛好，沒有把成功配方搞砸。P2S 保留了讓 P1S 成為工作室預設機的一切，再加上 5 吋彩色觸控螢幕、AI 錯誤偵測能抓義大利麵、噴嘴結塊跟換料堵塞、50 度主動控溫腔體、300 度噴嘴、強化 70% 的擠出機，運作還更安靜。決定性的是價格，單機 549 美元、combo 799 美元，只比它取代的機型貴 50 美元，這讓它成為現在認真做多色列印裡性價比最高的選擇。X1 Carbon 守第二，是久經考驗的旗艦，H2D 守第三，是大列印空間的雙噴嘴主力機，兩台只要你需要它們的特長都還是值得，但對大多數玩家來說，P2S 每塊錢買到的就是更多。Prusa Core One 守第四，靠生態系跟可靠度。這週沒有消息動到前段班，P2S 是我幾乎會推薦給任何從入門機升級的人的機型，它的 AMS combo 還是整個產品線裡最合理的買法。",
        "highlights": [
            {"title": "Bambu Lab P2S 把暢銷機改款改得對", "body": "保留 P1S 配方，加上 5 吋觸控螢幕、AI 錯誤偵測、50 度控溫腔體、300 度噴嘴跟強化 70% 的擠出機。升級都加在日常列印真正用得到的地方。"},
            {"title": "價格是封王關鍵", "body": "單機 549 美元、combo 799 美元，只比它取代的 P1S 貴 50 美元。這讓它成為現在認真做多色列印裡性價比最高的選擇。"},
            {"title": "H2D 還是雙噴嘴主力機", "body": "更大的列印空間、多材料支援跟雙噴嘴設計，讓它守住第三，給需要這些能力的玩家。從 1,899 美元起，是 P2S 不夠用時的升級選擇。"},
        ],
    },
}

# ----------------------------------------------------------------------------
# best-action-cameras.json
# ----------------------------------------------------------------------------
entries["best-action-cameras.json"] = {
    "references": [
        {"title": "DJI Osmo Action 6 review: Better than anything GoPro or Insta360 can offer", "url": "https://www.tomsguide.com/cameras-photography/gopro-action-cameras/dji-osmo-action-6-review", "source": "Tom's Guide"},
        {"title": "Insta360 Ace Pro 2 vs DJI Osmo Action 6 (2026)", "url": "https://droneandcam.com/en/post/insta360-ace-pro-2-vs-dji-osmo-action-6-which-action-camera-should-you-choose/", "source": "Drone & Cam"},
    ],
    "en": {
        "commentary": "The DJI Osmo Action 6 keeps my top spot into June 2026, and since its November 2025 launch it has held the consensus best overall position for good reason. It brought the industry's first variable aperture, f/2.0 to f/4.0, on a 1/1.1 inch square sensor delivering 13.5 stops of dynamic range, and that combination gives it the best all around image in the class along with the longest battery and the deepest waterproofing, 65 feet without a case versus 39 for the Ace Pro 2 and 33 for the Hero13 Black. If you want one camera that does everything well, this is it. The Insta360 Ace Pro 2 holds second and remains the pick for hands on vloggers who need the flip screen and the best onboard mic. The GoPro Mission 1 Pro keeps third on the strength of its stabilization and the HB lens ecosystem, which is exactly what motorcycle and MTB riders should weight. The Hero13 Black holds its spot as the value GoPro. Nothing this week reorders the field, the Action 6 is simply the most complete action camera you can buy, and unless you specifically need a flip screen or the GoPro mounting world, it is my confident recommendation.",
        "highlights": [
            {"title": "DJI Osmo Action 6 has the best all around image", "body": "Its industry first variable aperture on a 1/1.1 inch sensor delivers 13.5 stops of dynamic range, plus the longest battery and 65 foot waterproofing without a case. For one do everything camera, it is the pick."},
            {"title": "Insta360 Ace Pro 2 is the vlogger's choice", "body": "Its flip screen and best in class onboard mic make it the pick for hands on creators who film themselves. That keeps it a strong second for vloggers."},
            {"title": "GoPro Mission 1 Pro wins for riders", "body": "Its stabilization and the HB lens ecosystem are exactly what motorcycle and MTB riders should weight. For the most stable on bike footage, it holds third with a real purpose."},
        ],
    },
    "zh-tw": {
        "commentary": "DJI Osmo Action 6 守住我 2026 年 6 月的冠軍，從 2025 年 11 月上市以來，它一直穩坐公認的最佳全能機，這是有道理的。它帶來業界第一個可變光圈，f/2.0 到 f/4.0，配 1/1.1 吋方形感光元件，給出 13.5 級動態範圍，這個組合讓它有同級最好的全面畫質，加上最長電池續航跟最深防水，裸機防水約 20 公尺，Ace Pro 2 約 12 公尺，Hero13 Black 約 10 公尺。想要一台什麼都拍得好的相機，就是它。Insta360 Ace Pro 2 守第二，仍是手持自拍 vlogger 的首選，有翻轉螢幕跟同級最好的內建麥克風。GoPro Mission 1 Pro 守第三，靠它的防震跟 HB 鏡頭生態系，這正是機車族跟登山車騎士該看重的。Hero13 Black 守住位置，當性價比 GoPro。這週沒有消息動到排名，Action 6 就是現在最完整的運動相機，除非你特別需要翻轉螢幕或 GoPro 那套配件世界，否則它就是我有底氣的推薦。",
        "highlights": [
            {"title": "DJI Osmo Action 6 全面畫質最好", "body": "業界第一個可變光圈配 1/1.1 吋感光元件，給出 13.5 級動態範圍，加上最長電池續航跟裸機約 20 公尺防水。想要一台什麼都能拍的相機，就選它。"},
            {"title": "Insta360 Ace Pro 2 是 vlogger 首選", "body": "翻轉螢幕加同級最好的內建麥克風，讓自拍創作者愛不釋手。這讓它穩坐第二，是拍自己的人最佳選擇。"},
            {"title": "GoPro Mission 1 Pro 是騎士首選", "body": "它的防震跟 HB 鏡頭生態系，正是機車族跟登山車騎士該看重的。要最穩的車上畫面，它守住第三，定位明確。"},
        ],
    },
}

# ----------------------------------------------------------------------------
# Apply all
# ----------------------------------------------------------------------------
for fname, spec in entries.items():
    d, p = load(fname)
    entry = {
        "date": DATE,
        "rankings": last_rankings(d),
        "references": spec["references"],
        "i18n": {
            "en": {"commentary": spec["en"]["commentary"], "highlights": spec["en"]["highlights"]},
            "zh-tw": {"commentary": spec["zh-tw"]["commentary"], "highlights": spec["zh-tw"]["highlights"]},
        },
    }
    upsert(d, entry)
    save(p, d)
    print(f"updated {fname}: {len(d['history'])} entries, last={d['history'][-1]['date']}")
