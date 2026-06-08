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

# ---------------- best-smartphones ----------------
do("best-smartphones.json",
   [
     {"title": "I tested the 7 top flagship phones of 2026 — here's which I recommend", "url": "https://www.techradar.com/phones/i-tested-7-top-flagship-phones-from-apple-samsung-google-and-more", "source": "TechRadar"},
     {"title": "Best Phone 2026: Top 10 Android & iPhone Mobile Phones Today", "url": "https://www.techadvisor.com/article/724318/best-phone.html", "source": "Tech Advisor"},
   ],
   {
     "commentary": "The iPhone 17 Pro Max stays at number one, and the case is the same one TechRadar lands on: it is the most complete premium phone you can buy, with the same camera system and chip as the smaller Pro for a thousand-dollar entry, and a battery that finally goes the distance. I keep it on top because it has no glaring weakness, which is the whole point of a flagship. The Galaxy S26 Ultra holds second and earns it on the camera, the 200MP main sensor pulls color and detail in low light that nothing else matches, and the zoom and night photography are still class-leading. The one knock is the missing magnetic Qi2 charging, which keeps it a hair behind. The Pixel 10 Pro XL stays third and is genuinely the critics' darling, Tech Advisor calls it the best phone today on the strength of computational photography and the 100x Pro Res Zoom that produces usable shots no optical system alone could. I keep it third on the all-round balance rather than any weakness. OnePlus 15 holds fourth as the value flagship, and the iPhone 17 rounds out the top five as the smartest spend in the lineup. Nothing this week forced a reorder, so I held ranks.",
     "highlights": [
       {"title": "iPhone 17 Pro Max is the most complete phone", "body": "Same camera and chip as the smaller Pro for a $1,099 entry, plus a battery that finally lasts. It has no glaring weakness, which is exactly what a flagship at number one should deliver."},
       {"title": "Galaxy S26 Ultra owns the camera", "body": "Its 200MP main sensor pulls color and detail in low light nothing else matches, with class-leading zoom and night shots. The missing magnetic Qi2 charging is the only thing keeping it a hair behind at second."},
       {"title": "Pixel 10 Pro XL is the critics' darling", "body": "Tech Advisor calls it the best phone today, and the 100x Pro Res Zoom produces usable shots no optical system alone could. I hold it third on all-round balance, not on any weakness."},
       {"title": "OnePlus 15 is the value flagship", "body": "It delivers near-flagship performance and battery for noticeably less than the top three. For buyers who want most of the experience without the premium price, it stays the smart pick at fourth."},
     ],
   },
   {
     "commentary": "iPhone 17 Pro Max 我還是放第一，理由跟 TechRadar 一樣：它是你買得到最完整的高階手機，相機系統跟晶片跟小一號的 Pro 一模一樣，一千美元起跳，電池終於夠用一整天。我把它放頂端，是因為它沒有明顯短板，這正是旗艦的意義。Galaxy S26 Ultra 守第二，贏在相機，2 億畫素主感光元件在低光下抓到的色彩跟細節沒人能比，變焦跟夜拍依然是同級最強。唯一的扣分是少了磁吸 Qi2 充電，讓它差一點點。Pixel 10 Pro XL 守第三，是真正的評測寵兒，Tech Advisor 說它是現在最好的手機，靠的是運算攝影跟 100 倍 Pro Res Zoom，能拍出純光學系統做不到的可用畫面。我把它放第三是看整體均衡，不是它有什麼弱點。OnePlus 15 守第四，是性價比旗艦，iPhone 17 收尾前五，是整個陣容裡最聰明的花法。這週沒有事件逼我重排，所以守住排名。",
     "highlights": [
       {"title": "iPhone 17 Pro Max 是最完整的手機", "body": "相機跟晶片跟小一號的 Pro 一樣，台幣約三萬五起跳，電池終於撐得住一整天。它沒有明顯短板，這正是第一名旗艦該交出的東西。"},
       {"title": "Galaxy S26 Ultra 主宰相機", "body": "2 億畫素主感光元件在低光下抓到的色彩細節沒人能比，變焦跟夜拍同級最強。少了磁吸 Qi2 充電是唯一讓它差一點點、守第二的原因。"},
       {"title": "Pixel 10 Pro XL 是評測寵兒", "body": "Tech Advisor 說它是現在最好的手機，100 倍 Pro Res Zoom 拍得出純光學做不到的可用畫面。我放它第三是看整體均衡，不是它有弱點。"},
       {"title": "OnePlus 15 是性價比旗艦", "body": "它用明顯更低的價格給出接近旗艦的效能跟續航。想要大部分體驗又不想付高階價的人，它穩坐第四當聰明選擇。"},
     ],
   })

