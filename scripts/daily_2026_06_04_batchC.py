import sys; sys.path.insert(0, "/Users/etrexkuo/toprankland/scripts")
from daily_helper import load, save, upsert, last_rankings, DATE

entries = {}

# ---------------- FOLDABLE SMARTPHONES ----------------
entries["best-foldable-smartphones.json"] = {
  "references": [
    {"title": "Best foldable phones of 2026", "url": "https://www.tomsguide.com/best-picks/best-foldable-phones", "source": "Tom's Guide"},
    {"title": "The best foldable phones of 2026: All the top Flips and Folds", "url": "https://www.androidauthority.com/the-best-foldable-phones-3550058/", "source": "Android Authority"},
  ],
  "en": {
    "commentary": "Heading into June 2026 my foldable order is steady, and the Galaxy Z Fold 7 keeps the crown because it is the most refined book-style foldable on sale. Closed it measures barely thicker than a pair of stacked slab phones, it runs the Snapdragon 8 Elite for Galaxy, and that 200MP main camera is the sharpest shooter on any folding device right now. The Pixel 10 Pro Fold stays a very close second and it earns that spot on substance. It carries an IP68 rating, a first for a notebook-style fold, its inner panel is brighter than the Samsung, and battery life runs longer in day-to-day use while landing about 200 dollars cheaper at equivalent storage. That value gap is the reason Google keeps pressure on Samsung. Oppo Find N5 holds third as the slimmest large fold with the best open-flat feel, and Honor Magic V3 and Vivo X Fold 5 round out the import-heavy upper tier for buyers who import. On the flip side, the Galaxy Z Flip 7 remains the clamshell to beat for its cover-screen usability and clean One UI experience, with the Motorola Razr Ultra 2026 right behind as the style pick. This week the recurring theme across the roundups is that foldables have crossed from novelty into mainstream consideration, with three credible book-style options and several strong clamshells. Nothing shipped in the past seven days that forces a reshuffle, so I am carrying the order forward. If you want the most camera and polish, buy the Fold 7. If you want durability and battery for less money, the Pixel 10 Pro Fold is the smarter spend.",
    "highlights": [
      {"title": "Galaxy Z Fold 7 leads on polish", "body": "Barely thicker than a slab phone when shut, Snapdragon 8 Elite for Galaxy, and a 200MP main camera that out-shoots every rival fold."},
      {"title": "Pixel 10 Pro Fold is the value play", "body": "IP68 rating, a brighter inner display, longer real-world battery, and roughly 200 dollars cheaper at matched storage."},
      {"title": "Clamshell crown stays Samsung", "body": "The Galaxy Z Flip 7 keeps the best cover-screen flow and cleanest software, with the Razr Ultra 2026 as the style alternative."},
      {"title": "Mainstream moment", "body": "June roundups frame foldables as mainstream now, with three credible book folds and several strong flips to choose from."},
    ],
  },
  "zh-tw": {
    "commentary": "進到 2026 年 6 月，我的摺疊機排序很穩，三星 Galaxy Z Fold 7 繼續坐冠軍寶座，因為它就是目前最成熟的書本式摺疊機。闔起來幾乎跟兩支直板機疊起來差不多薄，跑的是 Snapdragon 8 Elite for Galaxy，那顆 2 億畫素主鏡頭也是現在所有摺疊機裡最銳利的。Pixel 10 Pro Fold 緊咬在第二，這名次是靠實力拿的。它有 IP68 防水防塵，這在書本式摺疊機裡是頭一個，內螢幕比三星更亮，日常續航更持久，同容量還便宜大概台幣六千上下，這個價差就是 Google 一直能壓著三星打的原因。Oppo Find N5 守住第三，是最薄、攤平手感最好的大摺,Honor Magic V3 跟 Vivo X Fold 5 則撐住水貨族群的上半段。翻蓋這邊，Galaxy Z Flip 7 還是最值得買的小摺，外螢幕好用、One UI 乾淨,Motorola Razr Ultra 2026 緊追在後當潮流選擇。這週各家評測一直在講同一件事，摺疊機已經從嚐鮮玩具變成主流選項了，光書本式就有三台能打,翻蓋也有好幾台不錯。過去七天沒有出什麼大事需要重排，所以我把名次照搬。想要最強相機跟質感就買 Fold 7,想要耐用、續航又省錢，Pixel 10 Pro Fold 更划算。",
    "highlights": [
      {"title": "Z Fold 7 質感稱王", "body": "闔起幾乎跟直板機一樣薄，Snapdragon 8 Elite for Galaxy，2 億畫素主鏡頭拍照贏過所有對手摺疊機。"},
      {"title": "Pixel 10 Pro Fold 主打划算", "body": "IP68 防護、內螢幕更亮、日常續航更久，同容量還便宜約台幣六千。"},
      {"title": "翻蓋還是三星天下", "body": "Galaxy Z Flip 7 外螢幕最好用、軟體最乾淨，Razr Ultra 2026 則是潮流替代款。"},
      {"title": "進入主流時代", "body": "6 月評測都把摺疊機視為主流選項，光書本式就有三台能打，翻蓋也有好幾台可選。"},
    ],
  },
}

