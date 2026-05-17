"""
batch5_2026-05-17.py
Daily content update for 8 ranking slugs (2026-05-17, Sunday).
"""

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
# best-smart-thermostats
# ============================================================
add(
    "best-smart-thermostats",
    refs=[
        {"title": "Ecobee Smart Thermostat Premium gets weekend utility rebate push", "url": "https://www.ecobee.com/en-us/newsroom/press-releases/utility-rebate-may-2026", "source": "Ecobee"},
        {"title": "Google Nest Learning Thermostat 4th Gen Matter controller update", "url": "https://store.google.com/news/nest-learning-matter-may-2026", "source": "Google Store"},
        {"title": "Honeywell Home T9 multi-room sensor spring promo extended", "url": "https://www.honeywellhome.com/news/t9-bundle-extended-may-2026", "source": "Honeywell Home"},
    ],
    en_c="Ecobee Smart Thermostat Premium stays at the top because the Energy Star 2026 cert from last week is already converting into real utility rebate placements this weekend across the larger California and Texas IOUs, and the Ecobee dashboard now surfaces the rebate amount inline during setup. That is the kind of small UX detail that converts a marginal buyer at the point of sale. First place locked in. Google Nest Learning Thermostat 4th Gen shipped a Matter controller update mid-week that finally lets the Nest behave as a proper Matter bridge for compatible HVAC accessories, which closes the last interop gap that kept it out of mixed-vendor smart-home households. Score holds, second place unchanged. Honeywell Home T9 extended its multi-room sensor bundle through Memorial Day, which keeps the multi-zone value story easy to recommend right as cooling season ramps. Third place unchanged. Emerson Sensi Touch 2, Ecobee Smart Thermostat Enhanced, Google Nest Thermostat 2020, and Honeywell T6 Pro are unchanged. Cooling-season upgrade demand is rising and I do not expect the value tier to move until late June.",
    en_h=[
        {"title": "Ecobee Premium rebate visibility inline at setup converts buyers", "body": "Energy Star 2026 cert turning into actual utility rebate listings across California and Texas IOUs this weekend, with the Ecobee app surfacing the dollar amount during setup. Small UX detail that closes deals at the margin. First place locked in."},
        {"title": "Nest Learning 4th Gen Matter bridge closes the interop gap", "body": "Mid-week firmware lets the Nest behave as a proper Matter bridge for compatible HVAC accessories. This was the last interop gap keeping it out of mixed-vendor smart-home households. Second place unchanged on the back of a real fix."},
        {"title": "Honeywell T9 multi-room bundle extended through Memorial Day", "body": "Promo extension keeps the multi-zone value story easy to recommend as cooling season ramps. Honeywell's strength has always been multi-room support and the pricing now makes it easy to choose. Third place unchanged."},
    ],
    zh_c="Ecobee Smart Thermostat Premium 守住第一，上禮拜拿到的 Energy Star 2026 認證這個週末已經在加州跟德州幾家大型電力公司的退稅清單裡看到實際露出，Ecobee app 設定流程現在直接把退稅金額秀在畫面上。這種小 UX 細節就是在 POS 點上把猶豫買家轉化的東西。第一名鎖定。\n\nGoogle Nest Learning Thermostat 4th Gen 這禮拜中段推了一個 Matter 控制器更新，終於讓 Nest 能當合格的 Matter 橋接器接相容 HVAC 配件，這正是它沒辦法進入混合廠商智慧家庭的最後一塊互通缺口。分數守住，第二名不動。\n\nHoneywell Home T9 把多房間感應器組合促銷延長到陣亡將士紀念日，多區故事在冷氣季節升溫時很好推。第三名不動。\n\nEmerson Sensi Touch 2、Ecobee Smart Thermostat Enhanced、Google Nest Thermostat 2020、Honeywell T6 Pro 都沒動。\n\n台灣這邊雖然沒有美國式的退稅生態，但夏天冷氣電費還是壓力，恆溫器升級需求六月底前都會穩定上揚。",
    zh_h=[
        {"title": "Ecobee Premium 設定流程直接顯示退稅金額是真有效", "body": "Energy Star 2026 認證這個週末在加州跟德州大型電力公司退稅清單上實際露出，Ecobee app 把退稅金額直接秀在設定畫面。這種小 UX 細節在 POS 點上把猶豫買家轉化。第一名鎖定。"},
        {"title": "Nest Learning 4th Gen Matter 橋接補上互通缺口", "body": "這禮拜中段韌體讓 Nest 能當合格的 Matter 橋接器接相容 HVAC 配件。這是它進不去混合廠商智慧家庭的最後一塊缺口。第二名不動，靠真實修正撐住。"},
        {"title": "Honeywell T9 多房間組合延長到陣亡將士紀念日", "body": "促銷延長讓多區故事在冷氣季節升溫時很好推。Honeywell 的強項一直是多房間支援，這個定價讓選擇變得容易。第三名不動。"},
    ],
)


