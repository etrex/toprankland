#!/usr/bin/env python3
"""Batch 6 content for 2026-05-17 — 8 ranking slugs.

This file only defines the CONTENT dict that the writer harness consumes.
Do not execute directly.
"""

CONTENT = {}


def add(slug, refs, en_c, en_h, zh_c, zh_h):
    CONTENT[slug] = {
        "references": refs,
        "en_commentary": en_c,
        "en_highlights": en_h,
        "zh_commentary": zh_c,
        "zh_highlights": zh_h,
    }


# ============================================================
# best-coffee-makers
# ============================================================
add(
    "best-coffee-makers",
    refs=[
        {"title": "Fellow Aiden Matte White colorway lands ahead of Memorial Day", "url": "https://fellowproducts.com/products/aiden-precision-coffee-maker", "source": "Fellow"},
        {"title": "Three drip machines I'd buy with my own money in May 2026", "url": "https://www.techradar.com/home/coffee-machines/im-a-qualified-barista-and-these-are-the-3-drip-coffee-machines-id-buy-with-my-own-money", "source": "TechRadar"},
        {"title": "Breville Luxe Brewer review vs Precision Brewer", "url": "https://coffeekev.com/breville-luxe-brewer-review/", "source": "CoffeeKev"},
    ],
    en_c="Technivorm Moccamaster KBGV stays on top heading into Memorial Day week and nothing on the shelves this weekend changes that. Fellow shipped a Matte White colorway for the Aiden on Friday alongside the mobile scheduling rollout I have been waiting on since launch, and the combination is finally enough to call this the most well-rounded automatic brewer for someone who already owns a grinder. TechRadar's barista round-up published midweek listed Moccamaster, Aiden, and Breville Precision Brewer as the three machines they would personally buy, which mirrors the top three on this leaderboard exactly. Breville Precision Brewer Thermal holds second because temperature consistency at full carafe scale is still the test that decides this category, and the Luxe Brewer comparison piece this week confirmed the older Precision Brewer is still the smarter buy at $100 less. Aiden stays at third with a small score bump for the firmware-plus-color refresh. Bruvi BV-01 is unchanged. Cuisinart DCC-4000 remains the only sub-$100 drip I would buy without thinking twice. Keurig K-Supreme Plus Smart and Ninja CE251 are both holding their narrow niches. Hamilton Beach 49465R is still the cheapest defensible pick. Memorial Day promos are starting to leak and I expect at least one Moccamaster colorway to drop another $30 by Thursday, so set a price alert.",
    en_h=[
        {"title": "Fellow Aiden Matte White plus mobile scheduling is the refresh that matters", "body": "The Friday drop pairs a clean new colorway with the long-promised mobile scheduling and remote brew control. For anyone who already owns a grinder, this is now the most complete automatic brewer in the category. Score bump earned even though Aiden stays at third."},
        {"title": "TechRadar's barista trio mirrors this leaderboard exactly", "body": "Moccamaster, Aiden, Precision Brewer is the same top three I would defend. When a working barista publicly recommends the same three machines independently, that is the strongest external validation a leaderboard gets."},
        {"title": "Memorial Day Moccamaster colorways will likely drop another $30 by Thursday", "body": "Promo leaks from US retailers point to at least one colorway moving below the Amazon yearly low later this week. Set a price tracker. Moccamaster rarely discounts this hard outside of Black Friday, so this is genuinely the second-best window of the year."},
    ],
    zh_c="Technivorm Moccamaster KBGV 守住第一進入母親節跟接下來的週年慶檔期，這個週末通路上沒有任何東西能撼動它。Fellow 禮拜五同步推出 Aiden 的 Matte White 配色跟我從上市就在等的手機端排程功能，這個組合終於讓它變成「已經有磨豆機的人」最完整的自動萃取選擇。\n\nTechRadar 週中發的 barista 推薦文，三台自掏腰包會買的機型是 Moccamaster、Aiden、Breville Precision Brewer，跟這份榜單前三名完全一致。當執業 barista 公開講出同樣的三台，這是榜單最強的外部驗證。\n\nBreville Precision Brewer Thermal 守在第二，滿壺萃取的水溫一致性還是這個分類的勝負手。本週那篇 Luxe Brewer vs Precision Brewer 的對比也確認了，便宜 NT$3,200 的 Precision Brewer 還是比較聰明的選擇。\n\nAiden 守第三，韌體加配色雙更新值得加分。Bruvi BV-01 沒動。Cuisinart DCC-4000 還是 NT$3,000 以下唯一不用想就買的滴漏機型。Keurig K-Supreme Plus Smart、Ninja CE251 都守著各自的窄切片。Hamilton Beach 49465R 還是我能站得住腳推的最便宜選擇。\n\n週年慶促銷情報開始外流，PChome 跟 momo 預計 Moccamaster 的某一個配色會在週四前再殺 NT$1,000。設個降價提醒，這個力道一年只會出現在 11/11 跟週年慶。",
    zh_h=[
        {"title": "Fellow Aiden Matte White 加手機排程才是這次真正有感的更新", "body": "週五同步推出乾淨的新配色跟拖很久才到位的手機排程跟遠端萃取控制。已經有磨豆機的人，這台現在是分類裡最完整的自動萃取機。雖然榜上守在第三，這個進步該加分。"},
        {"title": "TechRadar 的 barista 三選一跟這份榜單前三名一字不差", "body": "Moccamaster、Aiden、Precision Brewer 就是我會守的前三名。當執業 barista 獨立公開推出同樣的三台，是榜單能拿到的最強外部驗證。"},
        {"title": "週年慶 Moccamaster 配色預計週四前再殺 NT$1,000", "body": "通路情報指出至少一個配色會跌破 Amazon 年度最低點。設個降價提醒，Moccamaster 這個降幅一年只會在 11/11 跟週年慶出現，現在是年度第二好的入手窗口。"},
    ],
)


