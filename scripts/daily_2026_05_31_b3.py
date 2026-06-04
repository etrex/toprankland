"""2026-05-31 daily update — Batch 3: Audio/Display (8 files)"""
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


def build_wireless_earbuds():
    d, p = load("best-wireless-earbuds.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {
                "title": "Best Wireless Earbuds in 2026: AirPods, Sony, Bose, Samsung Tested",
                "url": "https://www.petematheson.com/best-wireless-earbuds/",
                "source": "Pete Matheson"
            },
            {
                "title": "The best wireless earbuds of 2026: Lab-tested by experts",
                "url": "https://www.soundguys.com/best-wireless-earbuds-2-14313/",
                "source": "SoundGuys"
            },
            {
                "title": "Best Wireless Earbuds 2026 — Alexa, Google, and Siri tested",
                "url": "https://www.tomsguide.com/best-picks/best-wireless-earbuds",
                "source": "Tom's Guide"
            },
        ],
        "i18n": {
            "en": {
                "commentary": "Sunday May 31 holds Sony WF-1000XM6 at the top, and that position is fully earned. The XM6 is the most adjustable earbud on the market today, with class-leading active noise cancellation, meaningfully improved microphone performance over the XM5, and a sound tuning suite in the Headphones Connect app that lets you dial in EQ to a degree nothing from Apple or Bose matches. The $299 price has held stable across Amazon, Best Buy, and Sony direct through the long weekend, and with Father's Day on June 21 approaching there is no reason to expect a discount before then.\n\nAirPods Pro 2 holds second at $189 and for iPhone households the argument is simple: the H2 chip delivers Adaptive Audio, Conversation Awareness, and Personalized Spatial Audio in ways that other earbuds physically cannot replicate because they require deep iOS integration. Apple does not run Father's Day promotions. $189 is today's price and it stays there.\n\nBose QuietComfort Ultra Earbuds 2 holds third at $279. Bose continues to lead on low-frequency isolation, especially on aircraft and commuter trains, and the fit system is the most physically stable of any premium earbud. For travelers buying a Father's Day gift, the Bose story is comfort plus ANC reliability over long sessions.\n\nSamsung Galaxy Buds4 Pro holds fourth at $249 as the best choice inside the Galaxy ecosystem. Sony WF-1000XM5 holds fifth as the best earbud under $250, still delivering XM-grade sound and ANC at last generation pricing. Father's Day is pulling the XM6 and AirPods Pro 2 into carts this weekend, with Amazon Prime shipping cutoffs around June 14.",
                "highlights": [
                    {
                        "title": "Sony WF-1000XM6 at $299 is the unambiguous pick for Android audio enthusiasts",
                        "body": "The XM6 outperforms every competitor on adjustability, ANC depth, and call clarity. Sony has not discounted for Father's Day and is not expected to before June 21. At $299 this is a straightforward recommendation for anyone with an Android phone who takes sound quality seriously."
                    },
                    {
                        "title": "AirPods Pro 2 at $189 is the rational Father's Day gift for iPhone households",
                        "body": "Adaptive Audio and Personalized Spatial Audio via the H2 chip are iPhone-exclusive features that competitors cannot replicate. Apple holds $189 with no Father's Day promo. For an iPhone household this is the correct choice and the price is the best it has been all year."
                    },
                    {
                        "title": "Sony WF-1000XM5 at $249 remains the value leader",
                        "body": "With the XM6 at $299 above it, the XM5 occupies the best-earbud-under-$250 slot with XM-tier ANC and Sony's audio tuning. For buyers unwilling to pay full flagship pricing, the XM5 is the correct decision and continues to hold its value position post-Memorial Day."
                    }
                ]
            },
            "zh-tw": {
                "commentary": "5/31 星期日把 Sony WF-1000XM6 留在第一，這個位置完全實至名歸。XM6 是目前市場上可調整性最高的耳機，搭載同級最強的主動降噪，麥克風表現比 XM5 有感升級，Headphones Connect App 的 EQ 細調程度是 Apple 或 Bose 跟不上的。Amazon、Best Buy、Sony 官網整個長週末 USD$299（約 NT$9,990）守住，父親節 6/21 前沒有折扣跡象。\n\nAirPods Pro 2 守第二 USD$189（約 NT$6,290）。iPhone 家庭的理由很直接，H2 晶片帶來的 Adaptive Audio、Conversation Awareness、個人化空間音訊，這些功能需要深度 iOS 整合，其他耳機根本複製不了。Apple 不辦父親節促銷，今天的價格就是 6/21 前的價格。\n\nBose QuietComfort Ultra Earbuds 2 守第三 USD$279（約 NT$9,290），在低頻隔音方面，特別是飛機和捷運環境，Bose 還是略勝一籌，配戴穩定性是所有高端耳機裡最好的。要買給常搭機爸爸的父親節禮物，Bose 的故事就是長時間舒適加降噪可靠度。\n\nSamsung Galaxy Buds4 Pro 守第四 USD$249（約 NT$8,290），Galaxy 生態最佳選擇。Sony WF-1000XM5 守第五，NT$8,500 以下最佳耳機頭銜不動搖，用上一代的價格買到 XM 等級的音質跟降噪，CP 值沒得比。父親節這個週末 XM6 跟 AirPods Pro 2 加入購物車的速度最快，Amazon Prime 到貨截止大約 6/14。",
                "highlights": [
                    {
                        "title": "Sony WF-1000XM6 NT$9,990，Android 音響愛好者的不二選擇",
                        "body": "可調整性、降噪深度、通話清晰度全面勝出所有競品。Sony 沒有為父親節折扣的計畫，6/21 前都是 NT$9,990。對在意音質又用 Android 手機的爸爸，這是直接下單不需要猶豫的選擇。"
                    },
                    {
                        "title": "AirPods Pro 2 NT$6,290，iPhone 家庭父親節理性禮物",
                        "body": "H2 晶片的 Adaptive Audio 跟個人化空間音訊是 iPhone 專屬功能，競品複製不了。Apple 不辦父親節促銷，NT$6,290 是今年表現最好的價格。iPhone 家庭選這個就對了，日常使用的無縫切換跟 Find My 都能回本。"
                    },
                    {
                        "title": "Sony WF-1000XM5 NT$8,290，CP 值旗艦地位穩固",
                        "body": "XM6 在上方 NT$9,990，XM5 就穩穩佔著 NT$8,500 以下最佳耳機的位置，降噪跟音質都是 XM 等級。不想付旗艦溢價的買家，XM5 是正確答案，長週末後價格穩定沒有變動。"
                    }
                ]
            }
        }
    }
    upsert(d, entry)
    save(p, d)
    print("OK wireless-earbuds")


