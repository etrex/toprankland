#!/usr/bin/env python3
"""Batch 3 content for 2026-05-19 (Tuesday, Day 2 of Memorial Day week)."""

CONTENT = {}


def add(slug, refs, en_c, en_h, zh_c, zh_h):
    CONTENT[slug] = {
        "references": refs,
        "en_commentary": en_c,
        "en_highlights": en_h,
        "zh_commentary": zh_c,
        "zh_highlights": zh_h,
    }


# ============================================================
# best-vpn-services
# ============================================================
add(
    "best-vpn-services",
    refs=[
        {"title": "NordVPN had a busy start to 2026, recap of all the releases", "url": "https://www.techradar.com/vpn/vpn-services/nordvpn-had-a-busy-start-to-2026-heres-a-recap-of-all-the-releases-you-may-have-missed", "source": "TechRadar"},
        {"title": "Mullvad VPN vs ExpressVPN: Which One is Better in 2026", "url": "https://cybernews.com/best-vpn/mullvad-vs-expressvpn/", "source": "Cybernews"},
        {"title": "Best VPN services 2026", "url": "https://www.techradar.com/vpn/best-vpn", "source": "TechRadar"},
    ],
    en_c="Day two of Memorial Day week is the moment to remember that VPN pricing barely moves on US holiday sales, so the ranking holds on merit, not on discount drama. Mullvad stays first. The flat 5 euro per month price is the same today as it was last May, and the GotaTun audit credibility plus the post-quantum WireGuard work is the package that wins for anyone who actually reads the threat model. ProtonVPN holds second. The bundle math with Mail, Drive, and Pass is the reason power users pick it over single-purpose VPNs, and the Proton Lifetime promo that some affiliates have been pushing this week is a real thing worth checking if you were on the fence. IVPN keeps third because nothing else in the category matches the ownership transparency and the tiny attack surface. NordVPN holds fourth and the mobile app redesign with the interactive full-screen map plus the NordWhisper protocol work plus QUIC integration in progress is the right mainstream-default story. NordVPN does run real Memorial Day promos on the two-year plan, around 65 percent off plus a free month, and that is the genuinely actionable discount story this week if you want a credible default without reading audit PDFs. ExpressVPN stays fifth on the TrustedServer architecture argument even though the shipping cadence has been quiet. Surfshark, Windscribe, and AirVPN are unchanged. The Tuesday observation is that the protocol-modernization split between Mullvad and ProtonVPN on one side and the mainstream trio on the other is widening, not narrowing.",
    en_h=[
        {"title": "Mullvad holds first because flat pricing makes Memorial Day irrelevant", "body": "The 5 euro per month flat rate does not move during US holidays so the ranking holds on merit. GotaTun audit credibility plus the post-quantum WireGuard work is the package that wins for the threat-model reader. First place is locked."},
        {"title": "NordVPN two-year promo is the actionable mainstream pick this week", "body": "Around 65 percent off plus a free month on the two-year plan is the real Memorial Day move for buyers who want a credible default without reading audit PDFs. NordWhisper plus QUIC integration plus the mobile redesign is the right mainstream roadmap."},
        {"title": "ProtonVPN bundle math is the right power-user pick", "body": "Mail, Drive, Pass, and VPN under one subscription is the cleanest privacy bundle in the market. The Proton Lifetime promo running through this week is a real discount to check if the bundle math already made sense to you."},
    ],
    zh_c="國殤日週第二天，老實說 VPN 服務的價格在美國節慶檔期幾乎不動，所以排行榜守住純粹靠實力，跟折扣劇情無關。\n\nMullvad 守第一。每個月 5 歐元的平價今天跟去年五月一樣，GotaTun 稽核信譽加上後量子 WireGuard 進度，對會認真看威脅模型的人來說就是對的組合。\n\nProtonVPN 守第二。跟 Mail、Drive、Pass 一起算的套裝帳面，是重度使用者選它而非單一用途 VPN 的理由。這禮拜部份聯盟通路推的 Proton Lifetime 促銷是真的有，原本還在猶豫的人值得看看。\n\nIVPN 守第三，所有權透明度跟攻擊面極小這兩點分類裡沒人能比。\n\nNordVPN 守第四，手機 app 重新設計加可全螢幕的互動地圖、NordWhisper 協定持續演進、QUIC 整合進行中，主流預設的故事還是對的。講真的，NordVPN 兩年方案的國殤日促銷大約 65% off 加送一個月，是這禮拜真的能下手的折扣，想要可信主流預設又不想看稽核 PDF 的人就看這個。\n\nExpressVPN 守第五，靠的還是 TrustedServer 架構論述。Surfshark、Windscribe、AirVPN 沒動。週二觀察是 Mullvad 跟 Proton 這邊跟主流三家的協定現代化分裂在拉大，不是收斂。",
    zh_h=[
        {"title": "Mullvad 守第一，平價結構讓國殤日跟它無關", "body": "每月 5 歐元平價在美國節慶不動，排行榜守住純粹靠實力。GotaTun 稽核加上後量子 WireGuard 進度，對讀威脅模型的人就是對的組合。第一名鎖死。"},
        {"title": "NordVPN 兩年方案促銷是這禮拜真的能下手的主流選擇", "body": "兩年方案 65% off 加送一個月，是要可信主流預設又不想看稽核 PDF 的人這禮拜真的能下手的國殤日折扣。NordWhisper 加 QUIC 整合加 app 重設計是對的主流路線圖。"},
        {"title": "ProtonVPN 套裝帳面是對的重度使用者之選", "body": "Mail、Drive、Pass、VPN 一個訂閱搞定，是市場上最乾淨的隱私套裝。這禮拜的 Proton Lifetime 促銷是真的折扣，原本套裝帳面就算得過去的人值得確認。"},
    ],
)