# ---------------- SMART WATCHES ----------------
entries["best-smart-watches.json"] = {
  "references": [
    {"title": "The best smartwatch 2026", "url": "https://www.techradar.com/news/wearables/best-smart-watches-what-s-the-best-wearable-tech-for-you-1154074", "source": "TechRadar"},
    {"title": "The best smartwatches for Android lovers in 2026", "url": "https://www.phonearena.com/news/best-android-smartwatch_id134203", "source": "PhoneArena"},
  ],
  "en": {
    "commentary": "In early June 2026 my smartwatch order holds, and the Apple Watch Ultra 3 stays on top because it is the most complete watch you can wear with an iPhone. The brightest panel Apple ships, roughly 60 hours of battery in the right mode, rugged titanium, and the deepest app library on any wrist keep it ahead. For most iPhone owners the Series 11 remains the smarter buy and it sits high for that reason, since you get the headline health features, now including AI-driven insights and glucose trend estimates, in a lighter, cheaper case. The Garmin Fenix 8 stays firmly in my top three because nobody touches it on endurance, multi-week battery and training-load analysis change how you live with a watch and you simply stop thinking about charging. The Garmin Venu X1 keeps climbing in reviewer favor as the sport pick this week, praised as the best-looking and most comfortable watch Garmin has built while still delivering up to five days with the always-on display lit. On the Android side the Galaxy Watch 8 and its Ultra sibling are the obvious choice, with smoother software, expanded Galaxy AI features, and a bright AMOLED panel, and the Pixel Watch 4 gives the cleanest Wear OS experience. The recurring story in this week's roundups is the ecosystem split, Garmin owns battery and endurance while Apple owns app depth and AI health, and my ranking mirrors that. Nothing launched in the past seven days that changes the math, so I carry the order forward unchanged.",
    "highlights": [
      {"title": "Apple Watch Ultra 3 stays No. 1", "body": "Brightest Apple display, about 60 hours of battery in the right mode, titanium build, and the deepest app library on any wrist."},
      {"title": "Series 11 is the value iPhone pick", "body": "Headline health features now include AI insights and glucose trend estimates in a lighter, cheaper case."},
      {"title": "Garmin owns endurance", "body": "The Fenix 8 delivers multi-week battery and training-load analysis, so charging stops being a daily chore."},
      {"title": "Best Android choice", "body": "Galaxy Watch 8 brings smoother software, expanded Galaxy AI, and a bright AMOLED panel, with Pixel Watch 4 the cleanest Wear OS."},
    ],
  },
  "zh-tw": {
    "commentary": "2026 年 6 月初，我的智慧手錶排序維持不變，Apple Watch Ultra 3 繼續居首，因為配 iPhone 用它就是最完整的一支。蘋果最亮的螢幕、特定模式下大約 60 小時續航、堅固的鈦金屬機身，再加上手腕上最豐富的 App 生態，這些優勢讓它穩坐第一。不過對大多數 iPhone 用戶來說，Series 11 才是更聰明的選擇，所以它排很前面，因為你能用更輕、更便宜的機身拿到主打的健康功能，現在還多了 AI 健康洞察跟血糖趨勢估測。Garmin Fenix 8 穩穩待在前三，續航沒人比得過，數週電力加上訓練負荷分析會徹底改變你用錶的方式，你會直接忘記什麼叫充電。Garmin Venu X1 這週在評測裡人氣繼續往上爬，被誇是 Garmin 做過最好看、最舒服的一支，開著常亮螢幕還能撐到五天，是運動取向的首選。Android 這邊，Galaxy Watch 8 跟 Ultra 版是理所當然的選擇，軟體更順、Galaxy AI 功能更多、AMOLED 螢幕又亮，Pixel Watch 4 則提供最乾淨的 Wear OS 體驗。這週評測一直在講生態系分流，Garmin 拿下續航跟耐力，蘋果掌握 App 深度跟 AI 健康，我的排名就反映這件事。過去七天沒出什麼會翻盤的大事，所以名次照搬。",
    "highlights": [
      {"title": "Ultra 3 穩居第一", "body": "蘋果最亮螢幕、特定模式約 60 小時續航、鈦金屬機身，外加手腕上最豐富的 App 生態。"},
      {"title": "Series 11 是 iPhone 划算選", "body": "主打健康功能現在還含 AI 洞察與血糖趨勢估測，裝在更輕更便宜的機身裡。"},
      {"title": "Garmin 續航無敵", "body": "Fenix 8 提供數週電力與訓練負荷分析，充電不再是每天的事。"},
      {"title": "Android 最佳選擇", "body": "Galaxy Watch 8 軟體更順、Galaxy AI 更多、螢幕更亮，Pixel Watch 4 則是最乾淨的 Wear OS。"},
    ],
  },
}

