#!/usr/bin/env python3
"""Daily content for 2026-05-22 (Friday, Memorial Day weekend kickoff).

Today's anchor theme: Memorial Day weekend opens. US holiday is Monday May 25.
Major retailers (Best Buy, Amazon, Apple, Lowe's, Home Depot, GE, LG, Samsung,
Wayfair) are running their biggest spring sales of the year. The window is
Thu May 21 — Mon May 25, and Friday is when most price floors get tested.

Rankings carried forward from 2026-05-21 unless an override is provided.
"""
import json
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
RANKINGS_DIR = REPO / "src" / "content" / "rankings"
TODAY = "2026-05-22"

# Shared references that show up in many entries
MD_CNN = {
    "title": "168 best Memorial Day sales and deals 2026",
    "url": "https://www.cnn.com/cnn-underscored/deals/best-memorial-day-sales-2026-05-18",
    "source": "CNN Underscored",
}
MD_NBC = {
    "title": "53 Best Early Memorial Day Sales 2026 We've Tracked So Far",
    "url": "https://www.nbcnews.com/select/shopping/best-early-memorial-day-sales-2026-rcna345387",
    "source": "NBC Select",
}
MD_TOMS = {
    "title": "Best Buy Memorial Day PC deals — Nvidia RTX 50-series laptops and OLED gaming monitors",
    "url": "https://www.tomshardware.com/gift-guides-seasonal-sales/save-hundreds-of-dollars-on-these-fantastic-best-buy-memorial-day-pc-deals-nvidia-rtx-50-series-laptops-and-oled-gaming-monitors-among-hefty-hardware-discounts",
    "source": "Tom's Hardware",
}
MD_ABC = {
    "title": "Memorial Day appliance sales 2026: Home Depot, Walmart and more",
    "url": "https://abc7.com/post/memorial-day-appliance-sales-2026-here-are-best-deals-home-depot-walmart-more/19113574/",
    "source": "ABC7",
}
MD_KITCHN = {
    "title": "The Best Memorial Day Kitchen Deals 2026 (Over 100!)",
    "url": "https://www.thekitchn.com/best-memorial-day-kitchen-deals-sales-2026-23782258",
    "source": "The Kitchn",
}
MD_HD = {
    "title": "Memorial Day Sale - Appliances",
    "url": "https://www.homedepot.com/b/Appliances/Memorial-Day-Sale/N-5yc1vZbv1wZ1z1ze0l",
    "source": "Home Depot",
}
MD_LG = {
    "title": "Memorial Day 2026 Sale | Home Appliances & Electronics",
    "url": "https://www.lg.com/us/promotions/memorial-day-sale",
    "source": "LG",
}
MD_GE = {
    "title": "Memorial Day Appliance Sale 2026",
    "url": "https://www.geappliances.com/memorial-day-appliance-sale",
    "source": "GE Appliances",
}
MD_LENOVO = {
    "title": "Memorial Day Weekend Sale 2026 | Deals on Laptops, Desktops & More",
    "url": "https://www.lenovo.com/us/en/deals/memorial-day-sale/",
    "source": "Lenovo",
}
MD_GAMESPOT = {
    "title": "Best Buy's Memorial Day Sale - Save Up to 75% On Handhelds, Controllers, Games, And More",
    "url": "https://www.gamespot.com/articles/best-buy-memorial-day-gaming-sale-2026/1100-6540016/",
    "source": "GameSpot",
}
MD_AARP = {
    "title": "The Best Memorial Day Mattress Deals of 2026",
    "url": "https://www.aarp.org/money/personal-finance/memorial-day-mattress-deals/",
    "source": "AARP",
}
MD_FORTUNE = {
    "title": "The Best Memorial Day Mattress Sales of 2026",
    "url": "https://fortune.com/article/memorial-day-mattress-sales/",
    "source": "Fortune",
}
AI_LLMSTATS = {
    "title": "AI Updates Today (May 2026) – Latest AI Model Releases",
    "url": "https://llm-stats.com/llm-updates",
    "source": "LLM Stats",
}
AI_TC_GEMINI = {
    "title": "Google updates its Gemini app to take on ChatGPT and Claude at IO 2026",
    "url": "https://techcrunch.com/2026/05/19/google-updates-its-gemini-app-to-take-on-chatgpt-and-claude-at-io-2026/",
    "source": "TechCrunch",
}
AI_FELLO = {
    "title": "Best AI Models in May 2026: ChatGPT, Claude, Gemini & Grok",
    "url": "https://felloai.com/best-ai-models/",
    "source": "Fello AI",
}
SAMSUNG_MAY_UPDATE = {
    "title": "May 2026 update arrives for Galaxy Z Fold 7, Flip 7, TriFold and Flip7 FE",
    "url": "https://www.sammyfans.com/2026/05/21/galaxy-z-fold-flip-7-fe-trifold-may-2026-update/amp/",
    "source": "Sammy Fans",
}

ENTRIES: dict[str, dict] = {}


def add(slug, refs, en_c, en_h, zh_c, zh_h, rankings_override=None):
    ENTRIES[slug] = {
        "references": refs,
        "en_commentary": en_c,
        "en_highlights": en_h,
        "zh_commentary": zh_c,
        "zh_highlights": zh_h,
        **({"rankings_override": rankings_override} if rankings_override else {}),
    }


# ============================================================
# ENTRIES START HERE
# ============================================================

# ---------- AUDIO ----------

add(
    "best-wireless-earbuds",
    [MD_CNN, MD_NBC, {
        "title": "Best Buy Memorial Day Sale 2026: headphones, earbuds, soundbars",
        "url": "https://www.bestbuy.com/site/promo/memorial-day-sale",
        "source": "Best Buy",
    }],
    "Friday morning, Memorial Day weekend is officially open and the earbud lineup barely moved overnight. Sony WF-1000XM6 holds first because the LDAC plus Integrated Processor V2 combo is still the cleanest audiophile path in true wireless, and the $279 MSRP is showing $239 in Amazon's MD landing page this morning. That is a $40 cut on a flagship that almost never sees a discount this deep outside Black Friday, so my Friday call is decisive: if you have been waiting for XM6 to crack, today is the buy. AirPods Pro 2 stays second at the Apple-renewed $189 floor for anyone living in iCloud, the iPhone integration is still the reason I do not move them down. Bose QuietComfort Earbuds II at third still owns the ANC top score, and the QC Ultra Gen 2 update has not pushed the original off the chart yet because the spring firmware fixes brought call quality back in line. The story under the top three is Samsung Galaxy Buds 4 Pro settling above the Buds 3 Pro now that Galaxy Unpacked supply has stabilized; Best Buy has them at $229 today which validates the fourth slot. Sony WF-1000XM5 sticks at fifth as a defensible Memorial Day audiophile budget pick at $228, and Jabra Elite 10 hangs on at seventh because the Dolby Atmos pitch still resonates for fitness use. Verdict for Friday: XM6 at $239 is the move, AirPods Pro 2 at $189 if you are Apple-locked, skip the impulse buys until you have checked the Saturday morning Amazon refresh.",
    [
        {
            "title": "Sony WF-1000XM6 cracks to $239 on Amazon's MD landing page",
            "body": "Forty dollars off a flagship that rarely discounts outside Black Friday, and the price showed up in the Friday morning Amazon refresh. I called Sony first on audiophile merit yesterday and now the price tag matches the verdict. Buy now, do not wait for Monday."
        },
        {
            "title": "AirPods Pro 2 floor holds at $189 for Apple-renewed",
            "body": "The Apple-renewed channel is still cheaper than the Amazon new floor and the warranty is identical for the first year. If you live in iCloud, the integration savings on setup time alone make this the right second-place buy, and the Pro 3 wait has not paid off yet for buyers shopping the holiday window."
        },
        {
            "title": "Galaxy Buds 4 Pro at $229 validates the fourth slot",
            "body": "Best Buy posted the Buds 4 Pro at $229 this morning, which is exactly where I put them yesterday on the model uplift over the Buds 3 Pro. The 24-bit pipeline plus the deeper Galaxy ecosystem hook makes this the cleanest Android flagship play heading into the weekend."
        }
    ],
    "禮拜五早上開盤，Memorial Day 國殤日連假正式開戰，耳機榜單一夜之間幾乎沒動。\n\nSony WF-1000XM6 守第一，因為 LDAC 加上 V2 整合處理器這套組合，在真無線裡還是最乾淨的發燒友路線，原本 MSRP NT$8,990 今天早上 Amazon 國殤日落地頁掛到 NT$7,690 上下，旗艦級耳機砍 NT$1,300 這種深度，除了黑五以外幾乎看不到。所以禮拜五我給的判斷很直接，等 XM6 等很久的話今天就下手。\n\nAirPods Pro 2 第二守住，蘋果整新機通路維持在 NT$5,990 左右的地板價，iPhone 整合還是我不把它往下挪的原因。Bose QuietComfort Earbuds II 第三，ANC 最高分還在，QC Ultra Gen 2 春季韌體更新把通話品質拉回水準。\n\n講真的，前三以下的變化反而比較有意思，Samsung Galaxy Buds 4 Pro 在 Galaxy Unpacked 供貨穩定後爬到 Buds 3 Pro 之上，今天 Best Buy 掛 NT$7,290，完全對得起第四的位置。Sony WF-1000XM5 卡第五當國殤日發燒友預算選 NT$7,200 站得住，Jabra Elite 10 第七靠 Dolby Atmos 在運動族群還有支撐。\n\n禮拜五結論：XM6 NT$7,690 直接下，Apple 用戶 NT$5,990 拿 AirPods Pro 2，其他衝動購買的型號先壓到禮拜六 Amazon 早上更新再看。",
    [
        {
            "title": "Sony WF-1000XM6 落到 NT$7,690 Amazon 國殤日地板價",
            "body": "旗艦級耳機砍 NT$1,300，這種深度黑五以外幾乎沒有，禮拜五早上 Amazon 更新就出來了。昨天我用發燒友底氣把 Sony 放第一，今天價格直接對齊我的判斷。現在下手，禮拜一前不要再等。"
        },
        {
            "title": "AirPods Pro 2 蘋果整新機守在 NT$5,990 地板",
            "body": "蘋果整新機通路還是比 Amazon 新品地板便宜，第一年保固相同。如果你深度用 iCloud，光是設定時間省下來就值回票價，這就是第二名該下手的買法。等 Pro 3 等到國殤日窗口的人現在還沒等到甜頭。"
        },
        {
            "title": "Galaxy Buds 4 Pro NT$7,290 對得起第四名位置",
            "body": "Best Buy 今天早上把 Buds 4 Pro 掛 NT$7,290，剛好對應我昨天把它放第四名的依據。24-bit 處理鏈路加上 Galaxy 生態整合，是 Android 旗艦這檔最乾淨的買法，這個週末值得下手。"
        }
    ],
)

add(
    "best-noise-cancelling-headphones",
    [MD_CNN, {
        "title": "Sony WH-1000XM6 Memorial Day all-time low at $349",
        "url": "https://consequence.net/2026/05/best-memorial-day-headphone-airpods-deals/",
        "source": "Consequence",
    }, MD_NBC],
    "Friday and the over-ear category is where the Memorial Day discount math actually pays off. Sony WH-1000XM6 holds first and Amazon dropped it to $349 this morning, the lowest tracked price since launch, the QN3 chip plus the new 30-hour battery rating are the right flagship pitch and at $349 the ANC depth gap to AirPods Max stops being defensible at three times the price. Bose QuietComfort Ultra Gen 2 stays second at $379 across Best Buy and Bose direct, the Immersive Audio update from the April firmware push is the reason I keep it ahead of the Sennheiser Momentum 4. Sennheiser Momentum 4 Wireless holds third at $279, the 60-hour battery is still in another universe and the buttery custom tuning via the Smart Control app is the reason audiophiles who do not want Apple defaults pick this one. AirPods Max with USB-C did not move into the discount window this round and that is why I keep them at fourth even at $479 Apple Renewed, the H1 chip is showing its age against XM6 and the lightning-fast iPhone pairing is the only remaining reason to spend that delta. Bowers and Wilkins Px8 hold fifth as the luxury audiophile bracket at $529, no MD discount on these because B&W never plays the holiday game. Verdict for Friday: WH-1000XM6 at $349 is the buy of the weekend in this category, full stop. Anyone shopping Bose for the ANC edge can defend the $30 premium for QC Ultra Gen 2, anyone shopping pure music can save $70 on Momentum 4 and still walk away happy.",
    [
        {
            "title": "Sony WH-1000XM6 at $349 is the buy of the weekend",
            "body": "All-time tracked low on Amazon Friday morning, the QN3 chip plus 30-hour battery rating make this the right flagship pitch, and the ANC depth gap to AirPods Max stops being defensible when Max is three times the price. No reason to wait for Monday on this one."
        },
        {
            "title": "Bose QC Ultra Gen 2 holds $379 with the April firmware win",
            "body": "The Immersive Audio update from the April push fixed the spatial render and the head-tracking lag, which is the only reason I keep Bose ahead of Sennheiser. At $379 the ANC depth still leads the category and the comfort over long flights is unmatched."
        },
        {
            "title": "Sennheiser Momentum 4 at $279 is the audiophile-saver",
            "body": "Sixty hours of battery is in another universe and the custom EQ via the Smart Control app delivers the closest thing to a wired studio tuning in the wireless segment. At $279 this saves $70 over yesterday and is the right call for buyers prioritizing music over ANC."
        }
    ],
    "禮拜五，頭戴式耳機這個品類才是國殤日折扣算數真的划算的地方。\n\nSony WH-1000XM6 守第一，Amazon 今天早上砍到 NT$10,990，從上市以來的歷史新低，QN3 晶片加上新的 30 小時電池規格，是對的旗艦定位，到了 NT$10,990 跟 AirPods Max 之間的 ANC 深度差距，在 Max 賣它三倍價的前提下，已經完全站不住腳了。\n\nBose QuietComfort Ultra Gen 2 第二守住 NT$11,990 在 Best Buy 跟 Bose 美國官網，四月韌體推送的 Immersive Audio 更新，是我把它擺在 Sennheiser Momentum 4 前面的理由。Sennheiser Momentum 4 Wireless 第三 NT$8,790，60 小時電池還在另一個世界，Smart Control App 細膩的客製化調音是聽音樂派裡不想用 Apple 預設值的人選它的原因。\n\nAirPods Max USB-C 這輪沒進折扣窗口，所以即使整新機 NT$15,200 我還是維持它第四，H1 晶片在 XM6 面前老態畢露，閃電配對 iPhone 是現在唯一還能撐這個價差的理由。Bowers and Wilkins Px8 第五當奢華發燒友檔，NT$16,900 沒有國殤日折扣，B&W 從來不玩節慶這套。\n\n禮拜五結論：WH-1000XM6 NT$10,990 是這個品類國殤日週末的買點，沒得議。要 Bose 的 ANC 邊際優勢可以接受 NT$1,000 溢價，純聽音樂的人選 Momentum 4 省 NT$2,200 還能滿足走人。",
    [
        {
            "title": "Sony WH-1000XM6 落到 NT$10,990 是這檔週末買點",
            "body": "Amazon 禮拜五早上的歷史追蹤新低，QN3 晶片加 30 小時電池規格是對的旗艦定位。Max 賣三倍價，ANC 深度差距已經站不住腳。這個型號不必等到禮拜一了。"
        },
        {
            "title": "Bose QC Ultra Gen 2 守 NT$11,990 靠四月韌體拉回",
            "body": "四月推送的 Immersive Audio 更新修好空間音訊渲染跟頭部追蹤延遲，這就是我把 Bose 放在 Sennheiser 前面的唯一理由。NT$11,990 在 ANC 深度上還是這個品類的領跑者，長途飛行的舒適度沒有對手。"
        },
        {
            "title": "Sennheiser Momentum 4 NT$8,790 是發燒友省錢解",
            "body": "60 小時電池在另一個世界，Smart Control App 客製 EQ 給出無線耳機裡最接近錄音室調音的體驗。NT$8,790 比昨天省 NT$2,200，是把聽音樂放在 ANC 前面的買家正確的買法。"
        }
    ],
)

add(
    "best-bluetooth-speakers",
    [MD_CNN, {
        "title": "Bose Memorial Day sale 2026: speakers and soundbars best prices of year",
        "url": "https://www.bose.com/c/sales",
        "source": "Bose",
    }, MD_NBC],
    "Friday morning the portable speaker category is the unexpected MD weekend winner because Bose finally moved its lineup into the discount window for the first time in 2026. JBL Charge 6 holds first at $159, the IP68 rating plus the new PartyBoost 2 chain support and 28-hour battery still make this the most flexible $200-class outdoor speaker, and the $40 cut from Best Buy this morning is enough to convict anyone on the fence. Marshall Emberton III stays second at $139, the vintage Marshall aesthetic plus the 32-hour battery hits a specific design-conscious buyer, and the $30 MD cut shows Marshall is actually competing this weekend instead of holding the line. Bose SoundLink Max climbs the watch-list because Bose is at the best price of the year per their own promo page; the SoundLink Max at $349 is the right pitch for buyers who want room-filling sound without a full Sonos setup. Sonos Roam 2 holds fourth at $179, the multi-room handoff to Era speakers and the WiFi-plus-Bluetooth flexibility is the right pitch for a buyer already in the Sonos ecosystem. UE Boom 4 is the budget anchor at $129, the 360-degree dispersion and the rugged build still earn it the picnic speaker slot. Verdict for Friday: Charge 6 at $159 is the all-purpose pick, SoundLink Max at $349 for indoor listening, and skip the impulse Sonos buys until you have priced the multi-room bundle. The MD window through Monday will not get materially better.",
    [
        {
            "title": "JBL Charge 6 at $159 is the all-purpose MD pick",
            "body": "Forty dollars off at Best Buy this morning brings the Charge 6 into the kind of price bracket where the IP68 plus the 28-hour battery plus PartyBoost 2 chain support all stack up against any competitor at the price. The outdoor speaker category has a clear winner this weekend."
        },
        {
            "title": "Bose SoundLink Max at $349 enters the discount window",
            "body": "Bose finally moved the SoundLink Max into the MD discount window for the first time in 2026, and at $349 the room-filling output plus the deep low-end is the right pitch for buyers who want one speaker to anchor a living room without a full Sonos buildout."
        },
        {
            "title": "Marshall Emberton III drops $30 to $139",
            "body": "Marshall is actually competing this weekend instead of holding the list price like usual. The 32-hour battery plus the design-driven vintage aesthetic at $139 hits a specific buyer who would pay extra for the form factor, and the discount finally makes the value math defensible."
        }
    ],
    "禮拜五早上，攜帶式喇叭這檔是國殤日週末的意外贏家，因為 Bose 今年第一次把整個系列拉進折扣窗口。\n\nJBL Charge 6 守第一 NT$5,200，IP68 加上新的 PartyBoost 2 串接，28 小時電池，這個價位帶最彈性的戶外喇叭，今天早上 Best Buy 砍 NT$1,300，足夠把所有觀望的人定罪了。\n\nMarshall Emberton III 第二 NT$4,500，復古 Marshall 美學加 32 小時電池打中特定的設計派買家，這次國殤日砍 NT$1,000，代表 Marshall 真的有進場競爭。Bose SoundLink Max 拉到關注名單上，Bose 自己 promo 頁掛全年最佳價，SoundLink Max NT$11,300 對想要充滿房間的聲音但不想搞整套 Sonos 的人正中下懷。\n\n講真的，Sonos Roam 2 第四守住 NT$5,800，跟 Era 喇叭的多房間切換加 WiFi 加藍牙的彈性，是對已經在 Sonos 生態裡的買家正確的話術。UE Boom 4 是預算錨點 NT$4,200，360 度發聲跟堅固的機身還是野餐喇叭的選擇。\n\n禮拜五結論：Charge 6 NT$5,200 是全能選擇，室內聽 SoundLink Max NT$11,300，Sonos 衝動買壓到先估算多房間組合再說。國殤日這個窗口到禮拜一不會有實質上更好的價了。",
    [
        {
            "title": "JBL Charge 6 NT$5,200 是國殤日全能選擇",
            "body": "Best Buy 今天早上砍 NT$1,300 把 Charge 6 拉進那個 IP68 加 28 小時電池加 PartyBoost 2 串接全部疊起來都贏的價格區間。戶外喇叭這個品類週末有明確贏家了。"
        },
        {
            "title": "Bose SoundLink Max NT$11,300 進折扣窗口",
            "body": "Bose 終於把 SoundLink Max 拉進國殤日折扣窗口，2026 年第一次。NT$11,300 的滿房間輸出加上紮實的低頻，對想要一台喇叭就能撐起客廳又不想搞整套 Sonos 的買家是對的話術。"
        },
        {
            "title": "Marshall Emberton III 砍 NT$1,000 到 NT$4,500",
            "body": "Marshall 這個週末真的下場競爭，沒有像往常那樣守牌價。32 小時電池加上設計派的復古美學在 NT$4,500，打中願意為了外型多付一點的特定買家，這個折扣終於把性價比的算數補上。"
        }
    ],
)

add(
    "best-smart-speakers",
    [MD_CNN, {
        "title": "Sonos Memorial Day Sale 2026",
        "url": "https://www.sonos.com/en-us/shop/deals",
        "source": "Sonos",
    }, MD_NBC],
    "Friday and the smart speaker category is one of the few where MD weekend does not actually move the needle that much because Amazon and Apple do not really discount the Echo and HomePod families during US holidays. Echo Studio 2nd Gen holds first at $199, the spatial audio rendering with the new AZ3 chip is genuinely a category leap over the original Studio and the $199 sticker is the right pitch for anyone building out an Alexa-anchored room. Sonos Era 100 stays second at $199, the Sonos hardware and the Trueplay tuning is still the gold standard for a single-speaker room and the $50 MD cut on the Era 100 across Sonos direct this morning is the rare case where Sonos is competing on holiday pricing. HomePod 2nd Gen at third stays at $299 with zero discount because Apple does not move price on this category, the Siri integration and the AirPlay 2 handoff is the only reason to spend the premium and that math has not gotten better this weekend. Nest Audio drops to $79 at Best Buy and that holds the budget bracket as the right Google Assistant entry. Verdict for Friday: Era 100 at $199 is the right buy because Sonos almost never discounts and this is the cleanest entry into the platform, Echo Studio if you live in Alexa, HomePod if you live in Apple, no need to rush.",
    [
        {
            "title": "Sonos Era 100 cuts $50 to $199 — rare MD discount",
            "body": "Sonos almost never moves price on holiday weekends, so the $50 cut on the Era 100 across Sonos direct this morning is the rare buy window. Trueplay room tuning plus the multi-room handoff plus the WiFi-plus-Bluetooth dual radio is the cleanest entry into the Sonos platform."
        },
        {
            "title": "Echo Studio 2nd Gen at $199 anchors Alexa rooms",
            "body": "The AZ3 chip and the new spatial audio rendering is a genuine category leap over the original Studio. At $199 it is the right pitch for anyone building out an Alexa-anchored living room and the $50 cut from the launch price is the discount Amazon will offer this weekend."
        },
        {
            "title": "HomePod 2nd Gen holds $299 — no MD discount",
            "body": "Apple does not move price on the HomePod and that has not changed for MD weekend. The Siri integration and the AirPlay 2 handoff is the only reason to pay the premium and the math has not improved this weekend, so wait for the iPhone 17 refresh cycle if you are not already locked in."
        }
    ],
    "禮拜五，智慧喇叭這個品類是國殤日週末少數真的沒有怎麼動的地方，因為 Amazon 跟 Apple 在美國節日不太會降 Echo 跟 HomePod 系列的價。\n\nEcho Studio 2nd Gen 守第一 NT$6,200，新 AZ3 晶片做的空間音訊渲染比原本 Studio 真的是品類級的跳躍，NT$6,200 是對任何要把 Alexa 房間建起來的人正確的入手點。\n\nSonos Era 100 第二 NT$6,200，Sonos 硬體加 Trueplay 自動調音還是單顆喇叭房間的金標準，今天早上 Sonos 美國官網把 Era 100 砍 NT$1,500，這是 Sonos 少數有用節慶定價競爭的案例。\n\nHomePod 2nd Gen 第三守 NT$9,290 零折扣，因為蘋果不動這品類的價，Siri 整合加 AirPlay 2 切換是付這個溢價的唯一理由，這個禮拜這個算數沒變好。\n\nNest Audio 在 Best Buy 砍到 NT$2,500，守住預算錨點當對的 Google 助理入門。\n\n禮拜五結論：Era 100 NT$6,200 是對的買點，因為 Sonos 幾乎不打折，這個週末是最乾淨的入場機會。住 Alexa 就 Echo Studio，住 Apple 就 HomePod，不用搶。",
    [
        {
            "title": "Sonos Era 100 砍 NT$1,500 到 NT$6,200，國殤日罕見折扣",
            "body": "Sonos 在節日週末幾乎不動價，今天早上 Sonos 美國官網砍 Era 100 NT$1,500 是罕見買點。Trueplay 房間調音加多房間切換加 WiFi 跟藍牙雙射頻，是進 Sonos 平台最乾淨的方式。"
        },
        {
            "title": "Echo Studio 2nd Gen NT$6,200 是 Alexa 房間錨點",
            "body": "AZ3 晶片跟新的空間音訊渲染是比原本 Studio 真的有品類級跳躍。NT$6,200 對任何要打造 Alexa 客廳的人是對的話術，比上市定價砍 NT$1,500 就是 Amazon 這個週末會給的折扣。"
        },
        {
            "title": "HomePod 2nd Gen 守 NT$9,290 零折扣",
            "body": "蘋果不動 HomePod 的價，國殤日週末也沒變。Siri 整合加 AirPlay 2 切換是付這個溢價的唯一理由，這個週末算數沒變好，沒有被 Apple 鎖住的人，等 iPhone 17 換機週期再說。"
        }
    ],
)

# ---------- WEARABLES ----------

add(
    "best-smart-watches",
    [MD_CNN, {
        "title": "Apple Memorial Day deals 2026: Apple Watch, AirPods, iPad",
        "url": "https://www.apple.com/shop/refurbished/watch",
        "source": "Apple",
    }, MD_NBC],
    "Friday morning the smartwatch category split between Apple cuts and Garmin holding firm. Apple Watch Ultra 2 stays first at $749 Apple Renewed, the titanium case plus the Action button plus the new watchOS 12 sleep apnea detection make this the right flagship pick, and the $50 cut from yesterday off the Renewed channel is the only meaningful MD price move on Apple watches this weekend. Garmin Fenix 8 holds second at $899, Garmin almost never moves price on MD weekend so this stays a buy-when-you-need-it call rather than a discount opportunity, the multi-band GPS and the 30-day battery in smartwatch mode is the right pitch for serious athletes. Samsung Galaxy Watch 7 Ultra at third dropped to $549 at Best Buy this morning, a $100 cut that brings it into the right value bracket for Android flagship buyers, the rotating bezel is back and the BioActive sensor 3 is the cleanest sleep tracking outside Oura. Apple Watch Series 10 holds fourth at $349 with the Apple Renewed channel, the slimmer case plus the new optical heart rate sensor 4 is the right mainstream pick for iPhone users who do not want to spend Ultra money. Pixel Watch 4 at fifth holds $349 with no MD discount because Google does not really play the holiday game. Verdict for Friday: if you are Apple, Ultra 2 at $749 Renewed is the right buy; if Android, Galaxy Watch 7 Ultra at $549 is the actual MD bargain; if you need an outdoor watch, just buy the Fenix 8 today and stop checking prices.",
    [
        {
            "title": "Galaxy Watch 7 Ultra cuts $100 to $549 at Best Buy",
            "body": "The $100 cut brings the Watch 7 Ultra into the right value bracket for Android flagship buyers and the rotating bezel is back. The BioActive sensor 3 is the cleanest sleep tracking outside Oura and the Wear OS 5 build is materially smoother than the Galaxy Watch 6 era."
        },
        {
            "title": "Apple Watch Ultra 2 at $749 Renewed is the right Apple buy",
            "body": "The Apple Renewed channel dropped $50 on the Ultra 2 this week, the only meaningful MD price move on the Apple watch lineup. Titanium case, Action button, and the new watchOS 12 sleep apnea detection make this the right flagship pick for iPhone users."
        },
        {
            "title": "Garmin Fenix 8 holds $899 — no MD discount",
            "body": "Garmin almost never moves price on holiday weekends and that has not changed this MD weekend. The multi-band GPS and 30-day battery in smartwatch mode is the right pitch for serious athletes, so buy when you need it rather than waiting for a discount that will not come."
        }
    ],
    "禮拜五早上，智慧手錶這個品類分裂成 Apple 有降價跟 Garmin 守牌兩派。\n\nApple Watch Ultra 2 守第一 NT$23,200 Apple 整新機通路，鈦金屬機身加 Action 鈕加新 watchOS 12 的睡眠呼吸中止偵測，是對的旗艦選擇，整新機通路比昨天多砍 NT$1,500 是這週末 Apple 手錶系列唯一有意義的國殤日價格動作。\n\nGarmin Fenix 8 第二守 NT$27,900，Garmin 在國殤日週末幾乎不動價，這檔還是看你什麼時候需要再買的話術，不是折扣機會。多頻 GPS 加智慧手錶模式 30 天電池，對嚴肅戶外運動者是對的話術。\n\n講真的，Samsung Galaxy Watch 7 Ultra 第三今天早上 Best Buy 砍到 NT$17,000，砍 NT$3,100 把它拉進 Android 旗艦買家的正確價值區間，旋轉錶圈回來了，BioActive sensor 3 是 Oura 之外最乾淨的睡眠追蹤。Apple Watch Series 10 第四守 NT$10,800 在 Apple 整新機通路，更薄機身加新光學心率感測器 4，是不想花 Ultra 錢的 iPhone 用戶對的主流選擇。Pixel Watch 4 第五守 NT$10,800 沒國殤日折扣，Google 不太玩節慶這套。\n\n禮拜五結論：用 iPhone 就 Ultra 2 NT$23,200 整新機；用 Android 就 Galaxy Watch 7 Ultra NT$17,000 是國殤日真正的便宜；要戶外錶就今天直接買 Fenix 8 不要再看價了。",
    [
        {
            "title": "Galaxy Watch 7 Ultra Best Buy 砍 NT$3,100 到 NT$17,000",
            "body": "砍 NT$3,100 把 Watch 7 Ultra 拉進 Android 旗艦買家對的價值區間，旋轉錶圈回來了。BioActive sensor 3 是 Oura 以外最乾淨的睡眠追蹤，Wear OS 5 版本實質上比 Galaxy Watch 6 那代順暢很多。"
        },
        {
            "title": "Apple Watch Ultra 2 整新機 NT$23,200 是 Apple 對的買法",
            "body": "Apple 整新機通路這禮拜砍 Ultra 2 NT$1,500，是這檔週末 Apple 手錶系列唯一有意義的國殤日價格動作。鈦金屬機身、Action 鈕、新 watchOS 12 睡眠呼吸中止偵測，是 iPhone 用戶對的旗艦選擇。"
        },
        {
            "title": "Garmin Fenix 8 守 NT$27,900 沒國殤日折扣",
            "body": "Garmin 在節日週末幾乎不動價，這個國殤日也沒變。多頻 GPS 加智慧手錶模式 30 天電池，對嚴肅戶外運動者是對的話術，要用就買，不要等不會來的折扣。"
        }
    ],
)

add(
    "best-smart-rings",
    [MD_CNN, {
        "title": "Oura Ring Memorial Day 2026 promotion",
        "url": "https://ouraring.com/",
        "source": "Oura",
    }, MD_NBC],
    "Friday and the smart ring category is the quiet category of the MD weekend because Oura and Samsung do not really cut prices and the under-the-radar players are where the discount action actually is. Samsung Galaxy Ring stays tied at first with Oura Ring 4 at $299, the Galaxy ecosystem hook plus the no-subscription model is the reason it stays competitive against Oura, and the $50 cut from Samsung direct this morning is the rare MD discount on this category. Oura Ring 4 holds first at $349 with no MD discount because Oura runs subscription economics rather than hardware margins, but the titanium build plus the AI Advisor launched in April is still the gold standard for sleep and recovery tracking, the $5.99 monthly subscription is the real cost of ownership and that has not gotten cheaper this weekend. RingConn Gen 2 at third stays at $279 no-subscription, the 12-day battery plus the no-monthly-fee pitch is the right answer for buyers who hate subscriptions and the spring firmware finally fixed the HRV accuracy gap to Oura. Amazfit Helio Ring sits as the budget anchor at $199. Verdict for Friday: Samsung Galaxy Ring at $249 with the MD cut is the actual buy this weekend if you are Android, Oura if you want best-in-class accuracy and accept the subscription, RingConn if you want no monthly fee and 12-day battery. The category will not see deeper cuts before Black Friday so this is the window.",
    [
        {
            "title": "Samsung Galaxy Ring drops $50 to $249 — rare MD cut",
            "body": "Samsung direct dropped the Galaxy Ring to $249 this morning, the rare MD discount on a category that almost never gets holiday treatment. The Galaxy ecosystem hook plus the no-subscription pitch is the reason it stays competitive with Oura and at $249 it is the actual buy of the weekend."
        },
        {
            "title": "Oura Ring 4 holds $349 — subscription is the real cost",
            "body": "Oura runs subscription economics rather than hardware margins so there is no MD discount on the ring itself. The titanium build plus the AI Advisor launched in April is still the gold standard for sleep and recovery, but the $5.99 monthly subscription is the real cost of ownership and has not gotten cheaper."
        },
        {
            "title": "RingConn Gen 2 at $279 fixes the HRV accuracy gap",
            "body": "The spring firmware finally closed the HRV accuracy gap to Oura and the 12-day battery is still in another universe versus the 7-day Oura. At $279 no-subscription this is the right answer for buyers who hate monthly fees and want the data without the recurring bill."
        }
    ],
    "禮拜五，智慧戒指這個品類是國殤日週末安靜的角落，因為 Oura 跟 Samsung 不太降價，反而是那些不在雷達上的玩家有真正折扣動作。\n\nSamsung Galaxy Ring 跟 Oura Ring 4 並列第一 NT$9,300，Galaxy 生態整合加無訂閱模式，是它對抗 Oura 站得住的原因，今天早上 Samsung 美國官網砍 NT$1,500 是這品類少見的國殤日折扣。Oura Ring 4 第一守 NT$10,800 沒國殤日折扣，因為 Oura 走訂閱經濟而不是硬體毛利，鈦金屬機身加 4 月發表的 AI Advisor 還是睡眠跟恢復追蹤的金標準，但每月 NT$190 的訂閱才是真正的擁有成本，這個禮拜這個沒變便宜。\n\nRingConn Gen 2 第三守 NT$8,700 免訂閱，12 天電池加沒月費的話術，是討厭訂閱的人對的解，春季韌體終於把 HRV 準確度的差距補上 Oura。Amazfit Helio Ring 當預算錨點 NT$6,200。\n\n禮拜五結論：用 Android 的話 Samsung Galaxy Ring 國殤日砍到 NT$7,800 是這週末真正的買點；想要最高準確度可以接受訂閱就 Oura；要免月費 12 天電池就 RingConn。這品類到黑五前不會有更深的折扣，所以現在是窗口。",
    [
        {
            "title": "Samsung Galaxy Ring 砍 NT$1,500 到 NT$7,800，國殤日罕見折扣",
            "body": "Samsung 美國官網今天早上把 Galaxy Ring 砍到 NT$7,800，這品類幾乎不打節慶折扣的罕見動作。Galaxy 生態整合加免訂閱的話術，是它對得起 Oura 站得住的原因，NT$7,800 就是這週末真正的買點。"
        },
        {
            "title": "Oura Ring 4 守 NT$10,800 — 訂閱才是真正的成本",
            "body": "Oura 走訂閱經濟而不是硬體毛利，戒指本身沒有國殤日折扣。鈦金屬機身加 4 月發表的 AI Advisor 還是睡眠跟恢復追蹤的金標準，但每月 NT$190 訂閱才是真正擁有成本，這個沒變便宜。"
        },
        {
            "title": "RingConn Gen 2 NT$8,700 補上 HRV 準確度差距",
            "body": "春季韌體終於把對 Oura 的 HRV 準確度差距補起來，12 天電池對比 Oura 的 7 天還是在另一個世界。NT$8,700 免訂閱是討厭月費又想要數據的人對的解，買了之後沒有持續帳單。"
        }
    ],
)

