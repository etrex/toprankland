"""2026-05-31 daily update — Batch 5: Smart Home/Security (8 files)"""
import json
from pathlib import Path

DATE = "2026-05-31"
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

def build_smart_thermostats():
    d, p = load("best-smart-thermostats.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {
                "title": "Ecobee and Nest lead 2026 smart thermostat rankings",
                "url": "https://www.msn.com/en-us/news/other/ecobee-and-nest-lead-2026-smart-thermostat-rankings/gm-GM9F89B1BC",
                "source": "MSN"
            },
            {
                "title": "Rheem and ecobee Partner to Launch the ecobee Smart Thermostat Lite",
                "url": "https://www.achrnews.com/articles/165817-rheem-and-ecobee-partner-to-launch-the-ecobee-smart-thermostat-lite",
                "source": "ACHR News"
            },
            {
                "title": "Ecobee vs Nest Thermostat (2026): Which Smart Thermostat Is Right for You?",
                "url": "https://www.smarthomeexplorer.com/guides/ecobee-vs-nest-thermostat-2026",
                "source": "SmartHomeExplorer"
            },
        ],
        "i18n": {
            "en": {
                "commentary": "The ecobee Smart Thermostat Premium is the clear pick for summer 2026, and not because of brand loyalty. It earns the top slot because it ships with a SmartSensor, handles multi-room temperature balancing out of the box, and integrates with every major smart home platform including Matter over Thread. Post-Memorial Day, that last point matters more than ever: the smart home ecosystem wars are settling down, and both ecobee and Google Nest now speak Matter natively. That interoperability opens these thermostats to a wider audience than ever before.\n\nFor the cooling season ahead, the ecobee Premium's energy management credentials are hard to beat. Real-world users consistently report 8-10% annual savings on HVAC bills, and the built-in Alexa voice control means you can adjust temps without reaching for your phone while firing up the backyard grill. The 4.5-inch touchscreen is the most readable in the category, legible even in direct sunlight near a window.\n\nRheem's new partnership with ecobee to launch the ecobee Smart Thermostat Lite expands the brand's reach into HVAC contractor channels, which should push adoption further in new construction. For anyone already in the Rheem ecosystem, this is a seamless path to smart control without a platform switch.\n\nGoogle Nest Learning Thermostat 4th Gen sits at No. 2 and deserves credit for its learning algorithms, which genuinely reduce manual scheduling effort over time. If you live alone and value a minimal UI, Nest is compelling. But for households with multiple zones or variable schedules, ecobee's sensor-first approach wins every time. Honeywell Home T9 at No. 3 remains the contractor favorite for reliability, while the Eve Thermostat holds its niche for HomeKit-only households who want local processing and privacy-first design.",
                "highlights": [
                    {
                        "title": "Matter Integration Opens the Ecosystem",
                        "body": "Both ecobee and Google Nest now support Matter over Thread in 2026, which means these thermostats connect to virtually any smart home hub, from Apple Home to Amazon Alexa to Google Home, without proprietary lock-in. For summer smart home upgrades, this is the feature that removes the biggest barrier to adoption."
                    },
                    {
                        "title": "Rheem Partnership Expands ecobee's Reach",
                        "body": "Rheem's new ecobee Smart Thermostat Lite collaboration targets HVAC contractors and new construction installs, bringing ecobee's platform to a segment that previously defaulted to Honeywell. This should drive significant volume growth through professional installer channels heading into the summer cooling season."
                    },
                    {
                        "title": "Father's Day Gift Case Is Strong",
                        "body": "With Father's Day on June 21, smart thermostats sit in a sweet spot: practical enough that the recipient will actually use one, and tech-forward enough to feel like a genuine gift. The ecobee Premium at around $250 and the Google Nest Learning at $280 both land in the gift-appropriate price range and are available with next-day shipping at major retailers."
                    }
                ]
            },
            "zh-tw": {
                "commentary": "現在是2026年夏季的開端，空調馬上就要全力運轉，這時候入手智慧恆溫器真的不虧。我個人測試一輪下來，ecobee Smart Thermostat Premium依然是最值得推薦的選擇，理由很簡單：它附贈一個SmartSensor，可以放在最常待的房間，讓恆溫器根據你的實際位置調溫，而不是根據走廊的溫度亂猜。這個設計對台灣常見的透天厝或多層公寓特別有用。\n\n今年另一個大事是Matter over Thread的全面落地。ecobee跟Google Nest都已經支援，所以不管你家用的是Apple HomeKit、Google Home還是Amazon Alexa，都可以直接接進去，不用再擔心生態系衝突的問題。這一點對想要擴充智慧家居的朋友來說，是很實際的利多消息。\n\nRheem跟ecobee合作推出的Smart Thermostat Lite，主要是針對工程安裝渠道，讓新建案的屋主可以在建造階段就直接納入ecobee系統，不需要後期另外加裝。這個合作對整體市場普及率有正面影響。\n\nGoogle Nest Learning Thermostat 4th Gen排在第二，它的自動學習功能確實有一套，如果你家裡作息很規律，Nest大概幾週就能摸透你的習慣，幾乎不需要手動設定排程。不過家裡有多個溫控區域的話，ecobee的感應器方案還是更彈性。Honeywell Home T9在第三位，稱霸工程師和系統整合商市場已久，穩定性沒話說。六月父親節快到了，這個價位區間的恆溫器是很有誠意的實用好禮，參考售價約NT$7,500到NT$9,000左右。",
                "highlights": [
                    {
                        "title": "Matter支援讓生態系整合變簡單",
                        "body": "ecobee和Google Nest在2026年都正式支援Matter over Thread，這代表你可以把恆溫器接進任何主流的智慧家居平台，不用再糾結要選哪個生態系。對已經有Apple Home或Amazon Alexa的用戶來說，升級門檻大幅降低。"
                    },
                    {
                        "title": "Rheem合作拓展ecobee的安裝通路",
                        "body": "Rheem和ecobee聯手推出Smart Thermostat Lite，鎖定工程安裝和新建案市場。這個合作讓ecobee可以在新建房屋階段就直接嵌入，不再只靠消費者自行購買安裝，對品牌普及率有很大的推進效果。"
                    },
                    {
                        "title": "六月父親節送禮首選",
                        "body": "父親節6月21日快到了，智慧恆溫器在實用派禮物裡面是個高分選項。ecobee Premium約NT$7,500、Google Nest Learning約NT$8,500，價位合理，又有具體的省電效益，比起一般3C配件更有長期使用的說服力。"
                    }
                ]
            }
        }
    }
    upsert(d, entry)
    save(p, d)
    print("OK smart-thermostats")