# ---------------- SMART RINGS ----------------
entries["best-smart-rings.json"] = {
  "references": [
    {"title": "Best smart ring 2026: From Oura and Samsung to other discreet trackers", "url": "https://www.techradar.com/health-fitness/fitness-trackers/best-smart-ring", "source": "TechRadar"},
    {"title": "Samsung Galaxy Ring vs. Oura Ring 4", "url": "https://www.tomsguide.com/wellness/fitness-trackers/samsung-galaxy-ring-vs-oura-ring-everything-we-know-so-far", "source": "Tom's Guide"},
  ],
  "en": {
    "commentary": "In June 2026 the smart-ring race is genuinely competitive, and that is why my top two sit so close. The Samsung Galaxy Ring holds the top spot for Galaxy owners because it is the ring that gets the most out of a phone you already carry. It feeds Samsung Health, and if you also wear a Galaxy Watch the two coordinate so the ring tracks at night while the watch tracks workouts, and the app stops double-counting. Just as important, there is no subscription, so every feature is yours out of the box. The Oura Ring 4 stays tied at the top for sleep, and this week's roundups still call it the deepest sleep tracker on the market, the answer if rest is your priority and the 5.99-a-month membership does not bother you. RingConn Gen 2 holds third as the best subscription-free all-rounder with genuinely long battery, and the Ultrahuman Ring AIR keeps its spot as the no-fee wellness alternative. The clear message in the latest coverage is that Oura is no longer the default, there are at least three rings that beat it on a single measurable axis, whether that is price, battery, or cross-phone support. Nothing in the past seven days forces a rank change, so I am carrying the order forward. Pick the Galaxy Ring on a Samsung phone, pick Oura if sleep depth rules everything, and pick RingConn if you want strong tracking with no recurring fee.",
    "highlights": [
      {"title": "Galaxy Ring wins for Samsung users", "body": "Deep Samsung Health integration, watch-and-ring coordination that stops double-counting, and zero subscription."},
      {"title": "Oura Ring 4 still owns sleep", "body": "This week's roundups call it the deepest sleep tracker, ideal if rest is your priority and the 5.99-a-month fee is fine."},
      {"title": "RingConn Gen 2 is the no-fee all-rounder", "body": "Long battery and solid tracking across phones with no recurring membership cost."},
      {"title": "Oura is no longer the default", "body": "Coverage notes at least three rings now beat Oura on a single axis, be it price, battery, or cross-phone support."},
    ],
  },
  "zh-tw": {
    "commentary": "2026 年 6 月，智慧戒指的競爭是真的激烈，所以我前兩名才會貼這麼近。Samsung Galaxy Ring 對 Galaxy 用戶來說守住第一，因為它最能把你手上那支手機的價值榨出來。它直接餵資料給 Samsung Health，如果你同時戴 Galaxy Watch，兩個裝置還會協調，晚上戒指追蹤睡眠、白天手錶追蹤運動，App 也不會重複計算。更重要的是，它完全不用訂閱，所有功能開箱即用。Oura Ring 4 在睡眠這塊跟它並列頂端，這週的評測還是把它捧成市面上最深度的睡眠追蹤，如果睡眠是你最在意的、又不介意每月台幣兩百左右的會員費，那它就是答案。RingConn Gen 2 守第三，是最棒的免訂閱全能款，續航真的長，Ultrahuman Ring AIR 則繼續當不用月費的健康替代選擇。最新報導講得很清楚，Oura 已經不是預設首選了，至少有三款戒指在某個可量化的點上贏過它，不管是價格、續航還是跨手機支援。過去七天沒有逼我換名次的事，所以照搬。用三星手機就選 Galaxy Ring，睡眠至上就選 Oura，想要好追蹤又不想付月費就選 RingConn。",
    "highlights": [
      {"title": "三星用戶選 Galaxy Ring", "body": "深度整合 Samsung Health，戒指手錶協調不重複計算，而且完全免訂閱。"},
      {"title": "Oura Ring 4 睡眠仍最強", "body": "這週評測仍稱它睡眠追蹤最深，適合最在意睡眠、不介意每月約台幣兩百會員費的人。"},
      {"title": "RingConn Gen 2 免月費全能", "body": "續航長、追蹤扎實，跨手機可用，沒有任何月費。"},
      {"title": "Oura 不再是預設首選", "body": "報導指出至少三款戒指在某個可量化點上贏過 Oura，無論價格、續航或跨手機支援。"},
    ],
  },
}

