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
     {"title": "Top Generative AI Chatbots by Market Share – June 2026", "url": "https://firstpagesage.com/reports/top-generative-ai-chatbots/", "source": "First Page Sage"},
     {"title": "June 2026 Top Generative AI Chatbots & LLMs by Market Share", "url": "https://momenticmarketing.com/blog/top-ai-chatbots", "source": "Momentic"},
   ],
   {
     "commentary": "ChatGPT stays at number one, and the freshest June numbers make the call effortless. It holds 54.7 percent of worldwide visits across the seven largest chatbots, more than double Gemini, and it is the app people actually open when they want an answer. For a consumer ranking, reach is the whole game. I keep Claude in a tight second because it is the model I open for real work. Anthropic now wins roughly 70 percent of head-to-head enterprise deals against OpenAI, and Claude posts the best engagement-to-traffic ratio in the field with the lowest bounce rate and the most pages per visit, so the people who land on it stay and go deep. Gemini holds third and is the story of the year on momentum, climbing from about 5.6 percent of visits in early 2025 to 27.4 percent now, up roughly 104 percent in six months on the strength of Google's free tier and Gemini 3.1 Pro's reasoning. Perplexity stays fourth as my pick when an answer needs live sources and citations. Grok sits fifth as the value play, cheap and strong on agentic work. The honest read this week: ChatGPT and Gemini together own about 82 percent of measured traffic, and the other five split the rest, so the gap between the top two and everyone else is what actually matters. Match the tool to the task and you win every time.",
     "highlights": [
       {"title": "ChatGPT keeps number one on sheer reach", "body": "June data puts it at 54.7 percent of worldwide chatbot visits, more than double Gemini. A consumer ranking should reward the app people actually open, and this is still the default answer for the largest audience by a wide margin."},
       {"title": "Claude is the model I trust for real work", "body": "Anthropic now wins about 70 percent of head-to-head enterprise deals against OpenAI, and Claude shows the lowest bounce rate and highest pages-per-visit of the consumer leaders. The people who open it stay and go deep, which holds it at a close second."},
       {"title": "Gemini is the momentum story of the year", "body": "It climbed from roughly 5.6 percent of visits in early 2025 to 27.4 percent now, up about 104 percent in six months. Google's free tier plus Gemini 3.1 Pro's reasoning keeps it the fastest-scaling assistant and a clear third."},
       {"title": "Grok is the value flagship", "body": "It is the cheapest of the strong models with genuinely capable agentic and tool-use scores. For high-volume automation where token cost dominates the bill, it is the smart spend and earns its mid-pack spot."},
     ],
   },
   {
     "commentary": "ChatGPT 我還是放第一，6 月最新數字讓這個決定毫無懸念。它在七大聊天機器人裡拿下全球流量 54.7 趴，是 Gemini 的兩倍多，想找答案時大家真的會打開的就是它。消費級榜單看的就是觸及面，這點它贏太多。Claude 我緊咬第二，因為它是我做正事會開的模型。Anthropic 現在在企業正面對決裡大約七成的案子贏過 OpenAI，而且 Claude 的互動品質是這群裡最好的，跳出率最低、每次造訪看的頁數最多，會點進去的人都是真的要深入用。Gemini 守第三，是今年成長最猛的故事，從 2025 年初約 5.6 趴的流量衝到現在 27.4 趴，半年漲了大約 104 趴，靠的是 Google 大方的免費額度跟 Gemini 3.1 Pro 的推理。Perplexity 守第四，要附即時來源、要引用時我首選它。Grok 排第五，是性價比牌，便宜又擅長代理工作。這週老實講，ChatGPT 跟 Gemini 加起來就佔了大約 82 趴的流量，剩下五家分剩下的，前兩名跟其他人的差距才是重點。把工具對準任務，每次你都會贏。",
     "highlights": [
       {"title": "ChatGPT 靠純觸及面守第一", "body": "6 月數據顯示它拿下全球聊天機器人流量 54.7 趴，是 Gemini 的兩倍多。消費級榜單該獎勵的就是大家真的會打開的 App，對最大的使用者群來說，它還是差距很大的預設答案。"},
       {"title": "Claude 是我做正事敢信的模型", "body": "Anthropic 現在企業正面對決大約七成案子贏過 OpenAI，Claude 的跳出率是消費級龍頭裡最低、每次造訪頁數最多。會打開它的人都是真的要深入用，所以緊咬第二。"},
       {"title": "Gemini 是今年成長最猛的故事", "body": "從 2025 年初約 5.6 趴的流量衝到現在 27.4 趴，半年漲約 104 趴。Google 免費額度加上 Gemini 3.1 Pro 的推理，讓它成長最快，穩坐第三。"},
       {"title": "Grok 是高性價比旗艦", "body": "它是強模型裡最便宜的，代理跟工具呼叫分數又紮實。量大、成本掛帥的自動化工作流拿它最聰明，中段位置站得很穩。"},
     ],
   })

