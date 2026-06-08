import sys; sys.path.insert(0, "/Users/etrexkuo/toprankland/scripts")
from daily_helper import load, save, upsert, last_rankings, DATE

def do(name, refs, en, zh):
    d, p = load(name)
    entry = {
        "date": DATE,
        "rankings": last_rankings(d),
        "references": refs,
        "i18n": {"en": en, "zh-tw": zh},
    }
    upsert(d, entry)
    save(p, d)
    print("updated", name)

# ---------------- best-robot-vacuums ----------------
do("best-robot-vacuums.json",
   [
     {"title": "The 4 Best Robot Vacuums of 2026", "url": "https://www.rtings.com/robot-vacuum/reviews/best/robot", "source": "RTINGS"},
     {"title": "Top 20 Best Robot Vacuums in 2026", "url": "https://vacuumwars.com/vacuum-wars-best-robot-vacuums/", "source": "Vacuum Wars"},
   ],
   {
     "commentary": "The Dreame X60 Max Ultra stays at number one because it is the robot that gets closest to actually replacing your manual vacuum, and that is the only bar that matters at the top. The suction handles carpet deep-cleaning that most robots fake, the mopping lifts and washes itself, and the dock automates everything so you genuinely forget it exists for weeks. For most homes that want true hands-off cleaning, this is the one worth the premium. The Roborock Saros 10R holds a close second and is a legitimate co-leader, its solid-state LiDAR and obstacle recognition give the best navigation in the category, so it threads around cables and clutter that trip up rivals. The choice between it and the Dreame comes down to whether you prioritize cleaning power or navigation smarts. The Dreame L50 Ultra stays third as the value flagship with most of the top features for less. The Roborock Saros Z70 holds fourth for its arm that picks up small objects. Nothing this week reordered the field. The read: best cleaning is the Dreame X60, best navigation is the Roborock Saros 10R, best value is the L50.",
     "highlights": [
       {"title": "Dreame X60 Max Ultra nearly replaces manual vacuuming", "body": "Real carpet deep-cleaning, self-washing mopping and a dock that automates everything so you forget it for weeks. For homes wanting true hands-off cleaning, it earns the premium at number one."},
       {"title": "Roborock Saros 10R is the navigation co-leader", "body": "Solid-state LiDAR and obstacle recognition give the best navigation in the category, threading around cables and clutter that trip up rivals. That smarts keeps it a very close second."},
       {"title": "Dreame L50 Ultra is the value flagship", "body": "It delivers most of the top-tier features for noticeably less than the leaders. For buyers who want flagship cleaning without the flagship price, it holds a firm third."},
       {"title": "Pick cleaning power or navigation", "body": "The Dreame wins on raw cleaning, the Roborock on threading around obstacles. A cluttered home with cables and toys leans Roborock; open floors that need deep carpet cleaning lean Dreame."},
     ],
   },
   {
     "commentary": "Dreame X60 Max Ultra 我還是放第一，因為它是最接近真正取代你手動吸塵的機器，而在頂端這是唯一重要的標準。吸力處理多數機器只是假裝的地毯深層清潔，拖地會自己抬升跟清洗，基座把一切自動化到你真的好幾週忘了它存在。對多數想要真正放手清潔的家庭，這台值得那個高價。Roborock Saros 10R 緊咬第二，是名副其實的並列領袖，固態 LiDAR 加障礙物辨識給這類別最好的導航，所以它能繞過絆倒對手的電線跟雜物。它跟 Dreame 之間的選擇就看你優先清潔力還是導航智慧。Dreame L50 Ultra 守第三，是性價比旗艦，用更低價給大部分頂級功能。Roborock Saros Z70 守第四，靠它能撿小物的機械臂。這週沒事件重排。判斷：清潔選 Dreame X60、導航選 Roborock Saros 10R、性價比選 L50。",
     "highlights": [
       {"title": "Dreame X60 Max Ultra 幾乎取代手動吸塵", "body": "真正的地毯深層清潔、自我清洗的拖地、把一切自動化到你好幾週忘了它的基座。對想要真放手清潔的家庭，它在第一名掙得高價。"},
       {"title": "Roborock Saros 10R 是導航並列領袖", "body": "固態 LiDAR 加障礙物辨識給這類別最好的導航，繞過絆倒對手的電線跟雜物。這份智慧讓它緊咬第二。"},
       {"title": "Dreame L50 Ultra 是性價比旗艦", "body": "它用比領袖明顯更低的價格給出大部分頂級功能。想要旗艦清潔又不付旗艦價的買家，它穩在第三。"},
       {"title": "選清潔力還是導航", "body": "Dreame 贏在純清潔、Roborock 贏在繞障礙。電線跟玩具多的雜亂家偏 Roborock；需要深層地毯清潔的開闊地板偏 Dreame。"},
     ],
   })

