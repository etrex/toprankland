#!/usr/bin/env python3
"""Apply 2026-05-18 history entries to all 48 ranking JSONs."""
import json
from pathlib import Path

DATE = "2026-05-18"
RANKINGS_DIR = Path("/Users/etrexkuo/toprankland/src/content/rankings")

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
        {"title": "Memorial Day TV deals are already here, save up to $1,400 on OLED, QLED and 4K TVs", "url": "https://www.techradar.com/seasonal-sales/dont-wait-for-memorial-day-to-buy-a-new-tv-shop-record-low-prices-right-now-with-up-to-usd1-400-off-4k-qled-and-oled-tvs", "source": "TechRadar"},
        {"title": "Samsung's massive Memorial Day TV sale is live, 4K, QLED, and OLED TVs from $349.99", "url": "https://www.techradar.com/seasonal-sales/samsungs-massive-memorial-day-sale-is-live-4k-qled-and-oled-tvs-from-usd349-99", "source": "TechRadar"},
        {"title": "Early Memorial Day TV sales are live, top 10 favorite deals starting from $369", "url": "https://www.tomsguide.com/tvs/early-memorial-day-tv-sales-are-already-live-and-ive-found-my-10-favorite-deals-starting-from-usd369", "source": "Tom's Guide"},
    ],
    en_c="Memorial Day proper hits next Monday but the deals officially kicked off today across every major retailer, and the leaderboard does not move because the discount curves confirm what I have been saying all spring. LG C6 OLED stays first. Best Buy and Crutchfield have both held the 65-inch C6 around $1,749 through the week and the new wave of Samsung S95F discounts at $400 to $600 over C6 still does not justify the premium unless your room has west-facing daylight you cannot control. Samsung S95F holds second and Sony Bravia 8 II holds third, where the cinema tone-mapping argument remains intact. The C5 at $1,399 from Best Buy is the value play of the week if you can live with last year's panel. I would still spend the extra $350 for the C6 because the new MLA panel and the brighter peak make the difference visible from across the room. LG G6 OLED is the upgrade story this week and Samsung's $500 cut puts the 65-inch within $200 of launch price, which is the steepest curve I have seen on a current flagship OLED. TCL QM8K and Hisense U8N each got another $100 to $200 trimmed, modest but enough to keep them in the back half. Below $700 the field is still uninspiring and the right move is to stretch for a C5.",
    en_h=[
        {"title": "Memorial Day official kickoff confirms C6 at $1,749 is the deal of the season", "body": "Best Buy and Crutchfield held the 65-inch C6 through the week's openers. The premium over the C5 is real and visible from across the room thanks to the new MLA panel and brighter peak. Anyone buying a 65-inch OLED this month should be looking here first."},
        {"title": "65-inch C5 at $1,399 is the value play if you can skip the MLA upgrade", "body": "Best Buy's $1,399 ask on last year's flagship is the cheapest current-gen LG OLED has been. The C5 panel is still excellent and the smart TV stack is identical. The $350 you save versus the C6 is genuinely defensible if your room is dim."},
        {"title": "LG G6 at within $200 of launch is the cleanest wall-mount story all year", "body": "Samsung dropped $500 off the 65-inch G6 to open Memorial Day week. The brightest WBE panel at this delta versus launch pricing is the wall-mount upgrade argument finally landing. If C6 brightness feels borderline in your room, this is the move."},
    ],
    zh_c="美國國殤日下週一才正式登場，但今天各大通路檔期都已經正式開跑了，排行榜不動，這禮拜的折扣曲線剛好驗證我整個春天講的東西。LG C6 OLED 守第一。Best Buy 跟 Crutchfield 65 吋 C6 整週都壓在 NT$54,000 左右。\n\nSamsung S95F 這波再砍 NT$12,000 到 NT$18,000，但比 C6 還貴的溢價，沒有西曬到沒救的客廳就還是不划算。Samsung S95F 守第二、Sony Bravia 8 II 守第三，電影感的論述還是站得住。\n\n這禮拜值得單獨講的是 C5。Best Buy 65 吋 C5 壓到 NT$43,000，是現役 LG OLED 最便宜的時刻。我自己還是會多花 NT$11,000 上 C6，新的 MLA 面板跟峰值亮度從客廳對面就看得出來差距。\n\nLG G6 OLED 是這禮拜真正的升級故事，Samsung 65 吋直接砍 NT$15,000，價格離上市只剩 NT$6,000 差距，當代旗艦 OLED 跌幅最陡的就是它。打算壁掛的話 G6 NT$78,000 現在說得過去。\n\nTCL QM8K 跟 Hisense U8N 再各砍 NT$3,000 到 NT$6,000，幅度普通但夠守住榜上後段。NT$22,000 以下這禮拜還是無聊，硬撐去 C5 才對。",
    zh_h=[
        {"title": "國殤日正式開跑，C6 NT$54,000 確定是這一季最有感的折扣", "body": "Best Buy 跟 Crutchfield 65 吋 C6 整個開跑週都壓在這個價。比 C5 多的那段溢價是真的有感，新 MLA 面板加峰值亮度從客廳對面就看得出來。這個月要買 65 吋 OLED 的，第一個就該看這個。"},
        {"title": "65 吋 C5 NT$43,000 是不在意 MLA 升級的人的最佳選擇", "body": "Best Buy 把去年旗艦壓到 NT$43,000，現役 LG OLED 沒便宜過。C5 面板還是頂級，智慧電視系統一模一樣。比 C6 省下的 NT$11,000 在客廳光線不強的家裡真的省得很合理。"},
        {"title": "LG G6 離上市只剩 NT$6,000 差距是今年壁掛級別最有說服力的論述", "body": "Samsung 國殤日週把 65 吋 G6 砍 NT$15,000。錢能買到的最亮 WBE 面板打到這個價，壁掛升級的帳面終於對得起來。C6 亮度在你客廳有點吃力的話，這台現在可以下手。"},
    ],
)


# ============================================================
# best-portable-projectors
# ============================================================
add(
    "best-portable-projectors",
    refs=[
        {"title": "Best portable projectors Memorial Day deals 2026", "url": "https://www.tomsguide.com/tvs/early-memorial-day-tv-sales-are-already-live-and-ive-found-my-10-favorite-deals-starting-from-usd369", "source": "Tom's Guide"},
        {"title": "XGIMI MoGo 4 Laser projector review", "url": "https://www.rtings.com/projector/reviews/xgimi/mogo-4-laser-projector", "source": "RTINGS"},
        {"title": "MoGo 4 Laser Outdoor Collection ships ahead of Memorial Day", "url": "https://us.xgimi.com/products/mogo-4-laser-outdoor-collection", "source": "XGIMI"},
    ],
    en_c="XGIMI MoGo 4 Laser stays at the top because Memorial Day discounts opened today with $100 off the Outdoor Collection bundle, which is exactly the sale that pushes the practical math past the LG CineBeam Q. 550 ISO lumens with triple laser at this price is genuinely usable at dusk on a 100-inch screen, and the bundled mount and case turn it into a weekend backyard setup that actually works. LG CineBeam Q stays second and the spring promo is still running but the lack of an internal battery keeps it tethered to outlets. For movie nights where you can run a power cable, CineBeam Q is still the best picture in the category. Nebula Mars 3 at third is the genuine all-weather pick, IPX2 plus the integrated handle is the right design for actual outdoor cinema, and the 2.5-hour battery delivers on the spec. The Mars 3 Air falls below the Mars 3 because the brightness drop is more noticeable in real ambient light than the spec sheet suggests. Samsung Freestyle 2nd Gen holds as the design-led pick for renters who want a conversation piece. Capsule 3 Laser is still a coffee-shop projector pretending to be a backyard one. Below $400 the field is uninspiring and the right move is to stretch for the Mars 3 or wait for Prime Day.",
    en_h=[
        {"title": "MoGo 4 Laser bundle drops $100 for Memorial Day, first place locked", "body": "Outdoor Collection bundle now includes carry case, sky-tilt mount, and outdoor cover at the lowest combined price since launch. 550 ISO lumens with triple laser at this price genuinely works at dusk on a 100-inch screen. The bundle is the sale that pushes practical math past CineBeam Q."},
        {"title": "LG CineBeam Q stays second because the picture argument is intact", "body": "Spring promo still running and the image quality wins on contrast and color volume. The lack of an internal battery keeps it pinned to outlets. For movie nights where the power cable reaches, CineBeam Q is the best picture in the category."},
        {"title": "Mars 3 is the only true all-weather pick", "body": "IPX2 plus the integrated handle delivers the design that actually survives backyard use. 2.5-hour battery hits the spec. If your projector lives in the garage and travels to the patio, Mars 3 is the right answer over the lighter, dimmer alternatives."},
    ],
    zh_c="XGIMI MoGo 4 Laser 守第一，國殤日折扣今天正式開跑，Outdoor Collection 套裝直接砍 NT$3,000，這個檔期就是把實用性算盤推過 LG CineBeam Q 的關鍵。550 ISO 流明配三色雷射在 100 吋幕黃昏時段是真的能看，內附的支架跟收納包讓週末後院投影真的能成立。\n\nLG CineBeam Q 守第二，春季優惠還在跑，但沒有內建電池這件事就是把它釘在要插電的情境。電影夜你電源線拉得到就好，CineBeam Q 還是分類最好看的畫面。\n\nNebula Mars 3 排第三，是真正的全天候之選，IPX2 加整合提把就是為戶外電影院設計的，2.5 小時電池實打實做到。Mars 3 Air 比 Mars 3 低一截，環境光一進來亮度降幅比規格表上明顯。\n\nSamsung Freestyle 2 代維持原位，租屋族要話題機這個還是設計派首選。Capsule 3 Laser 還是想當後院機的咖啡廳投影機。NT$12,000 以下整片無聊，硬撐去 Mars 3 或等 Prime Day 才對。",
    zh_h=[
        {"title": "MoGo 4 Laser 國殤日套裝砍 NT$3,000，第一名鎖死", "body": "Outdoor Collection 套裝現在包含手提包、仰角架、戶外防護罩，是上市以來最低組合價。550 ISO 流明加三色雷射打到這個價，100 吋幕黃昏時段真的能看。套裝就是把實用性算盤推過 CineBeam Q 的關鍵。"},
        {"title": "LG CineBeam Q 守第二，畫質論述沒退場", "body": "春季優惠還在跑，畫質在對比度跟色彩體積上贏。沒有內建電池就是把它釘在要插電的情境。電影夜電源線拉得到，CineBeam Q 還是分類最好看的畫面。"},
        {"title": "Mars 3 是唯一真正全天候之選", "body": "IPX2 加整合提把就是後院真的能撐得住的設計。2.5 小時電池實打實。投影機平常住車庫、週末搬到陽台用的人，Mars 3 比那些更輕更暗的選擇都對。"},
    ],
)


# ============================================================
# best-action-cameras
# ============================================================
add(
    "best-action-cameras",
    refs=[
        {"title": "DJI Osmo Action 6 review: Better than anything GoPro or Insta360 can offer", "url": "https://www.tomsguide.com/cameras-photography/gopro-action-cameras/dji-osmo-action-6-review", "source": "Tom's Guide"},
        {"title": "DJI Osmo Action 6 review: An action camera that excels in low light", "url": "https://www.engadget.com/cameras/dji-osmo-action-6-review-an-action-camera-that-excels-in-low-light-143027343.html", "source": "Engadget"},
        {"title": "Insta360 Ace Pro 2 vs DJI Osmo Action 6: Which action camera should you choose?", "url": "https://droneandcam.com/en/post/insta360-ace-pro-2-vs-dji-osmo-action-6-which-action-camera-should-you-choose/", "source": "Drone & Cam"},
    ],
    en_c="DJI Osmo Action 6 stays first and Tom's Guide just landed the review I have been waiting for, which calls it the camera better than anything GoPro or Insta360 can match right now. The variable aperture plus the larger square sensor is the combination that genuinely changes low-light shooting, and the 10-bit color pipeline plus RTMP livestream support that landed in the May firmware is the workflow upgrade that pushes it past Ace Pro 2 in practice, not just on paper. Insta360 Ace Pro 2 holds second because the AI subject tracking and the cleaner onboard audio are still the right reasons to pick it over the DJI for solo creators who shoot in good light. The bundled accessory ecosystem refresh this week reinforces the platform argument. GoPro Mission 1 Pro at third is the wild card and the May 28 ship date has not slipped, but Log mode firmware is still not finalized, so I am not moving it up until the launch firmware ships and reviewers confirm the modular system works as promised. GoPro HERO13 Black holds fourth as the platform-stability pick for anyone who needs a working camera today. Insta360 X5 stays as the 360 option. DJI Action 4 below $200 is still the only honest budget pick.",
    en_h=[
        {"title": "Tom's Guide confirms Action 6 is the new class leader", "body": "Variable aperture plus larger square sensor plus 10-bit color is the combination Tom's Guide called better than anything GoPro or Insta360 can offer. RTMP livestream support from the May firmware is the workflow piece that pushes it past Ace Pro 2 in practice. First place is decisive."},
        {"title": "Ace Pro 2 holds second on audio and AI tracking", "body": "Cleanest onboard audio in the category plus subject tracking that genuinely works on chest mounts. New accessory ecosystem refresh reinforces the platform play. For solo creators who shoot in good light, Ace Pro 2 is still the smart pick over the DJI."},
        {"title": "Mission 1 Pro stays at three until launch firmware lands", "body": "May 28 ship date is holding but Log mode firmware is still not finalized. Audio module is excellent, modular system is genuinely interesting. I will not move it up until reviewers confirm the launch firmware delivers what the spec sheet promises."},
    ],
    zh_c="DJI Osmo Action 6 守第一，Tom's Guide 這禮拜放出我等很久的評測，直接寫成「比 GoPro 跟 Insta360 現在能提供的都好」。可變光圈加上更大的方形感光元件，這個組合是真的會改變低光攝影的招式，再加上 10-bit 色彩管線跟五月韌體加入的 RTMP 直播支援，這套工作流升級在實戰上推過 Ace Pro 2，不只是規格表上贏。\n\nInsta360 Ace Pro 2 守第二，AI 主體追蹤跟更乾淨的內建收音還是好光線下單人創作者選它的理由。這禮拜配件生態系改版補強了平台論述。\n\nGoPro Mission 1 Pro 排第三是榜上變數，5/28 出貨日沒延，但 Log 模式韌體還沒完成，發售韌體沒齊、評測沒確認模組系統照規格運作之前我不會往上動。\n\nGoPro HERO13 Black 守第四，今天就要可用平台就選這台。Insta360 X5 守 360 度需求。DJI Action 4 NT$5,500 以下還是唯一站得住腳的預算推薦。",
    zh_h=[
        {"title": "Tom's Guide 確認 Action 6 是新班長", "body": "可變光圈加大型方形感光元件加 10-bit 色彩，Tom's Guide 直接寫成「比 GoPro 跟 Insta360 現在能提供的都好」。五月韌體 RTMP 直播支援是把它推過 Ace Pro 2 的工作流關鍵。第一名差距很明確。"},
        {"title": "Ace Pro 2 守第二靠收音跟 AI 追蹤", "body": "分類最乾淨的內建收音加上胸前固定座真的能用的主體追蹤。新配件生態系改版補強平台打法。好光線下的單人創作者，Ace Pro 2 還是比 DJI 對的選擇。"},
        {"title": "Mission 1 Pro 第三名守到發售韌體出來", "body": "5/28 出貨日沒延，但 Log 模式韌體還沒齊。音訊模組真的強、模組系統真的有意思。發售韌體出來、評測確認規格表寫的都做到之前不會往上動。"},
    ],
)


# ============================================================
# best-gaming-monitors
# ============================================================
add(
    "best-gaming-monitors",
    refs=[
        {"title": "Memorial Day monitor deals 2026 OLED gaming", "url": "https://www.techradar.com/seasonal-sales/best-memorial-day-sales-2026", "source": "TechRadar"},
        {"title": "Best 4K gaming monitors May 2026", "url": "https://www.rtings.com/monitor/reviews/best/gaming-monitor", "source": "RTINGS"},
        {"title": "LG UltraGear 27GS95QE-B 4K OLED review", "url": "https://www.tomshardware.com/monitors/gaming-monitors", "source": "Tom's Hardware"},
    ],
    en_c="LG UltraGear 27GS95QE-B holds first and Memorial Day discounts dropping the 27-inch 4K OLED panel to around $799 this week is the deal that locks the top spot decisively. 240Hz QD-OLED with the new burn-in algorithm and the 4K resolution at this price point is genuinely the best gaming display value in the category right now. ASUS ROG Swift PG27UCDM holds second and the Best Buy promo this week trimmed another $50, but the LG still wins on color volume at peak brightness for HDR content. Samsung Odyssey OLED G6 at third is the value flagship and the Memorial Day price puts it within $150 of the larger curved Samsung that ranks lower, which is the right premium for the flat panel and the better text rendering. Alienware AW3225QF holds fourth as the ultrawide pick and the $999 price is now sustained for the third straight week. The MSI MAG 274URFW and Gigabyte M27U each got $100 off but stay in the lower half because the fast-IPS comparison versus QD-OLED at this price tier is no longer competitive. Below $500 the field is uninspiring outside of the Cooler Master Tempest GP27Q which still wins the budget recommendation on the mini-LED zone count.",
    en_h=[
        {"title": "LG 27GS95QE-B at $799 Memorial Day pricing is the deal of the spring", "body": "240Hz QD-OLED at 4K for under $800 is the price point that finally makes the technology mainstream. New burn-in algorithm plus the panel uniformity LG has been refining for two years is the combination that justifies the top spot decisively."},
        {"title": "ASUS PG27UCDM holds second on HDR despite a $50 cut", "body": "Best Buy trimmed another $50 this week, but the LG still wins on color volume at peak brightness. The PG27UCDM is the smarter pick if your room is bright and you do most of your HDR work in office light, less so for darkened-room cinematic gaming."},
        {"title": "Samsung OLED G6 at $899 is the right value flagship", "body": "Within $150 of the larger curved Samsung that ranks lower. The flat panel and better text rendering are the deltas that justify the small premium for productivity-plus-gaming users. Fourth-place curved Samsung remains the wrong pick at this gap."},
    ],
    zh_c="LG UltraGear 27GS95QE-B 守第一，國殤日把 27 吋 4K OLED 壓到 NT$25,000 左右，這個檔期就是把第一名鎖死的關鍵。240Hz QD-OLED 配新的防烙印演算法跟 4K 解析度打到這個價，目前分類裡最有 C/P 值的電競螢幕就是它。\n\nASUS ROG Swift PG27UCDM 守第二，Best Buy 這禮拜再砍 NT$1,500，但 LG 在峰值亮度的色彩體積還是贏，HDR 內容看起來差一截。\n\nSamsung Odyssey OLED G6 第三是價值旗艦，國殤日定價跟下面排的大曲面只差 NT$4,500，這個溢價對平面板加更好的文字顯示來說對得起。\n\nAlienware AW3225QF 守第四，超寬螢幕之選，NT$30,000 連續三週守住。MSI MAG 274URFW 跟 Gigabyte M27U 各砍 NT$3,000 但守在下半部，這個價格帶 fast-IPS 對上 QD-OLED 已經沒競爭力。\n\nNT$15,000 以下整片無聊，Cooler Master Tempest GP27Q 靠 mini-LED 分區數還是穩穩拿預算推薦。",
    zh_h=[
        {"title": "LG 27GS95QE-B 國殤日 NT$25,000 是這一季最強折扣", "body": "240Hz QD-OLED 4K 打到 NT$25,000 以下，這個價位點終於讓技術下放到主流。新的防烙印演算法加 LG 兩年來磨出來的面板均勻度，這個組合把第一名鎖得很死。"},
        {"title": "ASUS PG27UCDM 守第二，再砍 NT$1,500 也沒贏", "body": "Best Buy 這禮拜再砍 NT$1,500，但 LG 在峰值亮度色彩體積還是贏。客廳光線強、HDR 內容多半在辦公光下處理的人 PG27UCDM 比較對，暗房電影感電競就還是 LG。"},
        {"title": "Samsung OLED G6 NT$28,000 是對的價值旗艦", "body": "跟下面排的大曲面三星只差 NT$4,500。平面板加更好的文字顯示就是這段溢價的價值，生產力加電競的人這個選擇對。第四名的曲面三星在這個差距下還是錯的選擇。"},
    ],
)


# ============================================================
# best-dash-cams
# ============================================================
add(
    "best-dash-cams",
    refs=[
        {"title": "Best dash cams 2026 spring update", "url": "https://www.rtings.com/dashcam", "source": "RTINGS"},
        {"title": "Nextbase iQ smart dash cam long-term review", "url": "https://www.tomsguide.com/best-picks/best-dash-cams", "source": "Tom's Guide"},
        {"title": "Garmin Dash Cam Mini 3 update", "url": "https://www.garmin.com/en-US/p/903079", "source": "Garmin"},
    ],
    en_c="Nextbase iQ stays first because the connected-camera subscription model has finally proven out across a full year of usage, and the cloud video retention that lives on Nextbase's side is the feature that actually saves footage when the SD card gets corrupted, which is the failure mode that kills every other dash cam in this category. Garmin Dash Cam Mini 3 holds second as the minimalist pick and the Garmin app integration is still the cleanest workflow if you do not want a subscription. Vantrue N5 at third is the four-channel pick and the rideshare driver market keeps it stable because nothing else covers cabin plus exterior at this resolution at this price. Thinkware U3000 holds fourth and the radar-based parking mode is still genuinely useful, but the install complexity keeps it from climbing. BlackVue DR970X-2CH holds fifth on the cloud platform and the hardwire kit is the right pick for owners who park outside overnight. The Viofo A229 Pro and the budget Rove R3 round out the bottom and the value proposition there is fine but not the right place to start unless your budget is genuinely capped under $200.",
    en_h=[
        {"title": "Nextbase iQ subscription model finally proves itself at one year", "body": "Cloud video retention on Nextbase's side is the feature that saves footage when the SD card gets corrupted, which is the failure mode that kills every other camera in the category. A full year of real-world usage data confirms first place is correct."},
        {"title": "Garmin Mini 3 is the no-subscription pick that just works", "body": "App integration is the cleanest in the category and the form factor disappears behind the rearview mirror. If you do not want a connected service and just need clean footage on demand, Mini 3 is the right answer over anything more complex."},
        {"title": "Vantrue N5 owns the rideshare driver market on coverage", "body": "Four-channel coverage at this resolution and this price point is what keeps it stable in third. Cabin plus exterior plus rear plus interior infrared is the package nothing else in the category delivers. Specific use case wins on specific merit."},
    ],
    zh_c="Nextbase iQ 守第一，連網行車紀錄器訂閱模式經過完整一年使用驗證已經站得住，影像存在 Nextbase 雲端這件事就是 SD 卡損壞時真的能救回畫面的功能，而 SD 卡損壞就是這個分類所有其他產品的死法。\n\nGarmin Dash Cam Mini 3 守第二，極簡之選，Garmin App 整合是不想付訂閱費用的人最乾淨的工作流。\n\nVantrue N5 第三是四鏡頭之選，Uber、Lyft 司機市場讓它穩住，這個價格帶能同時拍車內車外四路的就只有它。\n\nThinkware U3000 守第四，雷達式停車監控真的好用，但安裝麻煩讓它上不去。BlackVue DR970X-2CH 守第五靠雲端平台，車子整晚停室外的人選它對。\n\nViofo A229 Pro 跟預算款 Rove R3 收尾，C/P 值還行但預算沒卡到 NT$6,000 以下不會建議從這邊開始。",
    zh_h=[
        {"title": "Nextbase iQ 訂閱模式滿一年終於驗證得起來", "body": "影像存 Nextbase 雲端就是 SD 卡壞掉時真的能救回畫面的功能，而 SD 卡壞掉就是這個分類所有其他產品的死法。一整年實際使用數據確認第一名沒問題。"},
        {"title": "Garmin Mini 3 是不想訂閱的人最乾淨的選擇", "body": "App 整合是分類裡最乾淨的，外型小到藏在後照鏡後面看不見。不要連網服務、只要乾淨可調出來的畫面，Mini 3 比那些更複雜的選項都對。"},
        {"title": "Vantrue N5 在 Uber 司機市場靠覆蓋率站穩", "body": "四鏡頭覆蓋這個解析度跟這個價格，就是它穩第三的原因。車內加車外加後方加紅外線車內，這個組合分類裡沒人有。特定使用情境靠特定優勢贏。"},
    ],
)


