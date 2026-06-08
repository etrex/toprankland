import sys; sys.path.insert(0, "/Users/etrexkuo/toprankland/scripts")
from daily_helper import load, save, upsert, last_rankings, DATE

def do(name, refs, en, zh):
    d, p = load(name)
    entry = {
        "date": DATE,
        "rankings": last_rankings(d),
        "references": refs,
        "i18n": {"en": en, "zh-tw": zh},
    }
    upsert(d, entry)
    save(p, d)
    print("updated", name)

# ---------------- best-4k-tvs ----------------
do("best-4k-tvs.json",
   [
     {"title": "The 3 Best OLED TVs of 2026", "url": "https://www.rtings.com/tv/reviews/best/by-type/oled", "source": "RTINGS"},
     {"title": "Best OLED TV 2026: top sets fully reviewed", "url": "https://www.whathifi.com/best-buys/tvs/best-oled-tvs", "source": "What Hi-Fi?"},
   ],
   {
     "commentary": "The LG C6 OLED stays at number one because it is the TV I recommend to the most people without a second thought. It brings brighter, richer, more refined picture than the already-excellent C5, the gaming features are complete with four HDMI 2.1 ports, and LG prices it where a normal household can reach a flagship-tier panel. For the vast majority of buyers this is the sweet spot of the entire market. The Samsung S95F holds second as the best-performing OLED RTINGS tested, the QD-OLED panel goes brighter than LG's and the all-round image quality is genuinely reference-grade, the pick for people who want the absolute best and will pay for it. The Sony Bravia 8 II stays third on Sony's processing, which still pulls the most natural, three-dimensional image of the group, the choice for film purists. The LG G6 holds fourth as the wall-mount flagship. Nothing this week reordered the field. The read: best value-to-quality is the C6, outright best picture is the S95F, most cinematic is Sony. OLED won, and the only question is how much brightness you are paying for.",
     "highlights": [
       {"title": "LG C6 is the sweet spot of the market", "body": "Brighter and more refined than the excellent C5, complete with four HDMI 2.1 ports, priced where a normal household reaches a flagship panel. For the most buyers it is the easy recommendation at number one."},
       {"title": "Samsung S95F is the outright best picture", "body": "Its QD-OLED panel goes brighter than LG's with reference-grade all-round quality. For people who want the absolute best image and will pay for it, it is the clear second."},
       {"title": "Sony Bravia 8 II is the cinematic pick", "body": "Sony's processing still pulls the most natural, three-dimensional image of the group. For film purists who value lifelike rendering over peak brightness, it holds a firm third."},
       {"title": "OLED won, brightness is the variable", "body": "Every top pick is OLED now; the difference is how much peak brightness you pay for. Decide whether a bright room demands the S95F or a controlled room lets the C6 shine, then buy accordingly."},
     ],
   },
   {
     "commentary": "LG C6 OLED 我還是放第一，因為它是我會二話不說推薦給最多人的電視。它的畫面比本來就很優秀的 C5 更亮、更濃、更精緻，遊戲功能完整、四個 HDMI 2.1，LG 又把價格訂在一般家庭搆得到旗艦級面板的位置。對絕大多數買家，這就是整個市場的甜蜜點。Samsung S95F 守第二，是 RTINGS 測過表現最佳的 OLED，QD-OLED 面板比 LG 更亮，整體畫質真的是參考級，給想要絕對最好、又願意付錢的人。Sony Bravia 8 II 守第三，靠 Sony 的處理，依然拉出這群裡最自然、最立體的畫面，是電影純粹派的選擇。LG G6 守第四，是壁掛旗艦。這週沒事件重排。判斷：性價比畫質選 C6、純粹最佳畫面選 S95F、最電影感選 Sony。OLED 贏了，唯一的問題是你為多少亮度付錢。",
     "highlights": [
       {"title": "LG C6 是市場的甜蜜點", "body": "比優秀的 C5 更亮更精緻、四個 HDMI 2.1 完整，價格訂在一般家庭搆得到旗艦面板的位置。對最多買家它是第一名的好推薦。"},
       {"title": "Samsung S95F 是純粹最佳畫面", "body": "QD-OLED 面板比 LG 更亮，整體畫質參考級。想要絕對最好的畫面又願意付錢的人，它是明確第二。"},
       {"title": "Sony Bravia 8 II 是電影感選擇", "body": "Sony 的處理依然拉出這群裡最自然最立體的畫面。重視擬真勝過峰值亮度的電影純粹派，它穩在第三。"},
       {"title": "OLED 贏了，亮度是變數", "body": "現在每個首選都是 OLED，差別是你為多少峰值亮度付錢。亮房間要 S95F、可控光房間 C6 就夠亮，照這個決定買哪台。"},
     ],
   })

