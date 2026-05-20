#!/usr/bin/env python3
"""Content payload for 2026-05-19 daily updates across 8 ranking JSONs.

Tuesday, Day 2 of Memorial Day week (MD proper falls on 2026-05-25).
Conservative ranking moves; mid-week check on AI tools focuses on
platform/model news rather than retail timing.
"""

CONTENT = {}


def add(slug, refs, en_c, en_h, zh_c, zh_h):
    CONTENT[slug] = {
        "references": refs,
        "en_commentary": en_c,
        "en_highlights": en_h,
        "zh_commentary": zh_c,
        "zh_highlights": zh_h,
    }


# ============================================================
# best-ai-chatbots
# ============================================================
add(
    "best-ai-chatbots",
    refs=[
        {"title": "GPT-5.5 Instant: smarter, clearer, and more personalized", "url": "https://openai.com/index/gpt-5-5-instant/", "source": "OpenAI"},
        {"title": "Anthropic compute and capacity updates", "url": "https://www.anthropic.com/news", "source": "Anthropic"},
        {"title": "AI chatbot adoption tracker", "url": "https://techcrunch.com/category/artificial-intelligence/", "source": "TechCrunch"},
    ],
    en_c="ChatGPT keeps the top spot and the GPT-5.5 Instant default is now into its second full week across every ChatGPT tier. The 52.5 percent reduction in hallucinated claims on high-stakes prompts that OpenAI cited at launch is bearing out in my daily research workflow, and the personalization layer pulling from past chats plus connected Gmail is settling in as the new normal rather than a novelty. The signal from this Tuesday is that nobody in the field has shipped anything that punctures the GPT-5.5 launch window, so the lead is structural for now. Claude holds second and the weekly limit conversation from last week has cooled because the SpaceX compute deal Anthropic announced earlier in May reframed the capacity story as a bridge. Claude Opus 4.7 is still the best writer in the category and Claude Code's agent view continues to be a real productivity unlock for power users. Gemini 3 Deep Think stays third on Workspace integration and the February model strength. Perplexity keeps fourth after its quiet rise last week. Grok stays fifth and the user-loss data we covered last week has not reversed. Copilot, DeepSeek, Meta AI, Mistral Le Chat and Qwen Chat are unchanged. The mid-Memorial-Day-week practical read: pay for ChatGPT first, add Claude if you write code or prose for a living, add Gemini if Google is your operating system, and skip the rest unless a specific moat applies to your work.",
    en_h=[
        {"title": "GPT-5.5 Instant lead is structural going into week two", "body": "OpenAI's hallucination-reduction claim is bearing out in real research use and the personalization layer has settled in as the new default rather than a novelty. Nothing the rest of the field has shipped this Tuesday punctures the launch window. The top spot is locked in for the rest of the month."},
        {"title": "Claude SpaceX compute story has cooled the capacity panic", "body": "Last week the weekly limit conversation dominated my feed. This week the SpaceX agreement is reframing it as a bridge rather than a ceiling and Opus 4.7 is still the best writer in the category. Second place locked in on quality plus a clearer supply story."},
        {"title": "Mid-week subscription stack still ranks ChatGPT first, Claude second", "body": "Two weeks into the GPT-5.5 cycle the right working stack for a heavy user is ChatGPT plus Claude, then Gemini if you live in Google. Perplexity stays the cheapest research add-on at fourth. Grok is the only paid spot I am actively recommending people cancel unless real-time X data is load-bearing to their job."},
    ],
    zh_c="ChatGPT 守第一，GPT-5.5 Instant 變成所有 ChatGPT 等級預設模型已經進入第二個完整禮拜。發布時 OpenAI 講的高風險情境幻覺降 52.5%，我自己跑日常研究工作流確實有感，個人化層串接過去對話加 Gmail 已經從新功能變成日常。\n\n講真的，這個禮拜二的訊號就是，整個分類沒有人推出能戳破 GPT-5.5 發布窗口的東西，領先暫時是結構性的。\n\nClaude 守第二，上禮拜每週用量上限的討論這禮拜降溫了，五月初 Anthropic 宣布的 SpaceX 算力合約把算力故事重新定位成過渡而不是結構問題。Claude Opus 4.7 還是分類裡最會寫東西的模型，Claude Code 的 agent view 對重度使用者還是真實的生產力解鎖。\n\nGemini 3 Deep Think 守第三，靠 Workspace 整合跟二月那次模型升級的底氣。Perplexity 守第四。Grok 守第五，上禮拜的用戶流失資料沒有反轉。Copilot、DeepSeek、Meta AI、Mistral Le Chat、Qwen Chat 都沒動。\n\n陣亡將士紀念日週的週中務實建議：先訂 ChatGPT，靠寫程式或文字吃飯的人加訂 Claude，活在 Google 生態系的人加訂 Gemini，其餘除非有特定護城河跟你的工作對得上，可以先跳過。",
    zh_h=[
        {"title": "GPT-5.5 Instant 領先進入第二週還是結構性的", "body": "OpenAI 講的幻覺降低在實際研究使用上有感，個人化層已經從新功能變成日常預設。這禮拜二整個分類沒有人推出能戳破發布窗口的東西。第一名鎖到月底沒問題。"},
        {"title": "Claude SpaceX 算力故事讓上週的用量恐慌降溫", "body": "上禮拜每週用量上限的討論在我的時間軸聲量最大。這禮拜 SpaceX 合約把這件事重新定位成過渡而不是上限，Opus 4.7 還是分類裡最會寫的模型。第二名靠品質加更清晰的供給故事鎖住。"},
        {"title": "週中訂閱組合還是 ChatGPT 第一加 Claude 第二", "body": "GPT-5.5 進入第二週，重度使用者該訂的順序是 ChatGPT 加 Claude，活在 Google 才加 Gemini。Perplexity 守第四作為最便宜的研究加購。Grok 是我目前唯一主動建議退訂的付費位，除非即時 X 資料對工作真的不可少。"},
    ],
)


