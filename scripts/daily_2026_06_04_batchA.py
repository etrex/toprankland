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

# ---------------- best-ai-chatbots ----------------
do("best-ai-chatbots.json",
   [
     {"title": "AI Chatbots Comparison: ChatGPT, Claude, Gemini and more", "url": "https://artificialanalysis.ai/agents/chatbots", "source": "Artificial Analysis"},
     {"title": "AI Model Benchmarks June 2026: GPT-5.5, Claude, Gemini, Grok", "url": "https://lmcouncil.ai/benchmarks", "source": "LM Council"},
   ],
   {
     "commentary": "Heading into June 2026 the consumer chatbot race is the tightest it has ever been, and I am keeping ChatGPT at the top for one practical reason: reach. GPT-5.5, OpenAI's flagship since April, still leads creative writing and powers the app that hundreds of millions of casual users open by default. On the raw Artificial Analysis Intelligence Index, Claude Opus 4.8 actually edges ahead at 61.4 against GPT-5.5's 60.2, which is exactly why Claude sits a close second here. If your day is mostly coding or careful long-form reasoning, Claude is the one I reach for first, and the gap is small enough that picking either feels safe. Gemini holds third on the strength of Gemini 3.1 Pro, which since its February launch has been the best of the big four for data analysis and structured reasoning, and Google's free tier keeps it in front of the average user. Grok stays mid-pack but earns its keep: xAI's 4.3 release at the end of April is the cheapest of the flagship models with genuinely strong tool-use scores, so for high-volume agentic workloads it is the value play. Perplexity remains my pick when the answer needs to be sourced and current, because its search-grounded answers still beat a general chatbot for anything you would otherwise Google. The rest of the board, Copilot, DeepSeek, Meta AI, Mistral and Qwen, are carried forward unchanged because nothing this week reshuffled them. My honest take: stop chasing the single best model. Match the tool to the task and you win on every axis that matters.",
     "highlights": [
       {"title": "ChatGPT keeps number one on reach", "body": "GPT-5.5 has led creative writing since its April launch and the app is the default for hundreds of millions of casual users. A consumer ranking should reward the product people actually open, and that is still ChatGPT by a wide margin."},
       {"title": "Claude is the benchmark leader", "body": "Claude Opus 4.8 tops the Artificial Analysis Intelligence Index at 61.4, just ahead of GPT-5.5 at 60.2. For coding and careful long-form reasoning it is the model I open first, which is why it sits a hair behind the top spot."},
       {"title": "Gemini owns reasoning and the free tier", "body": "Gemini 3.1 Pro has been the best of the big four for data analysis and structured reasoning since February. Google's generous free access keeps it in front of everyday users who never pay for a chatbot."},
       {"title": "Grok is the value flagship", "body": "Grok 4.3 from late April is the cheapest of the four flagships and posts strong agentic and tool-use scores. For high-volume automated workloads where token cost dominates, it is the smart pick."},
     ],
   },
   {
     "commentary": "2026 年 6 月這個時間點，消費級聊天機器人的競爭比以往任何時候都更貼身，但我還是把 ChatGPT 放第一，理由很現實，就是觸及面。GPT-5.5 從 4 月當上 OpenAI 旗艦後，創意寫作依然稱霸，而且它撐起的那個 App 是好幾億輕度使用者打開就用的預設選擇。話說回來，純看 Artificial Analysis 智慧指數，Claude Opus 4.8 其實以 61.4 小贏 GPT-5.5 的 60.2，這也正是 Claude 緊咬第二的原因。如果你一天大部分時間在寫程式或處理需要細心推理的長文，我第一個開的就是 Claude，而且差距小到選哪個都很安全。Gemini 守住第三靠的是 Gemini 3.1 Pro，從 2 月上線以來，它在資料分析跟結構化推理上是四大旗艦裡最強的，加上 Google 免費額度大方，一般人用起來很有感。Grok 留在中段但站得住腳，xAI 4.3 在 4 月底推出，是旗艦群裡最便宜的，工具呼叫分數又紮實，量大的自動化任務拿它來算成本最划算。Perplexity 我自己在需要附來源、要最新資料時還是會選它，搜尋導向的回答對那種你本來要去 Google 的問題特別好用。後面的 Copilot、DeepSeek、Meta AI、Mistral、Qwen 這週沒有大事件，排名照舊。老實講，別再執著找唯一最強的模型了，把工具對準任務，每一項你都會贏。",
     "highlights": [
       {"title": "ChatGPT 靠觸及面守住第一", "body": "GPT-5.5 從 4 月上線後創意寫作一直領先，App 又是好幾億輕度使用者的預設選擇。消費級榜單該獎勵的就是大家真的會打開的產品，這點 ChatGPT 還是大幅領先。"},
       {"title": "Claude 是跑分冠軍", "body": "Claude Opus 4.8 在 Artificial Analysis 智慧指數拿 61.4，小贏 GPT-5.5 的 60.2。寫程式跟細心長文推理我第一個開的就是它，所以它緊咬第一只差一點點。"},
       {"title": "Gemini 推理跟免費額度都強", "body": "Gemini 3.1 Pro 從 2 月起在四大旗艦裡，資料分析跟結構化推理最強。Google 免費額度又大方，讓它在從不付費的日常使用者面前站得很前面。"},
       {"title": "Grok 是高性價比旗艦", "body": "4 月底的 Grok 4.3 是四大旗艦裡最便宜的，工具呼叫跟代理任務分數都不錯。量大、成本掛帥的自動化工作流，拿它最聰明。"},
     ],
   })