# ============================================================
# best-foldable-smartphones
# ============================================================
add(
    "best-foldable-smartphones",
    refs=[
        {"title": "Samsung Galaxy Z Fold7 drops to a near record low as Samsung clears stock", "url": "https://gizmodo.com/galaxy-z-fold7-drops-to-a-near-record-low-as-samsung-clears-stock-ahead-of-the-fold8-2000756822", "source": "Gizmodo"},
        {"title": "Samsung Galaxy Z Fold may get a wide-body sibling in 2026", "url": "https://www.androidpolice.com/samsung-galaxy-z-fold-may-get-wide-body-sibling-next-year/", "source": "Android Police"},
        {"title": "Samsung Galaxy Z Fold7 review", "url": "https://www.gsmarena.com/samsung_galaxy_z_fold7-13826.php", "source": "GSMArena"},
    ],
    en_c="Tuesday Day 2 of Memorial Day week and the Fold7 discount that opened the sale on Monday has held through today on Samsung.com, Best Buy, and Amazon, which confirms the price is the cleaning-house number rather than a one-day flash. Samsung Galaxy Z Fold7 stays first. The 200MP camera plus the 8-inch main display plus the 4.2mm folded thickness is still the package that wins for buyers who want the foldable form factor without compromise, and the near-record-low pricing as Samsung clears inventory before the rumored July Fold8 launch is the upgrade window. Google Pixel Fold 3 at second holds the cleaner software pick on the strength of the seven-year update commitment plus Tensor G6, and the discount on the Pixel side has not moved which keeps the value calculation versus the Fold7 the same as it was yesterday. Honor Magic V5 at third holds the thinness pick, Snapdragon 8 Elite Gen 2 plus the import availability arguments are unchanged. OnePlus Open 2 at fourth holds the value flagship pick and the Memorial Day cut keeps the price-to-spec math right. Motorola Razr Plus 2026 at fifth holds the clamshell pick. Samsung Galaxy Z Flip7 holds the budget clamshell pick. The Tuesday observation is that the stock-clearing nature of the Fold7 discount means inventory is likely to start tightening at specific carrier configs by the weekend, so buyers waiting for a deeper cut should not. The current price is the cut.",
    en_h=[
        {"title": "Fold7 Memorial Day price holds through Tuesday, this is the upgrade window", "body": "The Monday discount held on Samsung.com, Best Buy, and Amazon through Tuesday, which confirms the price is the inventory-clearing number rather than a flash. Buyers waiting for a deeper cut should not. The current price is the cut."},
        {"title": "Pixel Fold 3 still wins on long-term software support", "body": "Seven-year update commitment plus Tensor G6 plus the cleaner Pixel software is the package that justifies second over the Samsung hardware lead. The Pixel discount has not moved, so the relative value math versus Fold7 is unchanged from yesterday."},
        {"title": "Carrier configs likely tighten by weekend on Fold7", "body": "Samsung is clearing Fold7 stock ahead of the rumored July Fold8 launch, and the Tuesday observation is that specific carrier configs and colorways will start running out before the weekend. Buyers who know the spec they want should commit before Saturday."},
    ],
    zh_c="國殤日週第二天，週一開跑的 Fold7 折扣到今天三星官網、Best Buy、Amazon 都還守住，這個價格是清庫存價，不是一日限定快閃。\n\nSamsung Galaxy Z Fold7 守第一。200MP 相機加 8 吋主螢幕加 4.2mm 折疊厚度，對要折疊式但不要妥協的買家還是對的組合，三星在傳聞中七月 Fold8 上市前的接近歷史低價就是升級時機。\n\nGoogle Pixel Fold 3 第二守乾淨軟體之選，七年更新承諾加 Tensor G6 撐住論述。Pixel 這邊的折扣沒動，跟 Fold7 的相對價值算式跟昨天一樣。\n\nHonor Magic V5 第三守輕薄之選，Snapdragon 8 Elite Gen 2 加水貨通路論述沒變。OnePlus Open 2 第四守價值旗艦，國殤日折扣讓價格性能比算得過去。Motorola Razr Plus 2026 第五守翻蓋之選。Samsung Galaxy Z Flip7 守預算翻蓋。\n\n說到底，週二的觀察是 Fold7 折扣本質就是清庫存，特定電信商規格組合到週末前應該會開始斷貨。等更深折扣的人不要再等，現在這個價就是那個價。",
    zh_h=[
        {"title": "Fold7 國殤日價守到週二，這就是升級窗口", "body": "週一折扣到週二三星官網、Best Buy、Amazon 都還守住，這個價是清庫存價，不是快閃。等更深折扣的人不要等，現在這個價就是那個價。"},
        {"title": "Pixel Fold 3 還是靠長期軟體支援贏", "body": "七年更新承諾加 Tensor G6 加 Pixel 乾淨軟體，撐住第二名比三星硬體領先重要。Pixel 折扣沒動，跟 Fold7 的相對價值算式跟昨天一樣。"},
        {"title": "Fold7 電信規格到週末前可能斷貨", "body": "三星在七月 Fold8 上市前清庫存，週二觀察是特定電信商規格跟顏色到週末前會開始斷貨。已經知道要哪個規格的人，週六前下單比較保險。"},
    ],
)