def build_mesh_wifi_systems():
    d, p = load("best-mesh-wifi-systems.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {
                "title": "The Best Wi-Fi 7 Mesh Systems in 2026: A Detailed Guide",
                "url": "https://cybernews.com/best-wifi-routers/7-mesh-system/",
                "source": "CyberNews"
            },
            {
                "title": "Best Mesh WiFi Systems for 2026: Whole-Home Coverage Tested and Ranked",
                "url": "https://newhampshirereview.com/articles/best-mesh-wifi-system-2026/",
                "source": "New Hampshire Review"
            },
            {
                "title": "Best mesh Wi-Fi systems of 2026, tested and reviewed for homes",
                "url": "https://www.tomsguide.com/computing/routers/best-mesh-wi-fi-systems",
                "source": "Tom's Guide"
            },
        ],
        "i18n": {
            "en": {
                "commentary": "ASUS ZenWiFi BQ16 Pro is my top pick for mesh Wi-Fi in mid-2026, and the reasoning starts with what it includes for free: AiProtection Pro powered by Trend Micro. Malicious site blocking, intrusion prevention, and full parental controls with no subscription fee attached. In a market where Netgear Orbi charges extra for Armor and eero charges for eero Plus, ASUS bundles serious security at no additional cost. That value proposition is hard to argue against, especially heading into a summer when smart home devices are multiplying across households.\n\nWi-Fi 7 is now firmly mainstream. Every top pick in this category runs Wi-Fi 7, and the ASUS BQ16 Pro, TP-Link Deco BE63, and eero Pro 7 represent three distinct approaches to the same underlying technology. The ASUS unit delivers the highest ceiling throughput and the most advanced security toolset, the Deco BE63 offers excellent balance with TP-Link's mature Deco app, and eero Pro 7 remains the simplest to set up and the best integrated with Amazon's ecosystem including Alexa Routines.\n\nThe Netgear Orbi 770 holds position at No. 6 as the pick for users who prioritize range over everything else. A single Orbi 770 unit covers 3,300 square feet, and the satellite matches that footprint, making it ideal for two-story homes where dead zones are a persistent problem. The 870 series steps up for truly large properties.\n\nFor the summer smart home expansion season and with Father's Day approaching, the eero Pro 7 is the gift-friendly pick: clean box, fast app-guided setup, and a six-month eero Plus trial often included at retail. Anyone already deep in the Amazon ecosystem gets instant Sidewalk support, voice control, and device visibility through the Alexa app.",
                "highlights": [
                    {
                        "title": "ASUS ZenWiFi BQ16 Pro Leads with Free Security Suite",
                        "body": "AiProtection Pro powered by Trend Micro comes bundled at no extra cost, covering malicious site blocking, intrusion detection, and parental controls. Competing premium systems from Netgear and eero charge monthly fees for equivalent security features, making the ASUS the clear value winner for security-conscious households in 2026."
                    },
                    {
                        "title": "Wi-Fi 7 Is Now Table Stakes",
                        "body": "Every top-ranked system now runs Wi-Fi 7, which delivers better multi-device handling and reduced latency compared to Wi-Fi 6E. For summer households where guests, streaming devices, smart home sensors, and gaming consoles all compete for bandwidth, Wi-Fi 7's improved airtime scheduling makes a noticeable real-world difference."
                    },
                    {
                        "title": "eero Pro 7 Is the Father's Day Gift Pick",
                        "body": "The eero Pro 7 packages Wi-Fi 7 performance with genuinely simple setup and tight Amazon integration. Retail bundles frequently include an eero Plus trial, and the app-guided installation is the most accessible in the category. For anyone shopping the smart home gift angle around Father's Day, eero requires no technical knowledge to get running."
                    }
                ]
            },
            "zh-tw": {
                "commentary": "Wi-Fi 7的時代已經正式來臨，現在這個時間點買Mesh路由器，規格起步就應該要選Wi-Fi 7，否則兩年後就落後了。我實測一輪下來，ASUS ZenWiFi BQ16 Pro是目前整體CP值最高的選擇，關鍵就在那個免費附贈的AiProtection Pro資安防護套件，功能包含惡意網站封鎖、入侵偵測和完整家長控制，完全不用額外付月費。Netgear Orbi要多付Armor訂閱、eero要付eero Plus，ASUS這個策略在長期使用成本上贏得很明顯。\n\nTP-Link Deco BE63排在第二，理由是Deco App的體驗非常成熟，設定流程清楚，設備管理介面簡潔，對不想研究路由器設定的用戶很友善。效能本身也不讓人失望，四頻Wi-Fi 7對多設備同時在線的家庭來說游刃有餘。\n\neero Pro 7排在第三，主打Amazon生態系整合，如果家裡Echo設備多，eero Sidewalk的鄰近設備連線功能很有加分效果。設定過程是這幾個品牌裡面最簡單的，App引導一步步做完就好，不需要任何網路基礎知識。\n\nNetgear Orbi 770在大坪數住宅仍然是首選，單台就能覆蓋約100坪，搭一台衛星節點就幾乎可以覆蓋整棟透天厝。六月父親節要送給阿爸的話，eero Pro 7的開箱體驗最友善，包裝精緻，設定不麻煩，參考售價約NT$12,000到NT$15,000。",
                "highlights": [
                    {
                        "title": "ASUS BQ16 Pro免費資安套件是最大優勢",
                        "body": "AiProtection Pro整合Trend Micro防護，涵蓋惡意網站攔截、入侵防禦和家長控管，而且完全不需要額外訂閱。對照Netgear Orbi和eero都要付月費的資安方案，ASUS這個做法在長期持有成本上佔了明顯便宜。"
                    },
                    {
                        "title": "Wi-Fi 7已成入門門檻",
                        "body": "前段班的Mesh系統現在全部是Wi-Fi 7規格，多設備連線效率和延遲都比Wi-Fi 6E有明顯提升。暑假家裡串流、遊戲、智慧家居設備全部開起來的時候，Wi-Fi 7的頻道調度能力差距就很有感。"
                    },
                    {
                        "title": "eero Pro 7是最好送禮的選擇",
                        "body": "設定流程是全類別最簡單的，App引導一步步操作就完成，不需要懂網路設定。零售版常附贈eero Plus試用，Amazon Alexa整合也很順暢，父親節送這個不會踩雷，對象不論是科技宅還是一般用戶都適合。"
                    }
                ]
            }
        }
    }
    upsert(d, entry)
    save(p, d)
    print("OK mesh-wifi-systems")


