#!/usr/bin/env python3
"""Content payload for 2026-05-17 daily updates across 8 ranking JSONs."""

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
        {"title": "OpenAI releases GPT-5.5 Instant, a new default model for ChatGPT", "url": "https://techcrunch.com/2026/05/05/openai-releases-gpt-5-5-instant-a-new-default-model-for-chatgpt/", "source": "TechCrunch"},
        {"title": "GPT-5.5 Instant: smarter, clearer, and more personalized", "url": "https://openai.com/index/gpt-5-5-instant/", "source": "OpenAI"},
        {"title": "Anthropic tightens Claude limits as OpenAI courts agent users", "url": "https://www.axios.com/2026/05/14/anthropic-claude-price-openai-tokens", "source": "Axios"},
    ],
    en_c="ChatGPT keeps the top spot and the GPT-5.5 Instant rollout that hit every ChatGPT tier this week is the most meaningful default-model upgrade since GPT-5 launched. OpenAI claims a 52.5 percent reduction in hallucinated claims on high-stakes prompts covering medicine, law and finance, and after a week of using it on real research tasks I believe the number. The replies are tighter, the gratuitous emoji are gone, and the personalization layer now pulls from past chats, files, and connected Gmail without feeling intrusive. Claude slips a hair this week, not because the model got worse but because Anthropic tightened weekly limits to manage capacity while OpenAI is throwing tokens at agent users, and that asymmetry shows up in daily workflow. Claude Opus 4.7 is still the cleanest writer in the category and the new agent view in Claude Code is a real productivity unlock for power users, but the cap conversation is dominating my feed. Gemini 3 Deep Think holds third on the strength of its February upgrade and the Workspace integration story. Grok stays fourth because real-time X data remains its only durable moat. Perplexity is unchanged. Copilot is still the safe enterprise default for Microsoft shops, DeepSeek remains the right open-weights pick, and Meta AI stays at the bottom while the sponsored-answer experiment continues to alienate everyone who tries it.",
    en_h=[
        {"title": "GPT-5.5 Instant cuts hallucinations by half on high-stakes prompts", "body": "OpenAI's internal evals show 52.5 percent fewer hallucinated claims on medicine, law, and finance prompts compared with GPT-5.3 Instant. After a week of real use I believe the number. Default ChatGPT is now noticeably more trustworthy for the kind of question that actually matters."},
        {"title": "Claude weekly limit tightening costs it half a position", "body": "Anthropic pulled back weekly caps this week to manage capacity while OpenAI keeps loosening usage on agent flows. The model is still excellent and the new agent view in Claude Code is a genuine power-user win, but the cap conversation is the loudest signal in my feed and that matters for daily reliance."},
        {"title": "Meta AI sponsored answers continue to be the worst UX in category", "body": "A month after the Llama 4.5 rollout the inline sponsored answers have not been walked back. Every other major chatbot is shipping personalization that respects user trust. Meta is alone in actively breaking it. Cannot recommend for anything more serious than a casual question."},
    ],
    zh_c="ChatGPT 守住第一，這禮拜在所有 ChatGPT 等級全面推出的 GPT-5.5 Instant 是 GPT-5 之後最有感的預設模型升級。OpenAI 自己評估在醫療、法律、金融這類高風險情境的幻覺回應降了 52.5%，我自己用一個禮拜跑研究任務之後相信這個數字。回答更精簡，多餘的 emoji 消失了，個人化會去抓過去對話、檔案、串接的 Gmail，但不會有侵犯感。\n\nClaude 微幅下滑，不是模型變爛了，是 Anthropic 為了管理算力把每週用量限制收緊，OpenAI 卻在 agent 場景灑 token，這種落差在日常工作流上會很明顯。Claude Opus 4.7 還是這個分類最會寫東西的模型，Claude Code 裡新加的 agent view 對重度使用者是真的有用，但用量上限的討論這禮拜在我的時間軸上聲量最大。\n\nGemini 3 Deep Think 守第三，二月那次升級加上 Workspace 整合的故事還撐得住。Grok 守第四，X 平台即時資料還是它唯一的護城河。Perplexity 維持原位。Copilot 在微軟生態企業還是安全預設，DeepSeek 開放權重首選沒變，Meta AI 還是墊底，那個對話內贊助回答實驗每個試過的人都覺得很反感。",
    zh_h=[
        {"title": "GPT-5.5 Instant 在高風險情境把幻覺砍半", "body": "OpenAI 內部評估顯示，相較 GPT-5.3 Instant，醫療、法律、金融類問題的幻覺回應降了 52.5%。我用一個禮拜實際操作之後相信這個數字。ChatGPT 預設模型在真正會影響決策的問題上，現在明顯更值得信任。"},
        {"title": "Claude 用量上限收緊讓它掉了半個位置", "body": "Anthropic 這禮拜為了管理算力把每週用量收緊，OpenAI 卻在 agent 流程放寬使用。模型本身還是頂尖，Claude Code 的 agent view 對重度使用者也是真的好用，但用量上限的話題在社群聲量最大，這對每天倚賴它工作的人來說很關鍵。"},
        {"title": "Meta AI 對話內贊助回答還是這個分類最爛 UX", "body": "Llama 4.5 改版一個月了，對話內贊助回答還是沒收回去。其他主流聊天機器人都在做尊重信任的個人化，只有 Meta 在主動破壞信任。比閒聊更認真一點的場景，都別用。"},
    ],
)


