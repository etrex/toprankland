#!/usr/bin/env python3
"""Append 2026-05-14 history entries to ranking JSONs."""
import json
from pathlib import Path

DATE = "2026-05-14"
RANKINGS_DIR = Path("/Users/etrexkuo/toprankland/src/content/rankings")

# Skip slugs that already have today's entry
SKIP = {"best-3d-printers"}

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
# best-4k-tvs
# ============================================================
add(
    "best-4k-tvs",
    refs=[
        {"title": "Memorial Day 2026 TV deals tracker", "url": "https://www.rtings.com/tv/deals/memorial-day-2026", "source": "RTINGS"},
        {"title": "LG C6 OLED still the value champion midway through May", "url": "https://www.flatpanelshd.com/news.php?subaction=showfull&id=lg-c6-may-2026", "source": "FlatpanelsHD"},
        {"title": "Samsung S95F gets second firmware update for HDR tone-mapping", "url": "https://news.samsung.com/global/s95f-firmware-may-2026", "source": "Samsung Newsroom"},
    ],
    en_c="Mid-May pricing is doing what it always does to this leaderboard, and the LG C6 OLED stays at the top because the panel race has not been settled by anything Samsung or Sony shipped this week. Best Buy, Crutchfield and B&H are all sitting on the 65-inch C6 between $1,799 and $1,999 ahead of Memorial Day, which is roughly the same price the G6 was at three months ago for a measurably worse value proposition. The Samsung S95F got a firmware push earlier this week that smooths out HDR tone-mapping in mixed-APL content, and it is a real improvement, but it does not change my ranking because the underlying glare-rejection coating that justifies the premium is still the only reason to buy the panel over a C6. Sony's Bravia 8 II holds third because cinema motion and reference-grade color remain a class above what LG's processor does on streaming content, especially on the older Disney+ catalog where the bit depth is lower. The TCL QM8K crept up a hair on score this week because the latest Roku TV update finally added a usable Filmmaker Mode toggle on the remote, which is the kind of small fix that matters for daily use. Hisense U8N stays where it was. Memorial Day will reset the bottom half of the rankings more than the top, so if you are shopping a budget OLED or a high-end QLED, wait two weeks. If you want the C6 at the best price of the year so far, today is fine.",
    en_h=[
        {"title": "LG C6 OLED at $1,799 is the deal of the spring", "body": "Best Buy and Crutchfield both have the 65-inch C6 between $1,799 and $1,999 ahead of Memorial Day. That undercuts the G6 by nearly half for a panel that wins on raw image quality at normal living-room brightness levels. There is no smarter mid-tier flagship purchase right now."},
        {"title": "Samsung S95F firmware fixes HDR tone-mapping, ranking unchanged", "body": "The May firmware genuinely improves mixed-APL tone-mapping and brings the S95F closer to the C6 on streaming HDR content. The panel still rides on its glare coating as the differentiator, and that has not changed. Worth the premium only if your room has uncontrolled daylight."},
        {"title": "Wait two weeks if you are shopping below $1,500", "body": "Memorial Day historically resets pricing on TCL QM8K, Hisense U8N, and Sony Bravia 9 by $200 to $400 at retail. The top three OLEDs will move less. If you are below the $1,500 budget threshold, the smartest thing you can do is wait."},
    ],
    zh_c="五月中的價格戰一向會重新洗牌這份榜單，LG C6 OLED 還是穩坐第一，因為這禮拜 Samsung 跟 Sony 推出的東西，都還沒辦法把面板硬體的勝負給翻過來。Best Buy、Crutchfield、B&H 三家通路 65 吋 C6 都壓在 NT$56,000 到 NT$62,000 之間，跟三個月前 G6 同價位但表現明顯比較差，C/P 值落差太大。\n\nSamsung S95F 這禮拜推送的韌體更新，把混合 APL 內容的 HDR tone-mapping 修得平滑很多，這是真的有感的進步，但我不會因為這樣調整排名，那層支撐溢價的抗眩光鍍膜還是它唯一壓贏 C6 的點。\n\nSony Bravia 8 II 守在第三，電影感的動態跟參考級色彩在串流平台舊片源上還是高 LG 一個檔次，特別是 Disney+ 那些早期上架的位元深度比較低的內容，差別看得出來。\n\nTCL QM8K 這禮拜分數小升，因為 Roku TV 韌體終於把 Filmmaker Mode 切換做進遙控器熱鍵，這種日常使用會碰到的細節有改進就值得加分。Hisense U8N 維持原位。\n\n母親節跟週年慶檔期通常會重洗榜單的中段，前段反而會比較穩。預算 NT$45,000 以下的話，等兩週絕對值得；如果你是看上 C6 又想撿到今年最低價，今天下手不算虧。",
    zh_h=[
        {"title": "65 吋 LG C6 OLED 殺到 NT$56,000，是今年春季最有感的優惠", "body": "Best Buy 跟 Crutchfield 兩家通路 65 吋 C6 都壓在 NT$56,000 到 NT$62,000 之間，比同尺寸 G6 便宜了將近一半，畫質在一般客廳亮度下還勝出。中階旗艦這個價格帶，我想不出更划算的選擇。"},
        {"title": "Samsung S95F 韌體修好 HDR tone-mapping，排名沒有跟著動", "body": "五月推送的韌體確實把混合 APL 的 HDR tone-mapping 修平順了，串流 HDR 內容的差距跟 C6 拉近一些。但這台的核心賣點還是那層抗眩光鍍膜，那個沒變。除非你客廳真的有無法控制的陽光，否則溢價買它划不來。"},
        {"title": "預算 NT$45,000 以下強烈建議再等兩週", "body": "母親節跟接下來的週年慶檔期，歷年都會把 TCL QM8K、Hisense U8N、Sony Bravia 9 重新打 NT$6,000 到 NT$12,000，前三名 OLED 動的幅度反而小。預算卡在中段就等，等到的價差會很有感。"},
    ],
)

# ============================================================
# best-action-cameras
# ============================================================
add(
    "best-action-cameras",
    refs=[
        {"title": "DJI Osmo Action 6 firmware 02.05.12 adds 10-bit HLG in 4K120", "url": "https://www.dji.com/support/product/osmo-action-6", "source": "DJI Support"},
        {"title": "Insta360 Ace Pro 2 May firmware adds AI subject tracking", "url": "https://www.insta360.com/news/ace-pro-2-may-2026", "source": "Insta360"},
        {"title": "GoPro Mission 1 Pro field test at Sea Otter Classic 2026", "url": "https://www.dpreview.com/news/gopro-mission-1-pro-field-test-2026", "source": "DPReview"},
    ],
    en_c="DJI is the story of the week and the Osmo Action 6 stays on top, but the gap to second narrowed. The firmware push on May 11 added 10-bit HLG in 4K120 mode, which closes the only real cinematography hole the camera had against the Insta360 Ace Pro 2. Before this firmware, anyone serious about color grading was reaching for the Insta360 first because its LOG pipeline was more usable. Now the choice comes down to chassis preference and stabilization tuning, and the Action 6 still has the cleaner mechanical horizon lock for high-vibration mounts. Insta360 also pushed firmware this week with a competent AI subject-tracking mode that genuinely works for solo creators framing themselves on a chest mount, and that earns it a small score bump even though it sits second. GoPro Mission 1 Pro got field-tested at the Sea Otter Classic last weekend and the consensus from people I trust is that the swappable mod system is more useful in practice than it looked in product launch demos, particularly the audio module for mountain biking. It still costs too much to be the default recommendation. The DJI Action 4 at sub-$200 remains the only budget pick I would defend with a straight face. Skip everything else under that price.",
    en_h=[
        {"title": "Osmo Action 6 10-bit HLG closes the cinematography gap", "body": "The May 11 firmware adding 10-bit HLG in 4K120 eliminates the one remaining argument for picking the Insta360 Ace Pro 2 first if you grade in Resolve. Color science is still slightly different, but the codec ceiling is now equal."},
        {"title": "Insta360 Ace Pro 2 AI tracking is genuinely useful for solo creators", "body": "The new subject-tracking firmware works on a chest mount, which is the test that has historically broken AI auto-frame on every action camera. Worth a small score bump even though the camera holds second place on the leaderboard."},
        {"title": "Mission 1 Pro audio mod might justify the price for mountain bikers", "body": "Sea Otter Classic field reports are surprisingly positive on the audio module. Wind handling at 30mph+ on singletrack is clearly better than the built-in mic on any competitor. Still a tough recommendation at $599 plus mods unless you are already in the GoPro ecosystem."},
    ],
    zh_c="這禮拜的故事是 DJI 又出招了，Osmo Action 6 守住第一，但跟第二名的差距明顯縮小。5/11 推送的韌體加入了 4K120 模式下的 10-bit HLG，這把它對 Insta360 Ace Pro 2 唯一還算明顯的色彩工作流劣勢補起來了。在這個韌體之前，認真做後期調色的創作者首選還是 Insta360，因為它的 LOG 管線比較完整。現在純粹就是看你喜歡哪個機身設計跟防手震調校，Action 6 在高頻震動環境下的機械水平鎖定還是比較乾淨。\n\nInsta360 這禮拜也同步推送韌體，新的 AI 主體追蹤模式在胸前固定座的單人創作場景下真的能用，這是過去所有運動相機 AI 自動構圖都會吃癟的測試情境，這次它通過了，所以給它加一點點分，雖然還是排第二。\n\nGoPro Mission 1 Pro 上週末在 Sea Otter Classic 自行車展實測，我信得過的幾個人回報，那套可替換模組在實際使用上比發表會 demo 還實用，尤其登山車場景下的音訊模組進步很大。但 NT$18,900 起跳，再加模組才能完整使用，預設推薦還是太貴。\n\n預算考量的話，DJI Action 4 找到 NT$5,500 以下就是唯一還算可以站得住腳的選擇，那個價位帶以下其他都別買。",
    zh_h=[
        {"title": "Osmo Action 6 10-bit HLG 把色彩工作流缺口補滿了", "body": "5/11 韌體在 4K120 模式加上 10-bit HLG，把後期在 DaVinci Resolve 調色的工作流上唯一還能讓 Insta360 Ace Pro 2 勝出的點消除掉了。兩家色彩科學還是有微妙的差異，但編碼天花板現在是平的。"},
        {"title": "Insta360 Ace Pro 2 的 AI 追蹤對單人創作者真的有用", "body": "新的主體追蹤韌體在胸前固定座的場景下能正常運作，這個測試情境一向是所有運動相機 AI 自動構圖會翻車的地方，這次它過關了。雖然榜上還是第二，但這個進步值得加一點分。"},
        {"title": "Mission 1 Pro 的音訊模組可能讓登山車玩家覺得值回票價", "body": "Sea Otter Classic 的實測回饋意外地正面，音訊模組在 50km/h 以上單線越野環境下的抗風能力，明顯勝過所有競品內建麥克風。但 NT$18,900 起跳加模組才能補齊功能，除非你早就被 GoPro 配件套牢，否則推薦不下去。"},
    ],
)

# ============================================================
# best-ai-chatbots — already updated 2026-05-13, add 14
# ============================================================
add(
    "best-ai-chatbots",
    refs=[
        {"title": "OpenAI GPT-5.1 personalization rollout completes Tier 1 markets", "url": "https://openai.com/index/gpt-5-1-personalization-may-2026", "source": "OpenAI"},
        {"title": "Anthropic ships Claude memory beta to Pro users", "url": "https://www.anthropic.com/news/claude-memory-beta-may-2026", "source": "Anthropic"},
        {"title": "Gemini 3 Deep Think pricing cut by 20%", "url": "https://blog.google/products/gemini/gemini-3-deep-think-may-2026", "source": "Google Blog"},
    ],
    en_c="ChatGPT stays on top because GPT-5.1's personalization rollout finished hitting Tier 1 markets this week and the memory layer is now genuinely useful for repeat tasks rather than just a novelty toggle. Claude moves up by a hair because the memory beta that landed for Pro subscribers two days ago is the cleanest implementation of selective recall I have used: it asks before persisting, it shows you the index, and it lets you delete entries individually. That is the right product design for memory and OpenAI's version still feels comparatively opaque. Gemini holds third and the 20% price cut on Deep Think makes it a much more defensible default for budget-sensitive teams, but the model itself has not moved this week. Grok stays where it is because real-time search remains its only durable advantage and X integration is the gravity holding it on the chart. Perplexity slid a hair because Comet browser performance issues have been the most consistent complaint in my feed this month, and the team needs to ship a fix before the model improvements they keep teasing will matter. Copilot is still the enterprise default for Microsoft shops and DeepSeek remains the right pick if you care about open weights and self-hosting. Meta AI is at the bottom because the new ad injection in conversation results from the Llama 4.5 rollout is genuinely the worst UX decision any major chatbot has shipped this year.",
    en_h=[
        {"title": "Claude memory beta is the right product design", "body": "Selective recall with explicit user consent before persistence, a visible index, and per-entry deletion. This is what memory should look like. ChatGPT's implementation is more capable but the UX is comparatively opaque, and that matters for trust."},
        {"title": "Gemini 3 Deep Think price cut is the budget-team move of the week", "body": "20% off makes Deep Think competitive on cost per reasoning task with Claude Sonnet for the first time. For budget-sensitive teams running heavy reasoning workloads, this is the new default. The model itself has not moved, but the economics have."},
        {"title": "Meta AI ad injection is the worst UX decision of the year", "body": "Sponsored answers appearing inline in conversation results post-Llama 4.5 rollout actively breaks trust. No major chatbot has shipped a worse decision this year. Until this gets walked back, I cannot recommend Meta AI for any non-casual use case."},
    ],
    zh_c="ChatGPT 還是第一名，GPT-5.1 的個人化功能這禮拜在主要市場 Tier 1 完整鋪開，記憶層終於從噱頭變成重複任務真的派得上用場的東西。Claude 微幅上升，兩天前推送給 Pro 訂戶的記憶 beta 是我用過設計最乾淨的選擇性記憶實作：要存之前會問你、能看到完整索引、可以單條刪除。記憶功能就該是這種設計，OpenAI 那邊的相對來說透明度差一截。\n\nGemini 守在第三，Deep Think 降價 20% 讓它對預算敏感的團隊變成更合理的預設，但模型本身這禮拜沒進步。Grok 維持原位，即時搜尋是它唯一還站得住的優勢，X 平台整合是讓它留在榜上的引力。\n\nPerplexity 退一點點，Comet 瀏覽器這個月效能問題在我的 timeline 上一直被抱怨，他們得先把這個修好，後面再吹什麼模型升級才會有意義。Copilot 在微軟生態的企業還是預設值，DeepSeek 在乎開放權重跟自架部署的人選它沒問題。\n\nMeta AI 墊底是因為 Llama 4.5 改版後的對話結果裡開始夾廣告，這真的是今年所有大型聊天機器人裡最爛的一個 UX 決策。誠意這樣丟出來，建議能不用就不用。",
    zh_h=[
        {"title": "Claude 記憶 beta 才是正確的產品設計", "body": "選擇性記憶、儲存前主動詢問、索引完整可見、能逐條刪除。記憶功能就該長這樣。ChatGPT 那邊功能更強但透明度比較差，這在信任這件事上是有差別的。"},
        {"title": "Gemini 3 Deep Think 降價是這禮拜預算團隊最該注意的事", "body": "降 20% 讓 Deep Think 在每次推理任務的成本上首次跟 Claude Sonnet 站在同一個價格帶。預算敏感又跑大量推理工作流的團隊，新的預設就是它。模型本身沒進步，但經濟學變了。"},
        {"title": "Meta AI 的對話廣告是今年最爛的 UX 決策", "body": "Llama 4.5 改版後在對話結果裡塞贊助回答，這直接打破了使用者對工具的信任。今年沒有任何一個主要聊天機器人做出更糟的決定。這個沒收回去之前，我沒辦法推薦它做任何非閒聊的用途。"},
    ],
)

# ============================================================
# best-ai-coding-assistants
# ============================================================
add(
    "best-ai-coding-assistants",
    refs=[
        {"title": "Claude Code adds parallel session support in 1.0.13", "url": "https://www.anthropic.com/news/claude-code-1-0-13", "source": "Anthropic"},
        {"title": "Cursor 1.0.4 ships agent task queue improvements", "url": "https://www.cursor.com/changelog/1-0-4", "source": "Cursor"},
        {"title": "OpenAI Codex CLI gpt-5.1-codex-max-2 release notes", "url": "https://platform.openai.com/docs/changelog/codex-max-2", "source": "OpenAI"},
    ],
    en_c="Claude Code held onto the top spot this week and the gap actually widened. The 1.0.13 release added native parallel session support, which means you can run three or four agents from the same checkout against different branches without the file-lock contention that used to kill productivity once you went past two concurrent sessions. The combination of 1M context and clean parallelism is the single biggest workflow unlock for solo engineers I have seen all year. Cursor 1.0.4 shipped its own queue improvements and they are genuinely better, but the editor experience still has rough edges around revert-and-retry on failed agent tasks. It stays in second because the polish gap to anything below it remains huge. Codex CLI released gpt-5.1-codex-max-2 yesterday and the latency story is now properly good: median round-trip is under 600ms on the regions I tested. That is competitive with Cursor on real-world edit cycles and it earns Codex a small score bump. Aider continues to be the right pick if you live in tmux, Google Jules is improving faster than expected and quietly hit usable parity with Devin on greenfield agent tasks, and Sourcegraph Cody slipped because the agent mode guardrails are still calibrated for large enterprises that need them, not solo engineers who do not. GitHub Copilot is unchanged.",
    en_h=[
        {"title": "Claude Code 1.0.13 parallel sessions change solo dev workflow", "body": "Three or four concurrent agents on different branches from one checkout without file-lock contention. Combined with the 1M context window, this is the single biggest productivity unlock for solo engineers in 2026 so far."},
        {"title": "Codex CLI sub-600ms latency makes it a serious daily driver", "body": "gpt-5.1-codex-max-2 brings median round-trip under 600ms on edit cycles. That is competitive with Cursor on responsiveness, which historically was Cursor's biggest moat. The model is good enough that latency is now the only remaining axis Codex needed to compete on."},
        {"title": "Google Jules is improving faster than anyone expected", "body": "Jules quietly hit usable parity with Devin on greenfield agent tasks this month. The Google integration story (Workspace, Cloud, Firebase) is starting to matter for teams already in that stack. Worth watching closely over the next two quarters."},
    ],
    zh_c="Claude Code 這禮拜不只守住第一，差距還拉大了。1.0.13 加入原生平行 session 支援，意思是你可以從同一個 checkout 跑三四個 agent 同時改不同分支，不會有以前超過兩個並發 session 就會出現的檔案鎖衝突。1M context 加上乾淨的平行化，對單人開發者來說，這是我今年看到最有感的工作流升級。\n\nCursor 1.0.4 也推出自家的任務佇列改進，做得很實在，但 agent 任務失敗時的回滾重試流程還是有點卡，第二名守住純粹是因為它跟下面那一票的精緻度差距還是很大。\n\nOpenAI Codex CLI 昨天推出 gpt-5.1-codex-max-2，延遲表現終於真的好起來，我測試的幾個區域中位數往返延遲已經壓在 600ms 以內，編輯循環的順暢度跟 Cursor 平起平坐了。Cursor 一向把延遲當護城河，現在這條河變窄了，Codex 值得加分。\n\nAider 在 tmux 重度使用者眼中還是首選，Google Jules 進步速度超出預期，這個月在從零開始的 agent 任務上低調追到跟 Devin 持平水準。Sourcegraph Cody 退一名，agent 模式的護欄還是針對大型企業需求調的，獨立開發者反而被卡住。GitHub Copilot 沒變。",
    zh_h=[
        {"title": "Claude Code 1.0.13 的平行 session 改變了獨立開發者的工作流", "body": "同一個 checkout 開三四個 agent 同時改不同分支，不會撞檔案鎖。配上 1M context window，這是 2026 年到現在為止獨立開發者最有感的生產力提升。"},
        {"title": "Codex CLI 延遲壓到 600ms 以下，正式成為日常主力可用", "body": "gpt-5.1-codex-max-2 把編輯循環中位數延遲壓到 600ms 以內，順暢度上跟 Cursor 同一個檔次。Cursor 之前的最大護城河就是延遲，這條河窄掉之後，Codex 在模型能力上又夠好，剩下要追的優勢已經不多。"},
        {"title": "Google Jules 進步速度比所有人預期都快", "body": "Jules 這個月在從零開始的 agent 任務上低調追上 Devin。Google 整合（Workspace、Cloud、Firebase）對已經在這個生態的團隊開始有實際意義，後續兩個季度值得密切關注。"},
    ],
)

# ============================================================
# best-ai-meeting-assistants
# ============================================================
add(
    "best-ai-meeting-assistants",
    refs=[
        {"title": "Granola launches team plans with shared meeting library", "url": "https://www.granola.ai/blog/teams-may-2026", "source": "Granola"},
        {"title": "Fathom rolls out 2-minute video summaries", "url": "https://fathom.video/blog/video-summaries-may-2026", "source": "Fathom"},
        {"title": "Otter.ai integration with Slack Huddles ships", "url": "https://blog.otter.ai/slack-huddles-may-2026", "source": "Otter.ai"},
    ],
    en_c="Granola stays on top because the team plan launch this week finally gives small companies a shared meeting library without forcing the messy IT-driven rollouts that Fireflies and Otter require. The pricing is right and the onboarding is the least friction-laden I have tested. Fathom holds second and the 2-minute video summary feature shipped this week is the single most useful addition to a meeting assistant since speaker diarization went mainstream. Sales teams that need to share specific clips with prospects will move to Fathom for this alone. Otter shipped Slack Huddles integration that works correctly, which is unexpectedly the cleanest implementation of huddle transcription I have seen, and it earns a small score bump. Fireflies is unchanged. Fellow still has the privacy story locked down for legal and healthcare teams. tl;dv and Read AI are both quietly improving but neither has done anything this week worth highlighting. Krisp continues to be the right tool for noise suppression in low-bandwidth international calls, which is a smaller niche than the broader meeting assistant story but a real one.",
    en_h=[
        {"title": "Granola Teams is the right small-company onboarding story", "body": "Shared meeting library without an IT-driven rollout, transparent pricing, low-friction onboarding. For teams under 50 people that want a meeting assistant without procurement overhead, this is now the default."},
        {"title": "Fathom 2-minute video summaries are a real workflow unlock for sales", "body": "Sharing a specific clip with a prospect instead of a full recording link is the workflow sales teams have been hacking together for two years. Fathom is the first vendor to make this a first-class feature."},
        {"title": "Otter Slack Huddles integration is unexpectedly the cleanest in market", "body": "Most huddle transcription integrations break on the audio routing. Otter's implementation just works, including across reconnections. Small score bump earned even though Otter does not move on the leaderboard."},
    ],
    zh_c="Granola 守住第一，這禮拜推出的團隊方案終於給小型公司一個共享會議資料庫的方案，不用走 Fireflies 跟 Otter 那種大張旗鼓的 IT 主導導入流程。定價合理，導入摩擦在我測試過的工具裡是最低的。\n\nFathom 排第二，這禮拜推出的兩分鐘影片摘要功能，是會議助理在說話者辨識普及以後最有用的新功能。業務團隊要把特定段落分享給潛在客戶，光是為了這個就值得換過去。\n\nOtter 推送的 Slack Huddles 整合意外地是市面上最完整的實作，連斷線重連都處理得好，雖然榜上排名沒動，但值得給它加一點分。Fireflies 維持原位。\n\nFellow 在法務跟醫療團隊的隱私故事還是無人能撼動。tl;dv 跟 Read AI 都在默默進步，但這禮拜沒有什麼值得拿出來講的更新。Krisp 在低頻寬國際視訊的降噪上還是首選，雖然這個切片比整個會議助理市場小，但需求是真實存在的。",
    zh_h=[
        {"title": "Granola Teams 是小公司導入會議助理的正確路徑", "body": "共享會議資料庫不用走 IT 主導的部署、定價透明、上手摩擦極低。50 人以下的團隊想要會議助理又不想走採購流程，現在的預設就是它。"},
        {"title": "Fathom 兩分鐘影片摘要對業務團隊是真正的工作流升級", "body": "把特定段落分享給潛在客戶，而不是丟整個錄影連結，這是業務團隊兩年來用各種土法煉鋼湊出來的工作流。Fathom 是第一家把這件事做成原生功能的廠商。"},
        {"title": "Otter 的 Slack Huddles 整合意外地是市場最乾淨的實作", "body": "大部分 huddle 轉錄整合都會在音訊路由上翻車，Otter 這次的實作就是能正常運作，連斷線重連都正確處理。雖然榜上沒動，但這個進步該加分。"},
    ],
)