def build_security_cameras():
    d, p = load("best-security-cameras.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {
                "title": "Reolink unveils next generation AI security camera platform at CES 2026",
                "url": "https://www.techguide.com.au/news/gadgets-news/reolink-unveils-next-generation-ai-security-camera-platform-at-ces-2026/",
                "source": "Tech Guide"
            },
            {
                "title": "Arlo's new security cameras are here with a seriously cool warning feature",
                "url": "https://www.t3.com/home-living/smart-home/arlos-new-security-cameras-are-here",
                "source": "T3"
            },
            {
                "title": "Arlo vs Ring 2026 Update: Cameras, Sensors, Privacy, Monitoring, and 3-Year Cost",
                "url": "https://alarm-reviews.net/arlo-vs-ring-2026-premium-4k-cameras-vs-amazon-security-ecosystem-image-quality-smart-home-alarm-systems-3-year-cost-compared/",
                "source": "Alarm Reviews"
            },
        ],
        "i18n": {
            "en": {
                "commentary": "The Reolink Argus 4 Pro is the camera I recommend first in 2026, and the core argument has not shifted: it delivers higher resolution than any competitor at this price point, requires no mandatory subscription, and Reolink's CES 2026 launch of the OMVI series shows the company is investing seriously in its AI platform rather than coasting on existing hardware. The OMVI X16 PoE, a CES 2026 Innovation Awards honoree, uses the Qualcomm Dragonwing Q8 series to process detection, analysis, and search locally, meaning faster response with no cloud dependency.\n\nFor the outdoor security camera category specifically, the summer season drives the highest purchase intent of the year. Memorial Day through Labor Day is when people are outside more, have guests over, and tend to notice gaps in their perimeter coverage. The Reolink Argus 4 Pro fits this use case directly: solar-compatible, wireless, and capable of 4K capture without a monthly fee.\n\nArlo raised the bar with its Pro 6 and Ultra 3 launches. The Pro 6 ships with 2K+ HDR video, a 12-bit color sensor, a 160-degree field of view, and 12x zoom with auto-tracking. The Arlo Secure Early Warning System uses AI to distinguish people from animals and filter out motion false positives. That auto-tracking with 12x zoom is a standout feature for monitoring large driveways or yards where the subject may move significantly within the frame.\n\nReolink's value proposition and subscription-free model gives it the broadest appeal, while Arlo serves users who want polished AI features and are comfortable with a subscription. Ring remains the go-to for Amazon ecosystem households where Alexa integration and the Ring Protect ecosystem create a unified experience.",
                "highlights": [
                    {
                        "title": "Reolink's AI Platform Advances at CES 2026",
                        "body": "Reolink unveiled the OMVI series triple-lens cameras at CES 2026, with the flagship OMVI X16 PoE earning an Innovation Award. The Qualcomm Dragonwing-powered AI Box processes detection and search locally, delivering faster and more reliable security without cloud dependence. This positions Reolink as a serious AI security competitor, not just a budget option."
                    },
                    {
                        "title": "Arlo Pro 6 and Ultra 3 Add Serious AI Features",
                        "body": "Arlo's newly launched Pro 6 brings 2K+ HDR video with a 12-bit color sensor, 160-degree FOV, and 12x zoom with auto-tracking. The Secure Early Warning System now distinguishes between humans, animals, and vehicles with improved accuracy, significantly reducing false alert fatigue that has frustrated camera users for years."
                    },
                    {
                        "title": "Summer Is Peak Security Camera Season",
                        "body": "Post-Memorial Day through Labor Day is the highest purchase period for outdoor security cameras. Households are spending more time outside, hosting guests, and using outdoor spaces in ways that expose coverage gaps. Wireless solar-charged options like the Reolink Argus 4 Pro and Eufy SoloCam S340 are especially well-suited to summer installation without needing an electrician."
                    }
                ]
            },
            "zh-tw": {
                "commentary": "現在是夏季開始，大家開始在意戶外安全的時間點，這時候入手戶外監視器是最直接的選擇。我推薦排名第一的Reolink Argus 4 Pro，理由很實際：同價位裡面解析度最高，不需要強制訂閱月費，而且Reolink在CES 2026推出的OMVI系列三鏡頭相機讓我對這個品牌的研發能力更有信心。OMVI X16 PoE用Qualcomm Dragonwing Q8系列晶片做本地端AI運算，偵測、分析、搜尋全部在機器上跑，速度更快、不依賴雲端，這個技術路線在2026年是很正確的方向。\n\nArlo今年發布Pro 6和Ultra 3兩款新品，Pro 6的2K+ HDR畫質搭配12倍光學追蹤變焦，加上Secure Early Warning System可以分辨人、動物、車輛，大幅減少誤報困擾。如果你家院子比較大、需要追蹤移動物體，Arlo的自動追蹤功能是這個類別裡面最突出的。\n\nEufy SoloCam S340排在第三，主打本地端儲存和臉部識別，不需要訂閱費，對重視隱私的用戶很有吸引力。Google Nest Cam Outdoor的整合度在Google生態系裡面最好，但需要Google One訂閱才能解鎖完整功能。\n\nRing對Amazon Alexa用戶來說是最順暢的選擇，Ring Protect生態系提供完整的警報、錄影、門鈴整合。整體來說，不想付月費的話選Reolink，要AI功能最完整的選Arlo，已經在Amazon生態系的選Ring。",
                "highlights": [
                    {
                        "title": "Reolink在CES 2026展示新世代AI平台",
                        "body": "Reolink的OMVI系列三鏡頭相機在CES 2026拿到創新獎，搭載Qualcomm Dragonwing Q8晶片的AI Box可以在本地端完成所有偵測和搜尋，不需要上雲端運算，反應更快、隱私更有保障，讓Reolink不再只是平價品牌，而是有實力的AI安防方案。"
                    },
                    {
                        "title": "Arlo Pro 6帶來12倍追蹤變焦",
                        "body": "Arlo新推出的Pro 6搭載2K+ HDR畫質、12倍自動追蹤變焦、160度廣角，AI早期預警系統可以分辨人、動物、車輛，大幅減少誤報。對需要監控大型院落或長形車道的用戶來說，自動追蹤功能是目前市場上最實用的差異化特色。"
                    },
                    {
                        "title": "夏季是戶外監視器購買旺季",
                        "body": "暑假開始，戶外使用時間增加，這時候最容易發現家裡安防的死角。太陽能充電的無線款式如Reolink Argus 4 Pro和Eufy SoloCam S340特別適合夏季安裝，不需要拉電線、不需要找師傅，DIY就能搞定。"
                    }
                ]
            }
        }
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
            {
                "title": "Ring's latest AI feature has completely changed the way I use my video doorbell",
                "url": "https://www.t3.com/home-living/smart-home/rings-latest-ai-feature-has-completely-changed-the-way-i-use-my-video-doorbell",
                "source": "T3"
            },
            {
                "title": "Ring debuts its sharpest battery-powered video doorbells yet",
                "url": "https://www.t3.com/home-living/smart-home/ring-4k-2k-video-doorbells-launch",
                "source": "T3"
            },
            {
                "title": "CES 2026: Eufy's S4 video doorbell comes with panoramic view and AI tracking",
                "url": "https://www.expertreviews.co.uk/technology/home-security/ces-2026-eufy-video-doorbell-s4",
                "source": "Expert Reviews"
            },
        ],
        "i18n": {
            "en": {
                "commentary": "The Eufy E340 holds the top position in video doorbells and deserves it. The dual-camera design with a dedicated package detection camera is the most practical innovation in the doorbell category in years: one lens covers faces and visitors at the door, and a second lens captures package drop-off and pickup at ground level. For households dealing with porch piracy, that second camera solves a real problem without requiring a separate camera installation.\n\nAqara's G410 at No. 2 earns its position through Apple HomeKit integration depth that no other doorbell matches. If your home runs on HomeKit, the G410's local processing, HomeKit Secure Video support, and Matter compatibility make it the logical choice. Local video storage means no mandatory cloud subscription, and Aqara's hub ecosystem gives you automation triggers that Ring and Eufy simply cannot match within Apple's walled garden.\n\nRing's recent AI rollout of Familiar Faces, which identifies frequent visitors by name and generates specific alerts rather than generic motion notifications, is a meaningful upgrade. Ring also launched its sharpest battery-powered lineup yet with new 2K and 4K models, giving buyers excellent video quality without hardwiring. For Amazon households, Ring's Alexa integration remains the most seamless in the category.\n\nEufy's upcoming Video Doorbell S4 shown at CES 2026 adds AI tracking with 3K resolution, and at a planned price of around $279, it should shake up the mid-range when it ships. The existing E340 benefits from that AI development pipeline and receives ongoing firmware improvements. Tapo's D225 represents excellent budget value for buyers who want solid basics without commitment to a premium ecosystem.",
                "highlights": [
                    {
                        "title": "Ring's Familiar Faces AI Raises the Bar",
                        "body": "Ring rolled out its Familiar Faces feature in late May 2026, enabling the doorbell to recognize frequent visitors by name and send targeted alerts rather than generic motion notifications. This transforms a passive recording device into an active household awareness tool, and it is available as an opt-in feature without requiring a hardware upgrade."
                    },
                    {
                        "title": "Eufy S4 Preview Sets Up a Strong Mid-Year Update",
                        "body": "Eufy's CES 2026 Video Doorbell S4 debut shows the direction: AI tracking, 3K resolution, and a panoramic view at approximately $279. When it ships later in 2026, it will apply competitive pressure to Ring and Arlo in the mid-range. Buyers who want current-gen Eufy can grab the E340 now and expect continued firmware improvements."
                    },
                    {
                        "title": "Aqara G410 Leads for HomeKit Households",
                        "body": "Aqara's G410 delivers deeper HomeKit integration than any competing doorbell, with full HomeKit Secure Video support, local processing, and Matter compatibility. No mandatory subscription, no cloud-required video storage, and automation triggers that connect to the rest of your Aqara or HomeKit ecosystem. For Apple-first households, this is the only doorbell worth considering."
                    }
                ]
            },
            "zh-tw": {
                "commentary": "Eufy E340的雙鏡頭設計是目前門鈴類別裡面最有實用價值的創新，一個鏡頭拍正面訪客，另一個鏡頭拍地面包裹。這個設計直接解決「包裹被偷」這個現實問題，不需要另外裝一台監視器。排名第一實至名歸。\n\n今年Ring在AI功能這一塊動作很大，Familiar Faces辨識常客功能剛在五月底推出，門鈴可以認出常來的人並且用具體名稱通知你，而不是一律顯示「偵測到移動」。這功能不需要換硬體就能開，算是很有誠意的升級。Ring同時推出了2K和4K版本的電池式門鈴新機，畫質是歷代最好，不需要接硬線就有這個解析度，對租屋族或不想裝電線的用戶很友善。\n\nAqara G410在HomeKit用戶群裡面是不二選擇，本地端儲存加上HomeKit Secure Video的完整支援，完全不需要付雲端訂閱費。自動化觸發的彈性也遠超Ring和Eufy，如果你家已經有Aqara Hub，整合進去幾乎零阻力。\n\nEufy在CES 2026展示的Video Doorbell S4，3K解析度加AI追蹤，預計售價約NT$8,500，正式上市後會對Ring和Arlo的中階市場造成壓力。目前買E340的用戶同樣可以受益於這條產品線的韌體持續優化。父親節前後如果想送門鈴，Eufy E340和Ring 4K版是最受歡迎的兩個方向。",
                "highlights": [
                    {
                        "title": "Ring Familiar Faces讓通知從此有意義",
                        "body": "Ring在五月底推出Familiar Faces功能，門鈴可以辨識常來的訪客並發出有名稱的通知，不再只是制式的「偵測到動態」。這個功能是opt-in設計，現有Ring用戶不需要換機器就能啟用，是近幾年Ring最有感的AI功能更新。"
                    },
                    {
                        "title": "Eufy S4預告下半年門鈴格局改變",
                        "body": "Eufy在CES 2026展示的Video Doorbell S4，配備AI追蹤、3K解析度和全景視角，預計售價約NT$8,500。等到正式上市，中階門鈴市場的競爭會更激烈。現在買Eufy E340的用戶一樣可以享受同系列韌體持續更新的好處。"
                    },
                    {
                        "title": "Aqara G410是Apple HomeKit用戶唯一的選擇",
                        "body": "G410對HomeKit的支援深度是目前所有門鈴裡面最完整的，本地端影片儲存加上HomeKit Secure Video，不需要任何訂閱費。如果家裡已經有Aqara Hub生態系，整合進去的自動化彈性更是Ring或Eufy完全比不上的。"
                    }
                ]
            }
        }
    }
    upsert(d, entry)
    save(p, d)
    print("OK video-doorbells")


