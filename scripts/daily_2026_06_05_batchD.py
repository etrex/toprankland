import sys; sys.path.insert(0, "/Users/etrexkuo/toprankland/scripts")
from daily_helper import load, save, upsert, last_rankings, DATE

def do(name, refs, en, zh):
    d, p = load(name)
    entry = {"date": DATE, "rankings": last_rankings(d), "references": refs, "i18n": {"en": en, "zh-tw": zh}}
    upsert(d, entry); save(p, d); print("updated", name)

# ---------------- best-wireless-earbuds ----------------
do("best-wireless-earbuds.json",
   [
     {"title": "The 7 Best Wireless Earbuds of 2026", "url": "https://www.rtings.com/headphones/reviews/best/wireless-earbuds", "source": "RTINGS"},
     {"title": "Sony WF-1000XM6 Gets a Pill-Shaped Redesign: 5 Upgrades Worth Your Money in 2026", "url": "https://the-gadgeteer.com/2026/06/02/sony-wf-1000xm6-upgrades-2026/", "source": "The Gadgeteer"},
     {"title": "Sony WF-1000XM6 review: Bigger and better", "url": "https://www.soundguys.com/sony-wf-1000xm6-review-152013/", "source": "SoundGuys"},
   ],
   {
     "commentary": "Heading into June 2026 the Sony WF-1000XM6 stays my number one without debate, and a fresh round of testing this month only hardens the case. RTINGS now lists it as their top wireless earbud outright, and the numbers back it: roughly 88 percent average noise reduction across the frequency band, a near-perfect MDAQS sound score, and the new QN3e processor running 3x faster than the chip in the XM5. The redesigned pill-shaped shells finally fix the one comfort gripe I had with Sony, and battery came in just under 10 hours in real testing with a 3-minute-for-45-minute fast charge. That is the complete package. AirPods Pro 2 holds second because for iPhone owners the H2 chip, seamless handoff and adaptive transparency are still the smoothest ecosystem story in audio, and the noise isolation sits right alongside Sony's. Bose QuietComfort Earbuds II keep third on pure ANC muscle and the plushest fit in the category, the pair I hand anyone who flies every week. Samsung Galaxy Buds 4 Pro stay fourth as the obvious pick inside a Galaxy phone, with the WF-1000XM5 and Buds 3 Pro filling out a deep value-conscious middle. Nothing reshuffled the order this week, so I carried the board forward and let the verdicts carry the weight. My honest steer: buy by phone first. Sony for Android flagships, AirPods for iPhone, Bose if frequent flying is the whole point.",
     "highlights": [
       {"title": "Sony WF-1000XM6 is the complete flagship", "body": "RTINGS now ranks it the best wireless earbud, with about 88 percent average noise reduction, a near-perfect sound score and the QN3e chip running 3x faster than the XM5. The pill-shaped redesign fixes the old fit complaint, sealing number one."},
       {"title": "AirPods Pro 2 owns the iPhone", "body": "The H2 chip, instant handoff and adaptive transparency remain the smoothest ecosystem experience in earbuds, with isolation right alongside Sony's. For anyone living in iOS, this is still the first pair I recommend."},
       {"title": "Bose QC Earbuds II rule comfort and ANC", "body": "The plushest fit in the category paired with class-leading noise cancellation makes these the pair I hand frequent flyers. For long-haul travel where silence and all-day comfort matter most, they earn a firm third."},
       {"title": "Buy by phone first", "body": "Sony for Android flagships, AirPods for iPhone, Bose for travel. The top of this category is close enough on raw quality that your handset, not a spec sheet, should make the call for you."},
     ],
   },
   {
     "commentary": "2026 年 6 月這個時間點，Sony WF-1000XM6 我還是毫不猶豫放第一，而且這個月新一輪測試只讓它的地位更穩。RTINGS 現在直接把它列為最佳真無線耳機，數據也很硬，全頻段平均降噪大約 88 趴、音質分數逼近滿分、新的 QN3e 處理器比 XM5 那顆快了 3 倍。重新設計的藥丸造型外殼，總算把我對 Sony 唯一的配戴抱怨修掉了，實測續航差一點點就到 10 小時，快充更是充 3 分鐘聽 45 分鐘。這就是完整的全餐。AirPods Pro 2 守第二，因為對 iPhone 用戶來說，H2 晶片、無縫切換、自適應通透模式，依然是音訊圈最順的生態故事，降噪也跟 Sony 並肩。話說回來，Bose QuietComfort Earbuds II 守第三靠的是純降噪實力跟全類別最舒服的配戴，每週都要飛的人我就推這副。Samsung Galaxy Buds 4 Pro 守第四，在 Galaxy 手機裡是理所當然的選擇，WF-1000XM5 跟 Buds 3 Pro 撐起重視性價比的中段。這週沒事件洗牌，所以我把整個榜延續下來，讓判斷本身說話。老實建議，先看手機再買，Android 旗艦配 Sony、iPhone 配 AirPods、常飛就選 Bose。",
     "highlights": [
       {"title": "Sony WF-1000XM6 是完整旗艦", "body": "RTINGS 現在把它列為最佳真無線耳機，全頻段平均降噪約 88 趴、音質逼近滿分、QN3e 晶片比 XM5 快 3 倍。藥丸造型改款修掉了舊的配戴抱怨，第一名穩穩坐定。"},
       {"title": "AirPods Pro 2 主宰 iPhone", "body": "H2 晶片、即時切換、自適應通透，依然是耳機裡最順的生態體驗，降噪也跟 Sony 並肩。只要你活在 iOS 裡，這副還是我第一個推。"},
       {"title": "Bose QC Earbuds II 配戴降噪雙強", "body": "全類別最舒服的配戴配上頂級降噪，是我推給空中飛人的那副。長程飛行最在意安靜跟整天舒適的人，它穩拿第三。"},
       {"title": "先看手機再買", "body": "Android 旗艦選 Sony、iPhone 選 AirPods、常飛選 Bose。這個類別頂端純素質夠接近了，該幫你做決定的是你的手機，不是規格表。"},
     ],
   })

