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

# ---------------- best-action-cameras ----------------
do("best-action-cameras.json",
   [
     {"title": "Best Action Camera 2026: DJI vs GoPro vs Insta360", "url": "https://actioncameraview.com/best-action-camera-2026-ultimate-buying-guide/", "source": "Action Camera View"},
     {"title": "DJI Osmo Action 6 review: Better than anything GoPro or Insta360 can offer", "url": "https://www.tomsguide.com/cameras-photography/gopro-action-cameras/dji-osmo-action-6-review", "source": "Tom's Guide"},
   ],
   {
     "commentary": "Heading into June 2026 the action-camera order is locked, and I keep the DJI Osmo Action 6 at number one with full confidence. It is the only flat-body action cam shipping a true 1-inch-class sensor with a variable f/2.0 to f/4.0 aperture and roughly 13.5 stops of dynamic range, and Tom's Guide flatly calls it better than anything GoPro or Insta360 currently offers. When one camera has to nail daylight, low light and harsh contrast without fuss, this is the one I hand people. The Insta360 Ace Pro 2 stays a tight second and remains my night pick: it produced the cleanest streetlight rendering in low-light testing and has the best onboard audio of any action cam I have used, so for vlogging or after-dark riding it is the smarter buy. The GoPro Mission 1 Pro holds third on the strength of stabilization that simply does not break under extreme vibration, which is exactly why motorcycle and mountain-bike riders keep choosing GoPro. HERO13 Black and the Insta360 X5 sit fourth and fifth as the proven all-rounder and the best 360 cam respectively. One thing to watch: GoPro has confirmed a HERO14 Black for later this year, so if you ride GoPro and can wait, it may be worth holding. The rest of the board carries forward unchanged because nothing this week reshuffled it. Pick the Action 6 for outright image quality, the Ace Pro 2 for low light, the Mission 1 Pro for rough rides.",
     "highlights": [
       {"title": "Osmo Action 6 owns image quality", "body": "A true 1-inch-class sensor, a variable f/2.0 to f/4.0 aperture and around 13.5 stops of dynamic range put it ahead of every flat-body rival. Tom's Guide calls it better than anything GoPro or Insta360 offers, and that is why it stays number one."},
       {"title": "Ace Pro 2 is the low-light champion", "body": "It rendered streetlights the cleanest of any action cam in testing and carries the best onboard audio in the class. For vlogging or after-dark shooting it is the camera I reach for, holding a deserved second."},
       {"title": "Mission 1 Pro wins on rough rides", "body": "Its stabilization holds together under extreme vibration where others smear, which is exactly why motorcycle and mountain-bike riders keep buying GoPro. That durability of footage keeps it a solid third."},
       {"title": "A HERO14 Black is coming", "body": "GoPro has confirmed a new HERO14 Black for later this year. If you are committed to GoPro and can wait a few months, it is worth holding before buying into the current HERO13 generation."},
     ],
   },
   {
     "commentary": "2026 年 6 月這個時間點，運動相機的排序已經鎖定，我很有信心把 DJI Osmo Action 6 放第一。它是目前唯一一台扁身運動相機塞進接近 1 吋的感光元件，還配 f/2.0 到 f/4.0 可變光圈、約 13.5 級動態範圍，Tom's Guide 直接講它比 GoPro 跟 Insta360 現有任何機種都好。要一台相機白天、暗光、強反差全都搞定又不囉嗦，我就遞這台給人。Insta360 Ace Pro 2 緊咬第二，依然是我的夜拍首選，暗光測試裡它的路燈表現最乾淨，收音也是我用過運動相機裡最好的，拍 Vlog 或晚上騎車選它更聰明。GoPro Mission 1 Pro 守第三，靠的是在劇烈震動下也不崩的防手震，這正是重機跟登山車車友一直選 GoPro 的原因。HERO13 Black 跟 Insta360 X5 排第四第五，一個是驗證過的全能機、一個是最強 360 機。有件事要注意，GoPro 已經確認今年稍晚會出 HERO14 Black，所以你如果是 GoPro 派又等得起，或許值得先按住。其餘照舊，這週沒事件洗牌。要純畫質選 Action 6、要暗光選 Ace Pro 2、要耐操騎乘選 Mission 1 Pro。",
     "highlights": [
       {"title": "Osmo Action 6 畫質稱霸", "body": "接近 1 吋感光元件、f/2.0 到 f/4.0 可變光圈、約 13.5 級動態範圍，把每一台扁身對手都甩開。Tom's Guide 講它比 GoPro 跟 Insta360 都好，第一名穩穩的。"},
       {"title": "Ace Pro 2 是暗光冠軍", "body": "測試裡路燈渲染是所有運動相機最乾淨的，收音也是同級最好。拍 Vlog 或晚上拍攝我就拿它，第二實至名歸。"},
       {"title": "Mission 1 Pro 贏在耐操騎乘", "body": "在劇烈震動下防手震還撐得住，別人早就糊成一團，這正是重機跟登山車車友一直選 GoPro 的原因。畫面的穩定耐用讓它穩坐第三。"},
       {"title": "HERO14 Black 要來了", "body": "GoPro 已經確認今年稍晚會出新的 HERO14 Black。如果你認定 GoPro 又等得起幾個月，買進現在的 HERO13 世代前值得先按住。"},
     ],
   })