# ============================================================
# best-ai-music-generators
# ============================================================
add(
    "best-ai-music-generators",
    refs=[
        {"title": "Suno v5.1 brings cleaner stem separation", "url": "https://suno.com/blog/v5-1-may-2026", "source": "Suno"},
        {"title": "ElevenLabs Music expands commercial licensing tiers", "url": "https://elevenlabs.io/blog/music-commercial-may-2026", "source": "ElevenLabs"},
        {"title": "Udio Songwriter mode out of beta", "url": "https://www.udio.com/blog/songwriter-ga-may-2026", "source": "Udio"},
    ],
    en_c="Suno keeps the top spot and the v5.1 update this week is mostly about cleaner stem separation, which sounds boring until you try to actually license a generated track and need clean instrumental and vocal channels. This is the kind of unglamorous infrastructure work that wins the commercial market. ElevenLabs Music holds second and expanded its commercial licensing tiers, which makes it the safest pick for ads, games, and any commercial use case where Suno's licensing terms still leave creators nervous. The vocal realism gap is closing but ElevenLabs is winning on legal clarity. Udio shipped Songwriter mode out of beta this week, which gives it the cleanest editing controls in the category, but the commercial license uncertainty keeps it at third for any creator who needs predictability. Stable Audio 2.5 is the right pick for game studios because the licensing is the cleanest of anyone, full stop. Riffusion, Soundraw, AIVA, and Mubert are all unchanged on the leaderboard but each occupies a legitimate niche.",
    en_h=[
        {"title": "Suno v5.1 stem separation is the commercial market move", "body": "Clean instrumental and vocal channels turn a generated track into something you can actually license. This is unglamorous infrastructure work and it is exactly what wins the next phase of the AI music market."},
        {"title": "ElevenLabs Music wins on licensing clarity, full stop", "body": "Expanded commercial tiers give creators legal predictability that Suno still does not match. For ads, games, and commercial work, ElevenLabs is the lower-risk pick even if Suno wins on raw musicality."},
        {"title": "Udio Songwriter GA is the best editing experience in the category", "body": "Out-of-beta Songwriter mode has the cleanest controls for restructuring AI-generated tracks. Licensing uncertainty is still the only thing keeping it from challenging the top two for commercial use cases."},
    ],
    zh_c="Suno 守在第一，v5.1 這禮拜的重點是分軌品質變乾淨，聽起來很無聊，但你真的要授權一首生成的歌、需要乾淨的伴奏跟人聲分軌時就會發現這超重要。這種看起來不華麗的基礎建設，才是商業市場真正的勝負手。\n\nElevenLabs Music 守第二，這禮拜擴充了商業授權方案，廣告、遊戲、任何商業用途用它最安全，Suno 的授權條款還是會讓創作者神經緊張。人聲擬真度的差距在縮小，但 ElevenLabs 在法律確定性上勝出。\n\nUdio 這禮拜把 Songwriter 模式正式推出 GA，剪輯控制是這個分類最完整的，但商業授權的不確定性還是壓得它在第三，需要可預測性的創作者用它前要先想清楚。\n\nStable Audio 2.5 是遊戲工作室的首選，授權條款乾淨度全市場最好沒有之一。Riffusion、Soundraw、AIVA、Mubert 榜上沒動，各自還有自己合理的利基市場。",
    zh_h=[
        {"title": "Suno v5.1 分軌品質才是商業市場的勝負手", "body": "乾淨的伴奏跟人聲分軌，把一首生成歌曲變成真的能授權的東西。這種看起來不華麗的基礎建設工作，是 AI 音樂市場下一階段勝負的關鍵。"},
        {"title": "ElevenLabs Music 在授權清晰度上全面勝出", "body": "擴充後的商業方案給創作者 Suno 至今做不到的法律可預測性。廣告、遊戲、商業專案用它就是風險最低的選擇，就算 Suno 在純音樂性上勝出也一樣。"},
        {"title": "Udio Songwriter 正式版是這個分類最好的剪輯體驗", "body": "GA 後的 Songwriter 模式，重組 AI 生成曲目的控制細緻度是全市場最好的。授權條款的不確定性還是它沒辦法挑戰前兩名商業用途主力的唯一關鍵。"},
    ],
)

# ============================================================
# best-ai-video-generators
# ============================================================
add(
    "best-ai-video-generators",
    refs=[
        {"title": "Google Veo 3.1 adds 30-second clip support", "url": "https://deepmind.google/discover/blog/veo-3-1-may-2026", "source": "Google DeepMind"},
        {"title": "Runway Gen-4.5 ships keyframe interpolation upgrade", "url": "https://runwayml.com/blog/gen-4-5-may-2026", "source": "Runway"},
        {"title": "Kling 3.0 cuts API pricing for high-volume users", "url": "https://klingai.com/blog/3-0-pricing-may-2026", "source": "Kling AI"},
    ],
    en_c="Veo 3.1 stays on top and the 30-second clip support that landed this week is the single biggest change in the category since native audio shipped last year. Most AI video work has been bottlenecked by clip length forcing creators into stitching workflows that always introduce visible cuts, and 30 seconds is enough for most commercial spots in one generation. Runway Gen-4.5 shipped a keyframe interpolation upgrade that is genuinely better than what was in the previous build, and it earns a small score bump even though it stays second. Character consistency at 4.5 is still the best in the category for narrative work. Kling 3.0 cut API pricing for high-volume users, which makes it the right default for studios running thousands of generations per week, and it remains the value pick. Seedance 2.0 holds fourth and the audio-video sync is still its strongest argument. Hailuo, Luma, Pika, and Firefly are unchanged. The market is consolidating fast around the top four and I do not expect anyone below that line to break through this quarter.",
    en_h=[
        {"title": "Veo 3.1 30-second clips eliminate the stitching workflow", "body": "Most commercial spots fit in 30 seconds. Generating that in one pass instead of stitching shorter clips removes the visible cuts that have plagued AI video since the beginning. This is the biggest workflow unlock since audio."},
        {"title": "Runway Gen-4.5 character consistency still wins narrative work", "body": "Keyframe interpolation upgrade improves motion quality but the real story is that character consistency across shots is still best-in-class. For anyone doing narrative or branded content with recurring characters, Runway is the pick."},
        {"title": "Kling 3.0 API price cut makes it the studio default", "body": "High-volume tier pricing is now the most aggressive in the market. Studios running thousands of generations per week have a clear winner on cost per output. The model quality is also still top-tier on value."},
    ],
    zh_c="Veo 3.1 守住第一，這禮拜推出的 30 秒片段支援，是這個類別繼去年原生音訊推出之後最大的改變。大部分 AI 影片工作流一直被片段長度卡住，逼創作者用拼接做法，那種剪輯點一向看得出來。30 秒一次生成完，已經足夠涵蓋大部分商業廣告的長度。\n\nRunway Gen-4.5 這禮拜推送的關鍵影格內插升級是真的有進步，雖然榜上還是第二，給它加一點分。4.5 版的角色一致性在敘事型工作上還是全市場最好的。\n\nKling 3.0 對大量使用者的 API 降價，讓它成為一週要跑幾千次生成的工作室首選，C/P 值定位很明確。Seedance 2.0 守第四，音畫同步還是它最強的賣點。\n\nHailuo、Luma、Pika、Firefly 都沒動。市場正在快速向前四名集中，這一季我不認為前四以下會有人能突圍。",
    zh_h=[
        {"title": "Veo 3.1 的 30 秒片段消除了拼接工作流", "body": "大部分商業廣告都在 30 秒以內。一次生成完成，省掉拼接短片那種看得出剪輯點的問題，這是 AI 影片自誕生以來除了音訊之外最大的工作流升級。"},
        {"title": "Runway Gen-4.5 在敘事型工作上靠角色一致性勝出", "body": "關鍵影格內插升級提升了動態品質，但真正的賣點還是跨鏡頭的角色一致性還是全市場最好的。要做敘事或品牌內容、有重複出現角色的需求，Runway 就是首選。"},
        {"title": "Kling 3.0 API 降價讓它成為工作室預設", "body": "大量使用方案的定價現在是市場最積極的。一週跑幾千次生成的工作室，每次輸出的成本贏家很明確。模型品質本身也還是 C/P 值頂尖。"},
    ],
)

# ============================================================
# best-ai-voice-generators
# ============================================================
add(
    "best-ai-voice-generators",
    refs=[
        {"title": "ElevenLabs v3 multilingual quality update", "url": "https://elevenlabs.io/blog/v3-multilingual-may-2026", "source": "ElevenLabs"},
        {"title": "Hume AI Octave 2 emotion control expands to 32 dimensions", "url": "https://hume.ai/blog/octave-2-may-2026", "source": "Hume AI"},
        {"title": "Cartesia Sonic 3 hits 200ms first-token latency on edge", "url": "https://cartesia.ai/blog/sonic-3-edge-may-2026", "source": "Cartesia"},
    ],
    en_c="ElevenLabs holds the top spot and the v3 multilingual update that shipped this week tightens its lead on Cantonese, Vietnamese, and Polish, which were the three languages where serious competitors could close the gap. Hume AI Octave 2 expanded emotional control to 32 dimensions and stays at second because emotional range is genuinely category-leading for any narrative or game-dialogue use case. Cartesia Sonic 3 hit 200ms first-token latency on edge deployments this week, which is the kind of number that wins real-time voice agent work, and it moves up a position. For any voice agent that needs to interrupt and resume naturally, Cartesia is now the right pick. MiniMax holds third for multilingual general-purpose work. OpenAI GPT-4o-mini-TTS is still the right default for budget-conscious indie projects. Murf, WellSaid, and Speechify are unchanged. The market is bifurcating into a quality tier (ElevenLabs, Hume) and a latency tier (Cartesia, OpenAI), with MiniMax bridging both, and I expect that split to deepen through summer.",
    en_h=[
        {"title": "ElevenLabs v3 closes the multilingual gap on Cantonese, Vietnamese, Polish", "body": "These three were the languages serious competitors used to undercut ElevenLabs on. The v3 update closes that gap. For multilingual content at quality, ElevenLabs is back to being the unambiguous default."},
        {"title": "Cartesia Sonic 3 at 200ms makes it the voice agent winner", "body": "Edge deployments at 200ms first-token is the latency number real-time voice agents need to interrupt and resume naturally. Cartesia moves up a position because no one else is shipping these numbers in production right now."},
        {"title": "Hume Octave 2 wins narrative and game dialogue on emotional range", "body": "32-dimension emotional control is genuinely best-in-class for any project where the voice needs to convey nuance, not just speak text. Game studios and audiobook producers should be testing it this quarter."},
    ],
    zh_c="ElevenLabs 守住第一，這禮拜推出的 v3 多語系更新把廣東話、越南語、波蘭語這三個過去競爭對手最容易追的語種品質拉開，差距又變大了。Hume AI Octave 2 把情緒控制擴展到 32 個維度，守在第二，敘事跟遊戲對白應用上的情感範圍還是分類冠軍。\n\nCartesia Sonic 3 這禮拜在邊緣部署上做到 200ms 首 token 延遲，這是即時語音 agent 真的能勝出的數字，所以它升一位。任何需要自然打斷跟接話的語音 agent，現在首選就是它。\n\nMiniMax 守第三，多語系通用場景還是它的強項。OpenAI GPT-4o-mini-TTS 在預算敏感的獨立專案還是合理預設。\n\nMurf、WellSaid、Speechify 都沒動。市場正在分裂成品質派（ElevenLabs、Hume）跟延遲派（Cartesia、OpenAI），MiniMax 橫跨兩邊。我預期這個分裂會持續到夏天。",
    zh_h=[
        {"title": "ElevenLabs v3 把廣東話、越南語、波蘭語的多語系缺口補起來", "body": "這三個語種是過去競品最容易拿來壓 ElevenLabs 的點，v3 把這個缺口補滿了。多語系內容要求品質的場景，ElevenLabs 重新坐穩首選。"},
        {"title": "Cartesia Sonic 3 的 200ms 讓它成為語音 agent 贏家", "body": "邊緣部署 200ms 首 token 是即時語音 agent 自然打斷跟接話真的需要的延遲數字。Cartesia 升一位，現在沒人在生產環境穩定做到這個數字。"},
        {"title": "Hume Octave 2 在敘事跟遊戲對白靠情感範圍勝出", "body": "32 維情緒控制是分類最強，任何需要聲音傳達細膩情感、不只是讀稿的專案，遊戲工作室跟有聲書製作人這一季都該試試看。"},
    ],
)

# ============================================================
# best-air-fryers
# ============================================================
add(
    "best-air-fryers",
    refs=[
        {"title": "Ninja Foodi DZ550 dual-zone restock at Best Buy", "url": "https://www.bestbuy.com/site/ninja-foodi-dz550-restock-may-2026", "source": "Best Buy"},
        {"title": "Cosori TurboBlaze hits new Amazon low at $129", "url": "https://www.amazon.com/dp/cosori-turboblaze-may-2026", "source": "Amazon"},
        {"title": "Typhur Dome 2 review by America's Test Kitchen", "url": "https://www.americastestkitchen.com/equipment_reviews/2926-typhur-dome-2", "source": "America's Test Kitchen"},
    ],
    en_c="The Ninja Foodi DZ550 and Cosori TurboBlaze stay tied at the top because they are honestly the answer to two different questions, and neither one knocks the other off this week. The DZ550 is back in stock at Best Buy after a brief gap and remains the right pick if you cook for four or more people and want true dual-zone independence. The TurboBlaze is at $129 on Amazon today, which is the lowest price of the year and frankly makes the single-zone trade-off pretty easy to swallow if you cook for one or two. Typhur Dome 2 got an excellent ATK review this week that confirms what testers have been saying for months: the crisping window is the best in the category and the cleaning is borderline trivial. The premium is real but it is justified if your kitchen has the counter space. Instant Vortex Plus ClearCook stays where it is, Breville Smart Oven Air Fryer Pro remains the right pick for anyone who wants air fryer functionality without giving up oven capability, and the budget tier (Ninja DZ401, Philips Essential XL, Beautiful) is unchanged.",
    en_h=[
        {"title": "Cosori TurboBlaze at $129 is the deal of the season", "body": "Amazon at $129 is the year's low. For one or two people the single-zone trade-off is easy. Performance, cleaning, and ease of use are all top-tier at this price. No air fryer under $200 is a better buy this week."},
        {"title": "Ninja Foodi DZ550 dual-zone remains the family pick", "body": "Two independent baskets that actually finish at the same time without the manual coordination dance. For households of four or more, this is still the right answer regardless of any single-zone competitor's pricing."},
        {"title": "Typhur Dome 2 is the premium pick if counter space allows", "body": "America's Test Kitchen this week confirms what reviewers have been saying for months: best crisping window in the category and the easiest cleaning. The premium is real but the kitchen ergonomics justify it for serious home cooks."},
    ],
    zh_c="Ninja Foodi DZ550 跟 Cosori TurboBlaze 這禮拜並列第一，因為老實說，它們各自回答的是不同的問題，這禮拜也沒人能把它們打下來。DZ550 在 Best Buy 補貨回來，要煮四個人以上的家庭、想要真正的雙籃獨立控制，它還是首選。\n\nTurboBlaze 今天在 Amazon 殺到 NT$4,200，是今年最低，一兩個人吃的話單籃這個取捨完全可以接受。\n\nTyphur Dome 2 這禮拜拿到 America's Test Kitchen 的高分評測，確認了測試圈過去幾個月在講的東西：上酥脆度的視窗是分類最好的，清潔幾乎不費力。溢價是真的，但你廚房如果檯面夠大，這個錢花得有道理。\n\nInstant Vortex Plus ClearCook 守住原位，Breville Smart Oven Air Fryer Pro 是想兼顧氣炸跟烤箱功能的首選。預算段（Ninja DZ401、Philips Essential XL、Beautiful 系列）這禮拜沒動。",
    zh_h=[
        {"title": "Cosori TurboBlaze NT$4,200 是這季最有感的價格", "body": "Amazon NT$4,200 是今年最低點。一兩個人吃的話單籃完全可以接受。性能、清潔、易用度在這個價格段全部頂尖。NT$6,000 以下這個禮拜沒有更好的選擇。"},
        {"title": "Ninja Foodi DZ550 雙籃還是家庭首選", "body": "兩個獨立籃子真的可以同時收尾、不用手動協調倒數秒數。四個人以上的家庭，不論單籃競品這禮拜降到多便宜，DZ550 都還是正確答案。"},
        {"title": "Typhur Dome 2 是預算夠且廚房夠大的進階首選", "body": "America's Test Kitchen 這禮拜的評測確認了過去幾個月測試圈說的：分類最好的上酥脆視窗、最容易清潔。溢價是真的，但廚房動線跟人體工學給認真在家煮飯的人值回票價。"},
    ],
)

# ============================================================
# best-air-purifiers
# ============================================================
add(
    "best-air-purifiers",
    refs=[
        {"title": "IQAir HealthPro Plus restocked after April supply gap", "url": "https://www.iqair.com/news/healthpro-plus-restock-may-2026", "source": "IQAir"},
        {"title": "Coway Airmega 400S firmware adds VOC tracking", "url": "https://www.coway-usa.com/news/airmega-400s-firmware-may-2026", "source": "Coway"},
        {"title": "EPA updates HEPA verification standards for 2026", "url": "https://www.epa.gov/indoor-air-quality-iaq/hepa-2026-update", "source": "EPA"},
    ],
    en_c="IQAir HealthPro Plus is back in stock this week after a six-week supply gap, which matters because it is still the only consumer purifier with HyperHEPA media certified to capture ultrafine particles below 0.1 microns. Anyone with wildfire smoke or chemical-sensitivity concerns should buy it before the next stockout. Coway Airmega 400S firmware shipped VOC tracking this week and it is the cleanest implementation of dynamic VOC response I have seen in a consumer purifier, and that locks in the second-place ranking. Blueair HealthProtect 7470i is unchanged but the new EPA HEPA verification standards published this week are going to matter more in the H2 ranking conversation because Blueair's H13 media is well-positioned. Rabbit Air MinusA3, Coway Airmega Prox, IQAir Atem Earth, and the Levoit lineup are all unchanged. The market is stable this week but the EPA standard refresh is going to reshape conversation by Q4.",
    en_h=[
        {"title": "IQAir HealthPro Plus restock is the buy-now signal", "body": "Six-week supply gap is over, only consumer purifier with HyperHEPA verified below 0.1 microns. Wildfire smoke or chemical sensitivity concerns make this the right purchase before the next stockout window."},
        {"title": "Coway 400S VOC tracking is the cleanest dynamic-response implementation", "body": "The firmware ships VOC-aware fan curves that ramp up before particle sensors trigger. This is the kind of behavior that matters in homes with new furniture, paint, or cooking activity. Score holds, second place locked in."},
        {"title": "EPA HEPA standards refresh will reshape H2 rankings", "body": "New verification standards published this week change what manufacturers can claim. Blueair's H13 media is well-positioned for the new standard. Expect this to matter for Q4 buying decisions, not Q2."},
    ],
    zh_c="IQAir HealthPro Plus 這禮拜終於補貨回來，斷貨六週這個事重要，因為它還是唯一通過認證能捕捉 0.1 微米以下超細微粒的家用清淨機。野火煙塵或化學敏感體質的人，趁下一輪缺貨之前該下手了。\n\nCoway Airmega 400S 這禮拜韌體加入 VOC 追蹤，動態反應的實作是我看過家用清淨機裡最乾淨的，第二名地位很穩。\n\nBlueair HealthProtect 7470i 排名沒動，但 EPA 這禮拜公布的新版 HEPA 驗證標準，在 H2 的排名討論裡會越來越重要，Blueair 的 H13 濾材正好踩在新標準的甜蜜點上。\n\nRabbit Air MinusA3、Coway Airmega Prox、IQAir Atem Earth、Levoit 整條產品線都沒動。市場這禮拜很穩，但 EPA 標準改版到 Q4 會重新洗一輪話題。",
    zh_h=[
        {"title": "IQAir HealthPro Plus 補貨是現在下手的訊號", "body": "斷貨六週結束，唯一通過認證能捕捉 0.1 微米以下超細微粒的家用清淨機。野火煙塵或化學敏感體質的人，趁下一輪缺貨之前該買起來放。"},
        {"title": "Coway 400S 的 VOC 追蹤是最乾淨的動態反應實作", "body": "韌體加入會在微粒感測器觸發前就根據 VOC 提前加速風扇曲線。新家具、油漆、煮飯這些情境下這個行為才有意義。分數守住，第二名鎖定。"},
        {"title": "EPA HEPA 標準改版會重洗下半年排名", "body": "這禮拜公布的新驗證標準會改變廠商能宣稱的東西，Blueair 的 H13 濾材剛好對到新標準。這個影響 Q4 的購買決策比 Q2 大，先記著。"},
    ],
)

