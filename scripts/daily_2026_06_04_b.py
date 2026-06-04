import sys; sys.path.insert(0, "/Users/etrexkuo/toprankland/scripts")
from daily_helper import load, save, upsert, last_rankings, DATE  # DATE == "2026-06-04"

def build(name, refs, en, zh, rankings=None):
    d, p = load(name)
    entry = {
        "date": DATE,
        "rankings": rankings if rankings is not None else last_rankings(d),
        "references": refs,
        "i18n": {"en": en, "zh-tw": zh},
    }
    upsert(d, entry)
    save(p, d)
    print("updated", name)


# ---------------------------------------------------------------- LAPTOPS
build(
    "best-laptops.json",
    [
        {"title": "The best laptops of Computex 2026: top machines from Dell, MSI, Acer, and even Microsoft", "url": "https://www.techradar.com/computing/laptops/the-best-laptops-of-computex-2026", "source": "TechRadar"},
        {"title": "The best laptops in 2026 — tested, reviewed, and worth your money", "url": "https://www.tomsguide.com/computing/laptops/best-laptops", "source": "Tom's Guide"},
        {"title": "Best Laptops 2026: Our benchmarked picks for productivity, portability, and battery life", "url": "https://www.tomshardware.com/laptops/best-laptops", "source": "Tom's Hardware"},
    ],
    {
        "commentary": (
            "Coming out of Computex 2026 the picture at the top of this list is steady, and that is a good thing for buyers right now. "
            "The MacBook Air M5 keeps the number one slot because it does the thing most people actually need: it runs cool and silent on a full day of email, browser tabs and video calls, and the battery genuinely clears a work day with room to spare. "
            "The big news this week is the wave of Nvidia RTX Spark machines shown at Computex, including a Microsoft Surface Laptop Ultra, plus Intel Panther Lake and AMD Gorgon Point parts filtering into shipping Windows laptops. "
            "That matters for the middle of this list more than the podium. The Zenbook A16 and Dell XPS 14 still earn their places on battery life and build, and I am holding them steady because the genuinely new RTX Spark hardware is still arriving and needs real review testing before it moves anyone up. "
            "Dell also teased a cheaper XPS 13 around 599 to 699 dollars, which is the part of the market I would watch closest over the next month. "
            "The Razer Blade 16 stays the gaming pick at rank five thanks to its thin chassis and strong sustained performance under load. "
            "As of June 2026 my advice is simple: if you want a laptop today, the top of this list is exactly where your money is safest, and the Panther Lake and RTX Spark stuff is worth waiting on only if you specifically want on-device AI horsepower."
        ),
        "highlights": [
            {"title": "MacBook Air M5 holds number one", "body": "It stays silent and cool through a full day of everyday work, the display is bright and accurate, and battery life clears a work day comfortably. At its price it remains the easiest recommendation here."},
            {"title": "Computex 2026 brought RTX Spark laptops", "body": "Nvidia RTX Spark machines, including a Microsoft Surface Laptop Ultra, headlined the show. They look promising for on-device AI but need full review testing before any rank change."},
            {"title": "Panther Lake and Gorgon Point are shipping", "body": "Intel Core Ultra Series 3 (Panther Lake) and AMD Gorgon Point Ryzen AI chips are reaching real laptops, which should lift battery life and efficiency across the Windows middle of this list."},
            {"title": "A cheaper Dell XPS 13 is coming", "body": "Dell teased an XPS 13 around 599 to 699 dollars with a 2.5K touch display. If it ships as described it could shake up the value end of the list next month."},
            {"title": "Razer Blade 16 is the gaming pick", "body": "A genuinely thin 16-inch chassis with strong sustained performance keeps it at rank five for players who want one machine for games and work."},
        ],
    },
    {
        "commentary": (
            "Computex 2026 才剛落幕，這份榜單前段維持原樣，對現在想買的人來說反而是好事。MacBook Air M5 穩坐第一，原因很實際：日常收信、開一堆瀏覽器分頁、視訊會議全程安靜不發燙，電池撐一整個工作天還有餘裕，這就是大多數人真正需要的。"
            "這週最大的新聞是 Computex 上一票 Nvidia RTX Spark 筆電，包含 Microsoft Surface Laptop Ultra，加上 Intel Panther Lake 與 AMD Gorgon Point 處理器開始進到實際出貨的 Windows 機種。"
            "不過這影響的是榜單中段，不是前三名。Zenbook A16 跟 Dell XPS 14 靠續航跟做工還是站得住腳，我這次先按兵不動，因為這些真正全新的 RTX Spark 硬體還在陸續上市，得等實測出來才談得上誰往上移。"
            "Dell 還預告了一台更便宜的 XPS 13，大概台幣兩萬出頭，這塊是我接下來一個月最會盯的價位帶。Razer Blade 16 維持第五的電競定位，機身夠薄、長時間高負載效能也穩。"
            "講白了，2026 年 6 月這個時間點，想今天就入手的話，榜單前段就是你錢花得最安心的地方。Panther Lake 跟 RTX Spark 那些，除非你特別在意本機 AI 運算力，不然真的可以再等等看實測。"
        ),
        "highlights": [
            {"title": "MacBook Air M5 續坐第一", "body": "整天日常工作安靜不發熱，螢幕亮度跟色準都好，電池輕鬆撐過一個工作天。以這個價位來說，它還是最好推薦的一台。"},
            {"title": "Computex 2026 帶來 RTX Spark 筆電", "body": "Nvidia RTX Spark 機種，包含 Microsoft Surface Laptop Ultra 是這次焦點。本機 AI 看起來有料，但要等完整實測才會動到排名。"},
            {"title": "Panther Lake 與 Gorgon Point 開始出貨", "body": "Intel Core Ultra 第三代 Panther Lake 跟 AMD Gorgon Point Ryzen AI 進到實機，理論上會拉高榜單中段 Windows 機型的續航跟能效。"},
            {"title": "更便宜的 Dell XPS 13 要來了", "body": "Dell 預告一台約台幣兩萬出頭、配 2.5K 觸控螢幕的 XPS 13。真照規格出貨的話，下個月可能會搖動入門價位帶。"},
            {"title": "Razer Blade 16 是電競首選", "body": "16 吋機身做得夠薄，長時間高負載效能也穩，第五名的位置給想一台機器兼顧遊戲跟工作的人。"},
        ],
    },
)


