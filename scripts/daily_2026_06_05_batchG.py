import sys; sys.path.insert(0, "/Users/etrexkuo/toprankland/scripts")
from daily_helper import load, save, upsert, last_rankings, DATE


def do(name, refs, en, zh):
    d, p = load(name)
    entry = {"date": DATE, "rankings": last_rankings(d), "references": refs, "i18n": {"en": en, "zh-tw": zh}}
    upsert(d, entry); save(p, d); print("updated", name)


# ---------------- best-air-fryers ----------------
do("best-air-fryers.json",
   [
     {"title": "The 6 Best Air Fryers of 2026", "url": "https://www.rtings.com/air-fryer/reviews/best/air-fryers", "source": "RTINGS"},
     {"title": "Ninja vs Instant Pot vs Cosori vs Typhur vs Chefman (Best Air Fryer?)", "url": "https://prudentreviews.com/ninja-vs-instant-pot-vs-cosori-vs-typhur-vs-chefman/", "source": "Prudent Reviews"},
   ],
   {
     "commentary": "Heading into June 2026 my air-fryer board holds exactly where it was, and the Ninja Foodi DZ550 keeps number one because the dual-basket question is still the one that matters most in a real kitchen. RTINGS just reaffirmed it as the best air fryer they test, and the reason is simple: ten quarts split into two independent zones means your wings and your fries finish at the same time at different temperatures, which is the trick a single-basket machine cannot pull off. The Cosori TurboBlaze stays a very close second and it is the one I hand to most people, because it delivers genuinely crispy results fast, runs quieter than the Ninja, and costs noticeably less for a single-basket nine-in-one. If your counter is tight and you cook for one or two, this is the smart buy. The Typhur Dome 2 holds third as the premium splurge: the largest flat cooking surface here, beautifully even browning, and a price that only makes sense if you cook big and cook often. The Instant Vortex Plus ClearCook ties it on the strength of a viewing window and the easiest cleanup on the board. Below that, the Breville Smart Oven, the Ninja DZ401, the Philips Essential XL, the Beautiful 6-quart and the Ninja Crispi all carry forward unchanged. Nothing launched this week that moves the order, so I held it and let the dual-zone-versus-value split frame the top. Pick the DZ550 for two dishes at once, the Cosori for everyday value, the Dome 2 if browning is everything.",
     "highlights": [
       {"title": "Ninja Foodi DZ550 owns the dual-basket job", "body": "Ten quarts across two independent zones finishes wings and fries together at different temperatures, which a single basket simply cannot do. RTINGS still rates it their best tested air fryer, and that family-feeding flexibility keeps it at number one."},
       {"title": "Cosori TurboBlaze is the everyday pick", "body": "Fast, genuinely crispy results in a quiet nine-in-one that costs noticeably less than the Ninja. For a tight counter and a household of one or two, this is the one I tell most people to buy, and it sits a deserved second."},
       {"title": "Typhur Dome 2 is the browning specialist", "body": "The largest flat cooking surface here delivers the most even browning on the board. The price only makes sense for someone who cooks big and often, which is exactly why it holds third as the premium splurge rather than the default."},
       {"title": "Instant Vortex Plus is the easy-clean champ", "body": "A clear viewing window and the simplest cleanup on the board make it the low-stress choice. It ties the Dome 2 on score because convenience earns real points for anyone who hates scrubbing a basket after dinner."},
     ],
   },
   {
     "commentary": "2026 年 6 月，我的氣炸鍋榜單原封不動，Ninja Foodi DZ550 守第一，因為「雙籃」這個問題在真實廚房裡還是最關鍵的。RTINGS 最近又把它列為測過最好的氣炸鍋，道理很簡單，十夸脫拆成兩個獨立區，你的雞翅跟薯條可以用不同溫度同時完成，這招單籃機器就是做不到。話說回來，Cosori TurboBlaze 緊咬第二，而且是我最常推給一般人的那台，因為它真的炸得又快又酥、運轉比 Ninja 安靜，單籃九合一的價格又明顯更親民。如果你家流理台不大、只煮一兩人份，這台買下去最聰明。Typhur Dome 2 守第三，是奢華加碼款，平面烤盤是榜上最大、上色超均勻，但這個價格只有你常常大量料理才划算。Instant Vortex Plus ClearCook 跟它同分，靠的是可視窗口跟榜上最好清的設計。再下面的 Breville 烤箱、Ninja DZ401、Philips Essential XL、Beautiful 六夸脫、Ninja Crispi 全部照舊。這週沒有新品動到排名，所以我守住，讓「雙區對性價比」這條線去帶前段。要同時煮兩道選 DZ550，要日常划算選 Cosori，上色至上就選 Dome 2。",
     "highlights": [
       {"title": "Ninja Foodi DZ550 主宰雙籃需求", "body": "十夸脫拆成兩個獨立區，雞翅跟薯條能用不同溫度同時完成，單籃機就是辦不到。RTINGS 仍評它為測過最好的氣炸鍋，這份餵飽全家的彈性讓它穩坐第一。"},
       {"title": "Cosori TurboBlaze 是日常首選", "body": "九合一炸得又快又酥、運轉安靜，價格又明顯比 Ninja 親民。流理台小、家裡一兩人份，我最常推這台，第二實至名歸。"},
       {"title": "Typhur Dome 2 是上色專家", "body": "平面烤盤是榜上最大，上色也最均勻。這價格只有常常大量料理才划算，所以它守第三、定位是奢華加碼，而不是預設首選。"},
       {"title": "Instant Vortex Plus 最好清洗", "body": "可視窗口加上榜上最簡單的清潔，是最不費神的選擇。它跟 Dome 2 同分，因為對討厭飯後刷籃子的人來說，方便就是實打實的加分。"},
     ],
   })

