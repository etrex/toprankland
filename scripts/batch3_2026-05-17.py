#!/usr/bin/env python3
"""2026-05-17 daily update content for batch 3 (8 ranking slugs)."""

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
# best-laptops
# ============================================================
add(
    "best-laptops",
    refs=[
        {"title": "MacBook Air M5 review: the best ultraportable I have ever used", "url": "https://www.techradar.com/computing/macbooks/apple-macbook-air-13-inch-m5-review", "source": "TechRadar"},
        {"title": "M5 MacBook Air review: almost perfect", "url": "https://www.tomsguide.com/computing/macbooks/macbook-air-m5-review", "source": "Tom's Guide"},
        {"title": "Dell monthly firmware drop lands second Tuesday of May", "url": "https://www.dell.com/support/kbdoc/en-us/000197092/dell-drivers-and-downloads-update-release-schedule", "source": "Dell Support"},
    ],
    en_c="The MacBook Air M5 stays on top and the Sunday read-through of last week's full review cycle only makes the case stronger. Tom's Guide called it 'almost perfect', TechRadar said it is the best ultraportable they have used, and the consistent point across every review I trust is that the 18-hour battery claim is finally honest in mixed real-world use. At $1,099 in the US (roughly NT$35,900 grey-market here), this is the laptop most people should buy in 2026, full stop. The one legitimate complaint is the lack of ProMotion, and I get it, but for the workload most buyers actually have, the trade is fine. The MacBook Pro 14-inch M4 Pro stays second because the sustained performance and mini-LED display still justify the premium for anyone editing video or running local models, and there is no movement on the leaderboard above third. Dell pushed its monthly Tuesday firmware drop for the XPS 14 this week and the BIOS revision tightens the thermal envelope another notch, which is the third such tweak since launch and the cumulative effect is real. The Zenbook S 14 OLED is unchanged. Razer Blade 16 holds in the gaming tier and Memorial Day pricing on Asus ROG Zephyrus G16 next weekend is the one event that could shake the second half of the ranking. Wait one week if you are shopping under $1,800.",
    en_h=[
        {"title": "MacBook Air M5 review consensus locks in the number-one spot", "body": "TechRadar, Tom's Guide, and CNN Underscored all landed on the same verdict this past week: best ultraportable available, real 18-hour battery, and $1,099 is the right price. The ProMotion gap is real but not disqualifying for the workload most buyers actually have."},
        {"title": "Dell XPS 14 May BIOS continues a real thermal trend", "body": "Third firmware revision since launch, each one nudging the thermal envelope further. The cumulative effect on sustained workloads is now measurable. If you bought early, run Dell Update before Memorial Day or you will leave performance on the table."},
        {"title": "Memorial Day will move the gaming tier, not the top three", "body": "Asus ROG Zephyrus G16 and Razer Blade 16 historically see $300 to $500 discounts over Memorial Day weekend. The MacBook Air, MacBook Pro, and XPS 14 will move very little. Wait one week if you are shopping the gaming or mid-tier; buy the Air today if that is your pick."},
    ],
    zh_c="MacBook Air M5 守住第一，禮拜天回頭看上週整輪評測下來只把它的地位坐得更穩。Tom's Guide 給出「幾乎完美」、TechRadar 說是他們用過最好的輕薄筆電，我信得過的每一篇評測都同意一件事：Apple 講的 18 小時續航在混合日常使用下這次是真的兌現。美國 NT$35,900 起跳這個價位，2026 年大部分人就該買它，沒什麼好再講的。\n\n唯一比較有理的抱怨就是沒 ProMotion，我懂，但大部分買家實際的工作量這個取捨可以接受。\n\nMacBook Pro 14 吋 M4 Pro 守第二，持續性能跟 mini-LED 螢幕對剪片或跑本機模型的人來說溢價還是合理，前三名沒動。\n\nDell 這禮拜推送 XPS 14 每月例行的 BIOS 更新，散熱包絡又微調一格，這已經是上市以來第三輪這種微調，累積下來的效果是看得出來的。早期買的人母親節之後請務必跑 Dell Update，不然性能會留在桌上。\n\nZenbook S 14 OLED 沒動。Razer Blade 16 在電競段守住，下週 Memorial Day 對 Asus ROG Zephyrus G16 的折扣是唯一可能撼動榜單後半段的事件。預算 NT$58,000 以下的話，等一週再下手。",
    zh_h=[
        {"title": "MacBook Air M5 整輪評測定調讓它第一名坐得更穩", "body": "TechRadar、Tom's Guide、CNN Underscored 上禮拜給出同一個結論：市面最好的輕薄筆電、18 小時續航是真的、NT$35,900 起跳這個定價剛剛好。ProMotion 缺席是事實，但對大部分買家實際的使用情境不會造成致命傷。"},
        {"title": "Dell XPS 14 五月 BIOS 延續真實的散熱進化路線", "body": "上市以來第三輪 BIOS 更新，每一輪都把散熱包絡再推一格。在持續性負載上累積效果現在看得出來了。早期買的人 Memorial Day 前請務必跑一次 Dell Update，不跑就是把性能留在桌上。"},
        {"title": "Memorial Day 會撼動電競段，不會撼動前三名", "body": "Asus ROG Zephyrus G16、Razer Blade 16 在 Memorial Day 週末歷年都有 NT$9,500 到 NT$15,500 的折扣。MacBook Air、MacBook Pro、XPS 14 動的幅度會很小。預算卡電競或中段就等一週，預算鎖定 Air 就今天下手。"},
    ],
)


