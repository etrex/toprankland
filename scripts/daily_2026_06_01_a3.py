import json
from pathlib import Path

DATE = "2026-06-01"
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


ENTRIES = {
    "best-action-cameras.json": {
        "references": [
            {"title": "Sorry GoPro, the DJI Osmo Action 6 just won the action camera war", "url": "https://www.tomsguide.com/cameras-photography/gopro-action-cameras/dji-osmo-action-6-review", "source": "Tom's Guide"},
            {"title": "DJI Osmo Action 6 vs GoPro Hero 13 Black - for night it's no contest", "url": "https://amateurphotographer.com/buying-advice/dji-osmo-action-6-vs-gopro-hero-13-black-which-is-the-best-action-camera/", "source": "Amateur Photographer"},
            {"title": "Best Action Camera 2026: DJI vs GoPro vs Insta360", "url": "https://actioncameraview.com/best-action-camera-2026-ultimate-buying-guide/", "source": "Action Camera View"},
        ],
        "i18n": {
            "en": {
                "commentary": "The DJI Osmo Action 6 keeps the top spot, and after another week of comparisons I am more convinced than ever. That 1/1.1-inch square sensor with a variable f/2.0 to f/4.0 aperture is the real story here. It pulls roughly 13.5 stops of dynamic range and holds clean detail once the sun drops, which is exactly where most action cameras fall apart. At around 436 dollars on Amazon it asks for a premium, but you get 20 meters of waterproofing with no case and a battery that runs close to four hours of real shooting. For anyone filming dives, ski runs, or night rides, this is the camera I hand them first. The interesting wrinkle this week is GoPro. The Hero 14 Black is confirmed for a late April 2026 launch with a new 5nm GP3 processor, a 1-inch sensor, 8K30 capture, and HyperSmooth 7.0 with AI prediction. That is GoPro's biggest hardware leap since 2021, and it could shake up positions two through four once units ship and get tested. For now I am holding the order steady because real-world footage beats spec sheets every time. The Insta360 Ace Pro 2 stays my number two for its Leica color science and strong low-light handling, and the GoPro Mission 1 Pro keeps third on the strength of its stabilization. The Hero 13 Black remains a fine buy at 419 dollars if you live inside the GoPro modular ecosystem, but its 1/1.9-inch sensor shows grain after dark. My advice: if you shoot daytime adventure, any of the top five will serve you well, and if low light matters, the Action 6 is the safest money you can spend right now.",
                "highlights": [
                    {"title": "Variable aperture leads the field", "body": "The Action 6's f/2.0 to f/4.0 lens on a 1/1.1-inch sensor delivers around 13.5 stops of dynamic range, the widest in the category."},
                    {"title": "Night shooting is the dividing line", "body": "GoPro's 1/1.9-inch sensor grains up after sunset, while the larger DJI sensor stays clean, which decides most low-light comparisons."},
                    {"title": "Hero 14 Black is imminent", "body": "Confirmed for late April 2026 with a 5nm GP3 chip, 1-inch sensor, 8K30, and HyperSmooth 7.0, GoPro's biggest jump since 2021."},
                    {"title": "Waterproofing and battery seal the value", "body": "20 meters waterproof with no case plus near four-hour runtime make the Action 6 a confident pick at its roughly 436 dollar price."},
                ],
            },
            "zh-tw": {
                "commentary": "DJI Osmo Action 6 這週繼續穩坐冠軍，老實說我看了一輪比較之後更服氣了。它那顆 1/1.1 吋的方形感光元件，加上 f/2.0 到 f/4.0 的可變光圈，才是真正的關鍵。動態範圍大概有 13.5 級，太陽一下山照樣壓得住雜訊，這正是大多數運動相機會翻車的地方。台灣水貨大概落在台幣一萬三上下，價格確實不算親民，可是免防水殼就能下潛 20 公尺，實拍續航又能撐到接近四小時，對於玩潛水、滑雪、夜騎的人，我第一個就推它。這週比較有看頭的是 GoPro。Hero 14 Black 已經確定 2026 年四月底登場，換上 5nm 的 GP3 處理器、一吋感光元件、8K30 錄影，還有加上 AI 預測的 HyperSmooth 7.0。這是 GoPro 從 2021 年以來最大的硬體升級，等實機上市測完，第二到第四名很可能會洗牌。不過我現在還是先按兵不動，畢竟實拍畫面永遠比規格表可靠。Insta360 Ace Pro 2 靠著徠卡調色跟不錯的低光表現，繼續守住第二。GoPro Mission 1 Pro 靠防穩排第三。Hero 13 Black 台幣一萬二左右還是不錯，前提是你已經在 GoPro 模組生態裡，但那顆 1/1.9 吋感光元件入夜後雜訊就很明顯。我的建議很簡單，白天拍冒險，前五名隨便挑都好用。在意低光，現在最穩的選擇就是 Action 6。",
                "highlights": [
                    {"title": "可變光圈領先全場", "body": "Action 6 的 f/2.0 到 f/4.0 鏡頭搭 1/1.1 吋感光元件，動態範圍約 13.5 級，是這個級距最寬的。"},
                    {"title": "夜拍就是分水嶺", "body": "GoPro 的 1/1.9 吋感光元件入夜就起雜訊，DJI 大底依舊乾淨，低光比較幾乎一面倒。"},
                    {"title": "Hero 14 Black 蓄勢待發", "body": "確定 2026 年四月底登場，5nm GP3 晶片、一吋感光元件、8K30、HyperSmooth 7.0，是 GoPro 近年最大躍進。"},
                    {"title": "防水與續航撐起價值", "body": "免殼下潛 20 公尺加上接近四小時續航，讓 Action 6 在台幣一萬三上下依然推得下手。"},
                ],
            },
        },
    },
    "best-air-fryers.json": {
        "references": [
            {"title": "The 6 Best Air Fryers of 2026", "url": "https://www.rtings.com/air-fryer/reviews/best/air-fryers", "source": "RTINGS"},
            {"title": "Ninja Foodi FlexBasket Air Fryer review for 2026", "url": "https://shopping.yahoo.com/home-garden/kitchen/review/ninja-foodi-flexbasket-review-205822548.html", "source": "Yahoo Shopping"},
            {"title": "6 Best Air Fryers of 2026, Lab-Tested and Reviewed", "url": "https://www.consumerreports.org/appliances/air-fryers/best-air-fryers-of-the-year-a3919863393/", "source": "Consumer Reports"},
        ],
        "i18n": {
            "en": {
                "commentary": "The Ninja Foodi DZ550 stays my number one, and the latest lab roundups back it up. This 10-quart dual-basket model is the one I recommend to families because it cooks two foods two ways at once and still scales down for a solo dinner. RTINGS again names it the best air fryer they have tested, and that consistency matters when you are spending real money on a countertop appliance. The newer Ninja Foodi FlexBasket has been earning praise this season for the same dual-zone idea in a sleeker frame, running two 3.5-quart batches separately or opening up to a 7-quart single basket when you pull the divider. I am watching it closely, but I keep the DZ550 on top because its larger total capacity and proven track record give it the edge for the price. The Cosori TurboBlaze holds second as my value champion, fast, easy to clean, and quiet enough that I forget it is running. The Typhur Dome 2 sits third for anyone who wants near-oven results and does not mind paying for them. One trend worth flagging: glass-basket designs like the Ninja Crispi are gaining ground because you can see your food cook and the containers double as storage and serving dishes. That is genuinely useful for small kitchens. My buying advice stays simple. If you cook for a household, the DZ550 dual-basket is the workhorse. If you cook for one or two and want the lowest price with the least cleanup, the Cosori TurboBlaze is the smarter spend. Both will outlast the trend cycle.",
                "highlights": [
                    {"title": "Dual-basket is the family default", "body": "The DZ550's 10-quart twin zones cook two foods two ways at once, which is why it tops lab tests for households."},
                    {"title": "FlexBasket is the rising challenger", "body": "Ninja's newer model runs two 3.5-quart batches or opens to a 7-quart single basket, earning strong 2026 reviews."},
                    {"title": "Cosori TurboBlaze wins on value", "body": "Fast, quiet, and easy to clean, it stays my pick for one or two people who want the lowest cost per meal."},
                    {"title": "Glass baskets are trending up", "body": "Designs like the Ninja Crispi let you watch food cook and double as storage, a real win for small kitchens."},
                ],
            },
            "zh-tw": {
                "commentary": "Ninja Foodi DZ550 這週繼續第一，最新的實驗室評比也都站在它這邊。這台 10 夸脫的雙籃機種，我都直接推給有家庭的人，因為它能同時用兩種方式煮兩種食物，要煮一人份也縮得下去。RTINGS 又一次把它列為測過最好的氣炸鍋，這種穩定度在添購一台要佔流理台空間的家電時很重要。比較新的 Ninja Foodi FlexBasket 這季也很受好評，一樣是雙區概念，外型更俐落，可以分開炸兩份 3.5 夸脫，把隔板抽掉又能變成 7 夸脫的大單籃。我會持續觀察，但 DZ550 我還是放第一，總容量更大加上實績夠硬，以這個價位來說它更值。Cosori TurboBlaze 守住第二，是我心中的 CP 值王，炸得快、好清、又安靜到我常忘記它在運轉。Typhur Dome 2 排第三，適合想要接近烤箱效果、又願意多付錢的人。有個趨勢值得提一下，像 Ninja Crispi 這種玻璃籃設計越來越紅，因為看得到食物在炸，容器還能直接拿來收納跟上桌，對台灣小套房廚房真的很實用。我的建議很單純，全家吃就選 DZ550 雙籃這台主力。一兩個人吃、想花最少又最好清，Cosori TurboBlaze 更聰明。兩台都耐用，撐得過流行週期。",
                "highlights": [
                    {"title": "雙籃是家庭首選", "body": "DZ550 的 10 夸脫雙區能同時用兩種方式煮兩種菜，這也是它在家用實測拿第一的原因。"},
                    {"title": "FlexBasket 是竄起的挑戰者", "body": "Ninja 這台新機可分炸兩份 3.5 夸脫，或開成 7 夸脫單籃，2026 年好評不斷。"},
                    {"title": "Cosori TurboBlaze 主打 CP 值", "body": "炸得快、安靜又好清，是我推給一兩人、想壓低每餐成本的首選。"},
                    {"title": "玻璃籃設計正夯", "body": "像 Ninja Crispi 看得到食物在炸，容器又能收納上桌，對小廚房是實在的加分。"},
                ],
            },
        },
    },
    "best-electric-scooters.json": {
        "references": [
            {"title": "Segway Ninebot Max G3 Electric Scooter Review In 2026", "url": "https://www.voltridehub.com/segway-ninebot-max-g3-review/", "source": "VoltRideHub"},
            {"title": "Ninebot MAX G3 Review (2026): Full Specs, Performance, Range", "url": "https://gokartngear.com/blogs/blog/ninebot-max-g3-review-2026-full-specs-performance-range-upgrade-guide", "source": "GoKartNGear"},
            {"title": "Segway Ninebot Max G3 Review & Score 9.6/10 (2026)", "url": "https://gavler.com/products/segway-ninebot-max-g3", "source": "Gavler"},
        ],
        "i18n": {
            "en": {
                "commentary": "The Segway Ninebot Max G3 keeps the top spot, and the more reviews land, the more obvious the gap becomes. This is a genuine commuter flagship: a 2000W peak motor, a 28 mph top speed, and a 597Wh battery that returns up to 50 miles per charge. It climbs 30 percent grades without drama, which matters if your route has real hills. Dual hydraulic suspension and 11-inch self-sealing tires soak up broken pavement and shrug off punctures, and the fast charger refills it in about 3.5 hours, or 2.5 hours if you run dual input. Reviewers are landing scores as high as 9.6 out of 10, and that tracks with my own read. The trade-off is honest weight and a premium price, so if you live in a fourth-floor walk-up the portability score of 6 is your warning. For riders who want lighter and easier to carry, the Apollo City Pro stays my number two with a smoother ride feel, and the NIU KQi3 Pro holds third as the value sweet spot that most commuters actually need. The Xiaomi 4 Pro remains the budget benchmark. Nothing this week justified a reorder, because the G3 only consolidates its lead as testing piles up. My guidance is unchanged. If your commute is long, hilly, or rough, the Max G3 is the scooter I trust to get you there and back for years. If you carry your scooter up stairs or onto transit often, drop down to the NIU or Apollo and you will be happier every day.",
                "highlights": [
                    {"title": "Range leads the commuter class", "body": "A 597Wh pack returns up to 50 miles per charge, with fast charging in about 3.5 hours or 2.5 with dual input."},
                    {"title": "Built for hills and bad roads", "body": "A 2000W peak motor handles 30 percent grades while dual hydraulic suspension and self-sealing 11-inch tires smooth the ride."},
                    {"title": "Reviewers score it near the top", "body": "Independent reviews are landing as high as 9.6 out of 10, reinforcing the G3's hold on first place."},
                    {"title": "Weight is the honest trade-off", "body": "The portability score of 6 reflects real heft, so stair-carriers should consider the lighter NIU or Apollo."},
                ],
            },
            "zh-tw": {
                "commentary": "Segway Ninebot Max G3 這週繼續坐穩第一，而且評測出得越多，差距就越明顯。這台是貨真價實的通勤旗艦，2000W 峰值馬達、時速約 45 公里，加上 597Wh 電池，單次充電最遠能跑約 80 公里。爬 30% 的坡也不會卡卡，路線有真的山坡的人就知道這點多重要。雙液壓避震加上 11 吋自封式輪胎，把爛路坑洞吃掉、又不太會被刺破，快充大概 3.5 小時充飽，雙孔輸入更快只要 2.5 小時。國外評測甚至給到 9.6 分，跟我自己的感受滿一致的。代價就是它確實重、價格也偏高，所以你住在沒電梯的四樓，攜帶性只有 6 分就是給你的警告。想要輕一點、好搬一點的人，Apollo City Pro 還是我的第二名，騎感更順。NIU KQi3 Pro 守住第三，是多數通勤族真正需要的 CP 值甜蜜點。Xiaomi 4 Pro 繼續當入門標竿。這週沒有任何理由洗牌，因為測試越多，G3 的領先只是越穩。我的建議不變，通勤距離長、有坡、路又爛，Max G3 是我信得過、能載你來回好幾年的車。要常常扛上樓或帶上捷運，就降一級選 NIU 或 Apollo，每天都會更開心。",
                "highlights": [
                    {"title": "續航領先通勤級距", "body": "597Wh 電池單次最遠約 80 公里，快充約 3.5 小時，雙孔輸入只要 2.5 小時。"},
                    {"title": "為山坡與爛路而生", "body": "2000W 峰值馬達能爬 30% 坡，雙液壓避震加自封 11 吋胎，把坑洞都吃掉。"},
                    {"title": "評測給分接近滿分", "body": "國外獨立評測甚至打到 9.6 分，進一步鞏固 G3 的冠軍位置。"},
                    {"title": "重量是誠實的代價", "body": "攜帶性 6 分反映它真的重，常扛樓梯的人可以考慮更輕的 NIU 或 Apollo。"},
                ],
            },
        },
    },
    "best-laptops.json": {
        "references": [
            {"title": "M5 Apple MacBook Air (2026) review: A great laptop, but you have choices", "url": "https://www.expertreviews.co.uk/technology/laptops/m5-apple-macbook-air-review", "source": "Expert Reviews"},
            {"title": "M5 MacBook Air (2026) Review: No Longer The Budget MacBook", "url": "https://www.bgr.com/2131659/macbook-air-m5-review/", "source": "BGR"},
            {"title": "How the 13.6-Inch MacBook Air M5 Delivers Everyday Excellence", "url": "https://www.techeblog.com/13-6-macbook-air-m5-review-specs-deal-2026/", "source": "TechEBlog"},
        ],
        "i18n": {
            "en": {
                "commentary": "The 13-inch MacBook Air M5 keeps my number one spot, and the latest reviews confirm why it has been the default recommendation for years. The M5 chip brings strong all-round performance, more base RAM and storage, and a Liquid Retina display with accurate P3 color. At 2.7 pounds and 0.44 inches thick, it disappears into a bag, and the 18 hours of video playback means you genuinely stop carrying the charger. Reviewers call it the laptop most people should buy, and I agree, especially now that the base configuration is more generous than past Airs. The MacBook Pro 14 with M4 Pro stays second for creators who need sustained performance and a brighter display, and the Asus Zenbook A16 holds third as my Windows value pick with excellent battery and portability. Nothing this week pushed a reorder, because the Air's combination of weight, battery, and price remains the benchmark everyone else is measured against. One nuance from this round of testing: the M5 Air is no longer the cheap MacBook it once was, with UK pricing starting at 1,099 pounds for the 13.6-inch, so budget shoppers should look hard at the Asus Zenbook or the Acer Swift Go 16 lower in the list. My guidance is steady. If you want the best everyday laptop with the least compromise, the M5 Air is the safe answer. If your work is heavy video or 3D, step up to the Pro 14. And if you live in Windows or want to spend less, the Zenbook A16 gives you most of the experience for noticeably less money.",
                "highlights": [
                    {"title": "M5 Air remains the default pick", "body": "Strong all-round M5 performance, more base RAM and storage, and an accurate P3 Liquid Retina display keep it on top."},
                    {"title": "All-day battery, no charger needed", "body": "Up to 18 hours of video playback at 2.7 pounds means you genuinely leave the power brick at home."},
                    {"title": "Pricing has crept up", "body": "The 13.6-inch starts at 1,099 pounds, so the M5 Air is no longer the budget MacBook it once was."},
                    {"title": "Windows value lives lower in the list", "body": "The Asus Zenbook A16 delivers excellent battery and portability for less, my pick for cost-conscious buyers."},
                ],
            },
            "zh-tw": {
                "commentary": "13 吋 MacBook Air M5 這週繼續第一，最新評測也再次說明它為什麼這麼多年都是預設推薦。M5 晶片帶來全面又夠力的效能，基本款的記憶體跟儲存都加大了，Liquid Retina 螢幕的 P3 色域又準。重量只有 1.24 公斤、厚度 1.1 公分，放進包包就像不存在，18 小時的影片續航代表你真的可以不帶充電器出門。國外評測直接說它是多數人該買的筆電，我也同意，尤其現在基本規格比以前的 Air 大方很多。MacBook Pro 14 搭 M4 Pro 守住第二，給需要長時間滿載效能跟更亮螢幕的創作者。Asus Zenbook A16 排第三，是我心中 Windows 陣營的 CP 值首選，續航跟輕便都很強。這週沒有理由洗牌，因為 Air 在重量、續航、價格上的平衡，依舊是大家拿來比較的基準。這輪測試有個細節，M5 Air 已經不是當年那台便宜 MacBook 了，英國售價 13.6 吋從 1,099 英鎊起跳，換算台幣四萬出頭，預算有限的人就該認真看 Zenbook 或排在後面的 Acer Swift Go 16。我的建議很穩，想要最沒妥協的日常筆電，M5 Air 就是穩當解。工作是重度影片或 3D，往上選 Pro 14。習慣 Windows 或想省錢，Zenbook A16 用明顯更低的價格給你大部分體驗。",
                "highlights": [
                    {"title": "M5 Air 還是預設首選", "body": "M5 全面夠力、基本款記憶體與儲存加大、P3 Liquid Retina 螢幕又準，繼續穩坐第一。"},
                    {"title": "整天續航，不用帶充電器", "body": "1.24 公斤的機身有最高 18 小時影片續航，真的可以把變壓器留在家。"},
                    {"title": "價格悄悄往上爬", "body": "13.6 吋從 1,099 英鎊起跳，換算台幣四萬出頭，M5 Air 已經不是當年的平價 MacBook。"},
                    {"title": "Windows CP 值在榜單後段", "body": "Asus Zenbook A16 用更低價格給你優秀續航與輕便，是我推給精打細算族的選擇。"},
                ],
            },
        },
    },
    "best-portable-air-conditioners.json": {
        "references": [
            {"title": "Midea Duo Review | Test Results", "url": "https://www.consumeranalysis.com/guides/portable-ac/midea-duo-review/", "source": "Consumer Analysis"},
            {"title": "Midea Duo Portable Air Conditioner Review - Tested by Bob Vila", "url": "https://www.bobvila.com/reviews/midea-duo-portable-ac-review/", "source": "Bob Vila"},
            {"title": "Midea Duo MAP12S1TBL Air Conditioner Review", "url": "https://www.rtings.com/air-conditioner/reviews/midea/duo-map12s1tbl", "source": "RTINGS"},
        ],
        "i18n": {
            "en": {
                "commentary": "With summer heat arriving, the Midea Duo keeps my number one spot, and the test data makes the case better than I can. It delivers a higher seasonally adjusted cooling capacity than any other portable AC, and it pushes 389 CFM of airflow when most rivals sit in the 200 to 300 range. That extra airflow is why it actually cools a large room instead of just the corner near the unit. In testing it took a 500-square-foot room from 78 down to 72 degrees in under 15 minutes, which is the kind of result that ends the argument. It is also the most energy efficient portable on the market thanks to its inverter design, and the Wi-Fi app setup is quick with full scheduling and temperature control. The honest caveat is weight, at 74 pounds it is a two-person move, so plan to set it up at the start of summer and leave it. The Whynter NEX ARC stays second as a strong value alternative, and the LG model holds third for its quiet operation. Nothing this week warranted a reorder, because the Duo's cooling and efficiency lead is wide and well documented. My buying advice is direct. If you want the best cooling and the lowest running cost for a big room, the Midea Duo is worth the premium and the heft. If your space is smaller or your budget tighter, the Whynter gives you most of the performance for less, and the LG is the one to pick if a quiet bedroom is your priority.",
                "highlights": [
                    {"title": "Airflow that reaches the whole room", "body": "389 CFM beats the typical 200 to 300 of rivals, so the Duo cools a large space evenly rather than just nearby."},
                    {"title": "Fast, measured cooling", "body": "Testing dropped a 500-square-foot room from 78 to 72 degrees in under 15 minutes."},
                    {"title": "Most efficient portable on the market", "body": "Its inverter design gives the lowest running cost in the category, which adds up across a long summer."},
                    {"title": "Weight is the one caveat", "body": "At 74 pounds it is a two-person setup, so install it at the start of the season and leave it in place."},
                ],
            },
            "zh-tw": {
                "commentary": "夏天熱浪報到，Midea Duo 這週繼續第一，而且測試數據比我嘴砲還有說服力。它的季節調整製冷量比任何一台移動式冷氣都高，風量更推到 389 CFM，多數對手只落在 200 到 300 之間。多出來的風量，正是它能把整間房間吹涼、而不是只涼機器旁邊那一角的關鍵。實測把一間約 14 坪的房間，從攝氏 26 度在 15 分鐘內降到 22 度，這種結果基本上沒什麼好吵的。靠著變頻設計,它也是市面上最省電的移動式冷氣,Wi-Fi App 設定很快,排程跟溫控都完整。誠實要講的缺點是重,33 公斤要兩個人搬,所以建議夏天一開始就定位好,之後就別動它了。Whynter NEX ARC 守住第二,是 CP 值很強的替代選擇。LG 那台排第三,主打安靜。這週沒有洗牌的理由,因為 Duo 在製冷跟效率上的領先又大又有憑有據。我的建議很直接,大房間想要最強製冷又最省電,Midea Duo 值得這個價差跟這個重量。空間比較小、預算比較緊,Whynter 用更低價格給你大部分性能。臥室最在意安靜,就選 LG。",
                "highlights": [
                    {"title": "風量吹得到整間房", "body": "389 CFM 勝過對手常見的 200 到 300，Duo 能均勻吹涼大空間，不是只涼機器旁邊。"},
                    {"title": "降溫又快又有數據", "body": "實測把約 14 坪的房間在 15 分鐘內從 26 度降到 22 度。"},
                    {"title": "市面最省電的移動式", "body": "變頻設計帶來這個級距最低的運轉成本，整個夏天累積下來很有感。"},
                    {"title": "重量是唯一要注意的", "body": "33 公斤要兩個人搬，建議夏天一開始就定位好，之後就別搬了。"},
                ],
            },
        },
    },
    "best-robotic-pool-cleaners.json": {
        "references": [
            {"title": "Best Robotic Pool Cleaners of 2026. Over 30+ Tested & Reviewed", "url": "https://www.thepoolnerd.com/best-robotic-pool-cleaners", "source": "The Pool Nerd"},
            {"title": "Beatbot Robotic Pool Cleaner Reviews | Every Model Tested (2026)", "url": "https://www.thepoolnerd.com/beatbot-pool-cleaner-reviews", "source": "The Pool Nerd"},
            {"title": "16 Best Robotic Pool Cleaners of 2026 - Reviewed", "url": "https://www.reviewed.com/home-outdoors/best-right-now/best-robotic-pool-cleaners", "source": "Reviewed"},
        ],
        "i18n": {
            "en": {
                "commentary": "The Dolphin Premier holds my number one spot, and this week's head-to-head testing only strengthens the case. Its commercial-grade motors, Multi-Media filtration, and proven long-term reliability are exactly what you want in a machine you will run weekly for years. The big debate this season is corded versus cordless, and the data is clear. The Beatbot AquaSense 2 Ultra is the most capable battery robot, with AI mapping, surface skimming, and the longest runtime in its lineup, but at around 3,000 dollars it could not keep up with corded Dolphins at a fraction of the price in side-by-side tests. The cordless trade-offs are real: shorter run times, weaker suction, and constant recharging instead of a simple weekly timer. On fine debris, Dolphin's NanoFiltration captured noticeably finer particles than anything Beatbot offered. I keep the AquaSense 2 Ultra at number two because its convenience and navigation are genuinely class-leading, and for owners who hate cords it is the best of that breed. But for pure cleaning and value, corded still wins, which is why the Dolphin Nautilus CC Plus stays third as the smart-money pick. My guidance is steady. If you want the best clean and the longest service life, buy the Dolphin Premier and run it on a timer. If a cord around your pool genuinely bothers you and budget is no object, the Beatbot Ultra is the cordless to get. For most pool owners, though, the Nautilus CC Plus delivers the Dolphin cleaning experience at a price that makes sense.",
                "highlights": [
                    {"title": "Corded still wins on cleaning", "body": "In side-by-side tests, corded Dolphins out-cleaned the 3,000 dollar Beatbot Ultra at a fraction of the price."},
                    {"title": "NanoFiltration captures finer debris", "body": "Dolphin's filtration grabbed noticeably finer particles than any Beatbot system in this round of testing."},
                    {"title": "Cordless convenience leads, with trade-offs", "body": "The AquaSense 2 Ultra brings AI mapping and skimming but accepts shorter runtime, weaker suction, and frequent recharging."},
                    {"title": "Nautilus CC Plus is the smart money", "body": "It delivers the core Dolphin clean at a far friendlier price, my pick for most pool owners."},
                ],
            },
            "zh-tw": {
                "commentary": "Dolphin Premier 這週守住第一，最新的對打實測只是讓它更穩。商用等級馬達、Multi-Media 多重濾網,加上多年驗證的可靠度,正是你要一台每週跑、用好幾年的機器該有的條件。這季最大的爭論是有線對無線,數據講得很清楚。Beatbot AquaSense 2 Ultra 是目前最強的電池機種,有 AI 建圖、水面清潔,續航也是自家最長,可是要價約台幣九萬,在並排測試裡卻打不過價格只有它一小部分的有線 Dolphin。無線的代價是真的,續航較短、吸力較弱,還要不停回充,沒辦法像有線那樣設個每週定時就好。碰到細小髒污,Dolphin 的 NanoFiltration 抓到的顆粒明顯比 Beatbot 任何一款都細。我還是把 AquaSense 2 Ultra 放第二,因為它的便利性跟導航確實是同級最強,討厭拖線的人,它就是無線陣營的最佳解。但講純清潔跟 CP 值,有線還是贏,所以 Dolphin Nautilus CC Plus 守住第三,是精打細算族的聰明選擇。我的建議很穩。想要最乾淨、用最久,就買 Dolphin Premier,設定時器讓它自己跑。真的很受不了泳池邊那條線、又不在乎預算,Beatbot Ultra 就是該入手的無線機。但對多數泳池主人來說,Nautilus CC Plus 用合理價格給你 Dolphin 的清潔體驗。",
                "highlights": [
                    {"title": "純清潔有線還是贏", "body": "並排實測裡，有線 Dolphin 用一小部分的價格，清潔表現勝過台幣九萬的 Beatbot Ultra。"},
                    {"title": "NanoFiltration 抓得更細", "body": "這輪測試中，Dolphin 濾網抓到的顆粒明顯比任何 Beatbot 系統都細。"},
                    {"title": "無線便利領先但有取捨", "body": "AquaSense 2 Ultra 有 AI 建圖跟水面清潔，代價是續航較短、吸力較弱、要常回充。"},
                    {"title": "Nautilus CC Plus 是聰明選擇", "body": "用更親民的價格給你 Dolphin 的核心清潔力，是我推給多數泳池主人的款。"},
                ],
            },
        },
    },
    "best-standing-desks.json": {
        "references": [
            {"title": "Best standing desks of 2026: my top-performing height-adjustable desks", "url": "https://www.techradar.com/news/best-standing-desk", "source": "TechRadar"},
            {"title": "Uplift vs Jarvis Standing Desk: Which Should You Buy in 2026?", "url": "https://wetried.it/uplift-vs-jarvis-standing-desk/", "source": "We Tried It"},
            {"title": "Jarvis vs Uplift Desks: 1-Year Stability Test Results", "url": "https://ordinaryintrovert.com/adjustable-desks-jarvis-vs-uplift-after-1-year/", "source": "Ordinary Introvert"},
        ],
        "i18n": {
            "en": {
                "commentary": "The Uplift V2 Commercial keeps my number one spot, and the latest comparisons reinforce why. The V2 frame supports up to 355 pounds, one of the strongest in its class, and the four-leg design holds steady where many desks start to sway near full extension. It lifts from about 25 to 51 inches in roughly 12 seconds at under 45 dB, so it raises quietly while you are on a call. Reviewers continue to call out the Uplift four-leg frame as more stable than the rivals, and after long-term testing the stability gap holds up over a year of daily use. The newer comparisons pit it against the Fully Jarvis, now under Herman Miller, which earns praise for quiet dual motors and a generous 15-year warranty but shows a slight wobble at maximum height. That wobble is the deciding factor for me, which is why the Jarvis Bamboo stays at sixth while the Uplift leads. The FlexiSpot E7 Pro holds second as the value champion, giving you most of the experience for a few hundred dollars less, and the Secretlab Magnus Pro keeps third for buyers who want the cleanest cable management and a premium feel. Nothing this week justified a reorder. My guidance stays simple. If you want maximum stability and the widest height range for a serious daily setup, the Uplift V2 Commercial earns the premium. If budget leads your decision, the FlexiSpot E7 Pro is the smartest spend in the category, and it has closed much of the gap that used to separate it from the top.",
                "highlights": [
                    {"title": "Four-leg frame leads on stability", "body": "The Uplift V2 supports up to 355 pounds and holds steady near full extension where many desks sway."},
                    {"title": "Quiet, quick height changes", "body": "It travels roughly 25 to 51 inches in about 12 seconds at under 45 dB, so it raises during calls without disruption."},
                    {"title": "Jarvis wobble is the deciding factor", "body": "The Herman Miller Jarvis offers quiet motors and a 15-year warranty but shows slight wobble at max height."},
                    {"title": "FlexiSpot E7 Pro wins on value", "body": "It delivers most of the top experience for a few hundred dollars less, the smartest spend in the category."},
                ],
            },
            "zh-tw": {
                "commentary": "Uplift V2 Commercial 這週繼續第一,最新的比較也再次說明原因。V2 桌架承重高達約 161 公斤,是同級最強之一,四腳設計在升到接近最高點時依然穩,很多桌子到那高度就開始晃。它能在大約 12 秒內從 64 公分升到 130 公分,噪音低於 45 分貝,開會中升降也很安靜。評測一直點名 Uplift 的四腳桌架比對手更穩,而且經過一年的長期實測,這個穩定度差距撐得住每天使用。比較新的評比把它跟 Fully Jarvis 對打,Jarvis 現在歸在 Herman Miller 旗下,雙馬達安靜、15 年保固很大方,但升到最高時會有點晃。那個晃對我來說就是決勝點,所以 Jarvis Bamboo 排第六,Uplift 領先。FlexiSpot E7 Pro 守住第二,是 CP 值王,用少幾千塊台幣給你大部分體驗。Secretlab Magnus Pro 排第三,給想要最乾淨理線跟質感的人。這週沒有洗牌的理由。我的建議很單純。想要最高穩定度跟最寬升降範圍、認真用的每日工作站,Uplift V2 Commercial 值這個價。預算優先,FlexiSpot E7 Pro 是這個級距最聰明的花法,而且它已經把跟頂規之間的差距追得差不多了。",
                "highlights": [
                    {"title": "四腳桌架穩定度領先", "body": "Uplift V2 承重達約 161 公斤，升到接近最高點仍然穩，很多桌子那時已經開始晃。"},
                    {"title": "升降又快又安靜", "body": "約 12 秒從 64 升到 130 公分，噪音低於 45 分貝，開會中升降也不擾人。"},
                    {"title": "Jarvis 的晃動是決勝點", "body": "Herman Miller 版 Jarvis 馬達安靜、15 年保固，但升到最高時會有點晃。"},
                    {"title": "FlexiSpot E7 Pro 主打 CP 值", "body": "用少幾千塊台幣給你大部分頂規體驗，是這個級距最聰明的花法。"},
                ],
            },
        },
    },
}


def main():
    for name, payload in ENTRIES.items():
        data, p = load(name)
        entry = {
            "date": DATE,
            "rankings": last_rankings(data),
            "references": payload["references"],
            "i18n": payload["i18n"],
        }
        upsert(data, entry)
        save(p, data)
        print("updated", name)


if __name__ == "__main__":
    main()