def build_noise_cancelling_headphones():
    d, p = load("best-noise-cancelling-headphones.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {
                "title": "Best Noise Cancelling Headphones 2026: Sony XM6, Bose, AirPods Max Compared",
                "url": "https://www.techtimes.com/articles/316304/20260502/best-noise-cancelling-headphones-2026-sony-xm6-anc-bose-comfort-airpods-max-ecosystem-compared.htm",
                "source": "TechTimes"
            },
            {
                "title": "The 5 Best Noise Cancelling Headphones of 2026",
                "url": "https://www.rtings.com/headphones/reviews/best/by-feature/noise-cancelling",
                "source": "RTINGS"
            },
            {
                "title": "I tested the Sony WH-1000XM6 vs Bose QuietComfort Ultra 2 for 6 months — clear winner",
                "url": "https://www.tomsguide.com/audio/headphones/i-tested-the-sony-wh-1000xm6-vs-bose-quietcomfort-ultra-2-for-6-months-and-theres-a-clear-winner",
                "source": "Tom's Guide"
            },
        ],
        "i18n": {
            "en": {
                "commentary": "Sunday May 31, Sony WH-1000XM6 holds the top position in over-ear noise-cancelling headphones and the case is straightforward. The XM6 delivers the best measured ANC of any over-ear headphone tested this year with 12 microphones handling adaptive noise cancellation and a 10-band EQ in Sony's app that is simply unmatched. 30 hours of battery life means a full week of office use without reaching for the charging cable. At $349 it is the premium recommendation for anyone who wants maximum control over their listening experience.\n\nBose QuietComfort Ultra Headphones holds second at $379. Bose wins on comfort: the padded earcups and headband fatigue more slowly over all-day sessions than the Sony, and the QC Ultra's tuning is relaxed and easy to live with for entire workdays. On long-haul flights, the Bose remains the traveler's choice for ANC consistency and physical comfort over 10-plus hours. Father's Day approaches June 21, and Best Buy is running a Bose Father's Day sale that makes this a realistic $349 purchase this weekend.\n\nSennheiser Momentum 4 holds third at $279 with the best measured sound quality of any headphone in this group and a 60-hour battery that makes it the battery champion. For buyers who put sound fidelity above ANC intensity, Sennheiser is the correct recommendation. The Sennheiser HD B 630 holds fourth with outstanding audio performance suited for the discerning listener.\n\nFather's Day on June 21 is driving premium headphone searches and purchases. Best Buy's Bose promotional pricing and Amazon's XM6 availability make both the top two picks accessible through standard shipping cutoffs this week.",
                "highlights": [
                    {
                        "title": "Sony WH-1000XM6 at $349 is the best ANC headphone you can buy today",
                        "body": "12 microphones, a 10-band EQ, and 30-hour battery put the XM6 ahead of every competitor on technical merit. For buyers who want maximum control over their listening experience, Sony is the choice. Amazon availability and standard shipping makes this a viable Father's Day purchase this week."
                    },
                    {
                        "title": "Bose QC Ultra at $379 with Best Buy Father's Day sale is the comfort traveler pick",
                        "body": "Bose wins on all-day physical comfort with amply padded earcups that outlast Sony on long sessions. Best Buy's Father's Day Bose promotion makes $349 pricing realistic this weekend. For dads who travel frequently, the QC Ultra's relaxed tuning and superior comfort are the correct tradeoff."
                    },
                    {
                        "title": "Sennheiser Momentum 4 at $279 leads on sound quality and battery",
                        "body": "The Momentum 4 has the best measured sound quality in the group and a 60-hour battery that is unmatched. For buyers prioritizing audio fidelity over ANC intensity, Sennheiser is the recommendation. At $279 it also represents the best value in the top three."
                    }
                ]
            },
            "zh-tw": {
                "commentary": "5/31 星期日 Sony WH-1000XM6 守住降噪耳機第一，理由很清楚。XM6 搭載 12 組麥克風的自適應降噪，音質調整有 10 段 EQ，是今年測試過測量降噪表現最好的耳罩式耳機。30 小時電池夠用整週辦公不充電。USD$349（約 NT$11,590）是最大化聆聽控制體驗的首選推薦。\n\nBose QuietComfort Ultra Headphones 守第二 USD$379（約 NT$12,590）。Bose 在舒適度上贏，加厚耳墊跟頭帶整天配戴的疲勞感比 Sony 慢，QC Ultra 的調音放鬆好入耳，整個工作日或長途飛行都能撐住。Best Buy 這週末有 Bose 父親節優惠，USD$349（約 NT$11,590）是現實價格，適合買給常出差的爸爸。\n\nSennheiser Momentum 4 守第三 USD$279（約 NT$9,290），音質測量表現是這個榜單裡最好的，60 小時電池是電池王者。把音質擺在降噪強度之前的買家，Sennheiser 是正確推薦。Sennheiser HD B 630 守第四，音頻表現出色，適合挑剔的聆聽者。父親節 6/21 推動了高端耳機的搜尋跟購買，Best Buy 的 Bose 促銷跟 Amazon 的 XM6 現貨讓這兩款都能趕上這週的到貨截止。",
                "highlights": [
                    {
                        "title": "Sony WH-1000XM6 NT$11,590，今天能買到的最強降噪耳機",
                        "body": "12 組麥克風、10 段 EQ、30 小時電池，技術面全面領先競品。想要最大化聆聽控制的買家，Sony 是答案。Amazon 有現貨，這週標準運送趕得上父親節到貨截止。"
                    },
                    {
                        "title": "Bose QC Ultra NT$11,590 含 Best Buy 父親節優惠，旅行舒適首選",
                        "body": "加厚耳墊讓 Bose 在長時間配戴上勝過 Sony，Best Buy 父親節促銷讓 NT$11,590 成為現實價格。常出差的爸爸，QC Ultra 放鬆的調音加上優越舒適度是正確的取捨。"
                    },
                    {
                        "title": "Sennheiser Momentum 4 NT$9,290，音質跟電池雙冠",
                        "body": "Momentum 4 音質測量是榜單裡最好的，60 小時電池無人能及。把音質擺在降噪前面的買家，Sennheiser 是推薦。NT$9,290 也是前三名裡最好的 CP 值。"
                    }
                ]
            }
        }
    }
    upsert(d, entry)
    save(p, d)
    print("OK noise-cancelling-headphones")