# ---------------- best-cordless-vacuums ----------------
do("best-cordless-vacuums.json",
   [
     {"title": "Best cordless vacuum 2026 reviews", "url": "https://www.rtings.com/vacuum/reviews/best/cordless-stick", "source": "RTINGS"},
     {"title": "The Best Cordless Stick Vacuums of 2026", "url": "https://www.nytimes.com/wirecutter/reviews/best-cordless-stick-vacuum/", "source": "Wirecutter"},
   ],
   {
     "commentary": "The Shark PowerDetect stays at number one because it delivers Dyson-level cleaning with smarts Dyson does not match, at a price that undercuts it. The detection tech ramps suction automatically on carpet and around edges, the runtime covers a whole home, and the whole package costs less than the flagship Dyson it competes with. For most households this is simply the smarter buy, and that value-plus-performance combination is why it leads. The Dyson Gen5detect holds second and still wins the raw-power and filtration contest, the suction is the strongest you can buy and the particle sensing is genuinely useful, the pick for people who want the absolute best regardless of price. The Dyson V15 Detect stays third as the value Dyson, nearly as capable for less. The Tineco Pure One A90s holds fourth as the value-brand standout with strong auto-adjusting suction. Nothing this week reordered the field. The read: best overall value is the Shark, best raw power is the Dyson Gen5, and unless you specifically want maximum suction, the Shark saves you real money without giving up clean floors.",
     "highlights": [
       {"title": "Shark PowerDetect is the smarter buy", "body": "Detection tech ramps suction automatically on carpet and edges, runtime covers a whole home, and it undercuts the flagship Dyson. That value-plus-performance combination holds it at number one."},
       {"title": "Dyson Gen5detect wins raw power", "body": "The strongest suction you can buy plus genuinely useful particle sensing make it the pick for people who want the absolute best regardless of price. That ceiling keeps it a firm second."},
       {"title": "Dyson V15 Detect is the value Dyson", "body": "Nearly as capable as the Gen5 for noticeably less, it brings the brand's performance down a price tier. For Dyson fans on a budget, it holds a solid third."},
       {"title": "You do not need maximum suction", "body": "The Dyson Gen5 is the most powerful, but most homes are cleaned just as well by the smarter, cheaper Shark. Unless you have heavy carpet and pets, the value pick gets your floors equally clean."},
     ],
   },
   {
     "commentary": "Shark PowerDetect 我還是放第一，因為它用低於 Dyson 的價格，給出 Dyson 級的清潔加上 Dyson 沒有的智慧。偵測技術在地毯跟邊緣自動加大吸力，續航蓋得過整個家，整套又比它對打的旗艦 Dyson 便宜。對多數家庭這就是更聰明的買法，這份性價比加效能就是它領先的原因。Dyson Gen5detect 守第二，依然贏純力量跟過濾的比賽，吸力是你買得到最強的，粒子偵測也真的實用，給不計價格想要絕對最好的人。Dyson V15 Detect 守第三，是性價比 Dyson，用更低價給幾乎一樣的能力。Tineco Pure One A90s 守第四，是性價比品牌的亮點，自動調整吸力很強。這週沒事件重排。判斷：整體性價比選 Shark、純力量選 Dyson Gen5，除非你特別要最大吸力，否則 Shark 幫你省真錢又不犧牲乾淨地板。",
     "highlights": [
       {"title": "Shark PowerDetect 是更聰明的買法", "body": "偵測技術在地毯跟邊緣自動加大吸力、續航蓋過整個家，又比旗艦 Dyson 便宜。這份性價比加效能讓它守住第一。"},
       {"title": "Dyson Gen5detect 贏純力量", "body": "你買得到最強的吸力加真的實用的粒子偵測，讓它是不計價格想要絕對最好的人的選擇。這道天花板讓它穩在第二。"},
       {"title": "Dyson V15 Detect 是性價比 Dyson", "body": "用明顯更低的價格給出幾乎跟 Gen5 一樣的能力，把品牌效能帶到低一階。對預算有限的 Dyson 迷，它穩坐第三。"},
       {"title": "你不需要最大吸力", "body": "Dyson Gen5 最強，但多數家用更聰明更便宜的 Shark 也清得一樣乾淨。除非你有厚地毯跟寵物，性價比選擇把地板清得一樣好。"},
     ],
   })