# ---------------- best-ai-coding-assistants ----------------
do("best-ai-coding-assistants.json",
   [
     {"title": "Best AI Coding Assistants 2026: Cursor vs Copilot vs Claude Code", "url": "https://scrimba.com/articles/best-ai-coding-assistants-2026/", "source": "Scrimba"},
     {"title": "Claude Code vs Cursor vs Codex vs Antigravity, six months in", "url": "https://thenewstack.io/claude-code-vs-cursor-vs-codex-vs-antigravity-2026/", "source": "The New Stack"},
   ],
   {
     "commentary": "June brought real pricing and branding moves in the coding-tool space, and they sharpen rather than upend my ranking. Claude Code stays at number one because it is still the tool most production teams hand goal-level work to: describe an outcome, walk away, come back to a coherent multi-file change. Cursor holds second as the deepest in-editor experience, and its June Teams restructure into Standard seats at 32 dollars per seat annually and Premium at 96 makes the value math clearer for growing teams. Most shops I talk to run both, Cursor for line-level edits and Claude Code for delegation, and the new pricing does not change that pairing. The notable shake-up is at the edges of the board: Windsurf was renamed Devin Desktop on June 2 and now speaks the open Agent Client Protocol, so I am treating it as a continuation of the same product rather than a demotion, and it stays put. GitHub Copilot moved to usage-based AI Credits on June 1, which makes it harder to recommend blindly to casual users but keeps it the most broadly compatible option across editors, so third for OpenAI Codex and fourth for Copilot both hold. Google Jules sits fifth on the strength of Antigravity 2.0's multi-agent relaunch in May with Gemini 3.5 Flash as default. Everything below, Devin, Amazon Q, Zed, Aider, Windsurf and Augment, carries forward. The headline this month is billing, not capability, so I kept rank changes to zero and let the verdicts do the talking.",
     "highlights": [
       {"title": "Claude Code owns goal-level delegation", "body": "It remains the tool teams trust to take an outcome description and return a coherent multi-file change. That delegation workflow is what keeps it at number one even as rivals close on raw model quality."},
       {"title": "Cursor's new pricing clarifies the value", "body": "June's Teams restructure sets Standard seats at 32 dollars annually and Premium at 96 with 5x usage. As the deepest in-editor AI experience, it is still the line-level companion most teams pair with Claude Code."},
       {"title": "Copilot is now usage-based but still universal", "body": "The June 1 move to AI Credits changes the billing model, yet Copilot stays the most broadly compatible assistant across editors and languages. That reach keeps it solidly in the top four."},
       {"title": "Windsurf is now Devin Desktop", "body": "The June 2 rename brings open Agent Client Protocol support, so I treat it as the same product evolving rather than a new entrant. Its rank holds because the underlying tool and its strengths are unchanged."},
     ],
   },
   {
     "commentary": "6 月寫程式工具圈出現了真實的價格跟品牌動作，這些消息讓我的排名更清晰，而不是被翻盤。Claude Code 還是第一，因為它依然是多數正式團隊願意交付「目標級」工作的工具，你描述一個結果，人走開，回來就是一份前後一致的跨檔案修改。Cursor 守第二，編輯器內整合最深，6 月它把 Teams 方案重整成 Standard 每席年繳約台幣一千、Premium 約三千的級距，成長中的團隊算起來更好懂。我聊過的多數團隊兩個一起用，Cursor 做行級編輯、Claude Code 做委派，新價格沒改變這個搭配。比較有看頭的變動在榜單邊緣，Windsurf 在 6 月 2 日改名 Devin Desktop，現在支援開放的 Agent Client Protocol，我把它當同一個產品的延續，排名不動。GitHub Copilot 6 月 1 日改成用量計費的 AI Credits，要無腦推薦給輕度使用者變難了，但它仍是跨編輯器相容性最好的選擇，所以 Codex 第三、Copilot 第四都守住。Google Jules 排第五，靠的是 5 月 Antigravity 2.0 多代理重啟、預設用 Gemini 3.5 Flash。再下面的 Devin、Amazon Q、Zed、Aider、Windsurf、Augment 全部照舊。這個月的重點是計費，不是能力，所以我把排名變動壓到零，讓判斷本身說話。",
     "highlights": [
       {"title": "Claude Code 主宰目標級委派", "body": "它依然是團隊敢把「描述一個結果」交出去、然後拿回前後一致跨檔案修改的工具。這套委派工作流，是它在對手追近模型品質之際還能守第一的原因。"},
       {"title": "Cursor 新價格讓性價比更清楚", "body": "6 月 Teams 重整把 Standard 設在每席年繳約台幣一千、Premium 約三千含五倍用量。身為編輯器內整合最深的體驗，它仍是多數團隊拿來搭配 Claude Code 的行級夥伴。"},
       {"title": "Copilot 改用量計費但仍最通用", "body": "6 月 1 日改成 AI Credits 改了計費模式，但 Copilot 依然是跨編輯器、跨語言相容性最好的助手。這份廣度讓它穩穩待在前四。"},
       {"title": "Windsurf 現在叫 Devin Desktop", "body": "6 月 2 日改名同時帶來開放 Agent Client Protocol 支援，我把它當同一產品的演進，不是新面孔。底層工具跟強項沒變，所以排名不動。"},
     ],
   })

