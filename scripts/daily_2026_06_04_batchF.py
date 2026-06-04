import sys; sys.path.insert(0, "/Users/etrexkuo/toprankland/scripts")
from daily_helper import load, save, upsert, last_rankings, DATE

def apply(fname, refs, en, zh):
    d, p = load(fname)
    entry = {"date": DATE, "rankings": last_rankings(d), "references": refs,
             "i18n": {"en": en, "zh-tw": zh}}
    upsert(d, entry); save(p, d)
    print("updated", fname, "rank count", len(entry["rankings"]))

# ---------------- best-security-cameras.json ----------------
apply("best-security-cameras.json",
[
 {"title":"Best Home Security Cameras of 2026","url":"https://www.security.org/security-cameras/best/","source":"Security.org"},
 {"title":"9 Best Outdoor Security Cameras of 2026, Lab-Tested","url":"https://www.consumerreports.org/home-garden/home-security-cameras/best-outdoor-security-cameras-of-the-year-a2913488128/","source":"Consumer Reports"},
 {"title":"Best home security cameras of 2026","url":"https://www.pcworld.com/article/600008/best-home-security-camera.html","source":"PCWorld"},
],
{
 "commentary": "Heading into June 2026 I am keeping the Reolink Argus 4 Pro at the top, and the latest round of testing only reinforces why. Reviewers across Security.org and Consumer Reports keep landing on the same conclusion I reached: the dual-lens 4K sensor stitches a genuine 180-degree panorama, the bundled solar panel keeps it topped up year round, and ColorX night vision pulls full-color footage out of near darkness. The big theme this week is that the 2026 camera class is finally weaning itself off subscriptions, with 4K going mainstream and on-device AI trimming false alerts, and the Argus 4 Pro embodies all of it while staying cheaper than the brand names above it. The Arlo Pro 5S holds second on the strength of its AI detection, which remains the sharpest at flagging people versus passing cars, and its battery endurance is still class-leading. Eufy's SoloCam S340 stays my value champion at third because its local storage and dual-camera tracking deliver premium behavior with no monthly fee. Google's Nest Cam and the AOSU SolarCam round out the upper tier, with the AOSU still the spec monster whose only knock is price. TP-Link's Tapo C460 continues to punch far above its cost, which is why it anchors the list rather than falling off it. No major launch or recall landed this week to justify reshuffling, so I am holding the order steady and confident.",
 "highlights": [
  {"title":"Reolink Argus 4 Pro stays #1","body":"Dual-lens 4K panorama, solar power and ColorX color night vision keep it the outdoor pick reviewers converge on in 2026."},
  {"title":"Subscriptions on the way out","body":"The 2026 class leans on on-device AI and local storage, cutting false alerts and monthly fees, exactly the Argus 4 Pro's strength."},
  {"title":"Arlo Pro 5S owns AI detection","body":"Its person-versus-vehicle accuracy and long battery life keep it locked at second."},
  {"title":"Eufy SoloCam S340 is the value play","body":"Local storage plus dual-camera tracking give premium behavior with zero monthly cost."},
  {"title":"Tapo C460 punches above its price","body":"TP-Link's budget cam keeps strong AI and storage scores, anchoring the list on value."},
 ],
},
{
 "commentary": "進入 2026 年 6 月，我還是把 Reolink Argus 4 Pro 放第一，這週的測試結果只是讓我更確定。Security.org 跟 Consumer Reports 這幾家評測站的結論跟我一樣，雙鏡頭 4K 真的能拼出完整 180 度全景，附的太陽能板讓它一年四季幾乎不用充電，ColorX 夜視在快全黑的環境下還能拍到彩色畫面，這點很實用。這週整個品類最大的趨勢，就是 2026 的攝影機終於開始擺脫月費，4K 變主流、AI 在機身上判讀減少誤報，而 Argus 4 Pro 把這些全做到了，價格還比上面那些大牌便宜，CP 值很頂。Arlo Pro 5S 守在第二，靠的是它最準的 AI 辨識，分得清楚是人還是路過的車，續航也是同級最強。Eufy SoloCam S340 第三，依然是我心中的性價比王，本地儲存加雙鏡頭追蹤，不用月費就有旗艦級表現。Google Nest Cam 跟 AOSU SolarCam 補上中段，AOSU 規格最猛，唯一的缺點就是貴。TP-Link Tapo C460 用一千多塊的價位打出遠超身價的表現，所以它穩穩留在榜上。這週沒有重大新品或召回事件需要我重排，名次照舊，我很有把握。",
 "highlights": [
  {"title":"Reolink Argus 4 Pro 穩坐第一","body":"雙鏡頭 4K 全景、太陽能供電加 ColorX 彩色夜視，是 2026 各家評測一致推的戶外首選。"},
  {"title":"月費時代正在退場","body":"2026 這批主打機身 AI 跟本地儲存，誤報變少也省月費，正好是 Argus 4 Pro 的強項。"},
  {"title":"Arlo Pro 5S 辨識最準","body":"分得清人跟車，續航又長，第二名當之無愧。"},
  {"title":"Eufy SoloCam S340 主打性價比","body":"本地儲存加雙鏡頭追蹤，不付月費就有旗艦體驗。"},
  {"title":"Tapo C460 超越身價","body":"TP-Link 平價機 AI 跟儲存分數都不差，靠 CP 值穩住榜位。"},
 ],
})

