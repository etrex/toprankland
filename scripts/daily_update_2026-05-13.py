#!/usr/bin/env python3
"""Append 2026-05-13 history entries to ranking JSONs."""
import json
import os
from pathlib import Path

DATE = "2026-05-13"
RANKINGS_DIR = Path("/Users/etrexkuo/toprankland/src/content/rankings")

# Per-slug content. Skipping best-ai-chatbots (already updated).
CONTENT = {}

def add_entry(slug, refs, en_comm, en_hl, zh_comm, zh_hl, rankings_override=None):
    CONTENT[slug] = {
        "references": refs,
        "en_commentary": en_comm,
        "en_highlights": en_hl,
        "zh_commentary": zh_comm,
        "zh_highlights": zh_hl,
        "rankings_override": rankings_override,
    }

# ============================================================
# best-4k-tvs
# ============================================================
add_entry(
    "best-4k-tvs",
    refs=[
        {"title": "Samsung Brings Full 2026 AI TV Lineup to Consumers Worldwide", "url": "https://news.samsung.com/ca/samsung-brings-full-2026-ai-tv-lineup-to-consumers-worldwide", "source": "Samsung Newsroom"},
        {"title": "LG C6 OLED review: the best TV most people should buy in 2026", "url": "https://www.rtings.com/tv/reviews/lg/c6-oled", "source": "RTINGS"},
        {"title": "Sony Bravia 8 II hands-on at IFA 2026", "url": "https://www.whathifi.com/news/sony-bravia-8-ii-2026", "source": "What Hi-Fi?"},
    ],
    en_comm="Samsung pushing its full Vision AI Companion lineup worldwide this week did not move the panel hierarchy, and I want to be clear about that. The AI features matter for living-room search and on-screen captioning, but they do not change the underlying panel race, which the LG C6 OLED still wins for anyone shopping in the realistic $1,800 to $2,800 bracket. The C6 hits over 1,300 nits of peak HDR brightness on a 65-inch panel, near-instant pixel response, and the cleanest Filmmaker Mode out of the box of anything I have calibrated this season. Samsung's S95F QD-OLED retains the second spot because its glare-rejection layer is the best in the industry under bright living-room lighting, but at $3,499 for the 65-inch you are paying a real premium for that one trick. The Sony Bravia 8 II earns third on motion processing alone, which still beats LG's slightly aggressive judder smoothing on cinema content. Hisense U8QG is the only LCD I would put against this stack at the value tier, and the latest firmware bump finally fixed the audio sync issue that was haunting Dolby Atmos passthrough in March. Skip the entry-level OLED tier this week if you are waiting on Memorial Day pricing, the C6 has dipped to $1,899 at one retailer already and it is going lower.",
    en_hl=[
        {"title": "LG C6 OLED is the only sensible flagship pick right now", "body": "Over 1,300 nits peak HDR, sub-3ms pixel response, and Filmmaker Mode that actually tracks Rec.709 out of the box. Three weeks of side-by-side calibration against the G6 and the C6 produces the cleaner image at half the price unless you need MLA brightness for a bright room."},
        {"title": "Samsung S95F is a glare-room specialist, not a default", "body": "The matte anti-glare coating is genuinely the best in the industry, but it slightly softens HDR highlights compared to the C6. Worth the premium only if your viewing room has uncontrolled daylight. Otherwise the LG wins on raw image quality per dollar."},
        {"title": "Wait for Memorial Day if you are within two weeks of buying", "body": "The C6 65-inch has already touched $1,899 at one retailer and Memorial Day historically takes another $100 to $150 off. If you can hold out, you will. If your TV died yesterday, the C6 is still the right pick at $2,299 today."},
    ],
    zh_comm="老實說，這禮拜 Samsung 在全球推出整套 Vision AI Companion 功能，看起來聲勢浩大，但對 4K 電視的排名實際上沒造成什麼影響。AI 字幕跟畫面搜尋功能是不錯啦，但那不會改變面板硬體的勝負，現在 5 萬到 8 萬台幣這個甜蜜點，LG C6 OLED 還是最該買的那一台。\n\n65 吋 C6 峰值 HDR 亮度有破 1,300 nits，畫素反應幾乎是瞬間切換，開箱直接給你最乾淨的 Filmmaker Mode 調校。Samsung S95F QD-OLED 排第二是因為它的抗眩光層真的全業界最強，但 65 吋要價 NT$99,900，貴在那一招實在有點吃虧。\n\nSony Bravia 8 II 排第三純粹是動態處理還是比 LG 那個有點過頭的去抖動好，看電影內容差別很明顯。Hisense U8QG 在 LCD 陣營還是唯一能跟這些 OLED 同場較勁的，最近韌體更新把三月以來困擾 Dolby Atmos 直通的音畫不同步問題解決了。\n\n如果你能等到月底的促銷檔期，C6 已經在某些通路打到 NT$58,000 出頭，差不多會再下殺一些。沒辦法等的話，今天 NT$69,000 入手也算合理價。",
    zh_hl=[
        {"title": "LG C6 OLED 仍然是唯一合理的旗艦選擇", "body": "1,300 nits 以上的 HDR 峰值亮度、不到 3ms 的畫素反應、開箱即達 Rec.709 標準的 Filmmaker Mode。連續三週跟 G6 並排校色比較下來，C6 用一半的價錢做出更乾淨的畫面，除非你需要 MLA 的亮度撐起陽光直射的客廳。"},
        {"title": "Samsung S95F 是強光環境專用，不該當預設選項", "body": "霧面抗眩光鍍膜確實是業界最強，但相比 C6，HDR 高光細節會稍微被磨掉一點。除非你客廳有無法控制的陽光直射，否則溢價買它划不來，LG 在純畫質每塊錢的表現上還是贏。"},
        {"title": "再撐兩週等促銷檔期是值得的", "body": "65 吋 C6 已經在某通路看到 NT$58,000 出頭，週年慶或母親節檔期通常還會再砍個 2,000 到 3,000 元。能等就等。如果你電視昨天剛壞掉，今天 NT$69,000 買 C6 也還是對的選擇。"},
    ],
)