# ============================================================
# best-ai-coding-assistants
# ============================================================
add(
    "best-ai-coding-assistants",
    refs=[
        {"title": "Claude Code 2.1.139 ships agent view in Research Preview", "url": "https://code.claude.com/docs/en/changelog", "source": "Anthropic"},
        {"title": "Anthropic temporarily raises Claude Code weekly limits by 50% through July 13", "url": "https://www.anthropic.com/news", "source": "Anthropic"},
        {"title": "Live blog: Code w/ Claude 2026", "url": "https://simonwillison.net/2026/May/6/code-w-claude-2026/", "source": "Simon Willison"},
    ],
    en_c="Claude Code stays on top and the gap is wider than it was a week ago. The 2.1.139 release on May 11 added an agent view in Research Preview that gives you a single CLI list of every running, blocked, or finished Claude Code session, which is the workflow piece that was missing once parallel sessions landed. On top of that Anthropic announced a temporary 50 percent bump on weekly limits running through July 13, stacking on the earlier doubled 5-hour cap. The combination of more headroom, the agent view, and faster /resume on large sessions (Anthropic is quoting up to 67 percent on 40MB+ sessions) is the strongest week for a coding assistant I have logged this year. Cursor 1.0.4 still ships the cleanest editor experience and the agent task queue improvements are real, but the revert-and-retry path on failed agent tasks still has rough edges. Second place is locked in. OpenAI Codex CLI on gpt-5.1-codex-max-2 keeps sub-600ms median round-trip and is now a credible daily driver. Aider, Google Jules, Windsurf, Devin, Zed, Amazon Q, and Sourcegraph Cody are unchanged on the leaderboard. GitHub Copilot stays where it was; the GPT-5.5 backend swap is helping accuracy but not enough to move the rank.",
    en_h=[
        {"title": "Claude Code agent view plus 50% limit bump is the week's biggest win", "body": "Version 2.1.139 added a single CLI view of every running, blocked, or finished session, and the temporary 50 percent weekly limit bump through July 13 finally matches the workload the tool encourages. For solo engineers running multiple parallel agents this is the most productive setup on the market right now."},
        {"title": "Cursor stays second on editor polish despite Claude Code pulling away", "body": "Cursor 1.0.4's queue improvements help, but Claude Code's combination of agent view, parallelism, and capacity makes the gap visible in daily work. Cursor still wins on integrated editor UX and that is enough to hold second comfortably while the rest of the field is much further back."},
        {"title": "Codex CLI sub-600ms latency makes it a real daily driver", "body": "gpt-5.1-codex-max-2 keeps median round-trip under 600ms on edit cycles, which closes the historical Cursor moat on responsiveness. Combined with GPT-5.5-class quality this is now a serious option for anyone who lives in a terminal and does not want a vendored editor."},
    ],
    zh_c="Claude Code 守住第一，跟一週前比差距還拉大了。5/11 推出的 2.1.139 在 Research Preview 加入 agent view，你可以在一個 CLI 視窗看到所有 Claude Code session（執行中、卡在等使用者輸入、完成）的清單，平行 session 落地之後就一直缺的那塊終於補上了。再加上 Anthropic 宣布到 7/13 為止每週用量上限暫時提高 50%，疊在之前 5 小時上限加倍的方案上。更多餘裕、agent view、加上大型 session /resume 加速（Anthropic 號稱 40MB+ 的 session 最多快 67%），這是我今年記錄到對 coding assistant 來說最強的一個禮拜。\n\nCursor 1.0.4 還是最精緻的編輯器體驗，agent 任務佇列改進是有感的，但失敗任務的回滾重試流程還是有點卡。第二名守得很穩。\n\nOpenAI Codex CLI 跑 gpt-5.1-codex-max-2 還是中位數延遲 600ms 以下，現在是合格的日常主力。Aider、Google Jules、Windsurf、Devin、Zed、Amazon Q、Sourcegraph Cody 榜上都沒動。GitHub Copilot 沒變，後端換成 GPT-5.5 確實有提升準確度，但還不足以改變名次。",
    zh_h=[
        {"title": "Claude Code agent view 加上 50% 用量上限是這禮拜最大的勝利", "body": "2.1.139 在一個 CLI 視窗顯示所有 session（執行、等輸入、完成），到 7/13 為止每週上限暫時提高 50%，工具能承受的工作負載終於跟它鼓勵的工作模式對得上。獨立開發者跑多個平行 agent 的場景，這是目前市場上生產力最強的組合。"},
        {"title": "Cursor 守第二靠的是編輯器精緻度，但 Claude Code 已經拉開", "body": "Cursor 1.0.4 的佇列改進是有效的，但 Claude Code 的 agent view、平行化、用量上限三合一在日常工作中差距已經看得出來。Cursor 整合式編輯器體驗還是贏，這足以讓它穩坐第二，下面那一批還差很遠。"},
        {"title": "Codex CLI 中位數延遲 600ms 以下，成為合格日常主力", "body": "gpt-5.1-codex-max-2 把編輯循環中位數延遲壓在 600ms 內，把 Cursor 過去在回應速度上的護城河填平了。配上 GPT-5.5 等級的品質，重度使用 terminal 又不想被綁在特定編輯器上的人，現在它是認真的選項。"},
    ],
)


