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

# ---------------- best-treadmills ----------------
do("best-treadmills.json",
   [
     {"title": "Best treadmill 2026 reviews", "url": "https://www.runnersworld.com/gear/a20865012/best-treadmills/", "source": "Runner's World"},
     {"title": "The Best Treadmills of 2026", "url": "https://www.garagegymreviews.com/best-treadmills", "source": "Garage Gym Reviews"},
   ],
   {
     "commentary": "The NordicTrack Commercial 1750 stays at number one because it is the treadmill that gets the fundamentals right for the people who actually use one regularly. The cushioning protects your knees over years of miles, the deck is large enough for a real running stride, and the build holds up to daily use without the wobble that plagues cheaper machines. The iFit integration is genuinely good if you want guided runs, and you can ignore it if you do not. For most home gyms this is the proven workhorse. The NordicTrack X24 Incline holds second as the step-up for people who want serious incline training and a bigger screen. The Sole F80 stays third as the no-subscription pick, it is the treadmill I recommend to people who just want a great deck without paying monthly for content. The Bowflex Treadmill 22 holds fourth. Nothing this week reordered the field. The read: best all-round is the Commercial 1750, best incline is the X24, best no-subscription is the Sole F80. Buy for whether you want guided content or just a solid machine to run on.",
     "highlights": [
       {"title": "NordicTrack Commercial 1750 is the proven workhorse", "body": "Cushioning that protects your knees over years, a deck large enough for a real stride and a build that survives daily use. With optional iFit you can take or leave, it holds number one for most home gyms."},
       {"title": "NordicTrack X24 is the incline step-up", "body": "Serious incline training and a bigger screen make it the pick for people who want hill work and immersion. For buyers who train inclines, it is the natural upgrade and a firm second."},
       {"title": "Sole F80 is the no-subscription pick", "body": "A great deck without paying monthly for content makes it the choice for people who just want to run. For buyers who skip guided classes, it holds a solid third on value and build."},
       {"title": "Decide content versus just running", "body": "NordicTrack leans on iFit guided runs, the Sole skips subscriptions entirely. Figure out whether you want coached workouts or simply a reliable deck, and the right treadmill becomes obvious."},
     ],
   },
   {
     "commentary": "NordicTrack Commercial 1750 我還是放第一，因為它對真正規律使用的人把基本功做對了。緩衝在好幾年的里程裡保護你的膝蓋，跑板大到容得下真正的跑步步幅，做工撐得過每天使用、沒有便宜機器那種晃動。想要引導跑步的話 iFit 整合真的不錯，不想要的話可以無視。對多數家用健身房，這是經過驗證的主力。NordicTrack X24 Incline 守第二，是給想要認真坡度訓練跟更大螢幕的人的升級。Sole F80 守第三，是免訂閱選擇，我會推薦給只想要好跑板、不想每月付內容費的人。Bowflex Treadmill 22 守第四。這週沒事件重排。判斷：全能選 Commercial 1750、坡度選 X24、免訂閱選 Sole F80。照你要引導內容還是只要一台紮實機器來跑買。",
     "highlights": [
       {"title": "NordicTrack Commercial 1750 是經驗證主力", "body": "好幾年里程裡保護膝蓋的緩衝、容得下真正步幅的跑板、撐得過每天使用的做工。iFit 可有可無，對多數家用健身房守住第一。"},
       {"title": "NordicTrack X24 是坡度升級", "body": "認真的坡度訓練加更大螢幕，讓它是想要爬坡跟沉浸的人的選擇。練坡度的買家，它是自然升級，穩在第二。"},
       {"title": "Sole F80 是免訂閱選擇", "body": "好跑板又不用每月付內容費，讓它是只想跑步的人的選擇。跳過引導課程的買家，它靠性價比跟做工穩坐第三。"},
       {"title": "決定內容還是只要跑步", "body": "NordicTrack 靠 iFit 引導跑步，Sole 完全跳過訂閱。搞清楚你要教練課程還是單純一台可靠跑板，對的跑步機就很明顯。"},
     ],
   })