# ---------------- best-air-purifiers ----------------
do("best-air-purifiers.json",
   [
     {"title": "Best air purifier 2026 reviews", "url": "https://www.nytimes.com/wirecutter/reviews/best-air-purifier/", "source": "Wirecutter"},
     {"title": "The Best Air Purifiers of 2026", "url": "https://www.rtings.com/air-purifier/reviews/best/air-purifiers", "source": "RTINGS"},
   ],
   {
     "commentary": "The IQAir HealthPro Plus stays at number one because when air quality actually matters, for allergies, asthma or wildfire smoke, this is the purifier that does the job nothing else fully matches. The medical-grade HyperHEPA filtration captures particles smaller than standard HEPA, and the build is made to run for years rather than to look pretty on Instagram. It costs a lot and the filters are not cheap, but for someone whose health depends on clean air, it is the only honest top pick. The Coway Airmega 400S holds second as the best value-to-performance choice for most homes, it cleans large rooms quickly, the running costs are reasonable, and for the vast majority of buyers it is genuinely all the purifier they need. The Blueair HealthProtect 7470i stays third on its fast quiet cleaning and germ-trapping filtration. The Rabbit Air MinusA3 holds fourth as the design-and-quiet pick. Nothing this week reordered the field. The read: best for serious health needs is the IQAir, best value for most homes is the Coway, and most people should buy the Coway and save the difference.",
     "highlights": [
       {"title": "IQAir HealthPro Plus is the medical-grade pick", "body": "HyperHEPA filtration captures particles smaller than standard HEPA, built to run for years. When clean air is a health necessity for allergies, asthma or smoke, it is the only honest top pick at number one."},
       {"title": "Coway Airmega 400S is the value champ", "body": "It cleans large rooms quickly with reasonable running costs, and for the vast majority of buyers it is all the purifier they need. That balance keeps it a firm second."},
       {"title": "Blueair HealthProtect 7470i cleans fast and quiet", "body": "Quick, quiet cleaning plus germ-trapping filtration make it a strong all-round choice. For buyers who want performance without noise, it holds a solid third."},
       {"title": "Most people should buy the Coway", "body": "The IQAir is the best, but its cost only makes sense for genuine health needs. For a normal home wanting cleaner air, the Coway does the job for far less, so save the difference unless health demands more."},
     ],
   },
   {
     "commentary": "IQAir HealthPro Plus 我還是放第一，因為當空氣品質真的重要時，過敏、氣喘或野火煙霧，這台淨化器做的事沒人能完全比上。醫療級 HyperHEPA 過濾捕捉比標準 HEPA 更小的顆粒，做工是為了運轉好幾年而非在 Instagram 上好看。它很貴、濾網也不便宜，但對健康仰賴乾淨空氣的人，它是唯一誠實的首選。Coway Airmega 400S 守第二，是多數家庭最佳的性價比選擇，它快速清潔大房間、運轉成本合理，對絕大多數買家它真的是他們需要的全部淨化器。Blueair HealthProtect 7470i 守第三，靠快速安靜的清潔跟捕菌過濾。Rabbit Air MinusA3 守第四，是設計兼安靜選擇。這週沒事件重排。判斷：認真健康需求選 IQAir、多數家庭性價比選 Coway，多數人該買 Coway 把差價省下來。",
     "highlights": [
       {"title": "IQAir HealthPro Plus 是醫療級選擇", "body": "HyperHEPA 捕捉比標準 HEPA 更小的顆粒，做工為運轉好幾年打造。乾淨空氣是過敏、氣喘或煙霧的健康必需時，它是第一名唯一誠實的選擇。"},
       {"title": "Coway Airmega 400S 是性價比冠軍", "body": "它快速清潔大房間、運轉成本合理，對絕大多數買家是他們需要的全部。這份平衡讓它穩在第二。"},
       {"title": "Blueair HealthProtect 7470i 又快又安靜", "body": "快速安靜的清潔加捕菌過濾，讓它是強力全能選擇。想要效能又不要噪音的買家，它穩坐第三。"},
       {"title": "多數人該買 Coway", "body": "IQAir 最好，但它的成本只對真正的健康需求合理。一般家庭想要更乾淨空氣，Coway 用低很多的價格做到，除非健康要求更多，否則把差價省下來。"},
     ],
   })