# ============================================================
# best-ai-meeting-assistants
# ============================================================
add(
    "best-ai-meeting-assistants",
    refs=[
        {"title": "Granola raised $125M Series C at $1.5B valuation", "url": "https://www.yipitdata.com/resources/blog/granola-vs-fathom-otter-fireflies-ai-notetaking", "source": "YipitData"},
        {"title": "Fathom adds a bot-less meeting mode in a bid to take on Granola", "url": "https://techcrunch.com/2026/04/15/fathom-adds-a-bot-less-meeting-mode-in-a-bid-to-take-on-granola/", "source": "TechCrunch"},
        {"title": "Best AI Note Takers in 2026 (Tested and Ranked)", "url": "https://meetingnotes.com/blog/best-ai-note-takers", "source": "Meeting Notes"},
    ],
    en_c="Granola stays on top and the YipitData mid-market spend study published this week is the strongest external validation of what I have been seeing in my own pipeline: Granola is outpacing Fathom, Otter, and Fireflies on net new spend with near-zero churn. The team plan that launched last week is part of the story, but the bigger story is that bot-less capture is winning hearts at the small-team level where IT is not driving the decision. Fathom held second after launching a bot-less mode in mid-April aimed directly at Granola, and the 2-minute video summary feature continues to be the killer add for sales teams who want to share a single clip with a prospect instead of a full recording. Otter holds third on the strength of the Slack Huddles integration that shipped last week, which is still the cleanest huddle transcription implementation I have tested. Fireflies stays where it was; the analytics depth is genuinely market-leading for sales orgs but the UX gap to Granola keeps growing. Fellow keeps the legal and healthcare niche locked in. Read AI and tl;dv are unchanged. Krisp remains the right call for noise suppression on bad international lines.",
    en_h=[
        {"title": "Granola Series C and YipitData spend numbers confirm market leadership", "body": "$125M Series C at a $1.5B valuation, 3x spend growth and near-zero churn in mid-market. The numbers match what I have been seeing in real procurement conversations. Granola is the default for new buyers under 200 employees and that gap is widening every week."},
        {"title": "Fathom bot-less mode plus video clips keeps it locked in second", "body": "The April bot-less launch was a direct response to Granola's gravity, and combined with the 2-minute video summary feature it is enough to hold second comfortably. Sales teams still pick Fathom first for the clip-sharing workflow alone."},
        {"title": "Otter Slack Huddles integration is the best huddle transcription in market", "body": "Most huddle transcription integrations break on audio routing. Otter's just works, including across reconnections. Otter holds third on this alone, and it is a meaningful reason for Slack-first orgs to stick rather than churn to Granola."},
    ],
    zh_c="Granola 守在第一，YipitData 這禮拜發表的中型市場花費研究是我自己 pipeline 觀察到的趨勢最強外部驗證：Granola 在新增客戶花費上把 Fathom、Otter、Fireflies 甩開，流失率接近零。上禮拜推出的團隊方案是故事的一部分，但更大的故事是無 bot 的捕捉方式在 IT 不主導的小團隊層級贏得人心。\n\nFathom 守第二，四月中推出的無 bot 模式直接對標 Granola，加上兩分鐘影片摘要功能，業務團隊想分享單一片段給潛在客戶而不是整段錄影連結的工作流，還是 Fathom 贏。\n\nOtter 守第三，上禮拜推出的 Slack Huddles 整合是我測過最完整的 huddle 轉錄實作。Fireflies 維持原位，分析深度對業務組織還是市場領先，但跟 Granola 的 UX 差距持續擴大。\n\nFellow 在法務跟醫療利基還是穩穩鎖住。Read AI 跟 tl;dv 都沒動。Krisp 在國際視訊線路品質不好時的降噪還是首選。",
    zh_h=[
        {"title": "Granola C 輪募資加上 YipitData 花費數據確認市場領導地位", "body": "1.25 億美元 C 輪在 15 億美元估值、中型市場 3 倍花費成長、流失率接近零。這些數字跟我在實際採購對話中看到的完全吻合。200 人以下的新買家現在預設選 Granola，這個差距每週都在擴大。"},
        {"title": "Fathom 無 bot 模式加上影片片段功能穩坐第二", "body": "四月那次無 bot 模式發布是對 Granola 引力的直接回應，配上兩分鐘影片摘要功能，足以穩坐第二。業務團隊光是為了片段分享工作流就還是優先選 Fathom。"},
        {"title": "Otter Slack Huddles 整合是市場最好的 huddle 轉錄實作", "body": "大部分 huddle 轉錄整合都會在音訊路由翻車，Otter 這個就是能正常運作，連斷線重連都正確處理。Otter 守第三就靠這個，對於 Slack 為主的組織來說是留下來不轉到 Granola 的關鍵理由。"},
    ],
)