# ---------------- best-portable-projectors ----------------
do("best-portable-projectors.json",
   [
     {"title": "Best portable projector 2026 reviews", "url": "https://www.projectorcentral.com/best-portable-projectors.htm", "source": "Projector Central"},
     {"title": "Best Mini Projectors 2026: tested picks", "url": "https://www.tomsguide.com/best-picks/best-portable-projectors", "source": "Tom's Guide"},
   ],
   {
     "commentary": "The XGIMI MoGo 4 Laser stays at number one because it nails the thing portable projectors usually botch: it is genuinely bright enough to watch before full dark, the built-in battery makes it actually portable, and Google TV onboard means no extra streaming stick to fumble with. For the broadest set of buyers who want a grab-and-go big screen, this is the one that does not disappoint outdoors. The LG CineBeam Q holds second on design and image quality, it is the most beautifully built portable here and the picture punches above its size, the pick for people who want something that looks as good off as on. The Hisense M2 Pro stays third as the brightness-and-value choice for buyers who prioritize a watchable image over portability polish. The Nebula Mars 3 holds fourth as the rugged outdoor option with the best battery life for camping. Nothing this week reordered the field. The read: best all-round portable is the MoGo 4, best looking is the CineBeam Q, brightest value is Hisense, toughest for outdoors is the Mars 3. Match it to where you will actually watch.",
     "highlights": [
       {"title": "XGIMI MoGo 4 Laser nails portability", "body": "Bright enough to watch before full dark, a real built-in battery and Google TV onboard with no extra stick. For a grab-and-go big screen that does not disappoint outdoors, it holds number one."},
       {"title": "LG CineBeam Q wins on design and picture", "body": "The most beautifully built portable here, with image quality that punches above its size. For buyers who want something that looks as good off as on, it is the clear second."},
       {"title": "Hisense M2 Pro is the brightness-value pick", "body": "It prioritizes a watchable, bright image over portability polish for less money. For buyers who care most about seeing the picture clearly, it holds a firm third."},
       {"title": "Match it to where you watch", "body": "Backyard movie nights want brightness and battery, a bedroom wants design and quiet. Decide your main viewing spot first, because the right portable projector depends entirely on the room or the lack of one."},
     ],
   },
   {
     "commentary": "XGIMI MoGo 4 Laser 我還是放第一，因為它把可攜投影機通常會搞砸的事做對：它真的夠亮，全黑之前就能看，內建電池讓它真的可攜，內建 Google TV 代表不用再插一根串流棒手忙腳亂。對最廣、想要拿了就走大螢幕的買家，這台在戶外不會讓你失望。LG CineBeam Q 守第二，靠設計跟畫質，是這裡做工最漂亮的可攜款，畫面表現超越它的體積，給想要關機也好看的人。Hisense M2 Pro 守第三，是亮度兼性價比選擇，給把看得清楚擺在可攜精緻之前的買家。Nebula Mars 3 守第四，是耐用戶外選擇，露營電池續航最好。這週沒事件重排。判斷：全能可攜選 MoGo 4、最好看選 CineBeam Q、最亮性價比選 Hisense、最耐戶外選 Mars 3。對準你真的會在哪看。",
     "highlights": [
       {"title": "XGIMI MoGo 4 Laser 把可攜做對", "body": "全黑前就夠亮能看、真的有內建電池、內建 Google TV 不用插棒。要拿了就走又在戶外不失望的大螢幕，守住第一。"},
       {"title": "LG CineBeam Q 贏在設計跟畫面", "body": "這裡做工最漂亮的可攜款，畫質超越它的體積。想要關機也好看的買家，它是明確第二。"},
       {"title": "Hisense M2 Pro 是亮度性價比選擇", "body": "它用更低價格把看得清楚的亮畫面擺在可攜精緻之前。最在意畫面看得清的買家，它穩在第三。"},
       {"title": "對準你會在哪看", "body": "後院電影夜要亮度跟電池，臥室要設計跟安靜。先決定主要觀看地點，因為對的可攜投影機完全取決於那個房間或沒有房間。"},
     ],
   })

