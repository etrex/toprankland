import sys; sys.path.insert(0, "/Users/etrexkuo/toprankland/scripts")
from daily_helper import load, save, upsert, last_rankings, DATE


def do(name, refs, en, zh):
    d, p = load(name)
    entry = {"date": DATE, "rankings": last_rankings(d), "references": refs, "i18n": {"en": en, "zh-tw": zh}}
    upsert(d, entry)
    save(p, d)
    print("updated", name)


# ---------------- best-smartphones ----------------
do("best-smartphones.json",
   [
     {"title": "Top 10 flagship phones in June 2026", "url": "https://www.gadgetbridge.com/gadget-bridge-ace/top-10-flagship-phones-in-june-2026/", "source": "Gadget Bridge"},
     {"title": "I tested the 7 top flagship phones of 2026", "url": "https://www.techradar.com/phones/i-tested-7-top-flagship-phones-from-apple-samsung-google-and-more-heres-which-models-i-recommend-for-every-type-of-user", "source": "TechRadar"},
   ],
   {
     "commentary": "Heading into June I am keeping the iPhone 17 Pro Max at number one, and the reason is the same boring strength that wins every long-term test: battery life paired with a chip nobody catches. The A19 Pro still posts the highest sustained scores in the field, and the Pro Max simply lasts longer between charges than anything else this size. That combination is what I want from a phone I carry every day. The Galaxy S26 Ultra holds a very close second on the strength of its cameras. The 200MP main sensor and the new Privacy Shield display, the only S26 variant to get it, make it the most complete Android flagship, and Samsung held the starting price flat year over year, which keeps it honest value at this tier. Pixel 10 Pro XL stays third because Google's photography and on-device AI remain the smartest in any phone, from call screening to live translation in your own voice. The middle of the board is where the value lives. OnePlus 15 stays fourth as the performance-per-dollar champion with its huge battery, and the regular iPhone 17 holds fifth as the phone I recommend to most people who do not need a Pro. Xiaomi 17 Ultra, Oppo Find X9 Ultra and the rest carry forward. Nothing this week reshuffled the order, so I held ranks and let the verdicts stand. Buy the Pro Max for endurance, the S26 Ultra for the camera, the Pixel for AI.",
     "highlights": [
       {"title": "iPhone 17 Pro Max wins on endurance", "body": "The A19 Pro posts the highest sustained performance in the field and the Pro Max outlasts every rival its size between charges. That pairing of speed and battery is exactly what a daily driver needs, so it stays number one."},
       {"title": "Galaxy S26 Ultra owns the camera crown", "body": "Its 200MP main sensor and exclusive Privacy Shield display make it the most complete Android flagship, and Samsung kept the starting price flat year over year. That keeps it honest value and a deserved close second."},
       {"title": "Pixel 10 Pro XL is the smartest phone", "body": "Google's computational photography and on-device AI, from call screening to live translation in your own voice, remain unmatched. For anyone who buys a phone for its brains, the Pixel holds a clear third."},
       {"title": "OnePlus 15 is the value flagship", "body": "Its huge battery and top-tier performance deliver the best price-to-power ratio on the board. For buyers who want flagship speed without the flagship price, it stays the smart fourth-place pick."},
     ],
   },
   {
     "commentary": "進入 6 月，我還是把 iPhone 17 Pro Max 放第一，理由就是那個每次長期測試都會贏的無聊強項，續航加上一顆沒人追得上的晶片。A19 Pro 在持續效能上還是全場最高，Pro Max 同尺寸裡就是比別人撐更久。這個組合正是我每天帶著走的手機要的東西。Galaxy S26 Ultra 緊咬第二，靠的是相機。2 億畫素主鏡頭加上新的 Privacy Shield 螢幕，全 S26 系列只有它有，讓它成為最完整的 Android 旗艦，而且三星起售價跟去年持平，這個級距算很實在了。Pixel 10 Pro XL 守第三，因為 Google 的拍照跟裝置端 AI 還是所有手機裡最聰明的，從來電過濾到用你自己的聲音即時翻譯都是。話說回來，榜單中段才是性價比的天下。OnePlus 15 守第四，靠大電池當每塊錢效能最強的選手，一般版 iPhone 17 守第五，是我會推薦給多數不需要 Pro 的人的機型。Xiaomi 17 Ultra、Oppo Find X9 Ultra 跟其他全部照舊。這週沒事件洗牌，所以我守住排名。要續航選 Pro Max，要相機選 S26 Ultra，要 AI 選 Pixel。",
     "highlights": [
       {"title": "iPhone 17 Pro Max 贏在續航", "body": "A19 Pro 持續效能全場最高，Pro Max 同尺寸裡每次充電都撐得比對手久。這種速度加電量的搭配正是每日機要的，所以第一是它。"},
       {"title": "Galaxy S26 Ultra 拿下相機王冠", "body": "2 億畫素主鏡頭加獨家 Privacy Shield 螢幕，讓它成為最完整的 Android 旗艦，三星起售價又跟去年持平。這讓它實在又超值，緊咬第二實至名歸。"},
       {"title": "Pixel 10 Pro XL 是最聰明的手機", "body": "Google 的運算攝影跟裝置端 AI，從來電過濾到用你自己聲音即時翻譯，依然無人能比。買手機看腦袋的人，Pixel 穩坐第三。"},
       {"title": "OnePlus 15 是性價比旗艦", "body": "大電池加頂級效能，端出榜上最強的價格對效能比。想要旗艦速度又不想付旗艦價的人，它就是聰明的第四名選擇。"},
     ],
   })