# ---------------- best-ai-image-generators ----------------
do("best-ai-image-generators.json",
   [
     {"title": "Best AI Image Generators June 2026: Midjourney, Flux, DALL-E", "url": "https://aiflashreport.com/ai-image-generators.html", "source": "AI Flash Report"},
     {"title": "Best AI Image Generators 2026, ranked by blind human votes", "url": "https://llm-stats.com/leaderboards/best-ai-for-image-generation", "source": "LLM-Stats"},
   ],
   {
     "commentary": "The image-generation field in June 2026 has fully specialized, and my ranking reflects that rather than pretending one model wins everything. Midjourney V8 stays at the top for me because aesthetic quality is still where it is untouchable, and the V8 Alpha that just dropped renders roughly 5x faster with native 2K output, so the one historical knock against it, speed, is shrinking fast. Flux 2 Pro holds second as the photorealism default: if the brief is product photography or a portrait that has to pass as a real photo, this is what I open. The interesting tension is at number three, where GPT Image 2 currently tops the blind-vote arena with a score around 530, well ahead of the pack. I am keeping it third because raw arena ELO rewards prompt-following and versatility more than the artistic ceiling that still separates Midjourney, but it is the most well-rounded single tool on the board and a defensible number one for anyone who values reliability over style. Ideogram V3 stays fourth on the strength of text rendering that nobody else matches, the go-to for posters, packaging and any image with headline copy baked in. Imagen 4, Firefly 4, SD 3.5 Large, Recraft, Krea and Leonardo all carry forward unchanged because nothing this week moved them. My advice this month: pick by job. Midjourney for art, Flux for realism, GPT Image 2 for all-purpose reliability, Ideogram for text. That is the whole map.",
     "highlights": [
       {"title": "Midjourney V8 still owns aesthetics", "body": "Artistic image quality is where it remains untouchable, and the new V8 Alpha renders about 5x faster with native 2K output. The old speed complaint is fading, which keeps it at number one for anyone who cares how an image looks."},
       {"title": "Flux 2 Pro is the photorealism default", "body": "For product photography or a portrait that must pass as a real photo, this is the one I open first. That realism focus keeps it a clear second for commercial work where the image cannot look generated."},
       {"title": "GPT Image 2 is the all-rounder", "body": "It currently tops the blind-vote arena around 530, well ahead of the field on prompt-following and versatility. It is the most reliable single tool here and a defensible top pick for anyone valuing consistency over artistic ceiling."},
       {"title": "Ideogram V3 wins on text", "body": "It renders headline copy, logos and packaging mockups with an accuracy nobody else reliably matches. For any image that needs readable text baked in, it stays the specialist worth keeping in the kit."},
     ],
   },
   {
     "commentary": "2026 年 6 月的 AI 生圖已經徹底分眾，我的排名就照這個現實走，不假裝有哪個模型全包。Midjourney V8 我還是放第一，因為美感品質它依舊無敵，剛丟出來的 V8 Alpha 算圖快了大約 5 倍、原生 2K 輸出，過去唯一被嫌的速度問題正在快速縮小。Flux 2 Pro 守第二，是寫實的預設選擇，如果案子是商品攝影或要能當真人照片用的人像，我就開它。比較有張力的是第三名，GPT Image 2 現在在盲測競技場以約 530 分領先一大截。我把它擺第三，是因為競技場 ELO 獎勵的是指令遵循跟全能性，而 Midjourney 拉開差距靠的是藝術天花板，但平心而論 GPT Image 2 是榜上最全能的單一工具，對重視穩定勝過風格的人來說，放第一也說得通。Ideogram V3 守第四，靠的是沒人比得上的文字渲染，海報、包裝、任何要把標題文字嵌進去的圖都找它。Imagen 4、Firefly 4、SD 3.5 Large、Recraft、Krea、Leonardo 這週沒事件，全部照舊。這個月我的建議很簡單，看任務選工具，藝術找 Midjourney、寫實找 Flux、全能穩定找 GPT Image 2、文字找 Ideogram，整張地圖就這樣。",
     "highlights": [
       {"title": "Midjourney V8 美感依舊無敵", "body": "藝術圖質它還是沒人能碰，新的 V8 Alpha 算圖快約 5 倍、原生 2K 輸出。過去被嫌的速度問題正在消失，對在意成品好不好看的人，第一名穩穩的。"},
       {"title": "Flux 2 Pro 是寫實預設", "body": "商品攝影、或要能當真人照片用的人像，我第一個開它。這份寫實專注讓它在不能露出 AI 痕跡的商用場景穩坐第二。"},
       {"title": "GPT Image 2 是全能王", "body": "它現在在盲測競技場約 530 分，指令遵循跟全能性領先一截。是榜上最穩的單一工具，對重視一致性勝過藝術天花板的人，放第一也合理。"},
       {"title": "Ideogram V3 贏在文字", "body": "標題文字、Logo、包裝模擬，它渲染的準確度沒人能穩定追上。任何要嵌入可讀文字的圖，它都是值得留在工具箱裡的專家。"},
     ],
   })