# ---------------- SMART GLASSES ----------------
entries["best-smart-glasses.json"] = {
  "references": [
    {"title": "Best Smart Glasses 2026: Top AI and AR picks for Every Budget", "url": "https://the-gadgeteer.com/2026/05/28/best-smart-glasses-2026/", "source": "The Gadgeteer"},
    {"title": "Meta Ray-Ban Display and Neural Band", "url": "https://www.meta.com/ai-glasses/meta-ray-ban-display/", "source": "Meta"},
  ],
  "en": {
    "commentary": "In early June 2026 my smart-glasses ranking holds, and the second-gen Ray-Ban Meta keeps the lead because it is the only AI-glass family that consistently passes as ordinary eyewear. The on-frame camera shoots up to 3K Ultra HD video, the Meta AI button answers questions about whatever you are looking at, and the fit and weight are good enough that people forget they are wearing a computer. The Oakley Meta HSTN holds second as the sportier, sweat-friendly take on the same platform. The Meta Ray-Ban Display sits third and remains the most interesting pure-display play, its in-lens screen paired with the EMG Neural Band gives you a viewfinder, a 12MP camera with 3X zoom, and two-way video calls right on your face. The recurring story this week is that the field is finally getting a real fight, Google, Samsung, Warby Parker, and Gentle Monster jointly previewed the first Android XR reference glasses, and Meta with EssilorLuxottica rolled out new prescription-first frames across LensCrafters, so the prescription path is wider than ever. On the AR display side the Xreal One Pro stays my travel pick for head-tracked virtual screens, with the Viture leaning into raw image quality. None of this week's announcements ship a product that beats the current leaders, so I am carrying the order forward. Buy Ray-Ban Meta Gen 2 for everyday capture and AI, step up to the Display model if you want an in-lens screen, and grab the Xreal One Pro for big private screens on the move.",
    "highlights": [
      {"title": "Ray-Ban Meta Gen 2 leads", "body": "The only AI glasses that pass as normal eyewear, with up to 3K video capture and a Meta AI button for live answers."},
      {"title": "Display model is the screen play", "body": "An in-lens display plus the EMG Neural Band adds a viewfinder, 12MP camera with 3X zoom, and two-way video calls."},
      {"title": "Android XR enters the fight", "body": "Google, Samsung, Warby Parker, and Gentle Monster previewed the first Android XR reference glasses this week."},
      {"title": "Xreal One Pro for big screens", "body": "Stays the travel pick for head-tracked virtual displays, with Viture chasing raw image quality."},
    ],
  },
  "zh-tw": {
    "commentary": "2026 年 6 月初，我的智慧眼鏡排名維持不變，第二代 Ray-Ban Meta 繼續領先，因為它是唯一一個能穩定偽裝成普通眼鏡的 AI 眼鏡家族。鏡框上的相機能錄到 3K Ultra HD 影片，按下 Meta AI 鍵就能問你眼前看到的東西，配戴感跟重量也做得夠好，戴上去久了會忘記臉上掛著一台電腦。Oakley Meta HSTN 守第二，是同平台上更運動、更耐汗的版本。Meta Ray-Ban Display 排第三，仍是最有看頭的純顯示路線，鏡片內嵌螢幕搭配 EMG 神經手環，臉上就有取景器、12MP 加 3 倍變焦相機，還能雙向視訊。這週的重點是這個領域終於要打真正的仗了，Google、三星、Warby Parker 跟 Gentle Monster 聯手預覽了首批 Android XR 參考眼鏡，Meta 跟 EssilorLuxottica 也在 LensCrafters 鋪了主打度數的新鏡框，配度數的路比以前更寬了。AR 顯示這邊，Xreal One Pro 還是我的旅行首選，能投出頭部追蹤的虛擬大螢幕，Viture 則主打畫質。這週的發表沒有任何一款產品能贏過現任領頭羊，所以名次照搬。日常拍攝跟 AI 就買 Ray-Ban Meta Gen 2，想要鏡片內螢幕就升級 Display 版，移動中想看私人大螢幕就拿 Xreal One Pro。",
    "highlights": [
      {"title": "Ray-Ban Meta Gen 2 領先", "body": "唯一能偽裝成普通眼鏡的 AI 眼鏡，可錄 3K 影片，Meta AI 鍵即時回答眼前問題。"},
      {"title": "Display 版主打螢幕", "body": "鏡片內嵌螢幕加 EMG 神經手環，臉上就有取景器、12MP 加 3 倍變焦相機與雙向視訊。"},
      {"title": "Android XR 加入戰局", "body": "Google、三星、Warby Parker 與 Gentle Monster 這週聯手預覽首批 Android XR 參考眼鏡。"},
      {"title": "Xreal One Pro 投大螢幕", "body": "仍是旅行首選，能投出頭部追蹤的虛擬大螢幕，Viture 則主打畫質。"},
    ],
  },
}