# ---------------- best-video-doorbells.json ----------------
apply("best-video-doorbells.json",
[
 {"title":"Best Doorbell Cameras 2026: Reviewed by Home Security Experts","url":"https://www.security.org/doorbell-camera/best/","source":"Security.org"},
 {"title":"Best video doorbells in 2026: Ring, Nest, Wyze and more tested","url":"https://www.tomsguide.com/us/best-video-doorbells,review-4468.html","source":"Tom's Guide"},
 {"title":"10 Best Video Doorbell Cameras of 2026, Lab-Tested","url":"https://www.consumerreports.org/home-garden/home-security-cameras/best-video-doorbells-of-the-year-a1115426074/","source":"Consumer Reports"},
],
{
 "commentary": "As of June 2026 the Eufy E340 keeps my top spot, and nothing this week changed my mind. Its dual cameras cover the doorstep and a package zone, footage stays on a local hub with no monthly fee, and it installs in minutes, which is exactly the combination most people actually want. The recent Tom's Guide and Consumer Reports refreshes still rank Eufy and the budget no-subscription crowd highly, and that is the wind at this list's back. The Aqara G410 holds second because its Matter and Thread support makes it the smart-home connector that just slots into HomeKit, Google and Alexa without fuss. Google's third-gen Nest Doorbell deserves the callout this cycle: the jump to 2K and a wider 166-degree field of view delivers sharper day and night images, which is why I keep both the wired second and third-gen Nest units on the board. Ring's battery Doorbell Pro still has the cleanest video in the group, though its subscription reliance keeps its value score in check. Tapo's D225 and the Arlo 2K continue to serve buyers who want strong hardware on a tighter budget, and Blink anchors the list as the cheapest reliable entry. The market is competing hard on price and free local storage right now, which favors the order I already have, so I am carrying it forward unchanged.",
 "highlights": [
  {"title":"Eufy E340 stays #1","body":"Dual cameras, free local storage and easy install remain the package buyers want most."},
  {"title":"Aqara G410 is the smart-home glue","body":"Matter and Thread support drops it cleanly into HomeKit, Google and Alexa, holding second."},
  {"title":"Nest 3rd-gen jumps to 2K","body":"Sharper day and night footage plus a 166-degree view keep both wired Nest units on the board."},
  {"title":"Ring Doorbell Pro leads on video","body":"Cleanest image in the group, though subscription reliance caps its value score."},
  {"title":"Budget tier stays strong","body":"Tapo D225, Arlo 2K and Blink keep the lower ranks competitive on price and free storage."},
 ],
},
{
 "commentary": "到 2026 年 6 月，Eufy E340 還是我的第一名，這週也沒有任何消息讓我改變想法。它雙鏡頭同時顧到門口跟包裹區，影像存在自家 Hub 不用月費，幾分鐘就裝好，這組合正是多數人真正想要的。最近 Tom's Guide 跟 Consumer Reports 改版後，Eufy 跟那票免月費的平價機都排得很前面，等於幫這份榜單順風。Aqara G410 守第二，因為它支援 Matter 跟 Thread，能無痛接進 HomeKit、Google 跟 Alexa，是最好用的智慧家庭橋接。這一輪 Google 第三代 Nest Doorbell 值得一提，畫質升到 2K，視角拉寬到 166 度，白天晚上都更清楚，所以我把有線版第二代跟第三代都留在榜上。Ring 電池版 Doorbell Pro 畫質還是全場最乾淨，只是太依賴月費，性價比分數被壓住。Tapo D225 跟 Arlo 2K 繼續服務想要好硬體又預算有限的人，Blink 則是榜上最便宜又可靠的入門選擇。現在整個市場拼的就是價格跟免費本地儲存，剛好對我現有的排序有利，所以名次照舊往前帶。",
 "highlights": [
  {"title":"Eufy E340 穩坐第一","body":"雙鏡頭、免月費本地儲存加好安裝，依然是買家最想要的組合。"},
  {"title":"Aqara G410 是智慧家庭橋接王","body":"支援 Matter 跟 Thread，無痛接進 HomeKit、Google 跟 Alexa，守住第二。"},
  {"title":"Nest 第三代升到 2K","body":"畫質更清楚、視角 166 度，有線第二代跟第三代都留在榜上。"},
  {"title":"Ring Doorbell Pro 畫質最強","body":"全場影像最乾淨，只是依賴月費讓性價比分數受限。"},
  {"title":"平價陣容依舊穩","body":"Tapo D225、Arlo 2K 跟 Blink 靠價格跟免費儲存撐住中後段。"},
 ],
})