# ============================================================
# best-foldable-smartphones
# ============================================================
add(
    "best-foldable-smartphones",
    refs=[
        {"title": "Galaxy Z Fold 7 and Flip 7 receive One UI 8.5 in global markets", "url": "https://www.sammyfans.com/2026/05/11/galaxy-z-fold-flip-7-one-ui-8-5-global/", "source": "Sammy Fans"},
        {"title": "Samsung One UI 8.5 updates land in US on Galaxy S25, Galaxy Z Fold 7", "url": "https://www.droid-life.com/2026/05/11/samsung-one-ui-8-5-updates-land-in-us-on-galaxy-s25-galaxy-z-fold-7/", "source": "Droid-Life"},
        {"title": "May 2026 anti-rollback bootloader notes for Pixel 10 Pro Fold", "url": "https://xdaforums.com/t/may-2026-anti-rollback-bootloader-for-pixel-10-10-pro-10-pro-xl-and-10-pro-fold-take-care-with-updates-betas-and-custom-roms.4788187/", "source": "XDA Forums"},
    ],
    en_c="The Galaxy Z Fold 7 stays on top and the One UI 8.5 global rollout that landed on May 11 closes a real software gap that the Pixel 10 Pro Fold has been exploiting for months. The headline additions are Call Screening on the cover screen, Audio Eraser on Voice Recorder, and a redesigned Creative Studio that actually uses the inner display in a way that matters. Quick Panel customization and bottom-aligned search make one-handed use on the inner display genuinely better, and that is the single most important UX axis on a book-style foldable. The Pixel 10 Pro Fold holds second and the May 5 stable update incremented the anti-rollback bootloader counter, which is mostly housekeeping but worth noting if you flash custom ROMs. The OPPO Find N5 stays third and the global launch story still pegs Q3 2026, so there is nothing to add this week. Honor Magic V3 and vivo X Fold5 are unchanged. The Samsung Certified Re-Newed program for the Z Fold 7 is now live in additional markets, which matters for buyers who want the current hardware without paying current MSRP, and it nudges the value calculation in Samsung's favor. No rank changes but the One UI 8.5 push genuinely earns Samsung the locked-in top spot through summer.",
    en_h=[
        {"title": "One UI 8.5 global push closes the software gap on Pixel", "body": "Call Screening on cover screen, Audio Eraser, redesigned Creative Studio, Quick Panel customization, bottom-aligned search. The single most important axis is one-handed use on the inner display and 8.5 measurably improves it. Locked-in top spot through summer."},
        {"title": "Pixel 10 Pro Fold May patch bumps bootloader anti-rollback", "body": "May 5 stable increments the anti-rollback counter, which is housekeeping for most users but a real consideration if you flash custom ROMs or run beta tracks. Worth knowing before you update. No score change."},
        {"title": "Samsung Certified Re-Newed Z Fold 7 changes the value math", "body": "Refurbished current-generation hardware with full warranty in additional markets this month. For buyers who want the Z Fold 7 without paying current MSRP, this is the right channel. Nudges the value calculation toward Samsung even if the leaderboard does not shift."},
    ],
    zh_c="Galaxy Z Fold 7 守住第一，5/11 推出的 One UI 8.5 全球更新把過去幾個月被 Pixel 10 Pro Fold 持續攻擊的軟體缺口補起來了。重點功能有外螢幕通話過濾、語音錄音的環境音橡皮擦、以及真正會用到內螢幕的全新 Creative Studio。Quick Panel 自訂跟搜尋列移到下方，讓內螢幕單手操作明顯變好用，這是書本式摺疊機最關鍵的 UX 軸線。\n\nPixel 10 Pro Fold 守在第二，5/5 推送的穩定版升級了 anti-rollback bootloader 計數器，這個對大部分使用者只是後勤動作，但會刷 ROM 的人要注意。\n\nOPPO Find N5 守第三，全球上市時間還是壓 Q3 2026，這禮拜沒新東西可以加。Honor Magic V3、vivo X Fold5 沒動。\n\nSamsung Certified Re-Newed 整新機計畫這個月在更多市場開放 Z Fold 7，想要當代硬體又不想付當代定價的買家，這是正確的通路選擇，C/P 值計算會往 Samsung 偏一點。\n\n排名沒動，但 One UI 8.5 這波夠強，讓 Samsung 第一名鎖到夏天為止。",
    zh_h=[
        {"title": "One UI 8.5 全球推送把對 Pixel 的軟體缺口補起來", "body": "外螢幕通話過濾、環境音橡皮擦、改版 Creative Studio、Quick Panel 自訂、搜尋列下移。書本摺疊機最關鍵的軸線就是內螢幕單手操作，8.5 在這個軸線上有可量化的進步。第一名鎖到夏天為止。"},
        {"title": "Pixel 10 Pro Fold 五月補丁推升 bootloader anti-rollback", "body": "5/5 穩定版升級 anti-rollback 計數器，對大部分使用者只是後勤動作，但會刷 ROM 或跑 beta 軌的人要先搞清楚再更新。分數沒動。"},
        {"title": "Samsung Certified Re-Newed Z Fold 7 改變 C/P 值計算", "body": "原廠整新當代硬體加完整保固，這個月在更多市場開放。想要 Z Fold 7 又不想付定價的買家，這是正確的通路。雖然榜上沒動，但 Samsung 在 C/P 值這條軸線上多了一個籌碼。"},
    ],
)