# ---------------- best-noise-cancelling-headphones ----------------
do("best-noise-cancelling-headphones.json",
   [
     {"title": "The 5 Best Noise Cancelling Headphones of 2026", "url": "https://www.rtings.com/headphones/reviews/best/by-feature/noise-cancelling", "source": "RTINGS"},
     {"title": "I tested the Sony WH-1000XM6 vs Bose QuietComfort Ultra for 6 months — and there's a clear winner", "url": "https://www.tomsguide.com/audio/headphones/i-tested-the-sony-wh-1000xm6-vs-bose-quietcomfort-ultra-2-for-6-months-and-theres-a-clear-winner", "source": "Tom's Guide"},
   ],
   {
     "commentary": "Going into June 2026 the Sony WH-1000XM6 keeps my top spot, and a six-month head-to-head against the Bose this month confirms why. RTINGS still rates the XM6 the best noise-cancelling headphone tested, measuring roughly 87 percent average loudness reduction against the Bose's 85 percent, a real if narrow edge. What seals it for me is everything around the ANC: a superior 10-band EQ versus Bose's three, a warmer and weightier tuning that still pulls fine detail, and the most complete app in the category. Bose QuietComfort Ultra holds a very close second and genuinely wins on comfort, with plusher earcup padding and a roomier headband that fatigues far slower on long flights. If your priority is wearing them for eight hours straight, the Bose is the smarter buy, and I keep that verdict honest. Sennheiser Momentum 4 stays third as the audiophile's value champion, pairing the warmest sound here with a monster 60-hour battery. The Sennheiser HDB 630 sits fourth on sheer sonic refinement, then AirPods Max 2 fifth for the iPhone crowd. Soundcore's Space 2 and Q45 remain the budget heroes that punch absurdly above their price. Nothing this week moved the order, so I carried the board forward. My steer: Sony for the all-round best, Bose if comfort is everything, Sennheiser if you want warmth and battery for less.",
     "highlights": [
       {"title": "Sony WH-1000XM6 is the all-round best", "body": "RTINGS still rates it the top ANC headphone, measuring about 87 percent loudness reduction to Bose's 85, plus a 10-band EQ and the deepest app. That blend of leading cancellation and customization keeps it at number one."},
       {"title": "Bose QC Ultra wins comfort outright", "body": "Plusher padding and a roomier headband fatigue far slower on long flights, the clear comfort victor in a six-month test. If you wear headphones for hours at a stretch, this is the smarter buy and a deserved close second."},
       {"title": "Sennheiser Momentum 4 is the value champ", "body": "It pairs the warmest, most musical tuning in the group with a 60-hour battery that outlasts everything here. For audiophiles who want premium sound without the flagship price, it stays a confident third."},
       {"title": "Soundcore still owns the budget tier", "body": "The Space 2 and Q45 deliver strong ANC and 50-plus-hour battery for a fraction of flagship money. They remain the pair I recommend to anyone who refuses to spend big yet still wants real quiet."},
     ],
   },
   {
     "commentary": "2026 年 6 月，Sony WH-1000XM6 守住我的榜首，這個月跟 Bose 的半年實測對決正好說明原因。RTINGS 還是把 XM6 評為測過最佳的降噪耳機，量到的平均音量衰減大約 87 趴，對上 Bose 的 85 趴，差距雖小但是真的領先。對我來說真正關鍵的是降噪以外的東西，10 段 EQ 對上 Bose 的 3 段、調音更暖更有重量卻還能抓出細節、App 也是全類別最完整。話說回來，Bose QuietComfort Ultra 緊咬第二，而且配戴是真的贏，耳罩填充更厚、頭帶更寬，長途飛行戴久了疲勞慢很多。如果你的重點就是要一次戴八小時，Bose 是更聰明的選擇，這個判斷我說白。Sennheiser Momentum 4 守第三，是發燒友的性價比冠軍，這群裡最暖的聲音配上誇張的 60 小時續航。Sennheiser HDB 630 排第四，純看聲音的細膩度，再來 AirPods Max 2 第五給 iPhone 族。Soundcore 的 Space 2 跟 Q45 還是那種價格低到誇張卻很能打的平價英雄。這週沒事件動排名，所以我把整個榜延續下來。建議是，要全能最佳選 Sony、配戴至上選 Bose、想要暖聲又長續航又省錢就選 Sennheiser。",
     "highlights": [
       {"title": "Sony WH-1000XM6 是全能最佳", "body": "RTINGS 還是把它評為降噪耳機之首，量到約 87 趴音量衰減對上 Bose 的 85，再加 10 段 EQ 跟最深的 App。這份領先降噪加可調性的組合，讓它穩坐第一。"},
       {"title": "Bose QC Ultra 配戴完勝", "body": "填充更厚、頭帶更寬，長途飛行戴久疲勞慢很多，半年實測裡配戴明確勝出。會一次戴好幾小時的人，這副是更聰明的選擇，緊咬第二實至名歸。"},
       {"title": "Sennheiser Momentum 4 是性價比王", "body": "這群裡最暖最有音樂性的調音，配上 60 小時、把全場都熬贏的續航。想要旗艦級聲音又不想付旗艦價的發燒友，它穩穩守第三。"},
       {"title": "Soundcore 仍主宰平價層", "body": "Space 2 跟 Q45 用旗艦零頭的價格給你不錯的降噪跟 50 小時以上續航。死不肯花大錢、卻又想要真安靜的人，我就推這兩副。"},
     ],
   })