# ---------------- best-massage-guns ----------------
do("best-massage-guns.json",
   [
     {"title": "Best massage gun 2026 reviews", "url": "https://www.garagegymreviews.com/best-massage-guns", "source": "Garage Gym Reviews"},
     {"title": "The Best Percussion Massage Guns of 2026", "url": "https://www.menshealth.com/fitness/g26847676/best-massage-guns/", "source": "Men's Health"},
   ],
   {
     "commentary": "The Theragun Pro Plus stays at number one because Therabody still makes the massage gun that does the job best, and the Pro Plus adds genuinely useful features without losing what made the line great. The amplitude reaches deep into muscle in a way cheaper guns cannot, the build survives years of use, and the added therapies like heat and vibration are real additions rather than gimmicks. For anyone serious about recovery, this is the tool that earns its premium. The Rally Orbital Massager holds second as the innovative challenger, its orbital motion covers more tissue per pass and the design is genuinely fresh, the pick for people who want something beyond standard percussion. The Hyperice Hypervolt 2 Pro stays third as the quiet, refined option with the smoothest operation in the category. The Therabody Theragun Prime holds fourth as the value Theragun. Nothing this week reordered the field. The read: best overall is the Pro Plus, most innovative is the Rally, quietest is the Hypervolt. Buy for depth if you have dense muscle, quiet if you use it around others.",
     "highlights": [
       {"title": "Theragun Pro Plus does the job best", "body": "Amplitude that reaches deep into muscle, a build that survives years and genuinely useful heat and vibration therapies. For anyone serious about recovery, it earns its premium at number one."},
       {"title": "Rally Orbital Massager is the fresh challenger", "body": "Its orbital motion covers more tissue per pass than standard percussion, a genuinely new approach. For people who want something beyond the usual gun, it is the innovative pick and a firm second."},
       {"title": "Hyperice Hypervolt 2 Pro is the quietest", "body": "The smoothest, quietest operation in the category makes it the pick for use around others. For buyers who massage in shared spaces, that refinement holds it a solid third."},
       {"title": "Buy for depth or for quiet", "body": "Dense, large muscles need the deep amplitude of the Theragun; using it near others or late at night rewards the quiet Hypervolt. Match the gun to your muscle and your environment, not the spec list."},
     ],
   },
   {
     "commentary": "Theragun Pro Plus 我還是放第一，因為 Therabody 還是做出那把把活做得最好的按摩槍，而 Pro Plus 加了真的實用的功能、又沒丟掉讓這系列出色的東西。衝程深入肌肉的方式是便宜槍做不到的，做工撐得過好幾年，加進來的熱療跟振動是真的加分而非噱頭。對任何認真看待恢復的人，這把工具掙得起它的高價。Rally Orbital Massager 守第二，是創新挑戰者，軌道運動每一下覆蓋更多組織、設計也真的新鮮，給想要標準震動之外東西的人。Hyperice Hypervolt 2 Pro 守第三，是安靜精緻選擇，運轉是這類別最順的。Therabody Theragun Prime 守第四，是性價比 Theragun。這週沒事件重排。判斷：整體選 Pro Plus、最創新選 Rally、最安靜選 Hypervolt。肌肉密就買深度，在別人旁邊用就買安靜。",
     "highlights": [
       {"title": "Theragun Pro Plus 把活做得最好", "body": "深入肌肉的衝程、撐過好幾年的做工、真的實用的熱療跟振動。對任何認真看待恢復的人，它在第一名掙起高價。"},
       {"title": "Rally Orbital Massager 是新鮮挑戰者", "body": "軌道運動每一下覆蓋比標準震動更多組織，是真的新做法。想要常規槍之外東西的人，它是創新選擇，穩在第二。"},
       {"title": "Hyperice Hypervolt 2 Pro 最安靜", "body": "這類別最順最安靜的運轉，讓它是在別人旁邊用的選擇。在共享空間按摩的買家，這份精緻讓它穩坐第三。"},
       {"title": "買深度或買安靜", "body": "密實的大肌肉需要 Theragun 的深衝程；在別人旁邊或深夜用就獎勵安靜的 Hypervolt。把槍對準你的肌肉跟環境，而非規格清單。"},
     ],
   })

# ---------------- best-electric-bikes ----------------
do("best-electric-bikes.json",
   [
     {"title": "Best electric bike 2026 reviews", "url": "https://electrek.co/best-electric-bikes/", "source": "Electrek"},
     {"title": "The Best Electric Bikes of 2026", "url": "https://www.bicycling.com/bikes-gear/best-electric-bikes/", "source": "Bicycling"},
   ],
   {
     "commentary": "The Aventon Level 3 stays at number one because it nails the commuter e-bike brief better than anything at its price, and that value is the whole reason it leads. The range covers a real commute and then some, the integrated lights, fenders and rack mean it is ready to ride out of the box, and Aventon's torque sensor delivers power that feels natural rather than the lurchy on-off of cheaper hub motors. For most people buying an e-bike to actually replace car trips, this is the smart buy. The Lectric XP4 750 holds second as the value-and-versatility champion, the folding design and low price make e-biking accessible, and it is the bike I recommend to people on a budget. The Velotric Discover 3 stays third as the comfortable all-rounder with a smooth ride and clean design. The Segway Xyber and others carry forward. Nothing this week reordered the field. The read: best commuter is the Level 3, best value is the Lectric XP4, best comfort is the Velotric. Buy the torque-sensor bike if you can, because natural power delivery is the upgrade you feel every ride.",
     "highlights": [
       {"title": "Aventon Level 3 nails the commuter brief", "body": "Real commute range, integrated lights, fenders and rack ready out of the box, and a torque sensor that delivers natural power. For people replacing car trips with an e-bike, it is the smart buy at number one."},
       {"title": "Lectric XP4 750 is the value champion", "body": "A folding design and low price make e-biking accessible without giving up usable range. For budget buyers who want a genuine e-bike, it is the recommendation and a firm second."},
       {"title": "Velotric Discover 3 is the comfort all-rounder", "body": "A smooth ride and clean design make it the pick for relaxed riding rather than aggressive commuting. For comfort-focused buyers, it holds a solid third."},
       {"title": "Buy a torque-sensor bike", "body": "Torque sensors deliver power proportional to your pedaling, which feels natural; cheap cadence sensors lurch on and off. That single component is the upgrade you feel on every ride, so prioritize it."},
     ],
   },
   {
     "commentary": "Aventon Level 3 我還是放第一，因為它把通勤電動車的需求做得比同價位任何東西都好，而這份性價比就是它領先的全部理由。續航蓋得過真正的通勤還有餘，整合的車燈、擋泥板跟貨架代表開箱就能騎，Aventon 的扭力感測器給出感覺自然的動力、而非便宜輪轂馬達那種一開一關的頓挫。對多數買電動車真的要取代開車的人，這是聰明買法。Lectric XP4 750 守第二，是性價比兼多功能冠軍，折疊設計加低價讓騎電動車變得親民，是我推薦給預算有限的人的車。Velotric Discover 3 守第三，是舒適全能款，騎乘平順、設計乾淨。Segway Xyber 等照舊。這週沒事件重排。判斷：通勤選 Level 3、性價比選 Lectric XP4、舒適選 Velotric。能買扭力感測器的車就買，因為自然的動力輸出是你每次騎都感受得到的升級。",
     "highlights": [
       {"title": "Aventon Level 3 把通勤需求做對", "body": "真正的通勤續航、整合車燈擋泥板貨架開箱即騎、扭力感測器給自然動力。對用電動車取代開車的人，它是第一名聰明買法。"},
       {"title": "Lectric XP4 750 是性價比冠軍", "body": "折疊設計加低價讓騎電動車親民，又沒犧牲可用續航。想要真正電動車的預算買家，它是推薦，穩在第二。"},
       {"title": "Velotric Discover 3 是舒適全能款", "body": "平順騎乘加乾淨設計，讓它是輕鬆騎而非積極通勤的選擇。重視舒適的買家，它穩坐第三。"},
       {"title": "買扭力感測器的車", "body": "扭力感測器給的動力跟你踩踏成正比、感覺自然；便宜的踏頻感測器一開一關頓挫。這一個零件是你每次騎都感受到的升級，把它擺優先。"},
     ],
   })

