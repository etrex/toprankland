import sys; sys.path.insert(0, "/Users/etrexkuo/toprankland/scripts")
from daily_helper import load, save, upsert, last_rankings, DATE


def do(name, refs, en, zh, rankings=None):
    d, p = load(name)
    entry = {
        "date": DATE,
        "rankings": rankings if rankings is not None else last_rankings(d),
        "references": refs,
        "i18n": {"en": en, "zh-tw": zh},
    }
    upsert(d, entry)
    save(p, d)
    print("updated", name)


# ---------------- best-portable-power-stations ----------------
do("best-portable-power-stations.json",
   [
     {"title": "The Best Portable Power Stations of 2026, Tested by GearJunkie", "url": "https://gearjunkie.com/technology/best-portable-power-stations", "source": "GearJunkie"},
     {"title": "Best portable power stations of 2026", "url": "https://www.techradar.com/best/portable-power-stations", "source": "TechRadar"},
   ],
   {
     "commentary": "Heading into June 2026 my portable power station ranking holds firm, and the EcoFlow Delta 3 Plus stays at number one because it nails the balance the whole category chases. You get LFP cells rated for a decade of daily cycling, genuinely fast wall charging, and a price that keeps undercutting rivals with similar specs. When someone wants one unit that handles a blackout, a camping trip and the occasional jobsite tool without overthinking it, this is the one I hand them. Bluetti's Elite 200 V2 holds second and earns it on charging speed and a compact footprint that punches above its capacity, the pick when you want more headroom than the Delta 3 Plus without jumping to a giant. Anker's SOLIX C2000 Gen 2 keeps third as one of Anker's cleanest designs yet, reliable and sensibly priced. The EcoFlow Delta Pro 3 stays fourth as the heavy hitter for whole-home backup with 240V capability, and the DJI Power 2000 holds fifth on output and build. Down the board the Jackery Explorer 1500 Ultra, Anker C1000 Gen 2 and the rest carry forward, with the C1000 still the sweet-spot pick for most people now that it dips under 400 dollars on sale. Sodium-ion units are starting to appear for cold-weather reliability, but nothing shipping this week reshuffled the order. I held ranks and let the LFP-and-value story carry the verdicts. Buy the Delta 3 Plus first, step up to the Pro 3 only if you actually need 240V.",
     "highlights": [
       {"title": "EcoFlow Delta 3 Plus is the no-overthink champion", "body": "Decade-rated LFP cells, fast wall charging and a price that undercuts similar-spec rivals make it the one unit that covers blackouts, camping and light jobsite use. That balance keeps it firmly at number one."},
       {"title": "Bluetti Elite 200 V2 punches above its size", "body": "It charges faster from the wall than comparable units and takes up less space for the capacity it delivers. When you want more headroom without going giant, it is the clear second."},
       {"title": "Anker C1000 Gen 2 is the value sweet spot", "body": "Now dipping under 400 dollars on sale, it covers a blackout, a campsite and portable power for most households without overspending. That is exactly why it stays the pick I recommend to typical buyers."},
       {"title": "Delta Pro 3 earns the step-up only at 240V", "body": "Its capacity, output and 240V capability make it the whole-home backup play. Step up to it only when you genuinely need to run demanding appliances, otherwise the Delta 3 Plus is the smarter spend."},
     ],
   },
   {
     "commentary": "2026 年 6 月，我的行動電源站排名穩住沒動，EcoFlow Delta 3 Plus 還是第一，因為它把這個類別大家追求的平衡做到位了。它用 LFP 電芯，標稱可以每天循環用十年，牆充速度是真的快，價格又一直壓在同規格對手底下。當有人想要一台就能搞定停電、露營、偶爾接工地工具、不想想太多，我就把它遞給他。Bluetti Elite 200 V2 守第二，靠的是充電速度跟相對小的體積，容量做得比看起來大，適合想比 Delta 3 Plus 多一點餘裕、又不想直接跳大台的人。Anker SOLIX C2000 Gen 2 守第三，是 Anker 目前最俐落的設計之一，穩定、價格也合理。EcoFlow Delta Pro 3 守第四，是全屋備電的重砲，有 240V 能力，DJI Power 2000 守第五，輸出跟做工都到位。再往下 Jackery Explorer 1500 Ultra、Anker C1000 Gen 2 那些照舊，C1000 特價殺到一萬出頭台幣後，依然是多數人的甜蜜點。話說回來，鈉離子機種開始出現、主打低溫可靠度，但這週沒有哪台出貨改變排名。我守住順序，讓 LFP 加性價比這條線帶判斷。先買 Delta 3 Plus，真的需要 240V 再升級 Pro 3。",
     "highlights": [
       {"title": "EcoFlow Delta 3 Plus 是不用想太多的冠軍", "body": "標稱可用十年的 LFP 電芯、快速牆充，加上壓在同規格對手底下的價格，讓它一台就能顧停電、露營跟輕度工地。這份平衡讓它穩坐第一。"},
       {"title": "Bluetti Elite 200 V2 體積小卻能打", "body": "它牆充比同級快，相同容量下體積更小。想比 Delta 3 Plus 多一點餘裕又不想搬大台的人，它就是明確的第二名。"},
       {"title": "Anker C1000 Gen 2 是性價比甜蜜點", "body": "特價殺到一萬出頭台幣，對多數家庭來說顧停電、露營跟行動供電都夠，不用多花錢。這正是我推薦給一般買家的那台。"},
       {"title": "Delta Pro 3 只有要 240V 才值得升級", "body": "它的容量、輸出跟 240V 能力是全屋備電的解法。真的要跑吃電的家電再升級它，不然 Delta 3 Plus 才是更聰明的花法。"},
     ],
   })