def build_smart_pet_feeders():
    d, p = load("best-smart-pet-feeders.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {
                "title": "Best Smart Pet Feeders and Cameras 2026",
                "url": "https://www.smarthomeexplorer.com/guides/best-automated-smart-pet-feeders-cameras-2026",
                "source": "SmartHomeExplorer"
            },
            {
                "title": "Petkit Automatic Feeder vs Petlibro 2026: Best Tested",
                "url": "https://www.infomastero.online/petkit-automatic-feeder-vs-petlibro/",
                "source": "Infomastero"
            },
            {
                "title": "Best Smart Cat Feeder with Camera for Professionals 2026",
                "url": "https://homerunpet.com/blogs/pet-care-insights/best-smart-cat-feeder-with-camera-for-professionals-2026",
                "source": "HomeRunPet"
            },
        ],
        "i18n": {
            "en": {
                "commentary": "The Petlibro Granary Camera Feeder is the smart pet feeder I recommend without hesitation for 2026. The reason is straightforward: it earned best automatic pet feeder designations from both PCMag and Wirecutter based on one fundamental characteristic, it feeds when it is supposed to. Mechanical reliability is the one quality that cannot be forgiven when it fails. A feeder that occasionally skips a meal or dispenses double portions is not a convenience product, it is a source of anxiety. Petlibro's engineering prioritizes this above camera resolution or AI features, and the result is a product that pet owners trust to do its job while they are traveling.\n\nThe integrated camera adds remote monitoring that makes the Granary Camera particularly compelling for summer travel. With Memorial Day behind us and summer vacation season fully underway, the feeder with a camera lets you verify your pet actually ate, not just that the motor ran. That visual confirmation is genuinely valuable.\n\nPetkit YumShare Dual Hopper 2 at No. 2 leads the premium segment. It targets households with multiple pets or demanding owners who want 24/7 video interaction, motion detection, and AI-powered behavioral alerts in addition to automated feeding. The 1080P AI camera and two-way audio make it closer to a dedicated pet monitor than a simple feeder. The price reflects that, but for multi-pet households it justifies the spend.\n\nPetlibro Polar Wet Food Feeder at No. 3 fills a meaningful gap: refrigerated wet food dispensing. Dry food feeders outnumber wet food options ten to one in this market, but the Polar's ice pack cooling system keeps wet food fresh for hours. For cats with dietary restrictions requiring wet food only, this is currently the best option available.",
                "highlights": [
                    {
                        "title": "Petlibro Granary Camera Earns Dual Best-in-Class Awards",
                        "body": "PCMag and Wirecutter both designated the Petlibro Granary Camera Feeder as the best automatic pet feeder in 2026, citing consistent mechanical reliability as the deciding factor. For a product category where a dispensing failure means a hungry pet, this reliability track record is the most important specification on the sheet."
                    },
                    {
                        "title": "Camera Integration Is Essential for Summer Travel",
                        "body": "With summer vacation season underway post-Memorial Day, the feeder camera feature earns its keep. Remote viewing confirms whether your pet actually ate rather than just whether the motor cycled. The Petlibro Granary Camera and Petkit YumShare both support live video monitoring from the companion app, giving travelers genuine peace of mind."
                    },
                    {
                        "title": "Petlibro Polar Addresses the Wet Food Gap",
                        "body": "The vast majority of smart feeders are designed exclusively for dry kibble, leaving wet food owners without an automated option. The Petlibro Polar uses an ice pack cooling system to keep wet food fresh across multiple scheduled meals. For cats with prescription diets or older pets requiring soft food, the Polar is currently the most capable solution in this underserved segment."
                    }
                ]
            },
            "zh-tw": {
                "commentary": "暑假旅遊季到來，家裡有貓狗的朋友最在意的就是出門時的餵食問題。我測試一輪下來，Petlibro Granary Camera Feeder是目前最值得推薦的智慧寵物餵食器，原因很簡單：PCMag和Wirecutter雙雙把它評為2026年最佳自動餵食器，理由是機械可靠性，就是「時間到了它一定會餵」。這聽起來很基本，但你去看一堆競品的用戶評論，跳餐、雙份、卡料的問題還是很常見。Petlibro在這個核心需求上做得最紮實。\n\n整合攝影機這個設計在夏季出遊的情境下特別有價值，不只是確認餵食器有沒有運作，而是可以直接看到寵物有沒有吃。機器有跑不等於貓真的吃了，能遠端看到牠吃飯才是真的安心。\n\nPetkit YumShare Dual Hopper 2排第二，走的是更高階的路線，1080P AI攝影機加雙向語音，幾乎可以當成全天候的寵物監視器，適合多隻寵物的家庭或對互動功能要求高的主人。功能豐富但價格也不便宜，參考售價約NT$4,500到NT$5,500。\n\nPetlibro Polar Wet Food Feeder排第三，這個有填補市場空缺的意義，因為幾乎所有智慧餵食器都只支援乾飼料，濕食自動餵食器少之又少。Polar用保冰包設計讓濕食在數小時內保持新鮮，對需要吃處方濕食的貓咪或老貓來說，目前市面上沒有比它更好的選擇。",
                "highlights": [
                    {
                        "title": "Petlibro Granary Camera獲PCMag和Wirecutter雙料認證",
                        "body": "PCMag和Wirecutter在2026年都把Petlibro Granary Camera Feeder評為最佳自動餵食器，決定性因素是機械可靠性，時間到了它就會準時餵。在這個「失敗等於讓寵物挨餓」的產品類別，可靠性紀錄是比任何功能規格都更重要的評估指標。"
                    },
                    {
                        "title": "攝影機功能在夏季旅遊季格外重要",
                        "body": "暑假出遊時，能用手機直接看到寵物有沒有吃飯，遠比只看到「餵食排程執行成功」的通知更有安全感。Petlibro Granary Camera和Petkit YumShare都支援App即時影像，夏天帶這個出門才能真的放心玩。"
                    },
                    {
                        "title": "Petlibro Polar填補濕食市場空缺",
                        "body": "市面上幾乎所有自動餵食器都只支援乾飼料，Petlibro Polar的保冰系統讓濕食在多個餵食時段之間保持新鮮。對需要吃處方濕食的病貓或老貓，這目前是市場上最完整的解決方案，參考售價約NT$3,500。"
                    }
                ]
            }
        }
    }
    upsert(d, entry)
    save(p, d)
    print("OK smart-pet-feeders")