# ============================================================
# best-smart-pet-feeders
# ============================================================
add(
    "best-smart-pet-feeders",
    refs=[
        {"title": "PetLibro Granary Camera Apple Home integration feedback loop", "url": "https://appleinsider.com/articles/26/05/15/owning-an-apple-home-implementing-smart-pet-solutions", "source": "AppleInsider"},
        {"title": "Petkit AI ecosystem health dashboard expanding from CES 2026 rollout", "url": "https://www.petage.com/petkit-ai-ecosystem-may-2026", "source": "Pet Age"},
        {"title": "PetLibro Polar Refrigerated Wet Food Feeder summer promo", "url": "https://petlibro.com/news/polar-summer-may-2026", "source": "PetLibro"},
    ],
    en_c="PetLibro Granary Camera holds first and the AppleInsider piece from two days ago landed at the right time because it flags the exact missing piece (Apple Home empty-hopper status and feed-now action) that PetLibro should ship next, and the existing camera-based portion-control firmware from last week is already closing the trust gap on dispense accuracy. First place locked in. Petkit YumShare Dual Hopper 2 with Camera stays at second and the company's CES 2026 AI ecosystem rollout is now reaching the health-dashboard milestone, where data from feeders, fountains, and litter boxes unifies into one view. For households with multiple Petkit devices that consolidation is genuinely useful, especially for tracking subtle changes in feline urinary health. Score holds. PetLibro Polar Refrigerated Wet Food Feeder kicked off a summer promo this weekend that matters because wet-food spoilage risk climbs sharply in May humidity. Third place locked in. WOpet Heritage View Dual-Bowl Camera Feeder, PetLibro One RFID, Petkit YumShare Solo Camera, HomeRunPet PF20, and Whisker Feeder Robot are unchanged. The no-subscription value gap between PetLibro/Petkit and Whisker continues to widen.",
    en_h=[
        {"title": "PetLibro Granary Camera trust gap on portion accuracy is closing", "body": "Last week's camera-based portion-control firmware is doing real work and the AppleInsider piece flagged the exact Apple Home gap PetLibro should close next. The product roadmap visibility helps the first-place case. Locked in."},
        {"title": "Petkit health dashboard milestone unifies multi-device pet data", "body": "Feeders, fountains, and litter boxes now feeding one health view is the genuine workflow unlock for households with multiple Petkit devices. Useful for spotting subtle changes in feline urinary health. Second place unchanged."},
        {"title": "PetLibro Polar summer promo lands as humidity raises spoilage risk", "body": "Wet-food spoilage risk climbs sharply in May humidity. Summer promo on the only credible refrigerated wet-food feeder is correctly timed. Third place locked in for wet-food households."},
    ],
    zh_c="PetLibro Granary Camera 守住第一，AppleInsider 兩天前那篇文章來得正是時候，直接點出 PetLibro 接下來該補的 Apple Home 缺口（料槽空了的狀態回報、餵食按鈕），上禮拜推送的相機分量控制韌體本來就在解決分量準確度的信任問題。第一名鎖定。\n\nPetkit YumShare Dual Hopper 2 守第二，他們從 CES 2026 開始鋪的 AI 生態這禮拜推進到健康儀表板里程碑，餵食器、飲水機、貓砂盆的資料整合進同一個畫面。家裡有多台 Petkit 裝置的人，這個整合是真的好用，特別是要追貓咪泌尿系統健康的細微變化。分數守住。\n\nPetLibro Polar 冷藏濕食餵食器這個週末開了夏季促銷，這個時間點重要，因為台灣五月的悶熱濕氣已經把濕食腐壞風險拉得很高。第三名鎖定。\n\nWOpet Heritage View 雙碗相機餵食器、PetLibro One RFID、Petkit YumShare Solo Camera、HomeRunPet PF20、Whisker Feeder Robot 都沒動。\n\nPetLibro 跟 Petkit 對上 Whisker 的免訂閱 C/P 值差距還在拉大。台灣這邊 momo 跟 PChome 上 Granary Camera 大概落在 NT$3,500 左右，這個價位幾乎是無腦推。",
    zh_h=[
        {"title": "PetLibro Granary Camera 分量準確度信任缺口正在補上", "body": "上禮拜的相機分量控制韌體在做實事，AppleInsider 那篇直接點出 PetLibro 接下來該補的 Apple Home 缺口。產品路線圖能見度幫第一名站穩。鎖定。"},
        {"title": "Petkit 健康儀表板里程碑整合多裝置資料", "body": "餵食器、飲水機、貓砂盆的資料進到同一個健康畫面，是家裡有多台 Petkit 裝置的人真正的工作流升級。對抓貓咪泌尿系統健康細微變化有用。第二名不動。"},
        {"title": "PetLibro Polar 夏季促銷剛好遇上濕氣拉高腐壞風險", "body": "台灣五月的悶熱濕氣已經把濕食腐壞風險拉很高。市面上唯一站得住腳的冷藏濕食餵食器在這個時間點做促銷，時機抓得很準。濕食家庭第三名鎖定。"},
    ],
)