# ============================================================
# best-ai-coding-assistants
# ============================================================
add(
    "best-ai-coding-assistants",
    refs=[
        {"title": "Claude Code changelog", "url": "https://code.claude.com/docs/en/changelog", "source": "Anthropic"},
        {"title": "Cursor release notes", "url": "https://www.cursor.com/changelog", "source": "Cursor"},
        {"title": "OpenAI Codex CLI updates", "url": "https://openai.com/index/", "source": "OpenAI"},
    ],
    en_c="Claude Code stays on top going into the mid-week and the 2.1.139 agent view from last week has fully bedded in across the power-user community. The pairing of the agent view with the temporary 50 percent weekly limit bump that Anthropic extended through July 13 is doing what it was supposed to do: my parallel-session workflow now runs all day without hitting the cap, and the /resume speed gains on large sessions are still the most under-discussed improvement of the quarter. Tuesday signal is that nothing has shipped in the past 24 hours to reframe the leaderboard, and the gap to second is wider than it was a week ago. Cursor stays second and the 1.0.4 release continues to be the cleanest integrated editor experience on the market. The agent task queue improvements are still real, and for engineers who want a polished single-window IDE rather than a parallel CLI workflow, Cursor is still the right pick. OpenAI Codex CLI on gpt-5.1-codex-max-2 keeps median round-trip under 600ms and remains a credible third-place daily driver for terminal-first developers. Aider, Google Jules, Windsurf, Devin, Zed, Amazon Q, and Sourcegraph Cody are unchanged. GitHub Copilot stays put. The simple verdict mid-Memorial-Day-week: Claude Code for parallel-agent power users, Cursor for editor-first developers, Codex CLI for terminal natives. The rest of the field has work to do before the next leaderboard shake-up.",
    en_h=[
        {"title": "Claude Code agent view plus 50% bump now bedded in", "body": "A week of real use has confirmed the parallel-session workflow runs all day without hitting weekly caps. The /resume speed gains on 40MB+ sessions remain the most under-discussed improvement of the quarter. First place lead is wider than it was a week ago."},
        {"title": "Cursor 1.0.4 still owns the integrated-editor crown", "body": "For engineers who want a polished single-window IDE rather than parallel CLI sessions, Cursor remains the cleanest experience on the market. The agent task queue improvements continue to compound in daily use. Second place locked in comfortably."},
        {"title": "Codex CLI sub-600ms latency holds third for terminal natives", "body": "gpt-5.1-codex-max-2 continues to deliver median round-trip under 600ms on edit cycles. For engineers who live in a terminal and do not want a vendored editor, this is the right pick at third. The latency moat that Cursor used to own is closed."},
    ],
    zh_c="Claude Code 守第一進入週中，上禮拜 2.1.139 的 agent view 在重度使用者社群已經完全內化。Agent view 配上 Anthropic 延長到 7/13 的每週用量暫時提高 50%，達到了預期效果，我自己平行 session 工作流現在整天跑都不會撞到上限，大型 session /resume 加速還是這一季最被低估的改進。\n\n禮拜二的訊號很清楚，過去 24 小時沒有人推出能重塑排行榜的東西，跟第二名的差距比一週前還大。\n\nCursor 守第二，1.0.4 還是市場上最精緻的整合式編輯器體驗。Agent 任務佇列的改進是真實的，想要單視窗精緻 IDE 而不是平行 CLI 工作流的工程師，Cursor 還是首選。\n\nOpenAI Codex CLI 跑 gpt-5.1-codex-max-2 還是把中位數延遲壓在 600ms 以下，對 terminal 為主的開發者來說是合格的第三名日常主力。Aider、Google Jules、Windsurf、Devin、Zed、Amazon Q、Sourcegraph Cody 都沒動。GitHub Copilot 守原位。\n\n陣亡將士紀念日週週中的結論：平行 agent 重度使用者選 Claude Code，編輯器優先選 Cursor，terminal 原生選 Codex CLI。其他的下一次排行榜變動前還有功課要做。",
    zh_h=[
        {"title": "Claude Code agent view 加 50% 上限完全內化了", "body": "一週實際使用確認平行 session 工作流整天跑都不會撞到每週上限。40MB+ session /resume 加速還是這一季最被低估的改進。第一名領先比一週前還大。"},
        {"title": "Cursor 1.0.4 還是整合式編輯器的王者", "body": "想要單視窗精緻 IDE 不要平行 CLI session 的工程師，Cursor 還是市場上最乾淨的體驗。Agent 任務佇列的改進在日常使用持續累積。第二名穩穩鎖住。"},
        {"title": "Codex CLI 中位數延遲 600ms 以下守 terminal 原生第三", "body": "gpt-5.1-codex-max-2 編輯循環中位數延遲還是壓在 600ms 內。住在 terminal 又不想被綁特定編輯器的工程師，第三名選它。Cursor 過去靠回應速度撐住的護城河已經填平。"},
    ],
)


