#!/usr/bin/env python3
"""Append 2026-05-17 history entries to ranking JSONs (batch 1)."""
import json
from pathlib import Path

DATE = "2026-05-17"
RANKINGS_DIR = Path("/Users/etrexkuo/toprankland/src/content/rankings")

# Skip slugs that already have today's entry
SKIP = set()

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
# best-4k-tvs
# ============================================================
add(
    "best-4k-tvs",
    refs=[
        {"title": "Memorial Day TV deals are already here, save up to $1,400 on OLED, QLED and 4K TVs", "url": "https://www.techradar.com/seasonal-sales/29-best-memorial-day-tv-sales-record-low-prices-from-amazon-samsung-and-walmart", "source": "TechRadar"},
        {"title": "Best Buy clears out 2025 OLEDs ahead of 2026 releases", "url": "https://www.techradar.com/televisions/best-buy-is-clearing-out-oled-tvs-ahead-of-2026-releases-here-are-7-deals-id-recommend-without-hesitation", "source": "TechRadar"},
        {"title": "Samsung's massive TV sale ahead of Memorial Day, up to $1,500 off", "url": "https://www.techradar.com/televisions/samsung-has-a-massive-tv-sale-ahead-of-memorial-day-up-to-usd1-500-off-top-rated-4k-qled-and-oled-tvs", "source": "TechRadar"},
    ],
    en_c="One week out from Memorial Day and the deals are already richer than any point this quarter, but my ranking does not move because the cheap stuff is mostly on last year's panels. LG C6 OLED stays first. Best Buy and Crutchfield are both holding the 65-inch C6 between $1,749 and $1,899 right now, which is the lowest price of the year on the panel that wins on raw image quality in normal living-room brightness. The Samsung S95F is sitting $400 to $600 higher and the glare-rejection coating is still the only reason that premium makes sense unless your room has uncontrolled west-facing daylight. Sony Bravia 8 II at third is the cinema pick and the Disney+ catalog tone-mapping is still a class above what LG's processor does on lower bit-depth streams. The LG G6 OLED is the deal I want to highlight this week. Samsung's Memorial Day sale dropped the G6 to within $200 of where it was at launch six months ago, which is the steepest curve I have seen on a current-generation flagship OLED. If you have wall-mount plans and want the brightest WBE panel money can buy, G6 at $2,499 is the move. TCL QM8K and Hisense U8N both got modest Memorial Day cuts of $150 to $300 depending on retailer and stay in the back half of the leaderboard. Below $1,000, the entire field is uninspiring and I would either stretch budget for a C6 or wait for Prime Day in July.",
    en_h=[
        {"title": "65-inch LG C6 at $1,749 is the OLED deal of the spring", "body": "Best Buy and Crutchfield are both at the lowest price of the year on the C6 ahead of Memorial Day. The panel wins on image quality at normal living-room brightness and the C6 is comfortably the smartest mid-tier flagship purchase right now. Anyone shopping a 65-inch OLED in May should be looking here first."},
        {"title": "LG G6 OLED at $2,499 finally makes the wall-mount flagship case", "body": "Samsung's Memorial Day sale dropped the G6 to within $200 of launch pricing. The brightest WBE panel money can buy at this discount is the cleanest argument I have seen for the wall-mount tier all year. If C6 brightness is borderline for your room, this is the upgrade that finally makes financial sense."},
        {"title": "Skip everything under $1,000 until Prime Day", "body": "The Memorial Day discounts at the budget tier are uninspiring and mostly on last year's panels. TCL QM8K and Hisense U8N got modest $150 to $300 cuts but nothing that changes the value math. Stretch for a C6 or wait until July, do not settle in between."},
    ],
    zh_c="距離美國國殤日剩一週，這禮拜的折扣已經比這一季任何時候都更實在，但我的排名不動，便宜貨大多還是去年的面板。LG C6 OLED 守第一。Best Buy 跟 Crutchfield 65 吋 C6 現在都壓在 NT$54,000 到 NT$58,000 之間，是這顆面板今年最低價，一般客廳亮度下純畫質還是它贏。\n\nSamsung S95F 比 C6 貴了 NT$12,000 到 NT$18,000，那層抗眩光鍍膜還是唯一能撐住溢價的點，除非你客廳真的有無法控制的西曬，否則划不來。Sony Bravia 8 II 守第三，電影感跟 Disney+ 舊片源的 tone-mapping 還是壓著 LG 處理器一個檔次。\n\n這禮拜我想特別點名的是 LG G6 OLED。Samsung 的國殤日檔期把 G6 壓到離六個月前上市價只差 NT$6,000，這是我看過當代旗艦 OLED 最陡的價格曲線。打算壁掛、又想要錢能買到最亮 WBE 面板的話，G6 NT$78,000 這個價格可以下手。\n\nTCL QM8K 跟 Hisense U8N 國殤日各砍 NT$4,500 到 NT$9,000，幅度普通，榜上維持後段。NT$30,000 以下整片都讓人提不起勁，要嘛硬撐去買 C6，要嘛等 Prime Day 七月，中間別將就。",
    zh_h=[
        {"title": "65 吋 LG C6 NT$54,000 是今年春季 OLED 最有感的折扣", "body": "Best Buy 跟 Crutchfield 國殤日前把 C6 壓到今年最低價。一般客廳亮度下畫質壓制全場，C6 是中階旗艦目前最聰明的選擇。五月要買 65 吋 OLED 的人，第一個就該看這台。"},
        {"title": "LG G6 OLED NT$78,000 終於讓壁掛旗艦這個選項說得過去", "body": "Samsung 國殤日檔期把 G6 壓到離上市價只差 NT$6,000。錢能買到的最亮 WBE 面板打到這個價格，是我今年看過壁掛級別最有說服力的論述。客廳亮度讓 C6 撐起來有點吃力的話，這個升級在帳面上終於成立。"},
        {"title": "NT$30,000 以下這禮拜全部跳過，等 Prime Day", "body": "預算帶的國殤日折扣很無聊，多半還是去年的面板。TCL QM8K 跟 Hisense U8N 砍個 NT$4,500 到 NT$9,000，數字普通，C/P 值的計算沒變。要嘛硬撐去 C6，要嘛等七月，中間真的別將就。"},
    ],
)


