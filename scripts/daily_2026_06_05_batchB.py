import sys; sys.path.insert(0, "/Users/etrexkuo/toprankland/scripts")
from daily_helper import load, save, upsert, last_rankings, DATE


def do(name, refs, en, zh, rankings=None):
    d, p = load(name)
    entry = {
        "date": DATE,
        "rankings": rankings if rankings is not None else last_rankings(d),
        "references": refs,
        "i18n": {"en": en, "zh-tw": zh},
    }
    upsert(d, entry)
    save(p, d)
    print("updated", name)


# ---------------- best-ai-video-generators ----------------
do("best-ai-video-generators.json",
   [
     {"title": "Best AI Video Generator in 2026: Runway, Veo, Seedance, Kling", "url": "https://pixflow.net/blog/best-ai-video-generator/", "source": "Pixflow"},
     {"title": "Best AI Video Generator June 2026, ranked by humans", "url": "https://llm-stats.com/leaderboards/best-ai-for-video-generation", "source": "LLM-Stats"},
     {"title": "6 Best AI Video Generators in 2026 (Veo, Runway, Kling+)", "url": "https://chatcut.io/blog/best-ai-video-generator-2026", "source": "ChatCut"},
   ],
   {
     "commentary": "A week deeper into June 2026 and my read on AI video is the same one I would stake my reputation on: pick by the job, and Google Veo 3.1 wins the job of being the one model that just works. It pairs the best prompt adherence on the board with native audio and true 4K output in both landscape and portrait, so when a client hands me a brief and expects a usable clip on the first pass, this is what I open. That reliability is why it holds number one. Runway Gen-4.5 stays second because it is the closest thing we have to a real director's chair, motion brush, explicit camera moves and reference-driven character consistency that let you build a shot instead of rolling dice on a prompt. The most interesting story this week sits at third: Kling 3.0 is now leading the human-voted text-to-video arena around 2,104, and in side-by-side physics tests it handles water, smoke and fabric more convincingly than Veo. I considered moving it up, but Veo's complete-package advantage on audio and output flexibility still wins the everyday recommendation, so Kling stays the value-and-motion specialist at three. Seedance 2.0 holds fourth as the narrative tool, generating multi-shot sequences with synchronized footsteps and ambience in a single pass, which is genuinely rare. Hailuo 02 keeps fifth on budget value. Luma Ray3, Pika 2.2, Firefly Video, Hunyuan 1.5 and Wan 2.6 all carry forward. The order held this week, and the verdicts below explain why each pick earns its slot.",
     "highlights": [
       {"title": "Veo 3.1 is still the safest complete pick", "body": "Best prompt adherence on the board, native audio and real 4K in both orientations. When one model has to produce a usable clip for a client on the first try, this is the one I reach for, and that reliability keeps it at number one."},
       {"title": "Kling 3.0 owns motion and value", "body": "It now leads the human-voted arena around 2,104 and beats Veo on water, smoke and fabric physics while costing a fraction as much. For motion-heavy briefs and high-volume work it is the smart spend, holding a strong third."},
       {"title": "Runway Gen-4.5 is the director's chair", "body": "Motion brush, explicit camera moves and reference-driven character consistency let you build a shot deliberately. For real creative control rather than one-prompt luck, it stays the clear second."},
       {"title": "Seedance 2.0 is the narrative specialist", "body": "Multi-shot native generation with synchronized footsteps and ambient audio in a single pass is still rare to find anywhere else. For story-driven sequences it earns its fourth-place spot outright."},
     ],
   },
   {
     "commentary": "進到 2026 年 6 月再往後一週，我對 AI 影片的看法跟之前一樣，敢拿信用背書，照任務選工具，而「要一個模型給客戶交差就能用」這個任務，Google Veo 3.1 拿下。它把全場最好的指令遵循、原生音訊、橫幅直幅都能真 4K 這幾點湊在一起，客戶丟個 brief 過來、期待第一次就出一段能用的片，我開的就是它，這份穩定就是它守第一的原因。Runway Gen-4.5 守第二，因為它是目前最接近真正導演椅的東西，motion brush、明確運鏡、靠參考圖維持角色一致，讓你是在「搭一個鏡頭」而不是丟 prompt 賭運氣。這週最有看頭的故事在第三名，Kling 3.0 現在在真人投票的文字轉影片競技場約 2,104 分居首，物理對比測試裡水、煙、布料都比 Veo 更有說服力。我有考慮把它往上挪，但 Veo 在音訊跟輸出彈性的全包優勢，在日常推薦這件事上還是贏，所以 Kling 守在第三，當性價比加動態的專家。Seedance 2.0 守第四，是敘事工具，一次生成就能多鏡頭、腳步聲跟環境音同步，這真的很少見。Hailuo 02 守第五，靠預算性價比。Luma Ray3、Pika 2.2、Firefly Video、Hunyuan 1.5、Wan 2.6 全部照舊。這週排名守住，下面的判斷說明每個位置為什麼是它。",
     "highlights": [
       {"title": "Veo 3.1 仍是最安全的全能選擇", "body": "全場最好的指令遵循、原生音訊、橫直都真 4K。要一個模型第一次就給客戶交出能用的片，我就拿它，這份穩定讓它守第一。"},
       {"title": "Kling 3.0 主宰動態跟性價比", "body": "現在在真人投票競技場約 2,104 分居首，水、煙、布料的物理贏過 Veo，成本卻只有零頭。動態吃重的案子跟量大的活，拿它最划算，守住強勢第三。"},
       {"title": "Runway Gen-4.5 是導演椅", "body": "motion brush、明確運鏡、靠參考圖維持角色一致，讓你能刻意搭一個鏡頭。要真實創作掌控而非一鍵賭運氣，它穩坐第二。"},
       {"title": "Seedance 2.0 是敘事專家", "body": "一次生成就多鏡頭、腳步聲跟環境音同步，這在別處還是很難拿到。要做有故事性的連續鏡頭，第四名實至名歸。"},
     ],
   })