# ---------------- best-foldable-smartphones ----------------
do("best-foldable-smartphones.json",
   [
     {"title": "Best foldable phones to buy in 2026", "url": "https://www.phonearena.com/news/best-foldable-smartphones_id132093", "source": "PhoneArena"},
     {"title": "Why Pixel 10 Pro Fold beats Samsung Z Fold 7 (2026 Review)", "url": "https://www.loudnwireless.com/blog/why-pixel-10-pro-fold-beats-samsung-z-fold-7-2026-review", "source": "Loud and Wireless"},
   ],
   {
     "commentary": "The foldable race in June stays a two-horse fight, and I keep the Galaxy Z Fold 7 at number one because it is the most capable all-around book-style foldable you can buy. Samsung's engineering this generation is the story: it is remarkably slim both folded and open without giving up durability, and the 200MP main camera is the best optics ever bolted to a folding phone. When someone wants a foldable that does everything, this is still the answer. The Pixel 10 Pro Fold holds a close second and genuinely beats the Fold 7 on two real-world axes. It carries an IP68 rating, a first for a book-style foldable, and its battery life runs longer than Samsung's while costing 200 dollars less. If durability and endurance matter more to you than camera ceiling, the Pixel is the smarter buy, and that is exactly why it sits a hair behind. The Motorola Razr Fold stays third on this board as the entrant that directly fixes the category's two oldest complaints, battery and thickness. OPPO Find N5, Honor Magic V3 and vivo X Fold5 fill out the strong book-style tier, while the Z Flip 7 leads the clamshells on value. Nothing this week reshuffled the order, so I held ranks. Pick the Fold 7 for capability, the Pixel Fold for durability and battery.",
     "highlights": [
       {"title": "Galaxy Z Fold 7 is the most capable foldable", "body": "It is remarkably slim folded and open without sacrificing durability, and its 200MP main camera is the best optics ever on a folding phone. For a foldable that does everything well, it stays number one."},
       {"title": "Pixel 10 Pro Fold wins durability and battery", "body": "It is the first book-style foldable with an IP68 rating and outlasts the Fold 7 on battery while costing 200 dollars less. If toughness and endurance lead your list, it is the smarter buy and a close second."},
       {"title": "Motorola Razr Fold fixes the old complaints", "body": "It directly targets the two longest-standing foldable weaknesses, battery life and thickness, and lands them. That practical focus keeps it firmly in the top tier of this board."},
       {"title": "Z Flip 7 leads the clamshells on value", "body": "Among flip-style foldables it offers the best balance of price and everyday usability. For buyers who want a pocketable fold without the book-style premium, it is the value pick of the format."},
     ],
   },
   {
     "commentary": "6 月的折疊機戰局還是兩強對決，我把 Galaxy Z Fold 7 放第一，因為它是你買得到、最全能的橫向書本式折疊機。這代三星的工藝就是重點，折起來跟攤開都薄得驚人，卻沒犧牲耐用度，2 億畫素主鏡頭更是折疊機史上最強的光學。有人想要一支什麼都能做的折疊機，答案還是它。Pixel 10 Pro Fold 緊咬第二，而且在兩個實際面向上真的贏過 Fold 7。它有 IP68 防水，是書本式折疊機第一個做到的，續航又比三星長，價格還便宜約台幣六千。如果耐用跟續航對你比相機天花板更重要，Pixel 是更聰明的選擇，這也正是它只落後一點點的原因。Motorola Razr Fold 在這份榜單守第三，是直接修掉這類別兩個最老問題的選手，電量跟厚度。OPPO Find N5、Honor Magic V3、vivo X Fold5 撐起強勢的書本式中段，Z Flip 7 則是翻蓋機裡性價比最高的。這週沒事件洗牌，所以我守住排名。要全能選 Fold 7，要耐用跟續航選 Pixel Fold。",
     "highlights": [
       {"title": "Galaxy Z Fold 7 是最全能折疊機", "body": "折起攤開都薄得驚人卻沒犧牲耐用，2 億畫素主鏡頭是折疊機史上最強光學。要一支什麼都做得好的折疊機，第一還是它。"},
       {"title": "Pixel 10 Pro Fold 贏在耐用跟續航", "body": "它是第一個有 IP68 防水的書本式折疊機，續航贏過 Fold 7，價格還便宜約台幣六千。耐用跟續航排你清單前面，它是更聰明的買法，緊咬第二。"},
       {"title": "Motorola Razr Fold 修好老毛病", "body": "它直接針對折疊機最老的兩個弱點，續航跟厚度，而且都做到了。這份務實讓它穩穩待在這份榜單的上段。"},
       {"title": "Z Flip 7 是翻蓋機性價比王", "body": "翻蓋式折疊機裡，它在價格跟日常好用度之間平衡最好。想要能塞口袋的折疊機又不想付書本式溢價的人，它就是這個型態的性價比選擇。"},
     ],
   })