# ---------------- best-coffee-makers ----------------
do("best-coffee-makers.json",
   [
     {"title": "The Moccamaster is the coffee maker made to last a lifetime", "url": "https://www.tomsguide.com/home/coffee-makers/ive-tested-dozens-of-coffee-makers-heres-why-i-always-go-back-to-the-moccamaster", "source": "Tom's Guide"},
     {"title": "Fellow Aiden vs Moccamaster: The 2026 Brewer Showdown", "url": "https://stillwatercoffee.ca/blogs/brew_hacks/fellow-aiden-vs-moccamaster", "source": "Stillwater Coffee Club"},
   ],
   {
     "commentary": "Going into June 2026 my coffee-maker ranking holds, and the Technivorm Moccamaster KBGV Select stays number one for the reason it always has: it brews flawless coffee and it lasts a decade or more of daily use. Tom's Guide just reaffirmed this week why reviewers keep going back to it, and the case is durability plus brew quality with nothing to learn. Hand-built copper heating element, correct extraction temperature out of the box, and a machine you will still be using in 2036. The Breville Precision Brewer Thermal holds second as the versatile workhorse: it does drip, iced and cold brew with real temperature control, and it is the one I recommend when somebody wants to tinker without going full nerd. The Fellow Aiden sits third and it is the most interesting machine on the board. Its PID-controlled thermoblock adjusts temperature between water pulses and the touchscreen lets you dial bloom time and brew ratio, so reviewers now openly say it can out-brew both the Moccamaster and the Breville on a small batch. I keep it third only because the Moccamaster wins on proven longevity and simplicity, and that margin is thin. The Bruvi pod brewer, the Cuisinart DCC-4000, the Keurig K-Supreme, the Ninja CE251, the Hamilton Beach 49465R and the OXO Brew 9-Cup all carry forward. Nothing this week reshuffled them, so I held ranks and let the simplicity-versus-control split define the top three.",
     "highlights": [
       {"title": "Moccamaster KBGV is the lifetime buy", "body": "Flawless coffee from a hand-built copper element, correct extraction temperature with nothing to learn, and a body that survives a decade of daily brewing. Tom's Guide keeps going back to it, and that durability plus quality keeps it at number one."},
       {"title": "Breville Precision Brewer is the versatile workhorse", "body": "Drip, iced and cold brew with genuine temperature control in one machine. For the person who wants to experiment without studying coffee science, it is the most flexible pick on the board and a clear second."},
       {"title": "Fellow Aiden is the most advanced drip maker", "body": "Its PID thermoblock adjusts temperature between pulses and the touchscreen dials in bloom and ratio, and reviewers now say it out-brews both rivals on small batches. It holds third only because the Moccamaster wins on proven longevity."},
       {"title": "Cuisinart DCC-4000 is the value champion", "body": "It posts the highest value-for-money on the board with a programmable carafe that covers the everyday job for a fraction of the premium machines. For a reliable daily pot without the spend, it earns its mid-board spot."},
     ],
   },
   {
     "commentary": "2026 年 6 月，我的咖啡機排名守住，Technivorm Moccamaster KBGV Select 守第一的理由跟以前一樣，它煮出來的咖啡無懈可擊，每天用還能撐十年以上。Tom's Guide 這週又重申了為什麼評測者一再回頭選它，重點就是耐用加上品質、而且完全不用學。手工銅製加熱元件、開箱就是正確的萃取溫度，這台你到 2036 年都還會在用。Breville Precision Brewer Thermal 守第二，是多功能主力，滴漏、冰咖啡、冷萃都能做，還有真正的溫控，當有人想玩一下又不想變成咖啡宅，我就推這台。Fellow Aiden 排第三，是榜上最有看頭的機器。它的 PID 控溫加熱塊能在每次注水之間調溫，觸控螢幕讓你設定悶蒸時間跟粉水比，現在評測者已經公開說，小批量它能贏過 Moccamaster 跟 Breville。我把它擺第三，純粹是因為 Moccamaster 在「驗證過的耐用」跟「簡單」上勝出，而且差距其實很小。Bruvi 膠囊機、Cuisinart DCC-4000、Keurig K-Supreme、Ninja CE251、Hamilton Beach 49465R、OXO Brew 9-Cup 全部照舊。這週沒事件洗牌，所以我守住排名，讓「簡單對控制」這條線去定義前三。",
     "highlights": [
       {"title": "Moccamaster KBGV 是一輩子的投資", "body": "手工銅加熱元件煮出無懈可擊的咖啡，開箱就是正確萃取溫度、完全不用學，機身能撐十年每天沖煮。Tom's Guide 一再回頭選它，這份耐用加品質讓它穩坐第一。"},
       {"title": "Breville Precision Brewer 是多功能主力", "body": "一台搞定滴漏、冰咖啡、冷萃，還有真正的溫控。想實驗又不想鑽研咖啡科學的人，它是榜上最靈活的選擇，第二很明確。"},
       {"title": "Fellow Aiden 是最先進的滴漏機", "body": "PID 加熱塊在每次注水間調溫，觸控螢幕設定悶蒸跟粉水比，評測者現在說小批量它能贏兩個對手。它守第三純粹是 Moccamaster 在驗證過的耐用上勝出。"},
       {"title": "Cuisinart DCC-4000 是性價比冠軍", "body": "榜上性價比最高，可程式化壺身用零頭的價格就把日常工作做好。想要一台可靠的每日咖啡又不想花大錢，它穩穩待在中段。"},
     ],
   })