# ---------------- best-ai-voice-generators ----------------
do("best-ai-voice-generators.json",
   [
     {"title": "Inworld vs ElevenLabs: #1 Ranked TTS Compared (2026)", "url": "https://inworld.ai/resources/inworld-vs-elevenlabs", "source": "Inworld"},
     {"title": "Best AI Voice Generators 2026: Ranked by quality, latency, price", "url": "https://gradium.ai/content/best-ai-voice-generators-2026", "source": "Gradium"},
     {"title": "ElevenLabs Review 2026: Best AI Voice Generator?", "url": "https://cognitivefuture.ai/elevenlabs-review/", "source": "Cognitive Future"},
   ],
   {
     "commentary": "The top of the voice-generation board in June 2026 is still a photo finish, and I am keeping Inworld TTS-1.5 Max and ElevenLabs tied at 9.4 because they win different races. Inworld holds number one because it tops the Artificial Analysis Speech Arena around 1,236 ELO, winning blind tests for naturalness, emotional range and conversational flow, and it does it while streaming under 200ms at roughly 5 dollars per million characters. For real-time agents and interactive characters where latency and cost decide the build, that combination is decisive, and Inworld's newer Realtime TTS-2 research preview shows the lead is only widening. ElevenLabs sits right beside it as the more complete creator platform. Eleven v3 went GA in March handling emotion and pacing better than anything I have tested, the catalog now spans 70-plus languages, and the run of 2026 shipments, Flows, Dubbing v2 and Music v2 in May, makes it the obvious home for audiobooks, dubbing and branded voices. For voice cloning and a 10,000-plus community voice library, it is still my first call. Hume AI Octave 2 holds third for emotion-aware delivery, with Minimax Speech 02 HD and Cartesia Sonic 3 anchoring a strong upper tier on latency and quality. GPT-4o mini TTS, Murf, WellSaid, Speechify, Resemble and Descript Overdub carry forward. The split is clean: Inworld for live agents, ElevenLabs for finished audio. No rank change was warranted this week.",
     "highlights": [
       {"title": "Inworld TTS-1.5 Max keeps the blind-test crown", "body": "It tops the Artificial Analysis Speech Arena around 1,236 ELO while streaming under 200ms at about 5 dollars per million characters. For real-time agents where latency and cost decide the build, that combination keeps it at number one."},
       {"title": "ElevenLabs owns finished-audio production", "body": "Eleven v3 went GA in March with the best emotion and pacing I have tested, 70-plus languages, plus Dubbing v2 and Music v2 this spring. For audiobooks, dubbing, cloning and branded voices it remains my first call."},
       {"title": "Hume Octave 2 leads on emotion", "body": "Its emotion-aware delivery makes it the pick when a read has to carry genuine feeling rather than just clarity. That specialization holds it firmly at number three in a deep upper tier."},
       {"title": "The top two split by use case", "body": "Inworld edges live conversational quality and cost, ElevenLabs owns production and cloning. Choose by whether you are building an agent or shipping a deliverable, and either way you land on a top-tier tool."},
     ],
   },
   {
     "commentary": "2026 年 6 月語音生成的頂端還是衝線難分，我把 Inworld TTS-1.5 Max 跟 ElevenLabs 並列 9.4，因為它們贏的是不同的比賽。Inworld 守第一，是因為它在 Artificial Analysis 語音競技場約 1,236 ELO 居首，盲測的自然度、情緒幅度、對話流暢都拿下，而且做到這些的同時延遲壓在 200 毫秒內、每百萬字元大約只要五美金。即時語音代理跟互動角色這種「延遲跟成本決定能不能做」的場景，這個組合就是關鍵，而且 Inworld 更新的 Realtime TTS-2 研究預覽顯示，差距還在拉開。ElevenLabs 緊貼在旁，是更完整的創作者平台。Eleven v3 在 3 月轉正式版，情緒跟節奏比我測過的都好，語音庫現在涵蓋 70 多種語言，2026 一連串更新，Flows、5 月的 Dubbing v2 跟 Music v2，讓它成為有聲書、配音、品牌語音的明顯歸宿。論語音克隆跟那個破萬的社群聲音庫，我還是第一個推它。Hume AI Octave 2 守第三，主打情緒感知演繹，Minimax Speech 02 HD 跟 Cartesia Sonic 3 在延遲跟品質上撐起強勢上半段。GPT-4o mini TTS、Murf、WellSaid、Speechify、Resemble、Descript Overdub 全部照舊。這條分界很乾淨，做即時代理選 Inworld，做成品音檔選 ElevenLabs。這週沒有動排名的理由。",
     "highlights": [
       {"title": "Inworld TTS-1.5 Max 守住盲測王冠", "body": "它在 Artificial Analysis 語音競技場約 1,236 ELO 居首，延遲壓在 200 毫秒內、每百萬字元約五美金。即時代理這種延遲跟成本決勝的場景，這個組合讓它守第一。"},
       {"title": "ElevenLabs 主宰成品音檔製作", "body": "Eleven v3 在 3 月轉正式版，情緒跟節奏是我測過最好，涵蓋 70 多種語言，今春又有 Dubbing v2 跟 Music v2。有聲書、配音、克隆、品牌語音，我還是第一個推它。"},
       {"title": "Hume Octave 2 情緒最強", "body": "情緒感知的演繹讓它在「念稿要帶真情緒而不只是清楚」時成為首選。這份專長讓它在深厚的上半段裡穩穩守第三。"},
       {"title": "前兩名依場景分工", "body": "Inworld 小贏現場對話品質跟成本，ElevenLabs 握有製作跟克隆。看你是在做代理還是出交付物來選，兩邊都落在頂級工具上。"},
     ],
   })

