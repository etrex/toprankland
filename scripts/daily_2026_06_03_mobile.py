import sys
sys.path.insert(0, "/Users/etrexkuo/toprankland/scripts")
from daily_helper import load, save, upsert, last_rankings
DATE = "2026-06-03"

def do(fname, references, en_comm, en_hl, zh_comm, zh_hl):
    d, p = load(fname)
    entry = {"date": DATE, "rankings": last_rankings(d), "references": references,
             "i18n": {"en": {"commentary": en_comm, "highlights": en_hl},
                      "zh-tw": {"commentary": zh_comm, "highlights": zh_hl}}}
    upsert(d, entry); save(p, d); print("OK", fname)


# ---------------- Foldable smartphones ----------------
do("best-foldable-smartphones.json",
   [
     {"title": "Best foldable phones of 2026", "url": "https://www.tomsguide.com/best-picks/best-foldable-phones", "source": "Tom's Guide"},
     {"title": "The best foldable phones of 2026: All the top Flips and Folds", "url": "https://www.androidauthority.com/the-best-foldable-phones-3550058/", "source": "Android Authority"},
     {"title": "Samsung Galaxy Z Fold 7 review", "url": "https://www.whathifi.com/smartphones-tablets/samsung-galaxy-z-fold-7", "source": "What Hi-Fi?"}
   ],
   "The Galaxy Z Fold 7 stays my top book style foldable, and after another week of reading I am more convinced. At 4.2mm unfolded it is the thinnest, lightest Fold yet, and that single fact changes how the phone feels in a pocket and in the hand. You get the 8 inch OLED inner panel, the 200MP main camera lifted straight from the S25 Ultra, Snapdragon 8 Elite for Galaxy, and a hinge that finally makes the crease easy to forget. This is the foldable I would hand someone who wants the format without compromise. The Pixel 10 Pro Fold sits right behind it and earns the position with its IP68 rating, the first on a book style foldable, which means you stop babying it around water. Google's Tensor tuning and the clean camera processing make it the pick for anyone living inside Google's apps. The Motorola Razr Fold is the wildcard this month and reviewers keep praising it, which is why it holds a strong score in my list even at rank eleven, it is a genuinely fun take on the format. Oppo Find N5 and Honor Magic V3 round out the serious imports, both thin, both polished, both worth importing if you can. On the flip side, the Galaxy Z Flip 7 remains the clamshell to beat for its cover screen and battery, while the Razr Ultra 2026 counters with personality. Samsung's Galaxy Z TriFold launched early this year and sold out at 2,500 dollars, proof the appetite for ambitious folding hardware is real. Nothing in the past week moves me to reshuffle the order, the leaders are simply executing well.",
   [
     {"title": "Galaxy Z Fold 7 is the no-compromise pick", "body": "At 4.2mm unfolded it is the thinnest and lightest Fold ever, paired with an 8 inch OLED, the 200MP S25 Ultra sensor, and Snapdragon 8 Elite for Galaxy. The refined hinge makes the crease easy to ignore, and the result is a foldable that feels like a normal phone closed and a tablet open."},
     {"title": "Pixel 10 Pro Fold owns water resistance", "body": "Its IP68 rating is a first among book style foldables, so it survives rain and spills that used to scare foldable owners. Combine that durability with Google's clean camera processing and deep app integration and it is the obvious choice for anyone living in Gmail, Photos, and Maps."},
     {"title": "Motorola Razr Fold is the surprise of the season", "body": "Reviewers keep calling it one of the most fun foldables to use this year, which is why it carries a high score despite its rank. It proves Motorola can play in the book style arena, not just the clamshell one, and it is worth a look for buyers who want something different."}
   ],
   "Galaxy Z Fold 7 還是穩坐我的書本式摺疊機冠軍，這週又多用了幾天，我更確定它的地位。展開只有 4.2mm，是史上最薄最輕的 Fold，光這一點就讓它放口袋、拿在手上的感覺完全不一樣。8 吋 OLED 內螢幕、直接從 S25 Ultra 搬過來的 2 億畫素主鏡頭、Snapdragon 8 Elite for Galaxy，加上終於讓人忘記摺痕的轉軸，這就是我會推薦給想要摺疊機又不想妥協的人的機種。Pixel 10 Pro Fold 緊跟在後，靠的是書本式摺疊機首見的 IP68 防水，意思是你終於不用在水邊小心翼翼。Google 的影像調校乾淨自然，對天天用 Google 全家桶的人來說就是首選。這個月的黑馬是 Motorola Razr Fold，評測一直給好評，所以就算排在第十一，分數我還是給得很高，它把書本式摺疊玩得很有趣。Oppo Find N5 跟 Honor Magic V3 收尾，兩台都薄、都精緻，水貨買得到的話很值得入手。翻蓋這邊，Galaxy Z Flip 7 的外螢幕跟續航還是最強，Razr Ultra 2026 則靠個性取勝。Samsung 年初推的 Galaxy Z TriFold 賣台幣七萬多還是秒殺，說明市場真的買單敢衝的摺疊硬體。這週沒有任何消息讓我想動排名，前段班只是把該做的做好而已。",
   [
     {"title": "Galaxy Z Fold 7 就是無妥協首選", "body": "展開 4.2mm，史上最薄最輕的 Fold，搭 8 吋 OLED、S25 Ultra 那顆 2 億畫素感光元件，還有 Snapdragon 8 Elite for Galaxy。改良過的轉軸讓摺痕很難察覺，闔起來像正常手機、打開像平板，這台就是這種感覺。"},
     {"title": "Pixel 10 Pro Fold 防水最強", "body": "IP68 是書本式摺疊機首見，下雨潑到都不怕，以前摺疊機用戶最緊張的情境它都扛得住。再加上 Google 乾淨的影像處理跟深度 App 整合，天天用 Gmail、相簿、地圖的人選它準沒錯。"},
     {"title": "Motorola Razr Fold 是本季驚喜", "body": "評測一直說它是今年最好玩的摺疊機之一，所以分數我給得高、排名只是位置問題。它證明 Motorola 不只會做翻蓋，書本式也玩得起來，想要點不一樣的人值得看看。"}
   ])