# ---------------- best-smart-speakers.json ----------------
apply("best-smart-speakers.json",
[
 {"title":"Best smart speakers in 2026 - Alexa, Google, and Siri tested","url":"https://www.tomsguide.com/us/best-smart-speakers,review-4480.html","source":"Tom's Guide"},
 {"title":"This Smart Speaker Gets Consumer Reports' Top Rating","url":"https://www.bgr.com/2181217/smart-speaker-that-gets-consumer-reports-top-rating/","source":"BGR"},
 {"title":"Best smart speakers 2026: top Amazon Echo, Google Nest and Apple picks","url":"https://www.t3.com/features/best-smart-speaker","source":"T3"},
],
{
 "commentary": "This week handed me a real talking point: a June 1, 2026 BGR piece flagged that Consumer Reports now puts the Sonos Era 300 at the very top of its smart speaker ratings for sound. I respect that result, and the Era 300 stays a strong fourth on my board for exactly that spatial-audio prowess. But my ranking weighs the full smart-speaker job, not pure audio, and that is why the Amazon Echo Studio 2nd-gen keeps my top spot. It pairs genuinely room-filling Dolby Atmos with the deepest smart-home reach, a built-in Zigbee and Matter hub, and Alexa's mature voice control, so it does everything a smart speaker should. The Sonos Era 100 holds second as the best-sounding compact you can hand to a music lover, with the HomePod 2nd-gen at third for Apple households that want tight AirPlay and HomeKit integration. Google's 2026 Home Speaker sits fifth as the smartest assistant in the group. Down the order, Amazon's Echo 4th-gen, the new Echo Dot Max and the evergreen Dot 5th-gen keep value buyers covered, while the HomePod mini anchors the list for Apple fans on a budget. With Sonos winning on audio and Amazon winning on the whole package, the competitive picture is exactly what my order already reflects, so I am holding it.",
 "highlights": [
  {"title":"Echo Studio 2nd-gen stays #1","body":"Dolby Atmos sound plus a built-in Zigbee and Matter hub make it the most complete smart speaker."},
  {"title":"Sonos Era 300 wins on pure sound","body":"A June 1 Consumer Reports top rating confirms its spatial-audio edge, holding it strong at fourth."},
  {"title":"Era 100 is the music pick","body":"Best-sounding compact for someone who cares most about audio, locked at second."},
  {"title":"HomePod 2nd-gen for Apple homes","body":"Tight AirPlay and HomeKit integration keep it third for the Apple crowd."},
  {"title":"Value tier stays deep","body":"Echo 4th-gen, Dot Max and Dot 5th-gen cover budget buyers without dropping smarts."},
 ],
},
{
 "commentary": "這週有個很值得聊的點：6 月 1 日 BGR 報導，Consumer Reports 現在把 Sonos Era 300 排在智慧喇叭音質評測的最頂端。我認同這個結果，Era 300 也因為這個空間音效實力穩穩待在我榜單第四。不過我的排序看的是智慧喇叭的整體任務，不只純音質，所以第一名我還是給 Amazon Echo Studio 二代。它把真正能填滿房間的 Dolby Atmos，配上最廣的智慧家庭支援、內建 Zigbee 跟 Matter Hub，再加上 Alexa 成熟的語音控制，該有的全都有。Sonos Era 100 守第二，是我最推給愛聽音樂的人的小型機。HomePod 二代排第三，適合想要 AirPlay 跟 HomeKit 緊密整合的蘋果家庭。Google 2026 Home Speaker 第五，語音助理是全場最聰明的。再往下，Amazon Echo 四代、新的 Echo Dot Max 跟長青的 Dot 五代顧好了追求性價比的人，HomePod mini 則是預算有限蘋果迷的壓軸。Sonos 贏音質、Amazon 贏整體，這個競爭態勢剛好跟我現有排序一致，所以我維持不動。",
 "highlights": [
  {"title":"Echo Studio 二代穩坐第一","body":"Dolby Atmos 音效加內建 Zigbee、Matter Hub，是最全能的智慧喇叭。"},
  {"title":"Sonos Era 300 純音質奪冠","body":"6 月 1 日 Consumer Reports 給它最高評價，空間音效實力讓它穩居第四。"},
  {"title":"Era 100 是音樂首選","body":"音質最好的小型機，推給最在意聲音的人，鎖在第二。"},
  {"title":"HomePod 二代給蘋果家庭","body":"AirPlay 跟 HomeKit 整合緊密，第三名留給蘋果用戶。"},
  {"title":"性價比陣容夠深","body":"Echo 四代、Dot Max 跟 Dot 五代顧好預算族，又不犧牲智慧功能。"},
 ],
})

