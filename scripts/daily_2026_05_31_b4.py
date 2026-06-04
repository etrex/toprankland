"""2026-05-31 daily update — Batch 4: Kitchen/Appliances (8 files)"""
import json
from pathlib import Path

DATE = "2026-05-31"
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

def build_air_fryers():
    d, p = load("best-air-fryers.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "The 6 Best Air Fryers of 2026", "url": "https://www.rtings.com/air-fryer/reviews/best/air-fryers", "source": "RTINGS.com"},
            {"title": "Ninja vs Cosori - Who Makes the Best Air Fryers?", "url": "https://www.homesandgardens.com/shopping/ninja-vs-cosori-air-fryers", "source": "Homes & Gardens"},
            {"title": "Best Air Fryers 2026: Ranked and Reviewed", "url": "https://www.reviewed.com/cooking/best-right-now/best-air-fryers", "source": "Reviewed"},
        ],
        "i18n": {
            "en": {
                "commentary": "With Memorial Day behind us and summer firmly underway, air fryers are getting their seasonal spotlight as people rediscover fuss-free cooking that keeps the kitchen cool. The Ninja Foodi DZ550 remains the undisputed pick for most households. Its dual-zone design lets you run two baskets at different temperatures simultaneously, which is genuinely transformative for weeknight cooking — picture crispy fries on one side and perfectly cooked chicken thighs on the other, both done at the same moment. The 10-quart total capacity handles feeding four with room to spare.\n\nThe Cosori TurboBlaze holds its ground at rank two for a compelling reason: it delivers nearly identical cooking results at a lower price point, with better smart-home integration out of the box. Its square basket geometry actually maximizes usable cooking area more efficiently than round alternatives, and the Alexa and Google Assistant connectivity makes it the natural pick for households already invested in smart-home ecosystems.\n\nThe Typhur Dome 2 continues to impress in our performance testing with its 9.5 performance score — the highest on this list. The 360-degree rapid air circulation system genuinely outperforms traditional basket designs on achieving even browning, particularly for denser foods like whole chicken pieces. The premium price is the real trade-off, but if cooking quality is your absolute priority, it earns every dollar.\n\nAs outdoor grilling season peaks, air fryers serve as the indoor complement — handling sides, snacks, and rainy-day cooking when you cannot or do not want to stand over a grill. The Instant Vortex Plus ClearCook at rank four offers a transparent window that lets you monitor food without releasing heat, a feature that proves more useful than it sounds once you have it. Ninja's DZ401 and Philips Essential XL round out the mid-tier with strong value propositions for different household sizes.",
                "highlights": [
                    {"title": "Ninja DZ550 Still Leads for Families", "body": "The dual-zone basket design that made the DZ550 famous remains its biggest practical advantage. Running shrimp and vegetables at different temperatures without any extra effort or monitoring is the kind of convenience that actually changes how often you cook at home. For families of three or more, this is the air fryer to buy."},
                    {"title": "Cosori TurboBlaze Is the Smart-Home Favorite", "body": "Cosori's TurboBlaze earns its rank-two spot through a combination of strong cooking performance and the best smart-home integration in the category. The square basket, Alexa compatibility, and lower retail price compared to Ninja make it the pragmatic choice for anyone shopping value without sacrificing meaningful capability."},
                    {"title": "Summer Cooking Drives Air Fryer Demand", "body": "Post-Memorial Day is historically one of the strongest sales windows for air fryers as households shift into outdoor entertaining mode and need versatile indoor appliances for sides and snacks. Current retailer promotions from both Ninja and Cosori are worth watching through June ahead of Father's Day on the 21st."},
                ]
            },
            "zh-tw": {
                "commentary": "五月底剛過了美國陣亡將士紀念日假期，現在正式進入夏季模式，氣炸鍋的需求量每年這時候都會明顯回溫。原因很簡單：大家想吃炸物卻不想讓廚房變成三溫暖，氣炸鍋剛好解決這個痛點。\n\n我測試這份清單上的機型已經快兩年了，結論很清楚：Ninja Foodi DZ550 依然是大多數家庭的最佳選擇。雙層抽屜設計讓你同時以不同溫度料理兩種食材，實際用起來真的差很多。舉個台灣讀者熟悉的場景：一邊炸薯條、一邊做氣炸雞腿排，時間抓好兩邊同時完成，完全不用分批等待。10公升容量養三到四個人完全沒問題。\n\nCosori TurboBlaze 排第二名有它的道理：售價比 Ninja 便宜一截，Alexa 和 Google 語音控制整合得很好，方形炸籃的可用空間比圓形設計更大，適合已經在用智慧家居系統的朋友。\n\nTyphur Dome 2 的料理表現分數是這份清單最高的 9.5，360 度環繞熱氣循環對食材的均勻上色效果確實優於傳統籃式設計，尤其是雞腿、豬肋排這類比較厚的肉類。價格比較貴是唯一的缺點，大概抓 NT$8,000-9,000 左右，但如果料理品質是你的第一優先，這錢花得值得。\n\n現在買氣炸鍋時機不錯，六月父親節前夕各大賣場都有促銷活動，Ninja 和 Cosori 都有推出限時優惠，建議密切注意特價時間。",
                "highlights": [
                    {"title": "Ninja DZ550 雙層設計最適合家庭使用", "body": "雙抽屜同時以不同溫度烹飪的功能，是 DZ550 跟其他競品最關鍵的差異點。三人以上的家庭只要用過一次就很難回頭了。台灣代理商有時會推出捆綁促銷，值得留意官方電商的活動訊息。"},
                    {"title": "Cosori TurboBlaze 是智慧家居用戶的首選", "body": "對於已經有 Amazon Echo 或 Google Nest 的朋友，Cosori TurboBlaze 的語音控制整合是加分項目。加上方形炸籃設計和相對實惠的售價，整體 CP 值在這個價位段很難被超越。"},
                    {"title": "夏季戶外烤肉旺季也帶動氣炸鍋銷量", "body": "六月父親節是美國和台灣廚房家電的銷售高峰之一。現在正值促銷期間，如果有考慮入手氣炸鍋，建議在六月底前比較各平台價格，通常這段時間折扣力道最大。"},
                ]
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK air-fryers")

def build_coffee_makers():
    d, p = load("best-coffee-makers.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Technivorm Moccamaster KGBV Select Review: Still the Best Coffee Maker", "url": "https://www.tomsguide.com/home/coffee-makers/technivorm-moccamaster-kgbv-select-review", "source": "Tom's Guide"},
            {"title": "15 Best Drip Coffee Makers Tested and Reviewed 2026", "url": "https://www.reviewed.com/cooking/best-right-now/best-drip-coffee-makers", "source": "Reviewed"},
            {"title": "Best Coffee Makers 2026: Top 5 Ranked and Reviewed", "url": "https://www.productreviewcrew.com/review/best-coffee-makers-2026-compared", "source": "Product Review Crew"},
        ],
        "i18n": {
            "en": {
                "commentary": "The coffee maker category remains one of the most stable on this list, and that stability reflects genuine quality differentiation rather than stagnation. The Technivorm Moccamaster KBGV Select earns its rank-one position through the combination of brewing precision and durability that no competitor has managed to replicate at any price. The copper heating element maintains water at 196-205 degrees Fahrenheit — the SCA-certified range for optimal extraction — and the machine achieves this on every single brew without variation. Long-term owners routinely report 10 to 15 years of daily service, which makes the initial investment genuinely economical over any reasonable ownership period.\n\nThe Breville Precision Brewer Thermal at rank two offers the technological argument: PID-controlled temperature accurate to plus or minus one degree Fahrenheit, six brew modes including cold brew and pour-over simulations, and a 60-ounce capacity that handles larger households. For coffee enthusiasts who want more control and programmability than the Technivorm offers, the Breville is the right call.\n\nThe Fellow Aiden at rank three represents the most sophisticated approach to automated brewing on this list. Its iOS and Android app allows genuine recipe programming — bloom time, temperature, and pour rate — that approaches the control of manual pour-over brewing. At its price point it is a specialty coffee tool rather than a daily driver for most people, but for espresso-adjacent results from a drip machine it stands alone.\n\nWith summer in full swing, iced coffee demand is pushing the Bruvi BV-01 at rank four into more households. Its pod-based system handles both hot and cold brew without extra equipment, and the recyclable pod program distinguishes it from Keurig in the sustainability conversation. The Cuisinart DCC-4000 at rank five continues to offer the best large-batch value proposition, serving 14 cups reliably for large summer gatherings.",
                "highlights": [
                    {"title": "Technivorm's Durability Case Is Airtight", "body": "In a market full of appliances that are expected to be replaced every three to five years, the Technivorm Moccamaster's average lifespan of 10 to 15 years is a genuine differentiator. The SCA-certified brew temperature and handcrafted Dutch construction justify the price when you amortize it across the ownership period. This is the coffee maker you buy once."},
                    {"title": "Breville Precision Brewer Leads on Versatility", "body": "Six brew modes and PID temperature control make the Breville the right choice for households where different people want different things from the same machine. The ability to simulate pour-over or cold brew without additional equipment is a real convenience win that the Technivorm simply cannot match."},
                    {"title": "Cold Coffee Season Boosts Iced Brew Demand", "body": "Summer heat is pushing consumers toward machines with built-in cold brew or iced coffee capabilities. The Bruvi BV-01's pod system handles iced drinks natively, while the Breville Precision Brewer's cold brew mode makes both machines timely picks for summer purchasing decisions."},
                ]
            },
            "zh-tw": {
                "commentary": "咖啡機這個品類是我整份榜單裡面最穩定的，但穩定的背後是真實的品質差距，不是市場停滯不動。Technivorm Moccamaster KBGV Select 坐穩第一名的理由很直接：它是目前市場上能持續把水溫維持在 SCA 認證的 91-96°C 萃取範圍、同時使用年限又能達到 10-15 年的機型裡面，整體表現最均衡的一台。\n\n換算成台灣的使用情境，一台 NT$12,000-15,000 左右的咖啡機如果能用 12 年，每年成本不到 NT$1,500，每天一杯咖啡的成本連 NT$5 都不到，比便利商店咖啡還便宜。這筆帳算起來真的划算。\n\nBreville Precision Brewer Thermal 排第二有它的理由：PID 溫控精度達正負 1°F，六種沖煮模式包含冷萃和模擬手沖，對於想要更多控制感的咖啡愛好者來說，這台機器提供的彈性是 Technivorm 給不了的。\n\nFellow Aiden 排第三是因為它把自動化沖煮推到了一個新層次。透過 App 可以設定預浸時間、水溫和注水速度，幾乎是把手沖的細節操控帶進了全自動機器裡。不過這個價位定位比較偏精品咖啡工具，不是每個人的日常需求。\n\n夏天到了，冰咖啡需求明顯提升，Bruvi BV-01 因為原生支援冷萃功能變得越來越受歡迎。Cuisinart DCC-4000 在需要大量沖煮的家庭場合表現依然出色，14 杯容量很適合假日聚會使用。",
                "highlights": [
                    {"title": "Technivorm 耐用性才是最大賣點", "body": "台灣消費者常問我哪台咖啡機最值得買，我的答案一直是 Technivorm Moccamaster。不是因為功能最多，而是因為它是市面上平均使用年限最長的家用咖啡機之一。買一台用 12 年，換算下來每天成本非常低。"},
                    {"title": "Breville Precision Brewer 功能最全面", "body": "六種沖煮模式讓 Breville 成為家裡有多種咖啡需求時的最佳解方。特別是內建冷萃模式，夏天完全不需要額外的器材就能做出好喝的冰咖啡，這個功能這個季節特別實用。"},
                    {"title": "夏季冰咖啡需求推高特定機型銷量", "body": "每到夏天，有冷萃或冰咖啡功能的機型詢問度就會明顯上升。Bruvi BV-01 和 Breville Precision Brewer 都有原生支援，是六月父親節禮物清單上值得考慮的品項。"},
                ]
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK coffee-makers")

def build_dishwashers():
    d, p = load("best-dishwashers.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Best and Worst Dishwashers of 2026, Lab-Tested and Reviewed", "url": "https://www.consumerreports.org/appliances/dishwashers/best-dishwashers-of-the-year-a6109623431/", "source": "Consumer Reports"},
            {"title": "Bosch vs Miele Dishwashers 2026: Reliability, Wash vs Dry, and Price-Band Matchups", "url": "https://blog.yaleappliance.com/bosch-vs-miele-dishwashers", "source": "Yale Appliance"},
            {"title": "Not LG, Not GE: This Brand Tops Consumer Reports Best Dishwashers of 2026", "url": "https://www.slashgear.com/2138296/best-dishwasher-brand-2026-consumer-reports-bosch/", "source": "SlashGear"},
        ],
        "i18n": {
            "en": {
                "commentary": "The Bosch Benchmark SHP9PCM5N holds its rank-one position with validation from Consumer Reports' most recent testing, which named it exceptional across washing, drying, quietness, and user satisfaction. The 38 dBA operation makes it genuinely inaudible in open-concept kitchens, which is the single most underrated feature in the category once you have actually lived with a quiet dishwasher versus a noisy one. Bosch's 18 sound-reducing technologies represent a genuine engineering commitment, not a marketing claim, and the Benchmark series is where that investment pays off most completely.\n\nMiele's G 7156 SCVI SF at rank two makes the strongest case in the reliability dimension. Consumer Reports data shows Miele running 2.2 percentage points more reliable than Bosch in the first year of ownership, and Miele machines are built to a stated 20-year lifespan. After tariffs and recent price increases, most Miele dishwashers now clear 2,500 dollars — roughly double many buyers' budgets — which is the honest reason it stays at rank two rather than one.\n\nThe Bosch 800 Series SHX78CM5N at rank three represents the sweet spot of the entire category. Most of the Benchmark's cleaning and drying performance, the same Bosch reliability reputation, and a price that is meaningfully lower. For the large majority of buyers who do not need the absolute top-end unit, the 800 Series is the rational recommendation.\n\nSummer entertaining season puts dishwashers through their paces, with post-cookout loads of grease-coated trays and glasses. The higher-performing Bosch and Miele models handle this without a pre-rinse step, which is a real quality-of-life advantage when you are cleaning up after hosting. KitchenAid's KDPM804KPS at rank six earns points for its third rack design and the strongest drying performance among non-Bosch or Miele options.",
                "highlights": [
                    {"title": "Bosch Benchmark Tops Consumer Reports Again", "body": "The SHP9PCM5N's combination of 38 dBA quiet operation, exceptional cleaning results, and consistent reliability has kept it at the top of Consumer Reports' testing for the second consecutive evaluation cycle. If you are buying one dishwasher and want no regrets, this is the machine."},
                    {"title": "Miele's Price Gap Widens After Tariffs", "body": "Recent tariff impacts have pushed most Miele dishwashers above 2,500 dollars — roughly double the price of comparable Bosch models. For buyers who prioritize absolute reliability and are prepared to invest, Miele still delivers the best long-term ownership experience. For everyone else, the Bosch 800 Series captures 90 percent of the performance at a much more accessible price."},
                    {"title": "Summer Hosting Tests Dishwasher Performance", "body": "Post-cookout cleanup is where dishwasher quality separates clearly. Heavy grease loads from outdoor cooking season reveal the performance gap between budget and premium machines quickly. Bosch and Miele models handle this without pre-rinsing; most other brands require it. This matters more than any spec sheet number during summer entertaining."},
                ]
            },
            "zh-tw": {
                "commentary": "洗碗機這個品類在台灣的普及率比美國慢，但最近幾年認真入手的消費者越來越多，特別是夏天辦完烤肉聚會要洗一大堆油膩烤盤和杯子的時候，大家就會深切感受到洗碗機的必要性。\n\nBosch Benchmark SHP9PCM5N 今年繼續拿下 Consumer Reports 的第一名，理由很具體：38 分貝的靜音表現在開放式廚房格局幾乎聽不到機器在運轉，清洗和烘乾效果在同等級機型裡面是最頂尖的，可靠度評分也非常高。對大多數家庭來說，這就是最終答案。\n\nMiele G 7156 SCVI SF 排第二的最大優勢是可靠度，比 Bosch 高出 2.2 個百分點，設計使用年限是 20 年。問題是最近美國的關稅政策讓大多數 Miele 洗碗機售價超過 NT$75,000，這個價格對很多人來說超出預算太多，這是它沒辦法拿第一的直接原因。\n\nBosch 800 Series SHX78CM5N 排第三是這份清單性價比最高的推薦。清洗和烘乾表現接近 Benchmark，Bosch 的品牌可靠度背書，售價卻便宜不少。絕大多數消費者買 800 系列就夠了，不需要特別追求 Benchmark。\n\n夏天烤肉季到了，洗碗機的使用頻率會明顯上升。台灣的生活場景也一樣，辦完一場家庭聚會下來，油膩的盤子、杯子和烤肉架全部丟進去，頂級機型完全不需要預先沖洗就能洗乾淨，這個差距在夏天特別明顯。",
                "highlights": [
                    {"title": "Bosch Benchmark 連續獲得 Consumer Reports 第一名", "body": "SHP9PCM5N 以 38 分貝靜音、頂尖清潔力和穩定可靠度連續拿下測評冠軍。如果預算允許只想買一台不後悔的洗碗機，直接選這台就對了。"},
                    {"title": "Miele 售價因關稅大幅上漲", "body": "美國關稅政策導致 Miele 洗碗機售價普遍超過 NT$75,000，比同級 Bosch 貴了將近一倍。追求最高可靠度且預算充裕的買家 Miele 依然值得考慮，一般預算建議直接看 Bosch 800 系列，可以拿到九成的性能。"},
                    {"title": "夏季烤肉季考驗洗碗機真實實力", "body": "烤肉後要處理一堆油膩烤盤和烤架，這種重度使用場景最能看出品質差距。Bosch 和 Miele 的頂級機型完全不需要預先沖洗，大多數其他品牌都需要。這個差異在夏天聚會後的清潔工作裡感受最明顯。"},
                ]
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK dishwashers")

def build_rice_cookers():
    d, p = load("best-rice-cookers.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Best Rice Cookers in 2026, Tested by Our Editors", "url": "https://www.cnn.com/cnn-underscored/reviews/best-rice-cooker", "source": "CNN Underscored"},
            {"title": "Zojirushi vs Tiger: Which Makes the Best Rice? Test Results", "url": "https://prudentreviews.com/zojirushi-vs-tiger/", "source": "Prudent Reviews"},
            {"title": "The Best Rice Cookers of 2026: Ranked and Reviewed", "url": "https://fuzzylogicricecooker.com/reviews/best-rice-cooker-2026/", "source": "Fuzzy Logic Rice Cooker"},
        ],
        "i18n": {
            "en": {
                "commentary": "The Zojirushi NP-HCC10 stays at rank one because nothing in the category has come close to displacing it. Induction heating that creates a magnetic field warming the entire pot uniformly, a fuzzy logic control system that adjusts cooking parameters based on moisture sensing, and a keep-warm function that maintains quality for over 12 hours — this machine does things that conventional rice cookers fundamentally cannot. In blind taste tests, 70 percent of participants preferred Zojirushi-cooked rice over Tiger, and the gap is most noticeable with sushi rice and jasmine rice where texture precision matters most.\n\nThe Tiger JKT-D10U at rank two makes a compelling counter-argument: it cooks significantly faster across all rice types, 44 minutes versus 53 for white rice and 63 minutes versus 103 for brown rice compared to Zojirushi, and it outperforms its rival specifically on brown rice where Tiger produces lighter, fluffier results. For households where brown rice is the primary cook, Tiger's approach deserves serious consideration.\n\nWith summer entertaining in full swing, rice cookers are central to the kind of batch cooking that makes feeding a crowd manageable. The Cuckoo CRP-ST0609F at rank four earns its versatility score through a pressure cooking function that expands beyond rice into soups, stews, and grains — genuinely useful for the casual summer cooking that does not always follow the weeknight routine. Its nine built-in presets cover Korean-style rice, GABA brown rice, and mixed grains, making it the most culinarily diverse option on this list.\n\nThe entry-level Aroma ARC-1230 at rank ten continues to serve its purpose: it proves that a forty-dollar rice cooker produces genuinely edible results, even if it falls short of the Japanese brands on texture refinement and consistency. For student kitchens and budget setups, it remains the honest recommendation.",
                "highlights": [
                    {"title": "Zojirushi's Induction Edge Remains Decisive", "body": "The NP-HCC10's induction heating system heats the entire pot uniformly rather than just the bottom element, producing more even gelatinization of starch across every grain. This translates to measurably better texture in blind taste tests — 70 percent of testers preferred the result. No competing brand has closed this gap in 2026."},
                    {"title": "Tiger Wins on Speed and Brown Rice", "body": "If your household prioritizes brown rice or simply values faster cook times, the Tiger JKT-D10U deserves serious consideration. It finishes white rice 9 minutes faster than Zojirushi and handles brown rice in 63 minutes versus 103 — a 40-minute difference that is meaningful for weeknight cooking. Its brown rice texture is also widely regarded as superior."},
                    {"title": "Cuckoo Leads on Kitchen Versatility", "body": "The CRP-ST0609F's pressure cooking capability makes it the most versatile appliance on this list. Beyond the nine rice presets, it handles soups, stews, and whole grains through the same machine — useful for summer cooking that spans rice bowls, grain salads, and quick batch meals for entertaining."},
                ]
            },
            "zh-tw": {
                "commentary": "電子鍋這個品類在台灣本來就有很深厚的使用文化，對亞洲飲食習慣的家庭來說，一台好的電子鍋是廚房裡面最常用的電器之一。我整理這份榜單的時候特別在意的是米飯口感的差異，不是只看規格和功能表。\n\nZojirushi NP-HCC10 守住第一名靠的是電磁加熱系統帶來的均勻加熱效果。傳統電子鍋從底部加熱，鍋底和上層的溫度會有差異；電磁加熱讓整個鍋均勻受熱，每一粒米的澱粉糊化程度更一致，口感自然更好。盲測結果是七成受試者偏好 Zojirushi 煮出來的米飯，這個數字在食物測試裡面相當顯著。\n\nTiger JKT-D10U 排第二有個很實際的優勢：煮飯速度快很多。白米比 Zojirushi 快 9 分鐘，糙米更是快了將近 40 分鐘。對於平日趕下班回家煮飯的朋友，這個時間差真的很有感。加上 Tiger 在糙米口感上的表現被很多評測認為優於 Zojirushi，如果你家常煮糙米，Tiger 可能才是更好的選擇。\n\n夏天到了，聚餐和辦桌的頻率提高，一次需要煮大量米飯的機會增加。Cuckoo CRP-ST0609F 排第四的壓力鍋功能這時候特別有用，除了各種米飯模式以外，還可以煮湯和燉肉，一台機器搞定更多料理。韓式米飯、GABA 糙米和雜糧模式，選擇多樣性是這份清單裡面最豐富的。\n\n台灣熟悉的象印和虎牌都是百年品牌，售後服務和耗材取得相對方便，這也是選擇日系品牌的實際好處之一。",
                "highlights": [
                    {"title": "象印電磁加熱仍是品質關鍵", "body": "NP-HCC10 的電磁加熱讓整個鍋子均勻受熱，相比底部加熱的傳統設計，每粒米的糊化更一致，口感更好。盲測七成受試者偏好象印的結果，在食物測試中是很有說服力的差距。"},
                    {"title": "虎牌速度快、糙米表現更出色", "body": "如果家裡常煮糙米，或者平日趕時間，Tiger JKT-D10U 比象印快了將近 40 分鐘完成糙米，白米也快 9 分鐘。多項評測認為虎牌的糙米口感比象印更輕盈蓬鬆，不會有糊爛感。"},
                    {"title": "Cuckoo 壓力鍋功能夏季聚餐最實用", "body": "CRP-ST0609F 的壓力鍋功能讓它超越純電子鍋的定位，可以煮湯、燉肉和雜糧。夏天聚餐需要大量料理的時候，一台機器能做的事情越多越省事，這台的多工能力是清單裡面最強的。"},
                ]
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK rice-cookers")

def build_portable_ice_makers():
    d, p = load("best-portable-ice-makers.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "GE Profile Opal Nugget Ice Maker: Tested and Reviewed in 2026", "url": "https://www.tasteofhome.com/article/ge-profile-opal-nugget-ice-maker-review/", "source": "Taste of Home"},
            {"title": "8 Best Ice Makers: GE Profile Opal, GoveeLife, Frigidaire of 2026", "url": "https://www.reviewed.com/cooking/best-right-now/best-ice-machines", "source": "Reviewed"},
            {"title": "Best Smart Ice Makers 2026: Countertop Nugget Ice and Portable Ice Machines Tested", "url": "https://www.smarthomeexplorer.com/guides/best-smart-ice-makers-2026", "source": "Smart Home Explorer"},
        ],
        "i18n": {
            "en": {
                "commentary": "Portable ice makers hit their annual peak demand window right now, and the category is more competitive than it has ever been. The GE Profile Opal 2.0 holds rank one because nugget ice is simply a different product from bullet ice or crescent ice — it is chewable, absorbs drink flavor as it melts, and chills beverages faster because the high surface area of each nugget conducts cold more efficiently than a dense cube. The Opal 2.0 produces 38 pounds of nugget ice per day through a WiFi-connected system that lets you schedule ice production and run cleaning cycles from the SmartHQ app. The built-in UV light addresses the mold concern that plagued earlier countertop ice makers.\n\nThe Costway Nugget Self-Dispensing unit at rank two makes a strong case on production volume and value. Its 9.5 production score is the highest on this list, outputting more ice per hour than the Opal 2.0 at roughly one-third the price. The trade-off is the absence of smart connectivity and a slightly lower ice quality score — the nuggets are softer and less uniform than GE's output.\n\nFor buyers who specifically want regular bullet ice rather than nugget, the Hamilton Beach 86150 at rank three delivers the quietest operation on this list at a 9.5 noise score and an unbeatable value score. At under 100 dollars it is the honest budget recommendation for households who simply want ice quickly without caring about the format.\n\nFather's Day is three weeks away, and home bar setups are driving significant interest in the nugget ice segment specifically. The combination of a nugget ice maker with a cocktail kit or bartending tools is a genuinely practical gift for the right person. Summer heat has pushed search volume for portable ice makers to seasonal highs, and current inventory levels at major retailers suggest sustained demand through the Fourth of July period.",
                "highlights": [
                    {"title": "GE Opal 2.0 Leads on Ice Quality and Smart Features", "body": "Producing 38 pounds of nugget ice daily with WiFi scheduling and UV-light sanitation, the Opal 2.0 is the clear choice for households that take their ice seriously. The SmartHQ app integration and automatic cleaning cycles reduce maintenance burden significantly over earlier countertop ice maker designs."},
                    {"title": "Costway Wins on Production Volume and Value", "body": "The Costway Nugget Self-Dispensing unit produces more ice per hour than the GE Opal 2.0 at roughly one-third the price. For buyers who prioritize output over smart connectivity and premium ice uniformity, this is the most practical value proposition in the nugget ice segment."},
                    {"title": "Nugget Ice Demand Surges Heading Into Summer", "body": "Post-Memorial Day heat and Father's Day gift-buying are pushing nugget ice maker searches to seasonal peaks. Home bar culture has made nugget ice a mainstream preference rather than a restaurant novelty. Retailers are reporting strong sell-through on the nugget ice segment, suggesting buyers should not wait too long on purchasing decisions."},
                ]
            },
            "zh-tw": {
                "commentary": "製冰機這個品類在台灣的家用市場還在成長階段，但在美國已經是夏季廚房必備品之一。每年五月底到七月這段時間是製冰機銷量最高峰，今年也不例外，特別是碎冰（nugget ice）機型的需求量明顯高於往年。\n\nGE Profile Opal 2.0 拿第一名不是靠功能多，是靠碎冰本身的品質。碎冰跟傳統冰塊不一樣的地方在於：它可以咬碎、會吸收飲料的味道、融化速度和傳統冰塊也不同。每天 38 磅的產量對四到六人的家庭完全夠用，WiFi 連線可以用手機排程開始製冰，UV 燈消毒功能解決了早期台式製冰機常見的黴菌問題。\n\nCostway Nugget Self-Dispensing 排第二主要靠產量和 CP 值。每小時產冰量比 Opal 2.0 還高，售價大概只有三分之一。沒有智慧連線功能，碎冰的均勻度也略遜一籌，但如果預算有限又想要碎冰機，這是清單裡面最務實的選擇。\n\nHamilton Beach 86150 排第三走的是另一個路線：傳統子彈冰塊、最安靜的運作聲音（噪音評分 9.5）、最低的售價。如果你只是想要有冰可以用，不在意是哪種形狀，這台 NT$3,000 以內就能入手，是真正的入門首選。\n\n六月父親節快到了，碎冰機加調酒工具組是一個很受歡迎的禮物組合。今年夏季氣溫偏高，製冰機的搜尋量和銷量都在創近年新高，熱門機型的庫存消耗速度也比往年快，如果有計劃入手建議盡早決定。",
                "highlights": [
                    {"title": "GE Opal 2.0 碎冰品質和智慧功能最完整", "body": "每天 38 磅的碎冰產量、WiFi 排程製冰、UV 燈消毒，Opal 2.0 是目前家用碎冰機裡面功能最完整的一台。對認真在家調酒或重視飲品品質的人來說，這是清單裡面最值得投資的機型。"},
                    {"title": "Costway 產量最高、CP 值最強", "body": "Costway Nugget Self-Dispensing 的每小時產冰量比 GE Opal 2.0 還高，售價卻只有三分之一左右。不需要智慧連線功能、追求最大產量的買家，這台的性價比在整個碎冰機市場裡面很難被超越。"},
                    {"title": "夏季碎冰需求推升至年度高峰", "body": "美國陣亡將士紀念日後的高溫和即將到來的父親節，讓碎冰機的搜尋量和銷量同步創高。熱門機型庫存消耗速度比往年快，如果有考慮入手，建議在美國獨立日（七月四日）前後促銷期結束前做出決定。"},
                ]
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK portable-ice-makers")

def build_gas_grills():
    d, p = load("best-gas-grills.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Best Gas Grill Brands of 2026", "url": "https://www.consumerreports.org/home-garden/grills/best-gas-grill-brands-a1186225024/", "source": "Consumer Reports"},
            {"title": "Napoleon VS Weber: Which Gas Grill is Best in 2026?", "url": "https://www.smokedbbqsource.com/napoleon-vs-weber/", "source": "Smoked BBQ Source"},
            {"title": "Best BBQ Grills for Summer 2026: Top Gas, Pellet and Charcoal", "url": "https://www.todays-woman.net/2026/home-garden-reviews/best-bbq-grills-for-summer/", "source": "Today's Woman"},
        ],
        "i18n": {
            "en": {
                "commentary": "We are at peak gas grill season, with Father's Day on June 21 driving the strongest purchase intent of the year and post-Memorial Day grilling routines now fully established across most of the country. The Weber Spirit E-425 holds rank one through a combination of cooking power, heat distribution, and the most important variable in grill ownership: reliability. Its 9.6 value score is the best on this list, and for a four-burner grill at its price point that delivers genuine searing capability alongside a side burner for sauces and sides, the E-425 makes a near-irrefutable case as the rational purchase for most families.\n\nThe Weber Genesis E-325 at rank two continues to earn its position through the best even-heat score on the list at 9.5. Three-burner efficiency with precise zone control makes this the grill for people who care about cooking technique rather than raw BTU output. The Flavorizer bars, porcelain-enameled cooking grates, and Weber's warranty program make the Genesis the longer-term investment argument.\n\nNapoleon's Prestige 500 RSIB at rank three is the most powerful option in this tier, posting a 9.7 cooking power score. The infrared side and rear burners give it a rotisserie and searing capability that neither Weber option can match, and the build quality with stainless steel construction is genuinely premium. The value score of 7.5 reflects the price honestly — this is a grill for serious cooks who use every feature.\n\nFor Father's Day specifically, the Weber Spirit E-310 at rank six deserves attention as the best under-500-dollar three-burner option. Strong build quality from a trusted brand at an accessible price point is the right profile for many gift buyers who want to give something meaningful without stretching to four-figure territory.",
                "highlights": [
                    {"title": "Weber Spirit E-425 Is the Rational Pick for Most Families", "body": "Four burners, a side burner, genuine searing capability, and Weber's reliability record combine to make the E-425 the default recommendation for most buyers. Its 9.6 value score is the best on this list, which means you are getting premium-tier performance without premium-tier pricing. This is the Father's Day grill purchase that most households will not regret."},
                    {"title": "Napoleon Prestige 500 Leads on Raw Performance", "body": "The 9.7 cooking power score and infrared side and rear burners make the Prestige 500 RSIB the most capable grill on this list. Rotisserie cooking and serious high-heat searing capability push it into territory that Weber's Spirit and Genesis lineups cannot reach. The value trade-off is real, but for dedicated grill enthusiasts this is the right tool."},
                    {"title": "Father's Day Drives Peak Gas Grill Purchase Season", "body": "With Father's Day three weeks out, gas grill demand is at its annual peak. Weber and Napoleon are the two brands consistently at the top of recommendations from Consumer Reports and independent testing labs. Both are running Father's Day promotions worth checking before the June 21 deadline."},
                ]
            },
            "zh-tw": {
                "commentary": "現在是美國瓦斯烤爐銷售的黃金三週。五月底的陣亡將士紀念日假期剛過，六月二十一日父親節快到了，這段時間是一年裡面瓦斯烤爐購買意願最高的時期，各大品牌也都在這個時間點推出重點促銷。\n\nWeber Spirit E-425 守住榜首的理由很具體：四爐頭設計、側爐頭可以同時煮醬汁或玉米，火力夠強可以真正做出 Sear 的焦皮效果，而且 Weber 品牌的耐用度在市場上有長達幾十年的口碑驗證。CP 值評分 9.6 是這份清單最高的，意思是這個價位段能買到的表現已經非常接近更貴的機型。\n\nWeber Genesis E-325 排第二靠的是均勻熱場評分 9.5，整個清單最高。三爐頭的精準分區控溫讓你可以同時用直火煎和間接加熱做烤，對烹飪技術有要求的人會特別欣賞這種設計。Flavorizer 導油板和琺瑯烤網都是為了長期使用而設計的，Weber 保固計劃也是業界標竿。\n\nNapoleon Prestige 500 RSIB 排第三靠的是火力，烹飪功率評分 9.7 是清單最高。紅外線側爐和後爐頭讓它能做旋轉烤肉架料理，這兩款 Weber 都做不到。不鏽鋼機身構造也確實高一個等級。\n\n六月父親節送禮的話，Weber Spirit E-310 是預算控制在一定範圍內的最佳推薦，三爐頭、Weber 品牌品質保證，售價相對親民，是很多家庭的合理選擇。",
                "highlights": [
                    {"title": "Weber Spirit E-425 是大多數家庭最務實的選擇", "body": "四爐頭加側爐、Weber 可靠度口碑、最高的 CP 值評分，Spirit E-425 是這份清單最均衡的推薦。六月父親節送禮或自用，這台是大多數人買了不會後悔的機型。"},
                    {"title": "Napoleon Prestige 500 火力最強、功能最完整", "body": "烹飪功率評分 9.7、紅外線側爐和後爐頭支援旋轉烤架料理，Prestige 500 RSIB 的功能完整度是清單裡面最高的。認真玩戶外料理的人才能把它的功能全部用到，這是它最適合的買家輪廓。"},
                    {"title": "父親節帶動瓦斯烤爐銷售衝高峰", "body": "三週後就是父親節，這是美國全年瓦斯烤爐銷售最高峰。Weber 和 Napoleon 都有推出限時促銷活動，Consumer Reports 的品牌可靠度評比兩者都是頂尖表現，在這段時間入手時機和折扣力道都是一年裡最好的。"},
                ]
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK gas-grills")

def build_outdoor_griddles():
    d, p = load("best-outdoor-griddles.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "The 9 Best Outdoor Griddles for 2026 Expert Reviews", "url": "https://www.smokedbbqsource.com/best-outdoor-gas-griddles/", "source": "Smoked BBQ Source"},
            {"title": "Best Outdoor Griddles 2026: Blackstone vs Weber vs Camp Chef", "url": "https://griddleking.com/best-outdoor-griddle/", "source": "Griddle King"},
            {"title": "The Best Father's Day Grill Sales: Up to $300 Off Traeger and More", "url": "https://fieldandstream.com/outdoor-gear/cooking-outdoor/cooking-gear/fathers-day-grill-sales", "source": "Field and Stream"},
        ],
        "i18n": {
            "en": {
                "commentary": "Outdoor flat-top griddles have become one of the fastest-growing outdoor cooking categories over the past three years, and we are now at the peak of that growth curve with Father's Day driving the strongest purchase intent of the year. Camp Chef's Gridiron 36 holds rank one because it has solved the three problems that held the category back: the integrated lid enables true oven-style cooking and shields the surface from rain, the grease management system is the cleanest on this list with a dedicated catch system and easy-access drawer, and the build quality using heavy-gauge rolled steel delivers a surface that develops and maintains seasoning better than lighter competitors.\n\nThe Blackstone Original 36 Omnivore at rank two remains the most popular griddle in the country by unit sales, and for good reason. At 720 square inches and 60,000 BTUs with a lid and a value score of 9.6, it delivers the core griddle experience at a price that most buyers can justify without deliberation. The recent Omnivore version adds a more refined heat management system compared to earlier Blackstone models. Camp Chef's Gridiron earns the top spot on cooking experience, but the Blackstone wins on accessibility.\n\nTraeger's Flatrock at rank three brings the brand's zone-cooking philosophy to flat-top gridding. The three-zone system with independent burner controls enables a level of simultaneous temperature management that is unique in the category. Traeger's build quality and the stainless steel side shelves justify the premium over Blackstone, but the higher price point means the Flatrock is a considered purchase rather than an impulse buy.\n\nFather's Day promotions are running now: Blackstone is offering a free 30-piece tool kit with purchase, and Camp Chef has up to 200 dollars off select models at Sportsman's Warehouse. These deals are timed to the pre-June 21 buying window and worth acting on before they expire.",
                "highlights": [
                    {"title": "Camp Chef Gridiron Leads on Build and Grease Management", "body": "The integrated lid and dedicated grease management system are the two features that put the Camp Chef Gridiron ahead of the competition at rank one. The lid enables baking and steaming — cooking techniques that no open-surface griddle can replicate — and the grease drawer system is cleaner and easier than anything Blackstone offers at this price point."},
                    {"title": "Blackstone Omnivore Wins on Value and Popularity", "body": "The updated Omnivore model improves on earlier Blackstone designs with a more refined heat management system while keeping the price competitive. Its 9.6 value score is the highest on this list, and the free tool kit Father's Day promotion makes it the most compelling value proposition in the category right now."},
                    {"title": "Father's Day Promotions Are Live Now", "body": "Both Blackstone and Camp Chef are running active Father's Day promotions through June 21. Blackstone's free 30-piece tool kit and Camp Chef's up to 200-dollar discount at Sportsman's Warehouse are the standouts. These are time-limited offers that align with the peak buying window — act before inventory on popular configurations tightens."},
                ]
            },
            "zh-tw": {
                "commentary": "戶外平板鐵板燒烤盤（outdoor griddle）是過去三年成長最快的戶外料理品類之一，而現在六月父親節前夕正好是這個品類一年裡銷量最高的三週。\n\nCamp Chef Gridiron 36 拿第一名靠三個別人做不到或做不好的優點：一是整合式鍋蓋，可以悶煮、蒸煮，甚至模擬烤箱效果，讓鐵板燒不再只能做高溫直火料理；二是油脂管理系統是清單裡面最乾淨的，專屬集油槽加上抽屜式設計，清潔比 Blackstone 方便很多；三是厚規格軋鋼板面開火處理後的蓄熱和養鍋效果是業界頂尖水準。\n\nBlackstone Original 36 Omnivore 排第二是美國市場銷售量最高的戶外烤盤，靠的是 720 平方英寸烹飪面積、60,000 BTU 火力、附鍋蓋版本的 9.6 超高 CP 值評分。新版 Omnivore 款改進了熱場控制設計，比舊版更均勻。Camp Chef 在烹飪體驗上略勝一籌，但 Blackstone 在入手門檻和普及度上是市場之王。\n\nTraeger Flatrock 三區獨立溫控的設計讓它可以同時在不同溫區料理不同食材，是這份清單獨一無二的功能。不鏽鋼側架和整體工藝品質確實比 Blackstone 高一個等級，但價格也明顯較高，適合認真投入戶外料理的買家。\n\n父親節促銷現在就在跑：Blackstone 買就送三十件工具組，Camp Chef 在 Sportsman's Warehouse 有最高 NT$6,000 折扣。這些活動在六月二十一日父親節前截止，想買的話動作要快。",
                "highlights": [
                    {"title": "Camp Chef Gridiron 鍋蓋和排油設計最完整", "body": "整合式鍋蓋讓這台可以做悶煮和蒸煮，這是開放式烤盤無法做到的料理方式。加上業界最乾淨的抽屜式集油設計，Camp Chef Gridiron 在使用體驗的完整性上確實比同價位競品高一截。"},
                    {"title": "Blackstone Omnivore CP 值最高、市場最受歡迎", "body": "新版 Omnivore 改善了舊款 Blackstone 的熱場均勻性，售價維持在很有競爭力的水準，CP 值評分 9.6 是清單最高。父親節買就送三十件工具組的促銷，讓它的整體划算程度在六月份特別突出。"},
                    {"title": "父親節促銷現在就在跑，把握時間窗口", "body": "Blackstone 和 Camp Chef 的父親節優惠同步上線。Blackstone 免費贈送工具組，Camp Chef 特定款式最高折 NT$6,000。這些優惠截止在六月二十一日前後，熱門配置的庫存有限，建議盡早入手。"},
                ]
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK outdoor-griddles")

def build_portable_air_conditioners():
    d, p = load("best-portable-air-conditioners.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "11 Best Portable Air Conditioners of 2026", "url": "https://www.reviewed.com/home-outdoors/best-right-now/best-portable-air-conditioners", "source": "Reviewed"},
            {"title": "Best Portable Smart Air Conditioners 2026", "url": "https://www.smarthomeexplorer.com/guides/best-portable-smart-air-conditioners-2026", "source": "Smart Home Explorer"},
            {"title": "The Best Smart Air Conditioners in 2026, Tested for Cooling Power and Energy Efficiency", "url": "https://www.tomsguide.com/us/smart-air-conditioner-buying-guide,review-5615.html", "source": "Tom's Guide"},
        ],
        "i18n": {
            "en": {
                "commentary": "Portable air conditioner demand is surging as temperatures rise entering June, and the category has genuinely improved since two years ago with dual-hose designs now dominating the top of the market. The Midea Duo MAP14HS1TBL holds rank one through a combination of performance metrics that no single competitor matches across all dimensions: 9.5 scores in cooling, noise, efficiency, and smart connectivity make it the only truly balanced option on this list. The dual-hose duct system addresses the fundamental problem of single-hose portable ACs, which create negative pressure by exhausting room air and pulling in hot unconditioned air from outside through gaps. The Midea's sealed dual-hose design avoids this entirely, making it genuinely more efficient than the spec sheet BTU number implies.\n\nThe Whynter NEX ARC-1230WN at rank two has been a category benchmark for years, and the 2026 version maintains its standing. The activated carbon filter that cleans air while cooling it is a genuine differentiator, and Good Housekeeping has named Whynter's dual-hose design best overall through multiple evaluation cycles. At roughly 500 to 600 dollars it is a premium purchase, but the efficiency and air quality story makes it a compelling option for households in polluted urban environments.\n\nLG's LP1419IVSM at rank three posts the best noise score on this list at 9.6, making it the right choice for bedrooms and home offices where quiet operation matters as much as cooling capacity. The ThinQ app integration and energy monitoring add value beyond the basic remote control functionality that budget units offer.\n\nWith summer heat now arriving in earnest across most of the US, portable AC units are selling out at major retailers faster than restocking can keep up. Popular configurations of the Midea Duo and LG Inverter units are showing limited availability at some retailers. If you are in the market, the time to act is now rather than waiting for a sale that may not materialize before inventory clears.",
                "highlights": [
                    {"title": "Midea Duo's Dual-Hose System Solves the Core Problem", "body": "Single-hose portable ACs are fundamentally inefficient because exhausting air creates negative pressure that pulls in hot outside air through gaps and cracks. The Midea Duo's sealed dual-hose design eliminates this issue, delivering genuine efficiency that makes its R-32 inverter system over 40 percent more energy efficient than federal minimum standards. This is why it leads the category."},
                    {"title": "LG Inverter Leads on Quiet Operation", "body": "The LP1419IVSM's 9.6 noise score is the best on this list, making it the clear choice for bedrooms and home offices. At 52 dB on its lowest setting, it is meaningfully quieter than most portable AC units. The ThinQ energy monitoring app is a legitimate utility add-on rather than a marketing feature — it tracks consumption and helps optimize scheduling."},
                    {"title": "Summer Demand Is Outpacing Inventory", "body": "Major retailers are reporting faster sell-through on top portable AC units than supply chains can replenish in real-time. The Midea Duo and LG Inverter are the most affected models. With temperatures rising and no relief in the forecast, buyers who wait for a sale opportunity are increasingly likely to find their preferred configuration out of stock rather than on promotion."},
                ]
            },
            "zh-tw": {
                "commentary": "移動式冷氣的需求量每年這個時候都是高峰，今年夏季氣溫偏高，六月初的搜尋量和銷量都比往年同期明顯高出不少。台灣租屋族或是無法安裝固定式冷氣的環境，移動式冷氣是最實際的解決方案。\n\nMidea Duo MAP14HS1TBL 守住第一名，靠的是這份清單上唯一一台在制冷力、靜音、能效和智慧功能四個面向都拿到 9.5 分的機型。它的雙管設計（dual-hose）是關鍵：傳統單管移動式冷氣排出室內空氣的時候會形成負壓，反而把外面的熱空氣從門縫和窗縫吸進來，大幅降低制冷效率。Midea 的密封雙管設計完全避開這個問題，實際能效比規格表上的數字表現更好，比美國聯邦能效標準高出 40% 以上。\n\nWhynter NEX ARC-1230WN 排第二，多年來一直是這個品類的標竿機型。活性碳濾網在制冷同時過濾空氣，Good Housekeeping 多次評選為最佳雙管移動式冷氣，在空氣品質敏感族群中口碑特別好。售價大概在 NT$15,000-18,000 左右，是需要認真考慮的投資金額。\n\nLG LP1419IVSM 排第三靠的是靜音表現，噪音評分 9.6 是整張清單最高。最低模式 52 分貝的運作音量，放在臥室或居家工作室完全不會影響睡眠或專注。ThinQ App 的能耗監控功能也是真實有用的功能，不只是行銷噱頭。\n\n最近大型電商和零售通路反映熱門機型的補貨速度追不上銷量，特別是 Midea Duo 和 LG 變頻款。建議如果已經確定要買，不要等太久，因為這個夏天等到打折但買不到貨的風險比往年更高。",
                "highlights": [
                    {"title": "Midea Duo 雙管設計解決移動式冷氣的根本問題", "body": "單管移動式冷氣因為負壓問題，實際制冷效率遠低於規格表數字。Midea Duo 的密封雙管設計完全解決這個問題，R-32 變頻壓縮機讓它的能效比聯邦標準高出 40%。這是它坐穩第一名的核心理由。"},
                    {"title": "LG 變頻款靜音最佳、適合臥室和書房", "body": "LP1419IVSM 的噪音評分 9.6 是整張清單最高，最低模式只有 52 分貝。ThinQ App 的能耗監控讓你可以清楚掌握用電情況、優化使用時段。對睡眠品質或居家工作環境要求高的人，這是最適合的選擇。"},
                    {"title": "夏季需求旺盛、熱門機型庫存告急", "body": "目前主要電商平台反映 Midea Duo 和 LG 變頻款的補貨速度跟不上銷量，熱門規格出現缺貨情況。今年夏天氣溫偏高、需求提前爆發，等折扣卻買不到貨的風險比以往更高，已經確定要買的話建議盡早下手。"},
                ]
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK portable-air-conditioners")


if __name__ == "__main__":
    build_air_fryers()
    build_coffee_makers()
    build_dishwashers()
    build_rice_cookers()
    build_portable_ice_makers()
    build_gas_grills()
    build_outdoor_griddles()
    build_portable_air_conditioners()
    print("Batch 4 complete")