# ---------------- Smart watches ----------------
do("best-smart-watches.json",
   [
     {"title": "The best smartwatches in 2026: Options for every budget", "url": "https://www.wareable.com/smartwatches/best-smartwatch-reviews-compared-8286", "source": "Wareable"},
     {"title": "7 Of The Best Smartwatches You Can Buy In 2026", "url": "https://www.slashgear.com/2180881/best-smartwatches-in-2026/", "source": "SlashGear"},
     {"title": "Garmin Watch vs Apple Watch: What's Best in 2026?", "url": "https://vertu.com/guides/whats-the-best-smart-watch-apple-watch-vs-garmin-for-fitness-enthusiasts-in-2026", "source": "Vertu"}
   ],
   "The Apple Watch Ultra 3 holds my top spot and the reasoning has not changed this week, it is the most complete smartwatch you can strap on if you carry an iPhone. The brightest display Apple has shipped, up to roughly 60 hours of battery in the right mode, rugged titanium, and the deepest app ecosystem on any wrist. For most iPhone owners the Series 11 is the smarter buy and it sits high for that reason, you get the headline health features in a lighter, cheaper package. The story that keeps repeating in this week's roundups is the ecosystem split, and my ranking reflects it. Garmin owns endurance and battery, which is exactly why the Fenix 8 stays in my top three, its multi week battery and training load analysis change how you live with a watch, you stop thinking about charging. The Venu X1 keeps climbing in reviewer favor as the sport pick and I have nudged it accordingly. For Android, the Galaxy Watch 8 and its Ultra sibling are the obvious choice, tight integration with Samsung and Google services plus a bright AMOLED panel. The Pixel Watch 4 rounds out the Wear OS contingent with the cleanest Google experience. The honest summary I keep landing on is that the platform you already use decides more than any spec sheet, pick the watch that talks to your phone, then optimize for battery or fitness. Nothing this week justifies a reshuffle, the leaders are executing on exactly what makes them good.",
   [
     {"title": "Apple Watch Ultra 3 is the most complete watch for iPhone", "body": "It pairs the brightest display Apple has ever shipped with roughly 60 hours of battery in the right mode, rugged titanium, and the deepest app ecosystem on any wrist. For an iPhone owner who wants everything in one device, nothing else covers as much ground."},
     {"title": "Garmin Fenix 8 redefines what battery buys you", "body": "Multi week battery life and serious training load analysis mean you stop thinking about charging and start trusting the watch on long efforts. For marathon training, ultras, and multi day trips it changes the ownership experience entirely, which is why it stays in my top three."},
     {"title": "Galaxy Watch 8 is the Android pick", "body": "It integrates tightly with Samsung and Google services, runs a bright AMOLED panel, and delivers the smart features Android users actually want on the wrist. If your phone is Android, this is the watch that feels native rather than bolted on."}
   ],
   "Apple Watch Ultra 3 守住我的冠軍，這週理由沒變，只要你用 iPhone，它就是手腕上最完整的智慧手錶。Apple 史上最亮的螢幕、特定模式下大約 60 小時續航、堅固的鈦金屬，加上手錶界最完整的 App 生態。不過對大多數 iPhone 用戶來說，Series 11 才是更聰明的選擇，所以它排得高，重點健康功能都有，機身更輕、價格更甜。這週的評測一直在講生態系分裂這件事，我的排名也照這個邏輯走。Garmin 在耐力跟續航這塊是王者，這也是 Fenix 8 穩居前三的原因，數週續航加上訓練量分析會改變你的使用習慣，你根本不會去想充電這件事。Venu X1 在評測界當運動首選的聲量一直漲，我也順勢微調了一下分數。Android 這邊，Galaxy Watch 8 跟 Ultra 版就是直覺選擇，跟三星、Google 服務整合得緊，AMOLED 螢幕又亮。Pixel Watch 4 收尾 Wear OS 陣營，提供最純淨的 Google 體驗。老實說我每次的結論都一樣，你手上那支手機決定的，比任何規格表都多，先挑跟你手機合拍的，再去煩惱續航或運動功能。這週沒有任何消息值得我動排名，前段班把該做好的都做好了。",
   [
     {"title": "Apple Watch Ultra 3 是 iPhone 最完整的手錶", "body": "Apple 史上最亮螢幕，特定模式下約 60 小時續航，堅固鈦金屬機身，加上手腕上最完整的 App 生態。對想要一支搞定全部的 iPhone 用戶，沒有別台涵蓋面這麼廣。"},
     {"title": "Garmin Fenix 8 重新定義續航的價值", "body": "數週續航加上扎實的訓練量分析，意思是你不用再想充電，長距離挑戰時就放心信任它。馬拉松、超馬、多天行程，它徹底改變你的使用體驗，這就是它穩居前三的原因。"},
     {"title": "Galaxy Watch 8 是 Android 首選", "body": "跟三星、Google 服務整合得很緊，AMOLED 螢幕又亮，把 Android 用戶真正想要的智慧功能戴在手腕上。手機是 Android 的話，這支用起來就是原生感，不會像硬湊上去的。"}
   ])