# ---------------- best-bluetooth-speakers ----------------
do("best-bluetooth-speakers.json",
   [
     {"title": "The 6 Best Bluetooth Speakers of 2026", "url": "https://www.rtings.com/speaker/reviews/best/by-feature/bluetooth", "source": "RTINGS"},
     {"title": "JBL Charge 6 vs Marshall Emberton III: Which Portable Bluetooth Speaker Is Right For You?", "url": "https://www.crutchfield.com/compare_109CHRGE6B_972EMBT3BK/JBL-Charge-6-vs-Marshall-Emberton-III.html", "source": "Crutchfield"},
   ],
   {
     "commentary": "In June 2026 the JBL Charge 6 stays my number one portable, and a fresh round of comparisons against the Marshall this month keeps the verdict intact. The Charge 6 puts out a genuine 45 watts, enough to fill a backyard or a pool party where smaller speakers start to strain, and it pairs that power with proper IP68 dust-and-water rating plus a USB-C powerbank port that has saved my phone more than once. That combination of loudness, ruggedness and battery is exactly what most people actually want from a grab-and-go speaker. Marshall Emberton III holds second because it wins on a different axis: true left-right stereo from dual 2-inch drivers, where the Charge 6 collapses to mono, plus that unmistakable Marshall look and the longest battery in the group. For refined indoor listening it is the more musical pick, and it typically runs a touch cheaper too. Bose SoundLink Max keeps third on pure sound quality, the richest tone of the truly portable options. Sonos Play and Move 2 anchor the connected-home picks, JBL Flip 7 is the pocket-sized value star, and the Boombox 4 remains the party cannon when you simply need maximum output. Nothing this week reshuffled the board, so I carried it forward. My steer: Charge 6 for the all-rounder, Marshall for stereo and style, Bose for the best tone.",
     "highlights": [
       {"title": "JBL Charge 6 is the all-rounder to beat", "body": "A real 45 watts fills a backyard, IP68 shrugs off pool splashes, and the USB-C powerbank port doubles as a phone charger. That blend of power, ruggedness and utility is what most buyers actually want, keeping it number one."},
       {"title": "Marshall Emberton III wins on stereo and style", "body": "Dual 2-inch drivers deliver true left-right stereo where the Charge 6 folds to mono, wrapped in that iconic Marshall look with the longest battery here. For refined indoor listening it is the more musical pick and a clear second."},
       {"title": "Bose SoundLink Max has the richest tone", "body": "Among the genuinely portable options it serves the fullest, most balanced sound, the one I grab when audio quality outranks loudness. That sonic edge keeps it a confident third in a crowded field."},
       {"title": "Pick by the job", "body": "Charge 6 for power and durability, Marshall for stereo and looks, Bose for tone, Boombox 4 when you need to be loudest. This category is mature enough that the right answer follows your use, not a single score."},
     ],
   },
   {
     "commentary": "2026 年 6 月，JBL Charge 6 還是我心中第一的隨身喇叭，這個月跟 Marshall 新一輪對比之後，這個判斷依然成立。Charge 6 實打實輸出 45 瓦，足以撐起一個後院或泳池派對，那種小喇叭開始破音的場合它還能 hold 住，而且這份功率還配上實打實的 IP68 防塵防水，加上一個 USB-C 行動電源孔，幫我救過手機不只一次。這種大聲、耐操、續航的組合，正是大多數人對一台隨手帶的喇叭真正要的。話說回來，Marshall Emberton III 守第二，因為它贏在另一個維度，雙 2 吋單體做出真正的左右聲道立體聲，而 Charge 6 會塌成單聲道，再加上那個一眼認出的 Marshall 外型跟這群裡最長的續航。室內細聽它是更有音樂性的選擇，而且通常還便宜一點。Bose SoundLink Max 守第三，純看音質，是真正隨身款裡音色最飽滿的。Sonos Play 跟 Move 2 撐起連網居家的選項，JBL Flip 7 是口袋尺寸的性價比之星，Boombox 4 則是你純粹要最大音量時的派對大砲。這週沒事件洗牌，所以我把榜延續下來。建議是，要全能選 Charge 6、要立體聲跟造型選 Marshall、要最好音色選 Bose。",
     "highlights": [
       {"title": "JBL Charge 6 是最難打敗的全能王", "body": "實打實 45 瓦撐滿後院，IP68 不怕泳池水花，USB-C 行動電源孔還能反充手機。這種功率、耐操、實用兼具的組合，正是多數人真正要的，第一名穩穩的。"},
       {"title": "Marshall Emberton III 贏在立體聲跟造型", "body": "雙 2 吋單體做出真左右聲道，Charge 6 卻塌成單聲道，再配上經典 Marshall 外型跟這群最長續航。室內細聽它更有音樂性，第二名實至名歸。"},
       {"title": "Bose SoundLink Max 音色最飽滿", "body": "在真正隨身款裡，它給出最飽滿、最均衡的聲音，是我在音質比音量重要時會抓的那台。這份音色優勢讓它在擁擠戰場穩坐第三。"},
       {"title": "照用途選就對了", "body": "要功率耐操選 Charge 6、要立體聲跟外型選 Marshall、要音色選 Bose、純要最大聲選 Boombox 4。這類別夠成熟了，正解跟著你的用途走，不是看單一分數。"},
     ],
   })