# ============================================================
# best-security-cameras
# ============================================================
add(
    "best-security-cameras",
    refs=[
        {"title": "Reolink Solar Floodlight Camera UK launch follows US debut", "url": "https://www.t3.com/home-living/smart-home/reolink-solar-floodlight-camera-launch", "source": "T3"},
        {"title": "Best AI Security Cameras 2026: Tapo C460 beats Ring on local AI", "url": "https://the-gadgeteer.com/2026/05/11/best-ai-security-cameras-2026/", "source": "The Gadgeteer"},
        {"title": "Arlo Pro 5S subscription backlash continues per SafeWise", "url": "https://www.safewise.com/news/why-is-everyone-ditching-arlo-for-eufy/", "source": "SafeWise"},
    ],
    en_c="Reolink Argus 4 Pro holds first and the Solar Floodlight Camera UK launch this week (after the US debut last month) is part of the same playbook: subscription-free, solar-powered, local AI, and now with a 2K/1000-lumen floodlight variant that nobody else in the no-subscription tier has matched. The Gadgeteer's roundup this week specifically calls out the Argus 4 Pro alongside Tapo C460 and eufyCam S3 Pro as the only cameras running their core AI fully on-device, which is the durable architectural advantage. First place locked in. Arlo Pro 5S stays at second on hardware merit but the SafeWise piece this week documents what the broader market already knows: subscription pricing changes have triggered a real customer migration to Eufy and Reolink, and Arlo's brand is taking durable damage. Eufy SoloCam S340 stays at third and the local-storage privacy-first architecture is now its strongest sustained argument. Google Nest Cam Outdoor, Aosu SolarCam T2 Ultra, Ring Spotlight Cam Pro, and Blink Outdoor 4 are unchanged. The no-subscription tier keeps widening the gap on the subscription-required competitors and I do not see that reversing this quarter.",
    en_h=[
        {"title": "Reolink Solar Floodlight Camera extends the no-subscription playbook", "body": "UK launch after US debut, 2K with 1000-lumen flood, SolarEase needs one hour of sunlight per day, no subscription. Nobody else in the no-subscription tier has matched this combination. First place locked in for Argus 4 Pro lineup strength."},
        {"title": "Local on-device AI is the durable architectural advantage", "body": "The Gadgeteer roundup this week names Argus 4 Pro, Tapo C460, eufyCam S3 Pro, and UniFi AI Pro as the only cameras running core AI on-device. This is the architectural moat that subscription-cloud competitors cannot easily close. Score holds, position locked."},
        {"title": "Arlo subscription backlash is now documented brand damage", "body": "SafeWise documents what the broader market already knows: subscription pricing changes triggered real customer migration to Eufy and Reolink. Arlo's brand is taking durable damage even though the hardware still earns second place. Buyers should weigh the longer-term cost trajectory."},
    ],
    zh_c="Reolink Argus 4 Pro 守住第一，這禮拜 Reolink Solar Floodlight Camera 英國上市（上個月美國先發），同一套劇本：免訂閱、太陽能供電、本地 AI，再加上 2K 跟 1000 流明投光，免訂閱段沒人配得起這個組合。The Gadgeteer 這禮拜的整理特別點名 Argus 4 Pro、Tapo C460、eufyCam S3 Pro 是少數真的把核心 AI 跑在裝置上的攝影機，這是長期的架構優勢。第一名鎖定。\n\nArlo Pro 5S 守第二，純看硬體還是合理，但 SafeWise 這禮拜那篇文章把整個市場都知道的事寫清楚了：訂閱漲價已經造成實際的用戶外流到 Eufy 跟 Reolink，Arlo 品牌正在承受長期傷害。Eufy SoloCam S340 守第三，本地儲存、隱私優先的架構現在是它最持久的賣點。\n\nGoogle Nest Cam Outdoor、Aosu SolarCam T2 Ultra、Ring Spotlight Cam Pro、Blink Outdoor 4 都沒動。\n\n免訂閱段對需要訂閱的競品差距還在拉大，這一季我看不到逆轉跡象。台灣這邊燦坤跟 PChome 都還是 Reolink 比較容易找到貨，Arlo 通路相對少。",
    zh_h=[
        {"title": "Reolink Solar Floodlight Camera 延續免訂閱劇本", "body": "英國接著美國上市，2K 加 1000 流明投光，SolarEase 一天一小時陽光就能撐整天，免訂閱。免訂閱段沒人配得起這個組合。Argus 4 Pro 產品線整體強度讓第一名鎖定。"},
        {"title": "本地裝置端 AI 是長期架構優勢", "body": "The Gadgeteer 這禮拜的整理把 Argus 4 Pro、Tapo C460、eufyCam S3 Pro、UniFi AI Pro 列為少數真的把核心 AI 跑在裝置上的攝影機。這是訂閱雲端競品不容易追上的架構護城河。分數守住，位置鎖定。"},
        {"title": "Arlo 訂閱反彈現在是有紀錄的品牌傷害", "body": "SafeWise 把市場都知道的事寫清楚：訂閱漲價造成實際用戶外流到 Eufy 跟 Reolink。Arlo 硬體還能撐第二名，但品牌正在承受長期傷害。買家要把長期成本軌跡算進去。"},
    ],
)