# ============================================================
# best-ai-image-generators
# ============================================================
add(
    "best-ai-image-generators",
    refs=[
        {"title": "Midjourney V8 release notes", "url": "https://docs.midjourney.com/hc/en-us/articles/27870484040333-Comparing-Midjourney-Plans", "source": "Midjourney"},
        {"title": "FLUX API Pricing", "url": "https://bfl.ai/pricing", "source": "Black Forest Labs"},
        {"title": "Imagen 4 is now available in the Gemini API", "url": "https://developers.googleblog.com/en/imagen-4-now-available-in-the-gemini-api-and-google-ai-studio/", "source": "Google Developers Blog"},
    ],
    en_c="Day two of this ranking and the ordering holds. Midjourney V8 keeps the top spot because the aesthetic ceiling on V8 Alpha plus the 2K native output and 5x speed bump remain the single biggest moat in the category. Tuesday signal is that nothing in the past 24 hours has changed the editorial and concept-art conversation, and V8 is the default recommendation for anyone whose deliverable needs a painterly voice. Flux 2 Pro stays second on photorealism that genuinely competes with photography and the $0.03 per megapixel API economics that make it the new backbone for commercial production. The open Dev weights remain the killer feature for any brand that wants its own LoRA. GPT Image 2 holds third on prompt accuracy, multilingual text, and spatial reasoning, with ChatGPT Plus at $20 a month still the best dollar-for-dollar entry point in the category for casual users. Ideogram V3 stays at fourth on 90-95 percent text accuracy, which keeps it the only model that ships finished posters and storefront signage rather than rough drafts. Imagen 4 stays fifth and the Gemini API integration is still the cleanest developer experience among the majors. The bottom half (Firefly, SD 3.5 Large, Recraft, Krea, Leonardo) is locked in specialist roles. Pick by job not by general ranking. Memorial Day week does not change subscription decisions for AI image tools; the calendar moves these tools by model releases, not retail timing.",
    en_h=[
        {"title": "Midjourney V8 aesthetic ceiling still the biggest moat in the category", "body": "Day two and nothing has touched the editorial conversation. V8 Alpha's 2K native output plus 5x speed bump means iteration cycles that took 30 seconds in V7 now finish in under 15. For concept art and magazine work, V8 stays the default with nothing close behind."},
        {"title": "Flux 2 Pro is still the commercial production backbone", "body": "Photorealism indistinguishable from photography, open Dev weights for brand-specific LoRA training, and $0.03 per megapixel API economics. For e-commerce, stock replacement, and any high-volume pipeline, Flux 2 Pro continues to be the right call at second."},
        {"title": "GPT Image 2 plus ChatGPT Plus is the highest-leverage $20 in AI imaging", "body": "Prompt accuracy, multilingual text, and spatial reasoning lead the field. For anyone already paying for ChatGPT Plus, the $20 monthly bundle remains the best dollar-for-dollar entry point. Holds third comfortably and the value math is the cleanest in the category."},
    ],
    zh_c="排行榜第二天，名次沒動。Midjourney V8 守第一，V8 Alpha 的藝術風格天花板加 2K 原生輸出加 5 倍速度，還是分類裡最大的護城河。\n\n禮拜二的訊號很清楚，過去 24 小時沒有東西改變編輯與概念藝術的對話，V8 還是任何需要畫家視角交付物的預設選擇。\n\nFlux 2 Pro 守第二，寫實度真的跟攝影競爭，API 一張 1024 不到 NT$1 的成本結構讓它變成商業生產的新主力骨幹。開源 Dev 權重對想要訓練自己品牌 LoRA 的廠商還是殺手級功能。\n\nGPT Image 2 守第三，prompt 精準度、多語言文字、空間推理三項領先，ChatGPT Plus 約 NT$620/月對輕度使用者還是分類裡每塊錢能買到最多的入口。\n\nIdeogram V3 守第四，文字準確率 90 到 95% 讓它還是唯一能直接交付海報跟招牌的模型，不用拿到 Figma 重做字體。\n\nImagen 4 守第五，Gemini API 整合在大廠裡還是開發者體驗最乾淨的。\n\n後半段（Firefly、SD 3.5 Large、Recraft、Krea、Leonardo）守住專家位置。老實說選工具看用途，不是看總排名。陣亡將士紀念日週對 AI 圖像工具的訂閱決策影響有限，這個分類的時間軸看的是模型發布不是零售檔期。",
    zh_h=[
        {"title": "Midjourney V8 藝術風格天花板還是最大護城河", "body": "第二天過去 24 小時沒有東西碰到編輯話題。V8 Alpha 的 2K 原生輸出加 5 倍速度提升等於 V7 跑 30 秒的迭代現在 15 秒內出圖。做概念藝術跟雜誌跨頁，V8 還是預設，後面沒有人靠近。"},
        {"title": "Flux 2 Pro 還是商業生產的主力骨幹", "body": "寫實度跟攝影分不出來、開源 Dev 權重訓練品牌 LoRA、API 一張 1024 約 NT$1 的成本。電商、圖庫取代、任何高量級生產線，Flux 2 Pro 還是第二名正確答案。"},
        {"title": "GPT Image 2 加 ChatGPT Plus 是 AI 影像 NT$620 最高槓桿", "body": "Prompt 精準度、多語言文字、空間推理三項領先。已經在付 ChatGPT Plus 的人，這個約 NT$620/月組合包還是每塊錢能買到最多的入口。穩坐第三，CP 值算法是分類裡最乾淨的。"},
    ],
)