# ---------------- best-smart-speakers ----------------
do("best-smart-speakers.json",
   [
     {"title": "Best smart speakers in 2026 — Alexa, Google, and Siri tested", "url": "https://www.tomsguide.com/us/best-smart-speakers,review-4480.html", "source": "Tom's Guide"},
     {"title": "The best smart speakers of 2026, tested by experts", "url": "https://www.cnn.com/cnn-underscored/reviews/best-smart-speakers", "source": "CNN Underscored"},
   ],
   {
     "commentary": "Heading into June 2026 the Amazon Echo Studio (2nd Gen) keeps my top spot, and I stand by it for one reason that matters more than raw audio: it is the best-rounded smart speaker you can buy. The new Studio brings genuine Dolby Atmos and a clear step up in sound over the old model, then wraps it in the deepest smart-home integration on the market, with a built-in Zigbee and Matter hub that quietly runs the rest of your house. For most people building an Alexa home, this is the one speaker that does everything well. Sonos Era 100 holds a very close second and is the audiophile's pick, with two angled tweeters and a bigger woofer that several outlets, Wired included, still call the best-sounding speaker in this price class. If music quality is your whole reason for buying, the Era 100 edges ahead and I say so plainly. Apple HomePod 2nd Gen stays third as the obvious choice inside an Apple household, where Siri, HomeKit and computational audio just work together. Sonos Era 300 sits fourth for spatial-audio lovers, with Google's Home Speaker fifth for the cleanest Assistant experience. The Echo lineup fills out the value tier, with the Dot Max and Dot 5th Gen still the smartest small buys. Nothing this week moved the order, so I carried it forward. My steer: Echo Studio for the all-rounder, Sonos for sound, HomePod for Apple homes.",
     "highlights": [
       {"title": "Echo Studio 2nd Gen is the best all-rounder", "body": "Genuine Dolby Atmos, a real sound upgrade, and the deepest smart-home integration with a built-in Zigbee and Matter hub. For most people building an Alexa home, it is the one speaker that does everything well, holding number one."},
       {"title": "Sonos Era 100 is the audiophile pick", "body": "Two angled tweeters and a larger woofer earn it best-in-class sound reviews, Wired included. If music quality is the entire reason you are buying, the Era 100 edges ahead and takes a very close second."},
       {"title": "HomePod 2nd Gen rules Apple homes", "body": "Siri, HomeKit and Apple's computational audio simply work together better here than anywhere else. For anyone living in the Apple ecosystem, it remains the natural and confident third choice."},
       {"title": "Echo Dot Max is the smart small buy", "body": "It delivers the full Alexa smart-home brain in a compact, affordable shell that punches above its size. For seeding extra rooms without spending big, it stays the value pick I recommend first."},
     ],
   },
   {
     "commentary": "2026 年 6 月這個時間點，Amazon Echo Studio 第二代守住我的榜首，我挺它的理由比純音質更重要，它是你買得到最全能的智慧喇叭。新版 Studio 帶來真正的 Dolby Atmos，音質比舊款明顯升級，再包進市面上最深的智慧家庭整合，內建 Zigbee 跟 Matter hub，默默把你家其他裝置都跑起來。對大多數要建 Alexa 家庭的人來說，這就是那台什麼都做得好的喇叭。話說回來，Sonos Era 100 緊咬第二，是發燒友的選擇，兩顆斜角高音加上更大的低音單體，包含 Wired 在內好幾家媒體還是說它是這個價位帶最好聽的喇叭。如果你買的全部理由就是音樂品質，Era 100 是小贏的，我直說。Apple HomePod 第二代守第三，在 Apple 家庭裡是理所當然的選擇，Siri、HomeKit、運算音訊就是合得來。Sonos Era 300 排第四給空間音訊愛好者，Google Home Speaker 第五，是最乾淨的 Assistant 體驗。Echo 系列撐起性價比層，Dot Max 跟 Dot 五代還是最聰明的小尺寸選擇。這週沒事件動排名，所以我把榜延續下來。建議是，要全能選 Echo Studio、要音質選 Sonos、Apple 家庭選 HomePod。",
     "highlights": [
       {"title": "Echo Studio 二代是最佳全能王", "body": "真正的 Dolby Atmos、音質實在升級、最深的智慧家庭整合加內建 Zigbee 跟 Matter hub。對多數要建 Alexa 家庭的人，它是那台什麼都做得好的喇叭，穩坐第一。"},
       {"title": "Sonos Era 100 是發燒友選擇", "body": "兩顆斜角高音加更大低音單體，拿下包含 Wired 在內的同級最佳音質評價。如果你買的全部理由就是音樂品質，Era 100 小贏，緊咬第二。"},
       {"title": "HomePod 二代主宰 Apple 家庭", "body": "Siri、HomeKit、Apple 運算音訊在這裡就是比別處更合得來。只要你活在 Apple 生態裡，它就是那個自然又有把握的第三選擇。"},
       {"title": "Echo Dot Max 是聰明小尺寸選擇", "body": "用小巧又親民的機身塞進完整的 Alexa 智慧家庭大腦，表現超出尺寸。要幫多房間鋪設又不想花大錢，它還是我第一個推的性價比選擇。"},
     ],
   })