# ---------------- best-electric-scooters ----------------
do("best-electric-scooters.json",
   [
     {"title": "Best electric scooter 2026 reviews", "url": "https://electrek.co/best-electric-scooters/", "source": "Electrek"},
     {"title": "The Best Electric Scooters of 2026", "url": "https://www.rideapart.com/reviews/best-electric-scooters/", "source": "RideApart"},
   ],
   {
     "commentary": "The Segway Ninebot Max G3 stays at number one because it is the scooter that gets the commuter essentials right at a price most people can justify. The range genuinely covers a real round-trip commute, the ride is stable and comfortable thanks to the larger frame and suspension, and Segway's build quality and service network mean it is the safe long-term buy rather than a gamble. For most people commuting on a scooter, this is the proven default. The Apollo City Pro holds second as the step-up for ride quality, the dual suspension and premium feel make it the most comfortable in the class, the pick for rougher city streets. The NIU KQi3 Pro stays third as the value all-rounder that does everything well for less. The Apollo Go holds fourth. Nothing this week reordered the field. The read: best commuter is the Max G3, best ride quality is the Apollo City Pro, best value is the NIU. Prioritize suspension and tire size if your roads are rough, because a smooth ride is what keeps you actually using the scooter.",
     "highlights": [
       {"title": "Segway Ninebot Max G3 nails the commute", "body": "Real round-trip range, a stable comfortable ride from the larger frame and suspension, plus Segway's build and service network. For most scooter commuters it is the proven default at number one."},
       {"title": "Apollo City Pro is the ride-quality step-up", "body": "Dual suspension and a premium feel make it the most comfortable in the class. For riders on rougher city streets who want a smoother trip, it is the natural upgrade and a firm second."},
       {"title": "NIU KQi3 Pro is the value all-rounder", "body": "It does everything well for less, making it the pick for buyers who want a solid commuter without spending up. That balance holds it a solid third."},
       {"title": "Prioritize suspension on rough roads", "body": "Suspension and larger tires decide whether a scooter is comfortable or punishing on real city streets. If your commute has cracks and curbs, weight ride quality over top speed and you will ride it more."},
     ],
   },
   {
     "commentary": "Segway Ninebot Max G3 我還是放第一，因為它在多數人搆得到的價格上把通勤要素做對。續航真的蓋得過一趟來回通勤，較大車架加避震讓騎乘穩定舒適，Segway 的做工跟服務網又代表它是安全的長期買法、而非賭注。對多數騎滑板車通勤的人，這是經驗證的預設。Apollo City Pro 守第二，是騎乘品質的升級，雙避震加高級質感讓它是這級最舒適的，給較顛簸的市區街道。NIU KQi3 Pro 守第三，是性價比全能款，用更低價什麼都做得好。Apollo Go 守第四。這週沒事件重排。判斷：通勤選 Max G3、騎乘品質選 Apollo City Pro、性價比選 NIU。路爛就把避震跟輪胎尺寸擺優先，因為平順的騎乘才是讓你真的持續用滑板車的關鍵。",
     "highlights": [
       {"title": "Segway Ninebot Max G3 把通勤做對", "body": "真正來回通勤的續航、較大車架加避震的穩定舒適、Segway 的做工跟服務網。對多數滑板車通勤族，它是第一名經驗證的預設。"},
       {"title": "Apollo City Pro 是騎乘品質升級", "body": "雙避震加高級質感讓它是這級最舒適的。在較顛簸市區街道、想要更平順的騎士，它是自然升級，穩在第二。"},
       {"title": "NIU KQi3 Pro 是性價比全能款", "body": "用更低價什麼都做得好，是想要紮實通勤車又不想多花的買家的選擇。這份平衡讓它穩坐第三。"},
       {"title": "路爛就把避震擺優先", "body": "避震跟較大輪胎決定滑板車在真實街道上是舒適還是折磨。通勤路有裂縫跟路緣，把騎乘品質擺在極速之前，你才會多騎。"},
     ],
   })