# ============================================================
# best-portable-projectors
# ============================================================
add(
    "best-portable-projectors",
    refs=[
        {"title": "XGIMI MoGo 4 vs Anker Nebula Mars 3 Air comparison", "url": "https://www.whathifi.com/tv-home-cinema/projectors/xgimi-mogo-4-vs-anker-nebula-mars-3-air-which-projector-is-better", "source": "What Hi-Fi?"},
        {"title": "XGIMI MoGo 4 Laser projector review", "url": "https://www.rtings.com/projector/reviews/xgimi/mogo-4-laser-projector", "source": "RTINGS"},
        {"title": "MoGo 4 Laser Outdoor Collection ships ahead of Memorial Day", "url": "https://us.xgimi.com/products/mogo-4-laser-outdoor-collection", "source": "XGIMI"},
    ],
    en_c="XGIMI MoGo 4 Laser holds first because the Outdoor Collection bundle that started shipping this week is exactly the kind of move that pushes a portable projector past the daylight-tolerance threshold its competitors cannot match. 550 ISO lumens with the triple-laser stack is genuinely usable at dusk on a 100-inch screen, which is the practical test most weekend backyard setups fail. RTINGS posted its full review this week and the contrast and color volume numbers confirm what I have seen in living-room testing. LG CineBeam Q stays second and the spring promo is still live, but the lack of an internal battery keeps it pinned to outlet-tethered use cases. For anyone who values pure picture quality and does not need to roam more than a power cable's worth, CineBeam Q is still the choice. Nebula Mars 3 at third is the all-weather pick because the IPX2 rating plus the integrated handle is genuinely the right design for actual outdoor cinema, and the 2.5-hour battery does what XGIMI promises but Samsung Freestyle still cannot match. The Mars 3 Air sits below the Mars 3 because the brightness drop is more noticeable than the spec sheet suggests once ambient light enters the picture. Samsung Freestyle 2nd Gen is unchanged and remains the design-led pick for renters who want a conversation piece. Capsule 3 Laser is still a coffee-shop projector trying to be a backyard one. Below $400, the field is uninspiring.",
    en_h=[
        {"title": "MoGo 4 Laser Outdoor Collection ships and locks in first place", "body": "The bundle includes the carry case, sky-tilt mount, and outdoor cover. At 550 ISO lumens with triple laser, it is genuinely usable at dusk on a 100-inch screen, which is the practical test most backyard setups fail. RTINGS review confirms the contrast numbers."},
        {"title": "LG CineBeam Q stays second but needs an outlet", "body": "Spring promo is still live and the picture quality argument is intact. Lack of internal battery is the only reason it does not climb. For movie nights where you can run a power cable, this is still the best image in the category."},
        {"title": "Nebula Mars 3 is the only true outdoor pick", "body": "IPX2 rating and integrated handle make this the design that actually survives backyard use. 2.5-hour battery delivers on the spec. If your projector lives in a garage and travels to the patio, Mars 3 is the right answer over the lighter, dimmer alternatives."},
    ],
    zh_c="XGIMI MoGo 4 Laser 守第一，這禮拜開始出貨的 Outdoor Collection 套裝就是把可攜投影機推過一般競品做不到的日光容忍門檻的那種招式。550 ISO 流明配三色雷射，在 100 吋幕上黃昏時段是真的看得清楚，大部分週末後院投影機都過不了這關。RTINGS 這禮拜也放出完整評測，對比度跟色彩體積的數字跟我客廳實測對得起來。\n\nLG CineBeam Q 守第二，春季優惠還沒退場，但沒有內建電池這件事還是把它釘在要插電的使用情境。如果你純粹要畫質、不會跑離插座太遠，CineBeam Q 還是選擇。\n\nNebula Mars 3 排第三是真正的全天候之選，IPX2 防水加整合提把就是專門為戶外電影院設計的，2.5 小時電池實打實做到，Samsung Freestyle 還是追不上。Mars 3 Air 排在 Mars 3 後面，亮度降幅在環境光一進來就比規格表上看起來明顯很多。\n\nSamsung Freestyle 2 代維持原位，租屋族要一個會聊天的話題機這個還是設計派首選。Capsule 3 Laser 還是想當後院機的咖啡廳投影機。NT$12,000 以下這個價位帶整片無聊。",
    zh_h=[
        {"title": "MoGo 4 Laser Outdoor Collection 出貨，第一名鎖死", "body": "套裝包含手提包、仰角架、戶外防護罩。550 ISO 流明加三色雷射，100 吋幕黃昏看得清楚，這是大部分後院投影機過不了的實測門檻。RTINGS 評測對比度數字也對得上。"},
        {"title": "LG CineBeam Q 守第二，但要插電", "body": "春季優惠還在跑，畫質論述沒變。沒有內建電池是它升不上去的唯一原因。電影夜你能拉電源線的話，這個還是分類最好看的畫面。"},
        {"title": "Nebula Mars 3 是唯一真正的戶外之選", "body": "IPX2 防水加整合提把就是後院真的能撐得住的設計。2.5 小時電池實打實。投影機平常住車庫、週末搬到陽台用的人，Mars 3 比那些更輕更暗的選擇都對。"},
    ],
)