# ---------------- best-vpn-services ----------------
do("best-vpn-services.json",
   [
     {"title": "Mullvad vs Proton VPN: which one should you choose in 2026?", "url": "https://cybernews.com/best-vpn/mullvad-vs-proton-vpn/", "source": "Cybernews"},
     {"title": "The Best VPN Services of 2026: 50+ VPNs Tested & Ranked", "url": "https://www.security.org/vpn/best/", "source": "Security.org"},
     {"title": "The best VPN service 2026", "url": "https://www.techradar.com/vpn/best-vpn", "source": "TechRadar"},
   ],
   {
     "commentary": "My VPN ranking leads with privacy, and in June 2026 Mullvad keeps number one for the reason it has held all year: it is the purest privacy choice you can buy. You sign up with no email and no personal information, the no-logs policy is genuine, the tunnels are quantum-resistant, and the price has stayed a flat 5 euros a month since 2009 regardless of term. The one caveat I always give upfront stays true: Mullvad is reliably blocked by Netflix and most streaming services, so if streaming is the main reason you want a VPN, this is the wrong pick. That is exactly why ProtonVPN holds a close second. Recent testing puts Proton first overall on upload speed with only an eight percent download drop, making it one of the fastest VPNs going, and it is the clear winner for Netflix and other streaming. Proton's CEO has also confirmed an all-new in-house VPN architecture rolling out through 2026, which only strengthens the privacy story. If you want privacy you can trust plus real streaming access, Proton is the answer. NordVPN stays third on raw throughput and the widest server network, the pick when speed and server choice top your list. IVPN, ExpressVPN, Surfshark, Windscribe and Obscura VPN all carry forward unchanged. Nothing this week moved the board, so I held ranks. Mullvad for anonymity, Proton for privacy-plus-streaming, Nord for pure speed.",
     "highlights": [
       {"title": "Mullvad is the privacy benchmark", "body": "No email to sign up, a real no-logs policy, quantum-resistant tunnels, and a flat 5 euros a month unchanged since 2009. For pure anonymity it stays number one, and the value math is as clean as the privacy."},
       {"title": "ProtonVPN wins privacy plus streaming", "body": "Recent tests rank it first overall on upload speed with only an eight percent download drop, and it is the clear Netflix winner. With a new in-house architecture rolling out in 2026, it earns a confident second."},
       {"title": "NordVPN is the speed and network king", "body": "It still posts the fastest raw throughput of this group alongside the widest server network. For users who put download speed and server choice first, it stays a solid third."},
       {"title": "Mullvad's streaming caveat is real", "body": "It is reliably blocked by Netflix and most streaming services, so if streaming is your main goal you should pick Proton instead. I keep the verdict honest so the ranking matches how you actually use a VPN."},
     ],
   },
   {
     "commentary": "我的 VPN 排名以隱私掛帥，2026 年 6 月 Mullvad 守第一的理由跟一整年一樣，它是你能買到最純粹的隱私選擇。註冊不用 email、不用任何個資，無紀錄政策是真的，通道抗量子，價格從 2009 年到現在不分方案都是每月五歐元。我每次都先講白的那句但書還是成立，Mullvad 會被 Netflix 跟大多數串流穩定擋下，所以如果你裝 VPN 主要就是要追劇，這個選錯了。這正是 ProtonVPN 緊咬第二的原因。最近的測試裡，Proton 上傳速度整體第一、下載只掉八趴，是目前最快的 VPN 之一，而且是 Netflix 跟其他串流的明確贏家。Proton 執行長還確認了一套全新自研的 VPN 架構會在 2026 年陸續上線，這只會讓隱私故事更強。要可信任的隱私加上真的能追劇，答案就是 Proton。NordVPN 守第三，靠純吞吐量跟最廣的伺服器網路，當速度跟伺服器選擇排你清單最前面時就選它。IVPN、ExpressVPN、Surfshark、Windscribe、Obscura VPN 全部照舊。這週沒事件動榜，所以我守住排名。要匿名選 Mullvad，要隱私加串流選 Proton，要純速度選 Nord。",
     "highlights": [
       {"title": "Mullvad 是隱私標竿", "body": "註冊不用 email、真無紀錄政策、抗量子通道，價格從 2009 年到現在都是每月五歐元。要純匿名，第一還是它，性價比跟隱私一樣乾淨。"},
       {"title": "ProtonVPN 贏在隱私加串流", "body": "最近測試它上傳速度整體第一、下載只掉八趴，是 Netflix 明確贏家。2026 年又有全新自研架構陸續上線，第二名拿得很有底氣。"},
       {"title": "NordVPN 是速度與網路王", "body": "這群裡純吞吐量還是最快，伺服器網路也最廣。把下載速度跟伺服器選擇擺最前面的人，它穩坐第三。"},
       {"title": "Mullvad 的串流但書是真的", "body": "它會被 Netflix 跟多數串流穩定擋下，所以主要要追劇就該改選 Proton。我把判斷講白，讓排名對得上你實際怎麼用 VPN。"},
     ],
   })