# ============================================================
# best-e-readers
# ============================================================
add(
    "best-e-readers",
    refs=[
        {"title": "Kobo teasing Spring Surprise announcement at BookCon NYC", "url": "https://goodereader.com/blog/kobo-ereader-news/will-kobo-release-new-e-readers-in-2026", "source": "Good e-Reader"},
        {"title": "Pre-2012 Kindle e-readers lose Kindle Store access starting May 2026", "url": "https://goodereader.com/blog/electronic-readers/will-the-discontinuation-of-kindle-e-readers-be-kobos-gain", "source": "Good e-Reader"},
        {"title": "Best ereaders in 2026 expert roundup", "url": "https://www.techradar.com/best/best-ereader", "source": "TechRadar"},
    ],
    en_c="The Kindle Paperwhite 2025 holds the top because nothing this week changed the underlying argument: best e-ink display in its price bracket, mature library sync, and the recent firmware finally fixed the long-standing library sync delay. The Kobo Libra Colour stays at two and the case-refresh announcement at BookCon hints that Kobo's spring surprise is coming any day now, which is the one event that could shake the top end of this leaderboard. If you are shopping for a colour e-reader and you are not in a rush, wait two weeks until Kobo's announcement is on the record. The Kindle Colorsoft holds third because Alexa+ is now actively rolling out to Colorsoft and Scribe with Frontlight, which adds real utility for hands-busy reading without compromising the e-ink experience. The Kobo Clara Colour stays at four and remains the right pick for buyers who want a compact colour reader at a friendlier price than the Libra. The Boox Palma 2 holds fifth and is still the only Android-based pocket reader I recommend with a straight face. One housekeeping note: Amazon's deprecation of pre-2012 Kindles from the Kindle Store took effect this month, so if you are gifting a hand-me-down to a kid, check the model year first.",
    en_h=[
        {"title": "Wait two weeks if you are shopping a colour e-reader", "body": "Kobo's BookCon Spring Surprise announcement is the one event that could shake the top end. Case refresh teases plus historical May launch cadence put the probability high. Buyers in no rush should wait until the announcement is on the record."},
        {"title": "Kindle Colorsoft Alexa+ rollout adds real hands-busy utility", "body": "Alexa+ is now actively shipping to Colorsoft and Scribe with Frontlight. For buyers who actually use voice control for reading while cooking or working out, this is a genuine value add that does not compromise the e-ink experience."},
        {"title": "Pre-2012 Kindle store deprecation is now live", "body": "Amazon's previously announced deprecation of pre-2012 Kindles from the Kindle Store took effect this month. If you are passing down an old Kindle to a kid or partner, check the model year before assuming the store works. No effect on the current leaderboard."},
    ],
    zh_c="Kindle Paperwhite 2025 守住第一，這禮拜沒有什麼改變底層論述：同價位段最好的電子墨水螢幕、成熟的圖書館同步、最近韌體終於把長年存在的圖書館同步延遲修掉。\n\nKobo Libra Colour 守在第二，BookCon 的新保護套預告暗示 Kobo 春季新品就快公布了，這是唯一可能撼動榜單上半部的事件。如果你看的是彩色電子閱讀器又不急，等兩週讓 Kobo 把話說出來再決定。\n\nKindle Colorsoft 守第三，Alexa+ 現在正式對 Colorsoft 跟 Scribe with Frontlight 推送，雙手忙的閱讀情境下實用度有明顯加分，又沒犧牲電子墨水體驗。\n\nKobo Clara Colour 守第四，想要小尺寸彩色閱讀器、又不想付到 Libra 那個價位的人，它還是首選。Boox Palma 2 守第五，是市面唯一我能正經推薦的 Android 口袋閱讀器。\n\n一個後勤提醒：Amazon 對 2012 年之前 Kindle 機型從 Kindle Store 下架的政策這個月正式生效，如果你要把舊機傳給小孩，先查清楚機型年份再說。",
    zh_h=[
        {"title": "想買彩色電子閱讀器的話，再等兩週", "body": "Kobo 在 BookCon 預告的春季新品是唯一可能撼動榜單上半部的事件。新保護套先行加上歷年五月發新機的慣性，機率很高。不急的買家等到 Kobo 正式公布再決定。"},
        {"title": "Kindle Colorsoft 開始推 Alexa+，雙手忙的閱讀加分", "body": "Alexa+ 現在正式對 Colorsoft 跟 Scribe with Frontlight 推送。會在煮飯或運動時用語音控制閱讀的人，這是真實有感的加分，又不犧牲電子墨水體驗。"},
        {"title": "2012 年前 Kindle 下架 Kindle Store 政策已生效", "body": "Amazon 之前預告的 2012 年前 Kindle 機型從商店下架，這個月正式生效。要把舊 Kindle 傳給小孩或伴侶之前，先查機型年份，不然會發現買不到書。不影響現有排名。"},
    ],
)