# ---------------- best-dash-cams ----------------
do("best-dash-cams.json",
   [
     {"title": "I've reviewed over 15 dash cams this last year, and Viofo's A329 is the best of the bunch", "url": "https://www.techradar.com/vehicle-tech/dash-cams/ive-reviewed-over-15-dash-cams-this-last-year-and-viofos-a329-is-the-best-of-the-bunch-heres-why", "source": "TechRadar"},
     {"title": "The Best Dash Cams of 2026: Our Top Picks and What's New", "url": "https://www.viofo.com/blogs/viofo-car-dash-camera-guide-faq-and-news/the-best-dash-cams-of-2026-our-top-picks-and-whats-new", "source": "VIOFO"},
   ],
   {
     "commentary": "Going into June 2026 the dash-cam crown still belongs to the Viofo A329S, and I have no reason to move it. TechRadar reviewed over 15 dash cams this year and named the A329 the best of the bunch, while Vortex Radar ran a 13-model head-to-head and crowned it best all-around, tying for first in both daytime image quality and parking mode. The spec sheet earns it: 4K60 front and 2K HDR rear on dual Sony STARVIS 2 sensors, Wi-Fi 6 so a 4K clip moves to your phone in seconds, and SSD support up to 4TB for weeks of continuous recording. It is premium-priced at around $429 for the dual-channel kit, but you get what you pay for. The Vantrue N4 Pro S holds second as the multi-channel workhorse with strong night video, the pick for rideshare and fleet drivers who want a three-camera setup. BlackVue Elite 9 and Thinkware U3000 stay third and fourth as the polished cloud-connected premium options. For pure value the Viofo A119M Pro at sixth remains the smart budget buy. Everything else carries forward unchanged because nothing this week reshuffled the board. Buy the A329S for the best overall footage, the N4 Pro S for multi-channel coverage, the A119M Pro when budget rules.",
     "highlights": [
       {"title": "Viofo A329S is the clear best overall", "body": "TechRadar called it the best of 15-plus dash cams it tested, and Vortex Radar crowned it best all-around. With 4K60 STARVIS 2 front video, Wi-Fi 6 and 4TB SSD support, it stays number one without argument."},
       {"title": "Vantrue N4 Pro S owns multi-channel", "body": "Three-camera coverage with strong night video makes it the choice for rideshare and fleet drivers who need interior plus front and rear. That triple-cam strength keeps it a solid second."},
       {"title": "The A329S price is worth it", "body": "At around $429 for the dual-channel kit it is not cheap, but the STARVIS 2 footage, Wi-Fi 6 transfer speed and SSD endurance justify every dollar. For a buy-once dash cam, this is where the money goes."},
       {"title": "A119M Pro is the value pick", "body": "It delivers genuinely good footage at a fraction of the flagship price, which keeps it the smart budget choice at sixth. When you want reliable recording without the premium spend, this is the one."},
     ],
   },
   {
     "commentary": "2026 年 6 月，行車記錄器的王冠還是 Viofo A329S 的，我沒理由把它移走。TechRadar 今年測了 15 台以上，直接點名 A329 是裡頭最好的，Vortex Radar 跑了 13 台對決，也把它選為綜合最佳，白天畫質跟停車模式都並列第一。規格撐得起這個評價，前 4K60、後 2K HDR，雙 Sony STARVIS 2 感光元件，Wi-Fi 6 讓 4K 片段幾秒就傳到手機，還支援最大 4TB SSD，連續錄好幾週。雙鏡頭組約台幣一萬三千多，價格是貴，但一分錢一分貨。Vantrue N4 Pro S 守第二，是多鏡頭的工作機，夜拍紮實，要三鏡頭配置的網約車跟車隊司機選它。BlackVue Elite 9 跟 Thinkware U3000 排第三第四，是雲端連線、做工精緻的高階選擇。論純性價比，第六的 Viofo A119M Pro 還是聰明的預算選擇。其餘照舊，這週沒事件洗牌。要最佳綜合畫面選 A329S、要多鏡頭涵蓋選 N4 Pro S、預算掛帥選 A119M Pro。",
     "highlights": [
       {"title": "Viofo A329S 是明確的綜合最佳", "body": "TechRadar 在 15 台以上裡點名它最好，Vortex Radar 也選它綜合最佳。前 4K60 STARVIS 2 畫質、Wi-Fi 6、支援 4TB SSD，第一名沒得吵。"},
       {"title": "Vantrue N4 Pro S 主宰多鏡頭", "body": "三鏡頭涵蓋加紮實夜拍，讓它成為要車內加前後的網約車跟車隊司機首選。這份三鏡頭實力讓它穩坐第二。"},
       {"title": "A329S 的價格值得", "body": "雙鏡頭組約台幣一萬三千多不便宜，但 STARVIS 2 畫質、Wi-Fi 6 傳輸速度、SSD 耐用度，每一塊錢都花得有道理。要買一次用很久，錢就花在這。"},
       {"title": "A119M Pro 是性價比之選", "body": "用旗艦零頭的價格給出真的不錯的畫面，讓它穩坐第六的聰明預算選擇。想要可靠錄影又不想花大錢，就是它。"},
     ],
   })