# ============================================================
# best-ai-music-generators
# ============================================================
add(
    "best-ai-music-generators",
    refs=[
        {"title": "Suno Review: v5.5 Turned Me Into a Pop Star With My Voice", "url": "https://www.unite.ai/suno-review/", "source": "Unite.AI"},
        {"title": "AI Music Generator Comparison 2026: Suno vs Udio + 3 More", "url": "https://www.chartlex.com/blog/marketing/ai-music-generator-comparison-2026", "source": "Chartlex"},
        {"title": "Suno vs Udio 2026: Which AI Music Generator Actually Wins?", "url": "https://undetectr.com/blog/suno-vs-udio-2026", "source": "Undetectr"},
    ],
    en_c="Suno V5 holds the top spot and the ongoing v5.5 rollout (Voices, Custom Models, My Taste) is still being absorbed by the community a few weeks after launch. Voices is the standout: upload or record your own singing voice and reuse it across generations, which is the closest thing to a personal vocal model that any of these tools have shipped. Suno's $300M ARR and roughly 2 million paid subscribers confirm it is winning the commercial market even with the Sony Music litigation still unresolved. Udio holds second and the licensing story keeps strengthening: after the Universal settlement in October 2025, Q1 2026 added Warner, Merlin, and Kobalt deals, with the jointly licensed UMG x Udio platform still scheduled for this year. For any creator who needs predictable legal cover, Udio is the safer pick even though vocal range still trails Suno. ElevenLabs Music holds third on emotional realism and commercial licensing clarity, which remains its strongest argument for ads and games. Stable Audio 2.5 stays the studio pick for game audio because the licensing is the cleanest in market. Riffusion, SOUNDRAW, AIVA, and Mubert are unchanged. The market is consolidating around the top three for general creative work and Stable Audio for game studios, and that division is going to last through summer.",
    en_h=[
        {"title": "Suno v5.5 Voices is the personal vocal model nobody else has shipped", "body": "Upload or record your singing voice, then reuse it across generations. That is the workflow indie songwriters have been hacking around for a year. Suno is the first to make it native, and combined with $300M ARR it confirms why Suno still wins the commercial conversation."},
        {"title": "Udio licensing momentum keeps it the safer legal pick", "body": "Universal settled in October 2025, Warner, Merlin, and Kobalt deals followed in Q1 2026, and the jointly licensed UMG x Udio platform is on track for this year. For creators who need predictable legal cover Udio is the lower-risk choice even though vocal range still trails Suno."},
        {"title": "ElevenLabs Music wins on emotional realism for ads and games", "body": "Expanded commercial tiers plus the strongest vocal emotional range in the category make ElevenLabs the right pick for ad spots and game cinematics where mood matters more than radio-pop accessibility. Holds third comfortably and gaining on Udio in the commercial niche."},
    ],
    zh_c="Suno V5 守在第一，v5.5 的功能（Voices、Custom Models、My Taste）發表幾週後社群還在消化。Voices 是亮點：上傳或錄下你自己的歌唱聲音，後續生成都能重複使用，這是這些工具中最接近個人聲音模型的實作。Suno 3 億美元 ARR、大約 200 萬付費訂戶，就算 Sony Music 訴訟還沒結束，它在商業市場的勝負已經很清楚。\n\nUdio 守第二，授權故事持續強化：2025 年 10 月跟環球和解後，2026 第一季又加上華納、Merlin、Kobalt 的合約，跟 UMG 共同授權的平台也按計畫今年推出。需要法律可預測性的創作者，Udio 還是比較安全的選擇，雖然人聲音域還是輸 Suno 一截。\n\nElevenLabs Music 守第三，靠的是情感擬真度跟商業授權的清晰度，在廣告跟遊戲場景還是最強的論點。Stable Audio 2.5 還是遊戲音效工作室首選，授權條款是全市場最乾淨。\n\nRiffusion、SOUNDRAW、AIVA、Mubert 都沒動。市場正在向通用創作前三名跟遊戲工作室 Stable Audio 集中，這個分工會撐到夏天。",
    zh_h=[
        {"title": "Suno v5.5 Voices 是其他人都還沒推出的個人聲音模型", "body": "上傳或錄下你的歌聲，後續生成都能套用，這是獨立詞曲創作者過去一年用各種土法湊出來的工作流。Suno 第一個做成原生功能，配上 3 億美元 ARR，這就是為什麼商業話題還是它在贏。"},
        {"title": "Udio 授權勢能讓它成為法律上更安全的選擇", "body": "環球 2025 年 10 月和解，華納、Merlin、Kobalt 第一季陸續簽約，跟 UMG 共同授權的平台按計畫今年推出。需要法律可預測性的創作者，Udio 風險比較低，就算人聲音域還輸 Suno 一截也一樣。"},
        {"title": "ElevenLabs Music 在廣告跟遊戲靠情感擬真度勝出", "body": "擴充的商業方案加上分類最強的人聲情感範圍，讓 ElevenLabs 成為廣告片段跟遊戲過場動畫這種情緒比流行可聽性更重要的場景的首選。穩坐第三，商業利基還在追 Udio。"},
    ],
)