# ---------------- best-ai-coding-assistants ----------------
do("best-ai-coding-assistants.json",
   [
     {"title": "Best AI Coding Assistants 2026: Cursor vs Copilot vs Claude Code", "url": "https://scrimba.com/articles/best-ai-coding-assistants-2026/", "source": "Scrimba"},
     {"title": "Claude Code vs GitHub Copilot vs Cursor (2026): Honest Comparison", "url": "https://www.cosmicjs.com/blog/claude-code-vs-github-copilot-vs-cursor-which-ai-coding-agent-should-you-use-2026", "source": "Cosmic"},
   ],
   {
     "commentary": "Claude Code stays at number one, and this week's reviews keep landing on the same verdict: it has the strongest reasoning for complex tasks. Claude Code with Opus leads SWE-bench Pro at 64.3 percent, well ahead of GPT-5.4 and Gemini 3.1 Pro, and it is the agent teams reach for when the job is a multi-file refactor or a debugging session that has to read tests and adjust. It is terminal-first, the IDE integrations exist, but the magic is delegation: describe an outcome, walk away, come back to a coherent change. Cursor holds second as the developer favorite for agility, a full VS Code fork where the AI is first-class rather than bolted on, and Composer proposing multi-file edits in a single pass is still the best in-editor experience money buys. Codex stays third as OpenAI's agentic workhorse for long-running work across large codebases. Copilot holds fourth and earns it on reach alone, it runs in VS Code, Visual Studio, JetBrains, Neovim, Xcode, Eclipse, Zed and more, so for a team spread across editors nothing else competes, even with the June 1 move to usage-based AI Credits. The pattern every honest reviewer lands on this month is the same one I run: an IDE assistant for daily coding plus a terminal agent for multi-file work. You do not pick one, you pick where each gives you leverage.",
     "highlights": [
       {"title": "Claude Code owns complex, goal-level work", "body": "It leads SWE-bench Pro at 64.3 percent with Opus, ahead of GPT-5.4 and Gemini 3.1 Pro, and is the agent teams trust with multi-file refactors that recover from their own mistakes. That reasoning edge keeps it at number one."},
       {"title": "Cursor is the developer favorite for agility", "body": "A full VS Code fork with AI built in as a first-class citizen, and Composer's single-pass multi-file edits remain the best in-editor experience available. It is the line-level companion most teams pair with Claude Code, holding a clear second."},
       {"title": "Copilot wins on universal reach", "body": "It runs in VS Code, Visual Studio, JetBrains, Neovim, Xcode, Eclipse, Zed and more, so for a team spread across editors nothing matches it. That breadth keeps it solidly in the top four even after the move to usage-based AI Credits."},
       {"title": "The winning setup is two tools, not one", "body": "Every honest 2026 review lands here: an IDE assistant for daily coding plus a terminal agent for multi-file delegation. You pick by where each gives you leverage, which is exactly why I held ranks this week."},
     ],
   },
   {
     "commentary": "Claude Code 還是第一，這週的評測一再落在同一個判斷上：處理複雜任務它的推理最強。Claude Code 搭 Opus 在 SWE-bench Pro 拿 64.3 趴，明顯領先 GPT-5.4 跟 Gemini 3.1 Pro，碰到跨檔案重構、要讀測試再調整的除錯，團隊就是找它。它是終端機優先，IDE 整合也有，但真正的魔法是委派：你描述一個結果，人走開，回來就是一份前後一致的修改。Cursor 守第二，是開發者最愛的靈活派，完整 fork VS Code，AI 是原生一等公民不是外掛，Composer 一次提出跨檔案編輯依然是花錢買得到的最佳編輯器內體驗。Codex 守第三，是 OpenAI 的代理主力，處理大型程式庫的長時間工作。Copilot 守第四，光靠觸及面就夠格，它能跑在 VS Code、Visual Studio、JetBrains、Neovim、Xcode、Eclipse、Zed 等等，團隊散在不同編輯器時沒人能比，即使 6 月 1 號改成用量計費的 AI Credits 也一樣。這個月每個老實的評測都落在我自己在跑的組合：日常寫程式用 IDE 助手，跨檔案工作用終端機代理。你不是二選一，你是看哪個給你施力點。",
     "highlights": [
       {"title": "Claude Code 主宰複雜的目標級工作", "body": "它搭 Opus 在 SWE-bench Pro 拿 64.3 趴，領先 GPT-5.4 跟 Gemini 3.1 Pro，是團隊敢把會自己爬回來的跨檔案重構交出去的代理。這份推理優勢讓它守第一。"},
       {"title": "Cursor 是開發者最愛的靈活派", "body": "完整 fork VS Code，AI 是原生一等公民，Composer 一次提出跨檔案編輯依然是買得到的最佳編輯器內體驗。它是多數團隊拿來搭配 Claude Code 的行級夥伴，穩坐第二。"},
       {"title": "Copilot 贏在通用觸及面", "body": "它能跑在 VS Code、Visual Studio、JetBrains、Neovim、Xcode、Eclipse、Zed 等等，團隊散在不同編輯器時沒人能比。這份廣度讓它穩穩待在前四，即使改成用量計費也一樣。"},
       {"title": "贏家組合是兩個工具不是一個", "body": "2026 年每個老實的評測都落在這：日常寫程式用 IDE 助手，跨檔案委派用終端機代理。你照各自的施力點選，這正是我這週守住排名的原因。"},
     ],
   })

