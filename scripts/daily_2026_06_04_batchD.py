import sys; sys.path.insert(0, "/Users/etrexkuo/toprankland/scripts")
from daily_helper import load, save, upsert, last_rankings, DATE

updates = {}

# ---------------- AIR FRYERS ----------------
updates["best-air-fryers.json"] = {
  "references": [
    {"title": "The 6 Best Air Fryers of 2026", "url": "https://www.rtings.com/air-fryer/reviews/best/air-fryers", "source": "RTINGS"},
    {"title": "6 Best Air Fryers of 2026, Lab-Tested and Reviewed", "url": "https://www.consumerreports.org/appliances/air-fryers/best-air-fryers-of-the-year-a3919863393/", "source": "Consumer Reports"},
  ],
  "en": {
    "commentary": "Heading into the first week of June 2026, the dual-basket crowd still owns the top of this list and the Ninja Foodi keeps earning it. The 2026 refresh leans hard on Ninja's Smart-Sense sensing and the AI-Sync Finish trick, where you tell it salmon is in one basket and asparagus in the other and both land done at the same moment. That is a genuinely useful feature for a weeknight dinner, and it is the kind of thing that justifies holding the number one spot another week. Down the list, the value story is loud right now: the Instant Vortex Plus 6-quart has been sitting around $90 versus its usual $150, which makes it the single easiest air fryer to recommend to someone buying their first one. For small Taiwanese-style kitchens and solo cooks, the Cosori Lite and the Dash Tasti-Crisp remain the compact champions, with the Dash measuring a footprint under one square foot and still pulling top marks at Consumer Reports. Early summer is a quiet season for air fryer launches, so I am keeping the order steady this week. Nothing in the news cycle changed the fundamentals: the best overall performers still finish hottest and most evenly, the budget picks still deliver the best price-to-crisp ratio, and the compact units still win for anyone short on counter space. I would happily buy any machine in this top five today and feel confident about it.",
    "highlights": [
      {"title": "Ninja holds the crown", "body": "The 2026 Foodi's Smart-Sense and AI-Sync Finish sync two baskets to finish together, a real weeknight time-saver that keeps it at number one."},
      {"title": "Instant Vortex Plus is the value buy", "body": "Around $90 versus a $150 list price, the 6-quart Vortex Plus is the easiest first air fryer to recommend right now."},
      {"title": "Compact picks for small kitchens", "body": "The Cosori Lite and Dash Tasti-Crisp stay top compact choices, the Dash fitting in under a square foot of counter."},
      {"title": "Steady order in a quiet season", "body": "Early June brings no major launches, so the rankings carry forward unchanged this week."},
    ],
  },
  "zh-tw": {
    "commentary": "進入 2026 年六月第一週，雙籃機種依然穩坐榜首，Ninja Foodi 也確實撐得起這個位置。2026 改款主打 Ninja 的 Smart-Sense 感測還有 AI-Sync Finish 同步收尾功能，你只要告訴它一籃放鮭魚、一籃放蘆筍，兩邊就會同時完成，這對平日晚餐真的很實用，光這點就值得讓它再守第一名一週。往下看，現在最大的話題是性價比，Instant Vortex Plus 六夸脫款最近大概落在 90 美元，原價是 150 美元，對第一次買氣炸鍋的人來說，這台是最好開口推薦的選擇。台灣小坪數廚房或一個人住的朋友，Cosori Lite 跟 Dash Tasti-Crisp 還是輕巧首選，Dash 佔的桌面甚至不到一平方英尺，在 Consumer Reports 還拿到高分。初夏本來就是氣炸鍋的淡季，新機種不多，所以這週我維持原排序。新聞面沒有動搖任何基本盤，整體最強的機種依舊加熱最快最均勻，平價款依舊有最好的酥脆性價比，輕巧款依舊適合桌面空間有限的人。坦白說前五名我今天買哪一台都很安心。",
    "highlights": [
      {"title": "Ninja 續坐第一", "body": "2026 Foodi 的 Smart-Sense 與 AI-Sync Finish 能讓兩籃同時完成，平日晚餐省時，穩居榜首。"},
      {"title": "Instant Vortex Plus 是性價比首選", "body": "六夸脫款約 90 美元、原價 150 美元，現在最好推薦給第一次買氣炸鍋的人。"},
      {"title": "小廚房就選輕巧款", "body": "Cosori Lite 跟 Dash Tasti-Crisp 仍是輕巧首選，Dash 佔桌面不到一平方英尺。"},
      {"title": "淡季維持原排序", "body": "六月初沒有重大新機，本週排名照常延續。"},
    ],
  },
}