# ============================================================
# best-video-doorbells
# ============================================================
add(
    "best-video-doorbells",
    refs=[
        {"title": "Eufy Video Doorbell S4 CES 2026 panoramic and AI tracking detailed", "url": "https://www.expertreviews.co.uk/technology/home-security/ces-2026-eufy-video-doorbell-s4", "source": "Expert Reviews"},
        {"title": "Ring AI Unusual Event Alerts rolls out in beta to existing doorbells", "url": "https://www.t3.com/home-living/smart-home/ring-ai-unusual-event-alerts-may-2026", "source": "T3"},
        {"title": "Aqara Doorbell Camera Hub G410 Matter over Thread expansion", "url": "https://www.aqara.com/news/g410-matter-thread-may-2026", "source": "Aqara"},
    ],
    en_c="Eufy Video Doorbell E340 holds first because the broader Eufy doorbell story keeps strengthening: the S4 unveiled at CES 2026 with panoramic 180-degree view and AI tracking is the upcoming flagship, and the E340 already benefits from the same local AI package recognition firmware that shipped last week. Buyers shopping today get a no-subscription doorbell that genuinely matches subscription competitors on smart features. First place locked in. Aqara Doorbell Camera Hub G410 stays at second and the Matter over Thread certification keeps expanding to more regional Thread border routers, which strengthens the smart-home integration story for Matter-and-Thread households. Score holds. Google Nest Doorbell Wired 2nd Gen holds third. Ring Battery Doorbell Pro 2nd Gen is at fourth and the new AI Unusual Event Alerts beta is technically interesting but it lives inside the Ring Protect subscription, which only reinforces the long-term cost argument working against Ring right now. Ring Battery Doorbell Plus, Arlo Video Doorbell 2K 2nd Gen, and Blink Video Doorbell are unchanged. The no-subscription gap keeps widening.",
    en_h=[
        {"title": "Eufy doorbell roadmap strength reinforces E340 first place", "body": "S4 unveiled at CES 2026 with panoramic 180-degree view and AI tracking is the upcoming flagship, and the E340 already runs the same local AI package recognition firmware from last week. Buyers today get subscription-tier features without the subscription. First place locked in."},
        {"title": "Aqara G410 Matter over Thread keeps expanding regional support", "body": "Certification expanding to more regional Thread border routers strengthens the smart-home integration story for Matter-and-Thread households. For mixed-vendor Matter setups this is the most cleanly integrated video doorbell. Second place unchanged."},
        {"title": "Ring AI Unusual Event Alerts lives behind the subscription paywall", "body": "Beta is technically interesting but it requires Ring Protect. That only reinforces the long-term cost trajectory argument working against Ring right now. Fourth place unchanged and the value case keeps deteriorating."},
    ],
    zh_c="Eufy Video Doorbell E340 守住第一，整個 Eufy 門鈴產品線故事持續強化：CES 2026 公布的 S4 配 180 度全景跟 AI 追蹤是接下來的旗艦，而 E340 已經吃到上禮拜推送的本地 AI 包裹辨識韌體。今天買家拿到的是一台免訂閱、智慧功能真的能匹敵訂閱競品的門鈴。第一名鎖定。\n\nAqara Doorbell Camera Hub G410 守第二，Matter over Thread 認證持續擴展到更多區域 Thread 邊界路由器，Matter 跟 Thread 家庭的整合故事更強。分數守住。Google Nest Doorbell Wired 2nd Gen 守第三。\n\nRing Battery Doorbell Pro 2nd Gen 排第四，新的 AI 異常事件警示 beta 技術上有意思，但要綁 Ring Protect 訂閱才有，這只會強化長期成本對 Ring 不利的論點。\n\nRing Battery Doorbell Plus、Arlo Video Doorbell 2K 2nd Gen、Blink Video Doorbell 都沒動。\n\n免訂閱差距還在拉大。台灣這邊 Eufy 在 momo 跟 PChome 通路明顯比 Ring 完整，這個排序對本地買家來說也容易執行。",
    zh_h=[
        {"title": "Eufy 門鈴產品線實力強化 E340 第一名", "body": "CES 2026 公布的 S4 配 180 度全景跟 AI 追蹤是接下來旗艦，E340 已經吃到上禮拜的本地 AI 包裹辨識韌體。今天買家拿到訂閱等級功能但不用付訂閱。第一名鎖定。"},
        {"title": "Aqara G410 Matter over Thread 持續擴展區域支援", "body": "認證擴展到更多區域 Thread 邊界路由器，Matter 跟 Thread 家庭整合故事更強。混合廠商 Matter 場景下，最乾淨整合的視訊門鈴。第二名不動。"},
        {"title": "Ring AI 異常事件警示活在訂閱付費牆後面", "body": "Beta 技術上有意思，但要綁 Ring Protect。這只會強化長期成本對 Ring 不利的論點。第四名不動，C/P 值說服力持續惡化。"},
    ],
)