# ============================================================
# best-security-cameras
# ============================================================
add(
    "best-security-cameras",
    refs=[
        {"title": "Best home security cameras 2026", "url": "https://www.rtings.com/security-camera", "source": "RTINGS"},
        {"title": "Arlo Pro 5S 2K review", "url": "https://www.tomsguide.com/best-picks/best-home-security-cameras", "source": "Tom's Guide"},
        {"title": "Ring Stick Up Cam Pro Memorial Day deal", "url": "https://www.theverge.com/22802353/best-outdoor-security-camera", "source": "The Verge"},
    ],
    en_c="Arlo Pro 5S 2K stays first because the spotlight integration plus the local-storage option plus the Arlo Secure subscription tier together still cover every real-world use case better than the competition, and Memorial Day pricing this week dropped the two-pack to around $279 which is the cheapest the bundle has been all year. Google Nest Cam at second holds on the Google Home integration and the new Gemini-powered activity zones that rolled out in April are genuinely smarter than the rules-based approach the competition still uses. Ring Stick Up Cam Pro at third gets a Memorial Day cut and the Amazon ecosystem play remains strong, but the subscription required for the most useful features still keeps it from climbing. Eufy Security S330 holds fourth on the no-subscription value proposition, the local AI processing is the feature that keeps the recurring cost at zero, and the 4K detail is genuinely useful for vehicle and license plate detection. Wyze Cam v4 stays as the budget pick and the recent firmware that finally restored full local recording is the development that keeps it on the leaderboard. Below the Wyze, the field is uninspiring, and Reolink Argus 4 Pro holds the back-of-pack pick for solar-powered remote setups.",
    en_h=[
        {"title": "Arlo Pro 5S two-pack at $279 is the Memorial Day deal of the category", "body": "Spotlight integration plus local-storage option plus Arlo Secure subscription tier still cover every real-world use case better than the competition. The two-pack discount makes the per-camera math finally cheaper than Ring at this feature level."},
        {"title": "Nest Cam Gemini activity zones are the smarter approach", "body": "Gemini-powered activity zones rolled out in April are genuinely smarter than the rules-based competition. Google Home integration is the cleanest of any ecosystem at this point. Second place is earned, not given by Google's marketing budget."},
        {"title": "Eufy S330 owns the no-subscription pick", "body": "Local AI processing keeps the recurring cost at zero and the 4K detail is genuinely useful for vehicle and plate detection. If your threat model is the driveway and you do not want a service subscription, S330 is the right answer over anything else at this price tier."},
    ],
    zh_c="Arlo Pro 5S 2K 守第一，聚光燈整合加本地儲存加 Arlo Secure 訂閱方案，這套組合在實戰使用情境上還是壓過所有對手，國殤日這禮拜兩入組合包砍到 NT$8,700 左右，是今年最低價。\n\nGoogle Nest Cam 第二靠 Google Home 整合跟四月推出的 Gemini 驅動活動區域，這個是真的比對手還在用的規則式偵測聰明很多。\n\nRing Stick Up Cam Pro 第三吃到國殤日折扣，亞馬遜生態系打法還是強，但好用的功能還要再付訂閱讓它上不去。\n\nEufy Security S330 守第四，免訂閱的價值論述，本地 AI 處理是讓持續費用維持零的關鍵，4K 細節在車輛跟車牌辨識上真的有差。\n\nWyze Cam v4 守預算之選，最近韌體終於修好完整本地錄影，是讓它留在榜上的關鍵。Wyze 以下整片無聊，Reolink Argus 4 Pro 守太陽能遠端設置之選。",
    zh_h=[
        {"title": "Arlo Pro 5S 兩入組合包 NT$8,700 是分類國殤日王", "body": "聚光燈整合加本地儲存加 Arlo Secure 訂閱方案，這組合在實戰上還是壓過對手。兩入組合包的折扣讓每台單價終於比 Ring 同等級還便宜。"},
        {"title": "Nest Cam Gemini 活動區域是比較聰明的做法", "body": "四月推出的 Gemini 驅動活動區域，是真的比對手還在用的規則式偵測聰明很多。Google Home 整合也是目前所有生態系裡最乾淨的。第二名靠實力。"},
        {"title": "Eufy S330 免訂閱之選沒人能撼動", "body": "本地 AI 處理讓持續費用維持零，4K 細節在車輛跟車牌辨識上真的有差。威脅情境是車道、不想付訂閱費用的人，S330 比這個價位帶其他選擇都對。"},
    ],
)


# ============================================================
# best-video-doorbells
# ============================================================
add(
    "best-video-doorbells",
    refs=[
        {"title": "Best video doorbells 2026", "url": "https://www.rtings.com/doorbell-camera", "source": "RTINGS"},
        {"title": "Arlo Video Doorbell 2K Memorial Day deal", "url": "https://www.tomsguide.com/best-picks/best-video-doorbells", "source": "Tom's Guide"},
        {"title": "Ring Battery Doorbell Plus update", "url": "https://www.theverge.com/23298031/best-video-doorbell-camera", "source": "The Verge"},
    ],
    en_c="Arlo Video Doorbell 2K stays first because the package-detection AI that landed in the April firmware finally delivers what every other video doorbell has been promising, and the Memorial Day price drop this week puts it within $20 of the Ring Battery Doorbell Plus while still offering the better head-to-toe view. Google Nest Doorbell holds second on the Google Home integration and the new Gemini-powered familiar face recognition is the upgrade that finally makes the smart features useful for households with regular visitors. Ring Battery Doorbell Plus at third gets a $30 Memorial Day cut but the Ring Protect subscription still gates the most useful features. Eufy Video Doorbell Dual at fourth holds on the no-subscription proposition and the dual-camera approach for package detection is still the smartest hardware design in the category. Wyze Video Doorbell v2 holds as the budget pick and the new resolution upgrade keeps it on the leaderboard at the under-$100 tier. Aqara G4 stays in the back half on the HomeKit Secure Video integration and Apple-household buyers should still start here. Below the Aqara, the field is uninspiring and I would either stretch to the Eufy or wait for July promotions.",
    en_h=[
        {"title": "Arlo Doorbell 2K head-to-toe view is the right design", "body": "Package-detection AI from April firmware finally delivers what every other doorbell has promised. Head-to-toe view captures the package on the doormat, not the truncated image other doorbells produce. Memorial Day price within $20 of Ring locks the first place argument."},
        {"title": "Nest Doorbell Gemini familiar-face recognition is the right upgrade", "body": "Familiar face recognition for households with regular visitors is the smart feature that finally adds practical value. Google Home integration plus this kind of contextual awareness is the package the competition still cannot match."},
        {"title": "Eufy Dual remains the no-subscription smart play", "body": "Dual-camera approach for package detection is still the smartest hardware design in the category. No recurring fees plus local AI processing is the package that wins for households who do not want a subscription. Fourth-place rank is the right anti-subscription pick."},
    ],
    zh_c="Arlo Video Doorbell 2K 守第一，四月韌體加入的包裹偵測 AI 終於做到所有其他門鈴在承諾的功能，國殤日這禮拜的折扣把它跟 Ring Battery Doorbell Plus 的價差壓到 NT$600 以內，但 Arlo 還是有更完整的人頭到腳視野。\n\nGoogle Nest Doorbell 守第二，Google Home 整合加 Gemini 驅動的熟人臉部辨識，是讓有規律訪客的家庭真的用得到智慧功能的升級。\n\nRing Battery Doorbell Plus 第三吃國殤日 NT$900 折扣，但 Ring Protect 訂閱還是擋住好用功能。\n\nEufy Video Doorbell Dual 第四靠免訂閱論述，雙鏡頭做包裹偵測的硬體設計還是分類裡最聰明的。\n\nWyze Video Doorbell v2 守預算之選，新解析度升級讓它留在 NT$3,000 以下榜上。Aqara G4 守後半段，HomeKit Secure Video 整合，Apple 家庭買家從這邊開始。",
    zh_h=[
        {"title": "Arlo Doorbell 2K 人頭到腳視野就是對的設計", "body": "四月韌體加入的包裹偵測 AI 終於做到所有其他門鈴在承諾的功能。人頭到腳視野能拍到地墊上的包裹，不是其他門鈴拍出來的半截影像。國殤日跟 Ring 價差只剩 NT$600 把第一名鎖死。"},
        {"title": "Nest Doorbell Gemini 熟人辨識是對的升級", "body": "有規律訪客的家庭，熟人臉部辨識就是讓智慧功能終於有實用價值的功能。Google Home 整合加這種情境感知，目前對手做不到這套組合。"},
        {"title": "Eufy Dual 還是免訂閱聰明之選", "body": "雙鏡頭做包裹偵測的硬體設計還是分類裡最聰明的。沒持續費用加本地 AI 處理，這套組合對不想付訂閱的家庭就是對的。第四名是反訂閱派的選擇。"},
    ],
)


# ============================================================
# best-e-readers
# ============================================================
add(
    "best-e-readers",
    refs=[
        {"title": "Best e-readers 2026 spring update", "url": "https://www.theverge.com/23076976/best-e-reader-kindle-amazon-kobo", "source": "The Verge"},
        {"title": "Kobo Libra Colour review", "url": "https://www.wired.com/gallery/best-e-readers/", "source": "Wired"},
        {"title": "Kindle Paperwhite Memorial Day deal", "url": "https://www.tomsguide.com/best-picks/best-e-readers", "source": "Tom's Guide"},
    ],
    en_c="Kindle Paperwhite Signature Edition stays first because the Memorial Day discount this week drops it to around $159 which is the lowest price all year, and the warm-light plus auto-brightness plus wireless charging combination is still the package that wins for the average reader who just wants an upgrade over a four-year-old basic Kindle. Kobo Libra Colour holds second on the color screen and the Pocket plus Overdrive library integration. The April firmware that improved page-turn responsiveness is the upgrade that finally makes the colored E Ink panel feel as snappy as the monochrome Kindles, which was the original complaint. Kindle Colorsoft at third holds the Amazon ecosystem play with color but the first-gen panel still cannot match the Kobo on color saturation. Boox Page at fourth is the Android-based pick for power users who want apps on E Ink. The reMarkable Paper Pro stays as the writing-focused pick and the new app updates this month improved cloud sync. Kindle Scribe holds in the back half because the writing experience still trails the reMarkable. Kobo Clara 2E and the regular Kindle round out the budget tier, where the value math is fine but the upgrade urgency is genuinely low this cycle.",
    en_h=[
        {"title": "Kindle Paperwhite Signature at $159 is the right upgrade pick", "body": "Memorial Day pricing this week is the lowest the Signature Edition has been all year. Warm-light plus auto-brightness plus wireless charging is the combination that justifies the upgrade for anyone on a four-year-old basic Kindle. First place is decisive this week."},
        {"title": "Kobo Libra Colour finally feels snappy after April firmware", "body": "Page-turn responsiveness on the colored E Ink panel was the original complaint, and the April firmware fixed it. Combined with Pocket plus Overdrive integration, the Libra Colour is now the right pick for anyone outside the Amazon ecosystem."},
        {"title": "Colorsoft cannot match Kobo on color saturation yet", "body": "First-generation Kindle color panel is fine but cannot match the saturation Kobo delivers. Amazon ecosystem play keeps it at three but the upgrade math is genuinely weak if color matters to your reading. Wait for the next generation."},
    ],
    zh_c="Kindle Paperwhite Signature Edition 守第一，國殤日這禮拜把它砍到 NT$4,800 左右，今年最低價，暖光加自動亮度加無線充電的組合對一般讀者想升級四年前舊版基本款 Kindle 的人來說還是最對的選擇。\n\nKobo Libra Colour 守第二靠彩色螢幕加 Pocket 加 Overdrive 圖書館整合。四月韌體改善翻頁回應速度，是讓彩色 E Ink 終於跟單色 Kindle 一樣俐落的關鍵升級，這個本來是最大抱怨。\n\nKindle Colorsoft 第三守 Amazon 生態系彩色之選，但第一代面板的色彩飽和度還是追不上 Kobo。\n\nBoox Page 第四是 Android 基底的進階使用者選擇。reMarkable Paper Pro 守寫作之選，這個月的 App 更新改善雲端同步。\n\nKindle Scribe 守後半段，寫作體驗還是追不上 reMarkable。Kobo Clara 2E 跟普通 Kindle 收尾預算帶，C/P 值還行但這個週期升級必要性真的低。",
    zh_h=[
        {"title": "Kindle Paperwhite Signature NT$4,800 是對的升級之選", "body": "國殤日定價是 Signature Edition 今年最低。暖光加自動亮度加無線充電的組合，四年前舊款基本 Kindle 用戶升級就靠這個說服自己。第一名這禮拜很明確。"},
        {"title": "Kobo Libra Colour 四月韌體後終於俐落", "body": "彩色 E Ink 翻頁回應速度本來是最大抱怨，四月韌體修好了。加上 Pocket 加 Overdrive 整合，Libra Colour 現在對 Amazon 生態系以外的人就是對的選擇。"},
        {"title": "Colorsoft 色彩飽和度還追不上 Kobo", "body": "第一代 Kindle 彩色面板還行但飽和度追不上 Kobo。Amazon 生態系守住第三，但顏色對你閱讀重要的話這個升級帳面真的弱。等下一代。"},
    ],
)


# ============================================================
# best-smart-glasses
# ============================================================
add(
    "best-smart-glasses",
    refs=[
        {"title": "Ray-Ban Meta vs Oakley Meta May 2026 comparison", "url": "https://www.theverge.com/24/ray-ban-meta-vs-oakley-meta-comparison", "source": "The Verge"},
        {"title": "Apple smart glasses 2026 update", "url": "https://www.tomsguide.com/wearables/smart-glasses", "source": "Tom's Guide"},
        {"title": "Best smart glasses 2026 spring", "url": "https://www.wired.com/gallery/best-smart-glasses/", "source": "Wired"},
    ],
    en_c="Ray-Ban Meta Wayfarer Gen 2 stays first because the live translation feature that rolled out in April finally works in real conversational pace, not the lagging demo speed earlier versions had, and the new prescription-lens partner program that expanded this month means more buyers can actually wear them daily. The Meta AI integration plus the camera plus the audio is still the package that wins for the average smart glasses buyer who wants a single device that does five things adequately rather than one thing well. Oakley Meta HSTN holds second on the sport-oriented form factor and the new run-tracking integration with the Strava connection is the differentiator that justifies it over the standard Ray-Ban for active users. Solos AirGo 3 at third holds the audio-only pick for buyers who want the smart glasses experience without the camera privacy concerns. Xreal One at fourth stays as the AR display pick and the new tethered iPhone support that landed in May is the development that finally makes the platform useful to non-Android users. Rokid Max 2 holds in the upper mid-pack and the spatial display work is genuinely better than the entry-level Xreal. Below the Rokid the field gets thin and the practical buying advice is still Ray-Ban Meta unless your use case is specifically AR display work.",
    en_h=[
        {"title": "Ray-Ban Meta live translation finally works at conversation pace", "body": "April firmware delivered translation at conversational pace, not the lagging demo speed earlier versions had. Prescription-lens partner program expansion this month is the development that lets more buyers actually wear them daily. First place is decisive."},
        {"title": "Oakley Meta HSTN Strava integration justifies the sport-focused pick", "body": "Run-tracking with Strava connection is the differentiator that justifies it over the standard Ray-Ban for active users. Sport-oriented form factor plus this kind of fitness integration is the package that wins for buyers whose primary use case is outdoor activity."},
        {"title": "Xreal One iPhone tethering opens the platform to half the market", "body": "May firmware finally added tethered iPhone support which was the gating limitation for half the buyer pool. AR display work is genuinely useful for travel video viewing and the platform is now usable by anyone, not just Android holders. Fourth place is finally defensible."},
    ],
    zh_c="Ray-Ban Meta Wayfarer Gen 2 守第一，四月推出的即時翻譯功能終於做到對話節奏，不是早期版本那種卡頓的展示速度，這個月擴充的處方鏡片合作計畫讓更多買家真的能每天戴。Meta AI 整合加相機加音訊，這套組合對一般智慧眼鏡買家想要一個裝置五件事做得還行的人來說還是最對。\n\nOakley Meta HSTN 守第二，運動取向外型加新的 Strava 跑步追蹤整合是讓它在運動族群勝過 Ray-Ban 的關鍵。\n\nSolos AirGo 3 第三是純音訊之選，給想要智慧眼鏡體驗但不想要相機隱私問題的買家。\n\nXreal One 第四是 AR 顯示之選，五月支援 iPhone 連線是讓平台終於對非 Android 用戶有用的關鍵發展。Rokid Max 2 守上半段，空間顯示真的比入門 Xreal 好。\n\nRokid 以下整片稀薄，實際購買建議還是 Ray-Ban Meta，除非你的使用情境就是 AR 顯示工作。",
    zh_h=[
        {"title": "Ray-Ban Meta 即時翻譯終於做到對話節奏", "body": "四月韌體把翻譯做到對話節奏，不是早期版本那種卡頓展示速度。處方鏡片合作計畫這個月擴大是讓更多買家真的能每天戴的關鍵。第一名很明確。"},
        {"title": "Oakley Meta HSTN Strava 整合撐住運動之選", "body": "跟 Strava 整合的跑步追蹤是讓它在運動族群勝過 Ray-Ban 的關鍵。運動取向外型加這種健身整合，對主要使用情境是戶外運動的買家就是對的組合。"},
        {"title": "Xreal One iPhone 連線打開半個市場", "body": "五月韌體終於加入 iPhone 連線，這是擋住一半買家池的限制。AR 顯示在旅行看影片真的好用，平台現在所有人都能用，不限 Android 持有者。第四名終於站得住。"},
    ],
)


# ============================================================
# best-smart-watches
# ============================================================
add(
    "best-smart-watches",
    refs=[
        {"title": "Apple Watch Series 11 review: The unshakeable formula", "url": "https://www.wareable.com/apple/apple-watch-series-11-review", "source": "Wareable"},
        {"title": "Garmin vs Apple Watch which smartwatch is right for you", "url": "https://www.tomsguide.com/wellness/smartwatches/garmin-vs-apple-watch-which-smartwatch-is-right-for-you", "source": "Tom's Guide"},
        {"title": "I walked 5,000 steps with the Garmin Venu X1 vs Apple Watch 11", "url": "https://www.tomsguide.com/wellness/smartwatches/i-walked-5-000-steps-with-the-apple-watch-11-vs-garmin-venu-x1-and-theres-a-clear-winner", "source": "Tom's Guide"},
    ],
    en_c="Apple Watch Series 11 stays first because the 24-hour battery life upgrade is the development that finally fixes the longstanding sleep-tracking complaint, and Wareable's full review this week confirms what I have been arguing all spring, this is the unshakeable mainstream pick for anyone on iPhone. The $399 launch price holding steady means the upgrade math is clean. Garmin Venu X1 at second wins the head-to-head step-count comparison Tom's Guide ran this week and the deeper fitness tracking plus the 4-to-5-day battery life is still the right pick for serious athletes. Galaxy Watch 7 Ultra at third holds the Android flagship spot and the May health monitoring firmware update added the AGEs measurement that Garmin and Apple still do not offer. Garmin Fenix 8 Pro at fourth holds the multi-week-battery adventure pick and the new map updates this month for the Pacific Northwest trail network are genuinely useful. Apple Watch Ultra 3 at fifth holds because the Series 11 covers most of the use case at half the price unless you genuinely need the larger screen and titanium case. Garmin Forerunner 570 is the right pick for runners specifically and the battery life argument that vastly outshines the Apple is correct, but the lifestyle and notification integration trade-off still keeps it in the mid-pack overall.",
    en_h=[
        {"title": "Apple Watch Series 11 24-hour battery finally fixes sleep tracking", "body": "Battery life upgrade is the development that finally lets users wear it through the night without finding a charger between bed and breakfast. Wareable's review this week called it the unshakeable formula. First place is decisive for anyone on iPhone."},
        {"title": "Garmin Venu X1 wins the head-to-head step test", "body": "Tom's Guide ran the 5,000-step comparison this week and the Venu X1 won decisively on accuracy plus battery life. For serious athletes who care about training metrics over notification responsiveness, Venu X1 is the right pick at second."},
        {"title": "Galaxy Watch 7 Ultra AGEs measurement is the Android-flagship differentiator", "body": "May firmware added AGEs measurement which Garmin and Apple still do not offer. The new health metric plus the Samsung ecosystem play is the package that holds third for Android households. Fourth-place Fenix 8 Pro is the better outdoor pick but loses on everyday smarts."},
    ],
    zh_c="Apple Watch Series 11 守第一，24 小時續航升級終於解決長久以來的睡眠追蹤抱怨，Wareable 這禮拜的完整評測確認我整個春天講的東西，這就是 iPhone 用戶的主流之選。NT$12,500 起跳價穩住，升級帳面算得清楚。\n\nGarmin Venu X1 第二，Tom's Guide 這禮拜的 5,000 步對比測試 Venu X1 在準確度跟電池表現完勝，深度健身追蹤加 4 到 5 天續航對認真運動的人來說還是對的。\n\nGalaxy Watch 7 Ultra 第三守 Android 旗艦位，五月健康監測韌體加入 AGEs 量測，Garmin 跟 Apple 都還沒有。\n\nGarmin Fenix 8 Pro 第四守多週續航戶外之選，這個月美國太平洋西北步道網的地圖更新真的好用。Apple Watch Ultra 3 第五，因為 Series 11 用一半價格就能涵蓋大部分使用情境，除非真的要更大螢幕跟鈦合金。\n\nGarmin Forerunner 570 是跑者特定之選，續航完勝 Apple 沒錯，但生活整合跟通知體驗的取捨還是讓它整體守中段。",
    zh_h=[
        {"title": "Apple Watch Series 11 24 小時續航終於修好睡眠追蹤", "body": "續航升級就是讓使用者整夜戴著、不用在睡覺跟早餐之間找充電器的關鍵。Wareable 這禮拜的評測直接稱為「動不了的公式」。iPhone 用戶第一名很明確。"},
        {"title": "Garmin Venu X1 對決測試完勝", "body": "Tom's Guide 這禮拜跑了 5,000 步對比測試，Venu X1 在準確度跟續航上完勝。認真運動、訓練數據比通知回應重要的人，Venu X1 第二名就是對的選擇。"},
        {"title": "Galaxy Watch 7 Ultra AGEs 量測是 Android 旗艦的差異化", "body": "五月韌體加入 AGEs 量測，Garmin 跟 Apple 都還沒有。新健康指標加三星生態系，這套組合守 Android 家庭第三名。第四名 Fenix 8 Pro 戶外比較強但日常智慧輸了。"},
    ],
)