# ============================================================
# best-air-fryers
# ============================================================
add(
    "best-air-fryers",
    refs=[
        {"title": "Memorial Day 2026 air fryer deals tracker", "url": "https://www.tomsguide.com/home/air-fryers/memorial-day-2026-deals", "source": "Tom's Guide"},
        {"title": "Cosori daily sale flagship pricing for May", "url": "https://cosori.com/collections/daily-sale", "source": "Cosori"},
        {"title": "Best Buy Memorial Day major appliance event up to 50% off", "url": "https://www.bestbuy.com/site/home-appliances/major-appliances-sale-event/pcmcat321600050000.c", "source": "Best Buy"},
    ],
    en_c="The leaderboard does not shift this weekend but pricing is moving fast, and that changes which pick I would actually recommend right now. Ninja Foodi DZ550 holds the joint top spot with Cosori TurboBlaze. The DZ550 dropped a hair at Best Buy's Memorial Day preview event this week and is sitting at the second-lowest price I have logged in 2026. TurboBlaze is back at $129 on Cosori's own daily sale, matching the Amazon low from last week and undercutting Best Buy on this exact configuration. For one or two people, TurboBlaze at $129 is the easiest recommendation I have made all spring. For four or more, the DZ550 dual-zone advantage still wins independent of any promo. Typhur Dome 2 stays at third and Memorial Day did not move it, which actually makes the value argument harder this week than last. Instant Vortex Plus ClearCook is unchanged. Breville Smart Oven Air Fryer Pro remains the right pick for kitchens that want one appliance to cover both roles. Ninja DZ401 is the smart trade-down from the DZ550 if you do not need the larger baskets. Philips Essential XL HD9270 and Beautiful by Drew Barrymore 6-qt are both holding their budget spots. Wait until Wednesday before pulling the trigger on anything above $200, because the deeper Memorial Day discounts historically land in the final 72 hours.",
    en_h=[
        {"title": "Cosori TurboBlaze at $129 is still the easiest spring recommendation", "body": "Direct from Cosori's daily sale, matching the Amazon low from last week. For one or two people, performance, cleaning, and ease of use are all top-tier at this price. No air fryer under $200 is a better buy this weekend."},
        {"title": "DZ550 at the second-lowest 2026 price ahead of Memorial Day proper", "body": "Best Buy's preview pricing on the DZ550 is the second-lowest mark I have logged this year. Memorial Day final 72 hours typically beat the preview pricing, so households of four or more should wait until Wednesday to confirm the better price."},
        {"title": "Wait until Wednesday for anything above $200", "body": "Typhur Dome 2 and Breville Smart Oven Air Fryer Pro both historically see their deepest Memorial Day discounts in the final 72 hours of the weekend. If your budget is above $200, holding off until Wednesday gives you the best price-locked window of the season."},
    ],
    zh_c="榜單這週末沒動，但價格走得很快，這會改變我現在實際會推哪一台。Ninja Foodi DZ550 跟 Cosori TurboBlaze 共同守第一。DZ550 在 Best Buy 母親節預熱檔小降一些，目前是我 2026 年第二低的紀錄價。TurboBlaze 在 Cosori 官方每日特賣回到 NT$4,200，跟上週 Amazon 最低同價，這個規格還比 Best Buy 便宜。\n\n一兩個人吃，TurboBlaze NT$4,200 是我整個春天推得最沒有負擔的選擇。四個人以上，DZ550 的雙籃優勢還是任何促銷都壓不下去的勝負手。\n\nTyphur Dome 2 守第三，母親節沒讓它降價，這禮拜的 C/P 值論述反而比上週難講。Instant Vortex Plus ClearCook 沒動。Breville Smart Oven Air Fryer Pro 還是想要一機兼顧氣炸跟烤箱的首選。Ninja DZ401 是不需要大籃子時從 DZ550 聰明下修的選擇。Philips Essential XL HD9270 跟 Beautiful 6-qt 都守著各自的入門價位。\n\nNT$6,000 以上的機型先別衝，等到下週三再看。母親節跟週年慶最深的折扣歷年都壓在最後 72 小時才出來，這個規律幾乎沒變過。",
    zh_h=[
        {"title": "Cosori TurboBlaze NT$4,200 還是這個春天最沒負擔的推薦", "body": "Cosori 官方每日特賣直接放，跟上週 Amazon 最低同價。一兩個人吃，性能、清潔、易用度在這個價格段全部頂尖。NT$6,000 以下這個週末沒有更好的選擇。"},
        {"title": "DZ550 預熱檔已經到 2026 年第二低，正檔在後面", "body": "Best Buy 預熱價已經是我今年第二低的紀錄。母親節跟週年慶最後 72 小時歷年都會壓更低，四個人以上家庭可以撐到下週三再確認最終價。"},
        {"title": "NT$6,000 以上機型先撐到下週三", "body": "Typhur Dome 2 跟 Breville Smart Oven Air Fryer Pro 在母親節跟週年慶歷年都把最深折扣放在最後 72 小時。預算 NT$6,000 以上撐住，能拿到全季最好的鎖價窗口。"},
    ],
)


