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

# ---------------- best-wireless-earbuds ----------------
do("best-wireless-earbuds.json",
   [
     {"title": "The 7 Best Noise Cancelling Earbuds of 2026", "url": "https://www.rtings.com/headphones/reviews/best/noise-cancelling-earbuds", "source": "RTINGS"},
     {"title": "Best Wireless Earbuds of 2026 | Lab Tested & Ranked", "url": "https://www.techgearlab.com/topics/audio/best-wireless-earbuds", "source": "TechGearLab"},
   ],
   {
     "commentary": "The Sony WF-1000XM6 stays at number one because it does the two hardest things best at the same time: it blocks the most decibels on average of any earbud tested, and it pairs that with sound that audiophiles actually respect. When you want the best noise cancellation and the best sound in one shell, this is still the answer with no compromise asked of you. The AirPods Pro 2 hold second, and the reason is honest, for an iPhone owner the seamless integration, the spatial audio and the hearing-health features make them the better daily driver even though Sony wins the raw audio contest. Ecosystem fit is a real feature. The Bose QuietComfort Ultra Earbuds stay third as the cross-platform comfort pick, some of the best sound and ANC in the group and compatible with most everything. The Samsung Galaxy Buds always-on for Galaxy owners hold fourth as the Android-side mirror of the AirPods argument. Nothing this week reordered the field. The buying logic is clean: best overall is Sony, best for iPhone is AirPods, best for Galaxy is Buds, and pick by ecosystem before you pick by spec.",
     "highlights": [
       {"title": "Sony WF-1000XM6 wins sound and silence at once", "body": "It blocks the most decibels on average of any earbud tested and pairs that with audiophile-respected sound. Doing both hardest things best in one shell keeps it the no-compromise pick at number one."},
       {"title": "AirPods Pro 2 are the iPhone daily driver", "body": "Seamless integration, spatial audio and hearing-health features make them the better everyday choice for iPhone owners even though Sony wins the raw audio test. Ecosystem fit is a real feature, holding them second."},
       {"title": "Bose QC Ultra is the cross-platform comfort pick", "body": "Some of the best sound and ANC in the group with compatibility across nearly everything. For buyers not locked to one phone brand, it is the most universally satisfying choice and a firm third."},
       {"title": "Pick by ecosystem before spec", "body": "Sony wins on raw performance, but for most people the right earbud is the one that pairs instantly with the phone they already own. Match the buds to your platform and the spec gaps stop mattering."},
     ],
   },
   {
     "commentary": "Sony WF-1000XM6 我還是放第一，因為它同時把兩件最難的事做到最好：平均擋掉的分貝數是測過的耳機裡最高，又搭上發燒友真的尊重的音質。想在同一顆耳機裡要最好的降噪跟最好的音質，它依然是不用你妥協的答案。AirPods Pro 2 守第二，理由很誠實，對 iPhone 用戶來說，無縫整合、空間音訊跟聽力健康功能讓它成為更好的日常機，即使純音質的比賽是 Sony 贏。生態貼合本身就是一項功能。Bose QuietComfort Ultra 守第三，是跨平台的舒適選擇，音質跟降噪都在這群裡名列前茅，幾乎什麼裝置都相容。Samsung Galaxy Buds 對 Galaxy 用戶的 always-on 守第四，是 AirPods 論點的 Android 版鏡像。這週沒事件重排。買法很乾淨：整體最佳是 Sony、iPhone 最佳是 AirPods、Galaxy 最佳是 Buds，先看生態再看規格。",
     "highlights": [
       {"title": "Sony WF-1000XM6 同時贏音質跟安靜", "body": "平均擋掉的分貝是測過的耳機裡最高，又搭上發燒友尊重的音質。在同一顆耳機把兩件最難的事做到最好，讓它穩坐不妥協的第一。"},
       {"title": "AirPods Pro 2 是 iPhone 日常機", "body": "無縫整合、空間音訊跟聽力健康功能，讓它對 iPhone 用戶是更好的日常選擇，即使純音質是 Sony 贏。生態貼合本身就是功能，守住第二。"},
       {"title": "Bose QC Ultra 是跨平台舒適選擇", "body": "音質跟降噪都在這群裡名列前茅，幾乎什麼裝置都相容。對不綁單一手機品牌的買家，它是最普遍讓人滿意的選擇，穩在第三。"},
       {"title": "先看生態再看規格", "body": "Sony 贏在純效能，但對多數人，對的耳機是能跟手上手機秒配對的那一副。把耳機對準你的平台，規格差距就不重要了。"},
     ],
   })