# ---------------- best-ai-image-generators ----------------
do("best-ai-image-generators.json",
   [
     {"title": "Best AI Image Generators June 2026 — Midjourney, Flux, DALL-E Compared", "url": "https://aiflashreport.com/ai-image-generators.html", "source": "AI Flash Report"},
     {"title": "The 9 Best AI Image Generation Models in 2026", "url": "https://www.gradually.ai/en/ai-image-models/", "source": "Gradually"},
   ],
   {
     "commentary": "The image field in June 2026 is fully specialized, and my ranking maps that rather than pretending one model wins everything. Midjourney V8 stays at number one because aesthetic quality is where it stays untouchable, and the V8 Alpha renders roughly 5x faster with native 2K output, so the old speed knock keeps shrinking. When the brief is art, this is the answer. Flux 2 Pro holds second as the photorealism default: it posts the highest technical quality with a 4.5-second generation time, and for product shots or a portrait that has to pass as a real photo it is what I open first. GPT Image 2 stays third as the all-rounder, the most reliable single tool here on prompt-following and complex instructions, the safe pick for anyone who values consistency over an artistic ceiling. Ideogram V3 holds fourth on text rendering that still feels like a magic trick, the specialist for posters, packaging and any image with headline copy baked in. Imagen 4, Firefly 4, SD 3.5 Large and the rest carry forward unchanged because nothing this week moved them. The most common pro workflow is the same one the reviews keep describing: Midjourney for editorial and stylized work, Flux for realism and high-volume iteration, Ideogram for typography. Pick by job and you never waste a credit.",
     "highlights": [
       {"title": "Midjourney V8 still owns aesthetics", "body": "Artistic image quality is where it stays untouchable, and the V8 Alpha renders about 5x faster with native 2K output. The old speed complaint keeps fading, which holds it at number one for anyone who cares how an image looks."},
       {"title": "Flux 2 Pro is the photorealism default", "body": "It posts the highest technical quality with a 4.5-second generation time. For product photography or a portrait that must pass as a real photo, this is the one I open first, and that realism focus keeps it a clear second."},
       {"title": "GPT Image 2 is the dependable all-rounder", "body": "It is the most reliable single tool here on prompt-following and complex instructions. For anyone who values consistency over an artistic ceiling, it is a defensible top pick and holds a firm third."},
       {"title": "Ideogram V3 wins on text", "body": "It renders headline copy, logos and packaging mockups with an accuracy nobody else reliably matches. For any image that needs readable text baked in, it stays the specialist worth keeping in the kit at number four."},
     ],
   },
   {
     "commentary": "2026 年 6 月的 AI 生圖已經徹底分眾，我的排名就照這個現實走，不假裝有哪個模型全包。Midjourney V8 我還是放第一，因為美感品質它依舊無敵，V8 Alpha 算圖快了大約 5 倍、原生 2K 輸出，過去被嫌的速度問題持續縮小。案子是藝術，答案就是它。Flux 2 Pro 守第二，是寫實的預設選擇，技術品質最高、生成只要 4.5 秒，商品攝影或要能當真人照片用的人像，我第一個開它。GPT Image 2 守第三，是全能王，指令遵循跟複雜指示是榜上最穩的單一工具，重視一致性勝過藝術天花板的人放它最安全。Ideogram V3 守第四，靠的是依然像變魔術的文字渲染，海報、包裝、任何要嵌標題文字的圖都找它。Imagen 4、Firefly 4、SD 3.5 Large 這週沒事件，全部照舊。最常見的專業工作流就是評測一直在講的那套：Midjourney 做編輯與風格化、Flux 做寫實與大量迭代、Ideogram 做文字。看任務選工具，你一個額度都不會浪費。",
     "highlights": [
       {"title": "Midjourney V8 美感依舊無敵", "body": "藝術圖質它還是沒人能碰，V8 Alpha 算圖快約 5 倍、原生 2K 輸出。過去被嫌的速度問題持續消失，對在意成品好不好看的人，第一名穩穩的。"},
       {"title": "Flux 2 Pro 是寫實預設", "body": "技術品質最高、生成只要 4.5 秒。商品攝影、或要能當真人照片用的人像，我第一個開它，這份寫實專注讓它穩坐第二。"},
       {"title": "GPT Image 2 是靠得住的全能王", "body": "指令遵循跟複雜指示是榜上最穩的單一工具。重視一致性勝過藝術天花板的人，放它當第一也合理，這裡穩在第三。"},
       {"title": "Ideogram V3 贏在文字", "body": "標題文字、Logo、包裝模擬，它渲染的準確度沒人能穩定追上。任何要嵌入可讀文字的圖，它都是值得留在工具箱裡的專家，守第四。"},
     ],
   })