# ---------------- best-foldable-smartphones ----------------
do("best-foldable-smartphones.json",
   [
     {"title": "Best foldable phones of 2026", "url": "https://www.tomsguide.com/best-picks/best-foldable-phones", "source": "Tom's Guide"},
     {"title": "Best foldable phones to buy in 2026", "url": "https://www.phonearena.com/news/best-foldable-smartphones_id132093", "source": "PhoneArena"},
   ],
   {
     "commentary": "The Galaxy Z Fold 7 stays at number one because it is still the most capable all-around foldable, and this year the headline is how remarkably slim it got, both folded and unfolded, without giving up the 8-inch OLED, the 200MP camera or the flagship Snapdragon. When the brief is do everything, this is the foldable that does it. But the Pixel 10 Pro Fold is breathing down its neck at a close second, and the reason is durability and value: it is the first book-style foldable with a full IP68 rating and a gearless hinge that removes the small parts that wear out, and it lasts longer than the Fold 7 on battery for two hundred dollars less. For a lot of buyers that is the smarter purchase, and I would not argue. Oppo Find N5 holds third as the thinnest premium option for people who prioritize that. Honor Magic V3 stays fourth, and the Galaxy Z Flip 7 rounds out the visible top, its 4.1-inch cover screen finally making the flip format genuinely usable. The foldable category matured this year, the question stopped being whether to fold and became which fold fits you.",
     "highlights": [
       {"title": "Galaxy Z Fold 7 is still the do-everything foldable", "body": "It got remarkably slim folded and unfolded without giving up the 8-inch OLED, 200MP camera or flagship chip. When you want one device that does it all, it stays the most capable pick at number one."},
       {"title": "Pixel 10 Pro Fold is the smarter buy for many", "body": "The first book-style foldable with full IP68 and a gearless hinge, it outlasts the Fold 7 on battery for $200 less. That durability-plus-value combination earns it a very close second."},
       {"title": "Oppo Find N5 wins on thinness", "body": "For buyers who prioritize the slimmest possible premium foldable, it leads on that single axis. That focus keeps it a firm third for people who weigh pocketability above all else."},
       {"title": "Galaxy Z Flip 7 finally nails the flip", "body": "Its 4.1-inch cover screen makes the format genuinely usable, far more spacious than older flips. That fix rounds out the visible top tier and makes the compact foldable worth real consideration again."},
     ],
   },
   {
     "commentary": "Galaxy Z Fold 7 我還是放第一，因為它依然是全面性最強的折疊機，今年的重點是它薄得驚人，折起來跟攤開都是，卻沒犧牲 8 吋 OLED、2 億畫素相機跟旗艦 Snapdragon。要一支什麼都做的折疊機，就是它。但 Pixel 10 Pro Fold 緊咬在後當第二，理由是耐用跟性價比：它是第一支有完整 IP68 的書本式折疊機，無齒輪鉸鏈拿掉了會磨損的小零件，電池比 Fold 7 還耐用，又便宜兩百美元。對很多人這是更聰明的買法，我不會反駁。Oppo Find N5 守第三，是最薄的高階選擇，給最在意這點的人。Honor Magic V3 守第四，Galaxy Z Flip 7 收尾可見前段，4.1 吋封面螢幕終於讓翻蓋格式真的好用。折疊機今年成熟了，問題從要不要折變成哪一款折疊適合你。",
     "highlights": [
       {"title": "Galaxy Z Fold 7 還是什麼都做的折疊機", "body": "它折起跟攤開都薄得驚人，卻沒犧牲 8 吋 OLED、2 億畫素相機跟旗艦晶片。要一支什麼都做的裝置，它依然是最強的選擇，守住第一。"},
       {"title": "Pixel 10 Pro Fold 對很多人是更聰明的買法", "body": "第一支有完整 IP68 的書本式折疊機，無齒輪鉸鏈，電池比 Fold 7 還耐用，又便宜約台幣六千。這份耐用加性價比讓它緊咬第二。"},
       {"title": "Oppo Find N5 贏在薄", "body": "最在意要最薄高階折疊機的買家，它在這單一面向領先。這份專注讓它在最看重口袋友善的人面前穩坐第三。"},
       {"title": "Galaxy Z Flip 7 終於把翻蓋做對", "body": "4.1 吋封面螢幕讓這個格式真的好用，比舊款寬敞太多。這個修正補齊了可見前段，也讓小型折疊機重新值得認真考慮。"},
     ],
   })