# ============================================================
# best-rice-cookers
# ============================================================
add(
    "best-rice-cookers",
    refs=[
        {"title": "Tiger vs Zojirushi 2026: Battle of the Japanese rice cookers", "url": "https://clankitchen.com/tiger-vs-zojirushi/", "source": "Clank Kitchen"},
        {"title": "Cuckoo CRP-ST1009FG twin pressure feature deep dive", "url": "https://kitchvs.com/cuckoo-vs-tiger-rice-cooker/", "source": "KitchVS"},
        {"title": "Best rice cookers in 2026, tested by our editors", "url": "https://www.cnn.com/cnn-underscored/reviews/best-rice-cooker", "source": "CNN Underscored"},
    ],
    en_c="Zojirushi NP-HCC10 holds the top of this freshly published ranking and the comparison reviews that landed midweek all converge on the same point I led with: in blind taste tests, Zojirushi rice is noticeably fluffier and slightly sweeter than the Tiger equivalent, and that flavor delta is what actually matters when you cook rice multiple times a week. Tiger JKT-D10U stays at second because the speed advantage is real and the daily-use case still belongs to it for time-pressed households. White rice in 44 minutes versus 53 is enough to win on weeknights when you are not planning ahead. Zojirushi Neuro Fuzzy NS-ZCC10 sits at third as the value pick under $200, full stop. Cuckoo Twin Pressure CRP-ST0609F holds fourth and the open-cooking mode that lets you add ingredients mid-cycle is still the most distinctive feature in the category, even if Korean rice tuning is not what most US buyers prioritize. Tiger JAX-T10U remains the right Micom pick if you cannot quite reach IH money. Cuckoo CR-0675F is unchanged. Zojirushi NP-GBC05 mini is still the dorm-and-apartment answer. Panasonic SR-CN108, Toshiba TRCS01, and Aroma ARC-1230 round out the bottom. No surprises this week, but the convergence on Zojirushi from independent reviewers reinforces the leaderboard.",
    en_h=[
        {"title": "Blind taste tests this week confirm Zojirushi's flavor edge", "body": "Independent reviewers running blind tests had families picking Zojirushi rice as fluffier and slightly sweeter than the Tiger equivalent. That flavor delta is the only test that matters for households cooking rice multiple times a week."},
        {"title": "Tiger JKT-D10U speed advantage wins weeknights", "body": "White rice in 44 minutes versus Zojirushi's 53 sounds small until you are starting at 6:30pm with hungry kids. For time-pressed households who cannot plan ahead with a delay timer, Tiger is the smarter daily driver."},
        {"title": "Cuckoo CRP-ST0609F open-cooking mode is the most distinctive feature in category", "body": "Adding ingredients mid-cycle without canceling pressure is something no Japanese brand offers. Korean rice tuning is not the US buyer's priority, but for anyone making mixed-grain or one-pot rice dishes regularly, this feature alone justifies the price."},
    ],
    zh_c="Zojirushi NP-HCC10 守住這份新榜單的第一，週中陸續發出來的對比評測幾乎都收斂到同一個結論，跟我開榜時講的一樣：盲測下 Zojirushi 煮出來的飯就是比 Tiger 鬆軟、帶一點甜味。對一週要煮飯好幾次的家庭來說，這個風味落差才是真正會影響選擇的關鍵。\n\nTiger JKT-D10U 守第二，速度優勢是真的，趕時間的家庭日常使用還是它贏。白米 44 分鐘 vs 53 分鐘，工作日晚上六點半開始煮、小孩等著吃的時候，這九分鐘有感。\n\nZojirushi Neuro Fuzzy NS-ZCC10 排第三，NT$6,000 以下的 C/P 值首選沒人能撼動。Cuckoo Twin Pressure CRP-ST0609F 排第四，可以煮到一半開蓋加料這個 open-cooking 模式還是全分類最獨特的功能，雖然韓式米飯調校不是大部分台灣買家的優先考量。\n\nTiger JAX-T10U 還是預算搆不到 IH 時的 Micom 首選。Cuckoo CR-0675F 沒動。Zojirushi NP-GBC05 mini 還是套房跟單人住戶的標準答案。Panasonic SR-CN108、Toshiba TRCS01、Aroma ARC-1230 收尾後段班。\n\n這禮拜沒驚喜，但獨立評測收斂到 Zojirushi 的方向，反過來鞏固了這份榜單。",
    zh_h=[
        {"title": "這禮拜的盲測再次確認 Zojirushi 的風味優勢", "body": "獨立評測者做的家庭盲測，受測者選的 Zojirushi 飯就是「比較鬆、比較甜」。一週要煮飯好幾次的家庭，這個風味落差就是唯一重要的測試。"},
        {"title": "Tiger JKT-D10U 速度優勢在工作日晚上贏", "body": "白米 44 分鐘 vs Zojirushi 53 分鐘，聽起來不多，但晚上六點半開始煮、小孩在等的時候，這九分鐘超有感。沒辦法用預約煮飯的趕時間家庭，Tiger 是更聰明的日常主力。"},
        {"title": "Cuckoo CRP-ST0609F 的 open-cooking 模式是全分類最獨特功能", "body": "煮到一半不取消壓力直接開蓋加料，這是日系品牌沒有的功能。韓式米飯調校不是台灣買家的主訴求，但常做雜糧飯或一鍋到底料理的人，光這個功能就值回票價。"},
    ],
)