# ---------------- best-ai-meeting-assistants ----------------
do("best-ai-meeting-assistants.json",
   [
     {"title": "The 10 best AI meeting assistants in 2026", "url": "https://zapier.com/blog/best-ai-meeting-assistant/", "source": "Zapier"},
     {"title": "Meeting note tool pricing: Granola vs Fireflies vs Fathom vs Otter", "url": "https://www.granola.ai/blog/meeting-note-tool-pricing-granola-vs-fireflies-fathom-otter", "source": "Granola"},
   ],
   {
     "commentary": "Going into June 2026 the meeting-assistant category has split cleanly along one question: do you want a bot in the call or not, and I keep Granola at number one because it answers that best. It captures audio straight from your desktop output with no visible bot in the participant list, which matters more than ever now that plenty of clients and legal teams flag recording bots. Accuracy lands around 90 to 93 percent, close enough to the leaders that the privacy win is worth it. Fathom holds second and is genuinely the best free choice on the board: unlimited Zoom recording with no minute cap, 30-second post-call summaries, and the highest G2 rating in the category at 5.0 from over 6,000 reviews. If you are an individual or a small team that does not want to pay, I send you to Fathom first. Fireflies stays third as the searchable team archive with the deepest integration spread. Otter holds fourth and still posts the best raw transcription, 93 to 95 percent in good audio, which keeps it the pick when accuracy of the transcript itself is the whole job. The rest of the board, Fellow, tl;dv, Read.ai, Krisp, Zoom AI Companion, Avoma, Circleback, Microsoft 365 Copilot and Gong, carries forward unchanged. No launch this week justified a reshuffle, so I held ranks and let the bot-versus-no-bot framing guide the verdicts.",
     "highlights": [
       {"title": "Granola wins by skipping the bot", "body": "It records straight from your desktop audio with no visible bot in the call, which clients and legal teams increasingly demand. At 90 to 93 percent accuracy it gives up almost nothing for that privacy, keeping it at number one."},
       {"title": "Fathom is the best free option", "body": "Unlimited Zoom recording with no minute cap, 30-second summaries, and a 5.0 G2 rating from over 6,000 reviews. For an individual or small team that refuses to pay, this is the first tool I recommend."},
       {"title": "Otter still leads on raw accuracy", "body": "It posts 93 to 95 percent transcription accuracy in good audio, the best on the board. When a verbatim, searchable transcript is the entire deliverable, Otter stays the specialist pick."},
       {"title": "Fireflies owns the searchable archive", "body": "Its deep integration spread and team-wide search keep it third. For organizations that treat meeting notes as a knowledge base rather than a one-off summary, it remains the natural backbone."},
     ],
   },
   {
     "commentary": "2026 年 6 月，會議助理這個類別其實乾淨地分成一個問題，你到底要不要在會議裡放一隻 bot，我把 Granola 放第一就是因為它把這題答得最好。它直接從你桌面的音訊輸出抓聲音，與會者名單上不會出現一隻看得見的機器人，這點現在比以前更重要，因為不少客戶跟法務團隊看到錄音 bot 就皺眉。準確度落在 90 到 93 趴，跟領先群夠接近，這個隱私上的勝利很值得。Fathom 守第二，平心而論是榜上最好的免費選擇，Zoom 無限錄製、沒有分鐘上限，會後 30 秒出摘要，G2 評分還是全類別最高的 5.0、超過六千則評論。如果你是個人或不想付錢的小團隊，我第一個叫你去用 Fathom。Fireflies 守第三，是可搜尋的團隊知識庫，整合鋪得最廣。Otter 守第四，純逐字稿準確度還是最強，音質好時 93 到 95 趴，當任務本身就是要一份精準逐字稿，它就是首選。其餘的 Fellow、tl;dv、Read.ai、Krisp、Zoom AI Companion、Avoma、Circleback、Microsoft 365 Copilot、Gong 全部照舊。這週沒有哪個新發布值得洗牌，所以我守住排名，讓「要不要 bot」這個框架去帶判斷。",
     "highlights": [
       {"title": "Granola 靠不放 bot 取勝", "body": "它直接從桌面音訊錄，會議裡看不到機器人，這正是客戶跟法務越來越要求的。90 到 93 趴的準確度幾乎沒為隱私犧牲什麼，所以第一名是它。"},
       {"title": "Fathom 是最佳免費選擇", "body": "Zoom 無限錄製沒分鐘上限、30 秒出摘要、G2 評分 5.0 超過六千則評論。個人或死不付錢的小團隊，我第一個推這個。"},
       {"title": "Otter 純準確度仍領先", "body": "音質好時逐字稿準確度 93 到 95 趴，是榜上最高。當交付物就是一份精準、可搜尋的逐字稿，Otter 還是那個專家選擇。"},
       {"title": "Fireflies 主打可搜尋知識庫", "body": "整合鋪得最廣、全團隊可搜尋，守住第三。把會議記錄當知識庫而不是一次性摘要的組織，它仍是天然的骨幹。"},
     ],
   })