# ---------------- best-security-cameras ----------------
do("best-security-cameras.json",
   [
     {"title": "Reolink vs Eufy: Ultimate Security Camera Comparison (2026 Guide)", "url": "https://sipkosecurity.com/reolink-vs-eufy-security-camera-comparison-2026/", "source": "Sipko Security"},
     {"title": "15 Best Home Security Cameras of 2026, Lab-Tested and Reviewed", "url": "https://www.consumerreports.org/home-garden/home-security-cameras/best-wireless-home-security-cameras-of-the-year-a1535263710/", "source": "Consumer Reports"},
   ],
   {
     "commentary": "Heading into June 2026 my security-camera ranking still leads with the Reolink Argus 4 Pro, and the logic holds firm: it pairs genuinely sharp 4K with strong color night vision and, crucially, charges no monthly fee because local storage is free forever. Over five years a Reolink setup runs a fraction of what Ring or Arlo cost once subscriptions are added in, and that total-cost story is why it stays number one for most buyers. The Arlo Pro 5S holds second and earns it on pure imaging: it shoots true 4K HDR with the best color night vision I have tested, sharp and natural without the oversaturation rivals fall into. If picture quality is your single priority and you accept the subscription, it is the one. The Eufy SoloCam S340 stays third as the dual-camera solar pick that solves battery anxiety outright, no wiring, no recurring fee. Google Nest Cam holds fourth for the smartest detection and tightest Google Home integration. The Tapo C460 MagCam remains the standout budget value lower down. Everything else carries forward unchanged because nothing this week reshuffled the order. Pick Reolink for no-fee ownership, Arlo for best image, Eufy for solar set-and-forget, Nest for smart-home brains.",
     "highlights": [
       {"title": "Reolink Argus 4 Pro wins on total cost", "body": "Sharp 4K, strong color night vision and free local storage with no monthly fee mean it costs a fraction of Ring or Arlo over five years. That ownership math keeps it at number one for most buyers."},
       {"title": "Arlo Pro 5S has the best image", "body": "It shoots true 4K HDR with the best color night vision I have tested, sharp and natural without oversaturation. If picture quality is your priority and the subscription is fine, it is the clear second."},
       {"title": "Eufy SoloCam S340 kills battery anxiety", "body": "Its integrated solar panel and dual-camera design mean no wiring and no recurring fee, solving the single biggest pain of wireless cams. That set-and-forget convenience keeps it a strong third."},
       {"title": "Nest Cam owns smart detection", "body": "It still posts the smartest person and package detection and the cleanest Google Home integration on the board. For households already living in Google's ecosystem, it stays the natural fourth pick."},
     ],
   },
   {
     "commentary": "2026 年 6 月，我的監控攝影機排名還是 Reolink Argus 4 Pro 領頭，邏輯很穩，它把真正銳利的 4K 配上不錯的彩色夜視，而且最關鍵的是不收月費，因為本地儲存永久免費。算五年下來，一套 Reolink 的花費只有加上訂閱後的 Ring 或 Arlo 的零頭，這個總成本的故事，就是它對多數買家穩坐第一的原因。Arlo Pro 5S 守第二，靠的是純畫質，它拍真 4K HDR，彩色夜視是我測過最好的，銳利自然又不會像對手那樣過飽和。如果畫質是你唯一的優先、又能接受訂閱，就是它。Eufy SoloCam S340 守第三，是雙鏡頭太陽能款，直接解決電池焦慮，不用拉線、不用月費。Google Nest Cam 守第四，偵測最聰明、跟 Google Home 整合最緊。Tapo C460 MagCam 在後段仍是突出的預算性價比。其餘照舊，這週沒事件洗牌。要免月費選 Reolink、要最佳畫質選 Arlo、要太陽能裝了就忘選 Eufy、要智慧家庭大腦選 Nest。",
     "highlights": [
       {"title": "Reolink Argus 4 Pro 贏在總成本", "body": "銳利 4K、不錯的彩色夜視、本地儲存免費不收月費，算五年只要 Ring 或 Arlo 的零頭。這套擁有成本的算盤，讓它對多數買家穩坐第一。"},
       {"title": "Arlo Pro 5S 畫質最好", "body": "拍真 4K HDR，彩色夜視是我測過最好的，銳利自然不過飽和。如果畫質是你的優先、又能接受訂閱，第二非它莫屬。"},
       {"title": "Eufy SoloCam S340 終結電池焦慮", "body": "內建太陽能板加雙鏡頭設計，不用拉線、不用月費，直接解掉無線攝影機最大的痛。這份裝了就忘的方便讓它穩坐第三。"},
       {"title": "Nest Cam 偵測最聰明", "body": "人形跟包裹偵測還是榜上最聰明，跟 Google Home 整合也最乾淨。已經住在 Google 生態的家庭，它仍是天然的第四選擇。"},
     ],
   })