# ---------------------------------------------------------------- TABLETS
build(
    "best-tablets.json",
    [
        {"title": "The best tablet 2026: the best iPad and Android tablets from Apple, OnePlus, Samsung and more", "url": "https://www.techradar.com/news/best-tablet", "source": "TechRadar"},
        {"title": "We've tested the best tablets in 2026 for all budgets and uses", "url": "https://www.tomsguide.com/best-picks/best-tablet", "source": "Tom's Guide"},
    ],
    {
        "commentary": (
            "The iPad Air M4 stays my pick for most people heading into June 2026, and the reasoning has not changed: it pairs a desktop-class M4 chip and 12GB of RAM with a price that undercuts the Pro, so it flies through editing, gaming and heavy multitasking without making you pay flagship money. "
            "The iPad Pro M5 sits just behind it at rank two because it is the better tablet on paper, the tandem OLED display is gorgeous, but the value math keeps the Air on top. "
            "On the Android side the Galaxy Tab S11 Ultra holds rank three on the strength of that 14.6-inch 2.9K AMOLED panel, which genuinely lets it work like a small laptop when you dock the keyboard. "
            "The story to watch is Samsung reviving the plus-sized model: a Galaxy Tab S12 Plus is rumored to bring a big screen and battery at a lower price than the Ultra, and if it lands it slots right into the gap above the mid-range. "
            "The OnePlus Pad 3 stays the fastest Android tablet here at rank four thanks to its Snapdragon 8 Elite chip and excellent battery life. "
            "Nothing in my searches this week justified moving anyone, so the order carries forward. If you want a tablet today, the iPad Air M4 is still the safest spend, and Android buyers who want a laptop replacement should look hard at the Tab S11 Ultra."
        ),
        "highlights": [
            {"title": "iPad Air M4 is the pick for most", "body": "An M4 chip and 12GB of RAM at a sub-Pro price means it handles editing, gaming and multitasking smoothly. The value keeps it at number one."},
            {"title": "iPad Pro M5 is the spec champion", "body": "The tandem OLED display is stunning and performance is the best in class, but the premium keeps it at rank two behind the better-value Air."},
            {"title": "Galaxy Tab S11 Ultra is the Android laptop replacement", "body": "Its 14.6-inch 2.9K AMOLED panel and keyboard dock let it stand in for a small laptop, which earns it the top Android slot at rank three."},
            {"title": "A Galaxy Tab S12 Plus is rumored", "body": "Samsung is expected to revive the plus-sized model with a large screen and battery below Ultra pricing. It would slot in above the mid-range if it ships."},
            {"title": "OnePlus Pad 3 is the fastest Android tablet", "body": "Snapdragon 8 Elite power and long battery life keep it at rank four as the value-focused Android performance pick."},
        ],
    },
    {
        "commentary": (
            "進到 2026 年 6 月，iPad Air M4 還是我給大多數人的首選，理由沒變：桌機等級的 M4 晶片配 12GB RAM，價格又壓在 Pro 之下，剪片、玩遊戲、開一堆 App 多工都順，不用花到旗艦的錢。"
            "iPad Pro M5 緊跟在第二，規格上它確實更強，雙層 OLED 螢幕真的漂亮，但算 CP 值 Air 還是贏。Android 這邊，Galaxy Tab S11 Ultra 穩坐第三，靠的是那塊 14.6 吋 2.9K AMOLED 面板，接上鍵盤真的能當小筆電用。"
            "接下來最值得盯的是三星要復活 Plus 尺寸：傳聞中的 Galaxy Tab S12 Plus 會帶來大螢幕跟大電池，價格又比 Ultra 低，真的出的話剛好補上中階以上那個空缺。"
            "OnePlus Pad 3 維持第四，是這裡最快的 Android 平板，Snapdragon 8 Elite 配上很猛的續航。這週我查到的消息都不足以動到任何人的排名，所以順序照舊。"
            "想今天就買的話，iPad Air M4 還是最安心的選擇；想用平板取代筆電的 Android 用戶，認真看一下 Tab S11 Ultra。"
        ),
        "highlights": [
            {"title": "iPad Air M4 是多數人首選", "body": "M4 晶片配 12GB RAM，價格又在 Pro 之下，剪片、遊戲、多工都順。CP 值讓它穩坐第一。"},
            {"title": "iPad Pro M5 是規格王", "body": "雙層 OLED 螢幕很驚豔，效能也是同級最強，但貴一截，第二名輸給更划算的 Air。"},
            {"title": "Galaxy Tab S11 Ultra 能當筆電用", "body": "14.6 吋 2.9K AMOLED 面板加鍵盤底座，真的能取代小筆電，所以拿下 Android 第一、總榜第三。"},
            {"title": "Galaxy Tab S12 Plus 有傳聞", "body": "三星預計復活 Plus 尺寸，大螢幕大電池又比 Ultra 便宜。真的出貨會卡進中階以上的位置。"},
            {"title": "OnePlus Pad 3 是最快 Android 平板", "body": "Snapdragon 8 Elite 加上長續航，第四名穩穩的，是重效能又顧荷包的 Android 選擇。"},
        ],
    },
)