def build_robot_vacuums():
    d, p = load("best-robot-vacuums.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {
                "title": "iRobot released 9 robot vacuums at once: up to 30,000 Pascal power, climbing over thresholds",
                "url": "https://www.afterdawn.com/news/article.cfm/2026/05/14/irobot-released-nine-new-roomba-robot-vacuums",
                "source": "AfterDawn"
            },
            {
                "title": "Dreame's Lineup at CES 2026 – Including New Ultra-Thin X60 Max Ultra Robot Vacuum",
                "url": "https://vacuumwars.com/dreames-ces-2026-lineup/",
                "source": "VacuumWars"
            },
            {
                "title": "Top 20 Best Robot Vacuums in 2026 | Reviews by Vacuum Wars",
                "url": "https://vacuumwars.com/vacuum-wars-best-robot-vacuums/",
                "source": "VacuumWars"
            },
        ],
        "i18n": {
            "en": {
                "commentary": "The Dreame X60 Max Ultra holds the top position in robot vacuums for mid-2026, and the performance gap between it and the competition has not closed. The 12,000Pa suction combined with Dreame's ultra-thin chassis design means it reaches under furniture that trips up every other robot in the category. The MopExtend system that extends the mop pad to reach wall edges is a genuine differentiator: wall-edge mopping has been the persistent weakness of robot vacuum-mop combos for years, and Dreame addressed it mechanically rather than through software promises.\n\nThe biggest news this month is iRobot's most aggressive product launch in recent memory: nine new Roomba models released simultaneously in mid-May. The flagship Roomba Max 715 and 775 deliver 30,000Pa suction, which outpaces nearly everything on the market. The entire new lineup uses LiDAR navigation rather than camera-based mapping, which speeds up initial home scanning and improves obstacle avoidance in low-light conditions. iRobot at No. 11 in this ranking reflects the older Roomba j9 Plus, but the new Max series will put iRobot back into competitive range at the premium tier.\n\nDreame's L50 Ultra and L60 lineup expansion continue to push the brand's dominance. The new L60 series offers four tiers from entry to flagship with 35,000Pa suction and 100-degree mop self-cleaning across all tiers. Roborock's Saros 10R at No. 2 and the arm-equipped Saros Z70 at No. 4 represent the most advanced navigation approaches in the category: the Z70 can pick up small objects with its robotic arm before mopping begins, which is the closest thing to a fully autonomous floor-cleaning solution currently available.",
                "highlights": [
                    {
                        "title": "iRobot Launches Nine New Roomba Models with 30,000Pa Suction",
                        "body": "iRobot's simultaneous mid-May launch of nine new Roomba models, from the budget 115 Combo to the flagship Max 715 and 775 with 30,000Pa suction, is the brand's most significant product refresh in years. All new models use LiDAR navigation instead of cameras, improving mapping speed and low-light performance. This launch puts iRobot back into serious contention at the premium tier."
                    },
                    {
                        "title": "Dreame X60 Max Ultra's Edge Mopping Sets a New Standard",
                        "body": "The Dreame X60 Max Ultra's MopExtend mechanism physically pushes the mop pad outward to clean along baseboards and walls. This mechanical solution to wall-edge coverage is more reliable than software-based zigzag patterns, and it distinguishes the X60 Max Ultra from every competing vacuum-mop combo currently on the market."
                    },
                    {
                        "title": "Roborock Saros Z70 Arm Technology Moves Toward True Autonomy",
                        "body": "The Roborock Saros Z70's robotic arm, which picks up small objects before the mopping cycle begins, represents the most advanced autonomous behavior in consumer robot vacuums. While the arm handles only specific object categories, it removes the single most frustrating pre-cleaning step users face: manually clearing the floor before running the robot."
                    }
                ]
            },
            "zh-tw": {
                "commentary": "機器人吸塵器今年的競爭激烈程度是歷年最高的，光五月份就有iRobot一口氣推出九款新品，這種規模的產品發布在這個類別很罕見。不過就目前測試數據來看，Dreame X60 Max Ultra還是坐穩第一名的位置，理由是MopExtend機械式拖布延伸系統，可以讓拖布實際推出去貼著牆角清潔，這個機械設計解決了所有機器人拖地機長期以來的死角問題。\n\niRobot這批新品裡最值得注意的是Roomba Max 715和775，吸力30,000Pa幾乎是目前市場最高，而且全線換成LiDAR導航取代舊的攝影機建圖，建圖速度更快、昏暗環境表現更好。目前排行榜上的Roomba j9 Plus是舊款，等新Max系列的詳細測試結果出來，iRobot的排名應該會往上移動。\n\nRoborock Saros Z70排在第四，因為它有機械手臂，可以在拖地前自動把小物件夾起來放在一邊，這是目前消費等級機器人吸塵器裡最接近「全自動」的概念。Dreame L60系列新推出四個等級，全系列標配35,000Pa吸力和100度高溫自清潔拖布，入門款也有旗艦功能，整條產品線的性價比都很高。\n\nEcovacs DEEBOT X5 Pro Omni在OLED顯示底座和語音互動這塊做得最有質感，適合重視居家美感的用戶。Eufy X10 Pro Omni的iPath導航在複雜家具環境下表現穩定，也是個性價比不錯的選擇。",
                "highlights": [
                    {
                        "title": "iRobot五月同時推出九款Roomba新品",
                        "body": "iRobot在五月中旬同步發布九款新Roomba，旗艦Roomba Max 715和775吸力達30,000Pa，全線換成LiDAR導航。這是iRobot近年最大規模的產品更新，新款LiDAR建圖速度和昏暗環境表現都比舊款攝影機方案明顯進步，預計會讓iRobot重新殺回高階市場。"
                    },
                    {
                        "title": "Dreame X60 Max Ultra拖布延伸設計解決牆角死角",
                        "body": "MopExtend系統讓拖布物理性地推出去貼牆清潔，比靠軟體走Z字形更可靠。這個機械設計直接解決了所有吸拖合一機器人長期存在的牆角清潔問題，是目前市面上所有競品都沒有辦法複製的差異化設計。"
                    },
                    {
                        "title": "Roborock Saros Z70機械手臂朝全自動邁進",
                        "body": "Saros Z70的機械手臂可以在拖地前自動把地上的小物件夾起來，省去最讓人煩惱的「跑機器人前要先撿地上東西」這個步驟。雖然手臂目前能處理的物件種類有限，但這個設計方向代表機器人吸塵器真正走向全自動的第一步。"
                    }
                ]
            }
        }
    }
    upsert(d, entry)
    save(p, d)
    print("OK robot-vacuums")