# ---------------- best-ai-music-generators ----------------
do("best-ai-music-generators.json",
   [
     {"title": "Suno vs Udio vs ElevenLabs Music: the 2026 showdown", "url": "https://www.aimagicx.com/blog/suno-vs-udio-vs-elevenlabs-music-comparison-2026", "source": "AI Magicx"},
     {"title": "Best AI Music Generators in 2026: Suno vs Udio vs ElevenLabs", "url": "https://jam.com/resources/best-ai-music-generators-2026", "source": "Jam"},
   ],
   {
     "commentary": "In June 2026 Suno is still the one to beat, and I am keeping Suno v5 at number one without hesitation. Its ELO sits around 1,293, ahead of every competitor on audio fidelity, musical structure and vocal realism, and the business is just as dominant: roughly 2 million paid subscribers, 300 million in ARR and a 2.45 billion valuation as of February. When someone asks me to make a finished, full-length song with convincing vocals in one shot, this is the answer. ElevenLabs Music holds second and earns it on a point Suno cannot match: licensing. Eleven Music was built on licensed and royalty-free training data from the start, shipped commercial clearance through Merlin and Kobalt partnerships, and in April unified voice, music and sound effects under one iOS app. It is the first AI music tool I will tell a YouTuber to use without worrying about copyright strikes, and for monetized content that clean-rights story is worth real money. Udio stays third as the producer's scalpel: section-level inpainting lets you regenerate one part of a track without touching the rest, and combined with stem separation it is the closest thing to an AI DAW. Lyria 3 Pro, Stable Audio 2.5, Riffusion, Soundraw, AIVA, Mubert, Loudly and Boomy all carry forward unchanged. Nothing this week reshuffled the order, so I held ranks and let the licensing-versus-quality split frame the top three.",
     "highlights": [
       {"title": "Suno v5 is still the quality benchmark", "body": "Its ELO near 1,293 leads every rival on fidelity, structure and vocal realism, backed by 2 million paid subscribers and 300 million ARR. For a finished full-length song with convincing vocals in one pass, it stays number one."},
       {"title": "ElevenLabs Music wins on clean rights", "body": "Built on licensed and royalty-free data with Merlin and Kobalt clearance, it is the first AI music tool I recommend for monetized YouTube content without copyright-strike worry. That rights story earns it second."},
       {"title": "Udio is the producer's scalpel", "body": "Section-level inpainting regenerates one part of a track without disturbing the rest, and with stem separation it is the closest thing to an AI DAW. For hands-on producers who want surgical control, it holds third."},
       {"title": "The top three split by job", "body": "Suno for one-shot finished songs, ElevenLabs for monetization-safe rights, Udio for granular editing. The category has matured enough that you pick the tool by what you actually need to ship."},
     ],
   },
   {
     "commentary": "2026 年 6 月，Suno 還是那個要被超越的對象，我毫不猶豫把 Suno v5 放第一。它的 ELO 大約 1,293，音質、曲式結構、人聲擬真度都領先所有對手，生意也一樣猛，到 2 月大約有兩百萬付費訂戶、年經常性收入三億美金、估值 24.5 億美金。當有人叫我一次生出一首有說服力人聲的完整長曲，答案就是它。ElevenLabs Music 守第二，靠的是 Suno 比不上的一點，授權。Eleven Music 從一開始就用授權跟免版稅資料訓練，透過 Merlin 跟 Kobalt 的合作提供商用授權，4 月還把語音、音樂、音效整進同一個 iOS App。它是我會叫 YouTuber 放心用、不用怕版權檢舉的第一個 AI 音樂工具，對要營利的內容來說，這份乾淨的權利故事是真的能換成錢。Udio 守第三，是製作人的手術刀，段落級 inpainting 讓你只重生一段、不動其他，配上分軌，它是最接近 AI DAW 的東西。Lyria 3 Pro、Stable Audio 2.5、Riffusion、Soundraw、AIVA、Mubert、Loudly、Boomy 全部照舊。這週沒事件洗牌，所以我守住排名，讓「授權對品質」這條分界去定義前三名。",
     "highlights": [
       {"title": "Suno v5 仍是品質標竿", "body": "ELO 約 1,293，音質、結構、人聲擬真都領先所有對手，背後是兩百萬付費訂戶跟三億美金年收。要一次生出有說服力人聲的完整長曲，第一還是它。"},
       {"title": "ElevenLabs Music 贏在權利乾淨", "body": "用授權跟免版稅資料訓練，有 Merlin 跟 Kobalt 授權，是我會推薦給營利 YouTube 內容、不怕版權檢舉的第一個 AI 音樂工具。這份權利故事讓它穩坐第二。"},
       {"title": "Udio 是製作人的手術刀", "body": "段落級 inpainting 只重生一段不動其他，配上分軌，是最接近 AI DAW 的工具。想要外科級控制的動手派製作人，它守住第三。"},
       {"title": "前三名各司其職", "body": "Suno 一鍵成曲、ElevenLabs 營利免煩惱、Udio 精細編輯。這個類別已經成熟到，你照真正要交付的東西來選工具就對了。"},
     ],
   })