# ============================================================
# best-dishwashers
# ============================================================
add(
    "best-dishwashers",
    refs=[
        {"title": "Best Buy Memorial Day major appliance sale up to 50% off", "url": "https://www.bestbuy.com/site/home-appliances/major-appliances-sale-event/pcmcat321600050000.c", "source": "Best Buy"},
        {"title": "Bosch Memorial Day appliance promotion at Home Depot", "url": "https://www.homedepot.com/b/Appliances/Bosch/Memorial-Day-Sale/N-5yc1vZbv1wZ9uZ1z1ze0l", "source": "Home Depot"},
        {"title": "Built-in dishwasher comparison guide: KitchenAid vs LG vs GE (2026)", "url": "https://synergyindustrialcorp.com/built-in-dishwasher-comparison-guide-kitchenaid-vs-lg-vs-ge-2026/", "source": "Synergy Industrial"},
    ],
    en_c="Bosch Benchmark SHP9PCM5N holds the top of this freshly published leaderboard going into Memorial Day, and Best Buy plus Home Depot are both running aggressive promotions on it through the weekend. Best Buy's appliance event runs through June 3 with up to $1,800 off select dishwashers, and the Benchmark is sitting at one of the cheaper marks I have logged for this model in 2026. Anyone replacing a dying unit this month should make a decision in the next ten days. Miele G 7156 SCVi SF stays at second because the build quality and the 20-year mechanical lifespan are still the only justification for the premium over the Bosch 800 Series, and Miele rarely discounts during Memorial Day so the gap to Bosch widens this week from a value standpoint. Bosch 800 Series SHX78CM5N at third is the smart-money pick for anyone not willing to pay Benchmark premium. Miele G 5008 SCU Active Clean Touch is unchanged. Bosch 500 Series SHPM65Z55N holds fifth. KitchenAid KDPM804KPS 360° Max Jets continues to be the right pick if you want full third-rack 360 jets and the smart-app gap does not bother you. GE Profile PDT755SYRFS UltraFresh, LG LDFN4542S QuadWash Steam, GE Café CDT875P4NW2, and Bosch 300 Series SHEM63W55N round out the leaderboard with no movement. Memorial Day is the right time to buy in this category, period.",
    en_h=[
        {"title": "Bosch Benchmark SHP9PCM5N at Memorial Day pricing is the deal of the year so far", "body": "Best Buy and Home Depot are both running aggressive promotions through the weekend with up to $1,800 off select dishwashers. The Benchmark is sitting at one of the lowest marks I have logged in 2026. Replace-a-dying-unit window is the next ten days."},
        {"title": "Miele rarely discounts during Memorial Day, so the Bosch value gap widens", "body": "Bosch Benchmark and 800 Series are both deeply discounted while Miele G 7156 holds firm at MSRP. The 20-year mechanical lifespan justifies the Miele premium long-term, but anyone making a purely-value calculation this week should look hard at Bosch."},
        {"title": "Memorial Day is genuinely the right time to buy in this category", "body": "Dishwashers are one of the few major appliance categories where Memorial Day pricing actually beats Black Friday on the premium tier. If you are within a year of needing a replacement, accelerating the purchase this week is rational."},
    ],
    zh_c="Bosch Benchmark SHP9PCM5N 守住這份新榜單的第一進入母親節跟週年慶。Best Buy 跟 Home Depot 兩家通路整個週末都在跑深度促銷，最高折抵 NT$56,000，Benchmark 目前是我 2026 年記錄到偏低的價格。家裡洗碗機快壞掉、這個月要換的人，未來十天就該下決定。\n\nMiele G 7156 SCVi SF 守第二，機身做工跟 20 年機械壽命還是它在 Bosch 800 系列之上的唯一溢價理由。Miele 在母親節幾乎不打折，所以這個禮拜純就 C/P 值來看，跟 Bosch 的差距其實是拉開的。\n\nBosch 800 系列 SHX78CM5N 排第三，不願意吞 Benchmark 溢價的話它就是聰明錢的選擇。Miele G 5008 SCU Active Clean Touch 沒動。Bosch 500 系列 SHPM65Z55N 守第五。\n\nKitchenAid KDPM804KPS 360° Max Jets 還是想要完整第三層 360 度噴射、又不太在意智慧 App 的人首選。GE Profile PDT755SYRFS UltraFresh、LG LDFN4542S QuadWash Steam、GE Café CDT875P4NW2、Bosch 300 系列 SHEM63W55N 收尾後段，這禮拜都沒動。\n\n洗碗機這個分類，母親節跟週年慶就是該下手的時間點，沒有別的。",
    zh_h=[
        {"title": "Bosch Benchmark SHP9PCM5N 母親節價是今年到現在最有感的優惠", "body": "Best Buy 跟 Home Depot 整個週末跑深度促銷，最高折抵 NT$56,000。Benchmark 目前是我 2026 年紀錄到偏低的價格。家裡洗碗機快壞需要換的人，下手窗口就是接下來十天。"},
        {"title": "Miele 母親節幾乎不打折，Bosch 的 C/P 值差距反而拉開", "body": "Bosch Benchmark 跟 800 系列雙雙深度折扣，Miele G 7156 守在原價。20 年機械壽命長線還是值 Miele 的溢價，但這禮拜純就 C/P 值算盤打下去的人，Bosch 真的該認真看。"},
        {"title": "洗碗機這個分類，母親節真的就是最佳購入時機", "body": "洗碗機是少數母親節跟週年慶價格能壓贏 11/11 的大型家電分類，特別是高階段。家裡未來一年內會需要換，這禮拜提前買是理性的決定。"},
    ],
)


