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

# ---------------- best-gaming-mice ----------------
do("best-gaming-mice.json",
   [
     {"title": "Best Gaming Mouse 2026 — Top Picks for FPS, MOBA and Casual", "url": "https://gamingpcguru.com/best-gaming-mouse-2026/", "source": "Gaming PC Guru"},
     {"title": "Best gaming mouse 2026 reviews", "url": "https://www.rtings.com/mouse/reviews/best/gaming", "source": "RTINGS"},
   ],
   {
     "commentary": "The Logitech G Pro X Superlight family stays at the top because it is still the mouse the actual pros choose, and that is not branding, it is what shows up under the hands at LAN events. The shape is the safest neutral shape in the business, the weight is genuinely low without feeling hollow, and the sensor never misbehaves under pressure. For competitive FPS this remains the default, and I keep the Superstrike and Dex variants leading because Logitech kept iterating the click and sensor without breaking what works. The Razer Viper V4 Pro holds its tight spot as the strongest challenger, the ergonomics suit a different grip and the optical switches are excellent, so for players who never gelled with the Logitech shape this is the answer. The DeathAdder V4 Pro carries the ergonomic-grip crown for palm users who want low weight in a fuller shell. The OP1we rounds out the front as the enthusiast-favorite boutique option. Nothing this week reordered the field. The honest read: shape is everything in a mouse, so try the grip before you trust the spec sheet.",
     "highlights": [
       {"title": "Logitech G Pro X Superlight is still the pro default", "body": "It is the mouse that actually shows up under pro hands at LAN events: safest neutral shape, genuinely low weight, a sensor that never misbehaves under pressure. For competitive FPS it stays the default at the top."},
       {"title": "Razer Viper V4 Pro is the strongest challenger", "body": "Different ergonomics and excellent optical switches make it the answer for players who never gelled with the Logitech shape. That distinct fit keeps it in a tight battle near the very top."},
       {"title": "DeathAdder V4 Pro wins for palm grip", "body": "It carries the ergonomic crown for palm users who want low weight in a fuller shell. For the large share of players who do not use a claw or fingertip grip, it is the natural pick near the front."},
       {"title": "Shape beats spec in a mouse", "body": "Sensors are all excellent now, so the deciding factor is whether the shell fits your grip. Try the shape before trusting the spec sheet, because a mismatched shape ruins an otherwise perfect mouse."},
     ],
   },
   {
     "commentary": "Logitech G Pro X Superlight 家族我還是放頂端，因為它依然是真正的職業選手會選的滑鼠，這不是行銷，是 LAN 賽事桌上手底下真的出現的東西。它的形狀是業界最安全的中性形狀，重量真的輕又不會空心，感應器在壓力下從不出包。競技 FPS 它還是預設，我讓 Superstrike 跟 Dex 版本領先，是因為 Logitech 持續迭代點擊跟感應器，又沒破壞原本就對的東西。Razer Viper V4 Pro 守住緊咬的位置，是最強挑戰者，人體工學適合不同握法，光學微動也很優秀，跟 Logitech 形狀合不來的玩家答案就是它。DeathAdder V4 Pro 扛起人體工學握法的王冠，給想要在較飽滿外殼裡要低重量的趴握用戶。OP1we 收尾前段，是玩家最愛的精品選擇。這週沒事件重排。老實講：滑鼠形狀就是一切，相信規格表前先試握法。",
     "highlights": [
       {"title": "Logitech G Pro X Superlight 還是職業預設", "body": "它是 LAN 賽事手底下真的出現的滑鼠：最安全的中性形狀、真的輕的重量、壓力下不出包的感應器。競技 FPS 它穩坐頂端當預設。"},
       {"title": "Razer Viper V4 Pro 是最強挑戰者", "body": "不同的人體工學跟優秀的光學微動，讓它成為跟 Logitech 形狀合不來玩家的答案。這份獨特貼合讓它在最頂端緊咬。"},
       {"title": "DeathAdder V4 Pro 贏在趴握", "body": "它扛起人體工學的王冠，給想在較飽滿外殼裡要低重量的趴握用戶。對不用爪握或指尖握的大批玩家，它是前段的自然選擇。"},
       {"title": "滑鼠裡形狀勝過規格", "body": "現在感應器都很優秀，決勝點是外殼合不合你的握法。相信規格表前先試形狀，因為不合的形狀會毀掉一隻原本完美的滑鼠。"},
     ],
   })