# ---------------- best-pickleball-paddles ----------------
do("best-pickleball-paddles.json",
   [
     {"title": "Best pickleball paddle 2026 reviews", "url": "https://www.pickleballcentral.com/best-paddles", "source": "Pickleball Central"},
     {"title": "The Best Pickleball Paddles of 2026", "url": "https://pickleball.com/gear/best-pickleball-paddles", "source": "Pickleball.com"},
   ],
   {
     "commentary": "The Joola Perseus Pro IV 16mm stays at number one because it is the paddle that the most serious players keep coming back to, and that is the clearest signal in equipment. The thermoformed construction delivers a genuinely large sweet spot, the spin generation is among the best in the game thanks to the surface texture, and the balance of power and control suits the widest range of playing styles. For competitive players who want one paddle to play their whole game, this is the benchmark. The Honolulu J2CR holds second as the power-and-spin specialist that is winning over aggressive players, the pop off the face is exceptional. The Bread & Butter Loco 16mm Hybrid stays third as the value-leaning performance pick with a genuinely premium feel for less. The Selkirk LABS Project Boomstik holds fourth as the boutique power option. Nothing this week reordered the field. The read: best all-round is the Perseus Pro IV, best power and spin is the Honolulu, best value performance is the Bread & Butter. Pick the 16mm for control or a thinner core for power, because core thickness shapes your whole game more than the brand name.",
     "highlights": [
       {"title": "Joola Perseus Pro IV is the benchmark", "body": "A large sweet spot, top-tier spin from the surface texture and a power-control balance suiting the widest range of styles. For competitive players who want one paddle for their whole game, it holds number one."},
       {"title": "Honolulu J2CR is the power-and-spin pick", "body": "Exceptional pop off the face is winning over aggressive players who attack. For those who play a power game and want spin to match, it is the specialist choice and a firm second."},
       {"title": "Bread & Butter Loco is the value performer", "body": "A genuinely premium feel for less makes it the pick for players who want top performance without the top price. That value-to-feel balance holds it a solid third."},
       {"title": "Core thickness shapes your game", "body": "A 16mm core leans control and forgiveness; a thinner core leans power and pop. That single spec shapes how the paddle plays more than the brand, so choose thickness by whether you control or attack."},
     ],
   },
   {
     "commentary": "Joola Perseus Pro IV 16mm 我還是放第一，因為它是最認真的球員一再回頭選的拍子，而這在裝備裡是最清楚的訊號。熱成型結構帶來真的很大的甜蜜點，表面紋理讓旋轉生成是場上數一數二的，力量跟控制的平衡又適合最廣的打法。對想要一支拍子打完整場的競技球員，這是標竿。Honolulu J2CR 守第二，是力量兼旋轉專家，正在贏得積極型球員的心，拍面的彈射出色。Bread & Butter Loco 16mm Hybrid 守第三，是偏性價比的performance選擇，用更低價給真的高級的手感。Selkirk LABS Project Boomstik 守第四，是精品力量選擇。這週沒事件重排。判斷：全能選 Perseus Pro IV、力量旋轉選 Honolulu、性價比performance選 Bread & Butter。控制選 16mm、力量選較薄核心，因為核心厚度比品牌名更能塑造你的整場球。",
     "highlights": [
       {"title": "Joola Perseus Pro IV 是標竿", "body": "大甜蜜點、表面紋理帶來的頂級旋轉、適合最廣打法的力量控制平衡。對想要一支拍子打完整場的競技球員，守住第一。"},
       {"title": "Honolulu J2CR 是力量旋轉選擇", "body": "拍面出色的彈射正贏得積極進攻球員的心。打力量球又想要相稱旋轉的人，它是專家選擇，穩在第二。"},
       {"title": "Bread & Butter Loco 是性價比好手", "body": "用更低價給真的高級的手感，是想要頂級表現又不付頂價球員的選擇。這份性價比與手感的平衡讓它穩坐第三。"},
       {"title": "核心厚度塑造你的球", "body": "16mm 核心偏控制跟容錯；較薄核心偏力量跟彈射。這一個規格比品牌更能塑造拍子怎麼打，照你控制還是進攻選厚度。"},
     ],
   })