# ---------------- best-video-doorbells ----------------
do("best-video-doorbells.json",
   [
     {"title": "The Aqara Doorbell Camera Hub G410 is much more than just a video doorbell", "url": "https://www.techradar.com/home/smart-home/aqara-doorbell-camera-hub-g410-review", "source": "TechRadar"},
     {"title": "Best Smart Doorbell Cameras 2026: Ring vs Nest vs Eufy Compared", "url": "https://www.smarthomeexplorer.com/guides/best-smart-doorbell-cameras-2026", "source": "Smart Home Explorer"},
   ],
   {
     "commentary": "Going into June 2026 the Eufy Video Doorbell E340 stays my number one, and it is not close on value. You get dual 2K cameras, a front lens for faces and a downward lens that actually watches packages on your doorstep, AI that separates people from parcels, hardwired or six-month battery operation, and zero subscription because recording is local. For the money, nothing else covers this many bases. The Aqara G410 holds second and is the smart-home pick: 2K video, mmWave radar detection that cuts false alerts, and an indoor chime that doubles as a Matter-certified hub. My one honest caveat is its IPX3 rating, so it really wants a covered porch, but if you live in Matter and HomeKit it is the most capable doorbell here. The Google Nest Doorbell (Wired, 2nd Gen) stays third for the sharpest detection intelligence and tightest Google integration. Aqara's wired G400 sits fourth as the flexible PoE-and-local-recording option. The Ring Battery Doorbell Pro holds fifth on the strength of crisp video for anyone already in the Ring ecosystem. Tapo D225 remains the budget standout. Everything else carries forward unchanged because nothing this week moved the order. Pick the E340 for outright value, the G410 for Matter smarts, the Nest for detection.",
     "highlights": [
       {"title": "Eufy E340 wins on value", "body": "Dual 2K cameras with a dedicated package-watching lens, AI person and parcel detection, six-month battery and zero subscription cover more ground than anything at the price. That completeness keeps it at number one."},
       {"title": "Aqara G410 is the smart-home pick", "body": "2K video, mmWave radar that cuts false alerts, and a chime that doubles as a Matter-certified hub make it the most capable doorbell for Matter and HomeKit homes. It earns a clear second."},
       {"title": "The G410 wants a covered porch", "body": "Its IPX3 weather rating means it is best mounted under cover rather than fully exposed. I keep the verdict honest so you match the doorbell to your actual entryway before buying."},
       {"title": "Nest Doorbell owns detection", "body": "It still posts the smartest person, package and familiar-face detection with the cleanest Google Home integration. For households already in Google's world, it stays the natural third pick."},
     ],
   },
   {
     "commentary": "2026 年 6 月，Eufy Video Doorbell E340 還是我的第一，論性價比沒對手能貼近。你拿到雙 2K 鏡頭，前鏡頭看臉、下鏡頭真的盯著門口的包裹，AI 能把人跟包裹分開，可接電也可用六個月電池，而且不用訂閱，因為錄影存本地。這個價位，沒有別的能顧到這麼多面。Aqara G410 守第二，是智慧家庭之選，2K 畫質、mmWave 毫米波雷達偵測能砍掉誤報，室內門鈴還兼 Matter 認證的 Hub。我老實補一句但書，它防水只有 IPX3，所以真的需要有遮蓋的玄關，但你如果活在 Matter 跟 HomeKit 裡，它是這裡功能最強的門鈴。Google Nest Doorbell（有線二代）守第三，偵測智慧最銳利、跟 Google 整合最緊。Aqara 有線 G400 排第四，是彈性的 PoE 加本地錄影選項。Ring Battery Doorbell Pro 守第五，畫質清晰，適合已經在 Ring 生態的人。Tapo D225 仍是預算突出之選。其餘照舊，這週沒事件動排名。要純性價比選 E340、要 Matter 智慧選 G410、要偵測選 Nest。",
     "highlights": [
       {"title": "Eufy E340 贏在性價比", "body": "雙 2K 鏡頭加一個專盯包裹的下鏡頭、AI 人形與包裹偵測、六個月電池、零訂閱，顧到的面比同價位任何門鈴都多。這份完整度讓它穩坐第一。"},
       {"title": "Aqara G410 是智慧家庭之選", "body": "2K 畫質、能砍誤報的 mmWave 雷達、兼 Matter 認證 Hub 的門鈴，讓它成為 Matter 跟 HomeKit 家庭功能最強的門鈴。第二實至名歸。"},
       {"title": "G410 需要有遮蓋的玄關", "body": "它防水只有 IPX3，最好裝在有遮蓋處而非完全曝曬。我把判斷講白，讓你買前先對好自家門口的實際狀況。"},
       {"title": "Nest Doorbell 主宰偵測", "body": "人形、包裹、熟面孔偵測還是最聰明，跟 Google Home 整合也最乾淨。已經在 Google 生態的家庭，它仍是天然的第三選擇。"},
     ],
   })

