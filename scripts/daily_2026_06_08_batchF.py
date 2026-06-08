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

# ---------------- best-security-cameras ----------------
do("best-security-cameras.json",
   [
     {"title": "Best home security camera 2026 reviews", "url": "https://www.techradar.com/best/best-home-security-camera", "source": "TechRadar"},
     {"title": "The Best Home Security Cameras of 2026", "url": "https://www.cnet.com/home/security/best-home-security-camera/", "source": "CNET"},
   ],
   {
     "commentary": "The Reolink Argus 4 Pro stays at number one because it solves the two things that actually annoy people about security cameras: it runs on battery with solar so there is no wiring, and it stores locally so there is no mandatory subscription bleeding you monthly. Add genuinely sharp 4K with a wide 180-degree view and color night vision that works, and it is the camera I recommend to almost everyone. You own your footage and you pay once. The Arlo Pro 5S holds second as the polished ecosystem pick, the app and smart detection are the best in the business, but the best features sit behind a subscription, which is exactly why it is second and not first. The Eufy SoloCam S340 stays third as the other strong no-subscription option with dual cameras and solar. The Google Nest Cam holds fourth for households already inside Google's ecosystem. Nothing this week reordered the field. The read: best overall and no-subscription is Reolink, best app and detection is Arlo, and the subscription question should decide your purchase more than the spec sheet.",
     "highlights": [
       {"title": "Reolink Argus 4 Pro skips the subscription", "body": "Battery-plus-solar means no wiring, local storage means no monthly fee, and you get sharp 4K with a 180-degree view and working color night vision. You own your footage and pay once, holding it at number one."},
       {"title": "Arlo Pro 5S has the best app and detection", "body": "The smart detection and app polish are the best in the business, but the top features sit behind a subscription. That ongoing cost is exactly why it lands second rather than first."},
       {"title": "Eufy SoloCam S340 is the other no-fee pick", "body": "Dual cameras and solar charging with local storage make it a strong subscription-free alternative. For buyers who want flexibility without monthly bills, it holds a firm third."},
       {"title": "Let the subscription decide", "body": "Camera hardware is mostly excellent now; the real long-term cost is the cloud fee. Decide whether you will pay monthly for cloud smarts or want to own footage locally, then pick accordingly."},
     ],
   },
   {
     "commentary": "Reolink Argus 4 Pro 我還是放第一，因為它解決了安全攝影機真正惹人厭的兩件事：它用電池加太陽能所以不用牽線，本地儲存所以不用每個月被強制訂閱放血。再加上真的銳利的 4K、180 度廣角跟有用的彩色夜視，它是我幾乎會推薦給所有人的攝影機。畫面是你的，一次付清。Arlo Pro 5S 守第二，是精緻生態選擇，App 跟智慧偵測是業界最好的，但最好的功能在訂閱後面，這正是它第二而非第一的原因。Eufy SoloCam S340 守第三，是另一個強力免訂閱選擇，雙鏡頭加太陽能。Google Nest Cam 守第四，給已經在 Google 生態裡的家庭。這週沒事件重排。判斷：整體兼免訂閱選 Reolink、App 跟偵測選 Arlo，訂閱問題該比規格表更能決定你的購買。",
     "highlights": [
       {"title": "Reolink Argus 4 Pro 跳過訂閱", "body": "電池加太陽能不用牽線、本地儲存不用月費，還有銳利 4K、180 度視角跟有用的彩色夜視。畫面是你的、一次付清，守住第一。"},
       {"title": "Arlo Pro 5S 有最好的 App 跟偵測", "body": "智慧偵測跟 App 精緻是業界最好的，但頂級功能在訂閱後面。這份持續成本正是它落第二而非第一的原因。"},
       {"title": "Eufy SoloCam S340 是另一個免費選擇", "body": "雙鏡頭加太陽能充電配本地儲存，是強力的免訂閱替代。想要彈性又不想月費的買家，它穩在第三。"},
       {"title": "讓訂閱來決定", "body": "現在攝影機硬體大多優秀，真正的長期成本是雲端月費。決定你要不要每月付雲端智慧、還是想本地擁有畫面，再照這個選。"},
     ],
   })