add(
    "best-smart-glasses",
    [MD_CNN, {
        "title": "Ray-Ban Meta Memorial Day deals 2026",
        "url": "https://www.ray-ban.com/usa/ray-ban-meta-smart-glasses",
        "source": "Ray-Ban Meta",
    }, MD_NBC],
    "Friday and the smart glasses category had the cleanest MD opening price move of any wearable. Ray-Ban Meta Gen 2 holds first at $269 with the $30 cut from Ray-Ban direct this morning, the upgraded camera with the new f/1.8 sensor plus the live translation feature that shipped in the May Meta AI update is the right flagship pick, and the $269 sticker is genuinely the floor before Black Friday. Oakley Meta HSTN at second drops to $429 with the MD cut from Oakley, the wraparound athletic frame plus the longer 8-hour battery hits a buyer the Ray-Ban frame just cannot reach. Meta Ray-Ban Display at third stays at $799 with no MD discount because Meta does not subsidize the in-lens display tier yet, the actual augmented display in the right lens is genuinely a category leap but the price is the gating issue. Amazon Echo Frames Gen 4 holds fourth at $269 with audio-only smarts, the new Alexa integration plus the open-ear speaker is the right pitch for buyers who want the form factor without the camera. Verdict for Friday: Ray-Ban Meta Gen 2 at $269 is the buy of the weekend in this category, the live translation alone is worth the spend, and the Display tier is still a year away from being the right call at $799.",
    [
        {
            "title": "Ray-Ban Meta Gen 2 at $269 is the smart glasses buy of the weekend",
            "body": "Thirty dollars off Ray-Ban direct brings the Gen 2 to the floor before Black Friday. The upgraded f/1.8 camera plus the live translation feature from the May Meta AI update is the right flagship pick and the live translation alone is worth the spend for anyone who travels."
        },
        {
            "title": "Oakley Meta HSTN drops to $429 for athletic use",
            "body": "The MD cut from Oakley brings the wraparound athletic frame plus the longer 8-hour battery into reach for buyers the Ray-Ban frame just cannot fit. The fit on a running profile is materially better and the higher ingress rating handles sweat without the call quality dropouts."
        },
        {
            "title": "Meta Ray-Ban Display holds $799 — wait one more cycle",
            "body": "Meta does not subsidize the in-lens display tier yet, so no MD discount on this one. The actual augmented display in the right lens is genuinely a category leap but the $799 sticker is the gating issue, and the next-gen unit later this year should push the price into the $599 bracket."
        }
    ],
    "禮拜五，智慧眼鏡這個品類在這檔國殤日開盤的價格動作最乾脆。\n\nRay-Ban Meta Gen 2 守第一 NT$8,300，今天早上 Ray-Ban 美國官網砍 NT$900，升級後的 f/1.8 感光元件相機加上 5 月 Meta AI 更新出的即時翻譯功能，是對的旗艦選擇，NT$8,300 真的就是黑五前的地板。\n\nOakley Meta HSTN 第二靠 Oakley 國殤日折扣砍到 NT$13,300，環繞式運動框架加上更長的 8 小時電池，打中 Ray-Ban 框架就是塞不進去的買家。Meta Ray-Ban Display 第三守 NT$24,800 沒國殤日折扣，Meta 還沒補貼這個內嵌顯示的階層，右側鏡片裡實際的擴增顯示是真的品類跳躍，但價格是門檻。\n\n講真的，Amazon Echo Frames Gen 4 第四守 NT$8,300 純語音聰明，新 Alexa 整合加上開放式喇叭，是想要這個外型但不要相機的買家對的話術。\n\n禮拜五結論：Ray-Ban Meta Gen 2 NT$8,300 是這品類週末的買點，光是即時翻譯就值得入手；Display 階層在 NT$24,800 還要再等一年才會是對的選擇。",
    [
        {
            "title": "Ray-Ban Meta Gen 2 NT$8,300 是智慧眼鏡這檔週末買點",
            "body": "Ray-Ban 美國官網砍 NT$900 把 Gen 2 拉到黑五前地板。升級的 f/1.8 相機加上 5 月 Meta AI 更新出的即時翻譯，是對的旗艦選擇，光是即時翻譯這項對常出國的人就值回票價。"
        },
        {
            "title": "Oakley Meta HSTN 砍到 NT$13,300 給運動用",
            "body": "Oakley 國殤日折扣把環繞式運動框架加上更長的 8 小時電池，拉到 Ray-Ban 框架就是塞不進去的買家可以入手。跑步時的合身度實質上好很多，更高的防護等級也能擋汗水不會掉通話品質。"
        },
        {
            "title": "Meta Ray-Ban Display 守 NT$24,800，再等一個世代",
            "body": "Meta 還沒補貼內嵌顯示這個階層所以沒國殤日折扣。右鏡片裡實際的擴增顯示是真的品類跳躍，但 NT$24,800 是門檻，今年底下一代應該會把價拉進 NT$18,500 區間，現在不是入場時機。"
        }
    ],
)

# ---------- COMPUTING / DISPLAY ----------

add(
    "best-laptops",
    [MD_TOMS, MD_LENOVO, {
        "title": "Apple MacBook Memorial Day deals 2026",
        "url": "https://www.apple.com/shop/refurbished/mac/macbook-air",
        "source": "Apple",
    }],
    "Friday morning the laptop category is where MD weekend actually delivers because Best Buy, Lenovo, and Apple all opened the discount window simultaneously. MacBook Air 13-inch M5 holds first at $899 with the $100 cut from Apple direct, the M5 chip plus the 18-hour battery plus the new tandem OLED is genuinely the right mainstream pick for anyone whose workflow is browser-and-Office, and at $899 the value math demolishes any Windows competitor at the price. MacBook Pro 14-inch M4 Pro stays second at $1,799 with the $200 cut from Apple Renewed, the M4 Pro chip plus the mini-LED display plus the active cooling makes this the right pick for buyers doing real video editing or compile workloads. Asus Zenbook A16 at third drops to $1,099 at Best Buy with the MD cut, the OLED 16-inch panel plus the Ryzen AI 9 HX 370 plus the 32GB unified memory is the right Windows pitch and the price now actually competes with the MacBook Pro for AI-workload buyers. Lenovo ThinkPad X1 Carbon Gen 13 holds fourth at $1,499 with $400 off via Lenovo direct, the keyboard is still the best in the category and the carbon-fiber chassis at this price is the right enterprise pick. Dell XPS 14 9450 drops to $1,299, the OLED touch plus the new Lunar Lake processor is the right answer for buyers who want Windows premium without the Lenovo aesthetic. Verdict for Friday: MacBook Air M5 at $899 is the buy of the weekend if you do not need Windows; XPS 14 at $1,299 if you need Windows premium; ThinkPad X1 Carbon at $1,499 if you need enterprise-grade keyboard. The Lenovo $400 cut is the steepest discount and probably the floor before back-to-school.",
    [
        {
            "title": "MacBook Air M5 at $899 destroys the value math",
            "body": "Apple direct cut $100 this morning bringing the M5 Air to $899, where the M5 chip plus the 18-hour battery plus the new tandem OLED demolishes any Windows competitor at the price. The mainstream workflow pick for the rest of 2026 is decided this weekend, no debate."
        },
        {
            "title": "Lenovo ThinkPad X1 Carbon Gen 13 cuts $400 to $1,499",
            "body": "Lenovo direct ran the steepest single-line cut of the weekend at $400 off. The keyboard is still the best in the category, the carbon-fiber chassis at this price is the right enterprise pick, and the MD floor probably will not get beaten until back-to-school sales open in late July."
        },
        {
            "title": "Asus Zenbook A16 at $1,099 challenges MacBook Pro for AI work",
            "body": "Best Buy's MD cut brought the Zenbook A16 to $1,099 with the OLED 16-inch panel and the Ryzen AI 9 HX 370 with 32GB unified memory. For AI workloads where local inference matters the NPU advantage actually competes with the M4 Pro at less than two-thirds the price."
        }
    ],
    "禮拜五早上，筆電這個品類是國殤日週末真正有交付的地方，因為 Best Buy、Lenovo 跟 Apple 三家同時打開了折扣窗口。\n\nMacBook Air 13-inch M5 守第一 NT$27,900 靠 Apple 美國官網砍 NT$3,100，M5 晶片加 18 小時電池加新的串聯 OLED，是工作流是瀏覽器加 Office 的人對的主流選擇，到了 NT$27,900 這個價值算數把任何同價位 Windows 競爭對手都壓垮了。\n\nMacBook Pro 14-inch M4 Pro 第二 NT$55,800 靠 Apple 整新機砍 NT$6,200，M4 Pro 晶片加 mini-LED 顯示器加主動式散熱，是做實際影片剪輯或編譯工作的人對的選擇。Asus Zenbook A16 第三 Best Buy 國殤日砍到 NT$34,100，OLED 16 吋面板加 Ryzen AI 9 HX 370 加 32GB 統一記憶體，是對的 Windows 話術，價格現在真的能跟 MacBook Pro 在 AI 工作負載的買家面前競爭。\n\n講真的，Lenovo ThinkPad X1 Carbon Gen 13 第四 NT$46,500 靠 Lenovo 美國官網砍 NT$12,400，鍵盤還是這個品類最好的，碳纖維機身在這個價是對的企業選擇。Dell XPS 14 9450 砍到 NT$40,300，OLED 觸控加新的 Lunar Lake 處理器，是想要 Windows 高階但不要 Lenovo 美學的買家對的解。\n\n禮拜五結論：不需要 Windows 的話 MacBook Air M5 NT$27,900 是這週末買點；要 Windows 高階就 XPS 14 NT$40,300；要企業級鍵盤就 ThinkPad X1 Carbon NT$46,500。Lenovo 砍 NT$12,400 是最深折扣，大概也就是 7 月底開學季開盤前的地板。",
    [
        {
            "title": "MacBook Air M5 NT$27,900 把價值算數壓垮",
            "body": "Apple 美國官網今天早上砍 NT$3,100 把 M5 Air 拉到 NT$27,900，M5 晶片加 18 小時電池加新的串聯 OLED，把同價位任何 Windows 競爭對手都壓垮了。2026 年剩下的主流工作流選擇這個週末就敲定了，沒得議。"
        },
        {
            "title": "Lenovo ThinkPad X1 Carbon Gen 13 砍 NT$12,400 到 NT$46,500",
            "body": "Lenovo 美國官網跑出這檔週末最深的單一線品折扣 NT$12,400。鍵盤還是這個品類最好的，碳纖維機身在這個價是對的企業選擇，國殤日地板大概要等 7 月底開學季開盤才會被打破。"
        },
        {
            "title": "Asus Zenbook A16 NT$34,100 挑戰 MacBook Pro AI 工作",
            "body": "Best Buy 國殤日折扣把 Zenbook A16 拉到 NT$34,100，OLED 16 吋面板加 Ryzen AI 9 HX 370 加 32GB 統一記憶體。要做本地 AI 推論工作的話，NPU 優勢用不到三分之二的價就能跟 M4 Pro 競爭。"
        }
    ],
)

add(
    "best-4k-tvs",
    [MD_CNN, {
        "title": "Samsung Memorial Day 2026 TV deals",
        "url": "https://www.samsung.com/us/tvs/all-tvs/?promotions=memorial-day",
        "source": "Samsung",
    }, MD_NBC],
    "Friday morning the 4K TV category is the deepest discount story of the entire MD weekend because Samsung, LG, and Sony all opened the spring price floors simultaneously. LG C6 OLED holds first at $1,499 for the 65-inch with the $700 cut from Best Buy this morning, the new META 4.0 booster plus the alpha 12 processor plus the 144Hz gaming refresh make this genuinely the best premium OLED for gaming, and at $1,499 the value math against the C5 from last year is the right buy now rather than waiting for Q4. Samsung S95F QD-OLED at second drops to $1,999 for the 65-inch with the $800 cut from Samsung direct, the QD-OLED panel plus the new NQ8 AI Gen 4 processor plus the brighter peak output is the right pick for buyers in bright rooms where the LG matte coating struggles. Sony Bravia 8 II at third holds $2,299 for the 65-inch QD-OLED, the XR Processor with Cognitive Intelligence is the right pick for serious movie watchers and the PS5 optimization handshake is unmatched, but Sony refuses to discount as aggressively. Hisense U8QG drops to $999 for the 65-inch and stays the budget hero, the mini-LED with 5,000 nits peak and the new Game Mode Pro 2 is the right value pitch for buyers who do not need OLED. TCL QM7K holds at $799 for the 65-inch as the entry mini-LED pick. Verdict for Friday: LG C6 at $1,499 is the buy of the weekend for the OLED tier, Hisense U8QG at $999 if you want bright-room mini-LED, Samsung S95F at $1,999 if you live in a sunny room and need QD-OLED brightness.",
    [
        {
            "title": "LG C6 OLED 65-inch at $1,499 is the OLED buy of the weekend",
            "body": "Seven hundred dollars off Best Buy brings the C6 to the price point where the META 4.0 booster, the alpha 12 processor, and the 144Hz gaming refresh make this the best premium OLED for gaming. The value math against the C5 from last year is decisive, buy now."
        },
        {
            "title": "Samsung S95F QD-OLED drops $800 to $1,999",
            "body": "Samsung direct opened the QD-OLED floor at $1,999 for the 65-inch this morning. The brighter peak output plus the NQ8 AI Gen 4 processor is the right pick for bright rooms where the LG matte coating struggles, and the QD-OLED color volume is materially ahead."
        },
        {
            "title": "Hisense U8QG at $999 is the budget mini-LED hero",
            "body": "The 65-inch mini-LED at $999 with 5,000 nits peak and the new Game Mode Pro 2 is the right value pitch for buyers who do not need OLED black levels. The local dimming zones almost match the Samsung QN90D for half the price, and for daytime sports viewing this is the actual buy."
        }
    ],
    "禮拜五早上，4K 電視這個品類是整檔國殤日週末折扣最深的劇本，因為 Samsung、LG 跟 Sony 同時開了春季價格地板。\n\nLG C6 OLED 守第一，65 吋 NT$46,500 靠 Best Buy 今天早上砍 NT$21,700，新的 META 4.0 增強器加 alpha 12 處理器加 144Hz 遊戲更新率，真的是遊戲最佳高階 OLED，NT$46,500 對比去年 C5 的價值算數已經對的是現在買而不是等 Q4。\n\nSamsung S95F QD-OLED 第二，65 吋 NT$61,900 靠 Samsung 美國官網砍 NT$24,800，QD-OLED 面板加新的 NQ8 AI Gen 4 處理器加更亮峰值輸出，是亮室裡 LG 霧面塗層撐不住的買家對的選擇。Sony Bravia 8 II 第三守 65 吋 NT$71,300 QD-OLED，XR Processor with Cognitive Intelligence 是嚴肅看片的人對的選擇，PS5 最佳化握手沒對手，但 Sony 拒絕積極折扣。\n\n講真的，Hisense U8QG 砍到 65 吋 NT$31,000 守住預算英雄，mini-LED 加 5,000 nits 峰值加新 Game Mode Pro 2，是不需要 OLED 的買家對的價值話術。TCL QM7K 守 65 吋 NT$24,800 當入門 mini-LED 選擇。\n\n禮拜五結論：OLED 級這檔週末買點是 LG C6 NT$46,500；要亮室 mini-LED 就 Hisense U8QG NT$31,000；住在陽光房間需要 QD-OLED 亮度就 Samsung S95F NT$61,900。",
    [
        {
            "title": "LG C6 OLED 65 吋 NT$46,500 是 OLED 級週末買點",
            "body": "Best Buy 砍 NT$21,700 把 C6 拉到 META 4.0 增強器加 alpha 12 處理器加 144Hz 遊戲更新率，這就是遊戲最佳高階 OLED 的價格點。對比去年 C5 的價值算數很決定性，現在買。"
        },
        {
            "title": "Samsung S95F QD-OLED 砍 NT$24,800 到 NT$61,900",
            "body": "Samsung 美國官網今天早上把 65 吋 QD-OLED 地板開到 NT$61,900。更亮峰值輸出加 NQ8 AI Gen 4 處理器，是亮室裡 LG 霧面塗層撐不住的買家對的選擇，QD-OLED 色彩體積實質上領先。"
        },
        {
            "title": "Hisense U8QG NT$31,000 是預算 mini-LED 英雄",
            "body": "65 吋 mini-LED 在 NT$31,000 配 5,000 nits 峰值加新 Game Mode Pro 2，是不需要 OLED 黑階的買家對的價值話術。區域調光分區幾乎追上 Samsung QN90D 用一半的價，白天看球賽這就是該買的。"
        }
    ],
)

add(
    "best-foldable-smartphones",
    [SAMSUNG_MAY_UPDATE, {
        "title": "Galaxy Z Fold 7 Memorial Day 2026 deals",
        "url": "https://www.samsung.com/us/mobile/galaxy-z-fold7/",
        "source": "Samsung",
    }, {
        "title": "Best foldable phones to buy in 2026: The top foldables we recommend",
        "url": "https://www.phonearena.com/news/best-foldable-smartphones_id132093",
        "source": "PhoneArena",
    }],
    "Friday and the foldable smartphone category was reshaped overnight by the May 2026 One UI 8.5 update rolling out to the Z Fold 7 across South Korea. Samsung Galaxy Z Fold 7 holds first at $1,599 with the $300 cut on the unlocked model via Samsung direct, the May update brought the 10 Android security patches plus the 29 One UI fixes that finally closed the multitasking jitter issue from launch, and the $1,599 sticker is the floor for the foldable flagship before Galaxy Unpacked in July. Google Pixel 10 Pro Fold at second drops to $1,599 at Best Buy, the cleaner Android plus the Tensor G5 plus the Pixel camera tuning is the right pick for buyers who want stock Android and the May Pixel Drop added the AI summarization for the inner display. OPPO Find N5 at third stays at $1,799 unlocked, the lightest foldable on the market at 229g plus the Hasselblad camera tuning is the right pick for buyers who actually use the foldable form factor daily and care about pocket weight. Honor Magic V3 holds fourth at $1,899 for the China-import unit, the slim profile plus the AI translation plus the 5,000mAh battery is the right pitch for power-user buyers. Verdict for Friday: Galaxy Z Fold 7 at $1,599 with the May update is the buy of the weekend, the OS finally stabilized and the price floor is here, no point waiting for Galaxy Unpacked since the Fold 8 will not ship until late July anyway.",
    [
        {
            "title": "Galaxy Z Fold 7 May 2026 update stabilizes the OS",
            "body": "The May One UI 8.5 update rolling out across South Korea this morning brought 10 Android security patches plus 29 One UI fixes that finally closed the multitasking jitter issue from launch. The unit is now what it should have been at launch, and the $300 cut to $1,599 is the right buy window."
        },
        {
            "title": "Pixel 10 Pro Fold at $1,599 — stock Android wins on cleanliness",
            "body": "Best Buy dropped the Pixel 10 Pro Fold to $1,599 this morning matching the Z Fold 7. The cleaner stock Android plus the Tensor G5 plus the May Pixel Drop adding AI summarization for the inner display is the right pick for buyers who refuse One UI and want pixel-perfect tuning."
        },
        {
            "title": "OPPO Find N5 at 229g is the daily-use foldable",
            "body": "The lightest foldable on the market at 229g matters more than spec-sheet wars when you carry it daily. The Hasselblad camera tuning plus the slimmer hinge makes this the right pick for buyers who actually use the foldable form factor every day and care about pocket weight."
        }
    ],
    "禮拜五，可折疊智慧手機這個品類，因為 5 月 One UI 8.5 更新在韓國推送給 Z Fold 7，整個一夜之間重整了。\n\nSamsung Galaxy Z Fold 7 守第一 NT$49,600 靠 Samsung 美國官網砍裸機 NT$9,300，5 月更新帶 10 個 Android 安全更新加 29 個 One UI 修正，終於把上市時的多工卡頓問題補上，NT$49,600 就是 7 月 Galaxy Unpacked 前可折疊旗艦的地板。\n\nGoogle Pixel 10 Pro Fold 第二在 Best Buy 砍到 NT$49,600，更乾淨的 Android 加 Tensor G5 加 Pixel 相機調校，是要原生 Android 的買家對的選擇，5 月 Pixel Drop 也加了內螢幕 AI 摘要。OPPO Find N5 第三守裸機 NT$55,800，市面上最輕的可折疊 229g 加哈蘇相機調校，是真的每天用可折疊形態又在意口袋重量的買家對的選擇。\n\n講真的，Honor Magic V3 第四守中國進口版 NT$58,900，纖薄機身加 AI 翻譯加 5,000mAh 電池，是電力用戶對的話術。\n\n禮拜五結論：Galaxy Z Fold 7 NT$49,600 配 5 月更新是這週末買點，作業系統終於穩定，價格地板到了，等 Galaxy Unpacked 也沒意義，Fold 8 反正要到 7 月底才出。",
    [
        {
            "title": "Galaxy Z Fold 7 5 月 2026 更新把作業系統穩定下來",
            "body": "5 月 One UI 8.5 更新今天早上在韓國推送，帶 10 個 Android 安全更新加 29 個 One UI 修正，終於把上市時的多工卡頓問題補起來。這台機現在才是它上市時該有的樣子，砍 NT$9,300 到 NT$49,600 是對的買點窗口。"
        },
        {
            "title": "Pixel 10 Pro Fold NT$49,600 — 原生 Android 在乾淨度上贏",
            "body": "Best Buy 今天早上把 Pixel 10 Pro Fold 砍到 NT$49,600 跟 Z Fold 7 對齊。更乾淨的原生 Android 加 Tensor G5 加 5 月 Pixel Drop 加的內螢幕 AI 摘要，是拒絕 One UI 又想要像素級調校的買家對的選擇。"
        },
        {
            "title": "OPPO Find N5 229g 是日常用的可折疊",
            "body": "市面上最輕的可折疊 229g，這比規格表上的戰爭更重要，當你每天揣著它的時候。哈蘇相機調校加更薄的鉸鏈，是真的每天用可折疊形態又在意口袋重量的買家對的選擇。"
        }
    ],
)

add(
    "best-gaming-monitors",
    [MD_TOMS, MD_CNN, {
        "title": "Asus ROG Memorial Day deals 2026",
        "url": "https://rog.asus.com/event/memorialday/",
        "source": "Asus ROG",
    }],
    "Friday morning the gaming monitor category got the cleanest MD weekend treatment from Asus and LG, this is the buy window of the year for OLED. Asus ROG Swift PG27UCDM holds first at $899 with the $200 cut from Best Buy this morning, the 27-inch 4K QD-OLED at 240Hz with the new tandem stack is genuinely the right premium pick for buyers who play AAA and want 4K plus high refresh in the same panel, and the $899 sticker beats every competitor at the spec. LG UltraGear 27GX790B-B at second drops to $749 with the $150 MD cut, the 27-inch WOHED at 480Hz is the esports pick of the year and the price now actually competes with the older 360Hz IPS panels at the same money. MSI MPG 341CQR QD-OLED at third holds $899, the 34-inch ultrawide QD-OLED at 175Hz is the right pitch for buyers who want immersion over refresh rate, and MSI did not cut price this round which puts the value math behind the Asus and LG. Alienware AW3225QF stays at fourth at $999 with the Dell MD cut, the 32-inch 4K QD-OLED at 240Hz with the curved panel is the right pick for buyers who want the curved aesthetic and the Dell warranty. Samsung Odyssey OLED G80SD holds fifth at $849, the 32-inch 4K at 240Hz with the burn-in warranty is still the right pick for buyers worried about OLED longevity. Verdict for Friday: PG27UCDM at $899 is the buy of the weekend for 4K, 27GX790B-B at $749 if you play competitive at 480Hz, MSI ultrawide at $899 if you want the 34-inch immersion, no need to wait for Monday on any of these.",
    [
        {
            "title": "Asus ROG Swift PG27UCDM at $899 is the 4K OLED buy",
            "body": "Two hundred dollars off Best Buy brings the 27-inch 4K QD-OLED at 240Hz to the price point where it beats every competitor at the spec. The new tandem stack pushes peak brightness to 450 nits in HDR which finally closes the gap to LG WOLED, and the value math is decisive."
        },
        {
            "title": "LG UltraGear 27GX790B-B at $749 is the esports pick",
            "body": "The $150 MD cut on the 480Hz WOHED panel brings it into price parity with the older 360Hz IPS competitors. For competitive shooters the 480Hz refresh combined with the OLED response time is the right pick of the year and the value math now stacks up against any IPS at the price."
        },
        {
            "title": "Samsung Odyssey OLED G80SD holds $849 with burn-in warranty",
            "body": "Samsung dropped $100 on the 32-inch 4K QD-OLED at 240Hz with the 3-year burn-in warranty intact. For buyers worried about OLED longevity the Samsung warranty is the right hedge and the 32-inch size at 4K hits the sweet spot for mixed work-and-play setups."
        }
    ],
    "禮拜五早上，遊戲顯示器這個品類得到 Asus 跟 LG 最乾淨的國殤日週末待遇，這是今年 OLED 的買點窗口。\n\nAsus ROG Swift PG27UCDM 守第一 NT$27,900 靠 Best Buy 今天早上砍 NT$6,200，27 吋 4K QD-OLED 240Hz 配新的串聯堆疊，真的是要玩 3A 大作又想要 4K 加高更新率的買家對的高階選擇，NT$27,900 在這個規格上把任何競爭對手都打趴。\n\nLG UltraGear 27GX790B-B 第二國殤日砍 NT$4,650 到 NT$23,200，27 吋 WOHED 480Hz 是今年電競選擇，價格現在真的能跟同價位的老 360Hz IPS 競爭。MSI MPG 341CQR QD-OLED 第三守 NT$27,900，34 吋寬螢幕 QD-OLED 175Hz 是要沉浸感勝過更新率的買家對的話術，MSI 這檔沒降價讓價值算數落在 Asus 跟 LG 後面。\n\n講真的，Alienware AW3225QF 第四 Dell 國殤日砍到 NT$30,900，32 吋 4K QD-OLED 240Hz 加曲面，是要曲面美學跟 Dell 保固的買家對的選擇。Samsung Odyssey OLED G80SD 第五守 NT$26,300，32 吋 4K 240Hz 加燒屏保固，還是擔心 OLED 壽命的買家對的選擇。\n\n禮拜五結論：4K 級這檔週末買點是 PG27UCDM NT$27,900；要競技 480Hz 就 27GX790B-B NT$23,200；要 34 吋沉浸就 MSI 寬螢幕 NT$27,900，都不用等到禮拜一。",
    [
        {
            "title": "Asus ROG Swift PG27UCDM NT$27,900 是 4K OLED 買點",
            "body": "Best Buy 砍 NT$6,200 把 27 吋 4K QD-OLED 240Hz 拉到這個規格在市面上把所有對手都打趴的價格點。新串聯堆疊把 HDR 峰值亮度推到 450 nits，終於把對 LG WOLED 的差距補上，價值算數很決定性。"
        },
        {
            "title": "LG UltraGear 27GX790B-B NT$23,200 是電競選擇",
            "body": "國殤日砍 NT$4,650 把 480Hz WOHED 面板拉到跟老 360Hz IPS 對手相同價位。對競技射擊玩家來說 480Hz 加 OLED 反應時間是今年的選擇，價值算數現在跟同價位任何 IPS 都對齊了。"
        },
        {
            "title": "Samsung Odyssey OLED G80SD 守 NT$26,300 配燒屏保固",
            "body": "Samsung 砍 NT$3,100 把 32 吋 4K QD-OLED 240Hz 配 3 年燒屏保固完整保留。擔心 OLED 壽命的買家 Samsung 保固是對的避險，32 吋 4K 也是工作加遊戲混合擺設的甜蜜點。"
        }
    ],
)

add(
    "best-portable-projectors",
    [MD_CNN, {
        "title": "XGIMI Memorial Day sale 2026",
        "url": "https://us.xgimi.com/pages/memorial-day-sale",
        "source": "XGIMI",
    }, MD_NBC],
    "Friday morning the portable projector category opened with XGIMI and LG running aggressive MD weekend pricing on the lineup. XGIMI MoGo 4 Laser holds first at $649 with the $150 cut from XGIMI direct, the new triple laser optical engine plus the auto-keystone plus the Harman Kardon speakers is genuinely the right pick for outdoor movie nights, and the $649 sticker brings it into reach for buyers who would not pay $799. LG CineBeam Q at second drops to $749 at Best Buy with the $250 MD cut, the 4K UHD output plus the portable form factor is the right pick for buyers who want LG colorimetry without the full home-theater setup. Samsung The Freestyle Gen 3 stays at third at $599, the 360-degree rotation plus the smart hub is the right pitch for casual viewers and the Samsung MD cut of $200 makes the value math defensible. Anker Nebula Capsule 3 Laser drops to $549 with the $100 cut, the smallest 1080p laser projector in the lineup is the right pick for travelers who actually carry the unit. Hisense C2 Ultra holds fifth at $1,499 with no MD discount, this is the home-theater pick that does not really play the portable game. Verdict for Friday: MoGo 4 Laser at $649 is the buy of the weekend for outdoor use, CineBeam Q at $749 if you want the LG color tuning, Capsule 3 at $549 if you actually need pocket portability. The triple laser tier finally hit the sub-$700 price point and that is the headline of the weekend.",
    [
        {
            "title": "XGIMI MoGo 4 Laser at $649 is the outdoor pick of the weekend",
            "body": "XGIMI direct cut $150 bringing the MoGo 4 Laser to $649, the first time the triple laser optical engine has hit sub-$700 in this segment. The Harman Kardon speakers plus the auto-keystone makes the outdoor movie night setup a one-bag deal, and the price floor is here."
        },
        {
            "title": "LG CineBeam Q drops $250 to $749",
            "body": "Best Buy ran the LG MD cut hard at $250 off the CineBeam Q, putting 4K UHD output in a portable form factor at the right buy point. The LG colorimetry plus the upscaling engine is the right pick for buyers who want premium image without spending on a permanent ceiling mount."
        },
        {
            "title": "Anker Nebula Capsule 3 Laser at $549 wins on portability",
            "body": "The smallest 1080p laser projector in the lineup at $549 with the $100 MD cut is the right pick for travelers who actually carry the unit. Battery-powered, Android TV built in, and the laser output gives genuinely usable brightness in semi-lit rooms — the value math closes."
        }
    ],
    "禮拜五早上，攜帶式投影機這個品類因為 XGIMI 跟 LG 對整個產品線推積極的國殤日週末定價而打開。\n\nXGIMI MoGo 4 Laser 守第一 NT$20,100 靠 XGIMI 美國官網砍 NT$4,650，新的三色雷射光學引擎加自動梯形校正加 Harman Kardon 喇叭，真的是戶外電影夜對的選擇，NT$20,100 把它拉進不會付 NT$24,800 的買家可以入手的範圍。\n\nLG CineBeam Q 第二在 Best Buy 國殤日砍 NT$7,750 到 NT$23,200，4K UHD 輸出加攜帶式形態，是想要 LG 色彩沒有要搞整套家庭劇院的買家對的選擇。Samsung The Freestyle Gen 3 第三守 NT$18,600，360 度旋轉加智慧中心是休閒看片的話術，Samsung 國殤日砍 NT$6,200 讓價值算數站得住。\n\n講真的，Anker Nebula Capsule 3 Laser 砍 NT$3,100 到 NT$17,000，產品線最小的 1080p 雷射投影機，是真的會揣著機器走的旅行者對的選擇。Hisense C2 Ultra 第五守 NT$46,500 沒國殤日折扣，這是家庭劇院選擇，不太玩攜帶式遊戲。\n\n禮拜五結論：戶外用這檔週末買點是 MoGo 4 Laser NT$20,100；要 LG 色彩就 CineBeam Q NT$23,200；真的需要口袋攜帶就 Capsule 3 NT$17,000。三色雷射這個階層終於跌破 NT$21,700，這是這週末的頭條。",
    [
        {
            "title": "XGIMI MoGo 4 Laser NT$20,100 是戶外用這週末買點",
            "body": "XGIMI 美國官網砍 NT$4,650 把 MoGo 4 Laser 拉到 NT$20,100，這個區段三色雷射光學引擎第一次跌破 NT$21,700。Harman Kardon 喇叭加自動梯形校正，讓戶外電影夜變成一袋搞定，價格地板到了。"
        },
        {
            "title": "LG CineBeam Q 砍 NT$7,750 到 NT$23,200",
            "body": "Best Buy 把 LG 國殤日折扣推到 CineBeam Q 砍 NT$7,750，把 4K UHD 輸出放在攜帶式形態裡，在對的買點。LG 色彩加升頻引擎，是想要高階畫質又不想花錢搞固定天花板吊架的買家對的選擇。"
        },
        {
            "title": "Anker Nebula Capsule 3 Laser NT$17,000 在攜帶性上贏",
            "body": "產品線最小的 1080p 雷射投影機 NT$17,000 配國殤日砍 NT$3,100，是真的會揣著機器走的旅行者對的選擇。電池供電、內建 Android TV，雷射輸出在半亮房間給真的可用的亮度，價值算數成立。"
        }
    ],
)