# ---------------- COFFEE MAKERS ----------------
updates["best-coffee-makers.json"] = {
  "references": [
    {"title": "8 Best Coffee Makers of 2026, Lab Tested and Reviewed", "url": "https://www.consumerreports.org/appliances/coffee-makers/best-coffee-makers-of-the-year-a9612622702/", "source": "Consumer Reports"},
    {"title": "The best coffee makers in 2026, tested and reviewed", "url": "https://www.cnn.com/cnn-underscored/reviews/best-coffee-makers", "source": "CNN Underscored"},
  ],
  "en": {
    "commentary": "As of early June 2026, the Fellow Aiden remains the most exciting electric brewer on this list and it deserves the top spot. It swaps between true pour-over style and full batch brewing up to ten cups, and the interactive screen lets you dial in water temperature and pulse timing the way a cafe barista would. For anyone who takes their morning cup seriously, that level of control at home is the real reason to spend up. Just behind it, the Cuisinart PerfecTemp DCC-3200 keeps doing the unglamorous job perfectly: program it tonight, wake up to a full hot carafe, and the brew quality earns an excellent rating from Consumer Reports. That is exactly what most households actually want. On the espresso side, the De'Longhi La Specialista Opera continues to punch far above its price, pulling rich balanced shots that embarrass machines costing twice as much, and the cold brew function is a smart addition as the weather warms. For single-serve, the Bruvi BV-01 stays my pick over the usual pod giants because it handles coffee, espresso, and cold brew from one machine. This is a settled, mature category right now, so I am carrying the rankings forward unchanged. The picks are strong from top to bottom and nothing in the past week shifted the picture.",
    "highlights": [
      {"title": "Fellow Aiden leads on control", "body": "It switches between pour-over and ten-cup batch brewing with adjustable temperature and pulse timing, justifying its top spot."},
      {"title": "Cuisinart for set-and-forget mornings", "body": "Program the DCC-3200 overnight for a hot carafe at wake-up; Consumer Reports rates its brew excellent."},
      {"title": "De'Longhi Opera beats its price", "body": "Rich, balanced espresso plus a cold brew mode that suits warmer weather, outperforming pricier machines."},
      {"title": "Bruvi wins single-serve", "body": "One machine covers coffee, espresso, and cold brew, keeping it ahead of the big pod brands."},
    ],
  },
  "zh-tw": {
    "commentary": "截至 2026 年六月初，Fellow Aiden 依然是這份榜單上最讓人興奮的電動咖啡機，第一名實至名歸。它能在手沖模式跟最多十杯的批次沖煮之間切換，互動式螢幕讓你像咖啡師一樣調水溫跟注水節奏。對於很在意早上那杯咖啡的人來說，能在家裡有這種掌控度，就是值得多花錢的理由。緊追在後的是 Cuisinart PerfecTemp DCC-3200，它把最樸實的工作做到完美，晚上設定好，早上起床就有一整壺熱咖啡，沖煮品質在 Consumer Reports 拿到優異評價，這正是大多數家庭真正需要的。義式這邊，De'Longhi La Specialista Opera 持續超越自己的價位，萃出濃郁均衡的咖啡，讓貴一倍的機器都汗顏，而且冷萃功能在天氣轉熱的台灣夏天很加分。單杯機我還是選 Bruvi BV-01，因為一台就能做咖啡、義式跟冷萃，勝過常見的膠囊大廠。這個品類目前已經很成熟穩定，所以我把排名原封不動延續。前後名單都很強，過去一週也沒有任何變動。",
    "highlights": [
      {"title": "Fellow Aiden 以掌控度領先", "body": "可在手沖與十杯批次沖煮間切換，水溫與注水節奏皆可調，穩坐第一。"},
      {"title": "Cuisinart 適合設定好就不管", "body": "DCC-3200 前一晚設定，起床就有熱咖啡，Consumer Reports 評沖煮優異。"},
      {"title": "De'Longhi Opera 超越價位", "body": "濃郁均衡的義式加上冷萃模式，適合轉熱的天氣，表現勝過更貴機種。"},
      {"title": "單杯機選 Bruvi", "body": "一台搞定咖啡、義式與冷萃，領先常見膠囊大廠。"},
    ],
  },
}

