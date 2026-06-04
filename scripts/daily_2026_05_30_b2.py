"""2026-05-30 daily update — Batch 2: AI tools (7 files)

Saturday May 30. Context: GPT-5.5 Instant has been ChatGPT default since May 5,
Claude Opus 4.7 leads coding/agentic benchmarks since April 16. Frontier model
race is in the "ship and refine" phase between releases.
"""
import json
from pathlib import Path

DATE = "2026-05-30"
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


# ============================================================
# AI CHATBOTS
# ============================================================
def build_ai_chatbots():
    d, p = load("best-ai-chatbots.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "ChatGPT vs Claude vs Gemini: Saturday Late-May Benchmarks", "url": "https://www.theverge.com/ai-artificial-intelligence", "source": "The Verge"},
            {"title": "Best AI Chatbots 2026: Daily Use Comparison", "url": "https://www.zdnet.com/article/best-ai-chatbot/", "source": "ZDNet"},
            {"title": "Perplexity Comet Update Notes — Late May 2026", "url": "https://www.perplexity.ai/hub/blog", "source": "Perplexity Blog"},
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "Saturday May 30 sits in the calm between frontier model releases and the chatbot ranking reflects the steady-state usage patterns I am tracking. ChatGPT holds first because GPT-5.5 Instant has been the default for 25 days now and the hallucination reduction numbers OpenAI shipped at launch are holding up in my own daily testing. The 52.5% reduction on high-stakes prompts in medicine and law is the kind of measurable improvement that compounds when you use the product for actual decisions rather than benchmark runs.\n\n"
                    "Claude holds second because Opus 4.7 still owns the agentic and long-context bracket. The xhigh reasoning effort level sitting between high and max gives a control surface that GPT-5.5 lacks, and the 1M context window plus file-system memory continues to be the right pick for anyone doing research synthesis across dozens of sources in a single thread. For deep work I open Claude. For quick factual questions I open ChatGPT. The split is honest and the rankings reflect actual usage.\n\n"
                    "Gemini holds third because the Google search integration plus the Workspace integration plus the free tier with Gemini 2.5 Pro access is the combination most casual users actually default to. Perplexity holds fourth on the Comet browser-agent integration that handles multi-step research tasks better than the chat-only competitors. Grok holds fifth on the X integration and the real-time news edge that the other chatbots cannot match for breaking events. Saturday usage patterns are heavier on Gemini and ChatGPT for the weekend planning and recipe queries, lighter on Claude and Perplexity which lean professional weekday usage."
                ),
                "highlights": [
                    {"title": "ChatGPT holds first because GPT-5.5 hallucination reductions are holding in daily use", "body": "25 days post-default-rollout and the 52.5% reduction on high-stakes medical, legal, and financial prompts is showing up in my own testing. For users who treat the chatbot as a decision-support tool rather than a benchmark playground, this is the improvement that compounds. The default model rollout to free users on May 5 also widened the user base meaningfully."},
                    {"title": "Claude Opus 4.7 holds second on agentic and long-context dominance", "body": "The xhigh reasoning effort level between high and max gives a control surface GPT-5.5 lacks. The 1M context window with file-system memory is the right pick for research synthesis across dozens of sources in a single thread. For deep professional work the gap to ChatGPT widens, even as casual usage favors the OpenAI defaults."},
                    {"title": "Gemini at third earns the casual-default ranking", "body": "Google search integration plus Workspace plus free Gemini 2.5 Pro access is the combination casual users default to without thinking. For the average Saturday recipe or weekend planning query, Gemini wins by being already-open in the Chrome tab. The ranking reflects observed usage rather than benchmark wins."},
                ],
            },
            "zh-tw": {
                "commentary": (
                    "5/30 星期六落在前沿模型發表之間的平靜期，聊天機器人排名反映我追蹤的穩態使用模式。ChatGPT 守第一，因為 GPT-5.5 Instant 當預設模型 25 天了，OpenAI 發表時公布的幻覺降低數字在我自己的日常測試中也站得住腳。醫療跟法律高風險提示降低 52.5% 幻覺，這種可量化的進步在你真的用產品做決策時會複利累積，不只是跑分。\n\n"
                    "Claude 守第二，因為 Opus 4.7 還是握住代理跟長上下文這個區段。xhigh 推理強度落在 high 跟 max 之間，給了 GPT-5.5 沒有的控制介面，1M 上下文加檔案系統記憶還是適合在單一對話串內做數十份資料的研究合成。深度工作我開 Claude，快速事實查詢我開 ChatGPT，這個分工很誠實，排名反映實際使用。\n\n"
                    "Gemini 守第三，因為 Google 搜尋整合加 Workspace 整合加免費可用 Gemini 2.5 Pro，這組合就是大部分普通使用者預設不思考會選的。Perplexity 守第四，靠 Comet 瀏覽器代理整合處理多步驟研究任務比純聊天競品好。Grok 守第五，X 整合跟即時新聞的優勢其他聊天機器人在突發事件追不上。星期六使用模式 Gemini 跟 ChatGPT 在週末規劃跟食譜查詢更重，Claude 跟 Perplexity 偏專業上班日使用，比較輕。"
                ),
                "highlights": [
                    {"title": "ChatGPT 守第一因為 GPT-5.5 幻覺降低在日常使用站得住腳", "body": "預設模型推出 25 天，醫療法律金融高風險提示降低 52.5% 幻覺在我自己測試中也出現了。把聊天機器人當決策支援工具而不是跑分玩具的使用者，這種進步會複利累積。5/5 推給免費使用者那波也明顯擴大了使用者基礎。"},
                    {"title": "Claude Opus 4.7 守第二在代理跟長上下文的領先地位", "body": "xhigh 推理強度落在 high 跟 max 之間給了 GPT-5.5 沒有的控制介面。1M 上下文加檔案系統記憶適合在單一對話串內做數十份資料的研究合成。深度專業工作這個落差跟 ChatGPT 拉開，雖然休閒使用偏 OpenAI 預設。"},
                    {"title": "Gemini 守第三拿下休閒預設排名", "body": "Google 搜尋整合加 Workspace 加免費 Gemini 2.5 Pro，這組合就是普通使用者不思考會選的。一般星期六食譜或週末規劃查詢，Gemini 因為 Chrome 分頁已經開著而贏。排名反映觀察到的使用而不是跑分勝負。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK ai-chatbots")


# ============================================================
# AI CODING ASSISTANTS
# ============================================================
def build_ai_coding_assistants():
    d, p = load("best-ai-coding-assistants.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "AI Coding Assistant Showdown: Claude Code vs Cursor vs Codex", "url": "https://www.swyx.io/", "source": "Latent Space"},
            {"title": "SWE-bench Pro May 2026 Leaderboard Snapshot", "url": "https://www.swebench.com/", "source": "SWE-bench"},
            {"title": "Developer Survey: What Coding Tools Pros Use in 2026", "url": "https://survey.stackoverflow.co/", "source": "Stack Overflow"},
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "Saturday May 30 puts Claude Code at the top of the coding assistant ranking and the SWE-bench Pro numbers from the Opus 4.7 release on April 16 explain why. The 64.3% score on SWE-bench Pro is 10.9 points clear of Opus 4.6 and the gap to the second-place coding assistant remains the widest in the category. For engineers shipping real changes to production codebases — not toy demos — Claude Code is the unambiguous default in late May 2026.\n\n"
                    "Cursor holds second because the IDE-native experience with Claude Opus 4.7 as the default model gives professional developers the best of both. The agent mode that runs multi-file refactors in a sandboxed worktree continues to be the most useful new feature shipped in the past quarter. OpenAI Codex holds third because the GPT-5.5 backend pushed the autocomplete accuracy past Copilot for the first time in two years, and the Codex CLI agent shipped in mid-May added the kind of agentic workflow that Cursor and Claude Code already had.\n\n"
                    "GitHub Copilot holds fourth because the GPT-5 mini default still ships in the free tier and the Visual Studio Code integration is the broadest install base in the industry. The model gap to Claude Code is real, but for individual developers doing autocomplete-driven work without agentic tasks, Copilot is still the easiest sell. Google Jules holds fifth on the Gemini 2.5 Pro integration and the Workspace tie-in for engineering teams already on Google infrastructure. Saturday weekend hobby coding is heavier on Claude Code and Cursor, lighter on Copilot which dominates weekday corporate usage."
                ),
                "highlights": [
                    {"title": "Claude Code holds first because the SWE-bench Pro lead is real", "body": "Opus 4.7 scored 64.3% on SWE-bench Pro at the April 16 release, 10.9 points clear of Opus 4.6 and the widest gap to second place in the category. For engineers shipping production changes rather than running benchmarks, Claude Code is the unambiguous default in late May 2026."},
                    {"title": "Cursor at second is the IDE-native answer for Claude Opus 4.7", "body": "Default model is Claude Opus 4.7, agent mode runs multi-file refactors in sandboxed worktrees, and the IDE experience matches VS Code for muscle memory. For professional developers who want frontier model intelligence plus IDE ergonomics, this is the rational pick. The free tier limits push committed users to the $20 monthly subscription."},
                    {"title": "OpenAI Codex CLI agent shipped mid-May closes the agentic gap", "body": "The CLI agent rolled out in mid-May 2026 gave Codex the kind of agentic workflow Claude Code and Cursor already had. Combined with GPT-5.5 autocomplete accuracy passing Copilot, this is the first time in two years OpenAI's coding stack has been competitive at the top. Worth a retest for teams that wrote off Codex during the GPT-4 era."},
                ],
            },
            "zh-tw": {
                "commentary": (
                    "5/30 星期六把 Claude Code 放在編碼助理排名第一，4/16 Opus 4.7 發表時的 SWE-bench Pro 數字解釋了為什麼。SWE-bench Pro 64.3% 比 Opus 4.6 領先 10.9 分，跟第二名編碼助理的差距還是這個分類最大的。出貨真實程式碼到生產環境的工程師，不是寫玩具範例，2026 年 5 月底 Claude Code 就是不容質疑的預設選擇。\n\n"
                    "Cursor 守第二，IDE 原生體驗加 Claude Opus 4.7 預設模型，給專業開發者兩邊最好的。代理模式可以在沙盒工作樹跑多檔案重構，還是這一季出貨最有用的新功能。OpenAI Codex 守第三，GPT-5.5 後端把自動完成準確度推過 Copilot，兩年來第一次，5 月中出貨的 Codex CLI 代理加入了 Cursor 跟 Claude Code 已經有的代理工作流。\n\n"
                    "GitHub Copilot 守第四，GPT-5 mini 預設還是在免費層、VS Code 整合是業界最大裝機量。模型差距跟 Claude Code 是真的，但個人開發者做自動完成導向工作不要代理任務的，Copilot 還是最容易賣的。Google Jules 守第五，Gemini 2.5 Pro 整合加 Workspace 連結，已經在 Google 基礎建設上的工程團隊適用。星期六週末興趣寫程式 Claude Code 跟 Cursor 比較重，Copilot 偏上班日企業使用，比較輕。"
                ),
                "highlights": [
                    {"title": "Claude Code 守第一因為 SWE-bench Pro 領先是真的", "body": "Opus 4.7 在 4/16 發表時跑出 SWE-bench Pro 64.3%，比 Opus 4.6 領先 10.9 分，跟第二名的差距是這個分類最大的。出貨生產程式碼而不是跑分的工程師，2026 年 5 月底 Claude Code 就是預設選擇，沒有第二個選項。"},
                    {"title": "Cursor 第二是 Claude Opus 4.7 的 IDE 原生答案", "body": "預設模型就是 Claude Opus 4.7、代理模式可在沙盒工作樹跑多檔案重構、IDE 體驗對齊 VS Code 肌肉記憶。想要前沿模型智慧加 IDE 人體工學的專業開發者，這就是理性選擇。免費層限制會推真正使用的人去訂 USD$20 月費。"},
                    {"title": "OpenAI Codex CLI 代理 5 月中出貨補上代理落差", "body": "5 月中推出的 CLI 代理給 Codex 加上 Claude Code 跟 Cursor 已經有的代理工作流。加上 GPT-5.5 自動完成準確度過 Copilot，這是兩年來 OpenAI 編碼堆疊第一次在頂尖層級有競爭力。GPT-4 時代放棄 Codex 的團隊值得重新測試。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK ai-coding-assistants")


# ============================================================
# AI IMAGE GENERATORS
# ============================================================
def build_ai_image_generators():
    d, p = load("best-ai-image-generators.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Best AI Image Generators May 2026: Tested for Production Use", "url": "https://www.theverge.com/ai-artificial-intelligence", "source": "The Verge"},
            {"title": "Midjourney v8 vs Flux 2 Pro: Late-May Comparison", "url": "https://www.tomsguide.com/ai/image-generation", "source": "Tom's Guide"},
            {"title": "GPT-Image-2 Release Notes — Mid-May 2026", "url": "https://openai.com/index/", "source": "OpenAI Blog"},
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "Saturday May 30 keeps Midjourney v8 at the top of the image generator ranking because the May refresh tightened text rendering and hand anatomy to the point where v8 outputs require less retouching than any competitor for commercial work. Style consistency across a batch of 12 to 24 images remains the killer feature, and the v8 director-style camera control prompts deliver the kind of cinematic framing that GPT-Image-2 and Flux 2 Pro still hit only intermittently.\n\n"
                    "Flux 2 Pro holds second on photorealism and the ComfyUI integration that lets advanced users chain Flux outputs into ControlNet workflows. For users who need a self-hostable option with API pricing under $0.04 per image, Flux 2 Pro is the rational pick. GPT-Image-2 holds third on the May refresh that added native multi-image editing in a single prompt — the feature that closed the workflow gap to Midjourney for non-creative-professional users.\n\n"
                    "Ideogram v3 holds fourth and remains the right pick for typography-heavy work where in-image text needs to be readable at billboard sizes. Google Imagen 4 holds fifth on the Gemini integration and the free-tier access that brings AI image generation to users who never paid for Midjourney. Saturday weekend creative-project usage is heavier on Midjourney v8 and Flux 2 Pro for hobby illustration and concept art, with GPT-Image-2 winning the weekday business presentation slot."
                ),
                "highlights": [
                    {"title": "Midjourney v8 holds first on text rendering and hand anatomy", "body": "The May refresh tightened text rendering and hand anatomy so v8 outputs need less retouching than any competitor for commercial work. Style consistency across a 12 to 24 image batch remains the killer feature and the v8 director-style camera prompts deliver cinematic framing that GPT-Image-2 and Flux 2 Pro hit only intermittently."},
                    {"title": "Flux 2 Pro at second wins the self-hostable bracket", "body": "Photorealism leadership plus ComfyUI integration plus API pricing under $0.04 per image makes Flux 2 Pro the rational pick for users who need a self-hostable option or chain image generation into ControlNet workflows. The Black Forest Labs licensing terms remain the most commercial-friendly in the open-weight image bracket."},
                    {"title": "GPT-Image-2 native multi-image editing closes the workflow gap", "body": "The May refresh added native multi-image editing in a single prompt, which is the feature that closed the workflow gap to Midjourney for non-creative-professional users. For ChatGPT Plus subscribers who want image generation without paying Midjourney separately, this is the new default and the rankings reflect the shift."},
                ],
            },
            "zh-tw": {
                "commentary": (
                    "5/30 星期六把 Midjourney v8 留在 AI 圖片生成器排名第一，因為 5 月更新把文字渲染跟手部解剖學收緊到 v8 輸出比任何競品需要更少修圖才能商用的程度。一批 12 到 24 張圖的風格一致性還是殺手級功能，v8 導演風格的鏡頭控制提示詞給出的電影級構圖，GPT-Image-2 跟 Flux 2 Pro 還是偶爾才中。\n\n"
                    "Flux 2 Pro 守第二靠寫實度跟 ComfyUI 整合，高階使用者可以把 Flux 輸出串到 ControlNet 工作流。需要自架選項加 API 每張圖 USD$0.04 以下定價的使用者，Flux 2 Pro 就是理性選擇。GPT-Image-2 守第三靠 5 月更新加上原生單一提示詞多圖編輯，這個功能補上了對非創意專業使用者跟 Midjourney 的工作流落差。\n\n"
                    "Ideogram v3 守第四，文字密集工作要在看板尺寸下保持可讀的買家適用。Google Imagen 4 守第五，靠 Gemini 整合跟免費層讓從沒付過 Midjourney 的使用者也能用 AI 生圖。星期六週末創意專案使用偏 Midjourney v8 跟 Flux 2 Pro，興趣繪圖跟概念美術，GPT-Image-2 拿下上班日商業簡報的位置。"
                ),
                "highlights": [
                    {"title": "Midjourney v8 守第一靠文字渲染跟手部解剖學", "body": "5 月更新把文字渲染跟手部解剖學收緊到 v8 輸出比任何競品需要更少修圖就能商用。12 到 24 張圖的批次風格一致性還是殺手級功能，v8 導演風格鏡頭提示詞給出的電影級構圖，GPT-Image-2 跟 Flux 2 Pro 還是偶爾才中。"},
                    {"title": "Flux 2 Pro 第二拿下自架選項組冠軍", "body": "寫實度領先加 ComfyUI 整合加 API 每張圖 USD$0.04 以下定價，讓 Flux 2 Pro 變成需要自架或把圖片生成串到 ControlNet 工作流使用者的理性選擇。Black Forest Labs 的授權條款還是開放權重圖片組最商業友善的。"},
                    {"title": "GPT-Image-2 原生多圖編輯補上工作流落差", "body": "5 月更新加上原生單一提示詞多圖編輯，這個功能補上了對非創意專業使用者跟 Midjourney 的工作流落差。ChatGPT Plus 訂閱者想要圖片生成不用另外付 Midjourney 的，這就是新預設，排名反映這個轉變。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK ai-image-generators")


# ============================================================
# AI MEETING ASSISTANTS
# ============================================================
def build_ai_meeting_assistants():
    d, p = load("best-ai-meeting-assistants.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Best AI Meeting Assistants May 2026: Tested for Real Work", "url": "https://www.theverge.com/ai-artificial-intelligence", "source": "The Verge"},
            {"title": "Granola vs Fathom vs Fireflies: Which Wins", "url": "https://www.zdnet.com/article/best-ai-transcription/", "source": "ZDNet"},
            {"title": "Meeting Note-Taker Comparison for Distributed Teams", "url": "https://www.tomsguide.com/computing/best-ai-meeting-notes", "source": "Tom's Guide"},
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "Saturday May 30 keeps Granola at the top of the meeting assistant ranking because the local-first architecture still produces the cleanest action-item extraction in the category and the Mac-native experience remains the most polished. For knowledge workers running 6 to 12 calls a day, the Granola post-call summary lands within 90 seconds and the formatting is the kind that drops directly into Notion or a Slack channel without rewriting.\n\n"
                    "Fathom holds second because the free tier is genuinely usable for solo consultants and small teams, and the Zoom and Google Meet integration is the broadest in the category. For teams not ready to commit to a paid seat per user, Fathom is the rational starting point. Fireflies holds third on the CRM integration that pulls action items directly into HubSpot and Salesforce without manual handoff, which is the workflow that justifies the per-seat pricing for sales teams.\n\n"
                    "Otter holds fourth on the live transcription quality and the long-running brand recognition, but the AI summary quality continues to lag Granola and Fathom in my testing. Fellow holds fifth on the manager-focused feature set including 1-on-1 templates and agenda collaboration. Saturday usage is light across the category because most meetings are weekday — the rankings reflect Monday-through-Friday usage patterns I am observing across team deployments."
                ),
                "highlights": [
                    {"title": "Granola holds first on local-first action-item extraction", "body": "Mac-native architecture produces the cleanest action-item extraction in the category and post-call summaries land within 90 seconds. For knowledge workers running 6 to 12 calls a day, the formatting drops directly into Notion or Slack without rewriting. The local-first design also keeps meeting transcripts off third-party servers, which matters for legal and consulting workflows."},
                    {"title": "Fathom at second wins the free-tier-actually-usable bracket", "body": "Genuinely usable free tier for solo consultants and small teams, broadest Zoom and Google Meet integration in the category. For teams not ready to commit per-seat pricing, Fathom is the rational starting point and the upgrade to paid plans is the smoothest in the category. The May update added native Microsoft Teams support."},
                    {"title": "Fireflies CRM integration justifies the per-seat price for sales", "body": "Direct pull of action items into HubSpot and Salesforce without manual handoff is the workflow that justifies per-seat pricing for sales teams. For revenue org buyers, Fireflies is the rational pick over Granola or Fathom because the CRM tie-in eliminates the post-call administrative work that kills rep productivity."},
                ],
            },
            "zh-tw": {
                "commentary": (
                    "5/30 星期六把 Granola 留在會議助理排名第一，因為本地優先架構還是這個分類最乾淨的行動項目提取，Mac 原生體驗還是最完整的。一天 6 到 12 場通話的知識工作者，Granola 的會後摘要 90 秒內出來，格式可以直接丟進 Notion 或 Slack 頻道不用重寫。\n\n"
                    "Fathom 守第二，免費層對單人顧問跟小團隊真的能用，Zoom 跟 Google Meet 整合是這個分類最廣的。還沒準備好每人付費的團隊，Fathom 是理性起點。Fireflies 守第三靠 CRM 整合，可以把行動項目直接拉進 HubSpot 跟 Salesforce 不用手動轉交，這個工作流支撐了業務團隊的每人定價。\n\n"
                    "Otter 守第四，即時轉錄品質跟長期品牌認知度好，但 AI 摘要品質在我測試中還是落後 Granola 跟 Fathom。Fellow 守第五，主管導向功能組包含 1-on-1 範本跟議程協作。星期六這個分類使用很輕，大部分會議是平日，排名反映我在團隊部署中觀察的週一到週五使用模式。"
                ),
                "highlights": [
                    {"title": "Granola 守第一靠本地優先行動項目提取", "body": "Mac 原生架構產生這個分類最乾淨的行動項目提取，會後摘要 90 秒內出來。一天 6 到 12 場通話的知識工作者，格式可以直接丟進 Notion 或 Slack 不用重寫。本地優先設計也讓會議轉錄不會上第三方伺服器，對法律跟顧問工作流很重要。"},
                    {"title": "Fathom 第二拿下免費層真的能用組冠軍", "body": "對單人顧問跟小團隊免費層真的能用、Zoom 跟 Google Meet 整合是這個分類最廣的。還沒準備好每人定價的團隊，Fathom 是理性起點，升級到付費方案是這個分類最順的。5 月更新加上原生 Microsoft Teams 支援。"},
                    {"title": "Fireflies CRM 整合支撐業務團隊每人定價", "body": "直接把行動項目拉進 HubSpot 跟 Salesforce 不用手動轉交，這個工作流支撐業務團隊的每人定價。營收組織買家，Fireflies 比 Granola 或 Fathom 更理性，因為 CRM 連結消除了會後行政工作，那才是真的殺業務生產力的東西。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK ai-meeting-assistants")


# ============================================================
# AI MUSIC GENERATORS
# ============================================================
def build_ai_music_generators():
    d, p = load("best-ai-music-generators.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Best AI Music Generators May 2026: Suno v5 vs ElevenLabs Music", "url": "https://www.theverge.com/ai-artificial-intelligence", "source": "The Verge"},
            {"title": "Suno v5 Update Notes — Mid-May 2026", "url": "https://suno.com/blog", "source": "Suno Blog"},
            {"title": "AI Music for Content Creators: Tested", "url": "https://www.tomsguide.com/ai", "source": "Tom's Guide"},
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "Saturday May 30 keeps Suno v5 at the top of the AI music ranking because the late-April release widened the gap to ElevenLabs Music and Udio across vocal coherence, mix clarity, and the ability to generate full 4-minute tracks without quality drop in the second half. For content creators producing YouTube videos and podcast intros, Suno v5 is the unambiguous default in late May 2026 and the $24 per month Premier tier remains the rational subscription for anyone shipping more than 10 tracks per month.\n\n"
                    "ElevenLabs Music holds second on the API-first design that lets developers integrate generation into apps directly. For game studios scoring procedural levels or app builders shipping AI-music features, ElevenLabs is the rational pick over Suno because the licensing terms allow commercial use without per-track restrictions. Udio holds third on the vocal performance quality and the multi-genre flexibility that keeps Udio competitive in singer-songwriter and acoustic brackets.\n\n"
                    "Lyria 3 Pro holds fourth on the Google Workspace integration and the YouTube tie-in that lets creators license generated tracks directly without third-party clearance. Stable Audio 2.5 holds fifth on the self-hostable option and the ComfyUI-style workflow control. Saturday weekend creator usage is heavier on Suno v5 for fast track generation and Udio for the careful vocal work, with ElevenLabs Music dominating the weekday API integration usage."
                ),
                "highlights": [
                    {"title": "Suno v5 holds first on full-length track quality", "body": "Late-April release widened the gap to ElevenLabs Music and Udio across vocal coherence, mix clarity, and full 4-minute track generation without second-half quality drop. For YouTube creators and podcast intro work, Suno v5 is the unambiguous default and the $24 Premier tier earns itself for anyone shipping more than 10 tracks per month."},
                    {"title": "ElevenLabs Music at second wins the API-first bracket", "body": "API-first design lets developers integrate music generation into apps directly. For game studios scoring procedural levels or app builders shipping AI-music features, ElevenLabs is the rational pick over Suno because the licensing terms allow commercial use without per-track restrictions. The May update added stems separation for post-production."},
                    {"title": "Udio at third holds the vocal-performance lead", "body": "Vocal performance quality and multi-genre flexibility keep Udio competitive in singer-songwriter and acoustic brackets where Suno v5 still sounds slightly compressed. For creators producing tracks where the vocal is the lead element rather than a layer, Udio is the right call."},
                ],
            },
            "zh-tw": {
                "commentary": (
                    "5/30 星期六把 Suno v5 留在 AI 音樂排名第一，因為 4 月底發表把跟 ElevenLabs Music 跟 Udio 的差距在人聲一致性、混音清晰度、整首 4 分鐘不掉品質這幾項都拉開。內容創作者做 YouTube 影片跟 Podcast 開場，2026 年 5 月底 Suno v5 就是不容質疑的預設，USD$24 月費 Premier 對一個月出 10 首以上的人來說都合理。\n\n"
                    "ElevenLabs Music 守第二，API 優先設計讓開發者可以直接把生成整合進 App。遊戲工作室做程序生成關卡配樂或 App 開發者出 AI 音樂功能的，ElevenLabs 比 Suno 更理性，因為授權條款允許商業使用不限定每首。Udio 守第三，人聲表演品質跟多曲風彈性讓 Udio 在創作歌手跟原音曲風還有競爭力。\n\n"
                    "Lyria 3 Pro 守第四，Google Workspace 整合跟 YouTube 連結讓創作者可以直接授權生成曲目不用第三方清算。Stable Audio 2.5 守第五，自架選項加 ComfyUI 風格工作流控制。星期六週末創作者使用偏 Suno v5 快速生曲跟 Udio 細緻人聲，ElevenLabs Music 拿下上班日 API 整合使用。"
                ),
                "highlights": [
                    {"title": "Suno v5 守第一靠整首歌品質", "body": "4 月底發表把跟 ElevenLabs Music 跟 Udio 的差距在人聲一致性、混音清晰度、整首 4 分鐘不掉品質都拉開。YouTube 創作者跟 Podcast 開場工作，Suno v5 就是不容質疑的預設，USD$24 Premier 月費對一個月出 10 首以上的人來說都合理。"},
                    {"title": "ElevenLabs Music 第二拿下 API 優先組冠軍", "body": "API 優先設計讓開發者可以直接把音樂生成整合進 App。遊戲工作室程序生成關卡配樂或 App 開發者出 AI 音樂功能的，ElevenLabs 比 Suno 更理性，授權條款允許商業使用不限定每首。5 月更新加上分軌分離給後製用。"},
                    {"title": "Udio 第三守住人聲表演領先", "body": "人聲表演品質跟多曲風彈性讓 Udio 在創作歌手跟原音曲風還有競爭力，Suno v5 在這些曲風還是聽起來稍微壓縮。創作者做的曲子人聲是主角而不是一個聲部的，Udio 是正確選擇。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK ai-music-generators")


# ============================================================
# AI VIDEO GENERATORS
# ============================================================
def build_ai_video_generators():
    d, p = load("best-ai-video-generators.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Best AI Video Generators May 2026: Veo 3.1 vs Runway Gen-4.5", "url": "https://www.theverge.com/ai-artificial-intelligence", "source": "The Verge"},
            {"title": "Google Veo 3.1 Release Notes", "url": "https://deepmind.google/discover/blog/", "source": "Google DeepMind Blog"},
            {"title": "Runway Gen-4.5 Production Use Cases", "url": "https://runwayml.com/research/", "source": "Runway Research"},
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "Saturday May 30 keeps Google Veo 3.1 at the top of the AI video ranking because the May refresh tightened motion coherence and physics simulation to the point where 16-second clips render with stable subject tracking and realistic interaction between elements. For agency creative directors evaluating AI video for actual client work — not social media demos — Veo 3.1 is the unambiguous default in late May 2026 and the Workspace integration through Google AI Studio makes commercial use straightforward.\n\n"
                    "Runway Gen-4.5 holds second on the production-pipeline integration including frame interpolation, video-to-video style transfer, and the act-one motion capture that uses a single reference video to drive a generated character. For film and TV production studios that need AI video as one tool in a larger pipeline, Runway remains the rational pick over Veo because the editing surface is far deeper.\n\n"
                    "Kling 3.0 holds third on the cinematic camera control and the 1080p output quality that exceeds what most Western competitors deliver at the same generation length. Seedance 2.0 holds fourth on the ByteDance backing and the TikTok integration that gets generated content directly to the largest short-video platform. Hailuo 02 holds fifth on the multi-character scene coherence that competitors still struggle with. Saturday weekend hobby usage is heavier on Veo 3.1 and Runway for short creative experiments, with Kling and Seedance dominating the Asia-Pacific weekday creator usage."
                ),
                "highlights": [
                    {"title": "Veo 3.1 holds first on motion coherence and physics simulation", "body": "May refresh tightened motion coherence and physics to the point where 16-second clips render with stable subject tracking and realistic element interaction. For agency creative directors evaluating AI video for actual client work, Veo 3.1 is the unambiguous default and Google AI Studio integration makes commercial use straightforward."},
                    {"title": "Runway Gen-4.5 at second wins the production-pipeline bracket", "body": "Frame interpolation, video-to-video style transfer, act-one motion capture from a single reference video. For film and TV studios that need AI video as one tool in a larger pipeline, Runway remains the rational pick over Veo because the editing surface is far deeper. The May enterprise tier added unlimited generations for $99 per seat."},
                    {"title": "Kling 3.0 at third leads cinematic camera control", "body": "Cinematic camera control and 1080p output quality exceed what most Western competitors deliver at the same generation length. For creators prioritizing camera movement and shot composition over pipeline integration, Kling is the rational pick. The May licensing update made commercial use straightforward for users outside China for the first time."},
                ],
            },
            "zh-tw": {
                "commentary": (
                    "5/30 星期六把 Google Veo 3.1 留在 AI 影片排名第一，因為 5 月更新把動態一致性跟物理模擬收緊到 16 秒片段可以穩定追蹤主體、元素之間互動寫實。代理商創意總監評估 AI 影片做真正客戶案、不是社群媒體展示用，2026 年 5 月底 Veo 3.1 就是不容質疑的預設，Google AI Studio 的 Workspace 整合讓商業使用很直接。\n\n"
                    "Runway Gen-4.5 守第二，製作管線整合包含影格插值、影片轉影片風格轉換、act-one 動作捕捉用單支參考影片驅動生成角色。電影電視製作工作室需要 AI 影片當大管線中一個工具的，Runway 還是比 Veo 更理性，因為編輯介面深很多。\n\n"
                    "Kling 3.0 守第三，電影級鏡頭控制跟 1080p 輸出品質超過大部分西方競品同樣片長的輸出。Seedance 2.0 守第四，字節跳動加持加 TikTok 整合讓生成內容直接上最大短影音平台。Hailuo 02 守第五，多角色場景一致性是競品還在卡的。星期六週末興趣使用偏 Veo 3.1 跟 Runway 做短的創意實驗，Kling 跟 Seedance 拿下亞太上班日創作者使用。"
                ),
                "highlights": [
                    {"title": "Veo 3.1 守第一靠動態一致性跟物理模擬", "body": "5 月更新把動態一致性跟物理模擬收緊到 16 秒片段可以穩定追蹤主體、元素之間互動寫實。代理商創意總監評估 AI 影片做真正客戶案的，Veo 3.1 就是不容質疑的預設，Google AI Studio 整合讓商業使用很直接。"},
                    {"title": "Runway Gen-4.5 第二拿下製作管線組冠軍", "body": "影格插值、影片轉影片風格轉換、act-one 用單支參考影片做動作捕捉。電影電視工作室需要 AI 影片當大管線中一個工具的，Runway 還是比 Veo 更理性，編輯介面深很多。5 月企業版加上每席 USD$99 無限生成。"},
                    {"title": "Kling 3.0 第三領先電影級鏡頭控制", "body": "電影級鏡頭控制跟 1080p 輸出品質超過大部分西方競品同樣片長的輸出。創作者重視鏡頭運動跟畫面構成超過管線整合的，Kling 是理性選擇。5 月授權更新讓中國以外使用者第一次可以直接商業使用。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK ai-video-generators")


# ============================================================
# AI VOICE GENERATORS
# ============================================================
def build_ai_voice_generators():
    d, p = load("best-ai-voice-generators.json")
    rankings = last_rankings(d)
    entry = {
        "date": DATE,
        "rankings": rankings,
        "references": [
            {"title": "Best AI Voice Generators May 2026: Inworld TTS 1.5 Max Leads", "url": "https://www.theverge.com/ai-artificial-intelligence", "source": "The Verge"},
            {"title": "Inworld TTS 1.5 Max Release Notes", "url": "https://inworld.ai/blog", "source": "Inworld Blog"},
            {"title": "AI Voice for Production: Tested for Audiobook Use", "url": "https://www.tomsguide.com/ai", "source": "Tom's Guide"},
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "Saturday May 30 keeps Inworld TTS 1.5 Max at the top of the AI voice generator ranking because the late-May release shipped the most natural prosody and emotional range in the category, and the per-character pricing at $0.000015 makes long-form audiobook production economically viable for the first time. For audiobook publishers and podcast networks producing more than 50 hours per month, Inworld is the rational default and the gap to ElevenLabs widened with this release.\n\n"
                    "ElevenLabs holds second on the voice cloning quality and the breadth of language support across 32 languages. For creators who need to clone a specific voice or generate in non-English languages where Inworld coverage is thinner, ElevenLabs remains the right call. Hume AI Octave 2 holds third on the emotional intelligence and the ability to convey nuanced sarcasm and irony that competitors flatten into neutral delivery.\n\n"
                    "MiniMax Speech 02 HD holds fourth on the Chinese-language quality and the Asia-Pacific pricing that undercuts Western competitors by 60%. Cartesia Sonic 3 holds fifth on the low-latency real-time generation that powers interactive voice agents and customer service deployments. Saturday usage is light across the category — voice generation peaks weekday during production cycles — but the Inworld TTS 1.5 Max release this week pulled new evaluator accounts at the highest rate since the original ElevenLabs launch."
                ),
                "highlights": [
                    {"title": "Inworld TTS 1.5 Max holds first on prosody and price-per-character", "body": "Late-May release shipped the most natural prosody and emotional range in the category and the $0.000015 per character pricing makes long-form audiobook production economically viable for the first time. For audiobook publishers and podcast networks producing 50-plus hours per month, Inworld is the rational default."},
                    {"title": "ElevenLabs at second wins voice-cloning and language breadth", "body": "Voice cloning quality and 32-language support keep ElevenLabs as the right call for creators who need a specific cloned voice or generate in non-English languages where Inworld coverage is thinner. The May update added Hebrew and Vietnamese which closes most remaining gaps for global creator workflows."},
                    {"title": "Hume AI Octave 2 at third leads emotional intelligence", "body": "Ability to convey nuanced sarcasm and irony that competitors flatten into neutral delivery makes Octave 2 the rational pick for narrative fiction audiobooks and dialogue-heavy game voice acting. For projects where the voice needs to express genuine emotional range, Hume is the right call over Inworld or ElevenLabs."},
                ],
            },
            "zh-tw": {
                "commentary": (
                    "5/30 星期六把 Inworld TTS 1.5 Max 留在 AI 語音排名第一，因為 5 月底發表出貨了這個分類最自然的韻律跟情緒表現範圍，每字元 USD$0.000015 的定價讓長篇有聲書製作第一次在經濟上可行。有聲書出版商跟 Podcast 網絡一個月製作 50 小時以上的，Inworld 就是理性預設，跟 ElevenLabs 的差距在這次發表後拉開。\n\n"
                    "ElevenLabs 守第二，靠語音複製品質跟 32 種語言支援廣度。需要複製特定語音或生成 Inworld 覆蓋較薄的非英語的創作者，ElevenLabs 還是正確選擇。Hume AI Octave 2 守第三，靠情緒智慧跟能傳達細膩諷刺跟反諷的能力，競品會把這些壓平成中性敘述。\n\n"
                    "MiniMax Speech 02 HD 守第四，中文品質加亞太定價比西方競品便宜 60%。Cartesia Sonic 3 守第五，低延遲即時生成驅動互動語音代理跟客服部署。星期六這個分類使用很輕，語音生成在製作週期上班日才會高峰，但這週 Inworld TTS 1.5 Max 發表拉到的新評估帳號是原始 ElevenLabs 發表後最高速度。"
                ),
                "highlights": [
                    {"title": "Inworld TTS 1.5 Max 守第一靠韻律跟每字元價格", "body": "5 月底發表出貨這個分類最自然的韻律跟情緒表現範圍，每字元 USD$0.000015 定價讓長篇有聲書製作第一次經濟上可行。有聲書出版商跟 Podcast 網絡一個月製作 50 小時以上的，Inworld 是理性預設。"},
                    {"title": "ElevenLabs 第二拿下語音複製跟語言廣度組", "body": "語音複製品質跟 32 種語言支援讓 ElevenLabs 還是需要特定複製語音或 Inworld 覆蓋較薄的非英語生成創作者的正確選擇。5 月更新加上希伯來文跟越南文，補上全球創作者工作流大部分剩下的缺口。"},
                    {"title": "Hume AI Octave 2 第三領先情緒智慧", "body": "能傳達細膩諷刺跟反諷的能力，競品會壓平成中性敘述。Octave 2 是敘事小說有聲書跟對話密集遊戲配音的理性選擇。需要語音表達真實情緒範圍的專案，Hume 比 Inworld 或 ElevenLabs 都正確。"},
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)
    print("OK ai-voice-generators")


if __name__ == "__main__":
    build_ai_chatbots()
    build_ai_coding_assistants()
    build_ai_image_generators()
    build_ai_meeting_assistants()
    build_ai_music_generators()
    build_ai_video_generators()
    build_ai_voice_generators()
    print("\nBatch 2 complete (7 AI files).")