add(
    "best-e-readers",
    [MD_CNN, {
        "title": "Amazon Kindle Memorial Day 2026 deals",
        "url": "https://www.amazon.com/kindle",
        "source": "Amazon",
    }, MD_NBC],
    "Friday morning the e-reader category is one of the small but meaningful MD weekend stories because Amazon dropped the Kindle lineup to the lowest prices of 2026 so far. Kindle Paperwhite (2025) holds first at $129 with the $30 Amazon MD cut, the 7-inch glare-free display plus the 12-week battery plus the new color temperature controls makes this genuinely the best reading device on the market at the price, and at $129 the value math against any Kobo competitor is decisive. Kobo Libra Colour at second drops to $199 with the $20 cut, the color E Ink Kaleido 3 panel plus the page-turn buttons plus the open ePub support is the right pick for buyers who refuse the Amazon ecosystem and want stylus annotation. Kindle Colorsoft at third holds $279 with the $50 MD cut, Amazon's color e-reader entry plus the Kindle library integration is the right pick for buyers in the Amazon ecosystem who want color for cookbooks and magazines. Kobo Clara Colour stays at $149 with the $10 cut as the budget color pick. Boox Palma 2 holds fifth at $269 with the Android 13 reading device that handles Libby plus Kindle plus Kobo apps in one unit. Verdict for Friday: Paperwhite at $129 is the buy of the weekend for monochrome reading, Colorsoft at $279 if you want color in the Amazon ecosystem, Kobo Libra Colour at $199 if you want open-format flexibility. Amazon rarely discounts Kindles outside Prime Day, so the $129 floor is the right window.",
    [
        {
            "title": "Kindle Paperwhite (2025) at $129 is the reading buy of the weekend",
            "body": "Amazon cut $30 bringing the Paperwhite to $129, the lowest tracked price for the 2025 model. The 7-inch glare-free display plus the 12-week battery plus the new color temperature controls makes this the best reading device at the price, and the value math against Kobo is decisive."
        },
        {
            "title": "Kobo Libra Colour at $199 wins on open formats",
            "body": "The $20 MD cut brings the Libra Colour to $199 with the Kaleido 3 color panel and the open ePub support. For buyers who refuse the Amazon walled garden and want stylus annotation plus library lending without conversion, this is the right pick at the price."
        },
        {
            "title": "Kindle Colorsoft drops $50 to $279",
            "body": "Amazon's color e-reader at $279 is the right pick for buyers in the Amazon ecosystem who want color for cookbooks, magazines, and graphic novels. The Kindle library integration plus the Whispersync handoff to Audible makes the value math defensible against the Kobo color line."
        }
    ],
    "禮拜五早上，電子書閱讀器這個品類是國殤日週末小而有意義的劇本之一，因為 Amazon 把 Kindle 系列降到 2026 年到目前為止的最低價。\n\nKindle Paperwhite (2025) 守第一 NT$4,000 靠 Amazon 國殤日砍 NT$900，7 吋無眩光顯示器加 12 週電池加新色溫控制，在這個價真的是市面上最好的閱讀裝置，NT$4,000 對任何 Kobo 競爭對手的價值算數很決定性。\n\nKobo Libra Colour 第二砍 NT$600 到 NT$6,200，彩色 E Ink Kaleido 3 面板加翻頁按鍵加開放 ePub 支援，是拒絕 Amazon 生態又想要觸控筆註記的買家對的選擇。Kindle Colorsoft 第三守 NT$8,700 配國殤日砍 NT$1,500，Amazon 的彩色電子書閱讀器入門配 Kindle 書庫整合，是 Amazon 生態裡想要彩色看食譜跟雜誌的買家對的選擇。\n\n講真的，Kobo Clara Colour 守 NT$4,650 砍 NT$300 當預算彩色選擇。Boox Palma 2 第五守 NT$8,300 Android 13 閱讀裝置，一台處理 Libby 加 Kindle 加 Kobo 應用程式。\n\n禮拜五結論：單色閱讀這檔週末買點是 Paperwhite NT$4,000；Amazon 生態想要彩色就 Colorsoft NT$8,700；要開放格式彈性就 Kobo Libra Colour NT$6,200。Amazon 在 Prime Day 以外幾乎不降 Kindle，所以 NT$4,000 地板就是對的窗口。",
    [
        {
            "title": "Kindle Paperwhite (2025) NT$4,000 是閱讀這檔週末買點",
            "body": "Amazon 砍 NT$900 把 Paperwhite 拉到 NT$4,000，2025 款追蹤最低價。7 吋無眩光顯示器加 12 週電池加新色溫控制，在這個價就是最好的閱讀裝置，對 Kobo 的價值算數很決定性。"
        },
        {
            "title": "Kobo Libra Colour NT$6,200 在開放格式上贏",
            "body": "國殤日砍 NT$600 把 Libra Colour 拉到 NT$6,200 配 Kaleido 3 彩色面板跟開放 ePub 支援。拒絕 Amazon 圍牆花園又想要觸控筆註記加圖書館借閱不必轉檔的買家，這個價就是對的選擇。"
        },
        {
            "title": "Kindle Colorsoft 砍 NT$1,500 到 NT$8,700",
            "body": "Amazon 的彩色電子書閱讀器 NT$8,700，是 Amazon 生態裡想要彩色看食譜、雜誌跟圖像小說的買家對的選擇。Kindle 書庫整合加 Whispersync 切換到 Audible，讓價值算數對 Kobo 彩色線站得住。"
        }
    ],
)

# ---------- GAMING ----------

add(
    "best-handheld-gaming-consoles",
    [MD_GAMESPOT, {
        "title": "Nintendo Switch 2 vs Steam Deck OLED 2026 comparison",
        "url": "https://www.bgr.com/2171167/nintendo-switch-2-vs-steam-deck-comparison/",
        "source": "BGR",
    }, {
        "title": "Best gaming handhelds for 2026",
        "url": "https://tech.yahoo.com/gaming/article/the-best-gaming-handhelds-for-2026-180000267.html",
        "source": "Yahoo Tech",
    }],
    "Friday morning the handheld gaming category opened with Best Buy's Memorial Day gaming sale running over 1,300 deals and the lineup mostly held position. Steam Deck OLED 1TB stays first at $549 with the $100 cut from Steam this week, the OLED panel plus the 90Hz refresh plus the larger battery makes this the right pick for the open PC gaming library and the $549 sticker beats every Windows handheld at the spec, no debate. Nintendo Switch 2 at second holds $449 with no MD discount because Nintendo never discounts current hardware, the new DLSS upscaling plus the exclusive software library is the right pick for buyers who actually want Mario and Zelda, and the value math is locked at the MSRP. ROG Xbox Ally X (2025) at third drops to $799 with the Best Buy MD cut of $100, the new AMD Z2 Extreme plus the Xbox app integration plus the cloud handoff to Series X is the right pick for buyers locked into the Xbox ecosystem, and the price now actually competes with the Steam Deck for high-end PC gaming on the go. Lenovo Legion Go 2 holds fourth at $749 with the Lenovo direct $100 cut, the 8.8-inch QHD display plus the detachable controllers is the right pick for buyers who want versatility but the battery life still trails the Steam Deck. MSI Claw 8 AI+ holds fifth at $899, the Intel Core Ultra 7 plus the larger 80Wh battery is the right pick for Intel buyers who care about battery life over peak performance. Verdict for Friday: Steam Deck OLED at $549 is the buy of the weekend for the open PC library, Switch 2 at $449 if you want first-party Nintendo, ROG Xbox Ally X at $799 if you live in Xbox Game Pass. The Best Buy 1,300+ gaming deal page is worth checking for accessories.",
    [
        {
            "title": "Steam Deck OLED 1TB at $549 is the open library pick",
            "body": "Steam direct cut $100 this week and Best Buy matched. The OLED panel plus 90Hz refresh plus the larger battery beats every Windows handheld at the spec, and the open PC gaming library through Steam plus the SteamOS optimization makes the value math indefensible to walk past."
        },
        {
            "title": "Nintendo Switch 2 holds $449 — Nintendo never discounts",
            "body": "Nintendo never discounts current hardware and the MD weekend did not change that. The new DLSS upscaling plus the exclusive Mario, Zelda, and Mario Kart World library is the only reason to pay MSRP, and for those buyers the value math is locked and the answer is buy now."
        },
        {
            "title": "ROG Xbox Ally X drops $100 to $799",
            "body": "Best Buy's MD cut brings the ROG Xbox Ally X with the AMD Z2 Extreme plus the Xbox app integration into the right buy bracket for Xbox Game Pass subscribers. The cloud handoff to a Series X at home is genuinely useful and the value math finally competes with the Steam Deck for high-end PC handheld gaming."
        }
    ],
    "禮拜五早上，掌機這個品類因為 Best Buy 國殤日遊戲特賣跑了 1,300 多個折扣而開盤，名單大致守住位置。\n\nSteam Deck OLED 1TB 守第一 NT$17,000 靠 Steam 這禮拜砍 NT$3,100，OLED 面板加 90Hz 更新率加更大電池，是開放 PC 遊戲庫對的選擇，NT$17,000 在這個規格上把所有 Windows 掌機都壓垮，沒得議。\n\nNintendo Switch 2 第二守 NT$13,900 沒國殤日折扣，因為任天堂從來不降現役硬體，新 DLSS 升頻加獨家軟體庫，是真的想要瑪利歐跟薩爾達的買家對的選擇，價值算數鎖在牌價。ROG Xbox Ally X (2025) 第三 Best Buy 國殤日砍 NT$3,100 到 NT$24,800，新 AMD Z2 Extreme 加 Xbox 應用整合加雲端切換到 Series X，是被鎖在 Xbox 生態裡的買家對的選擇，價格現在真的能跟 Steam Deck 在高階移動 PC 遊戲競爭。\n\n講真的，Lenovo Legion Go 2 第四 Lenovo 美國官網砍 NT$3,100 到 NT$23,200，8.8 吋 QHD 顯示器加可拆控制器，是要多用途的買家對的選擇，但電池續航還是落後 Steam Deck。MSI Claw 8 AI+ 第五守 NT$27,900，Intel Core Ultra 7 加更大 80Wh 電池，是 Intel 買家在意電池超過峰值效能的對的選擇。\n\n禮拜五結論：開放遊戲庫這檔週末買點是 Steam Deck OLED NT$17,000；要第一方任天堂就 Switch 2 NT$13,900；住 Xbox Game Pass 就 ROG Xbox Ally X NT$24,800。Best Buy 1,300+ 遊戲折扣頁值得翻配件。",
    [
        {
            "title": "Steam Deck OLED 1TB NT$17,000 是開放遊戲庫選擇",
            "body": "Steam 美國官網這禮拜砍 NT$3,100 Best Buy 跟進。OLED 面板加 90Hz 更新率加更大電池，把所有 Windows 掌機在這個規格都壓垮，開放 PC 遊戲庫透過 Steam 加上 SteamOS 最佳化，讓價值算數變成繞不過去的入場機會。"
        },
        {
            "title": "Nintendo Switch 2 守 NT$13,900，任天堂從來不降價",
            "body": "任天堂從來不降現役硬體，國殤日週末也沒變。新 DLSS 升頻加獨家瑪利歐、薩爾達、瑪利歐賽車世界的軟體庫，是付牌價的唯一理由，對這群買家來說價值算數鎖死，答案就是現在買。"
        },
        {
            "title": "ROG Xbox Ally X 砍 NT$3,100 到 NT$24,800",
            "body": "Best Buy 國殤日折扣把 ROG Xbox Ally X 配 AMD Z2 Extreme 加 Xbox 應用整合拉進 Xbox Game Pass 訂閱者對的買點區間。雲端切換到家裡 Series X 真的有用，價值算數終於能跟 Steam Deck 在高階 PC 掌機上競爭。"
        }
    ],
)

add(
    "best-gaming-chairs",
    [MD_CNN, {
        "title": "Secretlab Memorial Day 2026 sale",
        "url": "https://secretlab.co/pages/sale",
        "source": "Secretlab",
    }, MD_NBC],
    "Friday morning the gaming chair category had a quiet but meaningful MD opening with Secretlab running the cleanest cut on the Titan Evo. Secretlab Titan Evo 2022 Series holds first at $474 with the $75 cut from Secretlab direct, the modular pillow system plus the magnetic memory foam head pillow plus the 4-way adjustable armrests still makes this the right premium pick under $500, and the $474 sticker is the floor before Black Friday on the Titan Evo. Razer Vantum Gaming Chair at second drops to $549 with the $50 Razer MD cut, the Chroma RGB lumbar plus the ergonomic frame is the right pick for buyers in the Razer ecosystem and the $549 sticker is competitive with Herman Miller without the office-chair aesthetic. Branch Omni Dynamic Ergonomic Chair at third holds $599 with no MD discount, the dynamic motion mechanism plus the office-style aesthetic is the right pick for buyers who want a chair that doubles as a work chair and Branch does not really play the holiday game. Steelcase Series 1 holds fourth at $499 with the Steelcase MD cut of $100, the air-mesh back plus the LiveBack technology is the office-chair pick that handles long gaming sessions without the gaming aesthetic. Herman Miller Embody Gaming holds fifth at $1,795 with no MD discount because Herman Miller refuses to discount the Embody and the $1,795 sticker is the right pick only for buyers who already own an Embody at the office and want the same chair at home. Verdict for Friday: Titan Evo at $474 is the buy of the weekend for traditional gaming aesthetic, Steelcase Series 1 at $499 if you want office-chair ergonomics without the racing-stripe look, Vantum at $549 if you live in the Razer ecosystem and want RGB.",
    [
        {
            "title": "Secretlab Titan Evo at $474 is the gaming chair buy of the weekend",
            "body": "Secretlab direct cut $75 bringing the Titan Evo to $474, the floor before Black Friday. The modular pillow system plus the magnetic head pillow plus the 4-way adjustable armrests still makes this the right premium pick under $500 and the value math against any office-chair competitor is locked."
        },
        {
            "title": "Steelcase Series 1 drops $100 to $499 for ergonomic buyers",
            "body": "The Steelcase MD cut of $100 brings the Series 1 to $499 with the air-mesh back and the LiveBack mechanism. For buyers who want office-chair ergonomics for long gaming sessions without the racing-stripe aesthetic, this is the right alternative to the Titan Evo at the same price."
        },
        {
            "title": "Razer Vantum at $549 wins the RGB ecosystem play",
            "body": "Razer cut $50 on the Vantum bringing it to $549 with the Chroma RGB lumbar lighting plus the ergonomic frame. For buyers locked into the Razer ecosystem who want the lighting synced with the rest of their peripherals, the value math now competes with Herman Miller without the office-chair aesthetic."
        }
    ],
    "禮拜五早上，電競椅這個品類有個安靜但有意義的國殤日開盤，Secretlab 對 Titan Evo 推最乾淨的折扣。\n\nSecretlab Titan Evo 2022 Series 守第一 NT$14,700 靠 Secretlab 美國官網砍 NT$2,300，模組化枕頭系統加磁吸記憶棉頭枕加 4 向可調扶手，還是 NT$15,500 以下對的高階選擇，NT$14,700 就是 Titan Evo 在黑五前的地板。\n\nRazer Vantum Gaming Chair 第二 Razer 國殤日砍 NT$1,500 到 NT$17,000，Chroma RGB 腰靠加人體工學機身，是 Razer 生態裡的買家對的選擇，NT$17,000 跟 Herman Miller 競爭得起又沒有辦公椅美學。Branch Omni Dynamic Ergonomic Chair 第三守 NT$18,600 沒國殤日折扣，動態運動機制加辦公風美學，是想要一張椅子兼當工作椅的買家對的選擇，Branch 不太玩節慶遊戲。\n\n講真的，Steelcase Series 1 第四 Steelcase 國殤日砍 NT$3,100 到 NT$15,500，網布背加 LiveBack 技術，是處理長時間電競又不要賽車條紋的辦公椅選擇。Herman Miller Embody Gaming 第五守 NT$55,600 沒國殤日折扣，Herman Miller 拒絕降 Embody，NT$55,600 是已經辦公室有 Embody 又想在家裡放一張的買家才會選的。\n\n禮拜五結論：傳統電競美學這檔週末買點是 Titan Evo NT$14,700；要辦公椅人體工學沒有賽車條紋就 Steelcase Series 1 NT$15,500；住 Razer 生態要 RGB 就 Vantum NT$17,000。",
    [
        {
            "title": "Secretlab Titan Evo NT$14,700 是電競椅這檔週末買點",
            "body": "Secretlab 美國官網砍 NT$2,300 把 Titan Evo 拉到 NT$14,700，黑五前的地板。模組化枕頭系統加磁吸頭枕加 4 向可調扶手，還是 NT$15,500 以下對的高階選擇，對任何辦公椅競爭對手的價值算數鎖死了。"
        },
        {
            "title": "Steelcase Series 1 砍 NT$3,100 到 NT$15,500 給人體工學買家",
            "body": "Steelcase 國殤日折扣 NT$3,100 把 Series 1 拉到 NT$15,500 配網布背跟 LiveBack 機制。要辦公椅人體工學打長時間電競又不要賽車條紋美學的買家，這個價是 Titan Evo 對的替代方案。"
        },
        {
            "title": "Razer Vantum NT$17,000 贏在 RGB 生態",
            "body": "Razer 砍 NT$1,500 把 Vantum 拉到 NT$17,000 配 Chroma RGB 腰靠加人體工學機身。被鎖在 Razer 生態又要燈光跟其他周邊同步的買家，價值算數現在跟 Herman Miller 競爭得起又沒有辦公椅美學。"
        }
    ],
)

add(
    "best-gaming-headsets",
    [MD_CNN, {
        "title": "SteelSeries Memorial Day deals 2026",
        "url": "https://steelseries.com/sales/memorial-day",
        "source": "SteelSeries",
    }, MD_NBC],
    "Friday morning the gaming headset category opened with SteelSeries running the deepest MD cut on the Arctis Nova Pro line. SteelSeries Arctis Nova Pro Wireless holds first at $279 with the $70 cut from SteelSeries direct, the dual-battery hot-swap system plus the active noise cancellation plus the active GameDAC remains the right premium pick and the $279 sticker is the floor before Black Friday. Audeze Maxwell 2 stays second at $329 with the $20 cut from Audeze, the 90mm planar magnetic drivers plus the wireless plus the 80-hour battery is the right pick for buyers who want true audiophile-grade sound in a gaming form factor, and the price gap to the Arctis is justified by the driver tech. Turtle Beach Stealth Pro II at third drops to $269 with the $60 MD cut from Best Buy, the dual-pack hot-swap battery plus the active noise cancellation plus the multi-platform support is the right pick for cross-platform players who switch between PC, PlayStation, and Xbox, and the value math against the Arctis is competitive. Logitech G Pro X 2 LIGHTSPEED holds fourth at $199 with the $50 cut, the graphene drivers plus the LIGHTSPEED wireless plus the comfort over long sessions is the right pick for esports buyers who care about response time over absolute sound quality. Sony INZONE H9 holds fifth at $249 with the $50 cut, the dual-pickup mic plus the 360 Spatial Sound for Gaming is the right pick for PS5 buyers who want the Sony optimization. Verdict for Friday: Arctis Nova Pro Wireless at $279 is the buy of the weekend for premium gaming audio, Maxwell 2 at $329 if you want audiophile-grade drivers, Stealth Pro II at $269 if you switch platforms daily.",
    [
        {
            "title": "SteelSeries Arctis Nova Pro Wireless at $279 wins the weekend",
            "body": "SteelSeries direct cut $70 bringing the Arctis Nova Pro Wireless to $279, the floor before Black Friday. The dual-battery hot-swap plus the ANC plus the GameDAC is the right premium pick for buyers who want one headset to do everything, and the value math against any competitor at the price is decisive."
        },
        {
            "title": "Audeze Maxwell 2 holds $329 with planar magnetic drivers",
            "body": "Audeze cut $20 on the Maxwell 2 to $329 with the 90mm planar magnetic drivers plus the wireless plus the 80-hour battery. The price gap to the Arctis is justified by the driver tech for buyers who actually want audiophile-grade sound in a gaming form factor, no compromise."
        },
        {
            "title": "Turtle Beach Stealth Pro II drops $60 to $269",
            "body": "Best Buy's MD cut brings the Stealth Pro II to $269 with the dual-pack hot-swap battery plus the multi-platform support. For cross-platform players who switch between PC, PlayStation, and Xbox daily, this is the right pick because the single-headset solution removes the need for separate units per platform."
        }
    ],
    "禮拜五早上，電競耳機這個品類因為 SteelSeries 對 Arctis Nova Pro 線推最深的國殤日折扣而開盤。\n\nSteelSeries Arctis Nova Pro Wireless 守第一 NT$8,700 靠 SteelSeries 美國官網砍 NT$2,200，雙電池熱插拔系統加主動降噪加主動 GameDAC，還是對的高階選擇，NT$8,700 就是黑五前的地板。\n\nAudeze Maxwell 2 第二 Audeze 砍 NT$600 到 NT$10,200，90mm 平面振膜驅動單體加無線加 80 小時電池，是想要真正發燒友等級聲音放在電競外型的買家對的選擇，跟 Arctis 的價差由驅動單體技術正當化。Turtle Beach Stealth Pro II 第三 Best Buy 國殤日砍 NT$1,900 到 NT$8,300，雙電池熱插拔加主動降噪加多平台支援，是 PC、PS、Xbox 每天切換的跨平台玩家對的選擇，價值算數跟 Arctis 競爭得起。\n\n講真的，Logitech G Pro X 2 LIGHTSPEED 第四 NT$6,200 砍 NT$1,500，石墨烯驅動單體加 LIGHTSPEED 無線加長時間舒適，是電競買家在意反應時間勝過絕對音質的對的選擇。Sony INZONE H9 第五 NT$7,700 砍 NT$1,500，雙拾音麥克風加遊戲 360 立體聲，是 PS5 買家要 Sony 最佳化的對的選擇。\n\n禮拜五結論：高階電競音訊這檔週末買點是 Arctis Nova Pro Wireless NT$8,700；要發燒友驅動單體就 Maxwell 2 NT$10,200；每天切換平台就 Stealth Pro II NT$8,300。",
    [
        {
            "title": "SteelSeries Arctis Nova Pro Wireless NT$8,700 贏這週末",
            "body": "SteelSeries 美國官網砍 NT$2,200 把 Arctis Nova Pro Wireless 拉到 NT$8,700，黑五前的地板。雙電池熱插拔加 ANC 加 GameDAC，是想要一支耳機搞定一切的買家對的高階選擇，在這個價對任何競爭對手的價值算數很決定性。"
        },
        {
            "title": "Audeze Maxwell 2 守 NT$10,200 配平面振膜驅動單體",
            "body": "Audeze 砍 NT$600 把 Maxwell 2 拉到 NT$10,200 配 90mm 平面振膜驅動單體加無線加 80 小時電池。跟 Arctis 的價差由驅動單體技術正當化，是真的要在電競外型裡發燒友等級聲音的買家對的選擇，沒妥協。"
        },
        {
            "title": "Turtle Beach Stealth Pro II 砍 NT$1,900 到 NT$8,300",
            "body": "Best Buy 國殤日折扣把 Stealth Pro II 拉到 NT$8,300 配雙電池熱插拔加多平台支援。PC、PS、Xbox 每天切換的跨平台玩家，這個對的選擇，因為一支耳機解掉每個平台買一支的需求。"
        }
    ],
)

add(
    "best-gaming-mice",
    [MD_CNN, {
        "title": "Logitech G Memorial Day 2026 deals",
        "url": "https://www.logitechg.com/en-us/promotions/sale.html",
        "source": "Logitech G",
    }, MD_NBC],
    "Friday morning the gaming mouse category opened with Logitech running the deepest MD weekend cuts on the Pro X line and Razer holding the Viper at MSRP. Logitech G Pro X2 SUPERSTRIKE holds first at $179 with the $50 cut from Logitech G direct, the optical-mechanical hybrid switches plus the HERO 2 sensor at 32,000 DPI plus the 60g weight is the right pick for serious esports buyers and the $179 sticker is the floor for the flagship. Logitech G Pro X Superlight 2 DEX at second drops to $129 with the $30 MD cut, the slimmer DEX shape plus the same HERO 2 sensor at lighter weight is the right pick for claw-grip players who found the standard Superlight too round. Razer Viper V4 Pro at third holds $179 with no MD discount because Razer is letting the Viper V4 stay at MSRP through MD, the Gen-4 optical switches plus the 8K polling rate is genuinely competitive on spec but the no-discount stance hurts the value math against the Pro X2. Glorious Model O 2 Pro Wireless holds fourth at $129 with the $20 cut, the lightweight 58g body plus the 4K polling kit option is the right pick for buyers who want a third-party flagship without the Logitech or Razer brand premium. Pulsar X2H eS holds fifth at $149 with the BAMF 2 switches plus the 26K DPI sensor, the boutique pick for buyers who follow the competitive Korean scene. Verdict for Friday: Pro X2 SUPERSTRIKE at $179 is the buy of the weekend for serious competitive play, Superlight 2 DEX at $129 if you have small hands or claw grip, Model O 2 Pro at $129 if you reject brand premiums. Razer's no-discount stance on the Viper V4 Pro makes the Logitech the obvious value pick.",
    [
        {
            "title": "Logitech G Pro X2 SUPERSTRIKE at $179 is the competitive pick",
            "body": "Logitech G direct cut $50 bringing the Pro X2 SUPERSTRIKE to $179, the floor for the flagship. The optical-mechanical hybrid switches plus the HERO 2 sensor at 32,000 DPI plus the 60g weight makes this the right pick for serious esports buyers and the value math at the price is locked."
        },
        {
            "title": "Razer Viper V4 Pro holds $179 — no discount hurts the value math",
            "body": "Razer is letting the Viper V4 stay at MSRP through MD weekend. The Gen-4 optical switches plus the 8K polling rate is genuinely competitive on spec but the no-discount stance hurts the value math against the Logitech Pro X2 SUPERSTRIKE at the same price with a $50 discount."
        },
        {
            "title": "Logitech Superlight 2 DEX drops $30 to $129 for claw grip",
            "body": "The MD cut on the DEX variant brings it to $129 with the slimmer shape and the same HERO 2 sensor at lighter weight. For claw-grip players who found the standard Superlight too round in the back, the DEX is the right pick and the price is the lowest tracked since launch."
        }
    ],
    "禮拜五早上，電競滑鼠這個品類因為 Logitech 對 Pro X 線推最深的國殤日週末折扣，而 Razer 把 Viper 維持牌價而開盤。\n\nLogitech G Pro X2 SUPERSTRIKE 守第一 NT$5,500 靠 Logitech G 美國官網砍 NT$1,500，光學機械混合微動加 HERO 2 感測器 32,000 DPI 加 60g 重量，是嚴肅電競買家對的選擇，NT$5,500 就是旗艦的地板。\n\nLogitech G Pro X Superlight 2 DEX 第二 NT$4,000 砍 NT$900，更窄的 DEX 形狀加同樣 HERO 2 感測器，是手小或趴爪握法找標準 Superlight 太圓的買家對的選擇。Razer Viper V4 Pro 第三守 NT$5,500 沒國殤日折扣，Razer 讓 Viper V4 整個國殤日守牌價，Gen-4 光學微動加 8K 輪詢率規格上競爭得起，但不打折姿態在同價位的 Pro X2 對比下價值算數受傷。\n\n講真的，Glorious Model O 2 Pro Wireless 第四 NT$4,000 砍 NT$600，輕量化 58g 機身加 4K 輪詢套件選項，是要第三方旗艦沒有 Logitech 或 Razer 品牌溢價的買家對的選擇。Pulsar X2H eS 第五 NT$4,650 配 BAMF 2 微動加 26K DPI 感測器，是追韓國競技圈的精品選擇。\n\n禮拜五結論：嚴肅競技這檔週末買點是 Pro X2 SUPERSTRIKE NT$5,500；手小或趴爪握就 Superlight 2 DEX NT$4,000；拒絕品牌溢價就 Model O 2 Pro NT$4,000。Razer 對 Viper V4 Pro 不打折讓 Logitech 變成明顯的價值選擇。",
    [
        {
            "title": "Logitech G Pro X2 SUPERSTRIKE NT$5,500 是競技選擇",
            "body": "Logitech G 美國官網砍 NT$1,500 把 Pro X2 SUPERSTRIKE 拉到 NT$5,500，旗艦的地板。光學機械混合微動加 HERO 2 感測器 32,000 DPI 加 60g 重量，是嚴肅電競買家對的選擇，在這個價的價值算數鎖死。"
        },
        {
            "title": "Razer Viper V4 Pro 守 NT$5,500 — 不打折讓價值算數受傷",
            "body": "Razer 讓 Viper V4 整個國殤日守牌價。Gen-4 光學微動加 8K 輪詢率規格上競爭得起，但不打折姿態在同價位 Pro X2 SUPERSTRIKE 有 NT$1,500 折扣的對比下，價值算數受傷了。"
        },
        {
            "title": "Logitech Superlight 2 DEX 砍 NT$900 到 NT$4,000 給趴爪握",
            "body": "DEX 版的國殤日折扣把它拉到 NT$4,000 配更窄的形狀跟同樣 HERO 2 感測器更輕重量。趴爪握的玩家找標準 Superlight 後段太圓，DEX 是對的選擇，價格是上市以來追蹤最低。"
        }
    ],
)

add(
    "best-mechanical-keyboards",
    [MD_CNN, {
        "title": "Wooting Memorial Day 2026 sale",
        "url": "https://wooting.io/sale",
        "source": "Wooting",
    }, MD_NBC],
    "Friday morning the mechanical keyboard category opened with Wooting running their first ever Memorial Day weekend sale on the 60HE+ and 80HE. Wooting 60HE+ holds first at $174 with the $20 cut from Wooting direct, the magnetic Lekker switches plus the rapid trigger plus the analog input is genuinely the right pick for competitive FPS players and the $174 sticker is the floor on the 60HE+ that Wooting almost never discounts. Wooting 80HE at second drops to $199 with the $30 MD cut, the TKL form factor plus the same magnetic switches plus the function row makes this the right pick for buyers who want analog input plus full functionality, and the $199 sticker is competitive with the Apex Pro TKL. SteelSeries Apex Pro TKL Wireless holds third at $229 with the $50 cut, the OmniPoint 3.0 magnetic switches plus the wireless plus the OLED display is the right pick for buyers who want premium magnetic switches without the Wooting wait time. Razer Huntsman V3 Pro TKL stays fourth at $179 with the $50 cut, the Gen-2 optical magnetic switches plus the Razer Synapse integration is the right pick for buyers locked into Razer ecosystem. Keychron Q1 Max holds fifth at $219 with the $20 cut, the gasket-mounted aluminum body plus the QMK/VIA firmware support is the right pick for enthusiasts who want hot-swap and full customization without going full custom-built. Verdict for Friday: 60HE+ at $174 is the buy of the weekend for competitive FPS, 80HE at $199 if you need the function row, Apex Pro TKL at $229 if you cannot wait for Wooting shipping. The Wooting MD discount is rare and probably will not repeat until Black Friday.",
    [
        {
            "title": "Wooting 60HE+ at $174 is rare MD discount on the FPS pick",
            "body": "Wooting almost never discounts the 60HE+ outside Black Friday so the $20 MD cut to $174 is the rare buy window. The magnetic Lekker switches plus the rapid trigger plus the analog input is the right competitive FPS pick and the discount is the trigger for buyers who have been waiting."
        },
        {
            "title": "Wooting 80HE drops $30 to $199 for full-size analog",
            "body": "The TKL form factor at $199 with the same magnetic switches plus the function row makes this the right pick for buyers who want analog input but need the function row for work or productivity. The $199 sticker is now genuinely competitive with the Apex Pro TKL Wireless at $50 less."
        },
        {
            "title": "SteelSeries Apex Pro TKL Wireless at $229 has no wait time",
            "body": "Wooting's shipping queue runs weeks and the Apex Pro TKL Wireless at $229 ships from Amazon next day. The OmniPoint 3.0 magnetic switches plus the OLED display is the right pick for buyers who want premium magnetic switches but cannot wait for Wooting shipping, no compromise on the switch tech."
        }
    ],
    "禮拜五早上，機械鍵盤這個品類因為 Wooting 對 60HE+ 跟 80HE 跑他們首次的國殤日週末特賣而開盤。\n\nWooting 60HE+ 守第一 NT$5,400 靠 Wooting 美國官網砍 NT$600，磁力 Lekker 軸加快速觸發加類比輸入，真的是競技 FPS 玩家對的選擇，NT$5,400 就是 Wooting 幾乎不降的 60HE+ 地板。\n\nWooting 80HE 第二國殤日砍 NT$900 到 NT$6,200，TKL 配置加同樣磁力軸加功能列，是要類比輸入加完整功能的買家對的選擇，NT$6,200 跟 Apex Pro TKL 競爭得起。SteelSeries Apex Pro TKL Wireless 第三 NT$7,100 砍 NT$1,500，OmniPoint 3.0 磁力軸加無線加 OLED 顯示器，是要高階磁力軸不想等 Wooting 出貨時間的買家對的選擇。\n\n講真的，Razer Huntsman V3 Pro TKL 第四 NT$5,500 砍 NT$1,500，Gen-2 光學磁力軸加 Razer Synapse 整合，是被鎖在 Razer 生態的買家對的選擇。Keychron Q1 Max 第五 NT$6,800 砍 NT$600，墊圈式鋁機身加 QMK/VIA 韌體支援，是要熱插拔跟完整客製化又不想完全客製組裝的玩家對的選擇。\n\n禮拜五結論：競技 FPS 這檔週末買點是 60HE+ NT$5,400；要功能列就 80HE NT$6,200；不能等 Wooting 出貨就 Apex Pro TKL NT$7,100。Wooting 國殤日折扣很罕見，大概要等黑五才會重來。",
    [
        {
            "title": "Wooting 60HE+ NT$5,400 是 FPS 選擇罕見國殤日折扣",
            "body": "Wooting 在黑五以外幾乎不降 60HE+，這次國殤日砍 NT$600 到 NT$5,400 是罕見買點窗口。磁力 Lekker 軸加快速觸發加類比輸入，是對的競技 FPS 選擇，折扣就是等很久的買家入手的扳機。"
        },
        {
            "title": "Wooting 80HE 砍 NT$900 到 NT$6,200 給全尺寸類比",
            "body": "TKL 配置在 NT$6,200 配同樣磁力軸加功能列，是要類比輸入又需要功能列做工作或生產力的買家對的選擇。NT$6,200 現在真的跟 Apex Pro TKL Wireless 競爭得起，便宜 NT$1,500。"
        },
        {
            "title": "SteelSeries Apex Pro TKL Wireless NT$7,100 沒等貨時間",
            "body": "Wooting 出貨佇列要好幾週，Apex Pro TKL Wireless NT$7,100 從 Amazon 隔日到貨。OmniPoint 3.0 磁力軸加 OLED 顯示器，是要高階磁力軸又不能等 Wooting 出貨的買家對的選擇，軸體技術上沒妥協。"
        }
    ],
)

# ---------- AI ----------

