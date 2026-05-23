#!/usr/bin/env python3
"""Daily content for 2026-05-23 (Saturday — peak Memorial Day weekend day).

Saturday sits in the middle of the four-day Memorial Day window (Thu May 21 –
Mon May 25). Friday's price floors largely held overnight, retailers refreshed
stock for Saturday foot traffic, and the LG / Best Buy / Home Depot / Bose
Memorial Day pages all extended to the full weekend. Several categories saw
sharper Saturday cuts as inventory was repriced for the holiday push.

Rankings carried forward from 2026-05-22 unless an override is provided.
"""
import json
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
RANKINGS_DIR = REPO / "src" / "content" / "rankings"
TODAY = "2026-05-23"

# ============================================================
# Shared references used across multiple entries
# ============================================================
MD_CNN = {
    "title": "168 best Memorial Day sales and deals 2026",
    "url": "https://www.cnn.com/cnn-underscored/deals/best-memorial-day-sales-2026-05-18",
    "source": "CNN Underscored",
}
MD_NBC = {
    "title": "93+ Best Early Memorial Day Sales 2026",
    "url": "https://www.nbcnews.com/select/shopping/best-early-memorial-day-sales-2026-rcna345387",
    "source": "NBC Select",
}
MD_TECHRADAR = {
    "title": "Memorial Day sales are already live — the only deals worth your money",
    "url": "https://www.techradar.com/seasonal-sales/best-memorial-day-sales-2026",
    "source": "TechRadar",
}
MD_POPSCI = {
    "title": "87+ best Memorial Day deals of 2026: Gozney, Ray-Ban Meta, Vitamix",
    "url": "https://www.popsci.com/gear/best-memorial-day-deals-2026/",
    "source": "Popular Science",
}
MD_GMA = {
    "title": "Memorial Day Sales 2026: early deals to shop now",
    "url": "https://www.goodmorningamerica.com/shop/story/memorial-day-sales-2026-132496776",
    "source": "Good Morning America",
}
MD_TECHTIMES = {
    "title": "Where to Find the Best Memorial Day Tech Deals and Gadget Discounts in 2026",
    "url": "https://www.techtimes.com/articles/317048/20260523/where-find-best-memorial-day-tech-deals-gadget-discounts-2026.htm",
    "source": "Tech Times",
}
MD_BB = {
    "title": "Best Buy Memorial Day appliance sale 2026 — up to 45% off",
    "url": "https://www.techradar.com/news/best-buy-memorial-day-sale-deals",
    "source": "TechRadar",
}
MD_LG = {
    "title": "Memorial Day 2026 Sale | LG Home Appliances & Electronics",
    "url": "https://www.lg.com/us/promotions/memorial-day-sale",
    "source": "LG",
}
MD_GE = {
    "title": "Memorial Day Appliance Sale 2026",
    "url": "https://www.geappliances.com/memorial-day-appliance-sale",
    "source": "GE Appliances",
}
MD_HD = {
    "title": "Memorial Day Appliance Sale 2026",
    "url": "https://www.homedepot.com/b/Appliances/Memorial-Day-Sale/N-5yc1vZbv1wZ1z1ze0l",
    "source": "Home Depot",
}
MD_KITCHN = {
    "title": "The Best Memorial Day Kitchen Deals 2026 (Over 100!)",
    "url": "https://www.thekitchn.com/best-memorial-day-kitchen-deals-sales-2026-23782258",
    "source": "The Kitchn",
}
MD_FOX = {
    "title": "Early Memorial Day mattress deals: Save up to 66% on Nectar, Helix",
    "url": "https://www.foxnews.com/deals/best-mattress-deals",
    "source": "Fox News",
}
MD_AARP = {
    "title": "The Best Memorial Day Mattress Deals of 2026",
    "url": "https://www.aarp.org/money/personal-finance/memorial-day-mattress-deals/",
    "source": "AARP",
}
MD_SLEEPF = {
    "title": "The Best 2026 Memorial Day Mattress Sales",
    "url": "https://www.sleepfoundation.org/mattress-sales/memorial-day-mattress-sales",
    "source": "Sleep Foundation",
}
MD_FORTUNE = {
    "title": "The Best Memorial Day Mattress Sales of 2026",
    "url": "https://fortune.com/article/memorial-day-mattress-sales/",
    "source": "Fortune",
}
MD_LENOVO = {
    "title": "Memorial Day Weekend Sale 2026 | Lenovo Laptops, Desktops",
    "url": "https://www.lenovo.com/us/en/deals/memorial-day-sale/",
    "source": "Lenovo",
}
MD_TOMS_GAMING = {
    "title": "Best Buy Memorial Day PC deals — RTX 50 laptops and OLED monitors",
    "url": "https://www.tomshardware.com/gift-guides-seasonal-sales/save-hundreds-of-dollars-on-these-fantastic-best-buy-memorial-day-pc-deals-nvidia-rtx-50-series-laptops-and-oled-gaming-monitors-among-hefty-hardware-discounts",
    "source": "Tom's Hardware",
}
MD_GAMESPOT = {
    "title": "Best Buy's Memorial Day Sale - Save Up to 75% On Handhelds, Controllers",
    "url": "https://www.gamespot.com/articles/best-buy-memorial-day-gaming-sale-2026/1100-6540016/",
    "source": "GameSpot",
}
MD_CONSEQUENCE = {
    "title": "Best Headphone Deals May 2026: Top Sales on Sony, Bose, and Beats",
    "url": "https://consequence.net/2026/05/best-headphone-deals-may-2026/",
    "source": "Consequence",
}
AI_LLMSTATS = {
    "title": "AI Updates Today (May 2026) – Latest AI Model Releases",
    "url": "https://llm-stats.com/llm-updates",
    "source": "LLM Stats",
}
AI_LLMNEWS = {
    "title": "LLM News Today (May 2026) – AI Model Releases",
    "url": "https://llm-stats.com/ai-news",
    "source": "LLM Stats",
}
AI_TC_GEMINI = {
    "title": "Google updates its Gemini app to take on ChatGPT and Claude at IO 2026",
    "url": "https://techcrunch.com/2026/05/19/google-updates-its-gemini-app-to-take-on-chatgpt-and-claude-at-io-2026/",
    "source": "TechCrunch",
}
AI_CNBC_GOOGLE = {
    "title": "Google debuts new AI models, personal AI agents to keep pace with OpenAI",
    "url": "https://www.cnbc.com/2026/05/19/google-ai-ultra-gemini-spark-omni.html",
    "source": "CNBC",
}
AI_WHATLLM = {
    "title": "New AI Models May 2026: The Frontier Took a Breath, Architecture Took the Stage",
    "url": "https://whatllm.org/blog/new-ai-models-may-2026",
    "source": "WhatLLM",
}
AI_FELLO = {
    "title": "Best AI Models in May 2026: ChatGPT, Claude, Gemini & Grok",
    "url": "https://felloai.com/best-ai-models/",
    "source": "Fello AI",
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
    [MD_CNN, MD_NBC, MD_CONSEQUENCE],
    "Saturday morning the earbud chart held its Friday shape but the Amazon price refresh confirmed XM6 at $239 is the buy of the weekend, full stop. Sony WF-1000XM6 keeps first because LDAC plus the V2 processor is still the cleanest audiophile pipeline in true wireless, and the $40 off a flagship that never normally cracks before Black Friday is a price call I am willing to convict on. AirPods Pro 2 stays second at Apple-renewed $189, the iCloud handoff is still the only Apple ecosystem reason that holds up after the Pro 3 delay, and the Amazon channel has not gone lower than the renewed channel this weekend. Bose QuietComfort Earbuds II at third, the spring firmware brought call quality back in line and the QC Ultra Gen 2 update has not displaced the original from the chart yet. Samsung Galaxy Buds 4 Pro at fourth at $229 across Best Buy, the 24-bit pipeline plus the Unpacked supply stabilizing is enough to validate the slot above Buds 3 Pro. Sony WF-1000XM5 at fifth at $228 is a defensible audiophile-budget play. Saturday call: XM6 if you want the best, AirPods Pro 2 if you live in iCloud, the Saturday Amazon refresh did not produce any new floor I would chase.",
    [
        {
            "title": "Sony WF-1000XM6 at $239 is the weekend's confirmed buy",
            "body": "The $239 floor held overnight from the Friday Amazon page, which means this is not an inventory blip — Sony is letting the flagship sit at the deepest cut since launch through the holiday window. Buy Saturday, do not wait for Monday."
        },
        {
            "title": "AirPods Pro 2 at Apple-renewed $189 still the iCloud play",
            "body": "The Amazon new channel never went below the Apple-renewed channel this weekend, and the warranty math comes out identical for the first year. If you live in iCloud, $189 with renewed condition and a 1-year warranty is the second-place buy and the rebuild story stays intact."
        },
        {
            "title": "Galaxy Buds 4 Pro at $229 validates the slot",
            "body": "Best Buy held the $229 sticker into Saturday, which confirms the Buds 4 Pro slot above the Buds 3 Pro is not a temporary supply blip. The 24-bit pipeline plus the deeper Galaxy hook is the cleanest Android flagship play this weekend."
        }
    ],
    "禮拜六早上，耳機榜單守住禮拜五的形狀，Amazon 早盤更新確認 XM6 NT$7,690 是這個週末的買點，沒得議。\n\nSony WF-1000XM6 守第一，LDAC 加 V2 處理器這條音訊管線在真無線裡還是最乾淨的發燒友路線，旗艦級耳機正常時候黑五前看不到 NT$1,300 的折扣深度，這個價格我願意直接判生死。\n\nAirPods Pro 2 第二守住，蘋果整新機通路 NT$5,990，Pro 3 延後後 iCloud 整合還是唯一站得住的蘋果生態理由，Amazon 新品這個週末沒有走到整新機之下。Bose QuietComfort Earbuds II 第三，春季韌體把通話品質拉回水準，QC Ultra Gen 2 還沒把原版擠下榜。\n\n講真的，前五名的價格全部對齊我前一天的判斷，沒什麼好猶豫的。Samsung Galaxy Buds 4 Pro 第四 NT$7,290 在 Best Buy，24-bit 管線加上 Unpacked 供貨穩定，這個位置坐穩了。Sony WF-1000XM5 第五 NT$7,200，發燒友預算選說得過去。\n\n禮拜六結論：要最好就 XM6，住 iCloud 就 AirPods Pro 2，禮拜六早盤 Amazon 沒生出新的地板價值得追的。",
    [
        {
            "title": "Sony WF-1000XM6 NT$7,690 是週末確認買點",
            "body": "禮拜五 Amazon 頁面的 NT$7,690 地板價守過夜，代表這不是庫存閃失，Sony 願意讓旗艦在連假窗口維持上市以來最深的折扣。禮拜六下手，不必等禮拜一。"
        },
        {
            "title": "AirPods Pro 2 蘋果整新機 NT$5,990 還是 iCloud 派買點",
            "body": "Amazon 新品這週末沒走到整新機之下，第一年保固算下來相同。如果你住在 iCloud 裡，NT$5,990 整新機加一年保固是第二名買點，重建敘事還是站得住。"
        },
        {
            "title": "Galaxy Buds 4 Pro NT$7,290 守住位置",
            "body": "Best Buy 把 NT$7,290 守進禮拜六，確認 Buds 4 Pro 在 Buds 3 Pro 之上不是供貨閃失。24-bit 管線加深度 Galaxy 整合，是這個週末 Android 旗艦最乾淨的買法。"
        }
    ],
)

add(
    "best-noise-cancelling-headphones",
    [MD_CNN, MD_NBC, MD_CONSEQUENCE],
    "Saturday and the over-ear chart proves the Friday verdict was right: WH-1000XM6 at $349 is the buy of this weekend in this category and the Amazon refresh held that price into Saturday morning. Sony WH-1000XM6 stays first, the QN3 chip plus the 30-hour battery is the right flagship pitch and at $349 the ANC depth gap to AirPods Max stops being defensible at three times the price. Bose QuietComfort Ultra Gen 2 holds second at $379 across Best Buy and Bose direct, the April firmware fix on Immersive Audio is the reason I keep Bose ahead of Sennheiser even with the price premium. Sennheiser Momentum 4 Wireless at third at $279 keeps the audiophile-saver pitch — 60 hours of battery is still in a different universe and the Smart Control EQ is the closest the wireless segment gets to wired studio tuning. AirPods Max with USB-C stays fourth at $479 Apple Renewed because Apple still refuses to discount the model and the H1 chip is showing its age. Bowers and Wilkins Px8 hold fifth at $529 as the luxury bracket. Saturday call: WH-1000XM6 at $349 is the conviction buy, Bose at $379 if ANC depth is the priority, Sennheiser at $279 if music quality outweighs ANC. Do not wait for Monday.",
    [
        {
            "title": "WH-1000XM6 at $349 confirmed as the weekend buy",
            "body": "Amazon held the $349 price floor from Friday into Saturday and the historic low has not bumped back up. QN3 chip plus 30-hour battery plus the ANC depth gap at three-times-the-price of Max means this is the right conviction buy through Monday."
        },
        {
            "title": "Bose QC Ultra Gen 2 still $379 — premium justified",
            "body": "The April Immersive Audio firmware push fixed the spatial render and the head-tracking lag, which is why Bose still earns the $30 premium over Sony for buyers prioritizing ANC depth and long-flight comfort. The Saturday price held."
        },
        {
            "title": "Momentum 4 at $279 is the music-first saver",
            "body": "Sixty hours of battery plus Smart Control EQ tuning at $279 saves $70 over Sony's price and delivers the closest the wireless segment gets to a wired studio sound. This is the right buy for buyers who put music quality ahead of ANC depth."
        }
    ],
    "禮拜六，頭戴式榜單證實禮拜五的判斷是對的，WH-1000XM6 NT$10,990 就是這個品類週末的買點，Amazon 早盤把這個價守進禮拜六早上。\n\nSony WH-1000XM6 守第一，QN3 晶片加 30 小時電池是對的旗艦定位，NT$10,990 跟 AirPods Max 之間的 ANC 深度差，在 Max 賣三倍價的前提下已經完全沒得辯。\n\nBose QuietComfort Ultra Gen 2 第二 NT$11,990 在 Best Buy 跟 Bose 美國官網都守住，四月 Immersive Audio 韌體修正是我把 Bose 擺在 Sennheiser 前面的理由，溢價合理。\n\n講真的，Sennheiser Momentum 4 Wireless 第三 NT$8,790 還是發燒友省錢解，60 小時電池在另一個宇宙，Smart Control EQ 是無線耳機裡最接近錄音室調音的選擇。AirPods Max USB-C 第四 NT$15,200 整新機，Apple 還是不肯打折，H1 晶片老態畢露。Bowers and Wilkins Px8 第五 NT$16,900 守住奢華檔。\n\n禮拜六結論：WH-1000XM6 NT$10,990 是有底氣的買點，要 ANC 深度就 Bose NT$11,990，音樂派就 Sennheiser NT$8,790 省 NT$2,200。不必等禮拜一。",
    [
        {
            "title": "WH-1000XM6 NT$10,990 確認為週末買點",
            "body": "Amazon 把禮拜五的 NT$10,990 地板價守進禮拜六，這個歷史新低沒往上跳。QN3 晶片加 30 小時電池加 Max 三倍價的 ANC 深度差，這就是禮拜一前該下手的有底氣買點。"
        },
        {
            "title": "Bose QC Ultra Gen 2 守 NT$11,990 溢價有理",
            "body": "四月 Immersive Audio 韌體推送修好空間音訊渲染跟頭部追蹤延遲，這就是 Bose 在 ANC 深度跟長途飛行舒適度派買家面前可以收 NT$1,000 溢價的原因。禮拜六價格守住。"
        },
        {
            "title": "Momentum 4 NT$8,790 是音樂優先的省錢解",
            "body": "60 小時電池加 Smart Control EQ 調音，NT$8,790 比 Sony 省 NT$2,200，給出無線耳機裡最接近錄音室聲音的體驗。這是把音樂品質放在 ANC 深度前面的買家正確的買法。"
        }
    ],
)

add(
    "best-bluetooth-speakers",
    [MD_CNN, MD_NBC, {
        "title": "Bose Memorial Day sale 2026: best prices of year",
        "url": "https://www.bose.com/c/sales",
        "source": "Bose",
    }],
    "Saturday morning the portable speaker category is the unexpected MD weekend winner because Bose extended the SoundLink discount into Saturday and the JBL Charge 6 at Best Buy held the $159 sticker overnight. JBL Charge 6 keeps first, the IP68 plus the PartyBoost 2 chain plus the 28-hour battery is the most flexible $200-class outdoor speaker and the $40 cut survives. Marshall Emberton III holds second at $139, the 32-hour battery plus the design-conscious vintage aesthetic is the right pitch for the buyer who wants the form factor. Bose SoundLink Max holds third at $349 because Bose extended its best-price-of-year through the weekend, the room-filling output and the deep low-end is the right indoor anchor without a Sonos setup. Sonos Roam 2 at fourth at $179, the multi-room handoff to Era and the WiFi-plus-BT flexibility is for buyers already in Sonos. UE Boom 4 at $129 is the budget anchor with 360-degree dispersion. Saturday verdict: Charge 6 if you want one outdoor speaker that does everything, SoundLink Max if you want one indoor speaker to anchor a room, the Sonos Roam buy is only worth it if you are buying the multi-room story. The MD window through Monday will not get materially better on this category.",
    [
        {
            "title": "JBL Charge 6 at $159 still the all-purpose pick",
            "body": "Best Buy held the $40 cut from Friday morning into Saturday, which means the IP68 plus 28-hour battery plus PartyBoost 2 chain stack is sitting at the best outdoor-speaker price the category has seen this year. The Saturday refresh did not move it."
        },
        {
            "title": "Bose SoundLink Max at $349 stays in the window",
            "body": "Bose held the SoundLink Max in the MD discount window through Saturday, and at $349 the room-filling output plus the deep low-end is the indoor anchor for buyers who refuse a Sonos buildout. First time Bose has competed on holiday pricing on this model this year."
        },
        {
            "title": "Marshall Emberton III at $139 — design-driven buy",
            "body": "Marshall held the $30 cut through Saturday morning. 32-hour battery plus the vintage Marshall form factor at $139 hits the buyer who would pay extra for the design, and the cut finally makes the value math defensible against the JBL and UE alternatives."
        }
    ],
    "禮拜六早上，攜帶式喇叭是國殤日週末的意外贏家，Bose 把 SoundLink 折扣延進禮拜六，JBL Charge 6 在 Best Buy 守住 NT$5,200 的價格守過夜。\n\nJBL Charge 6 守第一，IP68 加 PartyBoost 2 串接加 28 小時電池，這個價位帶最彈性的戶外喇叭，NT$1,300 的折扣沒消失。\n\nMarshall Emberton III 第二 NT$4,500，32 小時電池加設計派的復古美學，打中願意為了外型多付的買家，這個價格站得住。\n\n講真的，Bose SoundLink Max 第三 NT$11,300，Bose 把全年最佳價延到週末，滿房間輸出加紮實低頻是不想搞 Sonos 整套的室內錨點。Sonos Roam 2 第四 NT$5,800，跟 Era 喇叭的多房間切換加 WiFi 加藍牙彈性，是已經在 Sonos 生態裡的買家正確選擇。UE Boom 4 NT$4,200 守預算錨點。\n\n禮拜六結論：要一台戶外全能就 Charge 6，要一台室內坐鎮就 SoundLink Max，Sonos Roam 只有在你要買多房間敘事的時候才划算。這品類國殤日到禮拜一不會有實質更好的價了。",
    [
        {
            "title": "JBL Charge 6 NT$5,200 全能選擇守住",
            "body": "Best Buy 把禮拜五早上的 NT$1,300 折扣守進禮拜六，代表 IP68 加 28 小時電池加 PartyBoost 2 串接這套組合就坐在這品類今年最好的戶外喇叭價位上。禮拜六的更新沒動到。"
        },
        {
            "title": "Bose SoundLink Max NT$11,300 守在窗口內",
            "body": "Bose 把 SoundLink Max 守在國殤日折扣窗口進禮拜六，NT$11,300 的滿房間輸出加上紮實低頻，給不想搞 Sonos 整套又要室內錨點的買家正中下懷。Bose 今年第一次在這個型號跟節慶定價競爭。"
        },
        {
            "title": "Marshall Emberton III NT$4,500 設計派買點",
            "body": "Marshall 把 NT$1,000 折扣守進禮拜六早上。32 小時電池加 Marshall 復古外型 NT$4,500，打中願意為設計多付的買家，這個折扣終於把性價比補上 JBL 跟 UE 的競爭線。"
        }
    ],
)

add(
    "best-smart-speakers",
    [MD_CNN, MD_NBC, {
        "title": "Sonos Memorial Day Sale 2026",
        "url": "https://www.sonos.com/en-us/shop/deals",
        "source": "Sonos",
    }],
    "Saturday and the smart speaker chart confirms what I said yesterday: MD weekend barely moves Echo and HomePod because Amazon and Apple do not compete on holiday pricing for the first-party speakers. Echo Studio 2nd Gen holds first at $199, the AZ3 chip plus the new spatial audio rendering is a category leap and at $199 it is the right Alexa-room anchor. Sonos Era 100 stays second at $199 because Sonos held the rare $50 MD cut through Saturday, Trueplay room tuning plus the multi-room handoff is still the gold standard for a single-speaker room. HomePod 2nd Gen holds third at $299 because Apple still refuses to discount, the AirPlay 2 handoff and Siri integration is the only premium reason. Nest Audio at $79 at Best Buy keeps the budget bracket. Saturday verdict: Sonos Era 100 at $199 is the rare buy because Sonos almost never discounts and this is the cleanest entry into the platform, Echo Studio if you live in Alexa, HomePod if you live in Apple. The Sonos window will close Monday and the Era 100 price is the only one moving on this category this weekend.",
    [
        {
            "title": "Sonos Era 100 holds $199 — rare MD buy",
            "body": "Sonos held the $50 cut on the Era 100 through Saturday morning, which is the rare buy window because Sonos almost never moves holiday pricing. Trueplay tuning plus multi-room handoff plus WiFi-plus-BT dual radio is the cleanest entry into the Sonos platform and the only price actually moving in this category."
        },
        {
            "title": "Echo Studio at $199 — Alexa room anchor",
            "body": "The AZ3 chip plus the new spatial audio rendering is the genuine category leap over the original Studio, and at $199 it is the right pitch for any Alexa-anchored living room. The $50 cut from launch is the discount Amazon will hold through the weekend."
        },
        {
            "title": "HomePod 2nd Gen — Apple holds the line at $299",
            "body": "Apple still refuses to discount the HomePod and Saturday did not change that. The AirPlay 2 handoff plus Siri integration is the only premium justification, and unless you are locked into Apple already, wait for the iPhone 17 refresh cycle before paying $299."
        }
    ],
    "禮拜六，智慧喇叭榜單證實我昨天說的：國殤日對 Echo 跟 HomePod 沒什麼影響，因為 Amazon 跟 Apple 不會在節日跟自家喇叭打折扣戰。\n\nEcho Studio 2nd Gen 守第一 NT$6,200，AZ3 晶片加上空間音訊渲染是品類級跳躍，NT$6,200 是對的 Alexa 房間錨點。\n\nSonos Era 100 第二 NT$6,200，Sonos 把罕見的 NT$1,500 國殤日折扣守進禮拜六，Trueplay 自動房間調音加多房間切換還是單顆喇叭房間的金標準。\n\n講真的，HomePod 2nd Gen 第三 NT$9,290，Apple 還是不肯打折，AirPlay 2 切換跟 Siri 整合是唯一付溢價的理由。Nest Audio NT$2,500 在 Best Buy 守預算錨點。\n\n禮拜六結論：Sonos Era 100 NT$6,200 是罕見買點，因為 Sonos 幾乎不打折，這週末是進平台最乾淨的機會。住 Alexa 就 Echo Studio，住 Apple 就 HomePod。Sonos 這個窗口禮拜一關，這品類週末只有 Era 100 的價格真的在動。",
    [
        {
            "title": "Sonos Era 100 守 NT$6,200，國殤日罕見買點",
            "body": "Sonos 把 Era 100 的 NT$1,500 折扣守進禮拜六早上，這是 Sonos 幾乎不動節日定價的稀有買點。Trueplay 調音加多房間切換加 WiFi 跟藍牙雙射頻，是進 Sonos 平台最乾淨的方式，這品類週末只有這個價真的在動。"
        },
        {
            "title": "Echo Studio NT$6,200 Alexa 客廳錨點",
            "body": "AZ3 晶片加新的空間音訊渲染是比原版 Studio 真的有品類級跳躍，NT$6,200 是對任何 Alexa 客廳建構正確的話術。比上市定價砍 NT$1,500 就是 Amazon 這個週末會守住的折扣。"
        },
        {
            "title": "HomePod 2nd Gen Apple 守 NT$9,290",
            "body": "Apple 還是拒絕對 HomePod 打折，禮拜六也沒變。AirPlay 2 切換加 Siri 整合是唯一付溢價的理由，沒被 Apple 鎖住的人，等 iPhone 17 換機週期再說 NT$9,290。"
        }
    ],
)

# ---------- WEARABLES ----------

add(
    "best-smart-watches",
    [MD_CNN, MD_NBC, {
        "title": "Best smartwatch deals May 2026",
        "url": "https://www.tomsguide.com/wellness/smartwatches",
        "source": "Tom's Guide",
    }],
    "Saturday morning the smartwatch chart is largely unchanged because Apple and Samsung both held their MD price floors overnight. Apple Watch Series 10 keeps first at $329 (down from $399), the S10 chip plus the wider display plus the new sleep apnea detection is still the right flagship pitch and at $70 off through Best Buy this is the buy of the weekend in this category. Apple Watch Ultra 2 holds second at $699 with the $100 cut from Apple direct, the rugged frame and the longer battery is the right pitch for the outdoor athlete. Samsung Galaxy Watch 7 Classic at third at $359 with the rotating bezel back is the Android answer and the $80 cut through Samsung direct lands. Garmin Forerunner 965 at fourth at $499 holds, Garmin almost never discounts so the $100 cut on the 965 is rare. Pixel Watch 4 at fifth at $279 lands the budget Wear OS bracket. Saturday verdict: Series 10 at $329 if you are on iPhone, Watch 7 Classic at $359 if you are on Android, Forerunner 965 at $499 if running is your main use case. The MD prices will hold through Monday.",
    [
        {
            "title": "Apple Watch Series 10 at $329 — the weekend buy",
            "body": "Best Buy held the $70 cut from Friday into Saturday, and the S10 chip plus the wider display plus sleep apnea detection at $329 is the right flagship Apple play for any iPhone owner. No reason to wait for Monday."
        },
        {
            "title": "Watch Ultra 2 at $699 — Apple's rare $100 cut",
            "body": "Apple direct kept the $100 cut on Ultra 2 through Saturday, which is rare because Apple almost never discounts its flagship Watch SKUs. Rugged titanium frame plus the longer battery is the right outdoor-athlete pitch and the price floor justifies the slot."
        },
        {
            "title": "Garmin Forerunner 965 at $499 — rare Garmin discount",
            "body": "Garmin almost never participates in holiday pricing, so the $100 cut on the Forerunner 965 through Saturday is the rare buy window. The training-load math plus the multi-band GPS plus the long battery is the right call for buyers who put running ahead of smartwatch features."
        }
    ],
    "禮拜六早上，智慧手錶榜單大致沒動，Apple 跟 Samsung 都把國殤日地板價守過夜。\n\nApple Watch Series 10 守第一 NT$10,500（原 NT$12,700），S10 晶片加更寬螢幕加新的睡眠呼吸中止偵測還是對的旗艦定位，Best Buy 砍 NT$2,200 是這品類週末的買點。\n\nApple Watch Ultra 2 第二 NT$22,300 Apple 美國官網守 NT$3,200 折扣，堅固機身加長電池對戶外運動派是對的話術。Samsung Galaxy Watch 7 Classic 第三 NT$11,500 旋轉錶圈回歸加 Samsung 直營砍 NT$2,500，是 Android 的對應解。\n\n講真的，Garmin Forerunner 965 第四 NT$15,900，Garmin 幾乎不打折，這次砍 NT$3,200 罕見。Pixel Watch 4 第五 NT$8,900 守預算 Wear OS 檔。\n\n禮拜六結論：iPhone 就 Series 10 NT$10,500，Android 就 Watch 7 Classic NT$11,500，跑步派就 Forerunner 965 NT$15,900。國殤日價守到禮拜一。",
    [
        {
            "title": "Apple Watch Series 10 NT$10,500 週末買點",
            "body": "Best Buy 把禮拜五的 NT$2,200 折扣守進禮拜六，S10 晶片加寬螢幕加睡眠呼吸中止偵測在 NT$10,500，是對任何 iPhone 用戶正確的旗艦選擇。不必等禮拜一。"
        },
        {
            "title": "Watch Ultra 2 NT$22,300 Apple 罕見砍 NT$3,200",
            "body": "Apple 直營把 Ultra 2 的 NT$3,200 折扣守進禮拜六，罕見因為 Apple 幾乎不對旗艦 Watch SKU 打折。鈦合金堅固機身加長電池是對戶外運動派的話術，這個地板價對得起位置。"
        },
        {
            "title": "Garmin Forerunner 965 NT$15,900 罕見折扣",
            "body": "Garmin 幾乎不參與節慶定價，禮拜六守住的 NT$3,200 折扣是罕見買點。訓練負荷算法加多頻 GPS 加長電池，對把跑步擺在智慧手錶功能前面的買家是對的選擇。"
        }
    ],
)