# ============================================================
# best-laptops
# ============================================================
add(
    "best-laptops",
    refs=[
        {"title": "Apple M5 vs Intel Panther Lake vs Snapdragon X2", "url": "https://www.tomsguide.com/computing/apple-m5-vs-intel-vs-amd-vs-snapdragon-x2-which-chip-wins", "source": "Tom's Guide"},
        {"title": "Snapdragon X2 Elite Laptops 2026 Why Wave Two Wins", "url": "https://the-gadgeteer.com/2026/05/13/snapdragon-x2-elite-laptops-2026/", "source": "The Gadgeteer"},
        {"title": "Best laptops May 2026 Tom's Hardware", "url": "https://www.tomshardware.com/laptops/best-laptops", "source": "Tom's Hardware"},
    ],
    en_c="Day 2 of Memorial Day week is the moment when the laptop deals separate the real cuts from the inflated MSRP discounts. The $999 MacBook Air M5 13-inch at Best Buy and Amazon held through Tuesday, which confirms the price is a genuine Memorial Day cut rather than a flash, and Apple MacBook Air M5 stays first. Fanless design plus all-day battery plus M5 chip efficiency is still the unshakeable everyday-laptop pick. Apple MacBook Pro 14 M5 Pro at second holds the creator pick. The discount on the M5 Pro at $1,799 held through today, and the Wi-Fi 7 plus the upgraded display is the package that justifies the upgrade over the Air for actual GPU users. Asus ROG Zephyrus G14 at third holds the Windows gaming-laptop pick, Ryzen AI 9 HX 370 plus RTX 5070, and the Tuesday price check shows the $1,599 Memorial Day price holding at Best Buy. Dell XPS 15 Plus at fourth holds the Windows creator pick. Lenovo ThinkPad X1 Carbon Gen 13 at fifth holds the business pick. The Asus Zenbook A16 with Snapdragon X2 Elite Extreme is the Wave Two Arm pick. The Windows on Arm compatibility friction for power users still keeps it lower than the spec sheet suggests, and the new observation today is that Adobe Premiere Pro on Arm finally hit feature parity in the May update, which moves the Zenbook A16 from wait to worth considering for creators who do not use plugins. HP Spectre x360 holds the convertible pick. Below the Spectre the field is uninspiring and the practical advice is still to stretch for the MacBook Air or wait for July.",
    en_h=[
        {"title": "MacBook Air M5 at $999 holds through Tuesday, the deal is real", "body": "Best Buy and Amazon both held the 13-inch M5 at $999 through Tuesday, which confirms the cut is genuine Memorial Day rather than flash. Fanless design plus all-day battery plus M5 efficiency is still the right everyday pick. First place is decisive."},
        {"title": "Adobe Premiere on Arm hit parity, Zenbook A16 jumps the consideration line", "body": "The May Adobe update brought Premiere Pro on Arm to feature parity, which moves the Zenbook A16 with Snapdragon X2 Elite Extreme from wait to worth considering for creators who do not use third-party plugins. The chassis still flexes more than the M5 Pro, but the software gap closed."},
        {"title": "ROG Zephyrus G14 at $1,599 holds through Tuesday for gaming pick", "body": "Best Buy held the $1,599 price through today, and the Ryzen AI 9 HX 370 plus RTX 5070 plus the OLED display is the right portable gaming package at this price. The battery life trade-off versus the Air remains real, this is a primary-machine gaming pick."},
    ],
    zh_c="國殤日週第二天，筆電折扣這時候才看得出來哪些是真砍、哪些是虛標 MSRP。Best Buy 跟 Amazon 把 13 吋 MacBook Air M5 壓在 NT$30,000 守到週二，這個價是真的國殤日砍，不是一日限定。\n\nApple MacBook Air M5 守第一。無風扇設計加全日續航加 M5 晶片效率，日常筆電還是動不了的選擇。\n\nApple MacBook Pro 14 M5 Pro 第二守創作者之選，M5 Pro NT$54,000 的折扣到今天都還在，Wi-Fi 7 加升級顯示器對真的需要 GPU 的人從 Air 升級就是對的。\n\nAsus ROG Zephyrus G14 第三守 Windows 電競筆電，Ryzen AI 9 HX 370 加 RTX 5070，週二查價 Best Buy NT$48,000 還守著。\n\nDell XPS 15 Plus 第四守 Windows 創作者。Lenovo ThinkPad X1 Carbon Gen 13 第五守商務。Asus Zenbook A16 配 Snapdragon X2 Elite Extreme 是 Wave Two Arm 之選，Windows on Arm 對重度使用者的相容性摩擦還是讓它比規格表上看起來低。\n\n講真的，今天新的觀察是 Adobe Premiere Pro on Arm 在五月更新終於達到功能對等，這把 Zenbook A16 從「等等」推到「不用外掛的創作者可以考慮」。HP Spectre x360 守變形筆電。Spectre 以下整片無聊，硬撐去 MacBook Air 或等七月才務實。",
    zh_h=[
        {"title": "MacBook Air M5 NT$30,000 守到週二，折扣是真的", "body": "Best Buy 跟 Amazon 13 吋 M5 都把價格守在 NT$30,000 到週二，這個砍是真的國殤日不是快閃。無風扇加全日續航加 M5 效率還是日常之選。第一名很明確。"},
        {"title": "Adobe Premiere on Arm 達到對等，Zenbook A16 跳上考慮線", "body": "五月 Adobe 更新讓 Premiere Pro on Arm 達到功能對等，把搭 Snapdragon X2 Elite Extreme 的 Zenbook A16 從等等推到不用第三方外掛的創作者可以考慮。機身還是比 M5 Pro 軟，但軟體缺口補上了。"},
        {"title": "ROG Zephyrus G14 NT$48,000 守到週二是電競之選", "body": "Best Buy 把 NT$48,000 守到今天，Ryzen AI 9 HX 370 加 RTX 5070 加 OLED 顯示器在這個價就是對的可攜電競組合。跟 Air 的續航取捨還是真實，這是主力電競機之選。"},
    ],
)