# ---------------- best-ai-video-generators ----------------
do("best-ai-video-generators.json",
   [
     {"title": "Best AI Video Generators 2026: Sora 2 vs Veo 3.1 vs Kling 3.0 vs Runway", "url": "https://www.getaiperks.com/en/blogs/44-best-ai-video-generators-2026", "source": "Get AI Perks"},
     {"title": "After Sora: Best AI Video Generators 2026 Complete", "url": "https://www.digitalapplied.com/blog/after-sora-best-ai-video-generators-2026-runway-kling-veo", "source": "Digital Applied"},
   ],
   {
     "commentary": "Veo 3.1 stays at number one because it is the safest overall answer in the room, and the reason is native audio. When a script leans on natural dialogue or ambient sound generated inside the same pass, nothing else matches it, and for ads that is the whole job. Runway Gen-4.5 holds second as the control pick: reference images and character control give brand-consistent output that marketers can actually ship, and the Gen-4 Turbo family is fast enough for real production timelines. Kling 3.0 stays third and is the value story of the month, currently topping some text-to-video arenas while costing a fraction of the flagships, so for high-volume social work it is the smart spend. Seedance 2.0 holds fourth as the hottest image-to-video model right now. The big structural news colors the whole list: OpenAI shut down the Sora web and app on April 26 and the API runs only until September, which is exactly why Sora is no longer a default recommendation here, it matters mainly to teams migrating existing story-led workflows. The field moved from one assumed leader to a specialist map, and that is how I ranked it: Veo for all-purpose and dialogue, Runway for control, Kling for value, Seedance for image-to-video.",
     "highlights": [
       {"title": "Veo 3.1 wins on native audio", "body": "When a script relies on dialogue or ambient sound generated in the same pass, nothing else matches it, and for ads that is the entire job. That makes it the safest all-purpose pick and holds it at number one."},
       {"title": "Runway Gen-4.5 is the control pick", "body": "Reference images and character control deliver brand-consistent output marketers can actually ship, and the Gen-4 Turbo family is fast enough for real timelines. That reliability keeps it a clear second for professional work."},
       {"title": "Kling 3.0 is the value flagship", "body": "It tops some text-to-video arenas while costing a fraction of the flagships. For high-volume social and marketing work where budget per clip matters, it is the smart spend and earns a firm third."},
       {"title": "Sora's shutdown reshaped the field", "body": "OpenAI closed the Sora web and app on April 26 with the API running only until September. That is why it is no longer a default recommendation here, mattering mainly to teams migrating existing story-led workflows."},
     ],
   },
   {
     "commentary": "Veo 3.1 我還是放第一，因為它是全場最穩的通用答案，關鍵就在原生音訊。當腳本要靠自然對白或環境音、而且是在同一次生成裡一起產出時，沒人比得上它，做廣告這就是全部的活。Runway Gen-4.5 守第二，是掌控派的選擇：參考圖跟角色一致性讓品牌輸出穩定到行銷真的敢拿去用，Gen-4 Turbo 系列又快到跟得上真實製作時程。Kling 3.0 守第三，是這個月的性價比故事，現在在部分文字轉影片競技場領先，成本卻只有旗艦的零頭，量大的社群內容拿它最划算。Seedance 2.0 守第四，是現在最紅的圖生影片模型。最大的結構性新聞影響整張榜：OpenAI 在 4 月 26 號關掉 Sora 的網頁跟 App，API 也只撐到 9 月，這正是 Sora 在這裡不再是預設推薦的原因，它現在主要對要遷移既有敘事工作流的團隊有意義。整個領域從一個假定龍頭變成分眾地圖，我就照這樣排：通用跟對白找 Veo、要掌控找 Runway、要性價比找 Kling、圖生影片找 Seedance。",
     "highlights": [
       {"title": "Veo 3.1 贏在原生音訊", "body": "腳本要靠對白或環境音、又要在同一次生成裡一起產出時，沒人比得上它，做廣告這就是全部的活。這讓它成為最穩的通用選擇，守住第一。"},
       {"title": "Runway Gen-4.5 是掌控派選擇", "body": "參考圖跟角色一致性讓品牌輸出穩定到行銷敢直接拿去用，Gen-4 Turbo 系列又快到跟得上真實時程。這份可靠讓它在專業場景穩坐第二。"},
       {"title": "Kling 3.0 是性價比旗艦", "body": "它在部分文字轉影片競技場領先，成本卻只有旗艦零頭。量大的社群與行銷、每支成本要算清楚時，拿它最聰明，穩在第三。"},
       {"title": "Sora 收攤重塑了整個領域", "body": "OpenAI 在 4 月 26 號關掉 Sora 網頁跟 App，API 只撐到 9 月。這就是它在這裡不再是預設推薦的原因，現在主要對要遷移既有敘事工作流的團隊有意義。"},
     ],
   })