# ---------------- best-robot-lawn-mowers ----------------
do("best-robot-lawn-mowers.json",
   [
     {"title": "Best robot lawn mower 2026 reviews", "url": "https://www.tomsguide.com/best-picks/best-robot-lawn-mowers", "source": "Tom's Guide"},
     {"title": "The Best Robot Lawn Mowers of 2026", "url": "https://www.popsci.com/gear/best-robot-lawn-mowers/", "source": "Popular Science"},
   ],
   {
     "commentary": "The Mammotion Luba 3 AWD 5000 stays at number one because it handles the lawns that defeat every other robot mower, and that capability is the whole reason to buy at the top. The all-wheel drive climbs slopes that strand rivals, the wire-free RTK navigation means no buried boundary cable to install or repair, and it covers large yards without getting stuck. For anyone with a real yard rather than a flat suburban square, this is the one that actually does the job. The Ecovacs Goat A3000 LiDAR Pro holds second as the best navigation choice, its LiDAR maps and obstacle avoidance are the most reliable in the category, the pick for complex yards with trees, beds and tight passages. The Ecovacs Goat A3000 LiDAR stays third as the value version of that same smarts. The Navimow X315 holds fourth for large open lawns. Nothing this week reordered the field. The read: best for slopes and big yards is the Luba 3, best navigation is the Goat A3000 Pro, and the wire-free RTK and LiDAR systems made boundary wire obsolete this generation.",
     "highlights": [
       {"title": "Mammotion Luba 3 AWD conquers tough lawns", "body": "All-wheel drive climbs slopes that strand rivals, wire-free RTK skips the buried cable, and it covers large yards without getting stuck. For a real yard rather than a flat square, it holds number one."},
       {"title": "Ecovacs Goat A3000 Pro is the navigation pick", "body": "Its LiDAR mapping and obstacle avoidance are the most reliable in the category, threading complex yards with trees, beds and tight passages. That smarts keeps it a firm second."},
       {"title": "Goat A3000 LiDAR is the value version", "body": "It brings the same reliable navigation down a price tier for buyers who want the smarts for less. For complex yards on a budget, it holds a solid third."},
       {"title": "Boundary wire is obsolete now", "body": "Wire-free RTK and LiDAR navigation removed the buried cable that made early robot mowers a chore to install. This generation, skip any model that still needs a perimeter wire buried around your lawn."},
     ],
   },
   {
     "commentary": "Mammotion Luba 3 AWD 5000 我還是放第一，因為它搞得定打敗其他每台機器割草機的草坪，而這份能力就是在頂端購買的全部理由。四輪驅動能爬上困住對手的坡，無線 RTK 導航代表沒有要埋或修的邊界線，又能蓋大院子而不卡住。對任何有真正院子、而非平坦郊區方塊的人，這台真的把活做完。Ecovacs Goat A3000 LiDAR Pro 守第二，是最佳導航選擇，它的 LiDAR 地圖跟避障是這類別最可靠的，給有樹、花床跟狹窄通道的複雜院子。Ecovacs Goat A3000 LiDAR 守第三，是同樣智慧的性價比版。Navimow X315 守第四，給大片開闊草坪。這週沒事件重排。判斷：坡地跟大院子選 Luba 3、導航選 Goat A3000 Pro，無線 RTK 跟 LiDAR 系統這一代讓邊界線過時了。",
     "highlights": [
       {"title": "Mammotion Luba 3 AWD 征服難搞草坪", "body": "四輪驅動爬上困住對手的坡、無線 RTK 省去埋線、蓋大院子不卡住。對真正的院子而非平坦方塊，守住第一。"},
       {"title": "Ecovacs Goat A3000 Pro 是導航選擇", "body": "LiDAR 地圖跟避障是這類別最可靠的，穿過有樹、花床跟狹窄通道的複雜院子。這份智慧讓它穩在第二。"},
       {"title": "Goat A3000 LiDAR 是性價比版", "body": "它把同樣可靠的導航帶到低一階，給想要智慧又省錢的買家。複雜院子又預算有限，它穩坐第三。"},
       {"title": "邊界線現在過時了", "body": "無線 RTK 跟 LiDAR 導航拿掉了讓早期機器割草機難安裝的埋線。這一代，跳過任何還要在草坪周圍埋線的型號。"},
     ],
   })