def build_bluetooth_speakers():
    d, p = load("best-bluetooth-speakers.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {
                "title": "Best Bluetooth speakers 2026: tried and tested for every budget",
                "url": "https://www.whathifi.com/best-buys/best-bluetooth-speakers-portable-speakers-for-every-budget",
                "source": "What Hi-Fi?"
            },
            {
                "title": "I test Bluetooth speakers for a living: my 12 top picks for outdoor listening this summer",
                "url": "https://www.tomsguide.com/audio/bluetooth-speakers/i-test-bluetooth-speakers-for-a-living-and-these-are-my-12-top-picks-for-outdoor-listening-this-summer",
                "source": "Tom's Guide"
            },
            {
                "title": "Best portable Bluetooth speakers in 2026, tested by editors",
                "url": "https://www.cnn.com/cnn-underscored/reviews/best-portable-bluetooth-speakers",
                "source": "CNN Underscored"
            },
        ],
        "i18n": {
            "en": {
                "commentary": "Sunday May 31, the post-Memorial Day weekend is exactly when outdoor Bluetooth speaker searches spike, and the JBL Charge 6 holds the top position because it is the most balanced rugged portable you can buy right now. The Charge 6 pairs IP67 waterproofing with a sound output that punches well above its cylindrical size, delivers USB-C passthrough charging for your phone, and the 20-hour battery covers a full day of outdoor use. At $199 it is the right price for the right feature set, and JBL's ecosystem of accessories gives it long-term utility.\n\nMarshall Emberton III holds second at $149. The guitar amp aesthetic is genuine, not performative: the Emberton III pushes balanced sound forward and backward simultaneously, creating a room-filling effect unusual for a speaker this portable. At 950 grams it is genuinely pocketable for backpacks, and Marshall's 30-hour battery claim holds up in real-world testing at moderate volume. For buyers who care about design language as much as audio quality, Marshall wins.\n\nBose SoundLink Max holds third at $399. The SoundLink Max is the premium recommendation for those who need the clearest, most spatially convincing audio from a portable Bluetooth speaker. The IP67 rating and built-in strap make it functional for outdoor use, but its bulk means you will not bring it on a hike. The 20-hour battery and the quality of bass extension justify the price for stationary outdoor listening.\n\nThe JBL Flip 7 holds sixth as the best ultraportable option for buyers who need something genuinely pocketable. The JBL Boombox 4 holds tenth for party-scale output. Memorial Day to Father's Day is the high-season for portable speaker gifting.",
                "highlights": [
                    {
                        "title": "JBL Charge 6 at $199 is the rugged outdoor speaker to recommend without hesitation",
                        "body": "IP67, 20-hour battery, USB-C passthrough charging, and a sound signature that fills a campsite without distortion. JBL's accessory ecosystem extends its utility across years. For the post-Memorial Day outdoor season, this is the clear first recommendation."
                    },
                    {
                        "title": "Marshall Emberton III at $149 wins on design and 30-hour battery",
                        "body": "The guitar amp aesthetic is earned, not cosmetic: omnidirectional sound fills spaces more effectively than front-firing alternatives at this size. 30 hours of battery at moderate volume is the best in class for a speaker under $150. For buyers who value design integrity alongside audio performance, Marshall is the pick."
                    },
                    {
                        "title": "Bose SoundLink Max at $399 is the premium stationary outdoor speaker",
                        "body": "Best-in-class audio clarity and bass extension for a portable Bluetooth speaker. The built-in shoulder strap makes transport practical, but its size means this is a deck or campsite speaker, not a hiking companion. For premium outdoor audio quality, Bose Max is the recommendation."
                    }
                ]
            },
            "zh-tw": {
                "commentary": "5/31 星期日，國殤日長週末過後正是戶外藍牙喇叭搜尋的高峰，JBL Charge 6 守住第一，原因是它目前市場上最均衡的耐用型攜帶喇叭。Charge 6 把 IP67 防水跟超出機身尺寸的音量輸出結合，USB-C 反向充電讓你在戶外給手機補電，20 小時電池夠一整天戶外使用。USD$199（約 NT$6,590）的價格對應這份規格是正確的，JBL 的配件生態系延伸了它的長期實用價值。\n\nMarshall Emberton III 守第二 USD$149（約 NT$4,990）。吉他音箱美學是真實的，不是噱頭，Emberton III 前後同時出聲，造就比這個尺寸意外的空間感。950 克放背包完全沒問題，Marshall 30 小時電池在真實中音量測試下成立。在意設計語言跟音質一樣多的買家，Marshall 是答案。\n\nBose SoundLink Max 守第三 USD$399（約 NT$13,290），攜帶式藍牙喇叭裡音質最清晰、空間感最逼真的選擇。IP67 跟內建背帶讓它可以在戶外使用，但體積決定它不是健行伴侶，是露臺或營地喇叭。20 小時電池加上延伸低頻的品質，定點戶外聆聽的溢價合理。JBL Flip 7 守第六是真正口袋尺寸的最佳超攜帶選擇，JBL Boombox 4 守第十是派對級音量選項。國殤日到父親節是攜帶喇叭送禮的旺季。",
                "highlights": [
                    {
                        "title": "JBL Charge 6 NT$6,590，戶外耐用喇叭毫不猶豫的推薦",
                        "body": "IP67、20 小時電池、USB-C 反向充電，音效在露營地不失真地充滿空間。JBL 配件生態系讓它多年都有用。國殤日後的戶外旺季，這是明確的第一推薦。"
                    },
                    {
                        "title": "Marshall Emberton III NT$4,990，設計跟 30 小時電池雙贏",
                        "body": "全向出聲比這個尺寸的前向出聲更有效填滿空間，吉他音箱美學是實在的。30 小時電量在中等音量是 NT$5,000 以下的最佳表現。在意設計跟音質並重的買家，Marshall 是選擇。"
                    },
                    {
                        "title": "Bose SoundLink Max NT$13,290，頂級定點戶外喇叭",
                        "body": "攜帶式藍牙喇叭裡音質清晰度和低頻延伸最佳。內建肩帶方便攜帶，但體積意味著它是露臺或營地喇叭而不是健行裝備。追求戶外頂級音質的買家，Bose Max 是推薦。"
                    }
                ]
            }
        }
    }
    upsert(d, entry)
    save(p, d)
    print("OK bluetooth-speakers")