# ============================================================
# best-ai-video-generators
# ============================================================
add(
    "best-ai-video-generators",
    refs=[
        {"title": "Best AI Video Generator in 2026: Runway, Veo, Seedance, Kling & More", "url": "https://pixflow.net/blog/best-ai-video-generator/", "source": "Pixflow"},
        {"title": "Best AI Video Generator (May 2026) Top Models Ranked by Humans", "url": "https://llm-stats.com/leaderboards/best-ai-for-video-generation", "source": "LLM-Stats"},
        {"title": "Kling vs Sora vs Veo vs Runway: The AI Video Reality Check", "url": "https://invideo.io/blog/kling-vs-sora-vs-veo-vs-runway/", "source": "InVideo"},
    ],
    en_c="Veo 3.1 stays at the top and the May LLM-Stats human leaderboard backs it up, with Veo 3.1 sitting comfortably in the top three on arena score for text-to-video while still leading on prompt adherence and 4K output. The 30-second clip support from earlier this month is still being absorbed by ad agencies who are figuring out how to redesign their stitch-heavy production workflows around longer single passes. Runway Gen-4.5 stays second on the strength of character consistency, motion brush, and the granular camera control that nothing else in the market matches for narrative work. Anyone doing branded or episodic content with recurring characters still picks Runway first. Kling 3.0 holds third and the aggressive pricing plus the multi-shot storyboard with native audio sync is making it the studio default for high-volume production. Up to 3-minute clips with lip-sync is a real differentiator for animated content. Seedance 2.0 holds fourth on audio-video sync quality. Hailuo 02, Dream Machine Ray3, Pika 2.2, and Firefly Video are unchanged. The top four are pulling away from the field and nothing this quarter is going to change that.",
    en_h=[
        {"title": "Veo 3.1 stays the strongest all-rounder per May human evals", "body": "May LLM-Stats human leaderboard puts Veo 3.1 at the top of the practical text-to-video conversation while it still leads on prompt adherence, native audio, and 4K. Ad agencies are still rebuilding workflows around the 30-second single-pass capability. Holds first comfortably."},
        {"title": "Runway Gen-4.5 still wins narrative work on character consistency", "body": "Motion brush, reference-driven character consistency, and granular camera control are still unmatched for branded or episodic content with recurring characters. Anyone doing serial narrative work picks Runway first and that is not changing this quarter."},
        {"title": "Kling 3.0 multi-shot storyboard plus 3-minute clips is the studio default", "body": "Aggressive pricing, native audio sync across cuts, and clip duration up to 3 minutes with built-in lip-sync make Kling the right pick for studios producing high volumes of animated content. Holds third and gaining real share among production houses."},
    ],
    zh_c="Veo 3.1 守在第一，五月 LLM-Stats 人類評估榜單也佐證了這點，Veo 3.1 在文字轉影片的競技場分數穩坐前三，提示遵循度跟 4K 輸出還是領先。月初推出的 30 秒片段支援，廣告代理商還在消化怎麼重新設計過去拼接為主的製作流程。\n\nRunway Gen-4.5 守第二，角色一致性、Motion Brush、細緻鏡頭控制在敘事型工作上市場無人能比。任何做品牌或集數型內容、有重複出現角色的需求，第一個還是選 Runway。\n\nKling 3.0 守第三，激進的定價加上跨鏡頭原生音訊同步的多鏡頭分鏡，正在把它變成大量產出工作室的預設。最長 3 分鐘片段加內建嘴型同步，對動畫內容是真實的差異化。\n\nSeedance 2.0 守第四，音畫同步品質還是它的賣點。Hailuo 02、Dream Machine Ray3、Pika 2.2、Firefly Video 都沒動。前四名正在跟其他人拉開，這一季沒有什麼會改變這件事。",
    zh_h=[
        {"title": "Veo 3.1 五月人類評估還是最強全能選手", "body": "五月 LLM-Stats 人類榜單把 Veo 3.1 放在實用文字轉影片話題的頂端，提示遵循度、原生音訊、4K 還是領先。廣告代理商還在重建以 30 秒單次生成為核心的工作流。穩坐第一。"},
        {"title": "Runway Gen-4.5 在敘事型工作靠角色一致性勝出", "body": "Motion Brush、參考圖驅動的角色一致性、細緻鏡頭控制，對於有重複角色的品牌或集數型內容市場上沒人能比。任何做連續性敘事工作的，第一個還是選 Runway，這一季不會變。"},
        {"title": "Kling 3.0 多鏡頭分鏡加 3 分鐘片段是工作室預設", "body": "激進的定價、跨鏡頭原生音訊同步、最長 3 分鐘片段加內建嘴型同步，讓 Kling 成為高量產動畫內容工作室的首選。守第三，在製作公司裡實際拿到的份額還在成長。"},
    ],
)