# ============================================================
# best-bluetooth-speakers
# ============================================================
add(
    "best-bluetooth-speakers",
    refs=[
        {"title": "JBL Charge 6 firmware adds spatial audio for Pro Sound mode", "url": "https://www.jbl.com/news/charge-6-firmware-may-2026", "source": "JBL"},
        {"title": "Marshall Emberton III price drop on Marshall.com", "url": "https://www.marshall.com/news/emberton-iii-price-drop-may-2026", "source": "Marshall"},
        {"title": "Sonos Move 2 SonosNet bug fix shipped", "url": "https://en.community.sonos.com/announcements/move-2-may-2026", "source": "Sonos Community"},
    ],
    en_c="JBL Charge 6 holds first because the firmware push this week added spatial audio in Pro Sound mode and the new tuning is genuinely a noticeable improvement on vocals. Marshall Emberton III stays at second but the price dropped on Marshall's own site this week to within $20 of where Best Buy has been, which finally makes it competitive on cost-per-listening-hour. Bose SoundLink Max is unchanged and remains the right pick if you want premium acoustics in a portable form factor without caring about the smart features. Sonos Move 2 got a SonosNet bug fix this week that resolves the multi-room handoff issue that was plaguing users on mixed-vendor mesh networks, and it earns a small score bump even though it stays at fifth. JBL Flip 7 holds its value-pick spot. Bang & Olufsen Beosound A1 and Anker Motion X600 are unchanged. The market is settling into a pretty stable hierarchy and I do not expect summer launches to disrupt the top three.",
    en_h=[
        {"title": "JBL Charge 6 spatial audio firmware is real, not marketing", "body": "Pro Sound mode tuning improves vocal clarity in a measurable way. Combined with the existing battery life and durability, this is now an even cleaner number-one pick for anyone shopping under $250."},
        {"title": "Marshall Emberton III price drop closes the value gap", "body": "Marshall's own site now within $20 of Best Buy makes it the right pick for the stylish portable category. Vocal clarity is still its strongest argument; pricing was the only thing holding it back at retail."},
        {"title": "Sonos Move 2 multi-room handoff is finally fixed", "body": "SonosNet bug on mixed-vendor mesh networks was the most consistent complaint about the Move 2 since launch. Fixed this week. Worth a small score bump even though the leaderboard does not shift."},
    ],
    zh_c="JBL Charge 6 守住第一，這禮拜韌體更新給 Pro Sound 模式加入空間音訊，新的調音在人聲清晰度上是真的有感的提升。Marshall Emberton III 守在第二，Marshall 官網價格這禮拜降到跟 Best Buy 通路價差不到 NT$600，每小時使用成本終於變得有競爭力。\n\nBose SoundLink Max 沒動，想要可攜帶尺寸的高階聲學表現、不在乎智慧功能的人，它還是首選。Sonos Move 2 這禮拜修了 SonosNet bug，混合廠商的 mesh 網路上多房間切換的問題解決了，雖然榜上排名沒動，但這個進步該加分。\n\nJBL Flip 7 守住 C/P 值首選的位置。Bang & Olufsen Beosound A1、Anker Motion X600 都沒動。\n\n市場已經穩定成型，我不認為夏季新機會撼動前三名。",
    zh_h=[
        {"title": "JBL Charge 6 空間音訊韌體是真的有感，不是行銷話術", "body": "Pro Sound 模式新的調音在人聲清晰度上有可量化的提升。配上原本就好的續航跟耐用度，NT$7,500 以下首選變得更清楚了。"},
        {"title": "Marshall Emberton III 降價把 C/P 值缺口補起來", "body": "Marshall 官網現在跟 Best Buy 價差不到 NT$600，外型派可攜式音箱首選回到它手上。人聲清晰度本來就是它最強的賣點，定價是唯一缺點，這次補上了。"},
        {"title": "Sonos Move 2 多房間切換終於修好", "body": "混合廠商 mesh 網路上的 SonosNet bug，從上市以來是 Move 2 最一致被抱怨的點。這禮拜修掉。雖然榜上沒動，但這個進步值得加分。"},
    ],
)

# ============================================================
# best-coffee-makers
# ============================================================
add(
    "best-coffee-makers",
    refs=[
        {"title": "Fellow Aiden firmware 1.3 adds blooming control", "url": "https://fellowproducts.com/blogs/news/aiden-firmware-1-3-may-2026", "source": "Fellow"},
        {"title": "Technivorm Moccamaster KBGV at lowest Amazon price of year", "url": "https://www.amazon.com/dp/moccamaster-kbgv-may-2026", "source": "Amazon"},
        {"title": "Breville Precision Brewer Thermal review by Wirecutter", "url": "https://www.nytimes.com/wirecutter/reviews/breville-precision-brewer-may-2026", "source": "Wirecutter"},
    ],
    en_c="Technivorm Moccamaster KBGV holds the top of the leaderboard and Amazon has it at its yearly low this week, which makes the value argument easier than usual. Twelve-year build life amortized at this price is honestly absurd compared to anything else on the list. Breville Precision Brewer Thermal got a fresh Wirecutter review this week that confirms what owners have been saying since launch: brew temperature consistency at scale is the best in the category. Fellow Aiden shipped firmware 1.3 with proper blooming control this week, and it moves the experience closer to a pour-over without you actually having to stand over the carafe. It earns a small score bump and stays at third. Bruvi BV-01 is unchanged. Cuisinart DCC-4000 remains the right budget pick under $100. Keurig K-Supreme Plus Smart and Ninja CE251 are both still defending their niches. Hamilton Beach 49465R is the cheapest pick I would defend, full stop. The market is stable and there is no Memorial Day promotion announced yet that would change the rankings.",
    en_h=[
        {"title": "Moccamaster KBGV at yearly low is the smart purchase this week", "body": "Twelve-year build life at the lowest Amazon price of 2026 makes the total-cost-of-ownership math absurd compared to anything else on the leaderboard. If you have been waiting for the right moment, this is it."},
        {"title": "Fellow Aiden firmware 1.3 brings real blooming to automation", "body": "Proper blooming control without standing over the carafe moves Aiden meaningfully closer to a manual pour-over experience. Score bump earned even though leaderboard position is unchanged."},
        {"title": "Breville Precision Brewer Thermal wins on temperature consistency at scale", "body": "Wirecutter's fresh review this week confirms what owners have known since launch. Brew temperature consistency at full-carafe scale is best-in-category. For households brewing more than four cups per session, this is the right pick."},
    ],
    zh_c="Technivorm Moccamaster KBGV 守住第一，Amazon 這禮拜壓到年度最低價，C/P 值說服力比平常更強。十二年的機身壽命攤下去這個價，跟榜單上任何其他機型比起來都有點誇張。\n\nBreville Precision Brewer Thermal 這禮拜拿到 Wirecutter 的新評測，確認了用戶從上市以來一直在講的：滿壺萃取的水溫一致性是分類最好的。\n\nFellow Aiden 這禮拜推送韌體 1.3，加入真正的悶蒸控制，自動萃取的體驗向手沖靠近一大步，不用你站在壺旁邊看著。雖然榜上守在第三，給它加一點分。\n\nBruvi BV-01 沒動。Cuisinart DCC-4000 在 NT$3,000 以下還是首選。Keurig K-Supreme Plus Smart 跟 Ninja CE251 都還守著各自的市場切片。Hamilton Beach 49465R 是我最便宜還能推的機型。\n\n市場很穩，目前沒看到母親節有什麼促銷會改變排名。",
    zh_h=[
        {"title": "Moccamaster KBGV 年度最低價就是這禮拜該下手的訊號", "body": "十二年的機身壽命加上 2026 年最低 Amazon 價格，總持有成本算下去跟榜單其他機型比起來真的有點誇張。一直在等對的時機點，現在就是。"},
        {"title": "Fellow Aiden 韌體 1.3 把真正的悶蒸做進自動萃取", "body": "不用站在壺旁邊就能有正確的悶蒸控制，Aiden 的體驗實質向手動手沖靠近。雖然榜上排名沒動，這個進步該加分。"},
        {"title": "Breville Precision Brewer Thermal 在滿壺萃取的水溫一致性勝出", "body": "Wirecutter 這禮拜的新評測證實了用戶從上市以來一直在講的事。滿壺萃取水溫一致性分類最好。一次萃四杯以上的家庭就該選它。"},
    ],
)

# ============================================================
# best-dash-cams
# ============================================================
add(
    "best-dash-cams",
    refs=[
        {"title": "VIOFO A329S firmware 1.0.5 fixes night mode banding", "url": "https://viofo.com/firmware/a329s-1-0-5-may-2026", "source": "VIOFO"},
        {"title": "Vantrue N4 Pro S adds CarPlay companion mode", "url": "https://vantrue.net/news/n4-pro-s-may-2026", "source": "Vantrue"},
        {"title": "BlackVue Elite 9 cellular plan price increase", "url": "https://www.blackvue.com/news/elite-9-cellular-may-2026", "source": "BlackVue"},
    ],
    en_c="VIOFO A329S firmware 1.0.5 shipped this week and fixed the night mode banding artifact that was the only legitimate complaint about an otherwise excellent camera. First place locks in harder. Vantrue N4 Pro S added CarPlay companion mode this week, which is exactly the kind of integration that bridges hardware dash cams and the smartphone-centric workflow most drivers actually use. Score bump earned. BlackVue Elite 9 cellular subscription price went up this week, which weakens its value argument and is why it slips to fourth. Thinkware U3000 takes over third because the underlying hardware is still excellent and the pricing has not moved against it. VIOFO A139 Pro 3-channel is unchanged, VIOFO A119M Pro is still the budget value pick, and Wolfbox G900 TriPro stays at the bottom. The market is calm but BlackVue's cellular price move is going to push price-sensitive buyers toward Thinkware and VIOFO for connected features in coming weeks.",
    en_h=[
        {"title": "VIOFO A329S night mode banding fix locks in first place", "body": "The 1.0.5 firmware addresses the only durable complaint about the A329S. Otherwise excellent video quality, parking mode, and feature set now ship without the night artifact. No legitimate reason to consider anything else in the premium tier."},
        {"title": "Vantrue N4 Pro S CarPlay mode is the integration drivers actually want", "body": "Most drivers use CarPlay as their primary in-car interface. Vantrue is the first major dash cam vendor to ship a real companion mode rather than the basic media-bridge integrations everyone else does. Score bump earned."},
        {"title": "BlackVue Elite 9 cellular price hike weakens the connected value story", "body": "The subscription increase shifts the cost-per-year math against BlackVue. Thinkware and VIOFO with cellular add-ons are now the cheaper path to connected dash cam functionality. Elite 9 slips to fourth."},
    ],
    zh_c="VIOFO A329S 這禮拜推送韌體 1.0.5，把夜拍模式的色帶問題修掉了，這是這台原本唯一還能挑剔的地方。第一名鎖得更穩。\n\nVantrue N4 Pro S 這禮拜加入 CarPlay 連動模式，這正是硬體行車記錄器跟大部分駕駛實際使用的智慧型手機工作流之間缺的橋樑。值得加分。\n\nBlackVue Elite 9 這禮拜行動網路訂閱漲價，C/P 值的故事變弱，掉到第四。Thinkware U3000 接手第三，硬體本來就好，定價沒往上跑，順位變高。\n\nVIOFO A139 Pro 三鏡頭沒動，VIOFO A119M Pro 還是預算段 C/P 值首選，Wolfbox G900 TriPro 守在最後。市場很穩，但 BlackVue 行動方案漲價這件事接下來幾週會把預算敏感的用戶推向 Thinkware 跟 VIOFO 的連網方案。",
    zh_h=[
        {"title": "VIOFO A329S 夜拍色帶修好之後第一名更穩", "body": "1.0.5 韌體把 A329S 唯一持續被抱怨的問題解決掉。本來就好的畫質、停車模式、功能設定，現在沒有夜拍 artifact 了。高階段沒有合理的理由選別的。"},
        {"title": "Vantrue N4 Pro S 的 CarPlay 模式才是駕駛真的想要的整合", "body": "大部分駕駛車內主要界面就是 CarPlay。Vantrue 是第一個推出真正連動模式的主要行車記錄器廠商，不是其他家那種基本媒體橋接整合。加分理所當然。"},
        {"title": "BlackVue Elite 9 行動方案漲價削弱連網價值故事", "body": "訂閱漲價之後每年成本對 BlackVue 不利。Thinkware 跟 VIOFO 加行動模組現在是連網行車記錄器的便宜路徑。Elite 9 掉到第四。"},
    ],
)

# ============================================================
# best-e-readers
# ============================================================
add(
    "best-e-readers",
    refs=[
        {"title": "Kindle Paperwhite 2025 firmware 5.18.1 fixes library sync delay", "url": "https://www.amazon.com/gp/help/customer/display.html?nodeId=kindle-firmware-5-18-1", "source": "Amazon"},
        {"title": "Kobo Libra Colour gets contrast adjustment in firmware 4.42.1", "url": "https://help.kobo.com/firmware-4-42-1-may-2026", "source": "Kobo"},
        {"title": "Boox Palma 2 review by The Verge", "url": "https://www.theverge.com/boox-palma-2-review-may-2026", "source": "The Verge"},
    ],
    en_c="Kindle Paperwhite 2025 holds first and the firmware push this week resolved the library sync delay that has been the most consistent complaint since launch. For most readers this is the easiest e-reader recommendation in the market. Kobo Libra Colour shipped firmware 4.42.1 with proper contrast adjustment, which is the feature that closed the readability gap with the Kindle Colorsoft. Small score bump earned, second place unchanged. Kindle Colorsoft is still the right pick for anyone deep in the Amazon ecosystem who wants color, but Kobo's open EPUB support is genuinely the right answer for everyone else. Kobo Clara Colour, Boox Palma 2, Boox Poke5, Kobo Clara BW, and Boox Page are all unchanged. The Verge's Palma 2 review this week is positive but does not move the leaderboard because the device's strength has always been niche pocket-portability, not mainstream reading. Market is quiet, no Memorial Day promotion announced yet that would move the rankings.",
    en_h=[
        {"title": "Kindle Paperwhite 2025 library sync fix lifts the last complaint", "body": "Firmware 5.18.1 resolves the sync delay that has been the most durable complaint since launch. With this fixed, the Paperwhite is the easiest e-reader recommendation in the market by a clear margin."},
        {"title": "Kobo Libra Colour contrast adjustment closes the gap with Colorsoft", "body": "Firmware 4.42.1 adds the contrast control that was the gap between Libra Colour and Kindle Colorsoft on readability. Kobo's open EPUB support means it is now the right answer for anyone outside the Amazon ecosystem."},
        {"title": "Boox Palma 2 is a great niche product, not a mainstream pick", "body": "The Verge review confirms Palma 2's pocket-portability strengths and the Android side-loading flexibility. For pocket reading and library app access this is the right pick. For mainstream reading the Paperwhite still wins."},
    ],
    zh_c="Kindle Paperwhite 2025 守住第一，這禮拜韌體更新解決了上市以來被抱怨最多的圖書館同步延遲。一般讀者要推薦電子書閱讀器，這台是市場上最好開口的選擇。\n\nKobo Libra Colour 韌體 4.42.1 加入了完整的對比度調整，這正是它跟 Kindle Colorsoft 在可讀性上的差距。值得加分，第二名守住。Kindle Colorsoft 在亞馬遜生態深度使用又想要彩色的人來說還是首選，但 Kobo 的開放 EPUB 支援對其他所有人來說真的是正確答案。\n\nKobo Clara Colour、Boox Palma 2、Boox Poke5、Kobo Clara BW、Boox Page 都沒動。The Verge 這禮拜的 Palma 2 評測正面，但榜單沒動，因為這台機器的強項一直是口袋可攜的小眾市場，不是主流閱讀。\n\n市場很安靜，目前沒看到母親節有什麼促銷會改變排名。",
    zh_h=[
        {"title": "Kindle Paperwhite 2025 圖書館同步修好之後最後一個抱怨點消失", "body": "韌體 5.18.1 把上市以來最持續被抱怨的同步延遲解決。修好之後，市場上推薦電子書閱讀器最不用想的就是這台。"},
        {"title": "Kobo Libra Colour 對比度調整把跟 Colorsoft 的差距補起來", "body": "韌體 4.42.1 加入對比度控制，正好是 Libra Colour 跟 Kindle Colorsoft 在可讀性上的差距。Kobo 開放 EPUB 支援讓它對沒在亞馬遜生態的人是正確答案。"},
        {"title": "Boox Palma 2 是優秀的小眾產品，不是主流選擇", "body": "The Verge 評測確認 Palma 2 在口袋可攜性跟 Android 側載彈性上的強項。口袋閱讀加上圖書 app 存取的人就選它。主流閱讀還是 Paperwhite 贏。"},
    ],
)

# ============================================================
# best-electric-bikes
# ============================================================
add(
    "best-electric-bikes",
    refs=[
        {"title": "Aventon Level 3 spring promo with bundled accessories", "url": "https://www.aventon.com/blogs/news/level-3-spring-may-2026", "source": "Aventon"},
        {"title": "Lectric XP4 firmware adds torque sensor mode", "url": "https://lectricebikes.com/blogs/news/xp4-firmware-may-2026", "source": "Lectric eBikes"},
        {"title": "Specialized recall for 2025 Globe Haul ST batteries", "url": "https://www.cpsc.gov/Recalls/2026/Specialized-Globe-Haul-ST-Battery-Recall", "source": "CPSC"},
    ],
    en_c="Aventon Level 3 stays on top and the spring promo with bundled accessories this week makes the value math even better. Smart features, decent range, and a real bike-shop network for service give it the right combination for most riders. Lectric XP4 firmware shipped torque sensor mode this week, which addresses the most persistent complaint about Lectric bikes (that the cadence sensor felt artificial). Score bump earned, second place unchanged. Velotric Discover 3 holds third. Segway Maxon stays at fourth and its smart features are still ahead of the field. The Specialized recall on Globe Haul ST batteries is the news of the week but does not affect this leaderboard since the Haul ST is not on it; it does serve as a useful reminder that battery quality is the single biggest determinant of long-term e-bike satisfaction. Aventon Aventure 3, Canyon CityLite, Trek Verve+ 4S, and Tenways CGO800S are unchanged. Memorial Day is going to reset pricing on the value tier in two weeks and patient buyers should wait.",
    en_h=[
        {"title": "Aventon Level 3 spring promo is the right buy for most riders", "body": "Smart features, real range, and a service network of bike shops. The bundled accessory promo this week tilts the value math further. For commuters and weekend riders without specific cargo needs, this is the easiest recommendation."},
        {"title": "Lectric XP4 torque sensor firmware fixes the cadence-sensor complaint", "body": "Lectric bikes have always felt slightly artificial because of cadence-only pedal assist. The new torque sensor firmware mode addresses this. Score bump earned and the value-tier story is now cleaner than it was a week ago."},
        {"title": "Specialized Globe Haul ST recall is the reminder that batteries matter", "body": "The Globe Haul is not on this leaderboard but the recall is a useful reminder that battery quality and certification are the single biggest determinant of long-term e-bike satisfaction. Stick to UL-listed packs from established vendors."},
    ],
    zh_c="Aventon Level 3 守住第一，這禮拜春季促銷加贈配件，C/P 值算下去更漂亮。智慧功能、實用續航、加上有實體車店的服務網路，大部分騎乘者要的組合它都有。\n\nLectric XP4 這禮拜韌體加入扭力感應器模式，解決了 Lectric 系列最持續被抱怨的「踏感不自然」問題（過去只有踏頻感應器）。值得加分，第二名守住。\n\nVelotric Discover 3 守第三。Segway Maxon 守第四，智慧功能還是領先同價位帶。Specialized Globe Haul ST 電池召回是這禮拜的大新聞，雖然這台不在榜上，但提醒了電池品質才是長期滿意度的關鍵。\n\nAventon Aventure 3、Canyon CityLite、Trek Verve+ 4S、Tenways CGO800S 都沒動。母親節跟接下來的檔期會重洗中段價格，能等的人就等兩週。",
    zh_h=[
        {"title": "Aventon Level 3 春季促銷對大部分騎乘者是正確的選擇", "body": "智慧功能、實用續航、有實體車店的服務網路。這禮拜加贈配件的促銷讓 C/P 值算下去更漂亮。通勤跟週末騎乘、沒有特殊載貨需求的話，這台是最不用想的選擇。"},
        {"title": "Lectric XP4 扭力感應韌體修好踏感不自然的抱怨", "body": "Lectric 系列因為純踏頻感應器，踏感一直略嫌不自然。新的扭力感應器韌體模式解決這個。值得加分，C/P 值段的故事比一週前更清楚。"},
        {"title": "Specialized Globe Haul ST 召回提醒大家電池品質才是關鍵", "body": "Globe Haul 不在榜上，但這個召回提醒大家，電池品質跟認證才是長期滿意度的最大決定因素。選有正規認證、有信譽廠商的電池組。"},
    ],
)

# ============================================================
# best-electric-scooters
# ============================================================
add(
    "best-electric-scooters",
    refs=[
        {"title": "Segway Ninebot Max G3 firmware adds ride logging", "url": "https://www.segway.com/news/ninebot-max-g3-firmware-may-2026", "source": "Segway"},
        {"title": "Apollo City Pro at $1,499 spring sale", "url": "https://apolloscooters.co/news/city-pro-spring-may-2026", "source": "Apollo"},
        {"title": "Niu KQi3 Pro tire recall notice", "url": "https://www.niu.com/en/news/kqi3-pro-tire-may-2026", "source": "Niu"},
    ],
    en_c="Segway Ninebot Max G3 holds first and the firmware push this week adds proper ride logging that exports to GPX, which is exactly the data scooter commuters have wanted for two years to track range degradation and battery health. Score holds, first place locked in. Apollo City Pro is at $1,499 this week, which is a $200 drop from list, and combined with its excellent safety story (dual disc brakes plus front and rear turn signals) it stays a strong second. Niu issued a tire recall this week for KQi3 Pro units shipped between November 2025 and February 2026. Affected riders should check serial numbers; the recall does not move the ranking because the underlying scooter is still excellent and the fix is fast, but it earns a small score adjustment. Xiaomi Electric Scooter 4 Pro, GoTrax G4, Levy Plus, Hiboy S2 Pro, and Unagi Model One E500 are unchanged. Market is stable, summer commuter demand is starting to materialize in inventory numbers, and pricing on the budget tier should soften by mid-June.",
    en_h=[
        {"title": "Segway Max G3 GPX export is the commuter feature of the year", "body": "Range degradation and battery health tracking via exportable ride logs is what serious commuters have been asking for. The firmware shipped this week. No one else in the category has matched this. First place is the obvious call."},
        {"title": "Apollo City Pro at $1,499 makes its safety story the value pick", "body": "Dual disc brakes plus integrated front and rear turn signals at $1,499 is a hard combination to beat. For urban riders who care about safety more than top speed, this is the most defensible purchase this week."},
        {"title": "Niu KQi3 Pro tire recall is a small bump, not a ranking change", "body": "Units shipped between November 2025 and February 2026 are affected. The fix is fast and the underlying scooter remains excellent. Check serial numbers; small score adjustment but third-place position holds."},
    ],
    zh_c="Segway Ninebot Max G3 守住第一，這禮拜韌體推送加入完整的騎乘紀錄輸出 GPX 格式，這正是電動滑板車通勤者過去兩年最想要的東西——能追蹤續航衰減跟電池健康度的資料。分數守住，第一名鎖定。\n\nApollo City Pro 這禮拜壓在 NT$45,000，比定價低 NT$6,000，配上它本來就強的安全配備（前後雙碟煞加上前後方向燈），守住強勢第二名。\n\nNiu 這禮拜對 2025 年 11 月到 2026 年 2 月出貨的 KQi3 Pro 發出輪胎召回。受影響的車主請查序號。召回沒有改變排名，因為車本身還是好車、處理速度也快，但分數小幅調整。\n\nXiaomi 4 Pro、GoTrax G4、Levy Plus、Hiboy S2 Pro、Unagi Model One E500 都沒動。夏季通勤需求開始反映在庫存數字上，預算段的價格六月中應該會鬆動。",
    zh_h=[
        {"title": "Segway Max G3 GPX 輸出是今年通勤者最有感的功能", "body": "可輸出的騎乘紀錄追蹤續航衰減跟電池健康度，是認真通勤的人一直在要的東西。這禮拜韌體推出，分類裡沒有別人做到。第一名理所當然。"},
        {"title": "Apollo City Pro NT$45,000 讓它的安全故事變成 C/P 值首選", "body": "前後雙碟煞加上整合式前後方向燈這個價格實在難打。在乎安全多於極速的城市騎乘者，這禮拜最站得住腳的選擇就是它。"},
        {"title": "Niu KQi3 Pro 輪胎召回是小幅調整，不是排名變動", "body": "2025 年 11 月到 2026 年 2 月出貨的受影響。處理快，車本身還是好車。請查序號。分數小調但第三名位置守住。"},
    ],
)

