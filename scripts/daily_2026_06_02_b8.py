"""2026-06-02 daily update — Batch 8: Tech/Gadgets (8 files)"""
import json
from pathlib import Path

DATE = "2026-06-02"
ROOT = Path("/Users/etrexkuo/toprankland/src/content/rankings")

def load(name):
    p = ROOT / name
    return json.loads(p.read_text(encoding="utf-8")), p

def save(p, data):
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

def upsert(data, entry):
    for i, h in enumerate(data["history"]):
        if h["date"] == entry["date"]:
            data["history"][i] = entry
            return
    data["history"].append(entry)

def last_rankings(d):
    return d["history"][-1]["rankings"]


def build_dash_cams():
    d, p = load("best-dash-cams.json")
    entry = {
        "date": DATE,
        "rankings": last_rankings(d),
        "references": [
            {"title": "The Best Dash Cams of 2026: Our Top Picks and What's New", "url": "https://www.viofo.com/blogs/viofo-car-dash-camera-guide-faq-and-news/the-best-dash-cams-of-2026-our-top-picks-and-whats-new", "source": "VIOFO"},
            {"title": "Best Dash Cams for 2026: Tested & Ranked", "url": "https://www.vortexradar.com/best-dashcams/", "source": "Vortex Radar"},
            {"title": "Best Dash Cams of 2026: Top Picks Reviewed", "url": "https://www.getnexar.com/blog/best-dash-cams-of-2026-top-picks-reviewed", "source": "Nexar"},
        ],
        "i18n": {
            "en": {
                "commentary": "The dash cam category in mid-2026 has settled into a clear hierarchy, and the VIOFO A329S keeps the top spot because it does the one thing that matters most exceptionally well: it produces the sharpest, most usable footage in the class. Its 4K front sensor reads license plates cleanly in daylight and holds detail under headlights at night, which is the entire point of owning a dash cam. The flexible three-channel setup, front, rear, and interior, makes it the benchmark every reviewer measures against this year.\n\nThe Vantrue N4 Pro S at rank 2 remains my pick for drivers who want genuine three-channel coverage in a single compact unit. Capturing front, cabin, and rear simultaneously with consistent night performance is hard to do well, and the N4 Pro S does it without the cable mess of stitching separate cameras together. Rideshare and delivery drivers in particular get real value here.\n\nThe BlackVue Elite 9 at rank 3 is the connected-features champion. Cloud-based parking alerts and remote live viewing genuinely change how you use a dash cam, letting you check on your parked car from your phone anywhere. The Thinkware U3000 sits at rank 4 and its newly highlighted radar-based parking mode deserves attention: built-in front and rear radar starts recording before an impact rather than after, and it supports up to 40 days of parking recording, far beyond the 16 to 24 hours most units manage.\n\nWith summer road-trip season arriving, dash cam interest is climbing. The good news is that the rankings have been stable through the spring product cycle, so buyers can purchase with confidence that today's top picks are not about to be leapfrogged.",
                "highlights": [
                    {"title": "VIOFO A329S Is the 4K Video Quality Benchmark", "body": "The A329S produces the sharpest footage in the class with a 4K front sensor that reads plates cleanly in daylight and holds detail under headlights at night. Its flexible three-channel front, rear, and interior setup is the configuration every 2026 reviewer measures against."},
                    {"title": "Thinkware U3000 Radar Parking Mode Stands Out", "body": "The U3000's built-in front and rear radar sensors detect movement in low-power parking mode and start recording before an impact rather than after. It supports up to 40 days of parking recording, far beyond the 16 to 24 hours most dash cams manage."},
                    {"title": "BlackVue Elite 9 Owns Connected Features", "body": "Cloud-based parking alerts and remote live viewing let you check on a parked car from your phone anywhere. For drivers who want eyes on their vehicle remotely, the Elite 9 remains the clearest choice in the category heading into summer road-trip season."},
                ],
            },
            "zh-tw": {
                "commentary": "2026 年年中的行車記錄器市場已經排出清楚的順位，VIOFO A329S 穩坐第一，原因很單純：它在最關鍵的那件事上做得最好，畫質夠銳利、夠實用。4K 前鏡頭白天看車牌清清楚楚，晚上在對向大燈下也能保住細節，這才是裝記錄器的真正意義。前、後、車內三鏡頭的彈性配置，是今年所有評測拿來當標準的那一台。\n\n第二名的 Vantrue N4 Pro S，我推薦給想要單機搞定三鏡頭的人。前、車內、後同時錄，夜拍表現又能維持一致，這件事其實不好做，N4 Pro S 做到了，而且不用拉一堆線去拼湊。跑外送、開 Uber 的駕駛特別有感。\n\n第三名 BlackVue Elite 9 是聯網功能的王者。雲端停車警報加上遠端即時查看，真的改變了你用記錄器的方式，人在外面用手機就能看停在路邊的車。第四名 Thinkware U3000 這次特別值得提的是雷達停車模式，前後內建雷達在撞擊前就開始錄影，而不是撞了才錄，而且停車錄影撐到 40 天，遠超一般機種的 16 到 24 小時。\n\n夏天自駕旅遊旺季快到了，記錄器的搜尋量正在往上爬。好消息是整個春季產品週期榜單都很穩，現在買可以很放心，今天的前幾名短期內不會被洗掉。",
                "highlights": [
                    {"title": "VIOFO A329S：4K 畫質的標竿", "body": "A329S 是同級裡畫質最銳利的一台，4K 前鏡頭白天看車牌清晰，夜間在大燈下保住細節。前、後、車內三鏡頭的彈性配置，是 2026 年所有評測拿來對標的基準機。"},
                    {"title": "Thinkware U3000 雷達停車模式亮眼", "body": "U3000 前後內建雷達在低耗電停車模式下偵測移動，撞擊前就開始錄影，而非撞後才錄。停車錄影最長撐到 40 天，遠超一般機種的 16 到 24 小時。"},
                    {"title": "BlackVue Elite 9 聯網功能稱王", "body": "雲端停車警報加遠端即時查看，人在哪都能用手機看停在路邊的車。想遠端盯著愛車的駕駛，Elite 9 在夏季自駕旺季前仍是這個品類最明確的選擇。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK dash-cams")


def build_e_readers():
    d, p = load("best-e-readers.json")
    entry = {
        "date": DATE,
        "rankings": last_rankings(d),
        "references": [
            {"title": "Best ereaders in 2026: 9 top ebook readers from Kindle, Kobo and more", "url": "https://www.techradar.com/best/best-ereader", "source": "TechRadar"},
            {"title": "The best ereaders for 2026", "url": "https://www.engadget.com/mobile/tablets/best-ereader-130013808.html", "source": "Engadget"},
            {"title": "The Best Amazon Kindle Alternatives, Tested By Our Editors", "url": "https://www.nbcnews.com/select/shopping/best-kindle-alternatives-rcna195364", "source": "NBC Select"},
        ],
        "i18n": {
            "en": {
                "commentary": "The e-reader market in June 2026 rewards readers who care about the fundamentals, and the Kindle Paperwhite 2025 holds the top spot because it nails them all. Reading experience scores 9.5, battery life scores 9.5, and the Amazon ecosystem integration is the smoothest path from wanting a book to reading it that exists on any device. For most people, this is the e-reader to buy without overthinking it.\n\nThe Kobo Libra Colour at rank 2 is the device I recommend to anyone who wants more than Amazon's walled garden offers. It has a 7-inch E Ink Kaleido 3 color display, physical page-turn buttons, IPX8 waterproofing, Bluetooth for audiobooks, and optional stylus support. The June 2026 launch of native StoryGraph integration is a genuine win: the Libra Colour becomes the first e-reader to automatically sync your reads and progress from the independent book-tracking platform, which is a meaningful draw for serious readers who track their habits. Kobo's built-in OverDrive tab also lets you search and borrow library books directly on the device, something Kindle still cannot match.\n\nThe Kindle Colorsoft at rank 3 brings color to Amazon's ecosystem and suits readers with comic, manga, and illustrated book libraries. The Kobo Clara Colour at rank 4 puts the same Kaleido 3 color technology in a more pocketable 6-inch body for readers who prioritize portability.\n\nThe rankings stay stable this cycle. With summer reading season arriving and people loading up devices for vacation travel, an e-reader remains one of the smartest gadget purchases you can make, and the Paperwhite's weeks-long battery life is exactly what a beach trip demands.",
                "highlights": [
                    {"title": "Kindle Paperwhite 2025 Nails the Fundamentals", "body": "A 9.5 reading experience score, 9.5 battery life, and the smoothest ecosystem on any device make the Paperwhite the e-reader most people should buy without overthinking. Weeks-long battery life is exactly what summer vacation travel demands."},
                    {"title": "Kobo Libra Colour Adds Native StoryGraph Sync", "body": "Launching June 2026, the Libra Colour is the first e-reader to natively sync reads and progress from the independent StoryGraph tracking platform. Combined with its 7-inch Kaleido 3 color screen, page-turn buttons, and built-in OverDrive library borrowing, it is the top pick beyond Amazon's ecosystem."},
                    {"title": "Color E Ink Has Two Strong Paths", "body": "The Kindle Colorsoft brings color into Amazon's ecosystem for comic and manga libraries, while the Kobo Clara Colour packs the same Kaleido 3 technology into a pocketable 6-inch body. Both prove color E Ink has matured into a real option this year."},
                ],
            },
            "zh-tw": {
                "commentary": "2026 年六月的電子閱讀器市場，獎勵那些把基本功做好的產品，Kindle Paperwhite 2025 穩坐第一就是因為它樣樣到位。閱讀體驗 9.5 分、電池續航 9.5 分，加上 Amazon 生態系整合，從想看一本書到真的開始讀，這條路在任何裝置上都沒有比它更順的。對多數人來說，不用想太多，買它就對了。\n\n第二名的 Kobo Libra Colour，是我推薦給想跳出 Amazon 高牆的人。7 吋 E Ink Kaleido 3 彩色螢幕、實體翻頁鍵、IPX8 防水、藍牙聽有聲書、還能選配觸控筆。2026 年六月新增的 StoryGraph 原生整合是真的有感的加分，Libra Colour 成為第一台能自動同步 StoryGraph 閱讀進度的閱讀器，對會記錄閱讀習慣的重度讀者很有吸引力。Kobo 內建的 OverDrive 分頁還能直接在機上搜尋、借閱圖書館的書，這點 Kindle 到現在還是做不到。\n\n第三名 Kindle Colorsoft 把彩色帶進 Amazon 生態系，適合看漫畫、圖文書的人。第四名 Kobo Clara Colour 用同樣的 Kaleido 3 彩色技術，塞進更好攜帶的 6 吋機身，重視輕巧的人會喜歡。\n\n這一輪榜單很穩。夏天閱讀季到了，大家都在幫裝置塞滿書準備出遊，電子閱讀器仍然是最聰明的 3C 投資之一，Paperwhite 撐好幾週的電池，正是去海邊度假最需要的。",
                "highlights": [
                    {"title": "Kindle Paperwhite 2025 基本功樣樣到位", "body": "閱讀體驗 9.5 分、電池 9.5 分，加上任何裝置上最順的生態系整合，多數人不用想太多買它就對。撐好幾週的續航，正是夏天出遊最需要的特性。"},
                    {"title": "Kobo Libra Colour 新增 StoryGraph 原生同步", "body": "2026 年六月上線，Libra Colour 是第一台能原生同步 StoryGraph 閱讀進度的閱讀器。配上 7 吋 Kaleido 3 彩色螢幕、實體翻頁鍵、內建 OverDrive 圖書館借閱，是跳出 Amazon 生態系後的首選。"},
                    {"title": "彩色電子紙有兩條好路線", "body": "Kindle Colorsoft 把彩色帶進 Amazon 生態系，適合漫畫圖文書收藏；Kobo Clara Colour 用同樣的 Kaleido 3 技術做成好攜帶的 6 吋機身。兩台都證明彩色電子紙今年已經成熟到可以認真考慮。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK e-readers")


def build_foldable_smartphones():
    d, p = load("best-foldable-smartphones.json")
    entry = {
        "date": DATE,
        "rankings": last_rankings(d),
        "references": [
            {"title": "Samsung Galaxy Z Fold 7 available for over $800 off in new deals", "url": "https://www.sammyfans.com/2026/06/01/samsung-galaxy-z-fold-7-available-for-over-800-off-in-new-deals/", "source": "Sammy Fans"},
            {"title": "Samsung Galaxy Unpacked Summer 2026: How to watch and what to expect", "url": "https://www.androidcentral.com/phones/samsung-galaxy/samsung-galaxy-unpacked-summer-2026-how-to-watch-and-what-to-expect", "source": "Android Central"},
            {"title": "Last Year's Biggest Fold is Suddenly the Smartest Buy of 2026", "url": "https://the-gadgeteer.com/2026/05/23/samsung-galaxy-z-fold-7-sale/", "source": "The Gadgeteer"},
        ],
        "i18n": {
            "en": {
                "commentary": "Foldables have crossed from novelty into genuine flagship territory, and the Galaxy Z Fold 7 holds rank 1 because it is the most complete foldable you can buy right now. The first 200MP wide camera in the Z series captures 4x more detail and produces images 44% brighter, and it does this in the thinnest, lightest Z Fold body Samsung has ever shipped. The display scores 9.5 and the camera 9.6, the strongest combination on this list.\n\nThe timing for buyers is excellent. With Samsung Galaxy Unpacked Summer 2026 approaching and the Z Fold 8 on the horizon, retailers have cut the Z Fold 7 hard: the 256GB model is selling for $1,600, a $400 drop from its $2,000 launch price, and Best Buy open-box units have hit $1,221. For anyone who wanted this phone at launch but balked at the price, this is the moment. The Z Fold 7 does not become a worse phone because a successor is coming, it becomes a smarter buy.\n\nThe Pixel 10 Pro Fold at rank 2 stays my pick for buyers who prioritize battery and durability. Its 9.5 battery and 9.7 durability scores lead the category, and Google's clean software plus seven years of updates make it the long-haul choice. The Oppo Find N5 at rank 3 delivers the best raw display experience at 9.4 in an impressively thin frame, while the Honor Magic V3 at rank 4 offers the best value among the premium folds at 9.0.\n\nThe rankings hold steady this cycle. The Z Fold 7's lead is built on hardware that the discounts only make more compelling.",
                "highlights": [
                    {"title": "Galaxy Z Fold 7 Leads on Camera and Design", "body": "The first 200MP wide camera in the Z series captures 4x more detail and 44% brighter images, packed into the thinnest, lightest Z Fold Samsung has built. With a 9.5 display and 9.6 camera score, it is the most complete foldable on the market."},
                    {"title": "Pre-Unpacked Discounts Make the Z Fold 7 the Smart Buy", "body": "With Galaxy Unpacked Summer 2026 approaching, the Z Fold 7 256GB has dropped to $1,600 from its $2,000 launch price, and Best Buy open-box units have hit $1,221. The phone is not worse because a successor is coming, it is a smarter buy."},
                    {"title": "Pixel 10 Pro Fold Wins on Battery and Longevity", "body": "A 9.5 battery and 9.7 durability score lead the category, and Google's clean software plus seven years of updates make the Pixel 10 Pro Fold the choice for buyers who plan to keep a foldable for the long haul."},
                ],
            },
            "zh-tw": {
                "commentary": "摺疊機已經從新奇玩意跨進真正的旗艦級別，Galaxy Z Fold 7 拿下第一，因為它是現在能買到最完整的摺疊機。Z 系列第一次用上 2 億畫素廣角鏡頭，細節多 4 倍、畫面亮 44%，而且這一切塞在三星史上最薄最輕的 Z Fold 機身裡。螢幕 9.5 分、相機 9.6 分，是榜單裡最強的組合。\n\n現在進場的時機很好。三星夏季 Unpacked 發表會快到了，Z Fold 8 也在路上，通路因此把 Z Fold 7 砍很大：256GB 版本賣到 $1,600 美元，比 $2,000 上市價直接少 $400，Best Buy 的開箱機甚至殺到 $1,221。當初想買又被價格勸退的人，現在就是那個時機。Z Fold 7 不會因為後繼機要來就變差，它只是變成更聰明的選擇。\n\n第二名 Pixel 10 Pro Fold 是我給重視續航和耐用度的人的首選。電池 9.5 分、耐用度 9.7 分都是全榜領先，加上 Google 乾淨的系統和七年更新，是想用很久的長線選擇。第三名 Oppo Find N5 螢幕體驗 9.4 分最頂，機身又薄得誇張；第四名 Honor Magic V3 則是高階摺疊機裡 CP 值最好的，9.0 分。\n\n這一輪榜單很穩。Z Fold 7 的領先建立在硬體實力上，降價只是讓它更有說服力。",
                "highlights": [
                    {"title": "Galaxy Z Fold 7 相機與設計雙領先", "body": "Z 系列首搭 2 億畫素廣角鏡，細節多 4 倍、畫面亮 44%，全塞進三星史上最薄最輕的 Z Fold 機身。螢幕 9.5 分、相機 9.6 分，是市面上最完整的摺疊機。"},
                    {"title": "發表會前降價，Z Fold 7 成最聰明選擇", "body": "夏季 Unpacked 將至，Z Fold 7 256GB 從 $2,000 上市價降到 $1,600，Best Buy 開箱機更殺到 $1,221。後繼機要來不代表這台變差，反而是更划算的進場時機。"},
                    {"title": "Pixel 10 Pro Fold 續航與耐用度取勝", "body": "電池 9.5 分、耐用度 9.7 分全榜領先，加上 Google 乾淨系統和七年更新，Pixel 10 Pro Fold 是打算把摺疊機用很久的人的首選。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK foldable-smartphones")


def build_portable_chargers():
    d, p = load("best-portable-chargers.json")
    entry = {
        "date": DATE,
        "rankings": last_rankings(d),
        "references": [
            {"title": "Best Power Bank 2026: 5 New Chargers That Raised the Bar", "url": "https://the-gadgeteer.com/2026/05/06/best-power-bank-2026-five-new-chargers/", "source": "The Gadgeteer"},
            {"title": "The best power banks and portable chargers for every device in 2026", "url": "https://www.engadget.com/computing/accessories/best-power-bank-143048526.html", "source": "Engadget"},
            {"title": "Best Power Bank of 2026: Top Picks for iPhone, Android, and Laptops", "url": "https://www.anker.com/blogs/power-banks/best-power-bank", "source": "Anker"},
        ],
        "i18n": {
            "en": {
                "commentary": "The portable charger category in 2026 has split cleanly into a power tier and a pocket tier, and the Anker Prime 26K 300W holds rank 1 because it owns the power tier outright. It packs 26,250mAh into a single brick that delivers 300W total output across two USB-C ports and one USB-A, enough to run a 16-inch MacBook Pro at full speed through a single 140W port while topping off a phone and tablet on the side. The speed score of 9.9 is the highest on the list, and its 250W dual-port input recharges the bank to 50% in just 13 minutes, which is genuinely transformative for travel days. Anker's own 2026 roundup positions it as the bank to beat, and I agree.\n\nThe Anker Prime 27650 250W at rank 2 trades a little output for the highest capacity score on the list at 9.6, making it the pick for people who want maximum runtime over maximum wattage. The Anker 737 PowerCore 24K at rank 3 remains the reliable all-rounder, with a clear digital display and balanced 9.4 speed for buyers who do not need the bleeding edge.\n\nThe UGREEN Nexode 25000mAh 200W at rank 4 is the value play that clears the laptop-charging bar without the flagship price, and 2026 reviews consistently group it with the Anker Prime and EcoFlow Rapid Pro X as the chargers that genuinely run laptops.\n\nThe rankings stay steady this cycle. With summer travel ramping up and people packing for flights and road trips, a high-capacity bank that recharges in minutes rather than hours is exactly the kind of purchase that pays off the first time your phone hits 5% at an airport gate.",
                "highlights": [
                    {"title": "Anker Prime 26K 300W Owns the Power Tier", "body": "300W total output across three ports runs a 16-inch MacBook Pro at full speed through a single 140W port while charging a phone and tablet alongside. A 9.9 speed score leads the list, and 250W input refills the bank to 50% in just 13 minutes."},
                    {"title": "Anker Prime 27650 Wins on Capacity", "body": "With the highest capacity score on the list at 9.6, the Prime 27650 250W trades a little peak wattage for maximum runtime. It is the pick for travelers who want the most charges between top-ups rather than the absolute fastest output."},
                    {"title": "UGREEN Nexode Delivers Laptop Power for Less", "body": "The Nexode 25000mAh 200W clears the laptop-charging bar without flagship pricing, and 2026 reviews consistently group it with the Anker Prime and EcoFlow Rapid Pro X as banks that genuinely power laptops, not just phones."},
                ],
            },
            "zh-tw": {
                "commentary": "2026 年的行動電源市場乾淨地分成兩個層級，一個是大功率層、一個是口袋層，Anker Prime 26K 300W 拿下第一，因為它把大功率層整個吃下來。26,250mAh 塞進一塊磚裡，三個埠（兩個 USB-C 一個 USB-A）總輸出 300W，光是一個 140W 埠就能讓 16 吋 MacBook Pro 全速運轉，旁邊還能同時幫手機平板充電。速度 9.9 分是全榜最高，而且 250W 雙埠輸入只要 13 分鐘就能充回 50%，對要趕飛機的旅行日來說根本是救命功能。Anker 自己 2026 年的榜單也把它擺在標竿位置，我完全同意。\n\n第二名 Anker Prime 27650 250W 犧牲一點輸出，換來全榜最高的容量分 9.6，適合要的是最長續航而非最大瓦數的人。第三名 Anker 737 PowerCore 24K 仍是可靠的全能選手，數位顯示清楚、速度 9.4 分均衡，不需要頂規的人選它剛好。\n\n第四名 UGREEN Nexode 25000mAh 200W 是性價比之選，過了筆電充電的門檻又不用付旗艦價，2026 年的評測一直把它跟 Anker Prime、EcoFlow Rapid Pro X 歸在「真的能充筆電」這一群。\n\n這一輪榜單很穩。夏天出遊季升溫，大家在收行李準備搭機自駕，一顆大容量又能幾分鐘充飽的行動電源，就是那種你在登機門看到手機剩 5% 時會慶幸有買的東西。",
                "highlights": [
                    {"title": "Anker Prime 26K 300W 大功率層霸主", "body": "三埠總輸出 300W，光一個 140W 埠就能讓 16 吋 MacBook Pro 全速跑，旁邊還能充手機平板。速度 9.9 分全榜最高，250W 輸入只要 13 分鐘充回 50%。"},
                    {"title": "Anker Prime 27650 容量取勝", "body": "容量分 9.6 全榜最高，Prime 27650 250W 犧牲一點峰值瓦數換最長續航。適合要的是兩次補電之間能充最多次，而非最快輸出的旅行者。"},
                    {"title": "UGREEN Nexode 用更低價給你筆電功率", "body": "Nexode 25000mAh 200W 過了筆電充電門檻又不用付旗艦價，2026 年評測一直把它跟 Anker Prime、EcoFlow Rapid Pro X 歸在真能充筆電的那一群，不只是充手機。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK portable-chargers")


def build_portable_power_stations():
    d, p = load("best-portable-power-stations.json")
    entry = {
        "date": DATE,
        "rankings": last_rankings(d),
        "references": [
            {"title": "The 5 Best Portable Power Stations of 2026, Tested and Reviewed", "url": "https://www.outdoorlife.com/gear/best-portable-power-stations-2026/", "source": "Outdoor Life"},
            {"title": "6 Best Portable Power Stations of 2026 | The Inertia Tested", "url": "https://www.theinertia.com/gear/best-portable-power-stations/", "source": "The Inertia"},
            {"title": "BLUETTI vs EcoFlow: Which Portable Power Station Wins in 2026", "url": "https://rosettadigital.com/bluetti-vs-ecoflow/", "source": "Rosetta Digital"},
        ],
        "i18n": {
            "en": {
                "commentary": "Portable power station season peaks in summer, when camping trips, RV travel, and the threat of storm-season outages all converge, and the EcoFlow Delta 3 Plus holds rank 1 because it is the strongest all-around choice for most buyers. At $599 it balances capacity, output, expandability, and versatility better than anything else at its price. The charging speed score of 9.5 reflects EcoFlow's X-Stream technology that refills the unit in under two hours, and the 9.5 value score confirms you are not paying a premium for that speed. For anyone buying their first serious power station this summer, this is where I point them.\n\nThe Bluetti Elite 200 V2 at rank 2 represents the other philosophy in this category, and it represents it well. Bluetti builds around LiFePO4 chemistry rated for 3,500+ charge cycles, which translates into a longer usable lifespan and lower cost per watt-hour over years of ownership. Its reliability score of 9.2 is the highest on the list, and the longer warranty coverage matters for a device you expect to keep for a decade.\n\nThe Anker Solix C2000 Gen2 at rank 3 is the balanced middle path, pairing solid 9.0 output power with dependable reliability. The EcoFlow Delta Pro 3 at rank 4 is the high-capacity pick for whole-home backup ambitions, leading the list on raw capacity at 9.5 for buyers who need to power more than a campsite.\n\nThe rankings stay stable this cycle. The EcoFlow-versus-Bluetti split, speed and smart features against capacity and longevity, remains the clearest way to choose, and both top picks are genuinely excellent at what they set out to do.",
                "highlights": [
                    {"title": "EcoFlow Delta 3 Plus Is the Best All-Rounder at $599", "body": "It balances capacity, output, expandability, and versatility better than anything else at its price. A 9.5 charging speed via X-Stream refills the unit in under two hours, and a 9.5 value score confirms you are not paying a premium for that speed."},
                    {"title": "Bluetti Elite 200 V2 Wins on Longevity", "body": "Built around LiFePO4 chemistry rated for 3,500+ charge cycles, it delivers a longer usable lifespan and lower cost per watt-hour over years of ownership. Its 9.2 reliability score leads the list, backed by longer warranty coverage."},
                    {"title": "EcoFlow Delta Pro 3 Leads Raw Capacity", "body": "With the highest capacity score on the list at 9.5, the Delta Pro 3 is the pick for whole-home backup ambitions. It is the choice for buyers who need to power far more than a campsite through a multi-day outage."},
                ],
            },
            "zh-tw": {
                "commentary": "行動電源站的旺季就在夏天，露營、開露營車、加上颱風季停電的威脅全擠在一起，EcoFlow Delta 3 Plus 拿下第一，因為它是多數人最強的全能選擇。$599 美元的價位，在容量、輸出、擴充性、多功能之間的平衡比同價位任何一台都好。充電速度 9.5 分來自 EcoFlow 的 X-Stream 技術，不到兩小時就能充滿，而 9.5 分的性價比也證明你不是為了那個速度多付錢。今年夏天想買第一台像樣電源站的人，我就推這台。\n\n第二名 Bluetti Elite 200 V2 代表這個品類的另一種哲學，而且代表得很好。Bluetti 用磷酸鐵鋰電池，循環壽命標到 3,500 次以上，換算成多年使用就是更長的可用壽命、更低的每瓦時成本。可靠度 9.2 分是全榜最高，而且保固期更長，對一台你打算用十年的裝置來說很重要。\n\n第三名 Anker Solix C2000 Gen2 是平衡的中間路線，9.0 分的輸出功率配上可靠的穩定度。第四名 EcoFlow Delta Pro 3 是大容量取向，瞄準全屋備電，容量 9.5 分全榜領先，適合需要供電範圍遠超一個營地的人。\n\n這一輪榜單很穩。EcoFlow 對上 Bluetti 的選擇，速度與智慧功能對上容量與壽命，仍然是最清楚的判斷方式，而且兩個第一名在各自的定位上都做得真的好。",
                "highlights": [
                    {"title": "EcoFlow Delta 3 Plus：$599 最強全能", "body": "在容量、輸出、擴充性、多功能之間的平衡勝過同價位任何一台。X-Stream 充電速度 9.5 分，不到兩小時充滿，9.5 分性價比也證明你不是為速度多付錢。"},
                    {"title": "Bluetti Elite 200 V2 壽命取勝", "body": "採用磷酸鐵鋰電池，循環壽命標到 3,500 次以上，多年使用下來壽命更長、每瓦時成本更低。可靠度 9.2 分全榜最高，還有更長的保固撐腰。"},
                    {"title": "EcoFlow Delta Pro 3 容量領先", "body": "容量分 9.5 全榜最高，Delta Pro 3 是瞄準全屋備電的選擇。需要供電範圍遠超一個營地、撐過多日停電的人，就選它。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK portable-power-stations")


def build_portable_projectors():
    d, p = load("best-portable-projectors.json")
    entry = {
        "date": DATE,
        "rankings": last_rankings(d),
        "references": [
            {"title": "Best portable projector of 2026: Tested for streaming and presenting on the go", "url": "https://www.techradar.com/pro/best-portable-projector", "source": "TechRadar"},
            {"title": "Best portable projectors of 2026, tried and tested", "url": "https://www.cnn.com/cnn-underscored/reviews/best-portable-projectors", "source": "CNN Underscored"},
            {"title": "The Best Portable Projectors in 2026", "url": "https://www.gizmochina.com/2026/03/07/best-portable-projectors-in-2026/", "source": "Gizmochina"},
        ],
        "i18n": {
            "en": {
                "commentary": "Portable projectors hit their natural stride in summer, when backyard movie nights and camping trips give a battery-powered projector a real job to do, and the XGIMI MoGo 4 Laser holds rank 1 because it is the most complete package in the category. Its triple laser engine produces 550 ISO lumens and covers 110% of the BT.2020 color gamut, which means genuinely rich, saturated color rather than the washed-out look that plagued portable projectors a couple of years ago. The built-in battery delivers up to 2.5 hours of video, enough for a feature film under the stars, and the brightness, portability, and smart platform all score 9.0.\n\nThe LG CineBeam Q at rank 2 is the design-forward pick, a strikingly compact unit with a clean Google TV based smart platform and a 9.0 portability score that makes it the easiest to toss in a bag. The Hisense M2 Pro at rank 3 is the brightness specialist, scoring 9.0 there, best suited to a fixed spot where you can plug it in rather than a true grab-and-go device given its 6.5 battery score.\n\nThe Nebula Mars 3 at rank 4 is the rugged outdoor champion. Its 9.0 battery score leads the list, and the durable, splash-resistant build is purpose-made for camping and backyard use where the MoGo prioritizes image quality. For buyers whose projector will spend its life outdoors, the Mars 3 earns the look.\n\nThe rankings stay stable this cycle. With summer evenings arriving, the MoGo 4 Laser's combination of real color performance and genuine portability makes it the projector I would pack first.",
                "highlights": [
                    {"title": "XGIMI MoGo 4 Laser Leads on Color and Completeness", "body": "Its triple laser engine produces 550 ISO lumens and covers 110% of BT.2020 for genuinely rich, saturated color. A built-in battery delivers up to 2.5 hours of video, enough for a full feature film under the stars, with 9.0 scores across brightness, portability, and smart platform."},
                    {"title": "Nebula Mars 3 Owns the Outdoor Use Case", "body": "A category-leading 9.0 battery score and a durable, splash-resistant build make the Mars 3 purpose-built for camping and backyard movie nights. For buyers whose projector will live outdoors, it is the most sensible pick on the list."},
                    {"title": "LG CineBeam Q Is the Grab-and-Go Pick", "body": "A strikingly compact body and a 9.0 portability score make the CineBeam Q the easiest projector here to toss in a bag, paired with a clean Google TV based smart platform for fuss-free streaming wherever you set it up."},
                ],
            },
            "zh-tw": {
                "commentary": "可攜投影機在夏天才真正派上用場，後院電影夜和露營讓一台有電池的投影機有了真正的工作可做，XGIMI MoGo 4 Laser 拿下第一，因為它是這個品類裡最完整的方案。三雷射引擎產生 550 ISO 流明，涵蓋 110% 的 BT.2020 色域，意思是色彩真的飽和濃郁，不再是兩年前那種可攜投影機褪色的觀感。內建電池可播放最長 2.5 小時影片，星空下看完一整部電影綽綽有餘，亮度、便攜性、智慧平台都拿 9.0 分。\n\n第二名 LG CineBeam Q 是設計取向的選擇，機身小巧得很搶眼，搭配乾淨的 Google TV 智慧平台，9.0 分的便攜性讓它最容易塞進包包帶著走。第三名 Hisense M2 Pro 是亮度專家，這項拿 9.0 分，但電池只有 6.5 分，比較適合固定一個能插電的位置，而不是真的隨拿隨走。\n\n第四名 Nebula Mars 3 是戶外耐操王。電池 9.0 分全榜最高，堅固防潑水的機身就是為露營和後院使用而生，MoGo 拼的是畫質，Mars 3 拼的是耐用。投影機注定要在戶外過日子的人，Mars 3 當之無愧。\n\n這一輪榜單很穩。夏夜到了，MoGo 4 Laser 把真實色彩表現和真正的便攜性結合在一起，是我會第一個塞進行李的投影機。",
                "highlights": [
                    {"title": "XGIMI MoGo 4 Laser 色彩與完整度雙領先", "body": "三雷射引擎 550 ISO 流明，涵蓋 110% BT.2020 色域，色彩真的飽和濃郁。內建電池最長播 2.5 小時影片，星空下看完整部電影沒問題，亮度、便攜、智慧平台全拿 9.0 分。"},
                    {"title": "Nebula Mars 3 戶外場景之王", "body": "電池 9.0 分全榜最高，堅固防潑水的機身就是為露營和後院電影夜而生。投影機注定要在戶外過日子的人，它是榜單上最合理的選擇。"},
                    {"title": "LG CineBeam Q 隨拿隨走首選", "body": "機身小巧搶眼，便攜性 9.0 分，CineBeam Q 是這裡最容易塞進包包的投影機，配上乾淨的 Google TV 智慧平台，不管擺哪都能無痛串流。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK portable-projectors")


def build_soundbars():
    d, p = load("best-soundbars.json")
    entry = {
        "date": DATE,
        "rankings": last_rankings(d),
        "references": [
            {"title": "The 6 Best Dolby Atmos Soundbars of 2026", "url": "https://www.rtings.com/soundbar/reviews/best/by-type/dolby-atmos", "source": "RTINGS"},
            {"title": "Best Dolby Atmos soundbars 2026: our reviewers' five recommendations", "url": "https://www.whathifi.com/best-buys/best-dolby-atmos-soundbars-the-best-atmos-tv-speakers", "source": "What Hi-Fi?"},
            {"title": "Best soundbars in 2026: Top picks for movies, TV, and Dolby Atmos", "url": "https://www.soundguys.com/best-soundbars-6617/", "source": "SoundGuys"},
        ],
        "i18n": {
            "en": {
                "commentary": "The soundbar category in 2026 is genuinely spoiled for choice at the top, and the Samsung HW-Q990F holds rank 1 because no rival matches its sheer scale of immersion. This is an 11.1.4 system with discrete wireless rear satellites and four up-firing drivers, and the surround score of 9.8 reflects exactly what that hardware delivers: a fully wrapped, room-filling sound field that puts you inside the action. The Atmos score of 9.6 and gaming score of 9.3 round it out into the most complete home theater package you can buy in a box. If you want the biggest, most enveloping sound, this is the one.\n\nThe Sonos Arc Ultra at rank 2 is the choice I make for buyers who weigh music as heavily as movies. Its 14-driver array, with upgraded side-firing and up-firing units, creates a convincing Atmos bubble, and the music score of 9.7 leads the entire list. The minimal design and the Sonos ecosystem make it the most livable premium bar here, and reviewers across 2026 consistently call it the best overall for most people.\n\nThe Sony Bravia Theatre Bar 9 at rank 3 brings Sony's spatial processing expertise with a strong 9.4 Atmos score, especially compelling paired with a Bravia TV. The LG S95TR at rank 4 delivers a wide, articulate surround field at 9.2 for buyers in the LG ecosystem.\n\nThe rankings stay stable this cycle. The real story remains the gap between the Q990F's brute-force immersion and the Arc Ultra's musical finesse, and which one is right comes down to whether your priority is cinema scale or all-around versatility.",
                "highlights": [
                    {"title": "Samsung HW-Q990F Delivers the Biggest Immersion", "body": "An 11.1.4 system with discrete wireless rear satellites and four up-firing drivers earns a 9.8 surround score, the highest on the list. For a fully wrapped, room-filling sound field straight out of the box, no rival matches its scale."},
                    {"title": "Sonos Arc Ultra Leads on Music", "body": "A 14-driver array with upgraded side and up-firing units creates a convincing Atmos bubble, and a 9.7 music score tops the list. Its minimal design and ecosystem make it the most livable premium bar, and reviewers call it the best overall for most people."},
                    {"title": "The Choice Comes Down to Cinema vs Versatility", "body": "The Q990F's brute-force immersion suits movie-first buyers who want maximum scale, while the Arc Ultra's musical finesse and clean design suit those who weigh music as heavily as film. Both are genuinely excellent at what they set out to do."},
                ],
            },
            "zh-tw": {
                "commentary": "2026 年的 soundbar 市場頂端真的是選擇多到幸福，Samsung HW-Q990F 拿下第一，因為沒有對手能比得上它那種環繞的規模。這是一套 11.1.4 系統，配獨立無線後環繞和四顆向上發聲單體，環繞分數 9.8 反映的正是這套硬體帶來的東西：一個完整包覆、填滿整個房間的聲場，把你拉進畫面裡。Atmos 9.6 分、遊戲 9.3 分，補齊成市面上盒裝就能買到最完整的家庭劇院方案。想要最大、最包圍的聲音，就是它。\n\n第二名 Sonos Arc Ultra 是我給音樂跟電影一樣看重的人的選擇。14 單體陣列，側向和向上發聲單體都升級過，營造出有說服力的 Atmos 包圍感，音樂分數 9.7 是全榜最高。簡約的設計加上 Sonos 生態系，讓它成為這裡最好相處的高階 soundbar，2026 年的評測也一致說它是多數人最佳的整體選擇。\n\n第三名 Sony Bravia Theatre Bar 9 帶來 Sony 的空間音效處理功力，Atmos 9.4 分很強，搭 Bravia 電視特別有說服力。第四名 LG S95TR 提供寬闊清晰的環繞聲場，9.2 分，適合 LG 生態系的用戶。\n\n這一輪榜單很穩。真正的看點還是 Q990F 那種蠻力包圍感跟 Arc Ultra 音樂細膩度之間的差距，選哪個就看你要的是電影規模還是全面的多功能性。",
                "highlights": [
                    {"title": "Samsung HW-Q990F 帶來最大包圍感", "body": "11.1.4 系統配獨立無線後環繞和四顆向上單體，環繞分數 9.8 全榜最高。想要完整包覆、填滿整個房間的聲場，盒裝開箱即用，沒有對手比得上它的規模。"},
                    {"title": "Sonos Arc Ultra 音樂表現領先", "body": "14 單體陣列，側向與向上單體都升級，營造有說服力的 Atmos 包圍感，音樂分數 9.7 全榜最高。簡約設計加生態系讓它最好相處，評測一致說它是多數人最佳整體選擇。"},
                    {"title": "選擇取決於電影規模 vs 全面多功能", "body": "Q990F 的蠻力包圍感適合電影優先、要最大規模的人；Arc Ultra 的音樂細膩度和乾淨設計，適合音樂跟電影一樣看重的人。兩台在各自定位上都做得真的好。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK soundbars")


def build_vpn_services():
    d, p = load("best-vpn-services.json")
    entry = {
        "date": DATE,
        "rankings": last_rankings(d),
        "references": [
            {"title": "The 3 Best VPNs of 2026", "url": "https://www.rtings.com/vpn/reviews/best/vpn", "source": "RTINGS"},
            {"title": "Best VPN services 2026: 7 top picks for every VPN need", "url": "https://www.pcworld.com/article/406870/best-vpn-services-2.html", "source": "PCWorld"},
            {"title": "NordVPN vs Proton VPN: 8 Tests, 1 Clear Winner in 2026", "url": "https://cyberinsider.com/vpn/comparison/nordvpn-vs-protonvpn/", "source": "CyberInsider"},
        ],
        "i18n": {
            "en": {
                "commentary": "The VPN market in 2026 rewards genuine privacy engineering over marketing, and Mullvad holds rank 1 because it remains the purest expression of that principle. It requires no account or email, accepts cash and cryptocurrency, and operates under a no-logs policy that has been confirmed by an actual police raid rather than just a paid audit. Its flat 5 euro per month price comes with no manipulative long-term discounts, and the privacy score of 9.8 leads the list. A May 2026 disclosure about exit IP fingerprinting was notable, but the way Mullvad handled it is exactly why it keeps the top spot: the co-founder publicly acknowledged the vulnerability and confirmed a fix was already in testing. Transparency under pressure is the whole point of trusting a privacy provider, and Mullvad delivered it.\n\nProton VPN at rank 2 is the pick for users who want serious privacy with a mainstream-friendly interface. Swiss-based and independently audited four times, it pairs a 9.5 privacy score with the strongest network at 9.5, and at $3.59 per month on a two-year plan it stays competitive even after recent price changes.\n\nNordVPN at rank 3 wins on raw performance, leading the list on speed at 9.1 and network at 9.6. It now ships full post-quantum support in its NordLynx protocol across all apps, enabling hybrid NIST-standard algorithms that defend against harvest-now-decrypt-later attacks, which is a genuine forward-looking advantage for anyone protecting data over the long term.\n\nThe rankings stay stable this cycle. Mullvad's no-compromise privacy, Proton's audited balance, and NordVPN's speed-and-streaming strength remain the three clearest reasons to pick each, and how you weigh privacy against performance decides which fits.",
                "highlights": [
                    {"title": "Mullvad Leads on No-Compromise Privacy", "body": "No account or email, cash and crypto accepted, and a no-logs policy confirmed by an actual police raid rather than a paid audit. A 9.8 privacy score and flat 5 euro pricing with no manipulative discounts make it the purest privacy choice in 2026."},
                    {"title": "Mullvad's Handling of the Fingerprinting Disclosure", "body": "A May 2026 exit IP fingerprinting disclosure tested the provider, and Mullvad responded exactly right: its co-founder publicly acknowledged the vulnerability and confirmed a fix was already in testing. Transparency under pressure is why it keeps the top spot."},
                    {"title": "NordVPN Ships Full Post-Quantum Protection", "body": "NordVPN now enables full post-quantum support in NordLynx across all apps, using hybrid NIST-standard algorithms that defend against harvest-now-decrypt-later attacks. Paired with category-leading 9.1 speed and 9.6 network scores, it is the performance pick."},
                ],
            },
            "zh-tw": {
                "commentary": "2026 年的 VPN 市場，獎勵的是真正的隱私工程而非行銷話術，Mullvad 拿下第一，因為它仍然是這個原則最純粹的體現。不需要帳號或 email，接受現金和加密貨幣付款，而它的無紀錄政策是被真正的警方搜索驗證過的，不是花錢買的稽核報告。每月 5 歐元的平價沒有那種綁長約的誘導折扣，隱私分數 9.8 全榜最高。2026 年五月有一則關於出口 IP 指紋辨識的揭露值得注意，但 Mullvad 處理它的方式，正是它守住第一的原因：共同創辦人公開承認這個漏洞，並確認修正已在測試中。在壓力下保持透明，這才是信任一家隱私供應商的全部意義，而 Mullvad 做到了。\n\n第二名 Proton VPN 是給想要紮實隱私又要主流友善介面的人。瑞士公司、經過四次獨立稽核，隱私 9.5 分配上最強的伺服器網路 9.5 分，兩年方案每月 $3.59 美元，就算經過最近的調價仍然有競爭力。\n\n第三名 NordVPN 靠純效能取勝，速度 9.1 分、網路 9.6 分都是全榜領先。它現在在所有 App 的 NordLynx 協定裡都標配完整的後量子加密支援，採用混合 NIST 標準演算法，防範「先竊取、之後再解密」的攻擊，對需要長期保護資料的人是真正前瞻的優勢。\n\n這一輪榜單很穩。Mullvad 的零妥協隱私、Proton 的稽核平衡、NordVPN 的速度與串流實力，仍然是各自最清楚的選擇理由，你怎麼權衡隱私和效能，就決定哪一個適合你。",
                "highlights": [
                    {"title": "Mullvad 零妥協隱私領先", "body": "不用帳號或 email，接受現金和加密貨幣，無紀錄政策被真正的警方搜索驗證過，不是花錢買的稽核。隱私分數 9.8 加上每月 5 歐元無綁約誘導折扣的平價，是 2026 年最純粹的隱私選擇。"},
                    {"title": "Mullvad 處理指紋揭露的方式", "body": "2026 年五月出口 IP 指紋辨識的揭露考驗了這家供應商，Mullvad 的回應完全正確：共同創辦人公開承認漏洞，並確認修正已在測試中。壓力下的透明，就是它守住第一的原因。"},
                    {"title": "NordVPN 標配完整後量子防護", "body": "NordVPN 現在在所有 App 的 NordLynx 裡標配完整後量子支援，採用混合 NIST 標準演算法，防範先竊取後解密的攻擊。配上全榜領先的速度 9.1 分、網路 9.6 分，是效能取向的首選。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK vpn-services")


if __name__ == "__main__":
    build_dash_cams()
    build_e_readers()
    build_foldable_smartphones()
    build_portable_chargers()
    build_portable_power_stations()
    build_portable_projectors()
    build_soundbars()
    build_vpn_services()
    print("Batch 8 complete")