# ---------------- best-laptops ----------------
do("best-laptops.json",
   [
     {"title": "Apple MacBook Pro 16 2026 Review - M5 Pro makes a great laptop better", "url": "https://www.notebookcheck.net/Apple-MacBook-Pro-16-2026-Review-M5-Pro.1245523.0.html", "source": "Notebookcheck"},
     {"title": "Best Laptops 2026: benchmarked picks for productivity and battery", "url": "https://www.tomshardware.com/laptops/best-laptops", "source": "Tom's Hardware"},
   ],
   {
     "commentary": "The MacBook Air 13 M5 stays at number one because it remains the laptop I recommend to the most people without hesitation. It is fast enough for nearly everyone, silent because it is fanless, and the battery outlasts a full workday, all at a price that undercuts the Pro line. For everyday productivity it is still the smartest purchase in computing. The MacBook Pro 14 M4 Pro holds second as the workhorse, and the new M5 Pro generation reviewing this spring sharpens the case further, with roughly 20 percent more CPU and 30 to 50 percent more GPU than the M4 Pro, PCIe 5.0 SSDs, Wi-Fi 7 and up to 24 hours of battery. If you need real compute in a laptop, this is the bar. The Asus Zenbook A16 stays third as the best Windows all-rounder, and the Dell XPS 14 holds fourth on build and display. Razer Blade 16 rounds out the visible top as the gaming pick. The through-line this year is that Apple silicon still sets the efficiency ceiling, and the Windows field competes hardest on flexibility and price rather than battery. I held ranks because nothing this week changed that map.",
     "highlights": [
       {"title": "MacBook Air 13 M5 is the everyperson pick", "body": "Fast enough for nearly everyone, silent and fanless, with battery that outlasts a workday at a price under the Pro line. For everyday productivity it stays the smartest purchase in computing and holds number one."},
       {"title": "MacBook Pro 14 is the workhorse bar", "body": "The M5 Pro generation adds roughly 20 percent CPU and 30 to 50 percent GPU over M4 Pro, plus PCIe 5.0, Wi-Fi 7 and up to 24 hours of battery. If you need real compute in a laptop, this sets the standard at second."},
       {"title": "Apple silicon still owns efficiency", "body": "Nothing in the Windows field matches the performance-per-watt that lets these machines run silent and last all day. That efficiency ceiling is why Apple holds the top two slots again this month."},
       {"title": "The Windows field competes on flexibility", "body": "The Zenbook A16 and XPS 14 win on configurability, ports and price rather than battery. For buyers who need Windows or specific hardware, they are the strongest all-rounders, holding third and fourth."},
     ],
   },
   {
     "commentary": "MacBook Air 13 M5 我還是放第一，因為它依然是我會毫不猶豫推薦給最多人的筆電。對幾乎所有人都夠快、無風扇所以安靜、電池撐得過一整個工作天，價格又壓在 Pro 線之下。日常生產力它還是運算界最聰明的買法。MacBook Pro 14 M4 Pro 守第二，是主力機，今年春天評測的 M5 Pro 世代讓論點更銳利，CPU 比 M4 Pro 快約 20 趴、GPU 快 30 到 50 趴，配 PCIe 5.0 SSD、Wi-Fi 7、最高 24 小時電池。筆電要真算力，這就是標竿。Asus Zenbook A16 守第三，是最佳 Windows 全能機，Dell XPS 14 守第四，靠做工跟螢幕。Razer Blade 16 收尾可見前段，是電競選擇。今年的主軸是 Apple 晶片依然訂下能效天花板，Windows 陣營最拚的是彈性跟價格而非續航。這週沒事件改變這張地圖，所以我守住排名。",
     "highlights": [
       {"title": "MacBook Air 13 M5 是給所有人的選擇", "body": "對幾乎所有人都夠快、無風扇安靜、電池撐過一整個工作天，價格又壓在 Pro 線下。日常生產力它還是運算界最聰明的買法，守住第一。"},
       {"title": "MacBook Pro 14 是主力機標竿", "body": "M5 Pro 世代 CPU 比 M4 Pro 快約 20 趴、GPU 快 30 到 50 趴，配 PCIe 5.0、Wi-Fi 7、最高 24 小時電池。筆電要真算力，它在第二訂下標準。"},
       {"title": "Apple 晶片依然主宰能效", "body": "Windows 陣營沒有東西比得上那種讓機器安靜運作又撐一整天的每瓦效能。這道能效天花板就是 Apple 這個月再次包辦前兩名的原因。"},
       {"title": "Windows 陣營拚的是彈性", "body": "Zenbook A16 跟 XPS 14 贏在可配置、連接埠跟價格，而非續航。需要 Windows 或特定硬體的買家，它們是最強的全能機，守第三第四。"},
     ],
   })