# ---------------- best-mechanical-keyboards ----------------
do("best-mechanical-keyboards.json",
   [
     {"title": "Best gaming keyboards 2026: Hall effect, mechanical, TKL tested", "url": "https://www.pcgamer.com/best-gaming-keyboard/", "source": "PC Gamer"},
     {"title": "The 6 Best Gaming Keyboards of 2026", "url": "https://www.rtings.com/keyboard/reviews/best/by-usage/gaming", "source": "RTINGS"},
   ],
   {
     "commentary": "The Wooting 60HE stays at number one because it changed what a gaming keyboard is supposed to do, and the rest of the market is still catching up. Hall effect switches with adjustable actuation mean you set exactly how far a key travels before it fires, plus rapid trigger for instant resets, and once you play on it a normal mechanical board feels slow. For competitive FPS this is the standard now, full stop. The Wooting 80HE holds second as the same magic in a larger layout for people who want the arrows and a few extra keys. The SteelSeries Apex Pro TKL Wireless stays third as the mainstream-brand answer with Hall effect and the best software polish of the big names, the pick for buyers who want the tech without the enthusiast learning curve. The Keychron Q1 Pro holds fourth for the typing crowd who care about board feel and sound over actuation tricks. Nothing this week reordered the field. The clear read: Hall effect won the performance argument, so if you game competitively, buy a magnetic board and do not look back.",
     "highlights": [
       {"title": "Wooting 60HE redefined the gaming keyboard", "body": "Adjustable Hall effect actuation plus rapid trigger lets you tune exactly when each key fires, and a normal mechanical board feels slow afterward. For competitive FPS it is the standard now, holding number one."},
       {"title": "Wooting 80HE is the same magic, bigger", "body": "It brings the adjustable actuation and rapid trigger to a fuller layout with arrows and extra keys. For players who want the performance without the cramped 60 percent footprint, it is the clear second."},
       {"title": "Apex Pro TKL is the mainstream-brand pick", "body": "Hall effect tech with the best software polish among the big names, easier to live with than enthusiast boards. For buyers who want the performance without the learning curve, it holds a firm third."},
       {"title": "Hall effect won the performance argument", "body": "Adjustable actuation and rapid trigger are a genuine competitive edge, not marketing. If you game seriously, buy a magnetic board, because traditional mechanical switches now feel a step behind."},
     ],
   },
   {
     "commentary": "Wooting 60HE 我還是放第一，因為它改變了電競鍵盤該做什麼，而市場其他人還在追。霍爾效應軸搭可調觸發點，代表你能精確設定一個鍵要按多深才觸發，加上 rapid trigger 瞬間重置，玩過之後一般機械鍵盤就感覺慢。競技 FPS 現在就是這個標準，沒得談。Wooting 80HE 守第二，是同一套魔法換大配列，給想要方向鍵跟多幾顆鍵的人。SteelSeries Apex Pro TKL Wireless 守第三，是主流品牌的答案，有霍爾效應、軟體也是大廠裡最精緻的，給想要這技術又不想要玩家級學習曲線的買家。Keychron Q1 Pro 守第四，給在意敲擊手感跟聲音勝過觸發花招的打字派。這週沒事件重排。清楚的判斷：霍爾效應贏了效能這場辯論，認真打競技就買磁軸，別回頭。",
     "highlights": [
       {"title": "Wooting 60HE 重新定義電競鍵盤", "body": "可調霍爾效應觸發加 rapid trigger 讓你精確設定每顆鍵何時觸發，玩過之後一般機械鍵盤就感覺慢。競技 FPS 它現在就是標準，守第一。"},
       {"title": "Wooting 80HE 是同一套魔法換大號", "body": "它把可調觸發跟 rapid trigger 帶到有方向鍵跟多幾顆鍵的較完整配列。想要效能又不想要 60% 擁擠尺寸的玩家，它是明確第二。"},
       {"title": "Apex Pro TKL 是主流品牌選擇", "body": "霍爾效應技術加大廠裡最精緻的軟體，比玩家級鍵盤好相處。想要效能又不想要學習曲線的買家，它穩在第三。"},
       {"title": "霍爾效應贏了效能辯論", "body": "可調觸發跟 rapid trigger 是真的競技優勢，不是行銷。認真打就買磁軸，因為傳統機械軸現在感覺慢了一步。"},
     ],
   })