# ---------------- best-portable-chargers ----------------
do("best-portable-chargers.json",
   [
     {"title": "Anker's display-equipped Prime Power Banks are EDC must-haves, now up to 30% off", "url": "https://9to5toys.com/2026/06/01/anker-display-prime-power-banks-must-best/", "source": "9to5Toys"},
     {"title": "Best Power Bank 2026: 5 New Chargers That Raised the Bar", "url": "https://the-gadgeteer.com/2026/05/06/best-power-bank-2026-five-new-chargers/", "source": "The Gadgeteer"},
   ],
   {
     "commentary": "Going into June 2026 the portable charger board barely moves, and the Anker Prime 26K 300W stays at number one because nothing else packs laptop-class power into a brick this manageable. It pushes 300W across two USB-C and one USB-A, enough to run a 16-inch MacBook Pro at full speed off a single 140W port while topping a phone and tablet on the side, and the ActiveShield 4.0 thermal system means it does not throttle under sustained load the way last year's high-wattage banks did. With the June price drops on the Prime line, the value math only got better. The Anker Prime 27,650 250W holds second on sheer capacity, the pick when you want the most usable watt-hours from a bank you can still travel with. The Anker 737 stays third as the proven 140W workhorse, and the UGREEN Nexode 25,000mAh 200W keeps fourth as the value laptop charger that makes 200W feel routine. The Anker Nano 10K stays fifth as the pocketable everyday hero with its built-in cable, and the Baseus PicoGo Qi2.2 magnetic bank holds sixth as the best MagSafe-style option. Down through the Anker MagGo, Belkin, INIU, Mophie and Zendure, everything carries forward. No new launch this week reshuffled the order, so I held ranks. Buy the Prime 26K for laptop power, the Nano 10K for your pocket.",
     "highlights": [
       {"title": "Anker Prime 26K 300W is the laptop bank to beat", "body": "It runs a 16-inch MacBook Pro at full speed off a single 140W port while charging a phone and tablet alongside, and ActiveShield 4.0 stops the throttling that plagued last year's high-wattage banks. That keeps it number one."},
       {"title": "Prime 27,650 250W wins on usable capacity", "body": "It delivers the most usable watt-hours of any bank here you can still reasonably travel with. When runtime between charges matters most, it is the clear second."},
       {"title": "Anker Nano 10K is the everyday pocket hero", "body": "The built-in USB-C cable and genuinely pocketable size make it the one I actually carry daily. For phones and earbuds on the go it stays the smart fifth-place everyday pick."},
       {"title": "UGREEN Nexode makes 200W feel routine", "body": "It hits laptop-class wattage at a price that undercuts the premium players, the value play for charging a notebook without paying flagship money. That keeps it solidly in the top four."},
     ],
   },
   {
     "commentary": "2026 年 6 月，行動電源這個榜幾乎沒動，Anker Prime 26K 300W 還是第一，因為沒有別的能把筆電級的功率塞進這麼好拿的磚塊裡。它兩個 USB-C 加一個 USB-A 一共 300W，單一 140W 孔就能讓 16 吋 MacBook Pro 全速跑，旁邊同時還能補手機跟平板，而且 ActiveShield 4.0 散熱讓它在持續重載下不會像去年那些高瓦數電源一樣掉速。加上 6 月 Prime 系列降價，性價比只有更好。Anker Prime 27,650 250W 守第二，靠的是純容量，想從一顆還能帶著走的電源榨出最多可用瓦時，就選它。Anker 737 守第三，是驗證過的 140W 主力，UGREEN Nexode 25,000mAh 200W 守第四，是讓 200W 變家常便飯的高性價比筆電充。Anker Nano 10K 守第五，內建線、口袋好塞，是每天帶著跑的小英雄，Baseus PicoGo Qi2.2 磁吸款守第六，是最好的 MagSafe 風格選擇。再往下 Anker MagGo、Belkin、INIU、Mophie、Zendure 全部照舊。這週沒有新品洗牌，所以我守住排名。要筆電功率買 Prime 26K，要塞口袋買 Nano 10K。",
     "highlights": [
       {"title": "Anker Prime 26K 300W 是筆電電源的標竿", "body": "單一 140W 孔就能讓 16 吋 MacBook Pro 全速跑，旁邊還能補手機跟平板，ActiveShield 4.0 又擋掉了去年高瓦數電源的掉速問題。所以第一還是它。"},
       {"title": "Prime 27,650 250W 贏在可用容量", "body": "它在還能合理帶著走的電源裡，提供最多的可用瓦時。當你最在意兩次充電之間能撐多久，它就是明確的第二。"},
       {"title": "Anker Nano 10K 是每天的口袋小英雄", "body": "內建 USB-C 線、體積真的好塞口袋，是我每天真的會帶的那顆。手機跟耳機在外面要補電，它穩坐第五的日常首選。"},
       {"title": "UGREEN Nexode 讓 200W 變家常便飯", "body": "它做到筆電級瓦數，價格卻壓在旗艦底下，是不想花旗艦錢又要充筆電的高性價比選擇。這讓它穩穩待在前四。"},
     ],
   })