# ---------------- best-rice-cookers ----------------
do("best-rice-cookers.json",
   [
     {"title": "Best rice cookers in 2026, tested by our editors", "url": "https://www.cnn.com/cnn-underscored/reviews/best-rice-cooker", "source": "CNN Underscored"},
     {"title": "Zojirushi vs Tiger: Which Rice Cooker Is the Best?", "url": "https://prudentreviews.com/zojirushi-vs-tiger/", "source": "Prudent Reviews"},
   ],
   {
     "commentary": "In June 2026 my rice-cooker board holds, and the Zojirushi NP-HCC10 stays number one because induction heating is still the line between good rice and great rice. The whole inner pot becomes the heating element, so the cooker controls temperature with a precision that a single bottom plate cannot match, and the result is fluffy, evenly cooked grains across white, brown, sushi and mixed rice. The Tiger JKT-D10U holds a very close second and it genuinely cooks rice as well as the Zojirushi, with a stainless interior some buyers prefer and slightly more versatility. The only reason it sits behind is price: the Zojirushi delivers the same bowl for less, so it stays the better value. The Zojirushi Neuro Fuzzy NS-ZCC10 holds third and remains the smartest buy for most households, the fuzzy-logic workhorse that reviewers have recommended for nearly a decade. The Cuckoo Twin Pressure CRP-ST0609F stays fourth and is the one I point Korean-style cooks to, stickier rice and a fast 20-to-28-minute white-rice cycle. Below that the Tiger JAX-T10U, the Cuckoo CR-0675F, the Zojirushi mini, the Panasonic SR-CN108, the Toshiba TRCS01 and the Aroma ARC-1230 all carry forward unchanged. Nothing this week moved the order, so I held it. Buy induction if rice texture matters, the Neuro Fuzzy if value matters, the Cuckoo if you want it Korean-style and fast.",
     "highlights": [
       {"title": "Zojirushi NP-HCC10 wins on induction precision", "body": "The whole inner pot becomes the heating element, giving temperature control a single bottom plate cannot match. The payoff is fluffy, evenly cooked grains across every rice type, which is why it stays the number one pick."},
       {"title": "Tiger JKT-D10U cooks every bit as well", "body": "It matches the Zojirushi bowl for bowl, with a stainless interior some buyers prefer and a touch more versatility. It sits second only because the Zojirushi delivers the same result for less money, so value decides the order."},
       {"title": "Neuro Fuzzy NS-ZCC10 is the smartest buy", "body": "The fuzzy-logic workhorse reviewers have recommended for nearly a decade still nails white, brown and sushi rice at a friendly price. For most households it is the sweet spot, and it holds a deserved third."},
       {"title": "Cuckoo CRP-ST0609F is the Korean-style speedster", "body": "Twin-pressure cooking gives stickier, Korean-restaurant-style rice and a fast 20-to-28-minute white-rice cycle. For cooks who want that texture without the long wait, it stays the fourth-place specialist."},
     ],
   },
   {
     "commentary": "2026 年 6 月，我的電子鍋榜單守住，Zojirushi NP-HCC10 守第一，因為 IH 感應加熱還是「好吃的飯」跟「超好吃的飯」之間那條線。整個內鍋本身變成加熱體，溫控精準度是單一底盤比不上的，結果就是白米、糙米、壽司米、雜糧飯通通粒粒分明又均勻。Tiger JKT-D10U 緊咬第二，它煮飯真的跟 Zojirushi 一樣好，不鏽鋼內膽有些人更愛，功能也稍微多一點。它落後的唯一理由就是價格，Zojirushi 同樣一碗飯賣得更便宜，所以性價比還是它贏。Zojirushi Neuro Fuzzy NS-ZCC10 守第三，對多數家庭還是最聰明的選擇，這台模糊邏輯主力評測者推了快十年。Cuckoo 雙壓 CRP-ST0609F 守第四，是我會推給愛吃韓式飯的人那台，飯更黏、白米快煮只要 20 到 28 分鐘。再下面的 Tiger JAX-T10U、Cuckoo CR-0675F、Zojirushi 迷你款、Panasonic SR-CN108、Toshiba TRCS01、Aroma ARC-1230 全部照舊。這週沒事件動排名，所以我守住。在意口感買 IH、在意性價比買 Neuro Fuzzy、想要韓式又快就選 Cuckoo。",
     "highlights": [
       {"title": "Zojirushi NP-HCC10 贏在 IH 精準", "body": "整個內鍋變成加熱體，溫控精準度是單一底盤比不上的。回報就是各種米都粒粒分明又均勻，這就是它守第一的原因。"},
       {"title": "Tiger JKT-D10U 煮得一樣好", "body": "它一碗一碗跟 Zojirushi 不相上下，不鏽鋼內膽有些人更愛、功能也多一點。它排第二純粹是 Zojirushi 同樣結果賣更便宜，性價比決定了順序。"},
       {"title": "Neuro Fuzzy NS-ZCC10 是最聰明的選擇", "body": "這台模糊邏輯主力評測者推了快十年，白米、糙米、壽司米都煮得好、價格又親民。對多數家庭就是甜蜜點，第三實至名歸。"},
       {"title": "Cuckoo CRP-ST0609F 是韓式快煮王", "body": "雙壓煮出更黏的韓式餐廳口感，白米快煮只要 20 到 28 分鐘。想要那種口感又不想久等的人，它穩坐第四的專家位置。"},
     ],
   })