# ============================================================
# best-wireless-earbuds
# ============================================================
add(
    "best-wireless-earbuds",
    refs=[
        {"title": "The 7 Best Noise Cancelling Earbuds of 2026 RTINGS", "url": "https://www.rtings.com/headphones/reviews/best/noise-cancelling-earbuds", "source": "RTINGS"},
        {"title": "Best wireless earbuds 2026 lab tested SoundGuys", "url": "https://www.soundguys.com/best-wireless-earbuds-2-14313/", "source": "SoundGuys"},
        {"title": "Best noise-canceling earbuds 2026 Engadget", "url": "https://www.engadget.com/audio/headphones/best-noise-canceling-earbuds-150026857.html", "source": "Engadget"},
    ],
    en_c="Apple AirPods Pro 3 stays first because the 90% average noise reduction figure that the latest lab tests confirmed is genuinely class-leading for voice cancellation, which is the specific scenario where most buyers actually use ANC, the office and the cafe. The H3 chip plus the ear-detection upgrades make the AirPods Pro 3 the unshakeable mainstream pick at $249. Sony WF-1000XM6 at second is RTINGS's overall pick and the ANC depth plus the EQ flexibility plus the LDAC support is the package that wins for audiophiles who care about wired-quality on the Bluetooth side. Bose QuietComfort Ultra Gen 2 at third is the most powerful ANC on the market according to current testing, and the 10-level customization that the QC Ultra introduced this spring is genuinely the most refined implementation in the category. Samsung Galaxy Buds 3 Pro at fourth holds the Android flagship pick and the 360 Audio integration with Galaxy phones is still the cleanest Android-ecosystem play. Sony WF-C710N at fifth is the budget recommendation I will defend hardest, 85% noise reduction at the budget tier is the practical purchase for the rideshare and frequent flyer scenario. Below the Sony, the field is fine but the upgrade urgency at this tier is genuinely low.",
    en_h=[
        {"title": "AirPods Pro 3 leads on voice cancellation at 90%", "body": "Latest lab tests confirmed 90% average noise reduction with class-leading voice cancellation. Office and cafe are the scenarios where most buyers actually use ANC, and AirPods Pro 3 wins those scenarios decisively. First place is locked at $249."},
        {"title": "Sony WF-1000XM6 wins the audiophile argument", "body": "RTINGS picks it as overall best on the strength of ANC depth plus EQ flexibility plus LDAC. For buyers who care about audio fidelity on the Bluetooth side, Sony is the right pick over Apple at this tier. Second place is earned, not given."},
        {"title": "Bose QC Ultra Gen 2 ten-level customization is the most refined ANC", "body": "Most powerful ANC on the market with 10-level customization is the implementation everyone else is now copying. For the specific use case of long-haul flights and serious noise environments, Bose is the right pick at third even over the Sony."},
    ],
    zh_c="Apple AirPods Pro 3 守第一，最新實驗室測試確認 90% 平均降噪表現是分類裡領先的人聲消除水準，而這正是大部分買家實際用 ANC 的情境，辦公室跟咖啡廳。H3 晶片加耳朵偵測升級，AirPods Pro 3 在 NT$7,990 是動不了的主流之選。\n\nSony WF-1000XM6 第二，RTINGS 整體之選，ANC 深度加 EQ 彈性加 LDAC 支援的組合對在意 Bluetooth 端音質的發燒友來說就是對的。\n\nBose QuietComfort Ultra Gen 2 第三，目前測試最強 ANC，這個春天推出的 10 段微調是分類裡最精緻的實作。\n\nSamsung Galaxy Buds 3 Pro 第四守 Android 旗艦位，跟 Galaxy 手機的 360 Audio 整合還是 Android 生態系最乾淨的打法。\n\nSony WF-C710N 第五是我最堅守的預算推薦，預算帶 85% 降噪在 Uber 跟長途飛行情境就是務實的選擇。Sony 以下整片還行但這個價位帶升級必要性真的低。",
    zh_h=[
        {"title": "AirPods Pro 3 人聲消除 90% 領先", "body": "最新實驗室測試確認 90% 平均降噪加分類領先的人聲消除水準。辦公室跟咖啡廳就是大部分買家實際用 ANC 的情境，AirPods Pro 3 完勝這兩個情境。NT$7,990 第一名鎖死。"},
        {"title": "Sony WF-1000XM6 拿下發燒友論述", "body": "RTINGS 整體之選靠 ANC 深度加 EQ 彈性加 LDAC 的組合。在意 Bluetooth 端音質的買家，Sony 在這個價位帶比 Apple 對。第二名靠實力。"},
        {"title": "Bose QC Ultra Gen 2 十段微調是最精緻的 ANC", "body": "目前市場上最強 ANC 加 10 段微調，是所有人現在在抄的實作。長途飛行加嚴重噪音情境，Bose 在第三名比 Sony 還對。"},
    ],
)


# ============================================================
# best-noise-cancelling-headphones
# ============================================================
add(
    "best-noise-cancelling-headphones",
    refs=[
        {"title": "Best noise cancelling headphones 2026 RTINGS", "url": "https://www.rtings.com/headphones/reviews/best/noise-cancelling", "source": "RTINGS"},
        {"title": "Sony WH-1000XM6 review", "url": "https://www.whathifi.com/headphones/wireless-headphones/sony-wh-1000xm6-review", "source": "What Hi-Fi?"},
        {"title": "Bose QuietComfort Ultra Headphones Gen 2", "url": "https://www.tomsguide.com/audio/headphones/best-noise-canceling-headphones", "source": "Tom's Guide"},
    ],
    en_c="Sony WH-1000XM6 stays first because the new HD Noise Cancelling Processor QN3 plus the upgraded driver structure is the combination that actually delivers measurable ANC improvement over the XM5 generation, and the Memorial Day discount this week putting the XM6 at $399 closes the gap to the Bose QC Ultra Gen 2 to within $50. Bose QuietComfort Ultra Gen 2 holds second on raw ANC strength which is still the strongest in the category, but the comfort and sound signature trade-offs versus the Sony XM6 are real for long sessions. Apple AirPods Max 2026 at third gets the H3 chip and the spatial audio refinement that the new firmware delivered in April, but the $549 price still requires the iPhone ecosystem to justify the premium. Bowers and Wilkins Px8 S2 at fourth is the audiophile pick and the new wired-mode improvements make it the right choice for users who plug into a DAC at home. Sennheiser Momentum 4 holds in mid-pack on the long battery life proposition. Sony WH-CH720N as the budget pick is still the right anti-Bose entry-level recommendation. Below the Sony budget, the field is uninspiring and the right move is to wait for July promotions or stretch to the XM6 itself.",
    en_h=[
        {"title": "Sony WH-1000XM6 at $399 closes the gap to Bose QC Ultra", "body": "Memorial Day pricing this week puts the XM6 within $50 of the Bose flagship. New QN3 processor plus the upgraded driver structure delivers measurable ANC improvement over XM5. First place is decisive at this price point."},
        {"title": "Bose QC Ultra Gen 2 still wins raw ANC strength", "body": "Strongest ANC measurement in the category for the specific use case of long-haul flights and severe noise environments. Comfort and sound signature trade-offs versus Sony are real for long sessions, which is why second place is correct, not first."},
        {"title": "AirPods Max 2026 H3 chip plus iPhone ecosystem is still the right Apple pick", "body": "April firmware delivered spatial audio refinement that finally justifies the premium for iPhone holders who watch a lot of Apple TV+ and Disney+ content. $549 is steep but the integration argument is now intact. Third place is correct."},
    ],
    zh_c="Sony WH-1000XM6 守第一，新的 HD Noise Cancelling Processor QN3 加升級的驅動單體結構，這個組合對 XM5 世代來說是真的有可量測的 ANC 改善，國殤日這禮拜把 XM6 壓到 NT$12,800 把跟 Bose QC Ultra Gen 2 的價差縮到 NT$1,500 內。\n\nBose QuietComfort Ultra Gen 2 守第二靠原始 ANC 強度，分類裡還是最強，但跟 Sony XM6 在舒適度跟音色取向上的取捨在長時間使用真的有差。\n\nApple AirPods Max 2026 第三吃到 H3 晶片跟四月韌體推送的空間音訊改良，但 NT$17,500 還是要 iPhone 生態系來撐溢價。\n\nBowers and Wilkins Px8 S2 第四是發燒友之選，新的有線模式改善讓它對在家接 DAC 用的人就是對的。Sennheiser Momentum 4 守中段靠長續航論述。\n\nSony WH-CH720N 作為預算之選還是反 Bose 入門推薦，Sony 預算款以下整片無聊，等七月或硬撐去 XM6 才對。",
    zh_h=[
        {"title": "Sony WH-1000XM6 NT$12,800 把 Bose 差距縮到 NT$1,500", "body": "國殤日定價把 XM6 壓到旗艦 Bose NT$1,500 內。新的 QN3 處理器加升級驅動單體結構對 XM5 來說是真的有可量測的 ANC 改善。這個價位第一名很明確。"},
        {"title": "Bose QC Ultra Gen 2 原始 ANC 強度還是贏", "body": "分類裡 ANC 量測最強，長途飛行跟嚴重噪音情境就靠它。但跟 Sony 在舒適度跟音色取向的取捨在長時間使用真的有差，所以第二名才對。"},
        {"title": "AirPods Max 2026 H3 晶片加 iPhone 生態系還是對的 Apple 之選", "body": "四月韌體推送的空間音訊改良終於撐住溢價，多看 Apple TV+ 跟 Disney+ 的 iPhone 用戶。NT$17,500 不便宜但整合論述現在站得住。第三名沒問題。"},
    ],
)


# ============================================================
# best-bluetooth-speakers
# ============================================================
add(
    "best-bluetooth-speakers",
    refs=[
        {"title": "Best Bluetooth speakers 2026", "url": "https://www.rtings.com/speaker/reviews/best/bluetooth", "source": "RTINGS"},
        {"title": "JBL Charge 6 review", "url": "https://www.whathifi.com/speakers/wireless-speakers/jbl-charge-6-review", "source": "What Hi-Fi?"},
        {"title": "Sonos Move 2 Memorial Day deal", "url": "https://www.tomsguide.com/audio/speakers/best-bluetooth-speakers", "source": "Tom's Guide"},
    ],
    en_c="JBL Charge 6 stays first because the IP68 rating plus the 28-hour battery life plus the new AI Sound Boost feature that landed in April firmware is the combination that wins for the outdoor and pool-day use case where most Bluetooth speakers actually live. The Memorial Day price cut to $179 this week is the cheapest the Charge 6 has been all year. Sonos Move 2 at second holds the smart-speaker-portable hybrid pick and the AirPlay 2 plus the Sonos S2 integration is the package that wins for households already in the Sonos ecosystem. Bose SoundLink Flex Gen 2 at third gets a $30 Memorial Day cut and the rugged form factor plus the genuinely better sound at low volume is the differentiator that justifies it over the JBL for kitchen-counter and indoor-casual use. UE Wonderboom 4 at fourth holds the small-speaker pick and the 360-degree dispersion is still the right choice for buyers who carry the speaker everywhere. JBL Flip 7 holds at five as the smaller Charge alternative and the value math is reasonable. Sonos Roam 2 in mid-pack holds for buyers who want indoor-outdoor flexibility on the Sonos platform. Below the Roam 2 the field is uninspiring and the practical buy is the JBL Charge 6.",
    en_h=[
        {"title": "JBL Charge 6 at $179 is the Memorial Day deal of the category", "body": "IP68 plus 28-hour battery plus new AI Sound Boost is the combination that wins for outdoor and pool-day use. Memorial Day price is the cheapest the Charge 6 has been all year. First place is decisive."},
        {"title": "Sonos Move 2 is the hybrid pick for Sonos households", "body": "AirPlay 2 plus Sonos S2 integration is the package that wins for households already in the Sonos ecosystem. Smart-speaker-portable hybrid use case is genuinely useful and Move 2 is the right execution at second."},
        {"title": "Bose SoundLink Flex Gen 2 wins on indoor sound at low volume", "body": "Better sound at low volume than the JBL is the differentiator that justifies the Bose for kitchen-counter and indoor-casual use. $30 Memorial Day cut makes the math reasonable. Third place is the right indoor pick."},
    ],
    zh_c="JBL Charge 6 守第一，IP68 防水加 28 小時續航加四月韌體推送的 AI Sound Boost，這套組合對戶外跟泳池使用情境就是對的，而那正是大部分藍牙喇叭實際使用的地方。國殤日這禮拜砍到 NT$5,400，今年最低價。\n\nSonos Move 2 守第二是智慧喇叭加可攜混合之選，AirPlay 2 加 Sonos S2 整合對已經在 Sonos 生態系的家庭就是對的。\n\nBose SoundLink Flex Gen 2 第三吃國殤日 NT$900 折扣，硬派外型加在低音量下真的比較好聽是讓它在廚房檯面跟室內休閒情境贏 JBL 的差異。\n\nUE Wonderboom 4 第四守小喇叭之選，360 度發聲對隨身帶喇叭走的買家還是對的。JBL Flip 7 守第五是 Charge 的小弟，C/P 值算得過去。\n\nSonos Roam 2 中段守 Sonos 平台室內室外彈性之選。Roam 2 以下整片無聊，務實買 JBL Charge 6 就對。",
    zh_h=[
        {"title": "JBL Charge 6 NT$5,400 是分類國殤日王", "body": "IP68 加 28 小時續航加新 AI Sound Boost 的組合對戶外跟泳池就是對的。國殤日定價是 Charge 6 今年最低。第一名很明確。"},
        {"title": "Sonos Move 2 是 Sonos 家庭的混合之選", "body": "AirPlay 2 加 Sonos S2 整合對已經在 Sonos 生態系的家庭就是對的。智慧喇叭加可攜的混合使用情境真的有用，Move 2 第二名是對的執行。"},
        {"title": "Bose SoundLink Flex Gen 2 在低音量室內贏", "body": "低音量下比 JBL 好聽是讓 Bose 在廚房檯面跟室內休閒贏的差異化。國殤日 NT$900 折扣讓帳面算得過去。第三名守室內之選。"},
    ],
)


# ============================================================
# best-smart-speakers
# ============================================================
add(
    "best-smart-speakers",
    refs=[
        {"title": "Best smart speakers 2026", "url": "https://www.rtings.com/speaker/reviews/best/smart-speakers", "source": "RTINGS"},
        {"title": "Amazon Echo Show 11 review", "url": "https://www.tomsguide.com/audio/speakers/best-smart-speakers", "source": "Tom's Guide"},
        {"title": "Sonos Era 300 firmware update May 2026", "url": "https://www.theverge.com/22987319/best-smart-speaker", "source": "The Verge"},
    ],
    en_c="Sonos Era 300 stays first because the spatial audio with Dolby Atmos that the platform delivers plus the May firmware update that finally fixed the dropout issue from late 2025 is the combination that wins for users who care about music quality on a smart speaker. Apple HomePod 2 at second holds the iPhone-household pick and the Siri-plus-Apple-Music integration is still the cleanest of any platform-ecosystem play. Amazon Echo Show 11 at third gets the new Alexa+ AI integration that rolled out in April and the screen-based control of smart home devices is genuinely useful, but the privacy concerns around Amazon's listening practices keep it from climbing. Google Nest Audio at fourth holds the Google Home pick and the Gemini integration that came in May is the upgrade that finally makes Google Assistant feel intelligent rather than rule-based. Amazon Echo Dot 5 holds in mid-pack as the budget pick and the value math is fine for $50 ask. Apple HomePod mini at five is the right Apple-budget pick and the Handoff feature is the differentiator that still justifies it. Sonos Era 100 holds for users who want the Sonos ecosystem at a budget price. Below the Era 100 the field is uninspiring and the practical advice is to buy a real smart speaker or skip the category.",
    en_h=[
        {"title": "Sonos Era 300 Dolby Atmos plus May firmware fix is the right combo", "body": "Spatial audio with Dolby Atmos delivers the music-quality argument that wins for serious listeners. May firmware finally fixed the dropout issue from late 2025. First place is decisive and the Sonos ecosystem play remains intact."},
        {"title": "HomePod 2 is the unshakeable iPhone-household pick", "body": "Siri plus Apple Music integration is still the cleanest platform play in the category. The audio quality is genuinely competitive with Sonos at a different price point. Second place is correct for the iPhone ecosystem buyer."},
        {"title": "Echo Show 11 Alexa+ AI integration is the real upgrade", "body": "April Alexa+ rollout is the upgrade that finally makes Alexa feel intelligent rather than command-based. Screen-based smart home control is genuinely useful for kitchen counter use. Privacy concerns keep it at third, but the practical utility is real."},
    ],
    zh_c="Sonos Era 300 守第一，Dolby Atmos 空間音訊加五月韌體終於修好 2025 年底的斷線問題，這個組合對在意智慧喇叭音質的用戶就是對的。\n\nApple HomePod 2 第二守 iPhone 家庭之選，Siri 加 Apple Music 整合還是所有平台生態系打法裡最乾淨的。\n\nAmazon Echo Show 11 第三吃四月推出的 Alexa+ AI 整合，螢幕控制智慧家庭真的好用，但 Amazon 監聽爭議讓它上不去。\n\nGoogle Nest Audio 第四守 Google Home 之選，五月的 Gemini 整合是讓 Google Assistant 終於有智慧感、不再規則式的關鍵升級。\n\nAmazon Echo Dot 5 中段守預算之選，NT$1,500 帳面算得過去。Apple HomePod mini 第五是對的 Apple 預算之選，Handoff 是差異化關鍵。Sonos Era 100 守想要 Sonos 生態系預算版的人。\n\nEra 100 以下整片無聊，買真的智慧喇叭或跳過分類才務實。",
    zh_h=[
        {"title": "Sonos Era 300 Dolby Atmos 加五月韌體修復是對的組合", "body": "Dolby Atmos 空間音訊撐住認真聽眾的音質論述。五月韌體終於修好 2025 年底的斷線問題。第一名很明確，Sonos 生態系打法沒退場。"},
        {"title": "HomePod 2 是 iPhone 家庭動不了的選擇", "body": "Siri 加 Apple Music 整合還是分類裡所有平台打法最乾淨的。音質在另一個價位帶真的跟 Sonos 有得拚。iPhone 生態系買家第二名沒錯。"},
        {"title": "Echo Show 11 Alexa+ AI 整合是真升級", "body": "四月 Alexa+ 推送是讓 Alexa 終於有智慧感、不再指令式的關鍵升級。螢幕控制智慧家庭在廚房檯面真的好用。隱私問題讓它守第三，但實用價值是真的。"},
    ],
)


# ============================================================
# best-gaming-headsets
# ============================================================
add(
    "best-gaming-headsets",
    refs=[
        {"title": "Best gaming headsets 2026", "url": "https://www.rtings.com/headphones/reviews/best/gaming-headsets", "source": "RTINGS"},
        {"title": "SteelSeries Arctis Nova Pro Wireless 2 review", "url": "https://www.tomshardware.com/peripherals/gaming-headsets", "source": "Tom's Hardware"},
        {"title": "Logitech G Pro X 3 Lightspeed", "url": "https://www.pcgamer.com/hardware/best-gaming-headset/", "source": "PC Gamer"},
    ],
    en_c="SteelSeries Arctis Nova Pro Wireless 2 stays first because the dual-battery hot-swap system plus the parametric EQ control plus the Memorial Day price cut to $299 this week is the package that wins for serious PC and console gamers. Audeze Maxwell at second holds the audiophile gaming pick on the planar magnetic driver argument, the sound stage and detail retrieval is genuinely a class above anything else in gaming headsets. Logitech G Pro X 3 Lightspeed at third gets the new firmware that improved Blue Voice processing in May and the esports-focused tuning is still the right pick for competitive FPS players. Razer BlackShark V3 Pro at fourth holds for buyers who want the Razer ecosystem and the new THX Spatial Audio improvements are real. HyperX Cloud Alpha 2 holds the wired-headset pick and the comfort plus durability argument keeps it on the leaderboard. Corsair HS80 Max wireless holds for buyers in the Corsair ecosystem. Below the Corsair the field is uninspiring and the practical advice is to stretch to the Logitech or wait for July sales. The Beyerdynamic MMX 200 Wireless holds in mid-pack as the audiophile-leaning value pick.",
    en_h=[
        {"title": "Arctis Nova Pro Wireless 2 at $299 is the Memorial Day price", "body": "Dual-battery hot-swap plus parametric EQ plus the Memorial Day cut is the package that wins for serious PC and console gamers. The price point is the lowest the headset has been all year. First place is decisive."},
        {"title": "Audeze Maxwell planar magnetic is a class above on sound", "body": "Planar magnetic drivers in a gaming headset deliver sound stage and detail retrieval that nothing else in the category matches. For audiophile gamers who want the music-listening quality plus the chat features, Maxwell is the right pick at second."},
        {"title": "Logitech G Pro X 3 Blue Voice firmware upgrade matters for FPS", "body": "May firmware improved Blue Voice processing which is the chat-clarity feature that matters most for competitive FPS. Esports-focused tuning plus the new chat upgrade is the package that justifies third over the Razer."},
    ],
    zh_c="SteelSeries Arctis Nova Pro Wireless 2 守第一，雙電池熱抽換系統加參數 EQ 控制加國殤日這禮拜的 NT$9,500 折扣，這套組合對認真 PC 跟主機玩家就是對的。\n\nAudeze Maxwell 第二守發燒友電競之選，平面磁性振膜的音場跟細節真的比任何其他電競耳機都高一階。\n\nLogitech G Pro X 3 Lightspeed 第三，五月韌體改善 Blue Voice 處理，電競調音對競技 FPS 玩家還是對的。\n\nRazer BlackShark V3 Pro 第四對 Razer 生態系玩家就是對的，新的 THX Spatial Audio 改良是真的。\n\nHyperX Cloud Alpha 2 守有線之選，舒適度加耐用度論述讓它留在榜上。Corsair HS80 Max 守 Corsair 生態系玩家。Corsair 以下整片無聊，硬撐去 Logitech 或等七月才務實。Beyerdynamic MMX 200 Wireless 中段守發燒友傾向的價值之選。",
    zh_h=[
        {"title": "Arctis Nova Pro Wireless 2 NT$9,500 是國殤日定價", "body": "雙電池熱抽換加參數 EQ 加國殤日折扣的組合對認真 PC 跟主機玩家就是對的。這個價位是耳機今年最低。第一名很明確。"},
        {"title": "Audeze Maxwell 平面磁性振膜高一階", "body": "電競耳機裡平面磁性振膜的音場跟細節，分類裡沒人能比。要音樂聆聽水準加聊天功能的發燒友玩家，Maxwell 第二名就是對的。"},
        {"title": "Logitech G Pro X 3 Blue Voice 韌體升級對 FPS 玩家有差", "body": "五月韌體改善 Blue Voice 處理就是競技 FPS 最在意的聊天清晰度。電競調音加這個聊天升級的組合撐住第三名，比 Razer 對。"},
    ],
)