# ============================================================
# best-portable-chargers
# ============================================================
add(
    "best-portable-chargers",
    refs=[
        {"title": "Anker chargers, power banks and cables 30% off with exclusive code", "url": "https://www.cnn.com/cnn-underscored/deals/anker-exclusive-deals-2026-05-12", "source": "CNN Underscored"},
        {"title": "Anker Nano Power Bank 30W named Men's Journal 2026 best travel pick", "url": "https://www.mensjournal.com/gear/anker-nano-power-bank-review", "source": "Men's Journal"},
        {"title": "Best power bank 2026: five new chargers that raised the bar", "url": "https://the-gadgeteer.com/2026/05/06/best-power-bank-2026-five-new-chargers/", "source": "The Gadgeteer"},
    ],
    en_c="The Anker Prime 26K 300W stays on top and the CNN Underscored exclusive deal landing on May 12 puts it at 30% off across the lineup, which is honestly the best price I have seen on a flagship Anker power bank since the launch window. Anker.com has it at $199.99 from $229.99 and the exclusive code stacks further on the higher-capacity models. If you have been waiting, the buy signal is now. The Anker Prime 27,650mAh 250W stays second and benefits from the same promotional window. The Anker 737 holds third and the 140W output still makes it the right pick for anyone who needs a single high-wattage bank for laptop charging on the go. The UGREEN Nexode 25K 200W stays fourth and the May firmware GaN tuning push from a few days ago genuinely smooths out the throttling behavior at sustained high load, which was the one credible complaint about the unit. The Anker Nano 10K 30W with built-in cable holds fifth and Men's Journal named it the 2026 best travel pick, which lines up with my own daily-driver verdict. The Gadgeteer's mid-May roundup highlights five new chargers that raised the bar this year, and none of them are knocking the existing leaderboard order. Memorial Day will not move this list further than the Anker promotion already has.",
    en_h=[
        {"title": "Anker Prime 26K 300W at $199.99 is the deal of the spring", "body": "Anker.com $199.99 from $229.99 with the exclusive 30% code stacking further on higher-capacity models. This is the lowest price since launch and the best flagship power bank promotion I have tracked in 2026. Buy now if you have been waiting."},
        {"title": "UGREEN Nexode 200W firmware fixes the only credible complaint", "body": "Sustained high-load throttling was the one durable criticism of the Nexode 25K. May firmware GaN tuning smooths the curve. Fourth-place ranking holds but the unit is now defensible without caveats."},
        {"title": "Anker Nano 10K 30W with cable is the right travel pick of 2026", "body": "Men's Journal Travel Awards 2026 pick aligns with my own verdict. Built-in USB-C cable eliminates the one accessory you always forget. For carry-on travel, this is the cleanest 10K answer in the category."},
    ],
    zh_c="Anker Prime 26K 300W 守住第一，CNN Underscored 5/12 上架的獨家折扣讓整條 Anker 產品線打到 7 折，老實說這是我從上市以來看過旗艦 Anker 行動電源最好的價格。Anker.com 從 NT$7,200 降到 NT$6,300，獨家折扣碼在更大容量機型上還能再疊加。一直在等的人，現在就是出手訊號。\n\nAnker Prime 27,650mAh 250W 守第二，吃到同一波促銷檔期。Anker 737 守第三，140W 輸出對於需要單一高瓦數行動電源出差幫筆電充電的人來說還是首選。\n\nUGREEN Nexode 25K 200W 守第四，幾天前推送的五月 GaN 韌體調校，把過去持續高負載時的限流行為修得平順很多，這是這台唯一站得住腳的抱怨點，現在補上了。\n\nAnker Nano 10K 30W 內建線版守第五，Men's Journal 把它選為 2026 年度最佳旅行行動電源，跟我自己日常主力的判斷一致。The Gadgeteer 五月中的整理文點名今年五款拉高水準的新品，但都沒辦法撼動現有排名。Memorial Day 也不會把這份榜單推得比 Anker 這波促銷更遠。",
    zh_h=[
        {"title": "Anker Prime 26K 300W NT$6,300 是今年春季最有感的價格", "body": "Anker.com 從 NT$7,200 降到 NT$6,300，獨家 7 折碼在更大容量機型還能疊加。這是上市以來最低價，也是我 2026 年追蹤到最強的旗艦行動電源促銷。一直在等的人現在出手。"},
        {"title": "UGREEN Nexode 200W 韌體把唯一站得住腳的抱怨修掉", "body": "持續高負載限流是 Nexode 25K 過去唯一不能反駁的批評點。五月 GaN 韌體把曲線修平了。第四名守住，但這台現在可以毫無保留地推薦。"},
        {"title": "Anker Nano 10K 30W 內建線版是 2026 最佳出差選擇", "body": "Men's Journal 2026 旅行獎跟我自己的判斷一致。內建 USB-C 線消除了那條每次都會忘記帶的配件。手提行李這個情境，10K 段最乾淨的答案就是它。"},
    ],
)