add(
    "best-ai-chatbots",
    [AI_LLMSTATS, AI_TC_GEMINI, AI_FELLO],
    "Friday morning the AI chatbot ranking did not move because the market is in the post-Google IO 2026 settling period. ChatGPT holds first at 9.5 with GPT-5.5 still leading on SWE-bench plus general reasoning since the April 23 release, the 60 percent hallucination drop versus 5.4 is the right pitch and the inclusion of GPT-5.5 Thinking in the $20 Plus tier is genuinely the right pricing move for everyone who was holding out for affordable thinking. Claude stays tied second at 9.3 with Opus 4.7 still neck and neck with GPT-5.5 on SWE-bench, the 1M context plus the Sonnet 4.6 daily driver speed plus the new Memory feature is the right pitch for coding-heavy workflows and the value math against ChatGPT is largely driven by whether you need 1M context. Gemini at 9.3 holds tied second because the Gemini 3.5 Flash plus Gemini Omni Flash both shipped May 21 to AI Plus, Pro, and Ultra subscribers, the new Daily Brief feature plus the Gemini Spark background agent is the right pitch for buyers locked into Google Workspace and the May 22 morning is when those features are first usable in production. Grok 4 holds fourth at 8.8 with the X integration and the speed advantage staying the differentiator, and the value math at $30 per month is competitive for buyers who already pay for X Premium+. DeepSeek V4 Preview at fifth holds 8.5 as the open-source surprise, the 1M context at near-zero API cost is the right pitch for builders who care about cost over peak capability. Verdict for Friday: ChatGPT plus Claude plus Gemini is the three-way tie at the top, pick by ecosystem, and the new Gemini Spark agent is the headline this week.",
    [
        {
            "title": "Gemini 3.5 Flash plus Omni Flash shipped May 21 to all tiers",
            "body": "Google rolled out Gemini 3.5 Flash and Gemini Omni Flash to AI Plus, Pro, and Ultra subscribers yesterday. The Daily Brief feature plus the Gemini Spark background agent is the right pitch for Workspace buyers and Friday morning is when those features become first usable in real workflows."
        },
        {
            "title": "GPT-5.5 Thinking arrives in $20 Plus tier",
            "body": "OpenAI moved GPT-5.5 Thinking from the $200 Pro tier into the $20 Plus tier in late April, which is the genuinely right pricing move for everyone who was holding out for affordable thinking access. The 60 percent hallucination drop versus 5.4 is the headline feature and the price gate finally dropped."
        },
        {
            "title": "Claude Opus 4.7 stays competitive on SWE-bench",
            "body": "Anthropic's Opus 4.7 is still neck and neck with GPT-5.5 on SWE-bench, and the 1M context plus the new Memory feature is the right pitch for coding-heavy workflows. The value math against ChatGPT comes down to whether you actually need 1M context for your typical task, not benchmark scores."
        }
    ],
    "禮拜五早上，AI 聊天機器人榜單沒動，因為市場處在 Google IO 2026 後的沉澱期。\n\nChatGPT 守第一 9.5，GPT-5.5 從 4 月 23 日發表後在 SWE-bench 加一般推理上還是領跑，比 5.4 砍 60% 幻覺是對的話術，把 GPT-5.5 Thinking 放進 NT$620 月費的 Plus 階層，是對所有等實惠 thinking 等很久的人正確的定價動作。\n\nClaude 並列第二 9.3，Opus 4.7 在 SWE-bench 還是跟 GPT-5.5 肉搏，1M context 加 Sonnet 4.6 日常駕駛速度加新 Memory 功能，是寫程式工作流的話術，對 ChatGPT 的價值算數主要看你需不需要 1M context。Gemini 9.3 並列第二，Gemini 3.5 Flash 加 Gemini Omni Flash 5 月 21 日同時推送給 AI Plus、Pro、Ultra 訂閱者，新 Daily Brief 加 Gemini Spark 背景代理人是被鎖在 Google Workspace 買家的話術，5 月 22 日早上就是這些功能在生產環境第一次能用的時候。\n\n講真的，Grok 4 第四守 8.8，X 整合加速度優勢是差異化的支點，月費 NT$930 對已經付 X Premium+ 的買家來說競爭得起。DeepSeek V4 Preview 第五守 8.5 當開源驚喜，1M context 配近乎零成本的 API，是在意成本勝過峰值能力的開發者對的話術。\n\n禮拜五結論：ChatGPT 加 Claude 加 Gemini 是頂端三方並列，按生態選，Gemini Spark 新代理人是這禮拜頭條。",
    [
        {
            "title": "Gemini 3.5 Flash 加 Omni Flash 5 月 21 日推送給所有階層",
            "body": "Google 昨天把 Gemini 3.5 Flash 跟 Gemini Omni Flash 推給 AI Plus、Pro、Ultra 訂閱者。Daily Brief 加 Gemini Spark 背景代理人是 Workspace 買家的話術，禮拜五早上就是這些功能在真實工作流第一次能用的時候。"
        },
        {
            "title": "GPT-5.5 Thinking 進駐 NT$620 月費 Plus 階層",
            "body": "OpenAI 4 月底把 GPT-5.5 Thinking 從 NT$6,200 Pro 階層搬到 NT$620 Plus 階層，是對所有等實惠 thinking 訪問等很久的人對的定價動作。比 5.4 砍 60% 幻覺是頭條功能，價格門檻終於倒下。"
        },
        {
            "title": "Claude Opus 4.7 在 SWE-bench 上繼續競爭",
            "body": "Anthropic 的 Opus 4.7 在 SWE-bench 還是跟 GPT-5.5 肉搏，1M context 加新 Memory 功能是寫程式工作流的話術。對 ChatGPT 的價值算數歸結到你日常任務是否真的需要 1M context，不是基準分數。"
        }
    ],
)

add(
    "best-ai-coding-assistants",
    [AI_LLMSTATS, AI_FELLO, {
        "title": "Claude Code vs Cursor 2026 comparison",
        "url": "https://www.swebench.com/",
        "source": "SWE-bench",
    }],
    "Friday morning the AI coding assistant ranking is in the post-GPT-5.5 plus Opus 4.7 settling period and the market is now genuinely three-way competitive. Claude Code holds first at 9.3 because the Opus 4.7 model plus the 1M context plus the new Memory feature plus the recent terminal-native UX redesign makes this still the right pick for serious engineering work, and the value math at $20 per month for the Pro tier is locked. Cursor stays second at 9.0 with the new Cursor Agents feature plus the Cursor Tab 2 autocomplete plus the model picker that handles GPT-5.5 plus Opus 4.7 plus Gemini in one UI, the IDE-first approach is genuinely the right pitch for buyers who refuse to leave VS Code keybindings, and the $20 per month price plus the unlimited slow requests is the right value bracket. OpenAI Codex at third holds 8.6 with the GPT-5.5 Codex variant plus the deeper ChatGPT integration, the value math for ChatGPT Plus subscribers is decent but the agentic execution still lags Claude Code on benchmarks. Aider holds fourth at 8.4 as the open-source CLI play with multi-model support, the right pick for buyers who refuse vendor lock-in. GitHub Copilot Pro+ stays fifth at 8.3 with the Copilot Workspace agent that handles full PR generation, the integration into GitHub native flow is the right pitch for enterprise buyers and the $39 per month price is the right value for teams already deep in GitHub. Verdict for Friday: Claude Code at $20 is the buy for serious engineering, Cursor at $20 if you live in VS Code, Copilot Pro+ at $39 if your team is already in GitHub workflow. No big launches this week so the rankings hold.",
    [
        {
            "title": "Claude Code holds first with terminal-native UX redesign",
            "body": "Anthropic shipped the terminal-native UX redesign for Claude Code in early May plus the new Memory feature persists context across sessions. The Opus 4.7 model plus the 1M context plus the deeper agentic execution still makes this the right pick for serious engineering work at $20 per month."
        },
        {
            "title": "Cursor stays competitive with multi-model picker",
            "body": "Cursor's model picker handles GPT-5.5 plus Opus 4.7 plus Gemini in one UI without vendor lock-in, and the new Cursor Agents feature plus Cursor Tab 2 autocomplete makes the IDE-first approach the right pick for buyers who refuse to leave VS Code keybindings. The $20 per month bracket is the right value."
        },
        {
            "title": "GitHub Copilot Pro+ wins on enterprise integration",
            "body": "Copilot Workspace agent handles full PR generation inside the GitHub native flow, which is the right pitch for enterprise buyers whose teams are already deep in GitHub. The $39 per month price is the right value for teams who would rather pay for integration than swap toolchains, no need to leave the platform."
        }
    ],
    "禮拜五早上，AI 寫程式助手榜單處在 GPT-5.5 加 Opus 4.7 後的沉澱期，市場現在真的是三方競爭。\n\nClaude Code 守第一 9.3，因為 Opus 4.7 模型加 1M context 加新 Memory 功能加最近終端原生 UX 重設計，還是嚴肅工程工作的正確選擇，月費 NT$620 Pro 階層的價值算數鎖死。\n\nCursor 第二守 9.0，新 Cursor Agents 功能加 Cursor Tab 2 自動完成加同時處理 GPT-5.5 加 Opus 4.7 加 Gemini 的模型選擇器，IDE 優先的路線是拒絕離開 VS Code 鍵盤綁定的買家對的話術，月費 NT$620 加無限慢請求是對的價值區間。OpenAI Codex 第三守 8.6 配 GPT-5.5 Codex 變體加更深的 ChatGPT 整合，對 ChatGPT Plus 訂閱者的價值算數還可以，但代理執行還是在基準上落後 Claude Code。\n\n講真的，Aider 第四守 8.4 當開源 CLI 玩家配多模型支援，是拒絕廠商鎖定的買家對的選擇。GitHub Copilot Pro+ 第五守 8.3 配 Copilot Workspace 代理人處理完整 PR 產生，整合進 GitHub 原生流程是企業買家的話術，月費 NT$1,210 對已經在 GitHub 工作流深處的團隊是對的價值。\n\n禮拜五結論：嚴肅工程買 Claude Code NT$620；住 VS Code 就 Cursor NT$620；團隊已在 GitHub 工作流就 Copilot Pro+ NT$1,210。這禮拜沒大發表所以排名守住。",
    [
        {
            "title": "Claude Code 守第一配終端原生 UX 重設計",
            "body": "Anthropic 五月初推送 Claude Code 終端原生 UX 重設計加新 Memory 功能跨工作階段保存上下文。Opus 4.7 模型加 1M context 加更深的代理執行，還是讓這個在嚴肅工程工作上是對的選擇，月費 NT$620。"
        },
        {
            "title": "Cursor 靠多模型選擇器繼續競爭",
            "body": "Cursor 模型選擇器在一個 UI 裡同時處理 GPT-5.5 加 Opus 4.7 加 Gemini 沒有廠商鎖定，新 Cursor Agents 功能加 Cursor Tab 2 自動完成，讓 IDE 優先路線變成拒絕離開 VS Code 鍵盤綁定的買家對的選擇。月費 NT$620 是對的價值區間。"
        },
        {
            "title": "GitHub Copilot Pro+ 在企業整合上贏",
            "body": "Copilot Workspace 代理人在 GitHub 原生流程內處理完整 PR 產生，是團隊已在 GitHub 深處的企業買家對的話術。月費 NT$1,210 對寧可付整合錢也不想換工具鏈的團隊是對的價值，不必離開平台。"
        }
    ],
)

add(
    "best-ai-image-generators",
    [AI_LLMSTATS, AI_FELLO, {
        "title": "Midjourney V8 vs Flux 2 Pro vs GPT Image 2 comparison",
        "url": "https://artificialanalysis.ai/text-to-image",
        "source": "Artificial Analysis",
    }],
    "Friday morning the AI image generator ranking is in the post-Midjourney V8 settling period and the rankings held flat. Midjourney V8 holds first at 9.4 because the new V8 model that shipped April 30 plus the deeper style consistency plus the now-native web app makes this still the right pick for serious creative work, and the $10 per month entry tier is the right value bracket for buyers who actually produce images for client work. Flux 2 Pro at second holds 9.2 with the new control net suite plus the open-weights variant plus the API pricing at $0.045 per image, which is the right pitch for builders who want studio-grade output with API access and the value math against Midjourney is decent for developers who need control over the generation pipeline. GPT Image 2 stays third at 9.1 with the GPT-5.5 integration plus the new text rendering accuracy plus the multi-turn refinement makes this the right pick for buyers locked into ChatGPT Plus who do not want a separate subscription. Recraft V3 holds fourth at 8.8, the vector output mode plus the brand kit features is the right pick for buyers doing logo and brand work who need editable output rather than rasterized JPEG. Ideogram 3.0 stays fifth at 8.6 with the text rendering plus typography focus, the right pick for buyers who do poster and social-media work where text accuracy matters. Verdict for Friday: Midjourney V8 at $10 is the buy for creative work, Flux 2 Pro if you need API access, GPT Image 2 if you already pay for ChatGPT Plus. No big launches this week.",
    [
        {
            "title": "Midjourney V8 holds first with style consistency upgrade",
            "body": "The V8 model shipped April 30 with deeper style consistency plus the now-native web app removing the Discord requirement. For serious creative work the $10 per month entry tier is the right value bracket and the value math against Flux 2 Pro is locked for buyers who actually produce images for client deliverables."
        },
        {
            "title": "Flux 2 Pro at $0.045 per image wins on API economics",
            "body": "Flux 2 Pro's API pricing at $0.045 per image plus the new control net suite plus the open-weights variant is the right pitch for builders who want studio-grade output with API access. The value math against Midjourney is decent for developers who need control over the generation pipeline rather than the artist UI."
        },
        {
            "title": "GPT Image 2 wins on bundled ChatGPT Plus value",
            "body": "GPT Image 2 with the GPT-5.5 integration plus the new text rendering accuracy plus the multi-turn refinement is included in ChatGPT Plus at $20 per month with no extra subscription. For buyers already paying for ChatGPT this is the right pick because the marginal cost of image generation is zero."
        }
    ],
    "禮拜五早上，AI 圖像產生器榜單處在 Midjourney V8 後的沉澱期，名次橫盤。\n\nMidjourney V8 守第一 9.4，因為 4 月 30 日推送的 V8 模型加更深的風格一致性加現在原生網頁應用程式，還是嚴肅創意工作對的選擇，月費 NT$310 入門階層是真的會為客戶案子做圖的買家對的價值區間。\n\nFlux 2 Pro 第二守 9.2 配新控制網套件加開放權重版加 API 定價每張 NT$1.4，是要工作室等級輸出加 API 訪問的開發者對的話術，對 Midjourney 的價值算數對需要控制產生流程的開發者站得住。GPT Image 2 第三守 9.1 配 GPT-5.5 整合加新文字渲染準確度加多輪改良，是被鎖在 ChatGPT Plus 不想另外訂閱的買家對的選擇。\n\n講真的，Recraft V3 第四守 8.8，向量輸出模式加品牌套件功能，是做 logo 跟品牌工作要可編輯輸出而不是點陣 JPEG 的買家對的選擇。Ideogram 3.0 第五守 8.6 配文字渲染加排版聚焦，是做海報跟社群媒體工作在意文字準確度的買家對的選擇。\n\n禮拜五結論：創意工作買 Midjourney V8 NT$310；要 API 訪問就 Flux 2 Pro；已付 ChatGPT Plus 就 GPT Image 2。這禮拜沒大發表。",
    [
        {
            "title": "Midjourney V8 守第一配風格一致性升級",
            "body": "V8 模型 4 月 30 日推送配更深風格一致性加現在原生網頁應用程式拿掉 Discord 要求。嚴肅創意工作月費 NT$310 入門階層是對的價值區間，對 Flux 2 Pro 的價值算數對真的會為客戶交付做圖的買家鎖死。"
        },
        {
            "title": "Flux 2 Pro 每張 NT$1.4 在 API 經濟上贏",
            "body": "Flux 2 Pro API 定價每張 NT$1.4 加新控制網套件加開放權重版，是要工作室等級輸出加 API 訪問的開發者對的話術。對 Midjourney 的價值算數對需要控制產生流程而不是藝術家 UI 的開發者站得住。"
        },
        {
            "title": "GPT Image 2 贏在 ChatGPT Plus 綑綁價值",
            "body": "GPT Image 2 配 GPT-5.5 整合加新文字渲染準確度加多輪改良，包進 ChatGPT Plus 月費 NT$620 不必加訂閱。已經付 ChatGPT 的買家這個對的選擇，因為圖像產生的邊際成本是零。"
        }
    ],
)

add(
    "best-ai-video-generators",
    [AI_LLMSTATS, AI_FELLO, {
        "title": "Veo 3.1 vs Runway Gen-4.5 vs Kling 3.0 comparison",
        "url": "https://artificialanalysis.ai/text-to-video",
        "source": "Artificial Analysis",
    }],
    "Friday morning the AI video generator ranking is in the post-Veo 3.1 settling period and the rankings held flat with one notable shift on Sora discontinuation. Veo 3.1 holds first at 9.5 because the Google DeepMind model plus the native audio synthesis plus the 1080p at 60fps output plus the Vertex AI plus consumer access through Gemini Ultra makes this still the right pick for serious video work, and the value math at $250 per month for the Ultra tier is the right bracket for production buyers. Runway Gen-4.5 stays second at 9.3 with the new motion brush plus the act-one performance capture plus the multi-shot generation makes this the right pick for filmmakers who need control over framing and composition, and the $35 per month entry tier is the right value for indie creators. Kling 3.0 holds third at 9.2 with the China-first model from Kuaishou, the longer 2-minute clips plus the deeper camera control makes this the right pick for buyers who need extended sequences without cut-and-stitch workflows, and the value math at $8 per month is decisive. Pika 2.5 holds fourth at 8.9 with the new sound effects model plus the lip sync, the right pick for buyers doing short-form social media work. Note: Sora 2 was discontinued April 26 by OpenAI with the API following in September, which is why it has dropped out of consideration entirely. Verdict for Friday: Veo 3.1 at $250 is the buy for production video, Runway Gen-4.5 at $35 if you need filmmaker control, Kling 3.0 at $8 if you need long clips on budget.",
    [
        {
            "title": "Veo 3.1 holds first with native audio synthesis",
            "body": "Google DeepMind's Veo 3.1 plus the native audio synthesis plus the 1080p at 60fps output plus the Vertex AI access plus consumer access through Gemini Ultra makes this still the right pick for serious video work. The $250 per month Ultra tier is the right bracket for production buyers who actually deliver client work."
        },
        {
            "title": "Sora 2 discontinued April 26 — dropped from consideration",
            "body": "OpenAI killed Sora 2 on April 26 with the API following in September. The model dropped out of consideration entirely because there is no future path for buyers, and the share of the production video market that Sora 2 held has shifted to Veo 3.1 and Runway Gen-4.5."
        },
        {
            "title": "Kling 3.0 at $8 per month wins on long-clip budget",
            "body": "Kuaishou's Kling 3.0 with the 2-minute clips plus the deeper camera control plus the $8 per month price is the right pick for buyers who need extended sequences without cut-and-stitch workflows. For social-first creators on a budget, the value math against Veo and Runway is decisive."
        }
    ],
    "禮拜五早上，AI 影片產生器榜單處在 Veo 3.1 後的沉澱期，名次橫盤，Sora 停運是唯一明顯位移。\n\nVeo 3.1 守第一 9.5，因為 Google DeepMind 模型加原生音訊合成加 1080p 60fps 輸出加 Vertex AI 加透過 Gemini Ultra 的消費者訪問，還是嚴肅影片工作對的選擇，Ultra 階層月費 NT$7,750 是製作買家對的區間。\n\nRunway Gen-4.5 第二守 9.3 配新動態筆刷加 act-one 表演捕捉加多鏡頭產生，是要對構圖跟取景有控制的電影製作對的選擇，月費 NT$1,090 入門階層是獨立創作者對的價值。Kling 3.0 第三守 9.2 配快手中國優先模型，更長 2 分鐘片段加更深鏡頭控制，是要延伸序列又不要剪切縫合工作流的買家對的選擇，月費 NT$250 的價值算數很決定性。\n\n講真的，Pika 2.5 第四守 8.9 配新音效模型加對嘴同步，是做短影音社群媒體工作的買家對的選擇。註：Sora 2 4 月 26 日被 OpenAI 停運，API 9 月跟進，所以完全退出考慮。\n\n禮拜五結論：製作影片買 Veo 3.1 NT$7,750；要電影製作控制就 Runway Gen-4.5 NT$1,090；預算內要長片段就 Kling 3.0 NT$250。",
    [
        {
            "title": "Veo 3.1 守第一配原生音訊合成",
            "body": "Google DeepMind 的 Veo 3.1 加原生音訊合成加 1080p 60fps 輸出加 Vertex AI 訪問加透過 Gemini Ultra 的消費者訪問，還是嚴肅影片工作對的選擇。Ultra 階層月費 NT$7,750 是真的會交付客戶工作的製作買家對的區間。"
        },
        {
            "title": "Sora 2 4 月 26 日停運，退出考慮",
            "body": "OpenAI 4 月 26 日把 Sora 2 停運，API 9 月跟進。模型完全退出考慮，因為買家沒有未來路徑，Sora 2 在製作影片市場的份額已經轉移到 Veo 3.1 跟 Runway Gen-4.5。"
        },
        {
            "title": "Kling 3.0 月費 NT$250 在長片段預算上贏",
            "body": "快手的 Kling 3.0 配 2 分鐘片段加更深鏡頭控制加月費 NT$250，是要延伸序列又不要剪切縫合工作流的買家對的選擇。對社群優先預算內創作者來說，對 Veo 跟 Runway 的價值算數很決定性。"
        }
    ],
)

add(
    "best-ai-meeting-assistants",
    [AI_LLMSTATS, AI_FELLO, {
        "title": "Best AI meeting assistants 2026 comparison",
        "url": "https://www.granola.ai/",
        "source": "Granola",
    }],
    "Friday morning the AI meeting assistant ranking held flat in a category that the Google IO 2026 Daily Brief feature is starting to disrupt. Granola holds first at 9.1 because the local-first transcription plus the human-style template editing plus the integration with Notion, Linear, and Slack makes this the right pick for serious knowledge workers, and the value math at $20 per month for unlimited transcription is the right bracket. Fathom stays second at 9.0 with the free unlimited transcription plus the highlights feature plus the deep CRM integration, the right pick for sales teams and the value math against Granola is decisive for buyers who only need basic transcription plus action items. Fireflies.ai at third holds 8.6 with the deeper integration into Salesforce plus HubSpot, the right pick for enterprise sales orgs that already run those CRMs and the $18 per month price is the right enterprise value. Otter.ai holds fourth at 8.4 with the live captioning plus the longer history retention, the right pick for journalists and researchers who care about searchable transcript archives. Notion AI Meeting Notes stays fifth at 8.2 as the bundled play for buyers already paying for Notion AI, the value math is locked because the marginal cost is zero. Watch the Google Daily Brief feature that shipped May 21 because it threatens to commoditize the bottom half of this ranking for Workspace buyers. Verdict for Friday: Granola at $20 for knowledge workers, Fathom free for sales, Fireflies $18 for enterprise CRM-locked buyers.",
    [
        {
            "title": "Granola holds first with local-first transcription",
            "body": "The local-first transcription plus the human-style template editing plus the integration with Notion, Linear, and Slack makes this the right pick for serious knowledge workers. The $20 per month unlimited tier is the right bracket and the value math against Fireflies plus Otter is locked for buyers who care about template quality."
        },
        {
            "title": "Fathom free tier wins for sales teams",
            "body": "Free unlimited transcription plus the highlights feature plus the deep CRM integration is the right pick for sales teams who need basic transcription plus action items without paying for premium features. The value math against Granola is decisive for sales-only buyers who do not need template flexibility."
        },
        {
            "title": "Google Daily Brief threatens bottom half of category",
            "body": "Gemini's Daily Brief feature shipped May 21 to all AI Plus, Pro, and Ultra subscribers and threatens to commoditize transcription plus summarization for Workspace buyers. Otter and Notion AI Meeting Notes are the most exposed because the Daily Brief covers their core feature set at no marginal cost."
        }
    ],
    "禮拜五早上，AI 會議助手榜單橫盤，Google IO 2026 的 Daily Brief 功能開始攪局這個品類。\n\nGranola 守第一 9.1，因為本地優先轉寫加類人類範本編輯加跟 Notion、Linear、Slack 整合，是嚴肅知識工作者對的選擇，月費 NT$620 無限轉寫是對的區間。\n\nFathom 第二守 9.0 配免費無限轉寫加 highlights 功能加深度 CRM 整合，是業務團隊對的選擇，對 Granola 的價值算數對只需要基本轉寫加待辦的買家很決定性。Fireflies.ai 第三守 8.6 配 Salesforce 加 HubSpot 更深的整合，是已經在跑這些 CRM 的企業業務組對的選擇，月費 NT$560 是對的企業價值。\n\n講真的，Otter.ai 第四守 8.4 配即時字幕加更長歷史保存，是在意可搜尋逐字稿存檔的記者跟研究者對的選擇。Notion AI Meeting Notes 第五守 8.2 當已付 Notion AI 的買家的綑綁玩家，價值算數鎖死，因為邊際成本是零。注意 5 月 21 日推送的 Google Daily Brief 功能，因為它威脅把這品類下半商品化給 Workspace 買家。\n\n禮拜五結論：知識工作者買 Granola NT$620；業務團隊 Fathom 免費；企業被 CRM 鎖的買家 Fireflies NT$560。",
    [
        {
            "title": "Granola 守第一配本地優先轉寫",
            "body": "本地優先轉寫加類人類範本編輯加跟 Notion、Linear、Slack 整合，是嚴肅知識工作者對的選擇。月費 NT$620 無限階層是對的區間，對 Fireflies 加 Otter 的價值算數對在意範本品質的買家鎖死。"
        },
        {
            "title": "Fathom 免費階層贏業務團隊",
            "body": "免費無限轉寫加 highlights 功能加深度 CRM 整合，是只要基本轉寫加待辦不想付高階功能的業務團隊對的選擇。對 Granola 的價值算數對純業務不需要範本彈性的買家很決定性。"
        },
        {
            "title": "Google Daily Brief 威脅這品類下半",
            "body": "Gemini 的 Daily Brief 5 月 21 日推送給所有 AI Plus、Pro、Ultra 訂閱者，威脅把轉寫加摘要對 Workspace 買家商品化。Otter 跟 Notion AI Meeting Notes 暴露最大，因為 Daily Brief 覆蓋他們核心功能集而且邊際成本零。"
        }
    ],
)

add(
    "best-ai-voice-generators",
    [AI_LLMSTATS, AI_FELLO, {
        "title": "Best AI voice generators 2026 comparison",
        "url": "https://elevenlabs.io/",
        "source": "ElevenLabs",
    }],
    "Friday morning the AI voice generator ranking held flat as the category continues to mature around the ElevenLabs leadership position. ElevenLabs holds first at 9.4 because the Multilingual v2 model plus the voice cloning plus the new Voice Library marketplace plus the API at $0.18 per 1k characters makes this still the right pick for serious voice work, and the value math at $22 per month for the Creator tier is the right bracket for content creators who actually ship audio content. Hume AI Octave 2 stays second at 9.0 with the empathic voice plus the emotion-aware synthesis plus the API access, the right pick for buyers who need expressive performance for character voices and audio drama. MiniMax Speech 02 HD at third holds 8.8 with the China-first model that supports Chinese plus English plus the longer-form synthesis, the right pick for buyers doing bilingual content who need both languages from one model. Resemble AI holds fourth at 8.5 with the voice cloning plus the real-time API, the right pick for enterprise buyers building voice agents and call-center applications. OpenAI Voice through ChatGPT stays fifth at 8.3 as the bundled play for ChatGPT Plus subscribers, the value math is locked because the marginal cost is zero for buyers already paying for Plus. Verdict for Friday: ElevenLabs at $22 for content creators, Hume Octave 2 if you need empathic performance, MiniMax Speech for bilingual work.",
    [
        {
            "title": "ElevenLabs holds first with Voice Library marketplace",
            "body": "The Multilingual v2 model plus the voice cloning plus the new Voice Library marketplace plus the API at $0.18 per 1k characters makes this still the right pick for serious voice work. The $22 per month Creator tier is the right bracket for content creators who actually ship audio content."
        },
        {
            "title": "Hume AI Octave 2 wins on empathic performance",
            "body": "Hume's Octave 2 model with the empathic voice plus the emotion-aware synthesis is the right pick for buyers who need expressive performance for character voices and audio drama. The API access at competitive pricing plus the emotion-control parameters separates this from the flat-delivery competitors."
        },
        {
            "title": "MiniMax Speech 02 HD wins bilingual Chinese-English work",
            "body": "MiniMax's Speech 02 HD supports Chinese plus English in the same model with the longer-form synthesis, which is the right pick for buyers doing bilingual content who need both languages from one model. For Asian-market content creators the value math against ElevenLabs is decisive."
        }
    ],
    "禮拜五早上，AI 語音產生器榜單橫盤，這品類繼續圍繞 ElevenLabs 領導地位成熟。\n\nElevenLabs 守第一 9.4，因為 Multilingual v2 模型加語音克隆加新 Voice Library 市集加 API 每 1k 字元 NT$5.6，還是嚴肅語音工作對的選擇，Creator 階層月費 NT$680 是真的會出音訊內容的內容創作者對的區間。\n\nHume AI Octave 2 第二守 9.0 配同理心聲音加情緒感知合成加 API 訪問，是要角色配音跟音訊劇有表現力演出的買家對的選擇。MiniMax Speech 02 HD 第三守 8.8 配中國優先模型同時支援中英文加更長形式合成，是做雙語內容需要兩種語言用同一個模型的買家對的選擇。\n\n講真的，Resemble AI 第四守 8.5 配語音克隆加即時 API，是建語音代理人跟客服中心應用的企業買家對的選擇。OpenAI Voice 透過 ChatGPT 第五守 8.3 當 ChatGPT Plus 訂閱者的綑綁玩家，價值算數鎖死，因為對已付 Plus 的買家邊際成本是零。\n\n禮拜五結論：內容創作者買 ElevenLabs NT$680；要同理心表演就 Hume Octave 2；做雙語工作就 MiniMax Speech。",
    [
        {
            "title": "ElevenLabs 守第一配 Voice Library 市集",
            "body": "Multilingual v2 模型加語音克隆加新 Voice Library 市集加 API 每 1k 字元 NT$5.6，還是嚴肅語音工作對的選擇。Creator 階層月費 NT$680 是真的會出音訊內容的內容創作者對的區間。"
        },
        {
            "title": "Hume AI Octave 2 在同理心表演上贏",
            "body": "Hume 的 Octave 2 模型配同理心聲音加情緒感知合成，是要角色配音跟音訊劇有表現力演出的買家對的選擇。API 訪問配競爭定價加情緒控制參數，把這個跟平直發音的競爭對手分開。"
        },
        {
            "title": "MiniMax Speech 02 HD 贏中英文雙語工作",
            "body": "MiniMax 的 Speech 02 HD 在同一個模型支援中英文加更長形式合成，是做雙語內容需要兩種語言用同一個模型的買家對的選擇。對亞洲市場內容創作者來說，對 ElevenLabs 的價值算數很決定性。"
        }
    ],
)

add(
    "best-ai-music-generators",
    [AI_LLMSTATS, AI_FELLO, {
        "title": "Suno V5 vs Eleven Music vs Udio comparison",
        "url": "https://suno.com/",
        "source": "Suno",
    }],
    "Friday morning the AI music generator ranking held flat as the category settles around Suno V5 dominance after the spring release. Suno V5 holds first at 9.5 because the new V5 model that shipped April plus the deeper instrument separation plus the lyrics-aware composition plus the now-native stem export makes this still the right pick for serious music creators, and the value math at $10 per month for the Pro tier is the right bracket. Eleven Music stays second at 9.1 with the ElevenLabs music model that ships with the same API plus the better vocal naturalness plus the longer compositions, the right pick for buyers who need both voice and music from one vendor. Udio at third holds 8.7 with the high-fidelity output plus the deeper genre coverage plus the longer 4-minute compositions, the right pick for buyers who need long-form pieces and care about audiophile output quality. Riffusion holds fourth at 8.4 with the open-source community-driven model, the right pick for builders who refuse subscription pricing. Stable Audio 3.0 stays fifth at 8.2 with the Stability AI commercial license plus the API access, the right pick for commercial buyers who need the license cleared for ad and sync work. Verdict for Friday: Suno V5 at $10 for creators, Eleven Music if you already pay for ElevenLabs voice, Udio for long-form audiophile pieces. No big launches this week so the ranking is locked.",
    [
        {
            "title": "Suno V5 holds first with stem export plus lyrics-aware composition",
            "body": "The V5 model that shipped April with the deeper instrument separation plus the lyrics-aware composition plus the now-native stem export makes this still the right pick for serious music creators. The $10 per month Pro tier is the right bracket and the value math against Udio is locked."
        },
        {
            "title": "Eleven Music wins on one-vendor voice plus music play",
            "body": "ElevenLabs' Eleven Music ships with the same API as their voice product plus the better vocal naturalness plus the longer compositions. For buyers who need both voice and music from one vendor the consolidation play is the right pick and the value math against running two subscriptions is decisive."
        },
        {
            "title": "Udio wins long-form 4-minute audiophile pieces",
            "body": "Udio's high-fidelity output plus the deeper genre coverage plus the longer 4-minute compositions is the right pick for buyers who need long-form pieces and care about audiophile output quality. The value math for film scoring and longer-form work is where Udio actually beats Suno V5."
        }
    ],
    "禮拜五早上，AI 音樂產生器榜單橫盤，這品類在春季發表後圍繞 Suno V5 主導地位沉澱。\n\nSuno V5 守第一 9.5，因為 4 月推送的新 V5 模型加更深樂器分離加歌詞感知作曲加現在原生分軌匯出，還是嚴肅音樂創作者對的選擇，Pro 階層月費 NT$310 是對的區間。\n\nEleven Music 第二守 9.1 配 ElevenLabs 音樂模型用同一個 API 加更好人聲自然度加更長作曲，是要從同一個廠商拿到語音跟音樂的買家對的選擇。Udio 第三守 8.7 配高保真輸出加更深類型覆蓋加更長 4 分鐘作曲，是要長形式作品又在意發燒友輸出品質的買家對的選擇。\n\n講真的，Riffusion 第四守 8.4 配開源社群驅動模型，是拒絕訂閱定價的開發者對的選擇。Stable Audio 3.0 第五守 8.2 配 Stability AI 商用授權加 API 訪問，是要授權釐清做廣告跟同步工作的商業買家對的選擇。\n\n禮拜五結論：創作者買 Suno V5 NT$310；已付 ElevenLabs 語音就 Eleven Music；要長形式發燒友作品就 Udio。這禮拜沒大發表所以排名鎖死。",
    [
        {
            "title": "Suno V5 守第一配分軌匯出加歌詞感知作曲",
            "body": "4 月推送的 V5 模型配更深樂器分離加歌詞感知作曲加現在原生分軌匯出，還是嚴肅音樂創作者對的選擇。Pro 階層月費 NT$310 是對的區間，對 Udio 的價值算數鎖死。"
        },
        {
            "title": "Eleven Music 贏在單一廠商語音加音樂玩法",
            "body": "ElevenLabs 的 Eleven Music 跟他們語音產品用同一個 API 加更好人聲自然度加更長作曲。要從同一個廠商拿到語音跟音樂的買家整合玩法是對的選擇，對跑兩個訂閱的價值算數很決定性。"
        },
        {
            "title": "Udio 贏長形式 4 分鐘發燒友作品",
            "body": "Udio 高保真輸出加更深類型覆蓋加更長 4 分鐘作曲，是要長形式作品又在意發燒友輸出品質的買家對的選擇。電影配樂跟長形式工作的價值算數，這就是 Udio 真的贏過 Suno V5 的地方。"
        }
    ],
)

# ---------- KITCHEN ----------