# ---------------- Smart rings ----------------
do("best-smart-rings.json",
   [
     {"title": "Best smart rings 2026: Oura and top alternatives tested", "url": "https://www.wareable.com/fashion/best-smart-rings-1340", "source": "Wareable"},
     {"title": "Best smart ring 2026: From Oura and Samsung to other discreet fitness trackers", "url": "https://www.techradar.com/health-fitness/fitness-trackers/best-smart-ring", "source": "TechRadar"},
     {"title": "Best smart rings in 2026: we've tested Oura, Ultrahuman, Samsung and more", "url": "https://www.stuff.tv/features/best-smart-rings/", "source": "Stuff"}
   ],
   "The Galaxy Ring and the Oura Ring 4 stay locked at the top of my list and this week's reviews keep arguing the same friendly fight. For most people the Galaxy Ring is the easiest recommendation, it is a first generation product that nails the all round experience, the sleep tracking is genuinely reliable, the insights are detailed, and crucially there is no subscription, which makes the 399 dollar price land far better than rivals that nickel and dime you monthly. The catch is platform, you need an Android phone, and a Samsung phone specifically to unlock every AI feature, so it is not for everyone. The Oura Ring 4 is the one I still call the gold standard for polish and accuracy. Its sleep, stress, and readiness tracking is backed by a growing pile of scientific validation, and nothing else reads your body quite as convincingly. The 5.99 dollar monthly subscription is the price of admission and it is a real downside, but the data quality keeps earning it. RingConn Gen 2 deserves the bronze and the loud praise it gets, it offers the longest battery life in the category, premium finishes, and plenty of actionable insight with no subscription, which makes it the value pick for anyone who wants Oura style tracking without the recurring fee. Ultrahuman's Ring Pro and Ring Air round out the serious field with their metabolic focus. Nothing this week shifts the order, the top three are simply the three rings worth your money right now.",
   [
     {"title": "Galaxy Ring is the easiest recommendation", "body": "It nails the all round experience for a first generation product, with genuinely reliable sleep tracking, detailed insights, and no subscription, which makes the $399 price far easier to swallow. The catch is you need an Android phone, and a Samsung specifically for the full AI feature set."},
     {"title": "Oura Ring 4 is still the gold standard for accuracy", "body": "Its sleep, stress, and readiness tracking is backed by a growing body of scientific validation, and nothing else reads your body quite as convincingly. The $5.99 monthly subscription is a real cost, but the data quality keeps justifying it for people who want the best."},
     {"title": "RingConn Gen 2 is the value champion", "body": "It offers the longest battery life in the category, premium finishes, and plenty of actionable sleep and recovery insight with no subscription fee. For anyone who wants Oura style tracking without the recurring charge, it is the smart money pick."}
   ],
   "Galaxy Ring 跟 Oura Ring 4 還是牢牢卡在我清單前兩名，這週的評測繼續上演一樣的良性對決。對大多數人來說，Galaxy Ring 是最好推薦的，第一代產品就把整體體驗做到位，睡眠追蹤真的準，數據細節豐富，最關鍵的是免訂閱，所以台幣一萬出頭的價格比那些每月跟你收錢的對手好接受太多。缺點是平台限制，要 Android 手機，而且要三星手機才解得開全部 AI 功能，所以不是人人適合。Oura Ring 4 還是我口中精緻度跟準確度的黃金標準。它的睡眠、壓力、恢復追蹤背後有越來越多科學驗證撐腰，沒有別的環讀你的身體讀得這麼有說服力。每月台幣兩百的訂閱是入場券，這確實是個扣分點，可是數據品質一直撐得起這個價。RingConn Gen 2 拿銅牌實至名歸，評測一片好評，它有這個類別最長的續航、質感不錯的外型、夠用的可行動建議，而且免訂閱，想要 Oura 等級追蹤又不想被月費綁住的人就選它。Ultrahuman 的 Ring Pro 跟 Ring Air 靠代謝追蹤收尾。這週沒消息動搖排名，前三名就是現在值得你掏錢的三顆環。",
   [
     {"title": "Galaxy Ring 最好推薦", "body": "第一代產品就把整體體驗做到位，睡眠追蹤真的準、數據細節豐富，而且免訂閱，台幣一萬出頭的價格因此好接受很多。缺點是要 Android 手機，要三星才解得開全部 AI 功能。"},
     {"title": "Oura Ring 4 還是準確度的黃金標準", "body": "睡眠、壓力、恢復追蹤背後有越來越多科學驗證撐腰，沒有別的環讀身體讀得這麼有說服力。每月台幣兩百訂閱是實打實的成本，但對想要最好的人來說，數據品質一直撐得起這個價。"},
     {"title": "RingConn Gen 2 是性價比冠軍", "body": "這個類別最長的續航、質感不錯的外型、夠用的睡眠與恢復建議，而且完全免訂閱。想要 Oura 等級追蹤又不想被月費綁住的人，它就是聰明選擇。"}
   ])