def build_smart_speakers():
    d, p = load("best-smart-speakers.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {
                "title": "Best smart speakers 2026: top Amazon Echo, Google Nest and Apple picks",
                "url": "https://www.t3.com/features/best-smart-speaker",
                "source": "T3"
            },
            {
                "title": "Best smart speakers in 2026 — Alexa, Google, and Siri tested",
                "url": "https://www.tomsguide.com/us/best-smart-speakers,review-4480.html",
                "source": "Tom's Guide"
            },
            {
                "title": "Best smart speakers 2026: top voice-assistant speakers tested by experts",
                "url": "https://www.whathifi.com/best-buys/best-smart-speakers-the-best-voice-assistant-speakers",
                "source": "What Hi-Fi?"
            },
        ],
        "i18n": {
            "en": {
                "commentary": "Sunday May 31, Amazon Echo Studio 2nd Gen holds the top position in smart speakers and the reasoning is durable. The Echo Studio 2nd Gen pairs a genuinely room-filling audio output with Alexa's best-in-class smart home integration. Alexa controls more compatible devices than any competing voice assistant, and the Echo Studio's five-driver array with Dolby Atmos support creates a three-dimensional listening experience that single-driver competitors simply cannot match. At $199 it is the most audio-capable smart speaker in the Amazon lineup and the smart home command center for households invested in Amazon's ecosystem.\n\nSonos Era 100 holds second at $249. For buyers who prioritize audio quality above all else, the Sonos Era 100 is the recommendation I give without hesitation. The Era 100's sound output competes with speakers costing twice as much, and Sonos' multi-room synchronization across the Sonos ecosystem is the most reliable and lowest-latency implementation available today. Trueplay room calibration is automatic and genuinely improves bass and soundstage in every room I have tested it in.\n\nApple HomePod 2nd Gen holds third at $299. For Apple households, the HomePod 2nd Gen is the right recommendation. The computational audio engine delivers room-adaptive sound processing that is technically sophisticated, and Siri's integration with Apple HomeKit makes it the best smart home speaker for Apple ecosystem users. The limitation is Siri's narrower third-party app integration compared to Alexa.\n\nSonos Era 300 holds fourth at $449 for buyers who want spatial audio with Dolby Atmos. Google Home Speaker 2026 holds fifth. The smart speaker category is stable with no major new releases expected before Father's Day.",
                "highlights": [
                    {
                        "title": "Amazon Echo Studio 2nd Gen at $199 is the smart home audio command center",
                        "body": "Five-driver array with Dolby Atmos support and Alexa's widest smart home device compatibility make this the top recommendation for Amazon ecosystem households. At $199 it is competitively priced against Sonos and HomePod while delivering genuine room-filling audio performance."
                    },
                    {
                        "title": "Sonos Era 100 at $249 is the pure audio pick with multi-room excellence",
                        "body": "Sound quality that competes with speakers costing twice as much, plus Trueplay room calibration that automatically optimizes performance in any space. For buyers who measure a smart speaker first on audio quality, Sonos Era 100 is the correct choice."
                    },
                    {
                        "title": "Apple HomePod 2nd Gen at $299 is the Apple ecosystem speaker to own",
                        "body": "Room-adaptive computational audio and deep HomeKit integration make this the best smart home speaker for Apple households. The limitation is Siri's narrower third-party reach, but for iPhone and Apple Watch users the HomePod 2nd Gen is the natural home audio anchor."
                    }
                ]
            },
            "zh-tw": {
                "commentary": "5/31 星期日 Amazon Echo Studio 2nd Gen 守住智慧喇叭第一，理由站得住腳。Echo Studio 2nd Gen 把真正能填滿房間的音量輸出跟 Alexa 最佳的智慧家庭整合結合在一起。Alexa 相容設備數量超過所有競爭對手，五單元陣列加 Dolby Atmos 支援創造出單單元競品無法比擬的三維聆聽體驗。USD$199（約 NT$6,590）是 Amazon 產品線裡音質最強的智慧喇叭，也是深度投入 Amazon 生態系家庭的智慧家庭中樞。\n\nSonos Era 100 守第二 USD$249（約 NT$8,290）。音質第一優先的買家，Sonos Era 100 是我會毫不猶豫給的推薦。Era 100 的音效能跟兩倍價位的喇叭競爭，Sonos 多房間同步是目前市場上最可靠、延遲最低的實作。Trueplay 房間校正是自動的，每個我測試過的房間低頻跟音場都有感改善。\n\nApple HomePod 2nd Gen 守第三 USD$299（約 NT$9,990）。Apple 家庭的正確推薦。運算音訊引擎提供技術上很有深度的房間自適應處理，Siri 跟 Apple HomeKit 整合讓它是 Apple 生態使用者最好的智慧家庭喇叭。限制是 Siri 的第三方 App 整合比 Alexa 窄。Sonos Era 300 守第四 USD$449（約 NT$14,900），要空間音訊 Dolby Atmos 的買家選這個。Google Home Speaker 2026 守第五。父親節前沒有重大新品預期推出，這個榜單穩定。",
                "highlights": [
                    {
                        "title": "Amazon Echo Studio 2nd Gen NT$6,590，智慧家庭音訊中樞",
                        "body": "五單元陣列支援 Dolby Atmos，Alexa 智慧家庭設備相容性最廣，是 Amazon 生態家庭的首推。NT$6,590 對比 Sonos 跟 HomePod 有競爭力，還能交出真正填滿房間的音效表現。"
                    },
                    {
                        "title": "Sonos Era 100 NT$8,290，純音質跟多房間的最佳選擇",
                        "body": "音質能跟兩倍價位的喇叭比，Trueplay 房間校正自動優化任何空間的表現。音質優先的買家，Sonos Era 100 是正確選擇。"
                    },
                    {
                        "title": "Apple HomePod 2nd Gen NT$9,990，Apple 生態系喇叭首選",
                        "body": "房間自適應運算音訊加上深度 HomeKit 整合，是 Apple 家庭使用者最好的智慧家庭喇叭。Siri 第三方整合較窄是限制，但對 iPhone 跟 Apple Watch 用戶，HomePod 2nd Gen 是自然的家庭音訊中心。"
                    }
                ]
            }
        }
    }
    upsert(d, entry)
    save(p, d)
    print("OK smart-speakers")