add(
    "best-smart-rings",
    [MD_CNN, {
        "title": "Best smart ring 2026: Oura, Samsung, RingConn tested",
        "url": "https://www.techradar.com/health-fitness/fitness-trackers/best-smart-ring",
        "source": "TechRadar",
    }, {
        "title": "Best smart rings in 2026: Oura, Ultrahuman, Samsung",
        "url": "https://www.stuff.tv/features/best-smart-rings/",
        "source": "Stuff",
    }],
    "Saturday and the smart ring chart held its Friday shape because Oura and Samsung both lead the category with negligible MD discounting — they do not have to play the holiday game. Oura Ring 4 holds first at $349, the polished app plus the superior stress/sleep/health tracking accuracy is the right pitch for the buyer who wants the most-tested platform, and the new Wellbeing membership pricing rolled out in April still makes the $349 + $5.99/mo math defensible. Samsung Galaxy Ring stays second at $379 because Samsung is still fighting Oura in court over the twelve patents that Samsung argues should be invalidated, and the supply situation has stabilized. RingConn Gen 2 holds third at $299 — no subscription, two-week battery, the right pitch for the buyer who refuses Oura's recurring fee. Ultrahuman Ring AIR at $349 holds fourth, the metabolic and sleep-stage models are competitive but the app lags Oura. Pebble Round 2 lands as the new e-paper-display hybrid at $199 in May but is not yet a full ring competitor. Saturday verdict: Oura Ring 4 if you want the most-mature platform, Samsung Galaxy Ring if you live in Galaxy, RingConn Gen 2 if you refuse subscriptions. No new MD floors moved overnight.",
    [
        {
            "title": "Oura Ring 4 at $349 — most-mature platform holds",
            "body": "Oura did not discount for MD and did not need to. The polished app plus the most-tested sleep, stress and health-tracking accuracy is what justifies the $349 sticker and the membership fee. The April Wellbeing pricing refresh still makes the math defensible against the no-subscription alternatives."
        },
        {
            "title": "Samsung Galaxy Ring at $379 — Galaxy ecosystem play",
            "body": "Samsung is still fighting Oura in court over the patent suite that Samsung argues should be invalidated, but the consumer product supply has stabilized and the Galaxy integration is now polished. At $379 this is the right pitch for buyers locked into Galaxy phones and Watch."
        },
        {
            "title": "RingConn Gen 2 at $299 — the no-subscription option",
            "body": "Two-week battery, no recurring fee, full HR plus SpO2 plus skin temperature, and a comfortable titanium build. At $299 this is the right call for buyers who refuse Oura's $5.99/mo and refuse to be locked into Galaxy."
        }
    ],
    "禮拜六，智慧戒指榜單守住禮拜五形狀，Oura 跟 Samsung 在這品類領跑，國殤日折扣可有可無——它們本來就不必玩節慶這套。\n\nOura Ring 4 守第一 NT$10,800，精緻的 App 加上最被測試過的壓力、睡眠、健康追蹤精準度，是對想要最成熟平台買家的話術，四月 Wellbeing 會員費調整後 NT$10,800 加 NT$190/月的算數還是站得住。\n\nSamsung Galaxy Ring 第二 NT$11,800，Samsung 還在法院跟 Oura 打 12 個專利的官司，Samsung 反告主張這些專利應該無效，消費端供貨穩定，Galaxy 整合已經精緻。\n\n講真的，RingConn Gen 2 第三 NT$9,290，無訂閱、兩週電池，是拒絕 Oura 月費的買家正確選擇。Ultrahuman Ring AIR 第四 NT$10,800，代謝跟睡眠階段模型有競爭力但 App 落後 Oura。Pebble Round 2 五月以 e-paper 顯示混血錶 NT$6,200 上市但還不算完整的戒指對手。\n\n禮拜六結論：要最成熟就 Oura Ring 4，住 Galaxy 就 Samsung Galaxy Ring，拒絕訂閱就 RingConn Gen 2。國殤日早盤沒有新地板價。",
    [
        {
            "title": "Oura Ring 4 NT$10,800 最成熟平台守住",
            "body": "Oura 國殤日沒打折，也不必。精緻的 App 加最被測試過的睡眠、壓力、健康追蹤精準度，撐起 NT$10,800 的牌價跟會員費。四月 Wellbeing 定價調整後跟無訂閱的對手比，這個算數還是站得住。"
        },
        {
            "title": "Samsung Galaxy Ring NT$11,800 Galaxy 生態派買點",
            "body": "Samsung 還在法院跟 Oura 打 12 個專利的官司，Samsung 反告主張這些專利應該無效，但消費端供貨穩定，Galaxy 整合已經精緻。NT$11,800 對被鎖在 Galaxy 手機跟 Watch 的買家是對的話術。"
        },
        {
            "title": "RingConn Gen 2 NT$9,290 無訂閱選擇",
            "body": "兩週電池、無月費、完整 HR 加 SpO2 加皮膚溫度，加上舒適的鈦合金機身。NT$9,290 對拒絕 Oura NT$190/月又拒絕被 Galaxy 綁住的買家是對的話術。"
        }
    ],
)

add(
    "best-smart-glasses",
    [MD_POPSCI, MD_TECHTIMES, {
        "title": "Ray-Ban Meta smart glasses Memorial Day discount tracking",
        "url": "https://www.popsci.com/gear/best-memorial-day-deals-2026/",
        "source": "Popular Science",
    }],
    "Saturday morning the smart glasses chart confirms Ray-Ban Meta still owns this category and the MD discount window has Popular Science flagging Ray-Ban Meta in its top deal list. Ray-Ban Meta Gen 2 keeps first at $279 (down from $299), the Wayfarer form factor plus the upgraded camera plus the Meta AI integration on the new Llama 4 multimodal backbone is the right pitch and the $20 cut survives the Saturday refresh. Meta x Oakley HSTN holds second at $329, the sports-focused form factor plus the better fit for athletic use cases hits a specific buyer. Xreal Air 2 Pro at third at $499 holds because the AR display experience is genuinely category-leading for media playback, even though the everyday-glasses pitch is weaker. Even Realities G1 stays fourth at $549 with the better fit-and-finish hardware. Snap Spectacles 5 at $329 fifth — the public release this spring landed and the Snap AR app library is competitive but the camera quality lags Ray-Ban. Saturday verdict: Ray-Ban Meta Gen 2 at $279 is the conviction buy for everyday wear, Xreal at $499 for media playback, Oakley HSTN if you wear them for sports. The window holds through Monday.",
    [
        {
            "title": "Ray-Ban Meta Gen 2 at $279 — the conviction buy",
            "body": "Popular Science flagged Ray-Ban Meta in its MD top-deals list and the $20 cut held through Saturday morning. The Wayfarer form factor plus the upgraded camera plus the Llama 4 multimodal Meta AI is the right everyday-wear pitch and the price floor justifies the slot."
        },
        {
            "title": "Meta x Oakley HSTN at $329 — sports-form play",
            "body": "Oakley HSTN holds the sports-focused form factor for athletic use cases where the Wayfarer does not fit, and at $329 the camera quality plus the better fit during exercise is the right pitch for runners and cyclists. The Meta AI backbone is identical to Ray-Ban Gen 2."
        },
        {
            "title": "Xreal Air 2 Pro at $499 — media AR holds",
            "body": "The AR display experience for media playback is still genuinely category-leading because the 1080p microOLED panels plus the wider FOV deliver a virtual cinema feel that Ray-Ban and Oakley do not attempt. At $499 this is the right pitch for buyers who want a portable big-screen substitute."
        }
    ],
    "禮拜六早上，智慧眼鏡榜單確認 Ray-Ban Meta 還是這品類霸主，國殤日折扣窗口讓 Popular Science 把 Ray-Ban Meta 列進頂級優惠清單。\n\nRay-Ban Meta Gen 2 守第一 NT$8,790（原 NT$9,400），Wayfarer 經典版型加升級鏡頭加 Llama 4 多模態 Meta AI 整合，是對的話術，NT$620 折扣熬過禮拜六早盤。\n\nMeta x Oakley HSTN 第二 NT$10,300，運動向版型加運動使用情境的更貼合，打中特定買家。\n\n講真的，Xreal Air 2 Pro 第三 NT$15,700，AR 顯示體驗在媒體播放上真的是品類領跑，雖然當日常眼鏡的話術較弱。Even Realities G1 第四 NT$17,200 更好的硬體做工。Snap Spectacles 5 第五 NT$10,300，春季公開發售上市，Snap AR App 庫有競爭力但鏡頭品質落後 Ray-Ban。\n\n禮拜六結論：日常配戴就 Ray-Ban Meta Gen 2 NT$8,790 有底氣，媒體播放就 Xreal NT$15,700，運動配戴就 Oakley HSTN NT$10,300。窗口守到禮拜一。",
    [
        {
            "title": "Ray-Ban Meta Gen 2 NT$8,790 有底氣買點",
            "body": "Popular Science 把 Ray-Ban Meta 列進國殤日頂級優惠清單，NT$620 折扣守進禮拜六早上。Wayfarer 經典版型加升級鏡頭加 Llama 4 多模態 Meta AI，是對的日常配戴話術，這個地板價對得起位置。"
        },
        {
            "title": "Meta x Oakley HSTN NT$10,300 運動版型解",
            "body": "Oakley HSTN 守住運動向版型，給 Wayfarer 不適合的運動情境，NT$10,300 的鏡頭品質加運動中的更好貼合是對跑者跟自行車手的話術。Meta AI 後端跟 Ray-Ban Gen 2 一樣。"
        },
        {
            "title": "Xreal Air 2 Pro NT$15,700 媒體 AR 守住",
            "body": "AR 媒體播放體驗還是品類領跑，1080p microOLED 加更寬 FOV 給出 Ray-Ban 跟 Oakley 不嘗試的虛擬影院感。NT$15,700 對想要可攜大螢幕替代品的買家是對的選擇。"
        }
    ],
)

# ---------- COMPUTING ----------

add(
    "best-laptops",
    [MD_TOMS_GAMING, MD_LENOVO, MD_CNN],
    "Saturday morning the laptop chart confirms the RTX 50 generation discount window is open through MD weekend. Best Buy and Lenovo both extended the Friday floors into Saturday. Apple MacBook Air M5 13-inch holds first at $999 with the $200 cut from Apple direct, the M5 chip plus 18-hour battery is still the right thin-and-light pitch and the cut through MD weekend is rare for Apple. ASUS ROG Zephyrus G16 stays second at $1,799 (down $400 at Best Buy), the OLED panel plus the RTX 5070 plus the 1.85kg form factor is the right gaming-ultrabook pitch. Lenovo ThinkPad X1 Carbon Gen 13 holds third at $1,799, the Lenovo MD weekend cut $400 off and the Lunar Lake plus 16GB RAM is the right business pitch. MacBook Pro M5 Pro 14-inch at fourth at $1,899 (down $100), the M5 Pro chip plus the mini-LED display is the right creator pitch. Framework Laptop 13 holds fifth at $1,099 for the modular bracket. Saturday verdict: MacBook Air M5 at $999 if you want a thin-and-light, Zephyrus G16 at $1,799 if you want a gaming-creator hybrid, ThinkPad X1 Carbon at $1,799 if business is your main use. The MD window holds through Monday.",
    [
        {
            "title": "MacBook Air M5 at $999 — Apple's rare MD cut",
            "body": "Apple direct held the $200 cut on the M5 13-inch into Saturday, which is the rare buy window because Apple almost never discounts the current-generation MacBook Air. The M5 chip plus 18-hour battery plus the Air form factor at $999 is the conviction buy for anyone who needs portability over raw power."
        },
        {
            "title": "Zephyrus G16 at $1,799 — gaming-creator hybrid",
            "body": "Best Buy held the $400 cut on the G16 through Saturday. RTX 5070 plus the OLED panel plus the 1.85kg form factor is the right gaming-ultrabook pitch and at $1,799 this is the only RTX 50-generation laptop hitting that price-weight combination this weekend."
        },
        {
            "title": "ThinkPad X1 Carbon Gen 13 at $1,799 — Lenovo cut holds",
            "body": "Lenovo's MD weekend sale held the $400 cut on the X1 Carbon through Saturday. Lunar Lake plus the carbon-fiber chassis plus 16GB RAM is the right business pitch and the $1,799 price brings the X1 Carbon back into the conversation against the MacBook Air for road-warrior buyers."
        }
    ],
    "禮拜六早上，筆電榜單確認 RTX 50 世代折扣窗口在國殤日週末打開，Best Buy 跟 Lenovo 都把禮拜五的地板價延進禮拜六。\n\nApple MacBook Air M5 13 吋守第一 NT$31,400 Apple 直營砍 NT$6,300，M5 晶片加 18 小時電池還是輕薄筆電的對的話術，國殤日延進來這個折扣對 Apple 罕見。\n\nASUS ROG Zephyrus G16 第二 NT$56,500（Best Buy 砍 NT$12,600），OLED 螢幕加 RTX 5070 加 1.85 公斤機身，是電競超薄筆電的對的話術。Lenovo ThinkPad X1 Carbon Gen 13 第三 NT$56,500，Lenovo 國殤日砍 NT$12,600，Lunar Lake 加 16GB RAM 是商務派的話術。\n\n講真的，MacBook Pro M5 Pro 14 吋第四 NT$59,700（砍 NT$3,200），M5 Pro 加 mini-LED 是創作者的話術。Framework Laptop 13 第五 NT$34,500 守模組化檔。\n\n禮拜六結論：輕薄就 MacBook Air M5 NT$31,400，電競加創作混血就 Zephyrus G16 NT$56,500，商務就 ThinkPad X1 Carbon NT$56,500。國殤日窗口守到禮拜一。",
    [
        {
            "title": "MacBook Air M5 NT$31,400 Apple 罕見國殤日折扣",
            "body": "Apple 直營把 M5 13 吋的 NT$6,300 折扣守進禮拜六，這是罕見買點，因為 Apple 幾乎不對當代 MacBook Air 打折。M5 晶片加 18 小時電池加 Air 版型 NT$31,400，是把可攜性擺在純算力前面的買家正確選擇。"
        },
        {
            "title": "Zephyrus G16 NT$56,500 電競創作混血",
            "body": "Best Buy 把 G16 的 NT$12,600 折扣守進禮拜六。RTX 5070 加 OLED 螢幕加 1.85 公斤版型是電競超薄筆電的對的話術，NT$56,500 是這個週末唯一打到這個價格重量組合的 RTX 50 世代筆電。"
        },
        {
            "title": "ThinkPad X1 Carbon Gen 13 NT$56,500 Lenovo 折扣守住",
            "body": "Lenovo 國殤日週末特賣把 X1 Carbon 的 NT$12,600 折扣守進禮拜六。Lunar Lake 加碳纖維機身加 16GB RAM 是商務派的話術，NT$56,500 把 X1 Carbon 拉回跟 MacBook Air 在路上戰士買家的對話。"
        }
    ],
)

add(
    "best-4k-tvs",
    [MD_CNN, MD_LG, MD_BB],
    "Saturday and the 4K TV chart is where MD weekend math actually pays off. LG's MD page held the 30-58% off through Saturday, Best Buy is at up to 45% off, and Hisense at Lowe's is up to 45% off. LG C5 OLED 65 stays first at $1,799 (down $700), the WOLED panel plus the new α11 processor is the right gaming-creator pitch for 2026 and the cut survives Saturday. Samsung S95F QD-OLED 65 holds second at $2,499 (down $1,000), the QD-OLED brightness plus the One Connect Box is the right premium living-room pitch. Sony Bravia 9 Mini-LED 65 holds third at $2,498 with the new XR Backlight Master Drive at thousands of zones. Hisense U8N Mini-LED 65 at fourth at $999 (down $300 at Lowe's) — the brightness-per-dollar leader at this price floor. TCL QM9K Mini-LED at fifth at $2,499 — the new flagship I added yesterday with native 144Hz and 6,000+ nits. LG G5 OLED Evo 65 at sixth at $2,799 (down $700 at LG direct) — the right premium OLED for cinephiles. Saturday verdict: C5 if you want OLED at the best price, S95F if QD-OLED brightness matters, U8N if you want the best brightness-per-dollar. The MD window will not get materially better through Monday.",
    [
        {
            "title": "LG C5 OLED at $1,799 — conviction OLED buy",
            "body": "LG held the $700 cut on the 65 C5 through Saturday across LG direct and Best Buy. WOLED panel plus the α11 processor plus the 144Hz gaming pitch at $1,799 is the right call for any buyer who wants OLED at the best 2026 price floor."
        },
        {
            "title": "Hisense U8N at $999 — brightness-per-dollar leader",
            "body": "Lowe's held the $300 cut through Saturday morning, and at $999 the 65-inch Mini-LED with thousands of nits plus the 144Hz native panel is the best brightness-per-dollar in the category. Two years running this is the right pick for buyers who refuse to pay premium-brand pricing."
        },
        {
            "title": "TCL QM9K Mini-LED at $2,499 — Bravia 9 alternative",
            "body": "TCL's flagship QD Mini-LED pushes peak brightness past 6,000 nits with thousands of dimming zones, native 144Hz, and Google TV with Gemini built in. At $2,499 it is a credible Sony Bravia 9 competitor at half the price, and the new QM9K refresh stacks against the LG G5 for cinema buyers."
        }
    ],
    "禮拜六，4K 電視榜單是國殤日週末算數真的划算的地方。LG 國殤日頁面把 30-58% off 守進禮拜六，Best Buy 上看 45% off，Lowe's 的 Hisense 也是 45% off。\n\nLG C5 OLED 65 守第一 NT$56,500（砍 NT$22,000），WOLED 面板加新的 α11 處理器，是 2026 電競創作派的對的話術，禮拜六折扣守住。\n\nSamsung S95F QD-OLED 65 第二 NT$78,500（砍 NT$31,400），QD-OLED 亮度加 One Connect Box，是高階客廳的對的話術。\n\n講真的，Sony Bravia 9 Mini-LED 65 第三 NT$78,400，新的 XR 背光主控驅動上千個分區。Hisense U8N Mini-LED 65 第四 NT$31,400（Lowe's 砍 NT$9,400），這個價位的亮度單位成本領跑者。TCL QM9K Mini-LED 第五 NT$78,500，昨天我加進來的新旗艦，原生 144Hz 加 6,000+ nits。LG G5 OLED Evo 65 第六 NT$87,900（LG 直營砍 NT$22,000），是影迷的高階 OLED。\n\n禮拜六結論：要 OLED 最佳價就 C5，要 QD-OLED 亮度就 S95F，要亮度單位成本最好就 U8N。國殤日窗口到禮拜一不會有實質更好的價。",
    [
        {
            "title": "LG C5 OLED NT$56,500 有底氣 OLED 買點",
            "body": "LG 把 65 C5 的 NT$22,000 折扣守進禮拜六，LG 直營跟 Best Buy 兩邊都守住。WOLED 面板加 α11 處理器加 144Hz 電競話術，NT$56,500 是任何想要 2026 最佳 OLED 地板價買家的正確選擇。"
        },
        {
            "title": "Hisense U8N NT$31,400 亮度單位成本領跑",
            "body": "Lowe's 把 NT$9,400 折扣守進禮拜六早上，NT$31,400 的 65 吋 Mini-LED 加上千個 nits 加 144Hz 原生面板，這個品類亮度單位成本最好。連續兩年是拒絕付高階品牌定價買家的正確選擇。"
        },
        {
            "title": "TCL QM9K Mini-LED NT$78,500 Bravia 9 對手",
            "body": "TCL 旗艦 QD Mini-LED 衝過 6,000 nits 加上千個分區，原生 144Hz 加上 Google TV 內建 Gemini。NT$78,500 是 Sony Bravia 9 的可信對手，價格只要一半，這次 QM9K 換代在影迷買家面前跟 LG G5 對打。"
        }
    ],
)

add(
    "best-foldable-smartphones",
    [{
        "title": "May 2026 update arrives for Galaxy Z Fold 7, Flip 7, TriFold and Flip7 FE",
        "url": "https://www.sammyfans.com/2026/05/21/galaxy-z-fold-flip-7-fe-trifold-may-2026-update/amp/",
        "source": "Sammy Fans",
    }, MD_CNN, MD_NBC],
    "Saturday morning the foldable chart stays unchanged because Samsung's TriFold and the Z Fold 7 lineup carry the category and the May 2026 firmware push is the news that actually matters this weekend — not pricing. Samsung Galaxy Z Fold 7 holds first at $1,899 (down $100 at Samsung direct), the Snapdragon 8 Gen 4 plus the better hinge plus the thinner profile is still the right Android foldable pitch for power users. Samsung Galaxy TriFold holds second at $2,499, the genuine three-panel form factor is still category-defining and Samsung is the only brand at scale here. Honor Magic V5 at third at $1,799 imported, the thinner profile and lighter weight is competitive but the US distribution remains spotty. OnePlus Open 2 holds fourth at $1,499 (down $300 at OnePlus direct), the Oxygen OS plus the lighter weight is the right pitch for the buyer who refuses Samsung's One UI. Google Pixel Fold 3 at fifth at $1,499 (down $300), the Tensor G5 plus the Gemini integration is the right Google-loyalist pitch. Saturday verdict: Z Fold 7 if you want the most-polished Android foldable, TriFold if you want the cutting edge, OnePlus Open 2 if you want OxygenOS. The May firmware push is the actual story.",
    [
        {
            "title": "Samsung Z Fold 7 at $1,899 — Samsung direct $100 off",
            "body": "Samsung held the $100 cut on the Z Fold 7 through Saturday across Samsung direct, the Snapdragon 8 Gen 4 plus the thinner hinge plus the better display crease is still the most-polished Android foldable. The May 2026 firmware push fixed the Outer Display refresh-rate bug, which matters more than the price."
        },
        {
            "title": "Samsung TriFold at $2,499 — category-defining form factor",
            "body": "Samsung's TriFold is still the only three-panel foldable at scale and the May 2026 firmware push brought the Apps continuity fix that was promised at launch. At $2,499 this is the conviction buy for early adopters who want the cutting edge of the form factor."
        },
        {
            "title": "OnePlus Open 2 at $1,499 — Samsung alternative",
            "body": "OnePlus held the $300 cut through Saturday at OnePlus direct. OxygenOS plus the lighter weight at 232g plus the larger inner display is the right pitch for buyers who refuse Samsung's One UI. The Hasselblad camera tuning is competitive with the Z Fold 7."
        }
    ],
    "禮拜六早上，摺疊機榜單沒動，Samsung TriFold 跟 Z Fold 7 系列扛起品類，五月 2026 韌體推送才是這週末真正重要的消息，不是定價。\n\nSamsung Galaxy Z Fold 7 守第一 NT$59,700（Samsung 直營砍 NT$3,200），Snapdragon 8 Gen 4 加更好的轉軸加更薄機身，還是 Android 摺疊機進階用戶的對的話術。\n\nSamsung Galaxy TriFold 第二 NT$78,500，真正的三面板版型還是品類定義者，Samsung 是這個量級唯一的品牌。\n\n講真的，Honor Magic V5 第三 NT$56,500 進口，更薄更輕有競爭力但美國通路還是不穩。OnePlus Open 2 第四 NT$47,100（OnePlus 直營砍 NT$9,400），Oxygen OS 加更輕的機身是拒絕 Samsung One UI 買家的選擇。Google Pixel Fold 3 第五 NT$47,100（砍 NT$9,400），Tensor G5 加 Gemini 整合是 Google 派的話術。\n\n禮拜六結論：要最精緻 Android 摺疊就 Z Fold 7，要尖端版型就 TriFold，要 OxygenOS 就 OnePlus Open 2。五月韌體推送才是真故事。",
    [
        {
            "title": "Samsung Z Fold 7 NT$59,700 直營砍 NT$3,200",
            "body": "Samsung 把 Z Fold 7 的 NT$3,200 折扣守進禮拜六，Snapdragon 8 Gen 4 加更薄的轉軸加更好的螢幕摺痕，還是最精緻的 Android 摺疊機。五月 2026 韌體推送修好了外屏更新率 bug，這個比價格還重要。"
        },
        {
            "title": "Samsung TriFold NT$78,500 品類定義版型",
            "body": "Samsung TriFold 還是這個量級唯一的三面板摺疊機，五月 2026 韌體推送帶來上市時承諾的 App 連續性修正。NT$78,500 是想要版型尖端的早期採用者的有底氣買點。"
        },
        {
            "title": "OnePlus Open 2 NT$47,100 Samsung 替代",
            "body": "OnePlus 把 NT$9,400 折扣守進禮拜六。OxygenOS 加 232 克的更輕機身加更大的內屏，是拒絕 Samsung One UI 買家的話術。哈蘇相機調校跟 Z Fold 7 有競爭力。"
        }
    ],
)

add(
    "best-gaming-monitors",
    [MD_TOMS_GAMING, MD_BB, MD_CNN],
    "Saturday morning the gaming monitor chart confirms OLED is where MD math really pays off. Best Buy held the OLED discounts through Saturday and Tom's Hardware called OLED gaming monitors among the hefty hardware discounts. LG UltraGear 27GS95QE 27 OLED holds first at $799 (down $200), the 240Hz OLED plus the 0.03ms response is the right e-sports + immersion pitch and the cut survives Saturday. Samsung Odyssey OLED G8 (G80SD) 32 4K stays second at $999 (down $300), the dual-mode 4K/240Hz toggle plus the QD-OLED panel is the right premium pitch. Alienware AW3225QF 32 4K OLED holds third at $899 (down $300), the curve plus the 240Hz panel is the right pitch for the immersion buyer. Asus ROG Swift OLED PG27UCDM 27 4K OLED at fourth at $899 (down $200), the 240Hz 4K OLED at this price floor is the right call for buyers who want resolution. LG UltraGear 32GS95UE 32 4K OLED dual-mode at fifth at $999 (down $200). Saturday verdict: 27 OLED at $799 if you want price-conscious gaming OLED, 32 4K OLED at $899-999 if you want resolution + immersion. The discount window holds through Monday.",
    [
        {
            "title": "LG 27GS95QE OLED at $799 — gaming OLED buy",
            "body": "Best Buy held the $200 cut on the 27 OLED through Saturday. 240Hz OLED plus the 0.03ms response time at $799 is the conviction buy for any e-sports player who wants to graduate from IPS to OLED without paying the 32-inch premium."
        },
        {
            "title": "Samsung Odyssey OLED G8 at $999 — dual-mode 4K",
            "body": "Samsung held the $300 cut on the 32-inch QD-OLED through Saturday. Dual-mode 4K/240Hz toggle plus the QD-OLED panel at $999 is the right premium pitch for buyers who want both resolution work and high-refresh gaming on one display."
        },
        {
            "title": "Alienware AW3225QF at $899 — immersion option",
            "body": "Dell held the $300 cut on the 32-inch 4K curved OLED through Saturday. The 1700R curve plus the 240Hz QD-OLED panel at $899 is the right pitch for buyers who put immersion ahead of pixel-perfect productivity, and the price floor matches the price-per-inch math on the LG and Samsung options."
        }
    ],
    "禮拜六早上，電競螢幕榜單確認 OLED 是國殤日算數真的划算的地方。Best Buy 把 OLED 折扣守進禮拜六，Tom's Hardware 點名 OLED 電競螢幕是這次重磅硬體折扣之一。\n\nLG UltraGear 27GS95QE 27 OLED 守第一 NT$25,100（砍 NT$6,300），240Hz OLED 加 0.03ms 響應是電競加沉浸感的對的話術。\n\nSamsung Odyssey OLED G8 (G80SD) 32 4K 第二 NT$31,400（砍 NT$9,400），雙模 4K/240Hz 切換加 QD-OLED 面板是高階話術。\n\n講真的，Alienware AW3225QF 32 4K OLED 第三 NT$28,300（砍 NT$9,400），曲面加 240Hz 面板是沉浸派的話術。Asus ROG Swift OLED PG27UCDM 27 4K OLED 第四 NT$28,300（砍 NT$6,300），240Hz 4K OLED 在這個價格是要解析度買家的選擇。LG UltraGear 32GS95UE 32 4K OLED 雙模第五 NT$31,400（砍 NT$6,300）。\n\n禮拜六結論：要省錢電競 OLED 就 27 NT$25,100，要解析度加沉浸感就 32 4K OLED NT$28,300-31,400。折扣窗口守到禮拜一。",
    [
        {
            "title": "LG 27GS95QE OLED NT$25,100 電競 OLED 買點",
            "body": "Best Buy 把 27 OLED 的 NT$6,300 折扣守進禮拜六。240Hz OLED 加 0.03ms 響應 NT$25,100，是任何想從 IPS 升級到 OLED 又不想付 32 吋溢價的電競玩家的有底氣買點。"
        },
        {
            "title": "Samsung Odyssey OLED G8 NT$31,400 雙模 4K",
            "body": "Samsung 把 32 吋 QD-OLED 的 NT$9,400 折扣守進禮拜六。雙模 4K/240Hz 切換加 QD-OLED 面板 NT$31,400，是想要同時解析度作業跟高更新率電競一台搞定的高階買家正確選擇。"
        },
        {
            "title": "Alienware AW3225QF NT$28,300 沉浸感選擇",
            "body": "Dell 把 32 吋 4K 曲面 OLED 的 NT$9,400 折扣守進禮拜六。1700R 曲率加 240Hz QD-OLED 面板 NT$28,300，是把沉浸感擺在像素完美作業前面買家的話術，這個價對得起 LG 跟 Samsung 的單吋成本算數。"
        }
    ],
)