# ---------------------------------------------------------------- KEYBOARDS
build(
    "best-mechanical-keyboards.json",
    [
        {"title": "Best Hall effect keyboards in 2026: the fastest, most customizable keyboards for competitive gaming", "url": "https://www.pcgamer.com/hardware/gaming-keyboards/best-hall-effect-keyboards/", "source": "PC Gamer"},
        {"title": "The 6 Best Gaming Keyboards of 2026", "url": "https://www.rtings.com/keyboard/reviews/best/by-usage/gaming", "source": "RTINGS"},
    ],
    {
        "commentary": (
            "Hall effect is the whole conversation in keyboards right now, and as of June 2026 Wooting still owns it. The Wooting 60HE keeps my top spot and the 80HE sits right behind it, and the reason is the software as much as the switches: Wootility is the most extensive yet genuinely easy-to-use analog tuning suite out there, and that is what turns adjustable actuation and rapid trigger from a spec sheet into something you actually feel in an FPS. "
            "Fresh data backs this up. In the ProSettings.net April 2026 dataset of 2,252 tracked pros, the 80HE is the second most-used board overall, which is remarkable for a small Dutch company. The Lekker V2 switches paired with true 8,000Hz Tachyon polling land input latency around 0.125ms, and that is about as fast as this category gets today. "
            "The SteelSeries Apex Pro TKL Wireless holds rank three as the best big-brand HE option with a polished OmniPoint feel, and the Keychron Q1 Pro stays the enthusiast pick at four for anyone who cares more about typing feel and a gasket-mounted aluminium build than raw analog speed. "
            "Nothing this week warranted a rank change, so the order carries forward. If you play competitive FPS, the 60HE or 80HE is the safest buy here, and the choice between them is simply whether you want a 60 percent or a tenkeyless layout."
        ),
        "highlights": [
            {"title": "Wooting 60HE stays number one", "body": "Lekker V2 analog switches plus the deep, friendly Wootility software make adjustable actuation and rapid trigger feel real in-game. The 60 percent layout keeps it at the top."},
            {"title": "Wooting 80HE is the pro favorite", "body": "It is the second most-used board among 2,252 tracked pros in ProSettings' April 2026 data, with true 8KHz Tachyon polling and roughly 0.125ms latency."},
            {"title": "SteelSeries Apex Pro TKL Wireless is the big-brand HE pick", "body": "Polished OmniPoint adjustable switches and solid software keep it at rank three for buyers who want a major-brand Hall effect board."},
            {"title": "Keychron Q1 Pro is the enthusiast choice", "body": "A gasket-mounted aluminium build and excellent typing feel keep it at rank four for people who value feel over raw analog speed."},
            {"title": "Layout is the only real decision at the top", "body": "Between the 60HE and 80HE the question is simply 60 percent versus tenkeyless. Both deliver the same class-leading analog performance."},
        ],
    },
    {
        "commentary": (
            "鍵盤現在的話題就是磁軸（Hall effect），到 2026 年 6 月，Wooting 還是王者。Wooting 60HE 維持我這邊第一，80HE 緊跟在後，重點除了軸體，更在軟體：Wootility 是目前最完整又真的好上手的類比調校工具，它把可調觸發行程跟 rapid trigger 從規格表變成你在 FPS 裡真的感覺得到的東西。"
            "有新數據撐腰。ProSettings.net 2026 年 4 月、追蹤 2,252 名職業選手的資料裡，80HE 是整體第二多人用的鍵盤，對一家荷蘭小公司來說很猛。Lekker V2 軸配上真正的 8,000Hz Tachyon 輪詢，輸入延遲壓到約 0.125ms，這已經是這個類別目前的天花板等級。"
            "SteelSeries Apex Pro TKL Wireless 守住第三，是大廠磁軸裡手感最成熟的選擇；Keychron Q1 Pro 維持第四的玩家定位，給那些更在意打字手感跟 gasket 鋁殼、而不是純類比速度的人。"
            "這週沒有值得動排名的消息，順序照舊。打競技 FPS 的話，60HE 或 80HE 是這裡最安心的選擇，兩者怎麼選就只是你要 60% 還是 TKL 配列而已。"
        ),
        "highlights": [
            {"title": "Wooting 60HE 穩坐第一", "body": "Lekker V2 類比軸加上又深又好用的 Wootility 軟體，讓可調觸發跟 rapid trigger 在遊戲裡真的有感。60% 配列把它留在頂端。"},
            {"title": "Wooting 80HE 是職業選手最愛", "body": "ProSettings 2026 年 4 月、2,252 名職業選手資料中第二多人用，真 8KHz Tachyon 輪詢，延遲約 0.125ms。"},
            {"title": "SteelSeries Apex Pro TKL Wireless 是大廠磁軸首選", "body": "成熟的 OmniPoint 可調軸加上紮實軟體，第三名給想要大廠磁軸鍵盤的人。"},
            {"title": "Keychron Q1 Pro 是玩家最愛", "body": "Gasket 鋁殼加上一流打字手感，第四名給重手感勝過純類比速度的人。"},
            {"title": "頂端唯一要選的就是配列", "body": "60HE 跟 80HE 之間，差別只在 60% 還是 TKL。兩者類比效能都是同級最強。"},
        ],
    },
)