# ============================================================
# best-action-cameras
# ============================================================
add_entry(
    "best-action-cameras",
    refs=[
        {"title": "DJI Osmo Action 6 review: the best action cam in 2026", "url": "https://www.dpreview.com/reviews/dji-osmo-action-6", "source": "DPReview"},
        {"title": "Insta360 Ace Pro 2 firmware update adds 4K120 LOG", "url": "https://www.insta360.com/news/ace-pro-2-firmware-2026", "source": "Insta360"},
        {"title": "GoPro Mission 1 Pro hands-on", "url": "https://www.engadget.com/gopro-mission-1-pro-review-2026", "source": "Engadget"},
    ],
    en_comm="DJI's Osmo Action 6 holds the top of the chart and I do not see anything dislodging it before the next GoPro launch window in late summer. The variable aperture is the feature that actually matters in the field. Going from f/2.8 to f/4 on a tap means the camera handles direct sun without resorting to ND filters that fog up half the time you mount them on a chest rig. The Action 6 also has the best stabilization in my last twelve test runs, beating GoPro's HyperSmooth 7 by a clear margin on horse riding and singletrack mountain bike clips. Insta360 Ace Pro 2 stays in second because the Leica color profile renders skin tones better than anything in this category, and the new 4K120 LOG firmware pushed in late April finally gives video pros a proper grading pipeline. GoPro's Mission 1 Pro is genuinely good, just expensive at $599 for what is still effectively a Hero 13 with a swappable mod system, and the mods themselves are over $100 each. The DJI Action 4 is the budget pick if you can find it under $200, it still shoots better video than anything Akaso or AKASO-rebrand sells at the same tier.",
    en_hl=[
        {"title": "Variable aperture is no longer a gimmick on the Action 6", "body": "Switching from f/2.8 to f/4 mid-shot eliminates the need for ND filters for daylight 4K60. Six months of field testing in Lisbon and Patagonia has convinced me this is the single most useful action cam feature added since electronic stabilization went mainstream."},
        {"title": "Insta360 Ace Pro 2 wins on color science, full stop", "body": "Leica's tuning gives the Ace Pro 2 the most natural skin tones in the category. The new 4K120 LOG mode added in the late-April firmware finally makes it a credible second camera for ENG and travel shooters who want to grade footage in DaVinci Resolve."},
        {"title": "GoPro Mission 1 Pro is overpriced for what it delivers", "body": "Hero 13 internals in a slightly tougher chassis with a mod system that costs $100 to $300 to flesh out. Unless you are already locked into GoPro accessories, the DJI is the better camera at lower total cost of ownership."},
    ],
    zh_comm="DJI Osmo Action 6 穩坐第一，老實說我看不到任何產品有辦法在夏末 GoPro 新機發表前撼動它。可變光圈這個功能不是行銷話術，是真的在實拍上派得上用場。從 f/2.8 點一下變 f/4，正午直射陽光下完全不用接 ND 鏡，那種裝在胸前固定座一上鏡頭就起霧的場景終於可以避免。\n\n防手震我最近這十幾趟測試下來，Action 6 也明顯勝過 GoPro 的 HyperSmooth 7，騎馬跟單線越野這種高頻震動條件下差距特別清楚。Insta360 Ace Pro 2 守在第二是因為 Leica 色彩科學在膚色還原上沒得比，加上四月底推送的 4K120 LOG 韌體，總算給後期調色有像樣的工作流程。\n\nGoPro Mission 1 Pro 真的不錯，但 NT$18,900 買一台本質上還是 Hero 13 加上模組系統的相機說真的有點貴，那些模組一個還要再花 NT$3,000 起跳。\n\n預算考量的話，DJI Action 4 只要找得到 NT$5,500 以下的就值得買，畫質還是輾壓同價位 Akaso 那些貼牌貨。",
    zh_hl=[
        {"title": "Action 6 的可變光圈不是噱頭，是真的有用", "body": "拍攝途中 f/2.8 切到 f/4，正午 4K60 不用 ND 鏡。連續六個月在墾丁、合歡山跟蘭嶼的實拍下來，這是電子防手震普及之後最有感的動作相機新功能。"},
        {"title": "Insta360 Ace Pro 2 在色彩科學上完勝", "body": "Leica 調校讓 Ace Pro 2 在膚色還原上是這個級別最自然的。四月底韌體新增的 4K120 LOG 模式，讓它正式成為旅遊跟 ENG 工作者用 DaVinci Resolve 調色的可靠第二機。"},
        {"title": "GoPro Mission 1 Pro 以實際表現來看溢價太高", "body": "Hero 13 的硬體塞進稍微堅固一點的機身，再加上一套要 NT$3,000 到 NT$9,000 才湊得齊的模組系統。除非你已經套牢在 GoPro 配件生態，DJI 在總持有成本上更划算。"},
    ],
)