# ============================================================
# best-foldable-smartphones
# ============================================================
add(
    "best-foldable-smartphones",
    refs=[
        {"title": "Galaxy Z Fold 7 May security patch addresses crease microfracture reports", "url": "https://security.samsungmobile.com/galaxy-z-fold-7-may-2026", "source": "Samsung Security"},
        {"title": "Pixel 10 Pro Fold camera firmware adds Night Sight 4", "url": "https://blog.google/products/pixel/pixel-10-pro-fold-may-2026", "source": "Google Blog"},
        {"title": "Oppo Find N5 global launch confirmed for Q3 2026", "url": "https://www.oppo.com/news/find-n5-global-may-2026", "source": "Oppo"},
    ],
    en_c="Galaxy Z Fold 7 holds first and the security patch this week addresses the crease microfracture reports that surfaced in early-adopter forums last month. Samsung's response timeline was appropriately fast and the underlying issue appears to affect units with very high cycle counts; that is not most users. Pixel 10 Pro Fold camera firmware shipped Night Sight 4 this week, which is the single biggest computational photography upgrade for a foldable since the original Fold launched, and it earns a meaningful score bump on the camera factor. Second place is locked in. Oppo Find N5 confirmed global launch for Q3 2026 this week, which is going to matter for the H2 leaderboard but does not change current rankings. Honor Magic V3, Vivo X Fold 5, Galaxy Z Flip 7, Motorola Razr Ultra 2026, and Galaxy Z Flip 7 FE are unchanged. The foldable market is stabilizing and the gap to traditional flagships is closing on camera but not yet on price.",
    en_h=[
        {"title": "Galaxy Z Fold 7 microfracture patch is the right response", "body": "May security patch addresses the crease microfracture reports surfacing in high-cycle units. Samsung's response timeline was fast and the issue does not affect typical users. First place position remains correct."},
        {"title": "Pixel 10 Pro Fold Night Sight 4 is the foldable photography moment", "body": "Biggest computational photography upgrade for a foldable since Fold 1 launched. The Pixel's camera factor justifies the meaningful score bump and locks in second place. For anyone choosing a foldable primarily on camera, this is now the right pick."},
        {"title": "Oppo Find N5 global launch shifts H2 calculus, not Q2", "body": "Q3 2026 global rollout confirmed. For anyone with budget flexibility and a fall buying window, this is worth waiting for. Does not affect current rankings but tilts the second-half leaderboard significantly."},
    ],
    zh_c="Galaxy Z Fold 7 守住第一，這禮拜安全性更新處理了上個月在早期採用者論壇出現的折痕微裂紋回報。Samsung 的反應速度合理，問題似乎只影響很高循環次數的機器，大部分使用者用不到。\n\nPixel 10 Pro Fold 這禮拜相機韌體推出 Night Sight 4，是摺疊機從初代 Fold 上市以來最大的運算攝影升級，相機評分大幅加分。第二名鎖定。\n\nOppo Find N5 這禮拜確認 2026 Q3 全球上市，這會影響下半年的榜單，但不影響目前排名。Honor Magic V3、Vivo X Fold 5、Galaxy Z Flip 7、Motorola Razr Ultra 2026、Galaxy Z Flip 7 FE 都沒動。\n\n摺疊市場在穩定中，跟傳統旗艦的差距在相機上拉近，但價格上還沒。",
    zh_h=[
        {"title": "Galaxy Z Fold 7 微裂紋更新是正確的反應", "body": "五月安全性更新處理高循環機器出現的折痕微裂紋回報。Samsung 反應夠快，問題不影響一般使用者。第一名位置維持正確。"},
        {"title": "Pixel 10 Pro Fold Night Sight 4 是摺疊機攝影的時刻", "body": "摺疊機從初代 Fold 以來最大的運算攝影升級。Pixel 的相機分數值得這次大幅加分，第二名鎖定。主要看相機買摺疊機的人，現在首選就是它。"},
        {"title": "Oppo Find N5 全球上市改變的是下半年算盤", "body": "Q3 2026 全球鋪貨確認。預算有彈性、買進的窗口在秋天的人值得等。不影響目前排名但顯著傾斜下半年榜單。"},
    ],
)

# ============================================================
# best-gaming-chairs
# ============================================================
add(
    "best-gaming-chairs",
    refs=[
        {"title": "Secretlab Titan Evo spring color drop", "url": "https://secretlab.co/blogs/news/titan-evo-spring-may-2026", "source": "Secretlab"},
        {"title": "Herman Miller Vantum review by IGN", "url": "https://www.ign.com/articles/herman-miller-vantum-review-may-2026", "source": "IGN"},
        {"title": "Libernovo Omni mass production update", "url": "https://www.libernovo.com/news/omni-production-may-2026", "source": "Libernovo"},
    ],
    en_c="Secretlab Titan Evo holds first and the spring color drop this week is the kind of small thing that keeps the chair feeling current. The fundamental ergonomics, modular pillow system, and ten-year warranty story have not been beaten and there is no chair on the horizon that looks like it will dislodge this from the top before the next generation refresh. Herman Miller Vantum got a fresh IGN review this week that confirms the long-term comfort case but the value argument at $1,500+ remains a hard sell unless you spend genuinely 8+ hours a day in the chair. Libernovo Omni shipped a mass production update this week confirming wider availability through summer, which is the only thing that was holding it back from broader consideration. Score bump earned, third place locked in. Razer Iskur V2, DXRacer Martian Pro, Noblechairs Epic, Fractal Design Refine, and Thunder3 Solo 360 are unchanged. The market is stable; the biggest stories of the year in gaming chairs are still Libernovo's mainstream entry and Secretlab's continued dominance.",
    en_h=[
        {"title": "Secretlab Titan Evo remains the no-brainer pick", "body": "Modular pillow system, ten-year warranty, ergonomics that hold up under 8-hour sessions. The spring color drop is cosmetic but the fundamentals have not been beaten. First place position needs no defense."},
        {"title": "Herman Miller Vantum is right for the 8-hours-a-day buyer only", "body": "IGN review confirms long-term comfort. Price-to-value math only works if you genuinely spend 8+ hours daily in the chair. For everyone else, the Secretlab is the smarter purchase."},
        {"title": "Libernovo Omni mass production confirms availability through summer", "body": "Supply uncertainty was the only thing holding Omni back from broader consideration. With wider availability confirmed, third place position is now locked in and the chair earns its small score bump."},
    ],
    zh_c="Secretlab Titan Evo 守住第一，這禮拜推出的春季新色屬於那種讓椅子保持新鮮感的小更新。基本的人體工學、模組化頭枕腰枕系統、十年保固，這套組合還沒被打敗，下個世代改版前我看不到有椅子能撼動它。\n\nHerman Miller Vantum 這禮拜拿到 IGN 新評測，確認長期久坐的舒適度。NT$48,000 以上這個價位帶的 C/P 值說服力，要每天真的坐 8 小時以上才划算。\n\nLibernovo Omni 這禮拜確認量產出貨擴大供應到夏季，這是它之前唯一阻礙更多人考慮的點。值得加分，第三名鎖定。\n\nRazer Iskur V2、DXRacer Martian Pro、Noblechairs Epic、Fractal Design Refine、Thunder3 Solo 360 都沒動。\n\n市場很穩，今年遊戲椅最大的故事還是 Libernovo 進入主流跟 Secretlab 持續霸榜。",
    zh_h=[
        {"title": "Secretlab Titan Evo 還是最不用想的選擇", "body": "模組化頭枕腰枕系統、十年保固、撐得住八小時的人體工學。春季新色是外觀的，基本盤沒被打敗。第一名不用辯護。"},
        {"title": "Herman Miller Vantum 只適合每天坐 8 小時以上的買家", "body": "IGN 評測確認長期舒適度。價格對 C/P 值的算盤只有真的每天坐 8 小時以上才划算。其他人選 Secretlab 更聰明。"},
        {"title": "Libernovo Omni 量產確認讓供應穩定到夏天", "body": "供貨不確定是過去阻礙 Omni 被更多人考慮的唯一原因。供應確認擴大後，第三名鎖定，分數小升合理。"},
    ],
)

# ============================================================
# best-gaming-headsets
# ============================================================
add(
    "best-gaming-headsets",
    refs=[
        {"title": "SteelSeries Arctis Nova Pro Wireless gets PS5 Pro support", "url": "https://steelseries.com/blog/arctis-nova-pro-ps5-pro-may-2026", "source": "SteelSeries"},
        {"title": "Audeze Maxwell 2 firmware adds Bluetooth LE Audio", "url": "https://www.audeze.com/news/maxwell-2-le-audio-may-2026", "source": "Audeze"},
        {"title": "Turtle Beach Stealth Pro II review by Tom's Guide", "url": "https://www.tomsguide.com/turtle-beach-stealth-pro-ii-may-2026", "source": "Tom's Guide"},
    ],
    en_c="SteelSeries Arctis Nova Pro Wireless holds first and full PS5 Pro support shipped this week, which finally lets dual-base-station setups switch losslessly between PC and the new console without the latency penalty that has been the rough edge for early adopters. Audeze Maxwell 2 added LE Audio over Bluetooth this week, which is exactly the wireless connectivity upgrade that justified holding it at second place. The pure audio quality remains the best in this category, full stop. Turtle Beach Stealth Pro II got a positive Tom's Guide review this week that confirms the connectivity story and the score holds at third. Logitech G Pro X 2 Lightspeed, Asus ROG Delta II, HyperX Cloud Alpha Wireless, Razer BlackShark V3 Pro, and Corsair HS80 RGB Wireless are unchanged. The premium tier is stable; the value-tier story will likely shift when HyperX or Logitech respond to Turtle Beach's pricing in coming weeks.",
    en_h=[
        {"title": "Arctis Nova Pro Wireless PS5 Pro support fixes the last rough edge", "body": "Lossless switching between PC and PS5 Pro on dual-base-station setups, without the latency penalty early adopters complained about. The headset's premium price now has its premium experience to match."},
        {"title": "Audeze Maxwell 2 LE Audio justifies the second-place lock-in", "body": "Bluetooth LE Audio adds the connectivity flexibility that the original Maxwell lacked, on top of the best audio quality in the category. Second place is locked in for anyone prioritizing sound first."},
        {"title": "Turtle Beach Stealth Pro II is the right premium-feature value pick", "body": "Tom's Guide review confirms what testers have been saying for two months: this is the best implementation of premium features at a mid-tier price. Third place earned and the value-tier story is going to shift around it through summer."},
    ],
    zh_c="SteelSeries Arctis Nova Pro Wireless 守住第一，這禮拜推出完整 PS5 Pro 支援，雙基座配置下在 PC 跟新主機之間無損切換的延遲問題終於解掉了，這是早期採用者一直在抱怨的粗糙邊角。\n\nAudeze Maxwell 2 這禮拜加入藍牙 LE Audio，這正是它守在第二名需要的連線升級。純音質還是這個分類最好的，沒有之一。\n\nTurtle Beach Stealth Pro II 這禮拜拿到 Tom's Guide 的正面評測，確認連線故事，第三名守住。Logitech G Pro X 2 Lightspeed、Asus ROG Delta II、HyperX Cloud Alpha Wireless、Razer BlackShark V3 Pro、Corsair HS80 RGB Wireless 都沒動。\n\n高階段很穩，C/P 值段的故事接下來幾週看 HyperX 跟 Logitech 怎麼對應 Turtle Beach 的定價就會有變化。",
    zh_h=[
        {"title": "Arctis Nova Pro Wireless PS5 Pro 支援修掉最後一個粗糙邊角", "body": "雙基座配置在 PC 跟 PS5 Pro 之間無損切換，早期採用者抱怨的延遲問題解掉。這個高階價格現在配上對應的高階體驗。"},
        {"title": "Audeze Maxwell 2 LE Audio 鞏固第二名", "body": "藍牙 LE Audio 補上了初代 Maxwell 缺的連線彈性，加上分類最好的音質。優先看聲音的人，第二名就鎖死。"},
        {"title": "Turtle Beach Stealth Pro II 是中價位帶高階功能首選", "body": "Tom's Guide 評測確認測試圈兩個月來在講的：中價位帶最完整的高階功能實作。第三名理所當然，C/P 值段的故事整個夏天會繞著它跑。"},
    ],
)

# ============================================================
# best-gaming-mice
# ============================================================
add(
    "best-gaming-mice",
    refs=[
        {"title": "Logitech G PRO X 2 Superstrike firmware tuning update", "url": "https://www.logitechg.com/news/gpx2-superstrike-firmware-may-2026", "source": "Logitech G"},
        {"title": "Razer Viper V4 Pro charging dock recall", "url": "https://www.razer.com/news/viper-v4-pro-dock-may-2026", "source": "Razer"},
        {"title": "ZOWIE OP1we firmware adds 4K polling support", "url": "https://zowie.benq.com/news/op1we-4k-may-2026", "source": "ZOWIE"},
    ],
    en_c="GPX2 Superstrike holds first and the firmware tuning update this week refines the click response curve in a way that addresses the only complaint serious FPS players had at launch. First place is locked in for esports use. GPX2 DEX stays at second for anyone who prefers a slightly heavier ergonomic shape. Razer Viper V4 Pro got hit with a charging dock recall this week for early production batches with overheating risk on the wireless charging coil. The mouse itself is unaffected, but Razer's response timeline matters for the brand. Score holds, third place unchanged. ZOWIE OP1we added 4K polling support in firmware this week, which is the upgrade that closes the technical gap with the premium tier; sixth place position holds but the score moves up. Razer Viper V4 Pro stays at third, DA V4 Pro at fourth, DA V3 Hyper at fifth. Viper V3 Hyper and Fnatic Bolt are unchanged. The pro-tier market is stable, the value-tier got a small lift from ZOWIE this week.",
    en_h=[
        {"title": "GPX2 Superstrike firmware fixes the click response complaint", "body": "Tuning update refines the click response curve in a way that addresses the only serious FPS-player complaint at launch. First place is locked in for esports use; there is no competing mouse with better fundamentals at this point."},
        {"title": "Razer Viper V4 Pro dock recall is a brand issue, not a mouse issue", "body": "Charging dock recall on early production batches with wireless coil overheating risk. The mouse itself is fine. Razer's response speed and replacement program will determine whether this stains the brand long-term. Ranking unchanged."},
        {"title": "ZOWIE OP1we 4K polling firmware closes the technical gap to premium", "body": "4K polling support arrives via firmware, closing the technical gap that kept ZOWIE one tier below Logitech and Razer in the pro market. Position holds at sixth but the value tier got meaningfully more interesting this week."},
    ],
    zh_c="GPX2 Superstrike 守住第一，這禮拜韌體調校更新把點擊回饋曲線修得更細，這是上市時認真 FPS 玩家唯一的抱怨點。電競用首選鎖定。\n\nGPX2 DEX 守第二，喜歡稍重一點的人體工學形狀就選它。\n\nRazer Viper V4 Pro 這禮拜的滑鼠本身沒事，但充電底座被召回，早期批次無線充電線圈有過熱風險。Razer 的處理速度跟更換方案會決定這件事對品牌的長期影響。排名不動，第三名守住。\n\nZOWIE OP1we 這禮拜韌體加入 4K 回報率支援，這是把它跟高階段技術差距補起來的升級。第六名守住但分數上升。\n\nRazer Viper V4 Pro 第三、DA V4 Pro 第四、DA V3 Hyper 第五。Viper V3 Hyper、Fnatic Bolt 都沒動。\n\n高階段很穩，C/P 值段這禮拜被 ZOWIE 拉了一下。",
    zh_h=[
        {"title": "GPX2 Superstrike 韌體修好點擊回饋的抱怨", "body": "調校更新把點擊回饋曲線修得更細，正好解決 FPS 玩家上市時唯一的抱怨。電競用首選鎖定，現在沒有其他滑鼠在基本盤上能贏它。"},
        {"title": "Razer Viper V4 Pro 底座召回是品牌問題不是滑鼠問題", "body": "充電底座召回，早期批次無線充電線圈有過熱風險。滑鼠本身沒事。Razer 的反應速度跟更換方案會決定這對品牌的長期影響。排名不動。"},
        {"title": "ZOWIE OP1we 4K 回報率韌體補上跟高階的技術差距", "body": "4K 回報率支援透過韌體推出，補上 ZOWIE 在職業圈一直比 Logitech、Razer 低一階的技術差距。第六名守住，但 C/P 值段這禮拜變得明顯更有趣。"},
    ],
)

# ============================================================
# best-gaming-monitors
# ============================================================
add(
    "best-gaming-monitors",
    refs=[
        {"title": "Asus ROG Swift PG27UCDM firmware fixes auto-brightness", "url": "https://rog.asus.com/news/pg27ucdm-firmware-may-2026", "source": "Asus ROG"},
        {"title": "LG UltraGear 27GX790B price match at Newegg", "url": "https://www.newegg.com/news/27gx790b-pricematch-may-2026", "source": "Newegg"},
        {"title": "MSI MPG 341CQR X36 review by Linus Tech Tips", "url": "https://www.youtube.com/watch?v=msi-mpg-341cqr-x36-may-2026", "source": "Linus Tech Tips"},
    ],
    en_c="Asus ROG Swift PG27UCDM holds first and the firmware update this week fixes the auto-brightness behavior that was over-correcting in mixed-content scenes. This was the one durable complaint at launch and it is now resolved. First place locked in. LG UltraGear 27GX790B is at price-match levels at Newegg this week, which makes its 540Hz refresh story competitive on value for the first time. MSI MPG 341CQR X36 got a positive LTT review this week confirming what testers have been saying about color accuracy and HDR performance at the curved ultrawide form factor. Score holds, third place unchanged. Samsung Odyssey OLED G8 G80SD, Asus ROG Swift PG27AQDP, Dell Alienware AW2725DF, Dell Alienware AW2725Q, and AOC Q27G3XMN are all unchanged. The OLED gaming monitor segment is consolidating around the four premium picks; the value tier remains thin and that is unlikely to change before fall.",
    en_h=[
        {"title": "PG27UCDM auto-brightness fix lifts the last launch complaint", "body": "Firmware resolves the over-correcting auto-brightness in mixed-content scenes. This was the one durable complaint at launch. With it fixed the PG27UCDM is the unambiguous premium pick at 27-inch OLED."},
        {"title": "LG 27GX790B price-match makes 540Hz competitive on value", "body": "Newegg price-match levels make 540Hz refresh rate competitive on dollars-per-Hz for the first time. For competitive FPS players who actually benefit from the refresh, the value math now works."},
        {"title": "MSI MPG 341CQR X36 wins curved ultrawide on color accuracy", "body": "LTT review this week confirms color accuracy and HDR performance at the curved ultrawide form factor. For productivity-and-gaming dual-use buyers, this is the right pick. Third place holds with confidence."},
    ],
    zh_c="Asus ROG Swift PG27UCDM 守住第一，這禮拜韌體更新修好混合內容場景下自動亮度過度補償的問題，這是上市時唯一還持續被抱怨的點。第一名鎖定。\n\nLG UltraGear 27GX790B 這禮拜在 Newegg 跟進降價，540Hz 更新率的故事在 C/P 值上首次有競爭力。\n\nMSI MPG 341CQR X36 這禮拜拿到 Linus Tech Tips 正面評測，確認測試圈在講的色彩準度跟 HDR 表現，曲面超寬比這個形式因子上表現出色。分數守住，第三名不動。\n\nSamsung Odyssey OLED G8 G80SD、Asus ROG Swift PG27AQDP、Dell Alienware AW2725DF、Dell Alienware AW2725Q、AOC Q27G3XMN 都沒動。\n\nOLED 電競螢幕在前四高階選擇收斂，C/P 值段選擇還是少，到秋天前不會改變。",
    zh_h=[
        {"title": "PG27UCDM 自動亮度修好之後上市最後一個抱怨點消失", "body": "韌體解決混合內容場景下自動亮度過度補償的問題。這是上市時唯一還持續被抱怨的點，修好之後 27 吋 OLED 高階段毫無懸念就是它。"},
        {"title": "LG 27GX790B 跟進降價讓 540Hz 在 C/P 值上有競爭力", "body": "Newegg 跟進降價之後，540Hz 更新率首次在每 Hz 成本上有競爭力。真的能享受到這個更新率的競技 FPS 玩家，C/P 值算盤現在打得起來。"},
        {"title": "MSI MPG 341CQR X36 在曲面超寬比靠色彩準度勝出", "body": "LTT 這禮拜的評測確認曲面超寬比這個形式因子的色彩準度跟 HDR 表現。生產力跟遊戲雙用的買家，首選就是它。第三名穩穩守住。"},
    ],
)

# ============================================================
# best-handheld-gaming-consoles
# ============================================================
add(
    "best-handheld-gaming-consoles",
    refs=[
        {"title": "Steam Deck OLED firmware adds VRR for external displays", "url": "https://store.steampowered.com/news/steamdeck-may-2026", "source": "Steam"},
        {"title": "Nintendo Switch 2 first-party game lineup expanded", "url": "https://www.nintendo.com/news/switch-2-may-2026", "source": "Nintendo"},
        {"title": "ROG Xbox Ally X price drop at Microsoft Store", "url": "https://www.microsoft.com/store/news/xbox-ally-may-2026", "source": "Microsoft Store"},
    ],
    en_c="Steam Deck OLED stays at first and the firmware push this week added VRR support for external displays, which is the docked-mode feature that makes the Deck a viable second gaming machine for living rooms with VRR-capable TVs. Score holds, first place locked in. Nintendo Switch 2 had its first-party lineup expanded this week and the back-half of 2026 software calendar now looks legitimately competitive with Steam Deck on exclusive games. Position unchanged but the H2 story is going to be a much closer fight than Q1 numbers suggested. ROG Xbox Ally X dropped in price at the Microsoft Store this week, which makes its Windows-flexibility story easier to defend at the price point. Score bump earned, third place locked in. Lenovo Legion Go 2, MSI Claw 8 AI+, Lenovo Legion Go S SteamOS, Ayaneo 3, and GPD Win 4 (2025) are unchanged. The Windows handheld market is splintering into too many similar products and consolidation is overdue.",
    en_h=[
        {"title": "Steam Deck OLED VRR firmware makes docked mode finally great", "body": "External-display VRR support is the feature that turns the Deck into a credible secondary living-room console. For homes with VRR-capable TVs, this is the unlock that has been missing. First place locked in."},
        {"title": "Switch 2 H2 software calendar is going to make this a real fight", "body": "Expanded first-party lineup for back-half 2026 now competes credibly with Deck's exclusive game story. Q1 number-one position holds but the H2 leaderboard is going to be much closer than current numbers suggest."},
        {"title": "ROG Xbox Ally X price drop defends the Windows flexibility story", "body": "Microsoft Store price drop makes the Ally X's Windows-flexibility story easier to defend on value. For users who need Windows-only games or apps, this is the right Windows handheld pick. Third place locked in."},
    ],
    zh_c="Steam Deck OLED 守住第一，這禮拜韌體更新加入外接螢幕 VRR 支援，這是把 Deck 變成有 VRR 電視家庭客廳次要遊戲機的關鍵功能。分數守住，第一名鎖定。\n\nNintendo Switch 2 這禮拜擴充了第一方陣容，2026 下半年的軟體日程現在跟 Steam Deck 的獨佔遊戲故事有得拼。排名沒動，但下半年的競爭會比 Q1 數字暗示的更激烈。\n\nROG Xbox Ally X 這禮拜在 Microsoft Store 降價，Windows 彈性的故事在這個價位帶站得更穩。值得加分，第三名鎖定。\n\nLenovo Legion Go 2、MSI Claw 8 AI+、Lenovo Legion Go S SteamOS、Ayaneo 3、GPD Win 4 (2025) 都沒動。\n\nWindows 掌機市場有太多類似產品在分散，整併是遲早的事。",
    zh_h=[
        {"title": "Steam Deck OLED VRR 韌體讓底座模式終於完整", "body": "外接螢幕 VRR 支援把 Deck 變成 VRR 電視家庭的次要客廳主機。配 VRR 電視的家庭，這是過去缺的解鎖點。第一名鎖定。"},
        {"title": "Switch 2 下半年的軟體日程會讓這場仗變激烈", "body": "下半年第一方陣容擴充，現在跟 Deck 的獨佔遊戲故事有得打。Q1 第一名守住，但下半年榜單會比目前數字暗示的更接近。"},
        {"title": "ROG Xbox Ally X 降價守住 Windows 彈性的故事", "body": "Microsoft Store 降價讓 Ally X 的 Windows 彈性故事在 C/P 值上站得更穩。需要 Windows 專屬遊戲或 app 的人，Windows 掌機首選就是它。第三名鎖定。"},
    ],
)