# ---------------- best-portable-ice-makers ----------------
do("best-portable-ice-makers.json",
   [
     {"title": "GE Profile Opal Nugget Ice Maker: Tested & Reviewed in 2026", "url": "https://www.tasteofhome.com/article/ge-profile-opal-nugget-ice-maker-review/", "source": "Taste of Home"},
     {"title": "8 Best Ice Makers: GE Profile Opal, GoveeLife, Frigidaire of 2026", "url": "https://www.reviewed.com/cooking/best-right-now/best-ice-machines", "source": "Reviewed"},
   ],
   {
     "commentary": "Heading into June 2026 my ice-maker board holds, and the GE Profile Opal 2.0 stays number one because nobody else makes nugget ice this good at home. That soft, chewable, Sonic-style pellet is the whole reason people buy a countertop machine, and the Opal nails it, then adds a one-gallon detachable side tank and SmartHQ scheduling so you can run it overnight and wake to a full bin. Reviewed and Taste of Home both reaffirmed it as their top pick this season. The honest caveat: at around 419 dollars it costs roughly three times the budget machines, and the first batch takes about ten minutes. That price gap is exactly why the Costway Self-Dispensing nugget holds second, it makes the same chewable ice, dispenses straight into a glass, and undercuts the Opal hard, which is why I send value hunters there first. The Hamilton Beach 86150 stays third as the quiet bullet-ice champ, fast, cheap and nearly silent for anyone who just wants cold drinks. The Chefman Iceman, the Euhomy Luna Pro, the NewAir ClearIce40, the Igloo, the hOmeLabs nugget, the Sentern clear maker and the Frigidaire EFIC189 all carry forward unchanged. Nothing this week reshuffled the order, so I held ranks. Buy the Opal for the best nugget ice, the Costway to get that texture for less, the Hamilton Beach if quiet and cheap is the brief.",
     "highlights": [
       {"title": "GE Profile Opal 2.0 owns nugget ice", "body": "Nobody makes that soft, chewable Sonic-style pellet at home better, and the detachable side tank plus SmartHQ overnight scheduling seal it. Reviewed and Taste of Home both name it their top pick, so it stays number one."},
       {"title": "Costway Self-Dispensing is the value nugget", "body": "It makes the same chewable ice, dispenses straight into your glass, and undercuts the Opal by a wide margin. For anyone who wants that texture without the premium spend, it is the one I recommend first, a clear second."},
       {"title": "Hamilton Beach 86150 is the quiet pick", "body": "Fast, cheap and nearly silent, it is the bullet-ice champ for anyone who just wants cold drinks without the nugget premium. That low-stress simplicity keeps it solidly in third on the board."},
       {"title": "The Opal price gap is real but earned", "body": "At around 419 dollars it runs roughly three times the budget machines and takes about ten minutes for the first batch. I keep the verdict honest, yet the nugget quality and overnight convenience justify the spend for ice lovers."},
     ],
   },
   {
     "commentary": "2026 年 6 月，我的製冰機榜單守住，GE Profile Opal 2.0 守第一，因為在家做出這麼好的綿綿冰，沒人比得上它。那種軟軟、可以嚼、像得來速 Sonic 那樣的小冰粒，正是大家買桌上型製冰機的全部理由，Opal 把它做到位，還加上一加侖可拆側水箱跟 SmartHQ 排程，讓你半夜開機、早上醒來就有滿桶冰。Reviewed 跟 Taste of Home 這季都重申它是首選。誠實說一句但書，它大約 419 美金，差不多是入門機的三倍，第一批冰要等約十分鐘。這個價差正是 Costway 自動出冰款守第二的原因，它做一樣的綿綿冰、能直接出到杯子裡，價格又狠狠壓在 Opal 之下，所以想省錢的我第一個推它。Hamilton Beach 86150 守第三，是安靜的子彈冰王，又快又便宜、幾乎無聲，適合只想要冰飲的人。Chefman Iceman、Euhomy Luna Pro、NewAir ClearIce40、Igloo、hOmeLabs 綿綿冰、Sentern 透明冰、Frigidaire EFIC189 全部照舊。這週沒事件洗牌，所以我守住排名。要最好的綿綿冰買 Opal，想用更少錢拿到那口感選 Costway，要安靜又便宜就選 Hamilton Beach。",
     "highlights": [
       {"title": "GE Profile Opal 2.0 主宰綿綿冰", "body": "那種軟軟、可嚼、像得來速的小冰粒，在家做沒人比它好，可拆側水箱加 SmartHQ 過夜排程更是加分。Reviewed 跟 Taste of Home 都選它首選，所以第一是它。"},
       {"title": "Costway 自動出冰是性價比綿綿冰", "body": "它做一樣的綿綿冰、能直接出到杯子裡，價格又大幅壓在 Opal 之下。想要那口感又不想花大錢的人，我第一個推它，第二很明確。"},
       {"title": "Hamilton Beach 86150 是安靜選擇", "body": "又快又便宜、幾乎無聲，是只想要冰飲、不想為綿綿冰加價的人的子彈冰王。這份低負擔的簡單讓它穩穩待在第三。"},
       {"title": "Opal 的價差是真的但值得", "body": "約 419 美金、差不多是入門機三倍，第一批冰要等約十分鐘。我把話講白，但綿綿冰的品質跟過夜便利，對愛冰的人來說這錢花得值。"},
     ],
   })