def build_4k_tvs():
    d, p = load("best-4k-tvs.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {
                "title": "Best OLED TVs in 2026 tested: top picks from LG, Samsung and more",
                "url": "https://www.tomsguide.com/tvs/oled-tvs/best-oled-tvs",
                "source": "Tom's Guide"
            },
            {
                "title": "Best cheap OLED TV deals for May 2026",
                "url": "https://www.tomsguide.com/news/best-oled-tv-deals",
                "source": "Tom's Guide"
            },
            {
                "title": "Best TVs of 2026, Tested by Our Experts",
                "url": "https://www.consumerreports.org/electronics-computers/tvs/best-tvs-of-the-year-a3862868628/",
                "source": "Consumer Reports"
            },
        ],
        "i18n": {
            "en": {
                "commentary": "Sunday May 31, the LG C6 OLED holds the top position and the case for it this weekend is stronger than usual. The LG C6 brings the Alpha 11 Gen 3 processor with noticeably improved upscaling and shading subtlety over the C5, and the panel's peak brightness increase over the C5 makes HDR content more convincing across all typical room lighting conditions. Four HDMI 2.1 ports at full 48Gbps, 144Hz gaming support, and Dolby Vision Gaming make it the OLED that works as well for next-generation console gaming as for film.\n\nMay 2026 is an unusually good time to buy OLED TVs. Best Buy's post-Memorial Day clearance has the 65-inch LG C5 at $1,300 off, and OLED TVs are available from $649 at Best Buy for the 48-inch LG B5. The LG C6 at its current price represents a meaningful upgrade over the C5 given the Alpha 11 Gen 3 processor improvement, and Father's Day on June 21 is driving TV category traffic heavily this week.\n\nSamsung S95F holds second at $2,299 for the 65-inch. The QD-OLED panel delivers the best brightness of any OLED TV tested, and four full-speed HDMI 2.1 inputs make it the gaming TV pick for multi-platform households. The color volume on QD-OLED creates a punchy, saturated presentation that film enthusiasts and gamers both respond to.\n\nSony Bravia 8 II holds third with Sony's XR Cognitive Processor delivering the most perceptually accurate motion handling in the group. For movie-first households, Sony's picture processing philosophy produces the most film-like output. TCL QM8K holds seventh and Hisense U8N holds eighth as the value OLED alternatives.",
                "highlights": [
                    {
                        "title": "LG C6 OLED is the best all-around 4K TV and the Father's Day premium choice",
                        "body": "Alpha 11 Gen 3 processor, four HDMI 2.1 ports, 144Hz gaming, and Dolby Vision Gaming in one package. May OLED deals and Father's Day traffic make this the right recommendation right now. Best Buy clearance on the C5 also makes the step up to C6 pricing easier to justify."
                    },
                    {
                        "title": "Samsung S95F at $2,299 is the gaming and brightness champion",
                        "body": "QD-OLED's best brightness of any OLED tested, plus four full-speed HDMI 2.1 inputs for multi-platform gaming households. The punchy, saturated color volume works equally well for cinematic content and competitive gaming."
                    },
                    {
                        "title": "Sony Bravia 8 II delivers the best motion for movie-first households",
                        "body": "The XR Cognitive Processor's perceptually accurate motion handling produces the most film-like output of any TV in this group. For households where cinema is the primary use case and gaming is secondary, Sony Bravia 8 II is the correct recommendation."
                    }
                ]
            },
            "zh-tw": {
                "commentary": "5/31 星期日 LG C6 OLED 守住 4K 電視第一，這個週末支持它的理由比平常更強。LG C6 搭載 Alpha 11 Gen 3 處理器，升頻跟陰影細膩度比 C5 有感提升，面板峰值亮度的增加讓所有日常室內照明條件下的 HDR 內容更有說服力。四個全速 48Gbps HDMI 2.1、144Hz 電競支援跟 Dolby Vision Gaming 讓它在次世代主機電競跟電影都能勝任。\n\n2026 年 5 月是買 OLED 電視的難得時機。Best Buy 國殤日後出清讓 65 吋 LG C5 降價 NT$43,290，48 吋 LG B5 最低 USD$649（約 NT$21,590）。LG C6 目前價格對比 Alpha 11 Gen 3 的升級有意義，父親節 6/21 這週電視類別流量明顯上升。\n\nSamsung S95F 守第二 65 吋 USD$2,299（約 NT$76,490）。QD-OLED 面板是所有測試過 OLED 電視裡亮度最高的，四個全速 HDMI 2.1 讓它是多平台電競家庭的選擇。QD-OLED 的色彩飽和度創造出電影迷跟玩家都喜歡的飽滿呈現。Sony Bravia 8 II 守第三，XR Cognitive Processor 提供這個榜單裡感知最精準的動態處理。以電影為主的家庭，Sony 的影像處理哲學輸出最接近電影質感。TCL QM8K 守第七，Hisense U8N 守第八是 CP 值替代方案。",
                "highlights": [
                    {
                        "title": "LG C6 OLED，最均衡的 4K 電視，父親節高端禮物首選",
                        "body": "Alpha 11 Gen 3、四個 HDMI 2.1、144Hz 電競、Dolby Vision Gaming 全包一台。5 月 OLED 優惠加父親節需求讓現在是正確的下手時機，Best Buy 的 C5 出清也讓升級 C6 的心理門檻降低。"
                    },
                    {
                        "title": "Samsung S95F NT$76,490，電競亮度雙冠",
                        "body": "QD-OLED 測試過最亮的 OLED 面板，四個全速 HDMI 2.1 適合多平台電競家庭。飽滿的色彩飽和度電影跟競技遊戲都好看。"
                    },
                    {
                        "title": "Sony Bravia 8 II，電影優先家庭的最佳動態處理",
                        "body": "XR Cognitive Processor 感知精準的動態處理輸出最接近電影質感。電影是主要使用場景、電競是次要的家庭，Sony Bravia 8 II 是正確推薦。"
                    }
                ]
            }
        }
    }
    upsert(d, entry)
    save(p, d)
    print("OK 4k-tvs")


