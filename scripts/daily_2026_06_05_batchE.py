import sys; sys.path.insert(0, "/Users/etrexkuo/toprankland/scripts")
from daily_helper import load, save, upsert, last_rankings, DATE

def do(name, refs, en, zh):
    d, p = load(name)
    entry = {"date": DATE, "rankings": last_rankings(d), "references": refs, "i18n": {"en": en, "zh-tw": zh}}
    upsert(d, entry); save(p, d); print("updated", name)

# ---------------- best-gaming-mice ----------------
do("best-gaming-mice.json",
   [
     {"title": "Best Gaming Mouse 2026: Our Tested Picks for Every Grip Style", "url": "https://www.tomshardware.com/best-picks/best-gaming-mouse", "source": "Tom's Hardware"},
     {"title": "The Best Gaming Mouse of 2026", "url": "https://www.rtings.com/mouse/reviews/best/by-usage/gaming", "source": "RTINGS"},
     {"title": "Best Mouse for VALORANT (664 Pro Players, June 2026)", "url": "https://prosettings.net/guides/valorant-mouse/", "source": "ProSettings"},
   ],
   {
     "commentary": "Heading into June 2026 the gaming-mouse top tier has frozen into a shape I am happy to defend, and the Logitech G PRO X2 SUPERSTRIKE stays at number one because nothing else does what it does. It is still the only mainstream mouse with fully adjustable actuation and rapid trigger on the main clicks, so you can set a feather-light press and re-fire the instant you start lifting. For a Valorant or CS2 player who lives and dies on first-shot timing, that is a real mechanical advantage rather than a spec-sheet flex. The G Pro X Superlight 2 DEX holds second and remains the safest buy on the board: 60 grams, the HERO 2 sensor, flawless tracking, and the ergonomic shape that pro pools keep voting for in the latest ProSettings counts. Razer's Viper V4 Pro sits third and is genuinely the wireless mouse I hand to anyone who wants outright performance without thinking about actuation tuning, with the DeathAdder V4 Pro right behind it for ergo-grip players. The DeathAdder V3 HyperSpeed and Endgame Gear OP1we round out a value-rich middle where you give up almost nothing real. The honest read this month is that the field has matured past gimmicks. Sensors are all flawless, latency is all imperceptible, and weight has bottomed out around 50 grams. What separates these mice now is shape and the one or two genuine innovations like Superstrike's trigger. Pick by your grip, trust any of the top six, and spend the savings on a good mousepad. That is the whole game.",
     "highlights": [
       {"title": "Superstrike's adjustable trigger still leads", "body": "It remains the only mainstream mouse with fully adjustable actuation and rapid trigger on the main clicks. For players who win on first-shot timing, that light-press-and-re-fire mechanic is a real edge, which keeps it at number one."},
       {"title": "Superlight 2 DEX is the safest buy", "body": "At 60 grams with the HERO 2 sensor and a shape pro pools keep choosing, it is the mouse I recommend when someone just wants the proven option. Flawless tracking and rock-solid wireless keep it a clear second."},
       {"title": "Viper V4 Pro is the no-fuss performance pick", "body": "It delivers outright wireless performance without any actuation tuning to think about. For a player who wants top-tier feel straight out of the box, it is the easy third and the DeathAdder V4 Pro shadows it for ergo grips."},
       {"title": "The whole top six is flawless now", "body": "Sensors track perfectly, latency is imperceptible and weight has bottomed near 50 grams across the board. Shape is what separates them, so pick by grip and trust any of these six completely."},
     ],
   },
   {
     "commentary": "2026 年 6 月，電競滑鼠的頂端已經定型成一個我很願意捍衛的樣子，Logitech G PRO X2 SUPERSTRIKE 還是第一，因為沒別的滑鼠做得到它做的事。它依然是主流市場唯一在主鍵上做到完全可調觸發點加快速觸發的滑鼠，你可以設成羽毛般的輕壓，手指一抬起就能立刻再按。對一個 Valorant 或 CS2 玩家來說，先手開槍的時機就是生死，這是真實的機械優勢，不是規格表上的花拳繡腿。G Pro X Superlight 2 DEX 守第二，依然是榜上最安全的選擇，60 公克、HERO 2 感測器、追蹤零失誤，那個人體工學外型在最新 ProSettings 的職業選手統計裡還是一票一票被選出來。Razer 的 Viper V4 Pro 排第三，老實說它就是我會直接塞給「只想要純效能、懶得調觸發點」的人的無線滑鼠，DeathAdder V4 Pro 緊跟在後，給握姿派玩家。DeathAdder V3 HyperSpeed 跟 Endgame Gear OP1we 撐起一個高性價比的中段，你幾乎沒犧牲什麼。這個月講白了，整個市場已經成熟到過了噱頭階段，感測器全部零失誤、延遲全部感覺不到、重量也觸底在 50 公克上下。現在真正拉開差距的是外型，還有像 Superstrike 觸發點這種一兩個真本事。照你的握姿選，前六名閉著眼睛買都行，省下來的錢拿去買張好滑鼠墊，這樣就對了。",
     "highlights": [
       {"title": "Superstrike 可調觸發點仍領先", "body": "它依然是主流唯一在主鍵做到完全可調觸發加快速觸發的滑鼠。對靠先手開槍時機取勝的玩家，輕壓加立刻再按是真優勢，所以第一還是它。"},
       {"title": "Superlight 2 DEX 是最安全的買法", "body": "60 公克、HERO 2 感測器、外型又是職業選手一直選的，它就是我會推給「只想要驗證過的選擇」的人。追蹤零失誤、無線穩如石頭，穩坐第二。"},
       {"title": "Viper V4 Pro 是免煩惱效能派", "body": "它給你純無線頂級效能，完全不用去想觸發點怎麼調。想要開箱即頂級手感的玩家，它是輕鬆的第三，DeathAdder V4 Pro 在握姿派那邊緊跟。"},
       {"title": "前六名現在全部零失誤", "body": "感測器追蹤完美、延遲感覺不到、重量也觸底在 50 公克上下。現在拉開差距的是外型，照握姿選，這六支隨便挑都能完全信任。"},
     ],
   })