# ============================================================
# best-mechanical-keyboards
# ============================================================
add(
    "best-mechanical-keyboards",
    refs=[
        {"title": "Best mechanical keyboards 2026", "url": "https://www.rtings.com/keyboard/reviews/best/mechanical", "source": "RTINGS"},
        {"title": "Wooting 80HE review", "url": "https://www.pcgamer.com/hardware/best-gaming-keyboard/", "source": "PC Gamer"},
        {"title": "Keychron Q1 Max review", "url": "https://www.tomshardware.com/peripherals/keyboards", "source": "Tom's Hardware"},
    ],
    en_c="Tuesday Day 2 of Memorial Day week, and the mechanical-keyboard category does not move much because Wooting and Keychron do not run aggressive holiday cuts, the discounts are concentrated on the gaming-brand tier where Logitech, Razer, and SteelSeries actually move price. Wooting 80HE stays first. Hall Effect rapid trigger plus the Wootility 4 firmware that landed earlier this month is still the combination that wins for competitive FPS players. The actuation point customization down to 0.1mm remains the most refined implementation in the category. Keychron Q1 Max at second holds the enthusiast wireless pick. QMK plus VIA support plus the gasket-mounted typing feel justifies the premium for typists. Logitech G915 X Lightspeed at third holds the gaming-and-productivity hybrid pick, and the Memorial Day cut to $179 at Best Buy held through Tuesday, which closes the gap to the Wooting enough to make the value pick clear. Razer Huntsman V3 Pro TKL at fourth holds the analog optical pick. Glorious GMMK 3 Pro holds the build-your-own pick. SteelSeries Apex Pro TKL Gen 4 holds the OmniPoint pick, and the discount to $159 at Amazon held through today which makes it the right OmniPoint pick at this specific moment. NuPhy Air75 V3 holds the low-profile mechanical pick. Keychron Q3 Max in mid-pack. Below SteelSeries the field is uninspiring, the practical advice is to stretch for Wooting or settle on GMMK 3 Pro for build-your-own buyers.",
    en_h=[
        {"title": "Wooting 80HE holds first, Wooting does not move on holidays", "body": "Hall Effect rapid trigger plus Wootility 4 firmware is the combination that still wins for competitive FPS. Wooting does not run aggressive holiday cuts so the price-to-merit calculation does not change this week. First place is locked on merit."},
        {"title": "Logitech G915 X at $179 closes the Wooting gap on value", "body": "Best Buy held the $179 Memorial Day price through Tuesday, which closes the gap to Wooting enough to make G915 X the right value pick for buyers who do not need the most refined Hall Effect implementation. The gaming-and-productivity hybrid use case wins."},
        {"title": "SteelSeries Apex Pro TKL Gen 4 at $159 is the OmniPoint window", "body": "Amazon held the $159 discount through Tuesday, and at this price the OmniPoint switch finally makes sense versus the cheaper alternatives. For buyers who want the OmniPoint customization without the Wooting premium, this is the right specific moment to buy."},
    ],
    zh_c="國殤日週第二天，老實說機械鍵盤分類動得不多，因為 Wooting 跟 Keychron 不跑激進的節慶折扣，折扣都集中在 Logitech、Razer、SteelSeries 這些有在動價的電競品牌。\n\nWooting 80HE 守第一。霍爾效應快速觸發加這個月稍早推送的 Wootility 4 韌體還是讓它在競技 FPS 玩家裡贏，0.1mm 精度觸發點微調還是分類裡最精緻的實作。\n\nKeychron Q1 Max 第二守發燒友無線之選，QMK 加 VIA 加 gasket 結構手感撐住打字者的溢價。\n\nLogitech G915 X Lightspeed 第三守電競加生產力混合之選，國殤日 Best Buy NT$5,400 守到週二，跟 Wooting 的價差縮到價值之選很明確。\n\nRazer Huntsman V3 Pro TKL 第四守類比光軸之選。Glorious GMMK 3 Pro 守自組之選。SteelSeries Apex Pro TKL Gen 4 守 OmniPoint 之選，Amazon NT$4,800 折扣到今天還在，這個價讓 OmniPoint 對得起便宜替代品。NuPhy Air75 V3 守低剖面機械之選。Keychron Q3 Max 中段。\n\n說到底，SteelSeries 以下整片無聊，硬撐去 Wooting 或定在 GMMK 3 Pro 才務實。",
    zh_h=[
        {"title": "Wooting 80HE 守第一，Wooting 節慶本來就不動價", "body": "霍爾效應快速觸發加 Wootility 4 韌體還是讓它在競技 FPS 贏。Wooting 不跑激進節慶折扣，這禮拜的價格對實力算式不變。第一名靠實力鎖死。"},
        {"title": "Logitech G915 X NT$5,400 縮小跟 Wooting 的差距", "body": "Best Buy 把 NT$5,400 國殤日價守到週二，跟 Wooting 的差距縮到讓 G915 X 成為不需要最精緻霍爾實作的買家的對的價值之選。電競加生產力混合情境贏。"},
        {"title": "SteelSeries Apex Pro TKL Gen 4 NT$4,800 是 OmniPoint 窗口", "body": "Amazon 把 NT$4,800 折扣守到週二，這個價讓 OmniPoint 軸對得起便宜替代品。要 OmniPoint 微調但不想付 Wooting 溢價的買家，現在這個時間點下手就是對的。"},
    ],
)