# ---------------- best-mesh-wifi-systems.json ----------------
apply("best-mesh-wifi-systems.json",
[
 {"title":"The 4 Best Mesh Wi-Fi Systems of 2026","url":"https://www.rtings.com/router/reviews/best/mesh-wifi-system","source":"RTINGS"},
 {"title":"Best Wi-Fi 7 Mesh Systems: 2026's Battle-Tested Top Five","url":"https://dongknows.com/best-wi-fi-7-mesh-systems/","source":"Dong Knows Tech"},
 {"title":"Best WiFi 7 Mesh Routers 2026: Tested & Ranked","url":"https://medium.com/swlh/best-wifi-7-mesh-routers-2026-hands-on-real-world-testing-0dcd956e50c2","source":"The Startup"},
],
{
 "commentary": "In June 2026 the Wi-Fi 7 mesh field has stabilized into a clear shape, and my board reflects it. The ASUS ZenWiFi BQ16 Pro keeps the crown as the raw-performance king, with quad-band hardware and a 10G backhaul that simply outruns everything in a large multi-gig home. That said, the most useful story this week is value, and the TP-Link Deco BE63 holds my strong second precisely because reviewers keep crowning it the best Wi-Fi 7 mesh for typical 1Gbps to 2.5Gbps homes. It delivers tri-band Wi-Fi 7 across 2.4, 5 and 6GHz at a price that undercuts the premium pack, which is why it is the system I recommend to most people. The eero Pro 7 sits third and earns it as the pick for hands-off owners: testers running seven Wi-Fi 7 systems in a two-story house singled it out for the most reliable speeds, seamless roaming and zero disconnects, plus clean Matter and Thread support. TP-Link's Deco BE95 and BE85 keep the high-throughput middle locked, Netgear's Orbi 770 and 870 cover wide-coverage buyers, and the MSI RoamiI BE Pro stays the value surprise at the back. With the competition splitting cleanly into performance, value and simplicity lanes that match my existing order, I am carrying the ranking forward unchanged.",
 "highlights": [
  {"title":"ASUS BQ16 Pro stays #1","body":"Quad-band hardware and 10G backhaul keep it the raw-performance king for big multi-gig homes."},
  {"title":"TP-Link Deco BE63 is the value pick","body":"Reviewers keep crowning it the best Wi-Fi 7 mesh for typical 1 to 2.5Gbps homes, holding second."},
  {"title":"eero Pro 7 for hands-off owners","body":"Singled out for reliable speeds, seamless roaming and zero disconnects in seven-system testing."},
  {"title":"Throughput middle stays locked","body":"Deco BE95 and BE85 keep their high-speed positions for demanding setups."},
  {"title":"MSI RoamiI BE Pro is the back-row surprise","body":"Strong value scores keep it on the board against far pricier rivals."},
 ],
},
{
 "commentary": "2026 年 6 月，Wi-Fi 7 Mesh 市場已經定型成很清楚的樣子，我的榜單也照著走。ASUS ZenWiFi BQ16 Pro 守住冠軍，是純效能王，四頻硬體加 10G 回程，在大坪數多 Gigabit 的家裡就是跑得比誰都快。話說回來，這週最實用的主題是性價比，TP-Link Deco BE63 穩居第二，正是因為評測站一直把它選為一般 1Gbps 到 2.5Gbps 家庭最好的 Wi-Fi 7 Mesh。它三頻 Wi-Fi 7 涵蓋 2.4、5、6GHz，價格又比旗艦群低，所以是我推給多數人的系統。eero Pro 7 排第三也實至名歸，是最適合懶人的選擇，有測試者在兩層樓房子裡同時測七套 Wi-Fi 7，就點名它速度最穩、漫遊最順、完全不斷線，還有乾淨的 Matter 跟 Thread 支援。TP-Link Deco BE95 跟 BE85 鎖住高吞吐中段，Netgear Orbi 770 跟 870 顧到要大範圍覆蓋的人，MSI RoamiI BE Pro 則是壓軸的性價比黑馬。競爭剛好分成效能、性價比、易用三條線，跟我現有排序一致，所以名次照舊往前帶。",
 "highlights": [
  {"title":"ASUS BQ16 Pro 穩坐第一","body":"四頻硬體加 10G 回程，是大坪數多 Gigabit 家庭的純效能王。"},
  {"title":"TP-Link Deco BE63 主打性價比","body":"評測一致選為一般 1 到 2.5Gbps 家庭最佳 Wi-Fi 7 Mesh，守住第二。"},
  {"title":"eero Pro 7 適合懶人","body":"七套系統實測中被點名速度最穩、漫遊最順、零斷線。"},
  {"title":"高吞吐中段鎖死","body":"Deco BE95 跟 BE85 守住高速位置，給需求大的環境。"},
  {"title":"MSI RoamiI BE Pro 是壓軸黑馬","body":"性價比分數高，面對貴很多的對手照樣留在榜上。"},
 ],
})