# ---------------- Smart glasses ----------------
do("best-smart-glasses.json",
   [
     {"title": "Ray-Ban Meta Smart Glasses Review: Better, Cooler, and More Useful Than Ever", "url": "https://moorinsightsstrategy.com/research-notes/ray-ban-meta-smart-glasses-review-better-cooler-and-more-useful-than-ever/", "source": "Moor Insights & Strategy"},
     {"title": "Google AI Glasses vs Meta Ray-Ban: Smart Eyewear's First Real Fight", "url": "https://the-gadgeteer.com/2026/05/01/google-ai-glasses-vs-meta-ray-ban-smart-glasses-comparison/", "source": "The Gadgeteer"},
     {"title": "Meta Ray-Ban Display Smart Glasses Review 2026", "url": "https://www.technerdo.com/blog/meta-ray-ban-display-smart-glasses-review-2026", "source": "Technerdo"}
   ],
   "The second generation Ray-Ban Meta stays my number one, and this week's reviews land exactly where I do, Meta now carries the flag for smart glasses in everyday usefulness. The upgrade to Qualcomm's AR1 Gen 1 platform is the quiet hero here, it is a big jump over the wearable chip in the first pair, and it shows in faster captures, snappier voice commands, and on device AI that works without reaching for your phone. Add IPX4 water resistance and the same Ray-Ban looks people already love and you get the camera first social wearable that wins for most buyers. The Oakley Meta HSTN holds second on the strength of its sportier wraparound design and longer battery, it is the pick if your day involves running, cycling, or just a face that suits the Oakley shape. The Meta Ray-Ban Display sits third and earns its premium for the right person, the built in heads up display, 12MP camera, and Neural Band controller justify the 799 dollar price if you actually want hands free navigation, live translation, and glanceable notifications. On the display glasses side, the Xreal One Pro remains the best for turning a pair of glasses into a giant private screen, its optics and field of view lead the category for media and gaming. Even Realities G2 keeps climbing for its discreet everyday display. Google's AI glasses are circling but Meta still owns the practical crown today. Nothing this week moves the order.",
   [
     {"title": "Ray-Ban Meta Gen 2 owns everyday usefulness", "body": "The jump to Qualcomm's AR1 Gen 1 platform delivers faster captures, snappier voice commands, and on device AI that works without your phone. Add IPX4 water resistance and the iconic Ray-Ban looks and it is the camera first social wearable that wins for most people."},
     {"title": "Meta Ray-Ban Display justifies its premium for the right user", "body": "The built in heads up display, 12MP camera, and Neural Band controller make the $799 price worth it if you genuinely want hands free navigation, live translation, and glanceable notifications. It is the pick for someone who wants information in their line of sight, not just a camera."},
     {"title": "Xreal One Pro is the big screen champion", "body": "Its optics and field of view lead the category for turning a pair of glasses into a giant private display, ideal for movies and gaming on the go. For media first buyers who want a personal cinema rather than a social camera, it is the clear choice."}
   ],
   "第二代 Ray-Ban Meta 還是我的第一名，這週的評測跟我想的一樣，論日常實用度，Meta 現在就是智慧眼鏡的扛霸子。升級到 Qualcomm AR1 Gen 1 平台是低調的功臣，比第一代那顆穿戴晶片進步一大截，反映在更快的拍攝、更俐落的語音指令，還有不用掏手機就能跑的裝置端 AI。再加上 IPX4 防潑水跟大家本來就愛的 Ray-Ban 外型，這就是大多數人會買單的相機優先社交眼鏡。Oakley Meta HSTN 守第二，靠的是更運動感的環繞式設計跟更長的續航，跑步、騎車或臉型適合 Oakley 的人選它就對了。Meta Ray-Ban Display 排第三，對對的人來說值這個錢，內建抬頭顯示、1200 萬畫素相機、Neural Band 控制環，如果你真的想要免持導航、即時翻譯、瞄一眼就看到的通知，台幣兩萬四這價就划算。顯示型眼鏡這邊，Xreal One Pro 還是把眼鏡變成巨大私人螢幕的最強選擇，光學跟視野在這類別領先，看片打電動超讚。Even Realities G2 靠低調的日常顯示聲量一直漲。Google 的 AI 眼鏡在旁邊虎視眈眈，但今天實用王冠還是 Meta 的。這週排名不動。",
   [
     {"title": "Ray-Ban Meta 二代日常實用最強", "body": "升級 Qualcomm AR1 Gen 1 平台，拍攝更快、語音指令更俐落、裝置端 AI 不用掏手機就能跑。再加上 IPX4 防潑水跟經典 Ray-Ban 外型，這就是大多數人會買單的相機優先社交眼鏡。"},
     {"title": "Meta Ray-Ban Display 對的人就值這個錢", "body": "內建抬頭顯示、1200 萬畫素相機、Neural Band 控制環，如果你真的想要免持導航、即時翻譯、瞄一眼就看到通知，台幣兩萬四就划算。想把資訊放進視線裡、不只是拍照的人，選它。"},
     {"title": "Xreal One Pro 是大螢幕冠軍", "body": "光學跟視野在這類別領先，把眼鏡變成巨大私人螢幕，出門看片打電動超適合。想要個人劇院、不是社交相機的影音優先買家，它就是明確選擇。"}
   ])