# ---------------- WIRELESS EARBUDS ----------------
entries["best-wireless-earbuds.json"] = {
  "references": [
    {"title": "The 7 Best Wireless Earbuds of 2026", "url": "https://www.rtings.com/headphones/reviews/best/wireless-earbuds", "source": "RTINGS"},
    {"title": "The best wireless earbuds of 2026: Lab-tested by experts", "url": "https://www.soundguys.com/best-wireless-earbuds-2-14313/", "source": "SoundGuys"},
  ],
  "en": {
    "commentary": "As of June 2026 the Sony WF-1000XM6 stays my top pick because it is the most complete wireless earbud package on the market. Lab testing puts it at roughly 88 percent average noise reduction across frequencies with a 4.8 out of 5 sound score, and the new eight-mic array, up from six on the XM5, gives the AI beamforming far more data to clean up your voice on calls. Battery overdelivered too, nearly nine hours and forty minutes in one charge in testing against a 24-hour case total. The AirPods Pro 3 hold a strong second and the case for them is real, they measure the highest noise attenuation tested at around 90 percent, add heart-rate sensing, and undercut the Sony on price, so for iPhone owners they are often the smarter buy. The Bose QuietComfort Earbuds gen 2 stay third for the most comfortable fit and the most natural ANC, and the Samsung Galaxy Buds4 Pro round out the top tier as the obvious choice on a Galaxy phone. The honest summary this week is that the gap between the top three is small and largely down to ecosystem and price rather than raw capability. Nothing shipped in the past seven days that changes the order, so I am carrying it forward. Buy the XM6 for the best all-round package, the AirPods Pro 3 if you live on iPhone and want the tightest ANC, and the Bose if comfort is everything.",
    "highlights": [
      {"title": "Sony WF-1000XM6 leads overall", "body": "About 88 percent average noise reduction, a 4.8 sound score, and an eight-mic array that sharpens call clarity."},
      {"title": "AirPods Pro 3 for iPhone", "body": "Highest measured attenuation near 90 percent, heart-rate sensing, and a lower price make them the smart iPhone pick."},
      {"title": "Bose for comfort", "body": "QuietComfort Earbuds gen 2 keep the most comfortable fit and the most natural-sounding noise cancellation."},
      {"title": "Tight at the top", "body": "The top three are separated by ecosystem and price more than raw capability, so match the buds to your phone."},
    ],
  },
  "zh-tw": {
    "commentary": "到 2026 年 6 月，Sony WF-1000XM6 還是我的首選，因為它是市面上最完整的真無線耳機。實驗室測試顯示它跨頻段平均降噪大約 88%，音質拿到 4.8 分（滿分 5），全新的八麥克風陣列比 XM5 的六顆更多，讓 AI 波束成形有更多資料把你通話時的人聲清乾淨。續航也超出預期，實測單次接近 9 小時 40 分，搭配充電盒總共 24 小時。AirPods Pro 3 穩坐第二，理由很實在，它測到的降噪是全場最高、大約 90%，還多了心率偵測，價格又比 Sony 便宜，所以對 iPhone 用戶來說常常是更聰明的選擇。Bose QuietComfort Earbuds 二代守第三，配戴最舒服、降噪最自然，Samsung Galaxy Buds4 Pro 則撐住第一梯隊，是 Galaxy 手機用戶的當然之選。這週老實講，前三名的差距很小，主要是生態系跟價格在分高下，不是實力差。過去七天沒有東西改變排序，所以照搬。想要最全面就買 XM6，活在 iPhone 又想要最緊的降噪就選 AirPods Pro 3，舒適至上就選 Bose。",
    "highlights": [
      {"title": "Sony WF-1000XM6 整體第一", "body": "平均降噪約 88%、音質 4.8 分，八麥克風陣列讓通話人聲更清晰。"},
      {"title": "AirPods Pro 3 配 iPhone", "body": "降噪測得全場最高約 90%，加上心率偵測與更低價格，是 iPhone 聰明選。"},
      {"title": "Bose 主打舒適", "body": "QuietComfort Earbuds 二代配戴最舒服，降噪聽感最自然。"},
      {"title": "前段差距很小", "body": "前三名主要靠生態系與價格分高下，建議依手機選耳機。"},
    ],
  },
}