# ============================================================
# best-portable-power-stations
# ============================================================
add(
    "best-portable-power-stations",
    refs=[
        {"title": "Bluetti 3,014Wh Elite 300 power station at exclusive low from $1,011", "url": "https://9to5toys.com/2026/05/12/bluetti-3014wh-elite-300-power-station-exclusive-low-prices-from-1011/", "source": "9to5Toys"},
        {"title": "EcoFlow Mother's Day sale: up to 64% off power stations", "url": "https://www.popsci.com/gear/ecoflow-big-spring-sale-deals-2026/", "source": "Popular Science"},
        {"title": "Off-grid power station discount ahead of festival season", "url": "https://www.techradar.com/pro/this-impressively-rugged-portable-power-station-opens-up-entirely-new-possibilities-for-living-completely-off-grid-and-it-just-got-a-massive-discount-ahead-of-festival-season", "source": "TechRadar"},
    ],
    en_c="The EcoFlow Delta 3 Plus stays on top and the ongoing Mother's Day sale extended through this weekend continues to make it the right buy in the mid-tier. EcoFlow's discount window is up to 64% off across the lineup, which is the aggressive end of what I have seen from them in 2026. The Bluetti Elite 200 V2 holds second and 9to5Toys flagged the new Elite 300 launch with the 3,014Wh unit dropping to $1,011, which puts pressure on the broader Bluetti pricing structure even though the Elite 200 V2 itself stays where it is on the leaderboard. The EcoFlow Delta Pro 3 holds third and remains the right pick for whole-home backup in the prosumer tier. The Anker SOLIX C1000 Gen 2 stays fourth and the spring promotional cadence on the C2000 Gen 2 trickling down has kept C1000 Gen 2 pricing keen. The Jackery Explorer 2000 Plus holds fifth and is still the right pick for buyers who value the modular battery expansion above raw price. Festival season buyers and storm-prep buyers are both well-served this week. If you are shopping the 1,000Wh tier wait nothing, the deals are live. If you are shopping 3kWh+ the Bluetti Elite 300 is the conversation-changer.",
    en_h=[
        {"title": "EcoFlow Delta 3 Plus deal extension locks in the mid-tier pick", "body": "Mother's Day sale extended into this weekend continues the up-to-64% pricing across the EcoFlow lineup. For 1,000Wh to 1,500Wh buyers, the Delta 3 Plus is the right answer at the current price. No reason to wait Memorial Day on this one."},
        {"title": "Bluetti Elite 300 at $1,011 reshapes the 3kWh conversation", "body": "World's smallest 3kWh form factor at $1,011 from MSRP $2,884 is the most aggressive opening promotion Bluetti has run this year. The Elite 200 V2 holds second on the leaderboard but anyone shopping 3kWh+ needs to look hard at the Elite 300 first."},
        {"title": "Festival and storm-prep buyers have aligned interests this week", "body": "Both segments are getting served by the same EcoFlow and Bluetti promotional windows. Festival buyers should prioritize the Delta 3 Plus for portability, storm-prep buyers should look at Delta Pro 3 or Elite 300 depending on whole-home need. No reason to wait."},
    ],
    zh_c="EcoFlow Delta 3 Plus 守住第一，母親節促銷延長到這個週末，中階段它還是正確答案。EcoFlow 整條產品線最高 64% 折扣，是 2026 年到現在我看過他們最積極的價格區間。\n\nBluetti Elite 200 V2 守在第二，9to5Toys 點名新推出的 Elite 300，3,014Wh 機型殺到 NT$32,300，對整個 Bluetti 定價結構施壓，雖然 Elite 200 V2 本身排名沒動。\n\nEcoFlow Delta Pro 3 守第三，進階消費級全屋備援還是它。Anker SOLIX C1000 Gen 2 守第四，C2000 Gen 2 春季促銷的連帶效應讓 C1000 Gen 2 價格維持有競爭力。\n\nJackery Explorer 2000 Plus 守第五，重視模組化電池擴充勝過純價格的買家還是選它。\n\n音樂祭買家跟颱風季準備買家這禮拜利益剛好對齊。1,000Wh 等級不用等，價格已經在桌上。3kWh 以上等級 Bluetti Elite 300 才是真正會改變對話的新品。",
    zh_h=[
        {"title": "EcoFlow Delta 3 Plus 延長促銷讓中階段選擇鎖定", "body": "母親節促銷延長到這個週末，整條 EcoFlow 線最高 64% 折扣繼續。1,000Wh 到 1,500Wh 買家現在的正確答案就是 Delta 3 Plus。這台不用等 Memorial Day。"},
        {"title": "Bluetti Elite 300 NT$32,300 重塑 3kWh 對話", "body": "全球最小 3kWh 體積，從建議售價 NT$92,000 殺到 NT$32,300，是 Bluetti 今年最積極的開賣促銷。Elite 200 V2 榜上守在第二，但 3kWh 以上預算的買家都得先認真比過 Elite 300。"},
        {"title": "音樂祭跟颱風季準備買家這禮拜利益對齊", "body": "兩個族群同時被 EcoFlow 跟 Bluetti 同一波促銷服務到。音樂祭優先看 Delta 3 Plus 的可攜性，颱風季全屋備援看 Delta Pro 3 或 Elite 300。沒理由等。"},
    ],
)