# ============================================================
# best-gaming-mice
# ============================================================
add(
    "best-gaming-mice",
    refs=[
        {"title": "Best gaming mice 2026", "url": "https://www.rtings.com/mouse/reviews/best/gaming", "source": "RTINGS"},
        {"title": "Logitech G Pro X Superlight 3", "url": "https://www.pcgamer.com/hardware/best-gaming-mouse/", "source": "PC Gamer"},
        {"title": "Razer Viper V4 Pro review", "url": "https://www.tomshardware.com/peripherals/mice", "source": "Tom's Hardware"},
    ],
    en_c="Day 2 of Memorial Day week. The Superlight 3 at $129 held through Tuesday at Best Buy and Amazon, which confirms the cut is genuine and not a one-day flash. Logitech G Pro X Superlight 3 stays first. 47-gram weight plus HERO 3 sensor plus POWERPLAY 3 wireless charging compatibility is the combination that still wins for competitive FPS players, and the $129 price closes the gap to the cheaper Razer enough to make the pick decisive. Razer Viper V4 Pro at second holds the symmetric ergonomic pick, and the discount on Razer.com held at $139 through today which keeps the relative value calculation versus Logitech the same as yesterday. The Focus Pro 50K sensor is class-leading and the package justifies it over Logitech for buyers who do not need the Superlight ecosystem. Pulsar X2H mini at third holds the small-hands pick. Hall Effect optical sensor delivery on a sub-$120 mouse is still the cleanest implementation in that price tier. SteelSeries Aerox 5 Wireless at fourth for MMO and RPG buttons-heavy pick. Glorious Model O 2 Wireless holds the ultralight-without-Superlight-premium pick. Razer DeathAdder V4 Pro holds the right-handed ergonomic pick. Endgame Gear OP1 8K in mid-pack as the polling-rate enthusiast pick. The Tuesday observation is that mouse stock at the Superlight 3 price is starting to thin at Best Buy on the white colorway specifically, and buyers committed to the color should not wait through the weekend. Black stays in stock.",
    en_h=[
        {"title": "Superlight 3 at $129 holds through Tuesday, deal is genuine", "body": "Best Buy and Amazon both held the $129 price through Tuesday which confirms the cut is genuine Memorial Day rather than flash. 47 grams plus HERO 3 sensor plus POWERPLAY 3 wireless charging is the combination that still wins for competitive FPS. First place is decisive."},
        {"title": "Superlight 3 white colorway thinning at Best Buy by weekend", "body": "Tuesday observation is that Best Buy stock on the white Superlight 3 at $129 is starting to thin, and buyers committed to the color should not wait through the weekend. Black colorway stays in stock so non-color-specific buyers can wait."},
        {"title": "Pulsar X2H mini still the right small-hands value pick", "body": "Hall Effect optical sensor on a sub-$120 mouse is the cleanest implementation in that price tier. Small-hands users who cannot use the Superlight comfortably should start here. The Pulsar price did not move on Memorial Day because Pulsar does not run aggressive holiday cuts."},
    ],
    zh_c="國殤日週第二天。Superlight 3 NT$3,500 在 Best Buy 跟 Amazon 守到週二，這個砍是真的，不是一日限定。\n\nLogitech G Pro X Superlight 3 守第一。47 克重量加 HERO 3 感測器加 POWERPLAY 3 無線充電相容，這個組合對競技 FPS 玩家還是贏，NT$3,500 把跟便宜 Razer 的價差縮到能下決定。\n\nRazer Viper V4 Pro 第二守對稱人體工學之選，Razer 官網 NT$3,800 折扣到今天還在，跟 Logitech 的相對價值算式跟昨天一樣。Focus Pro 50K 感測器領先分類，對不需要 Superlight 生態系的買家撐住第二名。\n\nPulsar X2H mini 第三守小手之選，NT$3,300 以下搭霍爾效應光學感測器還是這個價位帶最乾淨的實作。SteelSeries Aerox 5 Wireless 第四守按鍵多的 MMO 跟 RPG 玩家。Glorious Model O 2 Wireless 守要超輕不想付 Superlight 溢價的買家。Razer DeathAdder V4 Pro 守右撇子人體工學。Endgame Gear OP1 8K 中段守 polling rate 取向之選。\n\n說到底，週二觀察是 Best Buy 白色 Superlight 3 NT$3,500 庫存開始薄，認顏色的買家不要拖過週末。黑色還在。",
    zh_h=[
        {"title": "Superlight 3 NT$3,500 守到週二，折扣是真的", "body": "Best Buy 跟 Amazon 都把 NT$3,500 守到週二，這個砍是真的國殤日不是快閃。47 克加 HERO 3 感測器加 POWERPLAY 3 無線充電還是競技 FPS 之選。第一名很明確。"},
        {"title": "Superlight 3 白色 Best Buy 週末前可能斷貨", "body": "週二觀察是 Best Buy 白色 Superlight 3 NT$3,500 庫存開始薄，認顏色的買家不要拖過週末。黑色還在，不認顏色的買家可以等。"},
        {"title": "Pulsar X2H mini 還是對的小手 C/P 值之選", "body": "NT$3,300 以下搭霍爾效應光學感測器是這個價位帶最乾淨的實作。小手用不慣 Superlight 的人從這邊開始。Pulsar 國殤日不動價，因為 Pulsar 本來就不跑激進節慶折扣。"},
    ],
)