# ---------------- best-noise-cancelling-headphones ----------------
do("best-noise-cancelling-headphones.json",
   [
     {"title": "Best noise-cancelling headphones 2026", "url": "https://www.whathifi.com/best-buys/headphones/best-noise-cancelling-headphones", "source": "What Hi-Fi?"},
     {"title": "The Best Noise Cancelling Headphones of 2026", "url": "https://www.rtings.com/headphones/reviews/best/noise-cancelling", "source": "RTINGS"},
   ],
   {
     "commentary": "The Sony WH-1000XM6 stays at number one because it remains the most complete over-ear you can buy. The noise cancellation is class-leading again, the foldable design returned by popular demand, the app gives you control nobody else matches, and the sound is tuned so well out of the box that most people never touch the EQ. For the broadest set of buyers this is simply the right pair. The Bose QuietComfort Ultra holds second and still wins one specific contest, raw quiet, the noise cancellation is the most physically convincing in the category and the comfort over long flights is unbeaten. If silence is your single priority, buy Bose. The Sennheiser Momentum 4 stays third as the audiophile's value pick, the most natural sound of the mainstream three and battery that runs longer than either rival. Sennheiser HDB 630 holds fourth as the wired-quality option. The Apple AirPods Max round out the visible top for the iPhone ecosystem. Nothing this week moved the order. The split stays simple: Sony for all-round, Bose for silence, Sennheiser for sound.",
     "highlights": [
       {"title": "Sony WH-1000XM6 is the most complete over-ear", "body": "Class-leading ANC, the return of folding, an unmatched app and sound tuned so well most never touch the EQ. For the broadest set of buyers it is simply the right pair, holding number one."},
       {"title": "Bose QC Ultra still wins raw silence", "body": "The noise cancellation is the most physically convincing in the category and long-flight comfort is unbeaten. If quiet is your single priority, this is the buy, which keeps it a firm second."},
       {"title": "Sennheiser Momentum 4 is the sound-and-value pick", "body": "It delivers the most natural tuning of the mainstream three and the longest battery of the group. For listeners who prioritize audio quality and runtime, it stays the smart choice at third."},
       {"title": "The split is simple", "body": "Sony for all-round completeness, Bose for raw silence, Sennheiser for natural sound and battery. The top tier is mature enough that you pick by your single priority and any of them satisfies."},
     ],
   },
   {
     "commentary": "Sony WH-1000XM6 我還是放第一，因為它依然是你買得到最完整的耳罩式。降噪再次同級最強，可折疊設計應觀眾要求回歸，App 給你的控制沒人比得上，音質出廠調得好到多數人從不動 EQ。對最廣的買家來說，這就是對的那副。Bose QuietComfort Ultra 守第二，依然贏一場特定比賽，純粹的安靜，它的降噪是這類別裡physically最有說服力的，長途飛行的舒適也無人能敵。安靜是你唯一優先就買 Bose。Sennheiser Momentum 4 守第三，是發燒友的性價比選擇，主流三強裡音色最自然，電池也比兩個對手都長。Sennheiser HDB 630 守第四，是有線級音質選擇。Apple AirPods Max 收尾可見前段，給 iPhone 生態。這週沒事件改變順序。分法很簡單：全面選 Sony、安靜選 Bose、音質選 Sennheiser。",
     "highlights": [
       {"title": "Sony WH-1000XM6 是最完整的耳罩式", "body": "降噪同級最強、折疊回歸、App 無人能比、音質出廠調到多數人從不動 EQ。對最廣的買家就是對的那副，守住第一。"},
       {"title": "Bose QC Ultra 依然贏純粹安靜", "body": "它的降噪是這類別裡最有說服力的，長途飛行舒適無人能敵。安靜是你唯一優先就買它，這讓它穩在第二。"},
       {"title": "Sennheiser Momentum 4 是音質兼性價比選擇", "body": "主流三強裡音色最自然，電池也是這群裡最長。對重視音質跟續航的聽眾，它穩坐第三當聰明選擇。"},
       {"title": "分法很簡單", "body": "全面完整選 Sony、純粹安靜選 Bose、自然音色跟續航選 Sennheiser。前段夠成熟，照你唯一的優先選，隨便一個都滿足。"},
     ],
   })