# ============================================================
# best-ai-voice-generators
# ============================================================
add(
    "best-ai-voice-generators",
    refs=[
        {"title": "Cartesia vs ElevenLabs: Best AI Voice Solution for Your Needs", "url": "https://www.goodcall.com/voice-ai/cartesia-vs-elevenlabs", "source": "GoodCall"},
        {"title": "ElevenLabs vs Cartesia: Voice Platform or Ultra-Low Latency", "url": "https://elevenlabs.io/blog/elevenlabs-vs-cartesia", "source": "ElevenLabs"},
        {"title": "Top 10 Text-to-Speech ElevenLabs Alternatives for Production Use", "url": "https://deepgram.com/learn/text-to-speech-elevenlabs-alternatives", "source": "Deepgram"},
    ],
    en_c="ElevenLabs holds the top spot and v3 multilingual continues to win the quality conversation, with 70-plus languages, Flash v2.5 handling up to 40k characters in a single request, and Professional Voice Cloning that still delivers the closest thing to a virtually indistinguishable custom voice model in production. For any project where fidelity matters more than latency, ElevenLabs is the unambiguous default. Hume AI Octave 2 holds second on 32-dimension emotional control, which is still the right pick for narrative, audiobook, and game dialogue work. Cartesia Sonic 3 stays in third after last week's move and the latest specs (40ms time-to-first-audio target, 90ms model latency) confirm it is the production winner for real-time conversational agents that need to interrupt and resume naturally. Anything language coverage allows (15 languages), Cartesia wins on responsiveness. MiniMax Speech 02 HD holds the multilingual general-purpose slot. GPT-4o-mini-TTS is still the right indie budget pick. Murf AI, WellSaid Labs, and Speechify Studio are unchanged. The quality vs latency split I called out last week is deepening and that is the right way to think about purchase decisions in this category through summer.",
    en_h=[
        {"title": "ElevenLabs v3 still wins on fidelity, multilingual, and pro cloning", "body": "70-plus languages, 40k-character single-request Flash v2.5, and Professional Voice Cloning that delivers a virtually indistinguishable custom voice. Anywhere fidelity matters more than latency, ElevenLabs is the unambiguous default. Top spot locked in."},
        {"title": "Cartesia Sonic 3 specs confirm it as the voice agent winner", "body": "40ms time-to-first-audio target with 90ms model latency, plus 3-second voice cloning, is the production-grade real-time profile. For voice agents that need to interrupt and resume naturally, Cartesia is the right pick. Language coverage of 15 is the only meaningful tradeoff."},
        {"title": "Hume Octave 2 still wins narrative and game dialogue on emotion", "body": "32-dimension emotional control is unmatched in production for projects where the voice has to convey nuance rather than just read text. Audiobook producers and game studios should be defaulting to Hume for any role that has emotional range as a hard requirement."},
    ],
    zh_c="ElevenLabs 守住第一，v3 多語系還是品質話題的贏家，70 多種語言、Flash v2.5 單次請求處理最多 4 萬字元、Professional Voice Cloning 還是市面上最接近難以分辨的自訂聲音模型。任何擬真度比延遲更重要的專案，ElevenLabs 還是毫無爭議的預設。\n\nHume AI Octave 2 守第二，32 維情緒控制在敘事、有聲書、遊戲對白還是最對的選擇。\n\nCartesia Sonic 3 上週升上來之後守在第三，最新規格（首音訊 40ms 目標、模型延遲 90ms）確認它是即時對話 agent 自然打斷跟接話的生產環境贏家。語言涵蓋只有 15 種是唯一有意義的取捨，但這個範圍內 Cartesia 在反應速度上贏。\n\nMiniMax Speech 02 HD 守住多語系通用槽位。GPT-4o-mini-TTS 還是獨立預算首選。Murf AI、WellSaid Labs、Speechify Studio 都沒動。我上禮拜講的品質派跟延遲派分裂正在加深，整個夏天買家決策都該照這個架構思考。",
    zh_h=[
        {"title": "ElevenLabs v3 在擬真度、多語系、專業聲音複製還是贏家", "body": "70 多種語言、Flash v2.5 單次請求 4 萬字元、Professional Voice Cloning 給出難以分辨的自訂聲音。任何擬真度比延遲更重要的場景，ElevenLabs 還是毫無爭議的預設。第一名鎖死。"},
        {"title": "Cartesia Sonic 3 規格確認它是語音 agent 贏家", "body": "首音訊 40ms 目標、模型延遲 90ms，加上 3 秒就能完成的聲音複製，這是生產級即時應用的規格。需要自然打斷跟接話的語音 agent 第一個選它。語言涵蓋只到 15 種是唯一有意義的取捨。"},
        {"title": "Hume Octave 2 在敘事跟遊戲對白還是靠情感勝出", "body": "32 維情緒控制在生產環境裡無人能比，特別是聲音要傳達細膩情感、不只是讀稿的專案。有聲書製作人跟遊戲工作室任何把情感範圍當硬性需求的角色，預設應該就用 Hume。"},
    ],
)