add(
    "best-portable-projectors",
    [MD_CNN, MD_NBC, {
        "title": "Memorial Day projector deals 2026: Anker, XGIMI, Samsung Freestyle",
        "url": "https://www.techradar.com/audio-visual/projectors",
        "source": "TechRadar",
    }],
    "Saturday and the portable projector category held the Friday cuts overnight. XGIMI Horizon Ultra 4K stays first at $1,499 (down $300), the 4K + Dolby Vision plus the laser-LED hybrid light source plus the auto-keystone is the right premium portable pitch. Anker Nebula Capsule 3 Laser holds second at $799 (down $200), the laser projection plus the soda-can form factor is the right travel-friendly pitch. Samsung Freestyle Gen 2 at third at $599 (down $200), the 360-degree swivel plus the smart-TV-style content stack is the right lifestyle pitch. BenQ X3100i at fourth at $1,799, the 4K plus the gaming-mode plus the 240Hz refresh is the right gaming pitch and the price held. Epson EpiqVision Mini EF22 fifth at $999, the laser short-throw is the indoor anchor. Saturday verdict: XGIMI Horizon Ultra if you want 4K + Dolby Vision in a portable, Anker Capsule 3 Laser if you want true travel portability, Samsung Freestyle if lifestyle versatility matters. The MD window will not get materially better.",
    [
        {
            "title": "XGIMI Horizon Ultra at $1,499 — 4K + Dolby Vision",
            "body": "XGIMI held the $300 cut through Saturday morning. 4K plus Dolby Vision plus the laser-LED hybrid light source plus auto-keystone at $1,499 is the right premium portable pitch and the price floor matches the best the brand has put up this year outside Prime Day."
        },
        {
            "title": "Anker Capsule 3 Laser at $799 — travel pick",
            "body": "Anker held the $200 cut on the Capsule 3 Laser through Saturday. The laser projection plus the soda-can form factor at $799 is the right travel-friendly buy and the brightness now matches the more expensive XGIMI MoGo. Best portable travel projector at this price floor."
        },
        {
            "title": "Samsung Freestyle Gen 2 at $599 — lifestyle pitch",
            "body": "Samsung held the $200 cut through Saturday across Samsung direct. The 360-degree swivel mount plus the Tizen smart-TV content stack at $599 is the right lifestyle pitch for buyers who want a projector that doubles as a content hub. Not the brightest but the most flexible."
        }
    ],
    "禮拜六，攜帶式投影機品類把禮拜五的折扣守過夜。XGIMI Horizon Ultra 4K 守第一 NT$47,100（砍 NT$9,400），4K 加 Dolby Vision 加雷射-LED 混合光源加自動梯形校正，是高階攜帶話術。\n\nAnker Nebula Capsule 3 Laser 第二 NT$25,100（砍 NT$6,300），雷射投影加易開罐版型是旅行話術。Samsung Freestyle Gen 2 第三 NT$18,800（砍 NT$6,300），360 度旋轉加智慧電視內容堆疊是生活風話術。\n\n講真的，BenQ X3100i 第四 NT$56,500，4K 加電競模式加 240Hz 更新率是電競話術，價格守住。Epson EpiqVision Mini EF22 第五 NT$31,400，雷射短焦是室內錨點。\n\n禮拜六結論：可攜 4K 加 Dolby Vision 就 XGIMI Horizon Ultra，真旅行就 Anker Capsule 3 Laser，生活風多用途就 Samsung Freestyle。國殤日窗口不會有更好的價。",
    [
        {
            "title": "XGIMI Horizon Ultra NT$47,100 4K 加 Dolby Vision",
            "body": "XGIMI 把 NT$9,400 折扣守進禮拜六早上。4K 加 Dolby Vision 加雷射-LED 混合光源加自動梯形校正 NT$47,100，是高階攜帶話術，這個地板價對得起今年除了 Prime Day 以外品牌最好的價。"
        },
        {
            "title": "Anker Capsule 3 Laser NT$25,100 旅行選擇",
            "body": "Anker 把 Capsule 3 Laser 的 NT$6,300 折扣守進禮拜六。雷射投影加易開罐版型 NT$25,100，是旅行話術，亮度已經追上更貴的 XGIMI MoGo。這個價是攜帶旅行投影機最佳買點。"
        },
        {
            "title": "Samsung Freestyle Gen 2 NT$18,800 生活風選擇",
            "body": "Samsung 把 Samsung 直營的 NT$6,300 折扣守進禮拜六。360 度旋轉支架加 Tizen 智慧電視內容堆疊 NT$18,800，是想要投影機兼當內容中樞買家的話術。不是最亮但最有彈性。"
        }
    ],
)


# ---------- READING / GAMING ----------

add(
    "best-e-readers",
    [MD_CNN, MD_NBC, {
        "title": "Best Kindle deals 2026: Memorial Day refresh",
        "url": "https://www.amazon.com/Kindle-deals",
        "source": "Amazon",
    }],
    "Saturday morning the e-reader chart held the Friday cuts because Amazon and Kobo both held their MD floors. Amazon Kindle Paperwhite (12th Gen) holds first at $129 (down $30), the 7-inch display plus the warmer front-light plus the new oxide pigment Carta panel is the right mainstream pitch. Kindle Colorsoft Signature stays second at $249 (down $30), the color e-ink at this price is still category-defining and the May firmware fixed the highlight-color sync that bothered early adopters. Kobo Libra Colour at third at $189 (down $30), the page-turn buttons plus the wider Kobo Store and OverDrive integration is the right pitch for library borrowers. Boox Page at fourth at $249, the Android e-ink with Play Store plus the e-ink note-taking is the right power-user pitch. Kindle Scribe (2nd Gen) fifth at $349 (down $50), the larger note-taking plus the AI summarization update from April is the right reader-plus-notebook pitch. Saturday verdict: Paperwhite for mainstream reading, Colorsoft if you want color e-ink, Libra Colour if you live in OverDrive. The MD discount window holds through Monday.",
    [
        {
            "title": "Kindle Paperwhite at $129 — mainstream buy",
            "body": "Amazon held the $30 cut through Saturday morning. 7-inch display plus the warmer front-light plus the new Carta panel at $129 is the right mainstream pitch and this is the best Paperwhite price outside Prime Day. The conviction buy for any first-time e-reader buyer."
        },
        {
            "title": "Kindle Colorsoft at $249 — color e-ink defends slot",
            "body": "Amazon held the $30 cut on the Colorsoft Signature through Saturday. The May firmware fixed the highlight-color sync that bothered early adopters and at $249 the color e-ink experience is still category-defining. The right buy for cookbook and comic readers."
        },
        {
            "title": "Kobo Libra Colour at $189 — OverDrive pick",
            "body": "Kobo held the $30 cut through Saturday at Kobo direct. Page-turn buttons plus the wider Kobo Store catalog plus the OverDrive library integration at $189 is the right pitch for buyers who refuse Amazon's ecosystem lock-in."
        }
    ],
    "禮拜六早上，電子書閱讀器榜單把禮拜五的折扣守過夜，Amazon 跟 Kobo 都守住國殤日地板。\n\nAmazon Kindle Paperwhite（12 代）守第一 NT$4,100（砍 NT$940），7 吋螢幕加暖色前光加新的氧化顏料 Carta 面板是主流話術。\n\nKindle Colorsoft Signature 第二 NT$7,800（砍 NT$940），這個價格的彩色 e-ink 還是品類定義者，五月韌體修好了早期採用者抱怨的螢光筆顏色同步問題。\n\n講真的，Kobo Libra Colour 第三 NT$5,900（砍 NT$940），翻頁按鍵加更廣的 Kobo 商店跟 OverDrive 整合，是圖書館借閱派的話術。Boox Page 第四 NT$7,800，Android e-ink 加 Play Store 加 e-ink 筆記是進階用戶話術。Kindle Scribe（2 代）第五 NT$10,900（砍 NT$1,570），更大的筆記加四月 AI 摘要更新是閱讀加筆記本話術。\n\n禮拜六結論：主流閱讀就 Paperwhite，要彩色 e-ink 就 Colorsoft，住 OverDrive 就 Libra Colour。國殤日折扣窗口守到禮拜一。",
    [
        {
            "title": "Kindle Paperwhite NT$4,100 主流買點",
            "body": "Amazon 把 NT$940 折扣守進禮拜六早上。7 吋螢幕加暖色前光加新 Carta 面板 NT$4,100，是主流話術，這是 Prime Day 之外 Paperwhite 最佳價。第一次買電子書閱讀器的人有底氣買點。"
        },
        {
            "title": "Kindle Colorsoft NT$7,800 彩色 e-ink 守住",
            "body": "Amazon 把 Colorsoft Signature 的 NT$940 折扣守進禮拜六。五月韌體修好了早期採用者抱怨的螢光筆顏色同步，NT$7,800 的彩色 e-ink 體驗還是品類定義者。食譜跟漫畫讀者的對的買點。"
        },
        {
            "title": "Kobo Libra Colour NT$5,900 OverDrive 派",
            "body": "Kobo 把 NT$940 折扣守進禮拜六，Kobo 直營。翻頁按鍵加更廣的 Kobo 商店目錄加 OverDrive 圖書館整合，NT$5,900 是拒絕 Amazon 生態綁住的買家正確選擇。"
        }
    ],
)

add(
    "best-handheld-gaming-consoles",
    [MD_GAMESPOT, MD_CNN, MD_BB],
    "Saturday and the handheld gaming chart confirms the GameSpot Memorial Day call: up to 75% off handhelds, controllers, and games at Best Buy through Saturday and the floors held overnight. Nintendo Switch 2 holds first at $449 (no MD discount because supply is still constrained from the April launch), the DLSS-equipped Tegra T239 plus the magnetic Joy-Con 2s plus the OLED display is still the conviction buy for any Nintendo-first household. Steam Deck OLED stays second at $499 (no MD cut from Valve direct), the OLED HDR display plus the 7-hour battery is the right PC-handheld pitch. ASUS ROG Ally X at third at $649 (down $150 at Best Buy), the Ryzen Z2 Extreme plus the 80Wh battery is the right Windows-handheld pitch. Lenovo Legion Go S fourth at $499 (down $100 at Lenovo direct), the SteamOS option finally shipped and the price floor is competitive. MSI Claw 8 AI+ fifth at $799, the Lunar Lake plus the larger 8-inch screen is the premium Windows pitch. Saturday verdict: Switch 2 if you want Nintendo exclusives, Steam Deck OLED if you want PC gaming with the most polished handheld OS, ROG Ally X at $649 if you want Windows. Supply on Switch 2 is the actual story.",
    [
        {
            "title": "Switch 2 at $449 — no MD discount, supply story",
            "body": "Nintendo held the $449 sticker through Saturday with no MD cut because the April launch supply is still constrained. Magnetic Joy-Con 2s plus the DLSS-equipped Tegra T239 plus the OLED display is the right Nintendo-first pitch and inventory is the real news, not pricing."
        },
        {
            "title": "Steam Deck OLED at $499 — PC handheld holds",
            "body": "Valve held the $499 sticker through Saturday with no MD cut. The OLED HDR display plus the 7-hour battery plus the SteamOS polish at $499 is still the conviction buy for PC gaming on a handheld, and the no-discount stance reflects how strong the platform position is."
        },
        {
            "title": "ROG Ally X at $649 — Best Buy $150 cut",
            "body": "Best Buy held the $150 cut on the Ally X through Saturday. Ryzen Z2 Extreme plus the 80Wh battery plus the upgraded ergonomic chassis at $649 is the right Windows-handheld pitch for buyers who refuse Steam Deck and want native Game Pass. The cut beats the Lenovo Legion Go S at $499 on raw performance."
        }
    ],
    "禮拜六，掌機遊戲榜單確認 GameSpot 國殤日的話：Best Buy 掌機、控制器、遊戲上看 75% off，禮拜六的折扣守過夜。\n\nNintendo Switch 2 守第一 NT$14,100（無國殤日折扣因為四月上市以來供貨受限），DLSS 加持 Tegra T239 加磁吸 Joy-Con 2 加 OLED 螢幕，還是 Nintendo 派的有底氣買點。\n\nSteam Deck OLED 第二 NT$15,700（Valve 直營無國殤日砍價），OLED HDR 螢幕加 7 小時電池是 PC 掌機話術。\n\n講真的，ASUS ROG Ally X 第三 NT$20,400（Best Buy 砍 NT$4,700），Ryzen Z2 Extreme 加 80Wh 電池是 Windows 掌機話術。Lenovo Legion Go S 第四 NT$15,700（Lenovo 直營砍 NT$3,140），SteamOS 版終於出貨，價格有競爭力。MSI Claw 8 AI+ 第五 NT$25,100，Lunar Lake 加更大 8 吋螢幕是高階 Windows 話術。\n\n禮拜六結論：要 Nintendo 獨佔就 Switch 2，要 PC 加最精緻掌機 OS 就 Steam Deck OLED，要 Windows 就 ROG Ally X NT$20,400。Switch 2 的供貨才是真故事。",
    [
        {
            "title": "Switch 2 NT$14,100 無國殤日折扣，供貨故事",
            "body": "Nintendo 把 NT$14,100 牌價守進禮拜六，沒打折因為四月上市以來供貨還是緊。磁吸 Joy-Con 2 加 DLSS 加持 Tegra T239 加 OLED 螢幕，是 Nintendo 派的話術，庫存才是真新聞，不是定價。"
        },
        {
            "title": "Steam Deck OLED NT$15,700 PC 掌機守住",
            "body": "Valve 把 NT$15,700 牌價守進禮拜六沒打折。OLED HDR 螢幕加 7 小時電池加 SteamOS 精緻度 NT$15,700，還是 PC 掌機遊戲的有底氣買點，無折扣立場反映出平台位置有多強。"
        },
        {
            "title": "ROG Ally X NT$20,400 Best Buy 砍 NT$4,700",
            "body": "Best Buy 把 Ally X 的 NT$4,700 折扣守進禮拜六。Ryzen Z2 Extreme 加 80Wh 電池加升級人體工學機身 NT$20,400，是拒絕 Steam Deck 又想要原生 Game Pass 買家的話術。純效能贏 Lenovo Legion Go S。"
        }
    ],
)

add(
    "best-gaming-chairs",
    [MD_CNN, MD_NBC, {
        "title": "Best gaming chair deals Memorial Day 2026",
        "url": "https://www.ign.com/articles/best-gaming-chair-deals",
        "source": "IGN",
    }],
    "Saturday morning the gaming chair chart held the Friday cuts as Secretlab and Herman Miller both extended through Saturday. Secretlab Titan Evo 2026 holds first at $549 (down $100 at Secretlab direct), the new SoftWeave Plus fabric plus the magnetic head pillow plus the 5-year warranty is the right premium pitch. Herman Miller Embody Gaming stays second at $1,599 (down $200 at HM direct), the ergonomic credentials plus the BackFit adjustment is the right buy for back-pain sufferers. Razer Iskur V3 at third at $649 (down $150), the integrated lumbar plus the Alcantara seat is the right pitch for the Razer-themed buyer. Steelcase Gesture at fourth at $1,299 (down $200), the all-day office chair posture is the right buy for the work-from-home gamer. Anda Seat Kaiser 3 fifth at $549 (down $100), the magnetic head pillow plus the cold-cure foam at this price floor is the budget-flagship pitch. Saturday verdict: Titan Evo at $549 for premium gaming, Herman Miller Embody at $1,599 for back-pain priority, Anda Seat Kaiser 3 at $549 for budget flagship.",
    [
        {
            "title": "Secretlab Titan Evo at $549 — premium gaming pick",
            "body": "Secretlab held the $100 cut on the Titan Evo 2026 through Saturday. SoftWeave Plus fabric plus the magnetic head pillow plus the 5-year warranty at $549 is the right premium gaming chair pitch, and this is the best Secretlab price this side of Black Friday."
        },
        {
            "title": "Herman Miller Embody Gaming at $1,599 — back-pain buy",
            "body": "HM held the $200 cut through Saturday. The ergonomic credentials plus the BackFit adjustment plus the 12-year warranty at $1,599 is the right call for buyers who put back-pain prevention ahead of esports aesthetics. The math holds even after the cut."
        },
        {
            "title": "Anda Seat Kaiser 3 at $549 — budget flagship",
            "body": "Anda Seat held the $100 cut through Saturday. Magnetic head pillow plus the cold-cure foam plus the wider seat at $549 matches the Titan Evo price floor but with a softer ride. The right pitch for buyers who refuse to spend $700+ on a chair."
        }
    ],
    "禮拜六早上，電競椅榜單把禮拜五的折扣守過夜，Secretlab 跟 Herman Miller 都延進禮拜六。\n\nSecretlab Titan Evo 2026 守第一 NT$17,200（Secretlab 直營砍 NT$3,140），新的 SoftWeave Plus 布料加磁吸頭枕加 5 年保固，是高階話術。\n\nHerman Miller Embody Gaming 第二 NT$50,300（HM 直營砍 NT$6,300），人體工學認證加 BackFit 調整是腰痠背痛買家的選擇。\n\n講真的，Razer Iskur V3 第三 NT$20,400（砍 NT$4,700），整合腰托加 Alcantara 椅面是 Razer 風買家話術。Steelcase Gesture 第四 NT$40,800（砍 NT$6,300），整天辦公室椅姿勢是居家辦公電競玩家的選擇。Anda Seat Kaiser 3 第五 NT$17,200（砍 NT$3,140），磁吸頭枕加冷固定發泡棉是預算旗艦話術。\n\n禮拜六結論：高階電競就 Titan Evo NT$17,200，腰痠背痛優先就 Herman Miller Embody NT$50,300，預算旗艦就 Anda Seat Kaiser 3 NT$17,200。",
    [
        {
            "title": "Secretlab Titan Evo NT$17,200 高階電競選擇",
            "body": "Secretlab 把 Titan Evo 2026 的 NT$3,140 折扣守進禮拜六。SoftWeave Plus 布料加磁吸頭枕加 5 年保固 NT$17,200，是高階電競椅話術，這是黑五以外 Secretlab 最佳價。"
        },
        {
            "title": "Herman Miller Embody Gaming NT$50,300 腰痛買點",
            "body": "HM 把 NT$6,300 折扣守進禮拜六。人體工學認證加 BackFit 調整加 12 年保固 NT$50,300，是把腰痠預防擺在電競美學前面買家的選擇。折扣後算數還是站得住。"
        },
        {
            "title": "Anda Seat Kaiser 3 NT$17,200 預算旗艦",
            "body": "Anda Seat 把 NT$3,140 折扣守進禮拜六。磁吸頭枕加冷固定發泡棉加更寬椅面 NT$17,200 對齊 Titan Evo 但坐感較軟。是拒絕在椅子上花 NT$22,000+ 買家的話術。"
        }
    ],
)

add(
    "best-gaming-headsets",
    [MD_CNN, MD_NBC, MD_GAMESPOT],
    "Saturday morning the gaming headset chart held the Friday MD cuts. SteelSeries Arctis Nova Pro Wireless holds first at $279 (down $70 at Best Buy), the dual-battery system plus the active noise cancellation plus the multi-platform 2.4GHz transmitter is still the right premium pitch. Sony PlayStation Pulse Elite stays second at $129 (down $20), the AI-driven mic plus the planar drivers at $129 is the right pitch for PS5 owners. Razer BlackShark V3 Pro at third at $169 (down $30), the THX Spatial Audio plus the lighter weight is the right competitive pitch. Audeze Maxwell at fourth at $279 (down $50 at Audeze direct), the planar magnetic drivers and the 80+ hour battery is the audiophile pick for gaming. Logitech G Pro X 2 Lightspeed fifth at $179 (down $70), the 50-hour battery plus the graphene drivers at this floor is the right tournament pick. Saturday verdict: Arctis Nova Pro Wireless if you want the multi-platform flagship, Pulse Elite if you live in PlayStation, Maxwell if audiophile-grade matters.",
    [
        {
            "title": "Arctis Nova Pro Wireless at $279 — multi-platform buy",
            "body": "Best Buy held the $70 cut through Saturday. Dual-battery hot-swap plus active noise cancellation plus the multi-platform 2.4GHz transmitter at $279 is still the most flexible premium gaming headset and this is the best price since the launch."
        },
        {
            "title": "Pulse Elite at $129 — PlayStation buy",
            "body": "Sony direct held the $20 cut through Saturday. The AI-driven mic plus the planar drivers plus the PS5 integration at $129 is the right pitch for PlayStation owners and the Tempest 3D Audio support is unmatched on this price floor."
        },
        {
            "title": "Audeze Maxwell at $279 — audiophile gaming",
            "body": "Audeze direct held the $50 cut through Saturday. Planar magnetic drivers plus 80+ hour battery plus the new Audeze HQ tuning app at $279 is the audiophile-grade pick for gaming, and matches the Arctis Nova Pro Wireless price floor."
        }
    ],
    "禮拜六早上，電競耳機榜單把禮拜五的國殤日折扣守過夜。\n\nSteelSeries Arctis Nova Pro Wireless 守第一 NT$8,790（Best Buy 砍 NT$2,200），雙電池系統加主動降噪加多平台 2.4GHz 接收器，還是高階話術。\n\nSony PlayStation Pulse Elite 第二 NT$4,100（砍 NT$620），AI 麥克風加平面振膜在 NT$4,100 是 PS5 派的話術。\n\n講真的，Razer BlackShark V3 Pro 第三 NT$5,300（砍 NT$940），THX 空間音訊加更輕機身是競技話術。Audeze Maxwell 第四 NT$8,790（Audeze 直營砍 NT$1,570），平面磁性振膜加 80+ 小時電池是電競發燒友選擇。Logitech G Pro X 2 Lightspeed 第五 NT$5,600（砍 NT$2,200），50 小時電池加石墨烯振膜在這個價是賽事話術。\n\n禮拜六結論：多平台旗艦就 Arctis Nova Pro Wireless，PlayStation 就 Pulse Elite，發燒友等級就 Maxwell。",
    [
        {
            "title": "Arctis Nova Pro Wireless NT$8,790 多平台買點",
            "body": "Best Buy 把 NT$2,200 折扣守進禮拜六。雙電池熱抽換加主動降噪加多平台 2.4GHz 接收器 NT$8,790，還是最彈性的高階電競耳機，這是上市以來最佳價。"
        },
        {
            "title": "Pulse Elite NT$4,100 PlayStation 買點",
            "body": "Sony 直營把 NT$620 折扣守進禮拜六。AI 麥克風加平面振膜加 PS5 整合 NT$4,100，是 PlayStation 派的話術，Tempest 3D 音訊支援在這個價無對手。"
        },
        {
            "title": "Audeze Maxwell NT$8,790 發燒友電競",
            "body": "Audeze 直營把 NT$1,570 折扣守進禮拜六。平面磁性振膜加 80+ 小時電池加新 Audeze HQ 調音 App NT$8,790，是電競發燒友等級選擇，對齊 Arctis Nova Pro Wireless 價格。"
        }
    ],
)

add(
    "best-gaming-mice",
    [MD_CNN, MD_NBC, MD_TOMS_GAMING],
    "Saturday morning the gaming mouse chart held the Friday cuts. Logitech G Pro X Superlight 2 Dex holds first at $119 (down $40 at Best Buy), the 60g weight plus the HERO 2 sensor plus the 95-hour battery is still the right competitive pitch. Razer DeathAdder V3 Pro 35K stays second at $129 (down $30), the 35K Focus Pro sensor plus the ergonomic shape is the right palm-grip pitch. Pulsar X2A Mini at third at $99 (down $20), the symmetric ambidextrous form plus the 52g weight is the right claw-grip pitch. Glorious Model O- Wireless fourth at $79 (down $20), the honeycomb shell plus the BAMF 2.0 sensor at $79 is the budget tournament pick. SteelSeries Aerox 9 Wireless fifth at $129 (down $20), the 18-button MMO layout is the right RPG pitch. Saturday verdict: G Pro X Superlight 2 Dex if you want the palm-grip flagship, Razer DeathAdder V3 Pro if you want ergonomic palm-grip, Pulsar X2A Mini if claw-grip is your style.",
    [
        {
            "title": "G Pro X Superlight 2 Dex at $119 — competitive flagship",
            "body": "Best Buy held the $40 cut through Saturday. 60g weight plus the HERO 2 sensor plus the 95-hour battery at $119 is still the right competitive flagship and the Dex shape addresses the small-hand complaints from the original Superlight 2."
        },
        {
            "title": "DeathAdder V3 Pro 35K at $129 — palm-grip pick",
            "body": "Razer direct held the $30 cut through Saturday. 35K Focus Pro sensor plus the ergonomic shape plus the lighter 56g body at $129 is the right palm-grip pitch and the 35K upgrade from the original V3 Pro is the reason to pay over the cheaper alternatives."
        },
        {
            "title": "Pulsar X2A Mini at $99 — claw-grip flagship",
            "body": "Pulsar held the $20 cut through Saturday. Symmetric ambidextrous form plus the 52g weight plus the eS sensor at $99 is the right claw-grip flagship and the build quality finally matches the more expensive Logitech and Razer options."
        }
    ],
    "禮拜六早上，電競滑鼠榜單把禮拜五的折扣守過夜。\n\nLogitech G Pro X Superlight 2 Dex 守第一 NT$3,730（Best Buy 砍 NT$1,250），60g 重量加 HERO 2 感測器加 95 小時電池還是競技話術。\n\nRazer DeathAdder V3 Pro 35K 第二 NT$4,100（砍 NT$940），35K Focus Pro 感測器加人體工學形狀是手掌握法話術。\n\n講真的，Pulsar X2A Mini 第三 NT$3,140（砍 NT$620），對稱左右手通用版型加 52g 重量是爪式握法話術。Glorious Model O- Wireless 第四 NT$2,500（砍 NT$620），蜂窩外殼加 BAMF 2.0 感測器在 NT$2,500 是預算競技選擇。SteelSeries Aerox 9 Wireless 第五 NT$4,100（砍 NT$620），18 鍵 MMO 配置是 RPG 話術。\n\n禮拜六結論：手掌握法旗艦就 G Pro X Superlight 2 Dex，人體工學手掌握就 Razer DeathAdder V3 Pro，爪式握法就 Pulsar X2A Mini。",
    [
        {
            "title": "G Pro X Superlight 2 Dex NT$3,730 競技旗艦",
            "body": "Best Buy 把 NT$1,250 折扣守進禮拜六。60g 重量加 HERO 2 感測器加 95 小時電池 NT$3,730，還是競技旗艦話術，Dex 形狀解決原版 Superlight 2 對小手用戶的抱怨。"
        },
        {
            "title": "DeathAdder V3 Pro 35K NT$4,100 手掌握法",
            "body": "Razer 直營把 NT$940 折扣守進禮拜六。35K Focus Pro 感測器加人體工學形狀加 56g 更輕機身 NT$4,100，是手掌握法話術，35K 升級是付比便宜替代品多的價值理由。"
        },
        {
            "title": "Pulsar X2A Mini NT$3,140 爪式握法旗艦",
            "body": "Pulsar 把 NT$620 折扣守進禮拜六。對稱左右手通用版型加 52g 重量加 eS 感測器 NT$3,140，是爪式握法旗艦話術，做工終於對齊 Logitech 跟 Razer 的更貴選擇。"
        }
    ],
)