# ---------------- best-e-readers.json ----------------
apply("best-e-readers.json",
[
 {"title":"Best ereaders in 2026: 9 top ebook readers tested","url":"https://www.techradar.com/best/best-ereader","source":"TechRadar"},
 {"title":"The Top 8 Best e-Readers to buy for Spring 2026","url":"https://goodereader.com/blog/electronic-readers/the-top-8-best-e-readers-to-buy-for-spring-2026","source":"Good e-Reader"},
 {"title":"Best E-Reader To Buy In 2026: Kindle Vs Kobo Vs Boox","url":"https://thetechjunction.net/best-e-reader-comparison/","source":"The Tech Junction"},
],
{
 "commentary": "As of early June 2026 the Kindle Paperwhite (2025) keeps my number one, and the latest TechRadar and Good e-Reader roundups land in the same place. It nails the blend most readers want: a crisp 7-inch display with adjustable warm light, fast page turns, a waterproof body, weeks of battery and Amazon's enormous store. For pure reading on Carta 1300, it is still the device I hand to anyone who just wants to read. The Kobo Libra Colour holds second as the best Kindle alternative and the color pick I recommend, because it adds color without giving up clarity and, crucially, supports EPUB and library lending natively where Kindle still needs conversion. Kindle's Colorsoft and the Kobo Clara Colour keep the color middle, the Boox Palma 2 stays the pocket-sized phone-shaped reader that power users love, and the Boox Page anchors the power-user end as an Android tablet in e-reader clothing. The brand split that reviewers keep drawing this season, Kindle for simplicity and store, Kobo for openness and comfort, Boox for power and customization, matches my order cleanly. No new launch this week shifts the board, so I am carrying it forward with confidence.",
 "highlights": [
  {"title":"Kindle Paperwhite (2025) stays #1","body":"Crisp warm-light 7-inch screen, waterproofing, weeks of battery and Amazon's store make it the default."},
  {"title":"Kobo Libra Colour is the color and EPUB pick","body":"Adds color without losing clarity and reads EPUB plus library books natively, holding second."},
  {"title":"Carta 1300 still rules black-and-white","body":"For pure reading the latest E Ink panel keeps Kindle and Kobo mono models unmatched."},
  {"title":"Boox Palma 2 wins on pocketability","body":"Phone-shaped Android reader power users keep reaching for, mid-board."},
  {"title":"Boox Page for power users","body":"An Android tablet in e-reader clothing anchors the customization-heavy end."},
 ],
},
{
 "commentary": "到 2026 年 6 月初，Kindle Paperwhite（2025）還是我的第一名，最新的 TechRadar 跟 Good e-Reader 評選也都站在同一邊。它把多數讀者要的東西都做到位，7 吋螢幕清晰、暖光可調、翻頁快、機身防水、電池撐好幾週，再加上 Amazon 超大書庫。純粹用 Carta 1300 看書，它還是我會直接推給只想好好讀書的人的機型。Kobo Libra Colour 守第二，是我推薦的最佳 Kindle 替代品兼彩色首選，因為它加了彩色又沒犧牲清晰度，更重要的是原生支援 EPUB 跟圖書館借閱，而 Kindle 到現在還得轉檔。Kindle Colorsoft 跟 Kobo Clara Colour 顧住彩色中段，Boox Palma 2 是進階玩家最愛的手機造型口袋機，Boox Page 則壓在進階端，根本是披著電子書外衣的 Android 平板。這季評測一直畫出的品牌分工，Kindle 簡單又有書庫、Kobo 開放又好讀、Boox 強大又能客製，剛好跟我的排序對上。這週沒有新機改變局勢，所以我很有把握地把名次往前帶。",
 "highlights": [
  {"title":"Kindle Paperwhite（2025）穩坐第一","body":"暖光 7 吋清晰螢幕、防水、電池撐好幾週加 Amazon 書庫，是預設首選。"},
  {"title":"Kobo Libra Colour 是彩色兼 EPUB 之選","body":"加彩色不犧牲清晰度，原生讀 EPUB 跟圖書館書，守住第二。"},
  {"title":"Carta 1300 黑白依舊無敵","body":"純看書，這代 E Ink 面板讓 Kindle 跟 Kobo 黑白機型沒對手。"},
  {"title":"Boox Palma 2 主打口袋好攜帶","body":"手機造型 Android 閱讀器，進階玩家愛不釋手，守在中段。"},
  {"title":"Boox Page 給進階玩家","body":"披著電子書外衣的 Android 平板，壓住高客製化那一端。"},
 ],
})