# ---------------- best-standing-desks ----------------
do("best-standing-desks.json",
   [
     {"title": "Best standing desk 2026 reviews", "url": "https://www.nytimes.com/wirecutter/reviews/best-standing-desks/", "source": "Wirecutter"},
     {"title": "The Best Standing Desks of 2026", "url": "https://www.pcmag.com/picks/the-best-standing-desks", "source": "PCMag"},
   ],
   {
     "commentary": "The Uplift V2 Commercial stays at number one because it is the standing desk that gets the one thing that matters most exactly right: stability. At full standing height it stays rock-solid where cheaper desks wobble every time you type, the build quality justifies the price over years of daily use, and the customization options let you spec exactly the desk you want. The industry-leading warranty tells you the company stands behind it. For most people buying a desk they will use every workday, this is the proven choice. The FlexiSpot E7 Pro 2026 holds second as the value champion, it delivers most of the Uplift's stability for noticeably less and is the desk I recommend to people on a budget. The Secretlab Magnus Pro stays third as the premium integrated option with the cleanest cable management in the category. The Branch Duo holds fourth. Nothing this week reordered the field. The read: best overall is the Uplift V2, best value is the FlexiSpot E7 Pro, best integrated is the Magnus Pro. Prioritize stability at standing height, because a wobbly desk is one you stop raising.",
     "highlights": [
       {"title": "Uplift V2 Commercial nails stability", "body": "It stays rock-solid at full standing height where cheaper desks wobble, with build quality and an industry-leading warranty that justify the price over years. For a daily-use desk, it holds number one."},
       {"title": "FlexiSpot E7 Pro is the value champion", "body": "It delivers most of the Uplift's stability for noticeably less, making it the recommendation for budget buyers. That value-to-performance balance keeps it a firm second."},
       {"title": "Secretlab Magnus Pro is the integrated pick", "body": "The cleanest cable management in the category makes it the choice for people who want a tidy, premium setup. That integration and design hold it a solid third."},
       {"title": "Stability is the spec that matters", "body": "A desk that wobbles at standing height is one you stop raising, defeating the entire purpose. Prioritize rigidity over features or price, because a stable desk is the one you actually stand at."},
     ],
   },
   {
     "commentary": "Uplift V2 Commercial 我還是放第一，因為它把最重要的那一件事做到完全正確：穩定。在站立全高它穩如磐石，便宜桌子每次打字都晃，它的做工在好幾年每天使用裡對得起價格，客製選項又讓你規格出剛好想要的桌子。業界領先的保固告訴你這家公司挺它。對多數買一張每個工作天都會用的桌子的人，這是經驗證的選擇。FlexiSpot E7 Pro 2026 守第二，是性價比冠軍，用明顯更低的價格給出 Uplift 大部分的穩定，是我推薦給預算有限的人的桌子。Secretlab Magnus Pro 守第三，是高階整合選擇，理線是這類別最乾淨的。Branch Duo 守第四。這週沒事件重排。判斷：整體選 Uplift V2、性價比選 FlexiSpot E7 Pro、整合選 Magnus Pro。把站立高度的穩定擺優先，因為會晃的桌子就是你不再升高的桌子。",
     "highlights": [
       {"title": "Uplift V2 Commercial 把穩定做對", "body": "站立全高穩如磐石，便宜桌子會晃，做工跟業界領先保固在好幾年裡對得起價格。對每天用的桌子，守住第一。"},
       {"title": "FlexiSpot E7 Pro 是性價比冠軍", "body": "用明顯更低的價格給出 Uplift 大部分的穩定，是預算買家的推薦。這份性價比與效能的平衡讓它穩在第二。"},
       {"title": "Secretlab Magnus Pro 是整合選擇", "body": "這類別最乾淨的理線，讓它是想要整潔高階配置的人的選擇。這份整合跟設計讓它穩坐第三。"},
       {"title": "穩定是最重要的規格", "body": "站立高度會晃的桌子就是你不再升高的桌子，整個目的就泡湯了。把剛性擺在功能或價格之前，因為穩定的桌子才是你真的會站著用的。"},
     ],
   })