# ---------------- E-readers ----------------
do("best-e-readers.json",
   [
     {"title": "Best ereaders in 2026: 9 top ebook readers tested", "url": "https://www.techradar.com/best/best-ereader", "source": "TechRadar"},
     {"title": "Best E-Readers 2026 - Kindle vs Kobo vs Color E-Ink", "url": "https://gadgetwisereviews.com/blog/best-ereaders-2026", "source": "Gadgetwise Reviews"}
   ],
   "The Kindle Paperwhite 2025 stays my top pick and the latest roundups back the call, it now competes with the Kobo Clara BW for the sharpest e-paper display thanks to the newest generation E Ink. For most readers this is the one, a fast, crisp, glare free screen, weeks of battery, and the biggest e-book store on the planet plus Kindle Unlimited and Libby library borrowing. It just works. The Kobo Libra Colour holds second and many reviewers actually call it the best ereader overall for value, and I see why, the physical page turn buttons, color E Ink, and seamless Overdrive and Libby integration make it the pick for library lovers and anyone who wants color comics or note taking. If you live outside Amazon's walls, Kobo is the freer ecosystem, native EPUB support means no conversion dance. The Kindle Colorsoft sits third as Amazon's color answer, smooth within the Kindle world but less flexible than Kobo. The Kobo Clara BW deserves a shout for adding repairability through an iFixit partnership, spare parts and step by step guides extend its life in a way the category badly needed. Boox Palma 2 stays the cult favorite for pocket sized Android reading. Nothing this week reshuffles the order, the choice still comes down to which store you want to live in, Amazon for convenience and catalog, Kobo for openness and library borrowing.",
   [
     {"title": "Kindle Paperwhite 2025 is the safe top pick", "body": "The newest generation E Ink gives it one of the sharpest e-paper displays available, with a fast glare free screen and weeks of battery. Paired with the largest e-book store, Kindle Unlimited, and Libby library support, it is the reader that simply works for most people."},
     {"title": "Kobo Libra Colour is the value and library champion", "body": "Physical page turn buttons, color E Ink, and seamless Overdrive and Libby integration make it the pick for library lovers and comic readers. Its native EPUB support and open ecosystem reward anyone who wants to read outside Amazon's walls without converting files."},
     {"title": "Kobo Clara BW leads on repairability", "body": "Through an iFixit partnership it offers spare parts, repair kits, and step by step guides, so the device lasts instead of landing in a drawer when something breaks. It is a meaningful answer to e-reader longevity that the rest of the category should copy."}
   ],
   "Kindle Paperwhite 2025 還是我的冠軍，最新評測也站我這邊，靠著最新一代 E Ink，它的螢幕銳利度已經跟 Kobo Clara BW 並駕齊驅。對大多數讀者來說這台就對了，快速、銳利、不反光的螢幕，續航好幾週，加上全球最大的電子書店、Kindle Unlimited，還能用 Libby 借圖書館的書。就是好用，沒煩惱。Kobo Libra Colour 守第二，很多評測甚至說它整體性價比最高，我懂為什麼，實體翻頁鍵、彩色 E Ink，加上跟 Overdrive、Libby 無縫整合，愛借圖書館書、想看彩色漫畫或做筆記的人選它。如果你不想被綁在 Amazon 裡，Kobo 的生態更自由，原生支援 EPUB，不用搞格式轉換那套。Kindle Colorsoft 排第三，是 Amazon 的彩色答案，在 Kindle 體系裡順，但彈性不如 Kobo。Kobo Clara BW 值得一提，跟 iFixit 合作加入可維修性，有零件、維修包、step by step 教學，延長壽命這點正是這個類別很缺的。Boox Palma 2 還是口袋 Android 閱讀的死忠最愛。這週排名不動，選擇還是看你想住在哪個書店，Amazon 圖方便跟書多，Kobo 圖自由跟借圖書館。",
   [
     {"title": "Kindle Paperwhite 2025 是安全冠軍", "body": "最新一代 E Ink 給它數一數二銳利的電子紙螢幕，快速、不反光，續航好幾週。再配上最大的電子書店、Kindle Unlimited、Libby 借書，對大多數人就是好用不用煩。"},
     {"title": "Kobo Libra Colour 是性價比與圖書館冠軍", "body": "實體翻頁鍵、彩色 E Ink，加上跟 Overdrive、Libby 無縫整合，愛借圖書館書跟看漫畫的人選它。原生支援 EPUB、生態開放，想在 Amazon 之外閱讀又不想轉檔的人最受用。"},
     {"title": "Kobo Clara BW 維修性領先", "body": "跟 iFixit 合作提供零件、維修包跟 step by step 教學，東西壞了能修，不會壞掉就丟抽屜。這對電子書閱讀器的壽命是個實在的解法，其他品牌該學起來。"}
   ])