# ---------------- best-gaming-headsets ----------------
do("best-gaming-headsets.json",
   [
     {"title": "Best gaming headset 2026 reviews", "url": "https://www.rtings.com/headphones/reviews/best/gaming", "source": "RTINGS"},
     {"title": "Best Gaming Headset 2026: tested picks", "url": "https://www.tomsguide.com/best-picks/best-gaming-headsets", "source": "Tom's Guide"},
   ],
   {
     "commentary": "The SteelSeries Arctis Nova Pro Wireless stays at number one because it is the headset that does everything well and nothing badly, and that completeness is rare. The dual-battery hot-swap means it never dies mid-session, the base station handles every input you own, the ANC actually works and the sound is tuned for both games and music. For most buyers who want one premium headset to cover everything, this is the benchmark. The Audeze Maxwell 2 holds second and wins the pure audio contest outright, the planar drivers sound dramatically better than anything else in the category, so for people who treat the headset as headphones that also game, this is the pick. The Turtle Beach Stealth Pro II stays third as the strongest all-round value challenger to the SteelSeries. The Logitech G Pro X 2 Lightspeed holds fourth on comfort and esports pedigree. Nothing this week reordered the field. The read: best all-rounder is SteelSeries, best sound is Audeze, and unless you specifically want planar audio, the Nova Pro is the safer recommendation.",
     "highlights": [
       {"title": "SteelSeries Arctis Nova Pro does everything well", "body": "Dual-battery hot-swap so it never dies mid-session, a base station for every input, working ANC and sound tuned for games and music. For one premium headset to cover everything, it is the benchmark at number one."},
       {"title": "Audeze Maxwell 2 wins pure audio", "body": "Its planar drivers sound dramatically better than anything else in the category. For players who treat the headset as headphones that also game, it is the clear pick and a firm second."},
       {"title": "Turtle Beach Stealth Pro II is the value challenger", "body": "It delivers the most complete all-round package short of the SteelSeries for less money. For buyers who want premium features without the top price, it holds a solid third."},
       {"title": "Pick by whether you want planar sound", "body": "The Nova Pro is the safer all-round recommendation, but if audio quality is your top priority, the Maxwell 2's planar drivers are worth the trade-offs. Decide on sound priority first."},
     ],
   },
   {
     "commentary": "SteelSeries Arctis Nova Pro Wireless 我還是放第一，因為它每件事都做得好、沒有一件做得差，這種完整度很稀有。雙電池熱抽換代表它不會在對戰中沒電，基座吃下你所有的輸入，ANC 真的有用，音質遊戲跟音樂兩邊都調得好。對多數想要一副高階耳機包辦一切的買家，這就是標竿。Audeze Maxwell 2 守第二，純音質的比賽直接贏，平板振膜聽起來比這類別任何東西都好太多，把耳機當成也能打遊戲的耳機的人就選它。Turtle Beach Stealth Pro II 守第三，是對 SteelSeries 最強的全能性價比挑戰者。Logitech G Pro X 2 Lightspeed 守第四，靠舒適跟電競血統。這週沒事件重排。判斷：全能最佳選 SteelSeries、音質最佳選 Audeze，除非你特別想要平板音質，否則 Nova Pro 是更安全的推薦。",
     "highlights": [
       {"title": "SteelSeries Arctis Nova Pro 每件事都做得好", "body": "雙電池熱抽換不會中途沒電、基座吃下所有輸入、ANC 真的有用、音質遊戲音樂都調得好。要一副高階耳機包辦一切，它是第一名標竿。"},
       {"title": "Audeze Maxwell 2 贏純音質", "body": "它的平板振膜聽起來比這類別任何東西都好太多。把耳機當成也能打遊戲的耳機的玩家，它是明確選擇，穩在第二。"},
       {"title": "Turtle Beach Stealth Pro II 是性價比挑戰者", "body": "它用更低的價格給出僅次於 SteelSeries 的最完整全能組合。想要高階功能又不想付頂價的買家，它穩在第三。"},
       {"title": "照你要不要平板音質選", "body": "Nova Pro 是更安全的全能推薦，但音質是你最高優先，Maxwell 2 的平板振膜值得那些取捨。先決定音質優先順序。"},
     ],
   })