# ---------------- best-ai-voice-generators ----------------
do("best-ai-voice-generators.json",
   [
     {"title": "Best AI Voice Generators 2026: ElevenLabs, Hume, Cartesia Compared", "url": "https://llm-stats.com/leaderboards/best-ai-for-voice-generation", "source": "LLM-Stats"},
     {"title": "Top Text-to-Speech Models June 2026", "url": "https://www.buildmvpfast.com/articles/best-llms-2026-guide", "source": "Build MVP Fast"},
   ],
   {
     "commentary": "Inworld TTS 1.5 Max and ElevenLabs sit tied at the top for me, and the tie is honest because they win different jobs. Inworld edges in on raw naturalness and the price-to-quality ratio that game and app developers care about when they are generating thousands of lines, so for production-scale voice it is the one I would build on. ElevenLabs stays its equal because the voice library, cloning quality and language breadth are still the deepest in the business, and for narration, audiobooks and dubbing it remains the default that just works. Hume AI Octave 2 holds third on emotional range, the model to reach for when delivery and feeling matter more than throughput. Minimax Speech 02 HD stays fourth as a genuine value standout with HD output that punches above its price. Cartesia Sonic 3 holds fifth on latency, the pick for real-time agents and live conversation where every millisecond shows. Nothing this week reordered the top tier, so I held ranks. The buying advice is simple: scale and games lean Inworld, library and cloning lean ElevenLabs, emotion leans Hume, real-time leans Cartesia. Match the voice engine to the use case and the quality gap between them stops mattering.",
     "highlights": [
       {"title": "Inworld and ElevenLabs are a genuine tie", "body": "Inworld edges in on naturalness and price-to-quality for production-scale generation, while ElevenLabs keeps the deepest voice library, best cloning and widest language support. They win different jobs, so they share the top."},
       {"title": "Hume Octave 2 owns emotional range", "body": "When delivery and feeling matter more than throughput, it is the model to reach for. That expressive edge keeps it a clear third for character work and any script where the emotion carries the line."},
       {"title": "Minimax Speech 02 HD is the value standout", "body": "Its HD output punches well above its price, making it the smart pick for teams that need strong quality without flagship spend. That value keeps it firmly in the top tier at fourth."},
       {"title": "Cartesia Sonic 3 wins on latency", "body": "For real-time voice agents and live conversation, every millisecond shows, and Sonic 3 is built for exactly that. It holds fifth as the specialist pick whenever speed of response is the deciding factor."},
     ],
   },
   {
     "commentary": "Inworld TTS 1.5 Max 跟 ElevenLabs 在我這並列第一，這個並列很誠實，因為它們贏的是不同的活。Inworld 在純自然度跟性價比上略勝，這正是遊戲跟 App 開發者要量產上千句台詞時最在意的，要做產線級的語音我會押它。ElevenLabs 平起平坐，是因為它的語音庫、複製品質跟語言廣度依然是業界最深的，旁白、有聲書、配音它還是那個開了就能用的預設。Hume AI Octave 2 守第三，靠情感表現，當演繹跟情緒比吞吐量更重要時就找它。Minimax Speech 02 HD 守第四，是真正的性價比亮點，HD 輸出的水準遠超它的價格。Cartesia Sonic 3 守第五，靠延遲，即時代理跟現場對話、每一毫秒都看得出來時就選它。這週沒有事件重排前段，所以我守住排名。買法很簡單：量產跟遊戲偏 Inworld、語音庫跟複製偏 ElevenLabs、情感偏 Hume、即時偏 Cartesia。把語音引擎對準使用情境，它們之間的品質差距就不重要了。",
     "highlights": [
       {"title": "Inworld 跟 ElevenLabs 是真正的並列", "body": "Inworld 在自然度跟產線級量產的性價比略勝，ElevenLabs 守住最深的語音庫、最好的複製跟最廣的語言支援。它們贏的是不同的活，所以共享第一。"},
       {"title": "Hume Octave 2 主宰情感表現", "body": "當演繹跟情緒比吞吐量更重要時就找它。這份表現力讓它在角色配音、以及任何靠情緒撐起台詞的腳本上穩坐第三。"},
       {"title": "Minimax Speech 02 HD 是性價比亮點", "body": "HD 輸出的水準遠超它的價格，是需要好品質又不想花旗艦錢的團隊的聰明選擇。這份性價比讓它穩在前段第四。"},
       {"title": "Cartesia Sonic 3 贏在延遲", "body": "即時語音代理跟現場對話，每一毫秒都看得出來，Sonic 3 就是為這個打造的。回應速度是決勝點時，它守第五當專家選擇。"},
     ],
   })