# ---------------- best-video-doorbells ----------------
do("best-video-doorbells.json",
   [
     {"title": "Best video doorbell 2026 reviews", "url": "https://www.techradar.com/best/best-video-doorbell", "source": "TechRadar"},
     {"title": "The Best Video Doorbells of 2026", "url": "https://www.cnet.com/home/security/best-video-doorbell/", "source": "CNET"},
   ],
   {
     "commentary": "The Eufy E340 stays at number one because it gives you everything the subscription brands charge monthly for, and asks nothing in return. Dual cameras mean you see faces and packages on the ground at once, the local storage is free forever, and the image quality holds up day and night. For the broadest set of buyers tired of doorbell subscriptions, this is the clear pick and the value is not close. The Aqara G410 holds second as the best choice for the smart-home crowd, deep Matter and HomeKit support plus local storage make it the doorbell that actually plays nice with the rest of your gear. The Google Nest Doorbell wired 2nd gen stays third on its excellent on-device AI for households inside Google, though the best features lean on a subscription. The Aqara G400 holds fourth as another strong local-storage option. Nothing this week reordered the field. The read: best value and no-fee is the Eufy, best for smart-home integration is the Aqara, best Google-ecosystem pick is the Nest. The dual-camera, local-storage formula won.",
     "highlights": [
       {"title": "Eufy E340 charges no monthly fee", "body": "Dual cameras show faces and ground-level packages at once, local storage is free forever, and image quality holds day and night. For buyers tired of doorbell subscriptions, the value is not close at number one."},
       {"title": "Aqara G410 is the smart-home pick", "body": "Deep Matter and HomeKit support plus local storage make it the doorbell that plays nice with the rest of your gear. For integration-focused buyers it is the clear second."},
       {"title": "Nest Doorbell wins inside Google", "body": "Its excellent on-device AI makes it the natural choice for Google households, though the best features lean on a subscription. That ecosystem fit holds it a firm third."},
       {"title": "Dual camera plus local storage won", "body": "Seeing packages on the ground and storing clips without a fee is now the formula to beat. Prioritize a second camera and free local storage over brand name, and the shortlist narrows fast."},
     ],
   },
   {
     "commentary": "Eufy E340 我還是放第一，因為它把訂閱品牌每月收費的東西全給你，又什麼都不跟你要。雙鏡頭代表你同時看到臉跟放在地上的包裹，本地儲存永遠免費，畫質日夜都撐得住。對最廣、受夠門鈴訂閱的買家，這是明確選擇，性價比差距不小。Aqara G410 守第二，是智慧家庭派的最佳選擇，深度 Matter 跟 HomeKit 支援加本地儲存，讓它是真的跟你其他裝置合得來的門鈴。Google Nest Doorbell 有線二代守第三，靠優秀的裝置端 AI，給 Google 生態家庭，雖然最好的功能偏向訂閱。Aqara G400 守第四，是另一個強力本地儲存選擇。這週沒事件重排。判斷：性價比兼免費選 Eufy、智慧家庭整合選 Aqara、Google 生態選 Nest。雙鏡頭加本地儲存的公式贏了。",
     "highlights": [
       {"title": "Eufy E340 不收月費", "body": "雙鏡頭同時看到臉跟地上包裹、本地儲存永遠免費、畫質日夜都撐。對受夠門鈴訂閱的買家，第一名的性價比差距不小。"},
       {"title": "Aqara G410 是智慧家庭選擇", "body": "深度 Matter 跟 HomeKit 支援加本地儲存，讓它是真的跟其他裝置合得來的門鈴。對重視整合的買家它是明確第二。"},
       {"title": "Nest Doorbell 在 Google 裡贏", "body": "優秀的裝置端 AI 讓它是 Google 家庭的自然選擇，雖然最好的功能偏向訂閱。這份生態貼合讓它穩在第三。"},
       {"title": "雙鏡頭加本地儲存贏了", "body": "看到地上包裹又免費存片現在是要打敗的公式。把第二顆鏡頭跟免費本地儲存擺在品牌名之前，候選清單很快就縮短。"},
     ],
   })