# ---------------- best-portable-projectors.json ----------------
apply("best-portable-projectors.json",
[
 {"title":"Best portable projector of 2026: Tested for streaming","url":"https://www.techradar.com/pro/best-portable-projector","source":"TechRadar"},
 {"title":"Best portable projectors of 2026, tried and tested","url":"https://www.cnn.com/cnn-underscored/reviews/best-portable-projectors","source":"CNN Underscored"},
 {"title":"The 8 Best Projectors of 2026","url":"https://www.rtings.com/projector/reviews/best/projector","source":"RTINGS"},
],
{
 "commentary": "Heading into June 2026 the XGIMI MoGo 4 Laser keeps my top spot, and the recent CNN Underscored and TechRadar testing backs the call. The latest MoGo generation finally added a real built-in battery, and the Laser version pairs that portability with the brightness and color the standard model can only hint at, so it is the travel projector I reach for first. Reviewers keep praising how the MoGo 4 line minimizes the usual portable-projector drawbacks while staying genuinely fun and simple to set up, which is exactly the bar a grab-and-go unit should clear. The LG CineBeam Q holds second as the most pocketable design with a polished smart platform, and the Hisense M2 Pro stays third as the brightness leader for anyone who occasionally fights ambient light, accepting that its bulk and shorter battery are the trade. The Nebula Mars 3 remains my endurance pick at fourth thanks to its big battery and rugged build for actual outdoor movie nights. Dangbei's Freedo, the Samsung Freestyle 2nd-gen and the rest of the Nebula stable round out a deep field that competes on size, battery and price. Nothing launched this week to upend that balance, so I am holding the order steady.",
 "highlights": [
  {"title":"XGIMI MoGo 4 Laser stays #1","body":"A real built-in battery plus laser brightness and color make it the go-to travel projector in 2026."},
  {"title":"Drawbacks minimized","body":"Reviewers praise how the MoGo 4 line stays fun and simple while cutting the usual portable compromises."},
  {"title":"LG CineBeam Q is the most pocketable","body":"Tiny design with a polished smart platform keeps it at second."},
  {"title":"Hisense M2 Pro leads on brightness","body":"Best for fighting ambient light, third, with bulk and battery as the trade-off."},
  {"title":"Nebula Mars 3 owns endurance","body":"Big battery and rugged build make it the outdoor movie-night pick at fourth."},
 ],
},
{
 "commentary": "進入 2026 年 6 月，XGIMI MoGo 4 Laser 還是我的第一名，最近 CNN Underscored 跟 TechRadar 的實測也支持這個判斷。最新一代 MoGo 終於加了真正的內建電池，而 Laser 版把這個便攜性配上標準版只能勉強做到的亮度跟色彩，所以它是我出門首選的投影機。評測一直稱讚 MoGo 4 系列把便攜投影常見的缺點壓到最低，又保持好玩、設定簡單，這正是隨手帶著走的機型該有的水準。LG CineBeam Q 守第二，是設計最迷你、智慧平台又完整的一台。Hisense M2 Pro 第三，是亮度王，適合偶爾要對抗環境光的人，代價就是體積大、電池短一點。Nebula Mars 3 守在第四，靠大電池跟堅固機身，是真的能在戶外放電影那種。Dangbei Freedo、Samsung Freestyle 二代跟其他 Nebula 系列補滿這個拼尺寸、拼電池、拼價格的深陣容。這週沒有新品打破平衡，所以我維持名次不動。",
 "highlights": [
  {"title":"XGIMI MoGo 4 Laser 穩坐第一","body":"真正的內建電池加雷射亮度跟色彩，是 2026 出門首選投影機。"},
  {"title":"缺點壓到最低","body":"評測稱讚 MoGo 4 系列好玩又好設定，同時砍掉便攜投影常見的妥協。"},
  {"title":"LG CineBeam Q 最迷你","body":"體積最小、智慧平台又完整，守住第二。"},
  {"title":"Hisense M2 Pro 亮度最強","body":"最能對抗環境光，排第三，代價是體積跟電池。"},
  {"title":"Nebula Mars 3 續航王","body":"大電池加堅固機身，是戶外放電影首選，守在第四。"},
 ],
})