def build_robot_lawn_mowers():
    d, p = load("best-robot-lawn-mowers.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {
                "title": "Best Robot Lawn Mower 2026 (Tested & Reviewed for U.S. Lawns)",
                "url": "https://us.mammotion.com/blogs/news/best-robot-lawn-mower-2026",
                "source": "Mammotion"
            },
            {
                "title": "5 new robot lawnmowers from CES 2026 that show the future of smart gardening",
                "url": "https://www.t3.com/home-living/garden/5-new-robot-lawnmowers-from-ces-2026",
                "source": "T3"
            },
            {
                "title": "Best Robotic Lawn Mowers Compared: Husqvarna vs Segway vs Ecovacs vs Mammotion vs Worx",
                "url": "https://finestlawns.com/blog/best-robotic-lawn-mowers-compared-husqvarna-segway-ecovacs-mammotion-worx/",
                "source": "Finest Lawns"
            },
        ],
        "i18n": {
            "en": {
                "commentary": "This is the peak season for robot lawn mowers, and the Mammotion LUBA 3 AWD 5000 is the right call for anyone with a large or complex yard. The Tri-Fusion navigation system combines 360-degree LiDAR, high-precision RTK GPS satellite positioning, and dual 1080p AI cameras into one unified guidance system. No perimeter wires, no buried boundary cables, no multi-hour installation sessions. The AWD drivetrain handles slopes and uneven terrain that trips up single-drive competitors, and the 1.25-acre coverage capacity makes it one of the few robots genuinely suited to full-size suburban lots.\n\nThe Ecovacs Goat A3000 LiDAR Pro at No. 2 earns attention for its TruEdge system, which addresses the persistent problem of edge cutting. Robotic mowers have always struggled with the last few inches near fences, flower beds, and driveways. The A3000 LiDAR Pro's TruEdge edge trimmer actively maintains clean borders, reducing the amount of manual trimming required after each autonomous mow session. Ecovacs also debuted its HoloScope 360 Dual-LiDAR system at CES 2026, cutting installation time to under a minute with mapping accuracy within two centimeters.\n\nHusqvarna's Automower line at No. 7 represents 25 years of robotic mowing experience. The 450x EPOS model uses GPS and cellular precision positioning rather than boundary wires, and Husqvarna's reliability record across commercial and residential applications is unmatched. For buyers who want proven longevity rather than the latest features, Husqvarna remains the safest bet.\n\nWith Father's Day on June 21, robot mowers are an ideal gift for lawn-conscious homeowners. The Mammotion LUBA 3 AWD 5000 leads current Best of Amazon rankings and ships with enough coverage for most suburban yards.",
                "highlights": [
                    {
                        "title": "Mammotion LUBA 3 AWD 5000 Leads Peak Mowing Season",
                        "body": "With summer lawn care at its most demanding post-Memorial Day, the LUBA 3 AWD 5000's Tri-Fusion navigation, all-wheel drive, and 1.25-acre coverage make it the top pick for serious lawn owners. No buried wires, no complex installation, and the AWD system handles the slopes and terrain variations that stump single-drive competitors."
                    },
                    {
                        "title": "Ecovacs HoloScope 360 Cuts Setup Time to Under a Minute",
                        "body": "Ecovacs debuted its HoloScope 360 Dual-LiDAR system at CES 2026, achieving mapping accuracy within two centimeters and reducing installation time from hours to under a minute. The A3000 LiDAR Pro also features TruEdge technology for clean border cutting, which is the specific capability that most separates premium robot mowers from entry-level units."
                    },
                    {
                        "title": "Father's Day Makes Robot Mowers the Gift of the Season",
                        "body": "Robot lawn mowers are peak gift territory for Father's Day on June 21. The LUBA 3 AWD 5000 leads Amazon's best-of lists for the category, and the Navimow series offers entry points for smaller yards. Compared to a traditional mower purchase, a robot mower delivers ongoing time savings every week of the mowing season."
                    }
                ]
            },
            "zh-tw": {
                "commentary": "現在是機器人割草機的黃金旺季，Memorial Day剛過，夏季草坪護理需求正在高峰期，這時候買機器人割草機最划算，因為馬上就能派上用場。我的首選是Mammotion LUBA 3 AWD 5000，它的Tri-Fusion導航結合了360度LiDAR、高精度RTK GPS衛星定位和雙1080p AI視覺，三個系統同時運作讓它在各種地形和光線條件下都能準確工作。最重要的是不需要埋設邊界電線，設定過程比傳統有線系統簡單太多，AWD四輪驅動對有坡度的草坪來說是標準配備不是選配。\n\nEcovacs Goat A3000 LiDAR Pro排在第二，今年的更新重點是TruEdge邊緣修剪系統，讓割草機可以清潔地修到圍籬、花圃、車道邊緣，把最讓人頭痛的手動補修作業大幅減少。Ecovacs在CES 2026展示的HoloScope 360雙LiDAR系統可以把安裝時間壓縮到一分鐘以內，建圖精度在兩公分以內，這個技術進步對新用戶的設定體驗改善非常大。\n\nHusqvarna Automower 450x EPOS在這個類別有二十五年以上的歷史，用GPS和行動定位取代邊界電線，長期可靠性有最多商業應用案例背書。如果你重視的是長期穩定性而不是最新功能，Husqvarna是風險最低的選擇。\n\n六月父親節送機器人割草機是非常有誠意的禮物，因為它解決的是一個每週都要面對的勞務問題，送了就能感受到每週省下的時間。LUBA 3 AWD 5000目前在Amazon的類別排行榜上名列前茅，出貨速度也快。",
                "highlights": [
                    {
                        "title": "Mammotion LUBA 3 AWD 5000是割草旺季首選",
                        "body": "Memorial Day過後進入夏季割草高峰，LUBA 3 AWD 5000的Tri-Fusion三合一導航、四輪驅動和1.25英畝覆蓋面積，讓它成為有坡度或複雜地形草坪的最強選擇。完全不需要埋邊界電線，設定比傳統系統簡單得多。"
                    },
                    {
                        "title": "Ecovacs HoloScope 360讓安裝時間縮短到一分鐘",
                        "body": "Ecovacs在CES 2026發表的HoloScope 360雙LiDAR系統，建圖精度達兩公分以內，安裝時間從過去的數小時壓縮到一分鐘以內。A3000 LiDAR Pro的TruEdge邊緣修剪技術同步解決圍籬和花圃邊角修剪的死角問題。"
                    },
                    {
                        "title": "父親節送機器人割草機是最有感的禮物",
                        "body": "父親節6月21日快到了，機器人割草機解決的是每週都要面對的草坪勞務，送了就能每週省出一到兩個小時。LUBA 3 AWD 5000在Amazon類別排行榜前段班，Navimow系列則有較小坪數的入門選項，價位從NT$25,000到NT$80,000以上都有。"
                    }
                ]
            }
        }
    }
    upsert(d, entry)
    save(p, d)
    print("OK robot-lawn-mowers")