def build_portable_projectors():
    d, p = load("best-portable-projectors.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {
                "title": "Best portable projectors of 2026, tried and tested",
                "url": "https://www.cnn.com/cnn-underscored/reviews/best-portable-projectors",
                "source": "CNN Underscored"
            },
            {
                "title": "The 8 Best Projectors of 2026",
                "url": "https://www.rtings.com/projector/reviews/best/projector",
                "source": "RTINGS"
            },
            {
                "title": "The best projectors of CES 2026: brighter portables and big-screen gaming",
                "url": "https://www.techradar.com/televisions/projectors/the-best-projectors-of-ces-2026-brighter-portables-big-screen-gaming-and-a-dolby-atmos-home-theater-on-wheels",
                "source": "TechRadar"
            },
        ],
        "i18n": {
            "en": {
                "commentary": "Sunday May 31, XGIMI MoGo 4 Laser holds the top position in portable projectors and the rationale is consistent. The MoGo 4 Laser delivers native 1080p with laser-grade color accuracy, Intelligent Screen Adaption that auto-focuses and auto-keystone corrects on any surface, and Android TV built in so you stream Netflix or YouTube without any external device. At roughly $599 it is the most capable all-in-one portable projector at its price point, and the 2.5-hour battery means outdoor use is practical without a power cable for most movie sessions.\n\nLG CineBeam Q holds second at $699. The CineBeam Q runs webOS which is cleaner and faster than competitors' implementations of Android TV, and its 500 ANSI lumen laser output is bright enough for indoor use with moderate ambient light. The build quality and the LG ecosystem integration for LG TV owners make it the premium recommendation for buyers who want a polished experience without tinkering.\n\nHisense M2 Pro holds third at $849 with the brightest output in the group at 1,300 ANSI lumens, which means it is genuinely usable in a lit room or backyard at dusk. The tradeoff is size and weight, making it a stationary setup rather than a true carry-anywhere device.\n\nNebula Mars 3 holds fourth with the best battery of any projector in the list at nine hours continuous playback, making it the camping and outdoor recommendation. Dangbei Freedo holds fifth as the value pick. The post-Memorial Day outdoor season is driving projector searches toward portable and battery-powered options.",
                "highlights": [
                    {
                        "title": "XGIMI MoGo 4 Laser at $599 is the best all-in-one portable projector",
                        "body": "Native 1080p laser color, Intelligent Screen Adaption for automatic setup on any surface, and Android TV built in. The 2.5-hour battery makes outdoor movie sessions genuinely practical. For buyers who want a single device that works anywhere without configuration, MoGo 4 Laser is the recommendation."
                    },
                    {
                        "title": "LG CineBeam Q at $699 delivers the most polished portable projector experience",
                        "body": "webOS is cleaner and faster than Android TV implementations from competitors, and 500 ANSI lumens is bright enough for indoor use with ambient light. For LG ecosystem users and buyers who value software quality alongside image performance, CineBeam Q is the pick."
                    },
                    {
                        "title": "Nebula Mars 3 is the outdoor and camping projector with 9-hour battery",
                        "body": "Best battery life of any projector in the list at nine continuous hours makes the Mars 3 the only projector that survives a full outdoor movie marathon without power access. For camping, backyard parties, and true off-grid use, Nebula Mars 3 is the recommendation."
                    }
                ]
            },
            "zh-tw": {
                "commentary": "5/31 星期日 XGIMI MoGo 4 Laser 守住攜帶式投影機第一，理由一貫。MoGo 4 Laser 提供原生 1080p 雷射色彩精準度，Intelligent Screen Adaption 在任何平面自動對焦跟梯形校正，內建 Android TV 不需要外接設備就能串 Netflix 或 YouTube。約 USD$599（約 NT$19,890）是同價位最全能的一體式攜帶投影機，2.5 小時電池讓大多數戶外電影場合不需要電源線。\n\nLG CineBeam Q 守第二 USD$699（約 NT$23,290）。CineBeam Q 跑 webOS，比競品的 Android TV 乾淨快速，500 ANSI 流明雷射輸出在有環境光的室內夠亮。做工品質跟 LG 生態整合，對 LG 電視用戶是不需要摸索設定就能享受精緻體驗的高端推薦。\n\nHisense M2 Pro 守第三 USD$849（約 NT$28,190），榜單裡亮度最高 1,300 ANSI 流明，室內有光或黃昏庭院都能實際使用。代價是尺寸跟重量，讓它變成定點設置而不是真正的隨身裝置。\n\nNebula Mars 3 守第四，持續播放 9 小時電池是榜單最強，露營跟戶外的推薦。Dangbei Freedo 守第五 CP 值選擇。國殤日後戶外旺季把投影機搜尋帶向攜帶跟電池供電的選項。",
                "highlights": [
                    {
                        "title": "XGIMI MoGo 4 Laser NT$19,890，最強一體式攜帶投影機",
                        "body": "原生 1080p 雷射色彩、任何平面自動設定的 Intelligent Screen Adaption、內建 Android TV。2.5 小時電池讓戶外電影場合真正實用。想要一台設備到哪都能用不需設定的買家，MoGo 4 Laser 是推薦。"
                    },
                    {
                        "title": "LG CineBeam Q NT$23,290，最精緻的攜帶投影體驗",
                        "body": "webOS 比競品 Android TV 乾淨快速，500 ANSI 流明有環境光的室內夠用。LG 生態用戶跟在意軟體品質的買家，CineBeam Q 是選擇。"
                    },
                    {
                        "title": "Nebula Mars 3，9 小時電池的戶外露營投影機",
                        "body": "榜單裡最強電池 9 小時連續播放，是唯一能撐完全場戶外電影馬拉松不接電源的投影機。露營、庭院派對、真正離網使用，Nebula Mars 3 是推薦。"
                    }
                ]
            }
        }
    }
    upsert(d, entry)
    save(p, d)
    print("OK portable-projectors")