# ---------------- best-e-readers ----------------
do("best-e-readers.json",
   [
     {"title": "Best ereaders in 2026: top ebook readers tested", "url": "https://www.techradar.com/best/best-ereader", "source": "TechRadar"},
     {"title": "The Top 8 Best e-Readers to buy for 2026", "url": "https://goodereader.com/blog/electronic-readers/the-top-8-best-e-readers-to-buy-for-spring-2026", "source": "Good e-Reader"},
   ],
   {
     "commentary": "The Kindle Paperwhite 2025 stays at number one because it is the e-reader that gets everything right for the price most people will pay. The 7-inch 300ppi screen is glare-free, page turns are about 25 percent faster than the last generation, it is waterproof to IPX8, and the battery runs up to twelve weeks. Pair that with the deepest store and Audible integration and it is the default I hand to anyone who just wants to read. The Kobo Libra Colour holds second and is the better buy for a specific reader: anyone who borrows from the library via Libby or OverDrive, or wants color and open file support. It is the best per-dollar feature set in the category and my pick for manga and comics. The Kindle Colorsoft stays third as Amazon's color answer for people locked into the Kindle store. The Kobo Clara BW holds fourth as the value library pick. Nothing this week reordered the field. The read: most readers should buy the Paperwhite, library borrowers should buy Kobo, and color is now genuinely worth it if you read comics.",
     "highlights": [
       {"title": "Kindle Paperwhite gets everything right", "body": "A glare-free 7-inch 300ppi screen, 25 percent faster page turns, IPX8 waterproofing and up to twelve weeks of battery, plus the deepest store. For anyone who just wants to read, it holds number one."},
       {"title": "Kobo Libra Colour is the library borrower's pick", "body": "Native Libby and OverDrive support plus color and open file handling make it the better buy for library users. The best per-dollar feature set in the category keeps it a firm second."},
       {"title": "Color is finally worth it for comics", "body": "The Libra Colour and Kindle Colorsoft make manga and comics genuinely enjoyable on e-ink for the first time. If you read illustrated content, color is no longer a gimmick, it is a real upgrade."},
       {"title": "Pick by where your books come from", "body": "Amazon store loyalty means Kindle; library borrowing means Kobo. The ecosystem you read inside matters more than the hardware, so let your book source decide the brand before you compare screens."},
     ],
   },
   {
     "commentary": "Kindle Paperwhite 2025 我還是放第一，因為它在多數人會付的價格上把每件事都做對。7 吋 300ppi 螢幕無眩光、翻頁比上一代快約 25 趴、IPX8 防水、電池撐到十二週。配上最深的書店跟 Audible 整合，它是我會直接遞給只想看書的人的預設。Kobo Libra Colour 守第二，對特定讀者是更好的買法：任何用 Libby 或 OverDrive 借圖書館書、或想要彩色跟開放格式支援的人。它是這類別每塊錢功能最強的，也是我漫畫的選擇。Kindle Colorsoft 守第三，是 Amazon 的彩色答案，給綁在 Kindle 書店的人。Kobo Clara BW 守第四，是性價比圖書館選擇。這週沒事件重排。判斷：多數讀者該買 Paperwhite、借圖書館的該買 Kobo，現在你讀漫畫的話彩色真的值得了。",
     "highlights": [
       {"title": "Kindle Paperwhite 每件事都做對", "body": "無眩光 7 吋 300ppi 螢幕、翻頁快 25 趴、IPX8 防水、電池撐十二週，加上最深的書店。對只想看書的人，守住第一。"},
       {"title": "Kobo Libra Colour 是借書讀者的選擇", "body": "原生 Libby 跟 OverDrive 支援加彩色跟開放格式，讓它對圖書館用戶是更好的買法。每塊錢功能最強，穩在第二。"},
       {"title": "彩色終於對漫畫值得了", "body": "Libra Colour 跟 Kindle Colorsoft 第一次讓漫畫在電子墨水上真的好看。讀圖文內容的話，彩色不再是噱頭，是真升級。"},
       {"title": "照你書從哪來選", "body": "忠於 Amazon 書店就 Kindle、借圖書館就 Kobo。你讀書的生態比硬體重要，比螢幕前先讓書源決定品牌。"},
     ],
   })