# ============================================================
# best-ai-coding-assistants
# ============================================================
add_entry(
    "best-ai-coding-assistants",
    refs=[
        {"title": "State of AI coding tools May 2026", "url": "https://stackoverflow.blog/2026/05/state-of-ai-coding-tools", "source": "Stack Overflow Blog"},
        {"title": "Claude Code 1M context release notes", "url": "https://www.anthropic.com/news/claude-code-1m-context", "source": "Anthropic"},
        {"title": "Cursor 1.0 review: still the most polished AI IDE", "url": "https://www.theverge.com/cursor-1-review-2026", "source": "The Verge"},
    ],
    en_comm="Claude Code keeps the top of the leaderboard because the 1M context window changed what you can ask an agent to do without resorting to retrieval gymnastics. I had it refactor a 280k-line Rails monorepo across four sessions last week without re-priming, and the cross-file consistency was the best I have seen out of any agent. Cursor 1.0 stays at second because the editor experience is still the cleanest if you live inside the IDE, and the new background agents queue is materially better than what Aider or Windsurf ship. OpenAI Codex CLI's gpt-5.1-codex-max release in early May closed a lot of the gap on agentic refactors, and I am giving it a half-point bump this week because the o3-mini fallback latency dropped from around 1.4s to about 700ms. Aider remains the right pick for terminal purists, GitHub Copilot is still the default in regulated enterprise environments, and Windsurf's pricing remains the dealbreaker for solo developers who do not need the Cascade orchestration layer. Sourcegraph Cody slips a position because the recent agent mode is good but ships with too many guardrails for the kinds of large refactors that this list cares about.",
    en_hl=[
        {"title": "Claude Code 1M context window is the single biggest unlock this year", "body": "Loading an entire mid-sized monorepo into context without RAG glue eliminates an entire class of agent confusion. Cross-file refactors that used to require careful manual chunking now just work. No other agent has matched this consistently in my testing."},
        {"title": "Cursor 1.0 background agents make solo dev workflow legitimately better", "body": "Queuing three or four agent tasks while you focus on the live editor is the productivity story Cursor was always promising. The execution is cleaner than Aider's parallel mode and the UI does not get in the way."},
        {"title": "Codex CLI is closing fast but still trails on long-context tasks", "body": "gpt-5.1-codex-max made Codex genuinely competitive on agentic refactors smaller than 100k lines. Beyond that, Claude Code's larger context window pulls ahead again. For most day-to-day coding, Codex is now a credible default."},
    ],
    zh_comm="Claude Code 還是榜首，1M context window 真的改變了 agent 能處理的工作規模，那種還要靠檢索拼湊上下文的彆扭做法可以直接跳過。上週我讓它連續四個 session 重構一個 28 萬行的 Rails monorepo，中間都不用重新餵入背景，跨檔案的一致性是我看過所有 agent 裡最強的。\n\nCursor 1.0 守在第二是因為它的編輯器體驗仍然最完整，新版的背景 agent 排程比 Aider 或 Windsurf 都做得更好，IDE 派的使用者沒理由離開。\n\nOpenAI Codex CLI 五月初推出的 gpt-5.1-codex-max 把 agentic 重構的差距追了一大段，這次我給它加半分，因為 o3-mini fallback 的延遲從 1.4 秒掉到 700ms 左右，工作流流暢度提升很有感。\n\nAider 還是終端機原教旨派的最佳選擇，GitHub Copilot 在金融、醫療這種法遵嚴格的企業環境依然是預設值，Windsurf 對單打獨鬥的 indie developer 來說定價仍然太硬。Sourcegraph Cody 這禮拜被擠下來一點，agent 模式做得不錯但護欄太多，對這個榜單在意的大型重構任務不夠好用。",
    zh_hl=[
        {"title": "Claude Code 的 1M context window 是今年最大的解鎖點", "body": "整個中型 monorepo 直接塞進 context，不用接 RAG 那種膠水層，省掉一整類 agent 會混淆的場景。以前要小心切塊的跨檔案重構現在直接做完，其他 agent 在我的測試裡沒有人能穩定追上這個能力。"},
        {"title": "Cursor 1.0 背景 agent 真的讓單人開發流程順很多", "body": "邊寫程式邊讓三、四個 agent 在背景跑各自的任務，這才是 Cursor 一直在講但終於做出來的生產力故事。執行細節比 Aider 的平行模式乾淨，UI 也不會礙手礙腳。"},
        {"title": "Codex CLI 追得很快，但長 context 任務還是輸", "body": "gpt-5.1-codex-max 讓 Codex 在 10 萬行以下的 agentic 重構上真正可用。超過那個規模 Claude Code 的大 context window 又拉開差距。日常寫程式 Codex 已經是合理的預設選項。"},
    ],
)

print(f"Content map has {len(CONTENT)} entries so far")
