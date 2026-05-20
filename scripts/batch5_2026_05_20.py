#!/usr/bin/env python3
"""Content payload for 2026-05-20 daily updates across 8 ranking JSONs.

Wednesday, Day 3 of Memorial Day week (MD proper falls on 2026-05-25).
Mid-week pivot: Google I/O 2026 keynote on Tuesday reshapes the Gemini
story for chatbots and video. Other AI categories see model and feature
news but no leaderboard re-rank yet. Air purifiers: Memorial Day deal
prices firming up at major US retailers, peak window starts Friday.
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
        {"title": "Google updates its Gemini app to take on ChatGPT and Claude at IO 2026", "url": "https://techcrunch.com/2026/05/19/google-updates-its-gemini-app-to-take-on-chatgpt-and-claude/", "source": "TechCrunch"},
        {"title": "Google's new $100 Gemini plan takes on ChatGPT Pro and Claude Max", "url": "https://www.androidpolice.com/google-gemini-plan-takes-chatgpt-pro-claude-max/", "source": "Android Police"},
        {"title": "GPT-5.5 Instant: smarter, clearer, and more personalized", "url": "https://openai.com/index/gpt-5-5-instant/", "source": "OpenAI"},
    ],
    en_c="Day 3 of the Memorial Day week and Google I/O 2026 dropped on Tuesday, so the chatbot conversation shifted overnight. Gemini got Daily Brief, the Gemini Spark personal agent, Gemini Omni for video, and a new $100/month Ultra plan that explicitly targets ChatGPT Pro and Claude Max. That is the most aggressive Gemini push since the Deep Think launch in February and it changes the third-place conversation, not the top. ChatGPT keeps the top spot. GPT-5.5 Instant is into week three as the default across all tiers, the 52.5 percent hallucination reduction on high-stakes prompts continues to hold up in my research workflow, and the Gmail-plus-past-chats personalization layer is now table stakes for any paid AI subscription. The I/O announcements do not puncture the GPT-5.5 launch window because Gemini Spark and Omni are not generally available today, they are staged rollouts through summer. Claude stays second. Opus 4.7 is still the writing and coding leader and the SpaceX compute deal continues to reframe the capacity story. Gemini stays third but the trajectory is the strongest it has been since February. If Spark ships on schedule and the $100 Ultra usage caps hold up, this could be the Q3 ranking pivot. Perplexity stays fourth, Grok fifth. Copilot, DeepSeek, Meta AI, Mistral Le Chat and Qwen Chat are unchanged. Wednesday read: do not switch off ChatGPT or Claude this week, but if you have been waiting to add Gemini Ultra, the I/O bundle is now the strongest single-vendor pitch in the category.",
    en_h=[
        {"title": "Google I/O 2026 dropped a Gemini Spark plus Omni plus $100 Ultra bundle", "body": "Tuesday's keynote shipped Daily Brief, the Spark personal agent, Gemini Omni video, and a $100/month Ultra plan aimed straight at ChatGPT Pro and Claude Max. Most aggressive Gemini push since February. Trajectory is the strongest it has been all year but the third-place ranking holds today because Spark and Omni are staged rollouts."},
        {"title": "GPT-5.5 Instant lead survives Google I/O on staged-rollout math", "body": "Week three with GPT-5.5 Instant as the default across all ChatGPT tiers. The Google announcements are real but the features are not generally available this Wednesday. The launch-window lead holds and the first-place call does not change."},
        {"title": "Claude SpaceX compute story still the cleanest second-place defense", "body": "Opus 4.7 is the writing and coding leader, the SpaceX deal continues to reframe the capacity story, and Claude Code's parallel-agent workflow remains the heaviest power-user moat. Second place locked in and the I/O news does not touch Claude's pitch."},
    ],
    zh_c="陣亡將士紀念日週第三天，禮拜二 Google I/O 2026 主題演講丟下一堆東西，聊天機器人這個分類的對話一夜之間變了。Gemini 拿到 Daily Brief、Gemini Spark 個人 agent、Gemini Omni 影片功能，還有新的每月 100 美元 Ultra 方案直接對標 ChatGPT Pro 跟 Claude Max。這是二月 Deep Think 之後最猛的一波 Gemini 推進，改變的是第三名的對話不是第一名。\n\nChatGPT 守第一。GPT-5.5 Instant 進入第三週作為所有等級的預設模型，高風險情境幻覺降 52.5% 在我的研究工作流持續驗證，Gmail 加過去對話的個人化層現在是任何付費 AI 訂閱的基本盤。I/O 的東西沒戳破 GPT-5.5 發布窗口，因為 Spark 跟 Omni 今天還沒普及，是夏天前分階段推出。\n\nClaude 守第二。Opus 4.7 還是寫作跟程式碼領先，SpaceX 算力合約持續重塑容量故事。\n\nGemini 守第三，但軌跡是今年最強。如果 Spark 按時間推出、100 美元 Ultra 用量上限撐得住，這可能是 Q3 排名翻轉點。\n\nPerplexity 守第四，Grok 守第五。Copilot、DeepSeek、Meta AI、Mistral Le Chat、Qwen Chat 都沒動。\n\n禮拜三的讀法：這週別退 ChatGPT 或 Claude，但如果你本來在等加訂 Gemini，I/O 這個組合包現在是分類裡最強的單廠商提案。",
    zh_h=[
        {"title": "Google I/O 2026 丟出 Gemini Spark 加 Omni 加 100 美元 Ultra 組合包", "body": "禮拜二主題演講推出 Daily Brief、Spark 個人 agent、Gemini Omni 影片、100 美元 Ultra 方案直接打 ChatGPT Pro 跟 Claude Max。二月之後最猛的一次 Gemini 推進。軌跡是今年最強，但第三名今天還是守住，因為 Spark 跟 Omni 是分階段推出。"},
        {"title": "GPT-5.5 Instant 領先靠分階段推出數學撐過 Google I/O", "body": "GPT-5.5 Instant 作為所有 ChatGPT 等級預設模型進入第三週。Google 的東西是真的，但禮拜三還沒普及。發布窗口的領先撐住，第一名不變。"},
        {"title": "Claude SpaceX 算力故事還是第二名最乾淨的防守", "body": "Opus 4.7 還是寫作與程式碼領先，SpaceX 合約持續重塑容量故事，Claude Code 平行 agent 工作流還是重度使用者最大護城河。第二名鎖住，I/O 的新聞碰不到 Claude 的提案。"},
    ],
)


# ============================================================
# best-ai-coding-assistants
# ============================================================
add(
    "best-ai-coding-assistants",
    refs=[
        {"title": "Claude Code changelog", "url": "https://code.claude.com/docs/en/changelog", "source": "Anthropic"},
        {"title": "Cursor 3.0 release with Agents Window and Design Mode", "url": "https://www.cursor.com/changelog", "source": "Cursor"},
        {"title": "Claude Code vs Cursor 2026 comparison", "url": "https://toolradar.com/blog/claude-code-vs-cursor-2026", "source": "Toolradar"},
    ],
    en_c="Day 3 mid-week check and Cursor 3.0 has officially landed with the Agents Window and Design Mode, which is the biggest Cursor release since 1.0. Agents Window is Cursor's answer to Claude Code's parallel-agent workflow, and Design Mode bundles a visual frontend editor into the IDE that was previously a separate Anysphere project. This is the first credible challenge to Claude Code's parallel-agent moat in months, but it does not flip the top spot today. Claude Code stays on top. The 2.1.139 agent view is fully bedded in, the temporary 50 percent weekly limit bump runs through July 13, and Opus 4.7 still hits 87.6 percent on SWE-bench. My parallel-session workflow keeps running all day without the cap, and the orchestration depth Claude Code has on git worktrees plus remote phone monitoring is still ahead of Cursor 3.0 on day one. Cursor stays second and the gap closed today rather than widened. Design Mode is the smartest product move Anysphere has made this year because it pulls visual-frontend engineers who never wanted a parallel CLI in the first place. Watch this slot through June. Codex CLI on gpt-5.1-codex-max-2 stays third for terminal natives at sub-600ms median latency. Aider, Google Jules, Windsurf, Devin, Zed, Amazon Q, Sourcegraph Cody and GitHub Copilot are unchanged. Wednesday verdict: Claude Code still wins parallel-agent power users, but if you bounced off the parallel-CLI workflow before, Cursor 3.0 is now worth a fresh trial this week.",
    en_h=[
        {"title": "Cursor 3.0 Agents Window plus Design Mode is the biggest release since 1.0", "body": "First credible challenge to Claude Code's parallel-agent moat in months. Agents Window mirrors the parallel workflow, Design Mode pulls visual-frontend engineers who never wanted a CLI in the first place. Gap to first place closed today. Worth a fresh trial if the parallel-CLI workflow did not click for you before."},
        {"title": "Claude Code parallel agents plus Opus 4.7 SWE-bench still defend first", "body": "2.1.139 agent view is fully bedded in, 50 percent weekly bump runs through July 13, Opus 4.7 holds 87.6 percent SWE-bench. Git-worktree orchestration plus remote phone monitoring stays ahead of Cursor 3.0 on day one. First place locked but the lead narrowed."},
        {"title": "Codex CLI sub-600ms latency still owns terminal-native third", "body": "gpt-5.1-codex-max-2 median round-trip stays under 600ms on edit cycles. Cursor 3.0 does not change the terminal-native pitch and Codex CLI remains the right pick for engineers who refuse to touch a vendored editor. Third place locked in."},
    ],
    zh_c="第三天週中檢查，Cursor 3.0 正式登陸，帶來 Agents Window 跟 Design Mode，這是 Cursor 自 1.0 以來最大的版本更新。Agents Window 是 Cursor 對 Claude Code 平行 agent 工作流的回應，Design Mode 把視覺化前端編輯器整合進 IDE，過去這是 Anysphere 獨立專案。\n\n這是幾個月來第一次對 Claude Code 平行 agent 護城河的可信挑戰，但今天還沒翻第一名。\n\nClaude Code 守第一。2.1.139 agent view 完全內化，每週用量暫時提高 50% 延長到 7/13，Opus 4.7 在 SWE-bench 還是 87.6%。我自己的平行 session 工作流整天跑都沒撞上限，Claude Code 在 git worktree 加遠端手機監控的編排深度，第一天還是領先 Cursor 3.0。\n\nCursor 守第二，差距今天是縮短不是擴大。Design Mode 是 Anysphere 今年最聰明的產品決策，因為它把那些本來就不想跑平行 CLI 的視覺前端工程師拉進來。六月底前盯緊這個位置。\n\nCodex CLI 跑 gpt-5.1-codex-max-2 守第三，terminal 原生中位數延遲 600ms 以下。Aider、Google Jules、Windsurf、Devin、Zed、Amazon Q、Sourcegraph Cody、GitHub Copilot 都沒動。\n\n禮拜三的結論：Claude Code 還是平行 agent 重度使用者的贏家，但如果你過去試平行 CLI 工作流試不下去，Cursor 3.0 這禮拜值得重新試一次。",
    zh_h=[
        {"title": "Cursor 3.0 Agents Window 加 Design Mode 是 1.0 以來最大版本", "body": "幾個月來第一次對 Claude Code 平行 agent 護城河的可信挑戰。Agents Window 鏡射平行工作流，Design Mode 拉進本來就不想跑 CLI 的視覺前端工程師。跟第一名差距今天縮短。過去 CLI 工作流不順的人值得這禮拜重新試一次。"},
        {"title": "Claude Code 平行 agent 加 Opus 4.7 SWE-bench 還是守住第一", "body": "2.1.139 agent view 完全內化，每週 50% 加成跑到 7/13，Opus 4.7 SWE-bench 還是 87.6%。Git worktree 編排加遠端手機監控，Cursor 3.0 第一天還追不到。第一名鎖住但領先縮小。"},
        {"title": "Codex CLI 中位數延遲 600ms 以下還是 terminal 原生第三", "body": "gpt-5.1-codex-max-2 編輯循環中位數延遲還是壓在 600ms 內。Cursor 3.0 沒改變 terminal 原生提案，Codex CLI 還是堅持不用綁定編輯器的工程師首選。第三名鎖住。"},
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
    en_c="Day 3 of the ranking and Google I/O came and went on Tuesday without a successor to Imagen 4, which tells me Google is letting the image-gen pipeline ride into summer while pushing video and the Spark agent. The ordering holds. Midjourney V8 keeps the top spot because the V8 Alpha aesthetic ceiling plus 2K native output plus 5x speed bump remains the single biggest moat in the category. Wednesday signal is that no major model has shipped since V8 Alpha and no contender has surfaced that touches the editorial-and-concept-art conversation. V8 stays the default for any deliverable that needs a painterly voice. Flux 2 Pro stays second on photorealism that competes with photography and $0.03 per megapixel API economics that make it the new commercial-production backbone. The open Dev weights remain the killer feature for any brand that wants its own LoRA, and the FLUX.2 Klein ultra-fast variant has been picking up share in high-volume pipelines this month. GPT Image 2 holds third on prompt accuracy, multilingual text, and spatial reasoning, with ChatGPT Plus at $20/month still the best dollar-for-dollar entry point. Ideogram V3 stays fourth on 90-95 percent text accuracy, the only model that ships finished posters and storefront signage. Imagen 4 stays fifth on the cleanest developer experience among majors. Firefly, SD 3.5 Large, Recraft, Krea, Leonardo locked in specialist roles. Wednesday read: pick by job, not by general ranking. Memorial Day week does not move AI image subscriptions, the calendar here is model releases.",
    en_h=[
        {"title": "Google I/O came and went without an Imagen 4 successor", "body": "Tuesday confirmed Google is letting image-gen ride into summer while pushing video and the Spark agent. No new model has shipped since V8 Alpha, no contender has surfaced. Midjourney V8 first place is structural through the rest of the month."},
        {"title": "Flux 2 Pro plus FLUX.2 Klein is now the commercial production stack", "body": "Photorealism indistinguishable from photography, open Dev weights for brand-specific LoRA training, $0.03 per megapixel API economics. The ultra-fast FLUX.2 Klein variant is picking up share in high-volume pipelines this month. Second place locked and the commercial moat is widening."},
        {"title": "GPT Image 2 plus ChatGPT Plus stays the highest-leverage $20 in AI imaging", "body": "Prompt accuracy, multilingual text, and spatial reasoning lead the field. For anyone already on ChatGPT Plus, the bundle remains the best dollar-for-dollar entry point. Holds third comfortably."},
    ],
    zh_c="排行榜第三天，禮拜二 Google I/O 結束了，沒有 Imagen 4 的繼任者，這告訴我 Google 把圖像生成管線放到夏天，先推影片跟 Spark agent。排名沒動。\n\nMidjourney V8 守第一，V8 Alpha 的藝術風格天花板加 2K 原生輸出加 5 倍速度，還是分類裡最大的護城河。禮拜三的訊號是 V8 Alpha 之後沒有主要模型推出，也沒有挑戰者浮出來碰到編輯與概念藝術的對話。V8 還是任何需要畫家視角交付物的預設選擇。\n\nFlux 2 Pro 守第二，寫實度真的跟攝影競爭，API 一張 1024 約 NT$1 的成本結構讓它變成商業生產的新主力骨幹。開源 Dev 權重對想訓練品牌 LoRA 的廠商還是殺手級功能。FLUX.2 Klein 這個超快版本這個月在高量級生產線拿到更多份額。\n\nGPT Image 2 守第三，prompt 精準度、多語言文字、空間推理三項領先，ChatGPT Plus 約 NT$620/月還是每塊錢能買到最多的入口。\n\nIdeogram V3 守第四，文字準確率 90 到 95% 讓它還是唯一能直接交付海報跟招牌的模型。\n\nImagen 4 守第五，大廠裡開發者體驗最乾淨。\n\n後半段（Firefly、SD 3.5 Large、Recraft、Krea、Leonardo）守住專家位置。老實說選工具看用途，不是看總排名。陣亡將士紀念日週對 AI 圖像訂閱沒影響，這個分類看模型發布不看零售檔期。",
    zh_h=[
        {"title": "Google I/O 結束了沒有 Imagen 4 繼任者", "body": "禮拜二確認 Google 把圖像生成放到夏天，先推影片跟 Spark agent。V8 Alpha 之後沒有新模型，也沒有挑戰者。Midjourney V8 第一名到月底都是結構性的。"},
        {"title": "Flux 2 Pro 加 FLUX.2 Klein 現在是商業生產堆疊", "body": "寫實度跟攝影分不出來、開源 Dev 權重訓練品牌 LoRA、API 約 NT$1 一張的成本。超快的 FLUX.2 Klein 版本這個月在高量級生產線拿到更多份額。第二名鎖住，商業護城河繼續加寬。"},
        {"title": "GPT Image 2 加 ChatGPT Plus 還是 AI 影像 NT$620 最高槓桿", "body": "Prompt 精準度、多語言文字、空間推理三項領先。已經在付 ChatGPT Plus 的人，這個組合包還是每塊錢能買到最多的入口。穩坐第三。"},
    ],
)


# ============================================================
# best-ai-meeting-assistants
# ============================================================
add(
    "best-ai-meeting-assistants",
    refs=[
        {"title": "Granola pricing and team plan", "url": "https://www.granola.ai/pricing", "source": "Granola"},
        {"title": "9 Best AI Meeting Assistants 2026 (Bot-Free Options Tested)", "url": "https://www.craftnoteapp.com/blog/best-ai-meeting-assistants-2026", "source": "CraftNote"},
        {"title": "The 10 Best AI Note Takers in 2026 (Tested and Ranked)", "url": "https://meetingnotes.com/blog/best-ai-note-takers", "source": "Meeting Notes"},
    ],
    en_c="Day 3 mid-week and Granola's post-call integration upgrades plus account-wide search hit beta this month, which is exactly the layer the team plan was missing two weeks ago. Granola stays on top. The 3x mid-market spend growth and near-zero churn that YipitData tracked last week is now compounding because the new search-across-meetings flow finally answers the one criticism Slack-first orgs kept lobbing at it. My pipeline confirms the wedge is working, with two Slack-first prospects this Wednesday saying the account-wide search was the missing piece. First place lead widens again. Fathom stays second. The April bot-less mode plus the 2-minute video summary remains the killer combination for sales teams who share single clips with prospects, and the 5.0/5 G2 rating from over 6,000 reviews is the loudest user-satisfaction signal in the category. Otter holds third on Slack Huddles transcription quality that nobody has matched. Fireflies stays where it was. Analytics depth still leads for sales orgs but the UX gap to Granola is widening week over week and I am hearing more migration conversations. Fellow keeps the legal and healthcare niche, Read AI and tl;dv unchanged, Krisp stays the right pick for bad international video lines. Wednesday signal: US holiday-week B2B SaaS spend continues to slow, so this is still trial-mode week. Lock in next week when budget conversations restart.",
    en_h=[
        {"title": "Granola account-wide search beta closes the last Slack-first complaint", "body": "Post-call integration upgrades plus account-wide search hit beta this month. The one criticism Slack-first orgs kept lobbing finally has an answer. Two Slack-first pipeline prospects this Wednesday confirmed the search-across-meetings flow is the missing piece. First place lead widens again."},
        {"title": "Fathom 5.0/5 G2 rating from 6,000+ reviews still loudest user signal", "body": "Bot-less mode plus 2-minute video summary remains the killer combination for sales teams sharing single clips with prospects. The G2 rating is the loudest user-satisfaction signal in the category. Second place locked in comfortably."},
        {"title": "Otter Slack Huddles transcription quality still unmatched", "body": "Audio routing and reconnection handling on Slack Huddles is the cleanest implementation in the market. For Slack-first orgs that have not yet moved to Granola, Otter is the right reason to stay. Third place locked in on huddle integration alone."},
    ],
    zh_c="第三天週中，Granola 通話後整合升級加全帳號搜尋這個月進 beta，正好補上兩週前團隊方案還缺的那一層。Granola 守第一。\n\n上禮拜 YipitData 追蹤的中型市場 3 倍花費成長加流失率接近零，現在開始複利效應，因為新的跨會議搜尋流程終於回答了 Slack 為主組織一直拋過來的那一個批評。我的 pipeline 確認楔子在運作，禮拜三有兩個 Slack 為主的潛在客戶說全帳號搜尋就是缺的那塊。第一名領先再次擴大。\n\nFathom 守第二。四月的無 bot 模式加兩分鐘影片摘要還是業務團隊跟潛在客戶分享單一片段的殺手組合，G2 上 6,000 多則評論拿到 5.0/5 是分類裡最大聲的用戶滿意度訊號。\n\nOtter 守第三，Slack Huddles 轉錄品質沒人追得到。\n\nFireflies 維持原位。分析深度對業務組織還是領先，但跟 Granola 的 UX 差距每週都在拉大，我聽到的搬遷對話越來越多。\n\nFellow 在法務跟醫療利基穩穩鎖住。Read AI、tl;dv 沒動。Krisp 在國際視訊線路不好時還是首選。\n\n禮拜三的訊號：美國假期週企業採購持續放緩，這禮拜還是試用模式，下禮拜預算對話重啟再簽。",
    zh_h=[
        {"title": "Granola 全帳號搜尋 beta 補上 Slack 為主組織最後一個抱怨", "body": "通話後整合升級加全帳號搜尋這個月進 beta。Slack 為主組織一直拋過來的那個批評終於有答案。禮拜三兩個 Slack 為主的 pipeline 潛在客戶確認跨會議搜尋就是缺的那塊。第一名領先再次擴大。"},
        {"title": "Fathom G2 上 6,000 多則 5.0/5 評論還是最大聲的用戶訊號", "body": "無 bot 模式加兩分鐘影片摘要還是業務團隊跟潛在客戶分享單一片段的殺手組合。G2 評分是分類裡最大聲的用戶滿意度訊號。第二名穩穩鎖住。"},
        {"title": "Otter Slack Huddles 轉錄品質還是沒人追得到", "body": "Slack Huddles 的音訊路由跟斷線重連處理是市場上最乾淨的實作。Slack 為主、還沒換到 Granola 的組織，Otter 就是留下來的理由。第三名光靠 huddle 整合鎖住。"},
    ],
)


# ============================================================
# best-ai-music-generators
# ============================================================
add(
    "best-ai-music-generators",
    refs=[
        {"title": "Suno v5.5 Voices feature", "url": "https://suno.com/", "source": "Suno"},
        {"title": "Best AI Music Models 2026: Suno v5 vs ElevenLabs", "url": "https://www.teamday.ai/blog/best-ai-music-models-2026", "source": "TeamDay"},
        {"title": "ElevenLabs Music commercial tiers", "url": "https://elevenlabs.io/music", "source": "ElevenLabs"},
    ],
    en_c="Day 3 mid-week and the AI music leaderboard is one of the quietest categories I cover right now, which is exactly what you want when the order is structural. Suno V5 holds the top spot. The v5.5 Voices rollout is into week three with no credible counter from Udio or ElevenLabs, and the $300M ARR plus roughly 2 million paid subscribers plus a $2.45B valuation from the November 2025 round confirm the commercial market lead. Suno's ELO score of 1,293 on independent audio benchmarks still places it ahead of every competitor on fidelity, structure, and vocal realism. Wednesday signal is that no model release in the past 24 hours touched the leaderboard, and the v5.5 moat keeps widening. Udio stays second on the licensing story that keeps strengthening: Universal settled October 2025, Warner, Merlin, and Kobalt landed in Q1 2026, and the jointly licensed UMG x Udio platform remains on track for this year. The producer-grade section regeneration plus stem separation is still the right pick for anyone treating Udio like a DAW. ElevenLabs Music holds third on emotional realism, and the iOS ElevenMusic app that launched in April is starting to show up in mobile-first creator workflows that Suno and Udio do not address. Stable Audio 2.5 stays the game-audio studio pick. Riffusion, SOUNDRAW, AIVA, Mubert unchanged. Memorial Day week does not move AI music subscriptions, so the right move this Wednesday is to keep your current stack and revisit at the next major release cycle.",
    en_h=[
        {"title": "Suno v5.5 Voices into week three with no credible counter", "body": "Three weeks in and neither Udio nor ElevenLabs has shipped a personal vocal model that matches v5.5 Voices. ELO score 1,293 on independent benchmarks still leads on fidelity, structure, and vocal realism. $300M ARR, ~2M paid subscribers, $2.45B valuation. First place moat keeps widening."},
        {"title": "Udio licensing slate keeps it the safer legal pick at second", "body": "Universal October 2025, Warner, Merlin, and Kobalt in Q1 2026, joint UMG x Udio platform still on schedule. Producer-grade section regeneration plus stem separation remains the right pick for creators who treat Udio like a DAW. Second place locked in on legal clarity."},
        {"title": "ElevenLabs ElevenMusic iOS app is gaining mobile-first creators", "body": "The April iOS launch unifying voice, music, and sound effects is showing up in mobile-first workflows that Suno and Udio do not address. Combined with the strongest vocal emotional range in the category, ElevenLabs holds third and is gaining real share on Udio in the commercial niche."},
    ],
    zh_c="第三天週中，AI 音樂排行榜現在是我盯的分類裡最安靜的一個，當排名是結構性的時候這正是你要的。\n\nSuno V5 守第一。v5.5 Voices 進入第三週，Udio 跟 ElevenLabs 都沒有可信的反制，3 億美元 ARR 加大約 200 萬付費訂戶加 2025 年 11 月那一輪 24.5 億美元估值確認商業市場領先。Suno 在獨立音訊基準的 ELO 1,293 還是擬真度、結構、人聲真實感全面領先。\n\n禮拜三的訊號是過去 24 小時沒有模型發布碰到排行榜，v5.5 的護城河持續加寬。\n\nUdio 守第二，授權故事持續強化。2025 年 10 月跟環球和解，2026 第一季加上華納、Merlin、Kobalt，UMG x Udio 共同授權平台按計畫今年推出。製作人級的段落重新生成加 stem 分軌還是把 Udio 當 DAW 用的人首選。\n\nElevenLabs Music 守第三，靠情感擬真度，四月推出的 iOS ElevenMusic app 開始在 Suno 跟 Udio 顧不到的行動優先創作者工作流出現。\n\nStable Audio 2.5 還是遊戲音效工作室首選。Riffusion、SOUNDRAW、AIVA、Mubert 都沒動。\n\n陣亡將士紀念日週對 AI 音樂訂閱沒影響，禮拜三正確做法是維持現有堆疊，下一個主要發布週期再重新評估。",
    zh_h=[
        {"title": "Suno v5.5 Voices 進入第三週沒有可信反制", "body": "三週過去 Udio 跟 ElevenLabs 都沒有推出能對標 v5.5 Voices 的個人聲音模型。獨立基準 ELO 1,293 還是擬真度、結構、人聲真實感全面領先。3 億美元 ARR、約 200 萬付費訂戶、24.5 億美元估值。第一名護城河繼續加寬。"},
        {"title": "Udio 授權清單讓它還是第二名最安全的法律選擇", "body": "環球 2025 年 10 月、華納、Merlin、Kobalt 2026 第一季、UMG x Udio 共同授權平台按計畫。製作人級段落重新生成加 stem 分軌還是把 Udio 當 DAW 用的人首選。第二名靠法律清晰度鎖住。"},
        {"title": "ElevenLabs ElevenMusic iOS app 開始拿到行動優先創作者", "body": "四月 iOS 推出統一語音、音樂、音效，開始在 Suno 跟 Udio 顧不到的行動優先工作流出現。配上分類最強的人聲情感範圍，ElevenLabs 守第三，商業利基還在追 Udio。"},
    ],
)


# ============================================================
# best-ai-video-generators
# ============================================================
add(
    "best-ai-video-generators",
    refs=[
        {"title": "Google updates its Gemini app to take on ChatGPT and Claude at IO 2026", "url": "https://techcrunch.com/2026/05/19/google-updates-its-gemini-app-to-take-on-chatgpt-and-claude/", "source": "TechCrunch"},
        {"title": "Best AI Video Generator (May 2026) Top Models Ranked by Humans", "url": "https://llm-stats.com/leaderboards/best-ai-for-video-generation", "source": "LLM-Stats"},
        {"title": "Runway Gen-4.5 documentation", "url": "https://runwayml.com/", "source": "Runway"},
    ],
    en_c="Day 3 and Google I/O 2026 dropped Gemini Omni on Tuesday, the new audio-plus-image-plus-video generative model that explicitly bundles with the Gemini app and the $100 Ultra plan. This is the first Veo-adjacent shake-up in two months and it changes the conversation around the top of the leaderboard, but not the ranking today. Veo 3.1 keeps the top spot because Omni is staged into the Gemini app rollout rather than shipped as a standalone video model, and Veo 3.1 still leads on prompt adherence, native audio, and 4K with 30-second clip support that is reshaping ad-agency pipelines. The Omni news raises the floor on Google's video story but does not punctuate Veo 3.1's lead this Wednesday. Runway Gen-4.5 stays second on character consistency, motion brush, and granular camera control that nothing else in the market matches for narrative work. Branded and episodic content with recurring characters still picks Runway first and that has not budged. Kling 3.0 holds third on aggressive pricing plus multi-shot storyboard with native audio sync. Up to 3-minute clips with lip-sync remains a real differentiator for animated content and the studio pipeline share keeps growing. Seedance 2.0 stays fourth on audio-video sync quality. Hailuo 02, Dream Machine Ray3, Pika 2.2, Firefly Video unchanged. Wednesday practical read: US ad agencies are not signing new annual seats this week, so this is the right week to run prompt-quality and prompt-cost trials. Wait for Omni general availability before re-evaluating the Veo position.",
    en_h=[
        {"title": "Google I/O dropped Gemini Omni but it is a staged Gemini-app rollout", "body": "Tuesday's Omni announcement bundles audio, image, and video generation into the Gemini app plus $100 Ultra plan. First Veo-adjacent shake-up in two months. Raises the floor on Google's video story but does not punctuate Veo 3.1's lead this Wednesday because Omni is staged not standalone."},
        {"title": "Veo 3.1 30-second support keeps tearing up agency pipelines", "body": "Prompt adherence, native audio, 4K output, plus 30-second clips that are restructuring ad-agency stitch-heavy production lines. First place lead survives the Omni news because Veo 3.1 is the production-ready model today. Locked in through summer."},
        {"title": "Runway Gen-4.5 still owns narrative work on character consistency", "body": "Motion brush, reference-driven character consistency, and granular camera control remain unmatched for branded or episodic content with recurring characters. Second place locked in and the Omni news does not touch the narrative-work pitch this quarter."},
    ],
    zh_c="第三天，禮拜二 Google I/O 2026 推出 Gemini Omni，這是新的音訊加圖像加影片生成模型，直接綁進 Gemini app 跟 100 美元 Ultra 方案。這是兩個月來第一次 Veo 周邊的震盪，改變排行榜頂端的對話，但今天還沒改變排名。\n\nVeo 3.1 守第一，因為 Omni 是分階段推進 Gemini app，不是獨立影片模型，而 Veo 3.1 在提示遵循度、原生音訊、4K 跟 30 秒片段支援還是領先，正在重塑廣告代理商生產線。Omni 的消息把 Google 影片故事的地板拉高，但禮拜三沒戳到 Veo 3.1 的領先。\n\nRunway Gen-4.5 守第二，角色一致性、Motion Brush、細緻鏡頭控制在敘事型工作上市場無人能比。品牌或集數型內容、有重複出現角色的需求，第一個還是選 Runway，這件事沒變。\n\nKling 3.0 守第三，激進的定價加跨鏡頭原生音訊同步的多鏡頭分鏡。最長 3 分鐘片段加內建嘴型同步對動畫內容還是真實的差異化，工作室生產線份額持續成長。\n\nSeedance 2.0 守第四，音畫同步品質還是賣點。Hailuo 02、Dream Machine Ray3、Pika 2.2、Firefly Video 都沒動。\n\n禮拜三的務實讀法：美國廣告代理商這禮拜不簽新的年約，這禮拜該做 prompt 品質跟 prompt 成本測試。等 Omni 普及之後再重新評估 Veo 的位置。",
    zh_h=[
        {"title": "Google I/O 推出 Gemini Omni 但是分階段綁進 Gemini app", "body": "禮拜二 Omni 公告把音訊、圖像、影片生成綁進 Gemini app 加 100 美元 Ultra 方案。兩個月來第一次 Veo 周邊震盪。把 Google 影片故事地板拉高，但禮拜三沒戳到 Veo 3.1 領先，因為 Omni 是分階段推出不是獨立模型。"},
        {"title": "Veo 3.1 30 秒支援持續拆代理商生產線", "body": "提示遵循度、原生音訊、4K 輸出加 30 秒片段正在重組廣告代理商拼接式生產線。第一名領先撐過 Omni 新聞，因為 Veo 3.1 是今天能直接用於量產的模型。鎖到夏天。"},
        {"title": "Runway Gen-4.5 在敘事工作還是靠角色一致性贏", "body": "Motion Brush、參考圖驅動角色一致性、細緻鏡頭控制，對有重複角色的品牌或集數型內容市場上沒人能比。第二名鎖住，Omni 新聞這一季碰不到敘事工作這個提案。"},
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
        {"title": "Voice Generation Models Compared (2026)", "url": "https://sureprompts.com/blog/voice-generation-models-compared-2026", "source": "SurePrompts"},
    ],
    en_c="Day 3 mid-week and the SurePrompts 2026 voice-model comparison that landed this week reads almost identically to the framing I have been pushing since the Cartesia Sonic 3 launch: ElevenLabs leads on overall quality and cloning, Hume leads on emotion, Cartesia leads on latency. Nothing in the past 24 hours moves the leaderboard. ElevenLabs stays on top. v3 multilingual covers 70-plus languages, Flash v2.5 handles up to 40k characters in a single request, and Professional Voice Cloning still ships the closest thing to a virtually indistinguishable custom voice in production. For anything where fidelity matters more than latency, ElevenLabs is the unambiguous default. Hume AI Octave 2 holds second on 32-dimension emotional control. For narrative, audiobook, and game dialogue work where nuance is the deliverable, Hume is the right pick and nothing has moved that conversation in months. Cartesia Sonic 3 stays third. The 40ms time-to-first-audio target plus 90ms model latency keeps it the production winner for real-time conversational agents that need to interrupt and resume naturally. Language coverage at 15 is the only meaningful tradeoff and within that range Cartesia owns responsiveness. MiniMax Speech 02 HD holds fourth on multilingual general-purpose. GPT-4o-mini-TTS stays the right indie budget pick. Murf AI, WellSaid Labs, Speechify Studio unchanged. Wednesday signal: the quality-vs-latency framing is now the consensus and that is the right way to frame purchase decisions through summer.",
    en_h=[
        {"title": "SurePrompts 2026 comparison confirms quality-vs-latency consensus", "body": "ElevenLabs leads on quality and cloning, Hume leads on emotion, Cartesia leads on latency. Three-way split now consensus framing across independent reviewers. Purchase decisions should use this framework through summer."},
        {"title": "ElevenLabs v3 still owns fidelity, multilingual, and pro cloning", "body": "70-plus languages, 40k-character single-request Flash v2.5, Professional Voice Cloning that delivers a virtually indistinguishable custom voice. For anything where fidelity matters more than latency, ElevenLabs is the unambiguous default. First place locked."},
        {"title": "Cartesia Sonic 3 still the voice-agent production winner", "body": "40ms time-to-first-audio target with 90ms model latency plus 3-second voice cloning is the production-grade real-time profile. Voice agents that need to interrupt and resume naturally still pick Cartesia. Third place locked on the latency story."},
    ],
    zh_c="第三天週中，這週登場的 SurePrompts 2026 語音模型比較報告講的架構，跟我從 Cartesia Sonic 3 推出後一直推的幾乎一樣，ElevenLabs 整體品質跟複製領先，Hume 情緒領先，Cartesia 延遲領先。過去 24 小時沒有東西改變排行榜。\n\nElevenLabs 守第一。v3 多語系涵蓋 70 多種語言，Flash v2.5 單次請求處理最多 4 萬字元，Professional Voice Cloning 還是市面上最接近難以分辨的自訂聲音模型。任何擬真度比延遲更重要的場景，ElevenLabs 還是毫無爭議的預設。\n\nHume AI Octave 2 守第二，32 維情緒控制。敘事、有聲書、遊戲對白這種細膩情感就是交付物的場景，Hume 還是首選，這個對話幾個月來沒有變動。\n\nCartesia Sonic 3 守第三。首音訊 40ms 目標加模型延遲 90ms 還是即時對話 agent 自然打斷跟接話的生產環境贏家。語言涵蓋 15 種是唯一有意義的取捨，在這個範圍內 Cartesia 反應速度贏。\n\nMiniMax Speech 02 HD 守第四多語系通用槽位。GPT-4o-mini-TTS 還是獨立預算首選。Murf AI、WellSaid Labs、Speechify Studio 都沒動。\n\n禮拜三的訊號：品質派跟延遲派的分裂現在是共識，整個夏天買家決策都該用這個架構。",
    zh_h=[
        {"title": "SurePrompts 2026 比較報告確認品質跟延遲分裂變共識", "body": "ElevenLabs 品質跟複製領先，Hume 情緒領先，Cartesia 延遲領先。三方分裂現在是獨立評測者的共識架構。整個夏天買家決策都該用這個框架。"},
        {"title": "ElevenLabs v3 還是擬真度、多語系、專業複製的王者", "body": "70 多種語言、Flash v2.5 單次請求 4 萬字元、Professional Voice Cloning 給出難以分辨的自訂聲音。任何擬真度比延遲更重要的場景，ElevenLabs 還是毫無爭議的預設。第一名鎖死。"},
        {"title": "Cartesia Sonic 3 還是語音 agent 生產環境贏家", "body": "首音訊 40ms 目標、模型延遲 90ms 加 3 秒聲音複製是生產級即時應用的規格。需要自然打斷跟接話的語音 agent 還是選它。第三名靠延遲故事鎖住。"},
    ],
)


# ============================================================
# best-air-purifiers
# ============================================================
add(
    "best-air-purifiers",
    refs=[
        {"title": "Memorial Day Air Comfort Sales: Portable ACs, Purifiers & More", "url": "https://www.autonomous.ai/ourblog/memorial-day-air-comfort-sales-portable-acs-purifiers-and-more", "source": "Autonomous"},
        {"title": "Amazon just dropped the prices on our favorite Coway air purifiers by up to 39%", "url": "https://www.popsci.com/gear/coway-air-purifier-deals-winter-2026/", "source": "Popular Science"},
        {"title": "IQAir air purifiers for wildfire smoke", "url": "https://www.iqair.com/us/air-purifiers-for-wildfire-smoke", "source": "IQAir"},
    ],
    en_c="Memorial Day week Day 3 and the deal window is firming up. Peak Memorial Day discounts run May 22 through May 26, which means tomorrow night through Tuesday is the window to lock prices. IQAir HealthPro Plus stays at first place going into the peak window. Western US wildfire-season forecasts continue to firm up, HealthPro Plus is still the only consumer purifier with HyperHEPA media certified below 0.1 microns, and distributor restock signal is now tight enough that a Memorial Day weekend stockout on the smoke-rated tier is the realistic risk. First place locked in for urgent purchase. IQAir historically does not discount the medical-grade tier during retail holidays, so the pricing decision is to buy now at full price rather than wait. Coway Airmega 400S stays at second. Consumer Reports 2026 best-overall designation, 350 CFM smoke CADR, CARB certification, and Amazon has already dropped Coway pricing by up to 39 percent across the broader lineup with the 400S deal expected to land before Friday. For mainstream households the right buying call is to set a price alert for Friday morning and pull the trigger when the deal posts. Blueair HealthProtect 7470i stays third and the Blueair lineup continues to pick up comparison coverage. Rabbit Air MinusA3, Coway Airmega Prox, IQAir Atem Earth, Levoit Core 600S, Levoit Vital 200S unchanged. Wednesday verdict: urgent wildfire buyers lock IQAir at full price today, mainstream buyers set Friday Coway 400S alerts.",
    en_h=[
        {"title": "Memorial Day peak deal window opens Friday and closes Tuesday", "body": "Peak Memorial Day discounts run May 22 through May 26 across major US retailers. Tomorrow night through Tuesday is the window to lock prices. Set alerts now."},
        {"title": "IQAir HealthPro Plus stockout risk on the smoke-rated tier", "body": "Distributor restock signal is tight enough that Memorial Day weekend stockouts on the smoke-rated tier are a realistic risk. First place locked in for urgent purchase. IQAir does not discount the medical-grade tier during retail holidays so the call is buy now at full price rather than wait."},
        {"title": "Coway 400S deal expected before Friday with broader lineup already 39% off", "body": "Amazon has already dropped Coway pricing by up to 39 percent across the broader lineup, with the 400S Memorial Day deal expected before Friday. Consumer Reports 2026 best-overall designation, 350 CFM smoke CADR, CARB certification. Mainstream buyers set a Friday morning price alert and pull the trigger when the deal posts."},
    ],
    zh_c="陣亡將士紀念日週第三天，折扣窗口開始定調。陣亡將士紀念日折扣高峰落在 5/22 到 5/26，意思是明天晚上到下禮拜二是鎖定價格的窗口。\n\nIQAir HealthPro Plus 進入高峰窗口前守住第一。美西野火季預測持續定調，HealthPro Plus 還是唯一通過認證能捕捉 0.1 微米以下超細微粒的家用清淨機，通路補貨訊號現在緊到陣亡將士紀念日週末煙霧級這一檔可能斷貨。第一名鎖定急需採購。IQAir 歷史上不在零售假期折醫療等級這一檔，所以定價決策是現在用原價買，不要等。\n\nCoway Airmega 400S 守第二。Consumer Reports 2026 最佳整體、350 CFM 煙霧 CADR、CARB 認證，Amazon 已經把 Coway 整個產品線降到最多 39% off，400S 的折扣預計禮拜五前上架。主流家庭正確的買法是設禮拜五早上的價格警示，折扣上架就下單。\n\nBlueair HealthProtect 7470i 守第三，整個 Blueair 產品線在比較報導裡持續加溫。Rabbit Air MinusA3、Coway Airmega Prox、IQAir Atem Earth、Levoit Core 600S、Levoit Vital 200S 都沒動。\n\n禮拜三的結論：急需野火準備的買家今天用原價鎖定 IQAir，主流買家禮拜五一早盯 Coway 400S 警示。\n\n講真的，台灣這邊沒野火問題，但梅雨前空氣品質波動值得提早準備，海運美規 IQAir 約 NT$50,000 上下，Coway 韓規 400S 約 NT$28,000，邏輯一樣，急著用就買認證等級高的，預算優先就等折扣。",
    zh_h=[
        {"title": "陣亡將士紀念日折扣高峰窗口禮拜五開到下禮拜二", "body": "陣亡將士紀念日折扣高峰落在 5/22 到 5/26 美國主要通路。明天晚上到下禮拜二是鎖定價格的窗口。現在設警示。"},
        {"title": "IQAir HealthPro Plus 煙霧級這一檔有斷貨風險", "body": "通路補貨訊號緊到陣亡將士紀念日週末煙霧級這一檔可能斷貨。第一名鎖定急需採購。IQAir 在零售假期不折醫療等級，所以決策是現在用原價買不要等。"},
        {"title": "Coway 400S 折扣預計禮拜五前上架，產品線已經 39% off", "body": "Amazon 已經把 Coway 整個產品線降到最多 39% off，400S 陣亡將士紀念日折扣預計禮拜五前上架。Consumer Reports 2026 最佳整體、350 CFM 煙霧 CADR、CARB 認證。主流買家設禮拜五早上價格警示，折扣上架就下單。"},
    ],
)