# ---------------- best-robotic-pool-cleaners ----------------
do("best-robotic-pool-cleaners.json",
   [
     {"title": "Best robotic pool cleaner 2026 reviews", "url": "https://www.popularmechanics.com/home/g42345/best-robotic-pool-cleaners/", "source": "Popular Mechanics"},
     {"title": "The Best Robotic Pool Cleaners of 2026", "url": "https://www.cnet.com/home/yard-and-outdoors/best-robotic-pool-cleaner/", "source": "CNET"},
   ],
   {
     "commentary": "The Dolphin Premier stays at number one because Maytronics has been making the most reliable pool robots for years, and the Premier is the one that cleans thoroughly, climbs walls properly and keeps running season after season. The multi-media filtration handles everything from fine silt to leaves, the scrubbing actually lifts grime rather than pushing it around, and reliability is the trait that matters most in a machine that lives in water. For most pool owners this is the safe, proven buy. The Beatbot AquaSense 2 Ultra holds a close second as the cordless future done right, no cord to tangle, smart mapping that cleans efficiently, and surface-skimming plus floor cleaning in one unit. The choice between it and the Dolphin is corded reliability versus cordless convenience. The Dolphin Nautilus CC Plus WiFi stays third as the value pick, less premium but genuinely capable. The Aiper Scuba S1 holds fourth as the value cordless option. Nothing this week reordered the field. The read: best proven reliability is the Dolphin Premier, best cordless is the Beatbot, best value is the Nautilus CC Plus.",
     "highlights": [
       {"title": "Dolphin Premier is the proven, reliable best", "body": "Multi-media filtration handles silt to leaves, the scrubbing lifts grime rather than pushing it, and it runs season after season. Reliability matters most in a machine that lives in water, holding number one."},
       {"title": "Beatbot AquaSense 2 Ultra is cordless done right", "body": "No cord to tangle, smart mapping for efficient cleaning, and surface skimming plus floor cleaning in one unit. For buyers who want convenience over cord reliability, it is a very close second."},
       {"title": "Dolphin Nautilus CC Plus is the value pick", "body": "Less premium but genuinely capable, it brings Maytronics reliability to a lower price. For pool owners who want a proven brand on a budget, it holds a solid third."},
       {"title": "Corded reliability versus cordless convenience", "body": "The Dolphin's cord is a minor hassle but rock-solid; the Beatbot's freedom comes with battery limits. Decide whether you value proven uptime or no cord, and the top choice falls out cleanly."},
     ],
   },
   {
     "commentary": "Dolphin Premier 我還是放第一，因為 Maytronics 多年來做的是最可靠的泳池機器人，而 Premier 是那台清得徹底、會好好爬牆、一季又一季持續運轉的。多媒體過濾從細泥到落葉全收，刷洗是真的把污垢抬起而非推來推去，而可靠正是一台活在水裡的機器最重要的特質。對多數泳池主，這是安全、經過驗證的買法。Beatbot AquaSense 2 Ultra 緊咬第二，是把無線未來做對的代表，沒有會纏的線、聰明地圖高效清潔、表面撇渣加底部清潔一機到位。它跟 Dolphin 之間的選擇是有線可靠對無線方便。Dolphin Nautilus CC Plus WiFi 守第三，是性價比選擇，沒那麼高階但真的能幹。Aiper Scuba S1 守第四，是性價比無線選擇。這週沒事件重排。判斷：經驗證可靠選 Dolphin Premier、無線選 Beatbot、性價比選 Nautilus CC Plus。",
     "highlights": [
       {"title": "Dolphin Premier 是經驗證的可靠之最", "body": "多媒體過濾從細泥到落葉全收、刷洗把污垢抬起而非推來推去、一季又一季運轉。活在水裡的機器最重可靠，守住第一。"},
       {"title": "Beatbot AquaSense 2 Ultra 把無線做對", "body": "沒有會纏的線、聰明地圖高效清潔、表面撇渣加底部清潔一機到位。想要方便勝過有線可靠的買家，它緊咬第二。"},
       {"title": "Dolphin Nautilus CC Plus 是性價比選擇", "body": "沒那麼高階但真的能幹，把 Maytronics 的可靠帶到低價。想要經驗證品牌又預算有限的泳池主，它穩坐第三。"},
       {"title": "有線可靠對無線方便", "body": "Dolphin 的線是小麻煩但超穩；Beatbot 的自由伴隨電池限制。決定你重視經驗證的妥當還是無線，首選就乾淨地出來。"},
     ],
   })