# ---------------- best-tablets ----------------
do("best-tablets.json",
   [
     {"title": "Best Android Tablet 2026: Samsung, Google, OnePlus & More", "url": "https://www.techadvisor.com/article/723363/best-android-tablet.html", "source": "Tech Advisor"},
     {"title": "We've tested the best tablets in 2026 for all budgets and uses", "url": "https://www.tomsguide.com/best-picks/best-tablet", "source": "Tom's Guide"},
   ],
   {
     "commentary": "My tablet board in June leads with the iPad Air (M4), and I stand by that over the more powerful Pro because the Air is the one most people should actually buy. It carries the same iPadOS app ecosystem that nobody on Android can match, runs every creative app smoothly, and lands at a price that makes the Pro feel like overkill for anyone who is not editing ProRes or running pro audio. The iPad Pro (M5) holds second as the most powerful tablet on the planet, with a display that is simply the best in the category and almost 13 hours of real battery in testing. If raw power and that tandem OLED screen are worth the premium to you, it is the obvious step up. The Galaxy Tab S11 Ultra stays third as the biggest and best Galaxy Tab ever, with a 14.6-inch screen and an 11,600mAh battery that make it the large-canvas Android pick. The OnePlus Pad 3 holds fourth and earns it as the value standout, pairing the Snapdragon 8 Elite with a 144Hz display and battery life that genuinely beats the field at its price. The iPad mini, Galaxy Tab S11 and the budget slates carry forward. Nothing this week moved the order. Buy the Air for most people, the Pro for power, the OnePlus Pad 3 for value.",
     "highlights": [
       {"title": "iPad Air M4 is the tablet most people should buy", "body": "It runs the iPadOS app ecosystem Android cannot match, handles every creative app smoothly, and costs far less than the Pro. For the vast majority of buyers it is the right call, so it stays number one."},
       {"title": "iPad Pro M5 is the power ceiling", "body": "It is the most powerful tablet on the planet with the best display in the category and nearly 13 hours of real battery. If you edit ProRes or run pro audio, the premium is worth it, and it holds a clear second."},
       {"title": "Galaxy Tab S11 Ultra owns the big canvas", "body": "Its 14.6-inch screen and 11,600mAh battery make it the biggest and best Galaxy Tab ever. For Android users who want maximum drawing and multitasking real estate, it stays the large-format pick at third."},
       {"title": "OnePlus Pad 3 is the value standout", "body": "It pairs the Snapdragon 8 Elite with a 144Hz display and battery life that beats rivals at its price. For buyers who want flagship speed without the Apple or Samsung premium, it holds a deserved fourth."},
     ],
   },
   {
     "commentary": "6 月我的平板榜由 iPad Air（M4）領軍，我堅持把它放在效能更猛的 Pro 前面，因為 Air 才是多數人真正該買的那台。它有同樣的 iPadOS App 生態，這點 Android 沒人比得上，每個創作 App 都跑得順，價格又讓 Pro 對那些不是在剪 ProRes 或跑專業音訊的人顯得過剩。iPad Pro（M5）守第二，是地表最強的平板，螢幕就是這個類別最好的，實測續航將近 13 小時。如果純效能跟那塊雙層 OLED 螢幕對你值得多花錢，它就是明顯的升級選擇。Galaxy Tab S11 Ultra 守第三，是史上最大最強的 Galaxy Tab，14.6 吋螢幕加 11,600mAh 電池，是大畫布的 Android 首選。OnePlus Pad 3 守第四，當之無愧是性價比之星，Snapdragon 8 Elite 配 144Hz 螢幕，續航在同價位真的贏過全場。iPad mini、Galaxy Tab S11 跟入門平板全部照舊。這週沒事件動排名。多數人買 Air，要效能買 Pro，要性價比買 OnePlus Pad 3。",
     "highlights": [
       {"title": "iPad Air M4 是多數人該買的平板", "body": "它有 Android 比不上的 iPadOS App 生態，每個創作 App 都跑得順，價格又比 Pro 低一截。對絕大多數買家來說它就是正解，所以第一是它。"},
       {"title": "iPad Pro M5 是效能天花板", "body": "它是地表最強平板，螢幕是類別最好，實測續航近 13 小時。剪 ProRes 或跑專業音訊的人，這個溢價值得，它穩坐第二。"},
       {"title": "Galaxy Tab S11 Ultra 主宰大畫布", "body": "14.6 吋螢幕加 11,600mAh 電池，是史上最大最強的 Galaxy Tab。想要最大繪圖跟多工空間的 Android 使用者，它穩坐第三的大尺寸選擇。"},
       {"title": "OnePlus Pad 3 是性價比之星", "body": "Snapdragon 8 Elite 配 144Hz 螢幕，續航在同價位贏過對手。想要旗艦速度又不想付蘋果三星溢價的人，它穩坐第四實至名歸。"},
     ],
   })