# ---------------- best-portable-power-stations ----------------
do("best-portable-power-stations.json",
   [
     {"title": "Best portable power station 2026 reviews", "url": "https://www.tomsguide.com/best-picks/best-portable-power-stations", "source": "Tom's Guide"},
     {"title": "The Best Portable Power Stations of 2026", "url": "https://www.cnet.com/home/energy-and-utilities/best-portable-power-station/", "source": "CNET"},
   ],
   {
     "commentary": "The EcoFlow Delta 3 Plus stays at number one because it hits the sweet spot of capacity, output and charging speed that makes a power station genuinely useful rather than a heavy paperweight. The LiFePO4 battery lasts thousands of cycles so it is still going strong years from now, it recharges astonishingly fast from the wall, and the output handles real appliances rather than just phones. For most people who want backup power for outages or camping, this is the one that does it all without overpaying. The Bluetti Elite 200 V2 holds second as the capacity-and-value champion, it gives you more stored energy per dollar and the build is excellent, the pick for people who prioritize runtime. The Anker Solix C2000 Gen2 stays third as the portable-and-fast option that balances weight against capacity well. The EcoFlow Delta Pro 3 holds fourth as the whole-home backup flagship. Nothing this week reordered the field. The read: best all-round is the Delta 3 Plus, best capacity value is the Bluetti Elite 200 V2, best for home backup is the Delta Pro 3. Buy LiFePO4 chemistry, because it is the difference between a station that lasts a decade and one that fades in a few years.",
     "highlights": [
       {"title": "EcoFlow Delta 3 Plus does it all", "body": "A LiFePO4 battery good for thousands of cycles, astonishingly fast wall charging and output that handles real appliances. For outage backup or camping, it hits the sweet spot at number one without overpaying."},
       {"title": "Bluetti Elite 200 V2 is the capacity champion", "body": "It gives more stored energy per dollar with an excellent build, making it the pick for people who prioritize runtime. That value-to-capacity balance keeps it a firm second."},
       {"title": "Anker Solix C2000 Gen2 is portable and fast", "body": "It balances weight against capacity well for buyers who carry their power station to campsites. That portability-to-output balance holds it a solid third."},
       {"title": "Buy LiFePO4 chemistry", "body": "LiFePO4 cells last thousands of cycles where older lithium fades in a few years. That chemistry is the difference between a station that survives a decade and one you replace, so make it non-negotiable."},
     ],
   },
   {
     "commentary": "EcoFlow Delta 3 Plus 我還是放第一，因為它命中容量、輸出跟充電速度的甜蜜點，讓電源站真的實用、而非沉重的紙鎮。LiFePO4 電池撐幾千次循環，所以好幾年後還是很強，從牆插充電快得驚人，輸出又應付得了真正的家電而非只有手機。對多數想要停電或露營備援電力的人，這台什麼都做又不多花錢。Bluetti Elite 200 V2 守第二，是容量兼性價比冠軍，每塊錢給你更多儲能、做工又優秀，給優先續航的人。Anker Solix C2000 Gen2 守第三，是可攜兼快充選擇，重量跟容量平衡得好。EcoFlow Delta Pro 3 守第四，是全屋備援旗艦。這週沒事件重排。判斷：全能選 Delta 3 Plus、容量性價比選 Bluetti Elite 200 V2、家庭備援選 Delta Pro 3。買 LiFePO4 化學，因為那是一台撐十年跟幾年就衰退的差別。",
     "highlights": [
       {"title": "EcoFlow Delta 3 Plus 什麼都做", "body": "撐幾千次循環的 LiFePO4 電池、快得驚人的牆插充電、應付真正家電的輸出。停電備援或露營，它在第一名命中甜蜜點又不多花錢。"},
       {"title": "Bluetti Elite 200 V2 是容量冠軍", "body": "每塊錢給更多儲能、做工又優秀，是優先續航的人的選擇。這份性價比與容量的平衡讓它穩在第二。"},
       {"title": "Anker Solix C2000 Gen2 又可攜又快", "body": "重量跟容量平衡得好，給會把電源站帶去營地的買家。這份可攜與輸出的平衡讓它穩坐第三。"},
       {"title": "買 LiFePO4 化學", "body": "LiFePO4 電芯撐幾千次循環，舊鋰電幾年就衰退。那個化學是撐十年跟得換掉的差別，把它當不可妥協的條件。"},
     ],
   })

# ---------------- best-portable-chargers ----------------
do("best-portable-chargers.json",
   [
     {"title": "Best portable charger 2026 reviews", "url": "https://www.tomsguide.com/best-picks/best-power-banks", "source": "Tom's Guide"},
     {"title": "The Best Power Banks of 2026", "url": "https://www.pcmag.com/picks/the-best-power-banks", "source": "PCMag"},
   ],
   {
     "commentary": "The Anker Prime 26K 300W stays at number one because it is the power bank that can actually charge a laptop, not just top up a phone, and that capability puts it in a different league. The 300W output runs a MacBook Pro at full speed, the 26,000mAh capacity covers multiple device-days, and the build and display are genuinely premium. For anyone who travels with a laptop and is tired of hunting for outlets, this is the one bank that replaces them. The Anker Prime 27650 250W holds second as the higher-capacity sibling for people who want even more runtime. The Anker 737 PowerCore 24K stays third as the proven workhorse that has earned its reputation over years. The Ugreen Nexode 25000mAh 200W holds fourth as the value high-output alternative. Nothing this week reordered the field. The read: best laptop-capable is the Prime 26K, most capacity is the Prime 27650, best value high-output is the Ugreen. Match wattage to your devices, because a 300W bank is wasted on a phone but essential for a laptop. Buy the output your actual gear needs.",
     "highlights": [
       {"title": "Anker Prime 26K 300W charges a laptop", "body": "Its 300W output runs a MacBook Pro at full speed and 26,000mAh covers multiple device-days, with a premium build and display. For laptop travelers tired of hunting outlets, it holds number one."},
       {"title": "Anker Prime 27650 is the capacity sibling", "body": "It brings even more runtime for people who want maximum stored power in one bank. For heavy users who need multiple full charges, it is the high-capacity pick and a firm second."},
       {"title": "Anker 737 PowerCore 24K is the proven workhorse", "body": "It has earned its reputation over years of reliable service. For buyers who want a dependable high-output bank with a track record, it holds a solid third."},
       {"title": "Match wattage to your devices", "body": "A 300W bank is overkill for a phone but essential for a laptop at full speed. Buy the output your actual gear needs, because paying for wattage you cannot use just adds weight and cost."},
     ],
   },
   {
     "commentary": "Anker Prime 26K 300W 我還是放第一，因為它是真的能充筆電、而非只幫手機補電的行動電源，這份能力讓它在不同等級。300W 輸出能讓 MacBook Pro 全速充電，26,000mAh 容量蓋得過多個裝置日，做工跟顯示又真的高級。對任何帶筆電出門、受夠找插座的人，這顆就是取代插座的那顆。Anker Prime 27650 250W 守第二，是更高容量的兄弟款，給想要更多續航的人。Anker 737 PowerCore 24K 守第三，是經驗證的主力，多年來掙得名聲。Ugreen Nexode 25000mAh 200W 守第四，是性價比高輸出替代。這週沒事件重排。判斷：能充筆電選 Prime 26K、最大容量選 Prime 27650、性價比高輸出選 Ugreen。把瓦數對準你的裝置，因為 300W 電源充手機是浪費、充筆電卻是必需。買你實際裝備需要的輸出。",
     "highlights": [
       {"title": "Anker Prime 26K 300W 能充筆電", "body": "300W 輸出讓 MacBook Pro 全速充電、26,000mAh 蓋過多個裝置日，做工跟顯示又高級。對受夠找插座的筆電旅人，守住第一。"},
       {"title": "Anker Prime 27650 是容量兄弟款", "body": "它帶來更多續航，給想要單顆最大儲能的人。需要多次完整充電的重度用戶，它是高容量選擇，穩在第二。"},
       {"title": "Anker 737 PowerCore 24K 是經驗證主力", "body": "它多年可靠服務掙得名聲。想要有實績的可靠高輸出電源的買家，它穩坐第三。"},
       {"title": "把瓦數對準你的裝置", "body": "300W 電源充手機是大材小用，全速充筆電卻是必需。買你實際裝備需要的輸出，因為付了用不到的瓦數只是增加重量跟成本。"},
     ],
   })