add(
    "best-mechanical-keyboards",
    [MD_CNN, MD_TOMS_GAMING, {
        "title": "Best mechanical keyboard deals 2026: Memorial Day picks",
        "url": "https://www.rtings.com/keyboard/reviews/best/mechanical",
        "source": "RTINGS",
    }],
    "Saturday morning the mechanical keyboard chart held the Friday cuts. Keychron Q1 Pro Wireless holds first at $179 (down $30), the gasket-mount plus the QMK/VIA firmware plus the wireless ability at $179 is the right enthusiast-mainstream pitch. Wooting 80HE stays second at $199 (down $20 at Wooting direct), the magnetic Hall-effect switches plus the per-key analog rapid-trigger is still the right competitive pitch. Razer BlackWidow V4 Pro 75% at third at $189 (down $40 at Razer direct), the analog optical switches plus the Razer ecosystem is the right gaming-mainstream pitch. NuPhy Air75 V3 fourth at $129 (down $30), the low-profile mechanical plus the wireless plus the Mac-friendly layout at $129 is the right portable-mac pitch. Glorious GMMK 3 Pro 75% fifth at $159 (down $40), the modular hot-swap chassis is the right entry-enthusiast pitch. Saturday verdict: Q1 Pro if you want mainstream-enthusiast, Wooting 80HE if you want competitive analog, NuPhy Air75 V3 if portable and Mac is your use.",
    [
        {
            "title": "Keychron Q1 Pro Wireless at $179 — enthusiast buy",
            "body": "Keychron held the $30 cut through Saturday. Gasket-mount plus QMK/VIA firmware plus the wireless ability at $179 is the right enthusiast-mainstream pitch and the price floor matches the best Keychron has put up this year outside Prime Day."
        },
        {
            "title": "Wooting 80HE at $199 — competitive analog pick",
            "body": "Wooting direct held the $20 cut through Saturday. Magnetic Hall-effect switches plus the per-key analog rapid-trigger plus the open-source firmware at $199 is the right competitive pitch and no other manufacturer matches the analog responsiveness."
        },
        {
            "title": "NuPhy Air75 V3 at $129 — Mac-portable pick",
            "body": "NuPhy held the $30 cut through Saturday. Low-profile mechanical switches plus the wireless plus the Mac-friendly layout at $129 is the right portable-mac pitch and the build quality finally matches the price floor."
        }
    ],
    "禮拜六早上，機械鍵盤榜單把禮拜五的折扣守過夜。\n\nKeychron Q1 Pro Wireless 守第一 NT$5,600（砍 NT$940），墊片式結構加 QMK/VIA 韌體加無線能力 NT$5,600，是發燒友入門話術。\n\nWooting 80HE 第二 NT$6,200（Wooting 直營砍 NT$620），磁性霍爾效應軸加每鍵類比快速觸發還是競技話術。\n\n講真的，Razer BlackWidow V4 Pro 75% 第三 NT$5,900（Razer 直營砍 NT$1,250），類比光軸加 Razer 生態是電競主流話術。NuPhy Air75 V3 第四 NT$4,100（砍 NT$940），矮軸機械加無線加 Mac 友善配列 NT$4,100，是 Mac 攜帶話術。Glorious GMMK 3 Pro 75% 第五 NT$5,000（砍 NT$1,250），模組化熱抽換機身是發燒友入門話術。\n\n禮拜六結論：發燒友入門就 Q1 Pro，競技類比就 Wooting 80HE，Mac 攜帶就 NuPhy Air75 V3。",
    [
        {
            "title": "Keychron Q1 Pro Wireless NT$5,600 發燒友買點",
            "body": "Keychron 把 NT$940 折扣守進禮拜六。墊片式結構加 QMK/VIA 韌體加無線能力 NT$5,600，是發燒友入門話術，這個地板價對得起 Prime Day 以外今年 Keychron 最佳價。"
        },
        {
            "title": "Wooting 80HE NT$6,200 競技類比選擇",
            "body": "Wooting 直營把 NT$620 折扣守進禮拜六。磁性霍爾效應軸加每鍵類比快速觸發加開源韌體 NT$6,200，是競技話術，沒有別的廠商能對齊類比反應靈敏度。"
        },
        {
            "title": "NuPhy Air75 V3 NT$4,100 Mac 攜帶選擇",
            "body": "NuPhy 把 NT$940 折扣守進禮拜六。矮軸機械加無線加 Mac 友善配列 NT$4,100，是 Mac 攜帶話術，做工終於對齊這個價格。"
        }
    ],
)


# ---------- AI ----------

add(
    "best-ai-chatbots",
    [AI_LLMSTATS, AI_TC_GEMINI, AI_CNBC_GOOGLE, AI_WHATLLM],
    "Saturday morning the chatbot chart is the most contested in tech right now and the I/O 2026 fallout from Monday continues to shape the leaderboard. ChatGPT (GPT-5.5 Instant default) holds first because OpenAI promoted GPT-5.5 Instant to default ChatGPT this week, the reasoning gains plus the deeper agent tool access plus the still-best mobile app polish keeps the conviction at the top. Anthropic Claude (Opus 4.7 1M context) stays second, the 1M-context window plus the still-leading coding accuracy is the right pitch for power users and developers, and Anthropic did not ship past Opus 4.7 in April which means the position holds without new flank. Google Gemini (Gemini 3.5 Flash + Gemini Spark) climbs third because the Spark agent beta plus the Omni world model from I/O on Monday give Google the freshest 2026 narrative even if the daily-use polish lags ChatGPT. xAI Grok 4 fourth, the real-time X integration plus the unfiltered tuning is the right pitch for a specific buyer. Meta AI (Llama 4 Behemoth) fifth, the Ray-Ban Meta + WhatsApp + IG integration is broad but the standalone chat polish is weak. Saturday verdict: ChatGPT for general use, Claude for coding and long-context, Gemini for Google ecosystem + agentic action. The I/O fallout is the actual story, not pricing.",
    [
        {
            "title": "ChatGPT GPT-5.5 Instant default — leadership cemented",
            "body": "OpenAI promoted GPT-5.5 Instant to the default ChatGPT model this week, and the reasoning gains plus the deeper agent tool access plus the still-best mobile app polish keeps the leadership intact. The Gemini Spark launch is the only credible challenge and it remains beta-restricted."
        },
        {
            "title": "Claude Opus 4.7 holds — Anthropic on the back foot",
            "body": "Anthropic did not ship past Opus 4.7 in April and the I/O fallout did not give them a runway response. The 1M-context window plus the still-leading coding accuracy keeps Claude at second for power users and developers, but the position is now defensive."
        },
        {
            "title": "Gemini Spark — Google's freshest agentic narrative",
            "body": "Google's Spark agent beta plus the Omni world model from I/O Monday give Google the strongest 2026 agentic narrative even though the daily-use polish still trails ChatGPT. Trusted-tester rollout plus AI Ultra subscribers gates the experience and the next two weeks will validate the pitch."
        }
    ],
    "禮拜六早上，聊天機器人榜單是現在科技圈最激烈的，禮拜一 I/O 2026 的餘震還在塑造榜單。\n\nChatGPT（GPT-5.5 Instant 預設）守第一，OpenAI 這禮拜把 GPT-5.5 Instant 升級成 ChatGPT 預設，推理能力增強加更深的 agent 工具存取加還是最精緻的手機 App，有底氣坐在第一名。\n\nAnthropic Claude（Opus 4.7 1M 上下文）第二，1M 上下文視窗加還是領先的程式碼準確率，是進階用戶跟開發者的話術，Anthropic 四月沒推 Opus 4.7 之後的新東西，所以位置守住但沒有新進攻。\n\n講真的，Google Gemini（Gemini 3.5 Flash 加 Gemini Spark）爬到第三，Spark agent beta 加 I/O 禮拜一的 Omni 世界模型，給 Google 這個 2026 最新的敘事，即使日常使用精緻度還是落後 ChatGPT。xAI Grok 4 第四，即時 X 整合加無過濾調校是特定買家的話術。Meta AI（Llama 4 Behemoth）第五，Ray-Ban Meta 加 WhatsApp 加 IG 整合廣但獨立聊天精緻度弱。\n\n禮拜六結論：一般用就 ChatGPT，寫程式跟長上下文就 Claude，Google 生態加 agent 行動就 Gemini。I/O 餘震才是真故事，不是定價。",
    [
        {
            "title": "ChatGPT GPT-5.5 Instant 預設，領先確立",
            "body": "OpenAI 這禮拜把 GPT-5.5 Instant 升級成 ChatGPT 預設，推理增強加更深的 agent 工具存取加最精緻的手機 App，撐住領先。Gemini Spark 上市是唯一可信挑戰，但還是 beta 限定。"
        },
        {
            "title": "Claude Opus 4.7 守住，Anthropic 進入守勢",
            "body": "Anthropic 四月沒推 Opus 4.7 之後的東西，I/O 餘震沒給他們回應的跑道。1M 上下文視窗加領先的程式碼準確率把 Claude 守在第二進階用戶跟開發者的位置，但這個位置現在是守勢。"
        },
        {
            "title": "Gemini Spark Google 最新 agent 敘事",
            "body": "Google 的 Spark agent beta 加禮拜一 I/O 的 Omni 世界模型，給 Google 2026 最強的 agent 敘事，雖然日常使用精緻度還是落後 ChatGPT。trusted-tester 加 AI Ultra 會員把體驗閘住，接下來兩週驗證話術。"
        }
    ],
)

add(
    "best-ai-coding-assistants",
    [AI_LLMSTATS, AI_FELLO, {
        "title": "Best AI coding assistants 2026: Claude Code, Cursor, Copilot",
        "url": "https://felloai.com/best-ai-models/",
        "source": "Fello AI",
    }],
    "Saturday morning the AI coding assistant chart confirms Claude Code holds first because the Opus 4.7 backbone plus the 1M context plus the agent tool integration is still the right pitch for serious software engineering work. The week of I/O 2026 did not produce a credible Anthropic challenger from Google's side. Cursor stays second, the IDE-native integration plus the model-router that ships with Opus 4.7 and GPT-5.5 plus Gemini 3.5 Flash is the right pitch for buyers who want one editor that uses every model. GitHub Copilot at third holds the Microsoft-shop pitch, the VS Code integration plus the Workspace agent plus the underlying GPT-5.5 access is still the broadest deployment. Windsurf (formerly Codeium) at fourth, the Cascade agent plus the lower price floor at $15/mo is the right pitch for the cost-conscious developer. Replit Agent fifth, the cloud-first dev environment plus the agent-driven scaffolding is the right pitch for prototyping. Saturday verdict: Claude Code for serious engineering, Cursor for editor-first model-routing, Copilot for Microsoft shops.",
    [
        {
            "title": "Claude Code — Opus 4.7 keeps the engineering crown",
            "body": "Anthropic's Opus 4.7 backbone plus the 1M context plus the agent tool integration plus the terminal-first workflow is still the right pitch for serious software engineering, and Google's I/O 2026 did not produce a credible challenger to dislodge it."
        },
        {
            "title": "Cursor — model-router editor wins for power users",
            "body": "Cursor's IDE-native integration plus the model-router that picks between Opus 4.7, GPT-5.5, and Gemini 3.5 Flash is the right pitch for buyers who want one editor that uses every model. The May refresh added Gemini 3.5 Flash to the routing pool."
        },
        {
            "title": "GitHub Copilot — Microsoft shop default",
            "body": "Copilot's VS Code integration plus the Workspace agent plus the GPT-5.5 access is still the broadest deployment in the category, and at $19/mo for Business it is the right default for any Microsoft-anchored engineering team. The Workspace agent finally caught up to Cursor on March refresh."
        }
    ],
    "禮拜六早上，AI 程式碼助手榜單確認 Claude Code 守第一，因為 Opus 4.7 後端加 1M 上下文加 agent 工具整合還是嚴肅軟體工程作業的對的話術。I/O 2026 那週 Google 沒有生出可信的 Anthropic 挑戰者。\n\nCursor 第二，IDE 原生整合加 model-router 一次配 Opus 4.7 加 GPT-5.5 加 Gemini 3.5 Flash，是想要一個編輯器用所有模型買家的對的話術。\n\n講真的，GitHub Copilot 第三守住微軟商店話術，VS Code 整合加 Workspace agent 加底層 GPT-5.5 存取還是部署最廣。Windsurf（前 Codeium）第四，Cascade agent 加 NT$470/月更低價是省錢派開發者的話術。Replit Agent 第五，雲端優先開發環境加 agent 驅動鷹架是原型話術。\n\n禮拜六結論：嚴肅工程就 Claude Code，編輯器優先 model-routing 就 Cursor，微軟商店就 Copilot。",
    [
        {
            "title": "Claude Code Opus 4.7 守住工程王座",
            "body": "Anthropic Opus 4.7 後端加 1M 上下文加 agent 工具整合加 terminal 優先工作流，還是嚴肅軟體工程作業的對的話術，Google I/O 2026 沒有生出可信挑戰者把它擠下去。"
        },
        {
            "title": "Cursor model-router 編輯器贏進階用戶",
            "body": "Cursor IDE 原生整合加 model-router 在 Opus 4.7、GPT-5.5、Gemini 3.5 Flash 之間挑，是想要一個編輯器用所有模型買家的話術。五月更新把 Gemini 3.5 Flash 加進路由池。"
        },
        {
            "title": "GitHub Copilot 微軟商店預設",
            "body": "Copilot 的 VS Code 整合加 Workspace agent 加 GPT-5.5 存取還是這品類部署最廣，Business 版 NT$600/月對任何微軟錨點工程團隊是對的預設選擇。三月更新後 Workspace agent 終於追上 Cursor。"
        }
    ],
)

add(
    "best-ai-image-generators",
    [AI_LLMSTATS, AI_FELLO, AI_LLMNEWS],
    "Saturday morning the AI image generator chart confirms Midjourney V7 holds first because the V7 aesthetic plus the still-best prompt adherence is the right pitch for serious creative work. The May 2026 frontier did not produce a Midjourney challenger because labs are catching their breath after April. OpenAI DALL-E 4 (via ChatGPT) stays second, the GPT-5.5-driven prompt understanding plus the inline ChatGPT workflow is the right pitch for general users who want image generation alongside chat. Google Imagen 4 climbs third because the I/O 2026 refresh tied Imagen tighter into the Gemini app and the photorealism on faces and text rendering closes the gap to Midjourney. Black Forest Labs FLUX.1 Pro at fourth, the open-weight option plus the still-leading hands and text rendering is the right pitch for self-hosted enterprise. Adobe Firefly Image 3 fifth, the Photoshop integration plus the commercial-safe training data is the right pitch for creative professionals. Saturday verdict: Midjourney for art-direction, DALL-E 4 for ChatGPT workflow, Imagen 4 for Gemini workflow, FLUX.1 Pro for self-host.",
    [
        {
            "title": "Midjourney V7 holds — aesthetic crown intact",
            "body": "The V7 aesthetic plus the still-best prompt adherence is the right pitch for serious creative work, and the May 2026 frontier did not produce a Midjourney challenger because labs are catching their breath after April. The aesthetic crown stays."
        },
        {
            "title": "Google Imagen 4 closes the gap at I/O 2026",
            "body": "I/O 2026 tied Imagen 4 tighter into the Gemini app and the photorealism on faces and text rendering closes the gap to Midjourney for everyday use cases. The Gemini app integration is the differentiator and Google now has the strongest mass-market image story."
        },
        {
            "title": "FLUX.1 Pro — the self-hosted enterprise pick",
            "body": "Black Forest Labs FLUX.1 Pro plus the open-weight FLUX.1 Schnell variants give the right pitch for self-hosted enterprise. The hands rendering and the text-in-image accuracy still lead the open-weight bracket and the May refresh improved the prompt adherence on long descriptions."
        }
    ],
    "禮拜六早上，AI 圖片產生器榜單確認 Midjourney V7 守第一，因為 V7 美學加還是最好的 prompt 遵從度，是嚴肅創作的對的話術。2026 五月前線沒有 Midjourney 挑戰者，因為各實驗室四月之後在喘氣。\n\nOpenAI DALL-E 4（透過 ChatGPT）第二，GPT-5.5 驅動的 prompt 理解加 ChatGPT 內嵌工作流，是一般用戶要圖片產生器搭聊天的話術。\n\n講真的，Google Imagen 4 爬到第三，I/O 2026 把 Imagen 跟 Gemini App 綁更緊，臉部跟文字渲染的擬真度縮小了跟 Midjourney 的差距。Black Forest Labs FLUX.1 Pro 第四，開放權重加還是領先的手部跟文字渲染，是自架企業話術。Adobe Firefly Image 3 第五，Photoshop 整合加商用安全訓練資料是創意專業話術。\n\n禮拜六結論：藝術導向就 Midjourney，ChatGPT 工作流就 DALL-E 4，Gemini 工作流就 Imagen 4，自架就 FLUX.1 Pro。",
    [
        {
            "title": "Midjourney V7 守住，美學王座完整",
            "body": "V7 美學加還是最好的 prompt 遵從度，是嚴肅創作的對的話術，2026 五月前線沒生出 Midjourney 挑戰者，因為各實驗室四月後在喘氣。美學王座守住。"
        },
        {
            "title": "Google Imagen 4 在 I/O 2026 縮小差距",
            "body": "I/O 2026 把 Imagen 4 跟 Gemini App 綁更緊，臉部跟文字渲染擬真度在日常使用情境縮小跟 Midjourney 的差距。Gemini App 整合是差異化，Google 現在有最強的大眾市場圖片故事。"
        },
        {
            "title": "FLUX.1 Pro 自架企業選擇",
            "body": "Black Forest Labs FLUX.1 Pro 加開放權重 FLUX.1 Schnell 變體，給自架企業的對話術。手部渲染跟圖片內文字準確率還是開放權重檔領先，五月更新改善長描述的 prompt 遵從度。"
        }
    ],
)

add(
    "best-ai-video-generators",
    [AI_LLMSTATS, AI_FELLO, AI_CNBC_GOOGLE],
    "Saturday morning the AI video generator chart confirms Google Veo 3 still holds first because the I/O 2026 refresh extended Veo 3 to longer-clip generation and integrated audio. OpenAI Sora 2 stays second, the physics-aware motion plus the ChatGPT-integrated workflow is the right pitch for general users. Runway Gen-4 climbs third, the creator-tuned controls plus the Director Mode is the right pitch for filmmakers. Pika Labs 2.0 at fourth, the social-share-friendly templates and the lower price floor are the right pitch for casual creators. Luma Dream Machine fifth, the camera-motion controls are competitive but the prompt adherence still lags. Saturday verdict: Veo 3 for filmmaker-grade output, Sora 2 for ChatGPT workflow, Runway for director controls. The I/O refresh is the actual story.",
    [
        {
            "title": "Veo 3 — I/O 2026 extends the lead",
            "body": "Google extended Veo 3 to longer-clip generation and integrated audio at I/O 2026, which is the right pitch for filmmaker-grade output and pushes the lead over Sora 2. The Gemini app integration is the right mass-market vector."
        },
        {
            "title": "Sora 2 — ChatGPT workflow holds second",
            "body": "OpenAI's Sora 2 physics-aware motion plus the ChatGPT-integrated workflow keeps the platform competitive for general-use video generation, and the May 2026 frontier did not produce a Veo 3 challenger that displaces Sora 2 from second."
        },
        {
            "title": "Runway Gen-4 — Director Mode wins filmmakers",
            "body": "Runway Gen-4 plus the Director Mode plus the creator-tuned controls is the right pitch for actual filmmakers who want frame-by-frame control. The lower price floor at $35/mo for Standard is the right call for indie creators."
        }
    ],
    "禮拜六早上，AI 影片產生器榜單確認 Google Veo 3 還是守第一，因為 I/O 2026 更新把 Veo 3 延伸到更長片段產生加整合音訊。\n\nOpenAI Sora 2 第二，物理感知運動加 ChatGPT 整合工作流是一般用戶的對的話術。\n\n講真的，Runway Gen-4 爬到第三，創作者調校控制加 Director Mode 是電影工作者的話術。Pika Labs 2.0 第四，社群分享友善範本加更低價是輕度創作者話術。Luma Dream Machine 第五，鏡頭運動控制有競爭力但 prompt 遵從度還是落後。\n\n禮拜六結論：電影級就 Veo 3，ChatGPT 工作流就 Sora 2，導演控制就 Runway。I/O 更新才是真故事。",
    [
        {
            "title": "Veo 3 I/O 2026 拉開差距",
            "body": "Google 在 I/O 2026 把 Veo 3 延伸到更長片段產生加整合音訊，是電影級輸出的對的話術，把領先拉得比 Sora 2 更開。Gemini App 整合是對的大眾市場向量。"
        },
        {
            "title": "Sora 2 ChatGPT 工作流守第二",
            "body": "OpenAI Sora 2 的物理感知運動加 ChatGPT 整合工作流，把平台守在一般用戶影片產生有競爭力的位置，2026 五月前線沒有生出把 Sora 2 擠下第二的 Veo 3 挑戰者。"
        },
        {
            "title": "Runway Gen-4 Director Mode 贏電影工作者",
            "body": "Runway Gen-4 加 Director Mode 加創作者調校控制，是真正電影工作者要逐格控制的對的話術。Standard 版 NT$1,100/月低價是獨立創作者的選擇。"
        }
    ],
)

add(
    "best-ai-meeting-assistants",
    [AI_LLMSTATS, AI_FELLO, {
        "title": "Best AI meeting assistants 2026",
        "url": "https://zapier.com/blog/best-ai-meeting-assistant/",
        "source": "Zapier",
    }],
    "Saturday morning the AI meeting assistant chart held its Friday shape. Otter.ai stays first, the live transcription plus the AI Chat that queries past meetings plus the new Outline AI feature from April is still the right pitch for any knowledge worker who lives in Zoom and Teams. Fireflies.ai holds second, the wider conference platform support plus the team-collaboration features plus the cheaper tier is the right pitch for small teams. Read.ai third, the meeting-effectiveness scoring plus the calendar-routing plus the integration with Notion and Slack is the right pitch for managers. Zoom AI Companion fourth, the native Zoom integration plus the free tier for paid Zoom users is the right pitch for Zoom-only shops. Microsoft Teams Copilot fifth, the Teams-native integration plus the Microsoft 365 backbone is the right pitch for Microsoft shops. Saturday verdict: Otter for general use, Fireflies for small teams, Read.ai for managers.",
    [
        {
            "title": "Otter.ai — Outline AI extends the lead",
            "body": "The April Outline AI feature pulls structured outcomes from any meeting and routes them into Notion or Asana, which is the right pitch for knowledge workers who want post-meeting actions instead of just transcripts. Otter's lead in this category extends after the spring update."
        },
        {
            "title": "Fireflies.ai — small-team default",
            "body": "Fireflies' wider conference platform support (Zoom, Teams, Meet, Webex) plus the team-collaboration features plus the cheaper Pro tier at $10/mo is the right pitch for small teams that need to share meeting notes without a Notion-style enterprise setup."
        },
        {
            "title": "Read.ai — manager-grade meeting analytics",
            "body": "Read.ai's meeting-effectiveness scoring plus the calendar-routing plus the integration with Notion and Slack is the right pitch for managers who want to measure meeting ROI, not just transcribe. The April update added speaking-time-by-person analytics."
        }
    ],
    "禮拜六早上，AI 會議助理榜單守住禮拜五形狀。\n\nOtter.ai 守第一，即時轉錄加 AI Chat 查詢過去會議加四月新 Outline AI 功能，還是住 Zoom 跟 Teams 知識工作者的對的話術。\n\nFireflies.ai 第二，更廣的會議平台支援加團隊協作功能加便宜方案是小團隊話術。\n\n講真的，Read.ai 第三，會議效果評分加日曆路由加 Notion 跟 Slack 整合是管理者話術。Zoom AI Companion 第四，原生 Zoom 整合加付費 Zoom 用戶免費，是 Zoom 商店話術。Microsoft Teams Copilot 第五，Teams 原生整合加 Microsoft 365 後端是微軟商店話術。\n\n禮拜六結論：一般用就 Otter，小團隊就 Fireflies，管理者就 Read.ai。",
    [
        {
            "title": "Otter.ai Outline AI 拉開差距",
            "body": "四月 Outline AI 功能從任何會議拉出結構化結果再路由到 Notion 或 Asana，是想要會後行動而不只是逐字稿知識工作者的話術。Otter 在這品類的領先在春季更新後拉得更開。"
        },
        {
            "title": "Fireflies.ai 小團隊預設",
            "body": "Fireflies 更廣的會議平台支援（Zoom、Teams、Meet、Webex）加團隊協作功能加 Pro 方案 NT$313/月便宜價，是要分享會議筆記又不想搞 Notion 等級企業設置小團隊的話術。"
        },
        {
            "title": "Read.ai 管理者級會議分析",
            "body": "Read.ai 會議效果評分加日曆路由加 Notion 跟 Slack 整合，是想要衡量會議 ROI 而不只是轉錄管理者的話術。四月更新加了個人發言時間分析。"
        }
    ],
)

add(
    "best-ai-voice-generators",
    [AI_LLMSTATS, AI_FELLO, AI_LLMNEWS],
    "Saturday morning the AI voice generator chart held its Friday shape. ElevenLabs holds first, the voice-cloning quality plus the multi-language support plus the still-best prosody is the right pitch for any voice-over or audiobook work. OpenAI Voice (via ChatGPT advanced voice mode + standalone API) stays second, the GPT-5.5-tied conversational naturalness plus the inline ChatGPT workflow is the right pitch for general users. PlayHT third, the studio-grade voice library plus the API-friendly pricing is the right pitch for developers. Resemble AI fourth, the real-time voice-cloning plus the brand-safe customization is the right pitch for enterprise. WellSaid Labs fifth, the e-learning-tuned voices plus the production-pipeline features are the right pitch for corporate training. Saturday verdict: ElevenLabs for voice work, OpenAI Voice for ChatGPT workflow, PlayHT for developers.",
    [
        {
            "title": "ElevenLabs — prosody crown intact",
            "body": "Voice-cloning quality plus the multi-language support plus the still-best prosody is the right pitch for any voice-over or audiobook work, and the May 2026 frontier did not produce an ElevenLabs challenger. The position is defended through the I/O fallout."
        },
        {
            "title": "OpenAI Voice — ChatGPT mode holds second",
            "body": "OpenAI's advanced voice mode plus the standalone API plus the GPT-5.5-tied conversational naturalness keeps the platform second for general users. The inline ChatGPT workflow is the right pitch for buyers who already pay for ChatGPT Plus."
        },
        {
            "title": "PlayHT — developer-tier default",
            "body": "PlayHT's studio-grade voice library plus the API-friendly pricing plus the streaming low-latency option is the right pitch for developers who need to embed voice into apps. The May refresh improved the multi-language support across European languages."
        }
    ],
    "禮拜六早上，AI 語音產生器榜單守住禮拜五形狀。\n\nElevenLabs 守第一，語音克隆品質加多語言支援加還是最好的韻律，是任何配音或有聲書作業的對的話術。\n\nOpenAI Voice（透過 ChatGPT 進階語音模式加獨立 API）第二，GPT-5.5 綁的對話自然度加 ChatGPT 內嵌工作流，是一般用戶的話術。\n\n講真的，PlayHT 第三，錄音室等級語音庫加 API 友善定價是開發者話術。Resemble AI 第四，即時語音克隆加品牌安全自訂是企業話術。WellSaid Labs 第五，e-learning 調校語音加製作流程功能是企業訓練話術。\n\n禮拜六結論：配音工作就 ElevenLabs，ChatGPT 工作流就 OpenAI Voice，開發者就 PlayHT。",
    [
        {
            "title": "ElevenLabs 韻律王座完整",
            "body": "語音克隆品質加多語言支援加還是最好的韻律，是任何配音或有聲書作業的話術，2026 五月前線沒有生出 ElevenLabs 挑戰者。在 I/O 餘震中位置守住。"
        },
        {
            "title": "OpenAI Voice ChatGPT 模式守第二",
            "body": "OpenAI 進階語音模式加獨立 API 加 GPT-5.5 綁的對話自然度，把平台守在一般用戶第二。ChatGPT 內嵌工作流是已經付 ChatGPT Plus 買家的話術。"
        },
        {
            "title": "PlayHT 開發者檔預設",
            "body": "PlayHT 錄音室等級語音庫加 API 友善定價加串流低延遲選項，是要把語音嵌進 App 開發者的話術。五月更新改善歐洲語言的多語言支援。"
        }
    ],
)