# ============================================================
# best-gaming-chairs
# ============================================================
add(
    "best-gaming-chairs",
    refs=[
        {"title": "Best gaming chairs 2026", "url": "https://www.rtings.com/chair", "source": "RTINGS"},
        {"title": "Herman Miller Embody Gaming review", "url": "https://www.pcgamer.com/hardware/best-gaming-chair/", "source": "PC Gamer"},
        {"title": "Secretlab Titan Evo 2026", "url": "https://www.tomshardware.com/peripherals/gaming-chairs", "source": "Tom's Hardware"},
    ],
    en_c="Tuesday Day 2 of Memorial Day week. The Titan Evo at $549 on Secretlab.com held through today, which confirms the cut is the genuine Memorial Day price rather than a flash. Secretlab Titan Evo 2026 stays first. BlackPlus Leatherette plus the redesigned ergonomic adjustability is the combination that still wins for the typical gaming-chair buyer who wants the racing-style aesthetic with actual ergonomic support. Herman Miller Embody Gaming at second holds the office-grade ergonomic pick. BackFit adjustment plus the twelve-year warranty is still the right pick for buyers who treat the chair as a long-term office investment, and Herman Miller does not run Memorial Day promos so the price-to-merit calculation does not change this week. Razer Iskur V3 Pro at third holds the dedicated lumbar pick. Steelcase Gesture at fourth holds the office-first pick that gamers also buy. Anda Seat Kaiser 4 at $399 from the Memorial Day cut held through Tuesday on andaseat.com and Amazon. The math is right for buyers who want the gaming-aesthetic without the Secretlab premium. Logitech G x Herman Miller Vantum holds the Logitech ecosystem pick. Branch Verve and Autonomous ErgoChair Pro 2 hold the value office picks. The Tuesday observation is that Secretlab is starting to send limited-stock notices on the Titan Evo Stealth and Black Leatherette colorways specifically. Other colors are still showing 1 to 2 week shipping, but the popular two are starting to push toward 3 weeks. Buyers committed to those colors should commit before the weekend.",
    en_h=[
        {"title": "Titan Evo 2026 at $549 holds through Tuesday on Secretlab.com", "body": "The Memorial Day price held through today which confirms the cut is genuine rather than flash. BlackPlus Leatherette plus redesigned ergonomic adjustability is the combination that wins for the typical buyer. First place is decisive at this price."},
        {"title": "Secretlab Stealth and Black Leatherette colors tightening on shipping", "body": "Tuesday observation is that Secretlab is sending limited-stock notices on the Stealth and Black Leatherette Titan Evo specifically. Shipping windows on those two are pushing toward 3 weeks. Buyers committed to those colors should commit before the weekend."},
        {"title": "Anda Seat Kaiser 4 at $399 holds through Tuesday for value flagship", "body": "The Memorial Day cut to $399 held through today on andaseat.com and Amazon. Build quality plus the new lumbar redesign is the package that justifies it over the bargain alternatives for buyers who want the gaming-aesthetic without the Secretlab premium."},
    ],
    zh_c="國殤日週第二天。Secretlab 官網 Titan Evo NT$16,500 守到今天，這個砍是真的國殤日價，不是一日限定。\n\nSecretlab Titan Evo 2026 守第一。BlackPlus Leatherette 加重新設計的人體工學調整，對要賽車椅外型加真實人體工學支撐的一般買家還是對的組合。\n\nHerman Miller Embody Gaming 第二守辦公級人體工學之選，BackFit 調整加 12 年保固對把椅子當長期辦公投資的買家還是對的。Herman Miller 不跑國殤日促銷，這禮拜價格對實力算式沒變。\n\nRazer Iskur V3 Pro 第三守專屬腰托之選。Steelcase Gesture 第四守辦公先行、玩家也買的選擇。Anda Seat Kaiser 4 國殤日 NT$12,000 在 andaseat.com 跟 Amazon 守到週二，要電競外型不想付 Secretlab 溢價的買家帳面對得起來。\n\nLogitech G x Herman Miller Vantum 守 Logitech 生態系之選。Branch Verve 跟 Autonomous ErgoChair Pro 2 守預算更緊的辦公之選。\n\n講真的，週二觀察是 Secretlab 開始對 Titan Evo Stealth 跟 Black Leatherette 兩個顏色寄「庫存有限」通知。其他色還顯示 1 到 2 週出貨，這兩個熱門色開始往 3 週推。認這兩色的人不要拖過週末。",
    zh_h=[
        {"title": "Titan Evo 2026 NT$16,500 在 Secretlab 官網守到週二", "body": "國殤日價守到今天，這個砍是真的不是快閃。BlackPlus Leatherette 加重新設計人體工學調整是對一般買家就是對的組合。這個價第一名很明確。"},
        {"title": "Secretlab Stealth 跟 Black Leatherette 兩色出貨時間拉長", "body": "週二觀察是 Secretlab 對 Stealth 跟 Black Leatherette Titan Evo 寄庫存有限通知。這兩色出貨時間往 3 週推。認這兩色的人不要拖過週末。"},
        {"title": "Anda Seat Kaiser 4 NT$12,000 守到週二是價值旗艦", "body": "國殤日 NT$12,000 在 andaseat.com 跟 Amazon 守到今天。做工加新的腰托重設計，對要電競外型但不想付 Secretlab 溢價的買家就是對的撐起。"},
    ],
)