# ---------------------------------------------------------------- GAMING MICE
build(
    "best-gaming-mice.json",
    [
        {"title": "The Razer DeathAdder V4 Pro is our top gaming mouse pick, but Logitech's Superstrike has our hearts", "url": "https://www.pcgamer.com/the-best-gaming-mouse/", "source": "PC Gamer"},
        {"title": "The 5 Best Razer Mice of 2026: Mouse Reviews", "url": "https://www.rtings.com/mouse/reviews/razer", "source": "RTINGS"},
    ],
    {
        "commentary": (
            "Gaming mice are having a genuinely great year, and June 2026 is where two different visions of the future sit side by side at the top. The Logitech G Pro X2 Superstrike keeps my number one slot because its haptic-inductive analog clicks are the fastest, most consistent main buttons I have used, and that click feel alone changes how a mouse responds. "
            "Right behind it the Razer side is heating up: the Viper V4 Pro has the spec sheet to take on anything, it is lighter than the DeathAdder V4 Pro and the build quality is close to flawless, and Razer's new FrameSync tech is the interesting wrinkle this week because it targets battery life, which is the one place flagship wireless mice still ask you to compromise. "
            "I keep the Viper V4 Pro at rank three and the DeathAdder V4 Pro at four, mirroring how reviewers now lean toward the lighter Viper, but the gap between them is tiny and grip shape will decide it for most people. "
            "The Lamzu Maya X and Pulsar X2 CL stay strong mid-list value picks because they deliver flagship sensors and sub-50-gram weights for noticeably less money. "
            "No major launch this week forced a reshuffle, so the order holds. If you want the absolute fastest clicks, the Superstrike is still it, and if you want pure lightweight wireless performance the Viper V4 Pro is the one I would buy."
        ),
        "highlights": [
            {"title": "Logitech Superstrike holds number one", "body": "Its haptic-inductive analog clicks are the fastest and most consistent main buttons available, which genuinely changes how the mouse responds in fast games."},
            {"title": "Razer Viper V4 Pro is the lightweight champ", "body": "A flagship spec sheet, lighter weight than the DeathAdder V4 Pro and near-flawless build keep it at rank three as the pure performance wireless pick."},
            {"title": "FrameSync targets battery life", "body": "Razer's new FrameSync tech on the Viper V4 Pro aims at battery endurance, addressing the last real compromise in flagship wireless mice."},
            {"title": "DeathAdder V4 Pro stays a top ergo option", "body": "It sits at rank four just behind the lighter Viper. For ergonomic-grip players the larger shape can still make it the better buy."},
            {"title": "Lamzu Maya X and Pulsar X2 CL are value stars", "body": "Both deliver flagship sensors and sub-50-gram weights for noticeably less money, holding strong mid-list value spots."},
        ],
    },
    {
        "commentary": (
            "電競滑鼠今年真的精彩，2026 年 6 月這個時間點，榜首正好擺著兩種未來路線。Logitech G Pro X2 Superstrike 維持我這邊第一，它的觸覺感應式類比微動是我用過最快、最一致的主鍵，光是這個點擊手感就改變了整隻滑鼠的反應。"
            "緊追在後的 Razer 這邊越來越熱：Viper V4 Pro 規格夠打天下，比 DeathAdder V4 Pro 還輕，做工幾乎無懈可擊，而這週的看點是 Razer 新的 FrameSync 技術，因為它瞄準的是電池續航，這正是旗艦無線滑鼠目前還要你妥協的地方。"
            "我把 Viper V4 Pro 放第三、DeathAdder V4 Pro 放第四，呼應現在評測普遍偏好較輕的 Viper，但兩者差距很小，多數人最後會看握感來決定。"
            "Lamzu Maya X 跟 Pulsar X2 CL 維持中段強力的 CP 值選擇，用明顯更低的價格給你旗艦感應器跟 50 克以下的重量。這週沒有重大新品逼著大洗牌，順序照舊。"
            "想要最快點擊就還是 Superstrike；想要純粹輕量無線效能，我會買 Viper V4 Pro。"
        ),
        "highlights": [
            {"title": "Logitech Superstrike 穩坐第一", "body": "觸覺感應式類比微動是目前最快、最一致的主鍵，在快節奏遊戲裡真的改變了滑鼠的反應方式。"},
            {"title": "Razer Viper V4 Pro 是輕量冠軍", "body": "旗艦規格、比 DeathAdder V4 Pro 更輕、做工幾近完美，第三名給純效能無線取向的人。"},
            {"title": "FrameSync 瞄準電池續航", "body": "Razer 在 Viper V4 Pro 上的新 FrameSync 主打續航，補上旗艦無線滑鼠最後一塊要妥協的地方。"},
            {"title": "DeathAdder V4 Pro 仍是人體工學首選", "body": "第四名，緊跟在較輕的 Viper 之後。偏好人體工學握法的人，較大的外型反而可能更合手。"},
            {"title": "Lamzu Maya X 與 Pulsar X2 CL 是 CP 值之星", "body": "兩者都用明顯更低的價格給你旗艦感應器跟 50 克以下重量，穩坐中段高 CP 值位置。"},
        ],
    },
)