add(
    "best-ai-music-generators",
    [AI_LLMSTATS, AI_FELLO, {
        "title": "Best AI music generators 2026: Suno, Udio, Stable Audio",
        "url": "https://felloai.com/best-ai-models/",
        "source": "Fello AI",
    }],
    "Saturday morning the AI music generator chart held its Friday shape. Suno V5 holds first, the vocal quality plus the still-best lyrics-to-song coherence is the right pitch for casual creators and content makers. Udio stays second, the producer-style controls plus the higher-fidelity instrument separation is the right pitch for music creators who want to layer and edit. Stable Audio 2.0 (Stability AI) third, the open-source ethos plus the longer-form generation is the right pitch for self-hosted enterprise. Google Lyria third because the I/O 2026 refresh tied Lyria to YouTube Shorts but the standalone polish lags Suno. SOUNDRAW fifth, the genre-specific templates and the royalty-free licensing are the right pitch for YouTubers. Saturday verdict: Suno for casual, Udio for creators, Stable Audio for self-host.",
    [
        {
            "title": "Suno V5 — vocal quality leads",
            "body": "Vocal quality plus the still-best lyrics-to-song coherence is the right pitch for casual creators and content makers. The V5 refresh from April improved the mixing balance and the Suno crown holds through the May 2026 frontier breath."
        },
        {
            "title": "Udio — producer-style controls",
            "body": "Producer-style controls plus the higher-fidelity instrument separation plus the May update on stems export is the right pitch for music creators who want to layer and edit. Udio is the second-place buy for anyone who treats AI music as a tool, not a finished product."
        },
        {
            "title": "Stable Audio 2.0 — self-host pick",
            "body": "Stability AI's open-source ethos plus the longer-form generation plus the new commercial-license tier is the right pitch for self-hosted enterprise. The model weights ship through Hugging Face and the inference cost on a single H100 is the lowest in the category."
        }
    ],
    "禮拜六早上，AI 音樂產生器榜單守住禮拜五形狀。\n\nSuno V5 守第一，人聲品質加還是最好的歌詞到歌曲一致性，是輕度創作者跟內容創作者的對的話術。\n\nUdio 第二，製作人風格控制加更高解析度的樂器分離，是要分層編輯的音樂創作者的話術。\n\n講真的，Stable Audio 2.0（Stability AI）第三，開源精神加更長片段產生是自架企業話術。Google Lyria 第四因為 I/O 2026 更新把 Lyria 綁進 YouTube Shorts 但獨立精緻度落後 Suno。SOUNDRAW 第五，類型專用範本加版稅免費授權是 YouTuber 話術。\n\n禮拜六結論：輕度就 Suno，創作者就 Udio，自架就 Stable Audio。",
    [
        {
            "title": "Suno V5 人聲品質領先",
            "body": "人聲品質加還是最好的歌詞到歌曲一致性，是輕度創作者跟內容創作者的話術。四月 V5 更新改善混音平衡，Suno 王座在 2026 五月前線喘氣中守住。"
        },
        {
            "title": "Udio 製作人風格控制",
            "body": "製作人風格控制加更高解析度的樂器分離加五月 stems 匯出更新，是要分層編輯音樂創作者的話術。Udio 是把 AI 音樂當工具不當成品買家的第二選擇。"
        },
        {
            "title": "Stable Audio 2.0 自架選擇",
            "body": "Stability AI 開源精神加更長片段產生加新的商用授權層，是自架企業話術。模型權重透過 Hugging Face 出貨，單台 H100 的推論成本是這品類最低。"
        }
    ],
)


# ---------- KITCHEN ----------

add(
    "best-air-fryers",
    [MD_KITCHN, MD_BB, MD_CNN],
    "Saturday morning the air fryer category held the Friday cuts and Best Buy plus The Kitchn both extended the MD picks into Saturday. Ninja DoubleStack XL holds first at $159 (down $50), the dual-basket plus the vertical stacking plus the SmartLid function is still the right family pitch. Instant Vortex Plus 6QT stays second at $99 (down $30), the larger 6QT capacity plus the clear-window basket plus the budget-friendly price is the right pitch for first-timers. Cosori Pro II 5.8QT third at $89 (down $30), the broader recipe library plus the cheaper price floor is the right pitch for budget buyers. Breville Smart Oven Air fourth at $349 (down $50), the multi-function countertop pitch is the right call for kitchens that want one device to do toast, bake, and air-fry. Ninja Foodi DualZone fifth at $169 (down $30), the dual-basket plus the synced finish is the right pitch for cooking two foods at once. Saturday verdict: DoubleStack XL for families, Instant Vortex Plus for first-timers, Breville Smart Oven Air for kitchens that want one multi-function device.",
    [
        {
            "title": "Ninja DoubleStack XL at $159 — family pick",
            "body": "Ninja held the $50 cut on the DoubleStack XL through Saturday. Dual-basket plus the vertical stacking plus the SmartLid function at $159 is the right family pitch, and this is the best DoubleStack price outside Prime Day."
        },
        {
            "title": "Instant Vortex Plus 6QT at $99 — first-timer buy",
            "body": "Instant held the $30 cut through Saturday. 6QT capacity plus the clear-window basket plus the friendlier learning curve at $99 is the right pitch for first-timers, and the Instant Brands recipe app integration matters more than the marginal feature differences with Cosori."
        },
        {
            "title": "Breville Smart Oven Air at $349 — multi-function pick",
            "body": "Breville held the $50 cut through Saturday. The multi-function pitch (toast + bake + air-fry + convection) at $349 is the right call for kitchens that want one device to replace toaster oven + air fryer. The build quality justifies the premium over the Ninja and Cosori options."
        }
    ],
    "禮拜六早上，氣炸鍋品類把禮拜五的折扣守過夜，Best Buy 跟 The Kitchn 都把國殤日推薦延進禮拜六。\n\nNinja DoubleStack XL 守第一 NT$5,000（砍 NT$1,570），雙籃加垂直堆疊加 SmartLid 功能還是家庭話術。\n\nInstant Vortex Plus 6QT 第二 NT$3,140（砍 NT$940），更大的 6QT 容量加透明窗口籃加預算友善價，是新手話術。\n\n講真的，Cosori Pro II 5.8QT 第三 NT$2,800（砍 NT$940），更廣的食譜庫加更低價是預算買家話術。Breville Smart Oven Air 第四 NT$10,900（砍 NT$1,570），多功能桌上型是想要一台搞定吐司、烘焙、氣炸廚房的話術。Ninja Foodi DualZone 第五 NT$5,300（砍 NT$940），雙籃加同步完成是同時煮兩種食物話術。\n\n禮拜六結論：家庭就 DoubleStack XL，新手就 Instant Vortex Plus，要一機多用就 Breville Smart Oven Air。",
    [
        {
            "title": "Ninja DoubleStack XL NT$5,000 家庭買點",
            "body": "Ninja 把 DoubleStack XL 的 NT$1,570 折扣守進禮拜六。雙籃加垂直堆疊加 SmartLid 功能 NT$5,000，是家庭話術，這是 Prime Day 之外 DoubleStack 最佳價。"
        },
        {
            "title": "Instant Vortex Plus 6QT NT$3,140 新手買點",
            "body": "Instant 把 NT$940 折扣守進禮拜六。6QT 容量加透明窗口籃加更友善學習曲線 NT$3,140，是新手話術，Instant Brands 食譜 App 整合比跟 Cosori 邊際功能差更重要。"
        },
        {
            "title": "Breville Smart Oven Air NT$10,900 多功能選擇",
            "body": "Breville 把 NT$1,570 折扣守進禮拜六。多功能話術（吐司加烘焙加氣炸加對流）NT$10,900，是要一台取代烤箱加氣炸鍋廚房的選擇。做工撐起對 Ninja 跟 Cosori 的溢價。"
        }
    ],
)

add(
    "best-coffee-makers",
    [MD_KITCHN, MD_CNN, MD_NBC],
    "Saturday morning the coffee maker chart held the Friday cuts. Breville Barista Express Impress holds first at $749 (down $150 at Williams Sonoma), the integrated grinder plus the smart assistive tamping plus the espresso quality is the right semi-pro pitch. Technivorm Moccamaster KBT stays second at $329 (down $30 at Moccamaster direct), the 5-year warranty plus the Dutch craftsmanship plus the SCA-certified brewing is the right pour-over pitch. De'Longhi Magnifica Evo at third at $549 (down $100), the bean-to-cup automation plus the LatteCrema system is the right pitch for milk-drink drinkers. Ninja CFP451 DualBrew Pro fourth at $179 (down $50), the K-Cup-plus-grounds dual-mode is the right pitch for mixed-household coffee drinkers. Keurig K-Supreme Plus Smart fifth at $149 (down $50), the BrewID and the smart-pour customization is the right K-Cup pick. Saturday verdict: Breville Barista Express Impress for espresso, Moccamaster for pour-over, De'Longhi Magnifica Evo for milk drinks.",
    [
        {
            "title": "Breville Barista Express Impress at $749 — semi-pro buy",
            "body": "Williams Sonoma held the $150 cut on the Impress through Saturday. Integrated grinder plus smart assistive tamping plus the espresso quality at $749 is the right semi-pro pitch and the assisted tamp is a meaningful upgrade over the original Barista Express for buyers who do not want to learn manual technique."
        },
        {
            "title": "Moccamaster KBT at $329 — pour-over king",
            "body": "Moccamaster held the $30 cut through Saturday at Moccamaster direct. The 5-year warranty plus the Dutch craftsmanship plus the SCA-certified brewing at $329 is the right pour-over pitch and no other drip brewer matches the long-term reliability."
        },
        {
            "title": "De'Longhi Magnifica Evo at $549 — milk-drink default",
            "body": "De'Longhi held the $100 cut through Saturday. Bean-to-cup automation plus the LatteCrema system at $549 is the right pitch for households that want one machine to produce espresso, latte, and cappuccino without barista training. The price floor is the lowest the model has hit this year."
        }
    ],
    "禮拜六早上，咖啡機榜單把禮拜五的折扣守過夜。\n\nBreville Barista Express Impress 守第一 NT$23,500（Williams Sonoma 砍 NT$4,700），整合磨豆加智慧輔助壓粉加義式品質是半專業話術。\n\nTechnivorm Moccamaster KBT 第二 NT$10,300（Moccamaster 直營砍 NT$940），5 年保固加荷蘭工藝加 SCA 認證萃取，是手沖話術。\n\n講真的，De'Longhi Magnifica Evo 第三 NT$17,200（砍 NT$3,140），全自動加 LatteCrema 系統是奶咖派話術。Ninja CFP451 DualBrew Pro 第四 NT$5,600（砍 NT$1,570），K-Cup 加粉雙模式是混合家庭話術。Keurig K-Supreme Plus Smart 第五 NT$4,700（砍 NT$1,570），BrewID 加智慧沖泡客製是 K-Cup 選擇。\n\n禮拜六結論：義式就 Breville Barista Express Impress，手沖就 Moccamaster，奶咖就 De'Longhi Magnifica Evo。",
    [
        {
            "title": "Breville Barista Express Impress NT$23,500 半專業買點",
            "body": "Williams Sonoma 把 Impress 的 NT$4,700 折扣守進禮拜六。整合磨豆加智慧輔助壓粉加義式品質 NT$23,500，是半專業話術，輔助壓粉對不想學手動技術買家是比原版 Barista Express 有意義的升級。"
        },
        {
            "title": "Moccamaster KBT NT$10,300 手沖王",
            "body": "Moccamaster 把 NT$940 折扣守進禮拜六，Moccamaster 直營。5 年保固加荷蘭工藝加 SCA 認證萃取 NT$10,300，是手沖話術，沒有別的滴漏咖啡機能對齊長期可靠度。"
        },
        {
            "title": "De'Longhi Magnifica Evo NT$17,200 奶咖預設",
            "body": "De'Longhi 把 NT$3,140 折扣守進禮拜六。全自動加 LatteCrema 系統 NT$17,200，是要一機產出義式、拿鐵、卡布奇諾又不用學咖啡師家庭的話術。這個地板價是今年型號最低。"
        }
    ],
)

add(
    "best-rice-cookers",
    [MD_KITCHN, MD_HD, MD_CNN],
    "Saturday morning the rice cooker chart held the Friday MD cuts. Zojirushi Neuro Fuzzy NS-ZCC10 holds first at $199 (down $30), the fuzzy-logic plus the multi-rice modes plus the lifetime durability is still the right pitch. Tiger JNP-S10U stays second at $99, the simple toggle plus the Tiger reliability is the right Japanese-rice pitch. Cuckoo CRP-LHTR0609F third at $399 (down $50), the high-pressure mode plus the Korean-rice optimization is the right pitch for Korean households. Aroma Housewares ARC-5000SB fourth at $69, the budget pick for plain rice. Toshiba TRCS01 fifth at $189 (down $30), the induction heating at this floor is the right value pitch. Saturday verdict: Neuro Fuzzy for Japanese rice, Cuckoo for Korean rice, Aroma for budget.",
    [
        {
            "title": "Zojirushi Neuro Fuzzy at $199 — Japanese rice king",
            "body": "Zojirushi held the $30 cut through Saturday. Fuzzy-logic plus the multi-rice modes plus the lifetime durability at $199 is the right Japanese rice pitch and no other brand matches the long-term reliability. Zojirushi remains the conviction buy."
        },
        {
            "title": "Cuckoo CRP-LHTR0609F at $399 — Korean rice pick",
            "body": "Cuckoo held the $50 cut through Saturday. High-pressure mode plus the Korean-rice optimization plus the dual-pack mode at $399 is the right pitch for Korean households that want bap perfection. The voice prompts in Korean and English ship in May firmware."
        },
        {
            "title": "Toshiba TRCS01 at $189 — induction value pick",
            "body": "Toshiba held the $30 cut through Saturday. Induction heating at $189 is the right value pitch for buyers who want IH technology without paying Zojirushi or Tiger premium prices. The 6-cup capacity is enough for a 3-person household."
        }
    ],
    "禮拜六早上，電子鍋榜單把禮拜五國殤日的折扣守過夜。\n\nZojirushi Neuro Fuzzy NS-ZCC10 守第一 NT$6,200（砍 NT$940），模糊邏輯加多種米模式加終身耐用度，還是日本米話術。\n\nTiger JNP-S10U 第二 NT$3,140，簡單切換加 Tiger 可靠度是日本米選擇。\n\n講真的，Cuckoo CRP-LHTR0609F 第三 NT$12,500（砍 NT$1,570），高壓力模式加韓國米優化是韓式家庭話術。Aroma Housewares ARC-5000SB 第四 NT$2,200，是白米預算選擇。Toshiba TRCS01 第五 NT$5,900（砍 NT$940），這個價位的 IH 加熱是值話術。\n\n禮拜六結論：日本米就 Neuro Fuzzy，韓國米就 Cuckoo，預算就 Aroma。",
    [
        {
            "title": "Zojirushi Neuro Fuzzy NT$6,200 日本米王",
            "body": "Zojirushi 把 NT$940 折扣守進禮拜六。模糊邏輯加多種米模式加終身耐用度 NT$6,200，是日本米話術，沒有別的品牌能對齊長期可靠度。Zojirushi 還是有底氣買點。"
        },
        {
            "title": "Cuckoo CRP-LHTR0609F NT$12,500 韓國米選擇",
            "body": "Cuckoo 把 NT$1,570 折扣守進禮拜六。高壓力模式加韓國米優化加雙艙模式 NT$12,500，是要韓式飯完美韓式家庭的話術。語音提示韓英雙語五月韌體出貨。"
        },
        {
            "title": "Toshiba TRCS01 NT$5,900 IH 值買點",
            "body": "Toshiba 把 NT$940 折扣守進禮拜六。IH 加熱 NT$5,900 是想要 IH 技術又不想付 Zojirushi 或 Tiger 溢價買家的話術。6 杯容量對 3 人家庭夠用。"
        }
    ],
)

add(
    "best-portable-ice-makers",
    [MD_CNN, MD_HD, MD_NBC],
    "Saturday morning the portable ice maker chart held the Friday cuts. GE Profile Opal 2.0 holds first at $499 (down $100 at Best Buy), the nugget-ice quality plus the WiFi-connected scheduling is still the right pitch for buyers who want Sonic-style chewable ice. Frigidaire EFIC117-SS stays second at $129 (down $40), the bullet-ice plus the 26 lb/day capacity at this price is the right value pitch. Newair Countertop Clear Ice Maker third at $299 (down $50), the crystal-clear cubes plus the bar-quality output is the right pitch for entertainment. NewAir Nugget Ice Maker NIM050SS fourth at $369 (down $80), the Opal alternative at a cheaper floor is the right pitch for nugget-ice buyers who refuse to pay GE premium. Sonic NewAir Sonic Ice Maker fifth at $349 (down $50), the Sonic-licensed branding plus the chewable nugget output is for the Sonic loyalists. Saturday verdict: Opal 2.0 for nugget ice premium, Frigidaire for bullet ice budget, Newair Clear for bar-quality cubes.",
    [
        {
            "title": "GE Profile Opal 2.0 at $499 — nugget ice king",
            "body": "Best Buy held the $100 cut on the Opal 2.0 through Saturday. Nugget-ice quality plus the WiFi-connected scheduling plus the smart side-tank at $499 is the right pitch for buyers who want Sonic-style chewable ice without the Sonic-licensed price tag."
        },
        {
            "title": "Frigidaire EFIC117-SS at $129 — bullet-ice value",
            "body": "Frigidaire held the $40 cut through Saturday. Bullet-ice plus the 26 lb/day capacity at $129 is the right value pitch for first-time ice maker buyers, and the build quality finally matches the price floor after the 2025 refresh."
        },
        {
            "title": "Newair Countertop Clear at $299 — entertainment pick",
            "body": "Newair held the $50 cut through Saturday. Crystal-clear cubes plus the bar-quality output at $299 is the right pitch for buyers who entertain and want cocktail-grade ice that doesn't cloud. The crystal cube output is the differentiator."
        }
    ],
    "禮拜六早上，攜帶式製冰機榜單把禮拜五的折扣守過夜。\n\nGE Profile Opal 2.0 守第一 NT$15,700（Best Buy 砍 NT$3,140），珍珠冰品質加 WiFi 連線排程，還是想要 Sonic 風可咀嚼冰買家的話術。\n\nFrigidaire EFIC117-SS 第二 NT$4,100（砍 NT$1,250），子彈冰加 26 磅/天容量在這個價是值話術。\n\n講真的，Newair Countertop Clear Ice Maker 第三 NT$9,400（砍 NT$1,570），水晶透明方塊加酒吧品質輸出是娛樂話術。NewAir Nugget Ice Maker NIM050SS 第四 NT$11,600（砍 NT$2,500），是拒絕付 GE 溢價珍珠冰買家的選擇。Sonic NewAir Sonic Ice Maker 第五 NT$10,900（砍 NT$1,570），Sonic 授權品牌加可咀嚼珍珠冰輸出是 Sonic 死忠選擇。\n\n禮拜六結論：高階珍珠冰就 Opal 2.0，預算子彈冰就 Frigidaire，酒吧品質方塊就 Newair Clear。",
    [
        {
            "title": "GE Profile Opal 2.0 NT$15,700 珍珠冰王",
            "body": "Best Buy 把 Opal 2.0 的 NT$3,140 折扣守進禮拜六。珍珠冰品質加 WiFi 連線排程加智慧側水箱 NT$15,700，是想要 Sonic 風可咀嚼冰又不要付 Sonic 授權牌價買家的話術。"
        },
        {
            "title": "Frigidaire EFIC117-SS NT$4,100 子彈冰值買點",
            "body": "Frigidaire 把 NT$1,250 折扣守進禮拜六。子彈冰加 26 磅/天容量 NT$4,100，是第一次買製冰機的話術，做工終於在 2025 改款後對齊這個價格。"
        },
        {
            "title": "Newair Countertop Clear NT$9,400 娛樂選擇",
            "body": "Newair 把 NT$1,570 折扣守進禮拜六。水晶透明方塊加酒吧品質輸出 NT$9,400，是常宴客要雞尾酒級不會渾濁冰塊買家的話術。透明方塊輸出就是差異化。"
        }
    ],
)

add(
    "best-outdoor-griddles",
    [MD_HD, MD_CNN, MD_NBC],
    "Saturday morning the outdoor griddle chart held the Friday MD cuts as Home Depot extended the Memorial Day appliance window. Blackstone 36-inch ProSeries 4-Burner holds first at $499 (down $100 at Home Depot), the 36-inch cooktop plus the 4-burner zone control plus the new electronic ignition is still the right pitch for tailgaters and large family cooking. Camp Chef Flat Top Grill FTG900 stays second at $529 (down $70), the dual-mode flat-top plus the grill grate is the right pitch for buyers who want one device. Pit Boss Ultimate 5-Burner Plancha at third at $599 (down $100), the 5-burner zone control plus the larger cooking surface is the right pitch for backyard parties. Royal Gourmet GB4002G 4-Burner fourth at $329 (down $50), the budget pick for first-time outdoor griddle buyers. Blackstone 28-inch Tabletop fifth at $189 (down $40), the tabletop pitch is the right buy for apartment balconies. Saturday verdict: Blackstone 36 ProSeries for large family, Camp Chef for dual-mode, Royal Gourmet for budget.",
    [
        {
            "title": "Blackstone 36 ProSeries at $499 — large family buy",
            "body": "Home Depot held the $100 cut through Saturday. 36-inch cooktop plus the 4-burner zone control plus the new electronic ignition at $499 is the right pitch for tailgaters and large family cooking. This is the best Blackstone price outside Prime Day."
        },
        {
            "title": "Camp Chef FTG900 at $529 — dual-mode pick",
            "body": "Camp Chef held the $70 cut through Saturday. Dual-mode flat-top plus the swappable grill grate at $529 is the right pitch for buyers who want one device for both flat-top and traditional grilling. The build quality justifies the premium over Blackstone."
        },
        {
            "title": "Royal Gourmet GB4002G at $329 — budget entry",
            "body": "Royal Gourmet held the $50 cut through Saturday. 4-burner zone control plus the 36-inch cooktop at $329 is the right budget pitch for first-time outdoor griddle buyers. The build quality is one tier below Blackstone but the value math is the strongest in the category."
        }
    ],
    "禮拜六早上，戶外鐵板燒榜單把禮拜五國殤日折扣守過夜，Home Depot 延展國殤日家電窗口。\n\nBlackstone 36 吋 ProSeries 4 燃燒器守第一 NT$15,700（Home Depot 砍 NT$3,140），36 吋烹飪面加 4 燃燒器分區控制加新電子點火，還是 tailgate 加大家庭料理話術。\n\nCamp Chef Flat Top Grill FTG900 第二 NT$16,600（砍 NT$2,200），雙模式平頂加烤架是想要一機到底買家的話術。\n\n講真的，Pit Boss Ultimate 5 燃燒器 Plancha 第三 NT$18,800（砍 NT$3,140），5 燃燒器分區控制加更大烹飪面是後院派對話術。Royal Gourmet GB4002G 4 燃燒器第四 NT$10,300（砍 NT$1,570），是第一次買戶外鐵板燒的預算選擇。Blackstone 28 吋桌上型第五 NT$5,900（砍 NT$1,250），桌上型是公寓陽台選擇。\n\n禮拜六結論：大家庭就 Blackstone 36 ProSeries，雙模式就 Camp Chef，預算就 Royal Gourmet。",
    [
        {
            "title": "Blackstone 36 ProSeries NT$15,700 大家庭買點",
            "body": "Home Depot 把 NT$3,140 折扣守進禮拜六。36 吋烹飪面加 4 燃燒器分區控制加新電子點火 NT$15,700，是 tailgate 加大家庭料理話術。Prime Day 之外 Blackstone 最佳價。"
        },
        {
            "title": "Camp Chef FTG900 NT$16,600 雙模式選擇",
            "body": "Camp Chef 把 NT$2,200 折扣守進禮拜六。雙模式平頂加可換烤架 NT$16,600，是要一機搞定平頂跟傳統燒烤買家的話術。做工撐起對 Blackstone 的溢價。"
        },
        {
            "title": "Royal Gourmet GB4002G NT$10,300 預算入門",
            "body": "Royal Gourmet 把 NT$1,570 折扣守進禮拜六。4 燃燒器分區控制加 36 吋烹飪面 NT$10,300，是第一次買戶外鐵板燒的預算話術。做工比 Blackstone 低一級但性價比是這品類最強。"
        }
    ],
)

add(
    "best-dishwashers",
    [MD_HD, MD_LG, MD_GE],
    "Saturday morning the dishwasher chart held the Friday cuts because LG, GE, and Home Depot all extended their MD appliance windows. Bosch 800 Series SHP78CM5N holds first at $1,099 (down $300 at Best Buy), the CrystalDry technology plus the third rack plus the 42 dB silent operation is still the right premium pitch. LG SmartDishwasher LDPS6762S stays second at $799 (down $300 at LG), the TrueSteam plus the QuadWash Pro plus the Wi-Fi diagnostics is the right pitch for value-conscious premium buyers. GE Profile UltraFresh PDT755SBVTS at third at $899 (down $300 at GE), the Microban antimicrobial protection plus the AutoSense cycle is the right pitch for hygiene priorities. Miele G 7106 SCU fourth at $1,499 (down $200), the AutoDos detergent dispensing plus the 20-year build life is the right premium-luxury pitch. Whirlpool WDTA50SAKZ fifth at $599 (down $150), the budget pick. Saturday verdict: Bosch 800 for quiet premium, LG for value premium, Miele for luxury.",
    [
        {
            "title": "Bosch 800 Series at $1,099 — quiet premium buy",
            "body": "Best Buy held the $300 cut on the Bosch 800 Series through Saturday. CrystalDry plus the third rack plus the 42 dB silent operation at $1,099 is the right premium pitch and this is the best Bosch 800 price since the last Black Friday."
        },
        {
            "title": "LG LDPS6762S at $799 — value premium pick",
            "body": "LG held the $300 cut through Saturday. TrueSteam plus the QuadWash Pro plus the Wi-Fi diagnostics at $799 is the right pitch for value-conscious premium buyers, and the price floor is $300 below the Bosch equivalent for similar feature parity."
        },
        {
            "title": "GE Profile UltraFresh at $899 — hygiene pick",
            "body": "GE held the $300 cut through Saturday. Microban antimicrobial protection plus the AutoSense cycle plus the deep-clean wash zones at $899 is the right pitch for households that put hygiene ahead of decibel performance. The MD pricing math holds through Monday."
        }
    ],
    "禮拜六早上，洗碗機榜單把禮拜五的折扣守過夜，LG、GE、Home Depot 都延展國殤日家電窗口。\n\nBosch 800 Series SHP78CM5N 守第一 NT$34,500（Best Buy 砍 NT$9,400），CrystalDry 技術加第三層架加 42 dB 靜音，還是高階話術。\n\nLG SmartDishwasher LDPS6762S 第二 NT$25,100（LG 砍 NT$9,400），TrueSteam 加 QuadWash Pro 加 Wi-Fi 診斷是性價比高階話術。\n\n講真的，GE Profile UltraFresh PDT755SBVTS 第三 NT$28,300（GE 砍 NT$9,400），Microban 抗菌保護加 AutoSense 行程是衛生優先話術。Miele G 7106 SCU 第四 NT$47,100（砍 NT$6,300），AutoDos 洗碗精配給加 20 年壽命是奢華話術。Whirlpool WDTA50SAKZ 第五 NT$18,800（砍 NT$4,700），是預算選擇。\n\n禮拜六結論：靜音高階就 Bosch 800，性價比高階就 LG，奢華就 Miele。",
    [
        {
            "title": "Bosch 800 Series NT$34,500 靜音高階買點",
            "body": "Best Buy 把 Bosch 800 Series 的 NT$9,400 折扣守進禮拜六。CrystalDry 加第三層架加 42 dB 靜音 NT$34,500，是高階話術，這是上次黑五以來 Bosch 800 最佳價。"
        },
        {
            "title": "LG LDPS6762S NT$25,100 性價比高階",
            "body": "LG 把 NT$9,400 折扣守進禮拜六。TrueSteam 加 QuadWash Pro 加 Wi-Fi 診斷 NT$25,100，是性價比高階話術，這個地板價比 Bosch 同級便宜 NT$9,400 功能差不多。"
        },
        {
            "title": "GE Profile UltraFresh NT$28,300 衛生選擇",
            "body": "GE 把 NT$9,400 折扣守進禮拜六。Microban 抗菌保護加 AutoSense 行程加深層清潔分區 NT$28,300，是把衛生擺在分貝表現前面家庭的話術。國殤日定價算數守到禮拜一。"
        }
    ],
)

# ---------- HOME ----------