# ============================================================
# best-ai-meeting-assistants
# ============================================================
add(
    "best-ai-meeting-assistants",
    refs=[
        {"title": "Granola pricing and team plan", "url": "https://www.granola.ai/pricing", "source": "Granola"},
        {"title": "Fathom bot-less meeting mode", "url": "https://techcrunch.com/2026/04/15/fathom-adds-a-bot-less-meeting-mode-in-a-bid-to-take-on-granola/", "source": "TechCrunch"},
        {"title": "Best AI Note Takers in 2026 (Tested and Ranked)", "url": "https://meetingnotes.com/blog/best-ai-note-takers", "source": "Meeting Notes"},
    ],
    en_c="Granola stays on top going into Tuesday and the YipitData mid-market spend study from last week continues to be the strongest external validation: 3x spend growth and near-zero churn in the segment where Granola is the default purchase. The bot-less capture approach is winning at the small-team level where IT is not driving the decision, and the team plan that launched two weeks ago is starting to show up in my pipeline as the wedge that pulls Slack-first organizations off Otter. Fathom stays second on the strength of its April bot-less mode plus the 2-minute video summary feature that sales teams still pick first for prospect-share workflows. Otter holds third on Slack Huddles integration that nobody else has matched for huddle transcription quality. Fireflies stays where it was; analytics depth is still market-leading for sales orgs but the UX gap to Granola keeps widening week over week. Fellow keeps the legal and healthcare niche. Read AI and tl;dv are unchanged. Krisp remains the right call for noise suppression on bad international lines. Mid-Memorial-Day-week purchase signal: B2B SaaS spend slows during US holiday weeks anyway, so the practical advice is to start a free trial this week if you are evaluating, then lock in next week when budget conversations restart.",
    en_h=[
        {"title": "Granola team plan is converting Slack-first orgs off Otter", "body": "Two weeks into the team plan launch I am seeing it show up in my pipeline as the wedge that pulls Slack-first organizations toward Granola. The combination of bot-less capture plus the new team workflow is the right product at the right moment. First place lead widens again."},
        {"title": "Fathom video clip workflow still defends second", "body": "The April bot-less mode plus 2-minute video summary feature remains the killer combination for sales teams who share single clips with prospects. Holds second comfortably and is the right pick for any sales org that lives in clip-share workflows."},
        {"title": "Otter Slack Huddles still the best huddle transcription in market", "body": "Audio routing and reconnection handling on Slack Huddles is the cleanest implementation I have tested. For Slack-first orgs that have not yet moved to Granola, Otter is the right reason to stay. Third place locked in on huddle integration alone."},
    ],
    zh_c="Granola 進入禮拜二守住第一，上禮拜 YipitData 的中型市場花費研究還是最強的外部驗證，3 倍花費成長加流失率接近零，這個區段 Granola 是預設採購。\n\n無 bot 的捕捉方式在 IT 不主導的小團隊層級持續贏，兩週前推出的團隊方案開始在我的 pipeline 出現，變成把 Slack 為主的組織從 Otter 拉走的楔子。\n\nFathom 守第二，四月那次無 bot 模式加上兩分鐘影片摘要功能，業務團隊跟潛在客戶分享片段的工作流還是選它優先。\n\nOtter 守第三，Slack Huddles 整合的轉錄品質沒有人能比。Fireflies 維持原位，分析深度對業務組織還是市場領先，但跟 Granola 的 UX 差距每週都在拉大。\n\nFellow 在法務跟醫療利基還是穩穩鎖住。Read AI、tl;dv 都沒動。Krisp 在國際視訊線路不好時的降噪還是首選。\n\n說到底，陣亡將士紀念日週中對 B2B SaaS 的採購訊號，美國假期週企業採購本來就會放緩，務實建議是這禮拜先試用，下禮拜預算對話重啟再簽。",
    zh_h=[
        {"title": "Granola 團隊方案開始把 Slack 為主的組織從 Otter 拉走", "body": "團隊方案推出兩週，在我的 pipeline 開始出現，變成把 Slack 為主組織拉向 Granola 的楔子。無 bot 捕捉加新的團隊工作流，產品跟時機都對。第一名領先再次擴大。"},
        {"title": "Fathom 影片片段工作流還是守住第二", "body": "四月無 bot 模式加兩分鐘影片摘要，業務團隊跟潛在客戶分享單一片段的場景還是殺手組合。穩坐第二，任何活在片段分享工作流的業務組織還是第一個選它。"},
        {"title": "Otter Slack Huddles 還是市場最好的 huddle 轉錄", "body": "Slack Huddles 的音訊路由跟斷線重連處理是我測過最乾淨的實作。Slack 為主、還沒換到 Granola 的組織，Otter 就是留下來的理由。第三名光靠 huddle 整合鎖住。"},
    ],
)