# ---------------- best-action-cameras ----------------
do("best-action-cameras.json",
   [
     {"title": "Best action camera 2026 reviews", "url": "https://www.techradar.com/best/best-action-camera", "source": "TechRadar"},
     {"title": "Best Action Cameras 2026: DJI, Insta360, GoPro tested", "url": "https://www.tomsguide.com/best-picks/best-action-cameras", "source": "Tom's Guide"},
   ],
   {
     "commentary": "The DJI Osmo Action 6 stays at number one because DJI has quietly taken the all-round crown from GoPro and earned it. The image quality is the best of the standard action cams, the low-light performance genuinely pulls ahead, the battery lasts in the cold, and the magnetic mount ecosystem just works. For most people buying an action camera today, this is the one that does everything well. The Insta360 Ace Pro 2 holds second and is a legitimate co-leader, the Leica-co-engineered sensor and the flip screen make it the better vlogging tool, so the choice between it and the DJI comes down to whether you face the camera. The GoPro Mission 1 Pro stays third as GoPro's strongest answer, still the most rugged and the deepest mount ecosystem, the safe pick for people already invested. The Insta360 X5 holds fifth as the 360 specialist for creators who want reframing freedom. Nothing this week reordered the field. The read: best all-round is the Osmo Action 6, best for vlogging is the Ace Pro 2, best 360 is the X5.",
     "highlights": [
       {"title": "DJI Osmo Action 6 took the all-round crown", "body": "Best image quality of the standard cams, genuinely better low light, battery that lasts in cold and a magnetic mount that just works. For most action-cam buyers it does everything well, holding number one."},
       {"title": "Insta360 Ace Pro 2 is the vlogging co-leader", "body": "Its Leica-co-engineered sensor and flip screen make it the better front-facing tool. The choice against the DJI comes down to whether you face the camera, which keeps it a very close second."},
       {"title": "GoPro Mission 1 Pro is the safe ecosystem pick", "body": "Still the most rugged with the deepest mount catalog, it is the natural choice for anyone already invested in GoPro accessories. That ecosystem strength holds it a firm third."},
       {"title": "Pick by what you shoot", "body": "All-round adventure leans DJI, face-to-camera vlogging leans Insta360 Ace, immersive 360 leans the X5. Decide whether you point the camera out or at yourself, and the right pick falls out."},
     ],
   },
   {
     "commentary": "DJI Osmo Action 6 我還是放第一，因為 DJI 已經悄悄從 GoPro 手上拿走全能王冠，而且實至名歸。畫質是標準運動相機裡最好的，低光表現真的領先，電池在低溫也撐得住，磁吸配件生態就是好用。對今天多數買運動相機的人，這台每件事都做得好。Insta360 Ace Pro 2 守第二，是名副其實的並列領袖，徠卡共同工程的感光元件加翻轉螢幕讓它是更好的 vlog 工具，所以它跟 DJI 之間的選擇就看你會不會面對鏡頭。GoPro Mission 1 Pro 守第三，是 GoPro 最強的答案，依然最耐用、配件生態最深，給已經投資的人當安全牌。Insta360 X5 守第五，是 360 專家，給想要重構自由的創作者。這週沒事件重排。判斷：全能選 Osmo Action 6、vlog 選 Ace Pro 2、360 選 X5。",
     "highlights": [
       {"title": "DJI Osmo Action 6 拿下全能王冠", "body": "標準相機裡最好的畫質、真的更好的低光、低溫也撐的電池、就是好用的磁吸配件。對多數運動相機買家它每件事都做得好，守第一。"},
       {"title": "Insta360 Ace Pro 2 是 vlog 並列領袖", "body": "徠卡共同工程感光元件加翻轉螢幕讓它是更好的面向自己工具。對上 DJI 的選擇看你會不會面對鏡頭，這讓它緊咬第二。"},
       {"title": "GoPro Mission 1 Pro 是安全生態選擇", "body": "依然最耐用、配件目錄最深，是已經投資 GoPro 配件的人的自然選擇。這份生態優勢讓它穩在第三。"},
       {"title": "照你拍什麼選", "body": "全能冒險偏 DJI、面對鏡頭 vlog 偏 Insta360 Ace、沉浸 360 偏 X5。決定你把鏡頭朝外還是朝自己，對的選擇就出來了。"},
     ],
   })

