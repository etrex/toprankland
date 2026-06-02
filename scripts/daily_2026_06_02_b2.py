"""2026-06-02 daily update — Batch 2: AI tools + Audio (7 files)"""
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


def build_ai_music_generators():
    d, p = load("best-ai-music-generators.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "AI music generator Suno hits 2M paid subscribers and $300M in annual recurring revenue", "url": "https://techcrunch.com/2026/02/27/ai-music-generator-suno-hits-2-million-paid-subscribers-and-300m-in-annual-recurring-revenue/", "source": "TechCrunch"},
            {"title": "Suno adjusts AI music ownership terms after Warner Music partnership", "url": "https://www.musicinafrica.net/magazine/suno-adjusts-ai-music-ownership-terms-after-warner-music-partnership", "source": "Music In Africa"},
            {"title": "Suno AI Complete Guide 2026: How to Create Music for AI Videos, Monetize, and Build a Full Production Pipeline", "url": "https://aivideobootcamp.com/blog/suno-ai-complete-guide-2026/", "source": "AI Video Bootcamp"},
        ],
        "i18n": {
            "en": {
                "commentary": "Suno V5 stays at the top of the AI music category, and the gap between it and everyone else is widening on the strength of pure scale. Suno now sits at 2 million paid subscribers and $300 million in annual recurring revenue, with users generating roughly 7 million tracks per day across every genre. That kind of volume creates a feedback loop competitors cannot easily match: more generation means more data, faster iteration, and a sound that keeps getting more convincing. The 9.7 audio quality score reflects exactly that maturity.\n\nThe most important development this week is Suno's revised ownership framework following its Warner Music Group partnership. The 2026 policy update reaffirms that music made on free accounts cannot be used commercially, and pushes monetization toward paid subscribers. If you are building anything for client work, YouTube, or a release, this is the signal to be on a paid tier. It is also why I keep Suno's commercial-license score at a measured 7.7 rather than higher: the platform is excellent, but the licensing terms reward subscribers and penalize free users.\n\nElevenLabs Music holds rank 2 on the strength of its 9.7 vocal realism, the best vocal score in the category, and a 9.6 commercial-license score that makes it the cleaner choice for anyone nervous about rights. For creators whose projects live or die on a believable lead vocal, ElevenLabs is the pick.\n\nUdio at rank 3 remains the producer's tool, with a category-leading 9.7 editing-control score for people who want to shape a track stem by stem rather than roll the dice on a full generation. Suno V5.5 added voice cloning and 8-minute studio-quality tracks earlier this year, so the ceiling on what one prompt can produce keeps rising. For most people most of the time, Suno is still the place to start.",
                "highlights": [
                    {"title": "Suno V5 Leads on Scale and Sound", "body": "Suno now has 2 million paid subscribers, $300M in annual recurring revenue, and roughly 7 million tracks generated per day. That data flywheel directly powers the 9.7 audio quality score that no competitor matches in 2026."},
                    {"title": "New Warner-Driven Ownership Terms Reward Paid Tiers", "body": "Suno's revised 2026 policy reaffirms that free-account music cannot be used commercially and shifts monetization to subscribers. Anyone producing for clients, YouTube, or a release should be on a paid plan, which is why the commercial-license score stays measured at 7.7."},
                    {"title": "ElevenLabs Music Wins on Vocals and Licensing", "body": "ElevenLabs Music holds rank 2 with a category-best 9.7 vocal realism score and a 9.6 commercial-license score. For projects that depend on a believable lead vocal and clean rights, it is the cleaner pick."},
                ],
            },
            "zh-tw": {
                "commentary": "Suno V5 繼續穩坐 AI 音樂生成的第一名，而且跟後面的差距還在拉大，靠的就是規模。Suno 現在有 200 萬付費訂閱用戶，年度經常性營收 3 億美元，每天產生大約 700 萬首曲子，橫跨所有曲風。這種量體會形成一個對手很難追上的飛輪，產得越多、資料越多、迭代越快，生成出來的聲音也越來越像真的。音質拿 9.7 分，反映的就是這種成熟度。\n\n這禮拜最重要的消息，是 Suno 跟 Warner Music 合作後更新的版權框架。2026 年的新政策再次明確，免費帳號做的音樂不能商用，把營利機制全面導向付費訂閱。講白了，如果你要接案、上 YouTube、或正式發行，現在就該用付費方案。這也是為什麼我把 Suno 的商用授權分數維持在 7.7，平台本身很強，但授權條款明顯偏袒訂閱用戶。\n\nElevenLabs Music 排第二，人聲擬真度 9.7 分是全榜最高，商用授權 9.6 分也讓它成為對版權比較敏感的人的安心選擇。專案成敗取決於主唱聽起來夠不夠真的話，選 ElevenLabs 就對了。\n\nUdio 第三名，仍然是製作人的工具，編輯控制 9.7 分全榜最高，適合想要一軌一軌慢慢雕、而不是賭一次整首生成的人。Suno V5.5 今年稍早加了語音克隆和 8 分鐘錄音室品質長曲，一個 prompt 能產出的東西天花板還在往上抬。對大多數人來說，Suno 還是最該先試的那一個。",
                "highlights": [
                    {"title": "Suno V5 規模與音質雙領先", "body": "Suno 現有 200 萬付費訂閱、3 億美元年度經常性營收，每天約產生 700 萬首曲子。這個資料飛輪直接撐起 9.7 分的音質評分，2026 年沒有對手追得上。"},
                    {"title": "Warner 合作後新版權條款偏向付費方案", "body": "Suno 2026 新政策重申免費帳號音樂不可商用，營利機制轉向訂閱用戶。要接案、上 YouTube、或發行的人都該用付費方案，這也是商用授權分維持 7.7 的原因。"},
                    {"title": "ElevenLabs Music 人聲與授權雙贏", "body": "ElevenLabs Music 排第二，人聲擬真度 9.7 分全榜最高，商用授權 9.6 分。專案靠主唱真實感決勝負、又在意版權乾不乾淨的人，選它最安心。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK ai-music-generators")


def build_ai_video_generators():
    d, p = load("best-ai-video-generators.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Best AI Video Generator (June 2026) — Top AI Video Generation Models Ranked by Humans", "url": "https://llm-stats.com/leaderboards/best-ai-for-video-generation", "source": "LLM-Stats"},
            {"title": "AI Video Market After Sora: Runway, Kling, and Veo", "url": "https://www.digitalapplied.com/blog/ai-video-market-after-sora-runway-kling-veo-2026", "source": "Digital Applied"},
            {"title": "Best AI Video Generator in 2026: Runway, Veo, Seedance, Kling & More", "url": "https://pixflow.net/blog/best-ai-video-generator/", "source": "Pixflow"},
        ],
        "i18n": {
            "en": {
                "commentary": "Google Veo 3.1 stays at rank 1, and the case for it has only gotten stronger this week. The single biggest story in AI video right now is what is NOT in the market anymore: OpenAI shut down Sora in April 2026 after burning roughly $15 million per day against $2.1 million in total lifetime revenue. That collapse removed a major competitor and consolidated the field around Veo, Runway, and Kling. Veo benefits most because it was already the strongest all-around quality model, with default output that looks closer to high-end stock footage than anything else, especially on natural scenes, fabric, and hair physics. Its 9.8 audio-video sync score remains the best in the category and is the feature that separates a usable clip from a polished one.\n\nKling 3.0 at rank 3 is the model to watch. On the human-ranked text-to-video leaderboard for June 2026, Kling v3 actually leads with an arena score of 2127, ahead of Seedance 2.0 Fast at 1993. Kling matches Veo on cinematic lighting and complex motion and adds a multi-shot storyboard mode with native audio sync across cuts. Its 9.7 value-for-money score is the highest on this list, which makes it the smart pick for creators who need volume on a budget.\n\nRunway Gen-4.5 holds rank 2 as the professional's control surface. Its 9.7 character-consistency score is the best here, and the combination of motion brush, granular camera moves, and reference-driven characters is why studios and serious creators keep reaching for it when a shot has to match an exact creative brief. The market after Sora is leaner and more competitive, and that is good news for anyone shopping these tools today.",
                "highlights": [
                    {"title": "Veo 3.1 Leads on Sync and All-Around Quality", "body": "Google Veo 3.1 holds rank 1 with a category-best 9.8 audio-video sync score and default output that looks closer to high-end stock footage than any competitor, especially on natural scenes and fabric and hair physics."},
                    {"title": "Sora Shutdown Reshapes the Market", "body": "OpenAI shut down Sora in April 2026 after roughly $15M/day in costs against $2.1M lifetime revenue. The exit consolidated the field around Veo, Runway, and Kling and strengthened Veo's position as the default all-rounder."},
                    {"title": "Kling 3.0 Tops the Human Leaderboard on Value", "body": "On the June 2026 human-ranked text-to-video leaderboard, Kling v3 leads with an arena score of 2127. Its 9.7 value-for-money score is the highest on this list, making it the smart pick for high-volume creators on a budget."},
                ],
            },
            "zh-tw": {
                "commentary": "Google Veo 3.1 繼續坐穩第一，而且這禮拜它的優勢又更明確了。AI 影片現在最大的新聞，其實是市場上「少了誰」：OpenAI 在 2026 年 4 月把 Sora 收掉了，原因是每天燒掉大約 1,500 萬美元，但累積總營收只有 210 萬美元。這一收，等於少了一個主要對手，整個市場往 Veo、Runway、Kling 三強集中。Veo 受惠最多，因為它本來就是整體品質最強的全能型，預設輸出的畫面接近高階素材庫等級，尤其自然場景、布料、頭髮的物理表現特別到位。9.8 分的音畫同步是全榜最高，這個功能就是「能用的片段」跟「完成度高的片段」之間的差別。\n\nKling 3.0 排第三，是最值得盯著看的一個。在 2026 年 6 月由真人投票的文生影片排行榜上，Kling v3 其實是第一名，arena 分數 2127，領先 Seedance 2.0 Fast 的 1993。Kling 在電影感打光和複雜運動上追平 Veo，還多了多鏡頭分鏡模式，剪接點之間音訊也能同步。性價比 9.7 分是全榜最高，預算有限但要大量產片的創作者，選它最聰明。\n\nRunway Gen-4.5 排第二，是專業人士的控制台。角色一致性 9.7 分全榜最高，搭配 motion brush、精細運鏡、參考圖驅動角色，畫面必須精準符合創意 brief 時，工作室和認真的創作者還是會回頭用它。Sora 退場後的市場更精實也更競爭，對現在要選工具的人來說是好事。",
                "highlights": [
                    {"title": "Veo 3.1 音畫同步與整體品質雙領先", "body": "Google Veo 3.1 穩坐第一，音畫同步 9.8 分全榜最高，預設輸出接近高階素材庫等級，自然場景、布料、頭髮的物理表現都比對手到位。"},
                    {"title": "Sora 收攤重塑市場版圖", "body": "OpenAI 2026 年 4 月關閉 Sora，每天燒約 1,500 萬美元、累積營收只有 210 萬美元。Sora 退場讓市場往 Veo、Runway、Kling 集中，鞏固了 Veo 全能首選的地位。"},
                    {"title": "Kling 3.0 真人榜奪冠又最划算", "body": "2026 年 6 月真人投票文生影片榜上，Kling v3 以 arena 分數 2127 居冠。性價比 9.7 分全榜最高，要大量產片又有預算考量的創作者最該選它。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK ai-video-generators")


def build_ai_voice_generators():
    d, p = load("best-ai-voice-generators.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Stan Lee Voice and Likeness Licensed to AI Company ElevenLabs", "url": "https://variety.com/2026/biz/news/stan-lee-elevenlabs-licensed-voice-likeness-1236759225/", "source": "Variety"},
            {"title": "Bringing voice AI into the classroom with ElevenLabs", "url": "https://elevenlabs.io/blog/bringing-voice-ai-into-the-classroom-with-elevenlabs", "source": "ElevenLabs"},
            {"title": "ElevenLabs Review 2026: The Most Realistic AI Voice Generator?", "url": "https://ucstrategies.com/news/elevenlabs-review-2026-the-most-realistic-ai-voice-generator/", "source": "UC Strategies"},
        ],
        "i18n": {
            "en": {
                "commentary": "Inworld TTS 1.5 Max holds rank 1 on the strength of the one metric that matters most for real-time applications: latency, where it scores a category-best 9.8. For voice agents, live assistants, and any product where the user is waiting for a reply, that responsiveness is the whole ballgame, and Inworld delivers it without sacrificing a 9.6 voice-realism score. This is the engine I would build a conversational product on today.\n\nElevenLabs sits at rank 2 in a near-tie, and it had the busiest news week in the category. ElevenLabs licensed the voice and likeness of Stan Lee, adding the late Marvel writer to its Iconic Marketplace of celebrity voices that companies can license for commercial use. It also launched an education program giving professors free Pro-tier access and a voice agent built on Einstein's archives. On the product side, Eleven v3 now supports 70+ languages, up from 28, with inline Audio Tags for emotional direction and a 68% reduction in errors on complex text. That 9.7 language-support score is earned, and the v3 alpha discount running through end of June makes this a smart moment to test it.\n\nHume AI Octave 2 at rank 3 remains the specialist's pick, with a category-leading 9.7 emotional-range score for projects where conveying a specific feeling matters more than raw speed. The choice between these three comes down to use case: pick Inworld for the lowest latency in live agents, ElevenLabs for the widest language coverage and the cleanest licensing path, and Hume when emotional nuance is the deliverable. All three are genuinely excellent in 2026, and the field has never been deeper.",
                "highlights": [
                    {"title": "Inworld TTS 1.5 Max Wins on Latency", "body": "Inworld holds rank 1 with a category-best 9.8 latency score alongside 9.6 voice realism. For voice agents and live assistants where the user is waiting on a reply, that responsiveness is the deciding factor."},
                    {"title": "ElevenLabs Licenses Stan Lee and Expands to 70+ Languages", "body": "ElevenLabs added Stan Lee's voice to its Iconic Marketplace and launched an education program with free Pro access for professors. Eleven v3 now supports 70+ languages, up from 28, earning its 9.7 language-support score."},
                    {"title": "Hume AI Octave 2 Owns Emotional Range", "body": "Hume holds rank 3 with a category-leading 9.7 emotional-range score. For projects where conveying a specific feeling matters more than raw speed, it is the specialist's pick."},
                ],
            },
            "zh-tw": {
                "commentary": "Inworld TTS 1.5 Max 穩坐第一，靠的是即時應用最關鍵的那個指標：延遲，它拿到全榜最高的 9.8 分。對語音代理人、即時助理、或任何使用者在等回覆的產品來說，反應速度就是一切，而 Inworld 在做到這點的同時，語音擬真度還有 9.6 分。要做對話型產品，我現在就會選這顆引擎。\n\nElevenLabs 排第二，分數咬得很緊，而且這禮拜它的新聞最多。ElevenLabs 取得了 Stan Lee 的聲音和肖像授權，把這位已故的漫威編劇加進它的 Iconic Marketplace 名人語音庫，企業可以付費商用。它還推出教育計畫，免費給教授 Pro 等級，並做了一個建立在愛因斯坦檔案上的語音代理人。產品面上，Eleven v3 現在支援超過 70 種語言，從原本的 28 種大幅擴充，還加了行內 Audio Tags 做情緒導引，複雜文字的錯誤率降了 68%。語言支援 9.7 分是實打實的，而且 v3 alpha 折扣優惠到六月底，現在正是測試的好時機。\n\nHume AI Octave 2 排第三，仍然是專業需求的選擇，情緒幅度 9.7 分全榜最高，適合「傳達特定情緒」比「純速度」更重要的專案。這三個怎麼選，看用途：要即時代理人最低延遲選 Inworld，要最廣語言覆蓋和最乾淨授權路徑選 ElevenLabs，要情緒細膩度當交付成果就選 Hume。2026 年這三個都真的很強，這個領域從沒這麼有看頭過。",
                "highlights": [
                    {"title": "Inworld TTS 1.5 Max 延遲制勝", "body": "Inworld 穩坐第一，延遲 9.8 分全榜最高，語音擬真度也有 9.6 分。語音代理人、即時助理這類使用者在等回覆的產品，反應速度就是決勝關鍵。"},
                    {"title": "ElevenLabs 拿下 Stan Lee 授權並擴充至 70+ 語言", "body": "ElevenLabs 把 Stan Lee 的聲音加進 Iconic Marketplace，並推出教育計畫免費給教授 Pro 權限。Eleven v3 現支援超過 70 種語言（原 28 種），語言支援 9.7 分當之無愧。"},
                    {"title": "Hume AI Octave 2 情緒幅度稱霸", "body": "Hume 排第三，情緒幅度 9.7 分全榜最高。傳達特定情緒比純速度更重要的專案，它是最對味的專業選擇。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK ai-voice-generators")


def build_bluetooth_speakers():
    d, p = load("best-bluetooth-speakers.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "The best Bluetooth speakers 2026: Which should you buy?", "url": "https://www.soundguys.com/best-bluetooth-speakers-2488/", "source": "SoundGuys"},
            {"title": "Bose SoundLink Plus vs JBL Charge 6: Battle for the best Bluetooth speaker", "url": "https://www.soundguys.com/bose-soundlink-plus-vs-jbl-charge-6-battle-for-the-best-bluetooth-speaker-140264/", "source": "SoundGuys"},
            {"title": "Bose SoundLink Flex (2nd Gen) vs JBL Charge 6: Which Speaker Is Better?", "url": "https://www.rtings.com/speaker/tools/compare/bose-soundlink-flex-2nd-gen-vs-jbl-charge-6/77098/94880", "source": "RTINGS"},
        ],
        "i18n": {
            "en": {
                "commentary": "The JBL Charge 6 stays at rank 1, and as summer listening season ramps up it is the speaker I recommend to the most people. The reason is balance: it packs 45 watts of power, an IP68 dust-and-water rating, and a 24-hour battery, which together make it genuinely reliable whether you are at the beach, a backyard cookout, or a pool deck. The 9.5 durability and 9.5 value scores are the heart of why it wins. It also adds lossless audio over USB-C, so if you stream FLAC from Tidal or Apple Music you get a cleaner signal path than most rivals offer, plus a 7-band customizable EQ that lets you actually dial in the sound.\n\nThe Marshall Emberton III at rank 2 is the pick for people who want a speaker that looks and feels like an object worth owning. The 9.5 battery score and its compact, tactile design make it the easiest one to grab on the way out the door, and the sound is warmer and more refined than its size suggests.\n\nThe Bose SoundLink Max at rank 3 is the choice when sound quality is your top priority. In head-to-head testing the Bose SoundLink line consistently posts higher overall sound-quality scores than the Charge 6, and the SoundLink Plus has beaten its own 20-hour battery claim in real-world testing. If you care more about how a single speaker sounds than about features or ruggedness, Bose is the more musical option. For most buyers heading into summer, though, the Charge 6 remains the smartest all-around buy: louder, tougher, better connected, and priced to move.",
                "highlights": [
                    {"title": "JBL Charge 6 Is the Best All-Around Buy", "body": "With 45W of power, an IP68 rating, a 24-hour battery, and 9.5 scores in both durability and value, the Charge 6 is the most reliable summer speaker. Lossless USB-C audio and a 7-band EQ round out the package."},
                    {"title": "Bose SoundLink Max Wins on Pure Sound", "body": "In head-to-head testing the Bose SoundLink line posts higher overall sound-quality scores than the Charge 6. For buyers who prioritize how a single speaker sounds over features or ruggedness, the SoundLink Max is the more musical pick."},
                    {"title": "Marshall Emberton III Is the Grab-and-Go Favorite", "body": "A 9.5 battery score plus a compact, tactile design make the Emberton III the easiest speaker to take anywhere. Its warm, refined sound punches above its size for casual listening."},
                ],
            },
            "zh-tw": {
                "commentary": "JBL Charge 6 繼續排第一，夏天聽歌旺季一到，它就是我會推薦給最多人的那一台。原因是均衡：45 瓦功率、IP68 防塵防水、24 小時電池，這三項加起來讓它不管在海邊、後院烤肉還是泳池邊都很可靠。耐用度 9.5 分、性價比 9.5 分，就是它勝出的核心。它還支援 USB-C 無損音訊，你用 Tidal 或 Apple Music 串 FLAC，訊號路徑比大多數對手乾淨，再加上 7 段可調 EQ，聲音真的能自己調到位。\n\nMarshall Emberton III 排第二，適合想要一台「拿在手上覺得值得擁有」的人。電池 9.5 分，加上小巧又有質感的設計，出門順手一抓就是它，聲音也比體積暗示的更溫暖、更精緻。\n\nBose SoundLink Max 排第三，當音質是你的第一順位時就選它。一對一實測裡，Bose SoundLink 系列的整體音質分數一直高於 Charge 6，而 SoundLink Plus 在實測中還跑贏自己標示的 20 小時電池。比起功能和耐操度，你更在意一台喇叭單純好不好聽的話，Bose 是更有音樂性的選擇。不過對大多數準備過暑假的人來說，Charge 6 還是最聰明的全能選擇：更大聲、更耐操、連線更好、價格也好入手。",
                "highlights": [
                    {"title": "JBL Charge 6 最強全能首選", "body": "45 瓦功率、IP68 防護、24 小時電池，耐用度與性價比雙 9.5 分，是夏天最可靠的喇叭。USB-C 無損音訊加 7 段 EQ 讓它更完整。"},
                    {"title": "Bose SoundLink Max 純音質取勝", "body": "一對一實測中 Bose SoundLink 系列整體音質分數高於 Charge 6。比起功能和耐操度更在意一台喇叭單純好不好聽的人，SoundLink Max 是更有音樂性的選擇。"},
                    {"title": "Marshall Emberton III 隨手帶走最對味", "body": "電池 9.5 分加上小巧有質感的設計，Emberton III 是最好帶出門的一台。溫暖精緻的聲音以這個體積來說相當超值，日常聆聽很夠用。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK bluetooth-speakers")


def build_noise_cancelling_headphones():
    d, p = load("best-noise-cancelling-headphones.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "I tested the Sony WH-1000XM6 vs Bose QuietComfort Ultra 2 for 6 months — and there's a clear winner", "url": "https://www.tomsguide.com/audio/headphones/i-tested-the-sony-wh-1000xm6-vs-bose-quietcomfort-ultra-2-for-6-months-and-theres-a-clear-winner", "source": "Tom's Guide"},
            {"title": "Sony WH-1000XM6 vs Bose QuietComfort Ultra Headphones (2nd Gen): which flagship wireless over-ears are best?", "url": "https://www.whathifi.com/headphones/wireless-headphones/sony-wh-1000xm6-vs-bose-quietcomfort-ultra-headphones-2nd-gen-which-flagship-wireless-over-ears-are-best", "source": "What Hi-Fi?"},
            {"title": "Sony WH-1000XM6 vs Bose QuietComfort Ultra Headphones: Battle of the ANC heavyweights", "url": "https://www.soundguys.com/sony-wh-1000xm6-vs-bose-quietcomfort-ultra-headphones-137869/", "source": "SoundGuys"},
        ],
        "i18n": {
            "en": {
                "commentary": "The Sony WH-1000XM6 holds rank 1, and the latest round of long-term testing confirms why it remains the class leader. In controlled measurements Sony reduces average ambient loudness by 87%, just ahead of the Bose QuietComfort Ultra 2 at 85%, and that 9.6 noise-cancellation score plays out exactly as you would hope on a plane or a noisy train. What pushes Sony over the top for me is the combination of that ANC with a 9.5 sound-quality score and a 10-band EQ that gives you real control over tuning. Sony's signature here is warmer and weightier than Bose, and after six months of testing reviewers still land on the XM6 as the overall winner at this price.\n\nThe Bose QuietComfort Ultra 2 at rank 2 is the comfort and isolation champion. Its more amply padded earcups and headband fatigue more slowly than Sony's somewhat thin padding, so for long-haul flights or full workdays it is the more wearable option. The second-gen model adds an auto-sleep mode that drops into low power when you take it off, no case required. Some testers genuinely rate its ANC as the best, full stop, calling it the set that blocks out everything. If comfort over many hours is your priority, this is the one.\n\nThe Sennheiser Momentum 4 at rank 3 stays the audiophile's value pick, pairing a 9.3 sound-quality score with a class-leading 9.5 battery-life rating. For listeners who care most about tonal accuracy and want their headphones to last days between charges, it remains a standout. The top three here are genuinely close, and the right call comes down to whether you weight raw ANC, all-day comfort, or sound character most.",
                "highlights": [
                    {"title": "Sony WH-1000XM6 Stays the Class Leader", "body": "Sony reduces average ambient loudness by 87% in measurements, edging the Bose QC Ultra 2 at 85%. Combined with a 9.5 sound-quality score and a 10-band EQ, the XM6 remains the reviewers' overall winner after six months of testing."},
                    {"title": "Bose QuietComfort Ultra 2 Wins on Comfort", "body": "More amply padded earcups and headband make the QC Ultra 2 the more wearable choice for long flights and full workdays. A new auto-sleep mode drops it into low power when removed, no case required."},
                    {"title": "Sennheiser Momentum 4 Is the Audiophile Value Pick", "body": "A 9.3 sound-quality score paired with a class-leading 9.5 battery-life rating makes the Momentum 4 the standout for listeners who prioritize tonal accuracy and want days of playback between charges."},
                ],
            },
            "zh-tw": {
                "commentary": "Sony WH-1000XM6 穩坐第一，最新一輪長期實測再次說明它為什麼還是同級之王。在受控量測裡，Sony 把環境平均音量降低 87%，些微領先 Bose QuietComfort Ultra 2 的 85%，而這個 9.6 分的降噪表現，在飛機上或吵雜的火車上完全如你所願。讓 Sony 在我心中勝出的，是降噪加上 9.5 分的音質，再配上 10 段 EQ，調音的自由度很高。Sony 的調性比 Bose 更溫暖、更有重量感，評測者用了六個月後，這個價位還是把 XM6 評為總體冠軍。\n\nBose QuietComfort Ultra 2 排第二，是舒適度和隔音的冠軍。它的耳罩和頭帶填充更飽滿，比 Sony 偏薄的填充更不容易戴累，長途飛行或整天上班，它是更耐戴的選擇。二代還加了自動休眠模式，拿下來就進低耗電，不用收進盒子。有些評測者真心認為它的降噪是最強的，說它能把所有聲音擋掉。長時間配戴的舒適是你的首要考量的話，選它。\n\nSennheiser Momentum 4 排第三，仍然是發燒友的性價比選擇，9.3 分音質搭配同級最高的 9.5 分電池續航。最在意音色準確、又希望耳機充一次能撐好幾天的人，它依然出色。前三名其實咬得很緊，怎麼選就看你最重視純降噪、全天舒適、還是聲音個性。",
                "highlights": [
                    {"title": "Sony WH-1000XM6 穩坐同級之王", "body": "量測中 Sony 把環境平均音量降低 87%，些微領先 Bose QC Ultra 2 的 85%。加上 9.5 分音質和 10 段 EQ，評測者用六個月後仍把 XM6 評為總體冠軍。"},
                    {"title": "Bose QuietComfort Ultra 2 舒適度取勝", "body": "更飽滿的耳罩和頭帶填充讓 QC Ultra 2 更耐戴，長途飛行和整天上班都更舒服。新增自動休眠模式，拿下來就進低耗電，不用收盒子。"},
                    {"title": "Sennheiser Momentum 4 發燒性價比之選", "body": "9.3 分音質搭配同級最高 9.5 分電池續航，Momentum 4 是最在意音色準確、又希望充一次撐好幾天的人的出色選擇。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK noise-cancelling-headphones")


def build_wireless_earbuds():
    d, p = load("best-wireless-earbuds.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "The Sony WF-1000XM6 are officially our favourite flagship wireless earbuds", "url": "https://www.whathifi.com/headphones/wireless-earbuds/the-sony-wf-1000xm6-are-officially-our-favourite-flagship-wireless-earbuds", "source": "What Hi-Fi?"},
            {"title": "AirPods Pro 3 vs. Sony WF-1000XM6: Which Flagship Earbuds Should You Buy?", "url": "https://www.macrumors.com/2026/04/21/sony-wf1000xm6-vs-airpods-pro-3/", "source": "MacRumors"},
            {"title": "Sony WF-1000XM6 vs Apple AirPods Pro 3: which premium wireless earbuds are better?", "url": "https://www.whathifi.com/headphones/wireless-earbuds/sony-wf-1000xm6-vs-apple-airpods-pro-3-which-premium-wireless-earbuds-are-better", "source": "What Hi-Fi?"},
        ],
        "i18n": {
            "en": {
                "commentary": "The Sony WF-1000XM6 holds rank 1, and What Hi-Fi has now named it their favorite flagship wireless earbuds outright. The headline upgrade is the new HD Noise Cancelling Processor QN3e, which is three times faster than the QN2e in the previous generation, and you hear the result in the 9.7 ANC score that leads this list. Beyond noise cancellation, the XM6 delivers excellent sound, AI-powered beamforming for standout call quality, LDAC for high-resolution audio on Android, and a 10-band EQ for people who like to tinker. At $330 it is the premium pick, and reviewers consistently rate it as sounding slightly better than the AirPods Pro 3.\n\nThe AirPods Pro at rank 2 remain the obvious answer for anyone living in Apple's ecosystem. The newest AirPods Pro 3 launched at $249, which undercuts the Sony by more than $80, and the seamless handoff across iPhone, iPad, and Mac is something no Android-first competitor can replicate. The 9.0 comfort score reflects a fit that disappears in your ears over a long day. If you carry an iPhone, this is the more sensible buy.\n\nThe Bose QuietComfort Earbuds at rank 3 stay the comfort-and-isolation specialist, with a 9.4 ANC score that rivals the leaders. The decision across the top three is mostly about ecosystem and fit: Sony for the best overall sound and noise cancellation, AirPods for Apple integration and value, and Bose when all-day comfort and isolation are what you care about most. All three are excellent, and the gap between them is small enough that you can buy on preference rather than worrying about missing out.",
                "highlights": [
                    {"title": "Sony WF-1000XM6 Leads on ANC and Sound", "body": "The new QN3e processor is three times faster than the previous generation, driving a class-leading 9.7 ANC score. Add LDAC, AI beamforming for calls, and a 10-band EQ, and What Hi-Fi now rates the XM6 as its favorite flagship earbuds."},
                    {"title": "AirPods Pro 3 Undercut Sony on Price", "body": "The newest AirPods Pro 3 launched at $249, more than $80 cheaper than the Sony, with seamless handoff across iPhone, iPad, and Mac. For anyone in the Apple ecosystem, it is the more sensible buy."},
                    {"title": "Bose QuietComfort Earbuds Own Comfort and Isolation", "body": "A 9.4 ANC score rivals the leaders, and Bose's signature fit makes these the pick when all-day comfort and isolation matter most to you."},
                ],
            },
            "zh-tw": {
                "commentary": "Sony WF-1000XM6 穩坐第一，What Hi-Fi 現在更直接把它評為心目中最愛的旗艦真無線耳機。最大的升級是全新的 HD 降噪處理器 QN3e，速度是上一代 QN2e 的三倍，這個結果你聽得到，就反映在領先全榜的 9.7 分 ANC 上。除了降噪，XM6 還有優異的音質、AI 波束成形帶來出色的通話品質、Android 上支援 LDAC 高解析音訊，以及給愛調音的人用的 10 段 EQ。售價 330 美元，是高階首選，評測者一致認為它聽起來比 AirPods Pro 3 略勝一籌。\n\nAirPods Pro 排第二，對活在 Apple 生態系裡的人來說是理所當然的答案。最新的 AirPods Pro 3 上市價 249 美元，比 Sony 便宜 80 多美元，而且在 iPhone、iPad、Mac 之間無縫切換，這點是任何主打 Android 的對手都複製不來的。舒適度 9.0 分，反映的是戴一整天會忘記它存在的服貼感。你帶的是 iPhone 的話，這台是更合理的選擇。\n\nBose QuietComfort Earbuds 排第三，仍然是舒適與隔音的專家，9.4 分的 ANC 直逼領先群。前三名怎麼選，主要看生態系和配戴感：要最佳整體音質和降噪選 Sony，要 Apple 整合和性價比選 AirPods，最在意整天舒適和隔音就選 Bose。三台都很優秀，彼此差距小到你可以照喜好買，不用怕選錯。",
                "highlights": [
                    {"title": "Sony WF-1000XM6 降噪與音質雙領先", "body": "全新 QN3e 處理器速度是上一代的三倍，撐起全榜最高的 9.7 分 ANC。再加上 LDAC、通話 AI 波束成形和 10 段 EQ，What Hi-Fi 現在把 XM6 評為最愛旗艦耳機。"},
                    {"title": "AirPods Pro 3 價格壓過 Sony", "body": "最新 AirPods Pro 3 上市價 249 美元，比 Sony 便宜 80 多美元，並在 iPhone、iPad、Mac 間無縫切換。活在 Apple 生態系裡的人，它是更合理的選擇。"},
                    {"title": "Bose QuietComfort Earbuds 舒適與隔音專家", "body": "9.4 分的 ANC 直逼領先群，Bose 招牌服貼感讓它成為最在意整天舒適和隔音時的首選。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK wireless-earbuds")


def build_smart_speakers():
    d, p = load("best-smart-speakers.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "14 Best Smart Speakers of 2026", "url": "https://www.reviewed.com/smarthome/best-right-now/best-smart-speakers", "source": "Reviewed"},
            {"title": "Best smart speaker 2026", "url": "https://www.androidcentral.com/best-smart-speaker", "source": "Android Central"},
            {"title": "Amazon Echo Studio Smart Speaker vs Sonos Era 100 Smart Speaker Comparison", "url": "https://hometheaterreview.com/vs/amazon-echo-studio-smart-speaker-vs-sonos-era-100-smart-speaker-comparison/", "source": "HomeTheaterReview"},
        ],
        "i18n": {
            "en": {
                "commentary": "The Amazon Echo Studio (2nd Gen) holds rank 1, and it earns it by being the most complete smart speaker for a connected home. Its 9.5 smart-home-integration score is the highest on this list, and that matters more than any single audio spec when the speaker is also the brain of your lights, locks, and routines. On the audio side it is a genuine performer: a five-driver configuration with a 5.25-inch subwoofer plus Dolby Atmos delivers immersive, room-filling sound, which is why Wirecutter calls it the best smart speaker for music. If you want one device that does both jobs well, this is it.\n\nThe Sonos Era 100 at rank 2 is the audiophile's choice and the one Wired names the best smart speaker overall. Its 9.5 sound-quality score is the highest here, and the tuning is more neutral and accurate than the Echo, with vocals that come through clearer and more natural. It supports Alexa and offers the flexibility of the broader Sonos multi-room ecosystem, so if you care most about how music actually sounds and plan to add speakers over time, the Era 100 is the smarter long-term platform.\n\nThe Apple HomePod (2nd Gen) at rank 3 remains the obvious pick for Apple households. It pairs a 9.0 sound-quality score with deep Siri and HomeKit integration, and for anyone whose home already runs on Apple devices, the handoff and ecosystem fit are worth a lot. The right choice across the top three comes down to your platform: Echo Studio for the most capable Alexa smart home, Sonos Era 100 for the best pure audio and multi-room flexibility, and HomePod when you are all-in on Apple.",
                "highlights": [
                    {"title": "Amazon Echo Studio Leads on Smart Home", "body": "A category-best 9.5 smart-home-integration score plus a five-driver Dolby Atmos setup make the Echo Studio the most complete pick. Wirecutter calls it the best smart speaker for music, and it doubles as the brain of your connected home."},
                    {"title": "Sonos Era 100 Wins on Pure Audio", "body": "The Era 100's 9.5 sound-quality score is the highest here, with neutral, accurate tuning and clearer vocals. Wired names it the best smart speaker overall, and it slots into the broader Sonos multi-room ecosystem."},
                    {"title": "Apple HomePod Is the Apple-Household Pick", "body": "A 9.0 sound-quality score plus deep Siri and HomeKit integration make the HomePod 2nd Gen the obvious choice for homes already running on Apple devices, where the ecosystem fit pays off daily."},
                ],
            },
            "zh-tw": {
                "commentary": "Amazon Echo Studio（第二代）穩坐第一，它靠的是當一個連網家庭最完整的智慧喇叭。智慧家庭整合 9.5 分是全榜最高，當這台喇叭同時是你家燈光、門鎖、自動化情境的大腦時，這點比任何單一音訊規格都重要。音訊方面它也是真本事：五單體配置加上 5.25 吋低音單體和 Dolby Atmos，營造沉浸式、充滿整個房間的聲音，這也是 Wirecutter 把它評為最佳音樂智慧喇叭的原因。想要一台兩件事都做得好的裝置，就是它。\n\nSonos Era 100 排第二，是發燒友的選擇，也是 Wired 評選的最佳智慧喇叭。音質 9.5 分全榜最高，調音比 Echo 更中性準確，人聲更清晰自然。它支援 Alexa，也能接進更大的 Sonos 多房間生態系，所以你最在意音樂實際聽起來如何、又打算之後慢慢加喇叭的話，Era 100 是更聰明的長期平台。\n\nApple HomePod（第二代）排第三，仍然是 Apple 家庭理所當然的選擇。音質 9.0 分搭配深度的 Siri 和 HomeKit 整合，家裡已經跑在 Apple 裝置上的人，那種無縫接續和生態系契合度很有價值。前三名怎麼選，看你的平台：要最強的 Alexa 智慧家庭選 Echo Studio，要最佳純音質和多房間彈性選 Sonos Era 100，全套都用 Apple 就選 HomePod。",
                "highlights": [
                    {"title": "Amazon Echo Studio 智慧家庭領先", "body": "智慧家庭整合 9.5 分全榜最高，加上五單體 Dolby Atmos 配置，Echo Studio 是最完整的選擇。Wirecutter 評它為最佳音樂智慧喇叭，同時還能當連網家庭的大腦。"},
                    {"title": "Sonos Era 100 純音質取勝", "body": "Era 100 音質 9.5 分全榜最高，調音中性準確、人聲更清晰。Wired 評它為最佳智慧喇叭，還能接進更大的 Sonos 多房間生態系。"},
                    {"title": "Apple HomePod 是 Apple 家庭首選", "body": "音質 9.0 分加上深度 Siri 與 HomeKit 整合，HomePod 第二代是家裡已經跑在 Apple 裝置上的人理所當然的選擇，生態系契合度每天都用得到。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK smart-speakers")


if __name__ == "__main__":
    build_ai_music_generators()
    build_ai_video_generators()
    build_ai_voice_generators()
    build_bluetooth_speakers()
    build_noise_cancelling_headphones()
    build_wireless_earbuds()
    build_smart_speakers()
    print("Batch 2 complete")