# ============================================================
# best-smart-rings
# ============================================================
add(
    "best-smart-rings",
    refs=[
        {"title": "Best smart rings 2026", "url": "https://www.wired.com/gallery/best-smart-rings/", "source": "Wired"},
        {"title": "Oura Ring 5 review", "url": "https://www.tomsguide.com/wearables/best-smart-rings", "source": "Tom's Guide"},
        {"title": "Samsung Galaxy Ring 2 firmware update May", "url": "https://www.theverge.com/24/best-smart-ring", "source": "The Verge"},
    ],
    en_c="Oura Ring 5 stays first because the new continuous glucose monitoring partnership with Stelo that the Oura platform integrated in April is the development that finally puts the smart ring ahead of every wrist-based wearable on a meaningful health metric. The $349 base price plus the $5.99 monthly Oura membership still represents the right pricing model for the recurring health data work. Samsung Galaxy Ring 2 at second holds the Samsung-ecosystem pick and the May firmware that improved the activity recognition is the upgrade that finally makes it competitive with the Oura on day-to-day tracking. Ultrahuman Ring AIR at third holds the no-subscription pick and the value math is still genuinely the cleanest in the category for buyers who do not want recurring fees. RingConn Gen 2 at fourth gets the new sleep coaching feature that rolled out in May and the value plus the multi-color options keeps it the right pick for first-time smart-ring buyers. Circular Ring 2 holds in mid-pack on the European ecosystem play. Below the Circular the field gets thin and the practical advice is to start with the Oura unless your specific concern is recurring fees, in which case Ultrahuman is correct.",
    en_h=[
        {"title": "Oura Ring 5 Stelo glucose integration is the new health frontier", "body": "Continuous glucose monitoring partnership with Stelo integrated in April puts Oura ahead of every wrist wearable on a meaningful health metric. $349 plus $5.99 monthly is the right pricing model for the data work. First place is decisive."},
        {"title": "Samsung Galaxy Ring 2 May firmware closes the gap to Oura", "body": "May firmware improved activity recognition to where Galaxy Ring 2 is finally competitive with Oura on day-to-day tracking. Samsung-ecosystem integration plus this kind of recognition upgrade is the package that holds second."},
        {"title": "Ultrahuman Ring AIR remains the no-subscription pick", "body": "Cleanest value math in the category for buyers who do not want recurring fees. Sleep tracking and activity scoring are genuinely competitive without the monthly cost. Third place is the right anti-subscription pick."},
    ],
    zh_c="Oura Ring 5 守第一，四月整合 Stelo 的連續血糖監測合作是讓智慧戒指終於在重要健康指標上勝過所有手腕穿戴的關鍵。NT$10,900 起跳價加每月 NT$190 的 Oura 會員制是健康數據工作對的訂價模式。\n\nSamsung Galaxy Ring 2 守第二是三星生態系之選，五月韌體改善活動識別是讓它在日常追蹤上終於跟 Oura 有得拚的關鍵升級。\n\nUltrahuman Ring AIR 第三守免訂閱之選，C/P 值還是分類裡最乾淨的，不想付持續費用的買家就選它。\n\nRingConn Gen 2 第四吃五月推出的睡眠教練功能，C/P 值加多色選擇是首次買智慧戒指的人對的選擇。Circular Ring 2 中段守歐洲生態系打法。\n\nCircular 以下整片稀薄，務實建議從 Oura 開始，除非特別在意持續費用就選 Ultrahuman。",
    zh_h=[
        {"title": "Oura Ring 5 Stelo 血糖整合開啟新健康前線", "body": "四月整合 Stelo 連續血糖監測，讓 Oura 在重要健康指標上勝過所有手腕穿戴。NT$10,900 加每月 NT$190 是健康數據工作對的訂價。第一名很明確。"},
        {"title": "Samsung Galaxy Ring 2 五月韌體縮小跟 Oura 差距", "body": "五月韌體改善活動識別，讓 Galaxy Ring 2 在日常追蹤上終於跟 Oura 有得拚。三星生態系整合加這種識別升級的組合撐住第二名。"},
        {"title": "Ultrahuman Ring AIR 還是免訂閱之選", "body": "C/P 值還是分類裡最乾淨的，不想付持續費用的買家就靠它。睡眠追蹤跟活動評分沒月費也真的有競爭力。第三名是反訂閱派的選擇。"},
    ],
)


# ============================================================
# best-smart-pet-feeders
# ============================================================
add(
    "best-smart-pet-feeders",
    refs=[
        {"title": "Best automatic pet feeders 2026", "url": "https://www.nytimes.com/wirecutter/reviews/best-automatic-cat-feeders/", "source": "Wirecutter"},
        {"title": "Petlibro Granary Wi-Fi review", "url": "https://www.tomsguide.com/best-picks/best-pet-feeders", "source": "Tom's Guide"},
        {"title": "Sure Petcare SureFeed update", "url": "https://www.theverge.com/24/best-smart-pet-feeder", "source": "The Verge"},
    ],
    en_c="Petlibro Granary Wi-Fi stays first because the dual-hopper design plus the camera integration plus the new Memorial Day price drop to $129 this week is the combination that wins for multi-pet households which is the actual market reality. PetSafe Smart Feed at second holds the single-pet pick and the iOS plus Android app stability is still the cleanest in the category. SureFeed Microchip at third holds the multi-cat household pick because microchip recognition that actually keeps the dominant cat out of the timid cat's food is the feature nothing else in the category delivers. Wopet 6L Smart Feeder at fourth gets a Memorial Day cut and the value math at $89 is genuinely the right entry-level pick. Whisker Litter-Robot 4 partner feeder holds for buyers in the Whisker ecosystem and the platform integration is the smart-home play that justifies the premium. Petsafe Healthy Pet Simply Feed holds in mid-pack on the no-Wi-Fi proposition which is genuinely the right choice for buyers who do not want yet another app on their phone. Below the Petsafe the field is uninspiring and the practical advice is to either start with the Petlibro for multi-pet or the Petsafe simple feeder for single-pet.",
    en_h=[
        {"title": "Petlibro Granary Wi-Fi at $129 is the Memorial Day deal", "body": "Dual-hopper design plus camera plus Memorial Day price is the package that wins for multi-pet households. The price point is the cheapest the Granary has been all year. First place is decisive for the typical buyer profile."},
        {"title": "SureFeed Microchip is irreplaceable for multi-cat households", "body": "Microchip recognition that actually keeps the dominant cat out of the timid cat's food is the feature nothing else in the category delivers. Third place is correct because the use case is specific but unmatched. Anti-bullying feed delivery is the niche."},
        {"title": "Wopet 6L at $89 is the right entry-level pick", "body": "Memorial Day cut puts the Wopet at the price point where the entry-level math finally works. Single-pet households on a budget who just want app-based scheduling should start here. Fourth place is the value floor of the category."},
    ],
    zh_c="Petlibro Granary Wi-Fi 守第一，雙料桶設計加相機整合加國殤日這禮拜砍到 NT$3,900 的組合，對多寵家庭這個實際市場主流就是對的。\n\nPetSafe Smart Feed 第二守單寵之選，iOS 跟 Android App 穩定度還是分類裡最乾淨的。\n\nSureFeed Microchip 第三守多貓家庭之選，晶片辨識真的能擋強勢貓進弱勢貓食盆，這個功能分類裡沒人有。\n\nWopet 6L Smart Feeder 第四吃國殤日折扣，NT$2,700 是真的對的入門價。\n\nWhisker Litter-Robot 4 配套餵食器守 Whisker 生態系買家，平台整合是撐住溢價的智慧家庭打法。Petsafe Healthy Pet Simply Feed 中段守免 Wi-Fi 之選，不想多裝 App 的人就選這個。\n\nPetsafe 以下整片無聊，務實建議多寵從 Petlibro 開始、單寵從 Petsafe 簡易款開始。",
    zh_h=[
        {"title": "Petlibro Granary Wi-Fi NT$3,900 是國殤日王", "body": "雙料桶加相機加國殤日定價的組合對多寵家庭就是對的。這個價位是 Granary 今年最低。一般買家輪廓第一名很明確。"},
        {"title": "SureFeed Microchip 在多貓家庭無可取代", "body": "晶片辨識真的能擋強勢貓進弱勢貓食盆，這個功能分類裡沒人有。第三名沒錯，使用情境特定但無可替代。反霸凌餵食是它的利基。"},
        {"title": "Wopet 6L NT$2,700 是對的入門選擇", "body": "國殤日折扣把 Wopet 壓到入門帳面終於算得過去的價位。預算有限的單寵家庭只要 App 排程就好，從這邊開始。第四名是分類的價值地板。"},
    ],
)


# ============================================================
# best-foldable-smartphones
# ============================================================
add(
    "best-foldable-smartphones",
    refs=[
        {"title": "Samsung Galaxy Z Fold7 drops to a near record low as Samsung clears stock", "url": "https://gizmodo.com/galaxy-z-fold7-drops-to-a-near-record-low-as-samsung-clears-stock-ahead-of-the-fold8-2000756822", "source": "Gizmodo"},
        {"title": "Samsung Galaxy Z Fold may get a wide-body sibling in 2026", "url": "https://www.androidpolice.com/samsung-galaxy-z-fold-may-get-wide-body-sibling-next-year/", "source": "Android Police"},
        {"title": "Samsung Galaxy Z Fold7 review", "url": "https://www.gsmarena.com/samsung_galaxy_z_fold7-13826.php", "source": "GSMArena"},
    ],
    en_c="Samsung Galaxy Z Fold7 stays first because the near-record-low price drop this week as Samsung clears stock ahead of the rumored Fold8 makes the upgrade math genuinely the best it has been since launch. The 200MP camera plus the 8-inch main display plus the 4.2mm folded thickness is still the package that wins for buyers who want the foldable form factor without compromise. Google Pixel Fold 3 at second holds the cleaner software pick and the Tensor G6 plus the better seven-year update commitment is the right pick for buyers who care about long-term software support over the Samsung hardware lead. Honor Magic V5 at third holds the China-and-international pick and the thinness argument plus the Snapdragon 8 Elite Gen 2 is the package that wins for buyers willing to operate outside the major US carriers. OnePlus Open 2 at fourth holds the value flagship pick and the Memorial Day discount this week makes the price-to-performance math right. Motorola Razr Plus 2026 at fifth holds the clamshell pick and the larger outer display is the right execution for the flip use case. Samsung Galaxy Z Flip7 holds the budget clamshell pick. Below the Z Flip7 the field is uninspiring and the practical advice is to wait for the Fold8 launch in July if you are not in a hurry.",
    en_h=[
        {"title": "Galaxy Z Fold7 near-record-low price is the upgrade window", "body": "Samsung is clearing stock ahead of the rumored Fold8 and the discount this week is the best the upgrade math has been since launch. The 200MP camera plus the 4.2mm folded thickness is still the package that wins. First place is decisive."},
        {"title": "Pixel Fold 3 wins on long-term software support", "body": "Seven-year update commitment plus Tensor G6 plus the cleaner Pixel software is the package that justifies second over the Samsung hardware lead. For buyers who keep phones for 4+ years, Pixel Fold 3 is the right pick."},
        {"title": "Wait for Fold8 in July if not in a hurry", "body": "Samsung is clearing Fold7 stock specifically because Fold8 is coming. If the upgrade can wait until July, the new generation will be worth checking. If you need a foldable now, Fold7 at this discount is the right call."},
    ],
    zh_c="Samsung Galaxy Z Fold7 守第一，這禮拜跌到接近歷史低點，三星在為傳聞中的 Fold8 清庫存，這個升級帳面是上市以來最對的時間點。200MP 相機加 8 吋主螢幕加 4.2mm 折疊厚度的組合對要折疊式但不要妥協的買家還是對的。\n\nGoogle Pixel Fold 3 第二守乾淨軟體之選，Tensor G6 加七年更新承諾對長期軟體支援比三星硬體領先重要的買家就是對的。\n\nHonor Magic V5 第三守中港跟國際之選，輕薄論述加 Snapdragon 8 Elite Gen 2 對能用美國主流電信以外通路的買家就是對的。\n\nOnePlus Open 2 第四守價值旗艦，國殤日折扣讓價格性能比算得過去。\n\nMotorola Razr Plus 2026 第五守翻蓋之選，更大外螢幕是翻蓋使用情境對的執行。Samsung Galaxy Z Flip7 守預算翻蓋之選。\n\nZ Flip7 以下整片無聊，不急的話等七月 Fold8 才務實。",
    zh_h=[
        {"title": "Galaxy Z Fold7 接近歷史低價是升級時機", "body": "三星在為傳聞中的 Fold8 清庫存，這禮拜折扣是上市以來升級帳面最對的時候。200MP 相機加 4.2mm 折疊厚度還是對的組合。第一名很明確。"},
        {"title": "Pixel Fold 3 靠長期軟體支援贏", "body": "七年更新承諾加 Tensor G6 加 Pixel 乾淨軟體的組合，撐住第二名比三星硬體領先重要。手機用 4 年以上的人，Pixel Fold 3 就是對的。"},
        {"title": "不急的話七月等 Fold8", "body": "三星清 Fold7 庫存就是因為 Fold8 要來。升級能等到七月就等。現在就要折疊式手機的話，這個折扣的 Fold7 是對的選擇。"},
    ],
)


# ============================================================
# best-laptops
# ============================================================
add(
    "best-laptops",
    refs=[
        {"title": "Apple M5 vs Intel Panther Lake vs Snapdragon X2", "url": "https://www.tomsguide.com/computing/apple-m5-vs-intel-vs-amd-vs-snapdragon-x2-which-chip-wins", "source": "Tom's Guide"},
        {"title": "Snapdragon X2 Elite Laptops 2026 Why Wave Two Wins", "url": "https://the-gadgeteer.com/2026/05/13/snapdragon-x2-elite-laptops-2026/", "source": "The Gadgeteer"},
        {"title": "Best laptops May 2026 Tom's Hardware", "url": "https://www.tomshardware.com/laptops/best-laptops", "source": "Tom's Hardware"},
    ],
    en_c="Apple MacBook Air M5 stays first because the fanless design plus the all-day battery plus the M5 chip efficiency is still the unshakeable everyday-laptop pick at this price tier. The Memorial Day discount that puts the 13-inch at $999 this week is the cheapest the M5 model has been all year. Apple MacBook Pro 14 M5 Pro at second holds the creator pick and the new Wi-Fi 7 plus the upgraded display is the package that justifies the upgrade over the Air for users who actually need the GPU. Asus ROG Zephyrus G14 at third holds the Windows gaming-laptop pick and the Ryzen AI 9 HX 370 plus the RTX 5070 is the right combination for portable gaming, but the battery life trade-off is real. Dell XPS 15 Plus at fourth holds the Windows creator pick and the OLED display plus the Intel Core Ultra 9 is the package that wins for the creator who does not want to leave Windows. Lenovo ThinkPad X1 Carbon Gen 13 at fifth holds the business pick and the keyboard plus the durability argument is unchanged. Asus Zenbook A16 with the Snapdragon X2 Elite Extreme is the new Wave Two Arm pick but the Windows on Arm compatibility friction keeps it lower than the spec sheet suggests. HP Spectre x360 holds the convertible pick and the value math is fine. Below the Spectre, the field is uninspiring and the right move is to stretch to the MacBook Air or wait for July sales.",
    en_h=[
        {"title": "MacBook Air M5 at $999 is the unshakeable everyday-laptop pick", "body": "Fanless design plus all-day battery plus M5 chip efficiency is still the right package for everyday use. Memorial Day price is the cheapest the M5 has been all year. First place is decisive at this price."},
        {"title": "Snapdragon X2 Elite Wave Two finally earns shelf space", "body": "Wave Two X2 Elite is the version that finally earns shelf space next to Lunar Lake and Ryzen AI 300, but Windows on Arm compatibility friction for power users is still real. The Zenbook A16 has the chip but flexes too much. Decision: wait for the next-gen Windows on Arm laptops with better chassis."},
        {"title": "M5 Pro MacBook 14 wins the creator pick on GPU work", "body": "M5 Pro plus Wi-Fi 7 plus the upgraded display is the package that justifies upgrading over the Air for users who actually need GPU work. For creators on macOS, this is the right pick at second. Anyone not doing GPU work should stay on the Air."},
    ],
    zh_c="Apple MacBook Air M5 守第一，無風扇設計加全日續航加 M5 晶片效率還是日常筆電動不了的選擇。國殤日把 13 吋壓到 NT$30,000，今年 M5 機型最低價。\n\nApple MacBook Pro 14 M5 Pro 第二守創作者之選，新的 Wi-Fi 7 加升級顯示器，對真的需要 GPU 的人來說從 Air 升級就是對的。\n\nAsus ROG Zephyrus G14 第三守 Windows 電競筆電之選，Ryzen AI 9 HX 370 加 RTX 5070 對可攜電競就是對的組合，但續航取捨真的有差。\n\nDell XPS 15 Plus 第四守 Windows 創作者，OLED 加 Intel Core Ultra 9 對不想離開 Windows 的創作者就是對的。Lenovo ThinkPad X1 Carbon Gen 13 第五守商務，鍵盤加耐用度沒變。\n\nAsus Zenbook A16 配 Snapdragon X2 Elite Extreme 是新 Wave Two Arm 之選，但 Windows on Arm 相容性摩擦讓它比規格表上看起來低。HP Spectre x360 守變形筆電，C/P 值還行。Spectre 以下整片無聊，硬撐去 MacBook Air 或等七月才務實。",
    zh_h=[
        {"title": "MacBook Air M5 NT$30,000 是日常筆電動不了的選擇", "body": "無風扇設計加全日續航加 M5 晶片效率，日常使用還是對的組合。國殤日定價是 M5 今年最低。這個價位第一名很明確。"},
        {"title": "Snapdragon X2 Elite Wave Two 終於上得了架", "body": "Wave Two X2 Elite 是終於能跟 Lunar Lake 跟 Ryzen AI 300 並列的版本，但 Windows on Arm 對重度使用者的相容性摩擦還是真的。Zenbook A16 有晶片但機身軟掉。決議：等下一代 Windows on Arm 配更好機身的筆電。"},
        {"title": "M5 Pro MacBook 14 靠 GPU 工作贏創作者之選", "body": "M5 Pro 加 Wi-Fi 7 加升級顯示器，對真的需要 GPU 的人從 Air 升級就是對的。macOS 創作者第二名沒錯。不做 GPU 工作的人留在 Air 才對。"},
    ],
)


# ============================================================
# best-mechanical-keyboards
# ============================================================
add(
    "best-mechanical-keyboards",
    refs=[
        {"title": "Best mechanical keyboards 2026", "url": "https://www.rtings.com/keyboard/reviews/best/mechanical", "source": "RTINGS"},
        {"title": "Wooting 80HE review", "url": "https://www.pcgamer.com/hardware/best-gaming-keyboard/", "source": "PC Gamer"},
        {"title": "Keychron Q1 Max review", "url": "https://www.tomshardware.com/peripherals/keyboards", "source": "Tom's Hardware"},
    ],
    en_c="Wooting 80HE stays first because the Hall Effect rapid trigger plus the new Wootility 4 firmware that landed this month is the combination that still wins for competitive FPS players, and the actuation point customization down to 0.1mm is genuinely the most refined implementation in the category. Keychron Q1 Max at second holds the enthusiast wireless pick and the QMK plus VIA support plus the gasket-mounted typing feel is the package that justifies the premium for typists who care about feel over speed. Logitech G915 X Lightspeed at third holds the gaming-and-productivity hybrid pick and the new Memorial Day cut this week makes the value math reasonable. Razer Huntsman V3 Pro TKL at fourth holds the analog optical pick and the 0.1mm actuation customization plus the Razer Synapse integration is the right pick for buyers in the Razer ecosystem. Glorious GMMK 3 Pro holds the build-your-own pick and the modular design plus the gasket mount is genuinely the right execution at this price tier. SteelSeries Apex Pro TKL Gen 4 holds the OmniPoint pick. Below the SteelSeries the field gets uninspiring and the practical advice is to stretch for the Wooting or settle on the GMMK 3 Pro. NuPhy Air75 V3 holds the low-profile mechanical pick and the keychron Q3 Max remains in mid-pack.",
    en_h=[
        {"title": "Wooting 80HE rapid trigger plus Wootility 4 firmware locks first", "body": "Hall Effect rapid trigger plus Wootility 4 firmware is the combination that still wins for competitive FPS. Actuation point customization down to 0.1mm is the most refined implementation in the category. First place is decisive for gamers."},
        {"title": "Keychron Q1 Max is the typist's pick", "body": "QMK plus VIA support plus the gasket-mounted typing feel is the package that justifies the premium for typists who care about feel over speed. For productivity-first users who type more than they game, Q1 Max is the right pick at second."},
        {"title": "Glorious GMMK 3 Pro is the right modular pick", "body": "Build-your-own approach plus the gasket mount is the right execution at this price tier. For buyers who want to swap switches and keycaps as a hobby, GMMK 3 Pro is the smarter platform than the premium pre-built alternatives."},
    ],
    zh_c="Wooting 80HE 守第一，霍爾效應快速觸發加這個月推送的 Wootility 4 韌體還是讓它在競技 FPS 玩家裡贏，0.1mm 精度的觸發點微調還是分類裡最精緻的實作。\n\nKeychron Q1 Max 第二守發燒友無線之選，QMK 加 VIA 支援加 gasket 結構手感對在意手感勝過速度的打字者就是對的。\n\nLogitech G915 X Lightspeed 第三守電競加生產力混合之選，國殤日這禮拜的折扣讓 C/P 值算得過去。\n\nRazer Huntsman V3 Pro TKL 第四守類比光軸之選，0.1mm 觸發點微調加 Razer Synapse 整合對 Razer 生態系玩家就是對的。\n\nGlorious GMMK 3 Pro 守自組之選，模組化設計加 gasket 結構在這個價位帶就是對的執行。SteelSeries Apex Pro TKL Gen 4 守 OmniPoint 之選。\n\nSteelSeries 以下整片無聊，硬撐去 Wooting 或定在 GMMK 3 Pro 才務實。NuPhy Air75 V3 守低剖面機械之選，Keychron Q3 Max 留在中段。",
    zh_h=[
        {"title": "Wooting 80HE 快速觸發加 Wootility 4 韌體鎖住第一", "body": "霍爾效應快速觸發加 Wootility 4 韌體在競技 FPS 玩家裡還是贏。0.1mm 精度觸發點微調是分類裡最精緻的實作。電競玩家第一名很明確。"},
        {"title": "Keychron Q1 Max 是打字者之選", "body": "QMK 加 VIA 支援加 gasket 結構手感的組合，對在意手感勝過速度的打字者撐住溢價。生產力優先、打字比打電動多的人，Q1 Max 第二名就是對的。"},
        {"title": "Glorious GMMK 3 Pro 是對的模組化選擇", "body": "自組路線加 gasket 結構在這個價位帶就是對的執行。想把換軸跟換鍵帽當興趣的買家，GMMK 3 Pro 比預組旗艦平台更聰明。"},
    ],
)