# ---------------- best-gaming-monitors ----------------
do("best-gaming-monitors.json",
   [
     {"title": "Best gaming monitor 2026 reviews", "url": "https://www.rtings.com/monitor/reviews/best/gaming", "source": "RTINGS"},
     {"title": "Best Gaming Monitors 2026: OLED and high-refresh picks", "url": "https://www.tomshardware.com/best-picks/best-gaming-monitors", "source": "Tom's Hardware"},
   ],
   {
     "commentary": "The Asus ROG Swift OLED PG27UCDM stays at number one because it is the monitor that finally stops asking you to choose. It is a 4K 240Hz QD-OLED, which means you get pixel density and refresh rate at the same time, and for a single display that does both productivity sharpness and competitive smoothness, nothing else hits this balance. The OLED contrast makes everything else look gray by comparison. The LG UltraGear 27GX790B holds second as the value high-refresh OLED, slightly lower resolution but blistering speed for less money, the pick for pure competitive players who care about frames over pixels. The MSI MPG 341CQR X36 stays third as the ultrawide immersion choice for people who want the wraparound experience in single-player and sim games. The Samsung Odyssey OLED G8 holds fourth as another strong 4K OLED option. Nothing this week reordered the field. The read is simple: QD-OLED won, the burn-in fear is largely solved with modern panel care, and the only real question is 4K-and-fast versus pure-speed for the budget you have.",
     "highlights": [
       {"title": "ROG Swift PG27UCDM stops you choosing", "body": "A 4K 240Hz QD-OLED delivers pixel density and refresh rate at once, the rare display that nails productivity sharpness and competitive smoothness together. That balance plus OLED contrast holds it at number one."},
       {"title": "LG UltraGear 27GX790B is the value speed pick", "body": "Slightly lower resolution but blistering refresh for less money makes it the choice for pure competitive players who value frames over pixels. That focus keeps it a firm second."},
       {"title": "MSI MPG 341CQR X36 wins on immersion", "body": "Its ultrawide curve delivers the wraparound experience that single-player and sim games thrive on. For players who prioritize immersion over esports speed, it holds a solid third."},
       {"title": "QD-OLED won the monitor argument", "body": "The contrast is transformative and modern panel care has largely solved the burn-in fear. The only real question left is 4K-and-fast versus pure-speed, decided by your budget and what you play."},
     ],
   },
   {
     "commentary": "Asus ROG Swift OLED PG27UCDM 我還是放第一，因為它終於不再要你二選一。它是 4K 240Hz QD-OLED，意思是你同時拿到像素密度跟更新率，要一台螢幕同時做到生產力的銳利跟競技的滑順，沒有別的能打到這個平衡。OLED 的對比讓其他東西相比之下都像灰的。LG UltraGear 27GX790B 守第二，是性價比高更新 OLED，解析度略低但速度兇猛、又更便宜，給在意幀數勝過像素的純競技玩家。MSI MPG 341CQR X36 守第三，是帶魚屏沉浸選擇，給想在單人跟模擬遊戲裡要包覆體驗的人。Samsung Odyssey OLED G8 守第四，是另一個強力 4K OLED 選擇。這週沒事件重排。判斷很簡單：QD-OLED 贏了，烙印的恐懼用現代面板養護大致解決，唯一真問題是你的預算要 4K 又快還是純速度。",
     "highlights": [
       {"title": "ROG Swift PG27UCDM 讓你不必二選一", "body": "4K 240Hz QD-OLED 同時給像素密度跟更新率，是少數同時做到生產力銳利跟競技滑順的螢幕。這份平衡加 OLED 對比讓它守第一。"},
       {"title": "LG UltraGear 27GX790B 是性價比速度選擇", "body": "解析度略低但更新率兇猛又更便宜，是在意幀數勝過像素的純競技玩家的選擇。這份專注讓它穩在第二。"},
       {"title": "MSI MPG 341CQR X36 贏在沉浸", "body": "帶魚屏曲面給單人跟模擬遊戲最適合的包覆體驗。重視沉浸勝過電競速度的玩家，它穩坐第三。"},
       {"title": "QD-OLED 贏了螢幕辯論", "body": "對比是顛覆性的，現代面板養護也大致解決了烙印恐懼。剩下的唯一真問題是 4K 又快還是純速度，由你的預算跟玩什麼決定。"},
     ],
   })