# ---------------- Portable chargers ----------------
do("best-portable-chargers.json",
   [
     {"title": "The best power banks and portable chargers for every device in 2026", "url": "https://www.engadget.com/computing/accessories/best-power-bank-143048526.html", "source": "Engadget"},
     {"title": "Anker Nano Power Bank 30W Review: Best Portable Charger 2026", "url": "https://www.mensjournal.com/gear/anker-nano-power-bank-review", "source": "Men's Journal"},
     {"title": "Best Power Bank 2026: 5 New Chargers That Raised the Bar", "url": "https://the-gadgeteer.com/2026/05/06/best-power-bank-2026-five-new-chargers/", "source": "The Gadgeteer"}
   ],
   "The Anker Prime 26K 300W keeps my crown and the latest reviews call it exactly what I do, the no compromise desktop replacement in your bag. It packs 26,250mAh into a pocketable brick that pushes 300W total across two USB-C and one USB-A, enough to run a 16 inch MacBook Pro at full speed, and Anker's 250W dual port input refills it to 50 percent in about 13 minutes. If you carry a laptop, this is the one. The Prime 27650 250W sits second for the same reasons in a slightly different balance of capacity and speed, it is the pick if you want maximum reserve over peak wattage. The pattern across 2026's best chargers is specialization, and my list reflects it. For phone first buyers the smaller Ankers earn their spots, the Nano 10K and the MagGo 10K Qi2 give you all day power that disappears into a jacket pocket, with the Nano's built in cable removing the one accessory everyone forgets. The Baseus PicoGo and Belkin BoostCharge Pro carry the magnetic Qi2 wireless crowd for iPhone owners who want to skip cables entirely. Ugreen's Nexode 25000mAh 200W remains the value heavyweight, a lot of laptop capable power for less than the Prime. Nothing this week reorders the list, the leaders are simply the most capable bricks you can buy, matched to how you actually charge.",
   [
     {"title": "Anker Prime 26K 300W is the laptop traveler's brick", "body": "It fits 26,250mAh into a pocketable body that delivers 300W across two USB-C and one USB-A, enough to run a 16 inch MacBook Pro at full speed. The 250W dual port input refills it to 50 percent in roughly 13 minutes, so it is ready almost as fast as you are."},
     {"title": "Anker Nano 10K is the everyday pocket pick", "body": "It delivers genuine all day phone power in a build that disappears into a jacket pocket, and the built in cable removes the one accessory everyone forgets at home. For phone first buyers who want simple, reliable top ups, it is the easy recommendation."},
     {"title": "Ugreen Nexode 25000mAh 200W is the value heavyweight", "body": "It offers a lot of laptop capable capacity and output for noticeably less than the Prime tier, making real high wattage charging accessible. If you want to power a laptop on the go without paying flagship money, this is the smart buy."}
   ],
   "Anker Prime 26K 300W 守住我的冠軍，最新評測的講法跟我一樣，它就是塞進包包的無妥協桌機替身。26,250mAh 塞進一個可放口袋的磚塊，兩個 USB-C 加一個 USB-A 合計輸出 300W，足以讓 16 吋 MacBook Pro 全速跑，而且 Anker 的 250W 雙孔輸入大約 13 分鐘就能充回一半。有帶筆電的人，就是這台。Prime 27650 250W 排第二，理由一樣，只是容量跟速度的平衡略不同，想要最大電量勝過最高瓦數的人選它。2026 最強行充的共同趨勢就是專業分工，我的清單也照這個走。手機優先的人，小台 Anker 各有定位，Nano 10K 跟 MagGo 10K Qi2 給你一整天的電力又能塞進外套口袋，Nano 內建線材更省掉那條大家總是忘記帶的配件。Baseus PicoGo 跟 Belkin BoostCharge Pro 服務磁吸 Qi2 無線族群，iPhone 用戶想完全擺脫線材就看它們。Ugreen Nexode 25000mAh 200W 還是性價比重量級，能餵筆電的大電力卻比 Prime 便宜不少。這週沒消息動排名，前段班就是最能打的磚塊，看你實際怎麼充來配。",
   [
     {"title": "Anker Prime 26K 300W 是筆電族的磚塊", "body": "26,250mAh 塞進可放口袋的機身，兩個 USB-C 加一個 USB-A 合計 300W，足以讓 16 吋 MacBook Pro 全速跑。250W 雙孔輸入約 13 分鐘充回一半，幾乎跟你出門一樣快就準備好。"},
     {"title": "Anker Nano 10K 是日常口袋首選", "body": "一整天的手機電力，機身小到能塞進外套口袋，內建線材還省掉那條大家總忘記帶的配件。手機優先、想要簡單可靠補電的人，這台最好推薦。"},
     {"title": "Ugreen Nexode 25000mAh 200W 是性價比重量級", "body": "能餵筆電的大容量跟輸出，價格卻比 Prime 等級便宜明顯一截，讓真正的高瓦數充電變得親民。想在外面餵筆電又不想花旗艦價的人，這台是聰明選擇。"}
   ])