# ---------------------------------------------------------------- GAMING MONITORS
build(
    "best-gaming-monitors.json",
    [
        {"title": "Best OLED Gaming Monitors 2026", "url": "https://www.tomshardware.com/monitors/gaming-monitors/best-oled-gaming-monitors", "source": "Tom's Hardware"},
        {"title": "The 5 Best OLED Monitors of 2026", "url": "https://www.rtings.com/monitor/reviews/best/oled", "source": "RTINGS"},
    ],
    {
        "commentary": (
            "The 27-inch 4K QD-OLED class is the sweet spot in gaming monitors right now, and the ASUS ROG Swift OLED PG27UCDM keeps my number one slot in June 2026 for exactly that reason: 4K at 240Hz on a fourth-gen QD-OLED panel, with Dolby Vision and a true full-speed DisplayPort 2.1 connection so you are not bottlenecked driving high frame rates. "
            "What is changing this month is competition at the value end of this same panel class. Dell's Alienware AW2725Q is now routinely the cheapest 27-inch 4K QD-OLED around, with a 900-dollar MSRP that dips to 800 or even 700 on sale, and BenQ's Mobiuz EX271UZ, a 27-inch 4K 240Hz True Black 400 model, landed on Amazon at the end of May. "
            "That pressure is good news for buyers and it is why I am watching the lower half of this list closely, but it does not move the podium yet because the new arrivals need full review testing first. "
            "The LG UltraGear 27GX790B holds rank two as the high-refresh alternative for competitive players, and the MSI MPG 341CQR ultrawide stays at three for anyone who wants immersion over raw pixel density. "
            "The order carries forward this week. If you want the best all-round gaming monitor today, the PG27UCDM is still the one, and bargain hunters should keep an eye on the AW2725Q during sales."
        ),
        "highlights": [
            {"title": "ASUS PG27UCDM holds number one", "body": "4K at 240Hz on a fourth-gen QD-OLED panel with Dolby Vision and full-speed DisplayPort 2.1 makes it the best all-round gaming monitor right now."},
            {"title": "Alienware AW2725Q is the value 4K OLED", "body": "Often the cheapest 27-inch 4K QD-OLED, its 900-dollar MSRP regularly drops to 800 or even 700 on sale, making it the bargain pick in this panel class."},
            {"title": "BenQ Mobiuz EX271UZ just arrived", "body": "A 27-inch 4K 240Hz True Black 400 OLED landed on Amazon at the end of May. It needs full review testing before it can challenge the top of the list."},
            {"title": "LG UltraGear 27GX790B is the high-refresh pick", "body": "It holds rank two as the alternative for competitive players who prioritize refresh rate and motion clarity."},
            {"title": "MSI MPG 341CQR is the ultrawide choice", "body": "It stays at rank three for players who want immersive width over the raw pixel density of a 27-inch 4K panel."},
        ],
    },
    {
        "commentary": (
            "27 吋 4K QD-OLED 現在是電競螢幕的甜蜜點，2026 年 6 月 ASUS ROG Swift OLED PG27UCDM 維持我這邊第一就是因為這個：第四代 QD-OLED 面板、4K 240Hz，支援 Dolby Vision，還有真正全速的 DisplayPort 2.1，推高更新率不會被頻寬卡住。"
            "這個月在變的是同級面板裡的低價競爭。Dell Alienware AW2725Q 現在常是最便宜的 27 吋 4K QD-OLED，原價約台幣兩萬七，特價時還會掉到更低；BenQ Mobiuz EX271UZ 這台 27 吋 4K 240Hz True Black 400 的機種，也在五月底上了 Amazon。"
            "這種價格壓力對買家是好事，也是我這次盯著榜單下半段的原因，但還動不到前三名，因為這些新機得先有完整實測。"
            "LG UltraGear 27GX790B 守住第二，是給競技玩家的高更新率選擇；MSI MPG 341CQR 帶魚螢幕維持第三，給重沉浸感勝過純像素密度的人。"
            "這週順序照舊。想今天就買最全能的電競螢幕，還是 PG27UCDM；想撿便宜的話，特價時盯緊 AW2725Q。"
        ),
        "highlights": [
            {"title": "ASUS PG27UCDM 穩坐第一", "body": "第四代 QD-OLED 面板、4K 240Hz，支援 Dolby Vision 與全速 DisplayPort 2.1，目前最全能的電競螢幕。"},
            {"title": "Alienware AW2725Q 是高 CP 值 4K OLED", "body": "常是最便宜的 27 吋 4K QD-OLED，特價時價格會明顯下殺，是這個面板等級的撿便宜首選。"},
            {"title": "BenQ Mobiuz EX271UZ 剛上市", "body": "27 吋 4K 240Hz True Black 400 的 OLED，五月底登上 Amazon。要先有完整實測才談得上挑戰榜首。"},
            {"title": "LG UltraGear 27GX790B 是高更新率選擇", "body": "守住第二，給重視更新率跟動態清晰度的競技玩家。"},
            {"title": "MSI MPG 341CQR 是帶魚螢幕之選", "body": "維持第三，給重沉浸感勝過 27 吋 4K 像素密度的玩家。"},
        ],
    },
)