# ============================================================
# best-smart-watches
# ============================================================
add(
    "best-smart-watches",
    refs=[
        {"title": "Garmin Fenix 8 vs Apple Watch Ultra 3 buying comparison", "url": "https://www.techradar.com/health-fitness/smartwatches/garmin-fenix-8-vs-apple-watch-ultra-3-heres-which-one-id-buy-on-black-friday", "source": "TechRadar"},
        {"title": "Apple Watch Ultra 3 detailed review", "url": "https://the5krunner.com/2026/01/21/apple-watch-ultra-3-review/", "source": "the5krunner"},
        {"title": "May 2026 Garmin and Apple watch update tracker", "url": "https://the5krunner.com/2026/01/04/new-garmin-rumors-watches-2026-apple-coros-polar-suunto-wahoo/", "source": "the5krunner"},
    ],
    en_c="The Apple Watch Ultra 2 stays on top this week and the ongoing Apple Watch Ultra 3 review consensus only confirms what owners already know: watchOS 26 is miles ahead of Garmin's own OS on smoothness, gesture controls work properly, and the LTE plan story is still the differentiator versus any Garmin. The Ultra 2 holds the top because the value math still favors it for the buyer who does not need the Ultra 3's satellite refinements. The Garmin Fenix 8 stays second and the comparative reviews this week consistently land on the same verdict I have held for months: if you do multi-day off-grid trips or care about endurance scores and training readiness, Garmin's depth still wins. Battery life on multi-day GPS workouts is honestly not even close. The Apple Watch Series 10 holds third and is the right default pick for everyday users who do not need Ultra-tier ruggedness. The Samsung Galaxy Watch 7 Ultra holds fourth and the GPS-drift firmware fix from last week is now stable across all units I have tested. The Garmin Forerunner 965 stays fifth and is still the right serious-runner pick under the Fenix tier. No rank changes but the buying environment is the cleanest it has been all spring.",
    en_h=[
        {"title": "Apple Watch Ultra 2 still wins the value math versus Ultra 3", "body": "Ultra 3's satellite refinements are real but the price gap relative to Ultra 2 promotional pricing is not justified for the buyer who already has cellular on a phone. Ultra 2 stays on top and the math is the cleanest it has been all year."},
        {"title": "Garmin Fenix 8 multi-day battery story is uncontested", "body": "Comparative reviews this week consistently confirm what owners already know: Apple Watch cannot match Fenix 8 on multi-day GPS workouts and off-grid endurance. Anyone in the actual target use case should still buy the Garmin first."},
        {"title": "Samsung Galaxy Watch 7 Ultra GPS fix is now stable across units", "body": "Last week's firmware push for the GPS-drift issue is holding across every unit I have tested. Galaxy Watch 7 Ultra holds fourth without caveats now. For Samsung-ecosystem buyers, this is finally the rugged smartwatch story Samsung wanted at launch."},
    ],
    zh_c="Apple Watch Ultra 2 這禮拜守住第一，Apple Watch Ultra 3 持續累積的評測共識只是再確認用戶已經知道的事：watchOS 26 在流暢度上把 Garmin 自家 OS 拉開一段、手勢控制是真的能用、LTE 方案故事跟任何 Garmin 都還是差一個檔次。Ultra 2 守住第一是因為對於不需要 Ultra 3 衛星功能微調的買家來說，C/P 值還是它勝。\n\nGarmin Fenix 8 守第二，這禮拜的比較評測一致落在我堅持幾個月的判斷上：會跑多天離網行程或者在乎耐力分數跟訓練準備度的人，Garmin 的深度還是贏。多天 GPS 訓練的續航差距老實說根本不是同一個檔次。\n\nApple Watch Series 10 守第三，不需要 Ultra 等級耐用度的日常使用者預設就是它。Samsung Galaxy Watch 7 Ultra 守第四，上週推送的 GPS 漂移修正韌體現在在我測試過的每一支機上都穩定。\n\nGarmin Forerunner 965 守第五，Fenix 等級以下的認真跑者首選還是它。排名沒動，但購買環境是整個春季最乾淨的一週。",
    zh_h=[
        {"title": "Apple Watch Ultra 2 對 Ultra 3 還是贏在 C/P 值", "body": "Ultra 3 的衛星功能微調是真的，但對於已經有手機 LTE 的買家來說，價差不合理。Ultra 2 守住第一，這個 C/P 值算式是全年最乾淨的。"},
        {"title": "Garmin Fenix 8 多天續航故事無人能撼動", "body": "這禮拜比較評測一致確認用戶已經知道的事：Apple Watch 在多天 GPS 訓練跟離網耐力上跟 Fenix 8 完全不是同一個檔次。真的在這個使用情境裡的人，還是應該先買 Garmin。"},
        {"title": "Samsung Galaxy Watch 7 Ultra GPS 修正現在所有機都穩定", "body": "上週推送的 GPS 漂移韌體修正在我測試過的每一支上都站得住。Galaxy Watch 7 Ultra 守第四，現在可以毫無保留地推薦。Samsung 生態買家終於拿到當初發表會上想要的耐用智慧錶故事。"},
    ],
)