# ---------------- best-ai-music-generators ----------------
do("best-ai-music-generators.json",
   [
     {"title": "Best AI Music Generators 2026: Suno, Udio, ElevenLabs Compared", "url": "https://www.gradually.ai/en/ai-music-models/", "source": "Gradually"},
     {"title": "AI Music Generation Leaderboard June 2026", "url": "https://llm-stats.com/leaderboards/best-ai-for-music-generation", "source": "LLM-Stats"},
   ],
   {
     "commentary": "Suno v5 stays at number one and it is not close. The vocal realism, the song structure that actually resolves, the sheer range from a one-line prompt, it remains the tool that turns a hum into a finished track faster than anything else on the market. For creators who want a complete song now, this is the answer. ElevenLabs Music holds second and earns it on production cleanliness and the brand trust that comes from a company whose audio pipeline is already industry standard, so for commercial use where licensing clarity matters it is my safe pick. Udio stays third on audio fidelity, the choice for people who care most about how the mix sounds rather than how fast it generates. Lyria 3 Pro holds fourth as Google's serious entry with strong instrumental control. Stable Audio 2.5 stays fifth as the value and open-leaning option. Nothing this week shifted the order. The honest read: Suno wins on completeness and speed, ElevenLabs on commercial polish, Udio on fidelity. If you are making music to actually release, start with Suno and master elsewhere. If you need clean licensing, start with ElevenLabs.",
     "highlights": [
       {"title": "Suno v5 turns a prompt into a finished song", "body": "Vocal realism, structure that resolves, and range from a single line keep it the fastest path from idea to complete track. For creators who want a song now, nothing else competes, which holds it at number one."},
       {"title": "ElevenLabs Music is the commercial-safe pick", "body": "Production cleanliness plus the trust of an already industry-standard audio company make licensing clarity its edge. For commercial use where rights matter, it is my default and a clear second."},
       {"title": "Udio wins on audio fidelity", "body": "For people who care most about how the mix actually sounds rather than generation speed, it delivers the cleanest output in the group. That focus on sound quality keeps it a firm third."},
       {"title": "Lyria 3 Pro brings real instrumental control", "body": "Google's serious entry gives more granular control over instrumentation than most rivals. That makes it the pick for creators who want to shape the arrangement, holding fourth this month."},
     ],
   },
   {
     "commentary": "Suno v5 還是第一，而且差距不小。人聲擬真、會真正收尾的歌曲結構、一句提示就能拉出的廣度，它依然是市面上把哼唱變成完整曲子最快的工具。想現在就要一首完整的歌，答案就是它。ElevenLabs Music 守第二，贏在製作的乾淨度，加上一家音訊管線本來就是業界標準的公司帶來的品牌信任，商用、授權要清楚時它是我的安全牌。Udio 守第三，靠音訊保真度，最在意混音聽起來如何、而非生成多快的人會選它。Lyria 3 Pro 守第四，是 Google 認真的作品，樂器控制很強。Stable Audio 2.5 守第五，是偏開放的性價比選擇。這週沒有事件改變順序。老實講：Suno 贏在完整度跟速度、ElevenLabs 贏在商用精緻度、Udio 贏在保真。要做真的會發行的音樂，從 Suno 起手再去別處母帶處理。需要乾淨授權，從 ElevenLabs 起手。",
     "highlights": [
       {"title": "Suno v5 一句提示變一首完整的歌", "body": "人聲擬真、會收尾的結構、一句話就能拉出的廣度，讓它是從想法到完整曲子最快的路。想現在就要一首歌，沒人能比，守住第一。"},
       {"title": "ElevenLabs Music 是商用安全牌", "body": "製作乾淨加上一家本來就是業界標準的音訊公司帶來的信任，授權清楚是它的優勢。商用、版權要算清楚時它是我的預設，穩坐第二。"},
       {"title": "Udio 贏在音訊保真", "body": "最在意混音聽起來如何、而非生成速度的人，它給的是這群裡最乾淨的輸出。這份對音質的專注讓它穩在第三。"},
       {"title": "Lyria 3 Pro 帶來真正的樂器控制", "body": "Google 認真的作品，對配器的控制比多數對手更細。這讓它成為想自己塑造編曲的創作者的選擇，這個月守第四。"},
     ],
   })