# ---------------- RICE COOKERS ----------------
updates["best-rice-cookers.json"] = {
  "references": [
    {"title": "Best rice cookers in 2026, tested by our editors", "url": "https://www.cnn.com/cnn-underscored/reviews/best-rice-cooker", "source": "CNN Underscored"},
    {"title": "Zojirushi vs Tiger: Which Rice Cooker Is the Best?", "url": "https://prudentreviews.com/zojirushi-vs-tiger/", "source": "Prudent Reviews"},
  ],
  "en": {
    "commentary": "In early June 2026 the Zojirushi Neuro Fuzzy stays my top rice cooker, and the case for it has not weakened. Across sushi rice, brown rice, and basmati it cooks fluffy, evenly textured results every time, and the NS-ZCC10 has held the number one recommendation for nearly a decade with a 4.8 rating. For people who cook rice several times a week, it is the better long-term investment, and that consistency is why it keeps the lead. That said, the Tiger JKT-D10U has a genuinely strong argument this week. It makes white and brown rice that taste just as good while cooking noticeably faster, 44 minutes versus 53 for white rice and 63 versus 103 for brown, and its Synchro-Cooking plate lets you steam a protein above the rice at the same time. It sits in the price sweet spot between budget units and the $200 Zojirushi, so it stays my value-forward IH pick. At the bottom of the list, the Aroma ARC-914SBD is still the one I point budget buyers toward: under $40 with digital fuzzy logic, a delay timer, a steamer basket, and a Flash Rice mode that halves cook time. The category is stable, so I am holding the order steady this week.",
    "highlights": [
      {"title": "Zojirushi Neuro Fuzzy stays number one", "body": "Fluffy, even results across every rice type and a near-decade run as the top pick keep the NS-ZCC10 ahead."},
      {"title": "Tiger JKT-D10U is the speed and value play", "body": "Equal taste with faster cook times and a Synchro-Cooking plate to steam protein over the rice."},
      {"title": "Aroma for budget buyers", "body": "Under $40 with fuzzy logic, delay timer, steamer basket, and a Flash Rice mode that halves cook time."},
      {"title": "Stable category, steady order", "body": "No major launches this week, so the rankings carry forward unchanged."},
    ],
  },
  "zh-tw": {
    "commentary": "2026 年六月初，Zojirushi Neuro Fuzzy 仍是我心中第一名的電子鍋，理由也沒有變弱。不管是壽司米、糙米還是印度香米，它每次都煮得粒粒分明、口感均勻，NS-ZCC10 已經連續近十年穩坐第一推薦，評分 4.8。對於一週煮好幾次飯的人來說，它是更值得的長期投資，這份穩定就是它持續領先的原因。不過這週 Tiger JKT-D10U 的賣點也很實在，白米跟糙米煮起來一樣好吃，速度卻明顯更快，白米 44 分鐘對上 53 分鐘，糙米 63 分鐘對上 103 分鐘，而且它的同步料理盤可以在飯上面同時蒸一份蛋白質。價格剛好卡在平價機種跟 200 美元 Zojirushi 之間，所以它仍是我主打性價比的 IH 首選。榜單最後，Aroma ARC-914SBD 還是我推薦給預算有限買家的那一台，不到 40 美元就有數位模糊邏輯、預約定時、蒸籃，還有把烹煮時間砍半的 Flash Rice 快煮模式。這個品類很穩，所以這週維持原排序。",
    "highlights": [
      {"title": "Zojirushi Neuro Fuzzy 續居第一", "body": "各種米都煮得粒粒分明，近十年穩坐第一推薦，NS-ZCC10 持續領先。"},
      {"title": "Tiger JKT-D10U 主打速度與性價比", "body": "口感一樣好但煮得更快，還有同步料理盤可在飯上蒸蛋白質。"},
      {"title": "Aroma 適合預算族", "body": "不到 40 美元就有模糊邏輯、預約定時、蒸籃與砍半時間的快煮模式。"},
      {"title": "品類穩定，排序延續", "body": "本週無重大新機，排名照常延續。"},
    ],
  },
}