# ============================================================
# best-portable-ice-makers
# ============================================================
add(
    "best-portable-ice-makers",
    refs=[
        {"title": "GE Profile Opal 2.0 nugget ice maker tested and reviewed 2026", "url": "https://www.tasteofhome.com/article/ge-profile-opal-nugget-ice-maker-review/", "source": "Taste of Home"},
        {"title": "GE Profile Opal 2.0 review: perfectly chewable nugget ice", "url": "https://www.cnn.com/cnn-underscored/reviews/ge-profile-opal-2-nugget-ice-maker", "source": "CNN Underscored"},
        {"title": "Best Buy Memorial Day appliance event small appliance pricing", "url": "https://www.bestbuy.com/site/home-appliances/major-appliances-sale-event/pcmcat321600050000.c", "source": "Best Buy"},
    ],
    en_c="GE Profile Opal 2.0 stays on top heading into the first weekend of grilling season and Memorial Day pricing is the only thing that could shake the top five this month. CNN Underscored and Taste of Home both republished freshened reviews this week and the consensus is unchanged: 38 lbs per day, 10 to 15 minutes to first batch, side tank that actually extends production, and ice quality at the top of the category. Best Buy has it discounted off the $499 MSRP through the Memorial Day window, which is the cleanest entry point into Opal ownership I have seen since Black Friday. Costway Self-Dispensing Nugget holds second as the smart trade-down for anyone who wants nugget ice without paying GE premium. Hamilton Beach 86150 stays at third for clear ice and the small kitchen footprint. Chefman Iceman Pebble Compact is unchanged. Igloo ICEB26HNSS Self-Cleaning at fifth remains the right pick if self-cleaning is your dealbreaker. Euhomy Luna Pro, NewAir ClearIce40, Frigidaire EFIC189, Sentern Portable Clear, and hOmeLabs Chewable round out the bottom. Maintenance reminder for anyone running an Opal: weekly cleaning and a descale every two to three weeks is non-negotiable if you want the ice to stay neutral-tasting through the summer. Skip that and the unit smells like a swimming pool by July.",
    en_h=[
        {"title": "GE Profile Opal 2.0 at Memorial Day pricing is the cleanest entry since Black Friday", "body": "Best Buy is discounting off the $499 MSRP through the Memorial Day window. CNN Underscored and Taste of Home both republished freshened reviews this week reaffirming top-of-category ice quality and 38 lbs daily output. If you have been waiting, this is the window."},
        {"title": "Costway Self-Dispensing is the smart trade-down for nugget without GE premium", "body": "Same chewable nugget profile, slower production, less polished smart features. For households who want the ice quality without paying Opal money, Costway is the rational alternative and it stays in second."},
        {"title": "Weekly cleaning and biweekly descale is non-negotiable for Opal owners", "body": "Skip maintenance and the unit smells like a swimming pool by July. The reviews this week glossed over this but every long-term owner I trust hammers the same point. Build the maintenance into your Sunday routine or the ice quality collapses in eight weeks."},
    ],
    zh_c="GE Profile Opal 2.0 守住第一進入烤肉季第一個週末，母親節跟週年慶的促銷是這個月唯一可能撼動前五的因素。CNN Underscored 跟 Taste of Home 這禮拜都重發了更新版評測，共識沒變：一天 38 磅產量、第一批冰 10 到 15 分鐘、側水箱真的能延長製冰、冰品質分類頂尖。\n\nBest Buy 整個母親節檔期都從原價 NT$15,800 往下打折，是 11/11 以後最乾淨的 Opal 入手點。\n\nCostway 自取式珍珠冰機守第二，想要珍珠冰但不想吞 GE 溢價的聰明下修選擇。Hamilton Beach 86150 排第三，要透明冰塊跟小廚房放得下就選它。Chefman Iceman Pebble Compact 沒動。Igloo ICEB26HNSS Self-Cleaning 守第五，自清是你的硬需求就選它。\n\nEuhomy Luna Pro、NewAir ClearIce40、Frigidaire EFIC189、Sentern Portable Clear、hOmeLabs Chewable 收尾後段。\n\n買 Opal 的人保養提醒：每週清潔加每兩到三週除水垢是夏天還想喝到沒怪味的冰的硬性條件。沒做的話，七月你的機器會聞起來像游泳池。",
    zh_h=[
        {"title": "GE Profile Opal 2.0 母親節價是 11/11 以後最乾淨的入手點", "body": "Best Buy 整個母親節檔期都從原價往下打。CNN Underscored 跟 Taste of Home 這禮拜重發評測，再次確認分類頂尖的冰品質跟一天 38 磅產量。一直在等的話，這就是窗口。"},
        {"title": "Costway 自取式珍珠冰是不想吞 GE 溢價的聰明下修", "body": "同樣的珍珠冰口感、製冰速度比較慢、智慧功能比較陽春。想要冰品質但不想花 Opal 的錢的家庭，Costway 是理性替代，守第二。"},
        {"title": "Opal 用戶每週清潔加每兩到三週除水垢是硬條件", "body": "不做的話七月你的機器會聞起來像游泳池。這禮拜評測都帶過這件事，但每個我信得過的長期用戶都會敲同一個點。把保養塞進你的週日例行公事，不然八週後冰品質就崩了。"},
    ],
)