# ---------------- best-tablets ----------------
do("best-tablets.json",
   [
     {"title": "Best tablets 2026: top iPads and Android slates tested", "url": "https://www.tomsguide.com/best-picks/best-tablets", "source": "Tom's Guide"},
     {"title": "Best Tablet 2026 reviews", "url": "https://www.techradar.com/best/best-tablet", "source": "TechRadar"},
   ],
   {
     "commentary": "The iPad Air M4 stays at number one because it is the tablet that gets the value math right. It runs the same apps and nearly the same speed as the Pro, takes the same accessories, and costs meaningfully less, so for the vast majority of people it is the correct iPad to buy. I keep it on top precisely because most buyers do not need the Pro. The iPad Pro M5 holds second as the ceiling, the tablet to buy if you drive a creative workflow that actually taps the extra GPU, the better display and the ProMotion panel. For everyone else it is more than they will use. The Galaxy Tab S11 Ultra stays third as the best Android slate and the only real choice if you want a giant screen and DeX desktop mode, a genuinely different proposition from the iPad. The OnePlus Pad 3 holds fourth as the value Android pick, and the iPad mini A17 Pro rounds out the visible top for people who want a small powerful tablet. Nothing this week moved the order. The buying logic stays simple: Air for most, Pro for creators, Tab S11 Ultra for big-screen Android.",
     "highlights": [
       {"title": "iPad Air M4 gets the value math right", "body": "Same apps, nearly Pro speed, same accessories, meaningfully lower price. For the vast majority of buyers it is the correct iPad, which is exactly why it holds number one over the more expensive Pro."},
       {"title": "iPad Pro M5 is the creative ceiling", "body": "Buy it if your workflow actually taps the extra GPU, the better display and ProMotion. For everyone else it is more tablet than they will use, so it holds a clear second behind the Air."},
       {"title": "Galaxy Tab S11 Ultra owns big-screen Android", "body": "It is the only real choice for a giant screen with DeX desktop mode, a genuinely different proposition from any iPad. That distinct strength keeps it the top Android slate at third."},
       {"title": "OnePlus Pad 3 is the value Android pick", "body": "It delivers strong performance and a big bright screen for noticeably less than the Galaxy. For Android buyers who want most of the experience on a budget, it stays the smart choice at fourth."},
     ],
   },
   {
     "commentary": "iPad Air M4 我還是放第一，因為它把性價比的算術算對了。它跑一樣的 App、速度幾乎跟 Pro 一樣、配件通用，價格卻明顯更低，對絕大多數人來說它就是該買的 iPad。我把它放頂端，正是因為多數人根本不需要 Pro。iPad Pro M5 守第二，是天花板，如果你的創作工作流真的用得到多出來的 GPU、更好的螢幕跟 ProMotion 才買它，其他人用不到那麼多。Galaxy Tab S11 Ultra 守第三，是最佳 Android 平板，想要巨大螢幕跟 DeX 桌面模式它是唯一真選擇，跟 iPad 是完全不同的提案。OnePlus Pad 3 守第四，是性價比 Android 選擇，iPad mini A17 Pro 收尾可見前段，給想要小而強平板的人。這週沒有事件改變順序。買法很簡單：多數人選 Air、創作者選 Pro、要大螢幕 Android 選 Tab S11 Ultra。",
     "highlights": [
       {"title": "iPad Air M4 把性價比算對了", "body": "一樣的 App、幾乎 Pro 的速度、通用配件、明顯更低的價格。對絕大多數買家它就是該買的 iPad，這正是它壓過更貴的 Pro、守住第一的原因。"},
       {"title": "iPad Pro M5 是創作天花板", "body": "工作流真的用得到多出來的 GPU、更好的螢幕跟 ProMotion 才買它。其他人用不到那麼多，所以它穩居 Air 之後的第二。"},
       {"title": "Galaxy Tab S11 Ultra 主宰大螢幕 Android", "body": "想要巨大螢幕加 DeX 桌面模式它是唯一真選擇，跟任何 iPad 都是不同提案。這份獨特優勢讓它穩坐 Android 平板第三。"},
       {"title": "OnePlus Pad 3 是性價比 Android 選擇", "body": "它用明顯更低的價格給出強效能跟又大又亮的螢幕。想要大部分體驗又預算有限的 Android 買家，它穩坐第四當聰明選擇。"},
     ],
   })