# ---------------- DISHWASHERS ----------------
updates["best-dishwashers.json"] = {
  "references": [
    {"title": "Best (and Worst) Dishwashers of 2026, Lab-Tested and Reviewed", "url": "https://www.consumerreports.org/appliances/dishwashers/best-dishwashers-of-the-year-a6109623431/", "source": "Consumer Reports"},
    {"title": "6 Best Bosch Dishwashers of 2026", "url": "https://www.reviewed.com/dishwashers/best-right-now/best-bosch-dishwashers", "source": "Reviewed"},
  ],
  "en": {
    "commentary": "As of early June 2026 Bosch still owns this category, and Consumer Reports just reaffirmed why: the brand earns the best overall brand score among dishwashers and lands multiple models at the very top. The Benchmark Series SHP9PCM5N sits at number one on CR's list, praised for washing and drying exceptionally while staying genuinely quiet, plus strong marks for predicted reliability and owner satisfaction. That combination of clean, dry, quiet, and dependable is the whole game with dishwashers, and Bosch nails all four. Right behind it, the 800 Series SHX78CM5N takes second at CR and actually ranked first at Reviewed thanks to its speed and stuck-on stain removal. The thread running through Bosch's lineup is CrystalDry, which converts moisture into heat to get dishes fully dry without a heated coil, a real advantage if you wash a lot of plastic. For a typical household I would buy an 800 Series and never think about it again. This is a slow-moving, reliability-driven category and early summer brings no new model news, so I am holding the rankings steady this week. The picks reflect what is genuinely the safest, best-performing money you can spend on a built-in dishwasher right now.",
    "highlights": [
      {"title": "Bosch tops the brand rankings", "body": "Consumer Reports gives Bosch the best overall dishwasher brand score and places multiple models at the top."},
      {"title": "Benchmark SHP9PCM5N is number one", "body": "Exceptional wash and dry, very quiet, and strong predicted reliability earn it CR's top spot."},
      {"title": "800 Series for most homes", "body": "The SHX78CM5N pairs fast cycles with excellent stuck-on stain removal, first place at Reviewed."},
      {"title": "CrystalDry drives the lineup", "body": "Converting moisture to heat gets dishes fully dry without a coil, a real plus for plastic loads."},
    ],
  },
  "zh-tw": {
    "commentary": "截至 2026 年六月初，Bosch 依然主宰這個品類，Consumer Reports 剛剛再次證明原因，這個品牌在洗碗機裡拿到最高的整體品牌分數，還有多款機型衝上榜首。Benchmark 系列 SHP9PCM5N 在 CR 榜上排第一，洗淨跟烘乾都表現傑出又安靜，預估妥善率跟用戶滿意度也都很高。洗得乾淨、烘得乾、運轉安靜又耐用，這四件事就是洗碗機的全部重點，Bosch 四項全中。緊追在後的 800 系列 SHX78CM5N 在 CR 排第二，在 Reviewed 甚至拿第一，靠的是速度跟頑垢清除能力。貫穿 Bosch 整個產品線的就是 CrystalDry，它把水氣轉換成熱能，不靠加熱管就能把碗盤完全烘乾，如果你常洗塑膠容器，這點很有感。一般家庭我會直接買 800 系列，買完就不用再煩惱。這是個更新緩慢、以妥善率為主的品類，初夏也沒有新機消息，所以這週維持原排序。這份名單反映的就是目前買嵌入式洗碗機最安全、表現最好的花法。",
    "highlights": [
      {"title": "Bosch 居品牌之冠", "body": "Consumer Reports 給 Bosch 洗碗機最高整體品牌分數，多款機型也排在前段。"},
      {"title": "Benchmark SHP9PCM5N 第一名", "body": "洗淨烘乾傑出又安靜，預估妥善率高，拿下 CR 榜首。"},
      {"title": "800 系列適合多數家庭", "body": "SHX78CM5N 快速又能清頑垢，在 Reviewed 拿第一。"},
      {"title": "CrystalDry 貫穿產品線", "body": "把水氣轉成熱能、不靠加熱管就烘乾，洗塑膠容器特別有感。"},
    ],
  },
}