# ---------------------------------------------------------------- GAMING HEADSETS
build(
    "best-gaming-headsets.json",
    [
        {"title": "Best gaming headsets in 2026: I'd bet my ears on these headphones", "url": "https://www.pcgamer.com/best-gaming-headset/", "source": "PC Gamer"},
        {"title": "The 6 Best Gaming Headsets of 2026", "url": "https://www.rtings.com/headphones/reviews/best/by-usage/gaming", "source": "RTINGS"},
    ],
    {
        "commentary": (
            "The top of the headset list is a genuine two-horse race in June 2026, and both horses are excellent. The SteelSeries Arctis Nova Pro Wireless keeps my number one slot because no other headset packs this many high-end features into one box: ANC with a transparency mode, simultaneous 2.4GHz and Bluetooth audio, dual USB for hopping between PC and console, and the hot-swap dual-battery dock that means you never wait to recharge. At around 380 dollars that combination is still unmatched for versatility. "
            "The Audeze Maxwell 2 sits right behind it at rank two and it is the one to buy if sound quality is your priority. Its planar magnetic drivers pull out detail that most gaming headsets simply cannot reproduce, it does 24-bit/96kHz low-latency wireless, and battery life runs past 80 hours with a fast charge that gives you 24 hours from a 20-minute top-up. "
            "Worth noting this week: SteelSeries' own Arctis Nova Elite exists as a 600-dollar flagship, but reviewers keep landing on the Maxwell 2 as the better-sounding, longer-lasting buy for nearly half the price, which is exactly why I keep the Maxwell at two rather than chasing the pricier option. "
            "The rest of the list carries forward unchanged. Pick the Nova Pro Wireless for features and console-hopping convenience, and the Maxwell 2 if you mainly care how it sounds."
        ),
        "highlights": [
            {"title": "SteelSeries Arctis Nova Pro Wireless holds number one", "body": "ANC with transparency, simultaneous 2.4GHz and Bluetooth, dual USB and a hot-swap battery dock pack more high-end features into one box than anything else at around 380 dollars."},
            {"title": "Audeze Maxwell 2 is the sound pick", "body": "Planar magnetic drivers reproduce detail most gaming headsets cannot, with 24-bit/96kHz wireless. It sits at rank two for audio-first buyers."},
            {"title": "Maxwell 2 battery is class-leading", "body": "Over 80 hours per charge with a fast top-up that delivers 24 hours of playback from 20 minutes, so it rarely leaves you stranded."},
            {"title": "Nova Elite exists but Maxwell 2 wins on value", "body": "SteelSeries' 600-dollar Arctis Nova Elite is impressive, yet reviewers favor the better-sounding, longer-lasting Maxwell 2 at nearly half the price."},
            {"title": "Pick by priority, not price", "body": "Choose the Nova Pro Wireless for features and seamless PC-to-console switching, and the Maxwell 2 if raw sound quality matters most."},
        ],
    },
    {
        "commentary": (
            "2026 年 6 月，耳機榜首是貨真價實的雙雄對決，而且兩台都很強。SteelSeries Arctis Nova Pro Wireless 維持我這邊第一，因為沒有別台把這麼多高階功能塞進一盒：ANC 加環境音模式、2.4GHz 與藍牙同時輸出、雙 USB 讓你在 PC 跟主機之間切換，還有可熱插拔的雙電池底座，等於永遠不用等充電。約台幣一萬二這個價位，這種全能性還是無人能比。"
            "Audeze Maxwell 2 緊跟第二，如果你最在意音質，買它就對了。平面振膜把大多數電競耳機根本還原不出來的細節挖出來，支援 24-bit/96kHz 低延遲無線，續航破 80 小時，快充 20 分鐘就能用 24 小時。"
            "這週值得一提：SteelSeries 自家還有一台台幣近兩萬的 Arctis Nova Elite 旗艦，但評測普遍還是回到 Maxwell 2，音質更好、續航更長，價格卻不到一半，這正是我把 Maxwell 留在第二、而不是去追更貴款的原因。"
            "榜單其餘維持不變。要功能跟跨主機切換方便就選 Nova Pro Wireless；主要在意聲音好不好聽就選 Maxwell 2。"
        ),
        "highlights": [
            {"title": "SteelSeries Arctis Nova Pro Wireless 穩坐第一", "body": "ANC 加環境音、2.4GHz 與藍牙同時輸出、雙 USB、熱插拔電池底座，約台幣一萬二這價位塞進的高階功能最多。"},
            {"title": "Audeze Maxwell 2 是音質之選", "body": "平面振膜還原出多數電競耳機做不到的細節，支援 24-bit/96kHz 無線。第二名給音質優先的人。"},
            {"title": "Maxwell 2 續航同級最強", "body": "單次充電破 80 小時，快充 20 分鐘換 24 小時播放，幾乎不會讓你斷電。"},
            {"title": "有 Nova Elite，但 Maxwell 2 贏在 CP 值", "body": "SteelSeries 台幣近兩萬的 Arctis Nova Elite 很厲害，但評測偏好音質更好、續航更長、價格不到一半的 Maxwell 2。"},
            {"title": "看需求選，不要只看價格", "body": "要功能跟 PC 主機無縫切換選 Nova Pro Wireless；最在意純音質就選 Maxwell 2。"},
        ],
    },
)