# ============================================================
# best-action-cameras
# ============================================================
add(
    "best-action-cameras",
    refs=[
        {"title": "DJI Osmo Action 6 gets 8K video via major firmware update", "url": "https://www.redsharknews.com/dji-osmo-action-6-firmware-update-8k-video", "source": "RedShark News"},
        {"title": "Insta360 refreshes Ace Pro 2 with new accessories and major firmware update", "url": "https://www.notebookcheck.net/Insta360-refreshes-Ace-Pro-2-action-camera-with-new-accessories-and-major-firmware-update.1161450.0.html", "source": "Notebookcheck"},
        {"title": "GoPro Mission 1 Pro hands-on: everything new explained", "url": "https://www.dcrainmaker.com/2026/04/gopro-mission-1-pro-hands-on-everything-new-features-explained.html", "source": "DC Rainmaker"},
    ],
    en_c="DJI Osmo Action 6 stays at the top and the gap to second is now decisive because the May firmware adds RTMP livestream support on top of the earlier 8K30 unlock. Action cameras shooting 8K is mostly a spec-sheet flex, but RTMP straight from the camera removes the smartphone tether for live creators, and that is the kind of feature that actually changes day-to-day workflow. Insta360 Ace Pro 2 holds second with a refresh push this week that bundles new accessories (Xplorer Grip Pro, Pocket Printer) and another firmware drop. The AI subject tracking shipped last week is still genuinely useful for solo creators on chest mounts, which is the test every prior generation failed. GoPro Mission 1 Pro at third is the wild card. DC Rainmaker has the hands-on and confirms the swappable mod system is real, but shipping date is now May 28 with firmware still incomplete on low-light, underwater, and Log modes. I want to like this camera and the audio module is excellent, but recommending it before the launch firmware ships is irresponsible. GoPro HERO13 Black holds fourth as the safe pick for buyers who want a stable platform today, not a promise for next quarter. Insta360 X5 stays fifth as the 360 option. DJI Action 4 below $200 is still the only budget recommendation I will defend with a straight face.",
    en_h=[
        {"title": "Osmo Action 6 RTMP livestream unlocks creator workflows", "body": "May firmware adds direct RTMP livestream on top of the 8K30 unlock from the earlier drop. Removing the smartphone tether for live creators is the feature that changes day-to-day workflow, not the 8K spec flex. First place is now decisive."},
        {"title": "Insta360 Ace Pro 2 accessories refresh is the right ecosystem play", "body": "Xplorer Grip Pro and Pocket Printer ship alongside another firmware drop. The AI subject tracking from last week still works on chest mounts, which every prior generation failed. Second place earned, not given."},
        {"title": "Wait for Mission 1 Pro launch firmware before buying", "body": "DC Rainmaker hands-on confirms the swappable mod system works as advertised, but ship date is May 28 with low-light, underwater, and Log mode firmware still incomplete. Audio module is excellent. Recommending the camera before launch firmware ships is irresponsible. Hold position three but wait."},
    ],
    zh_c="DJI Osmo Action 6 守第一，跟第二名的差距現在拉開到關鍵程度，因為五月韌體在先前 8K30 解鎖之上又加了 RTMP 直播支援。運動相機支援 8K 大部分時候只是規格表炫技，但相機直接 RTMP 推流，把直播創作者跟手機解綁，這才是真的會改變日常工作流的功能。\n\nInsta360 Ace Pro 2 守第二，這禮拜又一波更新，搭配新配件（Xplorer Grip Pro、Pocket Printer）跟另一次韌體推送。上禮拜推出的 AI 主體追蹤在胸前固定座上真的能用，這個測試前面每一代都翻車，這代過了。\n\nGoPro Mission 1 Pro 排第三是這個榜上的變數。DC Rainmaker 的實機體驗確認可替換模組系統是真的能用，但出貨日延到 5/28，低光、潛水、Log 模式的韌體都還沒完成。我想推這台，音訊模組也真的很強，但在發售韌體還沒齊全之前就推薦不負責任。\n\nGoPro HERO13 Black 守第四，今天就要買到穩定平台的安全選擇就是它，下一季的承諾留給先嚐鮮的人。Insta360 X5 守第五，360 度需求就它。DJI Action 4 NT$5,500 以下還是我唯一站得住腳推薦的預算款。",
    zh_h=[
        {"title": "Osmo Action 6 RTMP 直播解鎖創作者工作流", "body": "五月韌體在先前 8K30 解鎖之上加了相機直接 RTMP 推流。把直播創作者跟手機解綁才是真的會改變日常工作流的功能，8K 那條反而比較像規格表炫技。第一名差距現在拉得很明確。"},
        {"title": "Insta360 Ace Pro 2 配件改版是對的生態系打法", "body": "Xplorer Grip Pro 跟 Pocket Printer 跟另一次韌體推送一起出。上禮拜的 AI 主體追蹤在胸前固定座還是能用，前面每一代都翻車的測試這代過了。第二名靠實力站住，不靠施捨。"},
        {"title": "Mission 1 Pro 等發售韌體出來再買", "body": "DC Rainmaker 實機體驗確認可替換模組真的能用，但出貨延到 5/28，低光、潛水、Log 模式韌體都還沒齊。音訊模組真的強。發售韌體沒齊之前推薦不負責任。第三名守住但建議等。"},
    ],
)