# ---------------- best-gas-grills ----------------
do("best-gas-grills.json",
   [
     {"title": "Best Gas Grill Brands of 2026", "url": "https://www.consumerreports.org/home-garden/grills/best-gas-grill-brands-a1186225024/", "source": "Consumer Reports"},
     {"title": "Napoleon VS Weber: Which Gas Grill is Best in 2026?", "url": "https://www.smokedbbqsource.com/napoleon-vs-weber/", "source": "Smoked BBQ Source"},
   ],
   {
     "commentary": "With grilling season fully open in June 2026 my gas-grill board holds, and the Weber Spirit E-425 stays number one because it is the best balance of cooking power, build and value Weber makes right now. The GS4 grilling system gives you reliable ignition, even heat across the grates and the durability Weber is famous for, and the four-burner layout with a sear station handles a full backyard cook without the Genesis price. The Weber Genesis E-325 holds a close second as the step-up: a dedicated sear zone, sturdier cookbox and CRAFTED accessory compatibility that turns weekend grilling into something more serious, and reviewers love the steakhouse-quality cook it delivers. If you want premium without going luxury, this is the one. The Napoleon Prestige 500 RSIB stays third and earns it on raw heat output, infrared side and rear burners plus a lifetime bumper-to-bumper warranty that no Weber matches. It sits behind only on value, because you pay for that firepower. The Weber Summit S-470, the Genesis SX-335 Smart, the Broil King Regal S590, the Spirit E-310, the Bull Lonestar, the Char-Broil Performance, the Monument Mesa and the Royal Gourmet all carry forward. Nothing this week reshuffled the order, so I held it. Buy the Spirit E-425 for the best all-round value, the Genesis E-325 to step up, the Napoleon for sheer firepower and a lifetime warranty.",
     "highlights": [
       {"title": "Weber Spirit E-425 is the value champion", "body": "The GS4 system delivers reliable ignition, even heat and Weber durability, and four burners with a sear station cover a full backyard cook below the Genesis price. That balance of power and value keeps it at number one."},
       {"title": "Weber Genesis E-325 is the step-up pick", "body": "A dedicated sear zone, sturdier cookbox and CRAFTED accessory support earn it a steakhouse-quality cook reviewers rave about. For premium without going full luxury, it is the natural upgrade and a clear second."},
       {"title": "Napoleon Prestige 500 leads on firepower", "body": "Infrared side and rear burners plus a lifetime bumper-to-bumper warranty no Weber matches make it the heat-and-coverage champion. It sits third only because that firepower comes at a price, so value decides the order."},
       {"title": "Weber Spirit E-310 is the budget standout", "body": "It posts the highest value score on the board, the entry Weber that still brings GS4 reliability and even heat for far less. For a first serious grill without overspending, it remains the smart compact buy."},
     ],
   },
   {
     "commentary": "2026 年 6 月烤肉季全面開打，我的瓦斯烤爐榜單守住，Weber Spirit E-425 守第一，因為它是 Weber 目前火力、做工、性價比平衡得最好的一台。GS4 點火系統給你可靠點火、爐架受熱均勻，加上 Weber 招牌的耐用度，四燒爐配煎烤站能應付一整場後院烤肉，又不用付 Genesis 的價。Weber Genesis E-325 緊咬第二，是升級款，獨立煎烤區、更紮實的爐箱、CRAFTED 配件相容，把週末烤肉變得更講究，評測者很愛它牛排館等級的成果。想要高階又不到奢華等級，就選這台。Napoleon Prestige 500 RSIB 守第三，靠的是純火力，紅外線側燒跟後燒爐加上沒有任何 Weber 比得上的終身全機保固。它落後只在性價比，因為那份火力你得付錢。Weber Summit S-470、Genesis SX-335 Smart、Broil King Regal S590、Spirit E-310、Bull Lonestar、Char-Broil Performance、Monument Mesa、Royal Gourmet 全部照舊。這週沒事件洗牌，所以我守住。要全方位性價比選 Spirit E-425，要升級選 Genesis E-325，要純火力加終身保固選 Napoleon。",
     "highlights": [
       {"title": "Weber Spirit E-425 是性價比冠軍", "body": "GS4 系統給你可靠點火、均勻受熱跟 Weber 耐用度，四燒爐配煎烤站能搞定整場後院烤肉，價格又在 Genesis 之下。這份火力與性價比的平衡讓它守第一。"},
       {"title": "Weber Genesis E-325 是升級首選", "body": "獨立煎烤區、更紮實爐箱、CRAFTED 配件支援，烤出評測者讚不絕口的牛排館等級成果。想要高階又不到奢華，它是自然的升級、第二很明確。"},
       {"title": "Napoleon Prestige 500 火力最猛", "body": "紅外線側燒、後燒爐加上沒有 Weber 比得上的終身全機保固，是火力與覆蓋的王者。它排第三純粹因為那份火力要付錢，性價比決定了順序。"},
       {"title": "Weber Spirit E-310 是預算亮點", "body": "它是榜上性價比最高的，入門 Weber 仍帶來 GS4 可靠度跟均勻受熱、價格卻低很多。想要第一台像樣的烤爐又不超支，它還是聰明的精巧之選。"},
     ],
   })