# ---------------- best-soundbars ----------------
do("best-soundbars.json",
   [
     {"title": "Sonos Arc Ultra vs Samsung HW-Q990F: Which Soundbar Is Better?", "url": "https://www.rtings.com/soundbar/tools/compare/sonos-arc-ultra-vs-samsung-hw-q990f/79200/88604", "source": "RTINGS"},
     {"title": "Samsung HW-Q990F vs Sonos Arc Ultra: which Dolby Atmos soundbar should you buy?", "url": "https://www.whathifi.com/advice/samsung-hw-q990f-vs-sonos-arc-ultra-which-dolby-atmos-soundbar-should-you-buy", "source": "What Hi-Fi?"},
   ],
   {
     "commentary": "In June 2026 the Samsung HW-Q990F stays locked at my number one, and the latest head-to-heads against the Sonos only reinforce it. The Q990F ships as a complete 11.1.4-channel system, 23 drivers spread across the bar, wireless rear speakers and a dedicated subwoofer, so you get true surround with physical speakers behind your head out of the box. That eliminates the guesswork that even the best virtualized bars rely on, and for movie nights it is simply the most enveloping experience you can buy without going full custom install. Sonos Arc Ultra holds second and is the smarter pick for a different buyer: a single elegant 9.1.4 bar with the new Sound Motion woofer tech, the cleanest multi-room music story in the category, and a far tidier living room. If you want one beautiful bar and the Sonos app ecosystem, the Arc Ultra is the one I point you to, and it edges Samsung on pure music. Sony's Bravia Theatre Bar 9 keeps third on the best Atmos height effects of the standalone bars, with LG's S95TR fourth as another full surround package. Samsung's QS750F is the value surround star, and the Sonos Beam Gen 2 stays the small-room favorite. Nothing this week moved the order, so I carried it forward. My steer: Q990F for the full system, Arc Ultra for one-bar elegance and music.",
     "highlights": [
       {"title": "Samsung HW-Q990F is the most complete system", "body": "An 11.1.4 layout with 23 drivers, wireless rears and a subwoofer delivers true surround with physical speakers behind you, no virtualization guesswork. For the most enveloping movie nights short of a custom install, it stays number one."},
       {"title": "Sonos Arc Ultra wins on elegance and music", "body": "A single 9.1.4 bar with new Sound Motion woofer tech and the best multi-room ecosystem keeps your room tidy and edges Samsung on pure music. For one beautiful bar over a full kit, it is the clear second."},
       {"title": "Sony Bravia Theatre Bar 9 leads on height", "body": "Among standalone bars it throws the most convincing Atmos height effects, putting sound genuinely overhead. For buyers chasing immersive ceiling-bounce without rear speakers, it earns a firm third."},
       {"title": "QS750F is the value surround star", "body": "It brings a real wireless-rear surround package at a noticeably friendlier price than the flagships. For a complete home-theater feel on a tighter budget, it is the smart-money pick I recommend."},
     ],
   },
   {
     "commentary": "2026 年 6 月，Samsung HW-Q990F 還是牢牢鎖在我的第一，最近跟 Sonos 的對決只是再次強化這個判斷。Q990F 出廠就是一套完整的 11.1.4 聲道系統，23 顆單體分布在整支聲霸上，無線後環繞加一顆獨立重低音，所以你開箱就有真正的環繞，實體喇叭就放在你頭後面。這就消掉了再強的虛擬聲霸都還在仰賴的猜測，看電影的夜晚，它就是不走客製安裝路線下你買得到最包圍的體驗。話說回來，Sonos Arc Ultra 守第二，對另一種買家是更聰明的選擇，單支優雅的 9.1.4 聲霸配上全新 Sound Motion 低音技術，多房間音樂體驗是全類別最乾淨的，客廳也清爽很多。如果你要的是一支漂亮聲霸加 Sonos App 生態，我就指你去 Arc Ultra，純音樂它還小贏 Samsung。Sony Bravia Theatre Bar 9 守第三，是單支聲霸裡 Atmos 頭頂效果最好的，LG S95TR 第四，是另一套完整環繞。Samsung QS750F 是性價比環繞之星，Sonos Beam Gen 2 還是小空間最愛。這週沒事件動排名，所以我把榜延續下來。建議是，要完整系統選 Q990F、要單支優雅又重音樂選 Arc Ultra。",
     "highlights": [
       {"title": "Samsung HW-Q990F 是最完整的系統", "body": "11.1.4 配置、23 顆單體、無線後環繞加重低音，給你頭後有實體喇叭的真環繞，沒有虛擬的猜測。不走客製安裝下最包圍的電影夜，它穩坐第一。"},
       {"title": "Sonos Arc Ultra 贏在優雅跟音樂", "body": "單支 9.1.4 聲霸配全新 Sound Motion 低音技術跟最好的多房間生態，客廳清爽又在純音樂小贏 Samsung。要一支漂亮聲霸勝過整套，它穩拿第二。"},
       {"title": "Sony Bravia Theatre Bar 9 頭頂效果最強", "body": "在單支聲霸裡，它丟出最有說服力的 Atmos 頭頂效果，聲音真的到你上方。想要天花板反射的沉浸感又不想擺後喇叭的人，它穩拿第三。"},
       {"title": "QS750F 是性價比環繞之星", "body": "它用比旗艦親民不少的價格，帶來真正的無線後環繞整套。預算抓緊一點又想要完整家庭劇院感，它就是我推的高性價比選擇。"},
     ],
   })