add(
    "best-air-fryers",
    [MD_KITCHN, MD_CNN, MD_NBC],
    "Friday morning the air fryer category opened with Ninja running the deepest MD weekend cut on the Foodi DZ550 dual-zone line. Ninja Foodi DZ550 DualZone XL holds first at $179 with the $50 cut from Best Buy this morning, the dual basket plus the 10-quart total capacity plus the Smart Cook system makes this the right pick for families and the $179 sticker is the floor for the DZ550 outside Prime Day. Cosori TurboBlaze 9-in-1 stays second at $109 with the $40 MD cut, the 6-quart capacity plus the 9 cooking functions plus the quieter operation is the right pick for couples or small families and the value math at $109 is decisive against the Instant Vortex Plus. Typhur Dome 2 at third holds $399 with no MD discount because Typhur does not really play the holiday game, the premium build plus the deeper convection is the right pick for buyers who want commercial-grade output without the commercial footprint, and the value math is locked at MSRP. Breville Smart Oven Air Fryer holds fourth at $349 with the $50 Williams Sonoma MD cut, the toaster oven plus the air fryer combo plus the Element IQ heating is the right pick for buyers who want one appliance to replace toaster, air fryer, and small oven. Instant Vortex Plus stays fifth at $99 as the budget pick with the $30 MD cut, the 6-quart basket plus the OdorErase technology is the right pick for first-time air fryer buyers. Verdict for Friday: Foodi DZ550 at $179 for families, Cosori TurboBlaze at $109 for singles and couples, Breville Smart Oven at $349 if you want the toaster-oven combo. The dual-zone DZ550 cut is the deepest of the weekend.",
    [
        {
            "title": "Ninja Foodi DZ550 at $179 is the family-size buy of the weekend",
            "body": "Best Buy cut $50 bringing the DZ550 to $179, the floor outside Prime Day. The dual basket plus the 10-quart total capacity plus the Smart Cook system makes this the right pick for families who actually cook two dishes simultaneously and the value math against any single-basket competitor at the price is locked."
        },
        {
            "title": "Cosori TurboBlaze drops $40 to $109",
            "body": "The MD cut on the TurboBlaze brings it to $109 with the 6-quart capacity plus the 9 cooking functions plus the quieter operation. For couples or small families this is the right pick and the value math at $109 is decisive against the Instant Vortex Plus which sits at $99 with a smaller basket and noisier operation."
        },
        {
            "title": "Breville Smart Oven Air Fryer at $349 replaces three appliances",
            "body": "Williams Sonoma's $50 MD cut brings the Breville Smart Oven Air Fryer to $349 with the toaster oven plus the air fryer combo plus the Element IQ heating. For buyers with limited counter space who want one appliance to replace toaster, air fryer, and small oven, this is the right consolidation play."
        }
    ],
    "禮拜五早上，氣炸鍋這個品類因為 Ninja 對 Foodi DZ550 雙籃線推最深的國殤日週末折扣而開盤。\n\nNinja Foodi DZ550 DualZone XL 守第一 NT$5,500 靠 Best Buy 今天早上砍 NT$1,500，雙籃加 10 夸脫總容量加智慧烹飪系統，是家庭對的選擇，NT$5,500 就是 DZ550 在 Prime Day 以外的地板。\n\nCosori TurboBlaze 9-in-1 第二 NT$3,400 砍 NT$1,200，6 夸脫容量加 9 種烹飪功能加更安靜運轉，是情侶或小家庭對的選擇，NT$3,400 的價值算數對 Instant Vortex Plus 很決定性。Typhur Dome 2 第三守 NT$12,400 沒國殤日折扣，Typhur 不太玩節慶遊戲，高階做工加更深對流，是要商用級輸出又不要商用體積的買家對的選擇，價值算數鎖在牌價。\n\n講真的，Breville Smart Oven Air Fryer 第四 Williams Sonoma 國殤日砍 NT$1,500 到 NT$10,800，烤箱加氣炸鍋加 Element IQ 加熱組合，是想要一台取代烤箱、氣炸鍋跟小烤箱的買家對的選擇。Instant Vortex Plus 第五當預算選擇 NT$3,100 砍 NT$900，6 夸脫籃加 OdorErase 技術，是第一次買氣炸鍋的人對的選擇。\n\n禮拜五結論：家庭買 Foodi DZ550 NT$5,500；單身情侶 Cosori TurboBlaze NT$3,400；要烤箱組合就 Breville Smart Oven NT$10,800。雙籃 DZ550 折扣是這週末最深的。",
    [
        {
            "title": "Ninja Foodi DZ550 NT$5,500 是家庭尺寸這檔週末買點",
            "body": "Best Buy 砍 NT$1,500 把 DZ550 拉到 NT$5,500，Prime Day 以外的地板。雙籃加 10 夸脫總容量加智慧烹飪系統，是真的會同時煮兩道菜的家庭對的選擇，在這個價對任何單籃競爭對手的價值算數鎖死。"
        },
        {
            "title": "Cosori TurboBlaze 砍 NT$1,200 到 NT$3,400",
            "body": "國殤日對 TurboBlaze 的折扣把它拉到 NT$3,400 配 6 夸脫容量加 9 種烹飪功能加更安靜運轉。情侶或小家庭這個對的選擇，NT$3,400 的價值算數對 NT$3,100 但更小籃更吵的 Instant Vortex Plus 很決定性。"
        },
        {
            "title": "Breville Smart Oven Air Fryer NT$10,800 取代三台家電",
            "body": "Williams Sonoma 砍 NT$1,500 把 Breville Smart Oven Air Fryer 拉到 NT$10,800 配烤箱加氣炸鍋加 Element IQ 加熱。檯面空間有限想要一台取代烤箱、氣炸鍋跟小烤箱的買家，這個整合玩法對。"
        }
    ],
)

add(
    "best-coffee-makers",
    [MD_KITCHN, MD_CNN, {
        "title": "Williams Sonoma Memorial Day 2026 kitchen deals",
        "url": "https://www.williams-sonoma.com/shop/sale/",
        "source": "Williams Sonoma",
    }],
    "Friday morning the coffee maker category opened with Moccamaster running their first ever MD weekend cut on the KBGV Select. Moccamaster KBGV Select holds first at $309 with the $40 cut from Williams Sonoma direct, the SCA-certified brewer plus the copper boiling element plus the 5-year warranty makes this still the right pick for serious coffee drinkers and the $309 sticker is the floor outside Black Friday on the KBGV. Breville Precision Brewer Thermal (BDC450) at second drops to $279 with the $50 MD cut, the SCA-certified brewer plus the thermal carafe plus the gold cup standard temperature is the right pick for buyers who want SCA certification at a lower price than the Moccamaster. Fellow Aiden Precision Coffee Maker at third holds $345 with no MD discount because Fellow does not really play the holiday game, the SCA-certified brewer plus the per-brew profile customization plus the deep app integration is the right pick for nerd buyers who want to dial in by bean and the value math is locked at MSRP. OXO Brew 9-Cup holds fourth at $179 with the $20 cut, the SCA-certified brewer plus the rainmaker shower head is the right entry-level SCA pick. Ninja Specialty Coffee Maker stays fifth at $109 with the $30 MD cut as the multi-function budget pick. Verdict for Friday: KBGV Select at $309 is the buy of the weekend for serious coffee, Precision Brewer Thermal at $279 if you want thermal carafe, Aiden at $345 if you want app control. Williams Sonoma is running the deepest cuts so check their full sale page.",
    [
        {
            "title": "Moccamaster KBGV Select at $309 is the serious coffee buy",
            "body": "Williams Sonoma cut $40 bringing the KBGV Select to $309, the floor outside Black Friday. The SCA-certified brewer plus the copper boiling element plus the 5-year warranty is the right pick for serious coffee drinkers and the value math against any electric drip competitor at the price is locked."
        },
        {
            "title": "Breville Precision Brewer Thermal drops $50 to $279",
            "body": "The MD cut on the BDC450 brings the thermal carafe variant to $279 with the SCA-certified brewer plus the gold cup standard temperature. For buyers who want SCA certification at a lower price than the Moccamaster but with the thermal carafe to hold heat for hours, this is the right pick."
        },
        {
            "title": "Fellow Aiden holds $345 — app control nerd pick",
            "body": "Fellow does not discount the Aiden during holiday weekends. The SCA-certified brewer plus the per-brew profile customization plus the deep app integration is the right pick for nerd buyers who want to dial in by bean variety, and the value math is locked at MSRP for buyers who actually use the app features."
        }
    ],
    "禮拜五早上，咖啡機這個品類因為 Moccamaster 對 KBGV Select 推首次國殤日週末折扣而開盤。\n\nMoccamaster KBGV Select 守第一 NT$9,600 靠 Williams Sonoma 砍 NT$1,200，SCA 認證沖煮加銅煮水元件加 5 年保固，還是嚴肅咖啡人對的選擇，NT$9,600 就是 KBGV 在黑五以外的地板。\n\nBreville Precision Brewer Thermal (BDC450) 第二 NT$8,700 國殤日砍 NT$1,500，SCA 認證沖煮加保溫壺加金杯標準溫度，是要 SCA 認證又不要 Moccamaster 價的買家對的選擇。Fellow Aiden Precision Coffee Maker 第三守 NT$10,700 沒國殤日折扣，Fellow 不太玩節慶遊戲，SCA 認證沖煮加每次沖煮設定檔自訂加深度應用程式整合，是要按豆子精調的怪咖買家對的選擇，價值算數鎖在牌價。\n\n講真的，OXO Brew 9-Cup 第四 NT$5,500 砍 NT$600，SCA 認證沖煮加雨灑頭，是入門 SCA 選擇。Ninja Specialty Coffee Maker 第五 NT$3,400 砍 NT$900 當多功能預算選擇。\n\n禮拜五結論：嚴肅咖啡買 KBGV Select NT$9,600；要保溫壺就 Precision Brewer Thermal NT$8,700；要應用程式控制就 Aiden NT$10,700。Williams Sonoma 跑最深折扣，看完整特賣頁。",
    [
        {
            "title": "Moccamaster KBGV Select NT$9,600 是嚴肅咖啡買點",
            "body": "Williams Sonoma 砍 NT$1,200 把 KBGV Select 拉到 NT$9,600，黑五以外的地板。SCA 認證沖煮加銅煮水元件加 5 年保固，是嚴肅咖啡人對的選擇，在這個價對任何電動滴漏競爭對手的價值算數鎖死。"
        },
        {
            "title": "Breville Precision Brewer Thermal 砍 NT$1,500 到 NT$8,700",
            "body": "BDC450 的國殤日折扣把保溫壺版拉到 NT$8,700 配 SCA 認證沖煮加金杯標準溫度。要 SCA 認證又不要 Moccamaster 價的買家加保溫壺保溫好幾小時，這個對的選擇。"
        },
        {
            "title": "Fellow Aiden 守 NT$10,700 — 應用程式控制怪咖選擇",
            "body": "Fellow 在節日週末不降 Aiden 的價。SCA 認證沖煮加每次沖煮設定檔自訂加深度應用程式整合，是按豆子品種精調的怪咖買家對的選擇，對真的會用應用程式功能的買家來說價值算數鎖在牌價。"
        }
    ],
)

add(
    "best-rice-cookers",
    [MD_KITCHN, MD_CNN, {
        "title": "Zojirushi Memorial Day 2026 sale",
        "url": "https://www.zojirushi.com/",
        "source": "Zojirushi",
    }],
    "Friday morning the rice cooker category opened with Zojirushi and Tiger running their first MD weekend cuts on the IH lineup. Zojirushi Induction Heating NP-HCC10 holds first at $359 with the $40 cut from Williams Sonoma, the platinum infused inner pan plus the IH technology plus the 5-cup capacity makes this still the right pick for serious Asian-rice eaters and the $359 sticker is the floor outside Black Friday. Tiger JKT-D10U IH Stainless at second drops to $299 with the $40 MD cut, the IH technology plus the stainless interior plus the Tacook synchro-cooking insert is the right pick for buyers who want IH at a lower price than Zojirushi. Zojirushi Neuro Fuzzy NS-ZCC10 at third holds $199 with no MD discount, the micro-computerized fuzzy logic plus the 5-cup capacity is the right pick for buyers who want Zojirushi quality without the IH price premium and the value math is locked. Cuckoo CRP-LHTR0609F holds fourth at $279 with the $30 cut, the twin pressure plus the IH heating plus the Korean focus on japchae and brown rice is the right pick for Korean cuisine focused buyers. Aroma Housewares Digital stays fifth at $59 as the budget pick. Verdict for Friday: NP-HCC10 at $359 is the buy of the weekend for serious Japanese rice, JKT-D10U at $299 if you want IH at lower price, NS-ZCC10 at $199 if you want Zojirushi without IH premium.",
    [
        {
            "title": "Zojirushi NP-HCC10 at $359 is the serious rice buy",
            "body": "Williams Sonoma cut $40 bringing the NP-HCC10 to $359, the floor outside Black Friday on the IH model. The platinum-infused inner pan plus the IH technology plus the 5-cup capacity makes this the right pick for serious Asian-rice eaters and the value math against any non-IH competitor is locked."
        },
        {
            "title": "Tiger JKT-D10U IH Stainless drops $40 to $299",
            "body": "The MD cut on the JKT-D10U brings it to $299 with the IH technology plus the stainless interior plus the Tacook synchro-cooking insert. For buyers who want IH at a lower price than Zojirushi and like the Tacook feature for simultaneous main-and-rice cooking, this is the right pick at the price."
        },
        {
            "title": "Zojirushi Neuro Fuzzy NS-ZCC10 holds $199",
            "body": "The micro-computerized fuzzy logic plus the 5-cup capacity is the right pick for buyers who want Zojirushi quality without the IH price premium. At $199 with no MD discount the value math is locked because the Neuro Fuzzy is already the right entry-level Zojirushi pick at full price."
        }
    ],
    "禮拜五早上，電鍋這個品類因為 Zojirushi 跟 Tiger 對 IH 線推首次國殤日週末折扣而開盤。\n\nZojirushi Induction Heating NP-HCC10 守第一 NT$11,100 靠 Williams Sonoma 砍 NT$1,200，鉑金內鍋加 IH 技術加 5 杯容量，還是嚴肅吃日式米的人對的選擇，NT$11,100 就是黑五以外的地板。\n\nTiger JKT-D10U IH Stainless 第二 NT$9,300 國殤日砍 NT$1,200，IH 技術加不鏽鋼內膽加 Tacook 同步烹飪內插，是要 IH 但不要 Zojirushi 價的買家對的選擇。Zojirushi Neuro Fuzzy NS-ZCC10 第三守 NT$6,200 沒國殤日折扣，微電腦模糊邏輯加 5 杯容量，是要 Zojirushi 品質但不要 IH 溢價的買家對的選擇，價值算數鎖死。\n\n講真的，Cuckoo CRP-LHTR0609F 第四 NT$8,700 砍 NT$900，雙重加壓加 IH 加熱加韓系針對韓式雜菜跟糙米，是韓式料理聚焦買家對的選擇。Aroma Housewares Digital 第五 NT$1,800 當預算選擇。\n\n禮拜五結論：嚴肅日式米買 NP-HCC10 NT$11,100；要 IH 低價就 JKT-D10U NT$9,300；要 Zojirushi 不要 IH 溢價就 NS-ZCC10 NT$6,200。",
    [
        {
            "title": "Zojirushi NP-HCC10 NT$11,100 是嚴肅米買點",
            "body": "Williams Sonoma 砍 NT$1,200 把 NP-HCC10 拉到 NT$11,100，IH 機種黑五以外的地板。鉑金內鍋加 IH 技術加 5 杯容量，是嚴肅吃日式米的人對的選擇，對任何非 IH 競爭對手的價值算數鎖死。"
        },
        {
            "title": "Tiger JKT-D10U IH 不鏽鋼砍 NT$1,200 到 NT$9,300",
            "body": "JKT-D10U 的國殤日折扣把它拉到 NT$9,300 配 IH 技術加不鏽鋼內膽加 Tacook 同步烹飪內插。要 IH 但不要 Zojirushi 價又喜歡 Tacook 功能同時煮主菜跟米的買家，這個價對的選擇。"
        },
        {
            "title": "Zojirushi Neuro Fuzzy NS-ZCC10 守 NT$6,200",
            "body": "微電腦模糊邏輯加 5 杯容量，是要 Zojirushi 品質又不要 IH 溢價的買家對的選擇。NT$6,200 沒國殤日折扣價值算數鎖死，因為 Neuro Fuzzy 在牌價就已經是入門級 Zojirushi 對的選擇。"
        }
    ],
)

add(
    "best-portable-ice-makers",
    [MD_KITCHN, MD_CNN, MD_NBC],
    "Friday morning the portable ice maker category opened with GE Profile running their MD weekend cut on the Opal line which is the headline of the category. GE Profile Opal 2.0 Nugget holds first at $499 with the $80 cut from GE direct, the Sonic Ice nugget output plus the WiFi connection plus the side tank for 3-day production makes this still the right pick for nugget ice lovers and the $499 sticker is the floor outside Black Friday on the Opal 2.0. GE Profile Opal 2.0 with Side Tank at second holds $549 with the $50 cut, the same Opal 2.0 plus the larger reservoir for buyers who hate refilling, the right pick for daily-volume buyers. Frigidaire Countertop Ice Maker 86150 at third drops to $129 with the $40 MD cut, the chewable bullet ice plus the 26-pound daily output is the right pick for buyers who want lots of ice fast without paying for nugget. NewAir ClearIce 40 holds fourth at $199 with the $50 cut, the crystal clear cube ice plus the 40-pound daily output is the right pick for cocktail buyers who actually care about ice clarity. Igloo IGLICEB26HNSS stays fifth at $149 as the budget bullet ice pick. Verdict for Friday: Opal 2.0 at $499 for nugget lovers, Frigidaire 86150 at $129 for high-volume bullet ice, NewAir ClearIce at $199 for cocktail clarity. GE rarely discounts the Opal so the $499 floor is the right window.",
    [
        {
            "title": "GE Profile Opal 2.0 Nugget at $499 is rare MD discount",
            "body": "GE rarely discounts the Opal 2.0 outside Black Friday so the $80 MD cut to $499 is the right buy window. The Sonic Ice nugget output plus the WiFi connection plus the side tank for 3-day production makes this still the right pick for nugget ice lovers and the value math is locked at the price."
        },
        {
            "title": "Frigidaire 86150 at $129 wins high-volume bullet ice",
            "body": "The MD cut on the 86150 brings it to $129 with the chewable bullet ice plus the 26-pound daily output. For buyers who want lots of ice fast without paying for nugget production, this is the right pick at the price and the value math against any portable competitor is decisive."
        },
        {
            "title": "NewAir ClearIce 40 at $199 wins cocktail clarity",
            "body": "NewAir's $50 MD cut brings the ClearIce 40 to $199 with the crystal clear cube ice plus the 40-pound daily output. For cocktail buyers who actually care about ice clarity for whiskey rocks and aesthetic drinks, this is the right pick and the value math against the standard Frigidaire is justified by the clarity output."
        }
    ],
    "禮拜五早上，攜帶式製冰機這個品類因為 GE Profile 對 Opal 線推國殤日週末折扣而開盤，這就是這品類的頭條。\n\nGE Profile Opal 2.0 Nugget 守第一 NT$15,500 靠 GE 美國官網砍 NT$2,500，Sonic Ice 雪花冰輸出加 WiFi 連線加側邊水箱支撐 3 天產冰，還是雪花冰愛好者對的選擇，NT$15,500 就是 Opal 2.0 在黑五以外的地板。\n\nGE Profile Opal 2.0 with Side Tank 第二守 NT$17,000 砍 NT$1,500，一樣的 Opal 2.0 加更大水箱給討厭加水的買家，是日量買家對的選擇。Frigidaire Countertop Ice Maker 86150 第三 NT$4,000 國殤日砍 NT$1,200，可咬子彈冰加每日 26 磅輸出，是要快速大量冰又不為雪花冰付錢的買家對的選擇。\n\n講真的，NewAir ClearIce 40 第四 NT$6,200 砍 NT$1,500，水晶清澈方冰加每日 40 磅輸出，是真的在意冰的清澈度的調酒買家對的選擇。Igloo IGLICEB26HNSS 第五 NT$4,650 當預算子彈冰選擇。\n\n禮拜五結論：雪花冰愛好者買 Opal 2.0 NT$15,500；要大量子彈冰就 Frigidaire 86150 NT$4,000；要調酒清澈度就 NewAir ClearIce NT$6,200。GE 很少降 Opal 所以 NT$15,500 地板是對的窗口。",
    [
        {
            "title": "GE Profile Opal 2.0 Nugget NT$15,500 是罕見國殤日折扣",
            "body": "GE 在黑五以外很少降 Opal 2.0，所以國殤日砍 NT$2,500 到 NT$15,500 是對的買點窗口。Sonic Ice 雪花冰輸出加 WiFi 連線加側邊水箱支撐 3 天產冰，還是雪花冰愛好者對的選擇，在這個價的價值算數鎖死。"
        },
        {
            "title": "Frigidaire 86150 NT$4,000 贏大量子彈冰",
            "body": "86150 的國殤日折扣把它拉到 NT$4,000 配可咬子彈冰加每日 26 磅輸出。要快速大量冰又不為雪花冰產量付錢的買家，這個價對的選擇，對任何攜帶式競爭對手的價值算數很決定性。"
        },
        {
            "title": "NewAir ClearIce 40 NT$6,200 贏調酒清澈度",
            "body": "NewAir 國殤日砍 NT$1,500 把 ClearIce 40 拉到 NT$6,200 配水晶清澈方冰加每日 40 磅輸出。真的在意冰的清澈度做威士忌大冰塊跟美學飲料的調酒買家，這個對的選擇，對標準 Frigidaire 的價值算數由清澈度輸出正當化。"
        }
    ],
)

add(
    "best-outdoor-griddles",
    [MD_HD, MD_CNN, {
        "title": "Blackstone Memorial Day 2026 sale",
        "url": "https://blackstoneproducts.com/",
        "source": "Blackstone",
    }],
    "Friday morning the outdoor griddle category opened with the deepest MD weekend cuts of the year as Blackstone and Camp Chef ran aggressive grill-season pricing. Camp Chef Gridiron 36 holds first at $649 with the $150 cut from Home Depot, the propane plus the 4-burner setup plus the steel griddle plate plus the side shelves makes this still the right pick for serious outdoor cookers and the $649 sticker is the floor before grilling-season peak. Blackstone Original 36 Omnivore Griddle with Hood at second drops to $497 with the $100 MD cut from Walmart, the 36-inch griddle plus the hood for retained heat plus the side shelves is the right pick for buyers who want Blackstone reliability at lower price than the Camp Chef. Traeger Flatrock 3 Zone at third holds $899 with the $100 cut, the 3-zone heat plus the Traeger app integration plus the steel construction is the right pick for buyers locked into the Traeger ecosystem and the value math is locked at the premium price. Blackstone XL 36-inch Original holds fourth at $397 with the $100 cut as the budget Blackstone pick. Pit Boss Ultimate Plancha 5-Burner stays fifth at $549 with the $100 cut as the cross-shopping alternative to the Camp Chef. Verdict for Friday: Gridiron 36 at $649 is the buy of the weekend for serious cooks, Blackstone Original with Hood at $497 if you want hood-retained heat, XL 36 at $397 if budget matters more than features. MD weekend through Monday is the floor of the year before fall grilling deals.",
    [
        {
            "title": "Camp Chef Gridiron 36 at $649 is the serious cook buy",
            "body": "Home Depot cut $150 bringing the Gridiron 36 to $649, the floor before grilling-season peak. The propane plus the 4-burner setup plus the steel griddle plate plus the side shelves makes this the right pick for serious outdoor cookers and the value math against any Blackstone at the price is decisive."
        },
        {
            "title": "Blackstone Original 36 with Hood drops $100 to $497",
            "body": "Walmart's MD cut brings the 36-inch Original with Hood to $497 with the hood for retained heat plus the side shelves. For buyers who want Blackstone reliability at a lower price than the Camp Chef and need the hood for steam cooking and smash burgers, this is the right pick at the price."
        },
        {
            "title": "Traeger Flatrock 3 Zone holds $899 — locked-ecosystem premium",
            "body": "Traeger cut $100 on the Flatrock 3 Zone but kept the $899 premium. The 3-zone heat plus the Traeger app integration plus the steel construction is the right pick for buyers locked into the Traeger ecosystem who want the app handoff to the smoker, and the value math is locked at the premium price."
        }
    ],
    "禮拜五早上，戶外鐵板燒這個品類因為 Blackstone 跟 Camp Chef 對烤肉季積極推價而開盤，跑出今年最深的國殤日週末折扣。\n\nCamp Chef Gridiron 36 守第一 NT$20,100 靠 Home Depot 砍 NT$4,650，丙烷加 4 爐頭配置加鋼鐵板加側邊架，還是嚴肅戶外烹飪人對的選擇，NT$20,100 就是烤肉季高峰前的地板。\n\nBlackstone Original 36 Omnivore Griddle with Hood 第二 NT$15,400 在 Walmart 國殤日砍 NT$3,100，36 吋鐵板加保溫罩加側邊架，是要 Blackstone 可靠度又不要 Camp Chef 價的買家對的選擇。Traeger Flatrock 3 Zone 第三守 NT$27,900 砍 NT$3,100，3 區火力加 Traeger 應用程式整合加鋼鐵結構，是被鎖在 Traeger 生態的買家對的選擇，價值算數鎖在高階價。\n\n講真的，Blackstone XL 36-inch Original 第四 NT$12,300 砍 NT$3,100 當預算 Blackstone 選擇。Pit Boss Ultimate Plancha 5-Burner 第五 NT$17,000 砍 NT$3,100 當 Camp Chef 跨比較替代方案。\n\n禮拜五結論：嚴肅烹飪買 Gridiron 36 NT$20,100；要保溫罩就 Blackstone Original with Hood NT$15,400；預算重要勝過功能就 XL 36 NT$12,300。國殤日週末到禮拜一是秋季烤肉折扣前今年的地板。",
    [
        {
            "title": "Camp Chef Gridiron 36 NT$20,100 是嚴肅烹飪買點",
            "body": "Home Depot 砍 NT$4,650 把 Gridiron 36 拉到 NT$20,100，烤肉季高峰前的地板。丙烷加 4 爐頭加鋼鐵板加側邊架，是嚴肅戶外烹飪人對的選擇，在這個價對任何 Blackstone 的價值算數很決定性。"
        },
        {
            "title": "Blackstone Original 36 with Hood 砍 NT$3,100 到 NT$15,400",
            "body": "Walmart 國殤日折扣把 36 吋 Original with Hood 拉到 NT$15,400 配保溫罩加側邊架。要 Blackstone 可靠度又不要 Camp Chef 價的買家加保溫罩做蒸氣烹飪跟壓扁漢堡，這個價對的選擇。"
        },
        {
            "title": "Traeger Flatrock 3 Zone 守 NT$27,900 — 鎖生態高階",
            "body": "Traeger 砍 Flatrock 3 Zone NT$3,100 但守 NT$27,900 高階價。3 區火力加 Traeger 應用程式整合加鋼鐵結構，是被鎖在 Traeger 生態要切換到煙燻機的買家對的選擇，價值算數鎖在高階。"
        }
    ],
)

add(
    "best-dishwashers",
    [MD_HD, MD_LG, MD_ABC],
    "Friday morning the dishwasher category opened with Bosch and Miele running their first major MD weekend cuts on premium dishwashers and this is the buy window of the year. Bosch Benchmark Series SHP9PCM5N holds first at $1,499 with the $400 cut from Home Depot, the third rack PrecisionWash plus the CrystalDry plus the 39 dB noise level makes this still the right pick for serious kitchen upgraders and the $1,499 sticker is the floor before the fall cycle. Miele G 7156 SCVi SF at second drops to $1,799 with the $300 MD cut, the AutoDos automatic detergent dispensing plus the 38 dB noise level plus the German construction is the right pick for buyers who want premium build quality at lower price than the Benchmark. Bosch 800 Series SHX78CM5N at third holds $1,199 with the $300 cut, the third rack plus the CrystalDry plus the 42 dB noise level is the right pick for buyers who want Bosch quality without the Benchmark price premium. KitchenAid KDTM704LPA holds fourth at $1,099 with the $300 cut, the third rack plus the ProDry plus the 39 dB noise is the right pick for buyers who want kitchen appliance brand consistency with KitchenAid. GE Profile UltraFresh PDT785SYNFS stays fifth at $899 with the $300 cut as the value pick. Verdict for Friday: Benchmark at $1,499 for serious upgraders, Miele G 7156 at $1,799 for premium German build, 800 Series at $1,199 for Bosch without Benchmark premium. The Home Depot dishwasher floor through Monday is the lowest of 2026 so far.",
    [
        {
            "title": "Bosch Benchmark SHP9PCM5N at $1,499 is the upgrader buy",
            "body": "Home Depot cut $400 bringing the Benchmark to $1,499, the floor before the fall cycle. The third rack PrecisionWash plus the CrystalDry plus the 39 dB noise level makes this the right pick for serious kitchen upgraders and the value math against any non-Bosch premium competitor is locked at the price."
        },
        {
            "title": "Miele G 7156 SCVi SF drops $300 to $1,799",
            "body": "The MD cut on the Miele brings the G 7156 to $1,799 with the AutoDos automatic detergent dispensing plus the 38 dB noise level plus the German construction. For buyers who want premium build quality at lower price than the Benchmark and the AutoDos convenience, this is the right pick at the price."
        },
        {
            "title": "Bosch 800 Series SHX78CM5N at $1,199 wins on value",
            "body": "Bosch cut $300 on the 800 Series bringing it to $1,199 with the third rack plus the CrystalDry plus the 42 dB noise level. For buyers who want Bosch quality without the Benchmark price premium and accept the small noise gap, the value math is decisive at the price."
        }
    ],
    "禮拜五早上，洗碗機這個品類因為 Bosch 跟 Miele 對高階洗碗機推首次主要國殤日週末折扣而開盤，這就是今年的買點窗口。\n\nBosch Benchmark Series SHP9PCM5N 守第一 NT$46,500 靠 Home Depot 砍 NT$12,400，第三層 PrecisionWash 加 CrystalDry 加 39 分貝噪音，還是嚴肅廚房升級買家對的選擇，NT$46,500 就是秋季週期前的地板。\n\nMiele G 7156 SCVi SF 第二 NT$55,800 國殤日砍 NT$9,300，AutoDos 自動洗碗精給料加 38 分貝噪音加德國工藝，是要高階做工但不要 Benchmark 價的買家對的選擇。Bosch 800 Series SHX78CM5N 第三守 NT$37,200 砍 NT$9,300，第三層加 CrystalDry 加 42 分貝噪音，是要 Bosch 品質又不要 Benchmark 溢價的買家對的選擇。\n\n講真的，KitchenAid KDTM704LPA 第四 NT$34,100 砍 NT$9,300，第三層加 ProDry 加 39 分貝噪音，是要廚房家電品牌跟 KitchenAid 一致的買家對的選擇。GE Profile UltraFresh PDT785SYNFS 第五 NT$27,900 砍 NT$9,300 當價值選擇。\n\n禮拜五結論：嚴肅升級買 Benchmark NT$46,500；要高階德國工藝就 Miele G 7156 NT$55,800；要 Bosch 不要 Benchmark 溢價就 800 Series NT$37,200。Home Depot 洗碗機到禮拜一的地板是 2026 到目前為止最低。",
    [
        {
            "title": "Bosch Benchmark SHP9PCM5N NT$46,500 是升級買點",
            "body": "Home Depot 砍 NT$12,400 把 Benchmark 拉到 NT$46,500，秋季週期前的地板。第三層 PrecisionWash 加 CrystalDry 加 39 分貝噪音，是嚴肅廚房升級買家對的選擇，對任何非 Bosch 高階競爭對手的價值算數在這個價鎖死。"
        },
        {
            "title": "Miele G 7156 SCVi SF 砍 NT$9,300 到 NT$55,800",
            "body": "Miele 國殤日折扣把 G 7156 拉到 NT$55,800 配 AutoDos 自動洗碗精給料加 38 分貝噪音加德國工藝。要高階做工又不要 Benchmark 價的買家加 AutoDos 便利，這個價對的選擇。"
        },
        {
            "title": "Bosch 800 Series SHX78CM5N NT$37,200 在價值上贏",
            "body": "Bosch 砍 800 Series NT$9,300 把它拉到 NT$37,200 配第三層加 CrystalDry 加 42 分貝噪音。要 Bosch 品質又不要 Benchmark 溢價的買家接受小幅噪音差距，價值算數在這個價很決定性。"
        }
    ],
)

# ---------- HOME / WELLNESS ----------