# ============================================================
# best-smart-rings
# ============================================================
add(
    "best-smart-rings",
    refs=[
        {"title": "Oura Ring users get revamped AI-powered app", "url": "https://www.techradar.com/health-fitness/oura-ring-users-are-getting-a-revamped-ai-powered-app-and-samsung-galaxy-ring-users-are-going-to-be-seriously-jealous", "source": "TechRadar"},
        {"title": "Smart rings poised for 2026 growth, Oura set to lead", "url": "https://www.bloomberg.com/news/articles/2026-01-05/smart-rings-poised-for-2026-growth-oura-set-to-lead", "source": "Bloomberg"},
        {"title": "Samsung Galaxy Ring 2 shelved amid Oura patent dispute and underwhelming sales", "url": "https://www.techradar.com/health-fitness/samsung-galaxy-ring-2-shelved-an-oura-patent-dispute-and-reported-underwhelming-sales-casts-doubt-on-the-smart-rings-future", "source": "TechRadar"},
    ],
    en_c="The Oura Ring 4 stays on top and the Oura app redesign that landed this week is the single most important update on the leaderboard. Oura Advisor now has access to sleep trends, activity changes, dietary insights from Meals, and can analyze new Habits and Routines to build personalized plans. This is the kind of vertical AI integration that genuinely earns the subscription fee for the first time, and it puts daylight between Oura and everyone else in the category. The Samsung Galaxy Ring holds second on existing hardware merits but TechRadar's reporting this week that the Galaxy Ring 2 is unlikely in H1 2026 (and possibly shelved entirely) due to the Oura patent dispute and weaker-than-expected sales reframes the buying decision. If you are buying Galaxy Ring today, know that the platform's future is genuinely uncertain. The RingConn Gen 2 holds third and the sleep apnea detection expansion from last week is still the most credible non-Oura health feature in the category. The Ring PRO and Ring Air round out the top five and neither moved this week. Bloomberg's January framing that Oura is set to lead 2026 looks more accurate every week. If you are buying a smart ring today and the price gap is acceptable, buy the Oura.",
    en_h=[
        {"title": "Oura Advisor AI redesign earns the subscription fee for the first time", "body": "Sleep trends, activity changes, dietary insights from Meals, Habits and Routines analysis with personalized planning. This is the vertical AI integration that smart rings have promised since launch. Locked-in top spot and the gap to second just widened."},
        {"title": "Galaxy Ring 2 shelf risk reframes the buying decision today", "body": "TechRadar reporting this week confirms the Oura patent dispute plus weaker sales make the Galaxy Ring 2 unlikely in H1 2026 and possibly cancelled entirely. Buying Galaxy Ring today means accepting platform-future uncertainty. Be aware before purchase."},
        {"title": "RingConn Gen 2 sleep apnea detection is the credible non-Oura play", "body": "Expanded detection from last week holds as the most credible health feature outside Oura. For buyers who want a smart ring without the Oura subscription and without Samsung-ecosystem dependence, RingConn Gen 2 is the right answer."},
    ],
    zh_c="Oura Ring 4 守住第一，這禮拜推出的 Oura app 改版是榜上最重要的更新。Oura Advisor 現在可以存取睡眠趨勢、活動變化、Meals 飲食洞察，還能分析新的 Habits 跟 Routines 來建立個人化計畫。這種垂直 AI 整合終於讓訂閱費值回票價，跟分類裡其他人拉開明顯距離。\n\nSamsung Galaxy Ring 守在第二靠的是現有硬體本錢，但 TechRadar 這禮拜的報導指出 Galaxy Ring 2 因為 Oura 專利糾紛跟銷售低於預期，2026 上半年不太可能上市、甚至可能整個取消，這重新定義了購買決策。今天買 Galaxy Ring 要知道這個平台的未來是真的不確定。\n\nRingConn Gen 2 守第三，上週擴充的睡眠呼吸中止偵測還是分類裡 Oura 以外最可信的健康功能。Ring PRO、Ring Air 補滿前五，這禮拜都沒動。\n\nBloomberg 一月講 Oura 會領導 2026 這個論述，每禮拜看起來都更準確。今天要買智慧戒指、價差能接受，就買 Oura。",
    zh_h=[
        {"title": "Oura Advisor AI 改版讓訂閱費首次值回票價", "body": "睡眠趨勢、活動變化、Meals 飲食洞察、Habits 跟 Routines 分析加個人化規劃。這就是智慧戒指從上市以來承諾的垂直 AI 整合。第一名鎖定，跟第二名差距又拉大。"},
        {"title": "Galaxy Ring 2 取消風險重新定義今天的購買決策", "body": "TechRadar 這禮拜報導確認 Oura 專利糾紛加上銷售疲弱，讓 Galaxy Ring 2 在 2026 上半年不太可能上市、甚至可能整個取消。今天買 Galaxy Ring 就要接受平台未來的不確定性。買之前先想清楚。"},
        {"title": "RingConn Gen 2 睡眠呼吸中止偵測是 Oura 以外最可信的選擇", "body": "上週擴充的偵測功能維持是 Oura 以外最可信的健康功能。想要智慧戒指又不要 Oura 訂閱、也不想被 Samsung 生態綁的人，RingConn Gen 2 就是正確答案。"},
    ],
)