# ---------------------------------------------------------------- GAMING CHAIRS
build(
    "best-gaming-chairs.json",
    [
        {"title": "Best gaming chair in 2026: the seats I'd suggest for any PC gamer", "url": "https://www.pcgamer.com/best-gaming-chairs/", "source": "PC Gamer"},
        {"title": "Best Gaming Chair in 2026 — the top chairs for gamers for the money", "url": "https://www.tomshardware.com/best-picks/best-gaming-chairs", "source": "Tom's Hardware"},
    ],
    {
        "commentary": (
            "Gaming chairs do not move fast, and that steadiness is the story in June 2026. The Secretlab Titan Evo keeps my number one slot because after hundreds of hours of testing across reviewers it remains the chair that gets the fundamentals right: a genuinely supportive backrest, the magnetic head pillow and adjustable lumbar that actually help on long sessions, and build quality that holds up. At roughly 450 to 650 dollars depending on size and trim it is the chair I recommend to the most people. "
            "The Herman Miller Vantum holds rank two as the premium pick. It is the brand's first dedicated gaming chair, designed with Logitech, and at around 930 dollars it asks for a serious commitment, but the 12-year warranty and the fact that it doubles cleanly as a work chair justify the price for the right buyer. That warranty length, compared with the 2-to-5-year coverage typical of gaming chairs, is a real differentiator worth repeating. "
            "The Libernovo Omni stays at rank three as the standout newer ergonomic option, and the Razer Iskur V2 holds four for built-in lumbar support without office-chair pricing. "
            "Nothing this week justified a reshuffle, so the order carries forward. If you want one safe pick, the Titan Evo is it, and if budget is no object and you want a chair that lasts a decade, the Vantum earns the premium."
        ),
        "highlights": [
            {"title": "Secretlab Titan Evo holds number one", "body": "Hundreds of hours of testing keep it on top: a supportive backrest, genuinely helpful magnetic head pillow and adjustable lumbar, and durable build at 450 to 650 dollars."},
            {"title": "Herman Miller Vantum is the premium pick", "body": "The brand's first gaming chair, made with Logitech, holds rank two. At around 930 dollars it doubles as a work chair and carries a long warranty."},
            {"title": "A 12-year warranty sets the Vantum apart", "body": "Most gaming chairs cover 2 to 5 years. Herman Miller's 12-year warranty is a real reason to consider it a long-term investment."},
            {"title": "Libernovo Omni is the ergonomic standout", "body": "It stays at rank three as the newer ergonomic option for buyers who want adjustability beyond the racing-chair template."},
            {"title": "Razer Iskur V2 is value with real lumbar", "body": "It holds rank four for built-in lumbar support that works, without stepping up to office-chair pricing."},
        ],
    },
    {
        "commentary": (
            "電競椅本來就不太會大洗牌，而 2026 年 6 月的重點就是這份穩定。Secretlab Titan Evo 維持我這邊第一，因為經過各家評測上百小時實測，它還是把基本功做最好的那張：椅背支撐到位、磁吸頭枕跟可調腰靠在長時間久坐時真的有幫助、做工也耐用。視尺寸跟版本大約台幣一萬四到兩萬，是我會推薦給最多人的一張。"
            "Herman Miller Vantum 守住第二的高階定位。它是這個品牌第一張專屬電競椅，跟 Logitech 合作開發，約台幣兩萬八要下不小的決心，但 12 年保固加上能直接當辦公椅用，對對的人來說值這個價。這個保固長度，相較一般電競椅常見的 2 到 5 年，是真正的差異化，值得再講一次。"
            "Libernovo Omni 維持第三，是較新的人體工學亮點；Razer Iskur V2 守第四，內建腰靠又不用花到辦公椅的錢。"
            "這週沒有值得洗牌的消息，順序照舊。想要一張安心首選就是 Titan Evo；預算不是問題、又想要一張能撐十年的椅子，Vantum 值那個高價。"
        ),
        "highlights": [
            {"title": "Secretlab Titan Evo 穩坐第一", "body": "上百小時實測讓它續坐榜首：椅背支撐到位、磁吸頭枕與可調腰靠實用、做工耐用，約台幣一萬四到兩萬。"},
            {"title": "Herman Miller Vantum 是高階之選", "body": "品牌首張電競椅，與 Logitech 合作，第二名。約台幣兩萬八，能當辦公椅用，保固又長。"},
            {"title": "12 年保固是 Vantum 的差異點", "body": "多數電競椅只保 2 到 5 年。Herman Miller 的 12 年保固，是把它當長期投資的真實理由。"},
            {"title": "Libernovo Omni 是人體工學亮點", "body": "維持第三，是較新的人體工學選擇，給想要超越賽車椅框架、要更多可調性的人。"},
            {"title": "Razer Iskur V2 是有腰靠的高 CP 值選擇", "body": "守第四，內建好用的腰靠，又不用升級到辦公椅的價位。"},
        ],
    },
)


# ---------------------------------------------------------------- HANDHELDS  (rank change)
hh_d, _ = load("best-handheld-gaming-consoles.json")
hh_rankings = [dict(r, scores=dict(r["scores"])) for r in last_rankings(hh_d)]
# Steam Deck OLED took a $240 price hike in May 2026 (RAMageddon); trim its value/score
# and let ROG Xbox Ally X take rank 2. Conservative single swap grounded in dated event.
by_id = {r["id"]: r for r in hh_rankings}
sd = by_id["steam-deck-oled"]
ally = by_id["rog-xbox-ally-x"]
sd["rank"] = 3
sd["score"] = 8.9
sd["scores"]["value"] = round(sd["scores"]["value"] - 0.4, 1)
ally["rank"] = 2
hh_rankings.sort(key=lambda r: r["rank"])