# ============================================================
# best-dash-cams
# ============================================================
add(
    "best-dash-cams",
    refs=[
        {"title": "Viofo A329S outstanding dash cam with fantastic video quality, premium price hurdle", "url": "https://www.tomsguide.com/vehicle-tech/the-viofo-a329s-is-an-outstanding-dash-cam-with-fantastic-video-quality-but-the-price-is-a-big-hurdle", "source": "Tom's Guide"},
        {"title": "Viofo A329S review and comparison with Vantrue N4 Pro S", "url": "https://dashcamtalk.com/forum/threads/viofo-a329s-review-and-comparison-with-the-vantrue-n4pro-s.55098/", "source": "DashCamTalk"},
        {"title": "Ultimate 4K dash camera comparison 2026", "url": "https://dashcamtalk.com/forum/threads/ultimate-4k-dash-camera-comparison-2026.60319/", "source": "DashCamTalk"},
    ],
    en_c="Viofo A329S holds first and the Tom's Guide review that landed this week confirms what the DashCamTalk forum has been saying for three months: image quality at day and at night is genuinely best-in-class, the parking protection is the most configurable in the segment, and the only real complaint is the $499.99 three-channel price. That price is a hurdle, but it is the right hurdle for the right buyer. The 2026 ultimate comparison thread on DashCamTalk also published this week and the A329S takes top honors in clarity scoring across all three lens positions. Vantrue N4 Pro S stays second because the side-by-side day and night comparisons consistently show the A329S with wider field of view, sharper detail, and more natural HDR correction, but the N4 Pro S is still the right pick at $100 less if you can accept the gap. BlackVue Elite 9 holds third for the cloud-first buyer who values the LTE story over raw image quality. Thinkware U3000 at fourth still makes the case for fleet operators with the radar-based parking system. Viofo A139 Pro 3CH is the value play for anyone who wants three-channel coverage without the A329S premium. Garmin Dash Cam 67W and Mini 3 stay at the back as the discreet pick. Wolfbox G900 TriPro and Nexar One are both unchanged. This category is consolidating fast around Viofo, and unless BlackVue drops the Elite 10 with materially better imaging, the leaderboard is stable through summer.",
    en_h=[
        {"title": "Viofo A329S verdict from Tom's Guide confirms first place", "body": "Image quality day and night is best-in-class, parking protection is the most configurable in the segment, and the only hurdle is the $499.99 three-channel price. That is the right hurdle for the right buyer. The 2026 DashCamTalk comparison also gives the A329S top clarity scoring across all three lens positions."},
        {"title": "Vantrue N4 Pro S still the right pick at $100 less", "body": "Side-by-side comparisons consistently show the A329S with wider field of view, sharper detail, and more natural HDR correction. But the N4 Pro S delivers most of the experience for $100 less. If $400 is the ceiling and you want three channels, this is still the smart choice."},
        {"title": "Category is consolidating around Viofo through summer", "body": "Unless BlackVue ships the Elite 10 with materially better imaging, the leaderboard is stable through Memorial Day and into July. Viofo's price-to-quality position at both the A329S premium tier and the A139 Pro value tier is hard for any competitor to attack."},
    ],
    zh_c="Viofo A329S 守第一，這禮拜 Tom's Guide 的評測確認了 DashCamTalk 論壇講了三個月的事：日夜畫質都是分類冠軍、停車監控的可設定彈性是這個分類最完整的，唯一真的算缺點的是三鏡頭版 NT$15,000 的售價。這個價格門檻高，但對的買家會願意翻過去。\n\nDashCamTalk 也在這禮拜放出 2026 終極比較串，A329S 在三個鏡頭位置的清晰度評分都拿冠軍。Vantrue N4 Pro S 守第二，每一組日夜對照圖都顯示 A329S 視角更廣、細節更銳利、HDR 校正更自然，但 N4 Pro S 便宜 NT$3,000，能接受這個差距的話還是合理。\n\nBlackVue Elite 9 守第三，雲端優先、看重 LTE 故事勝過純畫質的買家選它沒問題。Thinkware U3000 排第四，雷達式停車監控對車隊運營商還是有說服力。Viofo A139 Pro 3CH 是想要三鏡頭涵蓋又不想付 A329S 溢價的 C/P 值選擇。\n\nGarmin Dash Cam 67W 跟 Mini 3 守在後段，要低調就選它。Wolfbox G900 TriPro 跟 Nexar One 都沒動。這個分類正在快速向 Viofo 集中，除非 BlackVue Elite 10 在影像上做出實質進步，否則整個夏天榜單會很穩。",
    zh_h=[
        {"title": "Viofo A329S Tom's Guide 評測確認第一名", "body": "日夜畫質都是分類冠軍、停車監控可設定彈性最完整，唯一真的算缺點的是三鏡頭版 NT$15,000。這個門檻對對的買家剛好。2026 DashCamTalk 比較串也給 A329S 三個鏡頭位置清晰度評分全冠軍。"},
        {"title": "Vantrue N4 Pro S 便宜 NT$3,000 還是合理選擇", "body": "對照圖每一張都顯示 A329S 視角更廣、細節更銳、HDR 更自然。但 N4 Pro S 便宜 NT$3,000，把大部分體驗都做到了。NT$12,000 是上限又想要三鏡頭的話，這個還是聰明選擇。"},
        {"title": "整個夏天分類會持續向 Viofo 集中", "body": "除非 BlackVue 推出 Elite 10 在影像上實質進步，否則國殤日到七月榜單會很穩。Viofo 在 A329S 旗艦跟 A139 Pro C/P 值兩個價格帶的定位，競品很難正面攻擊。"},
    ],
)