# ---------------- NOISE CANCELLING HEADPHONES ----------------
entries["best-noise-cancelling-headphones.json"] = {
  "references": [
    {"title": "The 5 Best Noise Cancelling Headphones of 2026", "url": "https://www.rtings.com/headphones/reviews/best/by-feature/noise-cancelling", "source": "RTINGS"},
    {"title": "Sony WH-1000XM6 vs Bose QuietComfort Ultra 2, tested for 6 months", "url": "https://www.tomsguide.com/audio/headphones/i-tested-the-sony-wh-1000xm6-vs-bose-quietcomfort-ultra-2-for-6-months-and-theres-a-clear-winner", "source": "Tom's Guide"},
  ],
  "en": {
    "commentary": "In June 2026 the Sony WH-1000XM6 stays my number one over-ear because it wins on the widest set of axes. RTINGS still rates it the best noise-cancelling headphone tested, and after a six-month head-to-head against the Bose, the Sony comes out ahead thanks to a 10-band EQ versus Bose's three bands, more noise-cancelling modes, and 30 hours of battery to Bose's 24. The QN3 processor and 12-mic array do the heavy lifting on isolation, and the sound is supremely customizable. The Bose QuietComfort Ultra Headphones hold a clear second and they deserve it, the cancellation is still best-in-class for sheer quiet, the new spatial audio mode is genuinely fun, and the fit stays the most comfortable in the category. Sennheiser's Momentum 4 keeps third for the warmest tuning and marathon battery, with the new HDB 630 right behind. Apple's AirPods Max remain the pick for deep iPhone integration despite their age. The recurring note in this week's coverage is that value models have closed the gap, the JBL Live 780NC delivers a lot of the experience for far less. Nothing launched in the past seven days that reorders the top, so I am carrying it forward. Buy the XM6 for the best all-rounder, the Bose for comfort and pure quiet, and the Momentum 4 if you want warmth and the longest battery.",
    "highlights": [
      {"title": "Sony WH-1000XM6 stays No. 1", "body": "A 10-band EQ, more ANC modes, and 30 hours of battery win the six-month head-to-head against Bose."},
      {"title": "Bose for comfort and quiet", "body": "QuietComfort Ultra keeps best-in-class isolation, a fun spatial mode, and the most comfortable fit."},
      {"title": "Sennheiser Momentum 4 for warmth", "body": "Warmest tuning and marathon battery hold third, with the new HDB 630 close behind."},
      {"title": "Value has closed the gap", "body": "Coverage highlights the JBL Live 780NC delivering much of the flagship experience for far less money."},
    ],
  },
  "zh-tw": {
    "commentary": "2026 年 6 月，Sony WH-1000XM6 還是我心中第一的罩耳式耳機，因為它在最多面向上都贏。RTINGS 仍把它評為測過降噪最強的耳機，而且經過六個月跟 Bose 的對決，Sony 勝出，靠的是 10 段 EQ（Bose 只有 3 段）、更多降噪模式，還有 30 小時續航對上 Bose 的 24 小時。QN3 處理器加 12 麥克風陣列扛起隔音重任，音色又能高度自訂。Bose QuietComfort Ultra 穩坐第二，這名次它當之無愧，論純粹的安靜，它的降噪仍是同級頂尖，新的空間音效模式也真的好玩，配戴感更是這個級距最舒服的。Sennheiser Momentum 4 守第三，音色最暖、續航超長，新的 HDB 630 緊追在後。蘋果 AirPods Max 雖然推出有些時間了，仍是 iPhone 深度整合的首選。這週報導一直提到一件事，平價款已經把差距追上來了，JBL Live 780NC 用低很多的價格給你大部分的體驗。過去七天沒有東西重排前段，所以照搬。要最全面就買 XM6，要舒適跟純粹安靜就選 Bose，想要暖聲跟最長續航就選 Momentum 4。",
    "highlights": [
      {"title": "Sony WH-1000XM6 穩居第一", "body": "10 段 EQ、更多降噪模式與 30 小時續航，贏下與 Bose 的六個月對決。"},
      {"title": "Bose 主打舒適與安靜", "body": "QuietComfort Ultra 隔音同級頂尖，空間音效好玩，配戴最舒服。"},
      {"title": "Sennheiser Momentum 4 暖聲", "body": "音色最暖、續航超長守第三，新款 HDB 630 緊追在後。"},
      {"title": "平價追上差距", "body": "報導指出 JBL Live 780NC 用低很多的價格給你大部分旗艦體驗。"},
    ],
  },
}