# ---------------- best-mesh-wifi-systems ----------------
do("best-mesh-wifi-systems.json",
   [
     {"title": "Best mesh Wi-Fi 2026 reviews", "url": "https://www.techradar.com/best/best-mesh-wifi", "source": "TechRadar"},
     {"title": "The Best Wi-Fi 7 Mesh Systems of 2026", "url": "https://www.pcmag.com/picks/the-best-wi-fi-mesh-network-systems", "source": "PCMag"},
   ],
   {
     "commentary": "The Asus ZenWiFi BQ16 Pro stays at number one because it is the mesh that finally makes Wi-Fi 7 worth the upgrade for a real house. The tri-band design with a fast dedicated backhaul means the speed actually reaches the far bedroom instead of collapsing two rooms away, and Asus gives you genuinely deep controls plus lifetime free security. For a large home that demands real throughput, this is the system I trust. The TP-Link Deco BE63 holds second as the value Wi-Fi 7 pick, it covers most homes beautifully for noticeably less, and for the majority of buyers it is honestly all the mesh they need. The Eero Pro 7 stays third as the set-and-forget choice, the simplest setup in the category and the pick for people who never want to open a settings menu, though some advanced features sit behind a subscription. The TP-Link Deco BE95 holds fourth as the maximum-coverage flagship. Nothing this week reordered the field. The read: best performance is Asus, best value is the Deco BE63, simplest is Eero. Buy coverage for your actual square footage, not the biggest number.",
     "highlights": [
       {"title": "Asus ZenWiFi BQ16 Pro makes Wi-Fi 7 worth it", "body": "A tri-band design with fast dedicated backhaul carries real speed to the far bedroom, plus deep controls and lifetime free security. For a large home that needs real throughput, it holds number one."},
       {"title": "TP-Link Deco BE63 is the value pick", "body": "It covers most homes beautifully for noticeably less, and for the majority of buyers it is honestly all the mesh they need. That value-to-coverage balance keeps it a firm second."},
       {"title": "Eero Pro 7 is the set-and-forget choice", "body": "The simplest setup in the category makes it the pick for people who never want to open a settings menu, though some features need a subscription. That ease holds it a solid third."},
       {"title": "Buy for your real square footage", "body": "The biggest tri-band flagship is wasted on an apartment, and a budget two-pack will not cover a large house. Measure your space and dead zones first, then size the mesh to match."},
     ],
   },
   {
     "commentary": "Asus ZenWiFi BQ16 Pro 我還是放第一，因為它終於讓 Wi-Fi 7 對一間真正的房子值得升級。三頻設計加快速專用回程，代表速度真的到得了最遠的臥室，而非兩個房間外就崩掉，Asus 又給你真的很深的控制加終身免費防護。對需要真實吞吐的大房子，這是我信的系統。TP-Link Deco BE63 守第二，是性價比 Wi-Fi 7 選擇，它用明顯更低的價格漂亮覆蓋多數家庭，對大多數買家老實說這就是他們需要的全部 mesh。Eero Pro 7 守第三，是裝好就忘的選擇，這類別設定最簡單，給從不想打開設定選單的人，雖然部分進階功能在訂閱後面。TP-Link Deco BE95 守第四，是最大覆蓋旗艦。這週沒事件重排。判斷：效能選 Asus、性價比選 Deco BE63、最簡單選 Eero。照你真實坪數買覆蓋，別追最大的數字。",
     "highlights": [
       {"title": "Asus ZenWiFi BQ16 Pro 讓 Wi-Fi 7 值得", "body": "三頻加快速專用回程把真實速度帶到最遠臥室，加上深度控制跟終身免費防護。對需要真實吞吐的大房子，守住第一。"},
       {"title": "TP-Link Deco BE63 是性價比選擇", "body": "它用明顯更低價漂亮覆蓋多數家庭，對大多數買家老實說這就是他們需要的全部。這份性價比與覆蓋的平衡讓它穩在第二。"},
       {"title": "Eero Pro 7 是裝好就忘的選擇", "body": "這類別設定最簡單，給從不想打開設定選單的人，雖然部分功能要訂閱。這份簡便讓它穩坐第三。"},
       {"title": "照你真實坪數買", "body": "最大的三頻旗艦在公寓是浪費，平價兩件組蓋不滿大房子。先量你的空間跟死角，再把 mesh 規模配上去。"},
     ],
   })