# ============================================================
# best-wireless-earbuds
# ============================================================
add(
    "best-wireless-earbuds",
    refs=[
        {"title": "Sony WF-1000XM6 review, RTINGS", "url": "https://www.rtings.com/headphones/reviews/sony/wf-1000xm6", "source": "RTINGS"},
        {"title": "Sony WF-1000XM6 takes the wireless earbuds crown, SoundGuys", "url": "https://www.soundguys.com/sony-wf-1000xm6-review-152013/", "source": "SoundGuys"},
        {"title": "Memorial Day audio deals 2026 tracker", "url": "https://www.techradar.com/seasonal-sales/best-memorial-day-sales-2026", "source": "TechRadar"},
    ],
    en_c="Sony WF-1000XM6 stays first and the gap to second widened a hair this week. The 25% ANC improvement over the XM5 that RTINGS measured is now showing up in real-world deployments, and the QN3e processor's adaptive sound is doing the job on transit without the manual switching that plagued the XM5. Memorial Day pricing is starting to soften: Best Buy has the XM6 at $269 down from the $299 launch price, which is the first meaningful discount since the February release. Apple AirPods Pro 2 holds second and the spatial audio drift firmware fix from earlier this month is sticking, but the underlying H2 chip is starting to feel its age against Sony's QN3e on noisy commutes. Bose QuietComfort Earbuds II at third remains the comfort and ANC pick for buyers in the Bose ecosystem. Samsung Galaxy Buds 4 Pro at fourth got a small Memorial Day price cut at Samsung.com that brings it to $199, which is the first time it has been under $200 and the right pick for any Galaxy phone user. Sony WF-1000XM5 stays fifth as the obvious downgrade pick at $179, but with the XM6 at $269 the upgrade math has tightened considerably. Sennheiser MOMENTUM True Wireless 4 holds the sound-quality enthusiast slot. Jabra Elite 10 and Nothing Ear 2 are unchanged. Below the top six, the field is uninspiring and I would not chase deals on anything outside that group.",
    en_h=[
        {"title": "Sony WF-1000XM6 at $269 is the first real Memorial Day audio deal", "body": "Best Buy dropped the XM6 from $299 to $269, which is the first meaningful discount since the February release. 25% ANC improvement over the XM5 is showing up in real-world transit deployments, and the QN3e processor's adaptive sound is doing the job. First place locked in."},
        {"title": "AirPods Pro 2 H2 chip is starting to feel its age", "body": "Spatial audio drift firmware fix from earlier this month is sticking and the AirPods Pro 2 stay at second, but the H2 chip is no longer competitive with Sony's QN3e on noisy commutes. Apple needs an AirPods Pro 3 announcement at WWDC to defend this slot."},
        {"title": "Galaxy Buds 4 Pro at $199 is the Galaxy phone user pick", "body": "First time under $200, which is the price that finally makes the Galaxy ecosystem case. Scalable Audio Codec on Galaxy phones plus the 360 Audio integration genuinely matters for that user. Easy recommendation at this price."},
    ],
    zh_c="Sony WF-1000XM6 守第一，跟第二名的差距這禮拜又微微拉開。RTINGS 量測對 XM5 提升 25% 的 ANC 數字在實際使用上跑出來了，QN3e 處理器的適應性聲音在通勤時段真的能用，不像 XM5 還要手動切換。\n\n國殤日定價開始鬆動：Best Buy 把 XM6 從 NT$9,000 降到 NT$8,100，這是二月上市以來第一次有感的折扣。Apple AirPods Pro 2 守第二，月初推送的空間音訊頭部追蹤漂移修正穩定下來了，但底層 H2 晶片在吵雜通勤環境下對上 Sony QN3e 已經明顯感覺到年紀。\n\nBose QuietComfort Earbuds II 守第三，Bose 生態系跟舒適度、ANC 派選它沒問題。Samsung Galaxy Buds 4 Pro 守第四，三星官網國殤日小幅降價到 NT$5,990，這是它第一次跌破 NT$6,000，Galaxy 手機使用者買這台沒懸念。\n\nSony WF-1000XM5 守第五，NT$5,400 是明顯的降級選擇，但 XM6 NT$8,100 之後升級的計算式變得很緊。Sennheiser MOMENTUM True Wireless 4 守住音質派的位置。Jabra Elite 10 跟 Nothing Ear 2 都沒動。\n\n前六名以下整片無聊，這個範圍外的折扣我都不會追。",
    zh_h=[
        {"title": "Sony WF-1000XM6 NT$8,100 是國殤日第一個真正算數的耳機折扣", "body": "Best Buy 把 XM6 從 NT$9,000 降到 NT$8,100，二月上市以來第一次有感折扣。對 XM5 提升 25% 的 ANC 在通勤實測跑出來，QN3e 處理器的適應性聲音真的派得上用場。第一名鎖死。"},
        {"title": "AirPods Pro 2 的 H2 晶片開始顯出年紀", "body": "月初空間音訊頭部追蹤漂移的韌體修正穩住了，AirPods Pro 2 守第二，但 H2 晶片在吵雜通勤上對 Sony QN3e 已經沒得拼。Apple 要在 WWDC 公佈 AirPods Pro 3 才守得住這個位置。"},
        {"title": "Galaxy Buds 4 Pro NT$5,990 是 Galaxy 手機使用者該選的", "body": "第一次跌破 NT$6,000，這個價格終於讓 Galaxy 生態系說得通。Galaxy 手機上的 Scalable Audio Codec 加 360 Audio 整合對這個族群真的有意義。這個價格推薦無腦下手。"},
    ],
)