# ---------------- BLUETOOTH SPEAKERS ----------------
entries["best-bluetooth-speakers.json"] = {
  "references": [
    {"title": "The best Bluetooth speakers 2026: Which should you buy?", "url": "https://www.soundguys.com/best-bluetooth-speakers-2488/", "source": "SoundGuys"},
    {"title": "Best Bluetooth speakers 2026: tried and tested for every budget", "url": "https://www.whathifi.com/best-buys/best-bluetooth-speakers-portable-speakers-for-every-budget", "source": "What Hi-Fi?"},
  ],
  "en": {
    "commentary": "Heading into June 2026 the JBL Charge 6 keeps my top spot because it balances sound, durability, and battery better than anything else I have tested. It runs 24 hours, adds four more with Playtime Boost, doubles as a power bank for your phone, and now carries lossless audio over USB-C so it pulls double duty as a desk speaker for FLAC streaming. That blend of range is why it stays the pick for most people. The Marshall Emberton III holds second for its retro looks and genuinely room-filling sound from a compact body, and the Bose SoundLink Max stays third as the premium choice, with the newer SoundLink Plus and SoundLink Micro 2nd Gen fleshing out the Bose range this year. The recurring theme in this week's roundups is that JBL has been busy, the new Go 5 and Xtreme 5 both landed strong reviews, but neither displaces the Charge 6 as the all-rounder. For louder outdoor duty the UE Hyperboom and JBL Boombox 4 remain the party picks, and the Sonos Move 2 stays the choice if you want a portable that folds into a whole-home system. Nothing in the past seven days reorders the top, so I am carrying it forward. Buy the Charge 6 for the best balance, the Emberton III for style and sound per liter, and the SoundLink Max if budget is no object.",
    "highlights": [
      {"title": "JBL Charge 6 stays No. 1", "body": "24 hours of battery plus four with Playtime Boost, power-bank duty, and lossless USB-C audio make it the all-rounder."},
      {"title": "Marshall Emberton III for style", "body": "Retro looks and room-filling sound from a compact body keep it in second."},
      {"title": "Bose SoundLink Max is the premium pick", "body": "Top-tier sound, with the SoundLink Plus and Micro 2nd Gen rounding out the Bose lineup this year."},
      {"title": "JBL has been busy", "body": "The new Go 5 and Xtreme 5 earned strong reviews, though neither unseats the Charge 6 as the all-rounder."},
    ],
  },
  "zh-tw": {
    "commentary": "進到 2026 年 6 月，JBL Charge 6 守住我的第一，因為論音質、耐用度跟續航的平衡，我測過沒有比它更好的。它能撐 24 小時，開 Playtime Boost 再加四小時，還能當行動電源幫手機充電，現在更支援 USB-C 無損音訊，所以放桌上串流 FLAC 也能兼差當桌面喇叭。就是這種全面性，讓它穩坐多數人首選。Marshall Emberton III 守第二，復古外型加上小機身竟能塞滿整個房間的聲音。Bose SoundLink Max 守第三，是高階首選，今年較新的 SoundLink Plus 跟 SoundLink Micro 二代也把 Bose 產品線補得更齊。這週評測的重點是 JBL 很忙，新的 Go 5 跟 Xtreme 5 評價都不錯，但都沒能取代 Charge 6 的全能地位。要更大聲、戶外開趴，UE Hyperboom 跟 JBL Boombox 4 還是派對首選，Sonos Move 2 則是想要可攜又能併進全家庭系統時的選擇。過去七天沒有東西重排前段，所以照搬。要最佳平衡就買 Charge 6，要外型跟單位體積音量就選 Emberton III，預算無上限就上 SoundLink Max。",
    "highlights": [
      {"title": "JBL Charge 6 穩居第一", "body": "24 小時續航加 Playtime Boost 四小時、可當行動電源、USB-C 無損音訊，全能取勝。"},
      {"title": "Marshall Emberton III 拚外型", "body": "復古造型加上小機身塞滿整房的聲音，守住第二。"},
      {"title": "Bose SoundLink Max 高階首選", "body": "頂級音質，今年再加 SoundLink Plus 與 Micro 二代把產品線補齊。"},
      {"title": "JBL 動作頻頻", "body": "新款 Go 5 與 Xtreme 5 評價都不錯，但都沒撼動 Charge 6 的全能地位。"},
    ],
  },
}