# ---------------- best-mesh-wifi-systems ----------------
do("best-mesh-wifi-systems.json",
   [
     {"title": "The 4 Best Mesh Wi-Fi Systems of 2026", "url": "https://www.rtings.com/router/reviews/best/mesh-wifi-system", "source": "RTINGS"},
     {"title": "Best Mesh WiFi Systems in 2026: Top 10 Compared", "url": "https://www.modemguides.com/blogs/modemguides-blog/best-mesh-wifi-systems-compared", "source": "Modem Guides"},
   ],
   {
     "commentary": "Heading into June 2026 the mesh Wi-Fi top tier stays settled, and I keep the Asus ZenWiFi BQ16 Pro at number one because it is still the performance and feature ceiling of the category. Quad-band Wi-Fi 7, dual 10Gb ports per node, the full ASUSWRT suite with AiProtection Pro security and parental controls bundled free with no subscription, and the raw throughput to back it up. For a power user who wants the best and will wire a multi-gig backhaul, nothing else touches it. The catch is price, which is exactly why the TP-Link Deco BE63 sits a close second and is the system I recommend to most homes. It delivers tri-band Wi-Fi 7, handles 200-plus devices and covers up to 7,600 square feet for around $270 a two-pack, and in head-to-head speed tests it trails the pricier flagships by single-digit megabits. That is the value play of 2026. The eero Pro 7 holds third for the cleanest app experience and the best built-in Thread, Zigbee and Matter smart-home hub. The MSI Roamii BE Pro lower down remains a quietly excellent budget Wi-Fi 7 buy. Everything else carries forward unchanged because nothing this week reshuffled it. Buy the BQ16 Pro for maximum performance, the Deco BE63 for the best overall value, the eero Pro 7 for smart-home simplicity.",
     "highlights": [
       {"title": "Asus BQ16 Pro is the performance ceiling", "body": "Quad-band Wi-Fi 7, dual 10Gb ports per node and the full ASUSWRT security suite free of subscription make it the most capable mesh on the board. For power users wiring a multi-gig backhaul, it stays number one."},
       {"title": "TP-Link Deco BE63 is the value champion", "body": "Tri-band Wi-Fi 7, 200-plus device support and 7,600 sq ft of coverage for around $270 a two-pack, trailing flagships by single-digit megabits in tests. That price-to-performance keeps it a close second."},
       {"title": "eero Pro 7 owns smart-home simplicity", "body": "The cleanest app experience plus built-in Thread, Zigbee and Matter make it the easiest mesh to live with in a connected home. For set-and-forget owners it holds a deserved third."},
       {"title": "Asus bundles security for free", "body": "AiProtection Pro, parental controls and network scanning come included with no recurring fee, unlike rivals that gate features behind subscriptions. That no-fee security stack is a real reason the BQ16 Pro leads."},
     ],
   },
   {
     "commentary": "2026 年 6 月，Mesh Wi-Fi 的頂端維持穩定，我把 Asus ZenWiFi BQ16 Pro 放第一，因為它依然是這個類別效能跟功能的天花板。四頻 Wi-Fi 7、每個節點雙 10Gb 埠、完整的 ASUSWRT，連 AiProtection Pro 防護跟家長控制都免費內建不用訂閱，再加上撐得起的純吞吐量。對想要最好、又願意拉多 gig 有線回程的玩家，沒有別的碰得到它。罩門是價格，這也正是 TP-Link Deco BE63 緊咬第二、又是我推薦給多數家庭的系統的原因。它給三頻 Wi-Fi 7、扛 200 多台裝置、涵蓋最大約 211 坪，兩入組約台幣八千多，速度對決裡只輸貴上一截的旗艦個位數 Mbps。這就是 2026 的性價比之選。eero Pro 7 守第三，App 體驗最乾淨，內建 Thread、Zigbee、Matter 智慧家庭 Hub 也最強。後段的 MSI Roamii BE Pro 仍是低調又優秀的預算 Wi-Fi 7 選擇。其餘照舊，這週沒事件洗牌。要最強效能選 BQ16 Pro、要最佳綜合性價比選 Deco BE63、要智慧家庭簡單選 eero Pro 7。",
     "highlights": [
       {"title": "Asus BQ16 Pro 是效能天花板", "body": "四頻 Wi-Fi 7、每節點雙 10Gb 埠、完整 ASUSWRT 防護免訂閱，是榜上功能最強的 Mesh。對拉多 gig 有線回程的玩家，第一名穩穩的。"},
       {"title": "TP-Link Deco BE63 是性價比冠軍", "body": "三頻 Wi-Fi 7、扛 200 多台裝置、涵蓋約 211 坪，兩入組約台幣八千多，測試裡只輸旗艦個位數 Mbps。這份性價比讓它緊咬第二。"},
       {"title": "eero Pro 7 主宰智慧家庭簡單度", "body": "最乾淨的 App 體驗加內建 Thread、Zigbee、Matter，是連網家庭最好相處的 Mesh。對裝了就忘的人，第三實至名歸。"},
       {"title": "Asus 防護免費附", "body": "AiProtection Pro、家長控制、網路掃描全部免費內建，不像對手把功能鎖在訂閱後面。這套不收費的防護，是 BQ16 Pro 領先的真實理由。"},
     ],
   })