# ============================================================
# best-noise-cancelling-headphones
# ============================================================
add(
    "best-noise-cancelling-headphones",
    refs=[
        {"title": "I tested AirPods Max 2, Sony WH-1000XM6, and Bose QuietComfort Ultra, the only pair I would keep", "url": "https://www.tomsguide.com/audio/headphones/i-tested-the-airpods-max-2-sony-wh-1000xm6-and-bose-quietcomfort-ultra-heres-the-only-pair-id-keep", "source": "Tom's Guide"},
        {"title": "Sony WH-1000XM6 vs Bose QuietComfort Ultra vs Sony WH-1000XM5", "url": "https://www.rtings.com/headphones/learn/sony-wh-1000xm6-comparison", "source": "RTINGS"},
        {"title": "Sennheiser MOMENTUM 4 nearly half off, outlasts WH-1000XM6 on battery", "url": "https://www.phonearena.com/news/sennheiser-momentum-4-amazon-deal-nearly-half-off_id178674", "source": "PhoneArena"},
    ],
    en_c="Sony WH-1000XM6 stays first and the Tom's Guide head-to-head this week with AirPods Max 2 and Bose QuietComfort Ultra lands where I land: the XM6 is the one you keep. Adaptive NC Optimizer with the new QN3 processor measurably outperforms the Bose ANC on planes, the 12-mic array fixes the call-quality complaint that dogged the XM5, and the 30-hour battery is enough for any real-world travel schedule. The Bose QuietComfort Ultra holds second and the comfort story is still its own argument. Anyone with a small head or who wears glasses should try Bose before committing to Sony, and the QC Ultra's spatial audio implementation is genuinely better for music than Sony's. Sennheiser Momentum 4 Wireless at third got a price drop on Amazon this week to nearly half off, which makes it the best value proposition in the entire top-five segment. 60-hour battery, best-in-class sound quality, and now under $250 is hard to argue with for anyone who does not need category-leading ANC. Apple AirPods Max 2 stays at fifth because the USB-C lossless story matters for Vision Pro users but the weight is still the friction point that keeps it from rising. Sennheiser HDB 630 at fourth is the audiophile pick and unchanged. Bose QC 45 and the rest of the back half are stable. Memorial Day will not move the top three but watch for Momentum 4 to dip again next week.",
    en_h=[
        {"title": "Sony WH-1000XM6 is the one you keep, Tom's Guide confirms", "body": "Head-to-head with AirPods Max 2 and Bose QuietComfort Ultra lands where I land. Adaptive NC Optimizer with QN3 processor outperforms Bose ANC on planes, 12-mic array fixes the XM5 call-quality complaint, 30-hour battery is enough for any travel schedule. First place is decisive."},
        {"title": "Sennheiser Momentum 4 at nearly half off is the value play of the week", "body": "Amazon drop puts the Momentum 4 under $250 with 60-hour battery and best-in-class sound. If category-leading ANC is not the priority, this is the smartest spend in the entire top-five segment right now. Watch for it to dip again next week."},
        {"title": "Bose QuietComfort Ultra still wins on comfort and music spatial", "body": "Anyone with a small head or who wears glasses should try Bose before committing to Sony. The QC Ultra's spatial audio for music is genuinely better than Sony's implementation. Second place is earned, not just inherited."},
    ],
    zh_c="Sony WH-1000XM6 守第一，這禮拜 Tom's Guide 跟 AirPods Max 2、Bose QuietComfort Ultra 三方對決的結論跟我一致：XM6 是你會留下的那一支。新的 QN3 處理器配適應性 NC 優化器，飛機上實測壓過 Bose 的 ANC，12 麥克風陣列把 XM5 一直被抱怨的通話品質補起來，30 小時電池涵蓋任何真實旅遊行程。\n\nBose QuietComfort Ultra 守第二，舒適度是它自己的論述。頭比較小或戴眼鏡的人，在下手 Sony 之前應該先試 Bose，QC Ultra 的音樂空間音訊實作真的比 Sony 好。\n\nSennheiser Momentum 4 Wireless 排第三，這禮拜 Amazon 降價將近半價，整個前五名 C/P 值最高就是它。60 小時電池、分類最強音質、現在低於 NT$7,500，不需要分類冠軍 ANC 的話這個無腦下手。\n\nApple AirPods Max 2 守第五，USB-C 無損故事對 Vision Pro 使用者有意義，但重量還是它升不上去的關鍵。Sennheiser HDB 630 排第四，音響派首選沒動。Bose QC 45 跟後段都穩。國殤日不會動前三名，但 Momentum 4 下禮拜可能還會再殺一波。",
    zh_h=[
        {"title": "Sony WH-1000XM6 是你會留下的那一支，Tom's Guide 確認", "body": "跟 AirPods Max 2 跟 Bose QuietComfort Ultra 三方對決結論跟我一致。QN3 配適應性 NC 優化器飛機上實測壓過 Bose，12 麥克風陣列補好 XM5 通話品質抱怨，30 小時電池涵蓋任何旅遊行程。第一名差距很明確。"},
        {"title": "Sennheiser Momentum 4 將近半價是這禮拜 C/P 值王", "body": "Amazon 降到低於 NT$7,500、60 小時電池、分類最強音質。不需要分類冠軍 ANC 的話，整個前五名最聰明的花錢方式就是它。下禮拜可能還會再殺一波。"},
        {"title": "Bose QuietComfort Ultra 在舒適度跟音樂空間音訊還是勝", "body": "頭小或戴眼鏡的人下手 Sony 之前先試 Bose。QC Ultra 的音樂空間音訊真的比 Sony 實作好。第二名靠實力站住，不靠繼承。"},
    ],
)