# ---------------- best-mattresses ----------------
do("best-mattresses.json",
   [
     {"title": "Best mattress 2026 reviews", "url": "https://www.nytimes.com/wirecutter/reviews/best-mattress/", "source": "Wirecutter"},
     {"title": "The Best Mattresses of 2026", "url": "https://www.sleepfoundation.org/best-mattress", "source": "Sleep Foundation"},
   ],
   {
     "commentary": "The Saatva Classic stays at number one because it does what most bed-in-a-box mattresses cannot: it feels like a genuinely premium hotel mattress, with real coil support, durable construction and the kind of edge support that lets you actually use the whole bed. It suits the most sleepers across firmness options, it does not sag in two years like cheaper foam, and you can try it risk-free. For the broadest set of buyers who want one mattress that just works, this is the safe, proven pick. The Helix Midnight Luxe holds second as the best for side sleepers, the pressure relief at the shoulders and hips is dialed in for the most common sleep position, the pick if you wake up sore. The Purple Restore Hybrid stays third as the cooling-and-pressure standout with its distinctive grid that sleeps cooler than foam. The Bear Elite Hybrid holds fourth for active recovery. Nothing this week reordered the field. The read: best all-round is the Saatva, best for side sleepers is the Helix, best for hot sleepers is the Purple. Buy for your actual sleep position, because that decides comfort more than any spec.",
     "highlights": [
       {"title": "Saatva Classic feels genuinely premium", "body": "Real coil support, durable construction and edge support that lets you use the whole bed, suiting the most sleepers across firmness options. For one mattress that just works, it holds number one."},
       {"title": "Helix Midnight Luxe is best for side sleepers", "body": "Its pressure relief at the shoulders and hips is dialed in for the most common sleep position. For people who wake up sore on the side, it is the targeted pick and a firm second."},
       {"title": "Purple Restore Hybrid sleeps coolest", "body": "Its distinctive grid sleeps noticeably cooler than foam while still relieving pressure. For hot sleepers who overheat on memory foam, it is the standout and a solid third."},
       {"title": "Buy for your sleep position", "body": "Side sleepers need shoulder and hip pressure relief, back sleepers need support, hot sleepers need cooling. Your actual sleep position decides comfort more than any spec, so match the mattress to how you lie."},
     ],
   },
   {
     "commentary": "Saatva Classic 我還是放第一，因為它做到多數壓縮床墊做不到的事：它睡起來像真正高級的飯店床墊，有真的彈簧支撐、耐用結構，還有那種讓你能真的用到整張床的邊緣支撐。它在不同軟硬度選項裡適合最多睡眠者，又不像便宜泡棉兩年就塌，而且你能無風險試睡。對最廣、想要一張就這樣好用的床墊的買家，這是安全、經過驗證的選擇。Helix Midnight Luxe 守第二，是側睡最佳，肩膀跟臀部的減壓針對最常見的睡姿調好，起床會痠的人選它。Purple Restore Hybrid 守第三，是散熱兼減壓亮點，獨特的格狀層睡起來比泡棉涼。Bear Elite Hybrid 守第四，給運動恢復。這週沒事件重排。判斷：全能選 Saatva、側睡選 Helix、怕熱選 Purple。照你真實睡姿買，因為那比任何規格更能決定舒適。",
     "highlights": [
       {"title": "Saatva Classic 睡起來真的高級", "body": "真的彈簧支撐、耐用結構、讓你用到整張床的邊緣支撐，不同軟硬度適合最多睡眠者。要一張就這樣好用的床墊，守住第一。"},
       {"title": "Helix Midnight Luxe 側睡最佳", "body": "肩膀跟臀部的減壓針對最常見睡姿調好。側睡起床會痠的人，它是針對性選擇，穩在第二。"},
       {"title": "Purple Restore Hybrid 睡得最涼", "body": "獨特格狀層睡起來比泡棉明顯涼，又能減壓。在記憶棉上會過熱的怕熱睡眠者，它是亮點，穩坐第三。"},
       {"title": "照你睡姿買", "body": "側睡要肩臀減壓、仰睡要支撐、怕熱要散熱。你真實的睡姿比任何規格更能決定舒適，把床墊對準你怎麼躺。"},
     ],
   })