# ---------------- best-electric-bikes ----------------
do("best-electric-bikes.json",
   [
     {"title": "Best Electric Bikes 2026 - Don't Buy Until You Read This", "url": "https://electricbikereport.com/best-electric-bikes/", "source": "Electric Bike Report"},
     {"title": "The Best Electric Bikes of 2026, Lab Tested & Ranked", "url": "https://www.outdoorgearlab.com/topics/biking/best-electric-bike", "source": "OutdoorGearLab"},
   ],
   {
     "commentary": "Going into June 2026 my e-bike ranking stays put, and the Aventon Level 3 holds number one as the best everyday electric bike you can buy. It is high-tech, well-designed and genuinely good value, with a torque sensor, integrated turn signals and an app that ties it all together, so it feels a generation ahead of the field on smart features without asking a premium price. When someone wants one commuter that just works and looks the part, this is my first answer. The Lectric XP4 750 holds second as the people's champ on value: it folds into a car trunk, packs more power and range than bikes costing twice as much, and stays the easiest bike to recommend to anyone watching their budget. The Velotric Discover 3 keeps third on comfort and a plush, confident ride, the pick for riders who prioritize how a bike feels over spec-sheet flash. The Segway Myon stays fourth on smart tech, and the Aventon Aventure 3 holds fifth as the fat-tire standard with a 750W motor and suspension fork. Down through the Canyon Citylite ON, Trek Verve+ 4S, Tenways CGO800S and Lectric XP Lite 2, everything carries forward. Aventon's new Current eMTB grabbed headlines this spring, but it is a different category and does not touch this commuter-focused board. I held ranks and let the value-versus-tech split frame the top of the list.",
     "highlights": [
       {"title": "Aventon Level 3 is the best everyday e-bike", "body": "A torque sensor, integrated turn signals and a cohesive app put it a generation ahead on smart features without a premium price. For one commuter that just works, it stays number one."},
       {"title": "Lectric XP4 750 is the people's champ", "body": "It folds into a trunk and delivers more power and range than bikes costing twice as much. For anyone watching their budget, it is the easiest bike on the board to recommend, a deserved second."},
       {"title": "Velotric Discover 3 wins on ride feel", "body": "Its plush, confident ride makes it the pick for riders who care more about comfort than spec-sheet flash. That keeps it a solid third for everyday cruising and commuting."},
       {"title": "Aventure 3 is the fat-tire standard", "body": "A 750W motor, suspension fork and Shimano drivetrain make it the reference 26x4 fat-tire bike. For go-anywhere traction it stays the fifth-place pick worth keeping in mind."},
     ],
   },
   {
     "commentary": "2026 年 6 月，我的電動自行車排名守住沒動，Aventon Level 3 穩坐第一，是現在能買到最好的日常通勤電輔車。它科技感足、設計到位、性價比也是真的好，有扭力感測、整合方向燈、還有一個把一切串起來的 App，所以智慧功能上它感覺領先同級一個世代，價格卻沒亂喊。當有人想要一台「就能用、外型又體面」的通勤車，我第一個推它。Lectric XP4 750 守第二，是性價比的庶民英雄，能折進後車廂，動力跟續航比貴一倍的車還強，對顧預算的人來說，它是榜上最好推薦的車。Velotric Discover 3 守第三，靠的是舒適跟扎實安心的騎乘感，適合在意「騎起來的感覺」勝過規格表花俏的人。Segway Myon 守第四，強在智慧科技，Aventon Aventure 3 守第五，是 750W 馬達加避震前叉的胖胎標竿。再往下 Canyon Citylite ON、Trek Verve+ 4S、Tenways CGO800S、Lectric XP Lite 2 全部照舊。Aventon 新的 Current eMTB 這個春天搶了不少版面，不過那是另一個類別，碰不到這個以通勤為主的榜。我守住排名，讓性價比對科技這條線去框榜首。",
     "highlights": [
       {"title": "Aventon Level 3 是最強日常電輔車", "body": "扭力感測、整合方向燈、加上一個把功能串起來的 App，讓它智慧功能領先同級一個世代，價格卻不喊高。要一台就能用的通勤車，第一還是它。"},
       {"title": "Lectric XP4 750 是庶民英雄", "body": "它能折進後車廂，動力跟續航卻比貴一倍的車強。對顧預算的人來說，它是榜上最好推薦的一台，第二名實至名歸。"},
       {"title": "Velotric Discover 3 贏在騎乘感", "body": "它柔順又安心的騎乘感，讓在意舒適勝過規格花俏的人選它。這讓它在日常巡航跟通勤穩坐第三。"},
       {"title": "Aventure 3 是胖胎標竿", "body": "750W 馬達、避震前叉加 Shimano 變速，讓它成為 26x4 胖胎的參考基準。要去哪都有抓地力，它穩坐值得記住的第五名。"},
     ],
   })

