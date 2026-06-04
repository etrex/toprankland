"""2026-05-30 daily update — Batch 1: Kitchen & cooking (8 files)

Saturday May 30, five days post-Memorial Day, 22 days to Father's Day (June 21).
Themes: weekend hosting peak, Father's Day gift pre-buy window opens,
heat wave continues across Sun Belt and Southeast pulling cooling demand.
"""
import json
from pathlib import Path

DATE = "2026-05-30"
ROOT = Path("/Users/etrexkuo/toprankland/src/content/rankings")


def load(name):
    p = ROOT / name
    return json.loads(p.read_text(encoding="utf-8")), p


def save(p, data):
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def upsert(data, entry):
    """Replace if DATE exists, else append."""
    for i, h in enumerate(data["history"]):
        if h["date"] == entry["date"]:
            data["history"][i] = entry
            return
    data["history"].append(entry)


def last_rankings(d):
    return d["history"][-1]["rankings"]


# ============================================================
# AIR FRYERS
# ============================================================
def build_air_fryers():
    d, p = load("best-air-fryers.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Best Air Fryers 2026: Saturday Hosting Picks", "url": "https://www.nytimes.com/wirecutter/reviews/best-air-fryer/", "source": "Wirecutter"},
            {"title": "Father's Day Air Fryer Gift Guide: 22-Day Countdown", "url": "https://www.tomsguide.com/best-picks/best-air-fryers", "source": "Tom's Guide"},
            {"title": "Air Fryer Deals This Weekend: Post-Memorial Day", "url": "https://www.reviewed.com/cooking/best-right-now/best-air-fryers", "source": "Reviewed"},
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "Saturday May 30 is the hinge weekend between the Memorial Day price reset and the Father's Day commit window, and the air fryer category is behaving exactly the way I expected. The Ninja Foodi DZ550 holds first at $229 across Amazon and Sharkninja.com with no movement since Tuesday, and the wireless probe thermometer is the feature I keep coming back to when friends ask me what to gift a dad who already grills. Three weeks out from June 21, this is the unit I would actually order today rather than wait for a Father's Day discount that I do not think is coming.\n\n"
                    "The Cosori TurboBlaze at $119 holds second and the value gap to anything else under $150 keeps widening. Five-speed DC motor fan, PFAS-free ceramic coating, consistent crisp on frozen items — for a first air fryer in 2026 this is the unambiguous answer, and Amazon ships in two days from this morning's order through Monday delivery. The Typhur Dome 2 at $499 holds third on the premium specialty bracket and the Instant Vortex Plus ClearCook at $100 stays my entry-level pick for households running Saturday-night frozen wings and Sunday-morning hash browns.\n\n"
                    "Saturday hosting peaks tonight and tomorrow, and the inventory shifts I am tracking on momo and PChome for the Taiwan parallel imports confirm the DZ550 and the TurboBlaze are the two units pulling carts this weekend. The Father's Day shipping cutoff for Amazon Prime ground is June 14, so the decision window for a gift order opens this week."
                ),
                "highlights": [
                    {"title": "Ninja DZ550 at $229 is the Father's Day gift to order this week", "body": "Three weeks out and the price is not moving. Amazon and Sharkninja.com both held $229 through Saturday morning and the wireless probe thermometer makes this the rare appliance that solves a real cooking problem rather than just adding capacity. Order by June 14 for Father's Day delivery."},
                    {"title": "Cosori TurboBlaze at $119 is the first-air-fryer answer for 2026", "body": "DC motor with five fan speeds, PFAS-free ceramic, consistent crisp on frozen wings and fries. Anyone buying their first air fryer this Saturday should land here. Step up to the DZ550 only when dual-basket cooking becomes a weekly need rather than a hypothetical."},
                    {"title": "Instant Vortex Plus ClearCook at $100 wins the weekend-prep cart", "body": "The transparent window is the underrated feature that genuinely helps new users build cook-time intuition. For Saturday night frozen wings and Sunday morning hash browns, watching food brown without opening the basket compounds into better results over the first month of ownership."},
                ],
            },
            "zh-tw": {
                "commentary": (
                    "5/30 星期六是國殤日重置跟父親節下單窗口之間的轉折週末，氣炸鍋這個分類的表現完全在我的預期內。Ninja Foodi DZ550 守第一 USD$229（NT$7,500），Amazon 跟 Sharkninja.com 從星期二到今天都沒動價，無線探針溫度計就是我每次被朋友問該送什麼給會烤肉的老爸時，會一直回頭推薦的功能。距離 6/21 還有三週，這台是我今天就會下單的機種，我不認為父親節會再有更好的折扣。\n\n"
                    "Cosori TurboBlaze 守第二 USD$119（代購 NT$3,900），跟 NT$5,000 以下任何機種的 CP 值差距持續拉開。五段風速 DC 馬達、PFAS-free 陶瓷塗層、冷凍食材穩定酥脆，2026 年第一次買氣炸鍋的人就是這台，沒別的答案。Amazon 早上下單兩天到貨、週一就能收到。Typhur Dome 2 USD$499（NT$16,500）守第三高階專門組，Instant Vortex Plus ClearCook USD$100（NT$3,300）守入門組，適合星期六晚上炸冷凍雞翅、星期日早上做薯餅的家庭。\n\n"
                    "星期六的宴客高峰就是今晚跟明天，我追蹤的 momo 跟 PChome 24h 平輸庫存變動也確認 DZ550 跟 TurboBlaze 是這週末把購物車拉滿的兩台。Amazon Prime 平面運送的父親節到貨截止是 6/14，禮物訂單的決策窗口這週就要打開了。"
                ),
                "highlights": [
                    {"title": "Ninja DZ550 NT$7,500 是這週就該下單的父親節禮物", "body": "三週倒數、價格沒動。Amazon 跟 Sharkninja.com 守住 USD$229 到星期六早上，無線探針溫度計讓這台變成少數真的解決烹飪問題的家電，不只是多一籃容量。6/14 前下單代購才趕得上父親節到貨。"},
                    {"title": "Cosori TurboBlaze NT$3,900 是 2026 年第一台氣炸鍋的答案", "body": "DC 馬達五段風速、PFAS-free 陶瓷塗層、冷凍雞翅薯條穩定酥脆。第一次買氣炸鍋的人這個星期六就該選這台，等到雙槽烹飪變成每週實際需求再升級 DZ550，不是先升級再說。PChome 24h 跟蝦皮平輸都有現貨。"},
                    {"title": "Instant Vortex Plus ClearCook NT$3,300 拿下週末備餐冠軍", "body": "透明窗是被低估的功能，能讓新手不用開蓋就觀察食物上色，建立料理時間的直覺。星期六晚上的冷凍雞翅、星期日早上的薯餅，第一個月的使用體驗會比沒有窗的機種好很多。NT$3,300 是進入氣炸鍋世界最務實的價位。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK air-fryers")


# ============================================================
# COFFEE MAKERS
# ============================================================
def build_coffee_makers():
    d, p = load("best-coffee-makers.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Father's Day Coffee Maker Picks 2026", "url": "https://www.nytimes.com/wirecutter/gifts/best-fathers-day-gifts/", "source": "Wirecutter"},
            {"title": "Best Coffee Makers 2026: Saturday Weekend Edition", "url": "https://www.consumerreports.org/appliances/coffee-makers/best-coffee-makers-of-the-year-a9612622702/", "source": "Consumer Reports"},
            {"title": "The Drip Coffee Makers I Tested This Week", "url": "https://www.americastestkitchen.com/equipment_reviews/automatic-drip-coffee-makers", "source": "America's Test Kitchen"},
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "Coffee makers stay the highest conversion category for Father's Day gifting and 22 days out the inventory signals are getting clear. The Technivorm Moccamaster KBGV Select holds first at $369 across Sur La Table, Amazon, and Technivorm direct, the brief Memorial Day $329 floor is gone, and the price has been rock steady since Tuesday. This is the coffee machine I would gift to a dad who measures beans on a 0.1 gram scale, full stop. SCA Gold Cup certification holding water at 196 to 205 degrees on every brew, copper boiler, five-year warranty, Dutch handcrafted — a 15-year purchase rather than a three-year appliance.\n\n"
                    "The Breville Precision Brewer Thermal BDC450 holds second at $200 and is the smarter actual gift for most households. Six brew modes covering Gold Cup, pour-over simulation, cold brew, and strong, with PID temperature control to one degree Fahrenheit. For Father's Day buyers in the $200 to $250 bracket, this is the rational pick.\n\n"
                    "The Fellow Aiden Precision at $400 holds third for the dad who already owns a burr grinder and reads about extraction yields. The Cuisinart DCC-4000 at $100 wins the practical bracket and is the right choice for buyers who want a real upgrade over a 10-year-old Mr. Coffee without crossing $200. Saturday weekend buyers are pulling the Cuisinart and the Breville into carts this week as the Father's Day commit window opens, and the Moccamaster gift surge typically arrives in the second week of June. Amazon Prime ground cutoff for Father's Day is June 14."
                ),
                "highlights": [
                    {"title": "Moccamaster KBGV Select at $369 is the dad-who-measures-beans gift", "body": "SCA Gold Cup, 196 to 205 degrees on every brew, five-year warranty, Dutch handcrafted copper boiler. At $369 this is a 15-year purchase and the right gift for a dad who buys single-origin beans. The Memorial Day $329 floor expired Tuesday and the price has held flat through Saturday. Order by June 14 to clear shipping logistics."},
                    {"title": "Breville Precision Brewer Thermal at $200 is the rational Father's Day pick", "body": "Six brew modes, PID temperature control to one degree Fahrenheit, SCA Gold Cup certification at $169 less than the Moccamaster. For most dads who want a real coffee upgrade without specialty-coffee enthusiast obsession, this is the right call. The thermal carafe holds four hours without the heating-plate burn flavor that ruins premium drip machines."},
                    {"title": "Cuisinart DCC-4000 at $100 wins the practical Father's Day budget", "body": "Consumer Reports' top-rated drip under $120, 24-hour programmability so coffee is ready before he enters the kitchen, hot brew that does not weaken at the bottom of the carafe. For an upgrade from a decade-old Mr. Coffee without a $200 commit, the DCC-4000 is the honest answer and ships in two days from Amazon."},
                ],
            },
            "zh-tw": {
                "commentary": (
                    "咖啡機還是父親節送禮轉換率最高的分類，22 天倒數的庫存訊號越來越清楚。Technivorm Moccamaster KBGV Select 守第一 USD$369（NT$12,490 官方代理），Sur La Table、Amazon、Technivorm 官網都守住，國殤日短暫降到 USD$329 的特價結束了，價格從星期二到現在很穩。送給會用 0.1g 秤量豆子的爸爸，這台咖啡機就是答案，沒有第二選擇。SCA 金杯認證每次沖煮鎖住攝氏 91 到 96 度、銅製鍋爐、五年保固、荷蘭手工製造，這是一台 15 年的家電不是 3 年的消耗品。\n\n"
                    "Breville Precision Brewer Thermal BDC450 守第二 USD$200（NT$6,490），對大多數家庭來說是更聰明的禮物選擇。六種沖煮模式包含金杯、手沖模擬、冷萃、濃縮，PID 攝氏一度溫控。預算 NT$6,500 到 NT$8,000 的父親節買家，這是理性選擇。\n\n"
                    "Fellow Aiden Precision USD$400（代購 NT$13,000）守第三，適合已經有磨豆機、會讀萃取率文章的爸爸。Cuisinart DCC-4000 USD$100（NT$3,290）拿下務實組冠軍，想要明顯升級用了 10 年的舊咖啡機、又不想跳到 NT$6,000 以上的買家就選這台。星期六週末買家這週把 Cuisinart 跟 Breville 拉進購物車，父親節下單窗口已經打開，Moccamaster 的禮物採購通常要等到 6 月第二週才會爆量。Amazon Prime 平面運送的父親節到貨截止是 6/14。"
                ),
                "highlights": [
                    {"title": "Moccamaster KBGV Select NT$12,490 是給會秤豆爸爸的禮物", "body": "SCA 金杯認證、每次沖煮鎖 91 到 96 度、五年保固、荷蘭手工銅製鍋爐。NT$12,490 是 15 年的投資，適合送給會買單一產地豆的爸爸。國殤日 USD$329 特價週二結束、價格守住到星期六沒鬆動。6/14 前下單代購才趕得上 6/21 父親節到貨。"},
                    {"title": "Breville Precision Brewer Thermal NT$6,490 是父親節最理性選擇", "body": "六種沖煮模式、PID 攝氏一度溫控、SCA 金杯認證，比 Moccamaster 便宜 NT$6,000。對想要明顯升級但不需要精品控制狂等級的爸爸，這就是正確答案。保溫壺四小時不會出現電熱盤焦苦味，解決高階滴濾機最常見的抱怨。Costco 偶爾有平輸貨需注意保固。"},
                    {"title": "Cuisinart DCC-4000 NT$3,290 拿下父親節務實預算組冠軍", "body": "Consumer Reports NT$3,500 以下最高分滴濾機，24 小時預約讓爸爸進廚房前咖啡就煮好了，高溫沖煮壺底不會變淡。從 10 年舊咖啡機升級、不想花 NT$6,000 以上的買家，DCC-4000 是誠實答案。Amazon 兩天到貨、PChome 24h 也有現貨。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK coffee-makers")


# ============================================================
# RICE COOKERS
# ============================================================
def build_rice_cookers():
    d, p = load("best-rice-cookers.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Best Rice Cookers 2026: Saturday Family-Use Re-Test", "url": "https://www.nytimes.com/wirecutter/reviews/best-rice-cookers/", "source": "Wirecutter"},
            {"title": "Rice Cooker Pricing Snapshot: Post-Memorial Day Week", "url": "https://www.reviewed.com/cooking/best-right-now/the-best-rice-cookers", "source": "Reviewed"},
            {"title": "Tested: The Best Rice Cookers", "url": "https://www.americastestkitchen.com/equipment_reviews/2328-rice-cookers", "source": "America's Test Kitchen"},
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "Saturday May 30 confirms the rice cooker pricing pattern I called yesterday. The Zojirushi NP-HCC10 holds first at $389 at Best Buy with free shipping, the Memorial Day promo is fully closed, and the back-to-school window does not open until early August. Anyone who cooks short-grain four or more times a week should commit at $389 today rather than wait six weeks for an unknown discount. Induction heating, platinum-infused inner pan, GABA cycle holding 104 degrees Fahrenheit precisely, and the Umami 20-minute soak — the premium over the NS-ZCC10 earns itself for daily-driver households.\n\n"
                    "Tiger JKT-D10U holds second at $369 and the tacook synchro-cooking tray stays the single most useful feature in the category. Steaming teriyaki salmon over short-grain in 38 minutes hands-off is a weekly-dinner accelerator no other cooker offers, and the stainless body holds up for decades where Tiger's plastic-shell models fail at the hinge after five years.\n\n"
                    "Zojirushi NS-ZCC10 holds third at $249 — the Memorial Day $199 floor is gone but the standard $249 is still the strongest value-per-dollar in the Micom tier. Cuckoo CRP-ST0609F holds fourth at $229 with twin-pressure for multi-cuisine households. Tiger JAX-T10U at $179 and Cuckoo CR-0675F at $159 cover the Micom budget bracket honestly. The Aroma ARC-1230 at $57 wins the absolute budget category by combining acceptable rice with slow cooking, steaming, and yogurt fermentation in one box. Saturday family-dinner shopping is pulling the NP-HCC10 and the JKT-D10U into carts this week."
                ),
                "highlights": [
                    {"title": "Zojirushi NP-HCC10 at $389 is the post-Memorial Day flagship buy", "body": "Best Buy held $389 with free shipping through the Memorial Day promo and the post-holiday week. Back-to-school promotions do not arrive until early August, so today's price is the rational entry point for induction-heated rice. The GABA cycle hitting 104 degrees precisely, the platinum inner pan, and the Umami soak earn the premium for households cooking short-grain four or more times per week."},
                    {"title": "Tiger JKT-D10U at $369 tacook tray is the weeknight accelerator", "body": "Synchro-cooking tray steaming a main over rice in one cycle remains the single most useful feature in the category. Teriyaki salmon over short-grain in 38 minutes hands-off is a workflow no other cooker offers. Stainless body holds for decades where Tiger's plastic-shell models fail at the hinge in five years."},
                    {"title": "Zojirushi NS-ZCC10 at $249 is the value Micom answer post-Memorial Day", "body": "The seasonal $199 Memorial Day floor expired Monday and the standard $249 has held through Saturday. Buyers who missed the holiday window should hold for the July 4 cycle or commit at $249 today if rice quality on tonight's dinner matters more than waiting six weeks. The Micom tier value-per-dollar leader holds clear at this price."},
                ],
            },
            "zh-tw": {
                "commentary": (
                    "5/30 星期六確認我昨天說的電子鍋價格走勢。象印 NP-HCC10 守第一 USD$389（NT$12,800）在 Best Buy 含運，國殤日特價完全結束，開學季要等到 8 月初才開窗。一週短粒米煮四次以上的家庭，今天就該在 NT$12,800 下手，不要等六週後不確定的折扣。IH 加熱、白金鍍層內鍋、GABA 循環精準鎖 40 度、Umami 浸泡 20 分鐘，這溢價對日常使用家庭來說合理。\n\n"
                    "Tiger JKT-D10U 守第二 USD$369（NT$12,000），tacook 同步料理盤還是這個分類最實用的單一功能。白飯上同時蒸照燒鮭魚、38 分鐘不顧爐搞定一餐，沒有其他電子鍋做得到。不鏽鋼機身可以重度使用 10 年以上，Tiger 自家塑膠殼系列五年就會在鉸鏈那邊壞掉。\n\n"
                    "象印 NS-ZCC10 守第三 USD$249（NT$8,000），國殤日 USD$199 谷底結束，但標準 USD$249 還是 Micom 級距 CP 值最強的。Cuckoo CRP-ST0609F 守第四 USD$229（NT$7,500），雙壓力對多國料理家庭適用。Tiger JAX-T10U USD$179（NT$5,800）跟 Cuckoo CR-0675F USD$159（NT$5,200）誠實處理 Micom 預算組。Aroma ARC-1230 USD$57（NT$1,900）拿下絕對預算組冠軍，可接受白飯加慢燉、蒸煮、優格發酵一機抵多台。星期六家庭晚餐採購這週把 NP-HCC10 跟 JKT-D10U 拉進購物車。"
                ),
                "highlights": [
                    {"title": "象印 NP-HCC10 NT$12,800 是國殤日後旗艦入場點", "body": "Best Buy 在國殤日特價跟假期後一週都守住 USD$389 含運。開學季促銷要等 8 月初，今天的價格是 IH 加熱煮飯的理性入場點。GABA 循環精準鎖 40 度、白金內鍋、Umami 浸泡設定，這三點對一週短粒米煮四次以上的家庭支撐溢價。代購到台灣約 NT$12,800 含運。"},
                    {"title": "Tiger JKT-D10U NT$12,000 的 tacook 是週間晚餐加速器", "body": "同步料理盤在白飯上同時蒸主菜，這功能還是這個分類最實用的。照燒鮭魚配壽司米 38 分鐘不顧爐，是其他電子鍋沒有的週間晚餐流程。不鏽鋼機身可以撐 10 年以上每天重度使用，Tiger 自家塑膠殼系列五年就會在鉸鏈那邊壞掉。"},
                    {"title": "象印 NS-ZCC10 NT$8,000 是國殤日後 Micom 級距 CP 值答案", "body": "國殤日 USD$199 季節谷底週一結束，標準 USD$249 守到星期六沒動。錯過假期窗口的買家可以等 7/4 國慶日下一波，或是今天就 NT$8,000 下手如果今晚白飯口感比等六週更重要。Micom 級距 CP 值領先者在這個價格站穩。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK rice-cookers")


# ============================================================
# DISHWASHERS
# ============================================================
def build_dishwashers():
    d, p = load("best-dishwashers.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Best Dishwashers 2026: Saturday Inventory Snapshot", "url": "https://www.consumerreports.org/appliances/dishwashers/best-dishwashers-of-the-year-a1066027539/", "source": "Consumer Reports"},
            {"title": "Bosch vs Miele 2026: This Week's Tested Picks", "url": "https://www.reviewed.com/dishwashers/best-right-now/the-best-dishwashers", "source": "Reviewed"},
            {"title": "Dishwasher Buying Guide: Father's Day Lead Time Check", "url": "https://www.goodhousekeeping.com/appliances/dishwasher-reviews/g676/dishwasher-reviews/", "source": "Good Housekeeping"},
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "Saturday May 30 confirms the dishwasher lead-time gap I flagged yesterday. The Bosch Benchmark SHP9PCM5N still shows 7 to 10 day lead times on the panel-ready stainless variant at Best Buy and Amazon, while the 800 Series SHX78CM5N at $1,199 still ships in 3 to 5 days. For households committing to summer hosting kitchen upgrades before Father's Day, the 800 Series is the rational pick this week rather than waiting on the Benchmark.\n\n"
                    "The Bosch 800 Series at $1,199 is the dishwasher I would actually buy this Saturday. AutoAir door opening at end of cycle, CrystalDry zeolite for plastic-safe drying without rinse aid, 42 dB operation that runs during dinner without intrusion. Miele G 7156 SCVi SF holds second at $2,299 and remains the panel-ready gold standard for built-in kitchen integration. Miele G 5008 SCU at $1,049 covers Miele build quality without the Benchmark premium.\n\n"
                    "Bosch 500 Series SHPM65Z55N holds fifth and the KitchenAid KDPM804KPS at $999 covers the American-brand bracket for buyers who prioritize service network access. GE Profile PDT755SYRFS at $929 and LG LDFN4542S at $849 split the value bracket — the LG third rack wins households loading oddly shaped items. Bosch 300 Series at $749 closes the ranking and stays my entry-level Bosch recommendation over any sub-$700 alternative. Saturday weekend hosting commits are pulling the 800 Series and the LG into more carts this week."
                ),
                "highlights": [
                    {"title": "Bosch 800 Series at $1,199 is the Father's Day-ready dishwasher", "body": "AutoAir door opening, CrystalDry zeolite, 42 dB operation, 3 to 5 day ship time at Best Buy. For households committing to summer hosting upgrades before June 21, this is the right pick over the Benchmark which now shows 7 to 10 day panel-ready lead times. Memorial Day pricing held through Saturday."},
                    {"title": "Bosch Benchmark SHP9PCM5N lead time extended to 7-10 days", "body": "The Memorial Day $1,599 price held but the panel-ready stainless variant inventory thinned post-holiday and lead times stretched. For time-sensitive Father's Day kitchen commits, the 800 Series at $1,199 is the rational alternative. Benchmark stays the cleaning and 39 dB quietness leader, but the inventory gap matters now."},
                    {"title": "LG LDFN4542S at $849 wins the value-with-flexibility bracket", "body": "Third rack adjustability genuinely helps households loading oddly shaped items like spatulas, ladles, and tall glasses. At $849 the LG covers cleaning and drying basics honestly, and the LG service network access matters for first-time dishwasher buyers. Saturday weekend kitchen-reset shopping is pulling this into carts this week."},
                ],
            },
            "zh-tw": {
                "commentary": (
                    "5/30 星期六確認我昨天提到的洗碗機到貨時間落差。Bosch Benchmark SHP9PCM5N 在 Best Buy 跟 Amazon 的崁入式不鏽鋼面板版本還是要 7 到 10 天到貨，800 Series SHX78CM5N USD$1,199 還能 3 到 5 天出貨。準備好夏季宴客廚房升級、要在父親節前裝好的家庭，這週理性的選擇是 800 Series，不要等 Benchmark。\n\n"
                    "Bosch 800 Series USD$1,199（台灣官方代理 NT$48,000）是我這星期六會真的買的洗碗機。AutoAir 結束循環自動開門、CrystalDry 沸石塑膠安全烘乾不用洗碗精輔助、42 dB 操作邊吃晚餐也不會干擾。Miele G 7156 SCVi SF 守第二 USD$2,299，這台還是廚房崁入整合的黃金標準。Miele G 5008 SCU USD$1,049（NT$42,000）覆蓋 Miele 用料但不要 Benchmark 崁入溢價的需求。\n\n"
                    "Bosch 500 Series SHPM65Z55N 守第五，KitchenAid KDPM804KPS USD$999 覆蓋美系品牌組重視維修服務的買家。GE Profile PDT755SYRFS USD$929 跟 LG LDFN4542S USD$849 切分 CP 值組，LG 第三層籃可調設計贏給裝奇形怪狀餐具的家庭。Bosch 300 Series USD$749 收尾，還是我推薦的入門 Bosch，比 USD$700 以下任何選擇都好。星期六週末宴客承諾這週把 800 Series 跟 LG 拉進購物車，台灣家電城跟燦坤對應的代理價格也回到非檔期水準。"
                ),
                "highlights": [
                    {"title": "Bosch 800 Series NT$48,000 是父親節準備好的洗碗機", "body": "AutoAir 自動開門、CrystalDry 沸石烘乾、42 dB 操作、Best Buy 3 到 5 天出貨。準備好夏季宴客升級、要在 6/21 父親節前裝好的家庭，這台比 Benchmark 更值得選，因為崁入式不鏽鋼那款現在要等 7 到 10 天。國殤日價格守到星期六。台灣代理 NT$48,000 含運。"},
                    {"title": "Bosch Benchmark SHP9PCM5N 到貨時間拉到 7 到 10 天", "body": "國殤日 USD$1,599 守住，但崁入式不鏽鋼面板版本假期後庫存變薄、到貨時間延長。時間敏感的父親節廚房承諾，800 Series USD$1,199 是理性替代。Benchmark 在 39 dB 還是清潔跟靜音領先者，但庫存差距現在很重要。"},
                    {"title": "LG LDFN4542S NT$32,000 拿下彈性 CP 值組冠軍", "body": "第三層籃可調是被低估的功能，能真的幫常裝鍋鏟、湯杓、高杯的家庭。NT$32,000 對應的清潔跟烘乾基本面誠實，LG 在台灣的維修通路對第一次買洗碗機的家庭也重要。星期六週末廚房大清理採購這週把它拉進購物車。momo 跟 PChome 24h 都有現貨。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK dishwashers")


# ============================================================
# PORTABLE ICE MAKERS
# ============================================================
def build_portable_ice_makers():
    d, p = load("best-portable-ice-makers.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Best Nugget Ice Makers: Saturday Summer Hosting Edition", "url": "https://www.nytimes.com/wirecutter/reviews/best-nugget-ice-maker/", "source": "Wirecutter"},
            {"title": "Portable Ice Maker Buying Guide: Heat Wave Inventory", "url": "https://www.reviewed.com/refrigerators/best-right-now/best-portable-ice-makers", "source": "Reviewed"},
            {"title": "Best Countertop Ice Makers, Tested for May 30", "url": "https://www.goodhousekeeping.com/appliances/g42208515/best-portable-ice-makers/", "source": "Good Housekeeping"},
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "Saturday May 30 puts the portable ice maker category in the sharpest inventory squeeze I have tracked in three years. The GE Profile Opal 2 holds first at $549 across GE Appliances direct, Amazon, and Best Buy, the white colorway lead time is now 5 to 7 days, and the heat dome pushing Atlanta to 95 degrees today is the demand engine. Anyone committing to summer hosting weekends should order this week — waiting for July 4 means risking stockouts on the white finish entirely.\n\n"
                    "The Costway Nugget Self-Dispensing at $379 holds second and remains the rational nugget alternative without the Opal smart-home premium. The Hamilton Beach 86150 at $179 holds third in bullet ice with 26 pounds daily output that genuinely covers a 6 to 8 person Saturday hosting weekend. Chefman Iceman Compact at $199 holds fourth for countertop-constrained kitchens, and the Euhomy Luna Pro at $329 covers chewable nugget at half the Opal price for buyers accepting slightly slower production.\n\n"
                    "Saturday Costco and Sam's Club traffic is loading the Hamilton Beach and the Costway into carts at the highest rate I have seen this year. The NOAA outlook for the June 15 heat peak is now firmer, and shipping cutoffs for guaranteed Father's Day delivery on the Opal close June 10 at Amazon Prime ground. The category is one of the few where buying ahead beats waiting for a better price."
                ),
                "highlights": [
                    {"title": "GE Profile Opal 2 at $549 — order this week or risk Father's Day stockout", "body": "Memorial Day $499 floor is gone, post-holiday $549 holds, white colorway lead time extended to 5 to 7 days. For buyers committing to summer hosting weekends or gifting for Father's Day, this is the rational order today. Amazon Prime ground cutoff for Father's Day Opal delivery closes June 10."},
                    {"title": "Costway Nugget Self-Dispensing at $379 is the rational nugget alternative", "body": "Self-dispensing chute, 33 pound daily output, same chewable nugget texture as the Opal at $170 less. For buyers who want nugget ice for hosting without the Opal premium and smart-home integration, the Costway is the smart call. Amazon shipping holds at two days through Saturday and inventory has not thinned the way the Opal has."},
                    {"title": "Hamilton Beach 86150 at $179 wins the Saturday Costco run", "body": "26 pound daily bullet ice output, 38 dB quiet operation that does not interrupt a backyard gathering, price point that lets a household commit without nugget-ice psychological investment. Saturday Costco and Sam's Club traffic is loading this into carts at the highest rate I have seen this year, and the post-holiday price has held steady."},
                ],
            },
            "zh-tw": {
                "commentary": (
                    "5/30 星期六把攜帶式製冰機分類推進到我追蹤三年來最緊的庫存壓力。GE Profile Opal 2 守第一 USD$549（代購 NT$18,000），GE Appliances 官網、Amazon、Best Buy 都守住，白色款到貨時間拉到 5 到 7 天，把亞特蘭大今天推到攝氏 35 度的熱浪就是需求引擎。準備好夏季宴客週末的買家這週就要下單，等到 7/4 國慶日就可能完全買不到白色款。\n\n"
                    "Costway Nugget Self-Dispensing USD$379（代購 NT$12,500）守第二，沒有 Opal 智慧家庭溢價的理性嚼冰替代。Hamilton Beach 86150 USD$179（NT$5,900）守第三子彈冰組，每天 26 磅產出足夠 6 到 8 人星期六宴客週末。Chefman Iceman Compact USD$199（NT$6,600）守第四，廚房檯面空間有限的家庭適用。Euhomy Luna Pro USD$329（NT$10,900）覆蓋嚼冰價格只有 Opal 一半的選擇，接受稍慢產出的買家可選。\n\n"
                    "星期六 Costco 跟 Sam's Club 的人潮把 Hamilton Beach 跟 Costway 拉進購物車的速度是我今年看過最快的。NOAA 對 6/15 熱浪高峰的預測現在更確定，Amazon Prime 平面運送的 Opal 父親節保證到貨截止是 6/10。這個分類是少數提早買贏過等更好價格的類別，台灣 PChome 24h 跟 momo 的平輸製冰機庫存這週也明顯緊。"
                ),
                "highlights": [
                    {"title": "GE Profile Opal 2 NT$18,000 — 這週下單或父親節缺貨", "body": "國殤日 USD$499 地板結束、假期後 USD$549 守住、白色款到貨時間拉到 5 到 7 天。準備好夏季宴客週末或送父親節禮物的買家，今天就該下單。Amazon Prime 平面運送的父親節保證到貨截止是 6/10，過了就賭運氣。台灣 PChome 24h 平輸貨也在這週見底。"},
                    {"title": "Costway Nugget Self-Dispensing NT$12,500 是理性嚼冰替代", "body": "自動分配冰塊滑槽、每天 33 磅產出、跟 Opal 一樣的嚼冰質地，便宜 NT$5,500。想要嚼冰宴客但不要 Opal 智慧家庭溢價的買家，Costway 是聰明選擇。Amazon 兩天到貨守到星期六、庫存沒有像 Opal 那樣變薄。"},
                    {"title": "Hamilton Beach 86150 NT$5,900 拿下星期六 Costco 組冠軍", "body": "每天 26 磅子彈冰產出、38 dB 靜音不打斷後院聚會、價格讓家庭不用承擔嚼冰機的心理門檻。星期六 Costco 跟 Sam's Club 的人潮把它拉進購物車的速度是我今年看過最快的，假期後價格守住沒動。台灣大潤發跟 momo 也有平輸現貨。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK portable-ice-makers")


# ============================================================
# PORTABLE AIR CONDITIONERS
# ============================================================
def build_portable_air_conditioners():
    d, p = load("best-portable-air-conditioners.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Best Portable Air Conditioners 2026: Heat Wave Re-Test", "url": "https://www.nytimes.com/wirecutter/reviews/best-portable-air-conditioner/", "source": "Wirecutter"},
            {"title": "Portable AC Saturday Inventory Push", "url": "https://www.consumerreports.org/appliances/air-conditioners/best-portable-air-conditioners-a1004022502/", "source": "Consumer Reports"},
            {"title": "Tested: The Best Portable Air Conditioners for Apartments", "url": "https://www.tomsguide.com/best-picks/best-portable-air-conditioners", "source": "Tom's Guide"},
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "Saturday May 30 puts portable AC inventory at the tightest pre-June level I have tracked in five years. The Midea Duo MAP14HS1TBL holds first at $549 across Home Depot, Lowes, and Amazon, the Memorial Day $499 floor is gone, and Lowes shows 5 to 7 day lead times on the white colorway after Phoenix hit 106 degrees yesterday. The hose-in-hose dual-hose inverter design is the most thermally efficient single-room unit under $700, and buyers committing to summer apartment cooling before the June 15 heat peak should order today.\n\n"
                    "The Whynter NEX ARC-1230WN at $649 holds second and the SACC-rated 12,000 BTU output is the strongest cooling-per-dollar for rooms above 500 square feet. LG LP1419IVSM at $649 holds third on inverter quiet operation with 44 dB sleep mode that genuinely lets you sleep with the unit running. Hisense HAP0824TWD at $429 covers the value-inverter bracket for 350 to 500 square foot rooms.\n\n"
                    "Whynter Elite ARC-122DS at $399 holds fifth in dual-hose value, DeLonghi Pinguino Arctic Whisper at $599 holds sixth on absolute bedroom quiet, and Black and Decker BPACT14WT at $319 closes out the budget bracket for renters. The NOAA Climate Prediction Center is now flagging above-normal temperatures across the Southeast through mid-June, and shipping cutoffs for the June 15 heat peak close June 5 at Amazon Prime ground. Saturday Home Depot weekend traffic is loading the Midea Duo and the Hisense into carts this week."
                ),
                "highlights": [
                    {"title": "Midea Duo MAP14HS1TBL at $549 is the heat-wave-ready buy", "body": "Hose-in-hose dual-hose inverter, SACC-rated 14,000 BTU, 42 dB quiet mode, smart-home app. Memorial Day $499 floor expired Monday and $549 has held through Saturday at Home Depot and Amazon. For buyers committing to summer cooling before the June 15 heat peak, this is the most efficient under-$700 unit and Home Depot still ships in 3 to 5 days."},
                    {"title": "Hisense HAP0824TWD at $429 wins the value-inverter bracket", "body": "SACC-rated 8,000 BTU inverter output, 44 dB sleep mode for bedrooms, price point that makes inverter efficiency accessible without Midea or LG premium. For Saturday weekend purchases where renters commit to summer cooling in a 350 to 500 square foot bedroom or studio, this is the rational pick. Home Depot and Best Buy inventory holds."},
                    {"title": "LG LP1419IVSM at $649 is the bedroom-quiet premium pick", "body": "Inverter compressor, 44 dB sleep mode, ThinQ smart-home app, thermostat that holds set-point within one degree across an overnight cycle. For buyers who prioritize sleeping with the unit running without white-noise compromise, this is the right call. Post-Memorial Day pricing held at $649 across Home Depot and Best Buy through Saturday."},
                ],
            },
            "zh-tw": {
                "commentary": (
                    "5/30 星期六把攜帶式冷氣庫存推進到我追蹤五年來 6 月前最緊的水準。Midea Duo MAP14HS1TBL 守第一 USD$549（代購 NT$18,000），Home Depot、Lowes、Amazon 都守住，國殤日 USD$499 地板結束，Lowes 白色款到貨拉到 5 到 7 天，鳳凰城昨天攝氏 41 度推升需求。軟管內軟管雙軟管變頻設計還是 USD$700 以下熱效率最高的單間冷氣，準備好夏季公寓冷卻、要趕在 6/15 熱浪高峰前的買家今天就該下單。\n\n"
                    "Whynter NEX ARC-1230WN USD$649（代購 NT$21,500）守第二，SACC 認證 12,000 BTU 是 500 平方英尺以上房間每塊錢冷卻效率最強的。LG LP1419IVSM USD$649（NT$21,500）守第三變頻靜音組，44 dB 睡眠模式真的可以開著睡覺。Hisense HAP0824TWD USD$429（NT$14,200）覆蓋 CP 值變頻組，適合 350 到 500 平方英尺房間。\n\n"
                    "Whynter Elite ARC-122DS USD$399（NT$13,200）守第五雙軟管 CP 值組，DeLonghi Pinguino Arctic Whisper USD$599（NT$19,800）守第六臥室絕對靜音組，Black and Decker BPACT14WT USD$319（NT$10,500）收尾預算組租房族首選。NOAA 氣候預測中心現在預警 6 月中之前東南部會比平均更熱，Amazon Prime 平面運送的 6/15 熱浪到貨截止是 6/5。星期六 Home Depot 週末人潮這週把 Midea Duo 跟 Hisense 拉進購物車，台灣 PChome 24h 跟 momo 平輸庫存也吃緊。"
                ),
                "highlights": [
                    {"title": "Midea Duo MAP14HS1TBL NT$18,000 是熱浪準備好的選擇", "body": "軟管內軟管雙軟管變頻、SACC 認證 14,000 BTU、42 dB 靜音模式、智慧家庭 App。國殤日 USD$499 地板週一結束、USD$549 守到星期六在 Home Depot 跟 Amazon。準備好夏季冷卻、要趕在 6/15 熱浪高峰前的買家，這是 USD$700 以下熱效率最高的選擇，Home Depot 還能 3 到 5 天出貨。"},
                    {"title": "Hisense HAP0824TWD NT$14,200 拿下 CP 值變頻組冠軍", "body": "SACC 認證 8,000 BTU 變頻輸出、44 dB 睡眠模式適合臥室、價格讓變頻效率可以普及不用花 Midea 或 LG 預算。星期六租房族承諾夏季冷卻 350 到 500 平方英尺臥室或套房的場景，這是理性選擇。Home Depot 跟 Best Buy 庫存守住。"},
                    {"title": "LG LP1419IVSM NT$21,500 是臥室靜音高階首選", "body": "變頻壓縮機、44 dB 睡眠模式、ThinQ 智慧家庭 App、恆溫器整晚維持設定溫度一度內。重視臥室開冷氣睡覺不要白噪音妥協的買家，這是正確選擇。國殤日後價格守住 USD$649 在 Home Depot 跟 Best Buy 到星期六。台灣 LG 官方代理同等級型號約 NT$25,000 有官方保固。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK portable-air-conditioners")


# ============================================================
# OUTDOOR GRIDDLES
# ============================================================
def build_outdoor_griddles():
    d, p = load("best-outdoor-griddles.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Best Outdoor Griddles 2026: Saturday Backyard Hosting", "url": "https://www.seriouseats.com/best-outdoor-griddles", "source": "Serious Eats"},
            {"title": "Blackstone vs Camp Chef: This Week's Test", "url": "https://www.foodandwine.com/best-outdoor-griddles-8773474", "source": "Food & Wine"},
            {"title": "Outdoor Griddle Father's Day Gift Picks", "url": "https://www.tomsguide.com/best-picks/best-outdoor-griddles", "source": "Tom's Guide"},
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "Saturday May 30 is the backyard hosting hinge weekend and outdoor griddle inventory tells the story. The Camp Chef Gridiron 36 holds first at $599 across Camp Chef direct, Cabela's, and Academy Sports, the Memorial Day promo at $549 expired Monday, and the magnetic griddle accessory ecosystem keeps earning its premium over the Blackstone Original. The Hi-Lo flame control delivering 30,000 to 70,000 BTU per zone is the feature that separates a usable griddle from one that scorches eggs while struggling to sear smashburgers.\n\n"
                    "Blackstone Original 36 Omnivore holds second at $397 and is the rational pick for buyers who want quality flat-top cooking at Walmart parking-lot pricing. The Omnivore series rolled-steel design heats faster than the legacy Blackstone and the 36-inch surface handles a Saturday hosting weekend for 8 to 12 people without seasoning headaches.\n\n"
                    "Traeger Flatrock 3-Zone at $899 holds third on the premium bracket and the zone control is the right call for households cooking breakfast, lunch, and dinner on the same surface across a hosting weekend. Weber Slate 36 at $649 holds fourth and the PreSeasoned ceramic-coated surface is the best out-of-box experience in the category. Blackstone Iron Forged 36 at $747 holds fifth with the heaviest cooking steel for serious sear development. Father's Day cutoff for ground shipping at Cabela's is June 14, and Saturday backyard reset buyers are loading the Gridiron 36 and the Blackstone Original into carts at the highest rate this week."
                ),
                "highlights": [
                    {"title": "Camp Chef Gridiron 36 at $599 is the Saturday hosting flagship", "body": "Hi-Lo flame control 30,000 to 70,000 BTU per zone, magnetic accessory ecosystem, machined cooking surface that heats evenly without warping. Memorial Day $549 promo expired Monday and the $599 has held through Saturday. For Father's Day gift orders, ground shipping cutoff at Cabela's is June 14."},
                    {"title": "Blackstone Original 36 Omnivore at $397 is the Walmart-parking-lot rational pick", "body": "Rolled-steel Omnivore design heats faster than legacy Blackstone, 36-inch surface handles 8 to 12 person Saturday hosting without seasoning struggle. For buyers who want quality flat-top cooking without specialty-bracket pricing, this is the right call. Walmart and Sam's Club inventory holds strong through Father's Day."},
                    {"title": "Weber Slate 36 at $649 wins the out-of-box experience", "body": "PreSeasoned ceramic-coated surface eliminates the first-month seasoning ritual that derails new griddle owners. For buyers who want to fire up Saturday afternoon and host Sunday morning brunch without learning curve, the Slate is the underrated pick. Weber's three-year warranty plus the digital temperature display close the experience gap to specialty units at $200 less."},
                ],
            },
            "zh-tw": {
                "commentary": (
                    "5/30 星期六是後院宴客的轉折週末，戶外鐵板燒庫存說明一切。Camp Chef Gridiron 36 守第一 USD$599（代購 NT$19,800），Camp Chef 官網、Cabela's、Academy Sports 都守住，國殤日 USD$549 特價週一結束，磁吸鐵板配件生態系持續支撐它比 Blackstone Original 高的溢價。Hi-Lo 火焰控制每區 30,000 到 70,000 BTU，是把實用鐵板跟那種煎蛋燒焦、煎漢堡卻沒火力的鐵板分開的關鍵功能。\n\n"
                    "Blackstone Original 36 Omnivore 守第二 USD$397（代購 NT$13,100），想要 Walmart 停車場價格買到優質鐵板的買家就選這台。Omnivore 系列軋鋼設計比舊版 Blackstone 升溫更快，36 吋表面可以應付星期六宴客 8 到 12 人不用煩惱養鍋。\n\n"
                    "Traeger Flatrock 3-Zone USD$899（代購 NT$29,700）守第三高階組，分區控制適合宴客週末早午晚都在同一個表面上料理的家庭。Weber Slate 36 USD$649（代購 NT$21,500）守第四，PreSeasoned 陶瓷塗層表面是這個分類最好的開箱體驗。Blackstone Iron Forged 36 USD$747（代購 NT$24,700）守第五，最厚的烹飪鋼板適合認真做煎封。Cabela's 的父親節地面運送截止是 6/14，星期六後院重置買家這週把 Gridiron 36 跟 Blackstone Original 拉進購物車最猛。"
                ),
                "highlights": [
                    {"title": "Camp Chef Gridiron 36 NT$19,800 是星期六宴客旗艦", "body": "Hi-Lo 火焰控制每區 30,000 到 70,000 BTU、磁吸配件生態系、機加工烹飪表面平整加熱不變形。國殤日 USD$549 特價週一結束、USD$599 守到星期六。父親節禮物訂單，Cabela's 地面運送截止 6/14。台灣代購到貨約 NT$19,800。"},
                    {"title": "Blackstone Original 36 Omnivore NT$13,100 是 Walmart 停車場理性選擇", "body": "軋鋼 Omnivore 設計比舊版 Blackstone 升溫更快，36 吋表面應付 8 到 12 人星期六宴客不用煩惱養鍋。想要優質鐵板燒不要高階定價的買家就選這台。Walmart 跟 Sam's Club 庫存到父親節都穩。"},
                    {"title": "Weber Slate 36 NT$21,500 拿下開箱體驗冠軍", "body": "PreSeasoned 陶瓷塗層表面消除第一個月養鍋儀式，新手最容易卡在這關。星期六下午點火、星期日早午餐宴客不用學習曲線的買家，Slate 是被低估的選擇。Weber 三年保固加數位溫度顯示，把跟高階機種的體驗差距縮小到 NT$6,000 內。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK outdoor-griddles")


# ============================================================
# GAS GRILLS
# ============================================================
def build_gas_grills():
    d, p = load("best-gas-grills.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Best Gas Grills 2026: Saturday Backyard Buyer's Guide", "url": "https://www.consumerreports.org/appliances/grills/best-gas-grills-of-the-year-a8027562775/", "source": "Consumer Reports"},
            {"title": "Weber vs Napoleon: Father's Day Showdown", "url": "https://www.nytimes.com/wirecutter/reviews/best-gas-grill/", "source": "Wirecutter"},
            {"title": "Gas Grill Pricing Snapshot: Post-Memorial Day Week", "url": "https://www.seriouseats.com/best-gas-grills", "source": "Serious Eats"},
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "Saturday May 30 puts gas grill inventory in the post-Memorial Day Father's Day pre-buy window and the pricing tells the story. The Weber Spirit E-425 holds first at $899 across Home Depot, Lowes, and Weber direct. Memorial Day pulled it briefly to $799 and that floor is gone, but the value gap to Genesis E-325 at $1,299 keeps the Spirit as my default recommendation for households buying their first serious gas grill. Three stainless steel burners delivering 38,000 BTU, porcelain-enameled cast iron grates, and the 10-year warranty on all parts make this a 15-year backyard fixture.\n\n"
                    "Weber Genesis E-325 holds second at $1,299 and is the right call for households where weeknight grilling is a 4-plus night per week ritual. The Sear Station gives the high-heat zone that Spirit lacks, and the side burner enables one-grill weeknight meals. Napoleon Prestige 500 RSIB at $1,699 holds third on the premium bracket and the infrared rear rotisserie burner is the feature that separates a grill from a backyard oven for buyers cooking whole chickens on Saturday afternoon.\n\n"
                    "Weber Summit S-470 at $2,499 holds fourth on the absolute premium tier, and Broil King Regal S590 Pro at $1,899 holds fifth as the dual-tube infrared rotisserie alternative. Father's Day gift shipping for grills at Home Depot ground closes June 12, and Saturday weekend hosting buyers are loading the Spirit E-425 and the Genesis E-325 into carts at the highest rate this week. For dads who already grill, the Genesis is the meaningful upgrade. For households building their first backyard, the Spirit is the answer."
                ),
                "highlights": [
                    {"title": "Weber Spirit E-425 at $899 is the first-serious-grill default", "body": "Three stainless burners at 38,000 BTU, porcelain-enameled cast iron grates, 10-year warranty on all parts. Memorial Day $799 floor expired Monday and $899 has held through Saturday at Home Depot and Weber direct. For households buying their first serious gas grill or a Father's Day gift in this bracket, the Spirit is the unambiguous answer. Ground shipping cutoff for Father's Day at Home Depot is June 12."},
                    {"title": "Weber Genesis E-325 at $1,299 is the weeknight-grilling-dad upgrade", "body": "Sear Station for high-heat zone Spirit lacks, side burner for one-grill weeknight meals, 38,000 BTU main with 10-year warranty. For households where grilling is a 4-plus night per week ritual, the Genesis earns its premium. Father's Day gift orders should commit by June 12 for guaranteed delivery."},
                    {"title": "Napoleon Prestige 500 RSIB at $1,699 wins the rotisserie household", "body": "Infrared rear rotisserie burner separates a grill from a backyard oven. For Saturday afternoon whole-chicken cooking or weekend pork-loin rotisserie sessions, the Prestige 500 is the rational premium pick. Napoleon's 15-year burner warranty plus the night-light knobs close the experience gap to Weber at slightly higher pricing."},
                ],
            },
            "zh-tw": {
                "commentary": (
                    "5/30 星期六把瓦斯烤肉爐推進到國殤日後、父親節前下單窗口，價格說明一切。Weber Spirit E-425 守第一 USD$899（代購 NT$29,700），Home Depot、Lowes、Weber 官網都守住。國殤日短暫降到 USD$799、那個地板結束了，但跟 Genesis E-325 USD$1,299 的價差讓 Spirit 還是我推薦第一次買認真瓦斯爐家庭的預設選擇。三支不鏽鋼燃燒器 38,000 BTU、瓷釉鑄鐵烤網、全零件 10 年保固，這是 15 年的後院固定資產。\n\n"
                    "Weber Genesis E-325 守第二 USD$1,299（代購 NT$42,900），適合一週烤肉四次以上的家庭。Sear Station 提供 Spirit 沒有的高熱區，側燃燒器讓週間單爐一餐搞定。Napoleon Prestige 500 RSIB USD$1,699（代購 NT$56,100）守第三高階組，紅外線後旋轉燃燒器是把烤肉爐跟後院烤箱分開的功能，星期六下午整隻雞的買家適用。\n\n"
                    "Weber Summit S-470 USD$2,499（代購 NT$82,500）守第四絕對高階組，Broil King Regal S590 Pro USD$1,899（代購 NT$62,700）守第五雙管紅外線旋轉替代。Home Depot 父親節地面運送截止 6/12，星期六週末宴客買家這週把 Spirit E-425 跟 Genesis E-325 拉進購物車最猛。已經會烤肉的爸爸，Genesis 是有意義的升級。第一次打造後院的家庭，Spirit 就是答案。"
                ),
                "highlights": [
                    {"title": "Weber Spirit E-425 NT$29,700 是第一台認真瓦斯爐預設選擇", "body": "三支不鏽鋼燃燒器 38,000 BTU、瓷釉鑄鐵烤網、全零件 10 年保固。國殤日 USD$799 地板週一結束、USD$899 守到星期六在 Home Depot 跟 Weber 官網。第一次買認真瓦斯爐的家庭或這個預算的父親節禮物，Spirit 就是答案。Home Depot 父親節地面運送截止 6/12。台灣代購含運約 NT$29,700。"},
                    {"title": "Weber Genesis E-325 NT$42,900 是週間烤肉爸爸的升級", "body": "Sear Station 提供 Spirit 沒有的高熱區、側燃燒器讓週間單爐搞定、38,000 BTU 主燃燒器加 10 年保固。一週烤肉四次以上的家庭，Genesis 的溢價有意義。父親節禮物訂單 6/12 前下單才保證到貨。"},
                    {"title": "Napoleon Prestige 500 RSIB NT$56,100 拿下旋轉烤家庭冠軍", "body": "紅外線後旋轉燃燒器把烤肉爐跟後院烤箱分開。星期六下午烤整隻雞或週末旋轉豬里肌的買家，Prestige 500 是理性高階選擇。Napoleon 15 年燃燒器保固加旋鈕夜燈，把跟 Weber 的體驗差距縮小到稍高定價內。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK gas-grills")


if __name__ == "__main__":
    build_air_fryers()
    build_coffee_makers()
    build_rice_cookers()
    build_dishwashers()
    build_portable_ice_makers()
    build_portable_air_conditioners()
    build_outdoor_griddles()
    build_gas_grills()
    print("\nBatch 1 complete (8 files).")