# ---------------- best-laptops ----------------
do("best-laptops.json",
   [
     {"title": "The best laptops in 2026 — tested, reviewed, and worth your money", "url": "https://www.tomsguide.com/computing/laptops/best-laptops", "source": "Tom's Guide"},
     {"title": "ASUS Zenbook A16 2026 vs MacBook Air 15 M5", "url": "https://www.windowscentral.com/hardware/asus/asus-zenbook-a16-2026-vs-macbook-air-15-m5", "source": "Windows Central"},
   ],
   {
     "commentary": "June keeps the MacBook Air 13-inch (M5) at the top of my laptop board, and it stays there because it remains the best laptop for most people by a comfortable margin. The M5 silicon delivers performance that punches far above the price, the fanless design runs silent, and the battery comfortably clears a full work day. Apple raised the base to 1,099 dollars but doubled storage to 512GB, so the value math still works. The MacBook Pro 14-inch (M4 Pro) holds second as the step up for anyone who needs sustained pro power, with a brighter display and the headroom for heavy video and code workloads. The interesting pressure this month comes from Windows: the Zenbook A16 with its Snapdragon X2 Elite genuinely beats the M5 on some battery and efficiency tests, and it stays third as the best-value all-rounder with an excellent OLED panel in a light chassis. The XPS 14 holds fourth for its display and endurance, and the Razer Blade 16 stays fifth as the performance pick when raw GPU is the job. Surface Pro 11, the Spectre x360 and the budget Acers carry forward. Nothing this week reshuffled the order, so I held ranks. Buy the Air for most people, the Pro for sustained power, the Zenbook A16 for Windows value.",
     "highlights": [
       {"title": "MacBook Air M5 is still the laptop for most people", "body": "Its M5 silicon punches above the price, the fanless design runs silent, and battery clears a full work day. Apple doubled base storage to 512GB, so the value holds, and it stays number one."},
       {"title": "MacBook Pro 14 M4 Pro is the power step up", "body": "It adds sustained pro performance, a brighter display and headroom for heavy video and code. For anyone whose work actually taxes a laptop, it is the natural upgrade and a clear second."},
       {"title": "Zenbook A16 is the Windows value champion", "body": "Its Snapdragon X2 Elite beats the M5 on some battery and efficiency tests, paired with a great OLED panel in a light chassis. That makes it the best-value all-rounder and a deserved third."},
       {"title": "Razer Blade 16 is the performance pick", "body": "When raw GPU power is the entire job, it delivers the muscle the ultraportables cannot. For gaming and creative workloads that demand a discrete GPU, it stays the specialist choice at fifth."},
     ],
   },
   {
     "commentary": "6 月我的筆電榜還是 MacBook Air 13 吋（M5）穩坐第一，它待在這裡是因為它依然是多數人最好的筆電，而且差距很舒服。M5 晶片端出遠超價格的效能，無風扇設計安靜，續航輕鬆撐過一整個工作天。蘋果把起售價拉到約台幣三萬五，但儲存空間翻倍到 512GB，所以性價比帳還是算得過去。MacBook Pro 14 吋（M4 Pro）守第二，是需要持續專業效能者的升級選擇，螢幕更亮，跑重度影片跟程式有餘裕。這個月有趣的壓力來自 Windows 陣營，搭 Snapdragon X2 Elite 的 Zenbook A16 在部分續航跟能效測試上真的贏過 M5，它守第三，是最超值的全能機，輕薄機身配一塊出色的 OLED 面板。XPS 14 守第四，靠螢幕跟續航，Razer Blade 16 守第五，是純 GPU 掛帥時的效能選擇。Surface Pro 11、Spectre x360 跟入門 Acer 全部照舊。這週沒事件洗牌，所以我守住排名。多數人買 Air，要持續效能買 Pro，要 Windows 性價比買 Zenbook A16。",
     "highlights": [
       {"title": "MacBook Air M5 仍是多數人的筆電", "body": "M5 晶片效能遠超價格，無風扇設計安靜，續航撐過一整個工作天。蘋果把起售儲存翻倍到 512GB，性價比站得住，所以第一是它。"},
       {"title": "MacBook Pro 14 M4 Pro 是效能升級", "body": "它加上持續專業效能、更亮的螢幕、跑重度影片跟程式的餘裕。工作真的會操爆筆電的人，它就是自然的升級，穩坐第二。"},
       {"title": "Zenbook A16 是 Windows 性價比王", "body": "Snapdragon X2 Elite 在部分續航跟能效測試贏過 M5，配一塊好 OLED 面板加輕薄機身。這讓它成為最超值的全能機，第三實至名歸。"},
       {"title": "Razer Blade 16 是效能選擇", "body": "當純 GPU 火力就是全部任務，它端出輕薄機給不了的肌肉。要獨顯的遊戲跟創作工作流，它穩坐第五的專家選擇。"},
     ],
   })