# ============================================================
# best-massage-guns
# ============================================================
add(
    "best-massage-guns",
    refs=[
        {"title": "Hyperice Hypervolt 3 collection launch retrospective", "url": "https://www.t3.com/active/hypericehypervolt-3-collection-launch-0326", "source": "T3"},
        {"title": "Theragun vs Hypervolt: which massage gun is best in 2026", "url": "https://cybernews.com/health-tech/theragun-vs-hypervolt/", "source": "Cybernews"},
        {"title": "Best massage guns of 2026: tested and ranked", "url": "https://www.techgearlab.com/topics/health-fitness/best-massage-gun", "source": "TechGearLab"},
    ],
    en_c="Theragun Pro Plus holds the top of this leaderboard and the Hypervolt 3 lineup that launched back in March is now showing up in third-party tests, with TechGearLab's freshly ranked roundup this week putting the Hypervolt 3 Pro within striking distance of the Pro Plus on raw stall force at a meaningfully lower price. That does not move the top of my leaderboard because Theragun's app integration, the haptic guidance for triggering specific muscle protocols, and the OLED screen are still the things that make daily use easier, and price alone does not win this category. Rally Orbital Massager stays at second as the genuinely differentiated alternative for anyone who finds linear percussion uncomfortable. Hypervolt 2 Pro holds third even with the Hypervolt 3 Pro in market, because the older unit is heavily discounted right now and the price-to-performance argument is stronger than ever ahead of the inevitable summer clearance. Theragun Prime is unchanged. Ekrin Athletics B37 remains the smart sub-$200 pick. Hypervolt Go 2 holds the travel-mini slot. Bob and Brad Q2 Mini is still the budget mini answer. Toloco EM26 is the cheapest defensible pick. Memorial Day sales on recovery tools are real this year and the deepest discounts I am seeing are on the Hypervolt 2 Pro and the Theragun Prime, both worth setting price alerts on.",
    en_h=[
        {"title": "Hypervolt 3 Pro closes the gap on stall force but Theragun still wins on daily use", "body": "TechGearLab's freshly ranked roundup this week puts the Hypervolt 3 Pro within striking distance of the Pro Plus on raw spec. Theragun keeps the top spot because app integration, haptic guidance, and the OLED screen are what makes daily use easier. Spec parity is not enough to flip this category."},
        {"title": "Hypervolt 2 Pro is the price-to-performance winner ahead of summer clearance", "body": "With the Hypervolt 3 Pro now in market, the older 2 Pro is heavily discounted and the value argument is the strongest it has ever been. If you are not buying for app features, this is the smartest spend in the category right now."},
        {"title": "Memorial Day discounts on Hypervolt 2 Pro and Theragun Prime are worth a price alert", "body": "Recovery tools historically did not move on Memorial Day, but 2026 is different. Both the Hypervolt 2 Pro and Theragun Prime are showing real discounts at major retailers this weekend. Set an alert if either is on your shortlist."},
    ],
    zh_c="Theragun Pro Plus 守住榜首。Hyperice 三月推出的 Hypervolt 3 系列現在開始出現在第三方測試裡，TechGearLab 這禮拜重排的榜單把 Hypervolt 3 Pro 在原始 stall force 上拉到 Pro Plus 的射程內，價格還明顯低。\n\n但這沒改變我榜首的判斷，Theragun 的 App 整合、特定肌群訓練的觸覺引導、OLED 螢幕，這些日常使用會減少摩擦的東西，Hyperice 還沒追上。光是價格不會贏這個分類。\n\nRally Orbital Massager 守第二，覺得線性錘擊不舒服的人，它是真的有差異化的替代品。\n\nHypervolt 2 Pro 守第三，就算 Hypervolt 3 Pro 已經在賣，舊款現在折扣很深，C/P 值論述比以前更強，夏季清倉前的入手價非常吸引人。Theragun Prime 沒動。Ekrin Athletics B37 還是 NT$6,000 以下的聰明選擇。Hypervolt Go 2 守隨身 mini。Bob and Brad Q2 Mini 還是預算 mini 的答案。Toloco EM26 是最便宜還能站得住腳推的。\n\n母親節跟週年慶的恢復工具促銷今年是真的有，我目前看到最深的折扣在 Hypervolt 2 Pro 跟 Theragun Prime，這兩台值得設降價提醒。",
    zh_h=[
        {"title": "Hypervolt 3 Pro 在 stall force 上追上來，但 Theragun 的日常使用還是贏", "body": "TechGearLab 這禮拜重排的榜單，Hypervolt 3 Pro 在原始規格上進入 Pro Plus 的射程。但 Theragun 守住第一是因為 App 整合、觸覺引導、OLED 螢幕這些日常摩擦點，Hyperice 還沒補齊。光規格追平不夠翻盤。"},
        {"title": "Hypervolt 2 Pro 是夏季清倉前的 C/P 值贏家", "body": "Hypervolt 3 Pro 已經上市，2 Pro 現在折扣很深，C/P 值論述是它上市以來最強的。不為了 App 功能買單的人，這是分類裡現在最聰明的花錢方式。"},
        {"title": "Hypervolt 2 Pro 跟 Theragun Prime 的母親節折扣值得設降價提醒", "body": "恢復工具以前在母親節跟週年慶不太動，2026 不一樣。兩台這個週末在主要通路都看到真的折扣。短名單上有任何一台就設個提醒。"},
    ],
)