# ---------------- best-smart-thermostats ----------------
do("best-smart-thermostats.json",
   [
     {"title": "Best smart thermostat 2026 reviews", "url": "https://www.cnet.com/home/energy-and-utilities/best-smart-thermostat/", "source": "CNET"},
     {"title": "The Best Smart Thermostats of 2026", "url": "https://www.nytimes.com/wirecutter/reviews/best-thermostat/", "source": "Wirecutter"},
   ],
   {
     "commentary": "The Ecobee Smart Thermostat Premium stays at number one because it does more out of the box than anything else and asks nothing extra of you. The included room sensor solves the single biggest thermostat problem, the temperature where you actually sit rather than where the box is mounted, and the built-in air quality monitor and smart-home support round out a genuinely complete package. For most homes that want real comfort and savings, this is the one I recommend without hesitation. The Google Nest Learning Thermostat 4th gen holds a very close second on its auto-scheduling, it still learns your patterns better than anyone and the redesigned hardware looks superb, the pick for people who want it to just figure them out. The Honeywell Home T9 stays third as the value choice with multi-room sensor support. The Eve Thermostat holds fourth for the HomeKit-only crowd. Nothing this week reordered the field. The read: best all-round is the Ecobee, best learning is the Nest, and both will pay for themselves in energy savings within a couple of seasons.",
     "highlights": [
       {"title": "Ecobee Premium is the most complete package", "body": "An included room sensor fixes the biggest thermostat problem, plus a built-in air quality monitor and broad smart-home support. For most homes wanting comfort and savings, it is the no-hesitation pick at number one."},
       {"title": "Nest 4th gen learns you best", "body": "Its auto-scheduling still reads your patterns better than anyone, and the redesigned hardware looks superb. For people who want the thermostat to just figure them out, it is a very close second."},
       {"title": "Honeywell T9 is the value pick", "body": "It brings multi-room sensor support at a lower price than the premium duo. For budget-conscious buyers who still want room-by-room comfort, it holds a firm third."},
       {"title": "Both leaders pay for themselves", "body": "The Ecobee and Nest each recoup their cost in energy savings within a couple of seasons. The smart-thermostat question is no longer whether it is worth it, but which interface you prefer living with."},
     ],
   },
   {
     "commentary": "Ecobee Smart Thermostat Premium 我還是放第一，因為它開箱即用就比任何東西做得多，又不額外要求你什麼。附的房間感測器解決了恆溫器最大的單一問題，你真正坐的地方的溫度、而非盒子裝在哪，內建空氣品質監測加智慧家庭支援湊成一個真正完整的組合。對多數想要真舒適跟省電的家庭，這是我毫不猶豫推薦的。Google Nest Learning Thermostat 4th gen 緊咬第二，靠它的自動排程，它學你的習慣還是比誰都好，重新設計的硬體又超好看，給想要它自己搞懂你的人。Honeywell Home T9 守第三，是性價比選擇，有多房感測器支援。Eve Thermostat 守第四，給只用 HomeKit 的人。這週沒事件重排。判斷：全能選 Ecobee、學習選 Nest，兩者都會在幾季內靠省電回本。",
     "highlights": [
       {"title": "Ecobee Premium 是最完整的組合", "body": "附的房間感測器解決恆溫器最大問題，加上內建空氣品質監測跟廣泛智慧家庭支援。對多數要舒適跟省電的家庭，它是第一名的毫不猶豫選擇。"},
       {"title": "Nest 四代最會學你", "body": "自動排程讀你的習慣還是比誰都好，重新設計的硬體超好看。想要恆溫器自己搞懂你的人，它緊咬第二。"},
       {"title": "Honeywell T9 是性價比選擇", "body": "它用比高階雙雄更低的價格帶來多房感測器支援。預算有限又想要逐房舒適的買家，它穩在第三。"},
       {"title": "兩個領袖都會回本", "body": "Ecobee 跟 Nest 都會在幾季內靠省電回本。智慧恆溫器的問題不再是值不值得，而是你偏好跟哪個介面一起生活。"},
     ],
   })