# ---------------- best-gaming-chairs ----------------
do("best-gaming-chairs.json",
   [
     {"title": "Best gaming chair 2026 reviews", "url": "https://www.rtings.com/chair/reviews/best/gaming", "source": "RTINGS"},
     {"title": "Best Gaming Chairs 2026: tested for comfort and support", "url": "https://www.tomsguide.com/best-picks/best-gaming-chairs", "source": "Tom's Guide"},
   ],
   {
     "commentary": "The Secretlab Titan Evo stays at number one because it is the gaming chair that gets the fundamentals right at a price most people can actually justify. The build quality is genuinely premium, the lumbar support is the best integrated system in a racing-style chair, and the materials hold up over years rather than peeling in months. For the broadest set of buyers who want a real gaming chair without office-chair money, this is the default and has been for a reason. The Herman Miller Vantum holds second as the proper ergonomic-grade option, it costs far more but it is built like the office chairs that justify their price, the pick for people who sit all day and treat the chair as a health purchase. The Libernovo Omni stays third as the ambitious value challenger with mesh and dynamic support. The Razer Iskur V2 holds fourth on its built-in lumbar adjustment. Nothing this week reordered the field. The honest split: racing-style comfort and value is Secretlab, true ergonomic posture is Herman Miller, and your spine decides which matters more.",
     "highlights": [
       {"title": "Secretlab Titan Evo gets the fundamentals right", "body": "Genuinely premium build, the best integrated lumbar in a racing-style chair and materials that last years. For a real gaming chair without office-chair money, it is the default at number one for good reason."},
       {"title": "Herman Miller Vantum is the ergonomic-grade pick", "body": "It costs far more but is built like office chairs that justify their price. For people who sit all day and treat the chair as a health purchase, it is the serious choice and a firm second."},
       {"title": "Libernovo Omni is the value challenger", "body": "Mesh construction and dynamic support deliver ambitious ergonomics for less than the establishment names. For buyers who want breathability and posture support on a budget, it holds a solid third."},
       {"title": "Your spine decides the category", "body": "Racing-style chairs like Secretlab win on comfort and value; true ergonomic chairs like Herman Miller win on all-day posture. Decide whether you want comfort or clinical support before you shop."},
     ],
   },
   {
     "commentary": "Secretlab Titan Evo 我還是放第一，因為它在多數人真的負擔得起的價格上把基本功做對。做工是真的高級，腰靠是賽車式椅子裡最好的整合系統，材質撐得過好幾年而非幾個月就脫皮。對最廣、想要一張真正電競椅又不想花辦公椅錢的買家，它是預設，而且是有道理的。Herman Miller Vantum 守第二，是真正人體工學等級的選擇，貴很多，但做工像那些對得起價格的辦公椅，給整天坐著、把椅子當健康投資的人。Libernovo Omni 守第三，是有野心的性價比挑戰者，網布加動態支撐。Razer Iskur V2 守第四，靠它內建的腰靠調整。這週沒事件重排。誠實的分法：賽車式舒適跟性價比選 Secretlab、真正人體工學坐姿選 Herman Miller，你的脊椎決定哪個更重要。",
     "highlights": [
       {"title": "Secretlab Titan Evo 把基本功做對", "body": "真的高級的做工、賽車式椅子裡最好的整合腰靠、撐得過好幾年的材質。要真正電競椅又不想花辦公椅錢，它是第一名預設，有道理。"},
       {"title": "Herman Miller Vantum 是人體工學等級選擇", "body": "貴很多但做工像那些對得起價格的辦公椅。整天坐著、把椅子當健康投資的人，它是認真的選擇，穩在第二。"},
       {"title": "Libernovo Omni 是性價比挑戰者", "body": "網布加動態支撐，用比老牌更低的價格給出有野心的人體工學。想要透氣跟坐姿支撐又預算有限的買家，它穩在第三。"},
       {"title": "你的脊椎決定類別", "body": "Secretlab 這種賽車式椅贏在舒適跟性價比；Herman Miller 這種真人體工學椅贏在整天坐姿。買前先決定你要舒適還是臨床級支撐。"},
     ],
   })