# ---------------- best-mechanical-keyboards ----------------
do("best-mechanical-keyboards.json",
   [
     {"title": "Best Hall effect keyboards in 2026", "url": "https://www.pcgamer.com/hardware/gaming-keyboards/best-hall-effect-keyboards/", "source": "PC Gamer"},
     {"title": "Best Hall effect keyboard 2026", "url": "https://www.gamesradar.com/hardware/gaming-keyboards/best-hall-effect-keyboard/", "source": "GamesRadar+"},
     {"title": "The 6 Best Gaming Keyboards of 2026", "url": "https://www.rtings.com/keyboard/reviews/best/by-usage/gaming", "source": "RTINGS"},
   ],
   {
     "commentary": "The big story in keyboards this June is that Hall effect has finished going mainstream, and my ranking has been built around that shift for months. The price gap collapsed: the magnetic-switch tech that used to mean spending 175 dollars now starts around 40 to 50, and as of April roughly 40 percent of tracked pro esports players run a Hall effect or analog optical board, up from essentially zero in 2022. That is exactly why the Wooting 60HE+ stays at number one. It is still the keyboard that defined rapid trigger, the Wootility software remains the best in the business for tuning actuation per key, and for a competitive player nothing else feels this responsive. The Wooting 80HE holds second for anyone who wants the same engine in a fuller, more premium TKL-ish layout with arrow keys. SteelSeries Apex Pro TKL Wireless stays third as the most polished all-rounder, the board I hand to someone who wants Hall effect performance plus genuinely good wireless and an OLED screen. Keychron's Q1 Pro keeps fourth because it is still the enthusiast pick when build quality, gasket feel and acoustics matter more than rapid trigger, and that gorgeous CNC case earns its keep. NuPhy Field75 HE rounds out a strong top five. The rest of the board carries forward unchanged. My advice has not moved: if you game competitively, buy Hall effect now that it is cheap, and if you type all day for the love of it, the Q1 Pro is still the one to beat.",
     "highlights": [
       {"title": "Wooting 60HE+ still defines rapid trigger", "body": "It is the board that created the category and the Wootility software remains the best for per-key actuation tuning. For a competitive player nothing else feels this responsive, which keeps it at number one."},
       {"title": "Hall effect is now a no-brainer", "body": "The tech that cost 175 dollars now starts near 40, and around 40 percent of tracked pros already run it. If you game seriously, this is the month the value math finally makes the switch obvious."},
       {"title": "Apex Pro TKL Wireless is the polished all-rounder", "body": "It pairs Hall effect performance with genuinely good wireless and an OLED screen. For someone who wants the speed plus everyday features rather than a pure esports tool, it stays a deserved third."},
       {"title": "Keychron Q1 Pro owns the enthusiast lane", "body": "When gasket feel, acoustics and that CNC case matter more than rapid trigger, it is still the board to beat. For typists who buy for the love of it, fourth undersells how good it feels."},
     ],
   },
   {
     "commentary": "這個 6 月鍵盤圈最大的故事，就是磁軸（Hall effect）徹底走進主流，而我的排名好幾個月前就照這個轉變在排了。價差崩了，以前要花一百七十幾美金的磁軸技術，現在四十到五十美金就有，而且到 4 月為止，被追蹤的職業電競選手大約有四成在用磁軸或類比光軸鍵盤，2022 年時這數字基本上是零。這正是 Wooting 60HE+ 守第一的原因。它依然是定義了快速觸發（rapid trigger）的那把鍵盤，Wootility 軟體在「逐鍵調觸發點」這件事上還是業界最強，對競技玩家來說沒有別的東西這麼跟手。Wooting 80HE 守第二，給想要同一套引擎、但要更完整更高級、帶方向鍵的接近 TKL 配列的人。SteelSeries Apex Pro TKL Wireless 守第三，是最成熟的全能型，我會推給想要磁軸效能又要真的好用的無線加 OLED 螢幕的人。Keychron Q1 Pro 守第四，因為當你更在意做工、gasket 手感跟敲擊音色而不是快速觸發時，它還是玩家首選，那個漂亮的 CNC 鋁殼值回票價。NuPhy Field75 HE 撐起紮實的前五。其餘照舊。我的建議沒變，你要打競技，現在磁軸這麼便宜就直接買，你是整天打字的愛好者，Q1 Pro 還是那把要被超越的標竿。",
     "highlights": [
       {"title": "Wooting 60HE+ 仍定義快速觸發", "body": "它是開創這個類別的鍵盤，Wootility 在逐鍵調觸發點上還是最強。對競技玩家沒別的東西這麼跟手，所以第一還是它。"},
       {"title": "磁軸現在閉著眼睛買就對", "body": "以前一百七十幾美金的技術現在四十美金起跳，而且約四成職業選手已經在用。你要認真打電競，這個月性價比終於讓換軸變得理所當然。"},
       {"title": "Apex Pro TKL Wireless 是成熟全能型", "body": "它把磁軸效能配上真的好用的無線跟 OLED 螢幕。想要速度又要日常功能、而不是純電競工具的人，它穩坐第三。"},
       {"title": "Keychron Q1 Pro 主宰玩家路線", "body": "當 gasket 手感、音色、CNC 鋁殼比快速觸發更重要時，它還是那把要被超越的。對為愛買鍵盤的打字派，第四其實低估了它的手感。"},
     ],
   })