# ---------------- best-smart-pet-feeders ----------------
do("best-smart-pet-feeders.json",
   [
     {"title": "Best automatic pet feeder 2026 reviews", "url": "https://www.nytimes.com/wirecutter/reviews/best-automatic-pet-feeders/", "source": "Wirecutter"},
     {"title": "The Best Smart Pet Feeders of 2026", "url": "https://www.cnet.com/home/smart-home/best-pet-feeder/", "source": "CNET"},
   ],
   {
     "commentary": "The Petlibro Granary Camera stays at number one because a pet feeder's one job is to never fail, and this is the one I trust to feed reliably and let me check in when I am away. The camera and two-way audio mean you actually see your pet eat, the portion control is precise, and the app does not flake out at dinner time. For most pet owners who want peace of mind on a normal budget, this is the default. The Petkit Yumshare Dual-Hopper 2 holds second and is the smarter buy for multi-food households, two hoppers let you mix or schedule different foods, and the build quality is a notch up. The Petlibro Polar Wet Food stays third as the only pick worth trusting for wet food, the cooling keeps it fresh for hours, which nothing else in the category does well. The Wopet Heritage View holds fourth as a strong dual-bowl alternative. Nothing this week reordered the field. The read: best all-round is the Granary Camera, best for multiple foods is the Petkit, best for wet food is the Polar. Buy for what your pet actually eats.",
     "highlights": [
       {"title": "Petlibro Granary Camera is the reliable default", "body": "A feeder's one job is to never fail, and this feeds reliably with camera and two-way audio so you see your pet eat. Precise portions and a stable app hold it at number one for most owners."},
       {"title": "Petkit Yumshare Dual-Hopper 2 wins for mixed diets", "body": "Two hoppers let you mix or schedule different foods, with a build quality a notch above the rest. For multi-food households it is the smarter buy and a firm second."},
       {"title": "Petlibro Polar is the wet-food specialist", "body": "Its cooling keeps wet food fresh for hours, something nothing else in the category does well. For owners who feed wet food on a schedule, it is the only pick worth trusting, holding third."},
       {"title": "Buy for what your pet eats", "body": "Dry-food households want the Granary, multiple foods want the dual-hopper, wet food demands cooling. The feeder that fits your pet's actual diet matters far more than the longest feature list."},
     ],
   },
   {
     "commentary": "Petlibro Granary Camera 我還是放第一，因為餵食器的唯一工作就是永不失手，而這台是我信得過會可靠餵食、又能在我出門時查看的那台。相機加雙向語音代表你真的看得到寵物吃飯，份量控制精準，App 又不會在晚餐時間出包。對多數想要在正常預算下安心的飼主，這是預設。Petkit Yumshare Dual-Hopper 2 守第二，對多種食物的家庭是更聰明的買法，兩個料倉讓你混搭或排程不同食物，做工也高一截。Petlibro Polar Wet Food 守第三，是唯一值得信賴餵濕食的選擇，保冷能讓它新鮮好幾個小時，這是這類別其他東西做不好的。Wopet Heritage View 守第四，是強力雙碗替代。這週沒事件重排。判斷：全能選 Granary Camera、多食物選 Petkit、濕食選 Polar。照你寵物真的吃什麼買。",
     "highlights": [
       {"title": "Petlibro Granary Camera 是可靠預設", "body": "餵食器唯一工作就是永不失手，這台可靠餵食加相機跟雙向語音讓你看到寵物吃飯。精準份量加穩定 App，對多數飼主守住第一。"},
       {"title": "Petkit Yumshare 雙料倉贏在混合飲食", "body": "兩個料倉讓你混搭或排程不同食物，做工也高一截。對多種食物的家庭它是更聰明的買法，穩在第二。"},
       {"title": "Petlibro Polar 是濕食專家", "body": "保冷能讓濕食新鮮好幾小時，這是這類別其他東西做不好的。照表餵濕食的飼主，它是唯一值得信賴的選擇，守第三。"},
       {"title": "照你寵物吃什麼買", "body": "乾食家庭要 Granary、多種食物要雙料倉、濕食需要保冷。合你寵物實際飲食的餵食器，比最長的功能清單重要太多。"},
     ],
   })

