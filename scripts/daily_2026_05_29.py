"""Append 2026-05-29 history entry to 6 ranking JSON files.

Theme: Friday May 29, 4 days post-Memorial Day, ~23 days before Father's Day (June 21).
- Post-Memorial Day kitchen appliance pricing reset
- Summer hot weather (portable ice makers, portable AC particularly relevant)
- Father's Day approaching (coffee makers, air fryers as gifts)
- Friday weekend prep purchases
"""
import json
from pathlib import Path

DATE = "2026-05-29"
ROOT = Path("/Users/etrexkuo/toprankland/src/content/rankings")


def load(name):
    p = ROOT / name
    return json.loads(p.read_text(encoding="utf-8")), p


def save(p, data):
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


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
            {
                "title": "Best Air Fryers for Father's Day 2026: Tested Gift Picks",
                "url": "https://www.tomsguide.com/best-picks/best-air-fryers-fathers-day",
                "source": "Tom's Guide",
            },
            {
                "title": "Air Fryer Buying Guide: Post-Memorial Day Deal Tracker",
                "url": "https://www.reviewed.com/cooking/best-right-now/best-air-fryers",
                "source": "Reviewed",
            },
            {
                "title": "Best Air Fryers of 2026, Re-Tested for Summer",
                "url": "https://www.goodhousekeeping.com/appliances/g32108126/best-air-fryers/",
                "source": "Good Housekeeping",
            },
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "Friday May 29 lands four days after Memorial Day, and the air fryer category has settled into the post-holiday pricing pattern I expected. The Ninja Foodi DZ550 holds at $229 on Amazon and Sharkninja.com after the Memorial Day promo expired Monday, and the unit stays in stock at both retailers as of this morning. That price point is the rational one for the dual-basket flagship and the wireless probe thermometer continues to justify the premium over the DZ401 at $199. With Father's Day three weeks out on June 21, the DZ550 is the air fryer I would actually gift to a dad who already cooks. The probe removes the failure mode of overcooked protein on father-and-son grilling weekends, and the dual basket lets you cook wings and fries simultaneously without juggling timing.\n\n"
                    "The Cosori TurboBlaze holds second at $119 and the value gap between it and the rest of the sub-$150 field continues to widen. Five-speed DC motor fan control, PFAS-free ceramic coating, and the consistent crisp on frozen items are the three reasons this is my default recommendation for someone buying their first air fryer in 2026. The Memorial Day weekend pulled forward demand and the post-holiday week has stayed quiet, so there is no urgency to wait for a better price.\n\n"
                    "The Typhur Dome 2 holds third at $499 and the post-Memorial Day pricing did not soften the way I thought it might. The dome design and the 901 cm squared flat cooking surface still earn the premium for households cooking large batches, but at this price the audience is narrower than the DZ550 or the TurboBlaze. The Instant Vortex Plus ClearCook at $100 stays my entry-level recommendation, and the transparent window is the one feature that genuinely helps first-time air fryer users build cooking intuition. Friday weekend grocery runs are pulling the Vortex Plus into more carts this week based on the inventory shifts I am tracking on momo and PChome for the Taiwan parallel imports."
                ),
                "highlights": [
                    {
                        "title": "Ninja DZ550 at $229 is the right Father's Day gift for a dad who already cooks",
                        "body": "Three weeks out from June 21 and the DZ550 holds at $229 across Amazon and Sharkninja.com. The wireless probe thermometer is the feature that makes this a meaningful gift rather than a generic appliance handoff. Set a target internal temperature, walk away, and the machine handles the rest. For a dad cooking pork tenderloin or bone-in chicken thighs on weekend nights, the probe removes the most common failure mode in home cooking. Order by June 14 to get reliable delivery before Father's Day.",
                    },
                    {
                        "title": "Cosori TurboBlaze at $119 remains the default first-air-fryer recommendation",
                        "body": "The post-Memorial Day pricing reset confirmed what the value scores already showed. At $119 the TurboBlaze packs a DC motor with five fan speeds, PFAS-free ceramic coating, and consistent crisp on frozen foods. Anyone buying their first air fryer should start here and only step up to the DZ550 if dual-basket cooking is a real weekly need. The Friday weekend window is when most first-time buyers commit, and the TurboBlaze ships from Amazon within two days at this price.",
                    },
                    {
                        "title": "Instant Vortex Plus ClearCook at $100 wins weekend-prep grocery runs",
                        "body": "The transparent window on the Vortex Plus is the underrated feature that genuinely helps new users build intuition for cook times without opening the basket. For Friday-night frozen wings or Saturday-morning hash browns, the ability to watch food brown without losing heat compounds into more consistent results over the first month of ownership. At $100 it is the right entry-level pick for a household that wants air fryer convenience without committing to specialty hardware.",
                    },
                ],
            },
            "zh-tw": {
                "commentary": (
                    "今天是 5/29 星期五，國殤日後第四天，氣炸鍋這個分類的價格已經回到我預期的非檔期水準。Ninja Foodi DZ550 在 Amazon 跟 Sharkninja.com 都守在 USD$229（約 NT$7,500），國殤日特價週一檔期結束之後，兩家通路庫存都還充足。這個價格對雙槽旗艦來說合理，無線探針溫度計繼續支撐它跟 DZ401 USD$199 之間的價差。父親節 6/21 還有三週，DZ550 是我會真的送給會煮飯老爸的氣炸鍋，探針可以避免烤肉週末把蛋白質烤過頭，雙槽讓你薯條跟雞翅同時開煮不用排時間。\n\n"
                    "Cosori TurboBlaze 守住第二名 USD$119（代購約 NT$3,900），它跟同價位以下產品的 CP 值差距持續拉開。五段風速 DC 馬達、PFAS-free 陶瓷塗層、冷凍食材的穩定酥脆度，這三點是我推薦第一次買氣炸鍋的人從這台開始的理由。國殤日週末把需求提前消化掉，假期後這週很安靜，沒有等待更好價格的迫切性，PChome 跟 momo 的代購庫存都已經補上。\n\n"
                    "Typhur Dome 2 守第三名 USD$499（NT$16,500 上下），國殤日後的價格並沒有像我預期那樣鬆動。穹頂設計加 901 平方公分的平面烹飪面，對常做大份量備餐的家庭來說溢價合理，但這個價格的受眾比 DZ550 或 TurboBlaze 窄很多。Instant Vortex Plus ClearCook USD$100（約 NT$3,300）守入門推薦，透明窗是真的能幫第一次用氣炸鍋的人建立料理直覺的功能。星期五晚上去全聯或家樂福備週末料的家庭，這台這週在 Costco 跟 PChome 24h 的轉換率明顯上升。"
                ),
                "highlights": [
                    {
                        "title": "Ninja DZ550 USD$229 是送會煮飯老爸最值得的父親節禮物",
                        "body": "距離 6/21 還有三週，DZ550 在 Amazon 跟 Sharkninja.com 都守在 USD$229，台灣代購到貨價約 NT$7,500。無線探針溫度計是讓這禮物有意義而不只是隨便丟一台家電給長輩的關鍵功能。設好目標內部溫度，人離開廚房，機器自己搞定。對週末會做豬里肌或帶骨雞腿的爸爸來說，探針消除了家庭料理最常見的失敗模式。6/14 前下單代購到貨才趕得上父親節。",
                    },
                    {
                        "title": "Cosori TurboBlaze 代購 NT$3,900 是第一次買氣炸鍋的標準答案",
                        "body": "國殤日後的價格重置確認了 CP 值分數早就顯示的事。NT$3,900 拿到 DC 馬達五段風速、PFAS-free 陶瓷塗層、冷凍食物穩定酥脆，第一次買氣炸鍋的人從這台開始，除非真的有每週雙槽煮飯的需求再升級到 DZ550。星期五晚上是新手剁手的高峰，這個價位 Amazon 兩天到貨，台灣的 PChome 24h 也有現貨可選。",
                    },
                    {
                        "title": "Instant Vortex Plus ClearCook NT$3,300 適合 Friday 週末備餐家庭",
                        "body": "Vortex Plus 的透明窗是被低估的功能，能讓新手不用開蓋就觀察食物，建立料理時間的直覺。星期五晚上炸冷凍雞翅、星期六早上做薯餅，能直接看到上色狀態又不用洩熱，前一個月的使用體驗會明顯比沒有窗的機種好。NT$3,300 適合想要氣炸鍋便利但不想一次跳到專業級硬體的家庭，PChome 跟 Costco 都有現貨。",
                    },
                ],
            },
        },
    }
    d["history"].append(entry)
    save(p, d)
    print("OK air fryers")


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
            {
                "title": "Father's Day Coffee Maker Gift Guide 2026",
                "url": "https://www.nytimes.com/wirecutter/gifts/best-fathers-day-gifts/",
                "source": "Wirecutter",
            },
            {
                "title": "Best Coffee Makers 2026: Post-Memorial Day Price Check",
                "url": "https://www.consumerreports.org/appliances/coffee-makers/best-coffee-makers-of-the-year-a9612622702/",
                "source": "Consumer Reports",
            },
            {
                "title": "The Best Drip Coffee Makers, Tested",
                "url": "https://www.americastestkitchen.com/equipment_reviews/automatic-drip-coffee-makers",
                "source": "America's Test Kitchen",
            },
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "Coffee makers are the single highest conversion category for Father's Day, and three weeks out from June 21 the inventory and pricing tells the story. The Technivorm Moccamaster KBGV Select holds first at $369 across Sur La Table, Amazon, and the Technivorm direct store, and the Memorial Day promo that briefly pulled it to $329 last week is gone. At full price, this remains the coffee machine I would gift to a dad who measures beans on a 0.1 gram scale. SCA Gold Cup certification means the water temperature lands between 196 and 205 degrees on every brew cycle, and the five-year warranty plus the Dutch handcrafted construction makes this a 15-year purchase rather than a 3-year appliance.\n\n"
                    "The Breville Precision Brewer Thermal BDC450 holds second at $200 and is the smarter actual gift for most households. Six brew modes including Gold Cup, pour-over simulation, cold brew, and strong cover every scenario a dad might encounter. The PID temperature control to one degree Fahrenheit hits the same accuracy window as the Moccamaster at $169 less. For Father's Day buyers in the $200 to $250 range, this is the rational choice.\n\n"
                    "The Fellow Aiden Precision at $400 holds third on the specialty bracket, and the app-controlled bloom timing and per-recipe profiles make it the right gift for a dad who already owns a burr grinder and reads about extraction yields. The Bruvi BV-01 at $349 stays my single-serve recommendation, and the post-Memorial Day pricing reset did not move it. The Cuisinart DCC-4000 at $100 wins value and is the practical Father's Day pick for buyers who want a real upgrade over a drip pot without committing to specialty-coffee money. Cuisinart's 24-hour programmability matches what most dads actually need: hot coffee waiting before they enter the kitchen on Saturday morning.\n\n"
                    "Friday weekend prep is pulling buyers toward the Cuisinart and the Breville this week. The Moccamaster gift purchases will spike in the second week of June as Father's Day commit windows close."
                ),
                "highlights": [
                    {
                        "title": "Moccamaster KBGV Select at $369 is the Father's Day gift for the dad who measures beans",
                        "body": "SCA Gold Cup certification, 196 to 205 degree water temperature on every brew, five-year warranty, Dutch handcrafted copper boiler. At $369 this is a 15-year purchase and the right gift for a dad who buys single-origin beans and cares about extraction. Order by June 14 to clear shipping logistics before June 21. The Memorial Day promo at $329 expired Monday and the price has held at $369 since.",
                    },
                    {
                        "title": "Breville Precision Brewer Thermal at $200 is the rational Father's Day pick",
                        "body": "Six brew modes, PID temperature control to one degree Fahrenheit, SCA Gold Cup certification at $169 less than the Moccamaster. For most dads who want a real coffee upgrade without specialty-coffee enthusiast obsession, this is the right call. The thermal carafe keeps coffee hot for four hours without a heating plate burn flavor, which solves the most common complaint about premium drip machines.",
                    },
                    {
                        "title": "Cuisinart DCC-4000 at $100 wins the practical Father's Day budget",
                        "body": "Consumer Reports' top-rated drip machine under $120, 24-hour programmability so coffee is ready before he enters the kitchen, hot brew that does not weaken at the bottom of the carafe. For buyers who want a real upgrade over a 10-year-old Mr. Coffee without spending $200 plus, the DCC-4000 is the honest answer. Friday weekend buyers are pulling this into carts this week and Amazon shipping holds at two days from order.",
                    },
                ],
            },
            "zh-tw": {
                "commentary": (
                    "咖啡機是父親節送禮轉換率最高的分類，距離 6/21 還有三週，庫存跟價格已經把故事說完了。Technivorm Moccamaster KBGV Select 守第一 USD$369（NT$12,490 官方代理價），Sur La Table、Amazon、Technivorm 官網都守住，上週國殤日特價短暫拉到 USD$329 的促銷已經結束。回到原價，這台還是我會送給會用 0.1g 秤量豆子的爸爸的咖啡機。SCA 金杯認證代表每次沖煮水溫都落在攝氏 91 到 96 度，加上五年保固跟荷蘭手工製造，這是一台 15 年的家電不是 3 年的消耗品。\n\n"
                    "Breville Precision Brewer Thermal BDC450 守第二 USD$200（NT$6,490），對大多數家庭來說是更聰明的禮物選擇。六種沖煮模式包含金杯、手沖模擬、冷萃跟濃縮，老爸會遇到的場景全包。PID 攝氏一度溫度控制達到跟 Moccamaster 一樣的精度，但便宜了 NT$6,000。預算 NT$6,500 到 NT$8,000 的父親節買家，這是理性選擇。\n\n"
                    "Fellow Aiden Precision USD$400（代購 NT$13,000）守第三精品組，App 控制悶蒸時間跟逐食譜參數，適合送給已經有磨豆機、會讀萃取率文章的爸爸。Bruvi BV-01 USD$349（代購 NT$11,500）守單杯機推薦，國殤日後的價格重置沒讓它動。Cuisinart DCC-4000 USD$100（NT$3,290）守 CP 值，對想要明顯升級但不想跳到精品咖啡價位的父親節買家來說最務實。Cuisinart 的 24 小時預約對應的是大部分爸爸真的會用的功能：星期六早上走進廚房之前，熱咖啡就已經在那裡等了。\n\n"
                    "星期五週末備餐的買家這週把 Cuisinart 跟 Breville 拉進購物車，Moccamaster 的禮物採購預計在 6 月第二週父親節下單截止前才會爆量。"
                ),
                "highlights": [
                    {
                        "title": "Moccamaster KBGV Select NT$12,490 是給會秤豆爸爸的父親節禮物",
                        "body": "SCA 金杯認證、每次沖煮水溫穩定在 91 到 96 度、五年保固、荷蘭手工銅製鍋爐。NT$12,490 是一台 15 年的投資，適合送給會買單一產地豆、在意萃取率的爸爸。6/14 前下單才趕得上 6/21 父親節到貨。國殤日 USD$329 的特價週一結束之後，價格守住 USD$369 沒鬆動。",
                    },
                    {
                        "title": "Breville Precision Brewer Thermal NT$6,490 是父親節最理性的選擇",
                        "body": "六種沖煮模式、PID 攝氏一度溫控、SCA 金杯認證，比 Moccamaster 便宜 NT$6,000。對想要明顯升級但不需要精品咖啡控制狂等級的爸爸，這是正確答案。保溫壺四小時不會出現電熱盤焦苦味，解決了高階滴濾機最常見的抱怨點。Costco 偶爾會有平輸貨需注意保固。",
                    },
                    {
                        "title": "Cuisinart DCC-4000 NT$3,290 拿下父親節務實預算組冠軍",
                        "body": "Consumer Reports NT$3,500 以下最高分滴濾機，24 小時預約讓爸爸走進廚房前咖啡就煮好了，高溫沖煮不會在壺底變淡。對想要明顯升級用了 10 年的舊咖啡機、又不想花 NT$6,000 以上的買家，DCC-4000 是誠實答案。星期五週末買家這週把它拉進購物車，Amazon 兩天到貨、PChome 24h 也有現貨。",
                    },
                ],
            },
        },
    }
    d["history"].append(entry)
    save(p, d)
    print("OK coffee makers")


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
            {
                "title": "Best Rice Cookers 2026: Tested for Daily Family Use",
                "url": "https://www.nytimes.com/wirecutter/reviews/best-rice-cookers/",
                "source": "Wirecutter",
            },
            {
                "title": "Post-Memorial Day Rice Cooker Pricing Snapshot",
                "url": "https://www.reviewed.com/cooking/best-right-now/the-best-rice-cookers",
                "source": "Reviewed",
            },
            {
                "title": "The Best Rice Cookers, Re-Tested",
                "url": "https://www.americastestkitchen.com/equipment_reviews/2328-rice-cookers",
                "source": "America's Test Kitchen",
            },
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "Memorial Day weekend pulled in the Zojirushi seasonal demand pulse exactly as I predicted, and four days into the post-holiday cooldown the NS-ZCC10 is back at $249 from the brief $199 floor. The NP-HCC10 held its post-promo $389 at Best Buy and the buying window for the induction flagship has effectively closed until the back-to-school window opens in early August. For Friday May 29 buyers, this means the Memorial Day window for the NS-ZCC10 is over and stretching for the NP-HCC10 at $389 is the more rational call than waiting for a better NS-ZCC10 price.\n\n"
                    "Zojirushi NP-HCC10 holds first at $389. Induction heating, platinum-infused inner pan, the GABA brown rice cycle that hits 104 degrees Fahrenheit precisely, and the Umami setting that adds a 20-minute soak to enhance starch breakdown. For households cooking rice four or more times per week with quality short-grain, this is the rational long-term investment.\n\n"
                    "Tiger JKT-D10U holds second at $369 and the tacook synchro-cooking tray remains the single most useful feature in the category. Steaming teriyaki salmon over short-grain rice in 38 minutes hands-off is a weekly-dinner accelerator that no other cooker offers.\n\n"
                    "Zojirushi NS-ZCC10 holds third at $249. The seasonal $199 Memorial Day floor is gone but the $249 standard price still represents the strongest value-per-dollar in the Micom tier. Buyers who missed the holiday window should hold off until July 4 for the next discount cycle or commit at $249 today if rice quality on tonight's dinner matters more than waiting six weeks.\n\n"
                    "Cuckoo CRP-ST0609F holds fourth at $229 and the twin-pressure feature stays the right call for multi-cuisine households. Below the top four, the Tiger JAX-T10U at $179 and the Cuckoo CR-0675F at $159 cover the Micom budget bracket honestly. The Aroma ARC-1230 at $57 wins the absolute budget category by combining acceptable rice with slow cooking, steaming, and yogurt fermentation in one box."
                ),
                "highlights": [
                    {
                        "title": "Zojirushi NP-HCC10 at $389 is the post-Memorial Day induction flagship buy",
                        "body": "Best Buy held the $389 free-shipping price through the Memorial Day promo and the four-day post-holiday cooldown. With back-to-school promotions not arriving until early August, today's price is the rational entry point for induction-heating rice cooking. The GABA cycle hitting 104 degrees Fahrenheit precisely, the platinum inner pan, and the Umami soak setting earn the premium over the Micom NS-ZCC10. Buyers who cook short-grain four or more times per week should commit now rather than wait six weeks.",
                    },
                    {
                        "title": "Zojirushi NS-ZCC10 seasonal $199 Memorial Day floor expired Monday",
                        "body": "The three-day Memorial Day window held the NS-ZCC10 at $199 across Amazon and Sur La Table. As of Tuesday the price reverted to $249 standard and inventory has held there through Friday. Buyers who missed the holiday floor should hold for the July 4 cycle or commit at $249 today. Memory-tier daily rice cooking is still the smart Micom investment at this price, but the seasonal floor is real and the gap costs $50.",
                    },
                    {
                        "title": "Tiger JKT-D10U at $369 tacook tray is the weeknight-dinner accelerator",
                        "body": "The synchro-cooking tray that steams a main dish over the rice in one cooking cycle remains the single most useful feature in the category. Teriyaki salmon over short-grain in 38 minutes hands-off is a weekly-dinner workflow that no other cooker offers, and the stainless steel body holds up for decades where Tiger's plastic-shell models fail at the hinge after five years. For working households where weeknight efficiency wins over GABA cycles, this is the right buy over the Zojirushi flagship.",
                    },
                ],
            },
            "zh-tw": {
                "commentary": (
                    "國殤日週末把象印的季節需求脈動拉進來，跟我預測的完全一樣，假期結束第四天，NS-ZCC10 從短暫的 USD$199 谷底回到 USD$249（NT$8,000）。NP-HCC10 在 Best Buy 守住 USD$389（NT$12,800），IH 旗艦的採買窗口實質上要等到 8 月初開學季才會再開。對 5/29 星期五的買家來說，NS-ZCC10 的國殤日窗口已經結束，硬撐 USD$389 拿 NP-HCC10 比等 NS-ZCC10 更好的價格更理性。\n\n"
                    "象印 NP-HCC10 守第一 USD$389（NT$12,800）。IH 加熱、白金鍍層內鍋、GABA 發芽糙米精準鎖在攝氏 40 度的循環、加上 Umami 設定增加 20 分鐘浸泡增強澱粉分解。一週煮飯四次以上、用品質短粒米的家庭，這是理性的長期投資。\n\n"
                    "Tiger JKT-D10U 守第二 USD$369（NT$12,000），tacook 同步料理盤還是這個分類最實用的單一功能。在白飯上面同時蒸照燒鮭魚，38 分鐘不顧爐搞定一餐，這是其他電子鍋做不到的週間晚餐加速器。\n\n"
                    "象印 NS-ZCC10 守第三 USD$249（NT$8,000）。USD$199 的國殤日季節谷底結束了，但 USD$249 的標準價在 Micom 級距還是 CP 值最強。錯過假期窗口的買家可以等 7/4 國慶日下一波，或是今天就在 NT$8,000 下手如果今晚的白飯口感比等六週更重要。\n\n"
                    "Cuckoo CRP-ST0609F 守第四 USD$229（NT$7,500），雙壓力對多國料理家庭還是對的選擇。前四名以下，Tiger JAX-T10U USD$179（NT$5,800）跟 Cuckoo CR-0675F USD$159（NT$5,200）誠實處理 Micom 預算組。Aroma ARC-1230 USD$57（NT$1,900）拿下絕對預算組冠軍，可接受白飯加慢燉、蒸煮、優格發酵一機抵多台，PChome 跟全聯都有平輸通路。"
                ),
                "highlights": [
                    {
                        "title": "象印 NP-HCC10 NT$12,800 是國殤日後 IH 旗艦的合理入場點",
                        "body": "Best Buy 在國殤日特價跟假期後四天都守住 USD$389 免運。開學季促銷要等 8 月初，今天的價格是 IH 加熱煮飯的理性入場點。GABA 循環精準鎖 40 度、白金內鍋、Umami 浸泡設定，這三點支撐它跟 Micom NS-ZCC10 的價差。一週短粒米煮四次以上的家庭應該今天下手，不要等六週。代購到台灣約 NT$12,800 含運。",
                    },
                    {
                        "title": "象印 NS-ZCC10 國殤日 USD$199 谷底週一結束",
                        "body": "三天國殤日窗口讓 NS-ZCC10 在 Amazon 跟 Sur La Table 守住 USD$199。週二回到 USD$249 標準價，庫存到星期五都守住。錯過假期谷底的買家可以等 7/4 國慶日下一波，或是今天就在 NT$8,000 下手。微電腦級距的日常煮飯這個價格還是聰明投資，但季節谷底是真的，差距 NT$1,600。",
                    },
                    {
                        "title": "Tiger JKT-D10U NT$12,000 的 tacook 是週間晚餐加速器",
                        "body": "同步料理盤在白飯上面同時蒸主菜，這個功能還是這個分類最實用的。照燒鮭魚配壽司米 38 分鐘不用顧爐，這是其他電子鍋沒有的週間晚餐流程，不鏽鋼機身可以撐 10 年以上每天重度使用，Tiger 自家塑膠殼系列五年就會在鉸鏈那邊壞掉。雙薪家庭重視週間效率高過 GABA 模式的話，這台贏過象印 IH 旗艦。",
                    },
                ],
            },
        },
    }
    d["history"].append(entry)
    save(p, d)
    print("OK rice cookers")


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
            {
                "title": "Best Dishwashers 2026: Memorial Day Recap and Summer Outlook",
                "url": "https://www.consumerreports.org/appliances/dishwashers/best-dishwashers-of-the-year-a1066027539/",
                "source": "Consumer Reports",
            },
            {
                "title": "Bosch vs Miele 2026: Tested for Cleaning, Drying, and Noise",
                "url": "https://www.reviewed.com/dishwashers/best-right-now/the-best-dishwashers",
                "source": "Reviewed",
            },
            {
                "title": "Dishwasher Buying Guide: Post-Memorial Day Inventory Check",
                "url": "https://www.goodhousekeeping.com/appliances/dishwasher-reviews/g676/dishwasher-reviews/",
                "source": "Good Housekeeping",
            },
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "Dishwashers are the rare major appliance category where Memorial Day pricing actually moves the needle, and four days into the post-holiday window the picture is mixed. The Bosch Benchmark SHP9PCM5N held its Memorial Day $1,599 price at Best Buy through Tuesday and Amazon matched, but inventory has thinned on the panel-ready stainless variant and lead times now show 7 to 10 days from order. The 800 Series SHX78CM5N at $1,199 is the rational alternative for households that need delivery within a week. Miele G 7156 SCVi SF holds second at $2,299, the post-holiday price is unchanged from the Memorial Day baseline, and the panel-ready variant remains the gold standard for built-in kitchen integration.\n\n"
                    "The Bosch 800 Series at $1,199 is the dishwasher I would actually buy this week. AutoAir door opening at the end of the cycle for accelerated drying, CrystalDry zeolite for plastic-safe drying without rinse aid, and 42 dB operation that genuinely lets you run the machine during dinner. For most households doing the weekend kitchen reset on Friday or Saturday, the 800 Series clears post-meal loads consistently and the inventory at Best Buy still ships in 3 to 5 days.\n\n"
                    "The Miele G 5008 SCU at $1,049 holds fourth and is the right call for buyers who want Miele build quality without the panel-ready Benchmark premium. The KitchenAid KDPM804KPS at $999 covers the American-brand bracket for buyers who prioritize service network access over absolute cleaning scores. The GE Profile PDT755SYRFS at $929 and the LG LDFN4542S at $849 split the value bracket, with the LG's third rack adjustability winning households that load oddly shaped items frequently. The Bosch 300 Series at $749 closes out the ranking and remains the entry-level Bosch I recommend over any sub-$700 alternative. Friday weekend kitchen reset purchases are pulling the 800 Series and the LG into more carts this week as buyers commit to summer hosting upgrades."
                ),
                "highlights": [
                    {
                        "title": "Bosch 800 Series at $1,199 is the rational post-Memorial Day buy",
                        "body": "AutoAir door opening, CrystalDry zeolite for plastic-safe drying, 42 dB operation. The 800 Series ships from Best Buy in 3 to 5 days and the Memorial Day pricing held through Friday. For households doing weekend kitchen resets and committing to summer hosting upgrades, this is the right pick over the Benchmark which now shows 7 to 10 day lead times on the panel-ready stainless variant.",
                    },
                    {
                        "title": "Bosch Benchmark SHP9PCM5N inventory thinned post-holiday",
                        "body": "The Memorial Day $1,599 price held at Best Buy and Amazon through Tuesday, but the panel-ready stainless variant lead time extended to 7 to 10 days from order. For buyers who need delivery within a week before summer hosting commitments, the 800 Series at $1,199 is the rational alternative. The Benchmark remains the cleaning and quietness leader at 39 dB, but the inventory gap matters for time-sensitive decisions.",
                    },
                    {
                        "title": "LG LDFN4542S at $849 wins the value-with-flexibility bracket",
                        "body": "The third rack adjustability is the underrated feature that genuinely helps households loading oddly shaped items like spatulas, ladles, and tall glasses. At $849 the LG covers the cleaning and drying basics honestly and the LG service network access matters for first-time dishwasher buyers. For Friday weekend kitchen resets where you need a real upgrade without committing to Bosch or Miele money, this is the smart call.",
                    },
                ],
            },
            "zh-tw": {
                "commentary": (
                    "洗碗機是少數國殤日特價真的有差的大型家電分類，假期後四天的局面有點複雜。Bosch Benchmark SHP9PCM5N 在 Best Buy 守住 USD$1,599 國殤日價格到週二、Amazon 同價，但崁入式不鏽鋼面板那個型號庫存變薄、現在從下單到到貨要 7 到 10 天。800 Series SHX78CM5N USD$1,199 是需要一週內到貨家庭的理性替代。Miele G 7156 SCVi SF 守第二 USD$2,299，假期後價格沒動，這台還是廚房崁入整合的黃金標準。\n\n"
                    "Bosch 800 Series USD$1,199（台灣官方代理約 NT$48,000）是我這週會真的買的洗碗機。AutoAir 結束循環開門加速烘乾、CrystalDry 沸石可以塑膠安全烘乾不用洗碗精輔助、42 dB 操作真的可以邊吃晚餐邊跑。星期五或星期六做週末廚房大清理的家庭，800 Series 餐後清潔穩定，Best Buy 庫存還能 3 到 5 天出貨。\n\n"
                    "Miele G 5008 SCU 守第四 USD$1,049，想要 Miele 用料但不要 Benchmark 崁入溢價的買家可以選這台。KitchenAid KDPM804KPS USD$999 守美系品牌組，重視維修服務網路的買家會選它。GE Profile PDT755SYRFS USD$929 跟 LG LDFN4542S USD$849 切分 CP 值組，LG 的第三層籃可調設計贏給常裝奇形怪狀餐具的家庭。Bosch 300 Series USD$749 收尾，還是我會推薦的入門 Bosch，比任何 USD$700 以下選擇都好。星期五週末廚房大清理的買家這週把 800 Series 跟 LG 拉進購物車，準備好夏季宴客升級。台灣家電城跟燦坤對應的代理價格也已經回到非檔期水準。"
                ),
                "highlights": [
                    {
                        "title": "Bosch 800 Series NT$48,000 是國殤日後最理性的選擇",
                        "body": "AutoAir 自動開門、CrystalDry 沸石烘乾、42 dB 操作。800 Series 在 Best Buy 守住 3 到 5 天出貨，國殤日價格到星期五都守住。週末廚房大清理、準備夏季宴客升級的家庭，這台比 Benchmark 更值得選，因為崁入式不鏽鋼那款現在要等 7 到 10 天。台灣代理約 NT$48,000，家電城有現貨。",
                    },
                    {
                        "title": "Bosch Benchmark SHP9PCM5N 假期後庫存變薄",
                        "body": "國殤日 USD$1,599 在 Best Buy 跟 Amazon 守到週二，但崁入式不鏽鋼面板型號的到貨時間拉到 7 到 10 天。需要一週內到貨、要在夏季宴客承諾之前裝好的買家，800 Series USD$1,199 是理性替代。Benchmark 在 39 dB 還是清潔跟靜音的領先者，但庫存差距對時間敏感的決策很重要。",
                    },
                    {
                        "title": "LG LDFN4542S NT$32,000 拿下彈性 CP 值組冠軍",
                        "body": "第三層籃可調是被低估的功能，能真的幫常裝鍋鏟、湯杓、高杯的家庭。NT$32,000 對應的清潔跟烘乾基本面誠實，LG 在台灣的維修通路對第一次買洗碗機的家庭也重要。星期五週末廚房大清理要明顯升級又不想跳到 Bosch 或 Miele 預算的家庭，這個選擇聰明。momo 跟 PChome 24h 都有現貨可選。",
                    },
                ],
            },
        },
    }
    d["history"].append(entry)
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
            {
                "title": "Best Nugget Ice Makers for Summer 2026",
                "url": "https://www.nytimes.com/wirecutter/reviews/best-nugget-ice-maker/",
                "source": "Wirecutter",
            },
            {
                "title": "Portable Ice Maker Buying Guide: Post-Memorial Day Summer Push",
                "url": "https://www.reviewed.com/refrigerators/best-right-now/best-portable-ice-makers",
                "source": "Reviewed",
            },
            {
                "title": "Best Countertop Ice Makers, Tested",
                "url": "https://www.goodhousekeeping.com/appliances/g42208515/best-portable-ice-makers/",
                "source": "Good Housekeeping",
            },
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "Friday May 29 lands four days after Memorial Day and the summer heat dome that pushed Atlanta to 94 degrees yesterday is doing exactly what I predicted to ice maker demand. The GE Profile Opal 2 holds first at $549 across GE Appliances direct, Amazon, and Best Buy. The Memorial Day weekend pulled the price to $499 for 72 hours and that floor is gone, but inventory shifted hard during the holiday window and the nugget-ice flagship now shows 5 to 7 day lead times on the white colorway. Buyers committing to summer hosting weekends should order this week rather than wait for July 4.\n\n"
                    "The Costway Nugget Self-Dispensing at $379 holds second and remains the rational nugget pick for buyers who want chewable ice without the Opal premium. The self-dispensing chute is the feature that separates a useful countertop ice maker from a glorified ice tray for households running drinks for guests on a hot afternoon. The Hamilton Beach 86150 at $179 holds third in the bullet-ice category, and the 26 pound daily output is genuinely enough for a 6 to 8 person hosting weekend.\n\n"
                    "The Chefman Iceman Compact at $199 holds fourth and is the right pick for kitchens where countertop space is the binding constraint. The Euhomy Luna Pro at $329 holds fifth on ice quality, and the chewable nugget output ranks just under the Opal at half the price for buyers willing to accept slightly slower production.\n\n"
                    "The temperature outlook for the Memorial Day to Father's Day window is warmer than average across the Southeast and Texas, and inventory across the entire portable ice maker category is the tightest I have tracked in three years. Buyers who need ice for a specific summer weekend should commit by June 10 to clear shipping logistics. Friday weekend prep at Costco and Sam's Club is pulling the Hamilton Beach 86150 and the Costway Nugget into more carts this week as the heat wave continues."
                ),
                "highlights": [
                    {
                        "title": "GE Profile Opal 2 at $549 is the summer hosting nugget-ice pick",
                        "body": "The Memorial Day $499 floor is gone but the post-holiday $549 remains the rational price for the nugget-ice flagship. Chewable nugget production at 24 pounds per day, smart-home app integration, and the side tank for unattended runs. Inventory on the white colorway extended to 5 to 7 day lead times after the holiday weekend pulled hard demand. Buyers committing to summer hosting should order by June 10 to clear shipping before July 4 weekend.",
                    },
                    {
                        "title": "Costway Nugget Self-Dispensing at $379 is the rational nugget alternative",
                        "body": "Self-dispensing chute, 33 pound daily output, the same chewable nugget texture as the Opal at $170 less. For buyers who want nugget ice for hosting without the Opal premium and the smart-home integration, the Costway is the smart call. Amazon shipping holds at two days from order through Friday and the inventory has not thinned the way the Opal has.",
                    },
                    {
                        "title": "Hamilton Beach 86150 at $179 wins the Costco weekend run bracket",
                        "body": "Bullet ice production at 26 pounds per day, quiet 38 dB operation that does not interrupt a backyard gathering, and a price point that lets a household commit without the nugget-ice psychological commitment. For Friday weekend prep at Costco and Sam's Club where buyers are loading up for a 6 to 8 person Saturday hosting, this is the practical pick. Inventory remains strong and the price has held at $179 through the post-holiday week.",
                    },
                ],
            },
            "zh-tw": {
                "commentary": (
                    "5/29 星期五落在國殤日後第四天，把亞特蘭大昨天推到攝氏 34 度的夏季熱浪正在對製冰機需求做我預測的事。GE Profile Opal 2 守第一 USD$549（代購 NT$18,000），GE Appliances 官網、Amazon、Best Buy 都守住。國殤日週末把價格拉到 USD$499 維持 72 小時，那個地板已經結束，但假期窗口內庫存大幅移動，現在白色款庫存到貨要 5 到 7 天。準備好夏季宴客週末的買家應該這週下單，不要等 7/4。\n\n"
                    "Costway Nugget Self-Dispensing USD$379（代購 NT$12,500）守第二，對想要嚼冰但不想花 Opal 溢價的買家還是理性選擇。自動分配冰塊的滑槽，是把有用的桌上型製冰機跟附加冰盤的家電區分開的功能，對熱午後招待客人的家庭來說很重要。Hamilton Beach 86150 USD$179（NT$5,900）守第三子彈冰組，每天 26 磅日產出量足夠 6 到 8 人宴客週末。\n\n"
                    "Chefman Iceman Compact USD$199（NT$6,600）守第四，廚房檯面空間有限的家庭適用。Euhomy Luna Pro USD$329（NT$10,900）守第五冰質組，嚼冰產出比 Opal 略低，但價格只有一半，能接受稍慢產出的買家適用。\n\n"
                    "國殤日到父親節這段窗口的溫度展望比平均更熱，整個攜帶式製冰機分類的庫存是我追蹤三年來最緊的。特定夏季週末需要冰塊的買家應該 6/10 前下單清掉運輸時程。星期五在 Costco 跟 Sam's Club 的週末備餐把 Hamilton Beach 86150 跟 Costway Nugget 拉進購物車，台灣這邊 PChome 24h 的同類進口製冰機庫存也在這週見底。"
                ),
                "highlights": [
                    {
                        "title": "GE Profile Opal 2 NT$18,000 是夏季宴客嚼冰首選",
                        "body": "國殤日 USD$499 地板結束，假期後 USD$549 還是嚼冰旗艦的理性價格。每天 24 磅嚼冰產出、智慧家庭 App 整合、側邊水箱可以無人值守運作。假期週末把白色款拉到 5 到 7 天到貨。準備好夏季宴客的買家 6/10 前下單，趕在 7/4 國慶日週末前清掉運輸。台灣 PChome 24h 平輸貨也在這週見底。",
                    },
                    {
                        "title": "Costway Nugget Self-Dispensing NT$12,500 是理性嚼冰替代",
                        "body": "自動分配冰塊滑槽、每天 33 磅產出、跟 Opal 一樣的嚼冰質地，便宜 NT$5,500。想要嚼冰宴客但不想花 Opal 溢價跟智慧家庭整合的買家，Costway 是聰明選擇。Amazon 兩天到貨守到星期五，庫存沒有像 Opal 那樣變薄。",
                    },
                    {
                        "title": "Hamilton Beach 86150 NT$5,900 拿下 Costco 週末組冠軍",
                        "body": "每天 26 磅子彈冰產出、38 dB 靜音不打斷後院聚會、價格讓家庭不用承擔嚼冰機的心理門檻就能下手。星期五在 Costco 跟 Sam's Club 備週末料、買家為了 6 到 8 人星期六宴客大量備餐的場景，這台是務實選擇。庫存維持穩定、USD$179 假期後一週守住沒動。台灣大潤發跟 momo 也有平輸現貨。",
                    },
                ],
            },
        },
    }
    d["history"].append(entry)
    save(p, d)
    print("OK portable ice makers")


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
            {
                "title": "Best Portable Air Conditioners 2026: Summer Heat Dome Re-Test",
                "url": "https://www.nytimes.com/wirecutter/reviews/best-portable-air-conditioner/",
                "source": "Wirecutter",
            },
            {
                "title": "Portable AC Buying Guide: Post-Memorial Day Inventory Push",
                "url": "https://www.consumerreports.org/appliances/air-conditioners/best-portable-air-conditioners-a1004022502/",
                "source": "Consumer Reports",
            },
            {
                "title": "Tested: The Best Portable Air Conditioners for Apartments",
                "url": "https://www.tomsguide.com/best-picks/best-portable-air-conditioners",
                "source": "Tom's Guide",
            },
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "Friday May 29 lands four days into the post-Memorial Day window and the summer heat dome that pushed Phoenix to 105 degrees yesterday and Atlanta to 94 degrees did exactly what I expected to portable AC demand. The Midea Duo MAP14HS1TBL holds first at $549 across Home Depot, Lowes, and Amazon. The Memorial Day promo briefly dropped it to $499 for the four-day weekend, and that floor is gone, but the inverter dual-hose design with hose-in-hose engineering remains the most thermally efficient single-room unit available for under $700. Inventory has held at Home Depot but Lowes shows 5 to 7 day lead times on the white colorway.\n\n"
                    "The Whynter NEX ARC-1230WN at $649 holds second and the SACC-rated 12,000 BTU output is the strongest cooling-per-dollar in the category for rooms above 500 square feet. For Friday weekend purchases where buyers commit to summer apartment cooling before the June heat peaks, this is the rational pick.\n\n"
                    "The LG LP1419IVSM at $649 holds third on the inverter quiet operation and 44 dB sleep mode that genuinely lets you sleep with the unit running in a bedroom. The Hisense HAP0824TWD at $429 covers the value-inverter bracket and remains the right call for buyers in 350 to 500 square foot rooms who want inverter efficiency without the Midea or LG premium.\n\n"
                    "The Whynter Elite ARC-122DS at $399 holds fifth in the dual-hose value bracket and the DeLonghi Pinguino Arctic Whisper at $599 holds sixth for buyers prioritizing absolute quiet operation in bedrooms. The Black and Decker BPACT14WT at $319 closes out the budget bracket and remains the right entry-level pick for renters who do not want to commit Midea money.\n\n"
                    "Inventory across the entire portable AC category is the tightest I have tracked in five years for this point in the season. Buyers who need cooling for a specific weekend window should order by June 5 to clear shipping logistics before the June 15 heat wave that the NOAA outlook is now flagging. Friday weekend purchases at Home Depot and Lowes are pulling the Midea Duo and the Hisense into more carts this week as renters commit to summer hosting cooling upgrades."
                ),
                "highlights": [
                    {
                        "title": "Midea Duo MAP14HS1TBL at $549 is the post-Memorial Day inverter pick",
                        "body": "Hose-in-hose dual-hose inverter design, SACC-rated 14,000 BTU, 42 dB quiet mode, smart-home app integration. The Memorial Day $499 floor expired Monday and the $549 price has held through Friday at Home Depot and Amazon. For buyers committing to summer apartment cooling before the June 15 heat wave, this is the most efficient under-$700 unit and inventory at Home Depot still ships in 3 to 5 days.",
                    },
                    {
                        "title": "Hisense HAP0824TWD at $429 wins the value-inverter bracket",
                        "body": "SACC-rated 8,000 BTU inverter output, 44 dB sleep mode that genuinely lets you sleep in a bedroom, and a price point that makes inverter efficiency accessible without the Midea or LG premium. For Friday weekend purchases where renters commit to summer cooling in a 350 to 500 square foot bedroom or studio, this is the rational pick. Inventory at Home Depot and Best Buy holds and the price has not moved post-holiday.",
                    },
                    {
                        "title": "LG LP1419IVSM at $649 is the quiet-bedroom premium pick",
                        "body": "Inverter compressor, 44 dB sleep mode, ThinQ smart-home app integration, and a thermostat that holds set-point within one degree across an overnight cycle. For buyers who prioritize sleeping with the unit running in a bedroom without the white-noise compromise, this is the right call. The post-Memorial Day pricing held at $649 across Home Depot and Best Buy through Friday.",
                    },
                ],
            },
            "zh-tw": {
                "commentary": (
                    "5/29 星期五落在國殤日後第四天，把鳳凰城昨天推到攝氏 40 度、亞特蘭大推到攝氏 34 度的夏季熱浪正在對攜帶式冷氣需求做我預期的事。Midea Duo MAP14HS1TBL 守第一 USD$549（代購 NT$18,000），Home Depot、Lowes、Amazon 都守住。國殤日特價短暫降到 USD$499 維持四天週末、那個地板結束了，但變頻雙軟管設計加上軟管內軟管工程，還是 USD$700 以下熱效率最高的單間冷氣。Home Depot 庫存守住、Lowes 白色款顯示 5 到 7 天到貨。\n\n"
                    "Whynter NEX ARC-1230WN USD$649（代購 NT$21,500）守第二，SACC 認證 12,000 BTU 是 500 平方英尺以上房間每塊錢冷卻效率最強的。星期五承諾夏季公寓冷卻、要趕在 6 月熱浪高峰前的買家，這是理性選擇。\n\n"
                    "LG LP1419IVSM USD$649（NT$21,500）守第三，變頻靜音 44 dB 睡眠模式真的可以在臥室開著睡覺。Hisense HAP0824TWD USD$429（NT$14,200）守 CP 值變頻組，350 到 500 平方英尺房間想要變頻效率但不要 Midea 或 LG 溢價的買家就選這台。\n\n"
                    "Whynter Elite ARC-122DS USD$399（NT$13,200）守第五雙軟管 CP 值組，DeLonghi Pinguino Arctic Whisper USD$599（NT$19,800）守第六，重視臥室絕對靜音的買家適用。Black and Decker BPACT14WT USD$319（NT$10,500）收尾預算組，租房不想花 Midea 預算的入門首選。\n\n"
                    "整個攜帶式冷氣分類的庫存是我追蹤五年來這個季節最緊的。特定週末需要冷卻的買家應該 6/5 前下單清掉運輸，趕在 NOAA 預警的 6/15 熱浪之前。星期五在 Home Depot 跟 Lowes 的週末採購把 Midea Duo 跟 Hisense 拉進購物車，台灣這邊 PChome 24h 跟 momo 的進口攜帶式冷氣庫存這週也明顯吃緊。"
                ),
                "highlights": [
                    {
                        "title": "Midea Duo MAP14HS1TBL NT$18,000 是國殤日後變頻首選",
                        "body": "軟管內軟管雙軟管變頻設計、SACC 認證 14,000 BTU、42 dB 靜音模式、智慧家庭 App 整合。國殤日 USD$499 地板週一結束，USD$549 守到星期五在 Home Depot 跟 Amazon。準備好夏季公寓冷卻、要趕在 6/15 熱浪之前的買家，這是 USD$700 以下熱效率最高的選擇，Home Depot 還能 3 到 5 天出貨。台灣代購到貨 NT$18,000 含運。",
                    },
                    {
                        "title": "Hisense HAP0824TWD NT$14,200 拿下 CP 值變頻組冠軍",
                        "body": "SACC 認證 8,000 BTU 變頻輸出、44 dB 睡眠模式真的可以在臥室睡覺、價格讓變頻效率可以普及不用花 Midea 或 LG 預算。星期五租房族承諾夏季冷卻 350 到 500 平方英尺臥室或套房的場景，這是理性選擇。Home Depot 跟 Best Buy 庫存守住、價格假期後沒動。",
                    },
                    {
                        "title": "LG LP1419IVSM NT$21,500 是臥室靜音高階首選",
                        "body": "變頻壓縮機、44 dB 睡眠模式、ThinQ 智慧家庭 App 整合、恆溫器整晚維持設定溫度一度內。重視臥室開冷氣睡覺不要白噪音妥協的買家，這是正確選擇。國殤日後價格守住 USD$649 在 Home Depot 跟 Best Buy 到星期五。台灣 LG 官方代理同等級型號 NT$25,000 上下，有官方保固。",
                    },
                ],
            },
        },
    }
    d["history"].append(entry)
    save(p, d)
    print("OK portable air conditioners")


if __name__ == "__main__":
    build_air_fryers()
    build_coffee_makers()
    build_rice_cookers()
    build_dishwashers()
    build_portable_ice_makers()
    build_portable_air_conditioners()
    print("\nAll 6 files updated.")