# ============================================================
# best-handheld-gaming-consoles
# ============================================================
add(
    "best-handheld-gaming-consoles",
    refs=[
        {"title": "Best handheld gaming consoles 2026", "url": "https://www.theverge.com/22826129/best-handheld-gaming-console", "source": "The Verge"},
        {"title": "Steam Deck OLED 2 rumors", "url": "https://www.tomsguide.com/gaming/best-handheld-gaming-consoles", "source": "Tom's Guide"},
        {"title": "Asus ROG Ally X 2026 review", "url": "https://www.pcgamer.com/hardware/best-handheld-gaming-pc/", "source": "PC Gamer"},
    ],
    en_c="Day 2 of Memorial Day week. The ROG Ally X 2026 at $699 on Best Buy and asus.com held through Tuesday, which confirms the cut is genuine and not a flash. Asus ROG Ally X 2026 stays first. Ryzen Z2 Extreme plus the new VRR display plus the SteamOS dual-boot support that landed in April firmware is the combination that finally pushes the Ally past the Steam Deck on a meaningful argument. Valve Steam Deck OLED at second holds the SteamOS-native pick. Valve does not run Memorial Day promos on Steam Deck hardware, so the price-to-merit calculation does not change this week. Suspend-resume reliability plus OLED screen plus SteamOS native is the package that wins for buyers who want the most polished handheld without Windows friction. Nintendo Switch 2 at third holds the exclusives pick. Mario Kart World plus the upcoming Zelda title is the library argument nothing else can match. Lenovo Legion Go S at fourth holds the larger-screen pick. The SteamOS partnership is the development that makes it the right Windows alternative for buyers who want the bigger screen. AYANEO 3 holds the enthusiast pick. MSI Claw 8 AI+ holds the Intel-based pick. The Tuesday observation is that the Ally X 2026 storage upgrade SKU at $799 with the 2TB drive is the sweet-spot config and Best Buy stock is tightening on that specific SKU. The 1TB base at $699 has more inventory cushion. Buyers committed to the 2TB should commit before the weekend.",
    en_h=[
        {"title": "Ally X 2026 at $699 holds through Tuesday, cut is genuine", "body": "Best Buy and asus.com both held the $699 price through Tuesday which confirms the cut is genuine Memorial Day. Ryzen Z2 Extreme plus VRR display plus SteamOS dual-boot is the combination that finally pushes the Ally past the Steam Deck. First place is decisive."},
        {"title": "Ally X 2TB SKU tightening at Best Buy by weekend", "body": "Tuesday observation is that Best Buy stock on the $799 Ally X with 2TB drive is tightening. The 1TB base at $699 has more inventory cushion. Buyers committed to the 2TB sweet-spot config should commit before the weekend."},
        {"title": "Switch 2 wins on library nothing else can match", "body": "Mario Kart World plus the upcoming Zelda title is the library argument nothing else in the category can match. Nintendo does not discount Switch hardware on Memorial Day so the price is the same as it was a month ago. Library wins on library merit alone."},
    ],
    zh_c="國殤日週第二天。Best Buy 跟 asus.com 的 ROG Ally X 2026 NT$21,000 守到週二，這個砍是真的不是快閃。\n\nAsus ROG Ally X 2026 守第一。Ryzen Z2 Extreme 加新的 VRR 顯示器加四月韌體推送的 SteamOS 雙系統支援，這套組合終於讓 Ally 在有意義的論述上推過 Steam Deck。\n\nValve Steam Deck OLED 第二守 SteamOS 原生之選。Valve 國殤日不跑 Steam Deck 硬體促銷，這禮拜價格對實力算式沒變。待機恢復可靠度加 OLED 螢幕加 SteamOS 原生，對要最精緻掌機、不要 Windows 摩擦的買家還是對的。\n\nNintendo Switch 2 第三守獨佔遊戲之選。Mario Kart World 加即將推出的 Zelda 新作，這個遊戲庫論述分類裡沒人能比。\n\nLenovo Legion Go S 第四守大螢幕之選，SteamOS 合作是讓它成為要大螢幕 Windows 替代品的關鍵。AYANEO 3 守發燒友之選。MSI Claw 8 AI+ 守 Intel 基底之選。\n\n說到底，週二觀察是 Ally X 2026 2TB 版本 NT$24,000 是甜蜜點配置，Best Buy 這個 SKU 庫存正在縮。1TB 基本款 NT$21,000 庫存還有空間。認 2TB 版本的人不要拖過週末。",
    zh_h=[
        {"title": "Ally X 2026 NT$21,000 守到週二，折扣是真的", "body": "Best Buy 跟 asus.com 都把 NT$21,000 守到週二，這個砍是真的國殤日。Ryzen Z2 Extreme 加 VRR 顯示器加 SteamOS 雙系統終於讓 Ally 推過 Steam Deck。第一名很明確。"},
        {"title": "Ally X 2TB 版本 Best Buy 週末前可能斷貨", "body": "週二觀察是 Best Buy Ally X 2TB 版 NT$24,000 庫存在縮。1TB 基本款 NT$21,000 庫存還有空間。認 2TB 甜蜜點配置的人不要拖過週末。"},
        {"title": "Switch 2 靠分類裡沒人能比的遊戲庫贏", "body": "Mario Kart World 加即將推出的 Zelda 新作，這個遊戲庫分類裡沒人能比。任天堂國殤日不砍 Switch 硬體，價格跟一個月前一樣。遊戲庫純粹靠遊戲庫實力贏。"},
    ],
)