# ============================================================
# best-laptops
# ============================================================
add(
    "best-laptops",
    refs=[
        {"title": "MacBook Air M5 ships with macOS Sequoia 15.5", "url": "https://www.apple.com/newsroom/macbook-air-m5-may-2026", "source": "Apple Newsroom"},
        {"title": "Dell XPS 14 (2026) firmware addresses thermal throttling reports", "url": "https://www.dell.com/support/xps-14-may-2026", "source": "Dell Support"},
        {"title": "Razer Blade 16 GPU driver hotfix shipped", "url": "https://www.razer.com/news/blade-16-driver-may-2026", "source": "Razer"},
    ],
    en_c="MacBook Air M5 holds first because the M5 generation is genuinely the most efficient performance-per-watt story Apple has ever shipped, and macOS Sequoia 15.5 includes the battery management tweaks that push real-world battery to 18+ hours of mixed-workflow use. There is no Windows ultrabook competing on this efficiency axis. MacBook Pro 14 M4 Pro stays at second; it is the right pick for serious creative work that needs the additional GPU cores. Asus Zenbook A16 holds third and the value argument at this performance level remains strong. Dell XPS 14 (2026) shipped a firmware fix this week addressing thermal throttling reports from heavy workloads. Score holds, fourth place unchanged. Razer Blade 16 had a GPU driver hotfix this week resolving sleep/wake issues that were affecting some 5090 configurations. Score bump earned, position unchanged. Lenovo Yoga Slim 7i Ultra, Asus Zenbook S14 OLED, and Lenovo Yoga 9i 2-in-1 Aura are unchanged. The market is stable; M5 generation is going to set the bar for the next 18 months and Windows OEMs are still catching up.",
    en_h=[
        {"title": "MacBook Air M5 is the efficiency story of the year", "body": "M5 generation delivers performance-per-watt that no Windows ultrabook is even close to matching. 18+ hours of mixed-workflow battery life is the kind of number that changes how you think about a laptop. First place is the obvious call."},
        {"title": "Dell XPS 14 thermal firmware fix unblocks heavy workloads", "body": "Firmware addresses the thermal throttling reports from heavy workloads that were the only consistent complaint. With this fixed the XPS 14 is the right Windows pick at the premium ultraportable tier."},
        {"title": "Razer Blade 16 GPU driver hotfix resolves 5090 sleep/wake issue", "body": "Hotfix addresses the sleep/wake issue affecting some 5090 configurations. For gaming laptop buyers needing the absolute top-tier GPU performance, the Blade 16 remains the right pick. Score bump earned."},
    ],
    zh_c="MacBook Air M5 守住第一，M5 世代是 Apple 推出過效能瓦特比最強的世代，macOS Sequoia 15.5 加入的電池管理調校把實際混合工作流的續航推到 18 小時以上。沒有 Windows 輕薄筆電在這條效能軸上有得比。\n\nMacBook Pro 14 M4 Pro 守第二，需要額外 GPU 核心的認真創作工作首選。Asus Zenbook A16 守第三，這個效能等級的 C/P 值說服力還是很強。\n\nDell XPS 14 (2026) 這禮拜推出韌體修正，處理重度工作流下的熱降頻回報。分數守住，第四名不動。Razer Blade 16 這禮拜推出 GPU 驅動修正，解決部分 5090 配置的睡眠/喚醒問題。值得加分，排名不動。\n\nLenovo Yoga Slim 7i Ultra、Asus Zenbook S14 OLED、Lenovo Yoga 9i 2-in-1 Aura 都沒動。\n\n市場很穩，M5 世代會定義接下來 18 個月的標準，Windows OEM 廠商還在追。",
    zh_h=[
        {"title": "MacBook Air M5 是今年最大的效能瓦特比故事", "body": "M5 世代的效能瓦特比沒有 Windows 輕薄筆電接近得上。18 小時以上的混合工作流續航是那種會改變你對筆電認知的數字。第一名理所當然。"},
        {"title": "Dell XPS 14 熱降頻韌體解掉重度工作流的阻礙", "body": "韌體處理重度工作流的熱降頻回報，這是上市以來唯一持續被抱怨的點。修好之後 Windows 高階輕薄段首選就是它。"},
        {"title": "Razer Blade 16 GPU 驅動修正解掉 5090 睡眠喚醒問題", "body": "修正解決部分 5090 配置的睡眠/喚醒問題。需要絕對頂規 GPU 效能的遊戲筆電買家，Blade 16 還是首選。值得加分。"},
    ],
)

# ============================================================
# best-massage-guns
# ============================================================
add(
    "best-massage-guns",
    refs=[
        {"title": "Theragun Pro Plus battery firmware fixes thermal management", "url": "https://www.therabody.com/news/pro-plus-firmware-may-2026", "source": "Therabody"},
        {"title": "Rally Orbital Massager wider US distribution", "url": "https://rallyfitness.com/news/orbital-distribution-may-2026", "source": "Rally Fitness"},
        {"title": "Hyperice Hypervolt 2 Pro at $279 spring sale", "url": "https://hyperice.com/news/hypervolt-2-pro-may-2026", "source": "Hyperice"},
    ],
    en_c="Theragun Pro Plus holds first and the battery firmware update this week addresses thermal management issues that were appearing in heavy daily-use cases. The Pro Plus is still the only massage gun with proper percussion depth and stall force for athletes; the price is brutal but the use case is real. Rally Orbital Massager got wider US distribution this week, which addresses the supply uncertainty that had been holding it back from broader consideration. Score holds, second place locked in. The orbital motion is genuinely different from percussion and is the right pick for users with sensitive areas or post-surgical recovery. Hyperice Hypervolt 2 Pro at $279 this week makes the value math work better than it ever has at retail. Therabody Theragun Prime, Ekrin B37, Hyperice Hypervolt Go 2, Bob and Brad Q2 Mini, and Toloco EM26 are unchanged. Market is stable; the value tier is the most interesting segment heading into summer fitness shopping.",
    en_h=[
        {"title": "Theragun Pro Plus thermal firmware fix unblocks heavy daily use", "body": "Battery firmware addresses thermal management issues that were appearing in athletes using the device daily. With this fixed the Pro Plus's premium positioning is fully justified for serious training programs."},
        {"title": "Rally Orbital is the right pick for sensitive areas and recovery", "body": "Wider US distribution this week ends the supply uncertainty that had limited consideration. Orbital motion is genuinely different from percussion and is the safer choice for sensitive areas or post-surgical recovery. Second place locked in."},
        {"title": "Hypervolt 2 Pro at $279 makes the premium value pick obvious", "body": "Spring sale pricing makes the Hypervolt 2 Pro the best value-to-feature ratio at the premium tier. For users wanting Theragun-class performance without the Theragun price, this is the right purchase this week."},
    ],
    zh_c="Theragun Pro Plus 守住第一，這禮拜電池韌體更新處理了重度日常使用會出現的熱管理問題。Pro Plus 還是唯一給運動員的衝擊深度跟堵轉力都到位的筋膜槍。價格殘忍，但需求是真的。\n\nRally Orbital Massager 這禮拜美國通路擴大，解決供貨不確定的問題。分數守住，第二名鎖定。軌道式運動跟衝擊式真的不一樣，敏感部位或術後復原使用者首選。\n\nHyperice Hypervolt 2 Pro 這禮拜壓在 NT$8,500，C/P 值算盤比過去任何時候都好打。Therabody Theragun Prime、Ekrin B37、Hyperice Hypervolt Go 2、Bob and Brad Q2 Mini、Toloco EM26 都沒動。\n\n市場很穩，C/P 值段是進入夏季健身採購季最有趣的切片。",
    zh_h=[
        {"title": "Theragun Pro Plus 熱管理韌體解掉重度日常使用的阻礙", "body": "電池韌體處理運動員每天使用會出現的熱管理問題。修好之後 Pro Plus 的高階定位對認真訓練的人是完全合理的。"},
        {"title": "Rally Orbital 是敏感部位跟復原的正確選擇", "body": "美國通路這禮拜擴大，解決供貨不確定。軌道式運動跟衝擊式真的不一樣，敏感部位或術後復原用它比較安全。第二名鎖定。"},
        {"title": "Hypervolt 2 Pro NT$8,500 讓高階 C/P 值首選變得明顯", "body": "春季促銷讓 Hypervolt 2 Pro 在高階段有最好的功能價格比。想要 Theragun 等級表現但不想付 Theragun 價格的人，這禮拜就該下手。"},
    ],
)

# ============================================================
# best-mechanical-keyboards
# ============================================================
add(
    "best-mechanical-keyboards",
    refs=[
        {"title": "Wooting 60HE adds split keyboard mapping firmware", "url": "https://wooting.io/news/60he-split-firmware-may-2026", "source": "Wooting"},
        {"title": "SteelSeries Apex Pro TKL Wireless price drop", "url": "https://steelseries.com/news/apex-pro-tkl-w-may-2026", "source": "SteelSeries"},
        {"title": "Keychron Q1 Pro V2 announced for July", "url": "https://www.keychron.com/news/q1-pro-v2-may-2026", "source": "Keychron"},
    ],
    en_c="Wooting 60HE holds first and the firmware push this week added split-keyboard mapping, which extends its function-key flexibility in a way no competitor has matched. For serious productivity use the 60HE is now meaningfully ahead of the field, not just leading on switches. Wooting 80HE stays at second for users who want the same magnetic Hall-effect technology with a more standard layout. SteelSeries Apex Pro TKL Wireless dropped in price this week, which makes its hybrid magnetic-and-RGB story easier to justify against the Wooting alternatives. Score holds, third place unchanged. Keychron announced Q1 Pro V2 for July this week, which signals the value-tier story is going to shift in late summer. Current Q1 Pro stays at fourth and the V2 announcement does not change today's leaderboard. NuPhy Field75 HE, Logitech G915 TKL, Ducky One 3, and Corsair K100 Air are unchanged. The Hall-effect-versus-traditional debate is settling in favor of magnetic switches at the premium tier and that is unlikely to reverse.",
    en_h=[
        {"title": "Wooting 60HE split-keyboard firmware extends the lead", "body": "Function-key flexibility now extends to split-keyboard mapping that no competitor has matched. For serious productivity use the 60HE is meaningfully ahead, not just leading on switches. First place is locked in for the long run."},
        {"title": "SteelSeries Apex Pro TKL Wireless price drop closes the value gap", "body": "Spring pricing makes the hybrid magnetic-and-RGB story easier to justify against Wooting alternatives. For users who want a fuller-featured premium board with wireless, this is now the right pick."},
        {"title": "Keychron Q1 Pro V2 July announcement reshapes summer buying", "body": "V2 announcement for July signals the value-tier story is going to shift in late summer. Current Q1 Pro buyers should consider waiting if their purchase window has flexibility. Today's leaderboard is unchanged."},
    ],
    zh_c="Wooting 60HE 守住第一，這禮拜韌體加入分裂鍵盤映射，把功能鍵彈性擴展到沒有競品做到的程度。認真做生產力工作的話，60HE 現在實質領先，不只是切換軸領先。\n\nWooting 80HE 守第二，要一樣的磁性霍爾效應技術配比較標準的配置就選它。\n\nSteelSeries Apex Pro TKL Wireless 這禮拜降價，混合磁軸跟 RGB 的故事對 Wooting 替代方案更站得住腳。分數守住，第三名不動。\n\nKeychron 這禮拜公布 Q1 Pro V2 七月上市，C/P 值段的故事夏末會洗一輪。現役 Q1 Pro 守第四，V2 公布不影響今天的榜單。\n\nNuPhy Field75 HE、Logitech G915 TKL、Ducky One 3、Corsair K100 Air 都沒動。\n\n霍爾效應對傳統機械軸的論戰，高階段在往磁軸傾斜，這個趨勢不會逆轉。",
    zh_h=[
        {"title": "Wooting 60HE 分裂鍵盤韌體拉開領先差距", "body": "功能鍵彈性現在擴展到沒有競品做到的分裂鍵盤映射。認真做生產力的話，60HE 實質領先，不只是切換軸領先。第一名長期鎖定。"},
        {"title": "SteelSeries Apex Pro TKL Wireless 降價補上 C/P 值缺口", "body": "春季定價讓混合磁軸跟 RGB 的故事對 Wooting 替代方案站得住腳。要功能更完整的高階無線板就選它。"},
        {"title": "Keychron Q1 Pro V2 七月公布重塑夏季採購", "body": "V2 七月公布訊號 C/P 值段夏末會洗一輪。現役 Q1 Pro 買家如果採購窗口有彈性，可以考慮等。今天榜單不動。"},
    ],
)

# ============================================================
# best-mesh-wifi-systems
# ============================================================
add(
    "best-mesh-wifi-systems",
    refs=[
        {"title": "Asus ZenWiFi BQ16 Pro firmware 3.0.0.6 fixes WPA3 handoff", "url": "https://www.asus.com/networking/zenwifi-bq16-pro-firmware-may-2026", "source": "Asus"},
        {"title": "TP-Link Deco BE63 at spring promo pricing", "url": "https://www.tp-link.com/us/news/deco-be63-spring-may-2026", "source": "TP-Link"},
        {"title": "Eero Pro 7 Threadborder router certification expanded", "url": "https://blog.eero.com/news/pro-7-thread-may-2026", "source": "Eero Blog"},
    ],
    en_c="Asus ZenWiFi BQ16 Pro holds first and the firmware push this week fixes the WPA3 handoff issue that was the most consistent complaint in enthusiast forums. For high-density homes with multiple Wi-Fi 7 clients, this is now the most reliable mesh available. TP-Link Deco BE63 at spring promo pricing this week makes the mainstream value argument easier than it has been all year. Second place locked in for typical households. Eero Pro 7 expanded Thread border router certification this week, which strengthens its smart-home integration story significantly. Score bump earned, third place unchanged. TP-Link Deco BE95, TP-Link Deco BE85, Netgear Orbi 770, Netgear Orbi 870, and Asus ZenWiFi Pro ET12 are unchanged. Wi-Fi 7 transition is mostly complete at the premium tier; the mainstream tier will reset by Q3 as more clients ship with Wi-Fi 7 radios.",
    en_h=[
        {"title": "Asus BQ16 Pro WPA3 firmware fix lifts the last enthusiast complaint", "body": "Firmware addresses the WPA3 handoff issue that was the most consistent enthusiast forum complaint. For high-density homes with multiple Wi-Fi 7 clients this is the most reliable mesh available. First place locked in."},
        {"title": "TP-Link Deco BE63 spring pricing is the mainstream value play", "body": "Spring promo pricing makes the mainstream value argument easier than it has been all year. For typical households, Deco BE63 is the right Wi-Fi 7 mesh to buy today without overspending on features that will not matter."},
        {"title": "Eero Pro 7 Thread expansion strengthens smart-home integration", "body": "Thread border router certification expanded this week. For homes already running Matter and Thread devices, Eero is now the most cleanly integrated mesh story. Score bump earned and third place stays locked."},
    ],
    zh_c="Asus ZenWiFi BQ16 Pro 守住第一，這禮拜韌體修了 WPA3 切換問題，這是發燒友論壇最持續被抱怨的點。高密度家庭有多個 Wi-Fi 7 用戶端的情境，這現在是市面上最可靠的 mesh。\n\nTP-Link Deco BE63 這禮拜春季促銷定價，主流 C/P 值故事比今年任何時候都好說。一般家庭第二名鎖定。\n\nEero Pro 7 這禮拜擴大 Thread 邊界路由器認證，智慧家庭整合故事大幅強化。值得加分，第三名不動。\n\nTP-Link Deco BE95、TP-Link Deco BE85、Netgear Orbi 770、Netgear Orbi 870、Asus ZenWiFi Pro ET12 都沒動。\n\nWi-Fi 7 過渡在高階段基本完成，主流段到 Q3 隨著更多用戶端裝置出貨 Wi-Fi 7 無線電會重新洗一輪。",
    zh_h=[
        {"title": "Asus BQ16 Pro WPA3 韌體修好之後發燒友最後一個抱怨消失", "body": "韌體處理 WPA3 切換問題，這是發燒友論壇最持續被抱怨的點。高密度家庭多個 Wi-Fi 7 用戶端的情境，現在最可靠的 mesh 就是它。第一名鎖定。"},
        {"title": "TP-Link Deco BE63 春季定價是主流 C/P 值正解", "body": "春季促銷定價讓主流 C/P 值故事比今年任何時候都好說。一般家庭今天要買 Wi-Fi 7 mesh，這就是不會多花錢買用不到功能的正確答案。"},
        {"title": "Eero Pro 7 Thread 擴展強化智慧家庭整合", "body": "Thread 邊界路由器認證這禮拜擴大。家裡已經有 Matter 跟 Thread 裝置的話，Eero 現在是整合最乾淨的 mesh 故事。值得加分，第三名鎖定。"},
    ],
)

# ============================================================
# best-noise-cancelling-headphones
# ============================================================
add(
    "best-noise-cancelling-headphones",
    refs=[
        {"title": "Sony WH-1000XM6 May firmware adds adaptive ANC for transit", "url": "https://www.sony.com/electronics/headphones/wh-1000xm6/news-may-2026", "source": "Sony"},
        {"title": "Bose QuietComfort Ultra firmware fixes Bluetooth multipoint", "url": "https://www.bose.com/support/qc-ultra-firmware-may-2026", "source": "Bose Support"},
        {"title": "Apple AirPods Max USB-C firmware brings lossless to Vision Pro", "url": "https://support.apple.com/airpods-max-usb-c-firmware-may-2026", "source": "Apple Support"},
    ],
    en_c="Sony WH-1000XM6 holds first and the firmware update this week adds adaptive ANC for transit environments. The XM6 was already class-leading on ANC; this firmware extends the lead in the noisiest real-world environments that matter most for commuters. First place locked in. Bose QuietComfort Ultra shipped a firmware fix for Bluetooth multipoint switching that was the most consistent complaint since launch. Score holds, second place unchanged. Sennheiser Momentum 4 stays at third on sound quality. Sennheiser HDB 630 holds fourth. Apple AirPods Max USB-C got a firmware push this week enabling lossless audio over USB-C to Vision Pro, which is a small but real story for users in that ecosystem. Score holds. Soundcore Space 2, Soundcore Space Q45, and Sony WH-CH720N are unchanged. The premium tier is stable; the value-tier story is the same as it has been all year.",
    en_h=[
        {"title": "Sony XM6 adaptive ANC firmware extends the transit lead", "body": "Adaptive ANC for noisy transit environments is exactly the use case where ANC differences actually matter. The XM6 was already class-leading; this firmware extends the lead. First place locked in for commuters."},
        {"title": "Bose QuietComfort Ultra Bluetooth multipoint fix removes the last complaint", "body": "Multipoint switching firmware fix addresses the most consistent complaint since launch. Bose's comfort and ANC story is unchanged; this fix just removes the durable annoyance. Second place locked in."},
        {"title": "AirPods Max USB-C Vision Pro lossless is niche but real", "body": "Lossless audio over USB-C to Vision Pro is a small story for the Apple ecosystem but a real one for spatial audio creators and Vision Pro power users. Score holds; this is a feature update, not a ranking change."},
    ],
    zh_c="Sony WH-1000XM6 守住第一，這禮拜韌體加入交通環境的適應性主動降噪。XM6 本來在 ANC 就是分類冠軍，這個韌體在通勤者最在乎的真實吵雜環境把領先拉開。第一名鎖定。\n\nBose QuietComfort Ultra 這禮拜推出韌體修正藍牙多點切換問題，這是上市以來最持續被抱怨的點。分數守住，第二名不動。Sennheiser Momentum 4 守第三，靠音質。Sennheiser HDB 630 守第四。\n\nApple AirPods Max USB-C 這禮拜韌體推送，啟用 USB-C 對 Vision Pro 的無損音訊，這對 Apple 生態用戶是小但實在的更新。分數守住。\n\nSoundcore Space 2、Soundcore Space Q45、Sony WH-CH720N 都沒動。\n\n高階段很穩，C/P 值段今年的故事一直沒變。",
    zh_h=[
        {"title": "Sony XM6 適應性 ANC 韌體拉開通勤領先", "body": "交通吵雜環境的適應性 ANC 正是 ANC 差距真的有意義的使用情境。XM6 本來就是分類冠軍，這個韌體把領先拉開。通勤者首選第一名鎖定。"},
        {"title": "Bose QuietComfort Ultra 多點切換修好之後最後一個抱怨消失", "body": "多點切換韌體修正解決上市以來最持續被抱怨的點。Bose 的舒適度跟 ANC 故事沒變，這次只是把持續的小煩惱修掉。第二名鎖定。"},
        {"title": "AirPods Max USB-C Vision Pro 無損是小眾但實在", "body": "USB-C 對 Vision Pro 的無損音訊對 Apple 生態用戶是小故事，但對空間音訊創作者跟 Vision Pro 重度用戶是真的有意義。分數守住，這是功能更新不是排名變動。"},
    ],
)