# ============================================================
# best-smart-glasses
# ============================================================
add(
    "best-smart-glasses",
    refs=[
        {"title": "Meta opens Ray-Ban Display to web app developers", "url": "https://gizmodo.com/meta-ray-ban-display-are-about-to-get-a-lot-more-chaotic-2000759107", "source": "Gizmodo"},
        {"title": "Google AI Glasses vs Meta Ray-Ban: smart eyewear's first real fight", "url": "https://the-gadgeteer.com/2026/05/01/google-ai-glasses-vs-meta-ray-ban-smart-glasses-comparison/", "source": "The Gadgeteer"},
        {"title": "Ray-Ban Meta Smart Glasses review: better, cooler, more useful", "url": "https://moorinsightsstrategy.com/research-notes/ray-ban-meta-smart-glasses-review-better-cooler-and-more-useful-than-ever/", "source": "Moor Insights & Strategy"},
    ],
    en_c="The Ray-Ban Meta Gen 2 stays on top because the Moor Insights & Strategy research note this week reinforces what owners have been saying since launch: this is finally the smart-glasses product that real people will wear all day without thinking about it. The Meta Ray-Ban Display moves up materially on momentum because Meta opened the Display to web app developers this week, which means the URL-launchable web app model is now live and the ecosystem is about to expand fast. The Gizmodo framing that the Display is 'about to get a lot more chaotic' is accurate, and chaotic in this category is good. The display itself still hits 5,000 nits at max brightness and 90Hz refresh, and translation plus walking directions are the killer use cases. The Oakley Meta HSTN holds third and remains the right pick for sport-styled buyers who want the Meta AI stack without the classic Ray-Ban silhouette. The Oakley Meta Vanguard holds fourth. The XREAL One Pro stays fifth and is still the right pick for buyers who care about display tech more than AI features. The Gadgeteer's May 1 comparison framing Google AI Glasses versus Meta Ray-Ban as 'smart eyewear's first real fight' is the right framing for the second half of 2026. Today, Meta is still winning.",
    en_h=[
        {"title": "Meta Ray-Ban Display web app opening is the ecosystem unlock", "body": "Developers can now ship URL-launchable web apps to Display plus Neural Band. This turns Display from a closed feature set into a platform with real third-party momentum. Score moves up because the trajectory now matters more than today's app count."},
        {"title": "Ray-Ban Meta Gen 2 stays the all-day wear winner", "body": "Moor Insights research note this week confirms what owners have been saying: this is the first smart-glasses product real people wear all day without thinking. That is the entire game in this category. Locked-in top spot."},
        {"title": "Google AI Glasses fight is coming and it sharpens the Meta argument", "body": "The Gadgeteer's May 1 framing of Google AI Glasses versus Meta Ray-Ban as the first real fight is accurate for H2 2026. Today Meta is still winning because the hardware ships and the ecosystem opening is now public. Watch the Google response carefully through summer."},
    ],
    zh_c="Ray-Ban Meta Gen 2 守住第一，Moor Insights & Strategy 這禮拜的研究報告再次強化用戶從上市就在講的事：這是第一款真實使用者會一整天戴著不去想它的智慧眼鏡產品。\n\nMeta Ray-Ban Display 動能上明顯上揚，因為 Meta 這禮拜把 Display 對網頁應用開發者開放，URL 啟動的 web app 模式現在正式上線，生態系即將快速擴張。Gizmodo 用「即將變得更加混亂」這個說法很準確，這個分類混亂是好事。顯示本身還是維持 5,000 nits 最高亮度跟 90Hz 更新率，翻譯跟導航是殺手級使用情境。\n\nOakley Meta HSTN 守第三，想要 Meta AI 生態又不想要經典 Ray-Ban 外型的運動風格買家還是選它。Oakley Meta Vanguard 守第四。XREAL One Pro 守第五，重視顯示技術勝過 AI 功能的買家還是選它。\n\nThe Gadgeteer 5/1 那篇把 Google AI Glasses 對 Meta Ray-Ban 定位成「智慧眼鏡第一場真正對決」，這對 2026 下半年是正確的定位。但今天 Meta 還是贏家。",
    zh_h=[
        {"title": "Meta Ray-Ban Display 開放 web app 是生態系解鎖", "body": "開發者現在可以把 URL 啟動的 web app 推送到 Display 加 Neural Band 組合。這把 Display 從封閉功能集變成有真實第三方動能的平台。分數上升是因為現在曲線比當下 app 數量更重要。"},
        {"title": "Ray-Ban Meta Gen 2 守住整天配戴的贏家位置", "body": "Moor Insights 這禮拜的研究報告確認用戶從上市就在講的事：這是第一款真實使用者會一整天戴著不去想它的智慧眼鏡。在這個分類，這就是整場遊戲的關鍵。第一名鎖定。"},
        {"title": "Google AI 眼鏡戰役即將開打，反而讓 Meta 論述更銳利", "body": "The Gadgeteer 5/1 把 Google AI Glasses 對 Meta Ray-Ban 定位成第一場真正對決，這對 2026 下半年是正確的定位。今天 Meta 還是贏家，因為硬體已經出貨、生態系也正式開放。Google 整個夏天的回應要密切觀察。"},
    ],
)