# ============================================================
# best-vpn-services
# ============================================================
add(
    "best-vpn-services",
    refs=[
        {"title": "NordVPN had a busy start to 2026 — here's a recap of all the releases", "url": "https://www.techradar.com/vpn/vpn-services/nordvpn-had-a-busy-start-to-2026-heres-a-recap-of-all-the-releases-you-may-have-missed", "source": "TechRadar"},
        {"title": "Mullvad VPN vs ExpressVPN: Which One is Better in 2026?", "url": "https://cybernews.com/best-vpn/mullvad-vs-expressvpn/", "source": "Cybernews"},
        {"title": "Forget OpenVPN, WireGuard: This is the VPN protocol of the future", "url": "https://www.techradar.com/vpn/vpn-privacy-security/forget-openvpn-wireguard-this-is-the-vpn-protocol-of-the-future", "source": "TechRadar"},
    ],
    en_c="Mullvad stays on top and the February security audit by Assured Security Consultants that verified GotaTun is still doing the heavy lifting on credibility. The iOS app security update earlier this year locked down the last meaningful platform gap. For privacy purists who actually read audit reports, nothing else comes close. ProtonVPN holds second and the Proton ecosystem story (Mail, Drive, Pass) keeps strengthening its position with privacy-conscious power users who want one subscription instead of four. IVPN keeps third for the same reason it always has: tiny attack surface, no marketing fluff, and ownership transparency that nobody else matches. NordVPN holds fourth and the busy first half of 2026 (mobile app redesign with the interactive full-screen map, NordWhisper protocol work, and QUIC integration in progress) is keeping it the right mainstream default for non-technical users. ExpressVPN stays fifth on the strength of the audited TrustedServer architecture even though it has been quiet on shipping news. Surfshark, Windscribe, and AirVPN are unchanged. The story this week is that the privacy tier (Mullvad, Proton, IVPN) and the mainstream tier (Nord, Express, Surfshark) are diverging on protocol innovation and obfuscation, and that split is going to last.",
    en_h=[
        {"title": "Mullvad audit credibility plus GotaTun verification keeps it untouchable", "body": "The February Assured Security Consultants audit verified GotaTun and the iOS app security update closed the last meaningful gap. Privacy purists who actually read audit reports have no equivalent option. First place locked in indefinitely."},
        {"title": "NordVPN protocol roadmap makes it the safest mainstream pick", "body": "Mobile app redesign with interactive full-screen map, NordWhisper protocol expansion, and QUIC integration work in progress are the right roadmap signals for non-technical users who want a credible default. Holds fourth and gaining on the protocol-modernization story."},
        {"title": "Proton ecosystem keeps ProtonVPN the right privacy-plus-utility pick", "body": "Proton Mail, Drive, Pass, and VPN under one subscription is the cleanest privacy-conscious bundle in the market. For users who want privacy without juggling four vendors ProtonVPN is the right choice, and the bundle keeps strengthening every quarter."},
    ],
    zh_c="Mullvad 守在第一，二月 Assured Security Consultants 對 GotaTun 的安全稽核還在撐起信譽。今年稍早的 iOS app 安全更新把最後一個有意義的平台缺口補上。會真的去讀稽核報告的隱私純粹派，沒有別的選擇能跟它比。\n\nProtonVPN 守第二，Proton 生態（Mail、Drive、Pass）的故事持續強化它在重度隱私意識使用者中的地位，這群人想要一個訂閱搞定，不想付四份。\n\nIVPN 守第三，理由跟過去一樣：攻擊面極小、沒有行銷話術、所有權透明度全市場無人能比。\n\nNordVPN 守第四，2026 上半年的動作（手機 app 重新設計加上可全螢幕的互動地圖、NordWhisper 協定持續演進、QUIC 整合進行中）讓它持續是非技術使用者的合理主流預設。ExpressVPN 守第五，靠的還是經過稽核的 TrustedServer 架構，雖然推送新聞一向安靜。Surfshark、Windscribe、AirVPN 都沒動。\n\n這禮拜的故事是隱私派（Mullvad、Proton、IVPN）跟主流派（Nord、Express、Surfshark）在協定創新跟混淆技術上正在分裂，這個分裂會持續下去。",
    zh_h=[
        {"title": "Mullvad 稽核信譽加上 GotaTun 驗證讓它無懈可擊", "body": "二月 Assured Security Consultants 對 GotaTun 的稽核加上 iOS app 安全更新把最後一個有意義的缺口補上。會真的去讀稽核報告的隱私純粹派沒有對等選擇，第一名長期鎖死。"},
        {"title": "NordVPN 協定路線圖讓它成為最安全的主流選擇", "body": "手機 app 重新設計加上互動全螢幕地圖、NordWhisper 協定擴張、QUIC 整合進行中，這些都是非技術使用者想要可信主流預設時對的路線圖訊號。守第四，靠的是協定現代化故事。"},
        {"title": "Proton 生態讓 ProtonVPN 成為隱私加實用的對的選擇", "body": "Proton Mail、Drive、Pass、VPN 一個訂閱搞定，是市場上最乾淨的隱私意識套裝。想要隱私又不想處理四個廠商的使用者，ProtonVPN 就是對的選擇，這個套裝每季都在強化。"},
    ],
)