# ---------------- best-smart-pet-feeders ----------------
do("best-smart-pet-feeders.json",
   [
     {"title": "Best Smart Pet Feeders and Cameras 2026", "url": "https://www.smarthomeexplorer.com/guides/best-automated-smart-pet-feeders-cameras-2026", "source": "Smart Home Explorer"},
     {"title": "Petkit Automatic Feeder vs Petlibro 2026: Best Tested", "url": "https://www.infomastero.online/petkit-automatic-feeder-vs-petlibro/", "source": "Infomastero"},
   ],
   {
     "commentary": "Heading into June 2026 the PETLIBRO Granary Smart Camera Feeder stays my number one for the one reason that matters most with a feeder: it feeds when it is supposed to. Its twin-turbine motor is documented by PCMag as roughly 4x more jam-resistant than single-auger designs, which is the top failure mode owners actually report. Add a sharp camera, dual USB-C and battery-backup power that keeps dispensing through outages and Wi-Fi drops, and both PCMag and Wirecutter name it best automatic feeder. If you want a workhorse that just works, this is it. The PETKIT YumShare Dual-Hopper 2 holds second and is the pick for multi-pet, multi-flavor homes: a sharp 1080p camera, two-way audio and dual hoppers for two foods. If aesthetics and premium features matter more than pure mechanical simplicity, PETKIT wins that argument. The PETLIBRO Polar Refrigerated Wet Food Feeder stays third as the only strong answer for wet food, keeping it fresh on a schedule. The WOpet Heritage View holds fourth as a solid dual-bowl camera option. Lower down, the homerunPET PF20 remains the standout reliability-per-dollar pick. Everything else carries forward unchanged because nothing this week moved the order. Pick the Granary for rock-solid feeding, the YumShare 2 for multi-pet features, the Polar for wet food.",
     "highlights": [
       {"title": "PETLIBRO Granary just works", "body": "Its twin-turbine motor is documented as roughly 4x more jam-resistant than single-auger rivals, and battery backup keeps it dispensing through outages and Wi-Fi drops. That reliability is why it stays number one."},
       {"title": "PETKIT YumShare 2 owns multi-pet homes", "body": "A sharp 1080p camera, two-way audio and dual hoppers for two foods make it the pick for multi-pet, multi-flavor households. For premium features and design, it earns a clear second."},
       {"title": "PETLIBRO Polar is the wet-food answer", "body": "Refrigerated dispensing keeps wet food fresh on a schedule, which almost no other smart feeder handles well. For cats that eat wet food it stays the obvious specialist at third."},
       {"title": "homerunPET PF20 is the value pick", "body": "It delivers the kind of dependable scheduled feeding that matters most at a notably lower price. For owners who want reliability without premium spend, it remains the smart budget choice."},
     ],
   },
   {
     "commentary": "2026 年 6 月，PETLIBRO Granary 智慧攝影餵食器還是我的第一，理由就是餵食器最重要的那一點，它該餵的時候真的會餵。它的雙渦輪馬達，PCMag 實測抗卡料大約是單絞龍設計的 4 倍，而卡料正是飼主最常回報的故障。再加上清晰的鏡頭、雙 USB-C 跟電池備援，斷電跟斷網時照樣出料，PCMag 跟 Wirecutter 都把它選為最佳自動餵食器。你要一台裝了就乖乖運作的工作機，就是它。PETKIT YumShare Dual-Hopper 2 守第二，是多寵物、多口味家庭之選，清晰 1080p 鏡頭、雙向語音、雙料倉裝兩種飼料。如果你更在意外型跟高階功能勝過純機械簡單，PETKIT 贏這場辯論。PETLIBRO Polar 冷藏濕食餵食器守第三，是濕食唯一像樣的答案，能照時程保鮮。WOpet Heritage View 守第四，是紮實的雙碗攝影款。後段的 homerunPET PF20 仍是每塊錢可靠度最突出的選擇。其餘照舊，這週沒事件動排名。要超穩餵食選 Granary、要多寵物功能選 YumShare 2、要濕食選 Polar。",
     "highlights": [
       {"title": "PETLIBRO Granary 裝了就乖乖運作", "body": "雙渦輪馬達實測抗卡料大約是單絞龍設計的 4 倍，電池備援讓它在斷電跟斷網時照樣出料。這份可靠度就是它穩坐第一的原因。"},
       {"title": "PETKIT YumShare 2 主宰多寵物家庭", "body": "清晰 1080p 鏡頭、雙向語音、雙料倉裝兩種飼料，是多寵物、多口味家庭之選。論高階功能跟設計，第二實至名歸。"},
       {"title": "PETLIBRO Polar 是濕食的答案", "body": "冷藏出料能照時程把濕食保鮮，這點幾乎沒有別台智慧餵食器做得好。吃濕食的貓，它穩坐第三的專家位。"},
       {"title": "homerunPET PF20 是性價比之選", "body": "用明顯更低的價格，給出最重要的那種可靠定時餵食。想要可靠又不想花大錢的飼主，它仍是聰明的預算選擇。"},
     ],
   })

print("ALL DONE")