# ---------------- best-3d-printers ----------------
do("best-3d-printers.json",
   [
     {"title": "Best 3D printer 2026 reviews", "url": "https://all3dp.com/1/best-3d-printer-reviews-top-3d-printers/", "source": "All3DP"},
     {"title": "The Best 3D Printers of 2026", "url": "https://www.tomshardware.com/best-picks/best-3d-printers", "source": "Tom's Hardware"},
   ],
   {
     "commentary": "The Bambu Lab P2S Combo stays at number one because Bambu Lab has done to 3D printing what Apple did to phones: it made the technology just work. The P2S prints fast, prints clean out of the box with almost no tuning, and the AMS multicolor system makes multi-material prints genuinely accessible rather than a fight. For most people, whether a beginner or an experienced maker who values their time, this is the printer that delivers results without the traditional 3D-printing frustration. The Bambu Lab X1-Carbon holds second as the flagship for people who want the absolute best print quality and the full feature set. The Bambu Lab H2D stays third as the large-format option for bigger prints. The Prusa Core One holds fourth as the open-ecosystem alternative for people who want to tinker and own their machine fully. Nothing this week reordered the field. The read: best all-round is the P2S Combo, best quality is the X1-Carbon, best open-source is the Prusa Core One. Bambu won on ease, but Prusa still wins for people who value repairability and an open ecosystem over plug-and-play convenience.",
     "highlights": [
       {"title": "Bambu Lab P2S Combo makes 3D printing just work", "body": "It prints fast and clean out of the box with almost no tuning, and the AMS makes multicolor genuinely accessible. For beginners and time-pressed makers alike, it delivers results without frustration at number one."},
       {"title": "Bambu Lab X1-Carbon is the quality flagship", "body": "The absolute best print quality and the full feature set make it the pick for people who want the ceiling. For makers who prioritize output quality, it holds a firm second."},
       {"title": "Prusa Core One is the open-ecosystem pick", "body": "It is the alternative for people who want to tinker, repair and fully own their machine. For makers who value openness over plug-and-play, it holds a solid fourth on principle and repairability."},
       {"title": "Ease versus openness is the real choice", "body": "Bambu won on plug-and-play convenience; Prusa still wins for repairability and an open ecosystem. Decide whether you want results immediately or a machine you can fully control, and the pick follows."},
     ],
   },
   {
     "commentary": "Bambu Lab P2S Combo 我還是放第一，因為 Bambu Lab 對 3D 列印做的事，就像 Apple 對手機做的：它讓這項技術就這樣能用。P2S 列印快、開箱幾乎不用調就印得乾淨，AMS 多色系統讓多材料列印真的變得親民、而非一場仗。對多數人，無論是新手還是珍惜時間的老手，這台印表機在沒有傳統 3D 列印挫折下交出成果。Bambu Lab X1-Carbon 守第二，是旗艦，給想要絕對最佳列印品質跟完整功能的人。Bambu Lab H2D 守第三，是大尺寸選擇，印更大的東西。Prusa Core One 守第四，是開放生態替代，給想要折騰、完全擁有自己機器的人。這週沒事件重排。判斷：全能選 P2S Combo、品質選 X1-Carbon、開源選 Prusa Core One。Bambu 靠易用贏了，但 Prusa 依然贏得那些重視可維修跟開放生態勝過隨插即用的人。",
     "highlights": [
       {"title": "Bambu Lab P2S Combo 讓 3D 列印就這樣能用", "body": "開箱幾乎不用調就印得又快又乾淨，AMS 讓多色真的親民。對新手跟時間緊的老手，它在第一名沒有挫折地交出成果。"},
       {"title": "Bambu Lab X1-Carbon 是品質旗艦", "body": "絕對最佳的列印品質跟完整功能，讓它是想要天花板的人的選擇。重視成品品質的玩家，它穩在第二。"},
       {"title": "Prusa Core One 是開放生態選擇", "body": "它是給想要折騰、維修、完全擁有自己機器的人的替代。重視開放勝過隨插即用的玩家，它靠原則跟可維修穩坐第四。"},
       {"title": "易用對開放是真正的選擇", "body": "Bambu 靠隨插即用便利贏了；Prusa 依然贏在可維修跟開放生態。決定你要立刻有成果還是一台能完全掌控的機器，選擇就跟著出來。"},
     ],
   })