# ============================================================
# best-gaming-mice
# ============================================================
add(
    "best-gaming-mice",
    refs=[
        {"title": "Best gaming mice 2026", "url": "https://www.rtings.com/mouse/reviews/best/gaming", "source": "RTINGS"},
        {"title": "Logitech G Pro X Superlight 3", "url": "https://www.pcgamer.com/hardware/best-gaming-mouse/", "source": "PC Gamer"},
        {"title": "Razer Viper V4 Pro review", "url": "https://www.tomshardware.com/peripherals/mice", "source": "Tom's Hardware"},
    ],
    en_c="Logitech G Pro X Superlight 3 stays first because the 47-gram weight plus the HERO 3 sensor plus the new POWERPLAY 3 wireless charging compatibility is the combination that still wins for competitive FPS players, and the Memorial Day discount this week putting it at $129 closes the gap to the cheaper Razer enough to make the pick decisive. Razer Viper V4 Pro at second holds the symmetric ergonomic pick and the new Focus Pro 50K sensor plus the lower price after Memorial Day cut is the package that justifies it over the Logitech for buyers who do not need the Superlight ecosystem. Pulsar X2H mini at third holds the small-hands pick and the Hall Effect optical sensor delivery on a sub-$120 mouse is genuinely the cleanest implementation in that price tier. SteelSeries Aerox 5 Wireless at fourth holds the buttons-heavy pick for MMO and RPG players. Glorious Model O 2 Wireless holds for buyers who want the ultralight without the Superlight premium. Razer DeathAdder V4 Pro holds for the right-handed ergonomic pick. Below the DeathAdder the field is uninspiring and the practical advice is to stretch for the Superlight or settle on the Pulsar. Endgame Gear OP1 8K holds in mid-pack as the polling-rate-focused enthusiast pick.",
    en_h=[
        {"title": "G Pro X Superlight 3 at $129 closes the Razer gap", "body": "Memorial Day discount this week puts the Superlight 3 at $129 and closes the gap to the cheaper Razer enough to make the pick decisive. 47 grams plus HERO 3 sensor plus POWERPLAY 3 wireless charging is the combination that still wins for competitive FPS."},
        {"title": "Razer Viper V4 Pro Focus Pro 50K sensor is genuine class-leading", "body": "New Focus Pro 50K sensor plus the lower price after Memorial Day cut is the package that justifies it over the Logitech for buyers who do not need the Superlight ecosystem. Symmetric ergonomic shape plus the new sensor is the right pick at second."},
        {"title": "Pulsar X2H mini is the small-hands value pick", "body": "Hall Effect optical sensor on a sub-$120 mouse is the cleanest implementation in that price tier. Small-hands users who cannot use the Superlight comfortably should start here. Third place is the right specific-use-case pick."},
    ],
    zh_c="Logitech G Pro X Superlight 3 守第一，47 克重量加 HERO 3 感測器加新的 POWERPLAY 3 無線充電相容，這個組合對競技 FPS 玩家還是贏，國殤日這禮拜砍到 NT$3,500 把跟便宜 Razer 的價差縮到能下決定。\n\nRazer Viper V4 Pro 第二守對稱人體工學之選，新的 Focus Pro 50K 感測器加國殤日折扣後的價格，對不需要 Superlight 生態系的買家就是對的。\n\nPulsar X2H mini 第三守小手之選，NT$3,300 以下的滑鼠搭霍爾效應光學感測器是這個價位帶最乾淨的實作。\n\nSteelSeries Aerox 5 Wireless 第四守按鍵多的 MMO 跟 RPG 玩家。Glorious Model O 2 Wireless 守要超輕但不想付 Superlight 溢價的買家。Razer DeathAdder V4 Pro 守右撇子人體工學之選。\n\nDeathAdder 以下整片無聊，硬撐去 Superlight 或定在 Pulsar 才務實。Endgame Gear OP1 8K 中段守 polling rate 取向發燒友之選。",
    zh_h=[
        {"title": "G Pro X Superlight 3 NT$3,500 縮小跟 Razer 差距", "body": "國殤日折扣把 Superlight 3 壓到 NT$3,500，跟便宜 Razer 的價差縮到能下決定。47 克加 HERO 3 感測器加 POWERPLAY 3 無線充電的組合對競技 FPS 還是贏。"},
        {"title": "Razer Viper V4 Pro Focus Pro 50K 感測器真的領先", "body": "新的 Focus Pro 50K 感測器加國殤日折扣後的價格，對不需要 Superlight 生態系的買家就是對的組合。對稱人體工學外型加新感測器，第二名就是對的選擇。"},
        {"title": "Pulsar X2H mini 是小手 C/P 值之選", "body": "NT$3,300 以下的滑鼠搭霍爾效應光學感測器，是這個價位帶最乾淨的實作。小手用不慣 Superlight 的人從這邊開始。第三名是特定使用情境的對的選擇。"},
    ],
)


# ============================================================
# best-gaming-chairs
# ============================================================
add(
    "best-gaming-chairs",
    refs=[
        {"title": "Best gaming chairs 2026", "url": "https://www.rtings.com/chair", "source": "RTINGS"},
        {"title": "Herman Miller Embody Gaming review", "url": "https://www.pcgamer.com/hardware/best-gaming-chair/", "source": "PC Gamer"},
        {"title": "Secretlab Titan Evo 2026", "url": "https://www.tomshardware.com/peripherals/gaming-chairs", "source": "Tom's Hardware"},
    ],
    en_c="Secretlab Titan Evo 2026 stays first because the new BlackPlus Leatherette material plus the redesigned ergonomic adjustability is the combination that still wins for the typical gaming-chair buyer who wants the racing-style aesthetic with actual ergonomic support. The Memorial Day discount this week puts the Titan Evo at $549 which is the cheapest it has been all year. Herman Miller Embody Gaming at second holds the office-grade ergonomic pick and the BackFit adjustment plus the twelve-year warranty is still the right pick for buyers who treat the chair as a long-term office investment, not a gaming-aesthetic statement. Razer Iskur V3 Pro at third holds the dedicated lumbar pick and the built-in 6D armrests are genuinely useful for long sessions. Steelcase Gesture at fourth holds the office-first pick that gamers also buy and the multi-position armrests are still the best execution in the category. Anda Seat Kaiser 4 holds the value flagship pick and the Memorial Day cut to $399 makes the math right. Logitech G x Herman Miller Vantum holds the Logitech ecosystem pick. Below the Vantum the field is uninspiring and the practical advice is to stretch for the Titan Evo or settle on the Anda Seat. Branch Verve and Autonomous ErgoChair Pro 2 hold the value office picks for buyers on a tighter budget.",
    en_h=[
        {"title": "Secretlab Titan Evo 2026 at $549 is the Memorial Day deal", "body": "BlackPlus Leatherette plus redesigned ergonomic adjustability is the combination that wins for the typical gaming-chair buyer. Memorial Day price is the cheapest the chair has been all year. First place is decisive."},
        {"title": "Herman Miller Embody Gaming is the long-term office investment pick", "body": "BackFit adjustment plus the twelve-year warranty is the package that justifies the premium for buyers who treat the chair as a long-term office investment. For users who sit 10+ hours daily, Embody Gaming is the right pick at second."},
        {"title": "Anda Seat Kaiser 4 at $399 is the value flagship pick", "body": "Memorial Day cut to $399 makes the math right for buyers who want the gaming-aesthetic without the Secretlab premium. Build quality plus the new lumbar redesign is the package that justifies it over the bargain alternatives."},
    ],
    zh_c="Secretlab Titan Evo 2026 守第一，新的 BlackPlus Leatherette 材質加重新設計的人體工學調整，對要賽車椅外型加真實人體工學支撐的一般電競椅買家還是對的。國殤日這禮拜把 Titan Evo 壓到 NT$16,500，今年最低。\n\nHerman Miller Embody Gaming 第二守辦公級人體工學之選，BackFit 調整加 12 年保固對把椅子當長期辦公投資、不是電競外型宣告的買家還是對的。\n\nRazer Iskur V3 Pro 第三守專屬腰托之選，內建 6D 扶手在長時間使用真的有用。\n\nSteelcase Gesture 第四守辦公先行、玩家也買的選擇，多角度扶手還是分類裡最好的執行。Anda Seat Kaiser 4 守價值旗艦之選，國殤日 NT$12,000 讓帳面算得過去。Logitech G x Herman Miller Vantum 守 Logitech 生態系之選。\n\nVantum 以下整片無聊，硬撐去 Titan Evo 或定在 Anda Seat 才務實。Branch Verve 跟 Autonomous ErgoChair Pro 2 守預算更緊的辦公之選。",
    zh_h=[
        {"title": "Secretlab Titan Evo 2026 NT$16,500 是國殤日王", "body": "BlackPlus Leatherette 加重新設計人體工學調整，對一般電競椅買家就是對的組合。國殤日定價是椅子今年最低。第一名很明確。"},
        {"title": "Herman Miller Embody Gaming 是長期辦公投資之選", "body": "BackFit 調整加 12 年保固的組合，對把椅子當長期辦公投資的買家撐住溢價。一天坐 10 小時以上的人，Embody Gaming 第二名就是對的。"},
        {"title": "Anda Seat Kaiser 4 NT$12,000 是價值旗艦", "body": "國殤日折扣讓帳面對想要電競外型但不想付 Secretlab 溢價的買家算得過去。做工加新的腰托重設計，是它在便宜替代品中對的撐起。"},
    ],
)


# ============================================================
# best-mesh-wifi-systems
# ============================================================
add(
    "best-mesh-wifi-systems",
    refs=[
        {"title": "Best mesh Wi-Fi 7 systems 2026", "url": "https://www.rtings.com/router/reviews/best/mesh-wifi", "source": "RTINGS"},
        {"title": "Eero Max 7 review", "url": "https://www.tomsguide.com/best-picks/best-mesh-wi-fi-systems", "source": "Tom's Guide"},
        {"title": "TP-Link Deco BE85 review", "url": "https://www.pcmag.com/picks/the-best-wi-fi-mesh-network-systems", "source": "PCMag"},
    ],
    en_c="Eero Max 7 stays first because the Wi-Fi 7 plus the 10Gbps wired backhaul plus the now-mature Eero Plus security subscription is the combination that wins for households running gigabit fiber, and the Memorial Day discount this week putting the three-pack at $1,199 is the lowest it has been since launch. TP-Link Deco BE85 at second holds the value Wi-Fi 7 pick and the no-subscription proposition is genuinely the right choice for buyers who do not want Amazon's recurring fees. Netgear Orbi 970 at third holds the premium flagship pick and the dedicated backhaul plus the 10Gbps WAN port is still the right pick for the highest-end home network, but the price premium is hard to defend versus the Eero Max 7 after this week's discount. Asus ZenWiFi BT10 at fourth holds the gaming-and-power-user pick and the AiMesh plus the new 2026 firmware that improved the QoS is the package that justifies it over the consumer-oriented alternatives. Google Nest Wifi Pro 7 holds the simple-setup pick and the Google Home integration is still the cleanest for buyers in that ecosystem. Linksys Velop Pro 7 holds in mid-pack. Below the Linksys the field is uninspiring and the practical advice is to stretch for the Eero or settle on the Deco BE85.",
    en_h=[
        {"title": "Eero Max 7 three-pack at $1,199 is the Memorial Day deal", "body": "Wi-Fi 7 plus 10Gbps wired backhaul plus mature Eero Plus is the combination that wins for gigabit-fiber households. Memorial Day discount this week is the lowest the three-pack has been since launch. First place is decisive."},
        {"title": "TP-Link Deco BE85 is the no-subscription pick", "body": "No recurring fees plus Wi-Fi 7 plus genuinely usable mobile app is the package for buyers who do not want Amazon's subscription model. For privacy-conscious or fee-averse buyers, Deco BE85 is the right pick at second."},
        {"title": "Asus ZenWiFi BT10 QoS firmware upgrade matters", "body": "2026 firmware improved QoS to where the gaming-and-power-user use case is finally well served. AiMesh plus the new QoS is the package that justifies it over consumer-oriented alternatives for buyers who run game servers or care about low-latency routing."},
    ],
    zh_c="Eero Max 7 守第一，Wi-Fi 7 加 10Gbps 有線回程加成熟的 Eero Plus 安全訂閱，這個組合對跑 gigabit 光纖的家庭就是對的。國殤日這禮拜把三入組合包壓到 NT$36,000，上市以來最低。\n\nTP-Link Deco BE85 第二守 Wi-Fi 7 價值之選，免訂閱論述對不想付 Amazon 持續費用的買家就是對的。\n\nNetgear Orbi 970 第三守頂級旗艦之選，獨立回程加 10Gbps WAN 對最高階家庭網路還是對的，但溢價在這禮拜 Eero Max 7 折扣後很難撐。\n\nAsus ZenWiFi BT10 第四守電競加重度使用之選，AiMesh 加 2026 韌體改善的 QoS 對消費取向替代品來說就是對的。\n\nGoogle Nest Wifi Pro 7 守簡易設定之選，Google Home 整合還是這個生態系最乾淨的。Linksys Velop Pro 7 中段守住。\n\nLinksys 以下整片無聊，硬撐去 Eero 或定在 Deco BE85 才務實。",
    zh_h=[
        {"title": "Eero Max 7 三入組合包 NT$36,000 是國殤日王", "body": "Wi-Fi 7 加 10Gbps 有線回程加成熟的 Eero Plus 組合，對跑 gigabit 光纖的家庭就是對的。國殤日折扣是三入組合包上市以來最低。第一名很明確。"},
        {"title": "TP-Link Deco BE85 是免訂閱之選", "body": "免持續費用加 Wi-Fi 7 加真的能用的 App，對不想付 Amazon 訂閱費的買家就是對的組合。注重隱私或排斥費用的買家，Deco BE85 第二名沒錯。"},
        {"title": "Asus ZenWiFi BT10 QoS 韌體升級有差", "body": "2026 韌體改善 QoS 到電競加重度使用情境終於服務得好。AiMesh 加新 QoS 對跑遊戲伺服器或在意低延遲路由的買家撐住消費級替代品。"},
    ],
)


# ============================================================
# best-3d-printers
# ============================================================
add(
    "best-3d-printers",
    refs=[
        {"title": "Best 3D printers 2026", "url": "https://www.tomshardware.com/best-picks/best-3d-printers", "source": "Tom's Hardware"},
        {"title": "Bambu Lab P1S Pro review", "url": "https://all3dp.com/1/best-3d-printer-reviews/", "source": "All3DP"},
        {"title": "Prusa Core ONE Memorial Day deal", "url": "https://www.theverge.com/22853321/best-3d-printer", "source": "The Verge"},
    ],
    en_c="Bambu Lab P1S Pro stays first because the auto bed leveling plus the AMS lite multi-color plus the new H2D hot-end upgrade that landed in April firmware is still the package that wins for the typical 3D printing buyer who wants reliable prints without the constant tuning. The Memorial Day discount this week puts the P1S Pro at $599 which is the cheapest it has been all year. Prusa Core ONE at second holds the open-source enthusiast pick and the Prusa support plus the Klipper-based firmware is the right pick for buyers who treat 3D printing as a serious hobby. Creality K2 Plus at third holds the larger-format pick and the 350mm build volume plus the multicolor support is the right pick for buyers who want to print larger parts. Anycubic Kobra 3 Combo at fourth holds the value multicolor pick and the Memorial Day cut makes the math right. Elegoo Centauri Carbon holds the carbon-fiber capable pick for buyers who need engineering-grade prints. Bambu Lab A1 holds the value mainstream pick and the cheap entry into the Bambu ecosystem is still the right starter. Below the A1 the field is uninspiring and the practical advice is to either start with the A1 mini or stretch for the P1S Pro.",
    en_h=[
        {"title": "Bambu Lab P1S Pro at $599 is the Memorial Day deal", "body": "Auto bed leveling plus AMS lite plus April firmware H2D hot-end upgrade is the package that wins for typical buyers. Memorial Day price is the cheapest the P1S Pro has been all year. First place is decisive."},
        {"title": "Prusa Core ONE is the serious-hobbyist pick", "body": "Open-source firmware plus Prusa community support plus the Klipper-based controller is the right pick for buyers who treat 3D printing as a serious hobby. For users who want to dive into the firmware and tune everything, Core ONE is correct at second."},
        {"title": "Creality K2 Plus owns the larger-format pick", "body": "350mm build volume plus multicolor support is the package nothing else in the category at this price delivers. For buyers who want to print parts larger than a soda bottle, K2 Plus is the right pick at third."},
    ],
    zh_c="Bambu Lab P1S Pro 守第一，自動床面調平加 AMS lite 多色加四月韌體推送的 H2D 熱端升級，這套組合對要可靠列印不要常微調的一般 3D 列印買家還是對的。國殤日這禮拜把 P1S Pro 砍到 NT$18,000，今年最低。\n\nPrusa Core ONE 第二守開源發燒友之選，Prusa 支援加 Klipper 基底韌體，對把 3D 列印當認真嗜好的買家就是對的。\n\nCreality K2 Plus 第三守大尺寸之選，350mm 列印體積加多色支援，對要列印大型零件的買家就是對的。\n\nAnycubic Kobra 3 Combo 第四守價值多色之選，國殤日折扣讓帳面算得過去。Elegoo Centauri Carbon 守碳纖維能力之選，要工程級列印的買家。Bambu Lab A1 守價值主流之選，便宜進入 Bambu 生態系還是對的入門。\n\nA1 以下整片無聊，務實建議從 A1 mini 開始或硬撐去 P1S Pro。",
    zh_h=[
        {"title": "Bambu Lab P1S Pro NT$18,000 是國殤日王", "body": "自動床面調平加 AMS lite 加四月韌體 H2D 熱端升級的組合，對一般買家就是對的。國殤日定價是 P1S Pro 今年最低。第一名很明確。"},
        {"title": "Prusa Core ONE 是認真嗜好者之選", "body": "開源韌體加 Prusa 社群支援加 Klipper 基底控制器，對把 3D 列印當認真嗜好的買家就是對的。想深入韌體微調的人，Core ONE 第二名沒錯。"},
        {"title": "Creality K2 Plus 拿下大尺寸之選", "body": "350mm 列印體積加多色支援，這個價位分類裡沒人做到。要列印比寶特瓶大的零件的買家，K2 Plus 第三名就是對的。"},
    ],
)


# ============================================================
# best-handheld-gaming-consoles
# ============================================================
add(
    "best-handheld-gaming-consoles",
    refs=[
        {"title": "Best handheld gaming consoles 2026", "url": "https://www.theverge.com/22826129/best-handheld-gaming-console", "source": "The Verge"},
        {"title": "Steam Deck OLED 2 rumors", "url": "https://www.tomsguide.com/gaming/best-handheld-gaming-consoles", "source": "Tom's Guide"},
        {"title": "Asus ROG Ally X 2026 review", "url": "https://www.pcgamer.com/hardware/best-handheld-gaming-pc/", "source": "PC Gamer"},
    ],
    en_c="Asus ROG Ally X 2026 stays first because the Ryzen Z2 Extreme plus the new VRR display plus the SteamOS dual-boot support that landed in April firmware is the combination that finally pushes the Ally past the Steam Deck on a meaningful argument. The Memorial Day discount this week puts the Ally X at $699 which is the cheapest the 2026 refresh has been since launch. Valve Steam Deck OLED at second holds the SteamOS-native pick and the suspend-resume reliability plus the OLED screen is still the right pick for buyers who want the most polished handheld experience without Windows friction. Nintendo Switch 2 at third holds the exclusives pick and the new Mario Kart World plus the upcoming Zelda title is the library argument that nothing else in the category can match. Lenovo Legion Go S at fourth holds the larger-screen pick and the new SteamOS partnership is the development that makes it the right Windows alternative for buyers who want the bigger screen. AYANEO 3 holds for enthusiasts and the build quality is genuinely a class above the mainstream. MSI Claw 8 AI+ holds the Intel-based pick. Below the Claw the field is uninspiring and the practical advice is to choose between the Ally X for power, Deck OLED for polish, or Switch 2 for the library.",
    en_h=[
        {"title": "ROG Ally X 2026 at $699 plus SteamOS dual-boot is the new package", "body": "Ryzen Z2 Extreme plus VRR display plus April firmware SteamOS dual-boot is the combination that finally pushes the Ally past the Steam Deck on argument. Memorial Day price is the cheapest the 2026 refresh has been. First place is decisive."},
        {"title": "Steam Deck OLED still wins on polish", "body": "Suspend-resume reliability plus OLED screen plus the SteamOS-native experience is the package that wins for buyers who want the most polished handheld. Windows friction on the Ally is real even with dual-boot. Second place is correct."},
        {"title": "Switch 2 wins on library nothing else can match", "body": "Mario Kart World plus the upcoming Zelda title is the library argument that nothing else in the category can match. For buyers whose handheld is primarily for Nintendo games, Switch 2 is the right pick at third regardless of the hardware spec sheet."},
    ],
    zh_c="Asus ROG Ally X 2026 守第一，Ryzen Z2 Extreme 加新的 VRR 顯示器加四月韌體推送的 SteamOS 雙系統支援，這套組合終於讓 Ally 在有意義的論述上推過 Steam Deck。國殤日這禮拜把 Ally X 砍到 NT$21,000，2026 改版上市以來最低。\n\nValve Steam Deck OLED 第二守 SteamOS 原生之選，待機恢復可靠度加 OLED 螢幕，對要最精緻掌機體驗、不要 Windows 摩擦的買家還是對的。\n\nNintendo Switch 2 第三守獨佔遊戲之選，新的 Mario Kart World 加即將推出的 Zelda 新作，這個遊戲庫論述分類裡沒人能比。\n\nLenovo Legion Go S 第四守大螢幕之選，新的 SteamOS 合作是讓它成為要大螢幕 Windows 替代品的關鍵。AYANEO 3 守發燒友之選，做工真的高一階。MSI Claw 8 AI+ 守 Intel 基底之選。\n\nClaw 以下整片無聊，務實建議性能選 Ally X、精緻選 Deck OLED、遊戲庫選 Switch 2。",
    zh_h=[
        {"title": "ROG Ally X 2026 NT$21,000 加 SteamOS 雙系統是新組合", "body": "Ryzen Z2 Extreme 加 VRR 顯示器加四月韌體 SteamOS 雙系統的組合，終於讓 Ally 在論述上推過 Steam Deck。國殤日定價是 2026 改版最低。第一名很明確。"},
        {"title": "Steam Deck OLED 還是靠精緻贏", "body": "待機恢復可靠度加 OLED 螢幕加 SteamOS 原生體驗，對要最精緻掌機的買家就是對的組合。Ally 雙系統開機後 Windows 摩擦還是真的有。第二名沒錯。"},
        {"title": "Switch 2 靠分類裡沒人能比的遊戲庫贏", "body": "Mario Kart World 加即將推出的 Zelda 新作，這個遊戲庫分類裡沒人能比。掌機主要玩任天堂遊戲的買家，不管硬體規格表怎樣 Switch 2 第三名就是對的。"},
    ],
)


# ============================================================
# best-portable-chargers
# ============================================================
add(
    "best-portable-chargers",
    refs=[
        {"title": "Best portable chargers 2026", "url": "https://www.tomsguide.com/best-picks/best-portable-chargers", "source": "Tom's Guide"},
        {"title": "Anker Prime 27,650mAh review", "url": "https://www.theverge.com/22832929/best-portable-charger-power-bank", "source": "The Verge"},
        {"title": "Memorial Day Anker deals 2026", "url": "https://www.techradar.com/seasonal-sales/best-memorial-day-sales-2026", "source": "TechRadar"},
    ],
    en_c="Anker Prime 27,650mAh stays first because the 250W output plus the smart display plus the new GaNPrime 2 internals is the combination that still wins for the laptop-and-phone power user, and the Memorial Day discount this week putting it at $149 is the cheapest the Prime has been all year. Anker MagGo 10,000mAh Power Bank holds second as the MagSafe-compatible pick and the iPhone 16-and-up snap-on usage is genuinely the right form factor for buyers in that ecosystem. Baseus Blade 2 at third holds the laptop-bag pick and the 100W output plus the slim profile is the right pick for daily commuter usage. UGREEN Nexode 25000 at fourth holds the value laptop charger and the four-port plus 200W output is the package that justifies it over the Anker for travelers who need to charge a family of devices. Anker 633 Magnetic 10K holds mid-pack as the budget MagSafe alternative. Anker 737 24K holds for buyers who want the workhorse rather than the Prime ecosystem. Mophie Powerstation Pro AC holds for buyers who specifically need an AC outlet. Below the Mophie the field is uninspiring and the practical advice is to start with the Anker Prime for laptop users or the MagGo for phone users.",
    en_h=[
        {"title": "Anker Prime 27,650mAh at $149 is the Memorial Day deal", "body": "250W output plus smart display plus GaNPrime 2 internals is the combination that wins for laptop-and-phone power users. Memorial Day price is the cheapest the Prime has been all year. First place is decisive."},
        {"title": "Anker MagGo is the right iPhone-ecosystem pick", "body": "MagSafe-compatible snap-on usage is the right form factor for iPhone 16-and-up buyers. The cleaner workflow plus the optimized power transfer is the package that justifies second over generic banks. Specific use case wins on specific merit."},
        {"title": "UGREEN Nexode 25000 wins the travel-family pick", "body": "Four-port plus 200W output is the package that justifies it over the Anker for travelers charging multiple devices simultaneously. For families on vacation, Nexode 25000 is the right pick at fourth over the single-laptop-focused alternatives."},
    ],
    zh_c="Anker Prime 27,650mAh 守第一，250W 輸出加智慧顯示器加新的 GaNPrime 2 內部結構，這個組合對筆電加手機的重度使用者還是對的。國殤日這禮拜把 Prime 壓到 NT$4,500，今年最低。\n\nAnker MagGo 10,000mAh Power Bank 守第二是 MagSafe 相容之選，iPhone 16 以上吸上去用的這個外型對這個生態系買家就是對的。\n\nBaseus Blade 2 第三守筆電包之選，100W 輸出加薄型外型對日常通勤就是對的。\n\nUGREEN Nexode 25000 第四守價值筆電充電器，四埠加 200W 輸出對要同時幫一家子裝置充電的旅行者，比 Anker 對。\n\nAnker 633 Magnetic 10K 中段守預算 MagSafe 替代品。Anker 737 24K 守要工作機而非 Prime 生態系的買家。Mophie Powerstation Pro AC 守特別需要 AC 插座的買家。\n\nMophie 以下整片無聊，務實建議筆電用戶從 Anker Prime 開始、手機用戶從 MagGo 開始。",
    zh_h=[
        {"title": "Anker Prime 27,650mAh NT$4,500 是國殤日王", "body": "250W 輸出加智慧顯示器加 GaNPrime 2 內部結構的組合，對筆電加手機重度使用者就是對的。國殤日定價是 Prime 今年最低。第一名很明確。"},
        {"title": "Anker MagGo 是對的 iPhone 生態系之選", "body": "MagSafe 相容吸上去用的外型，對 iPhone 16 以上買家就是對的。更乾淨的工作流加優化的功率傳輸，是它撐住第二名比通用行動電源好的原因。"},
        {"title": "UGREEN Nexode 25000 拿下旅行家庭之選", "body": "四埠加 200W 輸出，對要同時幫多裝置充電的旅行者比 Anker 對。家庭度假的買家，Nexode 25000 第四名比單筆電取向的替代品對。"},
    ],
)