# ============================================================
# best-robot-vacuums
# ============================================================
add(
    "best-robot-vacuums",
    refs=[
        {"title": "Dreame L60 lineup launches at Dreame Next event", "url": "https://vacuumwars.com/dreame-l60-launch-may-2026", "source": "Vacuum Wars"},
        {"title": "Roborock Saros 20 ships premium mop-and-vac combo update", "url": "https://us.roborock.com/news/saros-20-may-2026", "source": "Roborock"},
        {"title": "TechRadar 2026 robot vacuum standouts include walking robot concepts", "url": "https://www.techradar.com/home/robot-vacuums/best-2026-models", "source": "TechRadar"},
    ],
    en_c="Dreame X60 Max Ultra Complete holds first and the L60 lineup that just launched at the Dreame Next event reinforces the brand's positioning across entry to flagship: 100°C mop self-cleaning and suction up to 35,000Pa across the new tier sets the technical bar that competitors are now chasing. X60 Max Ultra remains the no-compromise pick. First place locked in. Roborock Saros 10R stays at second and the Saros 20 update this week confirms Roborock's commitment to the premium mop-and-vac combo segment, which keeps Saros 10R relevant on app ecosystem and resale value. Dreame L50 Ultra holds third. Roborock Qrevo CurvX stays at fourth. Ecovacs Deebot X5 Pro Omni holds fifth. Eufy X10 Pro Omni, Narwal Freo X Ultra, and Mova P10 Pro Ultra are unchanged. The walking robot vacuum category that TechRadar profiled this week is interesting but it is at least two product cycles from being something a normal household should buy; for now the leaderboard is stable and Dreame's technical lead at the top is widening.",
    en_h=[
        {"title": "Dreame L60 launch reinforces X60 Max Ultra first-place position", "body": "100°C mop self-cleaning and 35,000Pa suction across the new L60 tier sets the technical bar competitors are chasing. X60 Max Ultra remains the no-compromise flagship. First place locked in and the technical lead is widening."},
        {"title": "Roborock Saros 20 update keeps Saros 10R relevant on ecosystem", "body": "Saros 20 update this week signals Roborock's continued commitment to the premium mop-and-vac segment, which keeps the Saros 10R relevant on app ecosystem maturity and resale value. Second place locked in for the Roborock-ecosystem crowd."},
        {"title": "Walking robot vacuums are two cycles away from real households", "body": "TechRadar's profile of the walking-robot concepts is interesting but stair-climbing and obstacle-stepping prototypes are still pre-production. For now the leaderboard is stable and buyers should not wait. Dreame and Roborock at the top remain the smart 2026 purchases."},
    ],
    zh_c="Dreame X60 Max Ultra Complete 守住第一，Dreame Next 活動剛發表的 L60 產品線強化了品牌從入門到旗艦的整體定位：新一階全線標配 100°C 拖布自清跟最高 35,000Pa 吸力，把技術門檻拉到競品要追的位置。X60 Max Ultra 還是無妥協首選。第一名鎖定。\n\nRoborock Saros 10R 守第二，這禮拜 Saros 20 的更新確認 Roborock 對高階洗拖二合一的持續承諾，這讓 Saros 10R 在 app 生態成熟度跟二手價值上保持吸引力。Dreame L50 Ultra 守第三。Roborock Qrevo CurvX 守第四。Ecovacs Deebot X5 Pro Omni 守第五。\n\nEufy X10 Pro Omni、Narwal Freo X Ultra、Mova P10 Pro Ultra 都沒動。\n\nTechRadar 這禮拜介紹的會走路掃地機器人概念有趣，但離一般家庭該買還有至少兩個產品週期。目前榜單很穩，Dreame 在頂端的技術領先還在擴大。台灣 PChome 跟 momo 上 X60 Max Ultra 大概落在 NT$45,000，這個價位想一步到位的人就鎖定它。",
    zh_h=[
        {"title": "Dreame L60 上市強化 X60 Max Ultra 第一名位置", "body": "L60 新一階全線 100°C 拖布自清跟 35,000Pa 吸力，把技術門檻拉到競品要追的位置。X60 Max Ultra 還是無妥協旗艦。第一名鎖定，技術領先持續擴大。"},
        {"title": "Roborock Saros 20 更新讓 Saros 10R 在生態上保持吸引力", "body": "這禮拜 Saros 20 更新訊號 Roborock 對高階洗拖二合一的持續承諾，Saros 10R 在 app 生態成熟度跟二手價值上保持吸引力。Roborock 生態用戶第二名鎖定。"},
        {"title": "會走路的掃地機器人離真實家庭還有兩個產品週期", "body": "TechRadar 介紹的會走路概念有趣，但爬樓梯跟跨越障礙物的原型還在量產前。榜單目前穩定，買家不需要等。Dreame 跟 Roborock 在頂端就是 2026 年聰明的採購。"},
    ],
)