# ---------------- best-electric-scooters ----------------
do("best-electric-scooters.json",
   [
     {"title": "Apollo Go vs. Segway Max G3: The Ultimate Head-to-Head Showdown", "url": "https://electricscooterguide.com/apollo-go-vs-segway-max-g3/", "source": "Electric Scooter Guide"},
     {"title": "Segway Ninebot eKickscooter Max G3 review", "url": "https://www.tomsguide.com/home/electric-scooters/segway-ninebot-ekickscooter-max-g3-review", "source": "Tom's Guide"},
   ],
   {
     "commentary": "Heading into June 2026 my scooter ranking stays steady, and the Segway Ninebot Max G3 keeps number one as the most complete commuter on the market. A 2000W peak motor pushes it to 28 mph and up the kind of hills that stall lesser scooters, the 597Wh battery delivers a genuine 40-plus miles, and dual hydraulic suspension on self-sealing 11-inch tires makes it the smoothest ride in its class. Add dual disc brakes that haul it down from 15 mph in under three seconds and you have the scooter I trust most for a daily commute. The Apollo City Pro holds second as the refined all-rounder, and it is worth noting the Apollo Go just dropped to 999 dollars with a dual-motor setup, full suspension and IP66 rating, which makes it a louder value argument than ever, but the City Pro's polish keeps it ahead for now. The NIU KQi3 Pro stays third as the value-and-portability sweet spot, the easiest scooter to recommend to a first-time buyer. The Xiaomi 4 Pro holds fifth on value, and down through the GoTrax G4, Levy Plus, Hiboy S2 Pro and Unagi Model One E500, everything carries forward. No launch this week justified a reshuffle, so I held ranks. Buy the Max G3 for the complete package, the KQi3 Pro to save money, the Apollo Go if that price cut speaks to you.",
     "highlights": [
       {"title": "Segway Max G3 is the most complete commuter", "body": "A 2000W peak motor, real 40-plus-mile range, dual hydraulic suspension and disc brakes that stop it from 15 mph in under three seconds make it the scooter I trust daily. That keeps it number one."},
       {"title": "Apollo City Pro is the refined all-rounder", "body": "Its polish and balanced ride keep it second even as the cheaper Apollo Go gains ground. For riders who want a premium feel without going to the Max G3's weight, it is the pick."},
       {"title": "NIU KQi3 Pro is the value-portability sweet spot", "body": "It pairs a light, foldable frame with solid range at a friendly price, making it the easiest scooter to recommend to a first-time buyer. That keeps it a deserved third."},
       {"title": "Apollo Go's price cut sharpens the value fight", "body": "Now at 999 dollars with dual motors, full suspension and IP66, it is a louder value argument than before. The City Pro's refinement keeps it ahead, but the Go is the one to watch."},
     ],
   },
   {
     "commentary": "2026 年 6 月，我的電動滑板車排名很穩，Segway Ninebot Max G3 守住第一，是市面上最完整的通勤車。2000W 峰值馬達讓它衝到時速 45 公里，爬那種會讓低階車卡住的坡也輕鬆，597Wh 電池實測能跑 60 多公里，雙液壓避震配 11 吋自補胎，是同級最順的騎乘。再加上雙碟煞，從時速 24 公里煞停不到三秒，這就是我最信得過拿來每天通勤的車。Apollo City Pro 守第二，是精緻的全能型，這邊要提一下，Apollo Go 剛降到約台幣三萬、雙馬達、全避震、IP66，性價比的聲音比以前更大，不過 City Pro 的細膩度目前還是壓著它。NIU KQi3 Pro 守第三，是性價比加便攜的甜蜜點，最好推薦給第一次買的人。Xiaomi 4 Pro 守第五，主打性價比，再往下 GoTrax G4、Levy Plus、Hiboy S2 Pro、Unagi Model One E500 全部照舊。這週沒有新品值得洗牌，所以我守住排名。要完整就買 Max G3，要省錢買 KQi3 Pro，被降價打動就看 Apollo Go。",
     "highlights": [
       {"title": "Segway Max G3 是最完整的通勤車", "body": "2000W 峰值馬達、實測 60 多公里續航、雙液壓避震、碟煞從時速 24 公里不到三秒煞停，讓它成為我每天信得過的車。所以第一是它。"},
       {"title": "Apollo City Pro 是精緻全能型", "body": "它的細膩度跟均衡騎乘感，讓它在更便宜的 Apollo Go 追近時仍守第二。想要高級感又不想扛 Max G3 重量的人，選它。"},
       {"title": "NIU KQi3 Pro 是性價比與便攜的甜蜜點", "body": "輕巧可折的車架配上扎實續航，價格又親切，是最好推薦給第一次買的人的車。這讓它穩坐第三。"},
       {"title": "Apollo Go 降價讓性價比戰更激烈", "body": "現在約台幣三萬、雙馬達、全避震、IP66，性價比的聲音比以前更大。City Pro 的精緻度暫時壓著它，但 Go 是值得盯的那台。"},
     ],
   })

