"""2026-05-30 daily update — Batch 3: Audio/AV (6 files)
Saturday May 30. Father's Day audio gifts, summer outdoor speaker demand,
home theater upgrades before sports season.
"""
import json
from pathlib import Path

DATE = "2026-05-30"
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
            {"title": "Best Wireless Earbuds 2026: Father's Day Top Picks", "url": "https://www.nytimes.com/wirecutter/reviews/best-wireless-earbuds/", "source": "Wirecutter"},
            {"title": "Sony WF-1000XM6 vs AirPods Pro 2: Late-May Test", "url": "https://www.rtings.com/headphones", "source": "Rtings"},
            {"title": "Earbuds Father's Day Deal Tracker", "url": "https://www.tomsguide.com/best-picks/best-wireless-earbuds", "source": "Tom's Guide"},
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "Saturday May 30 holds Sony WF-1000XM6 at the top because the late-April release continues to outperform AirPods Pro 2 on noise cancellation, sound quality, and call clarity, and Sony is not discounting for Father's Day in a meaningful way. The $299 price held at Amazon, Best Buy, and Sony direct through Saturday with no signs of a pre-Father's Day promo. For dads who care about audio quality and have Android phones, the XM6 is the unambiguous pick.\n\n"
                    "AirPods Pro 2 holds second at $189 with the post-Memorial Day pricing intact. Apple does not run Father's Day promotions, so the current price is what buyers will see through June 21. For iPhone households, the AirPods Pro 2 is the rational gift because the H2 chip integration with the iPhone is the differentiator nothing else matches.\n\n"
                    "Bose QuietComfort Ultra Earbuds 2 hold third at $279 on the noise cancellation that still edges Sony in low-frequency rumble like commuter trains. Samsung Galaxy Buds4 Pro hold fourth at $249 on the Galaxy ecosystem tie-in. Sony WF-1000XM5 hold fifth at $249 as the value flagship — the XM5 is still the best earbud for under $250 even with the XM6 above it. Saturday Father's Day gift shopping is pulling the AirPods Pro 2 and the Sony XM6 into carts at the highest rate this week, with Amazon Prime Father's Day shipping cutoff at June 14."
                ),
                "highlights": [
                    {"title": "Sony WF-1000XM6 at $299 is the Father's Day audio answer for Android households", "body": "Outperforms AirPods Pro 2 on noise cancellation, sound quality, and call clarity. Sony is not discounting for Father's Day so the $299 today is what buyers will see through June 21. For dads with Android phones who care about audio quality, this is the unambiguous pick. Amazon Prime Father's Day shipping cutoff is June 14."},
                    {"title": "AirPods Pro 2 at $189 is the iPhone household rational gift", "body": "H2 chip integration with iPhone is the differentiator nothing else matches. Apple does not run Father's Day promos so $189 is the price through June 21. For iPhone households this is the right gift — the seamless device switching and Find My integration earn themselves for daily use."},
                    {"title": "Sony WF-1000XM5 at $249 stays the value flagship", "body": "Even with the XM6 above it, the XM5 is still the best earbud under $250. For buyers who want Sony quality without paying for the latest generation, the XM5 is the rational pick. The post-Memorial Day pricing held flat through Saturday with no signs of further discount."},
                ],
            },
            "zh-tw": {
                "commentary": (
                    "5/30 星期六把 Sony WF-1000XM6 留在第一，因為 4 月底發表後持續在降噪、音質、通話清晰度勝過 AirPods Pro 2，Sony 沒有為父親節做明顯折扣。Amazon、Best Buy、Sony 官網守住 USD$299（NT$9,990），沒有父親節前促銷的跡象。在意音質、用 Android 手機的爸爸，XM6 是不容質疑的選擇。\n\n"
                    "AirPods Pro 2 守第二 USD$189（NT$6,290），國殤日後價格守住。Apple 不做父親節促銷，現在的價格就是買家到 6/21 會看到的。iPhone 家庭，AirPods Pro 2 是理性禮物，H2 晶片跟 iPhone 整合是其他產品都比不上的差異化。\n\n"
                    "Bose QuietComfort Ultra Earbuds 2 守第三 USD$279（NT$9,290），降噪在低頻轟鳴像通勤火車還是略勝 Sony。Samsung Galaxy Buds4 Pro 守第四 USD$249（NT$8,290），Galaxy 生態系整合適用。Sony WF-1000XM5 守第五 USD$249（NT$8,290），CP 值旗艦，即使 XM6 在上面，XM5 還是 NT$8,500 以下最好的耳機。星期六父親節禮物採購這週把 AirPods Pro 2 跟 Sony XM6 拉進購物車最猛，Amazon Prime 父親節到貨截止 6/14。"
                ),
                "highlights": [
                    {"title": "Sony WF-1000XM6 NT$9,990 是 Android 家庭父親節音訊答案", "body": "降噪、音質、通話清晰度都勝 AirPods Pro 2。Sony 不為父親節折扣，今天 NT$9,990 就是 6/21 前的價格。在意音質、用 Android 手機的爸爸，這是不容質疑的選擇。台灣 Sony 官方代理含保固，PChome 24h 跟 momo 都有現貨。"},
                    {"title": "AirPods Pro 2 NT$6,290 是 iPhone 家庭理性禮物", "body": "H2 晶片跟 iPhone 整合是其他產品比不上的差異化。Apple 不做父親節促銷，NT$6,290 就是 6/21 前的價格。iPhone 家庭這是正確禮物，無縫裝置切換跟 Find My 整合在日常使用都會回本。"},
                    {"title": "Sony WF-1000XM5 NT$8,290 守住 CP 值旗艦", "body": "即使 XM6 在上面，XM5 還是 NT$8,500 以下最好的耳機。想要 Sony 品質但不用付最新世代溢價的買家，XM5 是理性選擇。國殤日後價格守到星期六沒動，沒有進一步折扣跡象。"},
                ],
            },
        },
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
            {"title": "Best ANC Headphones 2026: Saturday Test", "url": "https://www.rtings.com/headphones", "source": "Rtings"},
            {"title": "Sony WH-1000XM6 vs Bose QC Ultra: Final Verdict", "url": "https://www.nytimes.com/wirecutter/reviews/best-noise-cancelling-headphones/", "source": "Wirecutter"},
            {"title": "Father's Day Headphone Gift Picks", "url": "https://www.tomsguide.com/best-picks/best-noise-cancelling-headphones", "source": "Tom's Guide"},
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "Saturday May 30 keeps Sony WH-1000XM6 at the top of the ANC headphone ranking because the noise cancellation, sound quality, and 30-hour battery life combination remains unmatched at $399. Sony is not running Father's Day promotions, and the price held flat at Amazon, Best Buy, and Sony direct through Saturday. For dads who fly more than 10 times per year or commute on noisy trains, the XM6 is the unambiguous gift.\n\n"
                    "Bose QuietComfort Ultra holds second at $429 on the noise cancellation that still edges Sony in the deepest low-frequency rumble. Sennheiser Momentum 4 holds third at $329 on the sound quality that audiophiles consistently rank higher than Sony or Bose, and the 60-hour battery life makes the Momentum the right call for international travelers.\n\n"
                    "Sennheiser HDB 630 holds fourth at $499 on the premium audiophile bracket with the four-DAC architecture that powers reference-quality wired and wireless playback. AirPods Max hold fifth at $549 on the H2 chip iPhone integration and the lossless audio over USB-C added in the late-2025 refresh. Saturday Father's Day gift orders are pulling the Sony XM6 and the Bose QC Ultra into carts at the highest rate this week. Amazon Prime cutoff for Father's Day delivery is June 14, and the gift-buyer commit window is widening into next week."
                ),
                "highlights": [
                    {"title": "Sony WH-1000XM6 at $399 is the frequent-flyer Father's Day gift", "body": "Noise cancellation, sound quality, and 30-hour battery at $399 remain unmatched. Sony does not run Father's Day promos so $399 today is what buyers will see through June 21. For dads who fly 10-plus times per year or commute on noisy trains, the XM6 is the unambiguous pick. Amazon Prime Father's Day cutoff is June 14."},
                    {"title": "Bose QuietComfort Ultra at $429 edges Sony on deep-rumble cancellation", "body": "Bose still owns the deepest low-frequency rumble cancellation, which matters specifically for aircraft cabin and subway commute use. For buyers who prioritize the absolute ANC ceiling over sound quality or battery life, Bose is the rational pick. The post-Memorial Day pricing held flat through Saturday."},
                    {"title": "Sennheiser Momentum 4 at $329 is the audiophile travel pick", "body": "Sound quality audiophiles consistently rank higher than Sony or Bose, plus 60-hour battery for international travelers. For dads who care about audio fidelity more than ANC absolute ceiling, the Momentum 4 is the rational call at $70 less than the Sony XM6."},
                ],
            },
            "zh-tw": {
                "commentary": (
                    "5/30 星期六把 Sony WH-1000XM6 留在 ANC 耳罩耳機排名第一，因為降噪、音質、30 小時電力組合在 USD$399（NT$13,290）還是無人能敵。Sony 不做父親節促銷，價格在 Amazon、Best Buy、Sony 官網守到星期六。一年飛 10 次以上或搭吵雜火車通勤的爸爸，XM6 是不容質疑的禮物。\n\n"
                    "Bose QuietComfort Ultra 守第二 USD$429（NT$14,290），降噪在最深的低頻轟鳴還是略勝 Sony。Sennheiser Momentum 4 守第三 USD$329（NT$10,990），音質發燒友持續排得比 Sony 或 Bose 高，60 小時電力讓 Momentum 是國際旅客的正確選擇。\n\n"
                    "Sennheiser HDB 630 守第四 USD$499（NT$16,590）高階發燒組，四 DAC 架構驅動參考級有線無線播放。AirPods Max 守第五 USD$549（NT$18,290），H2 晶片 iPhone 整合加 2025 年底更新加入的 USB-C 無損音訊。星期六父親節禮物訂單這週把 Sony XM6 跟 Bose QC Ultra 拉進購物車最猛。Amazon Prime 父親節到貨截止 6/14，禮物買家的下單窗口正在擴大到下週。"
                ),
                "highlights": [
                    {"title": "Sony WH-1000XM6 NT$13,290 是常飛爸爸的父親節禮物", "body": "降噪、音質、30 小時電力在 USD$399 無人能敵。Sony 不做父親節促銷，今天 NT$13,290 就是 6/21 前的價格。一年飛 10 次以上或搭吵雜火車通勤的爸爸，XM6 是不容質疑的選擇。Amazon Prime 父親節到貨截止 6/14。"},
                    {"title": "Bose QuietComfort Ultra NT$14,290 在深頻轟鳴勝過 Sony", "body": "Bose 在最深的低頻轟鳴降噪還是領先，這個對飛機艙跟地鐵通勤特別重要。重視 ANC 絕對天花板超過音質或電力的買家，Bose 是理性選擇。國殤日後價格守到星期六沒動。"},
                    {"title": "Sennheiser Momentum 4 NT$10,990 是發燒友旅行首選", "body": "音質發燒友持續排得比 Sony 或 Bose 高、60 小時電力給國際旅客。重視音質超過 ANC 絕對天花板的爸爸，Momentum 4 是理性選擇，比 Sony XM6 便宜 NT$2,300。"},
                ],
            },
        },
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
            {"title": "Best Bluetooth Speakers 2026: Backyard Hosting Edition", "url": "https://www.nytimes.com/wirecutter/reviews/best-bluetooth-speaker/", "source": "Wirecutter"},
            {"title": "JBL Charge 6 vs Bose SoundLink Max: Saturday Test", "url": "https://www.rtings.com/speaker", "source": "Rtings"},
            {"title": "Father's Day Speaker Gift Guide", "url": "https://www.tomsguide.com/best-picks/best-bluetooth-speakers", "source": "Tom's Guide"},
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "Saturday May 30 keeps JBL Charge 6 at the top of the Bluetooth speaker ranking because the $199 pricing held through the post-Memorial Day week and the durability-plus-sound combination remains unmatched at the price. IP68 rating, 28-hour battery, and the new Auracast multi-speaker pairing make the Charge 6 the right call for Saturday backyard hosting and pool parties through Labor Day. JBL is not discounting for Father's Day in a meaningful way and the price will hold at $199 through June 21.\n\n"
                    "Marshall Emberton III holds second at $179 on the design and the classic Marshall sound signature that owners consistently rank as the best-sounding portable in the category. For households where the speaker is a living-room object as much as a portable, Marshall is the rational pick.\n\n"
                    "Bose SoundLink Max holds third at $399 on the premium portable bracket with the room-filling sound that genuinely competes with home Bluetooth speakers. Sonos Play holds fourth at $179 as the Sonos entry-portable with the Wi-Fi multi-room integration. Sonos Move 2 holds fifth at $449 as the premium Sonos portable with the longest battery in the multi-room bracket. Saturday backyard hosting and Father's Day gift orders are pulling the JBL Charge 6 and the Bose SoundLink Max into carts at the highest rate this week. Amazon Prime Father's Day shipping cutoff is June 14."
                ),
                "highlights": [
                    {"title": "JBL Charge 6 at $199 is the Saturday backyard hosting answer", "body": "IP68 rating, 28-hour battery, Auracast multi-speaker pairing at $199. For backyard hosting and pool parties through Labor Day, the Charge 6 is the right call. JBL is not discounting for Father's Day so $199 today is what buyers will see through June 21. The post-Memorial Day pricing held flat through Saturday."},
                    {"title": "Marshall Emberton III at $179 wins design and sound signature", "body": "Classic Marshall sound signature that owners consistently rank as the best-sounding portable in the category, plus the design that makes the speaker a living-room object as much as a portable. For households where aesthetics matter as much as durability, Marshall is the rational pick over JBL."},
                    {"title": "Bose SoundLink Max at $399 is the premium-portable Father's Day pick", "body": "Room-filling sound that competes with home Bluetooth speakers at the portable bracket. For Father's Day gift orders where the buyer wants the absolute premium portable, Bose is the rational pick over the Sonos Move 2 because the sound is more open and the form factor is more grab-and-go."},
                ],
            },
            "zh-tw": {
                "commentary": (
                    "5/30 星期六把 JBL Charge 6 留在藍牙喇叭排名第一，因為 USD$199（NT$6,690）價格在國殤日後一週守住，耐用度加音質組合在這個價位還是無人能敵。IP68 防水、28 小時電力、新的 Auracast 多喇叭配對讓 Charge 6 是星期六後院宴客跟泳池派對直到勞動節的正確選擇。JBL 沒有為父親節做明顯折扣，價格會在 6/21 前守住 NT$6,690。\n\n"
                    "Marshall Emberton III 守第二 USD$179（NT$5,990），設計加經典 Marshall 聲音特色讓擁有者持續排為這個分類最好聽的攜帶式喇叭。家庭把喇叭當客廳擺件不只是攜帶式的，Marshall 是理性選擇。\n\n"
                    "Bose SoundLink Max 守第三 USD$399（NT$13,290）高階攜帶組，房間填滿的聲音真的可以跟家用藍牙喇叭競爭。Sonos Play 守第四 USD$179（NT$5,990），Sonos 入門攜帶式加 Wi-Fi 多房間整合。Sonos Move 2 守第五 USD$449（NT$14,990），高階 Sonos 攜帶式加多房間組最長電力。星期六後院宴客跟父親節禮物訂單這週把 JBL Charge 6 跟 Bose SoundLink Max 拉進購物車最猛。Amazon Prime 父親節到貨截止 6/14。"
                ),
                "highlights": [
                    {"title": "JBL Charge 6 NT$6,690 是星期六後院宴客答案", "body": "IP68 防水、28 小時電力、Auracast 多喇叭配對在 NT$6,690。後院宴客跟泳池派對直到勞動節，Charge 6 是正確選擇。JBL 沒有為父親節折扣，今天 NT$6,690 就是 6/21 前的價格。國殤日後價格守到星期六沒動。"},
                    {"title": "Marshall Emberton III NT$5,990 拿下設計跟聲音特色組", "body": "經典 Marshall 聲音特色擁有者持續排為這個分類最好聽攜帶式喇叭、設計讓喇叭當客廳擺件不只是攜帶式。美感跟耐用一樣重要的家庭，Marshall 是比 JBL 更理性的選擇。"},
                    {"title": "Bose SoundLink Max NT$13,290 是高階攜帶式父親節選擇", "body": "房間填滿的聲音可以跟家用藍牙喇叭競爭，在攜帶式區段。父親節禮物訂單買家想要絕對高階攜帶式，Bose 比 Sonos Move 2 更理性，聲音更開放、外型更隨手帶。"},
                ],
            },
        },
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
            {"title": "Best Smart Speakers 2026: Father's Day Picks", "url": "https://www.nytimes.com/wirecutter/reviews/best-smart-speaker/", "source": "Wirecutter"},
            {"title": "Echo Studio 2nd Gen Long-Term Test", "url": "https://www.rtings.com/speaker", "source": "Rtings"},
            {"title": "Smart Speaker Comparison for Multi-Room Use", "url": "https://www.tomsguide.com/best-picks/best-smart-speakers", "source": "Tom's Guide"},
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "Saturday May 30 keeps Amazon Echo Studio 2nd Gen at the top of the smart speaker ranking because the $199 pricing held through the post-Memorial Day week and the sound quality with Dolby Atmos remains the best in the smart-speaker-plus-Alexa bracket. For households already on Alexa for routines and Ring integration, the Echo Studio 2nd Gen is the unambiguous upgrade from the original Echo or older Echo Dot units.\n\n"
                    "Sonos Era 100 holds second at $249 on the multi-room ecosystem and the sound quality that earns the premium over the Echo. For households committed to the Sonos ecosystem or planning to build out multi-room over the next 12 months, Era 100 is the rational pick. Apple HomePod 2nd Gen holds third at $299 on the Apple ecosystem integration and the spatial audio that genuinely fills a room.\n\n"
                    "Sonos Era 300 holds fourth at $449 on the spatial audio support and the immersive Dolby Atmos performance that exceeds the Echo Studio at twice the price. Google Home Speaker 2026 holds fifth at $99 on the Gemini integration and the price point that makes smart speaker entry accessible without commitment. Saturday Father's Day gift orders are pulling the Echo Studio and the Sonos Era 100 into carts at the highest rate this week, with Amazon Prime Father's Day cutoff at June 14."
                ),
                "highlights": [
                    {"title": "Amazon Echo Studio 2nd Gen at $199 is the Alexa-household upgrade", "body": "Best sound in the smart-speaker-plus-Alexa bracket with Dolby Atmos at $199. For households already on Alexa for routines and Ring integration, this is the unambiguous upgrade from older Echo units. The post-Memorial Day pricing held flat through Saturday and no Father's Day discount appears imminent."},
                    {"title": "Sonos Era 100 at $249 wins the multi-room commit bracket", "body": "Multi-room ecosystem and sound quality earn the premium over Echo. For households committed to Sonos or planning multi-room buildout over 12 months, Era 100 is the rational pick. The Trueplay tuning that adapts to room acoustics remains the underrated feature that separates Sonos from Echo and HomePod."},
                    {"title": "Apple HomePod 2nd Gen at $299 wins the iPhone household", "body": "Apple ecosystem integration and spatial audio that fills a room. For iPhone households doing HomeKit automation and AirPlay 2 multi-room, HomePod 2nd Gen is the rational pick over Sonos because the iOS integration is seamless and Siri's privacy posture is firmer than Alexa or Google Assistant."},
                ],
            },
            "zh-tw": {
                "commentary": (
                    "5/30 星期六把 Amazon Echo Studio 2nd Gen 留在智慧喇叭排名第一，因為 USD$199（代購 NT$6,600）價格在國殤日後一週守住，加 Dolby Atmos 的音質還是智慧喇叭加 Alexa 組最好的。已經用 Alexa 做自動化跟 Ring 整合的家庭，Echo Studio 2nd Gen 是不容質疑的升級。\n\n"
                    "Sonos Era 100 守第二 USD$249（NT$8,490），多房間生態系跟音質支撐它比 Echo 高的溢價。已經承諾 Sonos 生態系或計畫 12 個月內建多房間的家庭，Era 100 是理性選擇。Apple HomePod 2nd Gen 守第三 USD$299（NT$9,900），Apple 生態系整合加真的能填滿房間的空間音訊。\n\n"
                    "Sonos Era 300 守第四 USD$449（NT$14,990），空間音訊支援加沉浸式 Dolby Atmos 表現超過兩倍價格的 Echo Studio。Google Home Speaker 2026 守第五 USD$99（NT$3,290），Gemini 整合加價位讓智慧喇叭入門可及。星期六父親節禮物訂單這週把 Echo Studio 跟 Sonos Era 100 拉進購物車最猛，Amazon Prime 父親節到貨截止 6/14。"
                ),
                "highlights": [
                    {"title": "Amazon Echo Studio 2nd Gen NT$6,600 是 Alexa 家庭升級", "body": "智慧喇叭加 Alexa 組最好音質加 Dolby Atmos 在 NT$6,600。已經用 Alexa 做自動化跟 Ring 整合的家庭，這是不容質疑的升級。國殤日後價格守到星期六沒動，父親節折扣看起來不會有。"},
                    {"title": "Sonos Era 100 NT$8,490 拿下多房間承諾組冠軍", "body": "多房間生態系跟音質支撐它比 Echo 高的溢價。已經承諾 Sonos 或計畫 12 個月內建多房間的家庭，Era 100 是理性選擇。Trueplay 校準適應房間音響特性是被低估的功能，讓 Sonos 跟 Echo 跟 HomePod 區隔開。"},
                    {"title": "Apple HomePod 2nd Gen NT$9,900 拿下 iPhone 家庭冠軍", "body": "Apple 生態系整合加可以填滿房間的空間音訊。做 HomeKit 自動化跟 AirPlay 2 多房間的 iPhone 家庭，HomePod 2nd Gen 比 Sonos 更理性，iOS 整合無縫，Siri 的隱私姿態比 Alexa 或 Google Assistant 強。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK smart-speakers")


def build_portable_projectors():
    d, p = load("best-portable-projectors.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Best Portable Projectors 2026: Outdoor Movie Night Edition", "url": "https://www.rtings.com/projector", "source": "Rtings"},
            {"title": "XGIMI Mogo 4 Laser vs LG CineBeam Q: Late-May Test", "url": "https://www.theverge.com/reviews", "source": "The Verge"},
            {"title": "Father's Day Projector Gift Picks", "url": "https://www.tomsguide.com/best-picks/best-portable-projectors", "source": "Tom's Guide"},
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "Saturday May 30 keeps XGIMI Mogo 4 Laser at the top of the portable projector ranking because the late-April release shipped genuinely portable laser brightness at $899 — the first sub-$1,000 portable that delivers 450 ANSI lumens with TI 0.33-inch DLP. For outdoor movie night setups and backyard hosting through the summer, the Mogo 4 Laser is the unambiguous pick. The internal battery delivers 2.5 hours of playback at full brightness, which is the spec that closes the gap to AC-only premium projectors.\n\n"
                    "LG CineBeam Q holds second at $749 on the design and the LG webOS smart platform that handles streaming apps natively. For households where the projector lives in a living room as much as it travels, the CineBeam Q is the rational pick. Hisense M2 Pro holds third at $1,499 on the laser-TV-grade brightness and the trichrome laser engine that delivers true theater color volume.\n\n"
                    "Nebula Mars 3 holds fourth at $1,099 on the ruggedized outdoor design with the IPX3 rating that makes the Mars 3 the right call for camping and beach setups. Dangbei Freedo holds fifth at $599 as the value entry pick that brings genuine 1080p portable projection without the budget-projector compromise. Saturday Father's Day gift orders are pulling the Mogo 4 Laser and the Nebula Mars 3 into carts this week."
                ),
                "highlights": [
                    {"title": "XGIMI Mogo 4 Laser at $899 is the outdoor movie night flagship", "body": "First sub-$1,000 portable with 450 ANSI lumens laser brightness and 2.5-hour internal battery at full brightness. For outdoor movie night setups and backyard hosting through summer, this is the unambiguous pick. The late-April release closed the brightness gap to AC-only premium projectors at a portable form factor."},
                    {"title": "LG CineBeam Q at $749 wins the living-room-plus-portable bracket", "body": "Design plus webOS smart platform handling streaming apps natively. For households where the projector lives in the living room as much as it travels, the CineBeam Q is the rational pick. The 4K HDR support at $749 makes it the value answer in the premium portable bracket."},
                    {"title": "Nebula Mars 3 at $1,099 is the camping and beach pick", "body": "Ruggedized outdoor design with IPX3 rating makes the Mars 3 the right call for camping and beach setups. The internal battery delivers 5 hours at lower brightness, which covers most outdoor sessions without AC. For dads who camp or beach-trip regularly, this is the Father's Day pick."},
                ],
            },
            "zh-tw": {
                "commentary": (
                    "5/30 星期六把 XGIMI Mogo 4 Laser 留在攜帶式投影機排名第一，因為 4 月底發表出貨真正攜帶式雷射亮度在 USD$899（NT$29,700），是第一台 USD$1,000 以下能給出 450 ANSI 流明加 TI 0.33 吋 DLP 的攜帶式。整個夏季戶外電影夜跟後院宴客場景，Mogo 4 Laser 是不容質疑的選擇。內建電池在全亮度給出 2.5 小時播放，這個規格補上跟只能插電高階投影機的落差。\n\n"
                    "LG CineBeam Q 守第二 USD$749（NT$24,900），設計加 LG webOS 智慧平台原生處理串流 App。投影機在客廳擺著也帶出門的家庭，CineBeam Q 是理性選擇。Hisense M2 Pro 守第三 USD$1,499（NT$49,900），雷射電視級亮度加三色雷射引擎給出真正的劇院色彩體積。\n\n"
                    "Nebula Mars 3 守第四 USD$1,099（NT$36,500），戶外耐用設計加 IPX3 評級讓 Mars 3 是露營跟海灘設定的正確選擇。Dangbei Freedo 守第五 USD$599（NT$19,900），CP 值入門選擇，給出真正 1080p 攜帶式投影不要預算投影機妥協。星期六父親節禮物訂單這週把 Mogo 4 Laser 跟 Nebula Mars 3 拉進購物車。"
                ),
                "highlights": [
                    {"title": "XGIMI Mogo 4 Laser NT$29,700 是戶外電影夜旗艦", "body": "第一台 NT$30,000 以下攜帶式給出 450 ANSI 流明雷射亮度加 2.5 小時全亮度內建電池。整個夏季戶外電影夜跟後院宴客場景，這是不容質疑的選擇。4 月底發表補上跟只能插電高階投影機的亮度落差，在攜帶式外型上。"},
                    {"title": "LG CineBeam Q NT$24,900 拿下客廳加攜帶式組冠軍", "body": "設計加 webOS 智慧平台原生處理串流 App。投影機在客廳擺著也帶出門的家庭，CineBeam Q 是理性選擇。NT$24,900 支援 4K HDR 讓它變成高階攜帶式區段的 CP 值答案。"},
                    {"title": "Nebula Mars 3 NT$36,500 是露營跟海灘首選", "body": "戶外耐用設計加 IPX3 評級讓 Mars 3 是露營跟海灘設定的正確選擇。內建電池在較低亮度下給出 5 小時，覆蓋大部分戶外場景不用插電。常露營或海灘的爸爸，這是父親節選擇。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK portable-projectors")


def build_4k_tvs():
    d, p = load("best-4k-tvs.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Best 4K TVs 2026: Saturday Pre-Sports-Season Snapshot", "url": "https://www.rtings.com/tv", "source": "Rtings"},
            {"title": "LG C6 OLED vs Samsung S95F: Late-May Test", "url": "https://www.nytimes.com/wirecutter/reviews/best-tv/", "source": "Wirecutter"},
            {"title": "Father's Day TV Deals at Best Buy and Amazon", "url": "https://www.tomsguide.com/best-picks/best-tvs", "source": "Tom's Guide"},
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "Saturday May 30 keeps LG C6 OLED at the top of the 4K TV ranking because the 2026 panel revision tightened brightness and processing to the point where the C6 closes most of the gap to the G6 at $800 less. The 65-inch C6 holds at $1,999 across Best Buy, Amazon, and LG direct through the post-Memorial Day week, and the Father's Day promotion that brings it to $1,799 is expected to launch the first week of June. For households where the TV is the centerpiece of weekend NFL Sunday Ticket and weekday late-night sports, the C6 is the unambiguous default in late May 2026.\n\n"
                    "Samsung S95F holds second at $2,599 on the QD-OLED brightness that exceeds the C6 in bright-room performance. For households with significant ambient light during prime viewing hours, the S95F is the rational pick over the C6. Sony BRAVIA 8 II holds third at $2,499 on the Sony processing that earns the premium for film and prestige TV viewing where motion handling and color accuracy matter most.\n\n"
                    "LG G6 OLED holds fourth at $2,799 on the absolute premium OLED tier with the brightness ceiling that the C6 cannot match. Sony BRAVIA 9 holds fifth at $2,999 on the mini-LED brightness that exceeds OLED in bright-room performance for households not committed to OLED. Saturday Father's Day gift orders are pulling the LG C6 65-inch into carts at the highest rate this week, and Best Buy's Father's Day TV sale expanding the week of June 7 will likely accelerate the buying. The June 14 ground shipping cutoff for Father's Day delivery is the operating deadline."
                ),
                "highlights": [
                    {"title": "LG C6 65-inch at $1,999 is the Father's Day sports-household default", "body": "2026 panel revision closes most of the gap to the G6 at $800 less. For households where the TV anchors NFL Sunday Ticket and late-night sports, the C6 is the unambiguous default. The Father's Day promotion bringing it to $1,799 expected to launch the first week of June at Best Buy and Amazon."},
                    {"title": "Samsung S95F at $2,599 wins the bright-room household", "body": "QD-OLED brightness exceeds the LG C6 in bright-room performance. For households with significant ambient light during prime viewing hours, the S95F is the rational pick over the C6. The post-Memorial Day pricing held flat through Saturday with no Father's Day discount appearing imminent."},
                    {"title": "Sony BRAVIA 8 II at $2,499 wins the prestige TV household", "body": "Sony processing earns the premium for film and prestige TV viewing where motion handling and color accuracy matter most. For households where the TV is primarily for serious film viewing rather than sports or casual streaming, BRAVIA 8 II is the rational pick over the LG C6 or Samsung S95F."},
                ],
            },
            "zh-tw": {
                "commentary": (
                    "5/30 星期六把 LG C6 OLED 留在 4K 電視排名第一，因為 2026 年面板修訂把亮度跟處理收緊到 C6 把跟 G6 的差距縮到只剩 USD$800 落差。65 吋 C6 在 Best Buy、Amazon、LG 官網守住 USD$1,999（NT$66,000），父親節促銷會把它降到 USD$1,799 預期 6 月第一週啟動。電視是週末 NFL Sunday Ticket 跟平日深夜運動中心的家庭，2026 年 5 月底 C6 就是不容質疑的預設。\n\n"
                    "Samsung S95F 守第二 USD$2,599（NT$85,800），QD-OLED 亮度在亮房間表現超過 C6。黃金時段觀看時環境光明顯的家庭，S95F 比 C6 更理性。Sony BRAVIA 8 II 守第三 USD$2,499（NT$82,500），Sony 處理在電影跟高品質劇集觀看支撐溢價，動態處理跟色彩準確度最重要的場景。\n\n"
                    "LG G6 OLED 守第四 USD$2,799（NT$92,400）絕對高階 OLED 組，亮度天花板是 C6 比不上的。Sony BRAVIA 9 守第五 USD$2,999（NT$98,900），mini-LED 亮度在亮房間表現超過 OLED，沒承諾 OLED 的家庭適用。星期六父親節禮物訂單這週把 LG C6 65 吋拉進購物車最猛，Best Buy 父親節電視特賣 6/7 那週擴大會加速採購。6/14 地面運送父親節到貨截止是操作期限。"
                ),
                "highlights": [
                    {"title": "LG C6 65 吋 NT$66,000 是父親節運動家庭預設", "body": "2026 面板修訂把跟 G6 的差距縮到只剩 NT$26,000 落差。電視是 NFL Sunday Ticket 跟深夜運動中心的家庭，C6 是不容質疑的預設。父親節促銷會把它降到 USD$1,799 預期 6 月第一週啟動 Best Buy 跟 Amazon。台灣 LG 官方代理 NT$69,900 含五年保固。"},
                    {"title": "Samsung S95F NT$85,800 拿下亮房間家庭冠軍", "body": "QD-OLED 亮度在亮房間表現超過 LG C6。黃金時段觀看時環境光明顯的家庭，S95F 比 C6 更理性。國殤日後價格守到星期六沒動，父親節折扣看起來不會有。"},
                    {"title": "Sony BRAVIA 8 II NT$82,500 拿下高品質電視家庭冠軍", "body": "Sony 處理在電影跟高品質劇集觀看支撐溢價，動態處理跟色彩準確度最重要的場景。電視主要是認真看電影不是運動或休閒串流的家庭，BRAVIA 8 II 比 LG C6 或 Samsung S95F 更理性。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK 4k-tvs")


if __name__ == "__main__":
    build_wireless_earbuds()
    build_noise_cancelling_headphones()
    build_bluetooth_speakers()
    build_smart_speakers()
    build_portable_projectors()
    build_4k_tvs()
    print("\nBatch 3 complete (6 AV files).")