add(
    "best-air-purifiers",
    [MD_CNN, MD_NBC, MD_HD],
    "Saturday morning the air purifier chart held the Friday cuts. Coway Airmega 250 holds first at $279 (down $70 at Coway), the dual-filter HEPA plus the smart auto mode plus the energy-efficient operation is still the right mainstream pitch. Levoit Vital 200S stays second at $179 (down $40), the larger room coverage plus the quiet sleep mode plus the lower price floor is the right pitch for bedrooms. Dyson Purifier Cool TP09 at third at $549 (down $150 at Dyson direct), the formaldehyde-destruction plus the bladeless fan is the right pitch for buyers who want premium design and dual-function. Blueair Blue Pure 311i Max fourth at $249 (down $50), the HEPASilent plus the larger CADR is the right pitch for living rooms. IQAir HealthPro Plus fifth at $749 (down $150), the medical-grade HyperHEPA is the right pitch for allergy sufferers. Saturday verdict: Coway Airmega 250 for mainstream, Levoit Vital 200S for bedrooms, IQAir for medical-grade.",
    [
        {
            "title": "Coway Airmega 250 at $279 — mainstream buy",
            "body": "Coway held the $70 cut through Saturday. Dual-filter HEPA plus the smart auto mode plus the energy-efficient operation at $279 is the right mainstream pitch and Wirecutter has reaffirmed the Coway recommendation through the May refresh."
        },
        {
            "title": "Levoit Vital 200S at $179 — bedroom pick",
            "body": "Levoit held the $40 cut through Saturday. Larger room coverage plus the quiet sleep mode plus the lower price floor at $179 is the right pitch for bedrooms, and the 22 dB sleep mode is the differentiator over the Coway in night use."
        },
        {
            "title": "IQAir HealthPro Plus at $749 — medical pick",
            "body": "IQAir held the $150 cut through Saturday. Medical-grade HyperHEPA plus the 30-year filter life on the V5-Cell at $749 is the right pitch for allergy sufferers who need particulate filtration down to 0.003 microns. The premium is justified for serious respiratory conditions."
        }
    ],
    "禮拜六早上，空氣清淨機榜單把禮拜五的折扣守過夜。\n\nCoway Airmega 250 守第一 NT$8,790（Coway 砍 NT$2,200），雙濾網 HEPA 加智慧自動模式加節能運作，還是主流話術。\n\nLevoit Vital 200S 第二 NT$5,600（砍 NT$1,250），更大房間覆蓋加安靜睡眠模式加更低價，是臥室話術。\n\n講真的，Dyson Purifier Cool TP09 第三 NT$17,200（Dyson 直營砍 NT$4,700），甲醛分解加無葉風扇是要設計加雙功能買家話術。Blueair Blue Pure 311i Max 第四 NT$7,800（砍 NT$1,570），HEPASilent 加更大 CADR 是客廳話術。IQAir HealthPro Plus 第五 NT$23,500（砍 NT$4,700），醫療級 HyperHEPA 是過敏患者話術。\n\n禮拜六結論：主流就 Coway Airmega 250，臥室就 Levoit Vital 200S，醫療級就 IQAir。",
    [
        {
            "title": "Coway Airmega 250 NT$8,790 主流買點",
            "body": "Coway 把 NT$2,200 折扣守進禮拜六。雙濾網 HEPA 加智慧自動模式加節能運作 NT$8,790，是主流話術，Wirecutter 五月更新確認 Coway 推薦。"
        },
        {
            "title": "Levoit Vital 200S NT$5,600 臥室選擇",
            "body": "Levoit 把 NT$1,250 折扣守進禮拜六。更大房間覆蓋加安靜睡眠模式加更低價 NT$5,600，是臥室話術，22 dB 睡眠模式是夜間使用比 Coway 的差異化。"
        },
        {
            "title": "IQAir HealthPro Plus NT$23,500 醫療選擇",
            "body": "IQAir 把 NT$4,700 折扣守進禮拜六。醫療級 HyperHEPA 加 V5-Cell 上 30 年濾網壽命 NT$23,500，是要過濾到 0.003 微米過敏患者的話術。嚴重呼吸道狀況的人付溢價有理。"
        }
    ],
)

add(
    "best-robot-vacuums",
    [MD_CNN, MD_NBC, MD_TECHRADAR],
    "Saturday morning the robot vacuum chart held the Friday cuts as iRobot extended the Roomba Plus 505 Combo + AutoWash Dock at $549.99 (down $450) through Saturday. Roborock S8 MaxV Ultra holds first at $1,099 (down $500 at Best Buy), the dual-LiDAR navigation plus the AutoEmpty + AutoWash docks plus the 10,000 Pa suction is the right premium pitch. iRobot Roomba Plus 505 Combo stays second at $549.99 (down $450), the AutoWash Dock plus the rubber dual-roller plus the Genius mapping is the right pitch for the Roomba loyalist. Eufy X10 Pro Omni at third at $599 (down $200), the pivoting mop plus the auto-empty-and-wash is the right pitch for value-conscious premium buyers. Shark AI Ultra fourth at $349 (down $150), the Shark-friendly mop hybrid is the right pitch for budget-premium. iRobot Roomba i3+ EVO fifth at $279 (down $120), the entry-level Roomba with self-empty is the right pitch for first-timer mainstream. Saturday verdict: Roborock S8 MaxV Ultra for flagship, Roomba Plus 505 for $549.99 Roomba loyalty, Eufy X10 Pro Omni for value premium.",
    [
        {
            "title": "Roborock S8 MaxV Ultra at $1,099 — flagship buy",
            "body": "Best Buy held the $500 cut on the S8 MaxV Ultra through Saturday. Dual-LiDAR navigation plus the AutoEmpty + AutoWash docks plus the 10,000 Pa suction at $1,099 is the right flagship pitch and the mop-lift system handles carpets without the Roomba 9 series tradeoffs."
        },
        {
            "title": "iRobot Roomba Plus 505 Combo at $549.99 — Roomba loyalty pick",
            "body": "iRobot direct held the $450 cut on the Plus 505 Combo + AutoWash Dock through Saturday. The 45% off floor on a brand-new flagship is rare for iRobot and at $549.99 the AutoWash Dock plus the rubber dual-roller is the right pitch for the Roomba loyalist."
        },
        {
            "title": "Eufy X10 Pro Omni at $599 — value premium",
            "body": "Eufy held the $200 cut through Saturday. The pivoting mop plus the auto-empty-and-wash plus the AI obstacle avoidance at $599 is the right pitch for value-conscious premium buyers, and the price floor is $500 under the Roborock equivalent for similar feature parity."
        }
    ],
    "禮拜六早上，掃地機器人榜單把禮拜五折扣守過夜，iRobot 把 Roomba Plus 505 Combo 加 AutoWash Dock 的 NT$17,300（砍 NT$14,100）延進禮拜六。\n\nRoborock S8 MaxV Ultra 守第一 NT$34,500（Best Buy 砍 NT$15,700），雙 LiDAR 導航加 AutoEmpty 加 AutoWash 基座加 10,000 Pa 吸力，還是高階話術。\n\niRobot Roomba Plus 505 Combo 第二 NT$17,300（砍 NT$14,100），AutoWash Dock 加橡膠雙滾刷加 Genius 地圖是 Roomba 死忠話術。\n\n講真的，Eufy X10 Pro Omni 第三 NT$18,800（砍 NT$6,300），翻轉拖布加自動倒垃圾加清洗是性價比高階話術。Shark AI Ultra 第四 NT$10,900（砍 NT$4,700），Shark 友善拖布混血是預算高階話術。iRobot Roomba i3+ EVO 第五 NT$8,790（砍 NT$3,770），自動倒垃圾入門 Roomba 是新手主流話術。\n\n禮拜六結論：旗艦就 Roborock S8 MaxV Ultra，Roomba 死忠就 Plus 505 Combo NT$17,300，性價比高階就 Eufy X10 Pro Omni。",
    [
        {
            "title": "Roborock S8 MaxV Ultra NT$34,500 旗艦買點",
            "body": "Best Buy 把 S8 MaxV Ultra 的 NT$15,700 折扣守進禮拜六。雙 LiDAR 導航加 AutoEmpty 加 AutoWash 基座加 10,000 Pa 吸力 NT$34,500，是旗艦話術，拖布抬升系統不像 Roomba 9 系列有地毯權衡。"
        },
        {
            "title": "iRobot Roomba Plus 505 Combo NT$17,300 Roomba 死忠",
            "body": "iRobot 直營把 Plus 505 Combo 加 AutoWash Dock 的 NT$14,100 折扣守進禮拜六。45% off 全新旗艦對 iRobot 罕見，NT$17,300 的 AutoWash Dock 加橡膠雙滾刷是 Roomba 死忠話術。"
        },
        {
            "title": "Eufy X10 Pro Omni NT$18,800 性價比高階",
            "body": "Eufy 把 NT$6,300 折扣守進禮拜六。翻轉拖布加自動倒垃圾加清洗加 AI 障礙物迴避 NT$18,800，是性價比高階話術，地板價比 Roborock 同級便宜 NT$15,700 功能差不多。"
        }
    ],
)

add(
    "best-robot-lawn-mowers",
    [MD_HD, MD_NBC, MD_CNN],
    "Saturday morning the robot mower chart held the Friday cuts. Husqvarna Automower 430X NERA holds first at $3,499 (down $500), the no-wire EPOS satellite navigation plus the all-weather operation plus the 0.8 acre range is still the right premium pitch. Worx Landroid Vision L1600 stays second at $2,499 (down $300), the AI-camera mowing plus the no-wire setup plus the cheaper price floor is the right pitch for mid-yard buyers. Segway Navimow i108 at third at $1,499 (down $300), the GPS-based no-wire setup plus the smaller yard pitch is the right value choice. Ecovacs Goat G1 fourth at $1,799 (down $300), the AI vision plus the smart obstacle detection is the right pitch for cluttered yards. Mammotion LUBA 2 AWD 5000 fifth at $2,999 (down $300), the AWD plus the 1.25 acre coverage is the right pitch for hilly yards. Saturday verdict: Husqvarna 430X NERA for premium acres, Worx L1600 for mid-yard value, Segway i108 for small-yard budget.",
    [
        {
            "title": "Husqvarna 430X NERA at $3,499 — premium acres",
            "body": "Husqvarna held the $500 cut through Saturday. No-wire EPOS satellite navigation plus the all-weather operation plus the 0.8 acre range at $3,499 is the right premium pitch and the EPOS setup is the only one in the category that eliminates the perimeter wire entirely."
        },
        {
            "title": "Worx Landroid Vision L1600 at $2,499 — mid-yard pick",
            "body": "Worx held the $300 cut through Saturday. AI-camera mowing plus the no-wire setup plus the cheaper price floor at $2,499 is the right pitch for mid-yard buyers (up to half an acre) who refuse to spend $3,500 on a Husqvarna. The setup time is the differentiator."
        },
        {
            "title": "Mammotion LUBA 2 AWD 5000 at $2,999 — hilly-yard pick",
            "body": "Mammotion held the $300 cut through Saturday. AWD plus the 1.25 acre coverage plus the slope handling at $2,999 is the right pitch for hilly yards that the Husqvarna and Worx cannot navigate. The AWD differentiator is unique in the category at this price."
        }
    ],
    "禮拜六早上，割草機器人榜單把禮拜五的折扣守過夜。\n\nHusqvarna Automower 430X NERA 守第一 NT$110,000（砍 NT$15,700），無線 EPOS 衛星導航加全天候運作加 0.8 英畝範圍，還是高階話術。\n\nWorx Landroid Vision L1600 第二 NT$78,500（砍 NT$9,400），AI 攝影機割草加無線設置加更低價，是中型院子話術。\n\n講真的，Segway Navimow i108 第三 NT$47,100（砍 NT$9,400），GPS 無線設置加小院子話術是值選擇。Ecovacs Goat G1 第四 NT$56,500（砍 NT$9,400），AI 視覺加智慧障礙物偵測是雜亂院子話術。Mammotion LUBA 2 AWD 5000 第五 NT$94,200（砍 NT$9,400），AWD 加 1.25 英畝覆蓋是斜坡院子話術。\n\n禮拜六結論：高階英畝就 Husqvarna 430X NERA，中型院子就 Worx L1600，小院子預算就 Segway i108。",
    [
        {
            "title": "Husqvarna 430X NERA NT$110,000 高階英畝",
            "body": "Husqvarna 把 NT$15,700 折扣守進禮拜六。無線 EPOS 衛星導航加全天候運作加 0.8 英畝範圍 NT$110,000，是高階話術，EPOS 設置是這品類唯一完全沒有周界線的方案。"
        },
        {
            "title": "Worx Landroid Vision L1600 NT$78,500 中型院子",
            "body": "Worx 把 NT$9,400 折扣守進禮拜六。AI 攝影機割草加無線設置加更低價 NT$78,500，是中型院子（半英畝以下）拒絕花 NT$110,000 買 Husqvarna 買家的話術。設置時間是差異化。"
        },
        {
            "title": "Mammotion LUBA 2 AWD 5000 NT$94,200 斜坡院子",
            "body": "Mammotion 把 NT$9,400 折扣守進禮拜六。AWD 加 1.25 英畝覆蓋加斜坡處理 NT$94,200，是 Husqvarna 跟 Worx 無法處理斜坡院子的話術。AWD 差異化在這個價是這品類唯一。"
        }
    ],
)

add(
    "best-standing-desks",
    [MD_CNN, MD_NBC, MD_TECHRADAR],
    "Saturday morning the standing desk chart held the Friday cuts. Uplift V2 Commercial holds first at $649 (down $100 at Uplift direct), the dual-motor plus the wide configurability plus the 15-year warranty is still the right premium pitch. Fully Jarvis stays second at $589 (down $80), the Bamboo top option plus the customizable accessory ecosystem is the right pitch for ergonomics-conscious buyers. Branch Standing Desk Pro at third at $549 (down $50), the build quality at this floor plus the simpler design is the right pitch for minimalist offices. Vari Electric Standing Desk fourth at $695 (down $100), the higher load capacity plus the office-grade build is the right pitch for shared workspaces. FlexiSpot E7 Pro Plus fifth at $399 (down $80), the budget-premium pitch with dual-motor and decent build. Saturday verdict: Uplift V2 for premium ergonomics, Fully Jarvis for customization, FlexiSpot E7 Pro Plus for budget.",
    [
        {
            "title": "Uplift V2 Commercial at $649 — premium ergonomics",
            "body": "Uplift held the $100 cut through Saturday. Dual-motor plus wide configurability plus the 15-year warranty at $649 is still the right premium ergonomics pitch and the V2 Commercial frame is the rated workhorse for shared office spaces."
        },
        {
            "title": "Fully Jarvis at $589 — customization pick",
            "body": "Fully held the $80 cut through Saturday. The Bamboo top option plus the customizable accessory ecosystem plus the 7-year warranty at $589 is the right pitch for ergonomics-conscious buyers who want a desk that adapts over time, not a one-shot purchase."
        },
        {
            "title": "FlexiSpot E7 Pro Plus at $399 — budget-premium",
            "body": "FlexiSpot held the $80 cut through Saturday. Dual-motor plus the decent build at $399 is the right budget-premium pitch and the price floor matches the best FlexiSpot has put up this year. The right call for buyers who refuse to spend $600+ on a desk frame."
        }
    ],
    "禮拜六早上，升降桌榜單把禮拜五的折扣守過夜。\n\nUplift V2 Commercial 守第一 NT$20,400（Uplift 直營砍 NT$3,140），雙馬達加廣泛可組態加 15 年保固，還是高階話術。\n\nFully Jarvis 第二 NT$18,500（砍 NT$2,500），竹製桌面選項加可客製配件生態是人體工學派話術。\n\n講真的，Branch Standing Desk Pro 第三 NT$17,200（砍 NT$1,570），這個價格的做工加更簡單設計是極簡辦公室話術。Vari Electric Standing Desk 第四 NT$21,900（砍 NT$3,140），更高承重加辦公室級做工是共用工作空間話術。FlexiSpot E7 Pro Plus 第五 NT$12,500（砍 NT$2,500），雙馬達加不錯做工是預算高階話術。\n\n禮拜六結論：高階人體工學就 Uplift V2，客製化就 Fully Jarvis，預算就 FlexiSpot E7 Pro Plus。",
    [
        {
            "title": "Uplift V2 Commercial NT$20,400 高階人體工學",
            "body": "Uplift 把 NT$3,140 折扣守進禮拜六。雙馬達加廣泛可組態加 15 年保固 NT$20,400，還是高階人體工學話術，V2 Commercial 機架是共用辦公空間經評定的耐操機種。"
        },
        {
            "title": "Fully Jarvis NT$18,500 客製化選擇",
            "body": "Fully 把 NT$2,500 折扣守進禮拜六。竹製桌面選項加可客製配件生態加 7 年保固 NT$18,500，是要桌子隨時間調整不是一次到位人體工學派買家的話術。"
        },
        {
            "title": "FlexiSpot E7 Pro Plus NT$12,500 預算高階",
            "body": "FlexiSpot 把 NT$2,500 折扣守進禮拜六。雙馬達加不錯做工 NT$12,500，是預算高階話術，這個地板價對得起今年 FlexiSpot 最佳價。拒絕在桌架花 NT$19,000+ 買家的選擇。"
        }
    ],
)

add(
    "best-treadmills",
    [MD_CNN, MD_NBC, MD_HD],
    "Saturday morning the treadmill chart held the Friday cuts as NordicTrack and Peloton both extended their MD floors. NordicTrack Commercial 1750 holds first at $1,799 (down $500), the iFit subscription plus the 22-inch touchscreen plus the auto-incline -3% to 15% is still the right premium home-gym pitch. Peloton Tread+ stays second at $5,995 (down $500), the Peloton instructor library plus the cushioned slat-belt is the right pitch for the Peloton-loyal household. Sole F80 at third at $1,499 (down $300), the strong motor plus the simpler programming is the right pitch for buyers who refuse subscription fees. NordicTrack X22i Incline Trainer fourth at $2,499 (down $500), the steeper -6% to 40% incline plus the iFit is the right pitch for hill training. Bowflex Treadmill 22 fifth at $1,799 (down $300), the JRNY subscription plus the wider running surface is the right Bowflex pitch. Saturday verdict: Commercial 1750 for premium with iFit, Sole F80 for no-subscription, X22i for hill training.",
    [
        {
            "title": "NordicTrack Commercial 1750 at $1,799 — premium pick",
            "body": "NordicTrack held the $500 cut through Saturday. iFit subscription plus the 22-inch touchscreen plus the auto-incline -3% to 15% at $1,799 is still the right premium home-gym pitch and the price floor matches the best the model has hit outside Black Friday."
        },
        {
            "title": "Sole F80 at $1,499 — no-subscription pick",
            "body": "Sole held the $300 cut through Saturday. Strong motor plus the simpler programming plus no subscription required at $1,499 is the right pitch for buyers who refuse the iFit or JRNY recurring fees. The Sole reliability is the differentiator."
        },
        {
            "title": "NordicTrack X22i Incline Trainer at $2,499 — hill training",
            "body": "NordicTrack held the $500 cut through Saturday. The steeper -6% to 40% incline plus the iFit subscription at $2,499 is the right pitch for hill training and the auto-decline feature is unique in the category. The X22i is the conviction buy for hikers training indoors."
        }
    ],
    "禮拜六早上，跑步機榜單把禮拜五的折扣守過夜，NordicTrack 跟 Peloton 都延展國殤日地板。\n\nNordicTrack Commercial 1750 守第一 NT$56,500（砍 NT$15,700），iFit 訂閱加 22 吋觸控螢幕加自動坡度 -3% 到 15%，還是高階居家健身房話術。\n\nPeloton Tread+ 第二 NT$188,400（砍 NT$15,700），Peloton 教練庫加緩衝板帶是 Peloton 死忠家庭話術。\n\n講真的，Sole F80 第三 NT$47,100（砍 NT$9,400），強馬達加更簡單編程是拒絕訂閱費買家的話術。NordicTrack X22i Incline Trainer 第四 NT$78,500（砍 NT$15,700），更陡的 -6% 到 40% 坡度加 iFit 是爬坡訓練話術。Bowflex Treadmill 22 第五 NT$56,500（砍 NT$9,400），JRNY 訂閱加更寬跑步面是 Bowflex 話術。\n\n禮拜六結論：iFit 高階就 Commercial 1750，無訂閱就 Sole F80，爬坡訓練就 X22i。",
    [
        {
            "title": "NordicTrack Commercial 1750 NT$56,500 高階選擇",
            "body": "NordicTrack 把 NT$15,700 折扣守進禮拜六。iFit 訂閱加 22 吋觸控螢幕加自動坡度 -3% 到 15% NT$56,500，還是高階居家健身房話術，這個地板價對得起黑五以外型號最佳價。"
        },
        {
            "title": "Sole F80 NT$47,100 無訂閱選擇",
            "body": "Sole 把 NT$9,400 折扣守進禮拜六。強馬達加更簡單編程加無訂閱要求 NT$47,100，是拒絕 iFit 或 JRNY 月費買家的話術。Sole 可靠度是差異化。"
        },
        {
            "title": "NordicTrack X22i Incline Trainer NT$78,500 爬坡訓練",
            "body": "NordicTrack 把 NT$15,700 折扣守進禮拜六。更陡的 -6% 到 40% 坡度加 iFit 訂閱 NT$78,500，是爬坡訓練話術，自動下坡功能在這品類獨家。X22i 是室內訓練爬山者的有底氣買點。"
        }
    ],
)

add(
    "best-massage-guns",
    [MD_CNN, MD_NBC, MD_TECHRADAR],
    "Saturday morning the massage gun chart held the Friday cuts. Theragun Pro Plus holds first at $499 (down $100 at Therabody), the OLED screen plus the 16mm amplitude plus the new red-light therapy head is still the right premium pitch. Hyperice Hypervolt 2 Pro stays second at $329 (down $70), the quiet operation plus the longer battery plus the smarter Bluetooth integration is the right pitch for athletes. Theragun Mini 2nd Gen at third at $199 (down $50), the portable form factor plus the 12mm amplitude is the right travel pitch. Renpho R3 Mini fourth at $69 (down $30), the budget pick. Hyperice Vyper 3 fifth at $199 (down $50), the vibrating roller is the right pitch for foam-roller users. Saturday verdict: Theragun Pro Plus for premium with red-light, Hypervolt 2 Pro for quiet athletic, Theragun Mini for travel.",
    [
        {
            "title": "Theragun Pro Plus at $499 — premium pick",
            "body": "Therabody held the $100 cut through Saturday. OLED screen plus the 16mm amplitude plus the new red-light therapy head at $499 is still the right premium pitch and the red-light head is the differentiator over the previous Pro generation."
        },
        {
            "title": "Hypervolt 2 Pro at $329 — quiet athletic pick",
            "body": "Hyperice held the $70 cut through Saturday. Quiet operation plus the longer battery plus the smarter Bluetooth integration at $329 is the right pitch for athletes who train in shared spaces or hotels. The decibel performance is the differentiator over Theragun."
        },
        {
            "title": "Theragun Mini 2nd Gen at $199 — travel buy",
            "body": "Therabody held the $50 cut on the Mini 2nd Gen through Saturday. The portable form factor plus the 12mm amplitude at $199 is the right travel pitch, and the Mini 2nd Gen build is meaningfully better than the original Mini for serious recovery."
        }
    ],
    "禮拜六早上，按摩槍榜單把禮拜五的折扣守過夜。\n\nTheragun Pro Plus 守第一 NT$15,700（Therabody 砍 NT$3,140），OLED 螢幕加 16mm 振幅加新紅光治療頭，還是高階話術。\n\nHyperice Hypervolt 2 Pro 第二 NT$10,300（砍 NT$2,200），安靜運作加更長電池加更聰明藍牙整合，是運動員話術。\n\n講真的，Theragun Mini 2nd Gen 第三 NT$6,200（砍 NT$1,570），攜帶版型加 12mm 振幅是旅行話術。Renpho R3 Mini 第四 NT$2,200（砍 NT$940），是預算選擇。Hyperice Vyper 3 第五 NT$6,200（砍 NT$1,570），振動滾筒是泡棉滾筒用戶話術。\n\n禮拜六結論：紅光高階就 Theragun Pro Plus，安靜運動就 Hypervolt 2 Pro，旅行就 Theragun Mini。",
    [
        {
            "title": "Theragun Pro Plus NT$15,700 高階選擇",
            "body": "Therabody 把 NT$3,140 折扣守進禮拜六。OLED 螢幕加 16mm 振幅加新紅光治療頭 NT$15,700，還是高階話術，紅光頭就是比前代 Pro 的差異化。"
        },
        {
            "title": "Hypervolt 2 Pro NT$10,300 安靜運動",
            "body": "Hyperice 把 NT$2,200 折扣守進禮拜六。安靜運作加更長電池加更聰明藍牙整合 NT$10,300，是在共用空間或旅館訓練運動員的話術。分貝表現就是比 Theragun 的差異化。"
        },
        {
            "title": "Theragun Mini 2nd Gen NT$6,200 旅行買點",
            "body": "Therabody 把 Mini 2nd Gen 的 NT$1,570 折扣守進禮拜六。攜帶版型加 12mm 振幅 NT$6,200，是旅行話術，Mini 2nd Gen 做工對嚴肅恢復比原版 Mini 有意義升級。"
        }
    ],
)

# ---------- NETWORK / SECURITY ----------

add(
    "best-mesh-wifi-systems",
    [MD_CNN, MD_NBC, MD_BB],
    "Saturday morning the mesh WiFi chart held the Friday cuts. Eero Max 7 holds first at $1,499 (down $200 at Eero direct), the WiFi 7 plus the 10Gbps backhaul plus the Amazon ecosystem integration is still the right premium pitch. Netgear Orbi 970 Series stays second at $1,499 (down $300), the WiFi 7 plus the higher channel capacity plus the dedicated backhaul is the right pitch for power users. TP-Link Deco BE85 at third at $899 (down $200), the WiFi 7 at a cheaper floor plus the easy setup is the right value pitch. Asus ZenWiFi BQ16 Pro fourth at $1,099 (down $200), the WiFi 7 plus the AiMesh customization is the right pitch for tinkerers. Google Nest WiFi Pro fifth at $349 (down $80), the WiFi 6E entry-level mesh is the right pitch for Google-ecosystem buyers. Saturday verdict: Eero Max 7 for ecosystem premium, Orbi 970 for power-user premium, Deco BE85 for value WiFi 7.",
    [
        {
            "title": "Eero Max 7 at $1,499 — ecosystem premium",
            "body": "Eero direct held the $200 cut through Saturday. WiFi 7 plus the 10Gbps backhaul plus the Amazon ecosystem integration at $1,499 is still the right premium pitch and the Eero Max 7 is the only WiFi 7 system with native Alexa-bridging built in."
        },
        {
            "title": "Orbi 970 at $1,499 — power-user premium",
            "body": "Netgear held the $300 cut through Saturday. WiFi 7 plus higher channel capacity plus the dedicated backhaul at $1,499 is the right pitch for power users who run heavy mesh loads (10+ devices) and want maximum aggregate throughput across the home."
        },
        {
            "title": "TP-Link Deco BE85 at $899 — value WiFi 7",
            "body": "TP-Link held the $200 cut through Saturday. WiFi 7 plus the easy setup at $899 is the right value pitch and the price floor is $600 under the Eero Max 7 for similar feature parity on small-to-medium homes. The right buy for cost-conscious WiFi 7 upgraders."
        }
    ],
    "禮拜六早上，網狀網路榜單把禮拜五的折扣守過夜。\n\nEero Max 7 守第一 NT$47,100（Eero 直營砍 NT$6,300），WiFi 7 加 10Gbps 回傳加 Amazon 生態整合，還是高階話術。\n\nNetgear Orbi 970 Series 第二 NT$47,100（砍 NT$9,400），WiFi 7 加更高通道容量加專用回傳是進階用戶話術。\n\n講真的，TP-Link Deco BE85 第三 NT$28,300（砍 NT$6,300），更低價的 WiFi 7 加易設置是值話術。Asus ZenWiFi BQ16 Pro 第四 NT$34,500（砍 NT$6,300），WiFi 7 加 AiMesh 客製是改機派話術。Google Nest WiFi Pro 第五 NT$10,900（砍 NT$2,500），WiFi 6E 入門網狀是 Google 生態話術。\n\n禮拜六結論：生態高階就 Eero Max 7，進階用戶就 Orbi 970，值 WiFi 7 就 Deco BE85。",
    [
        {
            "title": "Eero Max 7 NT$47,100 生態高階",
            "body": "Eero 直營把 NT$6,300 折扣守進禮拜六。WiFi 7 加 10Gbps 回傳加 Amazon 生態整合 NT$47,100，還是高階話術，Eero Max 7 是唯一原生 Alexa 橋接 WiFi 7 系統。"
        },
        {
            "title": "Orbi 970 NT$47,100 進階用戶高階",
            "body": "Netgear 把 NT$9,400 折扣守進禮拜六。WiFi 7 加更高通道容量加專用回傳 NT$47,100，是跑重網狀負載（10+ 裝置）想要全家最大總吞吐進階用戶的話術。"
        },
        {
            "title": "TP-Link Deco BE85 NT$28,300 值 WiFi 7",
            "body": "TP-Link 把 NT$6,300 折扣守進禮拜六。WiFi 7 加易設置 NT$28,300 是值話術，地板價比 Eero Max 7 便宜 NT$18,800 對中小型住家功能差不多。省錢 WiFi 7 升級買家的選擇。"
        }
    ],
)