# ============================================================
# best-robot-lawn-mowers
# ============================================================
add(
    "best-robot-lawn-mowers",
    refs=[
        {"title": "Mammotion LUBA 3 AWD savings up to $700 with free garage attachment", "url": "https://9to5toys.com/2026/05/12/mammotion-luba-3-awd-robot-mowers-free-garage-attachment-from-2099/", "source": "9to5Toys"},
        {"title": "Mammotion 2026 upgrades highlight Tri-Fusion positioning and 10 TOPS AI", "url": "https://us.mammotion.com/blogs/news/mammation-robot-lawn-mowers-upgrades-2026", "source": "Mammotion"},
        {"title": "Mammotion brings iNavi service to the US for high-precision lawn care", "url": "https://www.prnewswire.com/news-releases/mammotion-brings-inavi-service-to-the-us-may-2026", "source": "PR Newswire"},
    ],
    en_c="Mammotion LUBA 3 AWD 5000 holds first and the price action this week is genuinely aggressive: standard model down from $2,608 to $2,099 with a free garage attachment thrown in, which makes this the best price-to-capability deal in the category right now. Combined with last week's zone-based scheduling firmware, the case for the LUBA 3 AWD at the top of the leaderboard is honestly stronger than it has been all year. First place locked in. The 2026 upgrade roadmap published this week (Tri-Fusion Positioning, 10 TOPS AI chip, DropMow Mode, Edge Cutting Disc) signals where the platform is heading, and the iNavi service launch in the US adds a layer of high-precision support that Husqvarna EPOS has only recently come close to matching. Ecovacs Goat A3000 LiDAR Pro stays at second. Ecovacs Goat A3000 LiDAR holds third. Segway Navimow X315 stays at fourth. Navimow i2 LiDAR holds fifth. Husqvarna Automower 450X EPOS at sixth benefits from last week's tree-canopy GPS drift fix but the broader category price reset (the 430X jumped 54% since March on tariffs and spring demand) makes the Mammotion deal stand out even more. Worx Landroid Vision M600 and Yarbo Lawn Mower Pro are unchanged.",
    en_h=[
        {"title": "Mammotion LUBA 3 AWD at $2,099 with free garage attachment is the deal", "body": "Standard model down from $2,608 to $2,099 with free garage attachment. Combined with last week's zone-based scheduling firmware, the case for LUBA 3 AWD at the top is the strongest it has been all year. First place locked in for large-yard buyers."},
        {"title": "Mammotion 2026 roadmap signals durable platform advantage", "body": "Tri-Fusion Positioning, 10 TOPS AI chip, DropMow Mode, Edge Cutting Disc, plus iNavi service launch in the US. This is the kind of platform investment that Husqvarna EPOS has only recently come close to matching. The technical moat is widening at the top."},
        {"title": "Category-wide price reset makes the Mammotion deal stand out further", "body": "Husqvarna 430X jumped 54% since March on tariffs and spring demand. Against that backdrop the Mammotion price action this week looks even more aggressive. Buyers should not wait for further softening this season."},
    ],
    zh_c="Mammotion LUBA 3 AWD 5000 守住第一，這禮拜的定價動作真的很積極：標準版從 $2,608 降到 $2,099，再送車庫配件，這是整個分類目前能力對價格最有感的組合。配上上禮拜的分區排程韌體，LUBA 3 AWD 站在榜首的論點老實說是今年最強。第一名鎖定。\n\n這禮拜公布的 2026 升級路線圖（Tri-Fusion 定位、10 TOPS AI 晶片、DropMow 模式、邊緣切割碟）標出平台往哪走，加上 iNavi 服務在美國上線，給了一層高精度服務支援，Husqvarna EPOS 也是最近才追到接近。\n\nEcovacs Goat A3000 LiDAR Pro 守第二。Ecovacs Goat A3000 LiDAR 守第三。Segway Navimow X315 守第四。Navimow i2 LiDAR 守第五。Husqvarna Automower 450X EPOS 第六名，吃到上禮拜樹冠 GPS 漂移修正的好處，但整個分類三月以來大幅漲價（430X 因為關稅跟春季需求漲了 54%）讓 Mammotion 這次的降價對比更突出。\n\nWorx Landroid Vision M600、Yarbo Lawn Mower Pro 都沒動。台灣割草機器人偏小眾，但有透天院子的買家，這個價格時點值得認真評估。",
    zh_h=[
        {"title": "Mammotion LUBA 3 AWD $2,099 送車庫配件就是時點", "body": "標準版從 $2,608 降到 $2,099 加送車庫配件。配上上禮拜的分區排程韌體，LUBA 3 AWD 站在榜首的論點是今年最強。大庭院買家第一名鎖定。"},
        {"title": "Mammotion 2026 路線圖標出長期平台優勢", "body": "Tri-Fusion 定位、10 TOPS AI 晶片、DropMow 模式、邊緣切割碟，加上 iNavi 服務美國上線。這種平台投資強度 Husqvarna EPOS 也是最近才追到。頂端的技術護城河持續擴大。"},
        {"title": "整體分類漲價讓 Mammotion 降價對比更突出", "body": "Husqvarna 430X 因為關稅跟春季需求自三月以來漲 54%。在這個背景下，Mammotion 這禮拜的降價動作更積極。買家這季不要再等更進一步軟化。"},
    ],
)


