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
     {"title": "June 2026 Top Generative AI Chatbots & LLMs by Market Share", "url": "https://momenticmarketing.com/blog/top-ai-chatbots", "source": "Momentic"},
     {"title": "Best AI Chatbots 2026: I Tested ChatGPT, Claude, Gemini, Perplexity and Grok", "url": "https://ucstrategies.com/news/best-ai-chatbots-2026-i-tested-chatgpt-claude-gemini-perplexity-and-grok/", "source": "UC Strategies"},
   ],
   {
     "commentary": "I am keeping ChatGPT at number one this week, and the fresh market-share numbers make the call easy. The latest June tally puts ChatGPT at 54.7 percent of worldwide visits across the seven largest chatbots, with Gemini at 27.4 percent and Claude at 8.2 percent. That is the product people actually open, and for a consumer ranking reach is the whole point. GPT-5.5 still leads creative writing, so the default app stays the default for a reason. Claude holds second because it is the model I open for real work. Opus 4.8 is neck and neck with GPT-5.5 at the top of the coding charts, and for careful long-form reasoning it is the one I trust to stay coherent across a long session. Gemini stays third on the strength of Gemini 3.1 Pro, which leads on reasoning and data analysis, and Google's free tier keeps it in front of everyday users who never pay a cent. Grok earns its mid-pack spot as the value flagship: xAI's 4.3 release is the cheapest of the four with genuinely strong agentic and tool-use scores, so for high-volume automation it is the smart spend. Perplexity remains my pick when the answer needs live sources and citations. Worth noting from this week's data: Claude is the fastest-growing chatbot of the bunch, followed by DeepSeek and Gemini, so the gap behind the leader is closing. Copilot, DeepSeek, Meta AI, Le Chat and Qwen carry forward unchanged. My advice stays the same. Match the tool to the task and you win every time.",
     "highlights": [
       {"title": "ChatGPT keeps number one on sheer reach", "body": "Fresh June data puts it at 54.7 percent of worldwide chatbot visits, more than double Gemini and far ahead of Claude. GPT-5.5 still leads creative writing, and a consumer ranking should reward the app people actually open."},
       {"title": "Claude is the model I open for real work", "body": "Opus 4.8 sits neck and neck with GPT-5.5 atop the coding charts and stays coherent across long reasoning sessions. It is also the fastest-growing chatbot this month, which is why it holds a close second."},
       {"title": "Gemini owns reasoning and the free tier", "body": "Gemini 3.1 Pro leads on reasoning and data analysis, and Google's generous free access keeps it in front of everyday users. At 27.4 percent of visits it is the clear number two on traffic, holding third here on the all-round balance."},
       {"title": "Grok is the value flagship", "body": "Grok 4.3 is the cheapest of the four flagship models and posts strong agentic and tool-use scores. For high-volume automated workloads where token cost dominates, it is the smart pick and earns its mid-pack spot."},
     ],
   },
   {
     "commentary": "這週我還是把 ChatGPT 放第一，剛出爐的市佔數字讓這個決定很好下。6 月最新統計顯示，七大聊天機器人裡 ChatGPT 拿下全球流量 54.7 趴，Gemini 27.4 趴，Claude 8.2 趴。這就是大家真的會打開的產品，消費級榜單看的就是觸及面。GPT-5.5 創意寫作還是領先，預設 App 之所以是預設，是有道理的。Claude 守第二，因為它是我做正事會開的模型。Opus 4.8 在寫程式榜上跟 GPT-5.5 咬得死緊，需要細心處理長文推理時，我相信它整段對話都能維持一致。Gemini 守第三靠的是 Gemini 3.1 Pro，推理跟資料分析最強，加上 Google 免費額度大方，一般人連一塊錢都不用付就能用，這點很實在。Grok 站穩中段，是性價比旗艦，xAI 4.3 是四大裡最便宜的，工具呼叫跟代理分數又紮實，量大的自動化拿它最划算。Perplexity 在我要附即時來源、要引用時還是首選。這週數據有個重點，Claude 是這群裡成長最快的，再來是 DeepSeek 跟 Gemini，所以跟龍頭的差距正在縮。Copilot、DeepSeek、Meta AI、Le Chat、Qwen 照舊。我的建議一樣，把工具對準任務，每次你都會贏。",
     "highlights": [
       {"title": "ChatGPT 靠純觸及面守住第一", "body": "6 月最新數據顯示它拿下全球聊天機器人流量 54.7 趴，是 Gemini 的兩倍多，遠超 Claude。GPT-5.5 創意寫作還是領先，消費級榜單該獎勵的就是大家真的會打開的 App。"},
       {"title": "Claude 是我做正事會開的模型", "body": "Opus 4.8 在寫程式榜上跟 GPT-5.5 咬得死緊，長推理整段都能維持一致。它也是這個月成長最快的聊天機器人，所以緊咬第二。"},
       {"title": "Gemini 推理跟免費額度都強", "body": "Gemini 3.1 Pro 推理跟資料分析最強，Google 免費額度又大方，讓它在從不付費的日常使用者面前站得很前面。流量 27.4 趴是明確第二，這裡靠全面均衡守第三。"},
       {"title": "Grok 是高性價比旗艦", "body": "Grok 4.3 是四大旗艦裡最便宜的，工具呼叫跟代理分數都不錯。量大、成本掛帥的自動化工作流拿它最聰明，中段位置站得很穩。"},
     ],
   })