# ---------------- best-gaming-monitors ----------------
do("best-gaming-monitors.json",
   [
     {"title": "The Best OLED Gaming Monitors to Buy in 2026", "url": "https://tftcentral.co.uk/recommendations/the-best-oled-gaming-monitors-to-buy-in-2026", "source": "TFTCentral"},
     {"title": "Best OLED Gaming Monitors 2026", "url": "https://www.tomshardware.com/monitors/gaming-monitors/best-oled-gaming-monitors", "source": "Tom's Hardware"},
     {"title": "The 5 Best OLED Monitors of 2026", "url": "https://www.rtings.com/monitor/reviews/best/oled", "source": "RTINGS"},
   ],
   {
     "commentary": "Going into June 2026 the gaming-monitor crown still belongs to the ASUS ROG Swift OLED PG27UCDM, and the more competitors launch, the more obvious that becomes. It runs Samsung's 4th-gen QD-OLED at 4K 240Hz on 27 inches, which lands a 166 PPI pixel density that is still the sharpest you can get on a mainstream high-refresh OLED. Add Dolby Vision, full DisplayPort 2.1 and ASUS's ELMB, and you have the most complete panel on the market. New arrivals like BenQ's Mobiuz QD-OLED line that shipped in late May, including the 27-inch 4K 240Hz EX271UZ, are excellent and bring black-frame insertion plus 90W USB-C, but they slot into the field rather than dethrone the leader. The LG UltraGear 27GX790B holds second on the strength of its tandem-RGB panel and class-leading refresh headroom, the pick if motion clarity is what you chase. MSI's MPG 341CQR QD-OLED X36 stays third as the ultrawide immersion choice, and Samsung's Odyssey OLED G8 G80SD keeps fourth as a superb 4K 240Hz alternative with a cleaner design. Down the board the Alienware AW2725Q remains my value 4K OLED hero and the AW2726DM the budget-bright pick. Nothing this week reshuffled the order, so I held ranks. The takeaway is simple: 4K 240Hz QD-OLED at 27 inches is now the sweet spot, the PG27UCDM does it best, and the rest of the top four are all genuinely great panels you can buy without regret.",
     "highlights": [
       {"title": "PG27UCDM is still the sharpest OLED", "body": "Its 4th-gen QD-OLED at 4K 240Hz on 27 inches hits 166 PPI, the highest density on a mainstream high-refresh OLED. With Dolby Vision and DisplayPort 2.1 it is the most complete panel, so it stays number one."},
       {"title": "New BenQ panels join, do not dethrone", "body": "The late-May Mobiuz QD-OLED line including the 27-inch 4K 240Hz EX271UZ is excellent with BFI and 90W USB-C. It strengthens the field, but the leader's sharpness and feature set keep it on top."},
       {"title": "LG 27GX790B chases pure motion", "body": "Its tandem-RGB panel and class-leading refresh headroom make it the pick when motion clarity matters most. That speed focus keeps it a clear second behind the all-round PG27UCDM."},
       {"title": "4K 240Hz at 27 inches is the sweet spot", "body": "The whole top tier now clusters around this exact spec, and every one of them is a great buy. Pick by whether you want sharpness, motion or ultrawide immersion and you cannot go wrong."},
     ],
   },
   {
     "commentary": "2026 年 6 月，電競螢幕的王座還是 ASUS ROG Swift OLED PG27UCDM 的，而且對手出得越多，這點就越明顯。它跑的是三星第四代 QD-OLED 面板，27 吋 4K 240Hz，換算下來 166 PPI 像素密度，這在主流高刷 OLED 裡還是最銳利的。再加上 Dolby Vision、完整 DisplayPort 2.1 跟 ASUS 的 ELMB，這就是市面上最完整的一塊面板。新面孔像 BenQ 5 月底出的 Mobiuz QD-OLED 系列，包含 27 吋 4K 240Hz 的 EX271UZ，都很優秀，帶黑幀插入跟 90W USB-C，但它們是補進這個戰場，而不是把王者拉下來。LG UltraGear 27GX790B 守第二，靠的是 tandem-RGB 面板跟同級最高的刷新餘裕，你追的是動態清晰度就選它。MSI 的 MPG 341CQR QD-OLED X36 守第三，是帶魚屏沉浸選擇，三星 Odyssey OLED G8 G80SD 守第四，是設計更乾淨的 4K 240Hz 好替代。再往下，Alienware AW2725Q 還是我的高性價比 4K OLED 英雄，AW2726DM 是預算型高亮選擇。這週沒事件洗牌，所以我守住排名。結論很簡單，27 吋 4K 240Hz QD-OLED 現在是甜蜜點，PG27UCDM 做得最好，前四名其餘那幾塊也全都是買了不會後悔的好面板。",
     "highlights": [
       {"title": "PG27UCDM 仍是最銳利的 OLED", "body": "第四代 QD-OLED、27 吋 4K 240Hz，166 PPI 是主流高刷 OLED 裡最高的密度。配上 Dolby Vision 跟 DisplayPort 2.1，它是最完整的面板，所以第一還是它。"},
       {"title": "BenQ 新面板補進不奪冠", "body": "5 月底的 Mobiuz QD-OLED 系列含 27 吋 4K 240Hz 的 EX271UZ 很優秀，有黑幀插入跟 90W USB-C。它讓戰場更強，但王者的銳利度跟功能完整度讓它穩坐第一。"},
       {"title": "LG 27GX790B 追純動態", "body": "tandem-RGB 面板加同級最高刷新餘裕，讓它在最在意動態清晰度時成為首選。這份速度專注讓它穩居全能型 PG27UCDM 之後的第二。"},
       {"title": "27 吋 4K 240Hz 是甜蜜點", "body": "整個頂端現在都集中在這個規格，而且每一台都是好買的。看你要銳利度、動態還是帶魚屏沉浸來選，怎麼挑都不會錯。"},
     ],
   })