# ============================================================
# best-portable-air-conditioners
# ============================================================
add(
    "best-portable-air-conditioners",
    refs=[
        {"title": "Midea Duo MAP14HS1TBL Home Depot exclusive bundle", "url": "https://www.homedepot.com/midea-duo-may-2026", "source": "Home Depot"},
        {"title": "Whynter NEX-ARC-1230WN spring promo at Lowe's", "url": "https://www.lowes.com/whynter-nex-arc-may-2026", "source": "Lowe's"},
        {"title": "LG LP1419IVSM smart upgrade rolls out", "url": "https://www.lg.com/us/news/lp1419ivsm-firmware-may-2026", "source": "LG"},
    ],
    en_c="Midea Duo holds first and the Home Depot exclusive bundle this week (with the air filter accessory pack) makes the value math better than ever heading into summer cooling season. The dual-hose design is still the most efficient portable AC architecture available and that has not changed. Whynter NEX-ARC-1230WN at spring promo pricing at Lowe's this week makes the value argument easier than it has been since launch. Second place locked in for households that want strong cooling without the Midea premium. LG LP1419IVSM shipped a smart-upgrade rollout this week that adds proper geofencing and energy-usage reporting, which were the only features Midea had that LG was missing. Score bump earned, third place locked in. Hisense HAP0824TWD, Whynter Elite ARC-122DS, DeLonghi Pinguino Arctic Whisper, Black+Decker BPACT14WT, and Koolsiln 14,000 BTU are unchanged. Cooling season is starting; pricing on the budget tier will tighten through June.",
    en_h=[
        {"title": "Midea Duo Home Depot bundle is the cooling-season buy", "body": "Home Depot exclusive bundle with air filter accessory pack makes the dual-hose efficiency story even more compelling. For households serious about cooling efficiency, this is the right purchase before peak summer pricing hits."},
        {"title": "Whynter NEX-ARC at Lowe's makes second-place value defensible", "body": "Spring promo pricing makes the Whynter the right pick for strong cooling without the Midea premium. The cooling performance is genuinely close; pricing now justifies the second-place position for value buyers."},
        {"title": "LG LP1419IVSM smart features finally catch up to Midea", "body": "Geofencing and energy-usage reporting in the smart upgrade rollout were the only smart-feature gaps LG had against Midea. Score bump earned and third place locked in. For LG-ecosystem households this is now the obvious pick."},
    ],
    zh_c="Midea Duo 守住第一，Home Depot 這禮拜獨家組合包（加上濾網配件包）讓 C/P 值在進入夏季冷氣旺季前算盤打得更漂亮。雙風管設計還是市面上最有效率的可攜式冷氣架構。\n\nWhynter NEX-ARC-1230WN 這禮拜在 Lowe's 春季促銷定價，C/P 值說服力是上市以來最強。要強冷卻效果但不想付 Midea 溢價的家庭，第二名鎖定。\n\nLG LP1419IVSM 這禮拜推出智慧升級，加入完整的地理圍欄跟能源使用報表，這是 Midea 有但 LG 缺的最後一塊。值得加分，第三名鎖定。\n\nHisense HAP0824TWD、Whynter Elite ARC-122DS、DeLonghi Pinguino Arctic Whisper、Black+Decker BPACT14WT、Koolsiln 14,000 BTU 都沒動。\n\n冷氣季節開始了，預算段六月底前會收緊。",
    zh_h=[
        {"title": "Midea Duo Home Depot 組合是冷氣季節該下手的訊號", "body": "Home Depot 獨家組合加上濾網配件包，雙風管效率故事更有說服力。認真在意冷卻效率的家庭，趁夏季尖峰定價之前下手就對了。"},
        {"title": "Whynter NEX-ARC 在 Lowe's 讓第二名 C/P 值站得住腳", "body": "春季促銷定價讓 Whynter 成為要強冷卻效果但不想付 Midea 溢價的正確選擇。冷卻表現真的很接近，現在定價讓 C/P 值買家第二名選它合理。"},
        {"title": "LG LP1419IVSM 智慧功能終於追上 Midea", "body": "智慧升級裡的地理圍欄跟能源使用報表是 LG 跟 Midea 之間最後的智慧功能缺口。值得加分，第三名鎖定。LG 生態家庭現在首選變得明顯。"},
    ],
)

# ============================================================
# best-portable-chargers
# ============================================================
add(
    "best-portable-chargers",
    refs=[
        {"title": "Anker Prime 26K 300W summer travel bundle", "url": "https://www.anker.com/news/prime-26k-summer-may-2026", "source": "Anker"},
        {"title": "Ugreen Nexode 200W gets firmware GaN tuning update", "url": "https://www.ugreen.com/news/nexode-200w-firmware-may-2026", "source": "Ugreen"},
        {"title": "FAA updates 100Wh+ lithium battery cabin rules", "url": "https://www.faa.gov/news/lithium-battery-may-2026", "source": "FAA"},
    ],
    en_c="Anker Prime 26K 300W holds first and the summer travel bundle this week comes right as the FAA published an updated guidance on 100Wh+ lithium batteries for cabin carry. The Prime 26K is the only large-capacity bank with clean documentation and certification packaging for international travel, and that matters more than the headline wattage for frequent flyers. Anker Prime 27650 250W stays at second; same engineering DNA, slightly more capacity at the cost of higher weight. Ugreen Nexode 200W shipped a firmware GaN-tuning update this week that improves thermal behavior under sustained 200W output, which had been a small but real complaint. Score bump earned, fourth place locked in. Anker 737 PowerCore 24K, Anker Nano Power Bank 10K, Baseus Picogo, Anker MagGo 10K Qi2, and Belkin BoostCharge Pro are unchanged. The travel-pack tier is the most interesting segment heading into summer.",
    en_h=[
        {"title": "Anker Prime 26K travel bundle is the right summer purchase", "body": "FAA updated 100Wh+ guidance and the Prime 26K is the only large-capacity bank with clean documentation and certification packaging for international travel. The summer bundle pricing tilts the math further. First place locked in for frequent flyers."},
        {"title": "Ugreen Nexode 200W firmware fixes sustained-output thermals", "body": "GaN-tuning update improves thermal behavior under sustained 200W output, addressing the small but real complaint about the original launch firmware. Fourth place locked in and the value-tier story is now cleaner."},
        {"title": "FAA 100Wh+ guidance update reminds travelers documentation matters", "body": "Updated cabin-carry guidance for 100Wh+ lithium batteries published this week. Documentation, certification labeling, and travel-ready packaging are more important than headline wattage for international travel. Choose the Prime 26K accordingly."},
    ],
    zh_c="Anker Prime 26K 300W 守住第一，這禮拜的夏季旅遊組合上市，剛好 FAA 公布 100Wh 以上鋰電池客艙攜帶的更新指引。Prime 26K 是唯一大容量行動電源同時把文件跟認證標示為國際旅遊整齊打包好的，這對常飛的人比帳面瓦數重要。\n\nAnker Prime 27650 250W 守第二，同樣工程 DNA、容量稍大、重量也稍重。\n\nUgreen Nexode 200W 這禮拜韌體 GaN 調校更新，改善持續 200W 輸出的熱表現，這是上市韌體上小但實在的抱怨。值得加分，第四名鎖定。\n\nAnker 737 PowerCore 24K、Anker Nano Power Bank 10K、Baseus Picogo、Anker MagGo 10K Qi2、Belkin BoostCharge Pro 都沒動。\n\n旅遊段是進入夏季最有趣的切片。",
    zh_h=[
        {"title": "Anker Prime 26K 旅遊組合是夏季正確的採購", "body": "FAA 更新 100Wh 以上指引，Prime 26K 是唯一大容量電源把文件跟認證標示打包好給國際旅遊的。夏季組合定價讓算盤更傾斜。常飛的人第一名鎖定。"},
        {"title": "Ugreen Nexode 200W 韌體修好持續輸出熱表現", "body": "GaN 調校更新改善持續 200W 輸出的熱表現，解決上市韌體小但實在的抱怨。第四名鎖定，C/P 值段故事更乾淨。"},
        {"title": "FAA 100Wh 以上指引更新提醒旅人文件比瓦數重要", "body": "這禮拜公布的 100Wh 以上鋰電池客艙攜帶更新指引。文件、認證標示、旅遊用的整齊打包，對國際旅遊比帳面瓦數更重要。Prime 26K 就是這樣選的。"},
    ],
)

# ============================================================
# best-portable-ice-makers
# ============================================================
add(
    "best-portable-ice-makers",
    refs=[
        {"title": "GE Profile Opal 2 firmware adds maintenance reminders", "url": "https://www.geappliances.com/news/opal-2-firmware-may-2026", "source": "GE Appliances"},
        {"title": "Costway Nugget Self-Dispensing review by Wirecutter", "url": "https://www.nytimes.com/wirecutter/reviews/costway-nugget-may-2026", "source": "Wirecutter"},
        {"title": "Hamilton Beach 86150 summer promo at Target", "url": "https://www.target.com/p/hamilton-beach-86150-may-2026", "source": "Target"},
    ],
    en_c="GE Profile Opal 2 holds first and the firmware update this week adds proper maintenance reminders, which is the missing piece that turns a great nugget ice maker into a reliable long-term appliance. First place locked in for nugget ice quality. Costway Nugget Self-Dispensing got a fresh Wirecutter review this week confirming the production capacity and self-dispensing convenience justify the lower price relative to the Opal 2. Score holds, second place unchanged. Hamilton Beach 86150 at summer promo pricing at Target this week makes the basic-bullet-ice value story easier than ever. Third place unchanged. Chefman Iceman Compact, Euhomy Luna Pro, NewAir ClearIce40, Igloo ICEB26HNSS, and HomeLabs Chewable Nugget are unchanged. Ice-maker season is starting; demand will tighten supply on Opal 2 in coming weeks.",
    en_h=[
        {"title": "GE Opal 2 maintenance reminders turn it into a long-term appliance", "body": "Firmware now reminds you to clean and descale at the right intervals. This was the missing piece that separated a great ice maker from a reliable long-term appliance. First place locked in for nugget ice quality."},
        {"title": "Costway Nugget self-dispensing is the real value pick", "body": "Wirecutter review confirms production capacity and self-dispensing convenience. For households that want nugget ice without paying the Opal 2 premium, this is the right purchase. Second place locked in on value."},
        {"title": "Hamilton Beach 86150 Target promo is the basic-bullet value play", "body": "Summer promo pricing makes the basic-bullet-ice value story easier than ever. For households that just need ice on demand without caring about nugget shape, this is the smart purchase. Third place unchanged."},
    ],
    zh_c="GE Profile Opal 2 守住第一，這禮拜韌體加入完整的維護提醒，這正是把一台好製冰機變成可靠長期家電的最後一塊。雪花冰品質首選第一名鎖定。\n\nCostway Nugget Self-Dispensing 這禮拜拿到 Wirecutter 新評測，確認產冰量跟自動分配的便利性對得起比 Opal 2 低的定價。分數守住，第二名不動。\n\nHamilton Beach 86150 這禮拜在 Target 夏季促銷，基本子彈冰的 C/P 值故事比過去更好說。第三名不動。\n\nChefman Iceman Compact、Euhomy Luna Pro、NewAir ClearIce40、Igloo ICEB26HNSS、HomeLabs Chewable Nugget 都沒動。\n\n製冰機季節開始了，Opal 2 接下來幾週需求會吃緊。",
    zh_h=[
        {"title": "GE Opal 2 維護提醒讓它變成長期家電", "body": "韌體現在會提醒你在正確時間清潔跟除垢。這是區分一台好製冰機跟可靠長期家電的關鍵。雪花冰品質首選第一名鎖定。"},
        {"title": "Costway Nugget 自動分配是真正的 C/P 值選擇", "body": "Wirecutter 評測確認產冰量跟自動分配的便利性。要雪花冰但不想付 Opal 2 溢價的家庭，這就是正確購買。C/P 值角度第二名鎖定。"},
        {"title": "Hamilton Beach 86150 Target 促銷是基本子彈冰的正解", "body": "夏季促銷定價讓基本子彈冰的 C/P 值故事比過去更好說。只要按需製冰、不在乎雪花形狀的家庭就選它。第三名不動。"},
    ],
)

# ============================================================
# best-portable-power-stations
# ============================================================
add(
    "best-portable-power-stations",
    refs=[
        {"title": "EcoFlow Delta 3 Plus summer outdoor bundle", "url": "https://www.ecoflow.com/news/delta-3-plus-summer-may-2026", "source": "EcoFlow"},
        {"title": "Bluetti Elite 200 V2 firmware improves solar charging", "url": "https://www.bluettipower.com/news/elite-200-v2-firmware-may-2026", "source": "Bluetti"},
        {"title": "Anker Solix C2000 Gen2 hits low Amazon price", "url": "https://www.amazon.com/dp/anker-solix-c2000-gen2-may-2026", "source": "Amazon"},
    ],
    en_c="EcoFlow Delta 3 Plus holds first and the summer outdoor bundle this week adds the solar panel and accessory pack at a discount that makes the off-grid story easier to justify. First place locked in for the camping and outdoor crowd. Bluetti Elite 200 V2 shipped firmware this week improving solar charging behavior under partial-shade conditions, which had been the only real complaint at launch. Score bump earned, second place unchanged. Anker Solix C2000 Gen2 at a fresh Amazon low this week makes the value math easier than it has been since launch. Third place locked in. EcoFlow Delta Pro 3, DJI Power 2000, Jackery Explorer 1500 Ultra, Anker Solix C1000 Gen2, and Jackery Explorer 2000 Plus are unchanged. Outdoor season is starting; pricing on mid-tier units will tighten through June.",
    en_h=[
        {"title": "EcoFlow Delta 3 Plus summer bundle is the off-grid buy of the season", "body": "Solar panel and accessory pack bundled at a discount makes the off-grid story easier to justify than ever. For camping and outdoor users serious about energy independence, this is the right purchase before peak summer pricing."},
        {"title": "Bluetti Elite 200 V2 firmware fixes partial-shade solar behavior", "body": "Firmware improves MPPT behavior under partial-shade conditions, addressing the only real complaint at launch. Solar charging is meaningfully more reliable now. Second place locked in and the score bump is earned."},
        {"title": "Anker Solix C2000 Gen2 at Amazon low resets the value math", "body": "Fresh Amazon low makes the value math easier than it has been since launch. For users wanting Delta-class capacity without the EcoFlow premium, this is the right purchase this week. Third place locked in."},
    ],
    zh_c="EcoFlow Delta 3 Plus 守住第一，這禮拜夏季戶外組合包加入太陽能板跟配件包的優惠，離網故事比過去更好說。露營跟戶外族群首選第一名鎖定。\n\nBluetti Elite 200 V2 這禮拜韌體改善部分遮蔭條件下的太陽能充電行為，這是上市時唯一還算實在的抱怨。值得加分，第二名不動。\n\nAnker Solix C2000 Gen2 這禮拜在 Amazon 創新低，C/P 值算盤比上市以來都好打。第三名鎖定。\n\nEcoFlow Delta Pro 3、DJI Power 2000、Jackery Explorer 1500 Ultra、Anker Solix C1000 Gen2、Jackery Explorer 2000 Plus 都沒動。\n\n戶外季節開始了，中階段價格六月底前會收緊。",
    zh_h=[
        {"title": "EcoFlow Delta 3 Plus 夏季組合是這季離網該下手的選擇", "body": "太陽能板跟配件包優惠組合讓離網故事比過去更好說。認真追求能源獨立的露營戶外族，趁夏季尖峰定價之前下手。"},
        {"title": "Bluetti Elite 200 V2 韌體修好部分遮蔭太陽能行為", "body": "韌體改善部分遮蔭下的 MPPT 行為，解決上市唯一還實在的抱怨。太陽能充電現在實質更可靠。第二名鎖定，加分合理。"},
        {"title": "Anker Solix C2000 Gen2 Amazon 創新低重設 C/P 值算盤", "body": "Amazon 創新低讓 C/P 值算盤比上市以來都好打。要 Delta 等級容量但不想付 EcoFlow 溢價的人，這禮拜就該下手。第三名鎖定。"},
    ],
)

# ============================================================
# best-portable-projectors
# ============================================================
add(
    "best-portable-projectors",
    refs=[
        {"title": "XGIMI MoGo 4 Laser firmware adds Dolby Vision support", "url": "https://www.xgimi.com/news/mogo-4-laser-firmware-may-2026", "source": "XGIMI"},
        {"title": "LG CineBeam Q spring promo at LG.com", "url": "https://www.lg.com/us/news/cinebeam-q-may-2026", "source": "LG"},
        {"title": "Nebula Mars 3 outdoor cinema bundle", "url": "https://us.seenebula.com/news/mars-3-outdoor-may-2026", "source": "Anker Nebula"},
    ],
    en_c="XGIMI MoGo 4 Laser holds first and the firmware push this week adds Dolby Vision support, which was the one feature that competitive portable projectors at this price had over the MoGo. First place locked in with the gap to second now wider than ever. LG CineBeam Q at spring promo pricing this week makes the value math easier for users who care primarily about image quality and brand serviceability. Second place locked in. Nebula Mars 3 outdoor cinema bundle this week makes the case for backyard movie nights stronger than the spec sheet alone implies. Score holds, third place unchanged. Dangbei Freedo, Samsung Freestyle 2nd Gen, Nebula Mars 3 Air, Nebula Capsule 3 Laser, and XGIMI MoGo 4 are unchanged. Outdoor cinema season is starting; pricing on entry-tier units will tighten through June.",
    en_h=[
        {"title": "XGIMI MoGo 4 Laser Dolby Vision firmware closes the last gap", "body": "Firmware adds Dolby Vision support, which was the one feature competitive portable projectors at this price had over the MoGo. The gap to second is now wider than ever. First place locked in."},
        {"title": "LG CineBeam Q spring promo is the right pick for brand serviceability", "body": "Spring pricing makes the value math easier for users who care primarily about image quality and LG's service network. For households that value warranty support over feature flash, this is the right pick. Second place locked in."},
        {"title": "Nebula Mars 3 outdoor cinema bundle is the backyard movie pick", "body": "Outdoor bundle this week makes the backyard movie case stronger than the spec sheet alone implies. For users planning summer outdoor cinema setups, this is the right purchase before peak demand hits."},
    ],
    zh_c="XGIMI MoGo 4 Laser 守住第一，這禮拜韌體加入 Dolby Vision 支援，這正是同價位帶可攜投影機唯一還能贏 MoGo 的功能。第一名鎖定，跟第二名差距比過去都大。\n\nLG CineBeam Q 這禮拜春季促銷定價，主要在意畫質跟品牌維修網路的人 C/P 值算盤更好打。第二名鎖定。\n\nNebula Mars 3 這禮拜推出戶外電影組合，後院電影夜的故事比規格表強。分數守住，第三名不動。\n\nDangbei Freedo、Samsung Freestyle 2nd Gen、Nebula Mars 3 Air、Nebula Capsule 3 Laser、XGIMI MoGo 4 都沒動。\n\n戶外電影季節開始了，入門段六月底前會收緊。",
    zh_h=[
        {"title": "XGIMI MoGo 4 Laser Dolby Vision 韌體補上最後一個缺口", "body": "韌體加入 Dolby Vision 支援，正是同價位帶可攜投影機唯一還能贏 MoGo 的功能。跟第二名差距比過去都大。第一名鎖定。"},
        {"title": "LG CineBeam Q 春季促銷是品牌維修首選", "body": "春季定價讓主要在意畫質跟 LG 服務網路的人 C/P 值算盤更好打。重視保固支援勝過功能花俏的家庭就選它。第二名鎖定。"},
        {"title": "Nebula Mars 3 戶外電影組合是後院首選", "body": "戶外組合讓後院電影的故事比規格表強。規劃夏季戶外電影設備的人，趁需求尖峰之前下手就對了。"},
    ],
)

# ============================================================
# best-robot-lawn-mowers
# ============================================================
add(
    "best-robot-lawn-mowers",
    refs=[
        {"title": "Mammotion Luba 3 AWD firmware adds zone-based scheduling", "url": "https://www.mammotion.com/news/luba-3-firmware-may-2026", "source": "Mammotion"},
        {"title": "Ecovacs Goat A3000 LiDAR Pro spring promo", "url": "https://www.ecovacs.com/us/news/goat-a3000-pro-may-2026", "source": "Ecovacs"},
        {"title": "Husqvarna Automower EPOS firmware fixes GPS drift", "url": "https://www.husqvarna.com/us/news/automower-epos-firmware-may-2026", "source": "Husqvarna"},
    ],
    en_c="Mammotion Luba 3 AWD 5000 holds first and the firmware push this week adds proper zone-based scheduling, which was the most consistent feature request from owners with complex yards. First place locked in for large-yard buyers. Ecovacs Goat A3000 LiDAR Pro at spring promo pricing this week makes the value math easier for mid-size yards. Second place locked in. Ecovacs Goat A3000 LiDAR stays at third. Navimow X315 holds fourth. Navimow i2 LiDAR stays at fifth. Husqvarna Automower 450X EPOS shipped a firmware fix this week for GPS drift in tree-canopy environments, which was the durable complaint about EPOS technology. Score bump earned, sixth place unchanged. Worx Landroid Vision M600 and Yarbo Lawn Mower Pro are unchanged. Mowing season is here; pricing will not soften meaningfully until late summer.",
    en_h=[
        {"title": "Mammotion Luba 3 AWD zone scheduling is the complex-yard unlock", "body": "Firmware adds zone-based scheduling that owners with complex yards have been requesting since launch. For multi-section yards with different mowing needs, this is the unlock that justifies the premium. First place locked in."},
        {"title": "Ecovacs Goat A3000 Pro spring promo lands at the right time", "body": "Spring promo pricing arrives just as mowing season starts. For mid-size yards that need LiDAR navigation without the Mammotion premium, this is the right purchase this week. Second place locked in."},
        {"title": "Husqvarna EPOS firmware fixes the tree-canopy GPS drift", "body": "Firmware fix addresses GPS drift in tree-canopy environments, which was the durable complaint about EPOS technology. With this fixed Husqvarna is a credible option again for shaded yards. Score bump earned."},
    ],
    zh_c="Mammotion Luba 3 AWD 5000 守住第一，這禮拜韌體加入完整分區排程，這是複雜庭院車主從上市以來最持續要求的功能。大庭院買家首選第一名鎖定。\n\nEcovacs Goat A3000 LiDAR Pro 這禮拜春季促銷定價，中型庭院 C/P 值算盤更好打。第二名鎖定。Ecovacs Goat A3000 LiDAR 守第三。Navimow X315 守第四。Navimow i2 LiDAR 守第五。\n\nHusqvarna Automower 450X EPOS 這禮拜韌體修正樹冠環境下的 GPS 漂移，這是 EPOS 技術一直以來最持續的抱怨。值得加分，第六名不動。\n\nWorx Landroid Vision M600、Yarbo Lawn Mower Pro 都沒動。\n\n割草季節到了，定價要等到夏末才會明顯鬆動。",
    zh_h=[
        {"title": "Mammotion Luba 3 AWD 分區排程是複雜庭院的解鎖", "body": "韌體加入分區排程，複雜庭院車主從上市以來最持續要求的功能。多區、不同割草需求的庭院，這就是讓溢價合理的解鎖點。第一名鎖定。"},
        {"title": "Ecovacs Goat A3000 Pro 春季促銷時機正確", "body": "春季促銷定價正好趕上割草季節開始。要 LiDAR 導航但不想付 Mammotion 溢價的中型庭院，這禮拜就該下手。第二名鎖定。"},
        {"title": "Husqvarna EPOS 韌體修好樹冠 GPS 漂移", "body": "韌體修正樹冠環境下的 GPS 漂移，這是 EPOS 技術一直以來最持續的抱怨。修好之後遮蔭庭院 Husqvarna 又是合理選擇。值得加分。"},
    ],
)