# ---------------- best-ai-coding-assistants ----------------
do("best-ai-coding-assistants.json",
   [
     {"title": "7 Best AI Coding Agents in June 2026 (15+ Reviewed)", "url": "https://usefulai.com/tools/ai-coding", "source": "Useful AI"},
     {"title": "Best AI Coding Agents for 2026: Real-World Developer Reviews", "url": "https://www.faros.ai/blog/best-ai-coding-agents-2026", "source": "Faros AI"},
   ],
   {
     "commentary": "Claude Code stays at number one, and this week's developer reviews back the call hard. It is the agent teams reach for when the job is complex: a multi-file refactor, a debugging session that needs reading tests and adjusting, a delegated task that recovers from its own mistakes. The adoption curve tells the story too, climbing from 4 percent to 63 percent developer adoption in nine months, which makes it the fastest-growing coding agent of the year. Describe an outcome, walk away, come back to a coherent change. Cursor holds second as the best AI-integrated IDE on the market. If you want AI woven into every keystroke with visual diffs and fast autocomplete, this is the one, and most shops I talk to run both: Cursor for line-level edits, Claude Code for delegation. OpenAI Codex stays third on the strength of GPT-5.5 for long-running agentic work across large codebases, multi-file refactors and validation loops. GitHub Copilot holds fourth and remains the adoption leader and the most broadly compatible option across editors and languages, which is exactly why it stays solidly in the top tier. Google Jules sits fifth on its Antigravity multi-agent relaunch. Devin, Amazon Q, Zed, Aider, Windsurf and Augment all carry forward. The honest read this month is that there is no single best agent in isolation. You pick by where you want leverage, speed inside the editor, control on large codebases, or autonomy up the stack, so I held ranks and let the verdicts do the talking.",
     "highlights": [
       {"title": "Claude Code owns complex, goal-level work", "body": "It is the agent teams trust with multi-file refactors and debugging sessions that recover from their own mistakes. Adoption jumped from 4 to 63 percent in nine months, the fastest-growing coding agent of the year, which keeps it at number one."},
       {"title": "Cursor is the best AI-integrated IDE", "body": "For AI woven into every keystroke with visual diffs and fast autocomplete, nothing else comes close. It is the line-level companion most teams pair with Claude Code, holding a clear second."},
       {"title": "Copilot stays the most universal pick", "body": "It leads the field in raw adoption and remains the most broadly compatible assistant across editors and languages. That reach keeps it solidly in the top four even as rivals push harder on autonomy."},
       {"title": "Codex is OpenAI's agentic workhorse", "body": "GPT-5.5 powers long-running agentic work across large codebases, multi-file refactors, tool use and validation loops. That capability holds it firmly at number three this month."},
     ],
   },
   {
     "commentary": "Claude Code 還是第一，這週的開發者評測把這個判斷撐得很穩。它是團隊碰到複雜活就會找的代理，跨檔案重構、要讀測試再調整的除錯、會從自己錯誤裡爬回來的委派任務，全靠它。採用曲線也說明一切，九個月內開發者採用率從 4 趴衝到 63 趴，是今年成長最快的寫程式代理。你描述一個結果，人走開，回來就是一份前後一致的修改。Cursor 守第二，是市面上 AI 整合最好的 IDE。要 AI 融進每一個按鍵、要視覺化 diff 跟快速補全，就是它，我聊過的多數團隊兩個一起用，Cursor 做行級編輯、Claude Code 做委派。OpenAI Codex 守第三，靠 GPT-5.5 處理大型程式庫的長時間代理工作、跨檔案重構跟驗證迴圈。GitHub Copilot 守第四，依然是採用率龍頭，也是跨編輯器、跨語言相容性最好的選擇，這正是它穩穩待在前段的原因。Google Jules 排第五，靠 Antigravity 多代理重啟。Devin、Amazon Q、Zed、Aider、Windsurf、Augment 全部照舊。這個月老實講，沒有單一最強的代理，你照想要施力的地方選，編輯器內的速度、大型程式庫的掌控、還是更上層的自主性，所以我守住排名，讓判斷本身說話。",
     "highlights": [
       {"title": "Claude Code 主宰複雜的目標級工作", "body": "它是團隊敢把跨檔案重構、會自己爬回來的除錯交出去的代理。九個月採用率從 4 趴跳到 63 趴，是今年成長最快的寫程式代理，所以守第一。"},
       {"title": "Cursor 是最強的 AI 整合 IDE", "body": "要 AI 融進每個按鍵、視覺化 diff 加快速補全，沒人能比。它是多數團隊拿來搭配 Claude Code 的行級夥伴，穩坐第二。"},
       {"title": "Copilot 仍是最通用的選擇", "body": "它在純採用率上領先全場，也是跨編輯器、跨語言相容性最好的助手。這份廣度讓它穩穩待在前四，即使對手在自主性上加碼。"},
       {"title": "Codex 是 OpenAI 的代理主力", "body": "GPT-5.5 撐起大型程式庫的長時間代理工作、跨檔案重構、工具呼叫跟驗證迴圈。這份能力讓它這個月穩在第三。"},
     ],
   })