# ---------------- best-gaming-chairs ----------------
do("best-gaming-chairs.json",
   [
     {"title": "Best Gaming Chair in 2026 — top chairs for the money", "url": "https://www.tomshardware.com/best-picks/best-gaming-chairs", "source": "Tom's Hardware"},
     {"title": "Best gaming chairs in 2026 - our top picks for June", "url": "https://www.wepc.com/gaming-chair/best-gaming-chairs/", "source": "WePC"},
     {"title": "Best gaming chair: top seats we've tested", "url": "https://www.techradar.com/gaming/best-gaming-chairs", "source": "TechRadar"},
   ],
   {
     "commentary": "Heading into June 2026 my gaming-chair ranking holds firm, and the Secretlab Titan Evo stays at number one because after hundreds of hours of testing across the press it is still the chair that gets the fundamentals most right. The build is tank-like, the magnetic head pillow and integrated lumbar are genuinely better than the bolt-on cushions most rivals ship, and at roughly 450 to 650 dollars it undercuts a real ergonomic office chair while feeling close to one. For most people wanting one chair that lasts years, this is the answer. The Herman Miller Vantum holds second and earns it on pure ergonomics plus that 12-year warranty, the pick if your back is the whole priority and budget is not. Libernovo Omni stays third as the dynamic-ergonomic wildcard, packing the most adjustable mechanism on the board for people who want an office-grade posture engine in a gaming shell. Razer's Iskur V2 keeps fourth with its adaptive lumbar that still impresses, and the DXRacer Martian Pro holds fifth on plush comfort. Down the value end the Corsair TC100 Relaxed keeps appearing at the top of budget lists for a reason, and it stays my pick when the budget is tight. Nothing this week justified a reshuffle, so I held the board. The honest framing: Secretlab for the best all-round buy, Herman Miller for pure ergonomics, Corsair when money is the constraint. That covers almost everyone.",
     "highlights": [
       {"title": "Titan Evo nails the fundamentals", "body": "Tank-like build, a magnetic head pillow and integrated lumbar that beat the bolt-on cushions rivals ship. At 450 to 650 dollars it undercuts a real ergonomic office chair while feeling close to one, so it stays number one."},
       {"title": "Herman Miller Vantum is the ergonomics king", "body": "Pure posture support plus a 12-year warranty make it the pick when your back is the whole priority and budget is not a constraint. That focus keeps it a deserved second."},
       {"title": "Corsair TC100 owns the budget tier", "body": "It keeps topping budget lists for a reason, delivering solid comfort for a fraction of the flagship price. When money is the constraint, it is still the first chair I recommend."},
       {"title": "Libernovo Omni is the adjustability wildcard", "body": "It packs the most adjustable mechanism on the board, an office-grade posture engine in a gaming shell. For tinkerers who want to dial in every angle, it holds a strong third."},
     ],
   },
   {
     "commentary": "2026 年 6 月，我的電競椅排名站得很穩，Secretlab Titan Evo 還是第一，因為各家媒體測了好幾百個小時下來，它依然是把基本功做得最對的那張椅子。骨架硬得像坦克，磁吸頭枕跟整合式腰靠是真的比多數對手那種外掛墊子好，而且台幣大概一萬五到兩萬，比一張真正的人體工學辦公椅便宜，坐起來卻很接近。對多數想要一張能撐好幾年的人，答案就是它。Herman Miller Vantum 守第二，靠的是純人體工學加上那 12 年保固，當你的腰就是一切、預算不是問題時就選它。Libernovo Omni 守第三，是動態人體工學的奇兵，搭載榜上最會調的機構，給想在電競外殼裡塞一顆辦公室級姿勢引擎的人。Razer 的 Iskur V2 守第四，自適應腰靠還是讓人印象深刻，DXRacer Martian Pro 守第五，靠的是軟綿綿的舒適度。性價比那端，Corsair TC100 Relaxed 一直出現在預算榜頂端是有原因的，預算緊的時候它還是我的首選。這週沒事件值得洗牌，所以我守住整個榜。講白了，要全方位最好買 Secretlab，要純人體工學選 Herman Miller，錢是限制就挑 Corsair，這樣幾乎涵蓋所有人。",
     "highlights": [
       {"title": "Titan Evo 把基本功做到位", "body": "坦克級骨架、磁吸頭枕加整合腰靠，贏過對手那種外掛墊。台幣一萬五到兩萬就比真正的人體工學辦公椅便宜、坐起來又接近，所以第一還是它。"},
       {"title": "Herman Miller Vantum 是人體工學王", "body": "純姿勢支撐加 12 年保固，當你的腰就是一切、預算不是問題時就選它。這份專注讓它穩坐第二。"},
       {"title": "Corsair TC100 主宰預算層", "body": "它一直霸榜預算清單是有原因的，用旗艦零頭的價格給你紮實舒適。錢是限制的時候，它還是我第一個推的椅子。"},
       {"title": "Libernovo Omni 是可調性奇兵", "body": "它搭載榜上最會調的機構，等於電競外殼裡的辦公室級姿勢引擎。愛微調每個角度的人，它穩坐第三。"},
     ],
   })