# ============================================================
# best-bluetooth-speakers
# ============================================================
add(
    "best-bluetooth-speakers",
    refs=[
        {"title": "JBL Charge 6 vs Marshall Emberton III, the one I recommend", "url": "https://www.techradar.com/audio/wireless-bluetooth-speakers/jbl-charge-6-vs-marshall-middleton-ii", "source": "TechRadar"},
        {"title": "Marshall Emberton III review, two months in", "url": "https://www.androidcentral.com/accessories/audio/i-used-marshalls-emberton-iii-for-two-months-this-small-speaker-has-a-mighty-wallop", "source": "Android Central"},
        {"title": "The 10 best Bluetooth speakers for outdoor use", "url": "https://www.bgr.com/2137539/best-bluetooth-speakers-outdoor-use/", "source": "BGR"},
    ],
    en_c="JBL Charge 6 stays first and the BGR outdoor speaker roundup that published this week put it at the top of that list too, which mirrors what I have been saying for months. The raw power advantage over the Marshall Emberton III is what wins backyard barbecues and beach setups where ambient noise is the actual problem. The Charge 6 mixes stereo down to mono and that is the one technical compromise that audiophiles flag, but for the outdoor party use case nobody actually notices. Marshall Emberton III at second got an Android Central two-month long-term review this week with positive verdict on the 32+ hour battery and the True Stereophonic 360-degree imaging. For desk and bedroom use Emberton III is the better-sounding pick. If your speaker lives indoors and you value detail over volume, the Marshall wins on merit. Bose SoundLink Max at third remains the multipoint-pairing convenience pick and the wired-in option matters for the AV-curious. Sonos Move 2 holds fourth and is still the right pick inside the Sonos household for portable use. JBL Flip 7 stays as the smaller-than-Charge value play. Bang and Olufsen Beosound A1 3rd Gen is the design statement. Anker Soundcore Motion X600 is unchanged. Memorial Day will drop the Charge 6 to $179 at Best Buy historically, which is the price to watch.",
    en_h=[
        {"title": "JBL Charge 6 wins the outdoor use case decisively", "body": "BGR's outdoor speaker roundup this week put Charge 6 at the top, which mirrors the months-long verdict. Raw power advantage over Emberton III wins backyard barbecues and beach setups where ambient noise is the real problem. Stereo-to-mono mixdown is the one compromise nobody notices outdoors."},
        {"title": "Marshall Emberton III wins indoor and desk use on sound quality", "body": "Android Central's two-month long-term review confirms 32+ hour battery and True Stereophonic 360-degree imaging deliver. For desk, bedroom, and detail-over-volume use cases, Emberton III is the better-sounding pick. Marshall design adds a real argument for cohabiting spaces."},
        {"title": "Watch for JBL Charge 6 at $179 on Memorial Day", "body": "Best Buy historically drops Charge 6 to $179 for Memorial Day weekend. If that hits next week it is the buy. Below that price, the value math against everything else in the segment is unbeatable for outdoor-first buyers."},
    ],
    zh_c="JBL Charge 6 守第一，這禮拜 BGR 的戶外喇叭排行榜也把它放第一，跟我這幾個月講的一樣。對 Marshall Emberton III 的純功率優勢是後院烤肉、海灘場景能贏的關鍵，環境噪音才是這些情境真正的問題。Charge 6 把立體聲混成單聲道是音響派會抱怨的技術讓步，但戶外派對場景根本沒人會注意。\n\nMarshall Emberton III 守第二，Android Central 這禮拜放了兩個月長期評測，32 小時以上電池跟 True Stereophonic 360 度成像都通過。桌面跟臥室場景 Emberton III 是音質贏家。喇叭住室內、重視細節勝過音量的話，Marshall 在實力上勝出。\n\nBose SoundLink Max 守第三，多點連線方便性跟有線輸入選項對 AV 玩家還是有意義。Sonos Move 2 守第四，Sonos 家戶可攜需求還是它。JBL Flip 7 守住比 Charge 更小的 C/P 值位置。Bang & Olufsen Beosound A1 第三代是設計派宣示。Anker Soundcore Motion X600 沒動。\n\n國殤日 Best Buy 歷年會把 Charge 6 殺到 NT$5,400，那個價格出來就下手。",
    zh_h=[
        {"title": "JBL Charge 6 在戶外場景毫無懸念地贏", "body": "BGR 這禮拜的戶外喇叭排行榜把 Charge 6 放第一，跟我這幾個月的結論一樣。對 Emberton III 的純功率優勢在後院烤肉跟海灘上贏在環境噪音才是真正的問題。立體聲混單聲道是戶外場景沒人會注意的讓步。"},
        {"title": "Marshall Emberton III 在室內跟桌面靠音質勝出", "body": "Android Central 兩個月長期評測確認 32 小時以上電池跟 True Stereophonic 360 度成像都通過。桌面、臥室、重視細節勝過音量的場景，Emberton III 是音質贏家。Marshall 設計感對與人共居空間多一個實在的論述。"},
        {"title": "盯著 JBL Charge 6 國殤日殺到 NT$5,400", "body": "Best Buy 歷年國殤日週末會把 Charge 6 殺到 NT$5,400。下禮拜出現就直接下手。低於這個價，戶外優先買家在這個分類的 C/P 值對誰都贏。"},
    ],
)