# ============================================================
# best-air-purifiers
# ============================================================
add(
    "best-air-purifiers",
    refs=[
        {"title": "Coway Airmega 400S confirmed Consumer Reports 2026 best-overall pick", "url": "https://www.consumerreports.org/appliances/air-purifiers/best-air-purifiers-of-the-year-a1197763201/", "source": "Consumer Reports"},
        {"title": "IQAir HealthPro Plus reaffirmed wildfire-smoke choice by IQAir guide", "url": "https://www.iqair.com/us/air-purifiers-for-wildfire-smoke", "source": "IQAir"},
        {"title": "Blueair Blue Pure 211+ large-space CADR matches Coway 400S at lower price", "url": "https://www.blueair.com/blogs/news/best-air-purifiers-may-2026", "source": "Blueair"},
    ],
    en_c="IQAir HealthPro Plus holds first because the wildfire-prep narrative is intensifying this week as Western US fire-season forecasts firm up, and HealthPro Plus remains the only consumer purifier with HyperHEPA media certified below 0.1 microns. Last week's restock window is starting to close again per IQAir distributor signal. First place locked in. Coway Airmega 400S stays at second and the Consumer Reports 2026 best-overall designation this week (350 CFM smoke CADR, CARB-certified, balanced noise and filter cost) validates the second-place position; the firmware VOC tracking from last week is now a meaningful tiebreaker in shopping decisions. Score holds. Blueair HealthProtect 7470i holds third and the broader Blueair lineup (notably Blue Pure 211+) is getting more comparison coverage this week as the lower-cost large-space pick. Rabbit Air MinusA3, Levoit Core 600S, Dyson Purifier Cool TP07, Honeywell HPA300, Coway Airmega Prox, and IQAir Atem Earth are unchanged. The EPA HEPA standards refresh from earlier this month will shape H2 conversation; for now the wildfire-prep window is the dominant near-term driver and IQAir is the right urgent purchase.",
    en_h=[
        {"title": "IQAir HealthPro Plus wildfire-prep window is the buy-now signal", "body": "Western US fire-season forecasts firming up and HealthPro Plus is the only consumer purifier with HyperHEPA media certified below 0.1 microns. Distributor restock signal suggests the window starts closing again. First place locked in for urgent purchase."},
        {"title": "Coway 400S Consumer Reports best-overall designation validates second", "body": "Consumer Reports 2026 picks confirm 350 CFM smoke CADR, CARB-certified, balanced noise and filter cost. Last week's firmware VOC tracking is now a meaningful tiebreaker in shopping decisions. Second place locked in on validated performance."},
        {"title": "Blueair lineup gaining comparison coverage as lower-cost large-space pick", "body": "Blue Pure 211+ matching Coway 400S CADR at lower price is getting more reviewer attention this week. HealthProtect 7470i benefits from the brand-level halo. Third place unchanged but the broader Blueair story is strengthening for H2 conversation."},
    ],
    zh_c="IQAir HealthPro Plus 守住第一，野火季節準備的話題這禮拜在美西火季預測逐漸定調的背景下持續加強，HealthPro Plus 還是唯一通過認證能捕捉 0.1 微米以下超細微粒的家用清淨機。上禮拜的補貨窗口從通路訊號看正在再次收窄。第一名鎖定。\n\nCoway Airmega 400S 守第二，這禮拜 Consumer Reports 2026 把它列為最佳整體（350 CFM 煙霧 CADR、CARB 認證、噪音與濾網成本平衡）驗證了第二名位置；上禮拜的韌體 VOC 追蹤現在在選購決策裡是有意義的決勝點。分數守住。\n\nBlueair HealthProtect 7470i 守第三，整個 Blueair 產品線（特別是 Blue Pure 211+）這禮拜在比較報導裡的曝光增加，被定位成大空間低成本選擇。Rabbit Air MinusA3、Levoit Core 600S、Dyson Purifier Cool TP07、Honeywell HPA300、Coway Airmega Prox、IQAir Atem Earth 都沒動。\n\n月初公布的 EPA HEPA 標準改版會影響下半年的話題，但目前野火準備窗口才是短期主導因素，IQAir 就是急需採購的正確答案。台灣這邊雖然沒野火問題，但五月沙塵跟梅雨前的空氣品質波動值得提早把機器準備好。",
    zh_h=[
        {"title": "IQAir HealthPro Plus 野火準備窗口就是現在下手的訊號", "body": "美西火季預測逐漸定調，HealthPro Plus 是唯一通過認證能捕捉 0.1 微米以下超細微粒的家用清淨機。通路補貨訊號顯示窗口開始再次收窄。緊急採購第一名鎖定。"},
        {"title": "Coway 400S Consumer Reports 最佳整體認證驗證第二名", "body": "Consumer Reports 2026 名單確認 350 CFM 煙霧 CADR、CARB 認證、噪音與濾網成本平衡。上禮拜韌體 VOC 追蹤在選購決策裡是有意義的決勝點。第二名靠驗證表現鎖定。"},
        {"title": "Blueair 產品線在比較報導被定位成大空間低成本選擇", "body": "Blue Pure 211+ 以較低價格達到 Coway 400S 級別 CADR 這禮拜在更多評測裡曝光。HealthProtect 7470i 吃到品牌光環。第三名不動，整個 Blueair 故事在下半年話題裡會更強。"},
    ],
)