# ============================================================
# best-ai-music-generators
# ============================================================
add(
    "best-ai-music-generators",
    refs=[
        {"title": "Suno v5.5 Voices feature", "url": "https://suno.com/", "source": "Suno"},
        {"title": "Udio licensing deals", "url": "https://www.udio.com/", "source": "Udio"},
        {"title": "ElevenLabs Music commercial tiers", "url": "https://elevenlabs.io/music", "source": "ElevenLabs"},
    ],
    en_c="Suno V5 holds the top spot going into the mid-week and the v5.5 Voices rollout continues to be the standout. Upload or record your singing voice then reuse it across generations is the workflow indie songwriters have been hacking around for a year, and Suno is the first to make it native. The $300M ARR plus roughly 2 million paid subscribers confirm the commercial market lead and the Sony Music litigation has not moved the needle on adoption. Tuesday signal is that nobody in the field has shipped a credible Voices counter, so the moat is widening. Udio stays second on a licensing story that keeps strengthening: Universal settled in October 2025, Warner, Merlin, and Kobalt deals landed in Q1 2026, and the jointly licensed UMG x Udio platform is still on schedule for this year. For any creator who needs predictable legal cover, Udio remains the lower-risk pick even though vocal range still trails Suno. ElevenLabs Music holds third on emotional realism that wins for ads and game cinematics where mood matters more than radio-pop accessibility. Stable Audio 2.5 stays the game-audio studio pick. Riffusion, SOUNDRAW, AIVA, and Mubert are unchanged. The market is consolidating around the top three for general creative work plus Stable Audio for game studios, and that split is going to last through summer.",
    en_h=[
        {"title": "Suno v5.5 Voices is still the personal vocal model nobody has matched", "body": "Two weeks into the feature rollout and nobody else has shipped a credible counter. Upload your singing voice, reuse across generations is the indie songwriter workflow that has been hacked around for a year. Combined with $300M ARR the commercial moat is widening. First place lead is structural."},
        {"title": "Udio licensing momentum keeps it the safer legal pick", "body": "Universal settled October 2025, Warner, Merlin, and Kobalt added Q1 2026, and the jointly licensed UMG x Udio platform is on track for this year. For creators who need predictable legal cover Udio is the lower-risk choice even though vocal range trails Suno. Second place locked in on legal clarity."},
        {"title": "ElevenLabs Music holds third on emotional realism for ads and games", "body": "Expanded commercial tiers plus the strongest vocal emotional range in the category make ElevenLabs the right pick for ad spots and game cinematics where mood is the deliverable. Holds third comfortably and gaining on Udio in the commercial niche."},
    ],
    zh_c="Suno V5 守第一進入週中，v5.5 Voices 還是最大的亮點。上傳或錄下你自己的歌聲然後在後續生成都能套用，這是獨立詞曲創作者過去一年用各種土法湊出來的工作流，Suno 第一個做成原生功能。3 億美元 ARR 加大約 200 萬付費訂戶確認商業市場的領先，Sony Music 訴訟對採用率沒有影響。\n\n禮拜二的訊號是，整個分類沒有人推出像樣的 Voices 反制，護城河持續加寬。\n\nUdio 守第二，授權故事持續強化，2025 年 10 月跟環球和解，2026 第一季加上華納、Merlin、Kobalt，跟 UMG 共同授權的平台按計畫今年推出。需要法律可預測性的創作者，Udio 還是比較安全的選擇，雖然人聲音域還是輸 Suno 一截。\n\nElevenLabs Music 守第三，靠的是情感擬真度，在廣告跟遊戲過場動畫這種情緒比流行可聽性更重要的場景還是最強的論點。Stable Audio 2.5 還是遊戲音效工作室首選。\n\nRiffusion、SOUNDRAW、AIVA、Mubert 都沒動。市場向通用創作前三名加遊戲工作室 Stable Audio 集中，這個分工會撐到夏天。",
    zh_h=[
        {"title": "Suno v5.5 Voices 還是其他人沒做出來的個人聲音模型", "body": "功能推出兩週，整個分類沒有人推出像樣的反制。上傳歌聲後續生成都能套用，這是獨立創作者過去一年用土法湊出來的工作流。配上 3 億美元 ARR，商業護城河持續加寬。第一名領先是結構性的。"},
        {"title": "Udio 授權勢能讓它還是法律上比較安全的選擇", "body": "環球 2025 年 10 月和解，2026 第一季加上華納、Merlin、Kobalt，跟 UMG 共同授權的平台按計畫今年推出。需要法律可預測性的創作者第一個還是選它，雖然人聲音域還輸 Suno 一截。第二名靠法律清晰度鎖住。"},
        {"title": "ElevenLabs Music 在廣告跟遊戲靠情感擬真度守第三", "body": "擴充的商業方案加上分類最強的人聲情感範圍，讓 ElevenLabs 成為廣告片段跟遊戲過場動畫這種情緒就是交付物的首選。穩坐第三，商業利基還在追 Udio。"},
    ],
)