# ---------------- best-soundbars ----------------
do("best-soundbars.json",
   [
     {"title": "Best soundbars 2026: tested and rated", "url": "https://www.whathifi.com/best-buys/tv-and-home-cinema/best-soundbars", "source": "What Hi-Fi?"},
     {"title": "The Best Soundbars of 2026", "url": "https://www.rtings.com/soundbar/reviews/best/by-price", "source": "RTINGS"},
   ],
   {
     "commentary": "The Samsung HW-Q990F stays at number one because it is the closest thing to a true wireless surround system you can buy in a box. You get real rear speakers and a big subwoofer, the Atmos height effects actually move overhead, and the whole thing sets up in minutes. For anyone who wants cinema-grade immersion without running speaker wire through the walls, nothing else delivers this much for the money. The Sonos Arc Ultra holds second and earns it on a different strength, it is the best single-bar Atmos performance available and the easiest to live with daily, especially if you already run Sonos elsewhere in the house. No rear speakers, but the soundstage it throws from one bar is genuinely impressive. The Sony Bravia Theatre Bar 9 stays third as the audiophile-leaning pick with the most precise dialogue and detail. The LG S95TR holds fourth as the value full-system alternative to the Samsung. Nothing this week reordered the field. The logic: full surround in a box is Samsung, best single bar is Sonos, detail and dialogue is Sony.",
     "highlights": [
       {"title": "Samsung HW-Q990F is surround in a box", "body": "Real rear speakers, a big sub and Atmos height that actually moves overhead, all set up in minutes. For cinema immersion without wiring the walls, nothing delivers this much for the money, holding number one."},
       {"title": "Sonos Arc Ultra is the best single bar", "body": "It throws an impressive soundstage from one bar and is the easiest to live with daily, especially inside a Sonos home. For buyers who want simplicity over a full kit, it is the clear second."},
       {"title": "Sony Bravia Theatre Bar 9 wins on detail", "body": "It delivers the most precise dialogue and fine detail of the group, the audiophile-leaning choice. For viewers who prioritize clarity over sheer surround scale, it holds a firm third."},
       {"title": "Pick by how much you want to install", "body": "Full surround means satellites and a sub, which Samsung nails; if you want one bar and done, Sonos is the answer. Match the choice to how much hardware you are willing to place."},
     ],
   },
   {
     "commentary": "Samsung HW-Q990F 我還是放第一，因為它是你能整盒買回家、最接近真正無線環繞系統的東西。你拿到真的後置喇叭跟大型重低音，Atmos 的高度效果真的會在頭頂移動，整套幾分鐘就裝好。想要電影級沉浸又不想在牆裡牽喇叭線的人，沒有別的東西用這個價格給這麼多。Sonos Arc Ultra 守第二，贏在不同的強項，它是買得到最佳的單件式 Atmos 表現，日常最好相處，尤其你家本來就有 Sonos。沒有後置喇叭，但一根 bar 拋出的音場真的令人印象深刻。Sony Bravia Theatre Bar 9 守第三，是偏發燒的選擇，人聲跟細節最精準。LG S95TR 守第四，是 Samsung 的性價比全套替代。這週沒事件重排。邏輯：整盒全環繞選 Samsung、最佳單件選 Sonos、細節跟人聲選 Sony。",
     "highlights": [
       {"title": "Samsung HW-Q990F 是整盒的全環繞", "body": "真的後置喇叭、大型重低音、Atmos 高度效果真的在頭頂移動，幾分鐘裝好。要電影沉浸又不想牽牆內線，這個價格沒人給這麼多，守第一。"},
       {"title": "Sonos Arc Ultra 是最佳單件式", "body": "一根 bar 拋出令人印象深刻的音場，日常最好相處，尤其在 Sonos 家庭裡。想要簡單勝過全套的買家，它是明確的第二。"},
       {"title": "Sony Bravia Theatre Bar 9 贏在細節", "body": "它的人聲跟細節是這群裡最精準的，是偏發燒的選擇。重視清晰勝過純環繞規模的觀眾，它穩在第三。"},
       {"title": "照你想裝多少來選", "body": "全環繞代表衛星喇叭加重低音，Samsung 做得好；想要一根 bar 搞定就選 Sonos。把選擇對準你願意擺多少硬體。"},
     ],
   })