# ---------------- best-e-readers ----------------
do("best-e-readers.json",
   [
     {"title": "Best ereaders in 2026: 9 top ebook readers from Kindle, Kobo and more", "url": "https://www.techradar.com/best/best-ereader", "source": "TechRadar"},
     {"title": "We Tested the Best E-readers of 2026", "url": "https://www.nbcnews.com/select/shopping/best-ereader-rcna203732", "source": "NBC Select"},
   ],
   {
     "commentary": "My e-reader board in June keeps the Kindle Paperwhite (2025) at number one, and that is still the easy call for most readers. The 7-inch 300ppi screen is sharp and easy on the eyes, the auto-adjusting warm light gets the reading temperature right without fuss, wireless charging is there, and the battery genuinely runs for weeks. Pair that with Amazon's library, which remains the deepest and most frictionless ebook ecosystem going, and it is the reader I hand to anyone who just wants to read. The Kobo Libra Colour holds second and is the one I steer people to when they want more. Its color E Ink screen, physical page-turn buttons and built-in note-taking deliver the best feature-per-dollar value on the board, and Kobo's open library support and Overdrive integration win for anyone who borrows from a public library. The Kindle Colorsoft stays third as Amazon's color answer, the pick when you want color pages without leaving the Kindle ecosystem. The Kobo Clara Colour, Boox Palma 2 and the rest of the compact field carry forward unchanged. Nothing this week reshuffled the order, so I held ranks. Buy the Paperwhite for the best all-round read, the Libra Colour for color and notes, the Colorsoft to stay in Kindle.",
     "highlights": [
       {"title": "Kindle Paperwhite is the best all-round reader", "body": "Its sharp 7-inch 300ppi screen, auto warm light, wireless charging and weeks of battery cover everything a reader needs. Paired with Amazon's deep library, it stays the easy number one for most people."},
       {"title": "Kobo Libra Colour is the best value", "body": "Its color E Ink screen, physical page-turn buttons and built-in notes deliver the most feature-per-dollar on the board. With open library and Overdrive support, it is the pick for library borrowers and a clear second."},
       {"title": "Kindle Colorsoft is Amazon's color answer", "body": "It brings color pages without leaving the Kindle ecosystem and its deep store integration. For readers who want color but stay loyal to Amazon, it holds a comfortable third."},
       {"title": "Boox Palma 2 is the pocket specialist", "body": "Its phone-sized form factor makes it the most portable E Ink reader on the board, ideal for one-handed reading anywhere. That niche keeps it firmly in the compact tier of this ranking."},
     ],
   },
   {
     "commentary": "6 月我的電子書閱讀器榜還是 Kindle Paperwhite（2025）排第一，對多數讀者這還是最好選的。7 吋 300ppi 螢幕銳利又護眼，自動調整的暖光不用你費心就把閱讀色溫弄對，有無線充電，電池真的能撐好幾週。再配上 Amazon 那個最深、最無痛的電子書生態，它就是我會丟給任何只想看書的人的那台。Kobo Libra Colour 守第二，是想要更多的人我會帶他去的選擇。彩色 E Ink 螢幕、實體翻頁鍵、內建手寫筆記，端出榜上最高的每塊錢功能價值，而且 Kobo 的開放書庫支援跟 Overdrive 整合，對會去公共圖書館借書的人是大贏。Kindle Colorsoft 守第三，是 Amazon 的彩色解答，想要彩色頁又不想離開 Kindle 生態時就選它。Kobo Clara Colour、Boox Palma 2 跟其他小尺寸機種全部照舊。這週沒事件洗牌，所以我守住排名。要最全面的閱讀體驗買 Paperwhite，要彩色跟筆記買 Libra Colour，想留在 Kindle 買 Colorsoft。",
     "highlights": [
       {"title": "Kindle Paperwhite 是最全面的閱讀器", "body": "銳利的 7 吋 300ppi 螢幕、自動暖光、無線充電、好幾週續航，讀者要的它都有。再配上 Amazon 深厚書庫，多數人第一名選它最輕鬆。"},
       {"title": "Kobo Libra Colour 是性價比王", "body": "彩色 E Ink 螢幕、實體翻頁鍵、內建筆記，端出榜上最高的每塊錢功能價值。加上開放書庫跟 Overdrive 支援，是借書族的選擇，穩坐第二。"},
       {"title": "Kindle Colorsoft 是 Amazon 的彩色解答", "body": "它帶來彩色頁又不用離開 Kindle 生態，書店整合又深。想要彩色又對 Amazon 死忠的讀者，它穩坐第三。"},
       {"title": "Boox Palma 2 是口袋專家", "body": "手機大小的尺寸讓它成為榜上最好攜帶的 E Ink 閱讀器，到哪都能單手讀。這個利基讓它穩穩待在這份榜單的小尺寸段。"},
     ],
   })