# ============================================================
# best-robot-vacuums
# ============================================================
add(
    "best-robot-vacuums",
    refs=[
        {"title": "Best Robot Vacuums May 2026 Vacuum Wars", "url": "https://vacuumwars.com/best-may-2026-robot-vacuums/", "source": "Vacuum Wars"},
        {"title": "Dreame X60 Max Ultra Complete review", "url": "https://www.rtings.com/robot-vacuum/reviews/best/robot", "source": "RTINGS"},
        {"title": "Roborock Saros 10R review", "url": "https://www.tomsguide.com/best-picks/best-robot-vacuums", "source": "Tom's Guide"},
    ],
    en_c="Dreame X60 Max Ultra Complete stays first because the 89% carpet deep clean score plus the AI-powered obstacle recognition plus the fully automated dock is the combination that wins for whole-home vacuuming, and Vacuum Wars rankings continue to back this up across multiple test categories. The Memorial Day discount this week puts the X60 Max Ultra Complete at $1,499 which is the cheapest the flagship has been all year. Roborock Saros 10R at second holds the obstacle-avoidance pick and the solid-state LiDAR plus the AI recognition is the right pick for buyers with cluttered homes. Dreame L50 Ultra at third holds the value flagship pick and the $799 price plus the friction-reduction features is the package that justifies it as the smart upgrade pick. Eufy E25 Omni at fourth holds the value-multi-functional pick and the $679 price is the right entry for households who want flagship features without the flagship cost. Roborock Qrevo Slim S5+ holds the low-profile pick for buyers with under-furniture cleaning needs. iRobot Roomba Combo 10 Max holds the iRobot ecosystem pick. Below the Roomba the field is uninspiring and the practical advice is to start with the Eufy E25 Omni or stretch for the X60 Max Ultra Complete. MOVA P10 Pro Ultra holds the under-$400 budget pick.",
    en_h=[
        {"title": "Dreame X60 Max Ultra Complete at $1,499 is the Memorial Day deal", "body": "89% carpet deep clean plus AI obstacle recognition plus fully automated dock is the combination that wins for whole-home vacuuming. Vacuum Wars confirms across multiple test categories. First place is decisive."},
        {"title": "Roborock Saros 10R solid-state LiDAR is the obstacle-avoidance pick", "body": "Solid-state LiDAR plus AI recognition is the right pick for buyers with cluttered homes where the robot needs to navigate around toys, cables, and pet bowls. For homes that fail other robots, Saros 10R is correct at second."},
        {"title": "Eufy E25 Omni at $679 is the value flagship pick", "body": "Vacuum Wars score 3.78 at $679 is the right entry for households who want flagship features without the flagship cost. For buyers who want above-average results across every category without the premium, E25 Omni is the right pick at fourth."},
    ],
    zh_c="Dreame X60 Max Ultra Complete 守第一，89% 地毯深層清潔分數加 AI 障礙物辨識加全自動底座，這套組合對全屋吸塵就是對的，Vacuum Wars 在多項測試類別都繼續支持這個結果。國殤日這禮拜把 X60 Max Ultra Complete 壓到 NT$45,000，旗艦今年最低。\n\nRoborock Saros 10R 第二守避障之選，固態 LiDAR 加 AI 辨識對家裡雜物多的買家就是對的。\n\nDreame L50 Ultra 第三守價值旗艦之選，NT$24,000 加摩擦降低功能對聰明升級就是對的組合。\n\nEufy E25 Omni 第四守價值多功能之選，NT$20,000 對想要旗艦功能但不要旗艦價格的家庭就是對的入門。Roborock Qrevo Slim S5+ 守低剖面之選，要清家具下方的買家。iRobot Roomba Combo 10 Max 守 iRobot 生態系之選。\n\nRoomba 以下整片無聊，務實建議從 Eufy E25 Omni 開始或硬撐去 X60 Max Ultra Complete。MOVA P10 Pro Ultra 守 NT$12,000 以下預算之選。",
    zh_h=[
        {"title": "Dreame X60 Max Ultra Complete NT$45,000 是國殤日王", "body": "89% 地毯深層清潔加 AI 障礙物辨識加全自動底座，全屋吸塵就是對的組合。Vacuum Wars 在多項測試類別都確認。第一名很明確。"},
        {"title": "Roborock Saros 10R 固態 LiDAR 是避障之選", "body": "固態 LiDAR 加 AI 辨識對家裡雜物多、要繞玩具線材寵物碗的家庭就是對的。其他機器人在你家裡卡關的話，Saros 10R 第二名就是對的。"},
        {"title": "Eufy E25 Omni NT$20,000 是價值旗艦之選", "body": "Vacuum Wars 3.78 分加 NT$20,000，對想要旗艦功能但不要旗艦價格的家庭就是對的入門。要每個類別都優於平均但不付旗艦溢價的買家，E25 Omni 第四名就是對的。"},
    ],
)


# ============================================================
# best-air-purifiers
# ============================================================
add(
    "best-air-purifiers",
    refs=[
        {"title": "8 Best Air Purifiers of 2026 Consumer Reports", "url": "https://www.consumerreports.org/appliances/air-purifiers/best-air-purifiers-of-the-year-a1197763201/", "source": "Consumer Reports"},
        {"title": "Coway Airmega ProX review", "url": "https://www.engadget.com/home/smart-home/best-air-purifier-120040002.html", "source": "Engadget"},
        {"title": "Shark BreatheClear launch", "url": "https://www.cnn.com/cnn-underscored/reviews/best-product-launches-2026-05-08", "source": "CNN Underscored"},
    ],
    en_c="Coway Airmega ProX stays first because Consumer Reports re-confirmed it as the best performer across dust, pollen, and smoke at both high and low speeds in the 2026 testing cycle, and the unit's 50-pound build quality plus the quiet operation at high CADR is the combination that genuinely justifies the premium for buyers who want one purifier that actually works for the largest room in the house. Levoit Core 400S at second holds the value flagship pick and the half-hour air exchange rate plus the $50 replacement filter cost is the math that wins over Coway at the price tier. Shark BreatheClear Series at third holds the new entrant slot and the 3,600-times-per-hour environmental sensor plus the activity-tracking approach is genuinely the most refined sensor implementation in the category. Dyson Purifier Big+Quiet Formaldehyde holds the formaldehyde-specific pick and the premium air-quality sensors are real, but the recurring filter cost still keeps it from climbing. Blueair Pure 211i Max holds the mid-pack value pick. IQAir HealthPro Plus holds the medical-grade pick for buyers who genuinely need HEPA-13 plus VOC filtration. Below the IQAir the field is uninspiring and the practical advice is to start with the Levoit Core 400S or stretch for the Coway Airmega ProX.",
    en_h=[
        {"title": "Coway Airmega ProX is the Consumer Reports 2026 top pick", "body": "Best performer across dust, pollen, and smoke at both high and low speeds confirmed by Consumer Reports 2026 testing. 50-pound build quality plus quiet operation at high CADR justifies the premium. First place is decisive."},
        {"title": "Levoit Core 400S wins on filter economics", "body": "Half-hour air exchange rate for 1,000 sq ft plus $50 replacement filter is the math that wins over Coway at this tier. For buyers who care about the five-year total cost of ownership, Core 400S is the right pick at second."},
        {"title": "Shark BreatheClear sensor implementation is genuinely smart", "body": "3,600-times-per-hour environmental scanning plus activity-tracking approach is the most refined sensor implementation in the category. New launch this month and the $230-to-$450 price range is the package that earns third on smart features."},
    ],
    zh_c="Coway Airmega ProX 守第一，Consumer Reports 在 2026 測試週期再次確認它在高速跟低速下對灰塵、花粉、煙霧的表現都是最佳，50 磅做工加高 CADR 下的安靜運轉，對要一台清潔機真的能搞定家裡最大房間的買家就是對的。\n\nLevoit Core 400S 第二守價值旗艦之選，半小時換氣一次 1,000 平方呎加 NT$1,500 濾網替換成本，這個帳面在這個價位帶贏 Coway。\n\nShark BreatheClear Series 第三守新進入者位，每小時 3,600 次環境感測加活動追蹤式做法，是分類裡最精緻的感測器實作。\n\nDyson Purifier Big+Quiet Formaldehyde 守甲醛專用之選，頂級空氣品質感測器是真的，但持續濾網成本讓它上不去。\n\nBlueair Pure 211i Max 中段守價值之選。IQAir HealthPro Plus 守醫療級之選，真的需要 HEPA-13 加 VOC 過濾的買家。IQAir 以下整片無聊，務實建議從 Levoit Core 400S 開始或硬撐去 Coway Airmega ProX。",
    zh_h=[
        {"title": "Coway Airmega ProX 是 Consumer Reports 2026 首選", "body": "Consumer Reports 2026 測試確認高速跟低速下對灰塵、花粉、煙霧表現都是最佳。50 磅做工加高 CADR 下的安靜運轉撐住溢價。第一名很明確。"},
        {"title": "Levoit Core 400S 靠濾網經濟學贏", "body": "半小時換氣一次 1,000 平方呎加 NT$1,500 濾網替換，這個帳面在這個價位帶贏 Coway。在意五年總持有成本的買家，Core 400S 第二名就是對的。"},
        {"title": "Shark BreatheClear 感測器實作真的聰明", "body": "每小時 3,600 次環境掃描加活動追蹤式做法，是分類裡最精緻的感測器實作。這個月新上市，NT$7,000 到 NT$13,500 價格帶，第三名靠智慧功能贏。"},
    ],
)


# ============================================================
# best-air-fryers
# ============================================================
add(
    "best-air-fryers",
    refs=[
        {"title": "Best air fryers 2026", "url": "https://www.nytimes.com/wirecutter/reviews/best-air-fryer/", "source": "Wirecutter"},
        {"title": "Ninja DZ550 review", "url": "https://www.tomsguide.com/home/best-air-fryers", "source": "Tom's Guide"},
        {"title": "NuWave Brio Plus Memorial Day sale", "url": "https://www.cnn.com/cnn-underscored/deals/best-amazon-prime-day-home-deals-2026-03-25", "source": "CNN Underscored"},
    ],
    en_c="Ninja DZ550 stays first because the two-basket simultaneous-cooking design plus the six functions plus the 6-quart capacity is still the combination that wins for the typical family of four, and the Memorial Day discount this week putting it at $179 is the cheapest the DZ550 has been all year. NuWave Brio Plus 37401 at second holds the batch-cooking pick and the 7.1-quart capacity at the best price of the year is the package that justifies it over single-basket competitors. Instant Vortex Plus 6-Quart at third holds the value mainstream pick and the ClearCook window plus the OdorErase filtration is the right pick for the apartment renter who cares about cooking visibility. Cosori Pro II Air Fryer at fourth holds the consumer-favorite pick and the new shake reminder plus the dishwasher-safe basket is the package that wins for users who care about ease of cleaning. Breville Smart Oven Air at five holds the toaster-oven hybrid pick for buyers who want flexibility over speed. Ninja Foodi 6-in-1 holds the multi-function pick. Below the Foodi the field is uninspiring and the practical advice is to start with the Ninja DZ550 for families or the Instant Vortex for singles and couples. Philips Premium XXL holds the European-style pick in mid-pack.",
    en_h=[
        {"title": "Ninja DZ550 at $179 is the Memorial Day family deal", "body": "Two-basket simultaneous cooking plus six functions plus 6-quart capacity is the combination for a family of four. Memorial Day price is the cheapest the DZ550 has been all year. First place is decisive."},
        {"title": "NuWave Brio Plus 7.1-quart at best price of the year", "body": "Memorial Day pricing on the NuWave Brio Plus 37401 is the best price seen all year. 7.1-quart capacity is the package that justifies it over single-basket competitors for batch-cookers. Second place is correct for high-volume households."},
        {"title": "Instant Vortex Plus ClearCook is the right apartment pick", "body": "ClearCook window plus OdorErase filtration is the package that wins for apartment renters who care about cooking visibility and odor control. For small kitchens, Vortex Plus is the right pick at third over the larger Ninja and NuWave."},
    ],
    zh_c="Ninja DZ550 守第一，雙籃同時烹調設計加六種功能加 6 夸脫容量，對典型四人家庭就是對的。國殤日這禮拜把 DZ550 砍到 NT$5,400，今年最低。\n\nNuWave Brio Plus 37401 第二守批次烹調之選，7.1 夸脫容量加今年最低價的組合對單籃對手就是對的。\n\nInstant Vortex Plus 6-Quart 第三守價值主流之選，ClearCook 透視窗加 OdorErase 過濾對在意烹調可視性的公寓租屋族就是對的。\n\nCosori Pro II Air Fryer 第四守消費者最愛之選，新的搖動提醒加可洗碗機清洗的烹調籃，對在意清潔便利性的使用者就是對的。\n\nBreville Smart Oven Air 第五守烤吐司爐混合之選，要彈性勝過速度的買家。Ninja Foodi 6-in-1 守多功能之選。\n\nFoodi 以下整片無聊，務實建議家庭從 Ninja DZ550 開始、單身或情侶從 Instant Vortex 開始。Philips Premium XXL 中段守歐洲風格之選。",
    zh_h=[
        {"title": "Ninja DZ550 NT$5,400 是國殤日家庭王", "body": "雙籃同時烹調加六種功能加 6 夸脫容量的組合，對四人家庭就是對的。國殤日定價是 DZ550 今年最低。第一名很明確。"},
        {"title": "NuWave Brio Plus 7.1 夸脫今年最低價", "body": "國殤日的 NuWave Brio Plus 37401 定價是今年最低。7.1 夸脫容量對批次烹調者，比單籃對手對。高用量家庭第二名沒錯。"},
        {"title": "Instant Vortex Plus ClearCook 是對的公寓之選", "body": "ClearCook 透視窗加 OdorErase 過濾的組合，對在意烹調可視性跟氣味控制的公寓租屋族就是對的。小廚房用戶第三名比更大的 Ninja 跟 NuWave 對。"},
    ],
)


# ============================================================
# best-coffee-makers
# ============================================================
add(
    "best-coffee-makers",
    refs=[
        {"title": "Best coffee maker 2026 Tom's Guide", "url": "https://www.tomsguide.com/home/coffee-makers/best-coffee-makers", "source": "Tom's Guide"},
        {"title": "Technivorm Moccamaster KBGV Select re-review", "url": "https://www.nytimes.com/wirecutter/reviews/the-best-coffee-maker/", "source": "Wirecutter"},
        {"title": "Breville Bambino Plus Memorial Day deal", "url": "https://www.theverge.com/24/best-coffee-maker", "source": "The Verge"},
    ],
    en_c="Technivorm Moccamaster KBGV Select stays first because Tom's Guide's early-2026 re-review put it back at the top of the drip-coffee category on durability and consistency, which is the metric that actually matters for daily morning use over five-plus years. The Memorial Day discount this week putting the KBGV at $329 is the cheapest the Moccamaster has been all year. Breville Bambino Plus at second holds the espresso entry pick and the milk-frothing automation plus the value math is the package that wins for buyers who want espresso quality without the prosumer learning curve. Fellow Aiden Precision Brewer at third holds the precision-pourover pick and the app-controlled brewing parameters is genuinely the most refined home brewer in the category. Ninja CFP451 DualBrew Pro at fourth holds the multi-format pick and the K-Cup plus carafe flexibility is the right pick for households where one person wants pourover and another wants pods. Breville Barista Touch Impress holds the all-in-one prosumer pick for buyers who want full espresso control with automation. De'Longhi Dinamica Plus holds the super-automatic pick. Below the De'Longhi the field is uninspiring and the practical advice is to start with the Moccamaster for drip or the Bambino Plus for espresso, and skip the bargain alternatives.",
    en_h=[
        {"title": "Moccamaster KBGV at $329 is the Memorial Day deal", "body": "Tom's Guide's early-2026 re-review put the KBGV back at the top on durability and consistency. Memorial Day price is the cheapest the Moccamaster has been all year. First place is decisive for drip coffee."},
        {"title": "Breville Bambino Plus wins the espresso entry pick", "body": "Milk-frothing automation plus the value math is the package that wins for buyers who want espresso quality without the prosumer learning curve. For first-time home espresso buyers, Bambino Plus is the right pick at second over the Barista Touch."},
        {"title": "Fellow Aiden is the precision-pourover answer", "body": "App-controlled brewing parameters is the most refined home brewer in the category. For pourover enthusiasts who care about replicating cafe-level pours, Aiden is the right pick at third. The premium is real but defensible for the use case."},
    ],
    zh_c="Technivorm Moccamaster KBGV Select 守第一，Tom's Guide 在 2026 年初的重評把 KBGV 放回滴漏咖啡分類榜首，靠的是耐用度跟一致性，這才是每天早上用五年以上真的有差的指標。國殤日這禮拜把 KBGV 砍到 NT$9,900，Moccamaster 今年最低。\n\nBreville Bambino Plus 第二守義式入門之選，奶泡自動化加 C/P 值，對要義式咖啡品質但不想要 prosumer 學習曲線的買家就是對的。\n\nFellow Aiden Precision Brewer 第三守精準手沖之選，App 控制萃取參數是分類裡最精緻的家用沖煮器。\n\nNinja CFP451 DualBrew Pro 第四守多格式之選，K-Cup 加咖啡壺彈性，對一個人要手沖、一個人要膠囊的家庭就是對的。\n\nBreville Barista Touch Impress 守一體式 prosumer 之選，要完整義式控制加自動化的買家。De'Longhi Dinamica Plus 守全自動之選。\n\nDe'Longhi 以下整片無聊，務實建議滴漏從 Moccamaster 開始、義式從 Bambino Plus 開始，跳過便宜替代品。",
    zh_h=[
        {"title": "Moccamaster KBGV NT$9,900 是國殤日王", "body": "Tom's Guide 2026 年初重評把 KBGV 放回榜首，靠的是耐用度跟一致性。國殤日定價是 Moccamaster 今年最低。滴漏咖啡第一名很明確。"},
        {"title": "Breville Bambino Plus 拿下義式入門", "body": "奶泡自動化加 C/P 值，對要義式咖啡品質但不要 prosumer 學習曲線的買家就是對的組合。首次買家用義式機，Bambino Plus 第二名比 Barista Touch 對。"},
        {"title": "Fellow Aiden 是精準手沖之選", "body": "App 控制萃取參數是分類裡最精緻的家用沖煮器。要複製咖啡館等級手沖的玩家，Aiden 第三名就是對的。溢價是真的但這個使用情境撐得起。"},
    ],
)


# ============================================================
# best-rice-cookers
# ============================================================
add(
    "best-rice-cookers",
    refs=[
        {"title": "Best rice cookers 2026", "url": "https://www.nytimes.com/wirecutter/reviews/best-rice-cookers/", "source": "Wirecutter"},
        {"title": "Zojirushi NS-ZCC10 review", "url": "https://www.seriouseats.com/best-rice-cookers", "source": "Serious Eats"},
        {"title": "Cuckoo CRP-CHSS1009FN review", "url": "https://www.consumerreports.org/appliances/rice-cookers/", "source": "Consumer Reports"},
    ],
    en_c="Zojirushi NS-ZCC10 stays first because the Neuro Fuzzy logic plus the heating-pattern adjustment plus the 25-year build reputation is still the combination that wins for daily Asian household rice cooking, and the Memorial Day discount this week putting it at $199 is the cheapest the NS-ZCC10 has been in three years. Cuckoo CRP-CHSS1009FN at second holds the Korean-style pressure pick and the 11 cooking presets plus the GABA rice mode is the right pick for buyers who want firmer rice and the pressure-cooking versatility. Tiger JKT-D10U at third holds the induction-heating premium pick and the temperature-distribution argument is genuinely the most refined cooker in the category, but the $400+ ask keeps it lower. Aroma ARC-954SBD at fourth holds the value mainstream pick and the digital display plus the 8-cup capacity at $79 is the package that wins for buyers who do not need flagship features. Toshiba TRCS01 at five holds the induction-budget pick and the 5.5-cup capacity is right for couples. Instant Pot Pro 10-in-1 holds the multifunction pick for buyers who treat rice cooking as one of many functions. Below the Instant Pot the field is uninspiring and the practical advice is to start with the Aroma or stretch for the Zojirushi.",
    en_h=[
        {"title": "Zojirushi NS-ZCC10 at $199 is the three-year low", "body": "Neuro Fuzzy logic plus heating-pattern adjustment plus the 25-year build reputation is still the right combination for daily Asian household rice cooking. Memorial Day price is the cheapest the NS-ZCC10 has been in three years. First place is decisive."},
        {"title": "Cuckoo CRP-CHSS1009FN wins on Korean pressure cooking", "body": "11 cooking presets plus GABA rice mode is the right pick for buyers who want firmer rice and pressure-cooking versatility. Korean-household buyers who want the homeland brand should start here. Second place is the right specific-use-case pick."},
        {"title": "Aroma ARC-954SBD at $79 is the value entry", "body": "Digital display plus 8-cup capacity at $79 is the package that wins for buyers who do not need flagship features. For first-time rice cooker buyers who just want consistent rice, Aroma is the right entry at fourth."},
    ],
    zh_c="Zojirushi NS-ZCC10 守第一，Neuro Fuzzy 模糊邏輯加加熱模式調整加 25 年做工口碑，這套組合對亞洲家庭日常煮飯還是對的。國殤日這禮拜把 NS-ZCC10 砍到 NT$6,000，三年最低。\n\nCuckoo CRP-CHSS1009FN 第二守韓式壓力之選，11 種烹調預設加 GABA 米模式，對要 Q 一點米飯加壓力烹調彈性的買家就是對的。\n\nTiger JKT-D10U 第三守 IH 加熱頂級之選，溫度分布論述真的是分類裡最精緻的，但 NT$12,000 以上的價格讓它排低。\n\nAroma ARC-954SBD 第四守價值主流之選，數位顯示加 8 杯容量在 NT$2,400 對不需要旗艦功能的買家就是對的。\n\nToshiba TRCS01 第五守 IH 預算之選，5.5 杯容量對情侶剛好。Instant Pot Pro 10-in-1 守多功能之選，把煮飯當眾多功能之一的買家。\n\nInstant Pot 以下整片無聊，務實建議從 Aroma 開始或硬撐去 Zojirushi。",
    zh_h=[
        {"title": "Zojirushi NS-ZCC10 NT$6,000 是三年最低", "body": "Neuro Fuzzy 模糊邏輯加加熱模式調整加 25 年做工口碑，對亞洲家庭日常煮飯就是對的組合。國殤日定價是 NS-ZCC10 三年最低。第一名很明確。"},
        {"title": "Cuckoo CRP-CHSS1009FN 拿下韓式壓力煮飯", "body": "11 種烹調預設加 GABA 米模式，對要 Q 一點米飯加壓力烹調彈性的買家就是對的。要本國品牌的韓國家庭買家從這邊開始。第二名是特定使用情境對的選擇。"},
        {"title": "Aroma ARC-954SBD NT$2,400 是價值入門", "body": "數位顯示加 8 杯容量在 NT$2,400，對不需要旗艦功能的買家就是對的組合。第一次買電鍋只要穩定的米飯的買家，Aroma 第四名就是對的入門。"},
    ],
)