# ---------------- best-portable-air-conditioners ----------------
do("best-portable-air-conditioners.json",
   [
     {"title": "Best portable air conditioner 2026 reviews", "url": "https://www.nytimes.com/wirecutter/reviews/best-portable-air-conditioner/", "source": "Wirecutter"},
     {"title": "The Best Portable Air Conditioners of 2026", "url": "https://www.rtings.com/air-conditioner/reviews/best/portable", "source": "RTINGS"},
   ],
   {
     "commentary": "The Midea Duo MAP14HS1TBL stays at number one because it solves the inefficiency that makes most portable AC units a disappointment. The dual-hose design cools far more effectively than the single-hose units that re-heat the room they are trying to cool, and the inverter compressor keeps the running cost and noise down. The result is a portable that actually cools a real room rather than just stirring warm air. For most people who cannot install a window unit, this is the one worth buying. The Whynter NEX ARC 1230WN holds second as the strong dual-hose alternative with reliable cooling and a cleaner design. The LG LP1419IVSM stays third as the brand-name inverter pick with quiet operation. The Hisense HAP0824TWD holds fourth as the value choice for smaller rooms. Nothing this week reordered the field. The read: best overall is the Midea Duo, best alternative is the Whynter, and the single most important spec is dual-hose, because a single-hose unit fights itself and never cools as well. Buy dual-hose and an inverter, and skip the rest.",
     "highlights": [
       {"title": "Midea Duo solves portable AC inefficiency", "body": "Its dual-hose design cools far better than single-hose units that re-heat the room, and the inverter keeps cost and noise down. For people who cannot install a window unit, it holds number one."},
       {"title": "Whynter NEX ARC 1230WN is the strong alternative", "body": "Reliable dual-hose cooling with a cleaner design makes it the backup pick to the Midea. For buyers who want effective cooling from a proven brand, it is a firm second."},
       {"title": "LG LP1419IVSM is the quiet brand pick", "body": "Its inverter compressor runs quietly with dependable cooling and the polish of a major brand. For buyers who value quiet operation and support, it holds a solid third."},
       {"title": "Dual-hose is the spec that matters", "body": "A single-hose unit pulls cooled air back out and re-heats the room, fighting itself the whole time. Buy dual-hose with an inverter and skip everything else, because that one choice decides whether it actually cools."},
     ],
   },
   {
     "commentary": "Midea Duo MAP14HS1TBL 我還是放第一，因為它解決了讓多數移動式冷氣令人失望的低效率問題。雙管設計比那些把自己想冷卻的房間重新加熱的單管機冷卻有效太多，變頻壓縮機又把運轉成本跟噪音壓低。結果是一台真的冷得了一間真房間、而非只是攪動暖空氣的移動式冷氣。對多數無法裝窗型的人，這台值得買。Whynter NEX ARC 1230WN 守第二，是強力雙管替代，冷卻可靠、設計更乾淨。LG LP1419IVSM 守第三，是品牌變頻選擇，運轉安靜。Hisense HAP0824TWD 守第四，是小房間的性價比選擇。這週沒事件重排。判斷：整體選 Midea Duo、替代選 Whynter，單一最重要的規格是雙管，因為單管機跟自己打架、永遠冷不夠。買雙管加變頻，其他跳過。",
     "highlights": [
       {"title": "Midea Duo 解決移動冷氣低效率", "body": "雙管設計比把房間重新加熱的單管機冷卻有效太多，變頻又把成本跟噪音壓低。對無法裝窗型的人，守住第一。"},
       {"title": "Whynter NEX ARC 1230WN 是強力替代", "body": "可靠的雙管冷卻加更乾淨的設計，讓它是 Midea 的備選。想要經驗證品牌有效冷卻的買家，它穩在第二。"},
       {"title": "LG LP1419IVSM 是安靜品牌選擇", "body": "變頻壓縮機運轉安靜、冷卻可靠，加上大品牌的精緻。重視安靜運轉跟售後的買家，它穩坐第三。"},
       {"title": "雙管是最重要的規格", "body": "單管機把冷卻的空氣抽回去又把房間重新加熱，整個過程跟自己打架。買雙管加變頻、其他跳過，因為這一個選擇決定它到底冷不冷。"},
     ],
   })

print("batchH done")