add(
    "best-security-cameras",
    [MD_CNN, MD_NBC, MD_BB],
    "Saturday morning the security camera chart held the Friday cuts. Arlo Pro 5S 2K holds first at $179 (down $50 at Best Buy), the 2K HDR plus the integrated spotlight plus the AI-driven Object Detection is still the right premium wireless pitch. Ring Stick Up Cam Pro stays second at $179 (down $50 at Ring), the Ring ecosystem plus the new radar-based motion detection is the right pitch for Ring-loyal households. Google Nest Cam (Battery) at third at $149 (down $30), the Nest Aware plus the Google Home integration is the right pitch for Google-ecosystem buyers. Eufy SoloCam S340 fourth at $169 (down $40), the dual-lens 3K plus the local storage and no-subscription pitch is the right value-premium buy. Wyze Cam OG fifth at $35 (down $5), the budget pick. Saturday verdict: Arlo Pro 5S for premium wireless, Ring Stick Up Cam Pro for Ring loyalty, Eufy SoloCam S340 for no-subscription.",
    [
        {
            "title": "Arlo Pro 5S at $179 — premium wireless buy",
            "body": "Best Buy held the $50 cut through Saturday. 2K HDR plus the integrated spotlight plus the AI-driven Object Detection at $179 is still the right premium wireless pitch and the AI Object Detection update from April reduced false positives by 30%."
        },
        {
            "title": "Ring Stick Up Cam Pro at $179 — Ring loyalty pick",
            "body": "Ring held the $50 cut through Saturday. The Ring ecosystem plus the new radar-based motion detection plus the Doorbell linking at $179 is the right pitch for Ring-loyal households that already pay for Ring Protect Plus."
        },
        {
            "title": "Eufy SoloCam S340 at $169 — no-subscription pick",
            "body": "Eufy held the $40 cut through Saturday. The dual-lens 3K plus the local storage plus the no-subscription pitch at $169 is the right value-premium buy for households that refuse Ring or Arlo recurring fees. The local storage matters for privacy-conscious buyers."
        }
    ],
    "禮拜六早上，監控攝影機榜單把禮拜五的折扣守過夜。\n\nArlo Pro 5S 2K 守第一 NT$5,600（Best Buy 砍 NT$1,570），2K HDR 加整合聚光燈加 AI 物件偵測，還是高階無線話術。\n\nRing Stick Up Cam Pro 第二 NT$5,600（Ring 砍 NT$1,570），Ring 生態加新雷達運動偵測是 Ring 死忠家庭話術。\n\n講真的，Google Nest Cam（電池版）第三 NT$4,700（砍 NT$940），Nest Aware 加 Google Home 整合是 Google 生態話術。Eufy SoloCam S340 第四 NT$5,300（砍 NT$1,250），雙鏡頭 3K 加本地儲存加無訂閱是性價比高階話術。Wyze Cam OG 第五 NT$1,100（砍 NT$160），是預算選擇。\n\n禮拜六結論：高階無線就 Arlo Pro 5S，Ring 死忠就 Stick Up Cam Pro，無訂閱就 Eufy SoloCam S340。",
    [
        {
            "title": "Arlo Pro 5S NT$5,600 高階無線買點",
            "body": "Best Buy 把 NT$1,570 折扣守進禮拜六。2K HDR 加整合聚光燈加 AI 物件偵測 NT$5,600，還是高階無線話術，四月 AI 物件偵測更新降低 30% 誤報。"
        },
        {
            "title": "Ring Stick Up Cam Pro NT$5,600 Ring 死忠",
            "body": "Ring 把 NT$1,570 折扣守進禮拜六。Ring 生態加新雷達運動偵測加門鈴連動 NT$5,600，是已經付 Ring Protect Plus Ring 死忠家庭的話術。"
        },
        {
            "title": "Eufy SoloCam S340 NT$5,300 無訂閱選擇",
            "body": "Eufy 把 NT$1,250 折扣守進禮拜六。雙鏡頭 3K 加本地儲存加無訂閱 NT$5,300，是拒絕 Ring 或 Arlo 月費家庭的性價比高階買點。本地儲存對隱私派買家重要。"
        }
    ],
)

add(
    "best-video-doorbells",
    [MD_CNN, MD_NBC, MD_BB],
    "Saturday morning the video doorbell chart held the Friday cuts. Ring Battery Doorbell Pro holds first at $179 (down $50 at Ring), the 1536p HD+ plus the radar-based 3D motion detection plus the Ring ecosystem is still the right premium pitch. Google Nest Doorbell (Battery) 2nd Gen stays second at $149 (down $30 at Google), the Google Home integration plus the 24/7 recording with Nest Aware is the right pitch for Google-ecosystem buyers. Arlo Video Doorbell 2K at third at $129 (down $40), the 2K HDR plus the wider 180-degree field-of-view is the right pitch for wider-coverage buyers. Eufy Video Doorbell Dual fourth at $179 (down $40), the dual-camera plus the no-subscription local storage is the right value-premium buy. Aqara G4 fifth at $99 (down $20), the HomeKit Secure Video integration is the right Apple-ecosystem pick. Saturday verdict: Ring Battery Doorbell Pro for premium Ring, Nest Doorbell for Google, Eufy Dual for no-subscription.",
    [
        {
            "title": "Ring Battery Doorbell Pro at $179 — premium pick",
            "body": "Ring held the $50 cut through Saturday. 1536p HD+ plus the radar-based 3D motion detection plus the Ring ecosystem at $179 is still the right premium pitch and the radar-based detection is the differentiator over the original Battery Doorbell."
        },
        {
            "title": "Google Nest Doorbell 2nd Gen at $149 — Google pick",
            "body": "Google held the $30 cut through Saturday. The Google Home integration plus the 24/7 recording with Nest Aware at $149 is the right pitch for Google-ecosystem buyers and the AI-driven Familiar Face detection finally caught up to Ring on the April refresh."
        },
        {
            "title": "Eufy Video Doorbell Dual at $179 — no-subscription pick",
            "body": "Eufy held the $40 cut through Saturday. Dual-camera plus the no-subscription local storage at $179 is the right value-premium buy for households that refuse Ring or Nest recurring fees. The dual-camera covers package delivery at the door step."
        }
    ],
    "禮拜六早上，視訊門鈴榜單把禮拜五的折扣守過夜。\n\nRing Battery Doorbell Pro 守第一 NT$5,600（Ring 砍 NT$1,570），1536p HD+ 加雷達 3D 運動偵測加 Ring 生態，還是高階話術。\n\nGoogle Nest Doorbell（電池版）2nd Gen 第二 NT$4,700（Google 砍 NT$940），Google Home 整合加 Nest Aware 24/7 錄影是 Google 生態話術。\n\n講真的，Arlo Video Doorbell 2K 第三 NT$4,100（砍 NT$1,250），2K HDR 加更廣 180 度視野是要更廣覆蓋買家話術。Eufy Video Doorbell Dual 第四 NT$5,600（砍 NT$1,250），雙鏡頭加無訂閱本地儲存是性價比高階話術。Aqara G4 第五 NT$3,140（砍 NT$620），HomeKit Secure Video 整合是 Apple 生態選擇。\n\n禮拜六結論：高階 Ring 就 Battery Doorbell Pro，Google 就 Nest Doorbell，無訂閱就 Eufy Dual。",
    [
        {
            "title": "Ring Battery Doorbell Pro NT$5,600 高階選擇",
            "body": "Ring 把 NT$1,570 折扣守進禮拜六。1536p HD+ 加雷達 3D 運動偵測加 Ring 生態 NT$5,600，還是高階話術，雷達運動偵測就是比原版 Battery Doorbell 的差異化。"
        },
        {
            "title": "Google Nest Doorbell 2nd Gen NT$4,700 Google 選擇",
            "body": "Google 把 NT$940 折扣守進禮拜六。Google Home 整合加 Nest Aware 24/7 錄影 NT$4,700，是 Google 生態話術，AI 熟面孔偵測四月更新終於追上 Ring。"
        },
        {
            "title": "Eufy Video Doorbell Dual NT$5,600 無訂閱選擇",
            "body": "Eufy 把 NT$1,250 折扣守進禮拜六。雙鏡頭加無訂閱本地儲存 NT$5,600，是拒絕 Ring 或 Nest 月費家庭的性價比高階話術。雙鏡頭涵蓋門口包裹送達。"
        }
    ],
)

add(
    "best-smart-thermostats",
    [MD_CNN, MD_NBC, MD_HD],
    "Saturday morning the smart thermostat chart held the Friday cuts. Google Nest Learning Thermostat 4th Gen holds first at $229 (down $50 at Google), the Matter-over-Thread plus the Soli radar gesture controls plus the Gemini-tuned learning is still the right premium pitch. Ecobee Smart Thermostat Premium stays second at $219 (down $30 at Ecobee), the built-in Alexa plus the SmartSensor support plus the dual-Zigbee + Thread radio is the right pitch for multi-room households. Amazon Smart Thermostat (3rd Gen) at third at $59 (down $20 at Amazon), the budget pick with Alexa integration is the right pitch for first-time smart-thermostat buyers. Mysa Smart Thermostat fourth at $129 (down $20), the electric-baseboard heating specific pitch is the right call for that buyer. Honeywell Home T9 fifth at $129 (down $20), the Honeywell legacy plus the geofencing is the right traditional brand pitch. Saturday verdict: Nest Learning for premium, Ecobee Premium for multi-room, Amazon Smart Thermostat for budget.",
    [
        {
            "title": "Nest Learning Thermostat 4th Gen at $229 — premium",
            "body": "Google held the $50 cut through Saturday. Matter-over-Thread plus the Soli radar gesture controls plus the Gemini-tuned learning at $229 is still the right premium pitch and the Gemini integration from the May firmware push improved the energy-saving learning curve."
        },
        {
            "title": "Ecobee Premium at $219 — multi-room pick",
            "body": "Ecobee held the $30 cut through Saturday. Built-in Alexa plus the SmartSensor support plus the dual-Zigbee + Thread radio at $219 is the right pitch for multi-room households that want per-room temperature management. The SmartSensor ecosystem is the differentiator."
        },
        {
            "title": "Amazon Smart Thermostat (3rd Gen) at $59 — budget",
            "body": "Amazon held the $20 cut through Saturday. The budget pick with Alexa integration at $59 is the right pitch for first-time smart-thermostat buyers and the basic geofencing plus the seasonal scheduling delivers the core savings without paying Nest or Ecobee premium."
        }
    ],
    "禮拜六早上，智慧溫控器榜單把禮拜五的折扣守過夜。\n\nGoogle Nest Learning Thermostat 4th Gen 守第一 NT$7,200（Google 砍 NT$1,570），Matter-over-Thread 加 Soli 雷達手勢加 Gemini 調校學習，還是高階話術。\n\nEcobee Smart Thermostat Premium 第二 NT$6,900（Ecobee 砍 NT$940），內建 Alexa 加 SmartSensor 支援加雙 Zigbee 加 Thread 射頻，是多房間話術。\n\n講真的，Amazon Smart Thermostat（3rd Gen）第三 NT$1,850（Amazon 砍 NT$620），預算選擇加 Alexa 整合是新手話術。Mysa Smart Thermostat 第四 NT$4,100（砍 NT$620），電熱踢腳板暖氣專用話術。Honeywell Home T9 第五 NT$4,100（砍 NT$620），Honeywell 傳統加地理圍欄是傳統品牌話術。\n\n禮拜六結論：高階就 Nest Learning，多房間就 Ecobee Premium，預算就 Amazon Smart Thermostat。",
    [
        {
            "title": "Nest Learning Thermostat 4th Gen NT$7,200 高階",
            "body": "Google 把 NT$1,570 折扣守進禮拜六。Matter-over-Thread 加 Soli 雷達手勢加 Gemini 調校學習 NT$7,200，還是高階話術，五月韌體 Gemini 整合改善節能學習曲線。"
        },
        {
            "title": "Ecobee Premium NT$6,900 多房間選擇",
            "body": "Ecobee 把 NT$940 折扣守進禮拜六。內建 Alexa 加 SmartSensor 支援加雙 Zigbee 加 Thread 射頻 NT$6,900，是要每房間溫度管理多房間家庭的話術。SmartSensor 生態是差異化。"
        },
        {
            "title": "Amazon Smart Thermostat（3rd Gen）NT$1,850 預算",
            "body": "Amazon 把 NT$620 折扣守進禮拜六。預算選擇加 Alexa 整合 NT$1,850 是新手話術，基本地理圍欄加季節排程交付核心省電，不必付 Nest 或 Ecobee 溢價。"
        }
    ],
)

add(
    "best-smart-pet-feeders",
    [MD_CNN, MD_NBC, MD_TECHRADAR],
    "Saturday morning the smart pet feeder chart held the Friday cuts. PetSafe Smart Feed 2.0 holds first at $169 (down $30), the wider portion-size programming plus the smartphone app plus the dual-cat support is still the right pitch for mainstream pet owners. WOPet Smart Feeder stays second at $129 (down $20), the 6L hopper plus the Alexa integration is the right pitch for larger pets. Petlibro Granary Camera Wi-Fi at third at $149 (down $30), the integrated camera plus the two-way audio plus the AI-driven feeding alerts is the right pitch for tech-loyal pet parents. Sure Petcare Microchip Feeder fourth at $179 (down $40), the microchip-restricted access is the right pitch for multi-pet households with diet conflicts. Whisker Feeder Robot 3 fifth at $399 (down $50), the smart-portion automation plus the dishwasher-safe bowls is the premium pitch. Saturday verdict: PetSafe Smart Feed 2.0 for mainstream, Petlibro Granary Camera for tech-savvy, Sure Petcare for multi-pet diet conflicts.",
    [
        {
            "title": "PetSafe Smart Feed 2.0 at $169 — mainstream pick",
            "body": "PetSafe held the $30 cut through Saturday. Wider portion-size programming plus the smartphone app plus the dual-cat support at $169 is still the right pitch for mainstream pet owners and the dual-cat support handles common multi-cat households."
        },
        {
            "title": "Petlibro Granary Camera Wi-Fi at $149 — tech-savvy pick",
            "body": "Petlibro held the $30 cut through Saturday. Integrated camera plus the two-way audio plus the AI-driven feeding alerts at $149 is the right pitch for tech-loyal pet parents who want to watch their pet eat from work."
        },
        {
            "title": "Sure Petcare Microchip Feeder at $179 — multi-pet pick",
            "body": "Sure Petcare held the $40 cut through Saturday. The microchip-restricted access at $179 is the right pitch for multi-pet households where one pet has dietary restrictions and another does not. The chip-recognition is the only meaningful solution in the category."
        }
    ],
    "禮拜六早上，智慧寵物餵食器榜單把禮拜五的折扣守過夜。\n\nPetSafe Smart Feed 2.0 守第一 NT$5,300（砍 NT$940），更廣的份量編程加手機 App 加雙貓支援，還是主流寵物主話術。\n\nWOPet Smart Feeder 第二 NT$4,100（砍 NT$620），6L 漏斗加 Alexa 整合是大型寵物話術。\n\n講真的，Petlibro Granary Camera Wi-Fi 第三 NT$4,700（砍 NT$940），整合攝影機加雙向音訊加 AI 餵食警報是科技派寵物家長話術。Sure Petcare Microchip Feeder 第四 NT$5,600（砍 NT$1,250），晶片限定存取是多寵物飲食衝突家庭話術。Whisker Feeder Robot 3 第五 NT$12,500（砍 NT$1,570），智慧份量自動化加洗碗機安全碗是高階話術。\n\n禮拜六結論：主流就 PetSafe Smart Feed 2.0，科技派就 Petlibro Granary Camera，多寵物飲食衝突就 Sure Petcare。",
    [
        {
            "title": "PetSafe Smart Feed 2.0 NT$5,300 主流選擇",
            "body": "PetSafe 把 NT$940 折扣守進禮拜六。更廣的份量編程加手機 App 加雙貓支援 NT$5,300，還是主流寵物主話術，雙貓支援處理常見多貓家庭。"
        },
        {
            "title": "Petlibro Granary Camera Wi-Fi NT$4,700 科技派",
            "body": "Petlibro 把 NT$940 折扣守進禮拜六。整合攝影機加雙向音訊加 AI 餵食警報 NT$4,700，是要從公司看寵物吃飯科技派寵物家長的話術。"
        },
        {
            "title": "Sure Petcare Microchip Feeder NT$5,600 多寵物",
            "body": "Sure Petcare 把 NT$1,250 折扣守進禮拜六。晶片限定存取 NT$5,600，是一隻寵物有飲食限制另一隻沒有多寵物家庭的話術。晶片識別是這品類唯一有意義解決方案。"
        }
    ],
)


# ---------- MOBILITY / CAMERAS ----------

add(
    "best-electric-bikes",
    [MD_CNN, MD_NBC, MD_TECHRADAR],
    "Saturday morning the e-bike chart held the Friday cuts. Specialized Turbo Vado SL 5.0 EQ holds first at $4,499 (down $500 at Specialized), the lightweight 33-lb frame plus the SL 1.2 motor plus the 80-mile range is still the right premium commuter pitch. Trek FX+ 2 stays second at $2,599 (down $400 at Trek), the city-tuned geometry plus the Bosch motor is the right mainstream pitch. Aventon Pace 500.3 at third at $1,299 (down $200), the value-premium pitch with longer range. Lectric XPedition 2.0 fourth at $1,499 (down $200), the cargo-class versatility is the right pitch for utility riders. Ride1Up Prodigy V2 fifth at $1,995 (down $300), the mid-drive at this price floor is the right pitch for value-premium buyers. Saturday verdict: Turbo Vado SL for premium commuter, FX+ 2 for mainstream, Lectric XPedition 2.0 for utility.",
    [
        {
            "title": "Turbo Vado SL 5.0 EQ at $4,499 — premium commuter",
            "body": "Specialized held the $500 cut through Saturday. The lightweight 33-lb frame plus the SL 1.2 motor plus the 80-mile range at $4,499 is still the right premium commuter pitch and the new April firmware push improved the motor torque curve."
        },
        {
            "title": "Trek FX+ 2 at $2,599 — mainstream city pick",
            "body": "Trek held the $400 cut through Saturday. The city-tuned geometry plus the Bosch motor plus the integrated lighting at $2,599 is the right mainstream pitch and Trek's dealer network is the differentiator over Specialized for buyers who want local service."
        },
        {
            "title": "Lectric XPedition 2.0 at $1,499 — utility pick",
            "body": "Lectric held the $200 cut through Saturday. The cargo-class versatility plus the 750W motor plus the long-range battery at $1,499 is the right pitch for utility riders who haul kids or groceries. The price floor is the strongest cargo-class value this year."
        }
    ],
    "禮拜六早上，電動腳踏車榜單把禮拜五的折扣守過夜。\n\nSpecialized Turbo Vado SL 5.0 EQ 守第一 NT$141,000（Specialized 砍 NT$15,700），輕量化 33 磅機架加 SL 1.2 馬達加 80 英里續航，還是高階通勤話術。\n\nTrek FX+ 2 第二 NT$81,700（Trek 砍 NT$12,500），城市調校幾何加 Bosch 馬達是主流話術。\n\n講真的，Aventon Pace 500.3 第三 NT$40,800（砍 NT$6,300），性價比高階加更長續航。Lectric XPedition 2.0 第四 NT$47,100（砍 NT$6,300），貨物級多用途是工具車騎士話術。Ride1Up Prodigy V2 第五 NT$62,700（砍 NT$9,400），這個價的中置馬達是性價比高階話術。\n\n禮拜六結論：高階通勤就 Turbo Vado SL，主流就 FX+ 2，工具就 Lectric XPedition 2.0。",
    [
        {
            "title": "Turbo Vado SL 5.0 EQ NT$141,000 高階通勤",
            "body": "Specialized 把 NT$15,700 折扣守進禮拜六。輕量化 33 磅機架加 SL 1.2 馬達加 80 英里續航 NT$141,000，還是高階通勤話術，四月新韌體推送改善馬達扭力曲線。"
        },
        {
            "title": "Trek FX+ 2 NT$81,700 主流城市選擇",
            "body": "Trek 把 NT$12,500 折扣守進禮拜六。城市調校幾何加 Bosch 馬達加整合燈組 NT$81,700，是主流話術，Trek 經銷網路就是比 Specialized 對要當地服務買家的差異化。"
        },
        {
            "title": "Lectric XPedition 2.0 NT$47,100 工具選擇",
            "body": "Lectric 把 NT$6,300 折扣守進禮拜六。貨物級多用途加 750W 馬達加長續航電池 NT$47,100，是載小孩或日用品工具車騎士的話術。這個地板價是今年貨物級最強性價比。"
        }
    ],
)

add(
    "best-electric-scooters",
    [MD_CNN, MD_NBC, MD_TECHRADAR],
    "Saturday morning the e-scooter chart held the Friday cuts. Segway Ninebot Max G3 holds first at $1,099 (down $200), the 40-mile range plus the dual-suspension plus the 350W motor is still the right commuter pitch. Niu KQi3 Pro stays second at $649 (down $150), the IP54 rating plus the 28-mile range plus the smartphone app integration is the right value pitch. Apollo City Pro at third at $1,399 (down $200), the dual-motor plus the off-road tires is the right pitch for hilly cities. Unagi Voyager fourth at $1,490 (down $200), the lightweight 28-lb foldable plus the dual-motor is the right pitch for urban commuters. NIU KQi 300P fifth at $899 (down $200), the long-range pitch at this floor. Saturday verdict: Ninebot Max G3 for mainstream commuter, NIU KQi3 Pro for value, Apollo City Pro for hilly.",
    [
        {
            "title": "Ninebot Max G3 at $1,099 — mainstream commuter",
            "body": "Segway held the $200 cut through Saturday. 40-mile range plus the dual-suspension plus the 350W motor at $1,099 is still the right commuter pitch and the May firmware push improved the regenerative braking response."
        },
        {
            "title": "Niu KQi3 Pro at $649 — value pick",
            "body": "Niu held the $150 cut through Saturday. IP54 rating plus the 28-mile range plus the smartphone app integration at $649 is the right value pitch and the price floor is $450 under the Ninebot Max G3 for similar core commute capability."
        },
        {
            "title": "Apollo City Pro at $1,399 — hilly-city pick",
            "body": "Apollo held the $200 cut through Saturday. Dual-motor plus the off-road tires plus the hill-climbing capability at $1,399 is the right pitch for hilly cities like San Francisco where the Ninebot Max G3 struggles. The dual-motor is the differentiator."
        }
    ],
    "禮拜六早上，電動滑板車榜單把禮拜五的折扣守過夜。\n\nSegway Ninebot Max G3 守第一 NT$34,500（砍 NT$6,300），40 英里續航加雙避震加 350W 馬達，還是通勤話術。\n\nNiu KQi3 Pro 第二 NT$20,400（砍 NT$4,700），IP54 防水加 28 英里續航加手機 App 整合，是值話術。\n\n講真的，Apollo City Pro 第三 NT$43,900（砍 NT$6,300），雙馬達加越野胎是丘陵城市話術。Unagi Voyager 第四 NT$46,800（砍 NT$6,300），輕量 28 磅可摺加雙馬達是都市通勤話術。NIU KQi 300P 第五 NT$28,300（砍 NT$6,300），這個價的長續航話術。\n\n禮拜六結論：主流通勤就 Ninebot Max G3，值就 NIU KQi3 Pro，丘陵就 Apollo City Pro。",
    [
        {
            "title": "Ninebot Max G3 NT$34,500 主流通勤",
            "body": "Segway 把 NT$6,300 折扣守進禮拜六。40 英里續航加雙避震加 350W 馬達 NT$34,500，還是通勤話術，五月韌體推送改善動能回收剎車反應。"
        },
        {
            "title": "Niu KQi3 Pro NT$20,400 值選擇",
            "body": "Niu 把 NT$4,700 折扣守進禮拜六。IP54 防水加 28 英里續航加手機 App 整合 NT$20,400，是值話術，地板價比 Ninebot Max G3 便宜 NT$14,100 通勤核心能力差不多。"
        },
        {
            "title": "Apollo City Pro NT$43,900 丘陵城市選擇",
            "body": "Apollo 把 NT$6,300 折扣守進禮拜六。雙馬達加越野胎加爬坡能力 NT$43,900，是 Ninebot Max G3 吃力的舊金山等丘陵城市話術。雙馬達是差異化。"
        }
    ],
)

add(
    "best-dash-cams",
    [MD_CNN, MD_NBC, MD_TECHRADAR],
    "Saturday morning the dash cam chart held the Friday cuts. Nextbase iQ holds first at $599 (down $100), the LTE-connected real-time alerts plus the dual-channel 4K + 1440p plus the parking surveillance mode is still the right premium pitch. Garmin Dash Cam Live stays second at $399 (down $100), the LTE connectivity plus the wider Garmin ecosystem is the right pitch for buyers in Garmin's GPS world. Vantrue N4 Pro at third at $349 (down $50), the three-channel coverage plus the 4K front + 2K rear is the right pitch for rideshare drivers. BlackVue DR970X-2CH fourth at $499 (down $100), the parking mode plus the cloud-connected services is the right Korean-brand pitch. Garmin Mini 2 fifth at $129 (down $30), the small form factor pitch. Saturday verdict: Nextbase iQ for premium LTE, Garmin Dash Cam Live for Garmin ecosystem, Vantrue N4 Pro for rideshare.",
    [
        {
            "title": "Nextbase iQ at $599 — premium LTE",
            "body": "Nextbase held the $100 cut through Saturday. LTE-connected real-time alerts plus the dual-channel 4K + 1440p plus the parking surveillance mode at $599 is still the right premium pitch and the iQ's LTE-driven alerts are the only category-leading approach."
        },
        {
            "title": "Garmin Dash Cam Live at $399 — Garmin ecosystem",
            "body": "Garmin held the $100 cut through Saturday. LTE connectivity plus the wider Garmin ecosystem at $399 is the right pitch for buyers already in Garmin's GPS world, and the Garmin Connect integration syncs alerts with the Garmin watch family."
        },
        {
            "title": "Vantrue N4 Pro at $349 — rideshare pick",
            "body": "Vantrue held the $50 cut through Saturday. Three-channel coverage plus the 4K front + 2K rear + interior at $349 is the right pitch for rideshare drivers and Uber Eats couriers who need legally defensible footage from every angle."
        }
    ],
    "禮拜六早上，行車紀錄器榜單把禮拜五的折扣守過夜。\n\nNextbase iQ 守第一 NT$18,800（砍 NT$3,140），LTE 連線即時警報加雙頻 4K 加 1440p 加停車監控模式，還是高階話術。\n\nGarmin Dash Cam Live 第二 NT$12,500（砍 NT$3,140），LTE 連線加更廣的 Garmin 生態是 Garmin GPS 世界買家話術。\n\n講真的，Vantrue N4 Pro 第三 NT$10,900（砍 NT$1,570），三頻覆蓋加 4K 前加 2K 後是 rideshare 駕駛話術。BlackVue DR970X-2CH 第四 NT$15,700（砍 NT$3,140），停車模式加雲端連線是韓國品牌話術。Garmin Mini 2 第五 NT$4,100（砍 NT$940），小版型話術。\n\n禮拜六結論：高階 LTE 就 Nextbase iQ，Garmin 生態就 Garmin Dash Cam Live，rideshare 就 Vantrue N4 Pro。",
    [
        {
            "title": "Nextbase iQ NT$18,800 高階 LTE",
            "body": "Nextbase 把 NT$3,140 折扣守進禮拜六。LTE 連線即時警報加雙頻 4K 加 1440p 加停車監控模式 NT$18,800，還是高階話術，iQ 的 LTE 驅動警報是這品類唯一領跑方式。"
        },
        {
            "title": "Garmin Dash Cam Live NT$12,500 Garmin 生態",
            "body": "Garmin 把 NT$3,140 折扣守進禮拜六。LTE 連線加更廣的 Garmin 生態 NT$12,500，是已經在 Garmin GPS 世界買家的話術，Garmin Connect 整合把警報跟 Garmin 手錶系列同步。"
        },
        {
            "title": "Vantrue N4 Pro NT$10,900 rideshare 選擇",
            "body": "Vantrue 把 NT$1,570 折扣守進禮拜六。三頻覆蓋加 4K 前加 2K 後加車內 NT$10,900，是要法律上可辯護全角度畫面的 rideshare 駕駛跟 Uber Eats 外送員話術。"
        }
    ],
)