add(
    "best-air-purifiers",
    [MD_CNN, MD_NBC, {
        "title": "Coway Memorial Day 2026 sale",
        "url": "https://cowaymega.com/",
        "source": "Coway",
    }],
    "Friday morning the air purifier category opened with Coway and Blueair running their MD weekend cuts on the flagship units which makes the spring allergy-season buy window finally aligned with deepest discounts. IQAir HealthPro Plus holds first at $899 with the $100 cut from IQAir direct, the medical-grade HyperHEPA filtration plus the swiss-engineered design plus the 5-year warranty makes this still the right pick for serious allergy sufferers and the $899 sticker is one of the rare IQAir MD weekend cuts. Coway Airmega 400S at second drops to $549 with the $100 MD cut, the dual filtration plus the 1,560 sq ft coverage plus the WiFi makes this still the right pick for buyers who want medical-quality output without paying IQAir money. Blueair HealthProtect 7470i at third holds $749 with the $100 cut, the HEPASilent technology plus the GermShield 24/7 plus the SpiralAir output is the right pick for buyers who want Blueair build quality in the Swedish style. Levoit Vital 200S holds fourth at $179 with the $50 cut, the 360-degree air intake plus the smart app plus the value pricing is the right pick for buyers who want decent output at budget price. Mila Air Purifier stays fifth at $399 with the $50 cut for buyers who want the design-focused boutique brand. Verdict for Friday: HealthPro Plus at $899 for serious allergy sufferers, Airmega 400S at $549 for value medical-quality, Vital 200S at $179 if you just need decent output cheap.",
    [
        {
            "title": "IQAir HealthPro Plus at $899 is rare MD discount",
            "body": "IQAir rarely runs MD weekend cuts so the $100 off to $899 is the right buy window for serious allergy sufferers. The medical-grade HyperHEPA filtration plus the swiss-engineered design plus the 5-year warranty makes this the right pick at the price and the value math against any competitor at the price is locked."
        },
        {
            "title": "Coway Airmega 400S drops $100 to $549",
            "body": "The MD cut on the Airmega 400S brings it to $549 with the dual filtration plus the 1,560 sq ft coverage plus the WiFi. For buyers who want medical-quality output without paying IQAir money and the large-room coverage matters, this is the right pick at the price and the value math is decisive against the HealthProtect."
        },
        {
            "title": "Levoit Vital 200S at $179 is the budget output pick",
            "body": "Levoit's $50 MD cut brings the Vital 200S to $179 with the 360-degree air intake plus the smart app. For buyers who want decent output at budget price without paying for medical-grade filtration or large-room coverage, this is the right pick and the value math at $179 is decisive against any sub-$200 competitor."
        }
    ],
    "禮拜五早上，空氣清淨機這個品類因為 Coway 跟 Blueair 對旗艦機型推國殤日週末折扣，讓春季過敏季的買點窗口跟最深折扣終於對齊。\n\nIQAir HealthPro Plus 守第一 NT$27,900 靠 IQAir 美國官網砍 NT$3,100，醫療級 HyperHEPA 過濾加瑞士工程設計加 5 年保固，還是嚴肅過敏患者對的選擇，NT$27,900 是 IQAir 國殤日週末罕見的折扣之一。\n\nCoway Airmega 400S 第二 NT$17,000 國殤日砍 NT$3,100，雙重過濾加 1,560 平方呎覆蓋加 WiFi，還是要醫療級輸出又不要付 IQAir 錢的買家對的選擇。Blueair HealthProtect 7470i 第三守 NT$23,200 砍 NT$3,100，HEPASilent 技術加 GermShield 24/7 加 SpiralAir 輸出，是要 Blueair 瑞典做工的買家對的選擇。\n\n講真的，Levoit Vital 200S 第四 NT$5,500 砍 NT$1,500，360 度進氣加智慧應用程式加價值定價，是要不錯輸出在預算價的買家對的選擇。Mila Air Purifier 第五 NT$12,400 砍 NT$1,500 是要設計聚焦精品品牌的買家對的選擇。\n\n禮拜五結論：嚴肅過敏患者買 HealthPro Plus NT$27,900；要價值醫療級就 Airmega 400S NT$17,000；要便宜不錯的輸出就 Vital 200S NT$5,500。",
    [
        {
            "title": "IQAir HealthPro Plus NT$27,900 是罕見國殤日折扣",
            "body": "IQAir 很少跑國殤日週末折扣，所以砍 NT$3,100 到 NT$27,900 是嚴肅過敏患者對的買點窗口。醫療級 HyperHEPA 過濾加瑞士工程設計加 5 年保固，是這個價的對的選擇，對任何競爭對手的價值算數鎖死。"
        },
        {
            "title": "Coway Airmega 400S 砍 NT$3,100 到 NT$17,000",
            "body": "Airmega 400S 的國殤日折扣把它拉到 NT$17,000 配雙重過濾加 1,560 平方呎覆蓋加 WiFi。要醫療級輸出又不要付 IQAir 錢的買家加大房間覆蓋重要，這個價對的選擇，價值算數對 HealthProtect 很決定性。"
        },
        {
            "title": "Levoit Vital 200S NT$5,500 是預算輸出選擇",
            "body": "Levoit 國殤日砍 NT$1,500 把 Vital 200S 拉到 NT$5,500 配 360 度進氣加智慧應用程式。要不錯輸出在預算價又不付醫療級過濾或大房間覆蓋錢的買家，這個對的選擇，NT$5,500 的價值算數對任何 NT$6,000 以下競爭對手很決定性。"
        }
    ],
)

add(
    "best-robot-vacuums",
    [MD_CNN, MD_NBC, {
        "title": "Roborock Memorial Day 2026 sale",
        "url": "https://us.roborock.com/pages/sale",
        "source": "Roborock",
    }],
    "Friday morning the robot vacuum category opened with Dreame and Roborock running aggressive MD weekend pricing on the flagship lineups. Dreame X60 Max Ultra Complete holds first at $1,499 with the $400 cut from Dreame direct, the auto-empty plus the auto-mop wash plus the mop lift plus the obstacle avoidance with VersaLift technology makes this still the right pick for serious cleaners and the $1,499 sticker is the floor before Black Friday on the X60. Roborock Saros 10R at second drops to $1,399 with the $400 MD cut, the StarSight LDS navigation plus the auto-empty plus the warm-water mop wash makes this the right pick for buyers who want Roborock build quality and the value math against the Dreame is competitive at $100 less. Dreame L50 Ultra at third holds $999 with the $300 cut, the mid-tier Dreame with auto-empty and auto-wash is the right pick for buyers who want flagship features at lower price. iRobot Roomba Combo j9+ holds fourth at $699 with the $300 cut, the SmartScrub plus the AutoFill is the right pick for buyers who want iRobot brand reliability without the new j10 price. Eufy Omni S1 Pro stays fifth at $799 with the $300 cut as the value challenger. Verdict for Friday: X60 Max Ultra at $1,499 for serious cleaners, Saros 10R at $1,399 for Roborock loyalty, L50 Ultra at $999 if you want flagship features at lower price. MD weekend cuts on this category are the deepest of the year, no waiting.",
    [
        {
            "title": "Dreame X60 Max Ultra Complete at $1,499 is the serious cleaner buy",
            "body": "Dreame direct cut $400 bringing the X60 Max Ultra Complete to $1,499, the floor before Black Friday. The auto-empty plus the auto-mop wash plus the mop lift plus the VersaLift obstacle avoidance makes this the right pick for serious cleaners and the value math against any competitor at the price is locked."
        },
        {
            "title": "Roborock Saros 10R drops $400 to $1,399",
            "body": "The MD cut on the Saros 10R brings it to $1,399 with the StarSight LDS navigation plus the auto-empty plus the warm-water mop wash. For buyers who want Roborock build quality and the warm-water mop matters for sticky messes, this is the right pick and the value math against the Dreame is competitive at $100 less."
        },
        {
            "title": "Dreame L50 Ultra at $999 wins flagship-features-at-lower-price",
            "body": "Dreame's $300 cut on the L50 Ultra brings it to $999 with the auto-empty and auto-wash. For buyers who want flagship features at lower price and accept the slightly weaker obstacle avoidance versus the X60, this is the right pick and the value math against the iRobot j9+ is decisive."
        }
    ],
    "禮拜五早上，掃地機器人這個品類因為 Dreame 跟 Roborock 對旗艦線推積極的國殤日週末定價而開盤。\n\nDreame X60 Max Ultra Complete 守第一 NT$46,500 靠 Dreame 美國官網砍 NT$12,400，自動倒垃圾加自動洗拖布加拖布抬升加 VersaLift 障礙物避讓，還是嚴肅清潔買家對的選擇，NT$46,500 就是 X60 在黑五前的地板。\n\nRoborock Saros 10R 第二 NT$43,400 國殤日砍 NT$12,400，StarSight LDS 導航加自動倒垃圾加溫水洗拖布，是要 Roborock 做工的買家對的選擇，價值算數對 Dreame 在便宜 NT$3,100 上競爭得起。Dreame L50 Ultra 第三守 NT$31,000 砍 NT$9,300，中階 Dreame 配自動倒垃圾跟自動洗，是要旗艦功能在較低價的買家對的選擇。\n\n講真的，iRobot Roomba Combo j9+ 第四 NT$21,700 砍 NT$9,300，SmartScrub 加 AutoFill，是要 iRobot 品牌可靠度又不要新 j10 價的買家對的選擇。Eufy Omni S1 Pro 第五 NT$24,800 砍 NT$9,300 當價值挑戰者。\n\n禮拜五結論：嚴肅清潔買 X60 Max Ultra NT$46,500；要 Roborock 忠誠就 Saros 10R NT$43,400；要旗艦功能在較低價就 L50 Ultra NT$31,000。這品類國殤日週末折扣是今年最深，不必等。",
    [
        {
            "title": "Dreame X60 Max Ultra Complete NT$46,500 是嚴肅清潔買點",
            "body": "Dreame 美國官網砍 NT$12,400 把 X60 Max Ultra Complete 拉到 NT$46,500，黑五前的地板。自動倒垃圾加自動洗拖布加拖布抬升加 VersaLift 障礙物避讓，是嚴肅清潔買家對的選擇，對任何競爭對手在這個價的價值算數鎖死。"
        },
        {
            "title": "Roborock Saros 10R 砍 NT$12,400 到 NT$43,400",
            "body": "Saros 10R 的國殤日折扣把它拉到 NT$43,400 配 StarSight LDS 導航加自動倒垃圾加溫水洗拖布。要 Roborock 做工的買家加溫水拖布對黏稠髒污有用，這個對的選擇，對 Dreame 的價值算數在便宜 NT$3,100 上競爭得起。"
        },
        {
            "title": "Dreame L50 Ultra NT$31,000 贏旗艦功能低價",
            "body": "Dreame 砍 L50 Ultra NT$9,300 把它拉到 NT$31,000 配自動倒垃圾跟自動洗。要旗艦功能在較低價又接受比 X60 略弱障礙物避讓的買家，這個對的選擇，對 iRobot j9+ 的價值算數很決定性。"
        }
    ],
)

add(
    "best-robot-lawn-mowers",
    [MD_CNN, MD_NBC, {
        "title": "Mammotion LUBA 3 AWD Memorial Day 2026 sale",
        "url": "https://mammotion.com/",
        "source": "Mammotion",
    }],
    "Friday morning the robot lawn mower category opened with Mammotion running deep MD weekend cuts on the LUBA 3 line to push grass-season adoption. Mammotion LUBA 3 AWD 5000 holds first at $2,799 with the $300 cut from Mammotion direct, the all-wheel-drive plus the 5,000 sq m coverage plus the RTK GPS navigation makes this still the right pick for buyers with large or sloped yards and the $2,799 sticker is the floor before mowing-season peak. ECOVACS GOAT A3000 LiDAR Pro at second drops to $2,499 with the $300 MD cut, the LiDAR navigation plus the boundary-wire-free setup plus the AI obstacle avoidance makes this the right pick for buyers who want premium LiDAR navigation at lower price than the LUBA 3 AWD. ECOVACS GOAT A3000 LiDAR at third holds $1,999 with the $200 cut, the standard A3000 LiDAR without the Pro upgrades is the right pick for buyers with smaller yards who do not need the AWD capability. Husqvarna Automower 450X EPOS holds fourth at $4,999 with no MD discount because Husqvarna refuses to discount the premium line, the EPOS GPS plus the Husqvarna service network is the right pick for buyers who want commercial-grade build with dealer service. Worx Landroid Vision L1300 stays fifth at $1,599 with the $200 cut as the budget pick. Verdict for Friday: LUBA 3 AWD 5000 at $2,799 for large yards, A3000 LiDAR Pro at $2,499 for medium yards with premium LiDAR, A3000 LiDAR at $1,999 for smaller yards. MD weekend is the floor before summer mowing-season peak.",
    [
        {
            "title": "Mammotion LUBA 3 AWD 5000 at $2,799 is the large-yard buy",
            "body": "Mammotion direct cut $300 bringing the LUBA 3 AWD 5000 to $2,799, the floor before mowing-season peak. The all-wheel-drive plus the 5,000 sq m coverage plus the RTK GPS navigation makes this the right pick for buyers with large or sloped yards and the value math against any competitor at the price is locked."
        },
        {
            "title": "ECOVACS GOAT A3000 LiDAR Pro drops $300 to $2,499",
            "body": "The MD cut on the A3000 LiDAR Pro brings it to $2,499 with the LiDAR navigation plus the boundary-wire-free setup plus the AI obstacle avoidance. For buyers who want premium LiDAR navigation at lower price than the LUBA 3 AWD and the medium yard size matches the coverage, this is the right pick at the price."
        },
        {
            "title": "Husqvarna Automower 450X EPOS holds $4,999 — no MD discount",
            "body": "Husqvarna refuses to discount the premium Automower line during holiday weekends. The EPOS GPS plus the Husqvarna service network is the right pick only for buyers who want commercial-grade build with dealer service and accept the $4,999 sticker, and the value math is locked at the premium price."
        }
    ],
    "禮拜五早上，割草機器人這個品類因為 Mammotion 對 LUBA 3 線推深度國殤日週末折扣以推動草地季採用而開盤。\n\nMammotion LUBA 3 AWD 5000 守第一 NT$86,700 靠 Mammotion 美國官網砍 NT$9,300，全輪驅動加 5,000 平方米覆蓋加 RTK GPS 導航，還是大或斜坡庭院買家對的選擇，NT$86,700 就是割草季高峰前的地板。\n\nECOVACS GOAT A3000 LiDAR Pro 第二 NT$77,500 國殤日砍 NT$9,300，LiDAR 導航加免邊界線設置加 AI 障礙物避讓，是要高階 LiDAR 導航又不要 LUBA 3 AWD 價的買家對的選擇。ECOVACS GOAT A3000 LiDAR 第三守 NT$61,900 砍 NT$6,200，標準 A3000 LiDAR 沒 Pro 升級，是較小庭院又不需要 AWD 能力的買家對的選擇。\n\n講真的，Husqvarna Automower 450X EPOS 第四守 NT$155,000 沒國殤日折扣，Husqvarna 拒絕降高階線價，EPOS GPS 加 Husqvarna 服務網路，是要商用級做工加經銷商服務的買家對的選擇。Worx Landroid Vision L1300 第五 NT$49,600 砍 NT$6,200 當預算選擇。\n\n禮拜五結論：大庭院買 LUBA 3 AWD 5000 NT$86,700；中庭院加高階 LiDAR 就 A3000 LiDAR Pro NT$77,500；較小庭院就 A3000 LiDAR NT$61,900。國殤日週末是夏季割草季高峰前的地板。",
    [
        {
            "title": "Mammotion LUBA 3 AWD 5000 NT$86,700 是大庭院買點",
            "body": "Mammotion 美國官網砍 NT$9,300 把 LUBA 3 AWD 5000 拉到 NT$86,700，割草季高峰前的地板。全輪驅動加 5,000 平方米覆蓋加 RTK GPS 導航，是大或斜坡庭院買家對的選擇，對任何競爭對手在這個價的價值算數鎖死。"
        },
        {
            "title": "ECOVACS GOAT A3000 LiDAR Pro 砍 NT$9,300 到 NT$77,500",
            "body": "A3000 LiDAR Pro 國殤日折扣把它拉到 NT$77,500 配 LiDAR 導航加免邊界線設置加 AI 障礙物避讓。要高階 LiDAR 導航又不要 LUBA 3 AWD 價的買家加中庭院尺寸對得上覆蓋，這個對的選擇。"
        },
        {
            "title": "Husqvarna Automower 450X EPOS 守 NT$155,000 — 沒國殤日折扣",
            "body": "Husqvarna 拒絕在節日週末降高階 Automower 線。EPOS GPS 加 Husqvarna 服務網路，只有要商用級做工加經銷商服務接受 NT$155,000 牌價的買家對的選擇，價值算數鎖在高階。"
        }
    ],
)

add(
    "best-standing-desks",
    [MD_CNN, MD_NBC, {
        "title": "UPLIFT Memorial Day 2026 sale",
        "url": "https://www.upliftdesk.com/specials/",
        "source": "UPLIFT Desk",
    }],
    "Friday morning the standing desk category opened with UPLIFT and FlexiSpot running their MD weekend cuts on the flagship lines and Secretlab dropping the MAGNUS Pro. UPLIFT V2 Commercial holds first at $649 with the $100 cut from UPLIFT direct, the heavy-duty 4-leg frame plus the 15-year warranty plus the 355-pound lift capacity makes this still the right pick for serious work-from-home setups and the $649 sticker is the floor before Q4 promotions. FlexiSpot E7 Pro (2026 Version) at second drops to $399 with the $100 MD cut, the dual motor plus the 220-pound lift plus the redesigned 2026 frame is the right pick for buyers who want decent commercial-grade build at lower price. Secretlab MAGNUS Pro at third holds $799 with the $50 cut, the integrated cable management plus the magnetic accessories plus the Secretlab brand aesthetic is the right pick for buyers in the Secretlab ecosystem who want the matching chair and desk combo. Vari Electric Standing Desk holds fourth at $599 with the $100 cut as the no-frills commercial pick. Jarvis Bamboo stays fifth at $549 with the $100 cut for buyers who want the bamboo top aesthetic. Verdict for Friday: V2 Commercial at $649 for serious work-from-home, E7 Pro at $399 for budget commercial-grade, MAGNUS Pro at $799 if you live in Secretlab ecosystem. UPLIFT $100 cut is the floor and probably will not get deeper until Black Friday.",
    [
        {
            "title": "UPLIFT V2 Commercial at $649 is the serious WFH buy",
            "body": "UPLIFT direct cut $100 bringing the V2 Commercial to $649, the floor before Q4 promotions. The heavy-duty 4-leg frame plus the 15-year warranty plus the 355-pound lift capacity makes this the right pick for serious work-from-home setups and the value math against any competitor at the price is locked."
        },
        {
            "title": "FlexiSpot E7 Pro (2026) drops $100 to $399",
            "body": "The MD cut on the E7 Pro 2026 brings it to $399 with the dual motor plus the 220-pound lift plus the redesigned 2026 frame. For buyers who want decent commercial-grade build at lower price than the UPLIFT and accept the shorter warranty, this is the right pick at the price."
        },
        {
            "title": "Secretlab MAGNUS Pro at $799 wins ecosystem play",
            "body": "Secretlab cut $50 on the MAGNUS Pro to $799 with the integrated cable management plus the magnetic accessories plus the Secretlab brand aesthetic. For buyers in the Secretlab ecosystem who already own the Titan Evo chair and want the matching desk, the consolidation play is the right pick at the price."
        }
    ],
    "禮拜五早上，升降桌這個品類因為 UPLIFT 跟 FlexiSpot 對旗艦線推國殤日週末折扣加 Secretlab 降 MAGNUS Pro 而開盤。\n\nUPLIFT V2 Commercial 守第一 NT$20,100 靠 UPLIFT 美國官網砍 NT$3,100，重型 4 腳框架加 15 年保固加 355 磅升降容量，還是嚴肅在家工作設置對的選擇，NT$20,100 就是 Q4 促銷前的地板。\n\nFlexiSpot E7 Pro (2026 Version) 第二 NT$12,400 國殤日砍 NT$3,100，雙馬達加 220 磅升降加重新設計 2026 框架，是要不錯商用級做工又較低價的買家對的選擇。Secretlab MAGNUS Pro 第三守 NT$24,800 砍 NT$1,500，整合理線加磁吸配件加 Secretlab 品牌美學，是 Secretlab 生態裡要椅桌組合的買家對的選擇。\n\n講真的，Vari Electric Standing Desk 第四 NT$18,600 砍 NT$3,100 當無花俏商用選擇。Jarvis Bamboo 第五 NT$17,000 砍 NT$3,100 是要竹木桌面美學的買家對的選擇。\n\n禮拜五結論：嚴肅在家工作買 V2 Commercial NT$20,100；預算商用級就 E7 Pro NT$12,400；住 Secretlab 生態就 MAGNUS Pro NT$24,800。UPLIFT 砍 NT$3,100 是地板，大概要等黑五才會更深。",
    [
        {
            "title": "UPLIFT V2 Commercial NT$20,100 是嚴肅在家工作買點",
            "body": "UPLIFT 美國官網砍 NT$3,100 把 V2 Commercial 拉到 NT$20,100，Q4 促銷前的地板。重型 4 腳框架加 15 年保固加 355 磅升降容量，是嚴肅在家工作設置對的選擇，對任何競爭對手在這個價的價值算數鎖死。"
        },
        {
            "title": "FlexiSpot E7 Pro (2026) 砍 NT$3,100 到 NT$12,400",
            "body": "E7 Pro 2026 的國殤日折扣把它拉到 NT$12,400 配雙馬達加 220 磅升降加重新設計 2026 框架。要不錯商用級做工又較 UPLIFT 低價接受較短保固的買家，這個價對的選擇。"
        },
        {
            "title": "Secretlab MAGNUS Pro NT$24,800 贏生態玩法",
            "body": "Secretlab 砍 MAGNUS Pro NT$1,500 到 NT$24,800 配整合理線加磁吸配件加 Secretlab 品牌美學。Secretlab 生態裡已有 Titan Evo 椅又要配對桌的買家，這個價整合玩法對。"
        }
    ],
)

add(
    "best-treadmills",
    [MD_CNN, MD_NBC, {
        "title": "NordicTrack Memorial Day 2026 sale",
        "url": "https://www.nordictrack.com/",
        "source": "NordicTrack",
    }],
    "Friday morning the treadmill category opened with NordicTrack and Sole running aggressive MD weekend cuts on the flagship lines for the spring fitness commitment season. NordicTrack Commercial 1750 holds first at $1,799 with the $200 cut from NordicTrack direct, the iFit subscription integration plus the 10-inch HD touchscreen plus the heavy-duty motor makes this still the right pick for serious runners and the $1,799 sticker is the floor before Q4 promotions. NordicTrack X24 Incline Trainer at second drops to $2,599 with the $400 MD cut, the steep 40-percent incline plus the 24-inch touchscreen plus the iFit integration is the right pick for buyers who want incline training plus the larger screen. Sole F80 at third holds $1,899 with the $200 cut, the no-subscription open-platform plus the heavy 3.5 HP motor plus the cushioning is the right pick for buyers who refuse iFit subscription lock-in. Peloton Tread+ holds fourth at $4,995 with no MD discount because Peloton does not discount during holiday weekends, the subscription-locked Peloton experience is the right pick only for buyers already in the Peloton ecosystem. Horizon 7.0 AT stays fifth at $999 with the $300 cut as the budget pick. Verdict for Friday: Commercial 1750 at $1,799 for serious runners, X24 Incline Trainer at $2,599 for incline plus large screen, Sole F80 at $1,899 if you refuse iFit subscription. The NordicTrack MD weekend cuts are the deepest of the year, no waiting.",
    [
        {
            "title": "NordicTrack Commercial 1750 at $1,799 is the serious runner buy",
            "body": "NordicTrack direct cut $200 bringing the Commercial 1750 to $1,799, the floor before Q4 promotions. The iFit subscription integration plus the 10-inch HD touchscreen plus the heavy-duty motor makes this the right pick for serious runners and the value math against any sub-$2k competitor at the price is locked."
        },
        {
            "title": "NordicTrack X24 Incline Trainer drops $400 to $2,599",
            "body": "The MD cut on the X24 brings it to $2,599 with the steep 40-percent incline plus the 24-inch touchscreen plus the iFit integration. For buyers who want incline training plus the larger immersive screen and the iFit subscription is part of the deal, this is the right pick at the price."
        },
        {
            "title": "Sole F80 at $1,899 wins for no-subscription buyers",
            "body": "Sole cut $200 on the F80 to $1,899 with the no-subscription open-platform plus the heavy 3.5 HP motor plus the cushioning. For buyers who refuse the iFit subscription lock-in and want to use the treadmill with their own apps or Netflix while running, this is the right pick at the price."
        }
    ],
    "禮拜五早上，跑步機這個品類因為 NordicTrack 跟 Sole 對旗艦線推積極的國殤日週末折扣以對應春季健身決心季而開盤。\n\nNordicTrack Commercial 1750 守第一 NT$55,800 靠 NordicTrack 美國官網砍 NT$6,200，iFit 訂閱整合加 10 吋 HD 觸控螢幕加重型馬達，還是嚴肅跑者對的選擇，NT$55,800 就是 Q4 促銷前的地板。\n\nNordicTrack X24 Incline Trainer 第二 NT$80,500 國殤日砍 NT$12,400，陡 40% 坡度加 24 吋觸控螢幕加 iFit 整合，是要坡度訓練加更大沉浸螢幕的買家對的選擇。Sole F80 第三守 NT$58,900 砍 NT$6,200，免訂閱開放平台加重型 3.5 HP 馬達加緩震，是拒絕 iFit 訂閱鎖定的買家對的選擇。\n\n講真的，Peloton Tread+ 第四守 NT$155,000 沒國殤日折扣，Peloton 在節日週末不降價，訂閱鎖定的 Peloton 體驗，只有 Peloton 生態裡的買家對的選擇。Horizon 7.0 AT 第五 NT$31,000 砍 NT$9,300 當預算選擇。\n\n禮拜五結論：嚴肅跑者買 Commercial 1750 NT$55,800；要坡度加大螢幕就 X24 Incline Trainer NT$80,500；拒絕 iFit 訂閱就 Sole F80 NT$58,900。NordicTrack 國殤日週末折扣是今年最深，不必等。",
    [
        {
            "title": "NordicTrack Commercial 1750 NT$55,800 是嚴肅跑者買點",
            "body": "NordicTrack 美國官網砍 NT$6,200 把 Commercial 1750 拉到 NT$55,800，Q4 促銷前的地板。iFit 訂閱整合加 10 吋 HD 觸控螢幕加重型馬達，是嚴肅跑者對的選擇，對任何 NT$62,000 以下競爭對手在這個價的價值算數鎖死。"
        },
        {
            "title": "NordicTrack X24 Incline Trainer 砍 NT$12,400 到 NT$80,500",
            "body": "X24 的國殤日折扣把它拉到 NT$80,500 配陡 40% 坡度加 24 吋觸控螢幕加 iFit 整合。要坡度訓練加更大沉浸螢幕又把 iFit 訂閱當成方案一部分的買家，這個價對的選擇。"
        },
        {
            "title": "Sole F80 NT$58,900 贏免訂閱買家",
            "body": "Sole 砍 F80 NT$6,200 到 NT$58,900 配免訂閱開放平台加重型 3.5 HP 馬達加緩震。拒絕 iFit 訂閱鎖定又想用自己應用程式或邊跑邊看 Netflix 的買家，這個價對的選擇。"
        }
    ],
)

add(
    "best-massage-guns",
    [MD_CNN, MD_NBC, {
        "title": "Therabody Memorial Day 2026 sale",
        "url": "https://www.therabody.com/us/en-us/sale.html",
        "source": "Therabody",
    }],
    "Friday morning the massage gun category opened with Therabody and Hyperice running deep MD weekend cuts on the flagship units. Theragun Pro Plus holds first at $499 with the $100 cut from Therabody direct, the QX150 motor plus the 6 attachments plus the OLED screen plus the integrated heat plus the cold therapy makes this still the right pick for serious athletes and the $499 sticker is the floor before Q4 promotions. Therabody Rally Orbital Massager at second drops to $199 with the $50 MD cut, the orbital motion plus the deeper percussion plus the smaller form factor is the right pick for buyers who want the Therabody quality at lower price. Hyperice Hypervolt 2 Pro at third holds $329 with the $70 cut, the 5-speed selection plus the Hyperice app integration plus the Bluetooth makes this the right pick for buyers locked into the Hyperice ecosystem with the Normatec boots. Bob and Brad C2 holds fourth at $129 with the $30 cut as the budget pick with surprisingly good amplitude. Ekrin B37 stays fifth at $179 with the $50 cut as the mid-tier value pick. Verdict for Friday: Theragun Pro Plus at $499 for serious athletes, Rally Orbital at $199 for Therabody quality at lower price, Hypervolt 2 Pro at $329 if you live in Hyperice ecosystem. MD weekend cuts on Therabody are the deepest of 2026 so far.",
    [
        {
            "title": "Theragun Pro Plus at $499 is the serious athlete buy",
            "body": "Therabody direct cut $100 bringing the Pro Plus to $499, the floor before Q4 promotions. The QX150 motor plus the 6 attachments plus the OLED screen plus the integrated heat plus the cold therapy makes this the right pick for serious athletes and the value math against any competitor at the price is locked."
        },
        {
            "title": "Therabody Rally Orbital drops $50 to $199",
            "body": "The MD cut on the Rally Orbital brings it to $199 with the orbital motion plus the deeper percussion plus the smaller form factor. For buyers who want Therabody quality at lower price than the Pro Plus and the orbital motion matches their recovery preference, this is the right pick at the price."
        },
        {
            "title": "Hyperice Hypervolt 2 Pro at $329 wins ecosystem play",
            "body": "Hyperice cut $70 on the Hypervolt 2 Pro to $329 with the 5-speed selection plus the Hyperice app integration plus the Bluetooth. For buyers locked into the Hyperice ecosystem with the Normatec boots or the Venom heat wraps and want the app to manage all devices, this is the right pick."
        }
    ],
    "禮拜五早上，按摩槍這個品類因為 Therabody 跟 Hyperice 對旗艦機型推深度國殤日週末折扣而開盤。\n\nTheragun Pro Plus 守第一 NT$15,500 靠 Therabody 美國官網砍 NT$3,100，QX150 馬達加 6 種按摩頭加 OLED 螢幕加整合熱療加冷療，還是嚴肅運動員對的選擇，NT$15,500 就是 Q4 促銷前的地板。\n\nTherabody Rally Orbital Massager 第二 NT$6,200 國殤日砍 NT$1,500，軌道運動加更深震動加更小外型，是要 Therabody 品質又較低價的買家對的選擇。Hyperice Hypervolt 2 Pro 第三守 NT$10,200 砍 NT$2,200，5 段速度選擇加 Hyperice 應用程式整合加藍牙，是被鎖在 Hyperice 生態加 Normatec 靴的買家對的選擇。\n\n講真的，Bob and Brad C2 第四 NT$4,000 砍 NT$900 當預算選擇，振幅意外的好。Ekrin B37 第五 NT$5,500 砍 NT$1,500 當中階價值選擇。\n\n禮拜五結論：嚴肅運動員買 Theragun Pro Plus NT$15,500；要 Therabody 品質較低價就 Rally Orbital NT$6,200；住 Hyperice 生態就 Hypervolt 2 Pro NT$10,200。Therabody 國殤日週末折扣是 2026 到目前為止最深。",
    [
        {
            "title": "Theragun Pro Plus NT$15,500 是嚴肅運動員買點",
            "body": "Therabody 美國官網砍 NT$3,100 把 Pro Plus 拉到 NT$15,500，Q4 促銷前的地板。QX150 馬達加 6 種按摩頭加 OLED 螢幕加整合熱療加冷療，是嚴肅運動員對的選擇，對任何競爭對手在這個價的價值算數鎖死。"
        },
        {
            "title": "Therabody Rally Orbital 砍 NT$1,500 到 NT$6,200",
            "body": "Rally Orbital 的國殤日折扣把它拉到 NT$6,200 配軌道運動加更深震動加更小外型。要 Therabody 品質又較 Pro Plus 低價加軌道運動對得上恢復偏好的買家，這個價對的選擇。"
        },
        {
            "title": "Hyperice Hypervolt 2 Pro NT$10,200 贏生態玩法",
            "body": "Hyperice 砍 Hypervolt 2 Pro NT$2,200 到 NT$10,200 配 5 段速度選擇加 Hyperice 應用程式整合加藍牙。被鎖在 Hyperice 生態加 Normatec 靴或 Venom 熱敷套又要應用程式管理所有裝置的買家，這個對的選擇。"
        }
    ],
)

# ---------- SMART HOME / SECURITY ----------

add(
    "best-mesh-wifi-systems",
    [MD_CNN, MD_NBC, {
        "title": "Asus Memorial Day 2026 networking deals",
        "url": "https://www.asus.com/event/memorial-day-sale/",
        "source": "Asus",
    }],
    "Friday morning the mesh WiFi category opened with Asus and TP-Link running their MD weekend cuts on the WiFi 7 lineups and this is the right buy window for WiFi 7 adoption. Asus ZenWiFi BQ16 Pro holds first at $799 with the $100 cut from Asus direct, the WiFi 7 quad-band plus the 6 GHz support plus the 5,500 sq ft coverage with 3-pack makes this still the right pick for serious WiFi 7 adopters and the $799 sticker is the floor before Q4 promotions. TP-Link Deco BE63 (Deco 7 Pro) at second drops to $549 with the $100 MD cut, the WiFi 7 tri-band plus the 6 GHz support plus the easier setup is the right pick for buyers who want WiFi 7 at lower price than the Asus. Eero Pro 7 at third holds $599 with the $100 cut, the WiFi 7 plus the Amazon ecosystem integration plus the simpler app is the right pick for buyers locked into the Amazon ecosystem who want the smart home device integration. Netgear Orbi 970 holds fourth at $1,499 with the $300 cut, the WiFi 7 quad-band plus the 10 Gbps backhaul plus the premium build is the right pick for buyers who want the premium tier and accept the premium price. Google Nest WiFi Pro stays fifth at $349 with the $50 cut as the value WiFi 6E pick. Verdict for Friday: BQ16 Pro at $799 for serious WiFi 7, Deco BE63 at $549 for value WiFi 7, Eero Pro 7 at $599 if you live in Amazon ecosystem. WiFi 7 is mature enough this MD weekend and the price floors here justify the upgrade.",
    [
        {
            "title": "Asus ZenWiFi BQ16 Pro at $799 is the WiFi 7 buy",
            "body": "Asus direct cut $100 bringing the BQ16 Pro to $799, the floor before Q4 promotions. The WiFi 7 quad-band plus the 6 GHz support plus the 5,500 sq ft coverage with 3-pack makes this the right pick for serious WiFi 7 adopters and the value math against the Netgear Orbi 970 at twice the price is decisive."
        },
        {
            "title": "TP-Link Deco BE63 drops $100 to $549",
            "body": "The MD cut on the Deco BE63 brings it to $549 with the WiFi 7 tri-band plus the 6 GHz support plus the easier setup. For buyers who want WiFi 7 at lower price than the Asus and accept the slightly weaker spec, this is the right pick at the price and the value math is decisive against the Eero Pro 7."
        },
        {
            "title": "Eero Pro 7 at $599 wins Amazon ecosystem play",
            "body": "Amazon cut $100 on the Eero Pro 7 to $599 with the WiFi 7 plus the simpler app plus the deeper Amazon smart home integration. For buyers locked into the Amazon ecosystem with Echo and Ring devices who want the mesh to act as the Thread border router, this is the right pick at the price."
        }
    ],
    "禮拜五早上，Mesh WiFi 這個品類因為 Asus 跟 TP-Link 對 WiFi 7 線推國殤日週末折扣，這是 WiFi 7 採用對的買點窗口。\n\nAsus ZenWiFi BQ16 Pro 守第一 NT$24,800 靠 Asus 美國官網砍 NT$3,100，WiFi 7 四頻加 6 GHz 支援加 5,500 平方呎覆蓋 3 顆組，還是嚴肅 WiFi 7 採用者對的選擇，NT$24,800 就是 Q4 促銷前的地板。\n\nTP-Link Deco BE63 (Deco 7 Pro) 第二 NT$17,000 國殤日砍 NT$3,100，WiFi 7 三頻加 6 GHz 支援加更簡單設定，是要 WiFi 7 又較 Asus 低價的買家對的選擇。eero Pro 7 第三守 NT$18,600 砍 NT$3,100，WiFi 7 加 Amazon 生態整合加更簡單應用程式，是被鎖在 Amazon 生態要智慧家裝置整合的買家對的選擇。\n\n講真的，Netgear Orbi 970 第四守 NT$46,500 砍 NT$9,300，WiFi 7 四頻加 10 Gbps 後傳加高階做工，是要高階階層接受高階價的買家對的選擇。Google Nest WiFi Pro 第五 NT$10,800 砍 NT$1,500 當價值 WiFi 6E 選擇。\n\n禮拜五結論：嚴肅 WiFi 7 買 BQ16 Pro NT$24,800；要價值 WiFi 7 就 Deco BE63 NT$17,000；住 Amazon 生態就 eero Pro 7 NT$18,600。WiFi 7 這檔國殤日週末夠成熟了，這裡的價格地板正當化升級。",
    [
        {
            "title": "Asus ZenWiFi BQ16 Pro NT$24,800 是 WiFi 7 買點",
            "body": "Asus 美國官網砍 NT$3,100 把 BQ16 Pro 拉到 NT$24,800，Q4 促銷前的地板。WiFi 7 四頻加 6 GHz 支援加 5,500 平方呎覆蓋 3 顆組，是嚴肅 WiFi 7 採用者對的選擇，對兩倍價的 Netgear Orbi 970 的價值算數很決定性。"
        },
        {
            "title": "TP-Link Deco BE63 砍 NT$3,100 到 NT$17,000",
            "body": "Deco BE63 的國殤日折扣把它拉到 NT$17,000 配 WiFi 7 三頻加 6 GHz 支援加更簡單設定。要 WiFi 7 又較 Asus 低價接受略弱規格的買家，這個價對的選擇，對 eero Pro 7 的價值算數很決定性。"
        },
        {
            "title": "eero Pro 7 NT$18,600 贏 Amazon 生態玩法",
            "body": "Amazon 砍 eero Pro 7 NT$3,100 到 NT$18,600 配 WiFi 7 加更簡單應用程式加更深 Amazon 智慧家整合。被鎖在 Amazon 生態加 Echo 跟 Ring 裝置又要 Mesh 當 Thread 邊界路由器的買家，這個價對的選擇。"
        }
    ],
)