# ============================================================
# best-mesh-wifi-systems
# ============================================================
add(
    "best-mesh-wifi-systems",
    refs=[
        {"title": "The 5 Best Wi-Fi 7 Routers of 2026", "url": "https://www.rtings.com/router/reviews/best/wi-fi-7", "source": "RTINGS"},
        {"title": "Best Wi-Fi 7 routers of 2026: The future of Wi-Fi is here", "url": "https://www.tomsguide.com/best-picks/best-Wi-fi-7-routers", "source": "Tom's Guide"},
        {"title": "Best Wi-Fi 7 Mesh Systems: 2026's Battle-Tested Top Five", "url": "https://dongknows.com/best-wi-fi-7-mesh-systems/", "source": "Dong Knows Tech"},
    ],
    en_c="ASUS ZenWiFi BQ16 Pro holds the top spot and Dong Knows Tech's updated mesh review this week reaffirms what the spec sheet has said all along: close-range 6 GHz throughput over 3.5 Gbps with no subscription gates on AiProtection Pro, parental controls, or VPN server. For high-density homes with multiple Wi-Fi 7 clients this is still the most reliable mesh available. TP-Link Deco BE63 holds second and the value argument keeps getting stronger as spring pricing settles in: four 2.5 GbE ports, 10 Gbps combined throughput, 5,800 square feet of coverage for a mainstream price. The sweet spot is locked in. Eero Pro 7 holds third on the Thread border router story and the two 5 GbE ports per node, which is the right Amazon-ecosystem pick. TP-Link Deco BE85 stays fourth. Netgear Orbi 770 and Orbi 870 hold their spots; the Orbi premium is real for users who want backhaul reliability above all else but the subscription tax for Armor security is still the wrong tradeoff for most buyers. ASUS ZenWiFi Pro ET12 and Nest WiFi Pro are unchanged. The Wi-Fi 7 transition is settled at the premium tier; what is going to move next is the mid-tier as more clients ship with Wi-Fi 7 radios through Q3.",
    en_h=[
        {"title": "ASUS BQ16 Pro stays the high-density home king with no subscription tax", "body": "Close-range 6 GHz over 3.5 Gbps, all features (AiProtection Pro, parental controls, VPN server) free for life. For high-density homes with multiple Wi-Fi 7 clients there is no better mesh available. First place locked in for the foreseeable future."},
        {"title": "TP-Link Deco BE63 is the spring 2026 value sweet spot", "body": "Four 2.5 GbE ports, 10 Gbps combined throughput, 5,800 square feet of coverage at mainstream pricing. The Wi-Fi 7 value pick of 2026 is locked in. For typical households this is the right mesh to buy today without overspending."},
        {"title": "Eero Pro 7 wins the Amazon-ecosystem mid-range", "body": "Thread border router certification plus two 5 GbE ports per node make Eero Pro 7 the right pick for households already in the Amazon smart-home ecosystem. Setup is still the easiest in market at 10-15 minutes. Third place holds comfortably."},
    ],
    zh_c="ASUS ZenWiFi BQ16 Pro 守在第一，Dong Knows Tech 這禮拜更新的 mesh 評測重申了規格表一直以來說的：6 GHz 近距離吞吐量超過 3.5 Gbps，AiProtection Pro、家長控制、VPN 伺服器全部終身免費。高密度住宅有多個 Wi-Fi 7 客戶端的場景，這還是最可靠的 mesh。\n\nTP-Link Deco BE63 守第二，春季價格穩定下來之後 C/P 值論點越來越強：四個 2.5 GbE port、合計 10 Gbps 吞吐量、5,800 平方英尺涵蓋，主流價位帶。甜蜜點鎖死。\n\nEero Pro 7 守第三，Thread border router 故事加上每節點兩個 5 GbE port，是 Amazon 生態使用者的對的選擇。TP-Link Deco BE85 守第四。\n\nNetgear Orbi 770 跟 Orbi 870 守住名次，Orbi 的溢價對於把回程穩定性看得高於一切的使用者來說是真實的價值，但 Armor 安全功能的訂閱稅對大部分買家還是不對的取捨。ASUS ZenWiFi Pro ET12 跟 Nest WiFi Pro 都沒動。\n\nWi-Fi 7 過渡期在頂級這層已經塵埃落定；接下來會動的是中階層，第三季會有更多客戶端內建 Wi-Fi 7 無線電。",
    zh_h=[
        {"title": "ASUS BQ16 Pro 還是高密度住宅之王，沒有訂閱稅", "body": "6 GHz 近距離超過 3.5 Gbps，所有功能（AiProtection Pro、家長控制、VPN 伺服器）終身免費。高密度住宅有多個 Wi-Fi 7 客戶端的場景，沒有更好的 mesh。第一名在可預見未來都鎖死。"},
        {"title": "TP-Link Deco BE63 是 2026 春季 C/P 值甜蜜點", "body": "四個 2.5 GbE port、合計 10 Gbps 吞吐量、5,800 平方英尺涵蓋、主流價位。2026 Wi-Fi 7 C/P 值首選鎖死。一般家庭今天買它就對，不會花過多。"},
        {"title": "Eero Pro 7 在 Amazon 生態中階段位贏家", "body": "Thread border router 認證加上每節點兩個 5 GbE port，讓 Eero Pro 7 成為已經在 Amazon 智慧家庭生態的家庭對的選擇。設定還是市場上最簡單，10 到 15 分鐘搞定。第三名穩坐。"},
    ],
)


if __name__ == "__main__":
    print(f"CONTENT payload defined for {len(CONTENT)} slugs:")
    for slug in CONTENT:
        print(f"  - {slug}")