# ---------------- best-sunscreens ----------------
do("best-sunscreens.json",
   [
     {"title": "Best sunscreen 2026 reviews", "url": "https://www.nytimes.com/wirecutter/reviews/best-sunscreen/", "source": "Wirecutter"},
     {"title": "The Best Sunscreens of 2026, dermatologist-tested", "url": "https://www.allure.com/gallery/best-sunscreens", "source": "Allure"},
   ],
   {
     "commentary": "EltaMD UV Clear SPF 46 stays at number one because it is the sunscreen dermatologists actually recommend most, and the reason is that it solves the problem that makes people skip sunscreen entirely: it feels like nothing. The lightweight finish disappears on the skin, the niacinamide calms redness and helps acne-prone skin, and it layers under makeup without pilling. A sunscreen only works if you wear it daily, and this is the one people genuinely keep using. For most faces, this is the buy. The ISDIN Eryfotona Actinica SPF 50 holds second as the mineral pick with antioxidant repair benefits, the choice for people who want sun protection plus active skin care. The La Roche-Posay Anthelios Melt-In Milk SPF 60 stays third as the best body sunscreen, high protection in a genuinely pleasant lotion. The Supergoop Unseen SPF 50 holds fourth as the invisible primer-like option. Nothing this week reordered the field. The read: best face sunscreen is EltaMD UV Clear, best mineral is ISDIN, best body is La Roche-Posay. The best sunscreen is the one you will actually wear, so prioritize feel.",
     "highlights": [
       {"title": "EltaMD UV Clear feels like nothing", "body": "Its lightweight finish disappears, the niacinamide calms redness and acne-prone skin, and it layers under makeup. A sunscreen only works if you wear it daily, and this is the one people keep using, holding number one."},
       {"title": "ISDIN Eryfotona Actinica is the mineral pick", "body": "Antioxidant repair benefits plus mineral protection make it the choice for people who want sun defense and active skin care in one. That dual benefit keeps it a firm second."},
       {"title": "La Roche-Posay Anthelios is best for the body", "body": "High protection in a genuinely pleasant melt-in lotion makes it the one people actually reapply on arms and legs. For body coverage, that wearability holds it a solid third."},
       {"title": "The best sunscreen is the one you wear", "body": "Protection on the bottle means nothing if the texture makes you skip it. Prioritize feel and finish over the highest SPF number, because daily wear beats a heavy formula that lives in the drawer."},
     ],
   },
   {
     "commentary": "EltaMD UV Clear SPF 46 我還是放第一，因為它是皮膚科醫師實際上最常推薦的防曬，理由是它解決了讓人乾脆不擦防曬的問題：它擦起來像沒擦。輕盈的膚感在皮膚上消失，菸鹼醯胺安撫泛紅、幫助容易長痘的膚質，上妝前打底也不會搓泥。防曬只有你每天擦才有用，而這支是大家真的會一直用下去的。對多數的臉，就是它。ISDIN Eryfotona Actinica SPF 50 守第二，是物理防曬選擇，有抗氧化修護加成，給想要防曬加保養的人。La Roche-Posay Anthelios Melt-In Milk SPF 60 守第三，是最佳身體防曬，高防護又是真的舒服的乳液。Supergoop Unseen SPF 50 守第四，是隱形妝前乳般的選擇。這週沒事件重排。判斷：臉部選 EltaMD UV Clear、物理選 ISDIN、身體選 La Roche-Posay。最好的防曬是你真的會擦的那支，把膚感擺優先。",
     "highlights": [
       {"title": "EltaMD UV Clear 擦起來像沒擦", "body": "輕盈膚感會消失，菸鹼醯胺安撫泛紅跟痘痘肌，上妝前打底也行。防曬只有每天擦才有用，這支是大家會一直用下去的，守住第一。"},
       {"title": "ISDIN Eryfotona Actinica 是物理選擇", "body": "抗氧化修護加成加物理防護，讓它是想要防曬跟保養一次到位的人的選擇。這份雙重好處讓它穩在第二。"},
       {"title": "La Roche-Posay Anthelios 身體最佳", "body": "高防護又是真的舒服的融入式乳液，讓它是大家真的會在手臂腿上補擦的那支。論身體覆蓋，這份好擦性讓它穩坐第三。"},
       {"title": "最好的防曬是你會擦的那支", "body": "瓶上的防護數字，質地讓你不擦就毫無意義。把膚感跟膚色表現擺在最高 SPF 數字之前，因為每天擦勝過躺在抽屜裡的厚重配方。"},
     ],
   })

print("batchI done")