# ---------------- PORTABLE ICE MAKERS ----------------
updates["best-portable-ice-makers.json"] = {
  "references": [
    {"title": "Best countertop ice makers: Tested and reviewed", "url": "https://www.cnn.com/cnn-underscored/reviews/best-countertop-ice-maker", "source": "CNN Underscored"},
    {"title": "Best Nugget Icemakers of 2026", "url": "https://www.consumerreports.org/appliances/icemakers/best-nugget-icemakers-a1126656403/", "source": "Consumer Reports"},
  ],
  "en": {
    "commentary": "We are now into the first week of June 2026 and portable ice maker demand is climbing fast as summer entertaining ramps up, which makes this week's picks especially relevant. The Chefman Iceman Dual-Size is the value standout right now: it produced its first cubes in just six minutes, the fastest of any machine tested, and at around $130 it undercuts the GE Profile Opal by nearly $300. At 17.5 pounds you can carry it to the patio with one hand, which is exactly what a portable unit should do. The GE Profile Opal 2.0 still wins for nugget ice for one simple reason, nobody else makes chewable nugget ice this good at home, and if that soft pellet texture is your priority it is worth the $419 and the 44-pound heft. For budget buyers the Igloo Premium self-cleaning unit is the most genuinely portable pick at $90 and 15 pounds with a carry handle, and the Costway nugget model delivers around 1,200 grams of ice at half the price of the popular names. With units producing 26 to 45 pounds a day and first ice in under ten minutes, any of these handles a summer party. Demand is seasonal but the lineup is settled, so I am holding the order this week.",
    "highlights": [
      {"title": "Chefman Iceman is the value pick", "body": "First cubes in six minutes and around $130, undercutting the GE Opal by nearly $300 while staying one-hand portable."},
      {"title": "GE Profile Opal owns nugget ice", "body": "Still the best chewable nugget ice at home, worth its $419 price if that soft texture is the goal."},
      {"title": "Budget portability from Igloo", "body": "At $90 and 15 pounds with a handle, the self-cleaning Igloo is the easiest unit to actually carry."},
      {"title": "Peak season timing", "body": "With summer entertaining ramping up, every top pick makes 26 to 45 pounds a day and first ice in under ten minutes."},
    ],
  },
  "zh-tw": {
    "commentary": "現在已經進入 2026 年六月第一週，隨著夏天聚會旺季升溫，可攜式製冰機的需求快速攀升，這週的推薦也就特別實用。Chefman Iceman Dual-Size 是目前的性價比之星，它只要六分鐘就做出第一批冰塊，是所有測試機種裡最快的，而且約 130 美元，比 GE Profile Opal 便宜將近 300 美元。重量 17.5 磅，單手就能拎到陽台，這正是可攜式機種該有的樣子。GE Profile Opal 2.0 在綿冰這塊仍是冠軍，原因很單純，沒有人能在家做出這麼好咬的綿冰，如果你就是要那種軟綿的顆粒口感，那 419 美元跟 44 磅的份量就值得。預算族的話，Igloo Premium 自清款是最實在的可攜選擇，90 美元、15 磅、有提把，Costway 綿冰款則能產出約 1,200 克的冰，價格只要熱門品牌的一半。這些機種一天能產 26 到 45 磅冰、十分鐘內出第一批，辦個夏天派對都綽綽有餘。需求雖然有季節性，但名單已經很穩，所以這週維持原排序。",
    "highlights": [
      {"title": "Chefman Iceman 是性價比首選", "body": "六分鐘出第一批冰、約 130 美元，比 GE Opal 便宜近 300 美元，還能單手攜帶。"},
      {"title": "GE Profile Opal 綿冰稱王", "body": "在家做出最好咬的綿冰，若你要那種軟綿口感，419 美元值得。"},
      {"title": "Igloo 兼顧預算與便攜", "body": "90 美元、15 磅、有提把的自清款，是最好拎著走的一台。"},
      {"title": "正逢旺季", "body": "夏天聚會升溫，前段機種一天產 26 到 45 磅冰、十分鐘內出第一批。"},
    ],
  },
}