# ============================================================
# best-dishwashers
# ============================================================
add(
    "best-dishwashers",
    refs=[
        {"title": "Best dishwashers 2026", "url": "https://www.consumerreports.org/appliances/dishwashers/", "source": "Consumer Reports"},
        {"title": "Bosch 800 Series review", "url": "https://www.nytimes.com/wirecutter/reviews/best-dishwasher/", "source": "Wirecutter"},
        {"title": "Memorial Day appliance deals 2026", "url": "https://www.techradar.com/news/best-buy-memorial-day-sale-deals", "source": "TechRadar"},
    ],
    en_c="Bosch 800 Series SHX78CM5N stays first because the CrystalDry tech plus the 42dB noise rating plus the third-rack adjustability is still the combination that wins for the typical kitchen-renovation buyer, and the Memorial Day appliance sale this week puts it at $1,299 which is the cheapest the 800 Series has been all year. Miele G 7000 Series at second holds the premium-flagship pick and the AutoDos plus the 20-year build quality argument is the right pick for buyers who treat the dishwasher as a long-term investment, not a five-year appliance. KitchenAid KDTM504KPS at third holds the American mainstream pick and the FreeFlex third rack plus the heated dry is the package that wins for buyers in the KitchenAid ecosystem. LG QuadWash LDPH7972D at fourth holds the smart pick and the TrueSteam plus the ThinQ app is the right pick for buyers who want app control and remote diagnostics. Samsung Bespoke DW80CB785US holds the customizable-front pick. GE Profile UltraFresh PDT755SYRFS holds the value flagship pick. Below the GE the field is uninspiring and the practical advice is to either stretch for the Bosch 800 or settle on the GE Profile.",
    en_h=[
        {"title": "Bosch 800 Series at $1,299 is the Memorial Day appliance deal", "body": "CrystalDry plus 42dB noise rating plus third-rack adjustability is the combination for typical kitchen-renovation buyers. Memorial Day appliance sale puts the 800 Series at its lowest price all year. First place is decisive."},
        {"title": "Miele G 7000 is the long-term investment pick", "body": "AutoDos plus 20-year build quality is the right pick for buyers who treat the dishwasher as a long-term investment. For homeowners staying in the house 15+ years, Miele is the right pick at second despite the premium."},
        {"title": "KitchenAid KDTM504KPS wins on third-rack flexibility", "body": "FreeFlex third rack plus heated dry is the package that wins for buyers who load awkward kitchen items like tall glasses and serving utensils. For US households who want the KitchenAid look in matching appliances, this is the right pick at third."},
    ],
    zh_c="Bosch 800 Series SHX78CM5N 守第一，CrystalDry 技術加 42 分貝噪音加第三層調整性，這套組合對典型廚房裝修買家還是對的。國殤日家電檔期這禮拜把它壓到 NT$39,000，800 Series 今年最低。\n\nMiele G 7000 Series 第二守頂級旗艦之選，AutoDos 加 20 年做工論述，對把洗碗機當長期投資、不是五年家電的買家就是對的。\n\nKitchenAid KDTM504KPS 第三守美式主流之選，FreeFlex 第三層加加熱乾燥，對 KitchenAid 生態系買家就是對的。\n\nLG QuadWash LDPH7972D 第四守智慧之選，TrueSteam 加 ThinQ App 對要 App 控制跟遠端診斷的買家就是對的。Samsung Bespoke DW80CB785US 守可客製面板之選。GE Profile UltraFresh PDT755SYRFS 守價值旗艦之選。\n\nGE 以下整片無聊，務實建議硬撐去 Bosch 800 或定在 GE Profile。",
    zh_h=[
        {"title": "Bosch 800 Series NT$39,000 是國殤日家電王", "body": "CrystalDry 加 42 分貝噪音加第三層調整性的組合，對典型廚房裝修買家就是對的。國殤日家電檔期讓 800 Series 跌到今年最低。第一名很明確。"},
        {"title": "Miele G 7000 是長期投資之選", "body": "AutoDos 加 20 年做工的組合，對把洗碗機當長期投資的買家就是對的。住在這個房子 15 年以上的屋主，雖然有溢價 Miele 第二名就是對的。"},
        {"title": "KitchenAid KDTM504KPS 靠第三層彈性贏", "body": "FreeFlex 第三層加加熱乾燥的組合，對要放高玻璃杯跟服務器皿這種奇怪廚房用品的買家就是對的。美國家庭要 KitchenAid 配套家電的，這個第三名就是對的。"},
    ],
)


# ============================================================
# best-portable-ice-makers
# ============================================================
add(
    "best-portable-ice-makers",
    refs=[
        {"title": "Best portable ice makers 2026", "url": "https://www.nytimes.com/wirecutter/reviews/best-ice-maker/", "source": "Wirecutter"},
        {"title": "GE Profile Opal 2.0 review", "url": "https://www.tomsguide.com/best-picks/best-portable-ice-makers", "source": "Tom's Guide"},
        {"title": "Memorial Day kitchen appliance sale", "url": "https://www.consumerreports.org/money/sales-promotions/best-deals-on-healthy-home-essentials-a5487006019/", "source": "Consumer Reports"},
    ],
    en_c="GE Profile Opal 2.0 stays first because the nugget-ice quality plus the WiFi smart-home integration plus the 1-pound-per-hour throughput is still the package that wins for the typical countertop buyer, and the Memorial Day discount this week putting it at $499 is the cheapest the Opal 2.0 has been since launch. Frigidaire EFIC189-Silver at second holds the value bullet-ice pick and the 26-pound-per-day capacity plus the sub-$150 price is the package that justifies it for buyers who do not care about nugget ice. Sentern Portable Ice Maker at third holds the dual-ice pick and the small-and-large cube modes is the right pick for buyers who want flexibility in cube size. Newair AI-100SS at fourth holds the stainless-steel pick and the 28-pound-per-day production is right for entertaining-focused households. Igloo ICEB26HNAQ holds the colorful budget pick for buyers who want a bright kitchen aesthetic. Whynter ICM-201SB holds the larger countertop pick. Below the Whynter the field gets uninspiring and the practical advice is to either stretch for the Opal 2.0 for nugget or settle on the Frigidaire for bullet. Crownful Compact Ice Maker holds the under-$100 pick which is the price floor that genuinely still produces usable ice.",
    en_h=[
        {"title": "GE Profile Opal 2.0 at $499 is the Memorial Day deal", "body": "Nugget-ice quality plus WiFi smart-home integration plus 1-pound-per-hour throughput is the package that wins for typical countertop buyers. Memorial Day price is the cheapest the Opal 2.0 has been since launch. First place is decisive."},
        {"title": "Frigidaire EFIC189 wins on bullet-ice value", "body": "26-pound-per-day capacity plus sub-$150 price is the package that justifies it for buyers who do not need nugget ice. For households who just want a lot of ice for drinks, Frigidaire is the right pick at second over the premium Opal."},
        {"title": "Sentern dual-cube modes are the right flexibility play", "body": "Small-and-large cube modes is the right pick for buyers who want flexibility in cube size depending on drink type. For cocktail-focused households who want both highball and rocks cubes, Sentern is the right pick at third."},
    ],
    zh_c="GE Profile Opal 2.0 守第一，珍珠冰品質加 WiFi 智慧家庭整合加每小時 1 磅產量，對典型流理台買家還是對的。國殤日這禮拜把 Opal 2.0 砍到 NT$15,000，上市以來最低。\n\nFrigidaire EFIC189-Silver 第二守價值子彈冰之選，每日 26 磅容量加 NT$4,500 以下的價格，對不在意珍珠冰的買家就是對的。\n\nSentern Portable Ice Maker 第三守雙冰塊之選，大小冰塊模式對要冰塊大小彈性的買家就是對的。\n\nNewair AI-100SS 第四守不鏽鋼之選，每日 28 磅產量對宴客取向家庭就是對的。Igloo ICEB26HNAQ 守繽紛預算之選，要明亮廚房美感的買家。Whynter ICM-201SB 守更大流理台之選。\n\nWhynter 以下整片無聊，務實建議硬撐去 Opal 2.0 拿珍珠冰或定在 Frigidaire 拿子彈冰。Crownful Compact Ice Maker 守 NT$3,000 以下之選，這是真的能做出可用冰塊的價格地板。",
    zh_h=[
        {"title": "GE Profile Opal 2.0 NT$15,000 是國殤日王", "body": "珍珠冰品質加 WiFi 智慧家庭整合加每小時 1 磅產量的組合，對典型流理台買家就是對的。國殤日定價是 Opal 2.0 上市以來最低。第一名很明確。"},
        {"title": "Frigidaire EFIC189 靠子彈冰 C/P 值贏", "body": "每日 26 磅容量加 NT$4,500 以下的價格，對不需要珍珠冰的買家就是對的組合。只要很多冰塊配飲料的家庭，Frigidaire 第二名比頂級 Opal 對。"},
        {"title": "Sentern 雙冰塊模式是對的彈性打法", "body": "大小冰塊模式對要看飲料類型決定冰塊大小的買家就是對的。同時要長飲杯冰跟岩石冰的調酒取向家庭，Sentern 第三名就是對的。"},
    ],
)


# ============================================================
# best-smart-thermostats
# ============================================================
add(
    "best-smart-thermostats",
    refs=[
        {"title": "Best smart thermostats 2026", "url": "https://www.nytimes.com/wirecutter/reviews/the-best-thermostat/", "source": "Wirecutter"},
        {"title": "Ecobee Premium 2nd Gen review", "url": "https://www.theverge.com/22847336/best-smart-thermostat", "source": "The Verge"},
        {"title": "Nest Learning Thermostat 4 review", "url": "https://www.tomsguide.com/best-picks/best-smart-thermostats", "source": "Tom's Guide"},
    ],
    en_c="Ecobee Premium 2nd Gen stays first because the included room sensors plus the air-quality monitoring plus the new Matter-over-Thread support that landed in April firmware is the combination that still wins for the typical smart-home enthusiast, and the Memorial Day discount this week puts it at $199 which is the cheapest the Premium 2nd Gen has been all year. Google Nest Learning Thermostat 4 at second holds the Google-ecosystem pick and the new Gemini-powered scheduling is the upgrade that finally makes the learning algorithm feel intelligent rather than rule-based. Amazon Smart Thermostat at third holds the value pick and the $79 price plus the basic Alexa integration is the package that justifies it for buyers who just want app control without the premium features. Honeywell Home T9 at fourth holds the multi-room sensor pick for buyers who already have a Honeywell system. Mysa Smart Thermostat holds the electric-heating pick which is the niche that matters for the specific use case of baseboard and in-floor heating. Sensi Touch 2 holds the wired-only pick for buyers who do not need wireless. Below the Sensi the field is uninspiring and the practical advice is to start with the Amazon or stretch for the Ecobee.",
    en_h=[
        {"title": "Ecobee Premium 2nd Gen at $199 is the Memorial Day deal", "body": "Included room sensors plus air-quality monitoring plus Matter-over-Thread is the combination for smart-home enthusiasts. Memorial Day price is the cheapest the Premium 2nd Gen has been all year. First place is decisive."},
        {"title": "Nest Learning Thermostat 4 Gemini scheduling is the right upgrade", "body": "New Gemini-powered scheduling is the upgrade that finally makes the learning algorithm feel intelligent rather than rule-based. Google-ecosystem buyers should start here. Second place is correct for the Google Home household."},
        {"title": "Amazon Smart Thermostat at $79 is the value pick", "body": "$79 price plus basic Alexa integration is the package that justifies it for buyers who just want app control without the premium features. For first-time smart-thermostat buyers in Alexa households, this is the right entry at third."},
    ],
    zh_c="Ecobee Premium 2nd Gen 守第一，內附房間感測器加空氣品質監測加四月韌體推送的 Matter-over-Thread 支援，這套組合對典型智慧家庭發燒友還是對的。國殤日這禮拜把 Premium 2nd Gen 壓到 NT$6,000，今年最低。\n\nGoogle Nest Learning Thermostat 4 第二守 Google 生態系之選，新的 Gemini 驅動排程是讓學習演算法終於有智慧感、不再規則式的關鍵升級。\n\nAmazon Smart Thermostat 第三守價值之選，NT$2,400 加基本 Alexa 整合，對只要 App 控制、不需要頂級功能的買家就是對的。\n\nHoneywell Home T9 第四守多房間感測之選，已經有 Honeywell 系統的買家。Mysa Smart Thermostat 守電熱之選，踢腳板加地暖的特定使用情境。Sensi Touch 2 守有線之選，不需要無線的買家。\n\nSensi 以下整片無聊，務實建議從 Amazon 開始或硬撐去 Ecobee。",
    zh_h=[
        {"title": "Ecobee Premium 2nd Gen NT$6,000 是國殤日王", "body": "內附房間感測器加空氣品質監測加 Matter-over-Thread 的組合，對智慧家庭發燒友就是對的。國殤日定價是 Premium 2nd Gen 今年最低。第一名很明確。"},
        {"title": "Nest Learning Thermostat 4 Gemini 排程是對的升級", "body": "新的 Gemini 驅動排程是讓學習演算法終於有智慧感、不再規則式的關鍵升級。Google 生態系買家從這邊開始。Google Home 家庭第二名沒錯。"},
        {"title": "Amazon Smart Thermostat NT$2,400 是價值之選", "body": "NT$2,400 加基本 Alexa 整合的組合，對只要 App 控制、不需要頂級功能的買家就是對的。Alexa 家庭首次買智慧恆溫器，這個第三名就是對的入門。"},
    ],
)


# ============================================================
# best-electric-bikes
# ============================================================
add(
    "best-electric-bikes",
    refs=[
        {"title": "Best Electric Bikes 2026 Electric Bike Report", "url": "https://electricbikereport.com/best-electric-bikes/", "source": "Electric Bike Report"},
        {"title": "Ride1Up Roadster V3 review", "url": "https://electrek.co/2026/05/best-electric-bikes/", "source": "Electrek"},
        {"title": "Specialized Turbo Vado SL 2 review", "url": "https://www.bicycling.com/bikes-gear/g28009298/best-electric-bikes/", "source": "Bicycling"},
    ],
    en_c="Specialized Turbo Vado SL 2 stays first because the lightweight commuter-frame design plus the SL drive system plus the now-mature Mission Control app integration is still the package that wins for the daily-commute buyer who wants the e-bike feel without the moped weight. The Memorial Day discount this week puts the Turbo Vado SL 2 at $3,499 which is the cheapest the model has been all year. Ride1Up Roadster V3 at second holds the value commuter pick and the lightweight frame plus the nimble handling plus the precise speed control is the package that justifies it as the right pick for first-time e-bike buyers. Aventon Level 3 at third holds the upright commuter pick and the torque sensor plus the integrated lights is the right pick for buyers who want a more relaxed posture. Lectric XP 3.0 at fourth holds the folding pick and the value math plus the 50-mile range is the package that wins for buyers with apartment storage constraints. Rad Power RadCity 5 Plus holds the cargo-capable pick. Trek FX+ 2 holds the road-bike-style pick for buyers who want the lighter feel. Specialized Globe Haul ST holds the cargo-bike pick for parents who want family hauling capability. Below the Globe Haul the field is uninspiring and the practical advice is to start with the Ride1Up for value or the Specialized for premium.",
    en_h=[
        {"title": "Specialized Turbo Vado SL 2 at $3,499 is the Memorial Day deal", "body": "Lightweight commuter-frame design plus SL drive system plus Mission Control app is the package for daily commuters who want e-bike feel without moped weight. Memorial Day price is the cheapest the model has been all year. First place is decisive."},
        {"title": "Ride1Up Roadster V3 wins the value commuter pick", "body": "Lightweight frame plus nimble handling plus precise speed control is the package that justifies it as the right pick for first-time e-bike buyers. For buyers who want quality without the premium, Ride1Up is the right pick at second."},
        {"title": "Lectric XP 3.0 owns the folding apartment pick", "body": "Folding form factor plus value price plus 50-mile range is the package that wins for buyers with apartment storage constraints. For renters who need to bring the bike inside, Lectric is the right pick at fourth over the larger alternatives."},
    ],
    zh_c="Specialized Turbo Vado SL 2 守第一，輕量通勤車架設計加 SL 動力系統加成熟的 Mission Control App 整合，對要電輔感但不要 moped 重量的日常通勤買家還是對的。國殤日這禮拜把 Turbo Vado SL 2 砍到 NT$105,000，型號今年最低。\n\nRide1Up Roadster V3 第二守價值通勤之選，輕量車架加靈活操控加精準速度控制，對首次買電輔車的買家就是對的。\n\nAventon Level 3 第三守直立通勤之選，扭力感測器加整合燈具對要更輕鬆騎姿的買家就是對的。\n\nLectric XP 3.0 第四守折疊之選，C/P 值加 50 英里續航對公寓收納受限的買家就是對的。Rad Power RadCity 5 Plus 守載貨能力之選。Trek FX+ 2 守公路車外型之選，要更輕的買家。Specialized Globe Haul ST 守載貨車之選，要全家出遊載貨能力的家長。\n\nGlobe Haul 以下整片無聊，務實建議價值從 Ride1Up 開始、頂級從 Specialized 開始。",
    zh_h=[
        {"title": "Specialized Turbo Vado SL 2 NT$105,000 是國殤日王", "body": "輕量通勤車架加 SL 動力系統加 Mission Control App 的組合，對要電輔感但不要 moped 重量的日常通勤者就是對的。國殤日定價是型號今年最低。第一名很明確。"},
        {"title": "Ride1Up Roadster V3 拿下價值通勤之選", "body": "輕量車架加靈活操控加精準速度控制的組合，對首次買電輔車的買家就是對的。要品質但不要溢價的買家，Ride1Up 第二名就是對的。"},
        {"title": "Lectric XP 3.0 拿下折疊公寓之選", "body": "折疊外型加價值定價加 50 英里續航的組合，對公寓收納受限的買家就是對的。需要把車牽進室內的租屋族，Lectric 第四名比更大的替代品對。"},
    ],
)


# ============================================================
# best-electric-scooters
# ============================================================
add(
    "best-electric-scooters",
    refs=[
        {"title": "Best Electric Scooters in 2026 Based on Real-World Tests", "url": "https://eridehero.com/best-electric-scooters/", "source": "ERide Hero"},
        {"title": "Segway Max G3 review", "url": "https://www.cnn.com/cnn-underscored/reviews/best-electric-scooters", "source": "CNN Underscored"},
        {"title": "Best electric scooters commuting 2026", "url": "https://apolloscooters.co/blogs/news/best-electric-scooters-for-commuting-2026", "source": "Apollo Scooters"},
    ],
    en_c="Segway Max G3 stays first because the dual-hydraulic adjustable suspension plus the 11-inch self-healing tubeless tires plus the 28 mph top speed is the combination that delivers a genuinely composed ride at price-tier levels other commuter scooters cannot match. The Memorial Day discount this week puts the Max G3 at $1,099 which is the cheapest the G3 has been all year. Apollo City Pro at second holds the dual-motor commuter pick and the hydraulic brakes plus the 50-mile claimed range is the right pick for buyers who care about real-world distance even if the actual measured range is 30-50% lower. NIU 100F at third holds the foldable portability pick and the under-desk fit plus the subway-friendly form factor is the right pick for the urban-commute use case. Segway E3 Pro at fourth holds the reliable first-scooter pick and the Segway support network is genuinely the smartest argument for the lower-power tier. Apollo Phantom V3 holds the performance pick for buyers who care about top speed over composure. Razor EcoSmart Metro HD holds the bike-replacement pick. Below the Razor the field is uninspiring and the practical advice is to either stretch for the Max G3 or settle on the E3 Pro for first-time buyers.",
    en_h=[
        {"title": "Segway Max G3 at $1,099 is the Memorial Day deal", "body": "Dual-hydraulic suspension plus 11-inch self-healing tubeless tires plus 28 mph is the combination that other commuter scooters cannot match at this price tier. Memorial Day price is the cheapest the G3 has been all year. First place is decisive."},
        {"title": "Real-world range is 30-50% lower than claimed", "body": "Segway G3 displays 25 miles at full charge but reviewers consistently measured 16-17 miles. This is the practical buying advice that matters more than the spec sheet. Cold weather cuts another 15%. Plan your commute based on measured range, not marketing copy."},
        {"title": "Segway E3 Pro is the reliable first-scooter pick", "body": "Segway's experience building scooters longer than almost anyone is the right reason to start at fourth place rather than chasing the spec sheet at lower price tiers. For first-time buyers who want a reliable platform, E3 Pro is the right pick."},
    ],
    zh_c="Segway Max G3 守第一，雙液壓可調懸吊加 11 吋自癒無內胎輪胎加 28 mph 極速，這個組合提供其他通勤滑板車這個價位帶做不到的沉穩騎乘感。國殤日這禮拜把 Max G3 砍到 NT$33,000，G3 今年最低。\n\nApollo City Pro 第二守雙馬達通勤之選，液壓煞車加 50 英里宣稱續航對在意真實距離的買家就是對的，即便實測續航比宣稱低 30 到 50%。\n\nNIU 100F 第三守可折疊可攜之選，能塞辦公桌下加捷運友善外型對都市通勤就是對的。\n\nSegway E3 Pro 第四守可靠首支滑板車之選，Segway 支援網路在低功率帶就是最聰明的論述。\n\nApollo Phantom V3 守性能之選，在意極速勝過沉穩的買家。Razor EcoSmart Metro HD 守取代腳踏車之選。\n\nRazor 以下整片無聊，務實建議硬撐去 Max G3 或定在 E3 Pro 給首次買家。",
    zh_h=[
        {"title": "Segway Max G3 NT$33,000 是國殤日王", "body": "雙液壓懸吊加 11 吋自癒無內胎輪胎加 28 mph 的組合，是其他通勤滑板車這個價位帶做不到的。國殤日定價是 G3 今年最低。第一名很明確。"},
        {"title": "實測續航比宣稱低 30 到 50%", "body": "Segway G3 滿電顯示 25 英里，但評測者一直量到 16 到 17 英里。這個務實建議比規格表重要，冷天還再砍 15%。通勤規劃用實測續航，別看行銷文案。"},
        {"title": "Segway E3 Pro 是可靠首支滑板車之選", "body": "Segway 做滑板車比幾乎所有人都久，這就是第四名從這邊開始、不要在更低價位帶追規格表的對的理由。首次買家要可靠平台，E3 Pro 就是對的選擇。"},
    ],
)