# ---------------- best-smart-watches ----------------
do("best-smart-watches.json",
   [
     {"title": "Smart Ring or Smartwatch? How to Choose in 2026", "url": "https://askvora.com/blog/smart-rings-vs-smartwatches-2026", "source": "Vora"},
     {"title": "Best smartwatch 2026 reviews", "url": "https://www.techradar.com/best/best-smartwatch", "source": "TechRadar"},
   ],
   {
     "commentary": "The Apple Watch Ultra 3 stays at number one because it is the most capable wrist computer you can buy if you live in the iPhone world. The Series 11 family delivers real-time heart rate zones on every workout, automatic exercise detection, built-in GPS and the deepest app ecosystem, and the Ultra adds the rugged build and multi-day-ish battery that the standard Watch lacks. For an iPhone owner who trains, this is the ceiling. The Ultra 2 holds second as the value version of that same ceiling, still excellent and now cheaper. The Garmin Fenix 8 stays third and is the pick I push hardest for serious endurance athletes, the battery measured in weeks rather than days changes how you actually use a watch, and the training metrics run deeper than Apple's. The Samsung Galaxy Watch 7 Ultra holds fourth as the best Android-side option, and the Apple Series 11 rounds out the visible top as the mainstream pick most people should actually buy. Nothing this week reordered the field. The honest split: Apple for iPhone, Garmin for endurance and battery, Samsung for Android.",
     "highlights": [
       {"title": "Apple Watch Ultra 3 is the iPhone ceiling", "body": "Real-time heart rate zones, auto exercise detection, built-in GPS and the deepest app ecosystem, plus a rugged build and longer battery than the standard Watch. For an iPhone owner who trains, nothing tops it at number one."},
       {"title": "Garmin Fenix 8 owns endurance and battery", "body": "Battery measured in weeks rather than days changes how you use a watch, and its training metrics run deeper than Apple's. For serious endurance athletes it is the pick I push hardest, holding a firm third."},
       {"title": "Ultra 2 is the value version of the ceiling", "body": "It delivers nearly the full Ultra experience now that it sits below the Ultra 3 on price. For buyers who want rugged Apple Watch capability without the latest premium, it stays an easy second."},
       {"title": "Galaxy Watch 7 Ultra leads the Android side", "body": "It is the most capable option for Android owners, with strong health tracking and tight Samsung integration. That makes it the clear cross-platform pick and a solid fourth this month."},
     ],
   },
   {
     "commentary": "Apple Watch Ultra 3 我還是放第一，因為你活在 iPhone 世界裡的話，它就是買得到最強的腕上電腦。Series 11 家族每次運動都給即時心率區間、自動偵測運動、內建 GPS 跟最深的 App 生態，Ultra 再加上三防機身跟接近多日的續航，是標準版沒有的。對會訓練的 iPhone 用戶，這就是天花板。Ultra 2 守第二，是同一道天花板的性價比版，依然出色而且現在更便宜。Garmin Fenix 8 守第三，是我對認真耐力運動者推最用力的選擇，電池用週計而非日計會改變你實際怎麼用錶，訓練數據也比 Apple 更深。Samsung Galaxy Watch 7 Ultra 守第四，是 Android 邊最佳選擇，Apple Series 11 收尾可見前段，是多數人真正該買的主流款。這週沒有事件重排。誠實的分法：iPhone 選 Apple、耐力跟續航選 Garmin、Android 選 Samsung。",
     "highlights": [
       {"title": "Apple Watch Ultra 3 是 iPhone 天花板", "body": "即時心率區間、自動偵測運動、內建 GPS、最深 App 生態，再加三防機身跟比標準版更長的續航。對會訓練的 iPhone 用戶，第一名沒人能超越。"},
       {"title": "Garmin Fenix 8 主宰耐力跟續航", "body": "電池用週計而非日計會改變你怎麼用錶，訓練數據也比 Apple 更深。對認真耐力運動者它是我推最用力的選擇，穩在第三。"},
       {"title": "Ultra 2 是天花板的性價比版", "body": "它現在價格落在 Ultra 3 之下，卻給出幾乎完整的 Ultra 體驗。想要三防 Apple Watch 能力又不想付最新高階價的人，它穩坐第二。"},
       {"title": "Galaxy Watch 7 Ultra 領先 Android 邊", "body": "它是 Android 用戶最強的選擇，健康追蹤紮實、跟 Samsung 整合緊密。這讓它成為明確的跨平台選擇，這個月穩在第四。"},
     ],
   })