# ============================================================
# best-portable-air-conditioners
# ============================================================
add(
    "best-portable-air-conditioners",
    refs=[
        {"title": "Reviewed 2026 best portable air conditioners crowns Whynter ARC top tier", "url": "https://www.reviewed.com/home-outdoors/best-right-now/best-portable-air-conditioners/", "source": "Reviewed"},
        {"title": "Midea Duo MAP14HS1TBL named 2026 best portable AC for most people", "url": "https://www.consumeranalysis.com/guides/portable-ac/midea-duo-review/", "source": "Consumer Analysis"},
        {"title": "RTINGS 2026 top four portable AC roundup confirms LG inverter strength", "url": "https://www.rtings.com/air-conditioner/reviews/best/portable", "source": "RTINGS"},
    ],
    en_c="Whynter NEX ARC-1230WN holds first this week because the broader review consensus from Reviewed and Forbes this month reaffirms the dual-hose architecture and 600 sq ft coverage as best-in-class, and the spring promo pricing at Lowe's that landed last week is still active heading into Memorial Day. First place locked in. Midea Duo MAP14HS1TBL stays at second and Consumer Analysis this week reiterated its 2026 best-portable-AC-for-most-people designation, with the variable-speed inverter genuinely the most efficient architecture on the market when you account for runtime electricity cost. The Home Depot exclusive bundle from last week makes the value math even tighter. Score holds. LG LP1419IVSM Dual Inverter holds third and the RTINGS top-four roundup this week confirms LG's inverter strength on energy efficiency; the smart upgrade firmware from last week closed the geofencing gap to Midea. Whynter Elite ARC-122DS stays at fourth. DeLonghi Pinguino Arctic Whisper holds fifth. Black+Decker BPACT14WT, KoolSiln 14,000 BTU, and Hisense HAP0824TWD are unchanged. Cooling season is fully on; budget-tier pricing will tighten further through June and serious buyers should commit now rather than wait.",
    en_h=[
        {"title": "Whynter NEX ARC-1230WN dual-hose architecture confirmed best-in-class", "body": "Reviewed and Forbes reaffirmed the dual-hose architecture and 600 sq ft coverage as best-in-class this month, and the Lowe's spring promo from last week is still active heading into Memorial Day. First place locked in for serious cooling households."},
        {"title": "Midea Duo named 2026 best portable AC for most people", "body": "Consumer Analysis reiterated the 2026 designation this week and the variable-speed inverter is the most electricity-efficient architecture on the market over a full cooling season. Home Depot exclusive bundle from last week tightens the math further. Second place locked in."},
        {"title": "LG LP1419IVSM Dual Inverter validated by RTINGS top-four", "body": "RTINGS top-four roundup this week confirms LG's inverter strength on energy efficiency, and last week's smart upgrade firmware closed the geofencing gap to Midea. For LG-ecosystem households this is now the obvious pick. Third place locked in."},
    ],
    zh_c="Whynter NEX ARC-1230WN 守住第一，整個五月 Reviewed 跟 Forbes 的評測共識重申雙風管架構跟 600 平方呎覆蓋是同級最佳，上禮拜在 Lowe's 開的春季促銷定價這禮拜進入陣亡將士紀念日週還在跑。第一名鎖定。\n\nMidea Duo MAP14HS1TBL 守第二，Consumer Analysis 這禮拜再次重申 2026 年「大多數人最佳選擇」定位，變頻壓縮機把整個冷氣季的電費算進去是市面上最有效率的架構。上禮拜 Home Depot 獨家組合讓 C/P 值算盤更緊。分數守住。\n\nLG LP1419IVSM Dual Inverter 守第三，RTINGS 這禮拜的前四名整理確認 LG 變頻在節能上的強度；上禮拜的智慧升級韌體把地理圍欄缺口補上對到 Midea。Whynter Elite ARC-122DS 守第四。DeLonghi Pinguino Arctic Whisper 守第五。\n\nBlack+Decker BPACT14WT、KoolSiln 14,000 BTU、Hisense HAP0824TWD 都沒動。\n\n冷氣季完全開跑，預算段定價六月底會再收緊，認真在採購的人就現在下手不要等。台灣這邊雖然主力還是分離式跟窗型，但租屋族或臨時加強冷房的場景，Midea Duo 這種雙風管架構效率還是值得認真評估。",
    zh_h=[
        {"title": "Whynter NEX ARC-1230WN 雙風管架構獲確認同級最佳", "body": "Reviewed 跟 Forbes 這個月重申雙風管架構跟 600 平方呎覆蓋同級最佳，上禮拜 Lowe's 春季促銷進入陣亡將士紀念日週還在跑。認真冷房家庭第一名鎖定。"},
        {"title": "Midea Duo 獲認證 2026 大多數人最佳便攜冷氣", "body": "Consumer Analysis 這禮拜再次重申 2026 年認定，變頻壓縮機把整個冷氣季電費算進去是市面上最有效率的架構。上禮拜 Home Depot 獨家組合讓算盤更緊。第二名鎖定。"},
        {"title": "LG LP1419IVSM Dual Inverter 獲 RTINGS 前四名驗證", "body": "RTINGS 這禮拜前四名整理確認 LG 變頻在節能上的強度，上禮拜智慧升級韌體把地理圍欄缺口補上對到 Midea。LG 生態家庭就選它。第三名鎖定。"},
    ],
)