# ---------------- best-outdoor-griddles ----------------
do("best-outdoor-griddles.json",
   [
     {"title": "The Best Outdoor Griddle for 2026", "url": "https://thebarbecuelab.com/best-outdoor-griddle/", "source": "The Barbecue Lab"},
     {"title": "Blackstone Griddle vs Traeger Flatrock", "url": "https://www.smokedbbqsource.com/blackstone-griddle-vs-traeger-flatrock/", "source": "Smoked BBQ Source"},
   ],
   {
     "commentary": "Heading into June 2026 my griddle board holds, and the Camp Chef Gridiron 36 stays number one because it brings the most complete package on a flat top: a lid, the best grease management on the board, even heat across four zones and a build that feels a tier above the price. For a little more than the Blackstone you get features that genuinely add up, which is why it leads. The Blackstone Original 36 Omnivore holds second and remains the best buy for most people, 720 square inches, 60,000 BTUs and a hood for around 400 dollars, the value benchmark every other griddle is measured against. If you want a huge, even cooking surface and do not want to overthink it, this is the default. The Traeger Flatrock 3-Zone stays third and it is the wind champion, a sunk-down surface and U-shaped baffled burners that hold temperature when a breeze would wreck a Blackstone, testers measured the smallest temperature swing in gusts. It sits third only on value, because that engineering costs more. The Weber Slate, the Blackstone Iron Forged, the Pit Boss Ultimate, the Traeger Flatrock 2-Zone, the Nexgrill Daytona and the Royal Gourmet all carry forward. Nothing this week moved the order, so I held it. Buy the Camp Chef for the most complete package, the Blackstone for unbeatable value, the Traeger if you cook somewhere windy.",
     "highlights": [
       {"title": "Camp Chef Gridiron 36 is the complete package", "body": "A lid, the best grease management on the board, even four-zone heat and a build a tier above the price. For a little more than the Blackstone you get features that genuinely add up, which is why it leads at number one."},
       {"title": "Blackstone Original 36 is the value benchmark", "body": "720 square inches, 60,000 BTUs and a hood for around 400 dollars make it the buy most people should make. For a huge, even surface without overthinking it, it is the default second-place pick everyone measures against."},
       {"title": "Traeger Flatrock 3-Zone wins in wind", "body": "A sunk-down surface and U-shaped baffled burners hold temperature when a breeze would wreck a Blackstone, and testers measured the smallest swing in gusts. That engineering keeps it third, behind only on value."},
       {"title": "Weber Slate brings rust resistance", "body": "Its rust-resistant top tackles the one maintenance headache that scares off griddle buyers, backed by Weber build quality. For anyone who hates seasoning and worrying about corrosion, it stays a strong fourth."},
     ],
   },
   {
     "commentary": "2026 年 6 月，我的鐵板燒榜單守住，Camp Chef Gridiron 36 守第一，因為它在平面鐵板上端出最完整的組合，有上蓋、榜上最好的集油系統、四區均勻受熱，做工也比這個價位該有的高一階。只比 Blackstone 多花一點點，你拿到的功能是實打實累加起來的，這就是它領先的原因。Blackstone Original 36 Omnivore 守第二，對多數人還是最划算的選擇，720 平方吋、60,000 BTU、附上蓋，價格約 400 美金，是其他鐵板都拿來比較的性價比標竿。想要超大又均勻的烤面、又不想想太多，這台就是預設。Traeger Flatrock 3-Zone 守第三，是抗風王，下沉式烤面加上 U 形擋板燒爐，在會把 Blackstone 搞砸的微風裡照樣穩住溫度，測試者量到陣風中溫差最小。它排第三只在性價比，因為這份工程要多花錢。Weber Slate、Blackstone Iron Forged、Pit Boss Ultimate、Traeger Flatrock 2-Zone、Nexgrill Daytona、Royal Gourmet 全部照舊。這週沒事件動排名，所以我守住。要最完整組合選 Camp Chef，要無敵性價比選 Blackstone，常在有風的地方煮就選 Traeger。",
     "highlights": [
       {"title": "Camp Chef Gridiron 36 是最完整組合", "body": "有上蓋、榜上最好的集油、四區均勻受熱、做工高一階。只比 Blackstone 多一點點，拿到的功能實打實累加，這就是它領先第一的原因。"},
       {"title": "Blackstone Original 36 是性價比標竿", "body": "720 平方吋、60,000 BTU、附上蓋，約 400 美金，是多數人該買的那台。想要超大均勻烤面又不想想太多，它就是預設的第二名、大家都拿來比較。"},
       {"title": "Traeger Flatrock 3-Zone 抗風最強", "body": "下沉式烤面加 U 形擋板燒爐，在會搞砸 Blackstone 的微風裡照樣穩溫，測試者量到陣風溫差最小。這份工程讓它守第三，只輸在性價比。"},
       {"title": "Weber Slate 帶來抗鏽", "body": "抗鏽烤面解決了嚇跑鐵板買家的那個保養痛點，背後是 Weber 做工。討厭養鍋又怕生鏽的人，它穩坐強勢第四。"},
     ],
   })