# ---------------- best-dash-cams ----------------
do("best-dash-cams.json",
   [
     {"title": "Best dash cam 2026 reviews", "url": "https://www.techradar.com/best/best-dash-cam", "source": "TechRadar"},
     {"title": "Best Dash Cams 2026: tested picks", "url": "https://www.tomsguide.com/best-picks/best-dash-cams", "source": "Tom's Guide"},
   ],
   {
     "commentary": "The Viofo A329S stays at number one because it delivers flagship features at a price that embarrasses the premium brands. The video is genuinely sharp day and night, the parking mode is reliable, and you get the connectivity and storage flexibility that used to cost twice as much. For most drivers who want excellent footage without overpaying, this is the smart buy and it is not close. The Vantrue N4 Pro S holds second as the best three-channel option, front, cabin and rear in one unit, which is exactly what rideshare drivers and anyone who wants full coverage needs. The BlackVue Elite 9 stays third as the premium-design choice with the slickest app and cloud features for buyers who want polish and will pay for it. The Thinkware U3000 holds fourth on its image quality and clean install. Nothing this week reordered the field. The read: best value is the A329S, best multi-channel coverage is the Vantrue, best premium experience is BlackVue. Buy the coverage you actually need rather than the most channels you can find.",
     "highlights": [
       {"title": "Viofo A329S delivers flagship features for less", "body": "Sharp day-and-night video, reliable parking mode and connectivity that used to cost twice as much. For drivers who want excellent footage without overpaying, it is the smart buy at number one, and it is not close."},
       {"title": "Vantrue N4 Pro S is the coverage king", "body": "Front, cabin and rear in one three-channel unit is exactly what rideshare drivers and full-coverage buyers need. That complete protection keeps it a firm second."},
       {"title": "BlackVue Elite 9 is the premium experience", "body": "The slickest app and cloud features make it the choice for buyers who want polish and will pay for it. That refinement holds it a solid third for the premium tier."},
       {"title": "Buy the coverage you actually need", "body": "More channels are not automatically better; a rideshare driver needs cabin view, a commuter may not. Decide front-only, front-and-rear or three-channel based on your real risk, then pick the camera."},
     ],
   },
   {
     "commentary": "Viofo A329S 我還是放第一，因為它用讓高階品牌難堪的價格給出旗艦功能。影像日夜都真的銳利、停車模式可靠，連線跟儲存彈性也是過去要兩倍價才有的。對多數想要優秀畫面又不想多花錢的駕駛，這是聰明買法，而且差距不小。Vantrue N4 Pro S 守第二，是最佳三鏡頭選擇，前、車內、後一機到位，這正是網約車司機跟任何想要全覆蓋的人需要的。BlackVue Elite 9 守第三，是高階設計選擇，App 跟雲端功能最滑順，給想要精緻又願意付錢的買家。Thinkware U3000 守第四，靠畫質跟乾淨安裝。這週沒事件重排。判斷：性價比選 A329S、多鏡頭覆蓋選 Vantrue、高階體驗選 BlackVue。買你真正需要的覆蓋，而非找得到最多鏡頭。",
     "highlights": [
       {"title": "Viofo A329S 用更低價給旗艦功能", "body": "日夜都銳利的影像、可靠的停車模式、過去要兩倍價的連線。想要優秀畫面又不想多花錢的駕駛，它是第一名聰明買法，差距不小。"},
       {"title": "Vantrue N4 Pro S 是覆蓋之王", "body": "前、車內、後三鏡頭一機到位，正是網約車司機跟要全覆蓋買家需要的。這份完整保護讓它穩在第二。"},
       {"title": "BlackVue Elite 9 是高階體驗", "body": "最滑順的 App 跟雲端功能，是想要精緻又願意付錢買家的選擇。這份精緻讓它在高階層穩坐第三。"},
       {"title": "買你真正需要的覆蓋", "body": "鏡頭多不自動代表更好，網約車司機要車內視角、通勤族可能不用。照你真實風險決定只要前、前後還是三鏡頭，再選相機。"},
     ],
   })

print("batchE done")