# ---------------- best-massage-guns ----------------
do("best-massage-guns.json",
   [
     {"title": "The Best Massage Guns of 2026, Tested & Ranked", "url": "https://www.techgearlab.com/topics/health-fitness/best-massage-gun", "source": "TechGearLab"},
     {"title": "12 Best Massage Guns of 2026, Lab-Tested and Reviewed", "url": "https://www.consumerreports.org/health/massage-guns/massage-guns-evaluated-a1174087874/", "source": "Consumer Reports"},
   ],
   {
     "commentary": "Going into June 2026 my massage gun ranking holds, and the Theragun Pro Plus stays at number one as the most capable device in the category. The amplitude and stall force are simply in a different league, it adds heat, vibration and breathwork modes that turn it from a percussion gun into a full recovery tool, and the rotating arm reaches the spots cheaper guns cannot. The only real knock is price, which is exactly why I am honest that most people do not need to spend this much. The Rally Orbital Massager holds second on a genuinely different feel: its orbital motion is quieter and easier on the body for everyday use, the pick for people who find standard percussion too harsh. The Hyperice Hypervolt 2 Pro stays third as the smoothest, quietest full-size option, around 40 to 60 decibels with a strong app, the one I recommend for living-room recovery without interrupting a podcast. The Theragun Prime holds fourth as the value entry into the Therabody ecosystem, and the Ekrin B37 keeps fifth as the value-and-battery champ. Down through the Hypervolt Go 2, Bob and Brad Q2 Mini and Toloco EM26, everything carries forward, with the Q2 Mini still the budget travel pick. No launch this week moved the board, so I held ranks. Buy the Pro Plus if budget is no object, the Hypervolt 2 Pro for quiet power, the Ekrin B37 to save money.",
     "highlights": [
       {"title": "Theragun Pro Plus is the most capable gun", "body": "Class-leading amplitude and stall force plus heat, vibration and breathwork modes turn it into a full recovery tool, and the rotating arm reaches what cheaper guns cannot. That keeps it number one."},
       {"title": "Rally Orbital is the gentle alternative", "body": "Its orbital motion runs quieter and easier on the body than standard percussion, the pick for anyone who finds typical guns too harsh. That distinct feel keeps it a deserved second."},
       {"title": "Hypervolt 2 Pro is the quiet powerhouse", "body": "At 40 to 60 decibels with strong power and a capable app, it delivers living-room recovery without interrupting a conversation. For quiet full-size use it stays the third-place pick."},
       {"title": "Ekrin B37 is the value-and-battery champ", "body": "It pairs strong power with class-leading battery life at a friendly price, the smart buy for anyone who wants Theragun-grade therapy without the premium. That keeps it firmly fifth."},
     ],
   },
   {
     "commentary": "2026 年 6 月，我的筋膜槍排名守住沒動，Theragun Pro Plus 還是第一，是這個類別最能打的機器。它的振幅跟堵轉力根本是另一個檔次，又加了熱敷、震動跟呼吸引導模式，把它從一支打擊槍變成完整的恢復工具，旋轉臂還能打到便宜槍碰不到的地方。唯一的硬傷就是價格，所以我也老實說，多數人其實不用花到這麼多。Rally Orbital Massager 守第二，靠的是真的不一樣的手感，它的軌道式運動更安靜、對身體更溫和，適合覺得一般打擊太硬的人。Hyperice Hypervolt 2 Pro 守第三，是全尺寸裡最順最安靜的，大約 40 到 60 分貝又有不錯的 App，是我推薦在客廳放鬆、不會打斷 Podcast 的那支。Theragun Prime 守第四，是進 Therabody 生態系的性價比入門款，Ekrin B37 守第五，是性價比加續航的冠軍。再往下 Hypervolt Go 2、Bob and Brad Q2 Mini、Toloco EM26 全部照舊，Q2 Mini 還是預算型旅行首選。這週沒有新品動到榜，所以我守住排名。預算無上限買 Pro Plus，要安靜又有力買 Hypervolt 2 Pro，要省錢買 Ekrin B37。",
     "highlights": [
       {"title": "Theragun Pro Plus 是最能打的筋膜槍", "body": "同級最強的振幅跟堵轉力，加上熱敷、震動、呼吸引導模式，把它變成完整恢復工具，旋轉臂還能打到便宜槍碰不到的地方。所以第一是它。"},
       {"title": "Rally Orbital 是溫和派替代方案", "body": "它的軌道式運動比一般打擊更安靜、對身體更溫和，適合覺得一般槍太硬的人。這份獨特手感讓它穩坐第二。"},
       {"title": "Hypervolt 2 Pro 是安靜的力量派", "body": "40 到 60 分貝、力道夠又有好用 App，讓你在客廳放鬆也不會打斷對話。要安靜的全尺寸使用，它守住第三。"},
       {"title": "Ekrin B37 是性價比加續航冠軍", "body": "力道強、續航同級最頂、價格又親切，是想要 Theragun 級療癒卻不想付旗艦錢的聰明選擇。這讓它穩穩待在第五。"},
     ],
   })