# ---------------- best-4k-tvs.json ----------------
apply("best-4k-tvs.json",
[
 {"title":"'Easily one of 2026's best OLED TVs': I tested the LG C6","url":"https://www.techradar.com/televisions/lg-c6-review","source":"TechRadar"},
 {"title":"The 3 Best OLED TVs of 2026","url":"https://www.rtings.com/tv/reviews/best/by-type/oled","source":"RTINGS"},
 {"title":"Best OLED TVs in 2026 tested: top picks from LG, Samsung and more","url":"https://www.tomsguide.com/tvs/oled-tvs/best-oled-tvs","source":"Tom's Guide"},
],
{
 "commentary": "As of June 2026 I am keeping the LG C6 OLED at number one, and the recent reviews reinforce why. TechRadar called it easily one of 2026's best OLED TVs, praising punchy, natural color, superb contrast with deep blacks and refined shadow detail, all driven by the new Alpha 11 AI Gen 3 processor with 13-bit image processing and an upgraded Brightness Booster. The one honest caveat reviewers raise is value: at launch the C6 runs near three thousand dollars while last year's C5 sits at roughly half that, so the smart shopper waits for the C6 to settle. I am still ranking it on picture quality, where it sets the bar, and that is why it leads. Samsung's S95F holds second as the brightest OLED in the group and the gamer's QD-OLED, with Sony's Bravia 8 II third for its reference-grade processing and the best built-in audio up top. LG's G6 and Sony's Bravia 9 cover the premium wall-mount and mini-LED brightness lanes. Down the value end, TCL's QM8K and QM9K plus Hisense's U8N keep delivering enormous brightness per dollar, which is why they stay firmly on the board. With the 2026 OLED class now fully reviewed and the order matching the verdicts, I am carrying it forward unchanged.",
 "highlights": [
  {"title":"LG C6 OLED stays #1","body":"Alpha 11 AI Gen 3 with 13-bit processing delivers punchy color, deep blacks and refined shadows, the picture-quality bar of 2026."},
  {"title":"The honest caveat is price","body":"At launch the C6 runs near $3,000 versus roughly half for last year's C5, so patient buyers wait for it to settle."},
  {"title":"Samsung S95F is the gamer's QD-OLED","body":"Brightest OLED in the group keeps it locked at second."},
  {"title":"Sony Bravia 8 II for processing and sound","body":"Reference-grade upscaling and the best built-in audio up top hold it at third."},
  {"title":"TCL and Hisense own value","body":"QM8K, QM9K and U8N keep delivering huge brightness per dollar to anchor the list."},
 ],
},
{
 "commentary": "到 2026 年 6 月，我還是把 LG C6 OLED 放在第一，最近的評測也讓我更確定。TechRadar 直接說它輕鬆躋身 2026 最佳 OLED 之列，誇它色彩鮮明自然、對比極好、黑得夠深、暗部細節細膩，全靠新的 Alpha 11 AI Gen 3 處理器，搭配 13-bit 影像處理跟升級的亮度增強。評測唯一誠實點出的缺點是價格，剛上市的 C6 要將近台幣九萬，而去年的 C5 大概只要一半，所以聰明的買家會等 C6 價格落下來。但我是看畫質排名，這方面它就是標竿，所以它領先。Samsung S95F 守第二，是全場最亮的 OLED，也是電競玩家的 QD-OLED 之選。Sony Bravia 8 II 第三，靠的是參考級影像處理跟頂規內建音效。LG G6 跟 Sony Bravia 9 顧住高階壁掛跟 mini-LED 亮度路線。價格端，TCL QM8K、QM9K 加 Hisense U8N 每塊錢買到的亮度依舊驚人，所以穩穩留在榜上。2026 這批 OLED 現在都評測完了，排序也跟結論一致，所以我名次照舊往前帶。",
 "highlights": [
  {"title":"LG C6 OLED 穩坐第一","body":"Alpha 11 AI Gen 3 加 13-bit 處理，色彩鮮明、黑得夠深、暗部細膩，是 2026 畫質標竿。"},
  {"title":"誠實的缺點是價格","body":"剛上市的 C6 要近台幣九萬，去年 C5 約一半，耐心的買家會等它降價。"},
  {"title":"Samsung S95F 是電競 QD-OLED","body":"全場最亮的 OLED，鎖在第二。"},
  {"title":"Sony Bravia 8 II 主打處理與音效","body":"參考級升頻加頂規內建音效，守住第三。"},
  {"title":"TCL 跟 Hisense 主打性價比","body":"QM8K、QM9K 跟 U8N 每塊錢買到的亮度驚人，穩住榜位。"},
 ],
})

print("ALL DONE")
