"""2026-06-02 daily update — Batch 6: Smart Home / Wearables (7 files)"""
import json
from pathlib import Path

DATE = "2026-06-02"
ROOT = Path("/Users/etrexkuo/toprankland/src/content/rankings")

def load(name):
    p = ROOT / name
    return json.loads(p.read_text(encoding="utf-8")), p

def save(p, data):
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

def upsert(data, entry):
    for i, h in enumerate(data["history"]):
        if h["date"] == entry["date"]:
            data["history"][i] = entry
            return
    data["history"].append(entry)

def last_rankings(d):
    return d["history"][-1]["rankings"]


def build_security_cameras():
    d, p = load("best-security-cameras.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Best AI Security Cameras 2026: On-Device Detection Tested", "url": "https://the-gadgeteer.com/2026/05/11/best-ai-security-cameras-2026/", "source": "The Gadgeteer"},
            {"title": "Best Smart Security Cameras 2026: No-Sub Picks That Actually Detect", "url": "https://www.smarthomeexplorer.com/guides/best-smart-security-cameras-2026", "source": "Smart Home Explorer"},
            {"title": "Best Battery Powered Outdoor Security Camera for Homes in 2026", "url": "https://the-gadgeteer.com/2026/04/02/best-battery-powered-outdoor-security-camera-for-homes-in-2026/", "source": "The Gadgeteer"},
        ],
        "i18n": {
            "en": {
                "commentary": "Summer is when home security cameras earn their keep. Longer evenings, more travel, and packages piling up on the porch all push this category to its peak demand window, and the 2026 lineup rewards buyers who care about owning their footage rather than renting access to it. The Reolink Argus 4 Pro holds the top spot at 9.2 overall for one decisive reason: it delivers a dual-lens 4K setup that stitches a seamless 180-degree panoramic view with zero monthly fees. Its 9.5 video quality and 9.5 value scores reflect a camera that gives you flagship image quality and then never asks for your credit card again.\n\nThe defining shift in 2026 is on-device AI. The cameras with the most reliable detection now run it locally rather than in the cloud, and the Argus 4 Pro and Arlo Pro 5S both sit on the right side of that line. The Arlo Pro 5S at rank 2 earns its place through the best AI detection in the lineup at 9.5 and a 9.5 battery score, plus the broadest smart home compatibility of any camera here. If you live across multiple platforms and want one camera that talks to all of them, the Arlo is the pick, just budget for the Arlo Secure plan to unlock its smartest features.\n\nThe eufy SoloCam S340 at rank 3 is my recommendation for buyers who want genuine local storage and solar charging in one package. The 9.0 storage flexibility and 9.0 value scores reflect eufy's no-subscription philosophy paired with dual cameras and a HomeBase-style local archive. With summer travel season here and porch-piracy at its annual high, a camera that records reliably without a recurring bill is exactly what most households actually need.",
                "highlights": [
                    {"title": "Reolink Argus 4 Pro Owns the No-Subscription Crown", "body": "A dual-lens 4K sensor stitches a seamless 180-degree panorama with zero monthly fees, earning 9.5 video quality and 9.5 value scores. For buyers who refuse to rent access to their own footage, this is the clearest pick in the category heading into summer."},
                    {"title": "On-Device AI Detection Separates the Best From the Rest", "body": "The most reliable 2026 cameras run AI detection locally rather than in the cloud. The Argus 4 Pro and Arlo Pro 5S both process on-device, which means faster alerts, better privacy, and detection that keeps working even when your internet hiccups."},
                    {"title": "eufy SoloCam S340 Pairs Solar Charging With Local Storage", "body": "Dual cameras, solar charging, and HomeBase-style local archiving give the SoloCam S340 a 9.0 storage flexibility score and 9.0 value with no recurring fees. It is the set-and-forget choice for households that want coverage without a monthly bill."},
                ],
            },
            "zh-tw": {
                "commentary": "夏天是居家監視器最該上場的季節。白天變長、出遊變多，包裹又常常堆在門口，這個品類的需求每年都在這時候衝到高點。2026 年的產品線特別照顧一種買家：想要真正擁有自己的錄影檔，而不是每個月付錢租用雲端權限的人。\n\n榜單第一的 Reolink Argus 4 Pro 總分 9.2，理由很直接，它用雙鏡頭 4K 拼出無縫的 180 度全景，而且完全不收月費。影像品質 9.5、性價比 9.5 分，畫質給你旗艦規格，之後再也不跟你要信用卡，這點台灣用戶會很有感。\n\n2026 年最關鍵的轉變是 On-Device AI。偵測最可靠的機型，現在都把運算放在本機端而不是雲端，Argus 4 Pro 和 Arlo Pro 5S 都站在對的那一邊。Arlo Pro 5S 排第二，AI 偵測 9.5 分是全榜最高，電池 9.5 分，相容性也是最廣的。如果你家同時跨好幾個智慧家庭平台，想要一台全都能溝通的相機，選 Arlo，但要記得 Arlo Secure 訂閱才能解鎖最聰明的功能。\n\neufy SoloCam S340 第三名，我推給想要真正本地儲存又要太陽能充電的人。儲存彈性 9.0、性價比 9.0 分，雙鏡頭加上 HomeBase 式的本地備份，免訂閱。夏天出遊旺季加上門口包裹失竊的高峰期，一台不用每月繳費就能穩定錄影的相機，才是多數家庭真正需要的。",
                "highlights": [
                    {"title": "Reolink Argus 4 Pro 免訂閱之王", "body": "雙鏡頭 4K 拼出無縫 180 度全景，完全零月費，影像品質 9.5、性價比 9.5 分。拒絕為自己的錄影檔付租金的買家，這台是夏天入手最明確的選擇。"},
                    {"title": "On-Device AI 偵測拉開頂尖與其餘的差距", "body": "2026 年最可靠的監視器都把 AI 偵測放在本機端而非雲端。Argus 4 Pro 和 Arlo Pro 5S 都是本機運算，警報更快、隱私更好，網路打嗝時偵測照樣能用。"},
                    {"title": "eufy SoloCam S340 太陽能加本地儲存一次到位", "body": "雙鏡頭、太陽能充電、HomeBase 式本地備份，儲存彈性 9.0、性價比 9.0 分，完全免月費。想要全程覆蓋又不想每月扣款的家庭，這台裝好就能放著不管。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK security-cameras")


def build_video_doorbells():
    d, p = load("best-video-doorbells.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Ring vs Eufy vs Aqara: Best Video Doorbell of 2026?", "url": "https://www.onesmartcrib.com/ring-vs-eufy-vs-aqara/", "source": "oneSmartcrib"},
            {"title": "Best Smart Doorbell Cameras 2026: Ring vs Nest vs Eufy Compared", "url": "https://www.smarthomeexplorer.com/guides/best-smart-doorbell-cameras-2026", "source": "Smart Home Explorer"},
            {"title": "The Best Video Doorbells of 2026", "url": "https://www.reviewed.com/smarthome/best-right-now/best-smart-doorbells", "source": "Reviewed"},
        ],
        "i18n": {
            "en": {
                "commentary": "Video doorbells hit peak demand in summer, when porch deliveries surge and households travel more than any other season. The 2026 lineup makes the smart-money choice clear: doorbells that store footage locally and skip the mandatory subscription. The eufy E340 holds the top spot at 9.2 overall, and it earns it with a genuinely clever dual-camera design. A front-facing lens watches the person at your door while a second downward lens watches your packages on the porch, and the whole thing leans on AI to detect faces and parcels for sharper notifications. With 8GB of local storage, roughly three months of recording, and a category-leading 9.8 value score, it is the doorbell I recommend to most people without hesitation.\n\nThe Aqara G410 at rank 2 is the most interesting play for smart home enthusiasts. It delivers 2K head-to-toe video, local recording, Wi-Fi 6, PoE support, and a 9.8 smart home integration score, the highest in the lineup. For anyone built around HomeKit, Apple Home Key support and native HomeKit Secure Video make this the natural choice.\n\nThe Google Nest Doorbell wired second-gen at rank 3 leads the field on detection at 9.8, with the most refined people, package, and familiar-face recognition here. It is the pick for buyers already living in the Google Home ecosystem who want detection that simply works. With package theft peaking through the summer months and more households away on vacation, a doorbell that reliably captures and stores what happens at your door is one of the highest-value smart home purchases you can make right now.",
                "highlights": [
                    {"title": "eufy E340 Dual Cameras Watch the Door and the Porch", "body": "A front lens covers visitors while a downward lens covers your packages, with AI face and parcel detection sharpening every alert. Add 8GB of local storage and a 9.8 value score with no mandatory subscription, and it is the easiest doorbell recommendation of 2026."},
                    {"title": "Aqara G410 Is the HomeKit Power User's Pick", "body": "2K head-to-toe video, Wi-Fi 6, PoE support, and a category-leading 9.8 smart home integration score. Native HomeKit Secure Video and Apple Home Key make it the natural doorbell for anyone built around the Apple smart home."},
                    {"title": "Local Storage Wins the Summer Package Season", "body": "With porch deliveries surging and households traveling, doorbells that record locally without a subscription deliver the best long-term value. The eufy E340, Aqara G410, and subscription-free rivals all skip the recurring fee that Ring requires for its best features."},
                ],
            },
            "zh-tw": {
                "commentary": "視訊門鈴的需求每年夏天衝到最高，因為包裹配送量暴增，加上大家出遊的比例也是全年最高。2026 年的產品線把聰明錢的選擇講得很清楚：選會把錄影存在本地、不強迫你訂閱的門鈴就對了。\n\n榜單第一的 eufy E340 總分 9.2，靠的是真的很聰明的雙鏡頭設計。前鏡頭盯著門口的人，第二顆向下的鏡頭盯著你放在門廊的包裹，整套還用 AI 偵測人臉和包裹，通知更精準。8GB 本地儲存大約能存三個月，性價比 9.8 分是全榜最高，這台我幾乎可以無腦推給大部分人。\n\nAqara G410 第二名，是智慧家庭玩家最有意思的選擇。2K 全身視角、本地錄影、Wi-Fi 6、支援 PoE，智慧家庭整合 9.8 分是全榜最高。如果你整套圍繞 HomeKit 建立，原生 HomeKit Secure Video 加上 Apple Home Key，這台就是自然的答案。\n\nGoogle Nest Doorbell 有線第二代排第三，偵測 9.8 分領先全場，人物、包裹、熟面孔辨識都是這裡最細膩的。已經住在 Google Home 生態系、想要偵測穩定不出錯的人，選它準沒錯。夏天包裹失竊高峰加上很多人出門度假，一台能可靠捕捉並保存門口畫面的門鈴，是現在性價比最高的智慧家庭投資之一。",
                "highlights": [
                    {"title": "eufy E340 雙鏡頭同時顧門口和包裹", "body": "前鏡頭看訪客，向下鏡頭看你的包裹，AI 人臉與包裹偵測讓每則警報更精準。再加上 8GB 本地儲存、性價比 9.8 分、無強制訂閱，這是 2026 年最好推薦的門鈴。"},
                    {"title": "Aqara G410 是 HomeKit 重度玩家的首選", "body": "2K 全身視角、Wi-Fi 6、支援 PoE，智慧家庭整合 9.8 分全榜最高。原生 HomeKit Secure Video 加上 Apple Home Key，圍繞蘋果智慧家庭建立的人選它最順。"},
                    {"title": "本地儲存才是夏天包裹季的贏家", "body": "包裹配送暴增、家裡常沒人，能本地錄影又免訂閱的門鈴長期最划算。eufy E340、Aqara G410 等免訂閱機型都跳過了 Ring 解鎖最佳功能要收的那筆月費。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK video-doorbells")


def build_smart_thermostats():
    d, p = load("best-smart-thermostats.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Best Smart Thermostats 2026: Ecobee vs Nest vs Honeywell — Which Saves Most?", "url": "https://www.smarthomeexplorer.com/guides/best-smart-thermostat-2026", "source": "Smart Home Explorer"},
            {"title": "Ecobee and Nest lead 2026 smart thermostat rankings", "url": "https://www.msn.com/en-us/news/other/ecobee-and-nest-lead-2026-smart-thermostat-rankings/gm-GM9F89B1BC", "source": "MSN"},
            {"title": "Nest vs Ecobee (2026): Which Thermostat Saves More Money & Energy?", "url": "https://smarthomefuel.com/article/nest-vs-ecobee-comparison", "source": "SmartHomeFuel"},
        ],
        "i18n": {
            "en": {
                "commentary": "June is the single most logical month to install a smart thermostat. Summer cooling is where these devices pay for themselves fastest, because the real savings come from demand-response pre-cooling: the thermostat chills your home while electricity is cheap, then throttles back when prices spike in the hot afternoon. The Ecobee Smart Thermostat Premium holds the top spot at 9.2 overall, and I keep recommending it for the same reasons it has earned that score. It ships with a remote room sensor, adds built-in air quality monitoring, and works across Alexa, Google, Siri, and HomeKit through Matter. Its 9.5 multi-room support and 9.5 smart home integration scores reflect a thermostat that genuinely solves the hot-bedroom-cold-living-room problem most homes face in summer.\n\nThe Google Nest Learning Thermostat fourth-gen at rank 2 is the pick for buyers who want the device to do the thinking. Its 9.8 auto-scheduling score is the highest in the lineup, the OLED display with Farsight is the best-looking screen here, and its AI learns your routine without manual programming. Both leaders support Matter, so neither locks you out of future smart home expansion.\n\nA reality check worth stating plainly: while manufacturers advertise savings up to 26 percent, independent ENERGY STAR data shows the typical home saves around 8 percent, roughly 50 to 100 dollars a year. The biggest gains come from replacing a poorly managed manual thermostat. If that describes your home and you cool through a hot summer, the payback math is genuinely strong, and June is exactly when it starts working for you.",
                "highlights": [
                    {"title": "Ecobee Premium Solves the Uneven-Cooling Problem", "body": "An included remote sensor, built-in air quality monitoring, and 9.5 multi-room support make the Ecobee Smart Thermostat Premium the best answer for homes with a hot bedroom and a cold living room. Full Matter support across Alexa, Google, Siri, and HomeKit seals it as the top pick for summer."},
                    {"title": "Nest 4th-Gen Leads on Hands-Off Auto-Scheduling", "body": "A 9.8 auto-scheduling score, the highest here, plus an OLED Farsight display and AI that learns your routine make the Nest Learning Thermostat the pick for buyers who want the device to think for them. No manual programming required."},
                    {"title": "Real Summer Savings Come From Pre-Cooling", "body": "Independent ENERGY STAR data points to roughly 8 percent typical savings, with the biggest gains replacing a poorly managed manual thermostat. Demand-response pre-cooling, chilling the home while power is cheap, is where smart thermostats earn their keep through a hot summer."},
                ],
            },
            "zh-tw": {
                "commentary": "六月是裝智慧溫控器最合理的月份。夏天冷氣才是這種裝置最快回本的場景，因為真正省到的是需量反應預冷：溫控器趁電價便宜時先把家裡降溫，等到下午高溫電價飆高時再放緩運轉。\n\n榜單第一的 Ecobee Smart Thermostat Premium 總分 9.2，我一直推它的理由就是它拿到這分數的原因。它附一顆遠端房間感測器，內建空氣品質監測，透過 Matter 同時支援 Alexa、Google、Siri 和 HomeKit。多房間支援 9.5、智慧家庭整合 9.5 分，真的能解決台灣很多家庭夏天那種「房間悶熱、客廳冷到發抖」的老問題。\n\nGoogle Nest Learning Thermostat 第四代排第二，推給想讓裝置自己思考的人。自動排程 9.8 分是全榜最高，OLED 加上 Farsight 遠距顯示是這裡最好看的螢幕，AI 會自己學你的作息，不用手動排程。兩款龍頭都支援 Matter，未來擴充智慧家庭都不會被綁死。\n\n講句實話：廠商廣告打省到 26%，但獨立的 ENERGY STAR 數據顯示一般家庭大約省 8%，換算一年大概省 50 到 100 美元。最大的進步來自取代原本管得很差的手動溫控器。如果你家正是這種情況、夏天又得整季吹冷氣，回本的數學真的很漂亮，而六月正是它開始替你省錢的起點。",
                "highlights": [
                    {"title": "Ecobee Premium 解決冷房不均的老問題", "body": "附遠端感測器、內建空氣品質監測、多房間支援 9.5 分，是「房間熱、客廳冷」家庭的最佳解答。透過 Matter 全面支援 Alexa、Google、Siri、HomeKit，夏天首選坐穩。"},
                    {"title": "Nest 第四代自動排程最省心", "body": "自動排程 9.8 分全榜最高，加上 OLED Farsight 顯示和會學作息的 AI，是想讓裝置自己思考的人的選擇，完全不用手動排程。"},
                    {"title": "夏天真正省錢靠的是預冷", "body": "獨立 ENERGY STAR 數據顯示一般家庭約省 8%，最大進步來自取代管得差的手動溫控器。需量反應預冷，趁電價便宜先降溫，才是智慧溫控器整個夏天回本的關鍵。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK smart-thermostats")


def build_smart_glasses():
    d, p = load("best-smart-glasses.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Meta adds a teleprompter and EMG handwriting to the Ray-Ban Display, delays international availability", "url": "https://www.androidcentral.com/apps-software/meta/meta-ray-ban-display-updates-ces-2026", "source": "Android Central"},
            {"title": "Meta launches two new Ray-Ban glasses designed for prescription wearers", "url": "https://techcrunch.com/2026/03/31/meta-launches-two-new-ray-ban-glasses-designed-for-prescription-wearers/", "source": "TechCrunch"},
            {"title": "Meta Slated to Launch Two New Ray-Ban Smart Glasses, According to FCC Filing", "url": "https://www.roadtovr.com/meta-ray-ban-smart-glasses-2026-next-gen/", "source": "Road to VR"},
        ],
        "i18n": {
            "en": {
                "commentary": "Smart glasses are the wearable story of 2026, and Meta owns the conversation. The Ray-Ban Meta Gen 2 holds the top spot at 9.3 overall because it nails the thing that matters most in this category: it is a pair of glasses people actually want to wear all day. The 9.5 design, 9.5 ecosystem, and 9.5 value scores reflect a product where the camera, audio, and AI assistant disappear into a frame that looks like normal Ray-Bans. That, not raw spec sheets, is why this category finally went mainstream.\n\nThe Oakley Meta HSTN at rank 2 brings the same Meta platform into a sportier frame, with strong battery life and the wraparound styling that active users prefer. The 9.0 features and 9.5 ecosystem scores carry directly over from the shared Meta foundation.\n\nThe Meta Ray-Ban Display at rank 3 is the most ambitious product here, with an in-lens display and the Neural Band for EMG input. Meta is leaning in hard: at CES 2026 it added teleprompter support and virtual EMG handwriting, both rolling out now. The flip side is scarcity. Meta delayed the Display's international launch in the UK, France, Italy, and Canada, citing extremely limited inventory and unprecedented demand. That demand signal is the real headline. With Meta also shipping new prescription-focused Blayzer and Scriber frames at 499 dollars, the platform is widening fast, and a next-gen Ray-Ban Meta is expected around Meta Connect later this year. For buyers right now, the Gen 2 remains the smart, available, everyday choice.",
                "highlights": [
                    {"title": "Ray-Ban Meta Gen 2 Wins by Being Wearable All Day", "body": "9.5 design, 9.5 ecosystem, and 9.5 value scores reflect glasses where the camera, audio, and AI disappear into a frame that looks like normal Ray-Bans. That everyday wearability, not a spec sheet, is why this is the category's clear leader."},
                    {"title": "Meta Ray-Ban Display Demand Outstrips Supply", "body": "Meta delayed the Display's launch in the UK, France, Italy, and Canada, citing extremely limited inventory and unprecedented demand. New CES 2026 teleprompter and EMG handwriting features are rolling out now, underscoring how hard Meta is pushing its in-lens display platform."},
                    {"title": "Meta's Platform Is Widening Fast", "body": "New prescription-focused Blayzer and Scriber frames at 499 dollars bring the Meta platform to all-day eyewear wearers, and a next-gen Ray-Ban Meta is expected around Meta Connect this year. The ecosystem advantage keeps compounding across the lineup."},
                ],
            },
            "zh-tw": {
                "commentary": "智慧眼鏡是 2026 年穿戴裝置的主角，而話題完全由 Meta 主導。榜單第一的 Ray-Ban Meta Gen 2 總分 9.3，靠的是這個品類最關鍵的一件事：它是一副人們真的願意整天戴出門的眼鏡。設計 9.5、生態系 9.5、性價比 9.5 分，相機、音訊、AI 助理全都藏進一副看起來就是普通雷朋的鏡框裡。讓這個品類終於走進主流的，是這個，不是規格表。\n\nOakley Meta HSTN 第二名，把同一套 Meta 平台放進更運動感的鏡框，電池續航不錯，包覆式造型是運動族的最愛。功能 9.0、生態系 9.5 分，直接繼承了共用的 Meta 基礎。\n\nMeta Ray-Ban Display 第三名，是這裡最有野心的產品，鏡片內建顯示加上 Neural Band 的 EMG 輸入。Meta 押得很重：CES 2026 加入了提詞機支援和虛擬 EMG 手寫，現在都在陸續推送。另一面則是缺貨。Meta 延後了 Display 在英國、法國、義大利和加拿大的上市，理由是庫存極度有限、需求空前。這個需求訊號才是真正的重點。Meta 同時推出主打處方鏡片的 Blayzer 和 Scriber 鏡框，售價 499 美元，平台正在快速擴張，下一代 Ray-Ban Meta 預計今年 Meta Connect 前後登場。對現在就想入手的人，Gen 2 仍然是聰明、買得到、最適合日常的選擇。",
                "highlights": [
                    {"title": "Ray-Ban Meta Gen 2 靠「整天戴得住」奪冠", "body": "設計 9.5、生態系 9.5、性價比 9.5 分，相機、音訊、AI 全藏進看起來就是普通雷朋的鏡框。讓它成為品類明確龍頭的，是這種日常可戴性，不是規格表。"},
                    {"title": "Meta Ray-Ban Display 需求遠超供給", "body": "Meta 延後了 Display 在英、法、義、加的上市，理由是庫存極度有限、需求空前。CES 2026 的提詞機和 EMG 手寫功能正在推送，凸顯 Meta 對鏡片內顯示平台押得有多重。"},
                    {"title": "Meta 的平台正在快速擴張", "body": "主打處方鏡片的 Blayzer 與 Scriber 新框售價 499 美元，把 Meta 平台帶給整天戴眼鏡的人，下一代 Ray-Ban Meta 預計今年 Meta Connect 前後登場，生態系優勢持續累積。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK smart-glasses")


def build_smart_rings():
    d, p = load("best-smart-rings.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Oura Ring 5 Launches as Samsung Galaxy Ring Falls Silent: What It Means for the Smart Ring Market", "url": "https://memeburn.com/oura-ring-5-launches-as-samsung-galaxy-ring-fall/", "source": "Memeburn"},
            {"title": "Best smart ring 2026: the best from Oura, Samsung, RingConn and more", "url": "https://www.techradar.com/health-fitness/fitness-trackers/best-smart-ring", "source": "TechRadar"},
            {"title": "Best Smart Rings 2026: 6 Picks for Sleep, Fitness and Cycle Tracking", "url": "https://the-gadgeteer.com/2026/05/23/best-smart-rings-health-fitness-sleep-tracking/", "source": "The Gadgeteer"},
        ],
        "i18n": {
            "en": {
                "commentary": "The smart ring market just got its biggest shake-up of the year. Oura launched the Ring 5 on May 28, calling it the world's smallest smart ring, with shipping starting June 4. It adds blood pressure trend monitoring, nighttime breathing analysis, and a portable charging case for the first time. That is a meaningful leap, and it raises the ceiling for what this category can do, even though our rankings stay conservative until the Ring 5 has been worn and tested in the wild.\n\nFor now the Samsung Galaxy Ring holds the top spot at 8.9 overall, and it earns it on value. A 9.5 value score makes it the most accessible entry into a premium smart ring, with no subscription, solid sleep tracking, and the cleanest path into a Samsung-centric setup. With Samsung now reportedly delaying the Galaxy Ring 2 to early 2027, the current Galaxy Ring remains the value anchor of this category.\n\nThe Oura Ring 4 sits at rank 2, also at 8.9, and it remains the gold standard for tracking depth. A 9.5 sleep tracking, 9.5 health features, and 9.5 app experience score reflect the most polished data and guidance in the category. The Ring 5 builds directly on this foundation, so the Oura platform is only getting stronger.\n\nThe RingConn Gen 2 at rank 3 is the battery champion at 9.5, pairing a multi-day charge with a 9.5 value score and no subscription. For buyers who want the smart ring experience without a recurring fee or nightly charging anxiety, it remains the practical pick. The takeaway: the platform you buy into matters more than ever, and all three leaders give you a strong, subscription-aware path.",
                "highlights": [
                    {"title": "Oura Ring 5 Resets the Category Ceiling", "body": "Launched May 28 and shipping June 4, the Ring 5 is billed as the world's smallest smart ring, adding blood pressure trend monitoring, nighttime breathing analysis, and a first-ever portable charging case. Our rankings stay conservative pending real-world testing, but the Oura platform clearly just got stronger."},
                    {"title": "Samsung Galaxy Ring Holds the Value Crown", "body": "A 9.5 value score makes the Galaxy Ring the most accessible premium smart ring, with no subscription and clean Samsung integration. With the Galaxy Ring 2 reportedly pushed to early 2027, this remains the category's value anchor."},
                    {"title": "RingConn Gen 2 Wins on Battery and No Fees", "body": "A 9.5 battery score and multi-day charge pair with a 9.5 value score and no subscription. For buyers who want smart ring health tracking without a recurring fee or nightly charging anxiety, it is the most practical pick on the list."},
                ],
            },
            "zh-tw": {
                "commentary": "智慧戒指市場剛迎來今年最大的洗牌。Oura 在 5 月 28 日推出 Ring 5，號稱世界最小的智慧戒指，6 月 4 日開始出貨。它加入血壓趨勢監測、夜間呼吸分析，還首度附上可攜式充電盒。這是個有意義的飛躍，把這個品類的天花板再往上推，不過在 Ring 5 真正被戴上手實測之前，我們的排名先保持保守。\n\n目前榜單第一仍是 Samsung Galaxy Ring，總分 8.9，靠的是性價比。9.5 的性價比分讓它成為進入高階智慧戒指最親民的選擇，免訂閱、睡眠追蹤扎實，又是進入 Samsung 生態系最順的路徑。Samsung 現在傳出把 Galaxy Ring 2 延到 2027 年初，現役的 Galaxy Ring 仍是這個品類的性價比定錨。\n\nOura Ring 4 排第二，同樣 8.9 分，依舊是追蹤深度的黃金標準。睡眠追蹤 9.5、健康功能 9.5、App 體驗 9.5 分，數據和指引都是這個品類最細膩的。Ring 5 正是直接建立在這個基礎上，所以 Oura 平台只會越來越強。\n\nRingConn Gen 2 第三名，是電池冠軍 9.5 分，多天續航搭配 9.5 性價比，免訂閱。想要智慧戒指體驗但不想被月費綁住、又不想每晚擔心充電的人，它仍然是務實的選擇。結論是：你買進哪個平台比以往更重要，而這三個龍頭都給了你一條扎實又考慮到訂閱負擔的路。",
                "highlights": [
                    {"title": "Oura Ring 5 重設品類天花板", "body": "5 月 28 日發表、6 月 4 日出貨，號稱世界最小智慧戒指，加入血壓趨勢監測、夜間呼吸分析和史上首見的可攜充電盒。排名待實測前保持保守，但 Oura 平台顯然又變更強了。"},
                    {"title": "Samsung Galaxy Ring 坐穩性價比王座", "body": "性價比 9.5 分讓 Galaxy Ring 成為最親民的高階智慧戒指，免訂閱、Samsung 整合順暢。Galaxy Ring 2 傳出延到 2027 年初，這款仍是品類的性價比定錨。"},
                    {"title": "RingConn Gen 2 靠電池與免月費取勝", "body": "電池 9.5 分、多天續航，搭配 9.5 性價比、免訂閱。想要智慧戒指健康追蹤又不想被月費綁住、不想每晚擔心充電的人，這是榜上最務實的選擇。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK smart-rings")


def build_smart_watches():
    d, p = load("best-smart-watches.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "The best smartwatches in 2026: Options for every budget", "url": "https://www.wareable.com/smartwatches/best-smartwatch-reviews-compared-8286", "source": "Wareable"},
            {"title": "The best smartwatch 2026: Wearables and fitness watches to buy", "url": "https://www.techradar.com/news/wearables/best-smart-watches-what-s-the-best-wearable-tech-for-you-1154074", "source": "TechRadar"},
            {"title": "Best Smartwatches of 2026: Our Editors' Top Tested Picks", "url": "https://www.nbcnews.com/select/shopping/best-smartwatches-rcna248847", "source": "NBC Select"},
        ],
        "i18n": {
            "en": {
                "commentary": "The smartwatch market in 2026 has settled into three clear paths: the do-it-all ecosystem watch, the long-lasting dedicated fitness tool, and the budget health tracker. Knowing which one you want makes the choice easy, and our top three map directly onto the first two paths. The Apple Watch Ultra 3 holds the top spot at 9.4 overall because it is the most complete wearable Apple has built. A 9.5 health score, 9.5 display, and 9.5 ecosystem reflect a watch that does everything for an iPhone owner, from advanced health sensing to genuinely useful battery life in a flagship body. For iPhone users who want the best, this is it.\n\nThe Apple Watch Ultra 2 at rank 2 remains a smart buy at 9.3, delivering nearly the same experience at a now-lower price as the Ultra 3 takes the spotlight. The 9.5 health and 9.5 ecosystem scores carry over intact, and the 8.5 battery is still excellent. If you want the Ultra experience for less, this is the value move within the Apple lineup.\n\nThe Garmin Fenix 8 at rank 3 owns the dedicated fitness path. A 9.5 health score and a category-leading 9.5 battery score reflect a watch built for athletes who measure runtime in weeks, not days. For trail runners, hikers, and anyone who prioritizes endurance and training depth over app ecosystems, the Fenix 8 is the clear pick. The newer Venu X1 and Venu 4 expand Garmin's reach into sleeker territory, with the Venu 4 hitting up to five days with an always-on display. Across all three leaders, the pattern holds: pick your path, and the right watch is obvious.",
                "highlights": [
                    {"title": "Apple Watch Ultra 3 Is the Most Complete iPhone Wearable", "body": "A 9.5 health score, 9.5 display, and 9.5 ecosystem make the Ultra 3 the do-it-all flagship for iPhone owners. Advanced health sensing and strong flagship battery life put it at the top of the lineup without compromise."},
                    {"title": "Apple Watch Ultra 2 Is the Value Move in Apple's Range", "body": "At 9.3 overall, the Ultra 2 delivers nearly the same 9.5 health and 9.5 ecosystem experience at a now-lower price as the Ultra 3 takes the spotlight. For buyers who want the Ultra feel for less, this is the smart pick."},
                    {"title": "Garmin Fenix 8 Owns the Endurance Path", "body": "A 9.5 health score and category-leading 9.5 battery measure runtime in weeks, not days. For trail runners, hikers, and athletes who prioritize training depth and endurance over app ecosystems, the Fenix 8 is the definitive choice."},
                ],
            },
            "zh-tw": {
                "commentary": "2026 年的智慧手錶市場已經分成三條清楚的路線：全能生態系手錶、續航超長的專業運動工具，以及平價健康追蹤器。先想清楚你要哪一種，選擇就變得很簡單，而我們的前三名剛好對應前兩條路線。\n\n榜單第一的 Apple Watch Ultra 3 總分 9.4，因為它是 Apple 做過最完整的穿戴裝置。健康 9.5、顯示 9.5、生態系 9.5 分，對 iPhone 用戶來說它什麼都能做，從進階健康感測到旗艦機身裡真的夠用的續航。iPhone 用戶想要最好的，就是它。\n\nApple Watch Ultra 2 排第二，9.3 分仍是聰明的選擇。當 Ultra 3 接棒鎂光燈後，它用現在更低的價格給你幾乎一樣的體驗。健康 9.5、生態系 9.5 完整保留，8.5 的電池依然優秀。想要 Ultra 體驗但花更少錢，這就是 Apple 陣容裡的性價比之選。\n\nGarmin Fenix 8 第三名，獨占專業運動這條路。健康 9.5 分加上全榜最高的電池 9.5 分，這是一支續航用「週」算而不是用「天」算的手錶。越野跑者、登山客，還有任何把續航和訓練深度看得比 App 生態系更重的人，Fenix 8 是明確的選擇。較新的 Venu X1 和 Venu 4 把 Garmin 拓展到更輕薄的領域，Venu 4 開啟常亮顯示也能撐到五天。三個龍頭一致的道理是：選好你的路線，對的手錶就很明顯了。",
                "highlights": [
                    {"title": "Apple Watch Ultra 3 是最完整的 iPhone 穿戴裝置", "body": "健康 9.5、顯示 9.5、生態系 9.5 分，Ultra 3 是 iPhone 用戶的全能旗艦。進階健康感測加上扎實的旗艦續航，讓它毫不妥協地坐穩榜首。"},
                    {"title": "Apple Watch Ultra 2 是 Apple 陣容的性價比之選", "body": "總分 9.3，當 Ultra 3 接棒後，它用更低價格給你幾乎一樣的健康 9.5、生態系 9.5 體驗。想要 Ultra 手感又想省一點的人，這是聰明選擇。"},
                    {"title": "Garmin Fenix 8 獨占續航路線", "body": "健康 9.5 分加上全榜最高的電池 9.5 分，續航用週算而非用天算。越野跑者、登山客，以及把訓練深度和續航看得比 App 生態系更重的人，Fenix 8 是不二之選。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK smart-watches")


def build_mesh_wifi():
    d, p = load("best-mesh-wifi-systems.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "The 4 Best Mesh Wi-Fi Systems of 2026", "url": "https://www.rtings.com/router/reviews/best/mesh-wifi-system", "source": "RTINGS"},
            {"title": "Best Wi-Fi 7 Mesh Systems (2026): UniFi vs TP-Link vs Eero", "url": "https://datawiresolutions.com/blog/best-wifi-7-mesh-systems", "source": "Data Wire Solutions"},
            {"title": "Best Mesh WiFi Systems in 2026: Top 10 Compared (Specs, Speeds, Price)", "url": "https://www.modemguides.com/blogs/modemguides-blog/best-mesh-wifi-systems-compared", "source": "Modem Guides"},
        ],
        "i18n": {
            "en": {
                "commentary": "Wi-Fi 7 is now the default standard for mesh in 2026, and the category has matured to the point where you can pick by priority rather than compromise. The ASUS ZenWiFi BQ16 Pro holds the top spot at 8.9 overall on the strength of raw performance and a no-subscription feature set. Its 9.8 performance and 9.5 coverage scores reflect a tri-band Wi-Fi 7 system that simply moves data faster, and crucially, every feature including AiProtection Pro, parental controls, and a VPN server is free for life. For power users who refuse recurring fees, this is the system to beat.\n\nThe TP-Link Deco BE63 at rank 2 is the value champion, and it is the system I recommend to most homes. A 9.5 value score backs a tri-band Wi-Fi 7 mesh that handles 200-plus devices and covers up to 7,600 square feet, starting around 270 dollars for a two-pack. Independent testing puts its real-world speeds within a hair of pricier rivals. For the typical 1 to 2.5 Gbps home, this is the smart-money pick.\n\nThe eero Pro 7 at rank 3 wins on simplicity. A 9.5 usability and 9.5 features score reflect the cleanest app-led setup in the category, with built-in Thread and Matter support that makes it a natural smart home hub. For households that value a system that just works over one they can tune endlessly, the eero is the answer. With more devices joining home networks every month and summer streaming loads climbing, upgrading to a Wi-Fi 7 mesh now is one of the most quietly impactful home tech moves you can make.",
                "highlights": [
                    {"title": "ASUS ZenWiFi BQ16 Pro Leads on Raw Speed and No Fees", "body": "A 9.8 performance and 9.5 coverage score back a tri-band Wi-Fi 7 system where every feature, including AiProtection Pro, parental controls, and a VPN server, is free for life. For power users who refuse subscriptions, it is the system to beat."},
                    {"title": "TP-Link Deco BE63 Is the Smart-Money Wi-Fi 7 Pick", "body": "A 9.5 value score, 200-plus device support, and coverage up to 7,600 square feet from around 270 dollars for a two-pack. Independent testing puts its real-world speed within a hair of pricier rivals, making it the best buy for most 1 to 2.5 Gbps homes."},
                    {"title": "eero Pro 7 Wins on Simplicity and Smart Home Integration", "body": "A 9.5 usability and 9.5 features score reflect the cleanest app-led setup in the category, with built-in Thread and Matter turning it into a natural smart home hub. For households that want a system that just works, this is the answer."},
                ],
            },
            "zh-tw": {
                "commentary": "Wi-Fi 7 在 2026 年已經是 mesh 的預設標準，這個品類成熟到你可以照需求挑，而不用妥協。\n\n榜單第一的 ASUS ZenWiFi BQ16 Pro 總分 8.9，靠的是純效能加上免訂閱的功能組合。效能 9.8、覆蓋 9.5 分，是一套單純把資料傳得更快的三頻 Wi-Fi 7 系統，而且最關鍵的是，包含 AiProtection Pro、家長控制、VPN 伺服器在內的所有功能終身免費。重度使用者只要拒絕月費，這就是要被超越的標竿。\n\nTP-Link Deco BE63 第二名，是性價比冠軍，也是我推給多數家庭的系統。性價比 9.5 分撐起一套能掛 200 多台裝置、覆蓋多達 7,600 平方英尺的三頻 Wi-Fi 7 mesh，兩入組約 270 美元起。獨立測試顯示它的實際速度跟更貴的對手只差一點點。對一般 1 到 2.5 Gbps 的家庭，這就是聰明錢的選擇。\n\neero Pro 7 第三名，靠的是簡單。易用性 9.5、功能 9.5 分，是這個品類最乾淨的 App 主導設定，內建 Thread 和 Matter 支援，自然就是一個智慧家庭中樞。比起一套可以無止盡調校的系統，更看重「裝好就能用」的家庭，eero 就是答案。家裡連網裝置每個月都在增加，夏天串流負載又往上爬，現在升級到 Wi-Fi 7 mesh，是你能做的最低調卻最有感的居家科技升級之一。",
                "highlights": [
                    {"title": "ASUS ZenWiFi BQ16 Pro 純速度加免月費領先", "body": "效能 9.8、覆蓋 9.5 分撐起一套三頻 Wi-Fi 7 系統，AiProtection Pro、家長控制、VPN 伺服器等所有功能終身免費。拒絕訂閱的重度使用者，這就是要被超越的標竿。"},
                    {"title": "TP-Link Deco BE63 是聰明錢的 Wi-Fi 7 選擇", "body": "性價比 9.5 分，支援 200 多台裝置，覆蓋多達 7,600 平方英尺，兩入組約 270 美元起。獨立測試顯示實際速度跟更貴對手只差一點點，是多數 1 到 2.5 Gbps 家庭的最佳買點。"},
                    {"title": "eero Pro 7 靠簡單與智慧家庭整合取勝", "body": "易用性 9.5、功能 9.5 分，是品類最乾淨的 App 主導設定，內建 Thread 和 Matter 讓它自然成為智慧家庭中樞。想要裝好就能用的家庭，這就是答案。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK mesh-wifi-systems")


if __name__ == "__main__":
    build_security_cameras()
    build_video_doorbells()
    build_smart_thermostats()
    build_smart_glasses()
    build_smart_rings()
    build_smart_watches()
    build_mesh_wifi()
    print("Batch 6 complete")