# ---------------- best-smart-rings ----------------
do("best-smart-rings.json",
   [
     {"title": "Best smart rings 2026: Oura and top alternatives tested", "url": "https://www.wareable.com/fashion/best-smart-rings-1340", "source": "Wareable"},
     {"title": "5 wearable smart rings challenging the Apple Watch in 2026", "url": "https://tech.sportskeeda.com/mobiles/wearable-smart-rings-challenging-apple-watch-2026", "source": "Sportskeeda"},
   ],
   {
     "commentary": "The Samsung Galaxy Ring and the Oura Ring 4 sit tied at the top for me, and the tie reflects how the category actually splits. Oura still owns the software, the sleep and readiness scoring is the most mature in the business and the daily insights are the ones I trust most, but it locks the best features behind a subscription. The Galaxy Ring matches it on the form factor and hardware with no mandatory subscription, which for Samsung phone owners makes it the better deal outright. That is why they share first. RingConn Gen 2 holds third as the value standout, strong tracking with no subscription and a longer battery than most, the pick I recommend to anyone who wants the smart-ring experience without ongoing cost. Ultrahuman Ring Pro stays fourth on its metabolic-health angle. The structural truth of 2026 is that rings won the sleep-tracking argument, the screenless form factor is lighter and compliance is far higher overnight than any watch, so for sleep and recovery this is the category to buy, and the choice comes down to whether you will pay a subscription for Oura's polish.",
     "highlights": [
       {"title": "Oura and Galaxy Ring are a genuine tie", "body": "Oura owns the most mature sleep and readiness software but locks it behind a subscription, while the Galaxy Ring matches the hardware with no mandatory fee. They win different buyers, so they share the top."},
       {"title": "RingConn Gen 2 is the value standout", "body": "Strong tracking, no subscription and longer battery than most make it the pick for anyone wanting the smart-ring experience without ongoing cost. That clean value proposition holds it a firm third."},
       {"title": "Rings won the sleep-tracking argument", "body": "The screenless form factor is lighter and overnight compliance runs far higher than any watch. For sleep and recovery specifically, this is the category to buy, which is why the field stays strong this month."},
       {"title": "The Oura choice is about the subscription", "body": "Its software polish is real, but so is the recurring fee. If you will pay for the best insights, Oura; if you want the data without the bill, the Galaxy Ring or RingConn make more sense."},
     ],
   },
   {
     "commentary": "Samsung Galaxy Ring 跟 Oura Ring 4 在我這並列第一，這個並列反映了這個類別實際的分法。Oura 軟體還是最強，睡眠跟 readiness 評分是業界最成熟的，每日洞察也是我最信的，但它把最好的功能鎖在訂閱後面。Galaxy Ring 在形體跟硬體上跟它打平，而且沒有強制訂閱，對 Samsung 手機用戶這直接就是更划算的選擇。這就是它們共享第一的原因。RingConn Gen 2 守第三，是性價比亮點，追蹤紮實、沒訂閱、電池比多數長，是我推薦給想要智慧戒指體驗又不想持續付費的人的選擇。Ultrahuman Ring Pro 守第四，靠它的代謝健康切角。2026 年的結構性事實是戒指贏了睡眠追蹤這場辯論，無螢幕形體更輕，整夜配戴率遠高於任何手錶，所以單講睡眠跟恢復，這就是該買的類別，選擇就看你願不願意為 Oura 的精緻付訂閱費。",
     "highlights": [
       {"title": "Oura 跟 Galaxy Ring 是真正的並列", "body": "Oura 有最成熟的睡眠跟 readiness 軟體但鎖在訂閱後面，Galaxy Ring 硬體打平卻沒有強制月費。它們贏的是不同買家，所以共享第一。"},
       {"title": "RingConn Gen 2 是性價比亮點", "body": "追蹤紮實、沒訂閱、電池比多數長，是想要智慧戒指體驗又不想持續付費的人的選擇。這個乾淨的價值主張讓它穩在第三。"},
       {"title": "戒指贏了睡眠追蹤這場辯論", "body": "無螢幕形體更輕，整夜配戴率遠高於任何手錶。單講睡眠跟恢復，這就是該買的類別，這也是這個月整體還是很強的原因。"},
       {"title": "Oura 的抉擇在於訂閱", "body": "它軟體的精緻是真的，但月費也是真的。願意為最好的洞察付費就選 Oura，想要數據又不想被收費，Galaxy Ring 或 RingConn 更合理。"},
     ],
   })