# ---------------- best-ai-video-generators ----------------
do("best-ai-video-generators.json",
   [
     {"title": "Best AI Video Generator in 2026: Runway, Veo, Seedance, Kling", "url": "https://pixflow.net/blog/best-ai-video-generator/", "source": "Pixflow"},
     {"title": "Best AI Video Generators June 2026, ranked by humans", "url": "https://llm-stats.com/leaderboards/best-ai-for-video-generation", "source": "LLM-Stats"},
   ],
   {
     "commentary": "June 2026 is the first month the AI video field feels settled at the top, and one piece of context frames everything: OpenAI's Sora is winding down, with the web and app experiences gone since April 26 and the API set to follow on September 24, so the conversation has fully moved on. I keep Google Veo 3.1 at number one because it is the safest complete pick: strong realism, good motion, native audio and 4K output in both landscape and portrait, with the best prompt adherence in the field. When I need one model to just work for a client, this is it. Runway Gen-4.5 holds second as the filmmaker's tool, the pro favorite when you need camera moves, motion brush and reference-driven character consistency rather than a one-prompt clip. Kling 3.0 stays third and is the value leader, currently topping the human-voted arena around 2,127 while costing a fraction of Veo, so for volume work it is the smart spend. Seedance 2.0 holds fourth as the narrative specialist, multi-shot native generation with synchronized audio in a single pass, which is genuinely hard to get anywhere else. Hailuo 02 keeps fifth as the budget value pick. Luma Ray3, Pika 2.2, Firefly Video, Hunyuan 1.5 and Wan 2.6 all carry forward unchanged. No new launch this week reshuffled the order, so I held ranks and let Sora's exit and the value gap shape the verdicts.",
     "highlights": [
       {"title": "Veo 3.1 is the safest complete pick", "body": "Strong realism, good motion, native audio and 4K in both orientations with the best prompt adherence on the board. When one model has to just work for a client, this is the one I reach for, so it stays number one."},
       {"title": "Runway Gen-4.5 is the filmmaker's tool", "body": "Camera moves, motion brush and reference-driven character consistency make it the pro favorite for real creative control. For shot-by-shot directing rather than one-prompt clips, it holds a clear second."},
       {"title": "Kling 3.0 is the value leader", "body": "It currently tops the human-voted arena around 2,127 while costing a fraction of Veo. For high-volume generation where budget matters, it is the smart spend and a deserved third."},
       {"title": "Sora's exit reshaped the field", "body": "OpenAI retired Sora's web and app on April 26 with the API ending September 24. With Sora gone, Veo, Runway, Kling and Seedance now define the top tier, which is exactly how this ranking reads."},
     ],
   },
   {
     "commentary": "2026 年 6 月是 AI 影片這塊頂端第一次感覺塵埃落定的月份，有個背景把全局都框住了，OpenAI 的 Sora 正在收攤，網頁跟 App 體驗從 4 月 26 日起就沒了，API 也排定 9 月 24 日跟進，所以話題已經完全往前走。我把 Google Veo 3.1 放第一，因為它是最安全的全能選擇，寫實夠強、動態好、原生音訊、橫幅直幅都能 4K，指令遵循也是全場最好。要一個模型給客戶交差就能用，就是它。Runway Gen-4.5 守第二，是電影人的工具，需要運鏡、motion brush、靠參考圖維持角色一致性時，它是專業圈的最愛，而不是只丟一個 prompt 出一段片。Kling 3.0 守第三，是性價比王，現在在真人投票競技場約 2,127 分居首，成本卻只有 Veo 的零頭，量大的活拿它最聰明。Seedance 2.0 守第四，是敘事專家，一次生成就能多鏡頭、音訊同步，這在別處真的很難拿到。Hailuo 02 守第五，是預算型選擇。Luma Ray3、Pika 2.2、Firefly Video、Hunyuan 1.5、Wan 2.6 全部照舊。這週沒有新發布洗牌，所以我守住排名，讓 Sora 退場跟性價比差距去帶判斷。",
     "highlights": [
       {"title": "Veo 3.1 是最安全的全能選擇", "body": "寫實強、動態好、原生音訊、橫直都能 4K，指令遵循全場最好。要一個模型給客戶交差就能用，我就拿它，所以第一是它。"},
       {"title": "Runway Gen-4.5 是電影人的工具", "body": "運鏡、motion brush、靠參考圖維持角色一致，讓它成為要真實創作掌控時的專業最愛。要一鏡一鏡導戲而非一鍵出片，它穩坐第二。"},
       {"title": "Kling 3.0 是性價比王", "body": "現在在真人投票競技場約 2,127 分居首，成本卻只有 Veo 的零頭。量大、預算掛帥的生成，拿它最聰明，第三實至名歸。"},
       {"title": "Sora 退場重塑了戰局", "body": "OpenAI 4 月 26 日關掉 Sora 網頁與 App，API 9 月 24 日結束。Sora 走了之後，Veo、Runway、Kling、Seedance 定義了頂端，這份榜單正是這樣讀。"},
     ],
   })