# ---------------- best-handheld-gaming-consoles ----------------
do("best-handheld-gaming-consoles.json",
   [
     {"title": "Best gaming handhelds 2026 ranked", "url": "https://www.windowscentral.com/gaming-best-gaming-handhelds", "source": "Windows Central"},
     {"title": "The best gaming handhelds for 2026", "url": "https://tech.yahoo.com/gaming/article/the-best-gaming-handhelds-for-2026-180000267.html", "source": "Engadget / Yahoo"},
     {"title": "The best handheld gaming consoles in 2026", "url": "https://www.tomsguide.com/round-up/best-handheld-gaming-consoles", "source": "Tom's Guide"},
   ],
   {
     "commentary": "June 2026 brings one piece of news that sharpens my handheld ranking without overturning it: Valve hiked the Steam Deck OLED price by 240 dollars in May, citing memory and storage costs, which pushes the 1TB model to 790 and up. That makes the Deck a tougher value proposition, and it is exactly why I keep the Nintendo Switch 2 at number one. The Switch 2 is the best way to play Nintendo's exclusives, runs a 7.9-inch 1080p 120Hz screen, outputs 4K 120fps docked for supported games, and at its price it is simply the easiest recommendation for families and everyday players. The ROG Xbox Ally X holds second and remains the performance king of the PC handhelds, with its Ryzen Z2 Extreme, 24GB of RAM and up to 35W plugged in. For raw Windows gaming power it more or less wins by default among handhelds that do not cost close to a thousand dollars. The Steam Deck OLED stays third, because even after the price jump that gorgeous HDR OLED panel, the unmatched SteamOS experience and the best ergonomics on the board keep it essential, though the value math is now closer. Lenovo's Legion Go 2 holds fourth as the big-screen power option, and the MSI Claw 8 AI+ keeps fifth. The rest carries forward. My read: Switch 2 for most people, Ally X for PC power, Steam Deck for the SteamOS faithful who can stomach the new price.",
     "highlights": [
       {"title": "Switch 2 is still the easy pick for most", "body": "Best access to Nintendo exclusives, a 7.9-inch 1080p 120Hz screen and 4K 120fps docked, at a price families can swallow. After the Deck's hike it is an even clearer number one for everyday players."},
       {"title": "Steam Deck's price hike reshapes value", "body": "Valve raised the OLED by 240 dollars in May, pushing the 1TB model past 790. The panel and SteamOS still keep it third, but the value gap to the Ally X has narrowed and I would not pretend otherwise."},
       {"title": "ROG Xbox Ally X is the PC power king", "body": "Ryzen Z2 Extreme, 24GB of RAM and up to 35W docked make it the most powerful handheld that does not cost a fortune. For raw Windows gaming it wins second almost by default."},
       {"title": "SteamOS is still worth paying for", "body": "Even pricier, the Deck's HDR OLED, best-in-class ergonomics and the smoothest handheld OS keep it essential for the SteamOS faithful. It holds third because the experience, not the price, defines it."},
     ],
   },
   {
     "commentary": "2026 年 6 月有一條消息讓我的掌機排名更清晰，但沒翻盤，Valve 在 5 月把 Steam Deck OLED 漲了 240 美金，理由是記憶體跟儲存成本，1TB 版本因此被推到 790 美金起跳。這讓 Deck 的性價比變得比較尷尬，這也正是我把 Nintendo Switch 2 放第一的原因。Switch 2 是玩任天堂獨佔最好的方式，7.9 吋 1080p 120Hz 螢幕，接電視支援的遊戲能輸出 4K 120fps，以它的價格，對家庭跟日常玩家就是最好開口推薦的那台。ROG Xbox Ally X 守第二，依然是 PC 掌機裡的效能王，Ryzen Z2 Extreme、24GB 記憶體、插電最高 35W。論純 Windows 遊戲性能，在那些不到一千美金的掌機裡，它幾乎是不戰而勝。Steam Deck OLED 守第三，因為就算漲價了，那塊漂亮的 HDR OLED 面板、無人能及的 SteamOS 體驗、加上榜上最好的握持人體工學，還是讓它不可或缺，只是性價比這筆帳現在算得比較接近。Lenovo 的 Legion Go 2 守第四，是大螢幕性能選擇，MSI Claw 8 AI+ 守第五。其餘照舊。我的看法是，多數人選 Switch 2，要 PC 性能選 Ally X，吃得下新價格的 SteamOS 信徒選 Steam Deck。",
     "highlights": [
       {"title": "Switch 2 對多數人還是好選擇", "body": "玩任天堂獨佔最好的方式、7.9 吋 1080p 120Hz 螢幕、接電視 4K 120fps，價格家庭吞得下。Deck 漲價後，它對日常玩家是更清楚的第一。"},
       {"title": "Steam Deck 漲價重塑性價比", "body": "Valve 5 月把 OLED 漲 240 美金，1TB 版破 790。面板跟 SteamOS 還是讓它守第三，但跟 Ally X 的性價比差距縮小了，我不會假裝沒這回事。"},
       {"title": "ROG Xbox Ally X 是 PC 性能王", "body": "Ryzen Z2 Extreme、24GB 記憶體、接電 35W，是不貴掌機裡最強的。論純 Windows 遊戲性能，它幾乎不戰而勝拿下第二。"},
       {"title": "SteamOS 還是值得花這個錢", "body": "就算變貴，Deck 的 HDR OLED、同級最佳握持、最順的掌機系統，對 SteamOS 信徒還是不可或缺。守第三靠的是體驗而不是價格。"},
     ],
   })