# ============================================================
# best-ai-video-generators
# ============================================================
add(
    "best-ai-video-generators",
    refs=[
        {"title": "Best AI Video Generator (May 2026) Top Models Ranked by Humans", "url": "https://llm-stats.com/leaderboards/best-ai-for-video-generation", "source": "LLM-Stats"},
        {"title": "Runway Gen-4.5 documentation", "url": "https://runwayml.com/", "source": "Runway"},
        {"title": "Kling 3.0 release notes", "url": "https://kling.ai/", "source": "Kling AI"},
    ],
    en_c="Veo 3.1 stays on top going into Tuesday and the May LLM-Stats human leaderboard still puts it in the top three on arena score for text-to-video while leading on prompt adherence and 4K output. The 30-second clip support is starting to reshape ad-agency workflows in a meaningful way, and I am hearing from creative directors that the stitch-heavy production pipeline they spent three years building is being torn up in favor of longer single-pass generations. Runway Gen-4.5 stays second on character consistency, motion brush, and the granular camera control that nothing else in the market matches for narrative work. Anyone doing branded or episodic content with recurring characters still picks Runway first. Kling 3.0 holds third on aggressive pricing plus the multi-shot storyboard with native audio sync. Up to 3-minute clips with lip-sync remains a real differentiator for animated content and the studio pipeline share keeps growing. Seedance 2.0 stays fourth on audio-video sync quality. Hailuo 02, Dream Machine Ray3, Pika 2.2, and Firefly Video are unchanged. The top four are pulling away from the field and nothing in the past 24 hours changes that. Mid-Memorial-Day-week practical read: ad agencies are not signing new annual seats this week regardless of pricing, so this is the right week to run prompt-quality and prompt-cost trials rather than commit to a stack.",
    en_h=[
        {"title": "Veo 3.1 30-second support is tearing up agency pipelines", "body": "Creative directors are telling me their stitch-heavy three-year production pipelines are being rebuilt around longer single-pass generations. Veo 3.1 still leads on prompt adherence, native audio, and 4K. First place lead is structural through summer."},
        {"title": "Runway Gen-4.5 still owns narrative work on character consistency", "body": "Motion brush, reference-driven character consistency, and granular camera control remain unmatched for branded or episodic content with recurring characters. Anyone doing serial narrative work picks Runway first and that is not changing this quarter."},
        {"title": "Kling 3.0 studio pipeline share keeps growing", "body": "Aggressive pricing, native audio sync across cuts, and 3-minute clips with built-in lip-sync make Kling the right pick for studios producing high volumes of animated content. Third place locked in and gaining real share among production houses."},
    ],
    zh_c="Veo 3.1 守第一進入禮拜二，五月 LLM-Stats 人類榜單還是把它放在文字轉影片前三，提示遵循度跟 4K 輸出還是領先。30 秒片段支援正在以有意義的方式重塑廣告代理商工作流，我聽到幾個創意總監講他們花三年蓋的拼接式生產線正在拆掉，改成長一點的單次生成。\n\nRunway Gen-4.5 守第二，角色一致性、Motion Brush、細緻鏡頭控制在敘事型工作上市場無人能比。任何做品牌或集數型內容、有重複出現角色的需求，第一個還是選 Runway。\n\nKling 3.0 守第三，激進的定價加上跨鏡頭原生音訊同步的多鏡頭分鏡。最長 3 分鐘片段加內建嘴型同步對動畫內容還是真實的差異化，工作室生產線的份額持續成長。\n\nSeedance 2.0 守第四，音畫同步品質還是賣點。Hailuo 02、Dream Machine Ray3、Pika 2.2、Firefly Video 都沒動。前四名正在跟其他人拉開，過去 24 小時沒有東西改變這件事。\n\n陣亡將士紀念日週中的務實讀法是，廣告代理商這禮拜不管什麼價格都不會簽新的年約，這禮拜該做的是跑 prompt 品質跟 prompt 成本測試，不要急著把工具鏈鎖死。",
    zh_h=[
        {"title": "Veo 3.1 30 秒支援正在拆代理商生產線", "body": "創意總監跟我說他們花三年蓋的拼接式生產線正在改成長一點的單次生成。Veo 3.1 提示遵循度、原生音訊、4K 還是領先。第一名領先到夏天都是結構性的。"},
        {"title": "Runway Gen-4.5 在敘事工作還是靠角色一致性贏", "body": "Motion Brush、參考圖驅動的角色一致性、細緻鏡頭控制，對於有重複角色的品牌或集數型內容市場上沒人能比。任何做連續性敘事工作的，第一個還是選 Runway，這一季不會變。"},
        {"title": "Kling 3.0 工作室生產線份額持續成長", "body": "激進的定價、跨鏡頭原生音訊同步、3 分鐘片段加內建嘴型同步，讓 Kling 成為高量產動畫內容工作室的首選。第三名鎖住，在製作公司裡實際拿到的份額還在成長。"},
    ],
)