# ---------------- Portable projectors ----------------
do("best-portable-projectors.json",
   [
     {"title": "Best portable projectors of 2026, tried and tested", "url": "https://www.cnn.com/cnn-underscored/reviews/best-portable-projectors", "source": "CNN Underscored"},
     {"title": "Best portable projector of 2026: Tested for streaming and presenting on the go", "url": "https://www.techradar.com/pro/best-portable-projector", "source": "TechRadar"},
     {"title": "The Best Portable Projectors in 2026", "url": "https://www.gizmochina.com/2026/03/07/best-portable-projectors-in-2026/", "source": "Gizmochina"}
   ],
   "The XGIMI MoGo 4 Laser keeps my top spot and the latest testing reinforces why, it delivers top tier performance with triple laser technology, 550 ISO lumens, 1080p, and a claimed 110 percent of the BT.2020 color gamut, which translates to vivid color, deep blacks, and sharp clarity in a genuinely portable body. For someone who wants a big bright picture without hauling a home theater projector, this is the pick. The LG CineBeam Q holds second on design and image quality, its tiny form and bright laser make it the most living room friendly portable on my list, though reviewers note LG's bigger CineBeam S struggled with auto adjustment and WebOS, so I keep the Q where it earns its place. The Hisense M2 Pro sits third as the value laser option with a strong picture for the money. The Nebula Mars 3 stays the outdoor champion, rugged, bright, and built around a big battery so movie night in the backyard does not need a wall outlet, and the new Nebula P1i deserves a mention this week for finally addressing sound, its detachable stereo speakers make it the well rounded pick reviewers keep praising for sports, films, and gaming. Samsung's Freestyle 2nd Gen remains the lifestyle wildcard for its swivel design. Nothing this week reorders the list, the leaders are simply the brightest, sharpest, most portable boxes you can carry to a screen anywhere.",
   [
     {"title": "XGIMI MoGo 4 Laser is the portable picture king", "body": "Triple laser tech, 550 ISO lumens, 1080p, and a claimed 110 percent BT.2020 gamut deliver vivid color, deep blacks, and sharp clarity in a body you can actually carry. For a big bright image without a full home theater rig, it is the clear top pick."},
     {"title": "Nebula Mars 3 owns the backyard", "body": "It is rugged, bright, and built around a large battery, so movie night outdoors does not need a wall outlet anywhere nearby. For camping, patios, and tailgates where power is scarce, this is the projector that keeps the show running."},
     {"title": "Nebula P1i finally fixes projector sound", "body": "Its detachable stereo speakers address the audio weakness that plagues most portables, making it the well rounded pick reviewers keep praising for sports, films, and gaming. When you do not want to drag along a separate speaker, the P1i covers picture and sound in one box."}
   ],
   "XGIMI MoGo 4 Laser 守住我的冠軍，最新測試又印證了原因，三雷射技術、550 ISO 流明、1080p，官方宣稱涵蓋 110% BT.2020 色域，換成實際體驗就是色彩鮮豔、黑階夠深、畫面銳利，而且機身真的好攜帶。想要大又亮的畫面、又不想扛一台家庭劇院投影機的人，就選它。LG CineBeam Q 守第二，靠的是設計跟畫質，小巧機身加亮眼雷射，是我清單裡最適合放客廳的攜帶款，不過評測說 LG 那台更大的 CineBeam S 在自動校正跟 WebOS 上卡卡，所以 Q 待在它該在的位置。Hisense M2 Pro 排第三，是性價比雷射選擇，這個價畫質很有料。Nebula Mars 3 還是戶外王者，堅固、夠亮、大電池為核心，後院電影夜不用找牆上插座。新的 Nebula P1i 這週值得一提，終於正視音效問題，可拆式立體聲喇叭讓它成為評測一直誇的全能款，看球、看片、打電動都行。Samsung Freestyle 2nd Gen 還是靠旋轉設計當生活風格黑馬。這週排名不動，前段班就是你能帶去任何牆面前最亮、最銳利、最好攜帶的盒子。",
   [
     {"title": "XGIMI MoGo 4 Laser 是攜帶畫質王", "body": "三雷射、550 ISO 流明、1080p，官方稱涵蓋 110% BT.2020 色域，帶來鮮豔色彩、深黑階跟銳利畫面，機身又真的帶得動。想要大又亮的畫面卻不用整套家庭劇院的人，它就是明確首選。"},
     {"title": "Nebula Mars 3 稱霸後院", "body": "堅固、夠亮、以大電池為核心，戶外電影夜附近沒插座也照放。露營、陽台、停車場聚會這種沒電源的場合，它就是讓節目繼續跑的投影機。"},
     {"title": "Nebula P1i 終於修好投影機音效", "body": "可拆式立體聲喇叭解決多數攜帶款的音效弱點，成為評測一直誇的全能款，看球、看片、打電動都行。不想另外帶喇叭的時候，P1i 一台搞定畫面跟聲音。"}
   ])

print("ALL DONE")