# ============================================================
# best-treadmills
# ============================================================
add(
    "best-treadmills",
    refs=[
        {"title": "Best treadmills 2026", "url": "https://www.runnersworld.com/gear/a20865620/best-treadmills/", "source": "Runner's World"},
        {"title": "NordicTrack Commercial 1750 review", "url": "https://www.cnet.com/health/fitness/best-treadmill/", "source": "CNET"},
        {"title": "Peloton Tread Memorial Day sale", "url": "https://www.tomsguide.com/best-picks/best-treadmills", "source": "Tom's Guide"},
    ],
    en_c="NordicTrack Commercial 1750 stays first because the 12 mph top speed plus the 15% incline plus the iFit live workout integration is the combination that wins for the typical at-home runner, and the Memorial Day discount this week puts it at $1,899 which is the cheapest the 1750 has been all year. Peloton Tread at second holds the connected-class pick and the instructor-led running classes plus the form-tracking integration is the right pick for buyers who care about motivation over self-guided pacing. The Memorial Day cut to $2,995 is reasonable but the upfront premium plus subscription still keeps it from first. Sole F85 at third holds the durability pick and the lifetime motor warranty plus the no-subscription approach is the right pick for buyers who do not want recurring fees. ProForm Pro 9000 at fourth holds the value flagship pick and the iFit integration at a lower price is the package that justifies it over NordicTrack for buyers on a tighter budget. Bowflex Treadmill 22 holds the JRNY-integrated pick. Echelon Stride holds the folding pick for buyers with space constraints. Below the Echelon the field is uninspiring and the practical advice is to start with the ProForm or stretch for the Commercial 1750.",
    en_h=[
        {"title": "NordicTrack Commercial 1750 at $1,899 is the Memorial Day deal", "body": "12 mph top speed plus 15% incline plus iFit live workout integration is the combination for typical at-home runners. Memorial Day price is the cheapest the 1750 has been all year. First place is decisive."},
        {"title": "Peloton Tread instructor-led classes wins on motivation", "body": "Instructor-led running classes plus form-tracking integration is the right pick for buyers who care about motivation over self-guided pacing. For users who need someone telling them what to do, Peloton is the right pick at second despite the subscription."},
        {"title": "Sole F85 wins on no-subscription durability", "body": "Lifetime motor warranty plus no recurring fees is the right pick for buyers who do not want subscription content. For users who design their own workouts and just need a reliable platform, Sole F85 is the right pick at third."},
    ],
    zh_c="NordicTrack Commercial 1750 守第一，12 mph 極速加 15% 坡度加 iFit 直播課程整合，這套組合對典型居家跑者就是對的。國殤日這禮拜把 1750 砍到 NT$57,000，今年最低。\n\nPeloton Tread 第二守連線課程之選，教練帶領跑步課加姿勢追蹤整合，對在意動力勝過自主配速的買家就是對的。國殤日 NT$90,000 折扣還行但前期溢價加訂閱讓它上不去。\n\nSole F85 第三守耐用之選，馬達終身保固加免訂閱做法，對不想付持續費用的買家就是對的。\n\nProForm Pro 9000 第四守價值旗艦之選，iFit 整合搭較低價格，對預算更緊的買家比 NordicTrack 對。Bowflex Treadmill 22 守 JRNY 整合之選。Echelon Stride 守折疊之選，空間受限的買家。\n\nEchelon 以下整片無聊，務實建議從 ProForm 開始或硬撐去 Commercial 1750。",
    zh_h=[
        {"title": "NordicTrack Commercial 1750 NT$57,000 是國殤日王", "body": "12 mph 極速加 15% 坡度加 iFit 直播課程整合的組合，對典型居家跑者就是對的。國殤日定價是 1750 今年最低。第一名很明確。"},
        {"title": "Peloton Tread 教練帶領課程靠動力贏", "body": "教練帶領跑步課加姿勢追蹤整合，對在意動力勝過自主配速的買家就是對的。要有人告訴他做什麼的使用者，雖然有訂閱費 Peloton 第二名還是對的。"},
        {"title": "Sole F85 靠免訂閱耐用度贏", "body": "馬達終身保固加免持續費用，對不要訂閱內容的買家就是對的。自己設計訓練、只要可靠平台的使用者，Sole F85 第三名就是對的。"},
    ],
)


# ============================================================
# best-massage-guns
# ============================================================
add(
    "best-massage-guns",
    refs=[
        {"title": "Best massage guns 2026", "url": "https://www.tomsguide.com/best-picks/best-massage-guns", "source": "Tom's Guide"},
        {"title": "Theragun Pro Plus review", "url": "https://www.cnet.com/health/fitness/best-massage-gun/", "source": "CNET"},
        {"title": "Hyperice Hypervolt 2 Pro review", "url": "https://www.wired.com/gallery/best-massage-guns/", "source": "Wired"},
    ],
    en_c="Theragun Pro Plus stays first because the QuietForce technology plus the 30-pound stall force plus the now-mature Therabody app guidance is the combination that still wins for the recovery-serious athlete, and the Memorial Day discount this week puts the Pro Plus at $499 which is the cheapest the flagship has been all year. Hyperice Hypervolt 2 Pro at second holds the quiet-and-versatile pick and the five attachment heads plus the pressure sensor display is the package that justifies it over the Theragun for buyers who care about real-time feedback. Bob and Brad C2 at third holds the value pick and the sub-$100 price plus the genuine therapeutic depth is the package that wins for first-time massage gun buyers. Ekrin Athletics B37S at fourth holds the mid-range pick and the longer battery life plus the lifetime warranty is the right pick for buyers who do not want the Theragun premium. Therabody Theragun Mini 2 holds the portable pick. LifePro Sonic LX Professional holds the budget percussion pick for buyers under $80. Below the LifePro the field gets uninspiring and the practical advice is to either start with the Bob and Brad or stretch for the Pro Plus.",
    en_h=[
        {"title": "Theragun Pro Plus at $499 is the Memorial Day deal", "body": "QuietForce technology plus 30-pound stall force plus mature Therabody app is the combination for recovery-serious athletes. Memorial Day price is the cheapest the flagship has been all year. First place is decisive."},
        {"title": "Hypervolt 2 Pro pressure sensor display wins on feedback", "body": "Five attachment heads plus pressure sensor display is the package that justifies it over the Theragun for buyers who care about real-time feedback. For users who want to see exactly how hard they are pressing, Hypervolt is the right pick at second."},
        {"title": "Bob and Brad C2 is the right entry pick", "body": "Sub-$100 price plus genuine therapeutic depth is the package that wins for first-time massage gun buyers. For users who want to try the therapy without committing $300+, Bob and Brad is the right pick at third."},
    ],
    zh_c="Theragun Pro Plus 守第一，QuietForce 技術加 30 磅失速力道加成熟的 Therabody App 指引，這套組合對認真在意恢復的運動員還是對的。國殤日這禮拜把 Pro Plus 砍到 NT$15,000，旗艦今年最低。\n\nHyperice Hypervolt 2 Pro 第二守安靜加多功能之選，五種按摩頭加壓力感測顯示，對在意即時反饋的買家就是對的。\n\nBob and Brad C2 第三守價值之選，NT$3,000 以下加真實治療深度，對首次買按摩槍的買家就是對的。\n\nEkrin Athletics B37S 第四守中階之選，更長續航加終身保固，對不要 Theragun 溢價的買家就是對的。\n\nTherabody Theragun Mini 2 守可攜之選。LifePro Sonic LX Professional 守預算敲擊之選，NT$2,500 以下的買家。\n\nLifePro 以下整片無聊，務實建議從 Bob and Brad 開始或硬撐去 Pro Plus。",
    zh_h=[
        {"title": "Theragun Pro Plus NT$15,000 是國殤日王", "body": "QuietForce 技術加 30 磅失速力道加成熟 Therabody App 的組合，對認真恢復的運動員就是對的。國殤日定價是旗艦今年最低。第一名很明確。"},
        {"title": "Hypervolt 2 Pro 壓力感測顯示靠反饋贏", "body": "五種按摩頭加壓力感測顯示的組合，對在意即時反饋的買家比 Theragun 對。要清楚看到自己壓多用力的使用者，Hypervolt 第二名就是對的。"},
        {"title": "Bob and Brad C2 是對的入門之選", "body": "NT$3,000 以下加真實治療深度的組合，對首次買按摩槍的買家就是對的。想試試這個療法但不想花 NT$9,000 以上的使用者，Bob and Brad 第三名就是對的。"},
    ],
)


# ============================================================
# best-portable-power-stations
# ============================================================
add(
    "best-portable-power-stations",
    refs=[
        {"title": "Best portable power stations 2026", "url": "https://www.tomsguide.com/best-picks/best-portable-power-stations", "source": "Tom's Guide"},
        {"title": "Jackery Explorer 2000 v2 Plus review", "url": "https://www.wired.com/gallery/best-portable-power-stations/", "source": "Wired"},
        {"title": "EcoFlow Delta Pro 3 review", "url": "https://www.theverge.com/24/best-portable-power-station", "source": "The Verge"},
    ],
    en_c="EcoFlow Delta Pro 3 stays first because the 4000W AC output plus the expandable battery architecture plus the new X-Boost technology that finally handles 4500W appliances is the combination that wins for whole-home backup, and the Memorial Day discount this week puts the Delta Pro 3 at $2,599 which is the cheapest the flagship has been all year. Jackery Explorer 2000 v2 Plus at second holds the camping-and-emergency pick and the LFP battery plus the 70-minute fast charge is the right pick for buyers who want a reliable portable platform without the whole-home architecture. Anker Solix F2000 at third holds the value flagship pick and the 2048Wh capacity plus the price tier is the package that justifies it over the Jackery for buyers who want more capacity per dollar. Bluetti AC180 at fourth holds the mid-range pick and the 1800W output plus the LFP battery at the lower price is the right pick for buyers who want flagship features at the mid-tier. Goal Zero Yeti 1500X holds the durability pick for buyers who do contractor work. Anker 535 holds the truly-portable pick for buyers who want under-15-pound weight. Below the Anker 535 the field is uninspiring and the practical advice is to start with the Bluetti AC180 or stretch for the Delta Pro 3 for whole-home backup needs.",
    en_h=[
        {"title": "EcoFlow Delta Pro 3 at $2,599 is the Memorial Day deal", "body": "4000W AC output plus expandable battery plus X-Boost for 4500W appliances is the combination for whole-home backup. Memorial Day price is the cheapest the Delta Pro 3 has been all year. First place is decisive."},
        {"title": "Jackery Explorer 2000 v2 Plus wins the camping pick", "body": "LFP battery plus 70-minute fast charge is the right pick for buyers who want a reliable portable platform without the whole-home architecture. For camping and emergency backup, Jackery is the right pick at second over the larger EcoFlow."},
        {"title": "Anker Solix F2000 wins on capacity per dollar", "body": "2048Wh capacity plus the price tier is the package that justifies it over the Jackery for buyers who want more capacity per dollar. For high-draw appliances like fridge backup during multi-day outages, Anker is the right pick at third."},
    ],
    zh_c="EcoFlow Delta Pro 3 守第一，4000W AC 輸出加可擴充電池架構加新的 X-Boost 技術終於能撐 4500W 家電，這套組合對全屋備援就是對的。國殤日這禮拜把 Delta Pro 3 砍到 NT$78,000，旗艦今年最低。\n\nJackery Explorer 2000 v2 Plus 第二守露營跟緊急之選，LFP 電池加 70 分鐘快充對要可靠可攜平台但不要全屋架構的買家就是對的。\n\nAnker Solix F2000 第三守價值旗艦之選，2048Wh 容量加價位帶，對要更多容量單位元的買家比 Jackery 對。\n\nBluetti AC180 第四守中階之選，1800W 輸出加 LFP 電池加較低價格，對要旗艦功能但在中階價位的買家就是對的。\n\nGoal Zero Yeti 1500X 守耐用之選，工程承包工作的買家。Anker 535 守真可攜之選，要 15 磅以下重量的買家。\n\nAnker 535 以下整片無聊，務實建議從 Bluetti AC180 開始或全屋備援需求硬撐去 Delta Pro 3。",
    zh_h=[
        {"title": "EcoFlow Delta Pro 3 NT$78,000 是國殤日王", "body": "4000W AC 輸出加可擴充電池加 X-Boost 撐 4500W 家電的組合，對全屋備援就是對的。國殤日定價是 Delta Pro 3 今年最低。第一名很明確。"},
        {"title": "Jackery Explorer 2000 v2 Plus 拿下露營之選", "body": "LFP 電池加 70 分鐘快充，對要可靠可攜平台但不要全屋架構的買家就是對的。露營跟緊急備援，Jackery 第二名比更大的 EcoFlow 對。"},
        {"title": "Anker Solix F2000 靠容量單位元贏", "body": "2048Wh 容量加價位帶，對要更多容量單位元的買家比 Jackery 對。多日停電時要撐冰箱這種高耗電家電的買家，Anker 第三名就是對的。"},
    ],
)


# ============================================================
# best-portable-air-conditioners
# ============================================================
add(
    "best-portable-air-conditioners",
    refs=[
        {"title": "Best portable air conditioners 2026", "url": "https://www.nytimes.com/wirecutter/reviews/best-portable-air-conditioner/", "source": "Wirecutter"},
        {"title": "Midea Duo MAP14HS1TBL review", "url": "https://www.cnet.com/home/smart-home/best-portable-air-conditioner/", "source": "CNET"},
        {"title": "LG LP1419IVSM Memorial Day sale", "url": "https://www.consumerreports.org/home-garden/air-conditioners/", "source": "Consumer Reports"},
    ],
    en_c="Midea Duo MAP14HS1TBL stays first because the dual-hose design plus the inverter compressor plus the 14,000 BTU rating is the combination that delivers actual cooling efficiency where single-hose portables waste 30%+ of their capacity, and the Memorial Day discount this week puts it at $599 which is the cheapest the Duo has been all year ahead of peak cooling season. LG LP1419IVSM at second holds the inverter-quiet pick and the 14,000 BTU plus the lower noise rating is the right pick for buyers who care about bedroom installation. Frigidaire Gallery Quiet Cool at third holds the conventional dual-hose pick and the build quality argument is intact. Whynter ARC-14S at fourth holds the value dual-hose pick and the no-inverter price tier is the right starting point for buyers who do not want the premium. Black+Decker BPACT14HWT holds the value single-hose pick for budget-tight buyers who accept the efficiency penalty. De'Longhi PACAN125ECC holds the eco-pick. Honeywell HF8CESVWK5 holds the smart-features pick. Below the Honeywell the field is uninspiring and the practical advice is to start with the Whynter for dual-hose or stretch for the Midea Duo for the inverter benefit. Hisense AP1419CR1W holds the budget alternative.",
    en_h=[
        {"title": "Midea Duo MAP14HS1TBL at $599 is the Memorial Day deal", "body": "Dual-hose design plus inverter compressor plus 14,000 BTU is the combination that delivers actual cooling efficiency. Single-hose units waste 30%+ of their capacity. Memorial Day price is the cheapest the Duo has been all year. First place is decisive."},
        {"title": "LG LP1419IVSM is the bedroom-quiet pick", "body": "Inverter design plus 14,000 BTU plus lower noise rating is the right pick for buyers who care about bedroom installation. For users who run the AC overnight, LG is the right pick at second over the louder alternatives."},
        {"title": "Single-hose units waste 30%+ of their capacity", "body": "Practical buying advice: dual-hose units extract less hot air from the room than single-hose because they vent makeup air outside. Single-hose units pull room air through the unit and exhaust it, drawing hot makeup air from outside through wall gaps. Dual-hose always wins on efficiency."},
    ],
    zh_c="Midea Duo MAP14HS1TBL 守第一，雙管設計加變頻壓縮機加 14,000 BTU 評級，這個組合提供單管可攜冷氣浪費 30% 以上效率做不到的真正冷卻表現。國殤日這禮拜把它砍到 NT$18,000，旺季前 Duo 今年最低。\n\nLG LP1419IVSM 第二守變頻安靜之選，14,000 BTU 加較低噪音對在意臥室裝設的買家就是對的。\n\nFrigidaire Gallery Quiet Cool 第三守傳統雙管之選，做工論述沒退場。\n\nWhynter ARC-14S 第四守價值雙管之選，沒有變頻的價位帶，對不要溢價的買家就是對的起點。\n\nBlack+Decker BPACT14HWT 守價值單管之選，預算緊接受效率懲罰的買家。De'Longhi PACAN125ECC 守節能之選。Honeywell HF8CESVWK5 守智慧功能之選。\n\nHoneywell 以下整片無聊，務實建議雙管從 Whynter 開始或為變頻優勢硬撐去 Midea Duo。Hisense AP1419CR1W 守預算替代品。",
    zh_h=[
        {"title": "Midea Duo MAP14HS1TBL NT$18,000 是國殤日王", "body": "雙管設計加變頻壓縮機加 14,000 BTU 的組合，提供真正冷卻效率。單管浪費 30% 以上容量。國殤日定價是 Duo 今年最低。第一名很明確。"},
        {"title": "LG LP1419IVSM 是臥室安靜之選", "body": "變頻設計加 14,000 BTU 加較低噪音的組合，對在意臥室裝設的買家就是對的。整晚開冷氣的使用者，LG 第二名比較吵的替代品對。"},
        {"title": "單管機浪費 30% 以上容量", "body": "務實建議：雙管機從室內抽出的熱氣比單管多，因為它從外面引進補充氣。單管機把室內空氣抽過機體排到外面，從牆縫拉進外面的熱補充氣。效率永遠雙管贏。"},
    ],
)


# ============================================================
# best-robot-lawn-mowers
# ============================================================
add(
    "best-robot-lawn-mowers",
    refs=[
        {"title": "Best robot lawn mowers 2026", "url": "https://www.popularmechanics.com/home/lawn-garden/g25683024/best-robotic-lawn-mowers/", "source": "Popular Mechanics"},
        {"title": "Husqvarna Automower 450X review", "url": "https://www.tomsguide.com/best-picks/best-robot-lawn-mowers", "source": "Tom's Guide"},
        {"title": "Mammotion LUBA AWD 5000 review", "url": "https://www.theverge.com/24/best-robot-lawn-mower", "source": "The Verge"},
    ],
    en_c="Mammotion LUBA AWD 5000 stays first because the wire-free RTK navigation plus the 4-wheel-drive capability plus the 1.25-acre coverage is still the combination that wins for buyers with larger yards who do not want to bury boundary wire, and the Memorial Day discount this week puts it at $2,799 which is the cheapest the AWD 5000 has been all year. Husqvarna Automower 450X at second holds the boundary-wire premium pick and the proven reliability across 0.8-acre yards plus the brand reputation is the right pick for buyers who do not mind the install. EcoFlow Blade at third holds the smart-features pick and the lift-detection plus the rain sensor is the right pick for buyers who want a more automated platform. Worx Landroid Vision M20 at fourth holds the camera-vision pick and the no-boundary-wire approach plus the value math is the right pick for smaller yards. Segway Navimow H800N holds the mid-yard wire-free pick. Robomow RX12u holds the small-yard value pick. Honda Miimo HRM 70 Live holds the boundary-wire mid-pack pick. Below the Honda the field is uninspiring and the practical advice is to start with the Worx for small yards or stretch for the LUBA AWD 5000 for larger acreage.",
    en_h=[
        {"title": "Mammotion LUBA AWD 5000 at $2,799 is the Memorial Day deal", "body": "Wire-free RTK navigation plus 4WD plus 1.25-acre coverage is the combination for larger yards without buried boundary wire. Memorial Day price is the cheapest the AWD 5000 has been all year. First place is decisive."},
        {"title": "Husqvarna Automower 450X wins on proven reliability", "body": "Boundary-wire install plus 0.8-acre coverage plus the brand reputation built over a decade is the right pick for buyers who do not mind the install. For users who want the longest track record, Husqvarna is the right pick at second."},
        {"title": "Worx Landroid Vision wins small-yard wire-free", "body": "Camera-vision plus no-boundary-wire approach plus the value math is the right pick for smaller yards under 0.25 acre. For suburban yards where buried wire is not worth it but cameras suffice, Worx is the right pick at fourth."},
    ],
    zh_c="Mammotion LUBA AWD 5000 守第一，免線 RTK 導航加四輪驅動加 1.25 英畝覆蓋，這套組合對較大院子且不想埋邊界線的買家還是對的。國殤日這禮拜把它砍到 NT$84,000，AWD 5000 今年最低。\n\nHusqvarna Automower 450X 第二守邊界線頂級之選，0.8 英畝院子的證實可靠度加品牌口碑，對不介意安裝的買家就是對的。\n\nEcoFlow Blade 第三守智慧功能之選，舉起偵測加雨水感測，對要更自動化平台的買家就是對的。\n\nWorx Landroid Vision M20 第四守相機視覺之選，免邊界線做法加 C/P 值，對較小院子就是對的。\n\nSegway Navimow H800N 守中院免線之選。Robomow RX12u 守小院價值之選。Honda Miimo HRM 70 Live 守邊界線中段之選。\n\nHonda 以下整片無聊，務實建議小院從 Worx 開始、大院子硬撐去 LUBA AWD 5000。",
    zh_h=[
        {"title": "Mammotion LUBA AWD 5000 NT$84,000 是國殤日王", "body": "免線 RTK 導航加四輪驅動加 1.25 英畝覆蓋的組合，對較大院子且不想埋邊界線的買家就是對的。國殤日定價是 AWD 5000 今年最低。第一名很明確。"},
        {"title": "Husqvarna Automower 450X 靠證實可靠度贏", "body": "邊界線安裝加 0.8 英畝覆蓋加十年累積的品牌口碑，對不介意安裝的買家就是對的。要最長履歷的使用者，Husqvarna 第二名就是對的。"},
        {"title": "Worx Landroid Vision 拿下小院免線之選", "body": "相機視覺加免邊界線做法加 C/P 值，對 0.25 英畝以下小院就是對的。郊區院子埋線不划算但相機夠用的情境，Worx 第四名就是對的。"},
    ],
)


def apply_update(slug, content):
    fpath = RANKINGS_DIR / f"{slug}.json"
    data = json.load(open(fpath))
    last = data["history"][-1]
    rankings = json.loads(json.dumps(last["rankings"]))
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": content["references"],
        "i18n": {
            "en": {
                "commentary": content["en_commentary"],
                "highlights": content["en_highlights"],
            },
            "zh-tw": {
                "commentary": content["zh_commentary"],
                "highlights": content["zh_highlights"],
            },
        },
    }
    found = False
    for i, h in enumerate(data["history"]):
        if h["date"] == DATE:
            data["history"][i] = entry
            found = True
            break
    if not found:
        data["history"].append(entry)
    json.dump(data, open(fpath, "w"), indent=2, ensure_ascii=False)
    return found


if __name__ == "__main__":
    all_jsons = {p.stem for p in RANKINGS_DIR.glob("*.json")}
    missing = all_jsons - set(CONTENT.keys())
    extra = set(CONTENT.keys()) - all_jsons
    if missing:
        print(f"MISSING: {sorted(missing)}")
    if extra:
        print(f"EXTRA: {sorted(extra)}")
    updated = 0
    for slug, content in CONTENT.items():
        if slug in extra:
            continue
        found = apply_update(slug, content)
        print(f"{'UPDATED' if found else 'ADDED'}: {slug}")
        updated += 1
    print(f"\nDone. {updated}/{len(all_jsons)} files updated.")