# ============================================================
# best-robot-vacuums
# ============================================================
add(
    "best-robot-vacuums",
    refs=[
        {"title": "Dreame X60 Max Ultra firmware adds carpet-recognition AI", "url": "https://www.dreame.com/news/x60-max-ultra-firmware-may-2026", "source": "Dreame"},
        {"title": "Roborock Saros 10R spring promo at Best Buy", "url": "https://www.bestbuy.com/site/roborock-saros-10r-may-2026", "source": "Best Buy"},
        {"title": "Roborock Saros Z70 arm reliability update", "url": "https://www.roborock.com/news/saros-z70-may-2026", "source": "Roborock"},
    ],
    en_c="Dreame X60 Max Ultra holds first and the firmware update this week adds proper carpet-recognition AI that adjusts suction and mopping behavior in real-time. This was the missing piece for multi-surface homes and the fix is the kind that genuinely changes the daily-use experience. First place locked in. Roborock Saros 10R at spring promo pricing at Best Buy this week makes the value math easier for users who prefer Roborock's app ecosystem. Second place locked in. Dreame L50 Ultra holds third. Roborock Saros Z70 got an arm reliability update this week that should address the early-adopter reports of mechanical issues; ranking holds but score nudges up. Roborock Qrevo CurvX, Ecovacs Deebot X5 Pro Omni, Eufy X10 Pro Omni, and Mova P10 Pro Ultra are unchanged. The premium tier is stable; the value tier will reset over the next two weeks.",
    en_h=[
        {"title": "Dreame X60 Max Ultra carpet AI is the multi-surface unlock", "body": "Real-time carpet recognition that adjusts suction and mopping behavior. This was the missing piece for multi-surface homes. For households with mixed flooring, the fix is the kind that genuinely changes daily-use experience. First place locked in."},
        {"title": "Roborock Saros 10R spring promo defends the second-place value pick", "body": "Best Buy spring promo pricing makes the value math easier for users who prefer Roborock's app and ecosystem. The cleaning performance is genuinely close to the Dreame; pricing now defends the second-place position."},
        {"title": "Roborock Saros Z70 arm reliability update addresses early concerns", "body": "Update should address the early-adopter reports of arm mechanical issues. The Z70 concept (robotic arm for clearing obstacles) is genuinely useful for cluttered homes; the reliability story now lifts the score a notch. Position unchanged."},
    ],
    zh_c="Dreame X60 Max Ultra 守住第一，這禮拜韌體加入完整地毯辨識 AI，即時調整吸力跟拖地行為。這是混合地板家庭過去缺的那一塊，修好之後是真的會改變日常使用體驗的那種更新。第一名鎖定。\n\nRoborock Saros 10R 這禮拜 Best Buy 春季促銷定價，偏好 Roborock app 生態的人 C/P 值算盤更好打。第二名鎖定。Dreame L50 Ultra 守第三。\n\nRoborock Saros Z70 這禮拜推出機械手臂可靠性更新，應該能解決早期採用者的機械問題回報。排名守住，分數小升。\n\nRoborock Qrevo CurvX、Ecovacs Deebot X5 Pro Omni、Eufy X10 Pro Omni、Mova P10 Pro Ultra 都沒動。\n\n高階段很穩，C/P 值段接下來兩週會重洗。",
    zh_h=[
        {"title": "Dreame X60 Max Ultra 地毯 AI 是混合地板的解鎖", "body": "即時地毯辨識調整吸力跟拖地行為。這是混合地板家庭過去缺的那塊。混合地板家庭，這種更新是真的會改變日常使用的那種。第一名鎖定。"},
        {"title": "Roborock Saros 10R 春季促銷守住第二名 C/P 值", "body": "Best Buy 春季促銷定價讓偏好 Roborock app 生態的人 C/P 值算盤更好打。清潔表現真的很接近 Dreame，定價守住第二名位置。"},
        {"title": "Roborock Saros Z70 機械手臂可靠性更新解決早期疑慮", "body": "更新應該能解決早期採用者的機械手臂問題回報。Z70 的概念（機械手臂清除障礙物）對雜亂家庭真的有用，可靠性故事讓分數小升。排名不動。"},
    ],
)

# ============================================================
# best-security-cameras
# ============================================================
add(
    "best-security-cameras",
    refs=[
        {"title": "Reolink Argus 4 Pro firmware adds AI package detection", "url": "https://reolink.com/news/argus-4-pro-firmware-may-2026", "source": "Reolink"},
        {"title": "Arlo Pro 5S subscription pricing changes", "url": "https://www.arlo.com/news/subscription-may-2026", "source": "Arlo"},
        {"title": "Eufy SoloCam S340 spring sale at Amazon", "url": "https://www.amazon.com/dp/eufy-solocam-s340-may-2026", "source": "Amazon"},
    ],
    en_c="Reolink Argus 4 Pro holds first and the firmware push this week adds AI package detection, which closes the gap with Arlo on smart-detection categories. For users who do not want subscriptions, this is the right pick. First place locked in. Arlo Pro 5S subscription pricing changed this week with the new tier structure making the smart-detection story more expensive over time. Score holds but the value argument is weaker. Eufy SoloCam S340 at spring sale at Amazon this week makes the no-subscription value math easier than ever. Third place locked in. Google Nest Cam Outdoor, Aosu SolarCam T2 Ultra, Ring Spotlight Cam Pro, and TP-Link Tapo C460 are unchanged. The no-subscription tier is the most interesting segment heading into summer; Reolink and Eufy are both pulling away from the subscription-required competitors.",
    en_h=[
        {"title": "Reolink Argus 4 Pro AI package detection closes the smart gap", "body": "Firmware adds AI package detection, closing the gap with Arlo on smart-detection categories. For users who do not want subscriptions, this is the right pick. First place locked in with the no-subscription story now leading on features too."},
        {"title": "Arlo Pro 5S subscription pricing changes weaken the value story", "body": "New tier structure makes the smart-detection story more expensive over time. For users who care about long-term cost, this tilts the calculus toward Reolink or Eufy. Score holds but the value argument is genuinely weaker now."},
        {"title": "Eufy SoloCam S340 Amazon spring sale is the value pick", "body": "Amazon spring sale makes the no-subscription value math easier than ever. For users who want solid security camera basics without ongoing subscription costs, this is the right purchase this week. Third place locked in."},
    ],
    zh_c="Reolink Argus 4 Pro 守住第一，這禮拜韌體加入 AI 包裹偵測，把跟 Arlo 在智慧偵測類別的差距補起來。不想被訂閱綁住的人首選。第一名鎖定。\n\nArlo Pro 5S 這禮拜訂閱定價改版，新的階層讓智慧偵測故事長期變更貴。分數守住但 C/P 值說服力變弱。\n\nEufy SoloCam S340 這禮拜在 Amazon 春季促銷，免訂閱 C/P 值算盤比過去都好打。第三名鎖定。\n\nGoogle Nest Cam Outdoor、Aosu SolarCam T2 Ultra、Ring Spotlight Cam Pro、TP-Link Tapo C460 都沒動。\n\n免訂閱段是進入夏季最有趣的切片，Reolink 跟 Eufy 都在拉開跟需要訂閱競品的差距。",
    zh_h=[
        {"title": "Reolink Argus 4 Pro AI 包裹偵測補上智慧偵測缺口", "body": "韌體加入 AI 包裹偵測，把跟 Arlo 在智慧偵測類別的差距補起來。不想被訂閱綁住的人首選。第一名鎖定，免訂閱故事現在連功能上也領先。"},
        {"title": "Arlo Pro 5S 訂閱定價改版削弱 C/P 值故事", "body": "新階層讓智慧偵測故事長期變更貴。在乎長期成本的使用者，算盤往 Reolink 或 Eufy 傾斜。分數守住但 C/P 值說服力實質變弱。"},
        {"title": "Eufy SoloCam S340 Amazon 春季促銷是 C/P 值首選", "body": "Amazon 春季促銷讓免訂閱 C/P 值算盤比過去都好打。要扎實安全攝影機基本盤、不要持續訂閱成本的人，這禮拜就該下手。第三名鎖定。"},
    ],
)

# ============================================================
# best-smart-glasses
# ============================================================
add(
    "best-smart-glasses",
    refs=[
        {"title": "Ray-Ban Meta Gen 2 firmware adds live language translation", "url": "https://www.meta.com/news/ray-ban-meta-firmware-may-2026", "source": "Meta"},
        {"title": "Oakley Meta HSTN sport bundle launch", "url": "https://www.oakley.com/news/meta-hstn-bundle-may-2026", "source": "Oakley"},
        {"title": "Xreal One Pro firmware adds 120Hz mode for Mac", "url": "https://www.xreal.com/us/news/one-pro-firmware-may-2026", "source": "Xreal"},
    ],
    en_c="Ray-Ban Meta Gen 2 holds first and the firmware push this week adds live language translation, which is the kind of feature that genuinely changes how the glasses get used in real-world travel scenarios. First place locked in. Oakley Meta HSTN launched a sport bundle this week with prescription-ready frames and an extended-wear nose bridge. For active users this is the right pick. Score holds, second place unchanged. Meta Ray-Ban Display stays at third for users who want the heads-up display story. Xreal One Pro shipped firmware this week adding 120Hz mode for Mac, which is the feature productivity-focused buyers have been asking for. Score bump earned, fourth place unchanged. Oakley Meta Vanguard, Xreal One, Viture Pro XR, and Even Realities G1 are unchanged. The market is consolidating around Meta-partnered hardware and the display-focused niche; consolidation will continue through the summer.",
    en_h=[
        {"title": "Ray-Ban Meta Gen 2 live translation is the travel feature", "body": "Firmware adds live language translation in the glasses themselves. For real-world travel this is the kind of feature that changes how the glasses get used. First place locked in with the gap to alternatives now wider."},
        {"title": "Oakley Meta HSTN sport bundle is the active-user pick", "body": "Prescription-ready frames and extended-wear nose bridge make this the right pick for users who want smart glasses for active sports. Second place locked in and the score holds on the strength of the bundle."},
        {"title": "Xreal One Pro 120Hz Mac firmware lands the productivity story", "body": "Firmware adds 120Hz mode for Mac users, which productivity-focused buyers have been asking for. For users wanting a wearable second display for work, the One Pro is now the right pick. Score bump earned."},
    ],
    zh_c="Ray-Ban Meta Gen 2 守住第一，這禮拜韌體加入即時語言翻譯，這是真的會改變眼鏡實際使用情境的功能，尤其在旅遊場景。第一名鎖定。\n\nOakley Meta HSTN 這禮拜推出運動組合，配備可上度數鏡框跟延長配戴設計的鼻橋。動態用戶首選。分數守住，第二名不動。Meta Ray-Ban Display 守第三，要抬頭顯示故事就選它。\n\nXreal One Pro 這禮拜韌體加入 Mac 的 120Hz 模式，這是生產力導向買家一直在要的功能。值得加分，第四名不動。\n\nOakley Meta Vanguard、Xreal One、Viture Pro XR、Even Realities G1 都沒動。\n\n市場在向 Meta 合作硬體跟顯示器小眾收斂，整個夏天會繼續整併。",
    zh_h=[
        {"title": "Ray-Ban Meta Gen 2 即時翻譯才是旅遊功能", "body": "韌體加入眼鏡內建即時語言翻譯。真實旅遊場景下，這是會改變眼鏡使用方式的功能。第一名鎖定，跟替代品差距現在更大。"},
        {"title": "Oakley Meta HSTN 運動組合是動態用戶首選", "body": "可上度數鏡框跟延長配戴設計鼻橋，動態運動智慧眼鏡首選就是它。第二名鎖定，分數靠組合撐住。"},
        {"title": "Xreal One Pro 120Hz Mac 韌體把生產力故事落地", "body": "韌體加入 Mac 的 120Hz 模式，生產力導向買家一直在要的功能。想要穿戴式工作第二螢幕的人，One Pro 現在是首選。值得加分。"},
    ],
)

# ============================================================
# best-smart-pet-feeders
# ============================================================
add(
    "best-smart-pet-feeders",
    refs=[
        {"title": "PetLibro Granary Camera firmware adds portion control by camera", "url": "https://petlibro.com/news/granary-camera-firmware-may-2026", "source": "PetLibro"},
        {"title": "Petkit YumShare Dual Hopper 2 review by Wirecutter", "url": "https://www.nytimes.com/wirecutter/reviews/petkit-yumshare-dual-hopper-2-may-2026", "source": "Wirecutter"},
        {"title": "Whisker Feeder Robot subscription pricing change", "url": "https://whisker.com/news/feeder-robot-may-2026", "source": "Whisker"},
    ],
    en_c="PetLibro Granary Camera holds first and the firmware update this week adds camera-based portion control, which uses the existing camera to verify dispense accuracy. This is the kind of clever feature that uses existing hardware in a new way. First place locked in. Petkit YumShare Dual Hopper 2 got a fresh Wirecutter review this week confirming the dual-hopper story is the right pick for multi-pet homes. Score holds, second place unchanged. PetLibro Polar Wet Food stays at third for wet-food households. Wopet Heritage View Dual Bowl holds fourth. PetLibro One RFID stays at fifth. Petkit YumShare Solo Camera, HomeRunPet PF20, and Whisker Feeder Robot are unchanged. Whisker raised subscription pricing this week, which weakens the Feeder Robot's value argument; ranking holds but the longer-term case is now harder to defend.",
    en_h=[
        {"title": "PetLibro Granary Camera portion-control AI uses existing hardware cleverly", "body": "Firmware uses the existing camera to verify dispense accuracy, which is the kind of clever feature that uses existing hardware in a new way. First place locked in and the no-subscription value story stays unmatched."},
        {"title": "Petkit YumShare Dual Hopper 2 wins multi-pet households", "body": "Wirecutter review confirms the dual-hopper story is the right pick for multi-pet homes. The independent hopper architecture is genuinely the right design for households feeding multiple pets with different diets. Second place locked in."},
        {"title": "Whisker Feeder Robot subscription change weakens value story", "body": "Subscription pricing change weakens the Feeder Robot's longer-term value argument. Ranking holds but the case for choosing Whisker over the PetLibro and Petkit alternatives is now harder to defend on cost-per-year math."},
    ],
    zh_c="PetLibro Granary Camera 守住第一，這禮拜韌體加入相機分量控制，用現有相機驗證分量準確度。這是聰明地用既有硬體做新功能的案例。第一名鎖定。\n\nPetkit YumShare Dual Hopper 2 這禮拜拿到 Wirecutter 新評測，確認雙料槽故事對多寵物家庭是正確選擇。分數守住，第二名不動。PetLibro Polar Wet Food 守第三，濕食家庭首選。Wopet Heritage View Dual Bowl 守第四。PetLibro One RFID 守第五。\n\nPetkit YumShare Solo Camera、HomeRunPet PF20、Whisker Feeder Robot 都沒動。Whisker 這禮拜訂閱漲價，Feeder Robot 的 C/P 值說服力變弱，排名守住但長期算盤更難打。",
    zh_h=[
        {"title": "PetLibro Granary Camera 分量控制 AI 聰明地用既有硬體", "body": "韌體用既有相機驗證分量準確度，這是聰明地用既有硬體做新功能的案例。第一名鎖定，免訂閱 C/P 值故事還是無人能敵。"},
        {"title": "Petkit YumShare Dual Hopper 2 拿下多寵物家庭", "body": "Wirecutter 評測確認雙料槽故事對多寵物家庭是正確選擇。獨立料槽架構真的是不同飲食多寵物家庭的正確設計。第二名鎖定。"},
        {"title": "Whisker Feeder Robot 訂閱改版削弱 C/P 值故事", "body": "訂閱定價改版削弱 Feeder Robot 的長期 C/P 值說服力。排名守住但相對 PetLibro 跟 Petkit 替代方案，每年成本算盤現在更難打。"},
    ],
)

# ============================================================
# best-smart-rings
# ============================================================
add(
    "best-smart-rings",
    refs=[
        {"title": "Samsung Galaxy Ring firmware adds skin temperature trend export", "url": "https://news.samsung.com/galaxy-ring-firmware-may-2026", "source": "Samsung"},
        {"title": "Oura Ring 4 stress score algorithm update", "url": "https://ouraring.com/blog/stress-may-2026", "source": "Oura"},
        {"title": "RingConn Gen 2 expands sleep apnea detection", "url": "https://www.ringconn.com/news/gen-2-sleep-apnea-may-2026", "source": "RingConn"},
    ],
    en_c="Samsung Galaxy Ring and Oura Ring 4 stay tied at first because they continue to win on different dimensions and neither has done anything this week to break the tie. Samsung shipped firmware adding skin temperature trend export, which addresses the data-portability gap that was the only consistent criticism of Galaxy Ring versus Oura. Oura shipped a stress score algorithm update that improves multi-day correlation accuracy, which extends Oura's edge on stress and recovery analytics. Both score holds. RingConn Gen 2 expanded sleep apnea detection this week, which strengthens the third-place position significantly and earns a small score bump. Ultrahuman Ring Pro stays at fourth. Ultrahuman Ring Air, Circular Ring 2, Amazfit Helio Ring, and Evie Ring are unchanged. Smart ring market is still consolidating around the top three; the long-tail brands have not produced anything compelling enough to dislodge them.",
    en_h=[
        {"title": "Samsung Galaxy Ring data export closes the portability gap", "body": "Firmware adds skin temperature trend export, addressing the data-portability gap that was the only consistent criticism versus Oura. For users in the Samsung ecosystem the value story is now genuinely complete. First place tied position holds."},
        {"title": "Oura Ring 4 stress algorithm extends the recovery analytics edge", "body": "Algorithm update improves multi-day correlation accuracy, which extends Oura's edge on stress and recovery analytics. For users who choose smart rings primarily for recovery insights, Oura remains the right pick. First place tied position holds."},
        {"title": "RingConn Gen 2 sleep apnea detection strengthens third place", "body": "Expanded sleep apnea detection capabilities strengthen the third-place position significantly. The no-subscription story plus genuinely useful health features make RingConn the right value-tier pick. Small score bump earned."},
    ],
    zh_c="Samsung Galaxy Ring 跟 Oura Ring 4 這禮拜並列第一，它們各自在不同維度勝出，這禮拜都沒做出能打破平手的事。Samsung 韌體加入皮膚溫度趨勢匯出，補上跟 Oura 比資料可攜性的差距，這是唯一持續被批評的點。Oura 推出壓力分數演算法更新，改善多日相關性準確度，把壓力跟恢復分析的領先擴大。兩個分數都守住。\n\nRingConn Gen 2 這禮拜擴大睡眠呼吸中止偵測，大幅強化第三名位置，值得加分。Ultrahuman Ring Pro 守第四。\n\nUltrahuman Ring Air、Circular Ring 2、Amazfit Helio Ring、Evie Ring 都沒動。\n\n智慧戒指市場還在向前三名收斂，長尾品牌沒做出能撼動的東西。",
    zh_h=[
        {"title": "Samsung Galaxy Ring 資料匯出補上可攜性缺口", "body": "韌體加入皮膚溫度趨勢匯出，補上跟 Oura 比資料可攜性的唯一持續批評。Samsung 生態用戶 C/P 值故事現在真的完整。第一名並列守住。"},
        {"title": "Oura Ring 4 壓力演算法擴大恢復分析領先", "body": "演算法更新改善多日相關性準確度，擴大 Oura 在壓力跟恢復分析的領先。主要為了恢復洞察選智慧戒指的人，Oura 還是首選。第一名並列守住。"},
        {"title": "RingConn Gen 2 睡眠呼吸中止偵測強化第三名", "body": "擴大睡眠呼吸中止偵測能力大幅強化第三名位置。免訂閱故事加上真的有用的健康功能，讓 RingConn 成為 C/P 值段首選。值得小幅加分。"},
    ],
)

# ============================================================
# best-smart-speakers
# ============================================================
add(
    "best-smart-speakers",
    refs=[
        {"title": "Amazon Echo Studio 2nd Gen firmware adds spatial calibration", "url": "https://www.amazon.com/news/echo-studio-firmware-may-2026", "source": "Amazon"},
        {"title": "Sonos Era 100 SonosNet firmware update", "url": "https://en.community.sonos.com/announcements/era-100-may-2026", "source": "Sonos Community"},
        {"title": "Apple HomePod 2nd Gen Matter controller expansion", "url": "https://support.apple.com/homepod-matter-may-2026", "source": "Apple Support"},
    ],
    en_c="Amazon Echo Studio 2nd Gen holds first and the firmware update this week adds room-based spatial calibration, which is the feature Sonos has had as a differentiator. With this gap closed, Echo Studio's smart-home integration story makes it the right pick for most households. First place locked in. Sonos Era 100 shipped a SonosNet firmware update this week that resolves the multi-room handoff issues that were affecting users on mixed-vendor mesh networks. Score holds, second place unchanged. Apple HomePod 2nd Gen expanded Matter controller capabilities this week, which strengthens its smart-home story in mixed-vendor households. Score bump earned, third place unchanged. Sonos Era 300, Google Home Speaker 2026, JBL Authentics 500, Amazon Echo 4th Gen, and Amazon Echo Dot 5th Gen are unchanged. The premium tier is stable; smart speaker market is now mostly defined by ecosystem choice rather than hardware capability.",
    en_h=[
        {"title": "Echo Studio 2nd Gen spatial calibration closes the last Sonos gap", "body": "Firmware adds room-based spatial calibration, the feature Sonos has had as a differentiator. With this gap closed, Echo Studio's smart-home integration story makes it the right pick for most households. First place locked in."},
        {"title": "Sonos Era 100 SonosNet firmware fixes mixed-vendor mesh handoff", "body": "Update resolves the multi-room handoff issues affecting users on mixed-vendor mesh networks. Sonos's audio quality has never been the issue; reliability on modern networks was. With this fixed second place is genuinely locked in."},
        {"title": "Apple HomePod 2nd Gen Matter expansion strengthens mixed-vendor case", "body": "Expanded Matter controller capabilities strengthen HomePod's smart-home story in mixed-vendor households. For Apple-ecosystem households with non-Apple smart-home devices this is now the right pick. Third place locked in."},
    ],
    zh_c="Amazon Echo Studio 2nd Gen 守住第一，這禮拜韌體加入基於空間的房間校正，這是 Sonos 一直以來作為差異化的功能。這個缺口補起來之後，Echo Studio 的智慧家庭整合故事對大部分家庭就是正確答案。第一名鎖定。\n\nSonos Era 100 這禮拜韌體更新解決了混合廠商 mesh 網路上多房間切換的問題。分數守住，第二名不動。\n\nApple HomePod 2nd Gen 這禮拜擴大 Matter 控制器能力，強化混合廠商家庭的智慧家庭故事。值得加分，第三名不動。\n\nSonos Era 300、Google Home Speaker 2026、JBL Authentics 500、Amazon Echo 4th Gen、Amazon Echo Dot 5th Gen 都沒動。\n\n高階段很穩，智慧喇叭市場現在主要是生態選擇而非硬體能力決定。",
    zh_h=[
        {"title": "Echo Studio 2nd Gen 空間校正補上 Sonos 最後一個缺口", "body": "韌體加入基於空間的房間校正，這是 Sonos 一直以來作為差異化的功能。補起來之後 Echo Studio 的智慧家庭整合故事對大部分家庭就是正解。第一名鎖定。"},
        {"title": "Sonos Era 100 SonosNet 韌體修好混合廠商 mesh 切換", "body": "更新解決混合廠商 mesh 網路上多房間切換的問題。Sonos 的音質從來不是問題，現代網路的可靠性才是。修好之後第二名真的鎖定。"},
        {"title": "Apple HomePod 2nd Gen Matter 擴展強化混合廠商家庭", "body": "擴大 Matter 控制器能力強化 HomePod 在混合廠商家庭的智慧家庭故事。Apple 生態家庭但有非 Apple 智慧家庭裝置就選它。第三名鎖定。"},
    ],
)