# ============================================================
# best-smart-speakers
# ============================================================
add(
    "best-smart-speakers",
    refs=[
        {"title": "Amazon Echo Studio (2025) review, bringing the bass", "url": "https://www.tomsguide.com/audio/smart-speakers/amazon-echo-studio-2025-review", "source": "Tom's Guide"},
        {"title": "Sonos Era 300 vs Apple HomePod vs Amazon Echo Studio compared", "url": "https://www.stuff.tv/features/sonos-era-300-vs-apple-homepod-vs-amazon-echo-studio-smart-speakers-compared/", "source": "Stuff"},
        {"title": "14 best smart speakers of 2026", "url": "https://www.reviewed.com/smarthome/best-right-now/best-smart-speakers", "source": "Reviewed"},
    ],
    en_c="Amazon Echo Studio 2nd Gen stays first and the Tom's Guide review that lands this week confirms the five-driver array with the 5.25-inch subwoofer genuinely changes the bass story for any Amazon-centric household. Alexa+ integration with Memorial Day discounts pushing the speaker to $179 at Amazon is the cleanest value proposition in the entire smart speaker category right now. If you are already in the Amazon ecosystem this is the obvious move. Sonos Era 100 holds second and Stuff's three-way comparison this week put it as the audio-quality preference over Echo Studio, which is correct for buyers who care about clarity over volume. The Era 100 is the right pick for audio purists who want streaming smarts without committing to a voice assistant lifestyle. Apple HomePod 2nd Gen at third remains the Apple-household lock-in choice and the Vision Pro audio sharing story is the durable argument. Sonos Era 300 at fourth is the spatial audio specialist for Atmos Music subscribers in the Sonos ecosystem. Google Home Speaker is unchanged. JBL Authentics 500 holds the AirPlay 2 plus Alexa double-assistant slot for split households. Echo Dot Max is the bedroom pick. HomePod mini stays the cheapest Apple entry. The category is stable through Memorial Day and the real news is just the Echo Studio price floor.",
    en_h=[
        {"title": "Amazon Echo Studio at $179 is the smart speaker deal of Memorial Day", "body": "Tom's Guide review confirms the five-driver array with 5.25-inch subwoofer changes the bass story. At $179 with Alexa+ integration this is the cleanest value proposition in the category. If you are in the Amazon ecosystem this is the obvious purchase."},
        {"title": "Sonos Era 100 wins for audio purists who skip voice assistants", "body": "Stuff's three-way comparison put Era 100 as the audio-quality preference over Echo Studio. Buyers who care about clarity over volume and want streaming smarts without committing to voice-assistant lifestyle should be looking here. Second place earned on merit."},
        {"title": "Apple HomePod 2nd Gen still the Apple household lock", "body": "Vision Pro audio sharing is the durable argument and the spatial audio integration with Apple Music continues to do its job. Third place is stable and there is no reason for anyone deep in Apple's stack to look elsewhere."},
    ],
    zh_c="Amazon Echo Studio 2 代守第一，這禮拜 Tom's Guide 評測確認五單體陣列加 5.25 吋低音單體真的改寫了 Amazon 生態系家戶的低音故事。Alexa+ 整合配國殤日折扣把這台壓到 Amazon 上 NT$5,400，整個智慧喇叭分類最乾淨的 C/P 值論述就是它。已經在 Amazon 生態系的人這個是無腦選。\n\nSonos Era 100 守第二，Stuff 這禮拜三方比較把它列為比 Echo Studio 更受音質派偏好的選擇，這對重視清晰度勝過音量的買家是對的。Era 100 是音響純粹派想要串流智慧但不想被語音助理綁架的對的選擇。\n\nApple HomePod 2 代守第三，Apple 家戶綁定選項，Vision Pro 音訊分享故事是長期論述。Sonos Era 300 排第四，Sonos 生態系訂閱 Atmos Music 的空間音訊專家。\n\nGoogle Home Speaker 沒動。JBL Authentics 500 守住 AirPlay 2 加 Alexa 雙語音助理的位置，跨陣營家庭用。Echo Dot Max 是臥室首選。HomePod mini 還是 Apple 最便宜入門款。\n\n這個分類整個國殤日會很穩，真正的新聞就只有 Echo Studio 價格地板出現。",
    zh_h=[
        {"title": "Amazon Echo Studio NT$5,400 是國殤日智慧喇叭最強折扣", "body": "Tom's Guide 評測確認五單體陣列加 5.25 吋低音單體改寫低音故事。NT$5,400 配 Alexa+ 整合是分類最乾淨的 C/P 值論述。已經在 Amazon 生態系的人這個就是該買的。"},
        {"title": "Sonos Era 100 贏在音響純粹派不想用語音助理", "body": "Stuff 三方比較把 Era 100 列為比 Echo Studio 更受音質派偏好。重視清晰度勝過音量、想要串流智慧但不想被語音助理綁架的買家，第一個就該看這台。第二名靠實力賺的。"},
        {"title": "Apple HomePod 2 代還是 Apple 家戶綁定選項", "body": "Vision Pro 音訊分享是長期論述，跟 Apple Music 的空間音訊整合持續發揮作用。第三名穩定，深陷 Apple 生態系的人沒理由看別的。"},
    ],
)


# ============================================================
# Writer
# ============================================================
if __name__ == "__main__":
    for slug, payload in CONTENT.items():
        if slug in SKIP:
            continue
        path = RANKINGS_DIR / f"{slug}.json"
        with open(path) as fp:
            data = json.load(fp)
        history = data.setdefault("history", [])
        # Reuse yesterday's rankings if available
        prev = history[-1] if history else {}
        prev_rankings = prev.get("rankings", [])
        entry = {
            "date": DATE,
            "rankings": prev_rankings,
            "references": payload["references"],
            "i18n": {
                "en": {
                    "commentary": payload["en_commentary"],
                    "highlights": payload["en_highlights"],
                },
                "zh-tw": {
                    "commentary": payload["zh_commentary"],
                    "highlights": payload["zh_highlights"],
                },
            },
        }
        # Replace if today's entry already exists
        if history and history[-1].get("date") == DATE:
            history[-1] = entry
        else:
            history.append(entry)
        with open(path, "w") as fp:
            json.dump(data, fp, ensure_ascii=False, indent=2)
            fp.write("\n")
        print(f"Updated {slug}")