add(
    "best-security-cameras",
    [MD_CNN, MD_NBC, {
        "title": "Reolink Memorial Day 2026 sale",
        "url": "https://reolink.com/",
        "source": "Reolink",
    }],
    "Friday morning the security camera category opened with Reolink and Arlo running deep MD weekend cuts on the flagship outdoor lineups. Reolink Argus 4 Pro holds first at $179 with the $40 cut from Reolink direct, the 4K plus the 180-degree wide-angle dual lens plus the no-subscription local recording plus the solar option makes this still the right pick for buyers who want flagship features without subscription lock-in and the $179 sticker is the floor before Q4 promotions. Arlo Pro 5S at second drops to $149 with the $50 MD cut, the 2K wireless plus the integrated spotlight plus the color night vision is the right pick for buyers who want the Arlo brand and accept the subscription model. Eufy SoloCam S340 at third holds $179 with the $20 cut, the dual-lens 3K plus the solar plus the no-subscription is the right pick for buyers cross-shopping Reolink. Google Nest Cam (Battery) holds fourth at $179 with the $30 cut, the Google Home integration plus the AI face recognition is the right pick for buyers in the Google ecosystem. Ring Stick Up Cam Pro stays fifth at $129 with the $40 cut as the budget Amazon ecosystem pick. Verdict for Friday: Argus 4 Pro at $179 for no-subscription flagship, Arlo Pro 5S at $149 for Arlo brand loyalty, Nest Cam Battery at $179 for Google ecosystem. The Reolink MD discount is the floor and the no-subscription pitch makes the value math decisive.",
    [
        {
            "title": "Reolink Argus 4 Pro at $179 wins no-subscription flagship",
            "body": "Reolink direct cut $40 bringing the Argus 4 Pro to $179, the floor before Q4 promotions. The 4K plus the 180-degree wide-angle dual lens plus the no-subscription local recording plus the solar option makes this the right pick for buyers who refuse subscription lock-in and the value math against any subscription competitor is decisive."
        },
        {
            "title": "Arlo Pro 5S drops $50 to $149",
            "body": "The MD cut on the Arlo Pro 5S brings it to $149 with the 2K wireless plus the integrated spotlight plus the color night vision. For buyers who want the Arlo brand and accept the subscription model for the AI features and the cloud storage, this is the right pick at the price."
        },
        {
            "title": "Google Nest Cam Battery at $179 wins Google ecosystem play",
            "body": "Google cut $30 on the Nest Cam Battery to $179 with the Google Home integration plus the AI face recognition. For buyers in the Google ecosystem who already use Nest hubs and want the camera to integrate with Routines and the Nest Hub Max, this is the right pick at the price."
        }
    ],
    "禮拜五早上，安全攝影機這個品類因為 Reolink 跟 Arlo 對戶外旗艦線推深度國殤日週末折扣而開盤。\n\nReolink Argus 4 Pro 守第一 NT$5,500 靠 Reolink 美國官網砍 NT$1,200，4K 加 180 度廣角雙鏡頭加免訂閱本地錄製加太陽能選項，還是要旗艦功能又不要訂閱鎖定的買家對的選擇，NT$5,500 就是 Q4 促銷前的地板。\n\nArlo Pro 5S 第二 NT$4,650 國殤日砍 NT$1,500，2K 無線加整合聚光燈加彩色夜視，是要 Arlo 品牌接受訂閱模式的買家對的選擇。Eufy SoloCam S340 第三守 NT$5,500 砍 NT$600，雙鏡頭 3K 加太陽能加免訂閱，是跨比較 Reolink 的買家對的選擇。\n\n講真的，Google Nest Cam (Battery) 第四 NT$5,500 砍 NT$900，Google Home 整合加 AI 臉部辨識，是 Google 生態裡的買家對的選擇。Ring Stick Up Cam Pro 第五 NT$4,000 砍 NT$1,200 當預算 Amazon 生態選擇。\n\n禮拜五結論：免訂閱旗艦買 Argus 4 Pro NT$5,500；要 Arlo 品牌忠誠就 Arlo Pro 5S NT$4,650；要 Google 生態就 Nest Cam Battery NT$5,500。Reolink 國殤日折扣是地板，免訂閱話術讓價值算數很決定性。",
    [
        {
            "title": "Reolink Argus 4 Pro NT$5,500 贏免訂閱旗艦",
            "body": "Reolink 美國官網砍 NT$1,200 把 Argus 4 Pro 拉到 NT$5,500，Q4 促銷前的地板。4K 加 180 度廣角雙鏡頭加免訂閱本地錄製加太陽能選項，是拒絕訂閱鎖定的買家對的選擇，對任何訂閱競爭對手的價值算數很決定性。"
        },
        {
            "title": "Arlo Pro 5S 砍 NT$1,500 到 NT$4,650",
            "body": "Arlo Pro 5S 的國殤日折扣把它拉到 NT$4,650 配 2K 無線加整合聚光燈加彩色夜視。要 Arlo 品牌接受訂閱模式為了 AI 功能加雲端儲存的買家，這個價對的選擇。"
        },
        {
            "title": "Google Nest Cam Battery NT$5,500 贏 Google 生態玩法",
            "body": "Google 砍 Nest Cam Battery NT$900 到 NT$5,500 配 Google Home 整合加 AI 臉部辨識。Google 生態裡已用 Nest hubs 又要相機跟 Routines 跟 Nest Hub Max 整合的買家，這個價對的選擇。"
        }
    ],
)

add(
    "best-video-doorbells",
    [MD_CNN, MD_NBC, {
        "title": "Eufy Memorial Day 2026 sale",
        "url": "https://us.eufy.com/",
        "source": "Eufy",
    }],
    "Friday morning the video doorbell category opened with Eufy and Aqara running their MD weekend cuts on the dual-camera flagships. Eufy Video Doorbell E340 holds first at $149 with the $30 cut from Eufy direct, the dual-camera package detection plus the 2K resolution plus the no-subscription local recording makes this still the right pick for buyers who refuse subscription lock-in and the $149 sticker is the floor before Q4 promotions. Aqara Doorbell Camera Hub G410 at second drops to $129 with the $30 MD cut, the dual-camera plus the Matter over Thread support plus the HomeKit Secure Video integration is the right pick for buyers in the Apple Home ecosystem. Google Nest Doorbell (Wired, 2nd Gen) at third holds $149 with the $30 cut, the Google Home integration plus the AI face recognition plus the longer cloud storage is the right pick for buyers in the Google ecosystem. Ring Battery Doorbell Pro holds fourth at $179 with the $50 cut, the 1536p HD Plus plus the radar motion detection plus the Amazon ecosystem integration is the right pick for buyers locked into Ring. Arlo Essential Video Doorbell stays fifth at $129 with the $30 cut as the cross-shopping pick. Verdict for Friday: E340 at $149 for no-subscription flagship, G410 at $129 for Apple Home users, Nest Doorbell at $149 for Google ecosystem. The dual-camera package detection on the E340 is the headline feature.",
    [
        {
            "title": "Eufy E340 at $149 wins no-subscription dual-camera flagship",
            "body": "Eufy direct cut $30 bringing the E340 to $149, the floor before Q4 promotions. The dual-camera package detection plus the 2K resolution plus the no-subscription local recording makes this the right pick for buyers who refuse subscription lock-in and the dual-camera detection on packages is the actual differentiator at the price."
        },
        {
            "title": "Aqara G410 drops $30 to $129 for Apple Home users",
            "body": "The MD cut on the G410 brings it to $129 with the dual-camera plus the Matter over Thread support plus the HomeKit Secure Video integration. For buyers in the Apple Home ecosystem who already pay for iCloud+ and want the HKSV cloud storage included, this is the right pick at the price."
        },
        {
            "title": "Google Nest Doorbell (Wired, 2nd Gen) at $149 for Google users",
            "body": "Google cut $30 on the Nest Doorbell to $149 with the Google Home integration plus the AI face recognition plus the longer cloud storage option. For buyers in the Google ecosystem who want the doorbell to integrate with Nest Hub Max plus the Routines plus the Pixel ecosystem, this is the right pick at the price."
        }
    ],
    "禮拜五早上，視訊門鈴這個品類因為 Eufy 跟 Aqara 對雙鏡頭旗艦推國殤日週末折扣而開盤。\n\nEufy Video Doorbell E340 守第一 NT$4,650 靠 Eufy 美國官網砍 NT$900，雙鏡頭包裹偵測加 2K 解析度加免訂閱本地錄製，還是拒絕訂閱鎖定的買家對的選擇，NT$4,650 就是 Q4 促銷前的地板。\n\nAqara Doorbell Camera Hub G410 第二 NT$4,000 國殤日砍 NT$900，雙鏡頭加 Matter over Thread 支援加 HomeKit Secure Video 整合，是 Apple Home 生態的買家對的選擇。Google Nest Doorbell (Wired, 2nd Gen) 第三守 NT$4,650 砍 NT$900，Google Home 整合加 AI 臉部辨識加更長雲端儲存，是 Google 生態的買家對的選擇。\n\n講真的，Ring Battery Doorbell Pro 第四 NT$5,500 砍 NT$1,500，1536p HD Plus 加雷達動作偵測加 Amazon 生態整合，是被鎖在 Ring 的買家對的選擇。Arlo Essential Video Doorbell 第五 NT$4,000 砍 NT$900 當跨比較選擇。\n\n禮拜五結論：免訂閱旗艦買 E340 NT$4,650；Apple Home 用戶 G410 NT$4,000；Google 生態 Nest Doorbell NT$4,650。E340 雙鏡頭包裹偵測是頭條功能。",
    [
        {
            "title": "Eufy E340 NT$4,650 贏免訂閱雙鏡頭旗艦",
            "body": "Eufy 美國官網砍 NT$900 把 E340 拉到 NT$4,650，Q4 促銷前的地板。雙鏡頭包裹偵測加 2K 解析度加免訂閱本地錄製，是拒絕訂閱鎖定的買家對的選擇，雙鏡頭包裹偵測就是這個價的真正差異化。"
        },
        {
            "title": "Aqara G410 砍 NT$900 到 NT$4,000 給 Apple Home 用戶",
            "body": "G410 的國殤日折扣把它拉到 NT$4,000 配雙鏡頭加 Matter over Thread 支援加 HomeKit Secure Video 整合。Apple Home 生態裡已付 iCloud+ 又要 HKSV 雲端儲存包含進去的買家，這個價對的選擇。"
        },
        {
            "title": "Google Nest Doorbell (Wired, 2nd Gen) NT$4,650 給 Google 用戶",
            "body": "Google 砍 Nest Doorbell NT$900 到 NT$4,650 配 Google Home 整合加 AI 臉部辨識加更長雲端儲存選項。Google 生態裡要門鈴跟 Nest Hub Max 加 Routines 加 Pixel 生態整合的買家，這個價對的選擇。"
        }
    ],
)

add(
    "best-smart-thermostats",
    [MD_CNN, MD_LG, MD_NBC],
    "Friday morning the smart thermostat category opened with Ecobee and Google running modest MD weekend cuts. Ecobee Smart Thermostat Premium holds first at $219 with the $30 cut from Ecobee direct, the integrated air quality sensor plus the SmartSensor included plus the Alexa built-in plus the Apple Home plus Google Home plus SmartThings support makes this still the right pick for buyers who refuse to be locked into one ecosystem and the $219 sticker is the floor outside Q4. Google Nest Learning Thermostat (4th gen) at second drops to $249 with the $30 MD cut, the redesigned circular display plus the new auto-learning algorithm plus the deeper Google Home integration is the right pick for buyers locked into Google ecosystem. Honeywell Home T9 Smart Thermostat at third holds $169 with the $30 cut, the multi-room sensor support plus the geofencing plus the simpler app is the right pick for buyers who want decent features at lower price than the Ecobee or Nest. Amazon Smart Thermostat (Honeywell-built) holds fourth at $59 with the $20 cut as the Alexa ecosystem budget pick. Mysa Smart Thermostat for Electric Baseboards stays fifth at $129 with the $20 cut as the niche pick for electric baseboard heating systems. Verdict for Friday: Premium at $219 for ecosystem-agnostic, Nest 4th gen at $249 for Google ecosystem, T9 at $169 for value with sensor support. The Ecobee MD cut is modest but the SmartSensor inclusion makes the bundle value real.",
    [
        {
            "title": "Ecobee Smart Thermostat Premium at $219 wins ecosystem-agnostic",
            "body": "Ecobee direct cut $30 bringing the Premium to $219, the floor outside Q4. The integrated air quality sensor plus the SmartSensor included plus the multi-ecosystem support across Alexa, Apple Home, Google Home, and SmartThings makes this the right pick for buyers who refuse to be locked into one ecosystem."
        },
        {
            "title": "Nest Learning Thermostat (4th gen) drops $30 to $249",
            "body": "The MD cut on the Nest 4th gen brings it to $249 with the redesigned circular display plus the new auto-learning algorithm plus the deeper Google Home integration. For buyers locked into the Google ecosystem who want the Nest brand plus the auto-learning feature, this is the right pick at the price."
        },
        {
            "title": "Honeywell Home T9 at $169 wins value with sensor support",
            "body": "Honeywell cut $30 on the T9 to $169 with the multi-room sensor support plus the geofencing plus the simpler app. For buyers who want decent features at lower price than the Ecobee or Nest and want the multi-room sensor option without paying premium, this is the right pick at the price."
        }
    ],
    "禮拜五早上，智慧恆溫器這個品類因為 Ecobee 跟 Google 推適度的國殤日週末折扣而開盤。\n\nEcobee Smart Thermostat Premium 守第一 NT$6,800 靠 Ecobee 美國官網砍 NT$900，整合空氣品質感測器加包含 SmartSensor 加內建 Alexa 加 Apple Home 加 Google Home 加 SmartThings 支援，還是拒絕被鎖進單一生態的買家對的選擇，NT$6,800 就是 Q4 以外的地板。\n\nGoogle Nest Learning Thermostat (4th gen) 第二 NT$7,700 國殤日砍 NT$900，重新設計圓形顯示器加新自動學習演算法加更深 Google Home 整合，是被鎖在 Google 生態的買家對的選擇。Honeywell Home T9 Smart Thermostat 第三守 NT$5,200 砍 NT$900，多房間感測器支援加地理圍籬加更簡單應用程式，是要不錯功能在 Ecobee 或 Nest 之下較低價的買家對的選擇。\n\n講真的，Amazon Smart Thermostat (Honeywell 製造) 第四 NT$1,800 砍 NT$600 當 Alexa 生態預算選擇。Mysa Smart Thermostat for Electric Baseboards 第五 NT$4,000 砍 NT$600 當電熱踢腳板系統的利基選擇。\n\n禮拜五結論：跨生態買 Premium NT$6,800；Google 生態就 Nest 4th gen NT$7,700；要價值加感測器支援就 T9 NT$5,200。Ecobee 國殤日折扣適度但包含 SmartSensor 讓組合價值真實。",
    [
        {
            "title": "Ecobee Smart Thermostat Premium NT$6,800 贏跨生態",
            "body": "Ecobee 美國官網砍 NT$900 把 Premium 拉到 NT$6,800，Q4 以外的地板。整合空氣品質感測器加包含 SmartSensor 加跨 Alexa、Apple Home、Google Home 跟 SmartThings 的多生態支援，是拒絕被鎖進單一生態的買家對的選擇。"
        },
        {
            "title": "Nest Learning Thermostat (4th gen) 砍 NT$900 到 NT$7,700",
            "body": "Nest 4th gen 的國殤日折扣把它拉到 NT$7,700 配重新設計圓形顯示器加新自動學習演算法加更深 Google Home 整合。被鎖在 Google 生態要 Nest 品牌加自動學習功能的買家，這個價對的選擇。"
        },
        {
            "title": "Honeywell Home T9 NT$5,200 贏價值加感測器支援",
            "body": "Honeywell 砍 T9 NT$900 到 NT$5,200 配多房間感測器支援加地理圍籬加更簡單應用程式。要不錯功能又較 Ecobee 或 Nest 低價，要多房間感測器選項不付高階溢價的買家，這個價對的選擇。"
        }
    ],
)

add(
    "best-smart-pet-feeders",
    [MD_CNN, MD_NBC, {
        "title": "PETLIBRO Memorial Day 2026 sale",
        "url": "https://petlibro.com/",
        "source": "PETLIBRO",
    }],
    "Friday morning the smart pet feeder category opened with PETLIBRO and PETKIT running their first MD weekend cuts of the year. PETLIBRO Granary Smart Camera Feeder holds first at $129 with the $30 cut from PETLIBRO direct, the built-in 1080p camera plus the two-way audio plus the WiFi plus the 5L capacity makes this still the right pick for buyers who want to see and talk to the pet while feeding and the $129 sticker is the floor outside Black Friday. PETKIT YumShare Dual-Hopper 2 with Camera at second drops to $179 with the $40 MD cut, the dual-hopper for two food types plus the camera plus the freshness lock is the right pick for buyers with multiple pets or who mix wet plus dry food. PETLIBRO Polar Refrigerated Wet Food Feeder at third holds $199 with the $30 cut, the refrigerated wet food capability plus the schedule control is the niche pick for buyers feeding raw or wet food daily. Sure Petcare SureFeed Microchip Pet Feeder holds fourth at $169 with the $20 cut, the microchip recognition plus the lid that opens only for the right pet is the right pick for multi-pet households with food competition issues. WOPET 7L Automatic Pet Feeder stays fifth at $59 with the $20 cut as the budget no-camera pick. Verdict for Friday: Granary at $129 for camera-equipped flagship, YumShare Dual-Hopper at $179 for dual food types, Polar at $199 for refrigerated wet food. PETLIBRO MD cuts are the deepest in this category.",
    [
        {
            "title": "PETLIBRO Granary at $129 wins camera-equipped flagship",
            "body": "PETLIBRO direct cut $30 bringing the Granary to $129, the floor outside Black Friday. The built-in 1080p camera plus the two-way audio plus the WiFi plus the 5L capacity makes this the right pick for buyers who want to see and talk to the pet while feeding and the value math at the price is locked."
        },
        {
            "title": "PETKIT YumShare Dual-Hopper 2 drops $40 to $179",
            "body": "The MD cut on the YumShare 2 brings it to $179 with the dual-hopper for two food types plus the camera plus the freshness lock. For buyers with multiple pets or who mix wet plus dry food and need the separate hoppers to keep portions accurate, this is the right pick at the price."
        },
        {
            "title": "PETLIBRO Polar at $199 wins refrigerated wet food niche",
            "body": "PETLIBRO cut $30 on the Polar to $199 with the refrigerated wet food capability plus the schedule control. For buyers feeding raw or wet food daily who need to keep portions refrigerated for hours and dispense on schedule, this is the right pick at the price and the niche value math is decisive."
        }
    ],
    "禮拜五早上，智慧寵物餵食器這個品類因為 PETLIBRO 跟 PETKIT 推首次年度國殤日週末折扣而開盤。\n\nPETLIBRO Granary Smart Camera Feeder 守第一 NT$4,000 靠 PETLIBRO 美國官網砍 NT$900，內建 1080p 相機加雙向音訊加 WiFi 加 5L 容量，還是要餵食時能看到跟對寵物說話的買家對的選擇，NT$4,000 就是黑五以外的地板。\n\nPETKIT YumShare Dual-Hopper 2 with Camera 第二 NT$5,500 國殤日砍 NT$1,200，雙料桶給兩種食物加相機加新鮮鎖，是有多隻寵物或混合濕乾食的買家對的選擇。PETLIBRO Polar Refrigerated Wet Food Feeder 第三守 NT$6,200 砍 NT$900，冷藏濕食能力加排程控制，是每天餵生食或濕食的買家利基選擇。\n\n講真的，Sure Petcare SureFeed Microchip Pet Feeder 第四 NT$5,200 砍 NT$600，晶片辨識加只對對的寵物打開蓋子，是多寵物家庭有搶食問題的買家對的選擇。WOPET 7L Automatic Pet Feeder 第五 NT$1,800 砍 NT$600 當預算無相機選擇。\n\n禮拜五結論：相機配備旗艦買 Granary NT$4,000；雙料桶就 YumShare Dual-Hopper NT$5,500；冷藏濕食就 Polar NT$6,200。PETLIBRO 國殤日折扣是這品類最深。",
    [
        {
            "title": "PETLIBRO Granary NT$4,000 贏相機配備旗艦",
            "body": "PETLIBRO 美國官網砍 NT$900 把 Granary 拉到 NT$4,000，黑五以外的地板。內建 1080p 相機加雙向音訊加 WiFi 加 5L 容量，是要餵食時能看到跟對寵物說話的買家對的選擇，在這個價的價值算數鎖死。"
        },
        {
            "title": "PETKIT YumShare Dual-Hopper 2 砍 NT$1,200 到 NT$5,500",
            "body": "YumShare 2 的國殤日折扣把它拉到 NT$5,500 配雙料桶給兩種食物加相機加新鮮鎖。有多隻寵物或混合濕乾食需要分開料桶讓份量準確的買家，這個價對的選擇。"
        },
        {
            "title": "PETLIBRO Polar NT$6,200 贏冷藏濕食利基",
            "body": "PETLIBRO 砍 Polar NT$900 到 NT$6,200 配冷藏濕食能力加排程控制。每天餵生食或濕食需要把份量冷藏好幾小時又按排程出料的買家，這個價對的選擇，利基價值算數很決定性。"
        }
    ],
)

# ---------- MOBILITY / OUTDOOR ----------

add(
    "best-electric-bikes",
    [MD_CNN, MD_NBC, {
        "title": "Aventon Memorial Day 2026 e-bike deals",
        "url": "https://www.aventon.com/",
        "source": "Aventon",
    }],
    "Friday morning the electric bike category opened with Aventon and Lectric running deep MD weekend cuts and this is the right buy window for the riding-season ramp. Aventon Level 3 holds first at $1,799 with the $200 cut from Aventon direct, the torque sensor plus the 750W rear hub motor plus the new color LCD display plus the integrated turn signals makes this still the right pick for serious commuters and the $1,799 sticker is the floor before peak riding season. Lectric XP4 750 at second drops to $999 with the $100 MD cut, the folding step-through plus the 750W motor plus the included accessories package is the right pick for value buyers who want everything included. Ride1Up Discover 3 at third holds $1,499 with the $200 cut, the gravel plus the 750W motor plus the longer-range battery is the right pick for buyers who ride mixed surfaces and want the gravel geometry. Specialized Como SL 5.0 holds fourth at $4,250 with no MD discount because Specialized refuses to discount the premium line, the lightweight aluminum plus the Mastermind TCU is the right pick for buyers who want premium brand and accept the price premium. Rad Power RadCity 5 Plus stays fifth at $1,599 with the $200 cut as the city commuter pick. Verdict for Friday: Level 3 at $1,799 for serious commuters, Lectric XP4 750 at $999 for value, Discover 3 at $1,499 for mixed-surface riders. MD weekend cuts on this category are the floor before peak riding season hits in June.",
    [
        {
            "title": "Aventon Level 3 at $1,799 is the serious commuter buy",
            "body": "Aventon direct cut $200 bringing the Level 3 to $1,799, the floor before peak riding season. The torque sensor plus the 750W rear hub motor plus the new color LCD display plus the integrated turn signals makes this the right pick for serious commuters and the value math against any direct-to-consumer competitor is locked."
        },
        {
            "title": "Lectric XP4 750 drops $100 to $999",
            "body": "The MD cut on the XP4 750 brings it to $999 with the folding step-through plus the 750W motor plus the included accessories package (fenders, rack, lights). For value buyers who want everything included without paying for premium frame materials, this is the right pick at the price."
        },
        {
            "title": "Ride1Up Discover 3 at $1,499 wins mixed-surface riding",
            "body": "Ride1Up cut $200 on the Discover 3 to $1,499 with the gravel-style geometry plus the 750W motor plus the longer-range battery. For buyers who ride mixed paved-and-dirt routes and want the gravel handling without compromising on motor power, this is the right pick at the price."
        }
    ],
    "禮拜五早上，電動腳踏車這個品類因為 Aventon 跟 Lectric 推深度國殤日週末折扣，這是騎乘季爬升對的買點窗口。\n\nAventon Level 3 守第一 NT$55,800 靠 Aventon 美國官網砍 NT$6,200，扭力感測器加 750W 後輪轂馬達加新彩色 LCD 顯示器加整合方向燈，還是嚴肅通勤族對的選擇，NT$55,800 就是高峰騎乘季前的地板。\n\nLectric XP4 750 第二 NT$31,000 國殤日砍 NT$3,100，可折疊跨車架加 750W 馬達加包含配件包，是要全部包含的價值買家對的選擇。Ride1Up Discover 3 第三守 NT$46,500 砍 NT$6,200，礫石加 750W 馬達加更長續航電池，是騎混合路面要礫石幾何的買家對的選擇。\n\n講真的，Specialized Como SL 5.0 第四守 NT$131,800 沒國殤日折扣，Specialized 拒絕降高階線價，輕量化鋁合金加 Mastermind TCU，是要高階品牌接受價格溢價的買家對的選擇。Rad Power RadCity 5 Plus 第五 NT$49,600 砍 NT$6,200 當城市通勤選擇。\n\n禮拜五結論：嚴肅通勤族買 Level 3 NT$55,800；要價值就 Lectric XP4 750 NT$31,000；混合路面騎乘者就 Discover 3 NT$46,500。這品類國殤日週末折扣是 6 月高峰騎乘季前的地板。",
    [
        {
            "title": "Aventon Level 3 NT$55,800 是嚴肅通勤族買點",
            "body": "Aventon 美國官網砍 NT$6,200 把 Level 3 拉到 NT$55,800，高峰騎乘季前的地板。扭力感測器加 750W 後輪轂馬達加新彩色 LCD 顯示器加整合方向燈，是嚴肅通勤族對的選擇，對任何直接面對消費者的競爭對手的價值算數鎖死。"
        },
        {
            "title": "Lectric XP4 750 砍 NT$3,100 到 NT$31,000",
            "body": "XP4 750 的國殤日折扣把它拉到 NT$31,000 配可折疊跨車架加 750W 馬達加包含配件包（擋泥板、後架、車燈）。要全部包含又不付高階車架材料錢的價值買家，這個價對的選擇。"
        },
        {
            "title": "Ride1Up Discover 3 NT$46,500 贏混合路面騎乘",
            "body": "Ride1Up 砍 Discover 3 NT$6,200 到 NT$46,500 配礫石風幾何加 750W 馬達加更長續航電池。騎混合柏油加泥土路線要礫石操控又不在馬達動力上妥協的買家，這個價對的選擇。"
        }
    ],
)

add(
    "best-electric-scooters",
    [MD_CNN, MD_NBC, {
        "title": "Segway-Ninebot Memorial Day 2026 sale",
        "url": "https://www.segway.com/",
        "source": "Segway",
    }],
    "Friday morning the electric scooter category opened with Segway and NIU running their MD weekend cuts on the commuter lineups. Segway-Ninebot MAX G3 holds first at $999 with the $100 cut from Segway direct, the dual suspension plus the 22-mile range plus the self-sealing tires plus the IPX7 water resistance makes this still the right pick for serious commuters and the $999 sticker is the floor before peak riding season. Apollo City Pro at second drops to $1,499 with the $200 MD cut, the dual motor plus the dual suspension plus the regenerative braking is the right pick for buyers who want premium build quality with serious power. NIU KQi3 Pro at third holds $599 with the $100 cut, the lightweight folding plus the 31-mile range plus the simpler app is the right pick for buyers who want decent commuter without paying for premium build. Unagi Model One Voyager holds fourth at $1,290 with the $100 cut, the carbon-fiber-look frame plus the dual motor plus the design aesthetic is the right pick for buyers who care about the form factor and the carbon look. Hiboy S2 stays fifth at $399 with the $50 cut as the budget pick. Verdict for Friday: MAX G3 at $999 for serious commuters, Apollo City Pro at $1,499 for premium dual-motor, KQi3 Pro at $599 for lightweight commuter. MD weekend pricing on this category is the floor before June riding season peak.",
    [
        {
            "title": "Segway-Ninebot MAX G3 at $999 is the serious commuter buy",
            "body": "Segway direct cut $100 bringing the MAX G3 to $999, the floor before peak riding season. The dual suspension plus the 22-mile range plus the self-sealing tires plus the IPX7 water resistance makes this the right pick for serious commuters and the value math against any sub-$1k competitor at the price is locked."
        },
        {
            "title": "Apollo City Pro drops $200 to $1,499",
            "body": "The MD cut on the City Pro brings it to $1,499 with the dual motor plus the dual suspension plus the regenerative braking. For buyers who want premium build quality with serious power for hills and longer commutes, this is the right pick at the price and the value math against the Unagi is decisive."
        },
        {
            "title": "NIU KQi3 Pro at $599 wins lightweight commuter",
            "body": "NIU cut $100 on the KQi3 Pro to $599 with the lightweight folding plus the 31-mile range plus the simpler app. For buyers who want decent commuter scooter without paying for premium build and the lightweight folding matters for carrying onto transit, this is the right pick at the price."
        }
    ],
    "禮拜五早上，電動滑板車這個品類因為 Segway 跟 NIU 對通勤線推國殤日週末折扣而開盤。\n\nSegway-Ninebot MAX G3 守第一 NT$31,000 靠 Segway 美國官網砍 NT$3,100，雙避震加 22 英里續航加自封式輪胎加 IPX7 防水，還是嚴肅通勤族對的選擇，NT$31,000 就是高峰騎乘季前的地板。\n\nApollo City Pro 第二 NT$46,500 國殤日砍 NT$6,200，雙馬達加雙避震加再生煞車，是要高階做工加嚴肅動力的買家對的選擇。NIU KQi3 Pro 第三守 NT$18,600 砍 NT$3,100，輕量化折疊加 31 英里續航加更簡單應用程式，是要不錯通勤車又不付高階做工錢的買家對的選擇。\n\n講真的，Unagi Model One Voyager 第四 NT$40,000 砍 NT$3,100，碳纖維風格機架加雙馬達加設計美學，是在意外型加碳纖風的買家對的選擇。Hiboy S2 第五 NT$12,400 砍 NT$1,500 當預算選擇。\n\n禮拜五結論：嚴肅通勤族買 MAX G3 NT$31,000；要高階雙馬達就 Apollo City Pro NT$46,500；要輕量通勤就 KQi3 Pro NT$18,600。這品類國殤日週末定價是 6 月騎乘季高峰前的地板。",
    [
        {
            "title": "Segway-Ninebot MAX G3 NT$31,000 是嚴肅通勤族買點",
            "body": "Segway 美國官網砍 NT$3,100 把 MAX G3 拉到 NT$31,000，高峰騎乘季前的地板。雙避震加 22 英里續航加自封式輪胎加 IPX7 防水，是嚴肅通勤族對的選擇，對任何 NT$31,000 以下競爭對手在這個價的價值算數鎖死。"
        },
        {
            "title": "Apollo City Pro 砍 NT$6,200 到 NT$46,500",
            "body": "City Pro 的國殤日折扣把它拉到 NT$46,500 配雙馬達加雙避震加再生煞車。要高階做工加嚴肅動力應付上坡跟較長通勤的買家，這個價對的選擇，對 Unagi 的價值算數很決定性。"
        },
        {
            "title": "NIU KQi3 Pro NT$18,600 贏輕量通勤",
            "body": "NIU 砍 KQi3 Pro NT$3,100 到 NT$18,600 配輕量化折疊加 31 英里續航加更簡單應用程式。要不錯通勤滑板車又不付高階做工錢加輕量折疊對搬上大眾運輸重要的買家，這個價對的選擇。"
        }
    ],
)

