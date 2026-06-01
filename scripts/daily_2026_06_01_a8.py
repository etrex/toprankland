import json
from pathlib import Path

DATE = "2026-06-01"
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


# ---------------------------------------------------------------------------
# 1. AI MUSIC GENERATORS
# ---------------------------------------------------------------------------
def ai_music():
    d, p = load("best-ai-music-generators.json")
    entry = {
        "date": DATE,
        "rankings": last_rankings(d),
        "references": [
            {
                "title": "ElevenLabs, Stability AI Drop New AI Music Models, Can They Catch Suno?",
                "url": "https://decrypt.co/369237/elevenlabs-stability-ai-new-music-models-suno",
                "source": "Decrypt",
            },
            {
                "title": "ElevenLabs Music v2: AI Music Generator Now Switches Genres Mid-Track",
                "url": "https://memeburn.com/elevenlabs-music-v2-ai-music-generator-now-switches-genres-mid-track/",
                "source": "Memeburn",
            },
            {
                "title": "Suno vs Udio vs ElevenLabs Music: The 2026 AI Music Generator Showdown",
                "url": "https://www.aimagicx.com/blog/suno-vs-udio-vs-elevenlabs-music-comparison-2026",
                "source": "AI Magicx",
            },
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "Suno stays at the top of my list this week, and the reason is simple. With a $300M ARR and "
                    "around 2 million paying subscribers, it has the deepest genre coverage and the most mature "
                    "editing ecosystem of anything I test. I will note the v5.5 update from late March drew real "
                    "complaints about high frequency hiss and quality drift past the first minute of a track, so I "
                    "am watching that closely, but for full songs with believable structure it remains my default. "
                    "ElevenLabs Music keeps climbing because v2 now switches genres mid-track and regenerates a "
                    "single section without touching the rest, which is exactly the kind of surgical control I want "
                    "when a chorus lands but the bridge does not. The company also cut API pricing by up to 50 "
                    "percent and self-serve by up to 40 percent, so the value math improved overnight. That price "
                    "move alone makes it the smart pick for anyone shipping commercial work, since its licensing "
                    "story is the cleanest in the field. Udio holds third on pure audio craft. The Universal Music "
                    "settlement points to a jointly licensed platform arriving this year, which is promising, but "
                    "downloads stay disabled across every tier right now, and that export gap keeps it out of "
                    "production pipelines for me. Lyria 3 Pro from Google and Stable Audio 3.0 round out the "
                    "serious tier, with Stable Audio now offering open weights and tracks that run past six "
                    "minutes. My advice this week: pick Suno for breadth, ElevenLabs for licensed commercial "
                    "delivery, and keep Udio on a watch list until exports come back."
                ),
                "highlights": [
                    {
                        "title": "ElevenLabs Music v2 adds mid-track genre switching",
                        "body": "Version 2 transitions genres within one track and regenerates a chosen section without altering the rest, giving me precise control over a weak bridge or chorus.",
                    },
                    {
                        "title": "ElevenLabs cut prices sharply",
                        "body": "API pricing dropped up to 50 percent and self-serve up to 40 percent, which materially improves its value for anyone shipping commercial tracks.",
                    },
                    {
                        "title": "Suno still leads on breadth and ecosystem",
                        "body": "With roughly 2 million paid subscribers and $300M ARR, Suno offers the widest genre range and the most mature editing tools I use day to day.",
                    },
                    {
                        "title": "Udio export gap persists",
                        "body": "Downloads remain disabled across all tiers following the Universal Music settlement, so I keep it ranked third despite excellent raw audio quality.",
                    },
                    {
                        "title": "Stable Audio 3.0 brings open weights",
                        "body": "Stability AI's new four-model family ships open weights and supports tracks past six minutes, a real draw for builders who want local control.",
                    },
                ],
            },
            "zh-tw": {
                "commentary": (
                    "這禮拜我還是把 Suno 放在第一，理由很單純。它的年營收衝到 3 億美金，付費用戶大概 200 萬，曲風"
                    "覆蓋度跟編輯生態系是我測過最完整的，整首歌的結構聽起來最像真的有人在編曲。老實說三月底那版 "
                    "v5.5 我有點皺眉，不少人反映高頻會有嘶嘶聲，過了第一分鐘音質會飄掉，這點我會持續盯。但要做完整"
                    "歌曲，它目前還是我的首選。ElevenLabs Music 這次往上爬，因為 v2 可以在同一首裡面換曲風，還能"
                    "只重生成某一段而不動到其他部分，這種開刀式的控制超實用，副歌很讚但過門卡卡的時候，動一段就好。"
                    "而且它這波 API 直接砍價最多 50%，自助訂閱也降最多 40%，CP 值一夜之間翻盤。光是這個降價，加上"
                    "它授權最乾淨，要接商案出片我會直接推它。Udio 排第三靠的是純音質，環球音樂和解後說今年會推共同"
                    "授權平台，聽起來不錯，但現在所有方案都還不能下載匯出，這個洞讓我沒辦法把它放進實際工作流。"
                    "Google 的 Lyria 3 Pro 跟 Stable Audio 3.0 也都站穩前段班，Stable Audio 現在開放權重，曲長"
                    "還能破六分鐘。這週我的建議很實在：要曲風廣選 Suno，要授權出商案選 ElevenLabs，Udio 先放觀察"
                    "名單，等它把匯出補回來再說。"
                ),
                "highlights": [
                    {
                        "title": "ElevenLabs Music v2 能在曲中換曲風",
                        "body": "v2 可以在同一首歌裡切換曲風，還能只重生成指定段落而不動其他部分，過門或副歌卡住時動一段就解決。",
                    },
                    {
                        "title": "ElevenLabs 大幅降價",
                        "body": "API 最多砍 50%，自助訂閱最多降 40%，對要出商業作品的人來說 CP 值直接拉高一大截。",
                    },
                    {
                        "title": "Suno 廣度與生態系仍最強",
                        "body": "付費用戶約 200 萬、年營收 3 億美金，曲風最廣、編輯工具最成熟，是我每天在用的主力。",
                    },
                    {
                        "title": "Udio 還是不能匯出",
                        "body": "環球音樂和解後各方案都還不能下載，所以即使原始音質很頂，我這週還是把它排第三。",
                    },
                    {
                        "title": "Stable Audio 3.0 開放權重",
                        "body": "Stability AI 推出四模型家族並開放權重，曲長可破六分鐘，想在本地端自己掌控的人會很心動。",
                    },
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)


# ---------------------------------------------------------------------------
# 2. DISHWASHERS
# ---------------------------------------------------------------------------
def dishwashers():
    d, p = load("best-dishwashers.json")
    entry = {
        "date": DATE,
        "rankings": last_rankings(d),
        "references": [
            {
                "title": "Best (and Worst) Dishwashers of 2026, Lab-Tested and Reviewed",
                "url": "https://www.consumerreports.org/appliances/dishwashers/best-dishwashers-of-the-year-a6109623431/",
                "source": "Consumer Reports",
            },
            {
                "title": "Not LG, Not GE: This Brand Tops Consumer Reports' Best Dishwashers Of 2026 List",
                "url": "https://www.slashgear.com/2138296/best-dishwasher-brand-2026-consumer-reports-bosch/",
                "source": "SlashGear",
            },
            {
                "title": "Bosch vs. Miele Dishwashers (2026): Reliability, Wash vs. Dry, and Price-Band Matchups",
                "url": "https://blog.yaleappliance.com/bosch-vs-miele-dishwashers",
                "source": "Yale Appliance",
            },
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "Consumer Reports just published its 2026 dishwasher tests, and Bosch swept the top three spots, "
                    "which lines up exactly with how I have my list ordered. The Bosch Benchmark SHP9PCM5N holds my "
                    "number one because it washes and dries exceptionally while staying whisper quiet, and Bosch's "
                    "18 sound-reducing technologies push some models down to 38 dBA, the quietest you can buy in the "
                    "US. CrystalDry with zeolite is the other reason it stays on top, since it gets dishes up to 60 "
                    "percent drier and finally solves the plastic-tub drying problem that haunts most machines. Miele "
                    "stays at number two, and the new reliability data backs that placement. The 2026 survey of more "
                    "than 77,000 buyers shows Miele needing service on just 5.6 percent of units in the first year, "
                    "about 2.2 points better than Bosch, and Miele builds these to last up to 20 years against "
                    "Bosch's 10-year design target. If you plan to keep a dishwasher for two decades, Miele is the "
                    "buy. Its AutoDos system also doses detergent earlier in the cycle for stronger cleaning from "
                    "the start. The interesting wrinkle this year is that one publication named the Miele G 5008 SCU "
                    "Active its overall winner for performance, quietness, and ease of use, so the gap at the very "
                    "top is small. Down the list, the Bosch 300 Series remains my value champion. It delivers the "
                    "brand's quiet operation and strong reliability at a price most kitchens can justify."
                ),
                "highlights": [
                    {
                        "title": "Bosch sweeps Consumer Reports' 2026 top three",
                        "body": "CR's lab tests put Bosch in the first three positions, with the Benchmark SHP9PCM5N leading for washing, drying, and quietness.",
                    },
                    {
                        "title": "Bosch is the quietest brand in the US",
                        "body": "Eighteen sound-reducing technologies bring some Bosch models to 38 dBA, which is why the Benchmark holds my top spot for open-plan kitchens.",
                    },
                    {
                        "title": "Miele leads first-year reliability",
                        "body": "A 2026 survey of 77,000-plus buyers shows Miele at just 5.6 percent service, about 2.2 points ahead of Bosch, and built to last up to 20 years.",
                    },
                    {
                        "title": "CrystalDry solves plastic drying",
                        "body": "Bosch's zeolite-based CrystalDry gets dishes up to 60 percent drier, the clearest advantage at the premium end.",
                    },
                    {
                        "title": "Bosch 300 Series is the value pick",
                        "body": "It carries the brand's quiet operation and strong reliability at a price most kitchens can comfortably justify.",
                    },
                ],
            },
            "zh-tw": {
                "commentary": (
                    "美國消費者報告 (Consumer Reports) 剛公布 2026 洗碗機測試，Bosch 直接包辦前三名，這跟我這份榜單"
                    "的排序完全吻合。我把 Bosch Benchmark SHP9PCM5N 放第一，因為它洗淨跟烘乾都頂尖，運轉又安靜到"
                    "靠北，Bosch 用了 18 項降噪技術，有些機型壓到 38 分貝，全美最安靜。它還有 CrystalDry 沸石烘乾，"
                    "把餐具烘到多乾 60%，終於把塑膠內桶烘不乾這個老問題解決掉。台灣很多人住開放式廚房，這台半夜跑"
                    "也不吵。Miele 穩穩排第二，新的妥善率數據也撐得住。2026 那份七萬七千多人的調查顯示，Miele 第一"
                    "年只有 5.6% 要叫修，比 Bosch 好約 2.2 個百分點，而且 Miele 是照用 20 年的標準在做，Bosch 設計"
                    "目標是 10 年。講白了，你打算一台用 20 年，就買 Miele。它的 AutoDos 自動投劑在循環一開始就放"
                    "洗劑，洗淨力起步就很猛。今年比較有趣的是，有家媒體把 Miele G 5008 SCU Active 選為綜合冠軍，"
                    "所以最頂端那個差距其實很小。榜單往下看，Bosch 300 系列還是我的 CP 值之王，一樣安靜、一樣耐用，"
                    "價格卻是多數家庭咬牙就買得下去的等級。"
                ),
                "highlights": [
                    {
                        "title": "Bosch 包辦消費者報告前三名",
                        "body": "CR 實驗室測試把 Bosch 排進前三，Benchmark SHP9PCM5N 在洗淨、烘乾、安靜度都領先。",
                    },
                    {
                        "title": "Bosch 是全美最安靜品牌",
                        "body": "18 項降噪技術讓部分機型壓到 38 分貝，所以開放式廚房我首推這台 Benchmark。",
                    },
                    {
                        "title": "Miele 第一年妥善率最高",
                        "body": "2026 七萬七千人調查顯示 Miele 只有 5.6% 叫修，比 Bosch 好約 2.2 個百分點，且照 20 年標準製造。",
                    },
                    {
                        "title": "CrystalDry 解決塑膠烘不乾",
                        "body": "Bosch 的沸石 CrystalDry 把餐具多烘乾 60%，是高階機種最明顯的優勢。",
                    },
                    {
                        "title": "Bosch 300 系列是 CP 值首選",
                        "body": "一樣有品牌的安靜與耐用，價格卻是多數家庭買得下手的等級。",
                    },
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)


# ---------------------------------------------------------------------------
# 3. GAMING MONITORS
# ---------------------------------------------------------------------------
def gaming_monitors():
    d, p = load("best-gaming-monitors.json")
    entry = {
        "date": DATE,
        "rankings": last_rankings(d),
        "references": [
            {
                "title": "The Best OLED Gaming Monitors to Buy in 2026",
                "url": "https://tftcentral.co.uk/recommendations/the-best-oled-gaming-monitors-to-buy-in-2026",
                "source": "TFTCentral",
            },
            {
                "title": "The 5 Best OLED Monitors of 2026",
                "url": "https://www.rtings.com/monitor/reviews/best/oled",
                "source": "RTINGS",
            },
            {
                "title": "Best OLED Gaming Monitors 2026",
                "url": "https://www.tomshardware.com/monitors/gaming-monitors/best-oled-gaming-monitors",
                "source": "Tom's Hardware",
            },
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "The 4K 240Hz OLED tier is where the action is in 2026, and my number one stays the ASUS ROG "
                    "Swift OLED PG27UCDM. That 27-inch QD-OLED panel pairs 4K with 240Hz, and the combination of "
                    "pixel density and motion clarity is still the best all-around image I put my eyes on. ASUS is "
                    "pushing the line forward, with the new PG32UCDM Gen 3 moving to a fourth-gen Samsung Tandem "
                    "QD-OLED and a matte coating, so the 32-inch route is getting stronger, but for a desk monitor "
                    "the 27-inch density wins for me. LG's UltraGear 27GX790B holds second on the strength of its "
                    "true 480Hz dual-mode panel, which is the refresh-rate champion of this list and the right call "
                    "for competitive shooters where every frame counts. The fresh news worth flagging is LG's "
                    "32GX870B, a 32-inch 4K 240Hz Tandem W-OLED rated up to 1500 nits peak, which is a serious HDR "
                    "number for an OLED and a sign of where brightness is heading. MSI's MPG 272URX and the 26.5-inch "
                    "MPG 341CQR keep the QD-OLED value conversation honest. If you want the widest immersion, the "
                    "new LG 45GX950A goes 45 inches at 5K2K, though that is a different use case than a focused "
                    "gaming desk. My guidance: take the PG27UCDM for the best balance, the LG 27GX790B if raw speed "
                    "is your priority, and watch the 1500-nit panels arriving this year."
                ),
                "highlights": [
                    {
                        "title": "PG27UCDM holds the all-around crown",
                        "body": "Its 27-inch 4K QD-OLED at 240Hz still gives me the best blend of pixel density and motion clarity on a desk.",
                    },
                    {
                        "title": "LG 27GX790B is the speed king",
                        "body": "The dual-mode panel hits a true 480Hz, making it my pick for competitive shooters where frame timing decides fights.",
                    },
                    {
                        "title": "LG 32GX870B pushes 1500 nits",
                        "body": "A new 32-inch 4K 240Hz Tandem W-OLED rated up to 1500 nits peak shows OLED brightness is finally climbing into serious HDR territory.",
                    },
                    {
                        "title": "ASUS PG32UCDM Gen 3 upgrades the panel",
                        "body": "The Gen 3 moves to a fourth-gen Samsung Tandem QD-OLED with a matte coating, strengthening the 32-inch 4K option.",
                    },
                    {
                        "title": "MSI keeps QD-OLED value honest",
                        "body": "The MPG 272URX and 26.5-inch MPG 341CQR deliver the same class of QD-OLED panel at prices that pressure the premium tier.",
                    },
                ],
            },
            "zh-tw": {
                "commentary": (
                    "2026 最精彩的戰場就是 4K 240Hz OLED 這一級，我第一名還是放 ASUS ROG Swift OLED PG27UCDM。"
                    "那塊 27 吋 QD-OLED 把 4K 配上 240Hz，像素密度加上動態清晰度，整體畫面到現在還是我看過最均衡"
                    "的。ASUS 也一直在往前推，新的 PG32UCDM Gen 3 換上第四代 Samsung Tandem QD-OLED 加霧面塗層，"
                    "32 吋這條路線越來越強，但桌上型監視器我還是吃 27 吋的密度。LG UltraGear 27GX790B 排第二，靠"
                    "的是真 480Hz 雙模面板，這是榜上更新率之王，玩競技射擊每一格都算數，選它就對了。這次值得提的"
                    "新消息是 LG 32GX870B，32 吋 4K 240Hz Tandem W-OLED，峰值亮度標到 1500 nits，對 OLED 來說這"
                    "個 HDR 數字很猛，也看得出亮度的走向。MSI 的 MPG 272URX 跟 26.5 吋 MPG 341CQR 則讓 QD-OLED 的"
                    "CP 值話題一直很實在。想要最沉浸的包覆感，新的 LG 45GX950A 直接上 45 吋 5K2K，不過那跟專心打"
                    "電動的桌面是兩種用法。我的建議：要最均衡選 PG27UCDM，純拚速度選 LG 27GX790B，今年的 1500 "
                    "nits 面板也值得盯著看。"
                ),
                "highlights": [
                    {
                        "title": "PG27UCDM 仍是全能王",
                        "body": "27 吋 4K QD-OLED 配 240Hz，像素密度跟動態清晰度的平衡在桌面上還是我心中第一。",
                    },
                    {
                        "title": "LG 27GX790B 是速度王",
                        "body": "雙模面板可達真 480Hz，玩競技射擊靠幀時間決勝負時，我首推這台。",
                    },
                    {
                        "title": "LG 32GX870B 衝上 1500 nits",
                        "body": "新的 32 吋 4K 240Hz Tandem W-OLED 峰值標到 1500 nits，代表 OLED 亮度終於踏進像樣的 HDR 領域。",
                    },
                    {
                        "title": "ASUS PG32UCDM Gen 3 升級面板",
                        "body": "Gen 3 換上第四代 Samsung Tandem QD-OLED 加霧面塗層，把 32 吋 4K 選項補得更強。",
                    },
                    {
                        "title": "MSI 維持 QD-OLED 的 CP 值",
                        "body": "MPG 272URX 跟 26.5 吋 MPG 341CQR 用同級 QD-OLED 面板，價格直接給高階機種壓力。",
                    },
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)


# ---------------------------------------------------------------------------
# 4. NOISE CANCELLING HEADPHONES
# ---------------------------------------------------------------------------
def headphones():
    d, p = load("best-noise-cancelling-headphones.json")
    entry = {
        "date": DATE,
        "rankings": last_rankings(d),
        "references": [
            {
                "title": "Sony WH-1000XM6 vs. Bose QuietComfort Ultra 2 Headphones: Review",
                "url": "https://www.rollingstone.com/product-recommendations/tech/sony-wh-1000xm6-vs-bose-quietcomfort-ultra-2-headphones-1235542693/",
                "source": "Rolling Stone",
            },
            {
                "title": "Sony WH-1000XM6 vs Bose QuietComfort Ultra Headphones (2nd Gen): which flagship is best?",
                "url": "https://www.whathifi.com/headphones/wireless-headphones/sony-wh-1000xm6-vs-bose-quietcomfort-ultra-headphones-2nd-gen-which-flagship-wireless-over-ears-are-best",
                "source": "What Hi-Fi?",
            },
            {
                "title": "I tested the AirPods Max 2, Sony WH-1000XM6, and Bose QuietComfort Ultra",
                "url": "https://www.tomsguide.com/audio/headphones/i-tested-the-airpods-max-2-sony-wh-1000xm6-and-bose-quietcomfort-ultra-heres-the-only-pair-id-keep",
                "source": "Tom's Guide",
            },
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "The Sony WH-1000XM6 keeps my number one spot, and the latest head-to-heads against the Bose "
                    "QuietComfort Ultra 2nd Gen reinforce why. Sony brought back folding hinges with a stainless "
                    "steel mechanism so the XM6 collapses into a ball for travel, and the call quality is the "
                    "standout, with beamforming AI and precise voice pickup that genuinely cuts background noise on "
                    "calls. At $449 it sits at the top of the price ladder, but the all-round package of sound, "
                    "cancellation, and software still leads my testing. Bose holds a close second, and I want to be "
                    "fair about where it actually wins. The QC Ultra 2nd Gen has the more amply padded earcups and "
                    "headband, so it fatigues more slowly on long-haul flights, and that extra cushioning also gives "
                    "it a slight edge in passive isolation. There is also a smart new auto-sleep feature that drops "
                    "the headphones into low-power mode the moment you take them off, no case required. If comfort "
                    "over six hours is your priority, Bose is the call. The interesting context this week is the "
                    "three-way with the AirPods Max 2, where reviewers tested all three and most still walked away "
                    "with one of the Sony or Bose pairs. Down the list, Sennheiser's Momentum 4 remains my value-"
                    "for-sound favorite with its 60-hour battery, and the Soundcore Space models stay the budget "
                    "champions for anyone who wants strong ANC without the flagship price."
                ),
                "highlights": [
                    {
                        "title": "Sony XM6 leads on calls and portability",
                        "body": "Returning stainless steel hinges fold it into a ball, and beamforming AI gives it the standout call quality in this group.",
                    },
                    {
                        "title": "Bose wins long-session comfort",
                        "body": "The QC Ultra 2nd Gen has more amply padded earcups and headband, so it fatigues more slowly on long flights and isolates slightly better passively.",
                    },
                    {
                        "title": "Bose adds caseless auto-sleep",
                        "body": "A new auto-sleep feature drops the headphones into low-power mode the moment you remove them, no case needed.",
                    },
                    {
                        "title": "Sennheiser Momentum 4 is the sound-value pick",
                        "body": "A 60-hour battery and rich tuning keep it my favorite for listeners who prioritize audio quality per dollar.",
                    },
                    {
                        "title": "Soundcore Space holds the budget crown",
                        "body": "Strong ANC and very long battery at a fraction of the flagship price keep the Space models the value champions.",
                    },
                ],
            },
            "zh-tw": {
                "commentary": (
                    "Sony WH-1000XM6 這週還是穩坐我的第一，最近跟 Bose QuietComfort Ultra 二代的對打，更讓我確定這"
                    "個排序。Sony 把折疊轉軸找回來了，用不鏽鋼機構，XM6 可以收成一顆球好攜帶，而通話品質是它最亮"
                    "的一點，靠波束成形 AI 跟精準收音，講電話時背景雜音壓得很乾淨。售價 449 美金確實站在價格頂端，"
                    "但音質、降噪、軟體整套加起來，它在我手上還是領先。Bose 緊咬第二，我也要公道講它強在哪。QC "
                    "Ultra 二代的耳罩跟頭帶填充更厚，長程飛機戴久比較不會悶痛，這層額外的軟墊也讓它在被動隔音上"
                    "小贏一點。它還多了一個聰明的自動休眠，一摘下來就進低功耗，不用收進盒子。你最在意的是連續戴六"
                    "小時的舒適度，那就選 Bose。這週有趣的背景是它跟 AirPods Max 2 的三方混戰，評測同時測了三支，"
                    "多數人最後還是帶走 Sony 或 Bose 其中一支。榜單往下，Sennheiser Momentum 4 靠 60 小時續航，"
                    "還是我心中音質 CP 值首選，Soundcore Space 系列則穩坐預算之王，想要強降噪又不想花旗艦價的人"
                    "選它準沒錯。"
                ),
                "highlights": [
                    {
                        "title": "Sony XM6 通話與攜帶最強",
                        "body": "不鏽鋼折疊轉軸回歸可收成一顆球，波束成形 AI 讓它在這組裡通話品質最突出。",
                    },
                    {
                        "title": "Bose 長時間配戴最舒服",
                        "body": "QC Ultra 二代耳罩與頭帶填充更厚，長程飛機戴久比較不悶，被動隔音也小贏一截。",
                    },
                    {
                        "title": "Bose 新增免盒自動休眠",
                        "body": "新的自動休眠功能一摘下就進低功耗模式，不必放回收納盒。",
                    },
                    {
                        "title": "Sennheiser Momentum 4 是音質 CP 值首選",
                        "body": "60 小時續航加上飽滿調音，是我推給重視每塊錢音質的人的選擇。",
                    },
                    {
                        "title": "Soundcore Space 穩坐預算王",
                        "body": "強降噪加超長續航，價格只要旗艦的一部分，Space 系列依然是 CP 值冠軍。",
                    },
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)


# ---------------------------------------------------------------------------
# 5. RICE COOKERS
# ---------------------------------------------------------------------------
def rice_cookers():
    d, p = load("best-rice-cookers.json")
    entry = {
        "date": DATE,
        "rankings": last_rankings(d),
        "references": [
            {
                "title": "Best rice cookers in 2026, tested by our editors",
                "url": "https://www.cnn.com/cnn-underscored/reviews/best-rice-cooker",
                "source": "CNN Underscored",
            },
            {
                "title": "Zojirushi vs Tiger: Which Rice Cooker Is the Best?",
                "url": "https://prudentreviews.com/zojirushi-vs-tiger/",
                "source": "Prudent Reviews",
            },
            {
                "title": "12 Best Rice Cookers: Our guide to perfect rice of 2026",
                "url": "https://www.reviewed.com/cooking/best-right-now/the-best-rice-cookers",
                "source": "Reviewed",
            },
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "My top two stay locked this week, but the case for them keeps getting clearer. The Zojirushi "
                    "NP-HCC10 holds number one because its induction heating delivers fluffy, consistent results "
                    "across sushi rice, brown rice, and basmati every single time, which is exactly what the 2026 "
                    "round of testing keeps confirming. It is the cooker I trust to never surprise me on a weeknight. "
                    "That said, the Tiger JKT-D10U has a genuine argument for the crown, and I want to be specific "
                    "about why it sits so close at number two. In side-by-side testing it matches Zojirushi on "
                    "overall rice quality, then pulls ahead on brown rice with lighter, fluffier grains, and it is "
                    "meaningfully faster: roughly 44 minutes for white rice against 53, and 63 minutes for brown "
                    "against 103. If you cook a lot of brown rice or you simply hate waiting, the Tiger is the "
                    "smarter buy. The Cuckoo CRP-ST0609F stays at four for its flexibility, letting you customize "
                    "settings down to the keep-warm temperature on some models, and it steams white and brown rice "
                    "quickly. Its grains do run stickier, so it is a texture preference call. For most kitchens I "
                    "still send people to the Zojirushi NS-ZCC10 at number three. It cooks excellent rice, costs "
                    "less than the induction flagships, and is the easiest entry into proper micom cooking."
                ),
                "highlights": [
                    {
                        "title": "Zojirushi NP-HCC10 stays the safe number one",
                        "body": "Induction heating delivers fluffy, consistent rice across sushi, brown, and basmati every time, which 2026 testing keeps confirming.",
                    },
                    {
                        "title": "Tiger JKT-D10U is faster and better at brown rice",
                        "body": "It matches Zojirushi on quality, then wins on brown rice and cooks far quicker: about 63 minutes versus 103 for brown.",
                    },
                    {
                        "title": "Tiger is the speed pick",
                        "body": "Roughly 44 minutes for white rice against 53 makes it the smarter buy for anyone who cooks often and hates waiting.",
                    },
                    {
                        "title": "Cuckoo CRP-ST0609F leads on flexibility",
                        "body": "It lets you customize settings down to keep-warm temperature on some models and steams quickly, though grains run stickier.",
                    },
                    {
                        "title": "Zojirushi NS-ZCC10 is the smart-value entry",
                        "body": "Excellent rice at a lower price than the induction flagships makes it the easiest way into proper micom cooking.",
                    },
                ],
            },
            "zh-tw": {
                "commentary": (
                    "前兩名這週鎖住不動，但理由越來越清楚。Zojirushi NP-HCC10 守第一，因為它的 IH 電磁加熱不管煮"
                    "壽司米、糙米還是印度香米，每次都鬆軟又穩定，2026 這輪測試一直在印證這點。平日晚上趕著開飯，"
                    "它是我最信任不會出包的那台。話說回來，Tiger JKT-D10U 真的有搶冠軍的本錢，我想講清楚它為什麼"
                    "貼第二貼這麼近。同場對比它整體米飯品質跟象印打平，糙米還更勝一籌，粒粒更鬆更輕，而且明顯快"
                    "很多：白米大約 44 分鐘對 53 分鐘，糙米 63 分鐘對 103 分鐘。你常煮糙米，或單純討厭等，Tiger "
                    "就是更聰明的選擇。Cuckoo CRP-ST0609F 排第四靠的是彈性，部分機型連保溫溫度都能自己調，蒸白米"
                    "糙米也快。它的飯粒比較黏，這就看你口感偏好。至於多數家庭，我還是推 Zojirushi NS-ZCC10 第三"
                    "名。它煮出來的飯很棒，價格又比 IH 旗艦親民，是踏進像樣微電腦電子鍋最好上手的入門款。台灣租"
                    "屋族小資首選它準沒錯。"
                ),
                "highlights": [
                    {
                        "title": "Zojirushi NP-HCC10 穩坐安全牌第一",
                        "body": "IH 加熱讓壽司米、糙米、香米每次都鬆軟一致，2026 測試一再印證。",
                    },
                    {
                        "title": "Tiger JKT-D10U 更快又更會煮糙米",
                        "body": "整體品質跟象印打平，糙米更勝，而且快很多：糙米約 63 分鐘對 103 分鐘。",
                    },
                    {
                        "title": "Tiger 是速度首選",
                        "body": "白米約 44 分鐘對 53 分鐘，常開伙又討厭等的人選它最划算。",
                    },
                    {
                        "title": "Cuckoo CRP-ST0609F 彈性最強",
                        "body": "部分機型連保溫溫度都能調，蒸飯也快，只是飯粒偏黏，看個人口感。",
                    },
                    {
                        "title": "Zojirushi NS-ZCC10 是聰明入門款",
                        "body": "米飯水準很高，價格又比 IH 旗艦親民，是踏進微電腦電子鍋最好上手的選擇。",
                    },
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)


# ---------------------------------------------------------------------------
# 6. SMART SPEAKERS
# ---------------------------------------------------------------------------
def smart_speakers():
    d, p = load("best-smart-speakers.json")
    entry = {
        "date": DATE,
        "rankings": last_rankings(d),
        "references": [
            {
                "title": "Best smart speakers 2026: top Amazon Echo, Google Nest and Apple picks",
                "url": "https://www.t3.com/features/best-smart-speaker",
                "source": "T3",
            },
            {
                "title": "Best smart speakers 2026: top voice-assistant speakers tested by our experts",
                "url": "https://www.whathifi.com/best-buys/best-smart-speakers-the-best-voice-assistant-speakers",
                "source": "What Hi-Fi?",
            },
            {
                "title": "Best smart speakers in 2026, Alexa, Google, and Siri tested",
                "url": "https://www.tomsguide.com/us/best-smart-speakers,review-4480.html",
                "source": "Tom's Guide",
            },
        ],
        "i18n": {
            "en": {
                "commentary": (
                    "My list holds steady this week, and the 2026 round of expert testing supports the shape of it. "
                    "The Amazon Echo Studio 2nd Gen stays my number one because it pairs genuinely room-filling sound "
                    "with the broadest smart-home brain in the category, handling Zigbee and Matter so it can act as "
                    "the hub a real connected home needs. For most people building out smart lighting and sensors, "
                    "this is the speaker that does the most jobs well. The Sonos Era 100 holds second on pure audio "
                    "craft. Reviewers keep calling out how it delivers spectacular sound from a very small footprint, "
                    "and a stereo pair gives you outstanding separation for far less than premium alternatives, which "
                    "is the value play I point music-first buyers toward. Apple's HomePod 2nd Gen stays at three, and "
                    "its standout trick is still real-time room scanning that optimizes audio for wherever you place "
                    "it, plus it now works as a stronger hub across both HomeKit and Matter. If you live in Apple's "
                    "world, it is the obvious pick. The Sonos Era 300 sits at four for spatial audio, wrapping a "
                    "room from a single cabinet using two woofers and four tweeters. Down the list, the Amazon Echo "
                    "lineup keeps owning value and voice. The 4th Gen remains the all-rounder I recommend most, and "
                    "the Echo Dot Max brings snappy Alexa and full smart-home control in a compact, affordable shell "
                    "for anyone starting out."
                ),
                "highlights": [
                    {
                        "title": "Echo Studio 2nd Gen does the most jobs well",
                        "body": "Room-filling sound plus Zigbee and Matter support let it serve as the hub a real connected home needs, holding my top spot.",
                    },
                    {
                        "title": "Sonos Era 100 is the music-first value pick",
                        "body": "Reviewers praise its spectacular sound from a tiny footprint, and a stereo pair gives outstanding separation for less than premium rivals.",
                    },
                    {
                        "title": "HomePod 2nd Gen owns room optimization",
                        "body": "Real-time room scanning tunes audio to placement, and stronger HomeKit plus Matter support makes it the clear Apple-ecosystem pick.",
                    },
                    {
                        "title": "Sonos Era 300 leads spatial audio",
                        "body": "Two woofers and four tweeters wrap a room from a single cabinet, the choice when immersive Atmos playback is the goal.",
                    },
                    {
                        "title": "Echo 4th Gen stays the all-rounder",
                        "body": "Responsive Alexa, Zigbee and Matter support, and built-in sensors keep it the speaker I recommend most for value.",
                    },
                ],
            },
            "zh-tw": {
                "commentary": (
                    "這週我的榜單維持原樣，2026 這輪專家測試也撐得住這個排序。Amazon Echo Studio 二代守第一，因為它"
                    "把真正充滿整個房間的聲音，跟全類別最強的智慧家庭大腦綁在一起，支援 Zigbee 跟 Matter，可以當"
                    "真正連網家庭需要的中樞。對多數要鋪智慧燈光跟感測器的人，這台一機多用又樣樣都行。Sonos Era "
                    "100 靠純音質排第二。評測一直強調它體積那麼小卻能塞出驚人的聲音，組一對立體聲分離度超好，價格"
                    "又比高階對手親民，這就是我推給音樂優先買家的 CP 值選擇。Apple HomePod 二代排第三，它的招牌絕"
                    "活還是即時掃描房間，依你擺放位置自動優化音場，現在當智慧中樞也更強，HomeKit 跟 Matter 都吃。"
                    "你活在蘋果生態圈裡，選它最直覺。Sonos Era 300 排第四主打空間音訊，用兩顆低音加四顆高音，單"
                    "一台就能把整個房間包起來。榜單往下看，Amazon Echo 系列在 CP 值跟語音這塊還是稱霸。四代依然"
                    "是我最常推的全能型，Echo Dot Max 則把俐落的 Alexa 跟完整智慧家庭控制塞進一個小巧又便宜的"
                    "殼裡，入門最適合。"
                ),
                "highlights": [
                    {
                        "title": "Echo Studio 二代一機多用樣樣行",
                        "body": "充滿房間的聲音加上 Zigbee、Matter 支援，能當真正連網家庭的中樞，穩坐我第一。",
                    },
                    {
                        "title": "Sonos Era 100 是音樂優先 CP 值首選",
                        "body": "評測讚它小體積塞出驚人音質，組一對立體聲分離度超好，價格又比高階對手親民。",
                    },
                    {
                        "title": "HomePod 二代房間優化最強",
                        "body": "即時掃描房間依擺位調音場，HomeKit 與 Matter 中樞也更強，蘋果生態圈首選就是它。",
                    },
                    {
                        "title": "Sonos Era 300 主打空間音訊",
                        "body": "兩顆低音加四顆高音，單一台就把整個房間包起來，想玩沉浸 Atmos 選它。",
                    },
                    {
                        "title": "Echo 四代仍是全能王",
                        "body": "靈敏的 Alexa、Zigbee 與 Matter 支援加內建感測器，CP 值上我最常推的就是它。",
                    },
                ],
            },
        },
    }
    upsert(d, entry)
    save(p, d)


if __name__ == "__main__":
    ai_music()
    dishwashers()
    gaming_monitors()
    headphones()
    rice_cookers()
    smart_speakers()
    print("done")