# ---------------- best-mattresses ----------------
do("best-mattresses.json",
   [
     {"title": "Saatva vs. Helix Mattress Comparison 2026", "url": "https://www.sleepfoundation.org/mattress-comparisons/saatva-vs-helix", "source": "Sleep Foundation"},
     {"title": "Helix vs. Saatva, 12 Mattresses Compared", "url": "https://naplab.com/mattress-comparisons/helix-vs-saatva/", "source": "NapLab"},
   ],
   {
     "commentary": "Going into June 2026 my mattress ranking holds, and the Saatva Classic stays at number one as the safest luxury pick for the widest range of sleepers. Its dual-coil innerspring build gives it the best edge support on the board and a responsive, never-stuck feel, and the white-glove delivery, lifetime warranty and year-long trial make it the lowest-risk premium purchase you can make. For back and stomach sleepers especially, that lumbar support is hard to beat. The Helix Midnight Luxe holds a very close second and is genuinely the better call for side sleepers: its zoned lumbar support and contouring foam layers relieve shoulder and hip pressure better than the Saatva's bouncier surface, and recent testing scored it a 9.43, among the highest across hundreds of beds. If you sleep on your side, start with the Helix. The Purple Restore Hybrid stays third as the cooling-and-pressure specialist with its GelFlex grid, and the Bear Elite Hybrid holds fourth for hot sleepers and athletes. The Nectar Premier Copper keeps fifth as the value-and-motion-isolation pick, ideal for couples on a budget. Down through the Tempur-Pedic ProAdapt, DreamCloud, Avocado Green, Brooklyn Aurora Luxe and WinkBed Plus, everything carries forward. No launch this week reshuffled the order, so I held ranks. Saatva for most sleepers, Helix if you are a side sleeper.",
     "highlights": [
       {"title": "Saatva Classic is the safest luxury pick", "body": "Its dual-coil build delivers the best edge support on the board and a responsive feel, backed by white-glove delivery, a lifetime warranty and a year-long trial. That low-risk premium package keeps it number one."},
       {"title": "Helix Midnight Luxe owns side sleeping", "body": "Zoned lumbar support and contouring foam relieve shoulder and hip pressure better than a bouncier innerspring, and recent testing scored it 9.43. For side sleepers it is the one to start with, a deserved second."},
       {"title": "Purple Restore Hybrid wins on cooling", "body": "Its GelFlex grid combines temperature-neutral airflow with strong pressure relief that no foam quite replicates. For hot sleepers who want a distinctive feel, it stays the third-place specialist."},
       {"title": "Nectar Premier Copper is the value pick", "body": "It pairs excellent motion isolation with a price well under the luxury players, the smart buy for couples on a budget. That keeps it firmly in the top five."},
     ],
   },
   {
     "commentary": "2026 年 6 月，我的床墊排名守住沒動，Saatva Classic 還是第一，是適合最多睡姿的人、最安全的奢華選擇。它雙層彈簧的內構給了它榜上最好的邊緣支撐，還有那種回彈、不會陷住的觸感，加上白手套到府、終身保固、整年試睡，是你能做的風險最低的高階購買。尤其對仰睡跟趴睡的人，那個腰部支撐很難被超越。Helix Midnight Luxe 緊咬第二，而且對側睡的人來說它其實是更好的選擇，分區腰部支撐加上貼合的泡棉層，紓解肩膀跟臀部壓力比 Saatva 偏彈的表面更好，最近測試還拿到 9.43，是幾百張床裡數一數二高的。如果你側睡，先從 Helix 看起。Purple Restore Hybrid 守第三，是涼感加減壓的專家，靠的是它的 GelFlex 凝膠格。Bear Elite Hybrid 守第四，適合怕熱的人跟運動族。Nectar Premier Copper 守第五，是性價比加抗干擾的選擇，預算有限的情侶很適合。再往下 Tempur-Pedic ProAdapt、DreamCloud、Avocado Green、Brooklyn Aurora Luxe、WinkBed Plus 全部照舊。這週沒有新品洗牌，所以我守住排名。多數人選 Saatva，側睡選 Helix。",
     "highlights": [
       {"title": "Saatva Classic 是最安全的奢華選擇", "body": "雙層彈簧帶來榜上最好的邊緣支撐跟回彈觸感，加上白手套到府、終身保固、整年試睡。這套低風險的高階組合讓它穩坐第一。"},
       {"title": "Helix Midnight Luxe 主宰側睡", "body": "分區腰部支撐加貼合泡棉，紓解肩臀壓力比偏彈的彈簧床更好，最近測試拿到 9.43。側睡的人就從它看起，第二實至名歸。"},
       {"title": "Purple Restore Hybrid 贏在涼感", "body": "它的 GelFlex 凝膠格把溫度中性的透氣跟強力減壓結合，是泡棉複製不來的。怕熱又想要獨特觸感的人，它守住第三的專家位。"},
       {"title": "Nectar Premier Copper 是性價比選擇", "body": "它把優異的抗干擾跟遠低於奢華品牌的價格結合，是預算有限情侶的聰明選擇。這讓它穩穩待在前五。"},
     ],
   })