# ---------------- best-standing-desks ----------------
do("best-standing-desks.json",
   [
     {"title": "Best standing desks of 2026", "url": "https://www.techradar.com/news/best-standing-desk", "source": "TechRadar"},
     {"title": "Best Standing Desk 2026: Our Top Picks After Testing 15+ Desks", "url": "https://testbeforeyoubuy.com/guides/office/best-standing-desk-2026", "source": "TestBeforeYouBuy"},
     {"title": "Standing Desk Brand Comparison: iMovR vs Uplift vs FlexiSpot", "url": "https://www.imovr.com/blogs/future-of-work/standing-desk-brand-comparison-imovr-vs-uplift-vs-flexispot", "source": "iMovR"},
   ],
   {
     "commentary": "Going into June 2026 my standing-desk ranking holds, and the UPLIFT V2 Commercial stays at number one because it is still the most customizable and durable desk a home office can buy. Cable management, a deep accessory ecosystem, rock-solid stability at standing height and a warranty that competitors struggle to match all keep it the consensus top pick for most setups. When someone wants one desk they will configure exactly and never replace, this is where I point them. The FlexiSpot E7 Pro holds a close second and is the value champion of the category, full stop. It delivers roughly 90 percent of premium-desk performance at a budget-friendly price, with a 440-pound capacity that beats desks costing twice as much, three-stage dual-motor legs and programmable memory. For most people who do not need Uplift's accessory depth, the E7 Pro is the smarter spend, and it is the desk I recommend more often than any other. Secretlab's MAGNUS Pro stays third as the premium all-in-one with the cleanest cable channel and magnetic ecosystem on the board. Branch Duo holds fourth on value and design, Vari fifth on reliability. Steelcase Migration SE remains the buy-it-for-life contract-grade option further down. Nothing this week reshuffled the order, so I held ranks. The honest split: Uplift for maximum customization, FlexiSpot E7 Pro for the best value, Secretlab for the cleanest premium setup. Pick your priority and any of the three will serve you for a decade.",
     "highlights": [
       {"title": "UPLIFT V2 Commercial is the durability king", "body": "Best-in-class cable management, the deepest accessory ecosystem and stability that holds at standing height keep it the consensus pick. For a desk you configure exactly and never replace, it stays number one."},
       {"title": "FlexiSpot E7 Pro is the value champion", "body": "Roughly 90 percent of premium performance at a budget price, with a 440-pound capacity that beats desks costing double. For most buyers it is the smarter spend and the one I recommend most often."},
       {"title": "Secretlab MAGNUS Pro owns clean setups", "body": "The cleanest cable channel and magnetic accessory ecosystem on the board make it the premium all-in-one. For a desk that looks immaculate with zero visible wires, it holds a strong third."},
       {"title": "Any top three lasts a decade", "body": "Uplift for customization, FlexiSpot for value, Secretlab for the cleanest premium build. These are decade-long purchases, so pick by your priority and none of them will let you down."},
     ],
   },
   {
     "commentary": "2026 年 6 月，我的升降桌排名守住，UPLIFT V2 Commercial 還是第一，因為它依然是家用辦公室能買到最會客製、最耐用的桌子。理線、龐大的配件生態、站立高度下穩如磐石、加上對手很難比的保固，全都讓它成為多數配置的共識首選。當有人想要一張會照自己需求調到精準、然後再也不用換的桌子，我就指向它。FlexiSpot E7 Pro 緊咬第二，是這個類別的性價比冠軍，沒得吵。它用親民的價格給你大約九成的旗艦桌效能，440 磅承重贏過貴一倍的桌子，三段式雙馬達桌腳加可程式記憶高度。對多數不需要 Uplift 那種配件深度的人，E7 Pro 是更聰明的花法，也是我推薦次數最多的桌子。Secretlab 的 MAGNUS Pro 守第三，是高階一體式，理線槽跟磁吸生態是榜上最乾淨的。Branch Duo 守第四，靠性價比跟設計，Vari 守第五，靠可靠度。Steelcase Migration SE 在再往下一點，是買一次用一輩子的商用級選擇。這週沒事件洗牌，所以我守住排名。講白了就是，要最大客製選 Uplift，要最佳性價比選 FlexiSpot E7 Pro，要最乾淨的高階配置選 Secretlab。選好你的優先順序，這三張隨便一張都能陪你用十年。",
     "highlights": [
       {"title": "UPLIFT V2 Commercial 是耐用王", "body": "同級最佳理線、最深的配件生態、站立高度仍穩，讓它成為共識首選。要一張調到精準、再也不換的桌子，第一還是它。"},
       {"title": "FlexiSpot E7 Pro 是性價比冠軍", "body": "親民價給你約九成旗艦效能，440 磅承重贏過貴一倍的桌子。對多數人是更聰明的花法，也是我推薦次數最多的那張。"},
       {"title": "Secretlab MAGNUS Pro 主宰乾淨配置", "body": "榜上最乾淨的理線槽跟磁吸配件生態，讓它成為高階一體式選擇。要一張看不到任何裸線、乾淨無瑕的桌子，它穩坐第三。"},
       {"title": "前三名隨便一張都能用十年", "body": "Uplift 客製、FlexiSpot 性價比、Secretlab 最乾淨。這都是十年級的購買，選好優先順序，這三張沒一張會讓你失望。"},
     ],
   })