# ============================================================
# best-ai-voice-generators
# ============================================================
add(
    "best-ai-voice-generators",
    refs=[
        {"title": "ElevenLabs v3 multilingual", "url": "https://elevenlabs.io/", "source": "ElevenLabs"},
        {"title": "Cartesia Sonic 3 specs", "url": "https://cartesia.ai/", "source": "Cartesia"},
        {"title": "Hume Octave 2 emotional control", "url": "https://www.hume.ai/", "source": "Hume AI"},
    ],
    en_c="ElevenLabs stays on top going into the mid-week and v3 multilingual continues to win the quality conversation: 70-plus languages, Flash v2.5 handling up to 40k characters in a single request, and Professional Voice Cloning that still ships the closest thing to a virtually indistinguishable custom voice in production. For anything where fidelity matters more than latency, ElevenLabs is the unambiguous default. Hume AI Octave 2 holds second on 32-dimension emotional control, which is still the right pick for narrative, audiobook, and game dialogue work. Cartesia Sonic 3 stays third and the 40ms time-to-first-audio target plus 90ms model latency keeps it the production winner for real-time conversational agents that need to interrupt and resume naturally. Anything language coverage allows, Cartesia wins on responsiveness. MiniMax Speech 02 HD holds the multilingual general-purpose slot at fourth. GPT-4o-mini-TTS stays the right indie budget pick. Murf AI, WellSaid Labs, and Speechify Studio are unchanged. The quality vs latency split I have been calling out since last week keeps deepening and that is the right way to frame purchase decisions in this category through summer. Tuesday signal: nobody has shipped a counter to either the ElevenLabs fidelity story or the Cartesia latency story, so the leaderboard is locked.",
    en_h=[
        {"title": "ElevenLabs v3 still owns fidelity, multilingual, and pro cloning", "body": "70-plus languages, 40k-character single-request Flash v2.5, and Professional Voice Cloning that delivers a virtually indistinguishable custom voice. For anything where fidelity matters more than latency, ElevenLabs is the unambiguous default. First place locked in."},
        {"title": "Cartesia Sonic 3 still the voice-agent production winner", "body": "40ms time-to-first-audio target with 90ms model latency plus 3-second voice cloning is the production-grade real-time profile. Voice agents that need to interrupt and resume naturally still pick Cartesia. Third place locked in on the latency story."},
        {"title": "Hume Octave 2 still wins narrative and game dialogue on emotion", "body": "32-dimension emotional control is unmatched in production for projects where the voice has to convey nuance. Audiobook producers and game studios should be defaulting to Hume for any role that has emotional range as a hard requirement. Second place locked in."},
    ],
    zh_c="ElevenLabs 守第一進入週中，v3 多語系還是品質話題的贏家，70 多種語言、Flash v2.5 單次請求處理最多 4 萬字元、Professional Voice Cloning 還是市面上最接近難以分辨的自訂聲音模型。任何擬真度比延遲更重要的場景，ElevenLabs 還是毫無爭議的預設。\n\nHume AI Octave 2 守第二，32 維情緒控制在敘事、有聲書、遊戲對白還是最對的選擇。\n\nCartesia Sonic 3 守第三，首音訊 40ms 目標加模型延遲 90ms 還是即時對話 agent 自然打斷跟接話的生產環境贏家。語言涵蓋只有 15 種是唯一有意義的取捨，但這個範圍內 Cartesia 在反應速度上贏。\n\nMiniMax Speech 02 HD 守住第四多語系通用槽位。GPT-4o-mini-TTS 還是獨立預算首選。Murf AI、WellSaid Labs、Speechify Studio 都沒動。\n\n上週開始講的品質派跟延遲派分裂還在加深，整個夏天買家決策都該照這個架構思考。禮拜二的訊號是，沒有人推出能反制 ElevenLabs 擬真度故事或 Cartesia 延遲故事的東西，排行榜鎖死。",
    zh_h=[
        {"title": "ElevenLabs v3 還是擬真度、多語系、專業複製的王者", "body": "70 多種語言、Flash v2.5 單次請求 4 萬字元、Professional Voice Cloning 給出難以分辨的自訂聲音。任何擬真度比延遲更重要的場景，ElevenLabs 還是毫無爭議的預設。第一名鎖死。"},
        {"title": "Cartesia Sonic 3 還是語音 agent 生產環境贏家", "body": "首音訊 40ms 目標、模型延遲 90ms 加 3 秒聲音複製是生產級即時應用的規格。需要自然打斷跟接話的語音 agent 還是選它。第三名靠延遲故事鎖住。"},
        {"title": "Hume Octave 2 在敘事跟遊戲對白還是靠情感勝出", "body": "32 維情緒控制在生產環境裡無人能比，特別是聲音要傳達細膩情感的專案。有聲書製作人跟遊戲工作室任何把情感範圍當硬性需求的角色，預設應該就用 Hume。第二名鎖住。"},
    ],
)