# ---------------- GAS GRILLS ----------------
updates["best-gas-grills.json"] = {
  "references": [
    {"title": "The Best Weber Grills of 2026, Tested and Reviewed", "url": "https://www.bobvila.com/reviews/best-weber-grill/", "source": "Bob Vila"},
    {"title": "Best Weber Gas Grills for 2026, Top Rated", "url": "https://www.bbqguys.com/a/23647/top-rated/bbq/gas-grills/weber", "source": "BBQGuys"},
  ],
  "en": {
    "commentary": "It is the first week of June 2026 and grilling season is in full swing, so this is the moment these rankings matter most. Weber continues to set the standard at the top, and the reasons are the same ones that have held for years: durable build, the reliable GS4 cooking system, effective Flavorizer bars, and a 10-year warranty that means you are buying a grill once. The Spirit II E-310 remains the smart mainstream choice, a three-burner workhorse that delivers even heat and starts reliably every time, which is exactly what you want when guests are waiting and the burgers are on. At the premium end, the Summit Series is the crown jewel, offering touchscreen ignition, tap-to-adjust burner control, and smartphone monitoring so you can track temps and get alerts from across the yard. That kind of connected convenience genuinely changes how you cook for a crowd. For most families a mid-range Weber hits the sweet spot of performance, durability, and price, and that is reflected in where these picks land. The category does not move quickly and early June brought no new launches that change the picture, so I am holding the rankings steady. Buy any grill near the top of this list and you are set for the whole summer.",
    "highlights": [
      {"title": "Weber sets the standard", "body": "Durable build, the GS4 system, Flavorizer bars, and a 10-year warranty mean you buy a grill once."},
      {"title": "Spirit II E-310 is the mainstream pick", "body": "A three-burner workhorse with even heat and reliable ignition, ideal when guests are waiting."},
      {"title": "Summit Series for the premium buyer", "body": "Touchscreen ignition, tap-to-adjust burners, and smartphone temp monitoring from across the yard."},
      {"title": "Peak grilling season", "body": "Demand is high in early June but no new launches shift the order, so the rankings hold steady."},
    ],
  },
  "zh-tw": {
    "commentary": "現在是 2026 年六月第一週，烤肉季正熱，這也是這份排名最派得上用場的時刻。Weber 在榜首持續樹立標竿，理由跟多年來一樣，扎實的做工、可靠的 GS4 烹調系統、好用的 Flavorizer 風味條，還有 10 年保固，等於這台烤爐你買一次就夠。Spirit II E-310 仍是聰明的主流選擇，三爐口的實力派，火力均勻、每次點火都很順，當客人在等、肉已經下爐時，這正是你要的穩定。高階這邊，Summit 系列是皇冠上的明珠，配備觸控點火、輕點即調的爐火控制，還能用手機監控溫度，人在院子另一頭也能收到提醒，這種連網便利確實改變了你替一群人烤肉的方式。對多數家庭來說，中階 Weber 在性能、耐用跟價格之間取得最佳平衡，這也反映在這些推薦的名次上。這個品類變動不快，六月初也沒有改變局面的新機，所以我維持原排序。買榜單前段任何一台，整個夏天就搞定了。",
    "highlights": [
      {"title": "Weber 樹立標竿", "body": "扎實做工、GS4 系統、Flavorizer 風味條加 10 年保固，買一次就夠。"},
      {"title": "Spirit II E-310 是主流首選", "body": "三爐口實力派，火力均勻、點火順暢，客人在等時最可靠。"},
      {"title": "Summit 系列給高階買家", "body": "觸控點火、輕點調火，還能用手機從院子另一頭監控溫度。"},
      {"title": "正逢烤肉旺季", "body": "六月初需求高但無新機改變局面，排名維持穩定。"},
    ],
  },
}

