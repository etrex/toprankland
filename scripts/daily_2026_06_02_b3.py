"""2026-06-02 daily update — Batch 3: Kitchen/Outdoor cooking (7 files)"""
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


def build_air_fryers():
    d, p = load("best-air-fryers.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "The Best Air Fryers of 2026 | Lab Tested & Ranked", "url": "https://www.techgearlab.com/topics/kitchen/best-air-fryer", "source": "TechGearLab"},
            {"title": "Cosori vs Ninja Air Fryer 2026: Which Is Better? (Tested)", "url": "https://kithub.blog/cosori-vs-ninja-air-fryer/", "source": "KitHub"},
            {"title": "Ninja vs Cosori Air Fryer: Which Brand Is Better in 2026?", "url": "https://sharkfryer.com/air-fryer-reviews/ninja-vs-cosori-air-fryer-brand/", "source": "SharkFryer"},
        ],
        "i18n": {
            "en": {
                "commentary": "The air fryer category in mid-2026 has settled into a clear hierarchy, and the Ninja Foodi DZ550 stays at the top for a reason that matters every single week: two independent baskets. With an 8-quart total capacity split into two zones, it cooks two different foods at two different temperatures and finishes them at the same moment. For anyone doing Sunday meal prep or feeding a family, that DualZone capability is the single most useful feature in the category, and the 9.5 capacity score reflects it directly.\n\nThe Cosori TurboBlaze at rank 2 is the pick I push hardest for families of three or more who want one big basket rather than two. TechGearLab named it their family favorite, and in head-to-head frozen-fry testing it produced slightly crispier, more evenly browned results than Ninja thanks to intelligent fan-speed control that adapts to each cooking mode. At 6 quarts it feeds a group without dominating the counter.\n\nThe Typhur Dome 2 at rank 3 is the premium statement piece, a large-capacity unit with a clear viewing window and genuinely fast convection. The Instant Vortex Plus ClearCook at rank 4 earns its spot on value and the see-through window that takes the guesswork out of doneness.\n\nGrilling season is in full swing, and air fryers have quietly become the indoor partner to the backyard grill, handling sides, wings, and reheats while the grill does the main event. With Father's Day on June 21, compact countertop cookers are climbing gift searches, and the dual-basket Ninja sits right in the sweet spot of price and practicality.",
                "highlights": [
                    {"title": "Ninja Foodi DZ550 Wins on DualZone Versatility", "body": "The 8-quart dual-basket design cooks two foods at two temperatures and syncs them to finish together. That 9.5 capacity score is the most practical feature in the category for meal prep and family dinners, and nothing at this price replicates it as cleanly."},
                    {"title": "Cosori TurboBlaze Is the Family Single-Basket Champion", "body": "TechGearLab named the TurboBlaze their favorite for families of three or more. Its intelligent fan-speed control delivered crispier, more even frozen fries than Ninja in head-to-head testing, and 6 quarts feeds a group without crowding the counter."},
                    {"title": "Air Fryers Are the Indoor Partner to Grilling Season", "body": "With grilling season peaking and Father's Day on June 21, air fryers handle wings, sides, and reheats indoors while the grill works outside. Compact countertop cookers are climbing gift searches, and the dual-basket Ninja hits the price-and-practicality sweet spot."},
                ],
            },
            "zh-tw": {
                "commentary": "氣炸鍋這個品類到了 2026 年中已經分出清楚的層次，Ninja Foodi DZ550 穩坐第一是有道理的，而且這個道理每週都用得到：雙獨立籃。8 夸脫的總容量切成兩個獨立溫區，可以同時用不同溫度炸兩種食物，還會自動讓兩邊同時完成。對每週六做備餐的人，或是要餵一家人的家庭來說，這個雙區功能就是整個品類最實用的設計，容量拿 9.5 分一點都不誇張。\n\n第二名的 Cosori TurboBlaze，我最推給三人以上、想要一個大籃子而不是兩個小籃的家庭。TechGearLab 直接把它選為家庭首選，而且在冷凍薯條對比測試裡，它靠著會隨烹飪模式自動調整的智慧風速控制，炸出來比 Ninja 更酥更均勻。6 夸脫的容量餵一桌人沒問題，又不會把整個流理台佔滿。\n\nTyphur Dome 2 第三名，走的是高階路線，大容量加上透明觀景窗，對流速度是真的快。Instant Vortex Plus ClearCook 第四，靠的是性價比和那扇看得到熟度的透明窗，炸東西不用一直開蓋確認。\n\n烤肉季正旺，氣炸鍋默默變成後院烤爐的室內好搭檔，主菜在外面烤，配菜、雞翅、復熱就交給氣炸鍋。父親節（6/21）快到了，這種小巧的桌上型廚電在禮物搜尋榜上一直往上爬，雙籃的 Ninja 剛好卡在價格和實用性的甜蜜點。",
                "highlights": [
                    {"title": "Ninja Foodi DZ550 雙區設計取勝", "body": "8 夸脫雙籃可同時用兩種溫度炸兩種食物，並自動同步完成。9.5 的容量分是這個品類裡備餐和家庭晚餐最實用的功能，這個價位找不到第二台做得這麼乾淨俐落。"},
                    {"title": "Cosori TurboBlaze 是單籃家庭冠軍", "body": "TechGearLab 把 TurboBlaze 選為三人以上家庭首選。智慧風速控制在對比測試中炸出比 Ninja 更酥更均勻的冷凍薯條，6 夸脫餵一桌人不擠台面。"},
                    {"title": "氣炸鍋是烤肉季的室內最佳拍檔", "body": "烤肉季正旺，父親節（6/21）在即，氣炸鍋在室內負責雞翅、配菜和復熱，烤爐在外面顧主菜。桌上型廚電禮物搜尋量持續攀升，雙籃 Ninja 卡在價格與實用性的甜蜜點。"},
                ],
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
            {"title": "Best coffee maker 2026: we tested over 90 machines, and these are the top 7", "url": "https://www.tomsguide.com/home/coffee-makers/best-coffee-makers", "source": "Tom's Guide"},
            {"title": "Technivorm Moccamaster KBGV Select review: Still the best coffee maker", "url": "https://www.tomsguide.com/home/coffee-makers/technivorm-moccamaster-kgbv-select-review", "source": "Tom's Guide"},
            {"title": "15 Best Drip Coffee Makers (Tested and Reviewed) of 2026", "url": "https://www.reviewed.com/cooking/best-right-now/best-drip-coffee-makers", "source": "Reviewed"},
        ],
        "i18n": {
            "en": {
                "commentary": "After re-reviewing the Technivorm Moccamaster KBGV Select in early 2026, the verdict has not changed: this is still the best drip coffee maker you can buy. Tom's Guide, which has tested over 90 machines, re-ranked it as their top pick, and the reasoning is exactly why it holds rank 1 here at a 9.2 overall. The dual brew-quality and durability scores both sit at 9.8 because this machine does two things better than anything else: it brews up to 10 cups of remarkably well-balanced coffee in about five minutes, and it is hand-built in the Netherlands to last a literal lifetime. You buy this once.\n\nThe Breville Precision Brewer Thermal at rank 2 is the versatility champion. It handles drip, iced, and cold brew with programmable temperature and bloom control, and reviewers describe it as a sleeker, more modern take on the Moccamaster formula. If you want to dial in exactly how your coffee is made, this is the machine.\n\nThe Fellow Aiden at rank 3 is the precision enthusiast's pick. Reviewers compare it to a Tesla, all PID-controlled thermoblock engineering wrapped in a touchscreen that lets you set bloom time, pulse patterns, and brew ratios. For people who treat morning coffee as a craft, nothing offers this much control.\n\nThe Bruvi BV-01 at rank 4 covers the single-serve pod crowd without the usual pod-coffee compromises, and the Cuisinart DCC-4000 at rank 5 remains the dependable mainstream value pick. Heading into summer, the Breville and Fellow earn extra relevance because both make genuinely good cold brew and iced coffee at home, which is exactly what people want when the temperature climbs.",
                "highlights": [
                    {"title": "Moccamaster KBGV Select Is Still the Best, Re-Confirmed", "body": "Tom's Guide re-reviewed it in early 2026 and kept it as their top pick after testing over 90 machines. Dual 9.8 scores in brew quality and durability reflect 10 cups of balanced coffee in five minutes from a hand-built machine engineered to last a lifetime."},
                    {"title": "Breville Precision Brewer Owns Versatility", "body": "Drip, iced, and cold brew with programmable temperature and bloom control make the Precision Brewer the most flexible machine here. Reviewers call it a sleeker, modern Moccamaster, and that flexibility matters most as summer iced-coffee season arrives."},
                    {"title": "Fellow Aiden Is the Precision Craft Pick", "body": "Reviewers liken the Aiden to a Tesla: a PID-controlled thermoblock and touchscreen let you set bloom time, pulse patterns, and brew ratios. For anyone who treats morning coffee as a craft, no other machine on this list offers comparable control."},
                ],
            },
            "zh-tw": {
                "commentary": "Technivorm Moccamaster KBGV Select 在 2026 年初被重新評測過一輪，結論沒變：它依然是你買得到最好的滴漏式咖啡機。測過 90 多台機器的 Tom's Guide 再次把它列為首選，這個理由也正是它在這裡穩坐第一、總分 9.2 的原因。沖煮品質和耐用度雙雙拿到 9.8 分，因為這台機器有兩件事做得比誰都好：五分鐘左右就能沖出最多 10 杯風味極度均衡的咖啡，而且它在荷蘭手工打造，真的可以用一輩子。買一次就夠了。\n\n第二名的 Breville Precision Brewer Thermal 是多功能冠軍。滴漏、冰咖啡、冷萃通通能做，溫度和悶蒸時間都能程式化設定，評測者形容它是 Moccamaster 配方的更時尚現代版。想要精準掌控咖啡怎麼沖，就選這台。\n\n第三名的 Fellow Aiden 是精準玩家的最愛。評測者把它比喻成特斯拉，PID 控溫的瞬熱模組加上觸控螢幕，讓你設定悶蒸時間、脈衝模式、粉水比。對把早晨咖啡當作一門手藝的人，沒有別台能給這麼多控制權。\n\n第四名 Bruvi BV-01 照顧到膠囊單杯族，又避開一般膠囊咖啡的妥協；第五名 Cuisinart DCC-4000 仍是可靠的主流性價比選擇。夏天到了，Breville 和 Fellow 更顯重要，因為兩台在家就能做出真正好喝的冷萃和冰咖啡，天氣一熱這正是大家想要的。",
                "highlights": [
                    {"title": "Moccamaster KBGV Select 依然最強，重新確認", "body": "Tom's Guide 在 2026 年初重評後，測過 90 多台機器仍把它列為首選。沖煮品質與耐用度雙 9.8 分，手工打造、可用一輩子的機身，五分鐘沖出 10 杯均衡咖啡。"},
                    {"title": "Breville Precision Brewer 多功能無人能敵", "body": "滴漏、冰咖啡、冷萃全包，溫度與悶蒸時間都能程式設定，是這裡最靈活的機器。評測者稱它是更時尚的現代版 Moccamaster，夏天冰咖啡季一到這份靈活性最有感。"},
                    {"title": "Fellow Aiden 是精準手藝派首選", "body": "評測者把 Aiden 比作特斯拉：PID 控溫瞬熱模組加觸控螢幕，可設定悶蒸時間、脈衝模式、粉水比。把早晨咖啡當手藝的人，這份榜單裡沒有第二台能給這麼多掌控權。"},
                ],
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
            {"title": "Best (and Worst) Dishwashers of 2026, Lab-Tested and Reviewed", "url": "https://www.consumerreports.org/appliances/dishwashers/best-dishwashers-of-the-year-a6109623431/", "source": "Consumer Reports"},
            {"title": "Not LG, Not GE: This Brand Tops Consumer Reports' 'Best Dishwashers Of 2026' List", "url": "https://www.slashgear.com/2138296/best-dishwasher-brand-2026-consumer-reports-bosch/", "source": "SlashGear"},
            {"title": "Bosch vs. Miele Dishwashers (2026): Reliability, Wash vs. Dry, and Price-Band Matchups", "url": "https://blog.yaleappliance.com/bosch-vs-miele-dishwashers", "source": "Yale Appliance"},
        ],
        "i18n": {
            "en": {
                "commentary": "Consumer Reports released its Best Dishwashers of 2026 rankings, and Bosch swept the top three spots, which is exactly the picture this list reflects. The Bosch Benchmark SHP9PCM5N holds rank 1 at a 9.4 overall because it pairs the best cleaning and drying in CR's lab with a 38 dBA noise rating that is effectively silent in a real kitchen. That 9.8 quietness score is not a spec-sheet flourish, it is the difference between running a wash mid-evening or waiting until everyone is asleep. For open-plan homes, the Benchmark is the one I recommend without hesitation.\n\nThe Miele G 7156 SCVi at rank 2 is the reliability and build-quality answer. Miele earned the most reliable dishwasher brand title for 2026 with a 5.6 percent first-year service rate, edging Bosch by a meaningful margin, and the brand's AutoDos automatic detergent dispensing remains a genuinely useful daily convenience. If you plan to keep a dishwasher for fifteen years, Miele is the long-game pick.\n\nThe Bosch 800 Series SHX78CM5N at rank 3 delivers most of the Benchmark experience, including the CrystalDry hot-zeolite drying that finally solves plastic-load drying, at a more approachable price. The Miele G 5008 SCU at rank 4 and Bosch 500 Series at rank 5 round out a list where, honestly, you cannot make a bad choice. The takeaway from CR's 2026 testing is simple: Bosch owns quiet and value across price bands, Miele owns reliability and drying, and both brands sit far ahead of the mainstream field.",
                "highlights": [
                    {"title": "Bosch Benchmark Tops Consumer Reports 2026", "body": "CR's 2026 rankings put Bosch in the top three spots, with the Benchmark SHP9PCM5N leading on combined cleaning and drying. Its 38 dBA rating and 9.8 quietness score make it effectively silent, the clear pick for open-plan kitchens where wash timing matters."},
                    {"title": "Miele G 7156 Wins Reliability for 2026", "body": "Miele earned the most reliable dishwasher brand title with a 5.6 percent first-year service rate, ahead of Bosch. Paired with AutoDos automatic detergent dispensing and premium build, it is the long-game pick for buyers planning to keep a machine fifteen years."},
                    {"title": "Bosch 800 Series Delivers CrystalDry Value", "body": "The 800 Series SHX78CM5N brings Benchmark-tier performance, including CrystalDry hot-zeolite drying that finally handles plastic loads, at a more approachable price. It is the value sweet spot for buyers who want flagship drying without flagship cost."},
                ],
            },
            "zh-tw": {
                "commentary": "Consumer Reports 公布了 2026 年最佳洗碗機排名，Bosch 直接包辦前三名，這份榜單呈現的正是這個局面。Bosch Benchmark SHP9PCM5N 穩坐第一、總分 9.4，因為它把 CR 實驗室裡最好的清潔和烘乾，搭配 38 分貝這種在真實廚房裡幾乎聽不到的噪音表現。9.8 的安靜分數不是規格表上的裝飾，它決定了你能不能在傍晚就開機洗，而不用等到全家都睡了。對開放式格局的家，Benchmark 我推得毫不猶豫。\n\n第二名的 Miele G 7156 SCVi 是可靠度和做工的答案。Miele 拿下 2026 年最可靠洗碗機品牌，第一年維修率只有 5.6%，明顯領先 Bosch，而且品牌的 AutoDos 自動投洗劑功能在日常使用上真的很方便。如果你打算一台洗碗機用十五年，Miele 是長期布局的選擇。\n\n第三名 Bosch 800 系列 SHX78CM5N 把 Benchmark 的體驗大部分都搬了過來，包括終於解決塑膠餐具烘乾問題的 CrystalDry 沸石熱烘技術，價格卻更親民。第四名 Miele G 5008 SCU 和第五名 Bosch 500 系列補齊整份榜單，老實說選哪一台都不會錯。CR 2026 測試的結論很簡單：Bosch 在各價位段拿下安靜和性價比，Miele 拿下可靠度和烘乾，兩個品牌都遠遠領先主流陣營。",
                "highlights": [
                    {"title": "Bosch Benchmark 登頂 Consumer Reports 2026", "body": "CR 2026 排名讓 Bosch 包辦前三，Benchmark SHP9PCM5N 以清潔加烘乾綜合表現居首。38 分貝、9.8 安靜分讓它幾乎無聲，開放式廚房在意洗碗時段的首選。"},
                    {"title": "Miele G 7156 拿下 2026 可靠度冠軍", "body": "Miele 以第一年 5.6% 維修率拿下最可靠品牌，領先 Bosch。搭配 AutoDos 自動投洗劑與頂級做工，是打算一台用十五年的長期布局首選。"},
                    {"title": "Bosch 800 系列帶來 CrystalDry 高性價比", "body": "800 系列 SHX78CM5N 把 Benchmark 等級表現帶到更親民價位，含終於搞定塑膠餐具的 CrystalDry 沸石熱烘。想要旗艦烘乾又不想付旗艦價，這是甜蜜點。"},
                ],
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
            {"title": "Best rice cookers in 2026, tested by our editors", "url": "https://www.cnn.com/cnn-underscored/reviews/best-rice-cooker", "source": "CNN Underscored"},
            {"title": "Zojirushi vs Tiger: Which Rice Cooker Is the Best?", "url": "https://prudentreviews.com/zojirushi-vs-tiger/", "source": "Prudent Reviews"},
            {"title": "12 Best Rice Cookers: Our guide to perfect rice of 2026", "url": "https://www.reviewed.com/cooking/best-right-now/the-best-rice-cookers", "source": "Reviewed"},
        ],
        "i18n": {
            "en": {
                "commentary": "The rice cooker rankings have a stable top, and the Zojirushi NP-HCC10 stays at rank 1 because nothing in 2026 has dethroned Zojirushi on the thing that matters most: rice quality. The 9.8 riceQuality score is earned through induction heating and fuzzy-logic temperature control that produce fluffy, evenly cooked grains whether you are making sushi rice, brown rice, or basmati. Zojirushi has held the top recommendation in this category for nearly a decade, and the consistency is the whole point.\n\nThe Tiger JKT-D10U at rank 2 is the pick for people who want Zojirushi-class rice with more speed. In testing it cooked white rice in 44 minutes versus 53 for the Zojirushi, and brown rice in 63 minutes versus 103, a genuinely large gap if you cook rice daily. The results are nearly indistinguishable in quality, so if your kitchen runs on a schedule, Tiger's speed advantage is the deciding factor.\n\nThe Zojirushi NS-ZCC10 at rank 3 remains the value-conscious Zojirushi, the model reviewers have called the number-one recommendation for nearly ten years, delivering most of the flagship's quality at a friendlier price. The Cuckoo CRP-ST0609F at rank 4 is the speed-and-durability specialist, cooking white rice in 20 to 28 minutes, faster than almost anything else here, with the high-pressure approach Korean brands are known for.\n\nFor everyday Taiwanese kitchens where rice is on the table at most meals, the choice comes down to priorities: Zojirushi for the absolute best grain, Tiger for quality plus speed, Cuckoo for the fastest cook. All three are genuinely excellent.",
                "highlights": [
                    {"title": "Zojirushi NP-HCC10 Still Owns Rice Quality", "body": "A 9.8 riceQuality score from induction heating and fuzzy-logic control produces fluffy, even grains across sushi, brown, and basmati rice. Zojirushi has held this category's top recommendation for nearly a decade, and nothing in 2026 has dethroned it."},
                    {"title": "Tiger JKT-D10U Matches Quality and Adds Speed", "body": "In testing, the JKT-D10U cooked white rice in 44 minutes versus Zojirushi's 53, and brown rice in 63 versus 103, with nearly indistinguishable results. For daily rice cooks running on a schedule, that speed advantage is the deciding factor."},
                    {"title": "Cuckoo CRP-ST0609F Is the Speed Specialist", "body": "Cooking white rice in 20 to 28 minutes, the Cuckoo is among the fastest here, using the high-pressure approach Korean brands are known for. It pairs that speed with the durability reputation that earns it rank 4 on this list."},
                ],
            },
            "zh-tw": {
                "commentary": "電子鍋榜單的頂端很穩，Zojirushi NP-HCC10 繼續穩坐第一，因為 2026 年沒有任何一台在最關鍵的事情上撼動象印：飯的品質。9.8 的米飯品質分來自 IH 電磁加熱加上模糊邏輯控溫，不管你煮壽司米、糙米還是印度香米，煮出來的飯都粒粒分明、受熱均勻。象印在這個品類的首選地位維持了將近十年，這份穩定就是它的全部價值。\n\n第二名的 Tiger JKT-D10U，是給想要象印等級的飯、但又想快一點的人。測試裡它煮白米只要 44 分鐘，象印要 53 分鐘；煮糙米 63 分鐘對上象印的 103 分鐘，每天煮飯的話這個差距很有感。品質幾乎分不出高下，所以如果你家廚房是照表操課的，Tiger 的速度優勢就是決勝點。\n\n第三名 Zojirushi NS-ZCC10 是預算取向的象印，評測者稱它將近十年來都是首選推薦，用更親民的價格給你旗艦機大部分的品質。第四名 Cuckoo CRP-ST0609F 是速度和耐用的專家，煮白米只要 20 到 28 分鐘，快過這裡幾乎所有對手，用的是韓系品牌擅長的高壓路線。\n\n對幾乎每餐都有飯的台灣家庭來說，選擇取決於你看重什麼：要最好的飯選象印，要品質加速度選 Tiger，要煮最快選 Cuckoo。這三台都是真材實料的好鍋。",
                "highlights": [
                    {"title": "Zojirushi NP-HCC10 米飯品質依然稱王", "body": "9.8 米飯品質分來自 IH 加熱與模糊邏輯控溫，壽司米、糙米、香米都粒粒分明受熱均勻。象印近十年穩居這個品類首選，2026 年沒有對手能撼動。"},
                    {"title": "Tiger JKT-D10U 品質齊平還更快", "body": "測試中 JKT-D10U 煮白米 44 分鐘對象印 53 分鐘，糙米 63 分鐘對 103 分鐘，品質幾乎難分。每天照表煮飯的家庭，這個速度優勢就是決勝點。"},
                    {"title": "Cuckoo CRP-ST0609F 是速度專家", "body": "白米 20 到 28 分鐘煮好，是這裡最快的之一，用的是韓系品牌擅長的高壓技術。速度加上耐用口碑，讓它穩居榜單第四。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK rice-cookers")


def build_gas_grills():
    d, p = load("best-gas-grills.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Weber Spirit vs Genesis: Entry Level VS Mid-Range Gas Grills", "url": "https://www.smokedbbqsource.com/weber-spirit-vs-genesis/", "source": "Smoked BBQ Source"},
            {"title": "Weber Genesis E-325: Expert Tested and Reviewed [2026]", "url": "https://www.tasteofhome.com/article/weber-genesis/", "source": "Taste of Home"},
            {"title": "Should You Still Buy a Weber Grill in 2026? Spirit, Genesis", "url": "https://blog.yaleappliance.com/difference-between-weber-bbq-grills", "source": "Yale Appliance"},
        ],
        "i18n": {
            "en": {
                "commentary": "Grilling season is at full boil, and with Father's Day on June 21 the gas grill market is in its single busiest stretch of the year. The Weber Spirit E-425 holds rank 1 at a 9.3 overall, and it earns it on the metric that matters to the most buyers: value. Reviewers consistently call the Spirit line the best bang for your buck in the entire BBQ industry, and the E-425 backs that up with a useful dedicated sear zone, three strong burners, and Weber's legendary porcelain-enameled durability, all available under $600 when it goes on sale. The 9.6 value score is the highest on this list, and for most families this is simply the grill to buy.\n\nThe Weber Genesis E-325 at rank 2 is the step-up pick that several outlets named their overall best for 2026. It cranks 39,000 BTUs across three burners with a 13,000 BTU sear zone for high-heat steaks, and its larger mass holds heat dead-even across the entire grate, which is exactly what you want when cooking for a crowd. Taste of Home praised its powerful performance and clever features.\n\nThe Napoleon Prestige 500 RSIB at rank 3 brings infrared side and rear burners and a premium stainless build for buyers who want maximum versatility. The Weber Summit S-470 at rank 4 is the four-burner powerhouse for serious entertainers, and the Broil King Regal S590 Pro at rank 5 rounds out a strong field. Heading into the Father's Day weekend, the Spirit E-425 sits right at the intersection of price, performance, and gift-ability.",
                "highlights": [
                    {"title": "Weber Spirit E-425 Is the Value King", "body": "A 9.6 value score, the highest on this list, backs the Spirit's reputation as the best bang for your buck in BBQ. A dedicated sear zone, three strong burners, and Weber's porcelain-enameled durability under $600 on sale make it the grill for most families."},
                    {"title": "Weber Genesis E-325 Is the 2026 Step-Up Best", "body": "Named overall best by several outlets, the Genesis E-325 delivers 39,000 BTUs across three burners plus a 13,000 BTU sear zone. Its larger mass holds dead-even heat across the entire grate, ideal for cooking for a crowd through grilling season."},
                    {"title": "Father's Day Drives Peak Grill Demand", "body": "With Father's Day on June 21 and grilling season peaking, gas grills are among the most-searched gifts right now. The Spirit E-425 sits at the intersection of price, performance, and gift-ability, making it the standout pick for the holiday weekend."},
                ],
            },
            "zh-tw": {
                "commentary": "烤肉季火力全開，父親節（6/21）又快到了，瓦斯烤爐市場正進入全年最忙的一段。Weber Spirit E-425 穩坐第一、總分 9.3，靠的是對最多買家最重要的那個指標：性價比。評測者一致把 Spirit 系列稱為整個烤肉產業最划算的選擇，E-425 用一個實用的專屬煎烤區、三支強力爐頭、加上 Weber 傳奇的琺瑯瓷塗層耐用度來證明這點，特價時不到 $600 美元就能入手。9.6 的性價比分是全榜最高，對大多數家庭來說，這就是該買的那台烤爐。\n\n第二名 Weber Genesis E-325 是升級選擇，好幾家媒體把它選為 2026 年綜合最佳。三支爐頭總輸出 39,000 BTU，加上 13,000 BTU 的煎烤區可以高溫煎牛排，而且它較大的爐體質量讓整個烤面受熱平均到不行，這正是你要餵一群人時想要的。Taste of Home 稱讚它性能強勁、設計聰明。\n\n第三名 Napoleon Prestige 500 RSIB 帶來紅外線側燒和後燒爐頭，加上高級不鏽鋼機身，給想要最多變化的買家。第四名 Weber Summit S-470 是四爐頭猛獸，給認真招待客人的人；第五名 Broil King Regal S590 Pro 補齊這個強悍陣容。父親節週末在即，Spirit E-425 剛好站在價格、性能、送禮三者的交叉點上。",
                "highlights": [
                    {"title": "Weber Spirit E-425 是性價比之王", "body": "9.6 性價比分全榜最高，撐起 Spirit 烤肉界最划算的名聲。專屬煎烤區、三支強力爐頭、Weber 琺瑯瓷耐用度，特價不到 $600 美元，大多數家庭該買的就是這台。"},
                    {"title": "Weber Genesis E-325 是 2026 升級首選", "body": "多家媒體選為綜合最佳，三爐頭總輸出 39,000 BTU 加 13,000 BTU 煎烤區。較大爐體質量讓整片烤面受熱平均，烤肉季餵一大群人最理想。"},
                    {"title": "父親節推升烤爐需求到高峰", "body": "父親節（6/21）加上烤肉季高峰，瓦斯烤爐是當前最熱搜的禮物之一。Spirit E-425 站在價格、性能、送禮的交叉點上，是這個假期週末最突出的選擇。"},
                ],
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
            {"title": "The Best Outdoor Griddle for 2026", "url": "https://thebarbecuelab.com/best-outdoor-griddle/", "source": "The Barbecue Lab"},
            {"title": "The 9 Best Outdoor Griddles for 2026", "url": "https://www.smokedbbqsource.com/best-outdoor-gas-griddles/", "source": "Smoked BBQ Source"},
            {"title": "Blackstone VS Camp Chef: Who Makes The Best Griddle?", "url": "https://www.smokedbbqsource.com/blackstone-vs-camp-chef-griddle/", "source": "Smoked BBQ Source"},
        ],
        "i18n": {
            "en": {
                "commentary": "Flat-top griddle cooking is having its biggest summer yet, and the Camp Chef Gridiron 36 holds rank 1 at a 9.3 overall because it takes the proven Blackstone formula and improves the two things that frustrate griddle owners most. The grease-management score of 9.6 is the headline: Camp Chef moved the grease trap to the front where it actually catches runoff cleanly instead of the rear-drain mess, and a built-in lid means you can store it outside and griddle-steam at will. For just a small step up in price over the standard Blackstone 36, you get a more refined daily-cook experience, which is exactly why reviewers have been flagging the Gridiron as the newest standout.\n\nThe Blackstone Original 36 Omnivore at rank 2 remains the people's champion and the best griddle for most buyers. With 720 square inches, four independent burners, and unbeatable value around $400, it is the default recommendation for backyard cooks who want maximum cooking surface per dollar. Nothing else delivers this much steel for the money.\n\nThe Traeger Flatrock 3-Zone at rank 3 is the premium engineering pick. Its three independently controlled TruZone burners let you sear steak at max heat, cook eggs on low, and toast buns in between, all at once, and it earned first place for wind resistance in testing, holding temperature far better than rivals on a breezy patio. The Weber Slate 36 at rank 4 brings a rust-resistant pre-seasoned top and Weber build quality, and the Blackstone Iron Forged 36 at rank 5 rounds out a strong field. With Father's Day on June 21, griddles are a top backyard-cooking gift, and the Gridiron 36 is the one I would put under the wrapping.",
                "highlights": [
                    {"title": "Camp Chef Gridiron 36 Fixes Grease and Adds a Lid", "body": "A 9.6 grease-management score comes from a front-mounted trap that catches runoff cleanly, and a built-in lid enables outdoor storage and griddle-steaming. For a small step up over the standard Blackstone 36, it is the most refined daily-cook experience here."},
                    {"title": "Blackstone Original 36 Is the People's Value Champion", "body": "720 square inches, four independent burners, and unbeatable value around $400 make the Original 36 the default pick for most backyard cooks. Nothing else delivers this much cooking steel per dollar, which keeps it firmly at rank 2."},
                    {"title": "Traeger Flatrock Wins on Zones and Wind", "body": "Three independent TruZone burners let you sear, fry, and toast simultaneously, and the Flatrock took first place for wind resistance in testing, holding temperature far better than rivals on a breezy patio. It is the premium engineering pick for serious griddlers."},
                ],
            },
            "zh-tw": {
                "commentary": "鐵板煎台料理正迎來史上最旺的一個夏天，Camp Chef Gridiron 36 穩坐第一、總分 9.3，因為它把已經被驗證過的 Blackstone 配方，在最讓煎台用戶頭痛的兩件事上做了改進。油脂管理 9.6 分是重點：Camp Chef 把集油盤移到前方，真的能乾淨接住流下來的油，不再是後方排油那種狼狽，而且內建的上蓋讓你可以放在戶外存放、想煎想蒸都行。只比標準款 Blackstone 36 貴一點點，就換來更精緻的日常烹煮體驗，這正是評測者紛紛點名 Gridiron 是最新黑馬的原因。\n\n第二名 Blackstone Original 36 Omnivore 仍是庶民冠軍，也是最多人該買的那台煎台。720 平方英吋、四支獨立爐頭、約 $400 美元的無敵性價比，是後院料理者想用最少錢換最大煎面的預設首選。論單位金額能買到多少鋼板，沒有對手。\n\n第三名 Traeger Flatrock 3-Zone 是高階工藝選擇。三個獨立控制的 TruZone 爐頭，讓你同時用最高溫煎牛排、小火煎蛋、中間烤麵包，而且它在測試中拿下抗風第一名，在有風的陽台上比對手更能穩住溫度。第四名 Weber Slate 36 帶來抗鏽預開鍋面板和 Weber 做工，第五名 Blackstone Iron Forged 36 補齊強悍陣容。父親節（6/21）在即，煎台是後院料理的熱門禮物，要包進禮物盒，我會選 Gridiron 36。",
                "highlights": [
                    {"title": "Camp Chef Gridiron 36 解決油脂還多了上蓋", "body": "9.6 油脂管理分來自前置集油盤，能乾淨接住流下的油，內建上蓋讓戶外存放與蒸煎都行。只比標準 Blackstone 36 貴一點，是這裡最精緻的日常烹煮體驗。"},
                    {"title": "Blackstone Original 36 是庶民性價比冠軍", "body": "720 平方英吋、四支獨立爐頭、約 $400 美元無敵性價比，讓 Original 36 成為多數後院料理者的預設首選。單位金額能買到的鋼板量沒人能比，穩居第二。"},
                    {"title": "Traeger Flatrock 靠分區與抗風取勝", "body": "三個獨立 TruZone 爐頭讓你同時煎、炒、烤，且在測試中抗風奪冠，有風陽台上比對手更穩溫。是給認真煎台玩家的高階工藝之選。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK outdoor-griddles")


def build_portable_ice_makers():
    d, p = load("best-portable-ice-makers.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "GE Profile Opal Nugget Ice Maker: Tested & Reviewed in 2026", "url": "https://www.tasteofhome.com/article/ge-profile-opal-nugget-ice-maker-review/", "source": "Taste of Home"},
            {"title": "Best Smart Ice Makers 2026: Countertop Nugget Ice and Portable Ice Machines Tested", "url": "https://www.smarthomeexplorer.com/guides/best-smart-ice-makers-2026", "source": "Smart Home Explorer"},
            {"title": "The 10 Best Countertop Nugget Ice Makers of 2026", "url": "https://www.theconsumers.guide/reviews/best-countertop-nugget-ice-makers-tested-ranked-2026", "source": "The Consumers Guide"},
        ],
        "i18n": {
            "en": {
                "commentary": "Summer heat is the entire reason this category exists, and the GE Profile Opal 2.0 holds rank 1 at a 9.1 overall because it makes the best ice of any countertop machine, full stop. The 9.8 ice-quality score reflects true Sonic-style soft nugget ice, the chewable pellet ice that people drive across town for, produced at up to 24 pounds a day with a first batch ready in about ten minutes. What pushes it past every rival is that the smart features actually get used: Wi-Fi scheduling through the SmartHQ app lets you run production overnight on off-peak rates and wake up to a full bin, set low-bin alerts, and check remotely whether you have enough ice before guests arrive. For summer entertaining, that is genuinely useful, not gimmick connectivity.\n\nThe Costway Nugget Self-Dispensing at rank 2 is the value nugget pick, delivering the same chewable pellet format with a built-in dispenser at a notably lower price than the Opal. For households that love nugget ice but cannot justify the GE premium, this is the smart compromise.\n\nThe Hamilton Beach 86150 at rank 3 is the fast-cube workhorse for buyers who care more about volume and speed than nugget texture, churning out bullet ice quickly for coolers and parties. The Chefman Iceman Compact at rank 4 is the small-footprint pick for tight counters and RVs, and the Euhomy Luna Pro at rank 5 rounds out the list. With temperatures climbing and backyard gatherings ramping up through June, a countertop ice maker is one of the most quietly life-improving summer purchases, and the Opal 2.0 is the one to beat.",
                "highlights": [
                    {"title": "GE Profile Opal 2.0 Makes the Best Nugget Ice", "body": "A 9.8 ice-quality score reflects true Sonic-style soft nugget ice at up to 24 pounds a day, with the first batch ready in about ten minutes. It is the chewable pellet ice people seek out, and no countertop rival matches its texture and output."},
                    {"title": "SmartHQ Scheduling Earns Its Keep in Summer", "body": "Wi-Fi scheduling lets you run the Opal overnight on off-peak rates, set low-bin alerts, and check ice levels remotely before guests arrive. For summer entertaining this connectivity is genuinely useful rather than a gimmick, which is why the Opal leads the category."},
                    {"title": "Costway Self-Dispensing Is the Value Nugget Pick", "body": "The Costway delivers the same chewable pellet format with a built-in dispenser at a notably lower price than the Opal. For households that love nugget ice but cannot justify the GE premium, it is the smart compromise that holds rank 2."},
                ],
            },
            "zh-tw": {
                "commentary": "夏天的高溫就是這個品類存在的全部理由，GE Profile Opal 2.0 穩坐第一、總分 9.1，因為它做出的冰是所有桌上型製冰機裡最好的，沒有之一。9.8 的冰質分代表的是真正 Sonic 風格的軟綿綿粒冰，就是那種大家會特地開車跨城去買的可咀嚼小冰粒，每天最多能做 24 磅，第一批大約十分鐘就好。讓它甩開所有對手的，是它的智慧功能是真的會被用到：透過 SmartHQ App 的 Wi-Fi 排程，可以在離峰時段整晚製冰，起床就有滿滿一桶，還能設定低冰量提醒、出門前遠端確認家裡的冰夠不夠招待客人。對夏天請客來說，這是真有用，不是裝飾性的連網功能。\n\n第二名 Costway 自動出冰款是性價比粒冰選擇，一樣的可咀嚼小冰粒、內建出冰口，價格比 Opal 親民不少。對喜歡粒冰但覺得 GE 溢價下不了手的家庭，這是聰明的折衷。\n\n第三名 Hamilton Beach 86150 是快速塊冰的主力機，給在意產量和速度勝過粒冰口感的人，子彈冰出得又快又多，冰桶、派對都好用。第四名 Chefman Iceman Compact 是小體積選擇，適合狹窄檯面和露營車；第五名 Euhomy Luna Pro 補齊榜單。隨著氣溫往上爬、後院聚會在六月越來越多，桌上型製冰機是夏天最默默提升生活品質的採購之一，而 Opal 2.0 就是那台要被超越的標竿。",
                "highlights": [
                    {"title": "GE Profile Opal 2.0 做出最好的粒冰", "body": "9.8 冰質分代表真正 Sonic 風格軟粒冰，每天最多 24 磅，第一批約十分鐘好。就是大家特地去買的可咀嚼小冰粒，桌上型對手在口感和產量上都比不上。"},
                    {"title": "SmartHQ 排程在夏天真有價值", "body": "Wi-Fi 排程可讓 Opal 在離峰整晚製冰、設低冰量提醒、出門前遠端查冰量。夏天請客這份連網是真有用而非噱頭，這正是 Opal 領先整個品類的原因。"},
                    {"title": "Costway 自動出冰是性價比粒冰選擇", "body": "Costway 用一樣的可咀嚼小冰粒加內建出冰口，價格比 Opal 親民不少。喜歡粒冰但下不了手付 GE 溢價的家庭，這是穩居第二的聰明折衷。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK portable-ice-makers")


if __name__ == "__main__":
    build_air_fryers()
    build_coffee_makers()
    build_dishwashers()
    build_rice_cookers()
    build_gas_grills()
    build_outdoor_griddles()
    build_portable_ice_makers()
    print("Batch 3 complete")