# ---------------- best-vpn-services ----------------
do("best-vpn-services.json",
   [
     {"title": "The best VPN service 2026", "url": "https://www.techradar.com/vpn/best-vpn", "source": "TechRadar"},
     {"title": "NordVPN vs Proton VPN 2026: Comparing Two Popular VPNs", "url": "https://cybernews.com/best-vpn/nordvpn-vs-protonvpn/", "source": "Cybernews"},
   ],
   {
     "commentary": "Mullvad stays at number one for me, and the reason is the one that matters most in a VPN: it is the most serious privacy product in the category. No account, no email, a flat price, and a no-logs posture that has been proven in the real world rather than just claimed in marketing. If the entire point of a VPN is that nobody can tie your traffic to you, Mullvad is the honest answer and nothing else comes close on principle. ProtonVPN holds a very close second and is the better all-rounder for most people, the Swiss jurisdiction and audited no-logs policy back real privacy, it has grown past 20,000 servers in 145 countries, and the unlimited free tier lets you try before you pay. NordVPN stays third and it is the mainstream winner in most reviews this month for a reason, it nails the sweet spot of features, speed and streaming unblocking, the pick if you want one app that does everything well. IVPN and ExpressVPN round out the visible top. Nothing this week reordered my field. The read: maximum privacy is Mullvad, best all-round privacy is Proton, best mainstream experience is Nord.",
     "highlights": [
       {"title": "Mullvad is the most serious privacy product", "body": "No account, no email, a flat price and a no-logs posture proven in the real world. If the whole point is that nobody can tie traffic to you, it is the honest answer and holds number one on principle."},
       {"title": "ProtonVPN is the best all-round privacy pick", "body": "Swiss jurisdiction, an audited no-logs policy, over 20,000 servers in 145 countries and an unlimited free tier to try first. For most privacy-minded users it is the complete package and a very close second."},
       {"title": "NordVPN wins the mainstream experience", "body": "It nails the sweet spot of features, speed and streaming unblocking, which is why it tops most general reviews this month. For one app that does everything well, it holds a firm third."},
       {"title": "Decide privacy versus convenience first", "body": "Mullvad and Proton lead on principled privacy; Nord leads on polish and streaming. Choose whether anonymity or all-round convenience is your priority, and the right VPN follows from that."},
     ],
   },
   {
     "commentary": "Mullvad 我還是放第一，理由是 VPN 裡最重要的那個：它是這類別最認真的隱私產品。不用帳號、不用 email、單一價格，無紀錄的立場是在現實裡被驗證過、而非只是行銷宣稱。如果 VPN 的整個重點是沒人能把你的流量連到你身上，Mullvad 就是誠實的答案，原則上沒人能比。ProtonVPN 緊咬第二，對多數人是更好的全能選擇，瑞士司法管轄加經稽核的無紀錄政策撐起真隱私，伺服器已成長超過 145 國 20,000 台，無限免費方案讓你先試再付。NordVPN 守第三，這個月在多數評測是主流贏家是有道理的，它命中功能、速度跟串流解鎖的甜蜜點，想要一個 App 什麼都做得好就選它。IVPN 跟 ExpressVPN 收尾可見前段。這週沒事件重排我的榜。判斷：最大隱私選 Mullvad、最佳全能隱私選 Proton、最佳主流體驗選 Nord。",
     "highlights": [
       {"title": "Mullvad 是最認真的隱私產品", "body": "不用帳號、不用 email、單一價格，無紀錄立場在現實被驗證過。如果整個重點是沒人能把流量連到你，它是誠實答案，原則上守住第一。"},
       {"title": "ProtonVPN 是最佳全能隱私選擇", "body": "瑞士管轄、經稽核無紀錄政策、145 國超過 20,000 台伺服器、無限免費方案先試。對多數重視隱私的人它是完整組合，緊咬第二。"},
       {"title": "NordVPN 贏主流體驗", "body": "它命中功能、速度跟串流解鎖的甜蜜點，這正是它這個月在多數一般評測奪冠的原因。想要一個 App 什麼都做得好，它穩在第三。"},
       {"title": "先決定隱私還是便利", "body": "Mullvad 跟 Proton 領先原則性隱私；Nord 領先精緻跟串流。決定匿名還是全能便利是你的優先，對的 VPN 就跟著出來。"},
     ],
   })

print("batchF done")