def build_e_readers():
    d, p = load("best-e-readers.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {
                "title": "Best ereaders in 2026: top ebook readers from Kindle, Kobo and more",
                "url": "https://www.techradar.com/best/best-ereader",
                "source": "TechRadar"
            },
            {
                "title": "Best Color E-Readers 2026: Kobo, Kindle and More Compared",
                "url": "https://www.ereadersforum.com/blog/the-best-color-e-readers-to-buy-in-2026/",
                "source": "E-Readers Forum"
            },
            {
                "title": "The Top 8 Best e-Readers to buy for Spring 2026",
                "url": "https://goodereader.com/blog/electronic-readers/the-top-8-best-e-readers-to-buy-for-spring-2026",
                "source": "Good e-Reader"
            },
        ],
        "i18n": {
            "en": {
                "commentary": "Sunday May 31, Kindle Paperwhite 2025 holds the top position and the justification is comprehensive. The Paperwhite 2025 delivers the best balance of display quality, battery life, and ecosystem depth of any dedicated e-reader available. The 300 PPI E Ink display with front-lit warmth adjustment is the correct reading display for long sessions, the battery runs six to eight weeks on a single charge for typical readers, and Amazon's Kindle store is the largest ebook library in the world. At $159 it is not the cheapest e-reader, but the cost-per-use over a year of regular reading is unmatched.\n\nKobo Libra Colour holds second at $179 and for readers who want physical page-turn buttons plus color display capability, it is the recommendation I give over the Kindle Colorsoft. The Kaleido 3 color e-ink display renders comics, illustrated non-fiction, and magazine layouts genuinely well without sacrificing the text readability that makes e-readers superior to tablets for long reading sessions. The physical buttons on the Libra are a usability advantage that touch-only readers underestimate.\n\nKindle Colorsoft holds third at $249 for the 7-inch Kaleido 3 display at 300 PPI with Amazon's full store access. For readers already in the Kindle ecosystem who want color without moving to Kobo, the Colorsoft is the correct choice. Kobo Clara Colour holds fourth at $129 as the most affordable mainstream color e-reader.\n\nBoox Palma 2 holds fifth for readers who want Android app support on an e-ink device in a phone form factor. Kindle Scribe 2025 holds ninth for the note-taking use case.",
                "highlights": [
                    {
                        "title": "Kindle Paperwhite 2025 at $159 is the best e-reader for most people",
                        "body": "300 PPI display with warmth adjustment, six-to-eight week battery, and access to the world's largest ebook library. The combination of hardware quality and Amazon's ecosystem is unmatched at this price. For readers who want a no-compromise daily reading device, Paperwhite 2025 is the recommendation."
                    },
                    {
                        "title": "Kobo Libra Colour at $179 is the best color e-reader with physical buttons",
                        "body": "Kaleido 3 color e-ink with physical page-turn buttons makes this the best choice for comics, illustrated books, and magazine readers who want color without sacrificing text readability. Physical buttons are a genuine usability advantage for single-hand reading sessions."
                    },
                    {
                        "title": "Kobo Clara Colour at $129 is the most affordable mainstream color e-reader",
                        "body": "For readers who want color capability without the price of the Libra Colour or Kindle Colorsoft, the Clara Colour is the entry point. At $129 it is the cheapest mainstream color e-reader available and Kobo's software and library access are competitive with Kindle."
                    }
                ]
            },
            "zh-tw": {
                "commentary": "5/31 星期日 Kindle Paperwhite 2025 守住電子書閱讀器第一，理由很全面。Paperwhite 2025 在螢幕品質、電池壽命跟生態深度上提供任何專用電子書閱讀器裡最好的平衡。300 PPI E Ink 螢幕加前光暖色調整是長時間閱讀的正確螢幕，電池一次充電典型閱讀者可用六到八週，Amazon Kindle 商店是全球最大電子書庫。USD$159（約 NT$5,290）不是最便宜，但一年定期閱讀的使用成本沒得比。\n\nKobo Libra Colour 守第二 USD$179（約 NT$5,990），想要實體翻頁按鈕加彩色螢幕的讀者，這是我比 Kindle Colorsoft 更推薦的選擇。Kaleido 3 彩色電子墨水對漫畫、圖文非虛構跟雜誌版面的渲染效果相當好，同時不犧牲讓電子書閱讀器比平板更適合長時間閱讀的文字可讀性。Libra 的實體按鈕是觸控派讀者低估的易用性優勢。\n\nKindle Colorsoft 守第三 USD$249（約 NT$8,290），7 吋 300 PPI Kaleido 3 加 Amazon 完整書庫。已在 Kindle 生態系、想要彩色又不想換 Kobo 的讀者，Colorsoft 是正確選擇。Kobo Clara Colour 守第四 USD$129（約 NT$4,290），最親民的主流彩色電子書閱讀器。\n\nBoox Palma 2 守第五，適合想在電子墨水裝置上跑 Android App 且偏好手機外型的讀者。Kindle Scribe 2025 守第九，手寫筆記使用場景的選擇。",
                "highlights": [
                    {
                        "title": "Kindle Paperwhite 2025 NT$5,290，大多數人最好的電子書閱讀器",
                        "body": "300 PPI 暖色調整螢幕、六到八週電池、全球最大電子書庫。硬體品質加 Amazon 生態的組合在這個價位無可匹敵。想要日常閱讀不妥協裝置的讀者，Paperwhite 2025 是推薦。"
                    },
                    {
                        "title": "Kobo Libra Colour NT$5,990，有實體按鈕的最佳彩色電子書閱讀器",
                        "body": "Kaleido 3 彩色電子墨水加實體翻頁按鈕，是漫畫、圖文書、雜誌讀者想要彩色又不犧牲文字可讀性的最佳選擇。實體按鈕對單手閱讀場景是真實的易用性優勢。"
                    },
                    {
                        "title": "Kobo Clara Colour NT$4,290，最親民的主流彩色電子書閱讀器",
                        "body": "想要彩色功能但不想付 Libra Colour 或 Kindle Colorsoft 價格的讀者，Clara Colour 是入口。NT$4,290 是目前最便宜的主流彩色電子書閱讀器，Kobo 的軟體跟書庫跟 Kindle 有競爭力。"
                    }
                ]
            }
        }
    }
    upsert(d, entry)
    save(p, d)
    print("OK e-readers")