# ---------------- best-smart-watches ----------------
do("best-smart-watches.json",
   [
     {"title": "Best Smartwatch in 2026", "url": "https://www.goodpickr.com/guides/best-smartwatch-2026", "source": "GoodPickr"},
     {"title": "I ran a marathon with the Apple Watch Ultra 3 vs Garmin Fenix 8 Pro", "url": "https://www.tomsguide.com/wellness/smartwatches/i-just-ran-a-marathon-with-the-apple-watch-ultra-3-vs-garmin-fenix-8-pro-heres-the-winner", "source": "Tom's Guide"},
   ],
   {
     "commentary": "My smartwatch board in June keeps the Apple Watch Ultra 3 at number one, and it earns the spot as the most capable smartwatch ever made for an iPhone owner. The S10 chip drives a fast, fluid experience, the 36-hour battery (72 in low power) finally puts real endurance on an Apple watch, and the health stack now spans blood oxygen, ECG, temperature and blood pressure trend monitoring. At 799 dollars it is the ultimate wrist computer if you live in iOS. The Ultra 2 holds second as the value version of that same package for anyone who does not need the newest chip. The Garmin Fenix 8 stays third and is the one I hand to serious athletes: 48-plus hours of battery with GPS, up to 30 days in expedition mode, and the most accurate wrist heart rate and GPS tracking in the field, all of it working with iPhone and Android. For multi-day adventures and training depth, nothing here touches it. The Galaxy Watch 7 Ultra holds fourth as the best Android-first option, and the Apple Series 11 rounds out a strong top five for iPhone owners who want the everyday watch rather than the rugged one. The rest of the board carries forward. Nothing this week reshuffled the order, so I held ranks. Buy the Ultra 3 for iPhone, the Fenix 8 for serious sport.",
     "highlights": [
       {"title": "Apple Watch Ultra 3 is the best smartwatch for iPhone", "body": "The S10 chip drives a fluid experience, the 36-hour battery adds real endurance, and the health stack now covers blood pressure trends. At 799 dollars it is the ultimate iOS wrist computer, so it stays number one."},
       {"title": "Garmin Fenix 8 is the athlete's pick", "body": "It posts 48-plus hours with GPS, up to 30 days in expedition mode, and the most accurate wrist heart rate and GPS on the board. For multi-day adventures and deep training metrics, it stays a clear third."},
       {"title": "Apple Watch Ultra 2 is the value flagship", "body": "It delivers nearly the same rugged package as the Ultra 3 for anyone who does not need the newest chip. That makes it the smart second choice for iPhone owners watching the price."},
       {"title": "Galaxy Watch 7 Ultra leads Android", "body": "It is the best Android-first smartwatch on the board, pairing a bright display with strong health tracking and deep Samsung integration. For Galaxy users it holds a deserved fourth."},
     ],
   },
   {
     "commentary": "6 月我的智慧手錶榜還是 Apple Watch Ultra 3 排第一，對 iPhone 使用者來說它當之無愧是史上最強的智慧手錶。S10 晶片帶來快又順的體驗，36 小時續航（低耗電模式 72 小時）終於讓 Apple 手錶有真正的耐力，健康功能現在涵蓋血氧、心電圖、體溫跟血壓趨勢監測。售價約台幣兩萬四，活在 iOS 裡的話它就是終極的手腕電腦。Ultra 2 守第二，是同一套配置的性價比版，給不需要最新晶片的人。Garmin Fenix 8 守第三，是我會丟給認真運動者的那支，開 GPS 還有 48 小時以上續航、探險模式最多 30 天，手腕心率跟 GPS 追蹤是全場最準，而且 iPhone 跟 Android 都能用。要多日探險跟訓練深度，這裡沒東西碰得到它。Galaxy Watch 7 Ultra 守第四，是最好的 Android 優先選擇，Apple Series 11 撐起強勢的前五，給想要日常款而非三防款的 iPhone 使用者。其餘照舊。這週沒事件洗牌，所以我守住排名。iPhone 買 Ultra 3，認真運動買 Fenix 8。",
     "highlights": [
       {"title": "Apple Watch Ultra 3 是 iPhone 最強錶", "body": "S10 晶片帶來順暢體驗，36 小時續航加上真正耐力，健康功能現在涵蓋血壓趨勢。售價約台幣兩萬四，是終極 iOS 手腕電腦，所以第一是它。"},
       {"title": "Garmin Fenix 8 是運動者首選", "body": "開 GPS 有 48 小時以上續航、探險模式最多 30 天，手腕心率跟 GPS 全場最準。要多日探險跟深度訓練數據，它穩坐第三。"},
       {"title": "Apple Watch Ultra 2 是性價比旗艦", "body": "它端出跟 Ultra 3 幾乎一樣的三防配置，給不需要最新晶片的人。這讓它成為精打細算 iPhone 使用者的聰明第二選擇。"},
       {"title": "Galaxy Watch 7 Ultra 領銜 Android", "body": "它是榜上最好的 Android 優先智慧錶，亮螢幕配上紮實健康追蹤跟深度三星整合。Galaxy 使用者第四名實至名歸。"},
     ],
   })