add(
    "best-action-cameras",
    [MD_CNN, MD_NBC, MD_TECHRADAR],
    "Saturday morning the action camera chart held the Friday cuts. GoPro HERO13 Black holds first at $399 (down $100 at GoPro), the HyperSmooth 7.0 plus the 5.3K60 plus the modular HB-series lenses is still the right premium pitch. DJI Osmo Action 5 Pro stays second at $349 (down $50), the larger 1/1.3-inch sensor plus the 4K120 plus the magnetic mount is the right pitch for cinematic action work. Insta360 Ace Pro 2 at third at $399 (down $50), the Leica co-engineered lens plus the 8K30 plus the AI subject tracking is the right pitch for creators. GoPro HERO13 Mini fourth at $199 (down $50), the small-form-factor mainstream pitch. Akaso Brave 8 Lite fifth at $149 (down $30), the budget pick. Saturday verdict: HERO13 Black for premium GoPro, Osmo Action 5 Pro for cinematic, Ace Pro 2 for AI tracking.",
    [
        {
            "title": "HERO13 Black at $399 — premium GoPro buy",
            "body": "GoPro held the $100 cut through Saturday. HyperSmooth 7.0 plus the 5.3K60 plus the modular HB-series lenses at $399 is still the right premium GoPro pitch and the HB-series mount system is the differentiator over the previous generation."
        },
        {
            "title": "Osmo Action 5 Pro at $349 — cinematic pick",
            "body": "DJI held the $50 cut through Saturday. The larger 1/1.3\" sensor plus the 4K120 plus the magnetic mount at $349 is the right pitch for cinematic action work and the dual-OLED screens make framing dramatically easier than HERO13."
        },
        {
            "title": "Insta360 Ace Pro 2 at $399 — AI creator pick",
            "body": "Insta360 held the $50 cut through Saturday. Leica co-engineered lens plus the 8K30 plus the AI subject tracking at $399 is the right pitch for creators who want auto-cinematic framing without manual editing. The AI tracking is the differentiator."
        }
    ],
    "禮拜六早上，運動攝影機榜單把禮拜五的折扣守過夜。\n\nGoPro HERO13 Black 守第一 NT$12,500（GoPro 砍 NT$3,140），HyperSmooth 7.0 加 5.3K60 加模組化 HB 系列鏡頭，還是高階話術。\n\nDJI Osmo Action 5 Pro 第二 NT$10,900（砍 NT$1,570），更大的 1/1.3\" 感光元件加 4K120 加磁吸支架是電影感運動話術。\n\n講真的，Insta360 Ace Pro 2 第三 NT$12,500（砍 NT$1,570），徠卡聯合工程鏡頭加 8K30 加 AI 主體追蹤是創作者話術。GoPro HERO13 Mini 第四 NT$6,200（砍 NT$1,570），小版型主流話術。Akaso Brave 8 Lite 第五 NT$4,700（砍 NT$940），是預算選擇。\n\n禮拜六結論：高階 GoPro 就 HERO13 Black，電影感就 Osmo Action 5 Pro，AI 追蹤就 Ace Pro 2。",
    [
        {
            "title": "HERO13 Black NT$12,500 高階 GoPro 買點",
            "body": "GoPro 把 NT$3,140 折扣守進禮拜六。HyperSmooth 7.0 加 5.3K60 加模組化 HB 系列鏡頭 NT$12,500，還是高階 GoPro 話術，HB 系列支架系統就是比前代的差異化。"
        },
        {
            "title": "Osmo Action 5 Pro NT$10,900 電影感選擇",
            "body": "DJI 把 NT$1,570 折扣守進禮拜六。更大的 1/1.3\" 感光元件加 4K120 加磁吸支架 NT$10,900，是電影感運動話術，雙 OLED 螢幕讓構圖比 HERO13 顯著容易。"
        },
        {
            "title": "Insta360 Ace Pro 2 NT$12,500 AI 創作者",
            "body": "Insta360 把 NT$1,570 折扣守進禮拜六。徠卡聯合工程鏡頭加 8K30 加 AI 主體追蹤 NT$12,500，是要無手動編輯自動電影感構圖創作者的話術。AI 追蹤是差異化。"
        }
    ],
)

# ---------- MISC ----------

add(
    "best-3d-printers",
    [MD_CNN, MD_NBC, MD_TECHRADAR],
    "Saturday morning the 3D printer chart held the Friday cuts. Bambu Lab P1S Combo holds first at $799 (down $100), the AMS multi-color plus the CoreXY motion plus the auto-bed-leveling is still the right enthusiast pitch. Prusa MK4S stays second at $1,099 (down $100), the upgrade kit pathway plus the Prusa community plus the build quality is the right pitch for tinkerers. Bambu Lab A1 Mini Combo at third at $399 (down $50), the entry-level enthusiast plus the AMS Lite is the right pitch for first-timers. Anycubic Kobra 3 Combo fourth at $529 (down $70), the ACE Pro multi-color option plus the lower price floor is the right budget pitch. Creality K2 Plus fifth at $1,299 (down $200), the larger build volume is the right pitch for big-print buyers. Saturday verdict: P1S Combo for enthusiast, Prusa MK4S for tinkerer, A1 Mini Combo for first-timer.",
    [
        {
            "title": "Bambu Lab P1S Combo at $799 — enthusiast pick",
            "body": "Bambu Lab held the $100 cut through Saturday. AMS multi-color plus the CoreXY motion plus the auto-bed-leveling at $799 is still the right enthusiast pitch and the multi-color combo is the differentiator over Prusa for printing complex multi-material designs."
        },
        {
            "title": "Prusa MK4S at $1,099 — tinkerer pick",
            "body": "Prusa held the $100 cut through Saturday. The upgrade kit pathway plus the Prusa community plus the build quality at $1,099 is the right pitch for tinkerers who want long-term modular upgradability. The Prusa MK4S is the only major printer that ships a dedicated upgrade kit from the MK4."
        },
        {
            "title": "Bambu Lab A1 Mini Combo at $399 — first-timer pick",
            "body": "Bambu Lab held the $50 cut through Saturday. Entry-level enthusiast plus the AMS Lite at $399 is the right pitch for first-timers who want multi-color from day one without paying P1S premium. The smaller build volume is the only meaningful tradeoff."
        }
    ],
    "禮拜六早上，3D 印表機榜單把禮拜五的折扣守過夜。\n\nBambu Lab P1S Combo 守第一 NT$25,100（砍 NT$3,140），AMS 多色加 CoreXY 運動加自動床校平，還是發燒友話術。\n\nPrusa MK4S 第二 NT$34,500（砍 NT$3,140），升級套件路徑加 Prusa 社群加做工是改機派話術。\n\n講真的，Bambu Lab A1 Mini Combo 第三 NT$12,500（砍 NT$1,570），入門發燒友加 AMS Lite 是新手話術。Anycubic Kobra 3 Combo 第四 NT$16,600（砍 NT$2,200），ACE Pro 多色選項加更低價是預算話術。Creality K2 Plus 第五 NT$40,800（砍 NT$6,300），更大列印體積是大件話術。\n\n禮拜六結論：發燒友就 P1S Combo，改機就 Prusa MK4S，新手就 A1 Mini Combo。",
    [
        {
            "title": "Bambu Lab P1S Combo NT$25,100 發燒友選擇",
            "body": "Bambu Lab 把 NT$3,140 折扣守進禮拜六。AMS 多色加 CoreXY 運動加自動床校平 NT$25,100，還是發燒友話術，多色組合就是比 Prusa 對列印複雜多材質設計的差異化。"
        },
        {
            "title": "Prusa MK4S NT$34,500 改機派選擇",
            "body": "Prusa 把 NT$3,140 折扣守進禮拜六。升級套件路徑加 Prusa 社群加做工 NT$34,500，是要長期模組化升級改機派的話術。Prusa MK4S 是唯一從 MK4 出貨專用升級套件的主要印表機。"
        },
        {
            "title": "Bambu Lab A1 Mini Combo NT$12,500 新手選擇",
            "body": "Bambu Lab 把 NT$1,570 折扣守進禮拜六。入門發燒友加 AMS Lite NT$12,500，是要從第一天就有多色又不想付 P1S 溢價新手的話術。較小列印體積是唯一有意義權衡。"
        }
    ],
)

add(
    "best-portable-air-conditioners",
    [MD_HD, MD_CNN, MD_NBC],
    "Saturday morning the portable AC chart held the Friday cuts as summer demand drives MD weekend volume. Midea Duo MAP14HS1TBL holds first at $649 (down $150 at Home Depot), the dual-hose design plus the 14,000 BTU plus the inverter compressor is still the right premium pitch. LG ZeroBreeze LP1419IVSM stays second at $599 (down $100 at Home Depot), the inverter plus the smartphone app plus the quieter operation is the right LG-ecosystem pitch. Whynter ARC-14SH at third at $549 (down $100), the dual-hose plus the heater function is the right year-round pitch. Black+Decker BPACT14WT fourth at $399 (down $80), the single-hose budget pick. Frigidaire FHPC102AB1 fifth at $479 (down $100), the inverter at a cheaper floor. Saturday verdict: Midea Duo for premium dual-hose, LG ZeroBreeze for app-connected, Whynter ARC-14SH for year-round.",
    [
        {
            "title": "Midea Duo at $649 — premium dual-hose buy",
            "body": "Home Depot held the $150 cut through Saturday. Dual-hose design plus the 14,000 BTU plus the inverter compressor at $649 is still the right premium pitch and the dual-hose design is the only architecture that delivers quoted BTU performance in real rooms."
        },
        {
            "title": "LG ZeroBreeze LP1419IVSM at $599 — app-connected pick",
            "body": "Home Depot held the $100 cut on the LG through Saturday. The inverter plus the smartphone app plus the quieter operation at $599 is the right pitch for buyers who want quiet bedroom operation and Wi-Fi control. The Inverter compressor is the efficiency differentiator."
        },
        {
            "title": "Whynter ARC-14SH at $549 — year-round pick",
            "body": "Whynter held the $100 cut through Saturday. The dual-hose plus the heater function at $549 is the right year-round pitch for buyers who want one unit for both summer cooling and shoulder-season heating. The dual-function math holds even after the cut."
        }
    ],
    "禮拜六早上，攜帶式冷氣榜單把禮拜五的折扣守過夜，夏季需求帶動國殤日週末量。\n\nMidea Duo MAP14HS1TBL 守第一 NT$20,400（Home Depot 砍 NT$4,700），雙風管設計加 14,000 BTU 加變頻壓縮機，還是高階話術。\n\nLG ZeroBreeze LP1419IVSM 第二 NT$18,800（Home Depot 砍 NT$3,140），變頻加手機 App 加更安靜運作是 LG 生態話術。\n\n講真的，Whynter ARC-14SH 第三 NT$17,200（砍 NT$3,140），雙風管加暖氣功能是全年話術。Black+Decker BPACT14WT 第四 NT$12,500（砍 NT$2,500），單風管預算選擇。Frigidaire FHPC102AB1 第五 NT$15,000（砍 NT$3,140），便宜變頻地板價。\n\n禮拜六結論：高階雙風管就 Midea Duo，App 連線就 LG ZeroBreeze，全年就 Whynter ARC-14SH。",
    [
        {
            "title": "Midea Duo NT$20,400 高階雙風管買點",
            "body": "Home Depot 把 NT$4,700 折扣守進禮拜六。雙風管設計加 14,000 BTU 加變頻壓縮機 NT$20,400，還是高階話術，雙風管設計是唯一在實際房間交付標示 BTU 表現的架構。"
        },
        {
            "title": "LG ZeroBreeze LP1419IVSM NT$18,800 App 連線",
            "body": "Home Depot 把 LG 的 NT$3,140 折扣守進禮拜六。變頻加手機 App 加更安靜運作 NT$18,800，是要安靜臥室運作加 Wi-Fi 控制買家的話術。變頻壓縮機是效率差異化。"
        },
        {
            "title": "Whynter ARC-14SH NT$17,200 全年選擇",
            "body": "Whynter 把 NT$3,140 折扣守進禮拜六。雙風管加暖氣功能 NT$17,200，是想要一台搞定夏季冷卻跟過渡季暖氣買家的話術。雙功能算數折扣後還是站得住。"
        }
    ],
)

add(
    "best-portable-chargers",
    [MD_CNN, MD_NBC, MD_TECHRADAR],
    "Saturday morning the portable charger chart held the Friday cuts. Anker Prime 27,650 holds first at $149 (down $30 at Anker), the 250W output plus the smart display plus the dual USB-C is still the right premium pitch. Anker 737 Power Bank PowerCore 24K stays second at $129 (down $20), the 140W output plus the 24,000 mAh capacity is the right MacBook-Pro-friendly pitch. UGREEN Nexode Power Bank 25,000 mAh at third at $89 (down $20), the 200W output at this floor is the right value pitch. Anker 511 Power Bank (Nano Fold) fourth at $39 (down $10), the foldable AC-prong combo is the right travel pitch. Mophie Powerstation Pro AC fifth at $169 (down $30), the AC outlet pitch for laptop chargers. Saturday verdict: Anker Prime 27,650 for premium, UGREEN Nexode for value, Nano Fold for travel.",
    [
        {
            "title": "Anker Prime 27,650 at $149 — premium buy",
            "body": "Anker held the $30 cut through Saturday. 250W output plus the smart display plus the dual USB-C at $149 is still the right premium pitch and the smart display is the differentiator over the previous Prime generation for buyers who want real-time power tracking."
        },
        {
            "title": "UGREEN Nexode 25,000 mAh at $89 — value pick",
            "body": "UGREEN held the $20 cut through Saturday. 200W output at this floor at $89 is the right value pitch and the price is $60 under the Anker Prime equivalent for comparable wattage. The right call for buyers who want flagship-level output at budget pricing."
        },
        {
            "title": "Anker 511 Nano Fold at $39 — travel pick",
            "body": "Anker held the $10 cut through Saturday. The foldable AC-prong combo at $39 is the right travel pitch and the compact form factor plus the dual-function (AC wall charger + power bank) makes this the conviction buy for any traveler who hates carrying two devices."
        }
    ],
    "禮拜六早上，行動電源榜單把禮拜五的折扣守過夜。\n\nAnker Prime 27,650 守第一 NT$4,700（Anker 砍 NT$940），250W 輸出加智慧顯示加雙 USB-C，還是高階話術。\n\nAnker 737 Power Bank PowerCore 24K 第二 NT$4,100（砍 NT$620），140W 輸出加 24,000 mAh 容量是 MacBook Pro 友善話術。\n\n講真的，UGREEN Nexode Power Bank 25,000 mAh 第三 NT$2,800（砍 NT$620），這個價的 200W 輸出是值話術。Anker 511 Power Bank（Nano Fold）第四 NT$1,250（砍 NT$313），可摺 AC 插腳組合是旅行話術。Mophie Powerstation Pro AC 第五 NT$5,300（砍 NT$940），AC 插座給筆電充電器話術。\n\n禮拜六結論：高階就 Anker Prime 27,650，值就 UGREEN Nexode，旅行就 Nano Fold。",
    [
        {
            "title": "Anker Prime 27,650 NT$4,700 高階買點",
            "body": "Anker 把 NT$940 折扣守進禮拜六。250W 輸出加智慧顯示加雙 USB-C NT$4,700，還是高階話術，智慧顯示就是比前代 Prime 對要即時電量追蹤買家的差異化。"
        },
        {
            "title": "UGREEN Nexode 25,000 mAh NT$2,800 值選擇",
            "body": "UGREEN 把 NT$620 折扣守進禮拜六。這個價的 200W 輸出 NT$2,800 是值話術，價格比 Anker Prime 同瓦數便宜 NT$1,900。要旗艦級輸出加預算定價買家的選擇。"
        },
        {
            "title": "Anker 511 Nano Fold NT$1,250 旅行選擇",
            "body": "Anker 把 NT$313 折扣守進禮拜六。可摺 AC 插腳組合 NT$1,250 是旅行話術，緊湊版型加雙功能（AC 牆充加行動電源）是任何討厭帶兩個裝置旅人的有底氣買點。"
        }
    ],
)

add(
    "best-portable-power-stations",
    [MD_CNN, MD_NBC, {
        "title": "Jackery Memorial Day deals up to 59% off Explorer 2000 Plus",
        "url": "https://www.jackery.com/",
        "source": "Jackery",
    }],
    "Saturday morning the portable power station chart held the Friday cuts as Jackery and EcoFlow both extended through MD weekend. Jackery Explorer 2000 Plus holds first at $899 (down $1,300, or 59% off through May 27 per Jackery's MD page), the 2,000W output plus the 2,042 Wh LFP battery plus the solar-input flexibility is still the right premium pitch. EcoFlow DELTA 2 Max stays second at $899 (down $1,000, 53% off), the 2,400W output plus the 2,048 Wh capacity is the right rival pitch. Bluetti AC180 at third at $599 (down $300), the 1,800W output plus the AC fast-charge is the right value pitch. Anker Solix C1000 fourth at $649 (down $250), the smaller 1,056 Wh plus the lighter weight is the right portable pitch. Goal Zero Yeti 1500X fifth at $1,599 (down $300), the rugged build plus the App control is the right premium pick. Saturday verdict: Jackery Explorer 2000 Plus at $899 is the conviction buy of MD weekend in this category, EcoFlow DELTA 2 Max if you prefer EcoFlow, Bluetti AC180 for value.",
    [
        {
            "title": "Jackery Explorer 2000 Plus at $899 — MD buy of the weekend",
            "body": "Jackery held the 59% off floor through Saturday. 2,000W output plus the 2,042 Wh LFP battery plus solar-input flexibility at $899 is the buy of the weekend in this category and the $1,300 cut survives through May 27. This is the deepest discount Jackery has run all year."
        },
        {
            "title": "EcoFlow DELTA 2 Max at $899 — rival pick",
            "body": "EcoFlow held the 53% off floor through Saturday. 2,400W output plus the 2,048 Wh capacity at $899 matches Jackery on price floor and edges higher on raw output. The right call for buyers who prefer EcoFlow's faster recharge and modular battery expansion."
        },
        {
            "title": "Bluetti AC180 at $599 — value buy",
            "body": "Bluetti held the $300 cut through Saturday. 1,800W output plus the AC fast-charge at $599 is the right value pitch and the price floor is $300 under the Jackery and EcoFlow equivalents for slightly lower wattage. Right for budget-conscious campers."
        }
    ],
    "禮拜六早上，攜帶式發電站榜單把禮拜五折扣守過夜，Jackery 跟 EcoFlow 都延展國殤日週末。\n\nJackery Explorer 2000 Plus 守第一 NT$28,300（依 Jackery 國殤日頁面砍 NT$40,800，59% off 到 5/27），2,000W 輸出加 2,042 Wh LFP 電池加太陽能輸入彈性，還是高階話術。\n\nEcoFlow DELTA 2 Max 第二 NT$28,300（砍 NT$31,400，53% off），2,400W 輸出加 2,048 Wh 容量是對手話術。\n\n講真的，Bluetti AC180 第三 NT$18,800（砍 NT$9,400），1,800W 輸出加 AC 快充是值話術。Anker Solix C1000 第四 NT$20,400（砍 NT$7,800），較小 1,056 Wh 加更輕是攜帶話術。Goal Zero Yeti 1500X 第五 NT$50,300（砍 NT$9,400），堅固機身加 App 控制是高階話術。\n\n禮拜六結論：Jackery Explorer 2000 Plus NT$28,300 是這品類國殤日週末有底氣買點，喜歡 EcoFlow 就 DELTA 2 Max，值就 Bluetti AC180。",
    [
        {
            "title": "Jackery Explorer 2000 Plus NT$28,300 週末有底氣買點",
            "body": "Jackery 把 59% off 地板價守進禮拜六。2,000W 輸出加 2,042 Wh LFP 電池加太陽能輸入彈性 NT$28,300，是這品類週末買點，NT$40,800 折扣熬過 5/27。這是 Jackery 今年最深折扣。"
        },
        {
            "title": "EcoFlow DELTA 2 Max NT$28,300 對手選擇",
            "body": "EcoFlow 把 53% off 地板價守進禮拜六。2,400W 輸出加 2,048 Wh 容量 NT$28,300，地板價對齊 Jackery 但純輸出略勝。要 EcoFlow 更快充電跟模組化電池擴充買家的選擇。"
        },
        {
            "title": "Bluetti AC180 NT$18,800 值買點",
            "body": "Bluetti 把 NT$9,400 折扣守進禮拜六。1,800W 輸出加 AC 快充 NT$18,800 是值話術，地板價比 Jackery 跟 EcoFlow 同級便宜 NT$9,400 瓦數略低。預算露營派的選擇。"
        }
    ],
)

add(
    "best-vpn-services",
    [{
        "title": "Best VPN services 2026 Memorial Day deals",
        "url": "https://www.cnet.com/vpn/best-vpn/",
        "source": "CNET",
    }, {
        "title": "NordVPN Memorial Day 2026 sale",
        "url": "https://nordvpn.com/",
        "source": "NordVPN",
    }, {
        "title": "ExpressVPN deals May 2026",
        "url": "https://www.expressvpn.com/",
        "source": "ExpressVPN",
    }],
    "Saturday morning the VPN chart held the Friday cuts. NordVPN holds first at $3.39/mo (2-year plan, 73% off through MD), the Threat Protection Pro plus the Meshnet plus the wide server count is still the right premium pitch. ExpressVPN stays second at $4.99/mo (2-year plan, 61% off), the proprietary Lightway protocol plus the 105-country coverage is the right pitch for streaming-heavy users. Surfshark at third at $1.99/mo (24-month, 86% off), the unlimited device count plus the CleanWeb pitch is the right value-premium choice. Proton VPN fourth at $4.99/mo (2-year), the open-source plus the Switzerland jurisdiction is the right pitch for privacy-conscious buyers. Mullvad fifth at $5/mo flat, the no-account model plus the cash-payment option is the right pitch for maximum privacy. Saturday verdict: NordVPN for premium all-purpose, Surfshark for unlimited devices, Mullvad for maximum privacy.",
    [
        {
            "title": "NordVPN at $3.39/mo — premium all-purpose",
            "body": "NordVPN held the 73% off 2-year MD floor through Saturday. The Threat Protection Pro plus the Meshnet plus the wide server count at $3.39/mo is still the right premium all-purpose pitch and the Threat Protection Pro is the differentiator over Surfshark."
        },
        {
            "title": "Surfshark at $1.99/mo — unlimited devices",
            "body": "Surfshark held the 86% off floor through Saturday. The unlimited device count plus the CleanWeb pitch at $1.99/mo is the right value-premium choice and the unlimited device math beats NordVPN for households with many devices to cover."
        },
        {
            "title": "Mullvad at $5/mo flat — maximum privacy",
            "body": "Mullvad does not run holiday sales because the $5/mo flat is already the lowest sustained price in the category. The no-account model plus the cash-payment option at $5/mo is the right pitch for maximum privacy and the Switzerland-Sweden alliance jurisdiction is unbeatable."
        }
    ],
    "禮拜六早上，VPN 服務榜單把禮拜五的折扣守過夜。\n\nNordVPN 守第一 NT$106/月（2 年方案，國殤日 73% off），Threat Protection Pro 加 Meshnet 加廣大伺服器數，還是高階話術。\n\nExpressVPN 第二 NT$157/月（2 年方案，61% off），專有 Lightway 協定加 105 國覆蓋是串流重度用戶話術。\n\n講真的，Surfshark 第三 NT$63/月（24 個月，86% off），無上限裝置加 CleanWeb 是性價比高階選擇。Proton VPN 第四 NT$157/月（2 年），開源加瑞士司法管轄是隱私派話術。Mullvad 第五 NT$157/月固定，無帳號模式加現金付款選項是極限隱私話術。\n\n禮拜六結論：高階全用途就 NordVPN，無上限裝置就 Surfshark，極限隱私就 Mullvad。",
    [
        {
            "title": "NordVPN NT$106/月 高階全用途",
            "body": "NordVPN 把 73% off 2 年國殤日地板價守進禮拜六。Threat Protection Pro 加 Meshnet 加廣大伺服器數 NT$106/月，還是高階全用途話術，Threat Protection Pro 就是比 Surfshark 的差異化。"
        },
        {
            "title": "Surfshark NT$63/月 無上限裝置",
            "body": "Surfshark 把 86% off 地板價守進禮拜六。無上限裝置加 CleanWeb NT$63/月，是性價比高階選擇，無上限裝置算數對要涵蓋很多裝置家庭贏 NordVPN。"
        },
        {
            "title": "Mullvad NT$157/月 極限隱私",
            "body": "Mullvad 不打節慶折扣，因為 NT$157/月固定已經是這品類最低永久價。無帳號模式加現金付款選項 NT$157/月，是極限隱私話術，瑞士瑞典聯盟司法管轄無對手。"
        }
    ],
)

# ---------- MATTRESSES ----------

add(
    "best-mattresses",
    [MD_FOX, MD_AARP, MD_SLEEPF, MD_FORTUNE],
    "Saturday morning the mattress chart enters peak MD weekend volume because the four-day window is when mattress brands move the most inventory. Nectar held its 50% off floor plus 66% off bundles, Helix held 25% off the entire site, Saatva held up to $625 off, and Leesa held 30% off mattresses. Saatva Classic holds first at $1,395 queen (down $625 at Saatva direct), the dual-coil construction plus the lumbar support plus the white-glove delivery is still the right luxury hybrid pitch. Helix Midnight Luxe stays second at $1,649 queen (down $549 at 25% off site-wide), the zoned lumbar plus the cooling cover is the right side-sleeper hybrid pitch. Nectar Premier Copper at third at $1,099 queen (down $1,098 at 50% off plus 66% bundle), the copper-infused memory foam plus the year trial is the right memory foam pitch. Leesa Sapira Chill at fourth at $1,259 queen (down $539 at 30% off), the cooling hybrid pitch lands. Tuft & Needle Mint at fifth at $895 queen (down $254 at MD), the budget hybrid. Saturday verdict: Saatva Classic for luxury hybrid, Helix Midnight Luxe for side-sleeper hybrid, Nectar Premier Copper for memory foam — the conviction buys of MD weekend in this category.",
    [
        {
            "title": "Saatva Classic at $1,395 queen — luxury hybrid buy",
            "body": "Saatva direct held the $625 off MD floor through Saturday. Dual-coil construction plus the lumbar support plus the white-glove delivery at $1,395 queen is still the right luxury hybrid pitch and this is the deepest cut Saatva has run all year."
        },
        {
            "title": "Helix Midnight Luxe at $1,649 queen — side-sleeper hybrid",
            "body": "Helix held the 25% off site-wide MD floor through Saturday. Zoned lumbar plus the cooling cover plus the medium-firm feel at $1,649 queen is the right side-sleeper hybrid pitch and the price floor matches the best Helix has run since the last Black Friday."
        },
        {
            "title": "Nectar Premier Copper at $1,099 queen — memory foam buy",
            "body": "Nectar held the 50% off plus 66% bundle MD floor through Saturday. Copper-infused memory foam plus the year trial plus the lifetime warranty at $1,099 queen is the right memory foam pitch and the bundle math (mattress + foundation + pillows + sheets) is the strongest value in the category."
        }
    ],
    "禮拜六早上，床墊榜單進入國殤日週末顛峰量，因為四天窗口是床墊品牌出貨最多庫存的時候。Nectar 守住 50% off 加組合 66% off，Helix 全站 25% off，Saatva 砍最多 NT$19,600，Leesa 床墊 30% off。\n\nSaatva Classic 守第一 NT$43,800 queen（Saatva 直營砍 NT$19,600），雙線圈構造加腰部支撐加白手套配送，還是奢華混合話術。\n\nHelix Midnight Luxe 第二 NT$51,800 queen（全站 25% off 砍 NT$17,200），分區腰托加涼感套是側睡者混合話術。\n\n講真的，Nectar Premier Copper 第三 NT$34,500 queen（50% off 加 66% 組合砍 NT$34,500），銅纖維記憶棉加全年試睡是記憶棉話術。Leesa Sapira Chill 第四 NT$39,500 queen（30% off 砍 NT$16,900），涼感混合話術。Tuft & Needle Mint 第五 NT$28,100 queen（國殤日砍 NT$8,000），是預算混合。\n\n禮拜六結論：奢華混合就 Saatva Classic，側睡者混合就 Helix Midnight Luxe，記憶棉就 Nectar Premier Copper——這品類國殤日週末的有底氣買點。",
    [
        {
            "title": "Saatva Classic NT$43,800 queen 奢華混合買點",
            "body": "Saatva 直營把 NT$19,600 國殤日地板價守進禮拜六。雙線圈構造加腰部支撐加白手套配送 NT$43,800 queen，還是奢華混合話術，這是 Saatva 今年最深折扣。"
        },
        {
            "title": "Helix Midnight Luxe NT$51,800 queen 側睡者混合",
            "body": "Helix 把全站 25% off 國殤日地板價守進禮拜六。分區腰托加涼感套加中等偏硬手感 NT$51,800 queen，是側睡者混合話術，地板價對得起 Helix 上次黑五以來最佳價。"
        },
        {
            "title": "Nectar Premier Copper NT$34,500 queen 記憶棉",
            "body": "Nectar 把 50% off 加 66% 組合國殤日地板價守進禮拜六。銅纖維記憶棉加全年試睡加終身保固 NT$34,500 queen，是記憶棉話術，組合算數（床墊加床架加枕頭加床單）是這品類最強值。"
        }
    ],
)


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