# ---------------- best-ai-voice-generators ----------------
do("best-ai-voice-generators.json",
   [
     {"title": "Eleven v3, the most expressive AI voice model", "url": "https://elevenlabs.io/v3", "source": "ElevenLabs"},
     {"title": "AI Chatbots and Speech Arena rankings", "url": "https://artificialanalysis.ai/agents/chatbots", "source": "Artificial Analysis"},
   ],
   {
     "commentary": "The voice-generation race in June 2026 is genuinely a two-horse photo finish at the top, and I have them tied at 9.4 for a reason. Inworld TTS-1.5 Max sits at number one because it currently tops the Artificial Analysis Speech Arena with an ELO around 1,236, winning blind tests for naturalness, emotional range and conversational flow, which is exactly what you want for real-time agents and interactive characters. ElevenLabs is right beside it and arguably still the more complete product: the Eleven v3 model launched in March handles emotional nuance, pacing and natural speech better than anything I have tested, now spans 70-plus languages, and the Text to Dialogue feature weaves multiple voices into one coherent scene with matched prosody. For voice cloning and creator tooling, ElevenLabs remains the king, so if your work is audiobooks, dubbing or branded voices, I still send you there first. Hume AI Octave 2 holds third for emotion-aware delivery, and Minimax Speech 02 HD and Cartesia Sonic 3 round out a strong upper tier on latency and quality. OpenAI GPT-4o mini TTS, Murf, WellSaid, Speechify, Resemble and Descript Overdub all carry forward unchanged. The honest read this month: Inworld edges the blind-test crown, ElevenLabs owns the ecosystem and cloning, and the right pick depends entirely on whether you are building agents or producing finished audio. No rank changes were warranted, so I held the board.",
     "highlights": [
       {"title": "Inworld TTS-1.5 Max takes the blind-test crown", "body": "It currently tops the Artificial Analysis Speech Arena around 1,236 ELO, winning on naturalness, emotional range and conversational flow. For real-time agents and interactive characters, that live-quality edge keeps it at number one."},
       {"title": "ElevenLabs owns cloning and the ecosystem", "body": "Eleven v3 from March handles emotion and pacing better than anything I have tested, spans 70-plus languages, and Text to Dialogue blends multiple voices seamlessly. For audiobooks, dubbing and branded voices it is still my first call."},
       {"title": "Hume Octave 2 leads on emotion", "body": "Its emotion-aware delivery makes it the pick when the read has to carry genuine feeling rather than just clarity. That specialization keeps it firmly in the upper tier at number three."},
       {"title": "The top two split by use case", "body": "Inworld edges live conversational quality, ElevenLabs owns finished-audio production and cloning. Pick by whether you are building an agent or producing a deliverable, and either choice is safe."},
     ],
   },
   {
     "commentary": "2026 年 6 月的語音生成，頂端真的是兩強衝線、難分軒輊，我把它們並列 9.4 是有道理的。Inworld TTS-1.5 Max 排第一，因為它現在在 Artificial Analysis 語音競技場以約 1,236 ELO 居首，盲測在自然度、情緒幅度、對話流暢度都拿下，這正是即時語音代理跟互動角色要的東西。ElevenLabs 緊貼在旁，平心而論還是更完整的產品，3 月推出的 Eleven v3 在情緒細節、節奏、自然語感上比我測過的任何東西都好，現在涵蓋 70 多種語言，Text to Dialogue 還能把多個聲音編進同一個場景、韻律對得上。論語音克隆跟創作者工具，ElevenLabs 依然是王，所以你的活如果是有聲書、配音、品牌語音，我還是第一個叫你去用它。Hume AI Octave 2 守第三，主打情緒感知的演繹，Minimax Speech 02 HD 跟 Cartesia Sonic 3 在延遲跟品質上撐起強勢的上半段。OpenAI GPT-4o mini TTS、Murf、WellSaid、Speechify、Resemble、Descript Overdub 全部照舊。這個月老實說，Inworld 小贏盲測王冠，ElevenLabs 握有生態跟克隆，怎麼選完全看你是在做代理還是在產出成品音檔。沒有需要動排名的理由，所以我守住整個榜。",
     "highlights": [
       {"title": "Inworld TTS-1.5 Max 拿下盲測王冠", "body": "它現在在 Artificial Analysis 語音競技場約 1,236 ELO 居首，自然度、情緒幅度、對話流暢都贏。即時代理跟互動角色要的就是這份現場品質，所以第一是它。"},
       {"title": "ElevenLabs 握有克隆與生態", "body": "3 月的 Eleven v3 情緒跟節奏比我測過的都好，涵蓋 70 多種語言，Text to Dialogue 能無縫混多個聲音。有聲書、配音、品牌語音，我還是第一個推它。"},
       {"title": "Hume Octave 2 情緒最強", "body": "情緒感知的演繹讓它在「念稿要帶真情緒而不只是清楚」時成為首選。這份專長讓它穩穩待在上半段、排第三。"},
       {"title": "前兩名依場景分工", "body": "Inworld 小贏現場對話品質，ElevenLabs 握有成品音檔製作跟克隆。看你是在做代理還是產交付物來選，兩個都安全。"},
     ],
   })