# ---------------- best-bluetooth-speakers ----------------
do("best-bluetooth-speakers.json",
   [
     {"title": "Best Bluetooth speakers 2026: portable picks tested", "url": "https://www.soundguys.com/best-bluetooth-speakers-20611/", "source": "SoundGuys"},
     {"title": "The Best Portable Bluetooth Speakers of 2026", "url": "https://www.rtings.com/speaker/reviews/best/bluetooth-speakers", "source": "RTINGS"},
   ],
   {
     "commentary": "The JBL Charge 6 stays at number one because it nails the brief most people actually have: big sound, genuinely rugged, all-day battery, and a built-in power bank that charges your phone at the beach. It is the speaker I hand to someone who just wants one that works everywhere and never babies it. For the broadest use case, this is the buy. The Marshall Emberton III holds second on character, it sounds richer and more distinctive than the JBL and the retro design earns its keep, the pick for people who want a speaker with a personality rather than maximum loudness. The Bose SoundLink Max stays third as the premium portable, the most refined sound of the truly portable group and built like a tank. The Sonos units round out the visible top for people anchored in that ecosystem who want portability plus whole-home sync. Nothing this week moved the order. The buying logic: rugged all-rounder is JBL, character and style is Marshall, refined sound is Bose, ecosystem is Sonos.",
     "highlights": [
       {"title": "JBL Charge 6 nails the real-world brief", "body": "Big sound, genuinely rugged, all-day battery and a power bank that charges your phone at the beach. For the broadest use case it is the speaker that just works everywhere, holding number one."},
       {"title": "Marshall Emberton III wins on character", "body": "It sounds richer and more distinctive than the JBL, and the retro design earns its place. For buyers who want personality over maximum volume, it is the natural pick and a firm second."},
       {"title": "Bose SoundLink Max is the premium portable", "body": "The most refined sound of the truly portable group, built like a tank. For listeners who prioritize audio quality in a grab-and-go speaker, it stays the upscale choice at third."},
       {"title": "Pick by what you value outdoors", "body": "Ruggedness and a power bank lean JBL, distinctive sound leans Marshall, refinement leans Bose. They all survive a pool day, so choose by whether you want toughness, character or polish."},
     ],
   },
   {
     "commentary": "JBL Charge 6 我還是放第一，因為它命中多數人真正的需求：聲音大、真的耐操、整天的電池，還內建行動電源能在海邊幫手機充電。它是我會直接遞給只想要一台到處能用、又不必小心呵護的人的喇叭。對最廣的使用情境，就是它。Marshall Emberton III 守第二，贏在個性，聲音比 JBL 更厚更有辨識度，復古設計也對得起價格，給想要有性格的喇叭而非單純最大聲的人。Bose SoundLink Max 守第三，是高階可攜款，真正可攜這群裡音色最精緻，做工又硬。Sonos 那幾台收尾可見前段，給綁在那個生態、想要可攜又要全屋同步的人。這週沒事件改變順序。買法：耐操全能選 JBL、個性跟造型選 Marshall、精緻音色選 Bose、生態選 Sonos。",
     "highlights": [
       {"title": "JBL Charge 6 命中真實需求", "body": "聲音大、真的耐操、整天電池，還有能在海邊幫手機充電的行動電源。對最廣的使用情境它就是到處都能用的喇叭，守住第一。"},
       {"title": "Marshall Emberton III 贏在個性", "body": "聲音比 JBL 更厚更有辨識度，復古設計對得起價格。想要性格勝過最大音量的買家，它是自然選擇，穩在第二。"},
       {"title": "Bose SoundLink Max 是高階可攜款", "body": "真正可攜這群裡音色最精緻，做工像坦克。重視拿了就走又要音質的聽眾，它穩坐第三當高階選擇。"},
       {"title": "照你戶外重視什麼選", "body": "耐操跟行動電源偏 JBL、有辨識度的聲音偏 Marshall、精緻偏 Bose。它們都撐得過泳池日，照你要硬、要個性還是要精緻來選。"},
     ],
   })