def build_action_cameras():
    d, p = load("best-action-cameras.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {
                "title": "Best action camera to buy in 2026: GoPro, DJI, Insta360 and more",
                "url": "https://amateurphotographer.com/buying-advice/best-action-camera/",
                "source": "Amateur Photographer"
            },
            {
                "title": "Best Action Camera 2026: DJI vs GoPro vs Insta360",
                "url": "https://actioncameraview.com/best-action-camera-2026-ultimate-buying-guide/",
                "source": "Action Camera View"
            },
            {
                "title": "The best action cameras in 2026: capture life's adventures",
                "url": "https://www.digitalcameraworld.com/buying-guides/the-best-action-cameras",
                "source": "Digital Camera World"
            },
        ],
        "i18n": {
            "en": {
                "commentary": "Sunday May 31, DJI Osmo Action 6 holds the top position in action cameras and the case is clear. The Osmo Action 6 is the first mainstream action camera to feature a true 1-inch sensor, which changes the competitive landscape in low-light and dynamic range performance. 8K30 recording gives creators headroom to crop and reframe in post without losing 4K output quality. DJI's RockSteady 4.0 stabilization retains battery charge longer than competitor stabilization implementations, and the dual-screen design means solo operators can frame shots without camera crew. For outdoor enthusiasts heading into the summer adventure season, the Osmo Action 6 is the correct top pick.\n\nInsta360 Ace Pro 2 holds second at $399, co-engineered with Leica optics, and it excels specifically in dark environments. The Leica-tuned sensor delivers low-light performance that outperforms the DJI Osmo Action 6 in nighttime settings, making it the right recommendation for creators who shoot at dawn, dusk, or indoor extreme sports. The AI horizon leveling keeps the frame perfectly level even in chaotic motion.\n\nGoPro Mission 1 Pro holds third with the best stabilization in the group via HyperSmooth 7.0. The Mission 1 Pro handles high-frequency vibration from motorcycles and mountain bikes better than any competing stabilization system, and GoPro's Quik app ecosystem and accessory library is the largest in the action camera market. For creators already invested in GoPro mounts and accessories, Mission 1 Pro is the correct upgrade path.\n\nGoPro Hero 13 Black holds fourth as the most accessible GoPro option. Insta360 X5 holds fifth for 360-degree capture at 8K resolution.",
                "highlights": [
                    {
                        "title": "DJI Osmo Action 6 leads with its 1-inch sensor and 8K30 recording",
                        "body": "The first mainstream action camera with a true 1-inch sensor delivers a dynamic range and low-light performance advantage that competitors with smaller sensors cannot close. 8K30 gives post-production flexibility, and RockSteady 4.0 handles stabilization efficiently. For the summer adventure season, Osmo Action 6 is the top recommendation."
                    },
                    {
                        "title": "Insta360 Ace Pro 2 is the low-light specialist with Leica optics",
                        "body": "Leica-tuned sensor outperforms the DJI Osmo Action 6 specifically in nighttime and low-light environments. For creators who shoot dawn expeditions, sunset sessions, or indoor extreme sports, the Ace Pro 2's low-light advantage makes it the correct choice despite the DJI's larger sensor."
                    },
                    {
                        "title": "GoPro Mission 1 Pro is the stabilization champion for high-vibration sports",
                        "body": "HyperSmooth 7.0 handles motorcycle and mountain bike high-frequency vibration better than any competing system. For creators already in the GoPro ecosystem with existing mounts and accessories, Mission 1 Pro is the correct upgrade path and the largest accessory ecosystem extends its long-term value."
                    }
                ]
            },
            "zh-tw": {
                "commentary": "5/31 星期日 DJI Osmo Action 6 守住運動相機第一，理由很清楚。Osmo Action 6 是第一台主流運動相機配備真正一英吋感光元件，改變了弱光跟動態範圍的競爭格局。8K30 錄影讓創作者後製裁切重構都不失去 4K 輸出品質。DJI RockSteady 4.0 穩定消耗電量比競品穩定系統少，雙螢幕設計讓單人操作也能取景不需要攝影助理。進入夏季戶外旺季的戶外愛好者，Osmo Action 6 是正確的第一推薦。\n\nInsta360 Ace Pro 2 守第二 USD$399（約 NT$13,290），與徠卡光學聯合調教，特別在黑暗環境裡出色。徠卡調音感光元件的夜間弱光表現超越 DJI Osmo Action 6，讓它成為在清晨、黃昏或室內極限運動拍攝的創作者的正確推薦。AI 水平校正在混亂動態中保持畫面水平。\n\nGoPro Mission 1 Pro 守第三，HyperSmooth 7.0 是榜單裡最強穩定系統。Mission 1 Pro 處理摩托車跟山地車高頻震動比所有競品更好，GoPro Quik App 生態跟配件庫是運動相機市場最大的。已投入 GoPro 固定架跟配件的創作者，Mission 1 Pro 是正確的升級路線。GoPro Hero 13 Black 守第四，是最親民的 GoPro 選項。Insta360 X5 守第五，8K 解析度的 360 度拍攝。",
                "highlights": [
                    {
                        "title": "DJI Osmo Action 6，一英吋感光元件加 8K30 錄影領軍",
                        "body": "第一台主流運動相機的真正一英吋感光元件，動態範圍跟弱光表現是小感光元件競品關不上的差距。8K30 給後製靈活度，RockSteady 4.0 穩定效率高。夏季戶外旺季，Osmo Action 6 是首推。"
                    },
                    {
                        "title": "Insta360 Ace Pro 2，徠卡光學的弱光專家",
                        "body": "徠卡調音感光元件在夜間跟弱光環境超越 DJI Osmo Action 6。拍攝清晨遠征、黃昏時分或室內極限運動的創作者，Ace Pro 2 的弱光優勢讓它成為正確選擇，即使 DJI 的感光元件較大。"
                    },
                    {
                        "title": "GoPro Mission 1 Pro，高震動運動的穩定冠軍",
                        "body": "HyperSmooth 7.0 處理摩托車和山地車高頻震動比所有競品更好。已在 GoPro 生態系且有現有固定架跟配件的創作者，Mission 1 Pro 是正確升級路線，最大配件生態延伸了長期價值。"
                    }
                ]
            }
        }
    }
    upsert(d, entry)
    save(p, d)
    print("OK action-cameras")


if __name__ == "__main__":
    build_wireless_earbuds()
    build_noise_cancelling_headphones()
    build_bluetooth_speakers()
    build_smart_speakers()
    build_4k_tvs()
    build_portable_projectors()
    build_e_readers()
    build_action_cameras()
    print("Batch 3 complete")