# ---------------- best-ai-image-generators ----------------
do("best-ai-image-generators.json",
   [
     {"title": "Best AI Image Generators June 2026 — Midjourney, Flux, DALL-E Compared", "url": "https://aiflashreport.com/ai-image-generators.html", "source": "AI Flash Report"},
     {"title": "Best AI Image Generators in 2026 — Ranked by Blind Human Votes", "url": "https://llm-stats.com/leaderboards/best-ai-for-image-generation", "source": "LLM-Stats"},
   ],
   {
     "commentary": "The image field in June 2026 is fully specialized, and my ranking maps that rather than pretending one model wins everything. Midjourney V8 stays at number one because aesthetic quality is where it remains untouchable, and the V8 Alpha renders roughly 5x faster with native 2K output, so the old speed knock keeps shrinking. When the brief is art, this is the answer. Flux 2 Pro holds second as the photorealism default: for product photography or a portrait that has to pass as a real photo, this is what I open first, and it still posts the highest technical quality with fast generation for commercial work. The live tension sits at number three, where GPT Image 2 currently tops the blind-vote arena around 509, well ahead of the pack on prompt-following and complex instructions. I keep it third because arena ELO rewards versatility more than the artistic ceiling that still separates Midjourney, but it is the most well-rounded single tool here and a defensible top pick for anyone who values reliability over style. Ideogram V3 stays fourth on text rendering nobody else reliably matches, the go-to for posters, packaging and any image with headline copy baked in. Imagen 4, Firefly 4, SD 3.5 Large, Recraft, Krea and Leonardo all carry forward unchanged because nothing this week moved them. My advice this month is simple. Pick by job. Midjourney for art, Flux for realism, GPT Image 2 for all-purpose reliability, Ideogram for text. That is the whole map.",
     "highlights": [
       {"title": "Midjourney V8 still owns aesthetics", "body": "Artistic image quality is where it remains untouchable, and the V8 Alpha renders about 5x faster with native 2K output. The old speed complaint keeps fading, which holds it at number one for anyone who cares how an image looks."},
       {"title": "Flux 2 Pro is the photorealism default", "body": "For product photography or a portrait that must pass as a real photo, this is the one I open first, with the highest technical quality and fast generation. That realism focus keeps it a clear second for commercial work."},
       {"title": "GPT Image 2 is the all-rounder", "body": "It currently tops the blind-vote arena around 509, well ahead of the field on prompt-following and complex instructions. It is the most reliable single tool here and a defensible top pick for anyone valuing consistency over artistic ceiling."},
       {"title": "Ideogram V3 wins on text", "body": "It renders headline copy, logos and packaging mockups with an accuracy nobody else reliably matches. For any image that needs readable text baked in, it stays the specialist worth keeping in the kit at number four."},
     ],
   },
   {
     "commentary": "2026 年 6 月的 AI 生圖已經徹底分眾，我的排名就照這個現實走，不假裝有哪個模型全包。Midjourney V8 我還是放第一，因為美感品質它依舊無敵，V8 Alpha 算圖快了大約 5 倍、原生 2K 輸出，過去被嫌的速度問題持續縮小。案子是藝術，答案就是它。Flux 2 Pro 守第二，是寫實的預設選擇，商品攝影或要能當真人照片用的人像，我第一個開它，技術品質還是最高、生成又快，商用很對味。比較有張力的是第三名，GPT Image 2 現在在盲測競技場以約 509 分領先一大截，指令遵循跟複雜指示都最強。我把它擺第三，是因為競技場 ELO 獎勵的是全能性，而 Midjourney 拉開差距靠的是藝術天花板，但平心而論 GPT Image 2 是榜上最全能的單一工具，重視穩定勝過風格的人放第一也說得通。Ideogram V3 守第四，靠的是沒人能穩定追上的文字渲染，海報、包裝、任何要嵌標題文字的圖都找它。Imagen 4、Firefly 4、SD 3.5 Large、Recraft、Krea、Leonardo 這週沒事件，全部照舊。這個月我的建議很簡單，看任務選工具，藝術找 Midjourney、寫實找 Flux、全能穩定找 GPT Image 2、文字找 Ideogram，整張地圖就這樣。",
     "highlights": [
       {"title": "Midjourney V8 美感依舊無敵", "body": "藝術圖質它還是沒人能碰，V8 Alpha 算圖快約 5 倍、原生 2K 輸出。過去被嫌的速度問題持續消失，對在意成品好不好看的人，第一名穩穩的。"},
       {"title": "Flux 2 Pro 是寫實預設", "body": "商品攝影、或要能當真人照片用的人像，我第一個開它，技術品質最高、生成又快。這份寫實專注讓它在不能露出 AI 痕跡的商用場景穩坐第二。"},
       {"title": "GPT Image 2 是全能王", "body": "它現在在盲測競技場約 509 分，指令遵循跟複雜指示領先一截。是榜上最穩的單一工具，重視一致性勝過藝術天花板的人，放第一也合理。"},
       {"title": "Ideogram V3 贏在文字", "body": "標題文字、Logo、包裝模擬，它渲染的準確度沒人能穩定追上。任何要嵌入可讀文字的圖，它都是值得留在工具箱裡的專家，守第四。"},
     ],
   })