# ---------------- best-smart-speakers ----------------
do("best-smart-speakers.json",
   [
     {"title": "Best smart speakers 2026", "url": "https://www.techradar.com/best/best-smart-speakers", "source": "TechRadar"},
     {"title": "The Best Smart Speakers of 2026", "url": "https://www.cnet.com/home/smart-home/best-smart-speaker/", "source": "CNET"},
   ],
   {
     "commentary": "The Amazon Echo Studio 2nd Gen stays at number one because it finally makes the Alexa speaker sound as good as it is smart. The audio is a real step up, room-filling with proper bass, the new Alexa is noticeably better at conversational requests, and it remains the cheapest way into the deepest smart-home ecosystem. For most households running Alexa devices, this is the speaker to anchor with. The Sonos Era 100 holds second and wins the sound contest outright, it is simply the better-sounding speaker and supports every major voice assistant, the pick for people who care about music first and assistant second. The Apple HomePod 2nd Gen stays third as the choice for Apple households, the best Siri integration and genuinely excellent audio, held back only by the closed ecosystem. The Sonos Era 300 holds fourth as the spatial-audio upgrade. Nothing this week reordered the field. The buying logic is clean: Alexa ecosystem and value is Echo Studio, best sound is Sonos, Apple household is HomePod. Pick your assistant first and the rest follows.",
     "highlights": [
       {"title": "Echo Studio 2nd Gen sounds as good as it is smart", "body": "Room-filling audio with proper bass, a noticeably better conversational Alexa and the cheapest way into the deepest smart-home ecosystem. For Alexa households it is the anchor speaker, holding number one."},
       {"title": "Sonos Era 100 wins the sound contest", "body": "It is simply the better-sounding speaker and supports every major voice assistant. For buyers who care about music first and the assistant second, it is the clear choice and a firm second."},
       {"title": "HomePod 2nd Gen is the Apple pick", "body": "Best Siri integration and genuinely excellent audio, held back only by its closed ecosystem. For Apple households it remains the natural anchor, holding a solid third."},
       {"title": "Pick your assistant first", "body": "The speaker matters less than the ecosystem it locks you into. Choose Alexa, Google or Siri based on your home, then buy the best-sounding speaker that speaks it. That order saves you regret."},
     ],
   },
   {
     "commentary": "Amazon Echo Studio 2nd Gen 我還是放第一，因為它終於讓 Alexa 喇叭聽起來跟它聰明一樣好。音質是真的進步，充滿房間又有像樣的低音，新版 Alexa 處理對話式請求明顯更好，而且它依然是進入最深智慧家庭生態最便宜的方式。對多數跑 Alexa 裝置的家庭，這是該當核心的喇叭。Sonos Era 100 守第二，純音質的比賽直接贏，它就是聲音更好的喇叭，又支援每個主流語音助手，給把音樂擺第一、助手擺第二的人。Apple HomePod 2nd Gen 守第三，是 Apple 家庭的選擇，Siri 整合最好、音質也真的優秀，唯一被封閉生態拖住。Sonos Era 300 守第四，是空間音訊升級款。這週沒事件重排。買法很乾淨：Alexa 生態跟性價比選 Echo Studio、最佳音質選 Sonos、Apple 家庭選 HomePod。先選你的助手，其他就跟著定了。",
     "highlights": [
       {"title": "Echo Studio 2nd Gen 聽起來跟它一樣聰明", "body": "充滿房間又有像樣低音的音質、明顯更好的對話式 Alexa、進入最深智慧家庭生態最便宜的方式。對 Alexa 家庭它是核心喇叭，守住第一。"},
       {"title": "Sonos Era 100 贏純音質比賽", "body": "它就是聲音更好的喇叭，又支援每個主流語音助手。把音樂擺第一、助手擺第二的買家，它是明確選擇，穩在第二。"},
       {"title": "HomePod 2nd Gen 是 Apple 選擇", "body": "Siri 整合最好、音質真的優秀，唯一被封閉生態拖住。對 Apple 家庭它依然是自然核心，穩坐第三。"},
       {"title": "先選你的助手", "body": "喇叭本身沒它綁住你的生態重要。照你家選 Alexa、Google 還是 Siri，再買講那套語言裡聲音最好的喇叭。這個順序讓你不後悔。"},
     ],
   })

print("batchC done")