# ---------------- best-portable-projectors ----------------
do("best-portable-projectors.json",
   [
     {"title": "XGIMI MoGo 4 Laser Projector Review", "url": "https://www.rtings.com/projector/reviews/xgimi/mogo-4-laser-projector", "source": "RTINGS"},
     {"title": "Best portable projector of 2026: Tested for streaming on the go", "url": "https://www.techradar.com/pro/best-portable-projector", "source": "TechRadar"},
     {"title": "XGIMI MoGo 4 Laser Review", "url": "https://www.trustedreviews.com/reviews/xgimi-mogo-4-laser", "source": "Trusted Reviews"},
   ],
   {
     "commentary": "For portable projectors in June 2026 I keep the XGIMI MoGo 4 Laser at number one, and the reviews this month back the call hard. It is the best iteration of XGIMI's MoGo line, with the triple-laser engine roughly doubling the brightness of something like the Samsung Freestyle Gen 2 and pushing color coverage from 90 percent up to 110 percent DCI-P3, so it throws a genuinely vivid 1080p image you can watch with some ambient light and still rely on the built-in battery for cord-free movie nights. That blend of brightness, color, smart Google TV platform and price is why it leads. The LG CineBeam Q holds second because it does something nobody else in this size class does: native 4K at 3840x2160 from an RGB laser engine, in a beautifully designed body under 1,000 dollars. If resolution and looks matter most and you can live with lower brightness, it is the connoisseur pick. The Hisense M2 Pro stays third as the brightness-first choice for rooms you cannot fully darken, trading some portability and battery life for output. Nebula Mars 3 holds fourth as the rugged outdoor king on battery endurance. Dangbei Freedo, Samsung Freestyle 2nd Gen, Nebula Mars 3 Air, Capsule 3 Laser, XGIMI MoGo 4 and Nebula P1i all carry forward. No launch this week reshuffled the board, so I held ranks and let the brightness-versus-resolution split frame the top two.",
     "highlights": [
       {"title": "XGIMI MoGo 4 Laser is the best all-rounder", "body": "Its triple-laser engine roughly doubles Freestyle Gen 2 brightness and lifts color to 110 percent DCI-P3, with cord-free battery play and Google TV built in. That balance of brightness, color and price keeps it at number one."},
       {"title": "LG CineBeam Q owns resolution and design", "body": "It is the only portable here pairing native 4K with an RGB laser engine, in a stylish body under 1,000 dollars. For viewers who prize sharpness and looks over peak brightness, it is the clear second."},
       {"title": "Hisense M2 Pro is the brightness pick", "body": "It pushes the most output of this group, making it the choice for rooms you cannot fully darken. It trades some portability and battery life for that punch, which keeps it a strong third."},
       {"title": "Nebula Mars 3 is the outdoor king", "body": "Its battery endurance and rugged build make it the one I take to a backyard or campsite. For genuine off-grid movie nights it holds a deserved fourth."},
     ],
   },
   {
     "commentary": "2026 年 6 月講可攜投影機，我把 XGIMI MoGo 4 Laser 放第一，這個月的評測也大力背書這個判斷。它是 XGIMI MoGo 系列做得最好的一代，三雷射光源把亮度拉到大約是 Samsung Freestyle 二代的兩倍，色域覆蓋從 90 趴一路推到 110 趴 DCI-P3，所以它投出來的 1080p 畫面是真的鮮豔，環境有點光也看得下去，內建電池又能讓你不插電在客廳看一整部電影。亮度、色彩、Google TV 智慧平台加上價格這個組合，就是它領先的原因。LG CineBeam Q 守第二，因為它做到這個體積級距沒人做到的事，RGB 雷射引擎的原生 4K、3840x2160，機身設計又漂亮，台灣入手大概三萬出頭。如果你最在意解析度跟外型、可以接受亮度低一點，它就是行家選擇。Hisense M2 Pro 守第三，是亮度優先的選擇，適合無法全暗的房間，代價是犧牲一點可攜性跟電池。Nebula Mars 3 守第四，是戶外耐久王，電池續航最強。Dangbei Freedo、Samsung Freestyle 二代、Nebula Mars 3 Air、Capsule 3 Laser、XGIMI MoGo 4、Nebula P1i 全部照舊。這週沒新品洗牌，所以我守住排名，讓「亮度對解析度」這條線去框前兩名。",
     "highlights": [
       {"title": "XGIMI MoGo 4 Laser 是最佳全能", "body": "三雷射引擎亮度大約是 Freestyle 二代的兩倍，色域拉到 110 趴 DCI-P3，內建電池能不插電看，Google TV 直接內建。亮度、色彩、價格這個平衡讓它守第一。"},
       {"title": "LG CineBeam Q 主宰解析度跟設計", "body": "它是這裡唯一把原生 4K 配上 RGB 雷射引擎的可攜機，機身漂亮、台灣大約三萬出頭。重視銳利度跟外型勝過峰值亮度的人，它穩坐第二。"},
       {"title": "Hisense M2 Pro 是亮度選擇", "body": "它的輸出是這群裡最猛的，適合沒辦法全暗的房間。代價是犧牲一點可攜性跟電池續航，這讓它守住強勢第三。"},
       {"title": "Nebula Mars 3 是戶外王", "body": "電池續航跟堅固機身，讓它是我會帶去後院或營地的那一台。要真正離電源的露天電影夜，第四名實至名歸。"},
     ],
   })