build(
    "best-handheld-gaming-consoles.json",
    [
        {"title": "Best gaming handhelds 2026 ranked: Steam Deck, Xbox Ally X, Switch 2, Legion Go 2, MSI Claw 8 AI+, and more", "url": "https://www.windowscentral.com/gaming-best-gaming-handhelds", "source": "Windows Central"},
        {"title": "The best handheld gaming consoles in 2026 — our top recommendations", "url": "https://www.tomsguide.com/round-up/best-handheld-gaming-consoles", "source": "Tom's Guide"},
    ],
    {
        "commentary": (
            "There is real movement at the top this week, and it comes straight from a price tag. Valve raised the Steam Deck OLED's price by 240 dollars in May 2026, blaming the surge in memory and storage costs that the industry is calling RAMageddon, and that hike dents the one thing the Steam Deck always led on: value. So I am sliding it from rank two to rank three and trimming its score to 8.9, with the ROG Xbox Ally X stepping up to rank two. "
            "To be clear, the Steam Deck OLED is still a brilliant handheld and SteamOS remains more efficient and easier to live with than Windows, with a deep well of community optimizations, so this is a conservative nudge driven by the new price, not a knock on the hardware. "
            "The Nintendo Switch 2 keeps number one because for most people it is simply the best way to play games on the go: a 7.9-inch 1080p 120Hz screen, 256GB of storage, a custom Nvidia chip with 4K docked output, and a first-party library nothing else can touch. "
            "The ROG Xbox Ally X earns its bump on raw Windows-handheld power, with a Ryzen Z2 Extreme chip, 24GB of RAM and a fast 1TB SSD. The Lenovo Legion Go 2 and MSI Claw 8 AI Plus hold their spots below. As of June 2026 the right handheld depends on whether you want the biggest library, the most power, or the lowest running cost."
        ),
        "highlights": [
            {"title": "Steam Deck OLED price hike drops it to rank three", "body": "Valve raised the OLED model by 240 dollars in May 2026 over RAMageddon memory costs. That dents its value lead, so it moves from two to three with a trimmed 8.9 score."},
            {"title": "ROG Xbox Ally X steps up to rank two", "body": "A Ryzen Z2 Extreme chip, 24GB of RAM and a fast 1TB SSD make it the most powerful Windows handheld, and the Steam Deck price move opens the door."},
            {"title": "Nintendo Switch 2 holds number one", "body": "A 7.9-inch 1080p 120Hz screen, 256GB storage, custom Nvidia silicon with 4K docked output and an unmatched first-party library keep it on top for most people."},
            {"title": "SteamOS still wins on efficiency", "body": "Even after the price hike the Steam Deck OLED stays a brilliant handheld, with SteamOS running leaner than Windows and a deep library of community tweaks."},
            {"title": "Pick by your priority", "body": "Choose the Switch 2 for the library, the ROG Xbox Ally X for raw power, and the Steam Deck OLED for the lowest-friction PC handheld experience."},
        ],
    },
    {
        "commentary": (
            "這週榜首真的有變動，原因直接來自一個價格。Valve 在 2026 年 5 月把 Steam Deck OLED 漲了 240 美元，理由是業界俗稱 RAMageddon 的記憶體與儲存成本暴漲，這一漲，正好打在 Steam Deck 一向最強的那一點：CP 值。所以我把它從第二降到第三，分數修到 8.9，由 ROG Xbox Ally X 遞補到第二。"
            "先講清楚，Steam Deck OLED 還是一台很棒的掌機，SteamOS 也還是比 Windows 省電、好上手，社群最佳化又多，所以這只是因應新價格的保守微調，不是嫌它硬體不好。"
            "Nintendo Switch 2 維持第一，因為對大多數人來說它就是出門玩遊戲最好的選擇：7.9 吋 1080p 120Hz 螢幕、256GB 儲存、客製 Nvidia 晶片支援接電視 4K 輸出，加上沒人比得上的第一方遊戲陣容。"
            "ROG Xbox Ally X 靠純 Windows 掌機效能拿下這次的遞補，Ryzen Z2 Extreme 晶片、24GB RAM、快速 1TB SSD。Lenovo Legion Go 2 跟 MSI Claw 8 AI Plus 維持下方位置。2026 年 6 月，怎麼選掌機就看你要最大遊戲庫、最強效能、還是最低的使用成本。"
        ),
        "highlights": [
            {"title": "Steam Deck OLED 漲價，掉到第三", "body": "Valve 2026 年 5 月因 RAMageddon 記憶體成本把 OLED 版漲 240 美元，CP 值優勢被削，從第二降到第三，分數修到 8.9。"},
            {"title": "ROG Xbox Ally X 遞補到第二", "body": "Ryzen Z2 Extreme 晶片、24GB RAM、快速 1TB SSD，是最強的 Windows 掌機，Steam Deck 漲價剛好給它機會。"},
            {"title": "Nintendo Switch 2 穩坐第一", "body": "7.9 吋 1080p 120Hz 螢幕、256GB 儲存、客製 Nvidia 晶片支援 4K 接電視，加上無人能及的第一方陣容，對多數人就是最好。"},
            {"title": "SteamOS 仍贏在省電", "body": "就算漲價，Steam Deck OLED 還是一台很棒的掌機，SteamOS 比 Windows 精簡，社群調校也多。"},
            {"title": "看需求選掌機", "body": "要遊戲庫選 Switch 2，要純效能選 ROG Xbox Ally X，要最低使用門檻的 PC 掌機就選 Steam Deck OLED。"},
        ],
    },
    rankings=hh_rankings,
)

print("DONE")