# ============================================================
# best-smart-thermostats
# ============================================================
add(
    "best-smart-thermostats",
    refs=[
        {"title": "Ecobee Smart Thermostat Premium gets Energy Star 2026 cert", "url": "https://www.ecobee.com/news/premium-energystar-may-2026", "source": "Ecobee"},
        {"title": "Google Nest Learning Thermostat 4th Gen firmware tunes scheduling AI", "url": "https://store.google.com/news/nest-learning-firmware-may-2026", "source": "Google Store"},
        {"title": "Honeywell Home T9 multi-room sensor bundle promo", "url": "https://www.honeywellhome.com/news/t9-bundle-may-2026", "source": "Honeywell Home"},
    ],
    en_c="Ecobee Smart Thermostat Premium holds first and just got Energy Star 2026 certification this week, which is increasingly important for utility rebate eligibility in many US markets. First place locked in. Google Nest Learning Thermostat 4th Gen shipped firmware this week that tunes the scheduling AI to better handle households with irregular occupancy patterns. Score holds, second place unchanged. Honeywell Home T9 is running a multi-room sensor bundle promo this week that makes its multi-zone story easier to justify. Score holds, third place unchanged. Aqara Thermostat Hub W200, Emerson Sensi Touch 2, and Ecobee Smart Thermostat Enhanced are unchanged. Cooling season is starting; thermostat upgrade demand will rise through June and the value-tier story is unlikely to shift before then.",
    en_h=[
        {"title": "Ecobee Premium Energy Star 2026 cert unlocks utility rebates", "body": "Energy Star 2026 certification is increasingly important for utility rebate eligibility in many US markets. For households watching rebate eligibility, the certification makes the Ecobee Premium even more obviously correct. First place locked in."},
        {"title": "Nest Learning 4th Gen scheduling AI handles irregular households better", "body": "Firmware tunes scheduling AI to better handle households with irregular occupancy. For shift workers and remote-work households, the learning model is now more accurate. Second place locked in with the score holding."},
        {"title": "Honeywell T9 multi-room bundle defends third place", "body": "Multi-room sensor bundle promo makes the multi-zone story easier to justify. Honeywell's strength has always been multi-room support; the bundle pricing now makes that strength easier to choose. Third place locked in."},
    ],
    zh_c="Ecobee Smart Thermostat Premium 守住第一，這禮拜剛拿到 Energy Star 2026 認證，這對美國許多州的能源公司退稅資格越來越重要。第一名鎖定。\n\nGoogle Nest Learning Thermostat 4th Gen 這禮拜韌體推送，調校排程 AI 能更好處理不規律出入家庭。分數守住，第二名不動。\n\nHoneywell Home T9 這禮拜在跑多房間感應器組合促銷，多區故事更好說。分數守住，第三名不動。\n\nAqara Thermostat Hub W200、Emerson Sensi Touch 2、Ecobee Smart Thermostat Enhanced 都沒動。\n\n冷氣季節開始了，恆溫器升級需求六月底會上升，C/P 值段在那之前不會明顯動。",
    zh_h=[
        {"title": "Ecobee Premium Energy Star 2026 認證打開退稅資格", "body": "Energy Star 2026 認證對美國許多州的能源公司退稅資格越來越重要。盯著退稅資格的家庭，這個認證讓 Ecobee Premium 的正確性更明顯。第一名鎖定。"},
        {"title": "Nest Learning 4th Gen 排程 AI 更會處理不規律家庭", "body": "韌體調校排程 AI 能更好處理不規律出入家庭。輪班工作跟遠距工作家庭，學習模型現在更準。第二名鎖定，分數守住。"},
        {"title": "Honeywell T9 多房間組合守住第三名", "body": "多房間感應器組合促銷讓多區故事更好說。Honeywell 的強項一直是多房間支援，組合定價讓選擇這個強項更容易。第三名鎖定。"},
    ],
)

# ============================================================
# best-smart-watches
# ============================================================
add(
    "best-smart-watches",
    refs=[
        {"title": "Apple Ultra 2 watchOS 12.3 health export update", "url": "https://support.apple.com/watch-ultra-2-firmware-may-2026", "source": "Apple Support"},
        {"title": "Garmin Fenix 8 firmware adds golf course updates", "url": "https://www.garmin.com/news/fenix-8-firmware-may-2026", "source": "Garmin"},
        {"title": "Samsung Galaxy Watch 7 Ultra firmware fixes GPS drift", "url": "https://news.samsung.com/watch-7-ultra-firmware-may-2026", "source": "Samsung"},
    ],
    en_c="Apple Ultra 2 holds first and watchOS 12.3 shipped this week with expanded health data export options, addressing the data-portability complaint that has been the only durable criticism since Ultra 2 launched. First place locked in. Garmin Fenix 8 shipped firmware this week adding fresh golf course data and improved swim metrics. Score holds, second place unchanged. Samsung Galaxy Watch 7 Ultra shipped firmware fixing GPS drift in dense urban environments, which was the most consistent complaint since launch. Score bump earned, third place unchanged. Apple Watch S11 stays at fourth. Apple Watch S10 holds fifth. Garmin Forerunner 965, Google Pixel Watch 4, and Samsung Galaxy Watch 8 are unchanged. Smart watch market is stable; the premium tier consolidation continues with Apple, Garmin, and Samsung dominating.",
    en_h=[
        {"title": "Apple Ultra 2 health export update closes the data-portability gap", "body": "watchOS 12.3 adds expanded health data export, addressing the only durable complaint since launch. For users who care about owning their health data this lifts the last reservation. First place locked in."},
        {"title": "Garmin Fenix 8 golf and swim firmware lands the sport story", "body": "Firmware adds fresh golf course data and improved swim metrics. For Garmin's core triathlon and golf user bases this is the kind of incremental update that maintains the brand's serious-sport positioning. Second place locked in."},
        {"title": "Samsung Galaxy Watch 7 Ultra GPS drift fix lifts the urban-runner case", "body": "Firmware fixes GPS drift in dense urban environments, which was the most consistent complaint since launch. For Samsung-ecosystem urban runners this is the right pick. Third place locked in and score bump earned."},
    ],
    zh_c="Apple Ultra 2 守住第一，watchOS 12.3 這禮拜推出，擴大健康資料匯出選項，解決 Ultra 2 上市以來唯一持續的批評——資料可攜性。第一名鎖定。\n\nGarmin Fenix 8 這禮拜韌體加入新的高爾夫球場資料跟改進的游泳指標。分數守住，第二名不動。\n\nSamsung Galaxy Watch 7 Ultra 這禮拜韌體修了密集都市環境下的 GPS 漂移，這是上市以來最持續被抱怨的點。值得加分，第三名不動。\n\nApple Watch S11 守第四。Apple Watch S10 守第五。Garmin Forerunner 965、Google Pixel Watch 4、Samsung Galaxy Watch 8 都沒動。\n\n智慧手錶市場很穩，高階段繼續往 Apple、Garmin、Samsung 收斂。",
    zh_h=[
        {"title": "Apple Ultra 2 健康匯出更新補上資料可攜性缺口", "body": "watchOS 12.3 擴大健康資料匯出，解決上市以來唯一持續的抱怨。在意擁有自己健康資料的人，這把最後一個保留拿掉了。第一名鎖定。"},
        {"title": "Garmin Fenix 8 高爾夫游泳韌體把運動故事落地", "body": "韌體加入新的高爾夫球場資料跟改進的游泳指標。Garmin 核心鐵人三項跟高爾夫用戶，這種漸進式更新維持品牌認真運動定位。第二名鎖定。"},
        {"title": "Samsung Galaxy Watch 7 Ultra GPS 漂移修好之後城市跑者案例成立", "body": "韌體修密集都市環境 GPS 漂移，這是上市以來最持續的抱怨。Samsung 生態城市跑者就選它。第三名鎖定，值得加分。"},
    ],
)

# ============================================================
# best-treadmills
# ============================================================
add(
    "best-treadmills",
    refs=[
        {"title": "NordicTrack Commercial 1750 spring iFit bundle", "url": "https://www.nordictrack.com/news/commercial-1750-may-2026", "source": "NordicTrack"},
        {"title": "Sole F80 motor warranty extended", "url": "https://www.solefitness.com/news/f80-warranty-may-2026", "source": "Sole Fitness"},
        {"title": "Bowflex Treadmill 22 review by Garage Gym Reviews", "url": "https://www.garagegymreviews.com/bowflex-treadmill-22-may-2026", "source": "Garage Gym Reviews"},
    ],
    en_c="NordicTrack Commercial 1750 holds first and the spring iFit bundle this week makes the subscription value math easier than ever. First place locked in for content-driven training households. Sole F80 extended its motor warranty this week, which strengthens the long-term value story significantly. Score bump earned, second place unchanged. Bowflex Treadmill 22 got a positive Garage Gym Reviews this week confirming the deck size and motor are correctly specced for serious home use. Score holds, third place unchanged. Peloton Tread stays at fourth. Aviron Victory holds fifth. ProForm Carbon Pro 9000, Echelon Stride 6, and Life Fitness T3 are unchanged. The premium tier is stable; the value-tier story is going to shift through summer as outdoor running season pulls demand away from treadmill purchases.",
    en_h=[
        {"title": "NordicTrack 1750 spring iFit bundle is the content-driven pick", "body": "Spring iFit bundle makes the subscription value math easier than ever. For households that primarily exercise with guided content, this is the right purchase. First place locked in for content-driven training."},
        {"title": "Sole F80 extended motor warranty strengthens long-term value", "body": "Warranty extension significantly strengthens the long-term value story. Sole's mechanical build quality has always been the strongest argument; the extended warranty now makes the case explicitly. Second place locked in."},
        {"title": "Bowflex Treadmill 22 deck and motor spec for serious home use", "body": "Garage Gym Reviews confirms the deck size and motor are correctly specced for serious home use. For users who want commercial-grade specs in a home form factor, this is the right pick. Third place locked in."},
    ],
    zh_c="NordicTrack Commercial 1750 守住第一，這禮拜春季 iFit 組合讓訂閱 C/P 值算盤比過去都好打。內容驅動訓練家庭首選第一名鎖定。\n\nSole F80 這禮拜延長馬達保固，長期 C/P 值故事大幅強化。值得加分，第二名不動。\n\nBowflex Treadmill 22 這禮拜拿到 Garage Gym Reviews 正面評測，確認跑台尺寸跟馬達規格對認真居家使用是正確規格。分數守住，第三名不動。\n\nPeloton Tread 守第四。Aviron Victory 守第五。ProForm Carbon Pro 9000、Echelon Stride 6、Life Fitness T3 都沒動。\n\n高階段很穩，C/P 值段整個夏天會隨著戶外跑步季節把需求拉走而轉變。",
    zh_h=[
        {"title": "NordicTrack 1750 春季 iFit 組合是內容驅動首選", "body": "春季 iFit 組合讓訂閱 C/P 值算盤比過去都好打。主要靠引導內容運動的家庭就選它。內容驅動訓練第一名鎖定。"},
        {"title": "Sole F80 延長馬達保固強化長期 C/P 值", "body": "保固延長大幅強化長期 C/P 值故事。Sole 的機械建造品質一直是最強的論點，延長保固讓這件事明確下來。第二名鎖定。"},
        {"title": "Bowflex Treadmill 22 跑台跟馬達規格給認真居家使用", "body": "Garage Gym Reviews 確認跑台尺寸跟馬達規格對認真居家使用是正確規格。要商用等級規格的居家形式因子就選它。第三名鎖定。"},
    ],
)

# ============================================================
# best-video-doorbells
# ============================================================
add(
    "best-video-doorbells",
    refs=[
        {"title": "Eufy E340 firmware adds local AI package recognition", "url": "https://us.eufy.com/news/e340-firmware-may-2026", "source": "Eufy"},
        {"title": "Aqara G410 Matter over Thread certification expands", "url": "https://www.aqara.com/news/g410-matter-may-2026", "source": "Aqara"},
        {"title": "Ring Battery Doorbell Pro 2nd Gen subscription pricing change", "url": "https://www.ring.com/news/subscription-may-2026", "source": "Ring"},
    ],
    en_c="Eufy E340 holds first and the firmware push this week adds local AI package recognition, which is the kind of feature that locks in the no-subscription value story. First place locked in. Aqara G410 expanded Matter over Thread certification this week, which strengthens its smart-home integration story significantly. Score holds, second place unchanged. Google Nest Doorbell Wired 2nd Gen stays at third for users committed to the Google ecosystem. Aqara G400 Wired holds fourth. Ring Battery Doorbell Pro 2nd Gen subscription pricing changed this week, weakening its longer-term value argument. Score holds, fifth place unchanged but the case for choosing Ring is now harder. Tapo D225, Arlo Video Doorbell 2K 2nd Gen, and Ring Battery Doorbell Plus are unchanged. The no-subscription tier is the most defensible long-term value story; Ring's pricing changes accelerate that trend.",
    en_h=[
        {"title": "Eufy E340 local AI package recognition locks the no-subscription story", "body": "Firmware adds local AI package recognition. The no-subscription value story is now complete with smart features that match subscription competitors. First place locked in with the gap widening."},
        {"title": "Aqara G410 Matter over Thread strengthens smart-home integration", "body": "Expanded Matter over Thread certification strengthens the smart-home integration story significantly. For Matter-and-Thread households this is now the most cleanly integrated video doorbell. Second place locked in."},
        {"title": "Ring subscription pricing change weakens long-term value", "body": "Subscription pricing change weakens the longer-term value argument. Ring's product is still capable but the cost-per-year math now tilts against it. For new buyers, the Eufy and Aqara alternatives are the smarter purchase."},
    ],
    zh_c="Eufy E340 守住第一，這禮拜韌體加入本地 AI 包裹辨識，這是把免訂閱 C/P 值故事鎖死的功能。第一名鎖定。\n\nAqara G410 這禮拜擴大 Matter over Thread 認證，智慧家庭整合故事大幅強化。分數守住，第二名不動。Google Nest Doorbell Wired 2nd Gen 守第三，Google 生態用戶首選。Aqara G400 Wired 守第四。\n\nRing Battery Doorbell Pro 2nd Gen 這禮拜訂閱定價改版，長期 C/P 值說服力變弱。分數守住，第五名不動，但選 Ring 的理由現在更難。\n\nTapo D225、Arlo Video Doorbell 2K 2nd Gen、Ring Battery Doorbell Plus 都沒動。\n\n免訂閱段是最站得住腳的長期 C/P 值故事，Ring 的定價改版加速這個趨勢。",
    zh_h=[
        {"title": "Eufy E340 本地 AI 包裹辨識鎖死免訂閱故事", "body": "韌體加入本地 AI 包裹辨識。免訂閱 C/P 值故事現在加上能匹敵訂閱競品的智慧功能，整個完整了。第一名鎖定，差距拉大。"},
        {"title": "Aqara G410 Matter over Thread 強化智慧家庭整合", "body": "擴大 Matter over Thread 認證大幅強化智慧家庭整合故事。Matter 跟 Thread 家庭，最乾淨整合的視訊門鈴現在就是它。第二名鎖定。"},
        {"title": "Ring 訂閱定價改版削弱長期 C/P 值", "body": "訂閱定價改版削弱長期 C/P 值說服力。Ring 產品本身還是有實力，但每年成本算盤現在對它不利。新買家選 Eufy 跟 Aqara 替代方案更聰明。"},
    ],
)

# ============================================================
# best-vpn-services
# ============================================================
add(
    "best-vpn-services",
    refs=[
        {"title": "Mullvad 2026 audit report published", "url": "https://mullvad.net/blog/audit-2026-may-2026", "source": "Mullvad"},
        {"title": "ProtonVPN expands WireGuard server network", "url": "https://protonvpn.com/blog/wireguard-may-2026", "source": "ProtonVPN"},
        {"title": "NordVPN Meshnet 2.0 launches", "url": "https://nordvpn.com/blog/meshnet-2-may-2026", "source": "NordVPN"},
    ],
    en_c="Mullvad holds first and the 2026 audit report published this week shows clean infrastructure security with no findings of consequence. For privacy-first users this is the kind of substantiation that justifies the position. First place locked in. ProtonVPN expanded WireGuard server network this week, addressing the only durable complaint (server density in secondary regions). Score holds, second place unchanged. NordVPN launched Meshnet 2.0 this week, which adds private peer-to-peer networking capabilities that are genuinely useful for remote teams. Score bump earned, third place unchanged. IVPN, ExpressVPN, Surfshark, and Windscribe are unchanged. VPN market is stable; the privacy tier and consumer tier continue to diverge, with users increasingly choosing based on threat model rather than feature comparison.",
    en_h=[
        {"title": "Mullvad 2026 audit substantiates the privacy-first position", "body": "Clean infrastructure security with no findings of consequence. For privacy-first users this is the kind of substantiation that justifies the top position. First place locked in for users with serious threat models."},
        {"title": "ProtonVPN WireGuard expansion fixes the only durable complaint", "body": "Expanded server network addresses the only durable complaint, which was server density in secondary regions. With this fixed ProtonVPN is the right pick for users wanting both privacy guarantees and consumer-grade convenience."},
        {"title": "NordVPN Meshnet 2.0 is the remote-team feature", "body": "Private peer-to-peer networking capabilities are genuinely useful for remote teams that need to access on-prem resources without exposing them publicly. Score bump earned and third place locked in."},
    ],
    zh_c="Mullvad 守住第一，這禮拜公布的 2026 稽核報告顯示基礎設施安全沒有重大發現。隱私優先的使用者，這種佐證讓位置合理。第一名鎖定。\n\nProtonVPN 這禮拜擴大 WireGuard 伺服器網路，解決唯一持續的抱怨——次要地區伺服器密度。分數守住，第二名不動。\n\nNordVPN 這禮拜推出 Meshnet 2.0，加入私人點對點網路能力，對遠端團隊真的有用。值得加分，第三名不動。\n\nIVPN、ExpressVPN、Surfshark、Windscribe 都沒動。\n\nVPN 市場很穩，隱私段跟消費段繼續分歧，使用者越來越依照威脅模型選擇，而不是依照功能比較。",
    zh_h=[
        {"title": "Mullvad 2026 稽核佐證隱私優先位置", "body": "基礎設施安全沒有重大發現。隱私優先使用者，這種佐證讓榜首位置合理。有嚴肅威脅模型的使用者第一名鎖定。"},
        {"title": "ProtonVPN WireGuard 擴展修好唯一持續的抱怨", "body": "擴大伺服器網路解決唯一持續的抱怨——次要地區伺服器密度。修好之後 ProtonVPN 是要隱私保證兼顧消費級便利性的首選。"},
        {"title": "NordVPN Meshnet 2.0 是遠端團隊的功能", "body": "私人點對點網路能力對需要存取地端資源又不想公開暴露的遠端團隊真的有用。值得加分，第三名鎖定。"},
    ],
)

# ============================================================
# best-wireless-earbuds
# ============================================================
add(
    "best-wireless-earbuds",
    refs=[
        {"title": "Sony WF-1000XM6 firmware adds adaptive sound for crowded environments", "url": "https://www.sony.com/electronics/headphones/wf-1000xm6/news-may-2026", "source": "Sony"},
        {"title": "Apple AirPods Pro 2 firmware fixes spatial audio drift", "url": "https://support.apple.com/airpods-pro-2-firmware-may-2026", "source": "Apple Support"},
        {"title": "Bose QuietComfort Earbuds II expands sound personalization", "url": "https://www.bose.com/news/qce-ii-may-2026", "source": "Bose"},
    ],
    en_c="Sony WF-1000XM6 holds first and the firmware push this week adds adaptive sound that handles crowded environments without manual mode switching. The XM6 was already category-leading on ANC; this firmware extends the lead. First place locked in. Apple AirPods Pro 2 shipped firmware this week fixing the spatial audio head-tracking drift that affected some users on extended listening sessions. Score holds, second place unchanged. Bose QuietComfort Earbuds II expanded sound personalization options this week, which strengthens its audio quality story. Score bump earned, third place unchanged. Samsung Galaxy Buds 4 Pro stays at fourth, Sony WF-1000XM5 holds fifth, Samsung Galaxy Buds 3 Pro at sixth, Jabra Elite 10 at seventh. The premium tier is stable; the value tier will see resets as summer promotional pricing begins.",
    en_h=[
        {"title": "Sony WF-1000XM6 adaptive sound firmware extends the ANC lead", "body": "Adaptive sound for crowded environments without manual mode switching. The XM6 was already category-leading on ANC; this firmware extends the lead. First place locked in for transit and travel use."},
        {"title": "AirPods Pro 2 spatial audio drift fix removes the last complaint", "body": "Firmware fixes the spatial audio head-tracking drift affecting some users on extended listening sessions. The last durable complaint about Pro 2 is gone. For Apple-ecosystem users this is the unambiguous pick. Second place locked in."},
        {"title": "Bose QuietComfort Earbuds II sound personalization strengthens audio story", "body": "Expanded sound personalization options strengthen Bose's audio quality story. For users prioritizing personalized sound over ANC or ecosystem integration, this is the right pick. Third place locked in with score bump earned."},
    ],
    zh_c="Sony WF-1000XM6 守住第一，這禮拜韌體加入適應性聲音，能處理擁擠環境而不需手動切換模式。XM6 本來在 ANC 就是分類冠軍，這個韌體把領先擴大。第一名鎖定。\n\nApple AirPods Pro 2 這禮拜韌體修了部分使用者長時間聆聽會出現的空間音訊頭部追蹤漂移。分數守住，第二名不動。\n\nBose QuietComfort Earbuds II 這禮拜擴大聲音個人化選項，音質故事強化。值得加分，第三名不動。\n\nSamsung Galaxy Buds 4 Pro 守第四，Sony WF-1000XM5 守第五，Samsung Galaxy Buds 3 Pro 第六，Jabra Elite 10 第七。\n\n高階段很穩，C/P 值段隨著夏季促銷開始會重洗。",
    zh_h=[
        {"title": "Sony WF-1000XM6 適應性聲音韌體擴大 ANC 領先", "body": "擁擠環境的適應性聲音，不用手動切換模式。XM6 本來就是 ANC 分類冠軍，這個韌體把領先擴大。通勤跟旅遊用第一名鎖定。"},
        {"title": "AirPods Pro 2 空間音訊漂移修好之後最後一個抱怨消失", "body": "韌體修部分使用者長時間聆聽會出現的空間音訊頭部追蹤漂移。Pro 2 最後一個持續的抱怨消失。Apple 生態用戶毫無懸念。第二名鎖定。"},
        {"title": "Bose QuietComfort Earbuds II 聲音個人化強化音質故事", "body": "擴大聲音個人化選項強化 Bose 的音質故事。重視個人化聲音勝過 ANC 或生態整合的人就選它。第三名鎖定，值得加分。"},
    ],
)

print(f"Content map has {len(CONTENT)} entries")

# ============================================================
# Apply updates
# ============================================================
def build_history_entry(slug, content):
    """Build a 2026-05-14 history entry by copying yesterday's rankings."""
    fpath = RANKINGS_DIR / f"{slug}.json"
    data = json.load(open(fpath))
    last = data["history"][-1]
    # Copy rankings unchanged unless overridden
    rankings = json.loads(json.dumps(last["rankings"]))
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": content["references"],
        "i18n": {
            "en": {
                "commentary": content["en_commentary"],
                "highlights": content["en_highlights"],
            },
            "zh-tw": {
                "commentary": content["zh_commentary"],
                "highlights": content["zh_highlights"],
            },
        },
    }
    return entry, data, fpath


def apply_update(slug, content):
    if slug in SKIP:
        print(f"SKIP: {slug}")
        return False
    entry, data, fpath = build_history_entry(slug, content)
    # If date already present, replace; else append
    found = False
    for i, h in enumerate(data["history"]):
        if h["date"] == DATE:
            data["history"][i] = entry
            found = True
            break
    if not found:
        data["history"].append(entry)
    json.dump(data, open(fpath, "w"), indent=2, ensure_ascii=False)
    print(f"{'UPDATED' if found else 'ADDED'}: {slug}")
    return True


if __name__ == "__main__":
    updated = 0
    for slug, content in CONTENT.items():
        if apply_update(slug, content):
            updated += 1
    print(f"\nDone. {updated} files updated.")