# ---------------- best-dishwashers ----------------
do("best-dishwashers.json",
   [
     {"title": "Best (and Worst) Dishwashers of 2026, Lab-Tested and Reviewed", "url": "https://www.consumerreports.org/appliances/dishwashers/best-dishwashers-of-the-year-a6109623431/", "source": "Consumer Reports"},
     {"title": "Bosch vs. Miele Dishwashers (2026): Reliability, Wash vs. Dry, and Price-Band Matchups", "url": "https://blog.yaleappliance.com/bosch-vs-miele-dishwashers", "source": "Yale Appliance"},
   ],
   {
     "commentary": "Going into June 2026 my dishwasher board holds, and the Bosch Benchmark SHP9PCM5N stays number one because Consumer Reports just put it at the top of their 2026 rankings, calling it exceptional at washing and drying while staying nearly silent. At 38 dBA it is one of the quietest machines you can buy, and the CrystalDry system finally solves the plastic-drying problem that used to be Bosch's one weak spot. For a quiet, open-concept kitchen this is the machine I recommend without hesitation. The Miele G 7156 SCVi SF holds a close second and it is the reliability king, Yale's data has Miele as the most reliable dishwasher brand for 2026 at roughly 5.6 percent service, ahead of Bosch in the first year, and the build quality justifies the premium for anyone planning to keep it twenty years. The Bosch 800 Series SHX78CM5N stays third as the value-smart flagship, almost all of the Benchmark's performance for noticeably less. The Miele G 5008, the Bosch 500 Series, the KitchenAid KDPM804, the GE Profile, the LG QuadWash, the Café and the Bosch 300 Series all carry forward. Nothing this week reshuffled the order, so I held it. Buy the Benchmark for the quietest top performer, the Miele for the longest life, the Bosch 800 for most of the Benchmark at a better price.",
     "highlights": [
       {"title": "Bosch Benchmark SHP9PCM5N tops the board", "body": "Consumer Reports just named it the best of 2026, exceptional at washing and drying at a near-silent 38 dBA, with CrystalDry solving the old plastic-drying weak spot. For a quiet open kitchen it is my no-hesitation number one."},
       {"title": "Miele G 7156 is the reliability king", "body": "Yale's 2026 data makes Miele the most reliable dishwasher brand at roughly 5.6 percent service, ahead of Bosch in year one. The build quality justifies the premium for anyone keeping a machine two decades, a clear second."},
       {"title": "Bosch 800 Series is the value-smart flagship", "body": "It delivers almost all of the Benchmark's wash, dry and quiet performance for noticeably less money. For buyers who want flagship results without the flagship price, it is the sweet spot and holds a solid third."},
       {"title": "Bosch 300 Series is the budget standout", "body": "It posts the highest value score on the board, bringing genuine Bosch cleaning and quiet operation at an entry price. For a reliable, quiet dishwasher without overspending, it remains the smart pick lower on the board."},
     ],
   },
   {
     "commentary": "2026 年 6 月，我的洗碗機榜單守住，Bosch Benchmark SHP9PCM5N 守第一，因為 Consumer Reports 剛把它放上 2026 排名榜首，說它洗淨跟烘乾都出色、運轉又幾乎無聲。38 分貝是你買得到最安靜的機種之一，CrystalDry 系統也終於解決了過去 Bosch 唯一的弱點，塑膠餐具烘不乾。開放式廚房想要安靜，這台我毫不猶豫推薦。Miele G 7156 SCVi SF 緊咬第二，是耐用之王，Yale 的數據把 Miele 列為 2026 最可靠的洗碗機品牌、維修率約 5.6%，第一年領先 Bosch，做工品質對打算用二十年的人來說，這個溢價付得值。Bosch 800 系列 SHX78CM5N 守第三，是性價比聰明的旗艦，幾乎拿到 Benchmark 全部的表現、價格卻明顯更低。Miele G 5008、Bosch 500 系列、KitchenAid KDPM804、GE Profile、LG QuadWash、Café、Bosch 300 系列全部照舊。這週沒事件洗牌，所以我守住。要最安靜的頂級表現選 Benchmark，要用最久選 Miele，要 Benchmark 大部分實力又更便宜選 Bosch 800。",
     "highlights": [
       {"title": "Bosch Benchmark SHP9PCM5N 登頂", "body": "Consumer Reports 剛把它選為 2026 最佳，洗淨烘乾都出色、38 分貝幾乎無聲，CrystalDry 解決了過去塑膠烘不乾的弱點。開放式廚房想安靜，它是我毫不猶豫的第一。"},
       {"title": "Miele G 7156 是耐用之王", "body": "Yale 的 2026 數據把 Miele 列為最可靠品牌、維修率約 5.6%，第一年領先 Bosch。做工對打算用二十年的人來說溢價付得值，第二很明確。"},
       {"title": "Bosch 800 系列是性價比旗艦", "body": "它幾乎拿到 Benchmark 全部的洗淨、烘乾、安靜表現，價格卻明顯更低。想要旗艦結果又不想付旗艦價的人，它就是甜蜜點，穩坐第三。"},
       {"title": "Bosch 300 系列是預算亮點", "body": "它是榜上性價比最高的，用入門價帶來真正的 Bosch 洗淨跟安靜運轉。想要可靠又安靜的洗碗機又不想超支，它還是榜單後段的聰明選擇。"},
     ],
   })

print("ALL DONE")