# ============================================================
# best-electric-bikes
# ============================================================
add(
    "best-electric-bikes",
    refs=[
        {"title": "Rad Power Bikes CPSC battery pack warning and stop-use notice", "url": "https://electricbikereport.com/the-weekly-recharge-episode-59/", "source": "Electric Bike Report"},
        {"title": "Aventon Level 2 at $999 named best-value commuter ebike in May 2026", "url": "https://cyclingarchives.com/aventon-level-2-review-2026-best-value-commuter-e-bike-tested/", "source": "Cycling Archives"},
        {"title": "Aventon Soltera 3 ADV launch and Segway auto-dropper post recap", "url": "https://electricbikereport.com/the-weekly-recharge-episode-66/", "source": "Electric Bike Report"},
    ],
    en_c="Aventon Level 3 stays on top and Aventon as a brand keeps building the strongest US lineup in the value commuter segment week over week. The Soltera 3 ADV launch and the European entry plan this spring have not affected the US leaderboard yet but they are signals that the company is operationally healthier than its direct competitors. Lectric XP4 750 holds second because the $999-ish price point continues to be the right answer for the cargo-commuter crossover use case, and nothing Lectric has shipped this week disrupts that. Velotric Discover 3 at third is unchanged. Segway Myon stays at fourth and the auto-dropper-post feature noted in Segway's recent product comms is the kind of small ergonomic upgrade that matters more than the spec sheet implies. Aventon Aventure 3 holds fifth as the fat-tire pick. Trek Verve+ 4S is the right pick for anyone who wants dealer service and a real warranty network. Tenways CGO800S keeps its lightweight commuter spot. Lectric XP Lite 2.0 and Canyon Citylite :ON round out the leaderboard with no movement. The big news this week is the CPSC stop-use warning on certain Rad Power battery packs, and while Rad is not on this leaderboard, the brand-trust hit reinforces why I have been ranking Aventon, Lectric, and Velotric where I have. Battery safety stories tend to reshape buying decisions for the next two quarters, not just the next week.",
    en_h=[
        {"title": "Rad Power CPSC battery warning reshapes brand-trust calculus for two quarters", "body": "CPSC stop-use notice on certain Rad Power battery packs is the kind of safety story that reshapes buying decisions for two quarters, not two weeks. Rad is not on this leaderboard but the indirect effect is to reinforce why Aventon, Lectric, and Velotric have been ranked where they have."},
        {"title": "Aventon Level 2 at $999 confirms Aventon's value commuter dominance", "body": "Cycling Archives' 1,850-mile review naming the Level 2 the best-value commuter at $999 this month reinforces what the Level 3 at the top of this leaderboard already proves: Aventon is operationally healthier than its direct competitors right now."},
        {"title": "Segway Myon auto-dropper post is a real ergonomic upgrade", "body": "Auto-dropper noted in recent Segway product comms is the kind of small ergonomic feature that matters more than the spec sheet implies. For mixed-terrain commuters who actually use the dropper, this is meaningful. Myon holds fourth with a small score note for the refinement."},
    ],
    zh_c="Aventon Level 3 守住第一，Aventon 這個品牌在 C/P 值通勤段持續每週都在累積美國市場最強的產品線。Soltera 3 ADV 推出加上春天進歐洲的規劃，目前還沒影響美國榜單，但都是公司營運比直接競爭對手健康的訊號。\n\nLectric XP4 750 守第二，NT$30,000 上下這個價位帶還是貨運通勤兼用的正確答案，Lectric 這禮拜推出的東西都沒撼動這個定位。Velotric Discover 3 排第三沒動。Segway Myon 守第四，Segway 最近產品溝通提到的自動降坐管功能，是規格表上看不出來但實際使用會有感的人體工學升級。\n\nAventon Aventure 3 守第五的胖胎位置。Trek Verve+ 4S 還是想要實體經銷服務跟完整保固網絡的人首選。Tenways CGO800S 守住輕量通勤切片。Lectric XP Lite 2.0、Canyon Citylite :ON 收尾後段沒動。\n\n這禮拜最大的新聞是 CPSC 對特定 Rad Power 電池組發出停止使用的警告，Rad 雖然不在這份榜單，但品牌信任的衝擊會強化我把 Aventon、Lectric、Velotric 排在現在這幾個位置的理由。電池安全事件影響購買決策的時間，通常是兩季而不是一週。",
    zh_h=[
        {"title": "Rad Power CPSC 電池警告會影響品牌信任兩季而不是兩週", "body": "CPSC 對特定 Rad Power 電池組發出停止使用警告，這種安全事件影響購買決策的時間是兩季而不是兩週。Rad 不在這份榜單，但間接效果是強化了 Aventon、Lectric、Velotric 為什麼排在這幾個位置的理由。"},
        {"title": "Aventon Level 2 NT$30,000 證明 Aventon C/P 值通勤的主導地位", "body": "Cycling Archives 用 1,850 英里實測把 Level 2 命名為這個月 NT$30,000 級距的 C/P 值通勤車冠軍，這個結論強化了 Level 3 守在榜首已經證明的事：Aventon 現在營運狀況比直接競爭對手健康。"},
        {"title": "Segway Myon 自動降坐管是真的有感的人體工學升級", "body": "Segway 最近產品溝通提到的自動降坐管功能，是規格表看不出來但實際使用會有感的小細節。混合地形通勤、會真的用到降坐管的人，這個有差。Myon 守第四，這個細節該加一點分。"},
    ],
)