# ---------------- best-3d-printers ----------------
do("best-3d-printers.json",
   [
     {"title": "Best 3D Printer 2026: 12 Models Tested and Compared", "url": "https://print2webcorp.com/best-3d-printer-tested-and-compared/", "source": "Print2Web"},
     {"title": "Bambu Lab vs Creality vs Prusa: The Definitive 2026 Comparison", "url": "https://adpindustries.com/blog/bambu-lab-vs-creality-vs-prusa-2026/", "source": "ADP Industries"},
     {"title": "Bambu vs Prusa vs Creality 2026 — Full Comparison Guide", "url": "https://layermath.com/blog/bambu-vs-prusa-vs-creality-2026", "source": "LayerMath"},
   ],
   {
     "commentary": "Heading into June 2026 the 3D-printer hierarchy holds, and the Bambu Lab P2S Combo stays at number one because it is simply the single best printer you can buy right now. At around 799 dollars it bundles an enclosed CoreXY, 500mm/s speeds, the AMS 2 Pro for clean four-color printing, an upgraded touchscreen and the best software ecosystem in consumer 3D printing. For the overwhelming majority of buyers, this is the answer, and nothing this month changes that. The fresh news is at the entry end: Bambu launched the A2L in June, a 330mm budget machine from 469 dollars with an optional cutting module, which is a great new on-ramp but slots below the flagship combos rather than challenging them. The X1-Carbon Combo holds second as the no-compromise flagship for those who want the absolute best print quality and do not blink at the price. The H2D stays third as the large-format, dual-nozzle powerhouse for makers who need the build volume and versatility. Prusa's CORE One keeps fourth as the best non-Bambu choice, the pick for open-source loyalists who value repairability and Prusa's legendary support, even at 1,199 assembled. The P1S holds fifth and remains my value-king recommendation for a first serious printer. Down the board Creality's K2 Plus, Elegoo's Centauri Carbon and the budget Ender 3 V3 SE carry forward. My read: P2S Combo for almost everyone, X1C for the perfectionist, Prusa for the tinkerer, P1S or the new A2L if money is tight.",
     "highlights": [
       {"title": "P2S Combo is the single best buy", "body": "Around 799 dollars gets enclosed CoreXY, 500mm/s, AMS 2 Pro four-color printing and the best software in consumer 3D printing. For the overwhelming majority of buyers it is the answer, so it stays number one."},
       {"title": "Bambu's new A2L widens the on-ramp", "body": "The June launch is a 330mm budget machine from 469 dollars with an optional cutting module. It is a great entry point, but it slots below the flagship combos rather than challenging the top of the board."},
       {"title": "X1-Carbon is the perfectionist's flagship", "body": "For buyers who want the absolute best print quality and do not blink at the price, it remains the no-compromise pick. That ceiling keeps it a deserved second behind the better-value P2S."},
       {"title": "Prusa CORE One is the best non-Bambu pick", "body": "Enclosed CoreXY, 500mm/s and legendary repairability and support make it the choice for open-source loyalists. Even at 1,199 assembled it earns its fourth spot for people who value owning every part."},
     ],
   },
   {
     "commentary": "2026 年 6 月，3D 列印機的階層守住，Bambu Lab P2S Combo 還是第一，因為它就是你現在能買到最好的單一機型。台幣大約兩萬五出頭，它就把封閉式 CoreXY、500mm/s 速度、能乾淨四色列印的 AMS 2 Pro、升級觸控螢幕、加上消費級 3D 列印裡最好的軟體生態，全部打包進去。對絕大多數買家，答案就是它，這個月沒有任何事改變這點。新消息在入門端，Bambu 6 月推出 A2L，330mm 的平價機種，台幣約一萬五起，可選切割模組，是很棒的新入門管道，但它落在旗艦 Combo 之下，而不是來挑戰它們。X1-Carbon Combo 守第二，是不妥協的旗艦，給想要絕對最佳列印品質、又不眨眼看價格的人。H2D 守第三，是大尺寸雙噴頭怪獸，給需要列印體積跟多功能性的玩家。Prusa 的 CORE One 守第四，是非 Bambu 裡最好的選擇，給重視可維修性跟 Prusa 傳奇級支援的開源死忠，就算組裝好要台幣三萬八也值得。P1S 守第五，依然是我推薦的第一台認真機種的性價比王。再往下，Creality K2 Plus、Elegoo Centauri Carbon、平價的 Ender 3 V3 SE 照舊。我的看法是，幾乎所有人選 P2S Combo，完美主義者選 X1C，愛動手的選 Prusa，預算緊就選 P1S 或新的 A2L。",
     "highlights": [
       {"title": "P2S Combo 是最強單一選擇", "body": "台幣約兩萬五出頭就有封閉 CoreXY、500mm/s、AMS 2 Pro 四色列印、加上消費級最好的軟體。對絕大多數買家就是答案，所以第一還是它。"},
       {"title": "Bambu 新 A2L 拓寬入門管道", "body": "6 月推出的 330mm 平價機種，台幣約一萬五起，可選切割模組。是很棒的入門點，但它落在旗艦 Combo 之下，不是來挑戰榜首的。"},
       {"title": "X1-Carbon 是完美主義者旗艦", "body": "想要絕對最佳列印品質、又不眨眼看價格的買家，它還是不妥協的選擇。這個天花板讓它穩居性價比更好的 P2S 之後、拿下第二。"},
       {"title": "Prusa CORE One 是非 Bambu 最佳", "body": "封閉 CoreXY、500mm/s、傳奇級可維修與支援，讓它成為開源死忠的選擇。就算組好要台幣三萬八，對重視能修每個零件的人，第四實至名歸。"},
     ],
   })

print("ALL DONE")