# ---------------- best-ai-meeting-assistants ----------------
do("best-ai-meeting-assistants.json",
   [
     {"title": "The 10 best AI meeting assistants in 2026", "url": "https://zapier.com/blog/best-ai-meeting-assistant/", "source": "Zapier"},
     {"title": "9 Best AI Meeting Assistants 2026 (Bot-Free Options Tested)", "url": "https://www.craftnoteapp.com/blog/best-ai-meeting-assistants-2026", "source": "Craft Note"},
   ],
   {
     "commentary": "The meeting-assistant category splits cleanly on one question heading into June 2026: do you want a bot in the call or not, and I keep Granola at number one because it answers that best. It captures audio straight from your desktop output with no visible bot in the participant list, so there is no 'Granola is joining' notification, which matters more than ever now that clients and legal teams flag recording bots. The quiet model lets you take notes while AI fills in details from the transcript, and that workflow is what broke the category open. Fathom holds second and is genuinely the strongest all-rounder on the board: unlimited free Zoom recording with no minute cap, 30-second post-call summaries, 95 percent transcription accuracy, native HubSpot and Salesforce integrations, and the highest G2 rating in the category at 5.0 from over 6,000 reviews. For an individual or small team that does not want to pay, I send you to Fathom first. Fireflies stays third as the searchable team archive with the deepest CRM integration spread, and its new Talk to Fireflies feature, powered by Perplexity, now answers web-search questions inside a meeting. Otter holds fourth and remains the king of searchable archives with strong raw transcription. Fellow, tl;dv, Read.ai, Krisp, Zoom AI Companion, Avoma, Circleback, Microsoft 365 Copilot and Gong all carry forward unchanged. No launch this week justified a reshuffle, so I held ranks and let the bot-versus-no-bot framing guide the verdicts.",
     "highlights": [
       {"title": "Granola wins by skipping the bot", "body": "It records straight from your desktop audio with no visible bot and no join notification, exactly what clients and legal teams increasingly demand. The quiet note-taking model broke the category open, keeping it at number one."},
       {"title": "Fathom is the strongest all-rounder", "body": "Unlimited free Zoom recording, 30-second summaries, 95 percent accuracy, native HubSpot and Salesforce, and a 5.0 G2 rating from over 6,000 reviews. For an individual or small team that refuses to pay, this is the first tool I recommend."},
       {"title": "Fireflies owns the searchable CRM archive", "body": "Its deep integration spread and the new Perplexity-powered Talk to Fireflies feature, which answers web questions mid-meeting, keep it third. For teams treating notes as a knowledge base, it remains the natural backbone."},
       {"title": "Otter is still the searchable-archive king", "body": "It posts strong raw transcription and remains the go-to for a verbatim, searchable record. When the deliverable is the transcript itself, Otter stays the specialist pick at number four."},
     ],
   },
   {
     "commentary": "2026 年 6 月，會議助理這個類別其實乾淨地分成一個問題，你到底要不要在會議裡放一隻 bot，我把 Granola 放第一就是因為它把這題答得最好。它直接從你桌面的音訊輸出抓聲音，與會者名單上不會出現一隻看得見的機器人，也不會跳出「Granola 正在加入」的通知，這點現在比以前更重要，因為不少客戶跟法務團隊看到錄音 bot 就皺眉。安靜的模式讓你一邊做筆記、AI 一邊從逐字稿補細節，這套工作流正是把這個類別打開的關鍵。Fathom 守第二，平心而論是榜上最強的全能選手，Zoom 免費無限錄製、沒有分鐘上限，會後 30 秒出摘要，逐字稿準確度 95 趴，原生整合 HubSpot 跟 Salesforce，G2 評分還是全類別最高的 5.0、超過六千則評論。如果你是個人或不想付錢的小團隊，我第一個叫你去用 Fathom。Fireflies 守第三，是可搜尋的團隊知識庫，CRM 整合鋪得最廣，新的 Talk to Fireflies 由 Perplexity 撐腰，現在能在會議裡直接回答網路搜尋問題。Otter 守第四，依然是可搜尋檔案之王，純逐字稿很強。Fellow、tl;dv、Read.ai、Krisp、Zoom AI Companion、Avoma、Circleback、Microsoft 365 Copilot、Gong 全部照舊。這週沒有哪個新發布值得洗牌，所以我守住排名，讓「要不要 bot」這個框架去帶判斷。",
     "highlights": [
       {"title": "Granola 靠不放 bot 取勝", "body": "它直接從桌面音訊錄，會議裡看不到機器人、也不跳加入通知，這正是客戶跟法務越來越要求的。安靜做筆記的模式把這個類別打開，所以第一名是它。"},
       {"title": "Fathom 是最強全能選手", "body": "Zoom 免費無限錄製、30 秒出摘要、準確度 95 趴、原生整合 HubSpot 跟 Salesforce、G2 評分 5.0 超過六千則評論。個人或死不付錢的小團隊，我第一個推這個。"},
       {"title": "Fireflies 主打可搜尋 CRM 知識庫", "body": "整合鋪得最廣，新的 Talk to Fireflies 由 Perplexity 撐腰，能在會議裡直接回答網路問題，守住第三。把會議記錄當知識庫的團隊，它仍是天然骨幹。"},
       {"title": "Otter 仍是可搜尋檔案之王", "body": "純逐字稿很強，依然是要一份精準、可搜尋紀錄時的首選。當交付物就是逐字稿本身，Otter 還是那個專家選擇，守第四。"},
     ],
   })