# ---------------- best-ai-meeting-assistants ----------------
do("best-ai-meeting-assistants.json",
   [
     {"title": "Best AI Meeting Assistants 2026: Granola, Fathom, Fireflies Compared", "url": "https://www.gradually.ai/en/ai-meeting-assistants/", "source": "Gradually"},
     {"title": "Top AI Notetakers June 2026", "url": "https://zapier.com/blog/best-ai-meeting-assistant/", "source": "Zapier"},
   ],
   {
     "commentary": "Granola stays at number one because it solved the thing every other notetaker got wrong: it does not send a bot into your call. It listens locally, augments your own typed notes, and produces a clean summary that reads like a sharp colleague wrote it, which is exactly why privacy-conscious teams keep switching to it. Fathom holds a close second as the best free-tier value in the category, genuinely usable without paying and fast at turning a call into shareable action items. Fireflies stays third on integrations, the pick for teams that need the transcript flowing into a CRM, a ticketing system and a dozen other tools automatically. Otter holds fourth and remains the most recognizable name with solid real-time transcription, the safe institutional choice. Fellow sits fifth on its meeting-management framing for teams that run on agendas and follow-ups. Nothing this week reordered the top. The buying logic is clean: privacy and note quality lean Granola, free value leans Fathom, integration depth leans Fireflies. Pick by what your workflow actually needs and any of the top three will serve you well.",
     "highlights": [
       {"title": "Granola wins by not sending a bot", "body": "It listens locally and augments your own notes instead of joining the call as a visible participant, which is exactly why privacy-conscious teams keep switching. That approach plus genuinely sharp summaries holds it at number one."},
       {"title": "Fathom is the best free-tier value", "body": "It is genuinely usable without paying and fast at turning a call into shareable action items. For individuals and small teams testing the category, nothing else delivers this much for free, holding a close second."},
       {"title": "Fireflies owns integrations", "body": "For teams that need the transcript flowing automatically into a CRM, ticketing and a dozen other tools, its connector depth is the deepest here. That makes it the workflow-automation pick and a firm third."},
       {"title": "Pick by what your workflow needs", "body": "Privacy and note quality lean Granola, free value leans Fathom, integration depth leans Fireflies. The category is mature enough that any top-three pick serves well, so match the tool to your actual stack."},
     ],
   },
   {
     "commentary": "Granola 還是第一，因為它解決了其他筆記工具都搞錯的事：它不會派一隻機器人進你的會議。它在本地聆聽、補強你自己打的筆記，產出一份讀起來像精明同事寫的乾淨摘要，這正是注重隱私的團隊一直轉過去的原因。Fathom 緊咬第二，是這個類別最佳的免費方案價值，不付錢也真的能用，把會議變成可分享的待辦又快。Fireflies 守第三，靠整合，要讓逐字稿自動流進 CRM、工單系統跟一堆其他工具的團隊會選它。Otter 守第四，依然是最有名的名字，即時轉錄紮實，是穩的機構型選擇。Fellow 排第五，靠它以議程跟追蹤為核心的會議管理定位，適合靠議程運作的團隊。這週沒有事件重排前段。買法很乾淨：隱私跟筆記品質偏 Granola、免費價值偏 Fathom、整合深度偏 Fireflies。照你工作流真正需要的選，前三名隨便挑一個都會服務得很好。",
     "highlights": [
       {"title": "Granola 贏在不派機器人進會議", "body": "它在本地聆聽、補強你自己的筆記，而不是當看得見的參與者加入通話，這正是注重隱私的團隊一直轉過去的原因。這套做法加上真的精明的摘要，守住第一。"},
       {"title": "Fathom 是最佳免費方案價值", "body": "不付錢也真的能用，把會議變成可分享待辦又快。對在試這個類別的個人跟小團隊，沒人免費給這麼多，緊咬第二。"},
       {"title": "Fireflies 主宰整合", "body": "要讓逐字稿自動流進 CRM、工單跟一堆其他工具的團隊，它的連接器深度是這裡最深的。這讓它成為工作流自動化的選擇，穩在第三。"},
       {"title": "照工作流需求選", "body": "隱私跟筆記品質偏 Granola、免費價值偏 Fathom、整合深度偏 Fireflies。這類別夠成熟，前三名隨便挑都好用，把工具對準你實際的工具鏈就對了。"},
     ],
   })

print("batchA done")