# ---------------- OUTDOOR GRIDDLES ----------------
updates["best-outdoor-griddles.json"] = {
  "references": [
    {"title": "The 9 Best Outdoor Griddles for 2026, Expert Reviews", "url": "https://www.smokedbbqsource.com/best-outdoor-gas-griddles/", "source": "Smoked BBQ Source"},
    {"title": "Best Outdoor Griddles and Flat-Top Grills of 2026, Tested", "url": "https://www.mensjournal.com/gear/best-outdoor-griddle", "source": "Men's Journal"},
  ],
  "en": {
    "commentary": "With summer cooking in full swing this first week of June 2026, the Blackstone 36-inch 4-burner remains the outdoor griddle I recommend to most people, and the season only sharpens the case. You get 720 square inches and 60,000 BTUs for around $400, which is enough room to run a full pancake breakfast on one half and smash burgers on the other. Testers came away genuinely impressed by how it handles both, and that all-in-one versatility is why a griddle can quietly replace several other cookers and save you both space and money. The Solo Stove Steelfire has earned best-overall honors elsewhere for its responsive tri-ply cooktop and rust-resistant design, so it stays high on my list as the premium pick for cooks who want faster heat response. Two honest trade-offs keep the Blackstone realistic: it struggled most in windy conditions during testing, and its lowest temperature runs hot at about 450 degrees, so delicate low-heat work takes more attention. For smaller spaces the 22-inch tabletop with hood is the one I point campers and tailgaters toward. This is peak griddle season, and while demand is high the lineup is stable, so I am holding the rankings steady this week.",
    "highlights": [
      {"title": "Blackstone 36-inch is the pick for most", "body": "720 square inches and 60,000 BTUs near $400 handle a full breakfast and smash burgers at once."},
      {"title": "Solo Stove Steelfire is the premium choice", "body": "A responsive tri-ply cooktop and rust-resistant design make it the best-overall pick elsewhere."},
      {"title": "Know the trade-offs", "body": "Blackstone struggles most in wind and runs hot at a 450-degree low, so delicate cooking needs care."},
      {"title": "Tabletop for camping", "body": "The 22-inch model with hood is the go-to for campers, tailgaters, and small outdoor spaces."},
    ],
  },
  "zh-tw": {
    "commentary": "2026 年六月第一週，夏季戶外料理正熱，Blackstone 36 吋四爐口仍是我最常推薦給一般人的鐵板燒，旺季更凸顯它的優勢。720 平方英寸、60,000 BTU，價格約 400 美元，空間大到可以一半煎一整份鬆餅早餐、另一半煎漢堡排。測試者對它同時搞定兩邊的能力真的很驚艷，這種全能多用途，就是一台鐵板可以默默取代好幾種爐具、幫你省空間又省錢的原因。Solo Stove Steelfire 在別的評測拿過最佳整體，靠的是反應靈敏的三層複合鐵板跟抗鏽設計，所以它在我榜上維持前段，是想要更快火力反應的人的高階首選。兩個誠實的取捨讓 Blackstone 回到現實，它在測試中最怕大風，而且最低溫偏高、大約 450 度，所以需要小火細煮時得多留意。空間小的話，22 吋桌上型加上蓋款是我推薦給露營跟車聚的選擇。現在是鐵板燒的最旺季，需求雖高但名單很穩，所以這週維持原排序。",
    "highlights": [
      {"title": "Blackstone 36 吋適合多數人", "body": "720 平方英寸、60,000 BTU、約 400 美元，可同時煎早餐與漢堡排。"},
      {"title": "Solo Stove Steelfire 是高階選擇", "body": "三層複合鐵板反應靈敏又抗鏽，在別處評測拿下最佳整體。"},
      {"title": "了解取捨", "body": "Blackstone 最怕大風，最低溫偏高約 450 度，小火細煮要多留意。"},
      {"title": "露營就選桌上型", "body": "22 吋加蓋款適合露營、車聚與小型戶外空間。"},
    ],
  },
}