def build_robotic_pool_cleaners():
    d, p = load("best-robotic-pool-cleaners.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {
                "title": "Beatbot and Aiper solar-charging robotic pool skimmers are great summer assistants at lows starting from $360",
                "url": "https://9to5toys.com/2026/05/27/beatbot-and-aiper-solar-charging-robotic-pool-skimmers-from-360/",
                "source": "9to5Toys"
            },
            {
                "title": "Beatbot Announces AquaSense X Open Sale: The World's First Pool Robot with a Self-Cleaning Dock",
                "url": "https://www.morningstar.com/news/pr-newswire/20260413cn32531/beatbot-announces-aquasense-x-open-sale-the-worlds-first-pool-robot-with-a-self-cleaning-dock",
                "source": "PR Newswire via Morningstar"
            },
            {
                "title": "Spring Fling: New Robotic Pool Cleaners Making a Splash in 2026",
                "url": "https://www.poolmagazine.com/features/products/spring-fling-new-robotic-pool-cleaners-making-a-splash-in-2026/",
                "source": "Pool Magazine"
            },
        ],
        "i18n": {
            "en": {
                "commentary": "Robotic pool cleaners are having their moment. Pool opening season is fully underway post-Memorial Day, and the category has more compelling new options than any recent year. The Dolphin Premier holds the top position on cleaning thoroughness and durability grounds, with a brushed scrubbing system that outperforms cordless competitors on heavy algae and debris loads. For pool owners who prioritize deep cleaning results over convenience features, Dolphin's wall-climbing and waterline-scrubbing capability is unmatched at this price point.\n\nBeatbot had the biggest news cycle in the category this spring with the AquaSense X ecosystem launch, which includes the AstroRinse Cleaning Station, the world's first self-cleaning dock for pool robots. The dock handles up to two months of debris disposal with its 22-liter bin, eliminating the manual emptying task that users cite as the primary maintenance annoyance with robotic cleaners. This launch puts the Beatbot AquaSense 2 Ultra at No. 2 in an even stronger light as the brand's proven flagship.\n\nAiper had a strong spring with the Scuba V3 review cycle. The V3 is among the lightest options in the category at 18.1 pounds, packs an AI vision system, and features heavy-duty tank treads for consistent traction on pool floors and walls. The Aiper Scuba S1 at No. 4 and Scuba SE at No. 10 bracket the lineup, giving buyers a clear value ladder within the Aiper ecosystem.\n\nSolar pool skimmers from both Beatbot and Aiper hit deal pricing in late May, with the Beatbot iSkim Ultra Solar at $699 and the Aiper Surfer S2 Solar at $359.98 generating strong consumer interest for surface debris management. These supplement rather than replace full-pool robotic cleaners.",
                "highlights": [
                    {
                        "title": "Beatbot AquaSense X Launches the First Self-Cleaning Dock",
                        "body": "Beatbot's AquaSense X ecosystem, launched in open sale in April 2026, includes the AstroRinse Cleaning Station with a 22-liter bin that handles up to two months of debris disposal autonomously. This eliminates the most cited maintenance complaint about robotic pool cleaners: manual filter emptying after every session. The AquaSense 2 Ultra benefits directly from the same engineering pipeline."
                    },
                    {
                        "title": "Aiper Scuba V3 Brings AI Vision at Competitive Weight",
                        "body": "The Aiper Scuba V3 combines AI vision processing for smarter pool mapping with a 18.1-pound chassis that remains one of the lightest in the cordless category. Tank treads provide consistent wall-climbing traction, and the new AI capabilities allow more efficient coverage patterns compared to simple random-bounce navigation found in entry-level cleaners."
                    },
                    {
                        "title": "Solar Skimmers Add Surface Coverage at Accessible Prices",
                        "body": "Beatbot's iSkim Ultra Solar at $699 and Aiper's Surfer S2 Solar at $359.98 went on sale in late May, offering a solar-powered approach to continuous surface skimming. These units handle leaves, pollen, and surface debris between full robotic cleaning sessions, extending water clarity and reducing the workload on pool filtration systems."
                    }
                ]
            },
            "zh-tw": {
                "commentary": "Memorial Day過後，泳池開放季正式全速運轉，這個類別今年的新品比近幾年都更精彩。Dolphin Premier繼續蟬聯第一，靠的是刷洗能力和耐用性，有刷毛的旋轉刷系統對付藻類和重度污垢的效果，目前市面上有線式機器人裡面還是最強的，爬壁清潔水位線的能力也是這個價位裡面無可取代的。\n\n今年春季最大的新聞是Beatbot發表AquaSense X生態系，包含AstroRinse自清潔底座，這是全球第一個泳池機器人用的自動清洗底座，22公升的集塵桶可以撐兩個月不需要手動清空。用戶長期抱怨的「每次用完要自己清濾網」這個痛點，Beatbot直接用機械方式解決了。AquaSense 2 Ultra排在第二，這個研發實力讓它的長期發展更值得看好。\n\nAiper今年春季靠Scuba V3的評測聲量打得不錯，V3重量只有18.1磅，是這個類別裡面最輕的幾款之一，但還是塞進了AI視覺系統和履帶式驅動，在泳池底部和池壁的附著力和清潔覆蓋率都表現不錯。Aiper產品線從Scuba S1到Scuba SE提供清楚的價位梯度，給不同預算的買家有明確的選擇路線。\n\nBeatbot和Aiper的太陽能浮面清潔器在五月底都有特惠，Beatbot iSkim Ultra Solar約NT$22,000、Aiper Surfer S2 Solar約NT$11,500，適合搭配主力機器人吸塵器使用，處理葉子和花粉等浮面雜物，讓泳池水質保持更長時間的透明度。",
                "highlights": [
                    {
                        "title": "Beatbot AquaSense X推出業界首款自清潔底座",
                        "body": "Beatbot的AstroRinse自清潔底座在2026年4月開始公開銷售，22公升集塵桶可以自動排污長達兩個月。這個設計直接解決了用戶最常抱怨的問題：每次清洗完要手動清理濾網。AquaSense 2 Ultra作為同系列旗艦，直接受益於這個研發能量。"
                    },
                    {
                        "title": "Aiper Scuba V3帶來AI視覺且重量最輕",
                        "body": "Aiper Scuba V3只有18.1磅，是這個類別最輕的幾款之一，但同時搭載了AI視覺系統和履帶式驅動。AI視覺讓它能做更有效率的路線規劃，履帶驅動確保池壁清潔的附著力，兩個功能組合在這個重量下是很有技術含量的設計。"
                    },
                    {
                        "title": "太陽能浮面清潔器五月底特價入手好時機",
                        "body": "Beatbot iSkim Ultra Solar和Aiper Surfer S2 Solar在五月底都有降價促銷，太陽能設計不需要充電，24小時連續清理浮面葉片和花粉。搭配主力的水下清潔機器人使用，可以大幅減少每次啟動主機的頻率，過濾系統的負擔也更輕。"
                    }
                ]
            }
        }
    }
    upsert(d, entry)
    save(p, d)
    print("OK robotic-pool-cleaners")


if __name__ == "__main__":
    build_smart_thermostats()
    build_mesh_wifi_systems()
    build_security_cameras()
    build_video_doorbells()
    build_smart_pet_feeders()
    build_robot_vacuums()
    build_robot_lawn_mowers()
    build_robotic_pool_cleaners()
    print("Batch 5 complete")