# ---------------- best-ai-music-generators ----------------
do("best-ai-music-generators.json",
   [
     {"title": "Suno vs Udio vs ElevenLabs Music: The 2026 AI Music Generator Showdown", "url": "https://www.aimagicx.com/blog/suno-vs-udio-vs-elevenlabs-music-comparison-2026", "source": "AI Magicx"},
     {"title": "Best AI Music Generators in 2026: Suno vs Udio vs ElevenLabs (Tested)", "url": "https://undetectr.com/blog/best-ai-music-generators-2026", "source": "Undetectr"},
   ],
   {
     "commentary": "In June 2026 Suno is still the one to beat, and I am keeping Suno V5 at number one without hesitation. Its ELO sits around 1,293, ahead of every competitor on audio fidelity, musical structure and vocal realism, with studio-quality output, stem editing and a full audio workstation no other tool matches. The business backs it up: a 2.45 billion valuation, 300 million in ARR and roughly 2 million paid subscribers as of February. When someone asks me to make a finished, full-length song with convincing vocals in one shot, this is the answer. ElevenLabs Music holds second and earns it on the point Suno cannot match: licensing. Eleven Music was built on a clean rights story, and the April launch of the dedicated ElevenMusic app added a Music Marketplace where creators can monetize tracks, plus the platform leads on vocal realism and natural expression. It is the first AI music tool I tell a YouTuber to use without copyright-strike worry, and for monetized content that clean-rights story is worth real money. Udio stays third as the producer's scalpel: section-level inpainting regenerates one part of a track without touching the rest, its 48kHz output has the highest sample rate on the board, and the UMG settlement plus the jointly licensed UMG x Udio platform coming this year strengthen its rights position. Lyria 3 Pro, Stable Audio 2.5, Riffusion, Soundraw, AIVA, Mubert, Loudly and Boomy all carry forward unchanged. Nothing this week reshuffled the order, so I held ranks and let the licensing-versus-quality split frame the top three.",
     "highlights": [
       {"title": "Suno V5 is still the quality benchmark", "body": "Its ELO near 1,293 leads every rival on fidelity, structure and vocal realism, with a full audio workstation no tool matches, backed by 2 million paid subscribers and 300 million ARR. For a finished full-length song in one pass, it stays number one."},
       {"title": "ElevenLabs Music wins on clean rights", "body": "Built on a clean licensing story with the April ElevenMusic app and a creator Marketplace, it leads on vocal realism. It is the first AI music tool I recommend for monetized YouTube content without strike worry, which earns it second."},
       {"title": "Udio is the producer's scalpel", "body": "Section-level inpainting regenerates one part of a track without disturbing the rest, its 48kHz output tops the board on sample rate, and the UMG settlement firms up its rights story. For hands-on producers wanting surgical control, it holds third."},
       {"title": "The top three split by job", "body": "Suno for one-shot finished songs, ElevenLabs for monetization-safe rights, Udio for granular editing and the highest audio fidelity. The category has matured enough that you pick the tool by what you actually need to ship."},
     ],
   },
   {
     "commentary": "2026 年 6 月，Suno 還是那個要被超越的對象，我毫不猶豫把 Suno V5 放第一。它的 ELO 大約 1,293，音質、曲式結構、人聲擬真度都領先所有對手，錄音室級輸出、分軌編輯、加上沒人比得上的完整音訊工作站。生意也撐得住，到 2 月大約有兩百萬付費訂戶、年經常性收入三億美金、估值 24.5 億美金。當有人叫我一次生出一首有說服力人聲的完整長曲，答案就是它。ElevenLabs Music 守第二，靠的是 Suno 比不上的一點，授權。Eleven Music 從一開始就有乾淨的權利故事，4 月推出的 ElevenMusic 專屬 App 還加了 Music Marketplace，讓創作者把曲子變現，平台在人聲擬真跟自然表現上又領先。它是我會叫 YouTuber 放心用、不怕版權檢舉的第一個 AI 音樂工具，對要營利的內容來說，這份乾淨權利是真的能換成錢。Udio 守第三，是製作人的手術刀，段落級 inpainting 讓你只重生一段、不動其他，48kHz 輸出是榜上最高取樣率，加上跟 UMG 和解、今年要上的 UMG x Udio 聯名授權平台，權利地位更穩。Lyria 3 Pro、Stable Audio 2.5、Riffusion、Soundraw、AIVA、Mubert、Loudly、Boomy 全部照舊。這週沒事件洗牌，所以我守住排名，讓「授權對品質」這條分界去定義前三名。",
     "highlights": [
       {"title": "Suno V5 仍是品質標竿", "body": "ELO 約 1,293，音質、結構、人聲擬真都領先所有對手，還有沒人比得上的完整音訊工作站，背後是兩百萬付費訂戶跟三億美金年收。要一次生出完整長曲，第一還是它。"},
       {"title": "ElevenLabs Music 贏在權利乾淨", "body": "從一開始就有乾淨授權故事，4 月的 ElevenMusic App 加上創作者 Marketplace，人聲擬真又領先。是我會推薦給營利 YouTube 內容、不怕檢舉的第一個 AI 音樂工具，穩坐第二。"},
       {"title": "Udio 是製作人的手術刀", "body": "段落級 inpainting 只重生一段不動其他，48kHz 輸出是榜上最高取樣率，跟 UMG 和解讓權利故事更穩。想要外科級控制的動手派製作人，它守住第三。"},
       {"title": "前三名各司其職", "body": "Suno 一鍵成曲、ElevenLabs 營利免煩惱、Udio 精細編輯加最高音質。這個類別已經成熟到，你照真正要交付的東西來選工具就對了。"},
     ],
   })

print("ALL DONE")