# ---------------- MATTRESSES ----------------
updates["best-mattresses.json"] = {
  "references": [
    {"title": "The 23 best Memorial Day mattress sales for every type of sleeper", "url": "https://www.cnn.com/cnn-underscored/deals/memorial-day-mattress-sales-2026-05-25", "source": "CNN Underscored"},
    {"title": "The Best Memorial Day Mattress Sales of 2026", "url": "https://fortune.com/article/memorial-day-mattress-sales/", "source": "Fortune"},
  ],
  "en": {
    "commentary": "As of early June 2026 the Helix Midnight Luxe holds my top spot, and the post-Memorial-Day window makes this the best buying moment of the season. It earned an overall 4.5 out of 5 and feels comfortable across nearly every sleeping position, which is rare, and it also tops the specialty lists for neck pain and sciatica, so it is the safest single recommendation for a household with mixed needs. Right now Helix is running 27 percent off sitewide, which pulls the real price into reach. For dedicated side sleepers the Nectar Premier takes the category crown thanks to pressure-relieving contouring at the shoulders and hips, and Nectar's current event runs up to 50 percent off mattresses and 66 percent off bundles, among the most aggressive pricing on this list. Saatva remains my pick for anyone who wants a more supportive innerspring-hybrid feel, and its sale knocks a queen from $2,179 to $1,854. DreamCloud and WinkBed round out strong value plays with up to 60 and 30 percent off respectively. The deals are the story this week, not the rankings themselves, so I am carrying the order forward. If you have been waiting to replace a mattress, this early-June stretch right after Memorial Day is the moment to act.",
    "highlights": [
      {"title": "Helix Midnight Luxe leads", "body": "A 4.5 of 5 overall plus top marks for neck pain and sciatica, now 27 percent off sitewide."},
      {"title": "Nectar Premier for side sleepers", "body": "Pressure-relieving shoulder and hip contouring, with up to 50 percent off mattresses and 66 percent off bundles."},
      {"title": "Saatva for hybrid support", "body": "The supportive innerspring-hybrid feel, with a queen dropping from $2,179 to $1,854 in the current sale."},
      {"title": "Best buying window", "body": "Post-Memorial-Day discounts make early June the season's strongest moment to replace a mattress."},
    ],
  },
  "zh-tw": {
    "commentary": "截至 2026 年六月初，Helix Midnight Luxe 穩坐我心中第一名，而陣亡將士紀念日後的這段時間，正是這一季最好的入手時機。它整體拿到 4.5 分（滿分 5 分），幾乎各種睡姿都覺得舒服，這很難得，而且它在頸痛跟坐骨神經痛的專項榜單也都奪冠，所以對需求不一的家庭來說，它是最保險的單一推薦。Helix 目前全站打 73 折，把實際價格拉進可入手的範圍。專門側睡的人，Nectar Premier 拿下這個分類的冠軍，靠的是肩部跟臀部的減壓貼合，Nectar 目前的活動床墊最高五折、組合最高 66 折，是這份名單上最殺的價格之一。Saatva 仍是我推薦給想要更有支撐感的獨立筒混合床墊的人，特價讓 Queen 尺寸從 2,179 美元降到 1,854 美元。DreamCloud 跟 WinkBed 分別最高 6 折跟 7 折，補上兩個很有競爭力的選項。這週的重點是優惠而不是排名本身，所以我把排序原封延續。如果你一直想換床墊，六月初這段緊接著紀念日的時間，就是該出手的時刻。",
    "highlights": [
      {"title": "Helix Midnight Luxe 領先", "body": "整體 4.5 分，頸痛與坐骨神經痛專項奪冠，現全站 73 折。"},
      {"title": "Nectar Premier 適合側睡", "body": "肩臀減壓貼合，床墊最高五折、組合最高 66 折。"},
      {"title": "Saatva 主打混合支撐", "body": "獨立筒混合床墊支撐感佳，特價讓 Queen 從 2,179 降到 1,854 美元。"},
      {"title": "最佳入手時機", "body": "紀念日後的折扣讓六月初成為這一季換床墊最划算的時刻。"},
    ],
  },
}

# ---------------- APPLY ----------------
for fname, u in updates.items():
    d, p = load(fname)
    entry = {
        "date": DATE,
        "rankings": last_rankings(d),
        "references": u["references"],
        "i18n": {
            "en": {"commentary": u["en"]["commentary"], "highlights": u["en"]["highlights"]},
            "zh-tw": {"commentary": u["zh-tw"]["commentary"], "highlights": u["zh-tw"]["highlights"]},
        },
    }
    upsert(d, entry)
    save(p, d)
    print(f"updated {fname}: {len(entry['rankings'])} rankings carried forward")