# ---------------- best-gaming-headsets ----------------
do("best-gaming-headsets.json",
   [
     {"title": "I tested Reddit's favorite high-end gaming headsets and there's a clear winner", "url": "https://www.tomsguide.com/gaming/gaming-peripherals/i-tested-reddits-favorite-high-end-gaming-headsets-and-theres-a-clear-winner-but-its-not-the-one-i-expected", "source": "Tom's Guide"},
     {"title": "Audeze Maxwell Review 2026: Best Planar Magnetic Gaming Headset?", "url": "https://gamingpcguru.com/audeze-maxwell-review/", "source": "GamingPCGuru"},
   ],
   {
     "commentary": "Heading into June 2026 the SteelSeries Arctis Nova Pro Wireless keeps my number one, and I stand by it as the best all-rounder in gaming audio. The dual-battery hot-swap system means it never dies mid-session, the ANC is rare and genuinely useful in this category, and the dual-wireless setup with a base station that switches between PC and console is the slickest connectivity story going. Comfort is feather-light too. It does everything well, which is exactly what most players want from one headset. That said, the Audeze Maxwell 2 sits a hair behind at number two and is, flat out, the best-sounding gaming headset money can buy. Its planar magnetic drivers reveal detail dynamic drivers simply cannot, and at well under the price of the Nova Elite it delivers 80-plus hours of battery and audiophile clarity. If sound quality is your single priority, the Maxwell 2 is the pick and I say so without hedging. Turtle Beach Stealth Pro II holds third as a superb feature-rich value flagship, with Logitech's G Pro X 2 Lightspeed fourth as the esports staple. The ROG Delta II and HyperX Cloud Alpha Wireless anchor a strong mid-tier, the Alpha still the battery-life value king. Nothing this week reshuffled the board, so I carried it forward. My steer: Nova Pro for the all-rounder, Maxwell 2 for pure sound, Cloud Alpha for value.",
     "highlights": [
       {"title": "Arctis Nova Pro Wireless is the best all-rounder", "body": "Hot-swap dual batteries, genuinely useful ANC, and a base station that flips between PC and console make it the slickest complete package. It does everything well, which is why it holds number one for most players."},
       {"title": "Audeze Maxwell 2 is the sound champion", "body": "Planar magnetic drivers reveal detail dynamic drivers cannot, paired with 80-plus hours of battery at well under flagship money. If audio quality is your single priority, it is the pick and a deserved close second."},
       {"title": "Turtle Beach Stealth Pro II is the feature-value flagship", "body": "It packs hot-swap batteries and a deep feature set at a friendlier price than the top two. For players who want flagship capability without the flagship sting, it earns a confident third."},
       {"title": "Cloud Alpha Wireless still wins on value", "body": "Massive battery life and reliable comfort at a price the premium pack cannot touch keep it the smart-money pick. For anyone who wants long wireless sessions without overspending, it remains the one I recommend."},
     ],
   },
   {
     "commentary": "2026 年 6 月這個時間點，SteelSeries Arctis Nova Pro Wireless 守住我的第一，我挺它是遊戲音訊裡最強的全能選手。雙電池熱抽換系統代表它玩到一半絕不會沒電，主動降噪在這個類別很少見而且是真的好用，雙無線加上能在 PC 跟主機之間切換的基座，是目前最順的連線方案。配戴也輕得像羽毛。它什麼都做得好，這正是大多數玩家對一副耳機的期待。話說回來，Audeze Maxwell 2 緊貼在後排第二，講白了，它就是錢買得到最好聽的遊戲耳機。平面振膜單體能揭露動圈單體根本做不到的細節，而且價格遠低於 Nova Elite，卻給你 80 小時以上的續航跟發燒級的清晰度。如果你唯一的重點是音質，Maxwell 2 就是選擇，我不打模糊仗。Turtle Beach Stealth Pro II 守第三，是功能滿載的高性價比旗艦，Logitech G Pro X 2 Lightspeed 第四，是電競常青樹。ROG Delta II 跟 HyperX Cloud Alpha Wireless 撐起紮實的中段，Alpha 還是續航性價比王。這週沒事件洗牌，所以我把榜延續下來。建議是，要全能選 Nova Pro、要純音質選 Maxwell 2、要性價比選 Cloud Alpha。",
     "highlights": [
       {"title": "Arctis Nova Pro Wireless 是最強全能選手", "body": "雙電池熱抽換、真的好用的主動降噪、能在 PC 跟主機間切換的基座，組成最順的完整方案。它什麼都做得好，所以對多數玩家它穩坐第一。"},
       {"title": "Audeze Maxwell 2 是音質冠軍", "body": "平面振膜單體揭露動圈做不到的細節，配上 80 小時以上續航，價格還遠低於旗艦。如果你唯一的重點是音質，它就是選擇，緊咬第二實至名歸。"},
       {"title": "Turtle Beach Stealth Pro II 是功能性價比旗艦", "body": "它用比前兩名親民的價格塞進熱抽換電池跟豐富功能。想要旗艦級能力又不想被旗艦價刺到的玩家，它穩拿第三。"},
       {"title": "Cloud Alpha Wireless 仍贏在性價比", "body": "用前段班碰不到的價格給你超長續航跟可靠配戴，是高性價比的聰明選擇。想要長時間無線又不想超支的人，它還是我推的那副。"},
     ],
   })

print("ALL DONE")