# ---------------- best-4k-tvs ----------------
do("best-4k-tvs.json",
   [
     {"title": "Best OLED TVs in 2026 tested: top picks from LG, Samsung and more", "url": "https://www.tomsguide.com/tvs/oled-tvs/best-oled-tvs", "source": "Tom's Guide"},
     {"title": "Best OLED TV 2026: top sets for serious movie fans, fully reviewed", "url": "https://www.whathifi.com/best-buys/tvs/best-oled-tvs", "source": "What Hi-Fi?"},
     {"title": "The 3 Best OLED TVs of 2026", "url": "https://www.rtings.com/tv/reviews/best/by-type/oled", "source": "RTINGS"},
   ],
   {
     "commentary": "For 4K TVs in June 2026 I keep the LG C6 OLED at number one, and the latest reviews make the case for me. What Hi-Fi calls it the pick of the latest 65-inch sets and a genuine revelation by C-series standards, better than its excellent predecessor and cheaper at launch. The new Alpha 11 Gen 3 processor sharpens tone and color management, brightness control and upscaling, and with four full HDMI 2.1 ports plus a gorgeous WOLED panel it is the all-round set I recommend to the most people. That balance of picture, gaming and value is why it leads. The Samsung S95F QD-OLED holds second as the brightness champion, frequently rated the single best-measuring OLED tested, the pick for a bright room and gamers who want four full-speed HDMI 2.1 inputs. Its trade-offs, no Dolby Vision and aggressive processing, are exactly why it sits behind the more universally agreeable C6. The Sony Bravia 8 II stays third as the picture-purist's choice, 25 percent brighter than the A95L it replaces with the most natural color and motion handling Sony offers. LG G6 OLED holds fourth on peak brightness, with the Bravia 9, Samsung QN90F, TCL QM8K, Hisense U8N, Samsung S85F, Hisense U7N and TCL QM9K carrying forward. No launch this week moved the order, so I held ranks.",
     "highlights": [
       {"title": "LG C6 OLED is the best all-rounder", "body": "Reviewers call it the pick of the latest 65-inch sets, better than its predecessor and cheaper at launch. The Alpha 11 Gen 3 processor, four HDMI 2.1 ports and a superb WOLED panel make it the set I recommend most, holding number one."},
       {"title": "Samsung S95F is the brightness champion", "body": "Often rated the best-measuring OLED tested, with four full-speed HDMI 2.1 inputs for gamers and a bright room. Its lack of Dolby Vision and aggressive processing keep it a close, deserved second behind the C6."},
       {"title": "Sony Bravia 8 II is the purist's pick", "body": "It is 25 percent brighter than the A95L it replaces, with the most natural color and motion Sony offers. For viewers who want filmmaker-accurate images over peak punch, it holds a confident third."},
       {"title": "LG G6 OLED leads on peak brightness", "body": "Its gallery-design panel pushes higher brightness than the C6 for bright-room HDR. For buyers who prioritize peak luminance and a wall-flush mount, it stays a strong fourth."},
     ],
   },
   {
     "commentary": "2026 年 6 月講 4K 電視，我把 LG C6 OLED 放第一，最新的評測幫我把話講完了。What Hi-Fi 說它是最新一批 65 吋裡的首選，以 C 系列的標準來看是真正的驚喜，比上一代那台已經很強的還要好，上市價還更便宜。新的 Alpha 11 Gen 3 處理器把色調與色彩管理、亮度控制、升頻都磨得更利，加上四個完整 HDMI 2.1 跟一面漂亮的 WOLED 面板，它就是我會推薦給最多人的全能機。畫質、電競、性價比這個平衡，就是它領先的原因。Samsung S95F QD-OLED 守第二，是亮度冠軍，常被評為實測表現最好的單一 OLED，亮房間跟想要四個全速 HDMI 2.1 的玩家就選它。它的取捨，沒有 Dolby Vision、處理偏激進，正是它排在更討喜的 C6 之後的原因。Sony Bravia 8 II 守第三，是畫質純粹派的選擇，比它取代的 A95L 亮了 25 趴，色彩跟動態是 Sony 最自然的調校。LG G6 OLED 守第四，靠峰值亮度，後面的 Bravia 9、Samsung QN90F、TCL QM8K、Hisense U8N、Samsung S85F、Hisense U7N、TCL QM9K 全部照舊。這週沒新品動排名，所以我守住。",
     "highlights": [
       {"title": "LG C6 OLED 是最佳全能", "body": "評測說它是最新 65 吋的首選，比上一代更好、上市價更便宜。Alpha 11 Gen 3 處理器、四個 HDMI 2.1、出色的 WOLED 面板，讓它是我推薦給最多人的機種，守住第一。"},
       {"title": "Samsung S95F 是亮度冠軍", "body": "常被評為實測最好的 OLED，四個全速 HDMI 2.1 給玩家跟亮房間用。少了 Dolby Vision、處理偏激進，讓它在更討喜的 C6 之後拿下實至名歸的第二。"},
       {"title": "Sony Bravia 8 II 是純粹派之選", "body": "比它取代的 A95L 亮了 25 趴，色彩跟動態是 Sony 最自然的調校。想要貼近導演原意的畫面勝過峰值衝擊力的人，它穩坐第三。"},
       {"title": "LG G6 OLED 峰值亮度領先", "body": "畫廊設計面板的亮度比 C6 更高，適合亮房間看 HDR。重視峰值亮度跟貼牆安裝的買家，它守住強勢第四。"},
     ],
   })

print("ALL DONE")