# ---------------- best-smart-glasses ----------------
do("best-smart-glasses.json",
   [
     {"title": "Best smart glasses 2026: Ray-Ban Meta and the field tested", "url": "https://www.theverge.com/smart-glasses", "source": "The Verge"},
     {"title": "Best AR and smart glasses 2026", "url": "https://www.cnet.com/tech/computing/best-smart-glasses/", "source": "CNET"},
   ],
   {
     "commentary": "The Ray-Ban Meta Gen 2 stays at number one because it is the only smart glasses I can recommend to a normal person without an asterisk. They look like Ray-Bans, the camera and audio are genuinely good, the Meta AI assistant is useful for quick lookups, and the battery finally lasts a real day. For the vast majority of buyers this is the pair to get. The Oakley Meta HSTN holds second as the same formula in a sportier frame, the pick for people who want the active styling, and the wraparound fit is better for running and cycling. The Meta Ray-Ban Display stays third and is the genuinely exciting one, the in-lens display and neural wristband point at where the category is going, but the price and first-gen rough edges keep it a step behind the no-display pairs for now. Xreal One Pro holds fourth as the best pick for a different job entirely, a wearable big-screen display for media and work rather than an everyday assistant. The map is clear: Ray-Ban Meta for everyday, Oakley for sport, Display for early adopters, Xreal for screens.",
     "highlights": [
       {"title": "Ray-Ban Meta Gen 2 is the no-asterisk pick", "body": "They look like Ray-Bans, the camera and audio are genuinely good, the AI is useful for lookups and battery lasts a real day. For most buyers this is the pair to get, holding a clear number one."},
       {"title": "Oakley Meta HSTN is the sport version", "body": "Same proven formula in a sportier wraparound frame that fits better for running and cycling. For active buyers who want the styling and fit, it is the natural pick and a firm second."},
       {"title": "Meta Ray-Ban Display points at the future", "body": "The in-lens display and neural wristband show where the category is heading, but first-gen rough edges and price keep it behind the simpler pairs for now. It holds an exciting third for early adopters."},
       {"title": "Xreal One Pro does a different job", "body": "It is a wearable big-screen display for media and work rather than an everyday AI assistant. For that specific use case it leads the field, holding fourth as the pick for portable screens."},
     ],
   },
   {
     "commentary": "Ray-Ban Meta Gen 2 我還是放第一，因為它是我能毫無但書推薦給一般人的唯一智慧眼鏡。它看起來就是 Ray-Ban，相機跟音訊都真的不錯，Meta AI 助手做快速查詢很實用，電池終於撐得過真正的一整天。對絕大多數買家，就是這副。Oakley Meta HSTN 守第二，是同一套公式換上運動感框型，給想要動感造型的人，包覆式設計跑步騎車更合適。Meta Ray-Ban Display 守第三，是真正讓人興奮的那副，鏡片內顯示加神經腕帶指向類別的未來，但價格跟第一代的粗糙讓它暫時落後無顯示款一步。Xreal One Pro 守第四，做的是完全不同的活，是穿戴式大螢幕顯示器、用來看影音跟工作，而非日常助手。地圖很清楚：日常選 Ray-Ban Meta、運動選 Oakley、嘗鮮選 Display、要螢幕選 Xreal。",
     "highlights": [
       {"title": "Ray-Ban Meta Gen 2 是無但書的選擇", "body": "看起來就是 Ray-Ban，相機跟音訊都真的不錯，AI 查詢實用，電池撐過真正一整天。對多數買家就是這副，穩坐第一。"},
       {"title": "Oakley Meta HSTN 是運動版", "body": "同一套成熟公式換上運動感包覆框型，跑步騎車更合適。對想要這種造型跟貼合度的活躍買家，它是自然選擇，穩在第二。"},
       {"title": "Meta Ray-Ban Display 指向未來", "body": "鏡片內顯示加神經腕帶展示類別的走向，但第一代的粗糙跟價格讓它暫時落後較單純的款式。它在第三，給嘗鮮者一個興奮的選擇。"},
       {"title": "Xreal One Pro 做的是不同的活", "body": "它是穿戴式大螢幕顯示器，用來看影音跟工作，不是日常 AI 助手。就這個特定用途它領先全場，守第四當可攜螢幕的選擇。"},
     ],
   })

print("batchB done")