# ---------------- best-pickleball-paddles ----------------
do("best-pickleball-paddles.json",
   [
     {"title": "Expert review: JOOLA Perseus Pro IV offers upgrade in feel, stability", "url": "https://thekitchenpickle.com/blogs/gear/joola-perseus-pro-iv-review/", "source": "The Kitchen Pickleball"},
     {"title": "Best Pickleball Paddles 2026 (From Testing 100+)", "url": "https://bepickleballer.com/best-pickleball-paddles/", "source": "Be Pickleballer"},
   ],
   {
     "commentary": "Going into June 2026 my paddle ranking holds, and the JOOLA Perseus Pro IV stays at number one as the most complete power paddle in the game. Designed with Ben Johns and the JOOLA pro roster, the Pro IV refines the line with better feel and stability, and reviewers note it tames the uncontrollable pop that some disliked on earlier Perseus models, so you get genuine power that you can actually aim. For an advanced player who wants to drive the ball without sacrificing control, this is still the paddle to beat. The Honolulu J2CR holds a very close second and is the value story of the year: it plays like a 250-dollar paddle, balances spin, control and power beautifully, and outlasts most of the field, all for around 175 dollars after codes. If you want roughly 85 percent of the top paddle's performance for far less money, the J2CR is the smart buy. The Bread and Butter Loco 16mm Hybrid stays third as the all-court value hybrid, and the Selkirk LABS Project Boomstik holds fourth as the pure-power specialist. The CRBN 1X Power Series keeps fifth on spin. Down through the Selkirk Vanguard Power Air, Paddletek Bantam ESQ-C, Gearbox Pro Ultimate, Six Zero Double Black Diamond and Vatic Pro Prism Flash, everything carries forward. No launch this week reshuffled the order, so I held ranks. Buy the Perseus Pro IV for top-tier power, the J2CR to save real money.",
     "highlights": [
       {"title": "JOOLA Perseus Pro IV is the power paddle to beat", "body": "Designed with Ben Johns, the Pro IV adds feel and stability while taming the uncontrollable pop of earlier models, so the power is finally aimable. For advanced players it stays number one."},
       {"title": "Honolulu J2CR is the value story of the year", "body": "It plays like a 250-dollar paddle, balances spin, control and power, and outlasts the field, all for around 175 dollars after codes. For roughly 85 percent of the top performance at far less cost, it is the smart buy and a clear second."},
       {"title": "Bread and Butter Loco is the all-court hybrid", "body": "Its 16mm hybrid build balances power and control with excellent value, the pick for players who want one do-everything paddle. That well-rounded profile keeps it a deserved third."},
       {"title": "Project Boomstik is the pure-power specialist", "body": "It posts the highest raw power on the board with a forgiving sweet spot, the choice for bangers who want to end points fast. That specialization keeps it firmly in the top four."},
     ],
   },
   {
     "commentary": "2026 年 6 月，我的球拍排名守住沒動，JOOLA Perseus Pro IV 還是第一，是現在最完整的力量型球拍。它跟 Ben Johns 還有 JOOLA 職業陣容一起設計，Pro IV 把這條線在手感跟穩定度上再打磨，評測也提到它馴服了早期 Perseus 那種有人不喜歡的失控爆發感，所以你拿到的是真的有力、又真的瞄得準的球。對想要強力進攻又不想犧牲控制的進階球友來說，它還是那支要被超越的拍。Honolulu J2CR 緊咬第二，是今年的性價比故事，它打起來像台幣七千多的拍子，旋轉、控制、力量平衡得漂亮，又比多數對手耐用，折扣後大約台幣五千出頭。想用遠少的錢拿到頂級拍大約 85% 的表現，J2CR 就是聰明的買法。Bread and Butter Loco 16mm Hybrid 守第三，是全場型的性價比混碳拍，Selkirk LABS Project Boomstik 守第四，是純力量專家。CRBN 1X Power Series 守第五，強在旋轉。再往下 Selkirk Vanguard Power Air、Paddletek Bantam ESQ-C、Gearbox Pro Ultimate、Six Zero Double Black Diamond、Vatic Pro Prism Flash 全部照舊。這週沒有新品洗牌，所以我守住排名。要頂級力量買 Perseus Pro IV，要省錢買 J2CR。",
     "highlights": [
       {"title": "JOOLA Perseus Pro IV 是要被超越的力量拍", "body": "跟 Ben Johns 一起設計，Pro IV 加強了手感跟穩定度，又馴服了早期款的失控爆發感，力量終於瞄得準。對進階球友，第一還是它。"},
       {"title": "Honolulu J2CR 是今年的性價比故事", "body": "它打起來像台幣七千多的拍，旋轉、控制、力量都平衡，又比對手耐用，折扣後約五千出頭台幣。用遠少的錢拿到頂拍約 85% 的表現，這是聰明買法，明確的第二。"},
       {"title": "Bread and Butter Loco 是全場型混碳拍", "body": "16mm 混碳結構把力量跟控制平衡得好，性價比又高，適合想要一支什麼都能打的人。這份全面讓它穩坐第三。"},
       {"title": "Project Boomstik 是純力量專家", "body": "它在榜上有最高的純力量，甜蜜點又寬容，是想快速結束分數的重砲手首選。這份專長讓它穩穩待在前四。"},
     ],
   })

print("ALL DONE")