# ---------------- SOUNDBARS ----------------
entries["best-soundbars.json"] = {
  "references": [
    {"title": "Samsung HW-Q990F vs Sonos Arc Ultra: which Dolby Atmos soundbar?", "url": "https://www.whathifi.com/advice/samsung-hw-q990f-vs-sonos-arc-ultra-which-dolby-atmos-soundbar-should-you-buy", "source": "What Hi-Fi?"},
    {"title": "Sonos Arc Ultra vs Samsung HW-Q990F", "url": "https://www.rtings.com/soundbar/tools/compare/sonos-arc-ultra-vs-samsung-hw-q990f/79200/88604", "source": "RTINGS"},
  ],
  "en": {
    "commentary": "In June 2026 the Samsung HW-Q990F keeps my top spot because it is the most complete out-of-the-box surround package you can buy. It ships as a true 11.1.4 system with wireless rear speakers and a subwoofer included, so you get real surround the moment you unbox it, and its connectivity leads the field with two HDMI 2.1 inputs that pass 4K at 120Hz alongside eARC. For a single purchase that fills a room, nothing else is this complete. The Sonos Arc Ultra holds a strong second and earns it on engineering, its new Sound Motion woofer uses four lightweight motors instead of one heavy magnet to push real bass from a slim standalone bar, and at 118cm it is more shelf-friendly than the 130cm Samsung. The catch stays the same, to match the Samsung's full surround you must add Sonos rears and a Sub, which raises the total. The Sony Bravia Theatre Bar 9 holds third for the cleanest Atmos height effects in a one-bar setup. The recurring point in this week's coverage is the all-in-one versus expandable split, Samsung for a complete box, Sonos for a premium bar you grow into. Nothing in the past seven days reorders the top, so I am carrying it forward. Buy the Q990F for instant full surround, the Arc Ultra if you want a slim bar and the Sonos ecosystem, and the Bravia Bar 9 for single-bar Atmos.",
    "highlights": [
      {"title": "Samsung HW-Q990F stays No. 1", "body": "A true 11.1.4 system with wireless rears and a sub included, plus two HDMI 2.1 inputs passing 4K at 120Hz."},
      {"title": "Sonos Arc Ultra for engineering", "body": "Its Sound Motion woofer pushes real bass from a slim 118cm standalone bar, more shelf-friendly than the Samsung."},
      {"title": "Sony Bravia Bar 9 for Atmos height", "body": "Holds third for the cleanest Dolby Atmos height effects in a single-bar setup."},
      {"title": "All-in-one vs expandable", "body": "Samsung wins as a complete box out of the gate, Sonos as a premium bar you expand over time."},
    ],
  },
  "zh-tw": {
    "commentary": "2026 年 6 月，Samsung HW-Q990F 守住我的第一，因為它是開箱即用最完整的環繞組合。它本身就是貨真價實的 11.1.4 系統，無線後喇叭跟重低音都附在盒裝裡，所以拆開當下就有真環繞，連接性也領先全場，兩組 HDMI 2.1 輸入能過 4K 120Hz，再加 eARC。要一次買齊就能填滿整個客廳，沒有別的這麼完整。Sonos Arc Ultra 穩坐第二，這名次靠工藝拿下，它新的 Sound Motion 低音單體用四顆輕量馬達取代單顆笨重磁鐵，從纖薄的單件式 Soundbar 裡推出真低音，118 公分的長度也比 130 公分的三星更好擺。但問題還是老樣子，要追上三星的完整環繞，你得加購 Sonos 後喇叭跟 Sub，總價就上去了。Sony Bravia Theatre Bar 9 守第三，單件式設定下 Atmos 的高度音效最乾淨。這週報導一直在講全合一對上可擴充的差別，三星是完整盒裝，Sonos 是值得慢慢養的高階單件。過去七天沒有東西重排前段，所以照搬。要立刻有完整環繞就買 Q990F，想要纖薄又進 Sonos 生態就選 Arc Ultra，單件式 Atmos 就選 Bravia Bar 9。",
    "highlights": [
      {"title": "Samsung HW-Q990F 穩居第一", "body": "真 11.1.4 系統，附無線後喇叭與重低音，兩組 HDMI 2.1 可過 4K 120Hz。"},
      {"title": "Sonos Arc Ultra 拚工藝", "body": "Sound Motion 低音單體從纖薄 118 公分單件 Soundbar 推出真低音，比三星更好擺。"},
      {"title": "Sony Bravia Bar 9 主打高度音效", "body": "單件式設定下 Atmos 高度音效最乾淨，守住第三。"},
      {"title": "全合一對上可擴充", "body": "三星開箱即完整，Sonos 則是值得慢慢養的高階單件 Soundbar。"},
    ],
  },
}

# ---------------- APPLY ----------------
for fname, e in entries.items():
    d, p = load(fname)
    entry = {
        "date": DATE,
        "rankings": last_rankings(d),
        "references": e["references"],
        "i18n": {"en": e["en"], "zh-tw": e["zh-tw"]},
    }
    upsert(d, entry)
    save(p, d)
    print(f"updated {fname}: {len(d['history'])} entries, last={d['history'][-1]['date']}")