# ============================================================
# best-air-purifiers
# ============================================================
add(
    "best-air-purifiers",
    refs=[
        {"title": "8 Best Air Purifiers of 2026 Consumer Reports", "url": "https://www.consumerreports.org/appliances/air-purifiers/best-air-purifiers-of-the-year-a1197763201/", "source": "Consumer Reports"},
        {"title": "IQAir air purifiers for wildfire smoke", "url": "https://www.iqair.com/us/air-purifiers-for-wildfire-smoke", "source": "IQAir"},
        {"title": "Memorial Day air purifier deals tracker", "url": "https://www.tomsguide.com/", "source": "Tom's Guide"},
    ],
    en_c="IQAir HealthPro Plus holds first going into Memorial Day week Day 2 and the wildfire-prep narrative is the dominant near-term driver. Western US fire-season forecasts firmed up further this Tuesday and HealthPro Plus is still the only consumer purifier with HyperHEPA media certified below 0.1 microns. Distributor restock signal points to the window narrowing as we approach Memorial Day weekend, which historically marks the start of serious wildfire-prep buying. First place locked in for urgent purchase. Coway Airmega 400S stays at second with the Consumer Reports 2026 best-overall designation, 350 CFM smoke CADR, CARB certification, and last week's firmware VOC tracking still a meaningful decision tiebreaker. Memorial Day discounts on the 400S are starting to surface across major US retailers and the price-to-performance math is the strongest in the category at the deal price. Blueair HealthProtect 7470i stays third and the broader Blueair lineup continues to pick up comparison coverage. Rabbit Air MinusA3, Coway Airmega Prox, IQAir Atem Earth, Levoit Core 600S, and Levoit Vital 200S are unchanged. Tuesday signal: the practical move for buyers who need a purifier before peak wildfire season is to lock in IQAir at full price now rather than wait for Memorial Day deals that traditionally do not apply to the medical-grade tier. For everyone else, wait through this week and pick up the Coway 400S or a Levoit at Saturday's deal pricing.",
    en_h=[
        {"title": "IQAir HealthPro Plus wildfire-prep window is closing into the weekend", "body": "Western US fire-season forecasts firmed up further this Tuesday and HealthPro Plus is still the only consumer purifier with HyperHEPA certified below 0.1 microns. Distributor restock signal points to the window narrowing into Memorial Day weekend. First place locked in for urgent purchase and IQAir traditionally does not discount the medical tier."},
        {"title": "Coway 400S Memorial Day deal pricing surfacing this week", "body": "Consumer Reports 2026 best-overall designation confirms 350 CFM smoke CADR, CARB certification, balanced noise and filter cost. Memorial Day discounts are starting to surface across major US retailers and the price-to-performance math is the strongest in the category at the deal price. Second place validated and the deal window is the right buying signal for mainstream households."},
        {"title": "Blueair lineup keeps gaining lower-cost large-space share", "body": "Blue Pure 211+ matching Coway 400S CADR at a lower price continues to pick up reviewer attention this week. HealthProtect 7470i benefits from the brand-level halo. Third place unchanged but the broader Blueair story is strengthening through summer."},
    ],
    zh_c="IQAir HealthPro Plus 進入陣亡將士紀念日週第二天還是守第一，野火季節準備是短期主導因素。美西火季預測這個禮拜二再次定調，HealthPro Plus 還是唯一通過認證能捕捉 0.1 微米以下超細微粒的家用清淨機。通路補貨訊號顯示窗口在陣亡將士紀念日週末前持續收窄，這個週末歷史上就是認真野火準備購買的起點。第一名鎖定急需採購。\n\nCoway Airmega 400S 守第二，Consumer Reports 2026 最佳整體（350 CFM 煙霧 CADR、CARB 認證、上禮拜的韌體 VOC 追蹤）還是有意義的決勝點。陣亡將士紀念日 400S 的折扣開始在美國主要通路浮現，折扣價的價格表現比是分類裡最強的。\n\nBlueair HealthProtect 7470i 守第三，整個 Blueair 產品線在比較報導裡持續加溫。Rabbit Air MinusA3、Coway Airmega Prox、IQAir Atem Earth、Levoit Core 600S、Levoit Vital 200S 都沒動。\n\n禮拜二的訊號：需要在野火季高峰前拿到清淨機的買家，務實做法是現在用原價鎖定 IQAir，不要等陣亡將士紀念日折扣，醫療等級這一檔歷史上不參與。其他人撐過這禮拜，週六去拿 Coway 400S 或 Levoit 折扣價。\n\n講真的，台灣這邊沒野火問題，但五月底沙塵跟梅雨前的空氣品質波動值得提早把機器準備好，下單邏輯也是同一套，急著用就買認證等級高的，預算優先就等折扣。",
    zh_h=[
        {"title": "IQAir HealthPro Plus 野火準備窗口在週末前收窄", "body": "美西火季預測禮拜二再次定調，HealthPro Plus 還是唯一通過認證能捕捉 0.1 微米以下超細微粒的家用清淨機。通路補貨訊號顯示窗口在陣亡將士紀念日週末前持續收窄。第一名鎖定急需採購，IQAir 醫療級這一檔歷史上不參與折扣。"},
        {"title": "Coway 400S 陣亡將士紀念日折扣這禮拜開始浮現", "body": "Consumer Reports 2026 最佳整體確認 350 CFM 煙霧 CADR、CARB 認證、噪音與濾網成本平衡。陣亡將士紀念日折扣開始在美國主要通路浮現，折扣價的價格表現比是分類裡最強的。第二名靠驗證表現鎖住，折扣窗口就是主流家庭的購買訊號。"},
        {"title": "Blueair 產品線持續吃低成本大空間份額", "body": "Blue Pure 211+ 以較低價格達到 Coway 400S 級別 CADR 這禮拜還在更多評測曝光。HealthProtect 7470i 吃到品牌光環。第三名不動，整個 Blueair 故事到夏天會持續加強。"},
    ],
)