add(
    "best-dash-cams",
    [MD_CNN, MD_NBC, {
        "title": "Viofo Memorial Day 2026 sale",
        "url": "https://www.viofo.com/",
        "source": "Viofo",
    }],
    "Friday morning the dash cam category opened with Viofo and Vantrue running their MD weekend cuts on the flagship 4K lineups. Viofo A329S holds first at $349 with the $50 cut from Viofo direct, the 4K plus the Sony Starvis 2 sensor plus the dual-band WiFi plus the parking mode makes this still the right pick for serious drivers and the $349 sticker is the floor outside Black Friday. Vantrue N4 Pro S at second drops to $299 with the $50 MD cut, the 3-channel coverage plus the 4K front plus the Sony Starvis 2 sensor is the right pick for rideshare drivers who need interior plus rear coverage. BlackVue Elite 9 2CH at third holds $549 with the $50 cut, the cloud connectivity plus the LTE option plus the premium build is the right pick for buyers who want cloud-uploaded footage and the BlackVue parking surveillance. Garmin Dash Cam Mini 3 holds fourth at $159 with the $20 cut, the tiny form factor plus the voice control plus the Garmin app integration is the right pick for buyers who want discreet camera. Nextbase iQ stays fifth at $499 with the $50 cut as the smart features pick. Verdict for Friday: A329S at $349 for serious flagship 4K, N4 Pro S at $299 for rideshare with interior, BlackVue Elite 9 at $549 for cloud-connected premium. Viofo MD cuts are the floor before Q4 promotions.",
    [
        {
            "title": "Viofo A329S at $349 is the serious 4K flagship buy",
            "body": "Viofo direct cut $50 bringing the A329S to $349, the floor outside Black Friday. The 4K plus the Sony Starvis 2 sensor plus the dual-band WiFi plus the parking mode makes this the right pick for serious drivers and the value math against any 4K dash cam at the price is locked."
        },
        {
            "title": "Vantrue N4 Pro S drops $50 to $299",
            "body": "The MD cut on the N4 Pro S brings it to $299 with the 3-channel coverage plus the 4K front plus the Sony Starvis 2 sensor. For rideshare drivers who need interior plus rear coverage plus the 4K front for license plate capture, this is the right pick at the price and the 3-channel value math is decisive."
        },
        {
            "title": "BlackVue Elite 9 2CH at $549 wins cloud-connected premium",
            "body": "BlackVue cut $50 on the Elite 9 to $549 with the cloud connectivity plus the LTE option plus the premium build. For buyers who want cloud-uploaded footage in case of theft and the BlackVue parking surveillance with remote video access, this is the right pick at the price."
        }
    ],
    "禮拜五早上，行車記錄器這個品類因為 Viofo 跟 Vantrue 對 4K 旗艦線推國殤日週末折扣而開盤。\n\nViofo A329S 守第一 NT$10,800 靠 Viofo 美國官網砍 NT$1,500，4K 加 Sony Starvis 2 感測器加雙頻 WiFi 加停車模式，還是嚴肅駕駛對的選擇，NT$10,800 就是黑五以外的地板。\n\nVantrue N4 Pro S 第二 NT$9,300 國殤日砍 NT$1,500，3 通道覆蓋加 4K 前鏡頭加 Sony Starvis 2 感測器，是要內部加後方覆蓋的共乘司機對的選擇。BlackVue Elite 9 2CH 第三守 NT$17,000 砍 NT$1,500，雲端連線加 LTE 選項加高階做工，是要雲端上傳影片加 BlackVue 停車監控的買家對的選擇。\n\n講真的，Garmin Dash Cam Mini 3 第四 NT$4,950 砍 NT$600，迷你外型加語音控制加 Garmin 應用程式整合，是要不顯眼相機的買家對的選擇。Nextbase iQ 第五 NT$15,500 砍 NT$1,500 當智慧功能選擇。\n\n禮拜五結論：嚴肅 4K 旗艦買 A329S NT$10,800；要共乘加內部就 N4 Pro S NT$9,300；要雲端連線高階就 BlackVue Elite 9 NT$17,000。Viofo 國殤日折扣是 Q4 促銷前的地板。",
    [
        {
            "title": "Viofo A329S NT$10,800 是嚴肅 4K 旗艦買點",
            "body": "Viofo 美國官網砍 NT$1,500 把 A329S 拉到 NT$10,800，黑五以外的地板。4K 加 Sony Starvis 2 感測器加雙頻 WiFi 加停車模式，是嚴肅駕駛對的選擇，對任何 4K 行車記錄器在這個價的價值算數鎖死。"
        },
        {
            "title": "Vantrue N4 Pro S 砍 NT$1,500 到 NT$9,300",
            "body": "N4 Pro S 的國殤日折扣把它拉到 NT$9,300 配 3 通道覆蓋加 4K 前鏡頭加 Sony Starvis 2 感測器。要內部加後方覆蓋加 4K 前鏡頭抓車牌的共乘司機，這個價對的選擇，3 通道的價值算數很決定性。"
        },
        {
            "title": "BlackVue Elite 9 2CH NT$17,000 贏雲端連線高階",
            "body": "BlackVue 砍 Elite 9 NT$1,500 到 NT$17,000 配雲端連線加 LTE 選項加高階做工。要雲端上傳影片以防被偷加 BlackVue 停車監控加遠端影片訪問的買家，這個價對的選擇。"
        }
    ],
)

add(
    "best-action-cameras",
    [MD_CNN, MD_NBC, {
        "title": "DJI Osmo Action Memorial Day 2026 sale",
        "url": "https://www.dji.com/osmo-action-6",
        "source": "DJI",
    }],
    "Friday morning the action camera category opened with DJI and Insta360 running their MD weekend cuts on the flagship lines. DJI Osmo Action 6 holds first at $349 with the $50 cut from DJI direct, the 1-inch sensor plus the magnetic mount plus the 4K at 120fps plus the latest D-Log M color profile makes this still the right pick for serious creators and the $349 sticker is the floor outside Black Friday. Insta360 Ace Pro 2 at second drops to $399 with the $50 MD cut, the Leica co-engineered lens plus the AI chip plus the flip-up screen is the right pick for buyers who want the Leica color tuning plus the flip screen for vlogging. GoPro Hero 14 Mission 1 Pro at third holds $399 with the $50 cut, the GoPro Quik integration plus the established mount ecosystem plus the proven durability is the right pick for buyers locked into the GoPro ecosystem with existing accessories. Insta360 X4 holds fourth at $499 with the $50 cut, the 360-degree 8K plus the invisible selfie stick is the right pick for buyers who want 360 capture and reframing flexibility. Akaso Brave 8 Lite stays fifth at $149 with the $30 cut as the budget pick. Verdict for Friday: Osmo Action 6 at $349 for serious creators, Ace Pro 2 at $399 for Leica plus flip screen, Hero 14 at $399 for GoPro ecosystem loyalty. The 1-inch sensor on the Osmo Action 6 is the actual differentiator at the price.",
    [
        {
            "title": "DJI Osmo Action 6 at $349 is the serious creator buy",
            "body": "DJI direct cut $50 bringing the Osmo Action 6 to $349, the floor outside Black Friday. The 1-inch sensor plus the magnetic mount plus the 4K at 120fps plus the latest D-Log M color profile makes this the right pick for serious creators and the value math against the smaller-sensor competitors at the price is decisive."
        },
        {
            "title": "Insta360 Ace Pro 2 drops $50 to $399",
            "body": "The MD cut on the Ace Pro 2 brings it to $399 with the Leica co-engineered lens plus the AI chip plus the flip-up screen. For buyers who want the Leica color tuning and the flip-up screen for vlogging-style framing while recording, this is the right pick at the price."
        },
        {
            "title": "GoPro Hero 14 holds $399 for ecosystem loyalists",
            "body": "GoPro cut $50 on the Hero 14 to $399 with the GoPro Quik integration plus the established mount ecosystem plus the proven durability. For buyers locked into the GoPro ecosystem with existing accessories and the Quik mobile editing flow, this is the right pick at the price."
        }
    ],
    "禮拜五早上，運動相機這個品類因為 DJI 跟 Insta360 對旗艦線推國殤日週末折扣而開盤。\n\nDJI Osmo Action 6 守第一 NT$10,800 靠 DJI 美國官網砍 NT$1,500，1 吋感測器加磁吸座加 4K 120fps 加最新 D-Log M 色彩描述檔，還是嚴肅創作者對的選擇，NT$10,800 就是黑五以外的地板。\n\nInsta360 Ace Pro 2 第二 NT$12,400 國殤日砍 NT$1,500，徠卡聯合工程鏡頭加 AI 晶片加翻轉螢幕，是要徠卡色彩調校加翻轉螢幕做 Vlog 的買家對的選擇。GoPro Hero 14 Mission 1 Pro 第三守 NT$12,400 砍 NT$1,500，GoPro Quik 整合加成熟的固定座生態加經驗證的耐用度，是被鎖在 GoPro 生態加既有配件的買家對的選擇。\n\n講真的，Insta360 X4 第四 NT$15,500 砍 NT$1,500，360 度 8K 加隱形自拍棒，是要 360 拍攝加重新取景彈性的買家對的選擇。Akaso Brave 8 Lite 第五 NT$4,650 砍 NT$900 當預算選擇。\n\n禮拜五結論：嚴肅創作者買 Osmo Action 6 NT$10,800；要徠卡加翻轉螢幕就 Ace Pro 2 NT$12,400；GoPro 生態忠誠就 Hero 14 NT$12,400。Osmo Action 6 的 1 吋感測器是這個價真正的差異化。",
    [
        {
            "title": "DJI Osmo Action 6 NT$10,800 是嚴肅創作者買點",
            "body": "DJI 美國官網砍 NT$1,500 把 Osmo Action 6 拉到 NT$10,800，黑五以外的地板。1 吋感測器加磁吸座加 4K 120fps 加最新 D-Log M 色彩描述檔，是嚴肅創作者對的選擇，對在這個價更小感測器競爭對手的價值算數很決定性。"
        },
        {
            "title": "Insta360 Ace Pro 2 砍 NT$1,500 到 NT$12,400",
            "body": "Ace Pro 2 的國殤日折扣把它拉到 NT$12,400 配徠卡聯合工程鏡頭加 AI 晶片加翻轉螢幕。要徠卡色彩調校加翻轉螢幕做 Vlog 風格邊錄邊取景的買家，這個價對的選擇。"
        },
        {
            "title": "GoPro Hero 14 守 NT$12,400 給生態忠誠者",
            "body": "GoPro 砍 Hero 14 NT$1,500 到 NT$12,400 配 GoPro Quik 整合加成熟固定座生態加經驗證耐用度。被鎖在 GoPro 生態加既有配件加 Quik 行動剪輯流程的買家，這個價對的選擇。"
        }
    ],
)

add(
    "best-3d-printers",
    [MD_CNN, MD_NBC, {
        "title": "Bambu Lab Memorial Day 2026 sale",
        "url": "https://us.store.bambulab.com/",
        "source": "Bambu Lab",
    }],
    "Friday morning the 3D printer category opened with Bambu Lab and Prusa running their MD weekend cuts on the flagship lineups. Bambu Lab P2S Combo holds first at $1,099 with the $200 cut from Bambu Lab direct, the AMS 2 included plus the CoreXY motion plus the carbon-fiber-capable hot end plus the 256mm build volume makes this still the right pick for serious hobbyists and the $1,099 sticker is the floor outside Black Friday. Bambu Lab X1-Carbon Combo at second drops to $1,299 with the $200 MD cut, the LiDAR plus the AMS plus the hardened nozzle plus the larger build volume is the right pick for buyers who want flagship build quality with multi-material printing. Bambu Lab H2D at third holds $1,899 with the $300 cut, the dual-extruder plus the larger build volume plus the AMS 2 is the right pick for buyers who want true dual-material printing without nozzle wipes. Prusa MK4S holds fourth at $999 with no MD discount because Prusa rarely discounts, the open-source ecosystem plus the Prusa Slicer integration plus the reliability is the right pick for buyers who refuse the Bambu closed ecosystem. Creality K2 Plus stays fifth at $1,299 with the $200 cut as the value flagship pick. Verdict for Friday: P2S Combo at $1,099 for serious hobbyists, X1-Carbon Combo at $1,299 for flagship build plus AMS, H2D at $1,899 for true dual-material. Bambu MD cuts are the deepest in this category outside Black Friday.",
    [
        {
            "title": "Bambu Lab P2S Combo at $1,099 is the serious hobbyist buy",
            "body": "Bambu Lab direct cut $200 bringing the P2S Combo to $1,099, the floor outside Black Friday. The AMS 2 included plus the CoreXY motion plus the carbon-fiber-capable hot end plus the 256mm build volume makes this the right pick for serious hobbyists and the value math against any sub-$1,200 competitor with multi-material is locked."
        },
        {
            "title": "Bambu Lab X1-Carbon Combo drops $200 to $1,299",
            "body": "The MD cut on the X1-Carbon Combo brings it to $1,299 with the LiDAR plus the AMS plus the hardened nozzle plus the larger build volume. For buyers who want flagship build quality with multi-material printing and the LiDAR for first-layer scanning, this is the right pick at the price."
        },
        {
            "title": "Prusa MK4S holds $999 — open-source ecosystem pick",
            "body": "Prusa rarely discounts the MK4S during MD weekend. The open-source ecosystem plus the Prusa Slicer integration plus the proven reliability is the right pick for buyers who refuse the Bambu closed ecosystem and value the open community modifications, and the value math is locked at MSRP."
        }
    ],
    "禮拜五早上，3D 印表機這個品類因為 Bambu Lab 跟 Prusa 對旗艦線推國殤日週末折扣而開盤。\n\nBambu Lab P2S Combo 守第一 NT$34,100 靠 Bambu Lab 美國官網砍 NT$6,200，包含 AMS 2 加 CoreXY 運動加碳纖維可用熱端加 256mm 列印體積，還是嚴肅愛好者對的選擇，NT$34,100 就是黑五以外的地板。\n\nBambu Lab X1-Carbon Combo 第二 NT$40,300 國殤日砍 NT$6,200，LiDAR 加 AMS 加硬化噴嘴加更大列印體積，是要旗艦做工加多材料列印的買家對的選擇。Bambu Lab H2D 第三守 NT$58,900 砍 NT$9,300，雙擠出機加更大列印體積加 AMS 2，是要真正雙材料列印免噴嘴擦拭的買家對的選擇。\n\n講真的，Prusa MK4S 第四守 NT$31,000 沒國殤日折扣，Prusa 很少降價，開源生態加 Prusa Slicer 整合加可靠度，是拒絕 Bambu 封閉生態的買家對的選擇。Creality K2 Plus 第五 NT$40,300 砍 NT$6,200 當價值旗艦選擇。\n\n禮拜五結論：嚴肅愛好者買 P2S Combo NT$34,100；要旗艦做工加 AMS 就 X1-Carbon Combo NT$40,300；要真正雙材料就 H2D NT$58,900。Bambu 國殤日折扣是這品類黑五以外最深。",
    [
        {
            "title": "Bambu Lab P2S Combo NT$34,100 是嚴肅愛好者買點",
            "body": "Bambu Lab 美國官網砍 NT$6,200 把 P2S Combo 拉到 NT$34,100，黑五以外的地板。包含 AMS 2 加 CoreXY 運動加碳纖維可用熱端加 256mm 列印體積，是嚴肅愛好者對的選擇，對任何 NT$37,200 以下加多材料的競爭對手的價值算數鎖死。"
        },
        {
            "title": "Bambu Lab X1-Carbon Combo 砍 NT$6,200 到 NT$40,300",
            "body": "X1-Carbon Combo 的國殤日折扣把它拉到 NT$40,300 配 LiDAR 加 AMS 加硬化噴嘴加更大列印體積。要旗艦做工加多材料列印加 LiDAR 做第一層掃描的買家，這個價對的選擇。"
        },
        {
            "title": "Prusa MK4S 守 NT$31,000 — 開源生態選擇",
            "body": "Prusa 在國殤日週末很少降 MK4S。開源生態加 Prusa Slicer 整合加經驗證可靠度，是拒絕 Bambu 封閉生態又重視開放社群改裝的買家對的選擇，價值算數鎖在牌價。"
        }
    ],
)

# ---------- POWER / VPN ----------

add(
    "best-portable-air-conditioners",
    [MD_CNN, MD_NBC, MD_LG],
    "Friday morning the portable air conditioner category opened with Midea and Whynter running their MD weekend cuts ahead of the summer heat peak. Midea Duo MAP14HS1TBL holds first at $599 with the $100 cut from Best Buy, the dual-hose plus the 14,000 BTU plus the inverter technology plus the WiFi makes this still the right pick for serious cooling and the $599 sticker is the floor before peak summer demand. Whynter NEX ARC-1230WN at second drops to $549 with the $100 MD cut, the dual-hose plus the 12,000 BTU plus the dehumidifier function is the right pick for buyers who want premium cooling at lower price than the Midea. LG LP1419IVSM Dual Inverter at third holds $549 with the $100 cut, the LG dual inverter plus the 14,000 BTU plus the LG ThinQ app is the right pick for buyers locked into the LG smart home ecosystem. Frigidaire Gallery Cool Connect FGPC1244T1 holds fourth at $499 with the $100 cut as the value LG-class pick. Black+Decker BPACT14HWT stays fifth at $399 with the $100 cut as the budget single-hose pick. Verdict for Friday: Midea Duo at $599 for serious cooling, Whynter ARC-1230WN at $549 for premium at lower price, LG LP1419IVSM at $549 for LG ecosystem. Buy now before June heat peaks demand and pushes prices back up.",
    [
        {
            "title": "Midea Duo MAP14HS1TBL at $599 is the serious cooling buy",
            "body": "Best Buy cut $100 bringing the Midea Duo to $599, the floor before peak summer demand. The dual-hose plus the 14,000 BTU plus the inverter technology plus the WiFi makes this the right pick for serious cooling and the dual-hose design is materially more efficient than single-hose competitors at the price."
        },
        {
            "title": "Whynter NEX ARC-1230WN drops $100 to $549",
            "body": "The MD cut on the Whynter brings it to $549 with the dual-hose plus the 12,000 BTU plus the dehumidifier function. For buyers who want premium dual-hose cooling at lower price than the Midea Duo and accept the slightly lower BTU rating, this is the right pick at the price."
        },
        {
            "title": "LG LP1419IVSM at $549 wins LG ecosystem",
            "body": "LG cut $100 on the LP1419IVSM to $549 with the LG dual inverter plus the 14,000 BTU plus the LG ThinQ app integration. For buyers locked into the LG smart home ecosystem who already use ThinQ for laundry or appliances and want the AC to join the same app, this is the right pick at the price."
        }
    ],
    "禮拜五早上，攜帶式冷氣機這個品類因為 Midea 跟 Whynter 在夏季熱浪高峰前推國殤日週末折扣而開盤。\n\nMidea Duo MAP14HS1TBL 守第一 NT$18,600 靠 Best Buy 砍 NT$3,100，雙管加 14,000 BTU 加變頻技術加 WiFi，還是嚴肅製冷對的選擇，NT$18,600 就是夏季高峰需求前的地板。\n\nWhynter NEX ARC-1230WN 第二 NT$17,000 國殤日砍 NT$3,100，雙管加 12,000 BTU 加除濕功能，是要高階製冷又較 Midea 低價的買家對的選擇。LG LP1419IVSM Dual Inverter 第三守 NT$17,000 砍 NT$3,100，LG 雙變頻加 14,000 BTU 加 LG ThinQ 應用程式，是被鎖在 LG 智慧家生態的買家對的選擇。\n\n講真的，Frigidaire Gallery Cool Connect FGPC1244T1 第四 NT$15,500 砍 NT$3,100 當價值 LG 級選擇。Black+Decker BPACT14HWT 第五 NT$12,400 砍 NT$3,100 當預算單管選擇。\n\n禮拜五結論：嚴肅製冷買 Midea Duo NT$18,600；要高階較低價就 Whynter ARC-1230WN NT$17,000；要 LG 生態就 LG LP1419IVSM NT$17,000。現在買，6 月熱浪高峰把需求推高價格回升前。",
    [
        {
            "title": "Midea Duo MAP14HS1TBL NT$18,600 是嚴肅製冷買點",
            "body": "Best Buy 砍 NT$3,100 把 Midea Duo 拉到 NT$18,600，夏季高峰需求前的地板。雙管加 14,000 BTU 加變頻技術加 WiFi，是嚴肅製冷對的選擇，雙管設計比同價位單管競爭對手實質上更有效率。"
        },
        {
            "title": "Whynter NEX ARC-1230WN 砍 NT$3,100 到 NT$17,000",
            "body": "Whynter 的國殤日折扣把它拉到 NT$17,000 配雙管加 12,000 BTU 加除濕功能。要高階雙管製冷又較 Midea Duo 低價接受略低 BTU 等級的買家，這個價對的選擇。"
        },
        {
            "title": "LG LP1419IVSM NT$17,000 贏 LG 生態",
            "body": "LG 砍 LP1419IVSM NT$3,100 到 NT$17,000 配 LG 雙變頻加 14,000 BTU 加 LG ThinQ 應用程式整合。被鎖在 LG 智慧家生態已用 ThinQ 在洗衣或家電要冷氣加入同一個應用程式的買家，這個價對的選擇。"
        }
    ],
)

add(
    "best-portable-chargers",
    [MD_CNN, MD_NBC, {
        "title": "Anker Memorial Day 2026 sale",
        "url": "https://www.anker.com/collections/sale",
        "source": "Anker",
    }],
    "Friday morning the portable charger category opened with Anker running 40 percent off across the lineup which is the deepest MD weekend cut on chargers ever seen. Anker Prime Power Bank (26K, 300W) holds first at $179 with the $50 cut, the 26,800mAh plus the 300W output across multiple ports plus the smart display makes this still the right pick for serious power users and the $179 sticker is the floor before Black Friday. Anker Prime Power Bank (27,650mAh, 250W) at second drops to $169 with the $40 MD cut, the slightly larger battery plus the 250W output plus the GaN charger pairing is the right pick for buyers who want maximum capacity at slightly lower wattage. Anker 737 Power Bank (PowerCore 24K, 140W) at third holds $149 with the $30 cut, the smaller form factor plus the 140W output plus the airline-compliant 99.71Wh is the right pick for buyers who fly often and need the airline-compliant capacity. Anker 633 Magnetic Wireless Charger holds fourth at $79 with the $20 cut as the wireless MagSafe-style pick. Zendure SuperTank Pro stays fifth at $199 with the $50 cut as the alternative high-wattage pick. Verdict for Friday: Prime 26K 300W at $179 for serious power users, Prime 27,650mAh at $169 for maximum capacity, 737 PowerCore 24K at $149 for frequent flyers. Anker 40 percent off across the lineup is the deepest MD weekend cut of the year.",
    [
        {
            "title": "Anker Prime 26K 300W at $179 is the serious power user buy",
            "body": "Anker direct cut $50 bringing the Prime 26K 300W to $179, the floor before Black Friday. The 26,800mAh plus the 300W output across multiple ports plus the smart display makes this the right pick for serious power users who actually need to charge a laptop and phone and tablet simultaneously, no compromise."
        },
        {
            "title": "Anker Prime 27,650mAh 250W drops $40 to $169",
            "body": "The MD cut on the Prime 27,650mAh brings it to $169 with the slightly larger battery plus the 250W output plus the GaN charger pairing. For buyers who want maximum capacity at slightly lower wattage than the 300W version and the GaN pairing matters, this is the right pick at the price."
        },
        {
            "title": "Anker 737 PowerCore 24K at $149 wins frequent flyer",
            "body": "Anker cut $30 on the 737 PowerCore 24K to $149 with the smaller form factor plus the 140W output plus the airline-compliant 99.71Wh capacity. For buyers who fly often and need the airline-compliant capacity to take onboard without issues, this is the right pick at the price and the value math is decisive."
        }
    ],
    "禮拜五早上，行動電源這個品類因為 Anker 對整個產品線推 40% 折扣而開盤，這是行動電源國殤日週末看過最深的折扣。\n\nAnker Prime Power Bank (26K, 300W) 守第一 NT$5,500 砍 NT$1,500，26,800mAh 加跨多個埠的 300W 輸出加智慧顯示器，還是嚴肅電力用戶對的選擇，NT$5,500 就是黑五前的地板。\n\nAnker Prime Power Bank (27,650mAh, 250W) 第二 NT$5,200 國殤日砍 NT$1,200，略大電池加 250W 輸出加 GaN 充電器配對，是要最大容量在略低瓦數的買家對的選擇。Anker 737 Power Bank (PowerCore 24K, 140W) 第三守 NT$4,650 砍 NT$900，更小外型加 140W 輸出加航空合規 99.71Wh，是常飛行需要航空合規容量的買家對的選擇。\n\n講真的，Anker 633 Magnetic Wireless Charger 第四 NT$2,500 砍 NT$600 當無線 MagSafe 風格選擇。Zendure SuperTank Pro 第五 NT$6,200 砍 NT$1,500 當替代高瓦數選擇。\n\n禮拜五結論：嚴肅電力用戶買 Prime 26K 300W NT$5,500；要最大容量就 Prime 27,650mAh NT$5,200；常飛行就 737 PowerCore 24K NT$4,650。Anker 整個產品線 40% 折扣是今年國殤日週末最深折扣。",
    [
        {
            "title": "Anker Prime 26K 300W NT$5,500 是嚴肅電力用戶買點",
            "body": "Anker 美國官網砍 NT$1,500 把 Prime 26K 300W 拉到 NT$5,500，黑五前的地板。26,800mAh 加跨多個埠的 300W 輸出加智慧顯示器，是嚴肅電力用戶對的選擇，真的需要同時充筆電、手機跟平板的人，沒妥協。"
        },
        {
            "title": "Anker Prime 27,650mAh 250W 砍 NT$1,200 到 NT$5,200",
            "body": "Prime 27,650mAh 的國殤日折扣把它拉到 NT$5,200 配略大電池加 250W 輸出加 GaN 充電器配對。要最大容量在略 300W 版低瓦數加 GaN 配對重要的買家，這個價對的選擇。"
        },
        {
            "title": "Anker 737 PowerCore 24K NT$4,650 贏常飛行",
            "body": "Anker 砍 737 PowerCore 24K NT$900 到 NT$4,650 配更小外型加 140W 輸出加航空合規 99.71Wh 容量。常飛行需要航空合規容量帶上機沒問題的買家，這個價對的選擇，價值算數很決定性。"
        }
    ],
)

add(
    "best-portable-power-stations",
    [MD_CNN, MD_NBC, {
        "title": "EcoFlow Memorial Day 2026 sale",
        "url": "https://www.ecoflow.com/us/sale",
        "source": "EcoFlow",
    }],
    "Friday morning the portable power station category opened with EcoFlow and Bluetti running deep MD weekend cuts and this is the right buy window for summer camping and emergency prep. EcoFlow Delta 3 Plus holds first at $799 with the $200 cut from EcoFlow direct, the 1024Wh LFP battery plus the 1800W output plus the 56-minute fast charge plus the WiFi makes this still the right pick for serious off-grid users and the $799 sticker is the floor before camping-season peak. Bluetti Elite 200 V2 at second drops to $999 with the $200 MD cut, the 2073Wh LFP plus the 2600W output plus the lighter weight is the right pick for buyers who want larger capacity than the Delta 3 Plus. Anker SOLIX C2000 Gen 2 at third holds $999 with the $200 cut, the 2048Wh LFP plus the 2400W output plus the deeper Anker ecosystem integration is the right pick for buyers who already own Anker chargers and want the cross-device app. Jackery Explorer 1500 Pro holds fourth at $999 with the $200 cut, the established Jackery brand plus the solar panel pairing is the right pick for buyers who want the Jackery solar ecosystem. EcoFlow River 3 Plus stays fifth at $399 with the $100 cut as the smaller-capacity entry pick. Verdict for Friday: Delta 3 Plus at $799 for serious off-grid users, Elite 200 V2 at $999 for larger capacity, SOLIX C2000 at $999 for Anker ecosystem. EcoFlow MD cuts on the Delta 3 Plus are the deepest of 2026 so far.",
    [
        {
            "title": "EcoFlow Delta 3 Plus at $799 is the off-grid buy",
            "body": "EcoFlow direct cut $200 bringing the Delta 3 Plus to $799, the floor before camping-season peak. The 1024Wh LFP battery plus the 1800W output plus the 56-minute fast charge plus the WiFi makes this the right pick for serious off-grid users and the value math against any 1000Wh competitor at the price is locked."
        },
        {
            "title": "Bluetti Elite 200 V2 drops $200 to $999",
            "body": "The MD cut on the Elite 200 V2 brings it to $999 with the 2073Wh LFP plus the 2600W output plus the lighter weight. For buyers who want larger capacity than the Delta 3 Plus and the lighter weight matters for portability between truck and campsite, this is the right pick at the price."
        },
        {
            "title": "Anker SOLIX C2000 Gen 2 at $999 wins Anker ecosystem",
            "body": "Anker cut $200 on the SOLIX C2000 Gen 2 to $999 with the 2048Wh LFP plus the 2400W output plus the deeper Anker ecosystem integration. For buyers who already own Anker chargers and want the cross-device app to manage all power devices, this is the right pick at the price."
        }
    ],
    "禮拜五早上，攜帶式電源這個品類因為 EcoFlow 跟 Bluetti 推深度國殤日週末折扣，這是夏季露營跟緊急準備對的買點窗口。\n\nEcoFlow Delta 3 Plus 守第一 NT$24,800 靠 EcoFlow 美國官網砍 NT$6,200，1024Wh LFP 電池加 1800W 輸出加 56 分鐘快充加 WiFi，還是嚴肅離網用戶對的選擇，NT$24,800 就是露營季高峰前的地板。\n\nBluetti Elite 200 V2 第二 NT$31,000 國殤日砍 NT$6,200，2073Wh LFP 加 2600W 輸出加更輕重量，是要比 Delta 3 Plus 大容量的買家對的選擇。Anker SOLIX C2000 Gen 2 第三守 NT$31,000 砍 NT$6,200，2048Wh LFP 加 2400W 輸出加更深 Anker 生態整合，是已有 Anker 充電器要跨裝置應用程式的買家對的選擇。\n\n講真的，Jackery Explorer 1500 Pro 第四 NT$31,000 砍 NT$6,200，成熟 Jackery 品牌加太陽能板配對，是要 Jackery 太陽能生態的買家對的選擇。EcoFlow River 3 Plus 第五 NT$12,400 砍 NT$3,100 當較小容量入門選擇。\n\n禮拜五結論：嚴肅離網用戶買 Delta 3 Plus NT$24,800；要更大容量就 Elite 200 V2 NT$31,000；要 Anker 生態就 SOLIX C2000 NT$31,000。EcoFlow 對 Delta 3 Plus 的國殤日折扣是 2026 到目前為止最深。",
    [
        {
            "title": "EcoFlow Delta 3 Plus NT$24,800 是離網買點",
            "body": "EcoFlow 美國官網砍 NT$6,200 把 Delta 3 Plus 拉到 NT$24,800，露營季高峰前的地板。1024Wh LFP 電池加 1800W 輸出加 56 分鐘快充加 WiFi，是嚴肅離網用戶對的選擇，對任何 1000Wh 競爭對手在這個價的價值算數鎖死。"
        },
        {
            "title": "Bluetti Elite 200 V2 砍 NT$6,200 到 NT$31,000",
            "body": "Elite 200 V2 的國殤日折扣把它拉到 NT$31,000 配 2073Wh LFP 加 2600W 輸出加更輕重量。要比 Delta 3 Plus 大容量加更輕重量對在卡車跟營地之間搬動重要的買家，這個價對的選擇。"
        },
        {
            "title": "Anker SOLIX C2000 Gen 2 NT$31,000 贏 Anker 生態",
            "body": "Anker 砍 SOLIX C2000 Gen 2 NT$6,200 到 NT$31,000 配 2048Wh LFP 加 2400W 輸出加更深 Anker 生態整合。已有 Anker 充電器要跨裝置應用程式管理所有電源裝置的買家，這個價對的選擇。"
        }
    ],
)

add(
    "best-vpn-services",
    [MD_CNN, MD_NBC, {
        "title": "Mullvad VPN 2026 review",
        "url": "https://mullvad.net/",
        "source": "Mullvad",
    }],
    "Friday morning the VPN category opened with NordVPN and ProtonVPN running their MD weekend cuts on the long-term subscription plans while Mullvad holds firm on the no-discount no-account policy. Mullvad VPN holds first at $5 per month flat rate with no MD discount because Mullvad refuses to play the discount game, the WireGuard protocol plus the anonymous account number plus the lack of logging plus the diskless servers makes this still the right pick for privacy-first buyers and the $5 flat rate is the right value bracket forever. ProtonVPN at second runs the MD weekend cut on the 2-year plan at $3.59 per month, the Secure Core multi-hop plus the open-source apps plus the Switzerland jurisdiction is the right pick for buyers who want strong privacy with mainstream features. NordVPN at third runs the MD weekend cut on the 2-year plan at $2.99 per month with the Threat Protection plus the Meshnet, the right pick for buyers who want broader feature set and accept the marketing-heavy brand. Surfshark holds fourth at $2.49 per month with the 2-year plan, the unlimited simultaneous connections plus the CleanWeb ad blocker is the right pick for households with many devices. ExpressVPN stays fifth at $4.99 per month with the 2-year plan as the established premium pick. Verdict for Friday: Mullvad at $5 flat for privacy-first, ProtonVPN at $3.59 for strong privacy with features, NordVPN at $2.99 for broader features at lower price. Long-term commits during MD weekend are where the actual savings live.",
    [
        {
            "title": "Mullvad holds $5 flat — no MD discount on principle",
            "body": "Mullvad refuses to play the discount game during MD weekend or ever. The WireGuard protocol plus the anonymous account number plus the lack of logging plus the diskless servers makes this the right pick for privacy-first buyers and the $5 flat rate is the right value bracket regardless of subscription length."
        },
        {
            "title": "ProtonVPN drops to $3.59/month on 2-year plan",
            "body": "The MD cut on the 2-year ProtonVPN plan brings it to $3.59 per month with the Secure Core multi-hop plus the open-source apps plus the Switzerland jurisdiction. For buyers who want strong privacy with mainstream features and accept the longer commit to lock the discount, this is the right pick."
        },
        {
            "title": "NordVPN at $2.99/month wins broader-features value",
            "body": "NordVPN's MD cut on the 2-year plan brings it to $2.99 per month with the Threat Protection plus the Meshnet plus the broader feature set. For buyers who want broader feature set at lower price than Proton and accept the marketing-heavy brand, this is the right pick at the price."
        }
    ],
    "禮拜五早上，VPN 服務這個品類因為 NordVPN 跟 ProtonVPN 對長期訂閱方案推國殤日週末折扣，而 Mullvad 守住無折扣無帳號政策。\n\nMullvad VPN 守第一月費 NT$155 平價，沒國殤日折扣，因為 Mullvad 拒絕玩折扣遊戲，WireGuard 協定加匿名帳號加無日誌加無磁碟伺服器，還是隱私優先買家對的選擇，NT$155 平價永遠都是對的價值區間。\n\nProtonVPN 第二國殤日對 2 年期方案推折扣到月費 NT$111，Secure Core 多重跳轉加開源應用程式加瑞士司法管轄，是要強隱私加主流功能的買家對的選擇。NordVPN 第三國殤日對 2 年期方案推折扣到月費 NT$93 配 Threat Protection 加 Meshnet，是要更廣功能集接受行銷重品牌的買家對的選擇。\n\n講真的，Surfshark 第四月費 NT$77 配 2 年期方案，無限同時連線加 CleanWeb 廣告阻擋，是多裝置家庭對的選擇。ExpressVPN 第五月費 NT$155 配 2 年期方案當成熟高階選擇。\n\n禮拜五結論：隱私優先買 Mullvad NT$155 平價；要強隱私加功能就 ProtonVPN NT$111；要更廣功能較低價就 NordVPN NT$93。國殤日週末長期承諾才是真正省錢的地方。",
    [
        {
            "title": "Mullvad 守 NT$155 平價 — 原則上沒國殤日折扣",
            "body": "Mullvad 拒絕在國殤日週末或任何時候玩折扣遊戲。WireGuard 協定加匿名帳號加無日誌加無磁碟伺服器，是隱私優先買家對的選擇，NT$155 平價不論訂閱長度都是對的價值區間。"
        },
        {
            "title": "ProtonVPN 砍到 2 年期月費 NT$111",
            "body": "ProtonVPN 2 年期方案的國殤日折扣把它拉到月費 NT$111 配 Secure Core 多重跳轉加開源應用程式加瑞士司法管轄。要強隱私加主流功能接受較長承諾鎖折扣的買家，這個對的選擇。"
        },
        {
            "title": "NordVPN 月費 NT$93 贏更廣功能價值",
            "body": "NordVPN 2 年期方案的國殤日折扣把它拉到月費 NT$93 配 Threat Protection 加 Meshnet 加更廣功能集。要更廣功能又較 Proton 低價接受行銷重品牌的買家，這個價對的選擇。"
        }
    ],
)

# ============================================================
# ENTRIES END — execute via add_today_entry.py
# ============================================================


def main():
    payload_json = json.dumps(ENTRIES, ensure_ascii=False)
    add_script = REPO / "scripts" / "add_today_entry.py"
    result = subprocess.run(
        ["python3", str(add_script)],
        input=payload_json,
        text=True,
        capture_output=True,
    )
    print(result.stdout)
    if result.returncode != 0:
        print("STDERR:", result.stderr)
        raise SystemExit(result.returncode)
    print(f"\nProcessed {len(ENTRIES)} categories")


if __name__ == "__main__":
    main()