# ---------------- best-smart-rings ----------------
do("best-smart-rings.json",
   [
     {"title": "Best smart ring 2026: From Oura and Samsung to other discreet fitness trackers", "url": "https://www.techradar.com/health-fitness/fitness-trackers/best-smart-ring", "source": "TechRadar"},
     {"title": "Best Smart Rings 2026: Oura vs Ultrahuman vs RingConn", "url": "https://foliumbiosciences.com/oura-vs-ultrahuman-vs-ringconn-best-smart-rings/", "source": "Folium Biosciences"},
   ],
   {
     "commentary": "The smart ring race in June is genuinely tight at the top, and I have the Galaxy Ring and Oura Ring 4 tied at 8.9 for a reason. I keep the Galaxy Ring at number one on value and integration: it is the lightest ring on the board at 2.3 to 3 grams, it gets the most out of a Galaxy phone, and crucially it carries no monthly subscription. If you already use a Samsung phone, this is the ring that just makes sense. The Oura Ring 4 sits right beside it and is still the gold standard for the data itself. Its sleep, stress and health tracking accuracy beats anything else I have tested and the app is the most polished in the category, so if sleep depth is the whole point and the 5.99-dollar monthly fee does not bother you, Oura remains the answer. The RingConn Gen 2 holds third and is the smart pick for anyone allergic to subscriptions, matching or beating Oura on battery with up to 10 days of life and no recurring cost. The Ultrahuman Ring PRO stays fourth for its metabolic and battery strengths, and the Ring Air, Circular Ring 2, Helio Ring and Evie Ring carry forward. Nothing this week reshuffled the order, so I held ranks. Buy the Galaxy Ring for Samsung value, Oura for the best data, RingConn for no subscription.",
     "highlights": [
       {"title": "Galaxy Ring wins on value and no subscription", "body": "It is the lightest ring on the board at 2.3 to 3 grams, pairs deeply with Galaxy phones, and charges no monthly fee. For Samsung owners who want insights without a subscription, it stays the number one pick."},
       {"title": "Oura Ring 4 is the data gold standard", "body": "Its sleep, stress and health tracking accuracy beats everything I have tested and the app is the most polished in the category. If sleep depth is the point and the fee is fine, it ties for the top spot."},
       {"title": "RingConn Gen 2 is the no-subscription pick", "body": "It matches or beats Oura on battery with up to 10 days of life and charges no recurring fee. For buyers allergic to monthly costs who still want solid tracking, it holds a deserved third."},
       {"title": "Ultrahuman Ring PRO leads on metabolic depth", "body": "Its metabolic insights and strong battery life make it the specialist choice for users focused on glucose and recovery data. That focus keeps it firmly in the top tier at fourth."},
     ],
   },
   {
     "commentary": "6 月的智慧戒指戰局頂端真的很貼身，我把 Galaxy Ring 跟 Oura Ring 4 並列 8.9 是有道理的。我把 Galaxy Ring 放第一，靠的是性價比跟整合，它是榜上最輕的戒指，2.3 到 3 克，跟 Galaxy 手機搭配發揮最大，而且關鍵是它沒有月費。如果你本來就用三星手機，這支戒指就是順理成章的選擇。Oura Ring 4 緊貼在旁，論數據本身它還是黃金標準。睡眠、壓力、健康追蹤的準確度贏過我測過的任何東西，App 也是類別裡最精緻的，所以如果睡眠深度就是重點、每月約台幣一百八的訂閱你不介意，Oura 還是答案。RingConn Gen 2 守第三，是對訂閱過敏者的聰明選擇，續航最多 10 天追平或贏過 Oura，又完全沒月費。Ultrahuman Ring PRO 守第四，靠代謝跟續航強項，Ring Air、Circular Ring 2、Helio Ring、Evie Ring 全部照舊。這週沒事件洗牌，所以我守住排名。三星性價比買 Galaxy Ring，要最好數據買 Oura，不想訂閱買 RingConn。",
     "highlights": [
       {"title": "Galaxy Ring 贏在性價比跟免訂閱", "body": "它是榜上最輕的戒指，2.3 到 3 克，跟 Galaxy 手機深度搭配，而且沒有月費。想要洞察又不想訂閱的三星使用者，它穩坐第一。"},
       {"title": "Oura Ring 4 是數據黃金標準", "body": "睡眠、壓力、健康追蹤的準確度贏過我測過的一切，App 也是類別裡最精緻的。睡眠深度就是重點、月費也 OK 的話，它並列榜首。"},
       {"title": "RingConn Gen 2 是免訂閱選擇", "body": "續航最多 10 天追平或贏過 Oura，又完全沒有月費。對月費過敏又想要紮實追蹤的買家，它穩坐第三實至名歸。"},
       {"title": "Ultrahuman Ring PRO 主打代謝深度", "body": "代謝洞察加上強勁續航，讓它成為專注血糖跟恢復數據者的專家選擇。這份專注讓它穩穩待在第四的上段。"},
     ],
   })