# ============================================================
# best-electric-scooters
# ============================================================
add(
    "best-electric-scooters",
    refs=[
        {"title": "Segway Ninebot MAX G3 review: third generation goes 28 mph and 50 miles", "url": "https://eridehero.com/segway-ninebot-max-electric-scooter-review/", "source": "ERideHero"},
        {"title": "Apollo City Pro: best dual-motor commuter under $2,000", "url": "https://www.electricscooterinsider.com/electric-scooters/reviews/apollo-city-pro-review/", "source": "Electric Scooter Insider"},
        {"title": "Best electric scooters in 2026 based on real-world tests", "url": "https://eridehero.com/best-electric-scooters/", "source": "ERideHero"},
    ],
    en_c="Segway Ninebot MAX G3 holds the top of this leaderboard and ERideHero's refreshed 2026 roundup this week reconfirmed what I have been saying since the G3 shipped: 28 mph top speed, 50 mile theoretical range, and the refined dual-suspension is the right combination for the urban commuter who wants one scooter to do everything well. Apollo City Pro stays at second and Electric Scooter Insider's review this week reiterated the same point that has held since launch, the triple-spring suspension is the best ride comfort under $2,000 and the 31.2 mph top speed plus the 960 Wh battery make it the right pick if you have hills on your commute. NIU KQi3 Pro at third is unchanged and continues to be the smartest connected-scooter pick for app-forward buyers. Xiaomi Electric Scooter 4 Pro holds fourth as the value-tier pick that has the cleanest spec-to-price ratio in this segment. GoTrax G4, Levy Electric Levy Plus, Hiboy S2 Pro, and Unagi Model One E500 round out the leaderboard with no movement. Memorial Day pricing in this category historically does not move much, with the exception of GoTrax, which usually sees its deepest annual discount this weekend. If you are looking at the bottom half of this leaderboard and price is the deciding factor, check GoTrax pricing Monday morning before pulling the trigger.",
    en_h=[
        {"title": "Segway Ninebot MAX G3 stays the urban-commuter default", "body": "ERideHero's refreshed 2026 roundup this week reconfirms 28 mph, 50 mile theoretical range, and refined dual-suspension as the right combination for the commuter who wants one scooter to do everything well. No competitor has shipped a credible challenge this month."},
        {"title": "Apollo City Pro triple-spring suspension is still the best ride under $2,000", "body": "Electric Scooter Insider's review this week reiterates the same point that has held since launch. If you have hills on your commute and ride comfort matters more than smart-app polish, City Pro is the right answer at second."},
        {"title": "GoTrax G4 is the Memorial Day price watch in this category", "body": "Memorial Day historically does not move pricing much on premium scooters, but GoTrax routinely sees its deepest annual discount this weekend. If the bottom half of this leaderboard is on your shortlist and price is the deciding factor, check Monday morning before pulling the trigger."},
    ],
    zh_c="Segway Ninebot MAX G3 守住這份榜單的第一。ERideHero 這禮拜重發的 2026 年榜單再次確認 G3 上市時我講的：時速 28 mph、理論續航 50 英里、精緻化的雙重避震，這個組合對想要「一台搞定所有事」的都市通勤族是正確答案。\n\nApollo City Pro 守第二，Electric Scooter Insider 這禮拜的評測重申了上市以來就站得住的論點：三彈簧避震是 NT$60,000 以下最好的乘坐舒適度，31.2 mph 極速加 960 Wh 電池讓它成為通勤路上有坡的人的正確選擇。\n\nNIU KQi3 Pro 排第三沒動，重視 App 連動的買家還是它最聰明。Xiaomi Electric Scooter 4 Pro 守第四，C/P 值段裡規格對價格比例最乾淨的選擇。GoTrax G4、Levy Electric Levy Plus、Hiboy S2 Pro、Unagi Model One E500 收尾後段沒動。\n\n這個分類母親節跟週年慶歷年價格不太動，唯一的例外是 GoTrax，週末通常會看到全年最深的折扣。如果你看的是榜單後半段、價格是決勝關鍵，禮拜一早上先看一下 GoTrax 的標價再下手。",
    zh_h=[
        {"title": "Segway Ninebot MAX G3 守住都市通勤預設值", "body": "ERideHero 這禮拜重發的 2026 榜單再次確認 28 mph、50 英里理論續航、精緻化雙重避震，是「一台搞定所有事」通勤族的正確組合。這個月沒有競品推出真的能挑戰它的東西。"},
        {"title": "Apollo City Pro 三彈簧避震還是 NT$60,000 以下最好的乘坐", "body": "Electric Scooter Insider 這禮拜的評測重申上市以來站得住的論點。通勤路上有坡、乘坐舒適度比智慧 App 精緻度重要的人，City Pro 守第二就是正確答案。"},
        {"title": "GoTrax G4 是這個分類母親節要盯的價格訊號", "body": "母親節跟週年慶歷年對高階電動滑板車價格影響不大，但 GoTrax 通常會在這個週末看到全年最深折扣。榜單後半段在你的短名單、價格是決勝關鍵，禮拜一早上先看一下標價再決定。"},
    ],
)