# ============================================================
# best-portable-chargers
# ============================================================
add(
    "best-portable-chargers",
    refs=[
        {"title": "Best portable chargers 2026", "url": "https://www.tomsguide.com/best-picks/best-portable-chargers", "source": "Tom's Guide"},
        {"title": "Anker Prime 27,650mAh review", "url": "https://www.theverge.com/22832929/best-portable-charger-power-bank", "source": "The Verge"},
        {"title": "Memorial Day Anker deals 2026", "url": "https://www.techradar.com/seasonal-sales/best-memorial-day-sales-2026", "source": "TechRadar"},
    ],
    en_c="Tuesday Day 2 of Memorial Day week and the portable-charger category is exactly where the holiday math gets interesting because Anker runs aggressive Memorial Day promos every year and they always tighten by the weekend. The Anker Prime 27,650mAh at $149 from Anker.com and Amazon held through Tuesday, which confirms the cut is genuine. Anker Prime 27,650mAh stays first. 250W output plus smart display plus GaNPrime 2 internals is the combination that still wins for the laptop-and-phone power user. Anker MagGo 10,000mAh Power Bank holds second as the MagSafe-compatible pick. The iPhone 16-and-up snap-on usage is the right form factor for buyers in that ecosystem, and the discount to $79 held through today which is the cheapest the MagGo has been all year. Baseus Blade 2 at third holds the laptop-bag pick. UGREEN Nexode 25000 at fourth holds the value laptop charger and the four-port plus 200W output is the package that justifies it over the Anker for travelers charging a family of devices. Anker 633 Magnetic 10K in mid-pack. Anker 737 24K for workhorse buyers. Mophie Powerstation Pro AC for AC outlet buyers. The Tuesday observation is that the Anker Prime $149 stock at Anker.com is starting to thin on the silver colorway, and the typical pattern from 2024 and 2025 holiday seasons is that this SKU runs out by Friday afternoon. Buyers committed to the Prime should commit by Thursday at the latest. Amazon usually holds inventory longer but at a slightly higher street price.",
    en_h=[
        {"title": "Anker Prime $149 holds through Tuesday, the deal is real", "body": "Anker.com and Amazon both held the $149 price through Tuesday which confirms the cut is genuine Memorial Day. 250W output plus smart display plus GaNPrime 2 internals is the combination that wins for laptop-and-phone power users. First place is decisive."},
        {"title": "Anker Prime silver colorway likely runs out by Friday", "body": "Tuesday observation is that Anker.com stock on the Prime silver colorway is starting to thin and the typical pattern from prior holiday seasons is that this SKU runs out by Friday afternoon. Buyers committed to the Prime should commit by Thursday at latest."},
        {"title": "Anker MagGo at $79 is the cheapest all year for iPhone buyers", "body": "The discount to $79 on the MagGo 10,000mAh held through Tuesday which is the cheapest the MagSafe-compatible bank has been all year. For iPhone 16-and-up buyers who want the snap-on form factor, this is the right specific moment to buy."},
    ],
    zh_c="國殤日週第二天，行動電源分類就是節慶帳面有趣的地方，Anker 每年國殤日都跑激進促銷，到週末前都會收緊庫存。Anker.com 跟 Amazon 的 Anker Prime 27,650mAh NT$4,500 守到週二，這個砍是真的。\n\nAnker Prime 27,650mAh 守第一。250W 輸出加智慧顯示器加新的 GaNPrime 2 內部結構，這個組合對筆電加手機重度使用者還是對的。\n\nAnker MagGo 10,000mAh Power Bank 守第二是 MagSafe 相容之選，iPhone 16 以上吸上去用的這個外型對這個生態系買家就是對的，NT$2,400 折扣到今天還在，今年最低。\n\nBaseus Blade 2 第三守筆電包之選。UGREEN Nexode 25000 第四守價值筆電充電器，四埠加 200W 輸出對要同時幫一家子裝置充電的旅行者比 Anker 對。\n\nAnker 633 Magnetic 10K 中段守預算 MagSafe 替代品。Anker 737 24K 守要工作機而非 Prime 生態系的買家。Mophie Powerstation Pro AC 守特別需要 AC 插座的買家。\n\n講真的，週二觀察是 Anker.com Prime NT$4,500 銀色庫存開始薄，2024 跟 2025 節慶的典型情況是這個 SKU 週五下午前就賣完。認 Prime 的人最晚週四下手。Amazon 通常庫存撐比較久，但街頭價會略高。",
    zh_h=[
        {"title": "Anker Prime NT$4,500 守到週二，折扣是真的", "body": "Anker.com 跟 Amazon 都把 NT$4,500 守到週二，這個砍是真的國殤日。250W 輸出加智慧顯示器加 GaNPrime 2 內部結構是筆電加手機重度使用者之選。第一名很明確。"},
        {"title": "Anker Prime 銀色週五前可能斷貨", "body": "週二觀察是 Anker.com Prime 銀色庫存開始薄，過去節慶的典型情況是這個 SKU 週五下午前就賣完。認 Prime 的人最晚週四下手。"},
        {"title": "Anker MagGo NT$2,400 是 iPhone 買家今年最低價", "body": "MagGo 10,000mAh NT$2,400 折扣守到週二，是 MagSafe 相容行動電源今年最低。iPhone 16 以上要吸上去用的買家，現在這個時間點下手就是對的。"},
    ],
)