# ---------------- best-handheld-gaming-consoles ----------------
do("best-handheld-gaming-consoles.json",
   [
     {"title": "Best gaming handheld 2026: Switch 2, Steam Deck and the field", "url": "https://www.theverge.com/gaming-handhelds", "source": "The Verge"},
     {"title": "Best handheld gaming console 2026 reviews", "url": "https://www.ign.com/articles/best-gaming-handheld", "source": "IGN"},
   ],
   {
     "commentary": "The Nintendo Switch 2 stays at number one because the question for a handheld is never raw specs, it is what you can actually play, and nothing else has Nintendo's library. The hardware finally got the horsepower and screen it needed, third-party ports run well, and the first-party games remain the reason the whole category exists. For most buyers this is the handheld to own, full stop. The ROG Xbox Ally X holds second as the best Windows handheld, the most powerful way to play your existing PC library on the go, and the Xbox-flavored interface finally tames Windows handheld jank enough to recommend. The Steam Deck OLED stays third and remains my pick for the best overall PC-handheld value, the SteamOS experience is still the smoothest and the OLED screen is gorgeous, held back only by raw power against newer chips. The Lenovo Legion Go 2 holds fourth on its versatile detachable design. Nothing this week reordered the field. The read: library-first buyers get the Switch 2, PC-library buyers choose between Ally X power and Steam Deck polish.",
     "highlights": [
       {"title": "Switch 2 wins because of the library", "body": "A handheld lives or dies on what you can play, and nothing matches Nintendo's first-party catalog. The hardware finally has the horsepower and screen to match, holding it the default at number one."},
       {"title": "ROG Xbox Ally X is the best Windows handheld", "body": "It is the most powerful way to play your existing PC library on the go, and the Xbox interface finally tames Windows handheld jank. For PC gamers who want raw power, it is a clear second."},
       {"title": "Steam Deck OLED is the value champ", "body": "SteamOS stays the smoothest handheld experience and the OLED screen is gorgeous, held back only by raw power against newer chips. For best overall PC-handheld value, it holds a firm third."},
       {"title": "Pick by which library you want", "body": "Nintendo exclusives mean the Switch 2; your Steam catalog means choosing between Ally X power and Steam Deck polish. The library you already own should decide the purchase, not the spec sheet."},
     ],
   },
   {
     "commentary": "Nintendo Switch 2 我還是放第一，因為掌機的問題從來不是純規格，是你真的能玩什麼，而沒人有任天堂的遊戲庫。硬體終於拿到它需要的馬力跟螢幕，第三方移植跑得好，第一方遊戲依然是整個類別存在的理由。對多數買家這就是該擁有的掌機，沒得談。ROG Xbox Ally X 守第二，是最佳 Windows 掌機，是帶著你既有 PC 遊戲庫出門最強的方式，Xbox 風格介面終於把 Windows 掌機的卡頓馴服到能推薦。Steam Deck OLED 守第三，依然是我心中最佳整體 PC 掌機性價比，SteamOS 體驗還是最順、OLED 螢幕漂亮，唯一被新晶片在純效能上比下去。Lenovo Legion Go 2 守第四，靠它多用途的可拆設計。這週沒事件重排。判斷：遊戲庫優先的買家拿 Switch 2、PC 庫買家在 Ally X 的力量跟 Steam Deck 的細膩間選。",
     "highlights": [
       {"title": "Switch 2 贏在遊戲庫", "body": "掌機成敗看你能玩什麼，沒人比得上任天堂的第一方陣容。硬體終於有相稱的馬力跟螢幕，守住第一名預設位置。"},
       {"title": "ROG Xbox Ally X 是最佳 Windows 掌機", "body": "它是帶著既有 PC 庫出門最強的方式，Xbox 介面終於馴服 Windows 掌機的卡頓。想要純力量的 PC 玩家，它是明確第二。"},
       {"title": "Steam Deck OLED 是性價比冠軍", "body": "SteamOS 還是最順的掌機體驗，OLED 螢幕漂亮，唯一被新晶片在純效能比下去。論最佳整體 PC 掌機性價比，它穩在第三。"},
       {"title": "照你要哪個遊戲庫選", "body": "想要任天堂獨佔就 Switch 2；想要你的 Steam 庫就在 Ally X 力量跟 Steam Deck 細膩間選。已經擁有的遊戲庫該決定購買，而非規格表。"},
     ],
   })

print("batchD done")