# ---------------- best-vpn-services ----------------
do("best-vpn-services.json",
   [
     {"title": "Mullvad vs Proton VPN: which VPN is best in 2026?", "url": "https://cyberinsider.com/vpn/comparison/mullvad-vs-proton-vpn/", "source": "CyberInsider"},
     {"title": "The 3 Best VPNs of 2026", "url": "https://www.rtings.com/vpn/reviews/best/vpn", "source": "RTINGS"},
   ],
   {
     "commentary": "Heading into June 2026 my VPN ranking still leads with privacy, and Mullvad stays at number one for the same reason it has held the spot all year: it is the strongest pure-privacy choice on the market. No email or personal info to sign up, a genuine no-logs policy, quantum-resistant tunnels, and RTINGS still rates it the best overall VPN tested on the balance of security, speed, reliability and value. The honest caveat I always give: Mullvad is consistently blocked by Netflix and most streaming services, so if streaming is your main goal, look elsewhere. That is exactly why ProtonVPN holds a close second. Recent head-to-head testing has Proton outpacing Mullvad on speed for streaming, torrenting and browsing on both local and remote servers, and it is the clear winner for Netflix and one of the best streaming VPNs going. If you want privacy you can trust plus actual streaming access, Proton is the pick. NordVPN stays third and earns it on raw speed: when throughput is the single thing you care about, it is still the fastest of this group. IVPN, ExpressVPN, Surfshark, Windscribe and Obscura VPN all carry forward unchanged. Nothing this week moved the order, so I held ranks and let the privacy-versus-streaming split frame the top three. Pick Mullvad for anonymity, Proton for the privacy-plus-streaming balance, Nord for pure speed.",
     "highlights": [
       {"title": "Mullvad is the privacy benchmark", "body": "No email to sign up, a real no-logs policy and quantum-resistant tunnels, and RTINGS still rates it the best overall on the balance of security, speed and value. For pure anonymity it stays number one."},
       {"title": "ProtonVPN wins on privacy plus streaming", "body": "Recent testing has it beating Mullvad on speed across streaming, torrenting and browsing, and it is the clear Netflix winner. If you need trustworthy privacy and real streaming access, Proton is the pick, a deserved second."},
       {"title": "NordVPN is the speed king", "body": "When raw throughput is the one thing that matters, it is still the fastest of this group. That keeps it a solid third for users who prioritize download speed over a no-email signup."},
       {"title": "Mullvad's streaming caveat is real", "body": "It is consistently blocked by Netflix and most streaming services, so if streaming is your main goal you should pick Proton instead. I keep the verdict honest so the ranking matches how you actually use a VPN."},
     ],
   },
   {
     "commentary": "2026 年 6 月，我的 VPN 排名還是以隱私掛帥，Mullvad 守第一的理由跟一整年一樣，它是市面上最純粹的隱私選擇。註冊不用 email、不用個資，真正的無紀錄政策，抗量子加密通道，RTINGS 綜合安全、速度、穩定、性價比評下來，還是把它列為測過最佳的整體 VPN。我每次都會誠實補一句但書，Mullvad 會被 Netflix 跟大多數串流服務穩定擋下來，所以如果你主要是要追劇，請看別的。這正是 ProtonVPN 緊咬第二的原因。最近的對決測試裡，Proton 在串流、torrent、一般瀏覽的速度，本地跟遠端伺服器都贏過 Mullvad，而且是 Netflix 的明確贏家、目前最好的串流 VPN 之一。如果你要的是可信任的隱私加上真的能追劇，選 Proton。NordVPN 守第三，靠的是純速度，當你唯一在意的就是吞吐量，它在這群裡還是最快的。IVPN、ExpressVPN、Surfshark、Windscribe、Obscura VPN 全部照舊。這週沒事件動排名，所以我守住，讓「隱私對串流」這條線去框前三名。要匿名選 Mullvad，要隱私加串流選 Proton，要純速度選 Nord。",
     "highlights": [
       {"title": "Mullvad 是隱私標竿", "body": "註冊不用 email、真無紀錄政策、抗量子通道，RTINGS 綜合安全、速度、性價比仍評它整體最佳。要純匿名，第一還是它。"},
       {"title": "ProtonVPN 贏在隱私加串流", "body": "最近測試裡它在串流、torrent、瀏覽的速度都贏過 Mullvad，是 Netflix 明確贏家。要可信隱私又真的能追劇，選 Proton，第二實至名歸。"},
       {"title": "NordVPN 是速度王", "body": "當你唯一在意的就是吞吐量，它在這群裡還是最快。這讓它穩坐第三，適合重下載速度勝過免 email 註冊的人。"},
       {"title": "Mullvad 的串流但書是真的", "body": "它會被 Netflix 跟多數串流穩定擋下，所以主要要追劇就該改選 Proton。我把判斷講白，讓排名對得上你實際怎麼用 VPN。"},
     ],
   })

print("ALL DONE")