# ---------------- best-smart-glasses ----------------
do("best-smart-glasses.json",
   [
     {"title": "Ray-Ban Meta AI glasses Gen 2 & Gen 1", "url": "https://www.ray-ban.com/usa/ray-ban-meta-ai-glasses", "source": "Ray-Ban"},
     {"title": "Every Smart Glasses Design Tells You Who They're Chasing", "url": "https://the-gadgeteer.com/2026/05/25/smart-glasses-2026-design-strategy/", "source": "The Gadgeteer"},
   ],
   {
     "commentary": "My smart glasses board in June keeps the Ray-Ban Meta (Gen 2) at number one because it is still the pair that gets the everyday formula right. The Llama 4 integration makes Meta AI genuinely useful for hands-free questions, calls and texts, and the Gen 2 added 42 percent more battery capacity for up to five hours of music or voice calls. It looks like normal Ray-Bans, costs far less than the display models, and that combination of style, price and a camera that just works keeps it the default I recommend. The Oakley Meta HSTN holds second as the sportier sibling, the same proven Meta platform in a frame built for active wear, which is the pick for runners and cyclists. The Meta Ray-Ban Display stays third and is the only serious display-equipped option you can buy today, with its in-lens screen and Neural Band wristband control, but at 799 dollars with weaker battery it is still the early-adopter choice rather than the everyday one. The XREAL One Pro holds fourth as the best media-viewing AR glasses, and the Oakley Meta Vanguard and XREAL One round out a strong upper tier. Even Realities G1, the Solos and RayNeo entries carry forward. Nothing this week reshuffled the order, so I held ranks. Buy the Ray-Ban Meta for everyday, the Display for AR, XREAL for big-screen viewing.",
     "highlights": [
       {"title": "Ray-Ban Meta Gen 2 nails the everyday formula", "body": "Llama 4 makes Meta AI genuinely useful, the Gen 2 added 42 percent more battery for up to five hours of use, and it looks like normal Ray-Bans. That style, price and camera combo keeps it number one."},
       {"title": "Meta Ray-Ban Display is the only real AR pick", "body": "Its in-lens screen and Neural Band wristband control make it the only serious display-equipped option you can buy today. At 799 dollars with weaker battery it is the early-adopter choice, holding third."},
       {"title": "Oakley Meta HSTN is the sport pick", "body": "It brings the proven Meta platform in a frame built for active wear, ideal for runners and cyclists. That athletic focus on the same strong software keeps it a clear second."},
       {"title": "XREAL One Pro owns big-screen viewing", "body": "Its display glasses deliver the best private big-screen media experience on the board, ideal for travel and gaming. For viewing rather than AI assistance, it stays the specialist pick at fourth."},
     ],
   },
   {
     "commentary": "6 月我的智慧眼鏡榜還是 Ray-Ban Meta（Gen 2）排第一，因為它依然是把日常公式做對的那副。Llama 4 整合讓 Meta AI 在免手操作問問題、打電話、傳訊息上真的好用，Gen 2 又加了 42% 電池容量，音樂或語音通話最多撐五小時。它長得就像普通 Ray-Ban，價格遠低於有顯示器的型號，這種風格、價格加上一個真的能用的相機的組合，讓它穩坐我推薦的預設選擇。Oakley Meta HSTN 守第二，是運動版兄弟，同樣成熟的 Meta 平台裝進為運動打造的鏡框，是跑者跟單車族的選擇。Meta Ray-Ban Display 守第三，是你今天買得到唯一認真的顯示器款，鏡片內螢幕加 Neural Band 腕帶操控，但售價約台幣兩萬四、電池又較弱，還是早期採用者的選擇而非日常款。XREAL One Pro 守第四，是最好的影音觀看 AR 眼鏡，Oakley Meta Vanguard 跟 XREAL One 撐起強勢上段。Even Realities G1、Solos 跟 RayNeo 全部照舊。這週沒事件洗牌，所以我守住排名。日常買 Ray-Ban Meta，要 AR 買 Display，要大螢幕觀看買 XREAL。",
     "highlights": [
       {"title": "Ray-Ban Meta Gen 2 把日常公式做對", "body": "Llama 4 讓 Meta AI 真的好用，Gen 2 加了 42% 電池最多撐五小時，外觀就像普通 Ray-Ban。這種風格、價格加相機的組合讓它穩坐第一。"},
       {"title": "Meta Ray-Ban Display 是唯一認真 AR 款", "body": "鏡片內螢幕加 Neural Band 腕帶操控，是你今天買得到唯一認真的顯示器款。售價約台幣兩萬四、電池較弱，是早期採用者選擇，守第三。"},
       {"title": "Oakley Meta HSTN 是運動選擇", "body": "它把成熟的 Meta 平台裝進為運動打造的鏡框，跑者跟單車族很適合。同樣強的軟體加上運動取向，讓它穩坐第二。"},
       {"title": "XREAL One Pro 主宰大螢幕觀看", "body": "它的顯示器眼鏡端出榜上最好的私人大螢幕影音體驗，旅行跟遊戲很適合。要觀看而非 AI 助理，它穩坐第四的專家選擇。"},
     ],
   })

print("ALL DONE")
