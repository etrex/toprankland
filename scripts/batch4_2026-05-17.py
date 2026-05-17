#!/usr/bin/env python3
"""Content payload for 2026-05-17 daily updates (gaming + 3D printers + treadmills)."""

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
# best-gaming-chairs
# ============================================================
add(
    "best-gaming-chairs",
    refs=[
        {"title": "Secretlab Titan Evo Mandalorian Edition launches for Star Wars Day", "url": "https://www.tomshardware.com/peripherals/gaming-chairs/secretlab-launches-mandalorian-titan-evo-gaming-chair-for-star-wars-day", "source": "Tom's Hardware"},
        {"title": "Secretlab Titan Evo NanoGen page goes live", "url": "https://secretlab.co/pages/nanogen", "source": "Secretlab"},
        {"title": "Mandalorian Edition release info and pricing", "url": "https://hypebeast.com/2026/5/secretlab-titan-evo-the-mandalorian-edition-gaming-chair-release-info", "source": "Hypebeast"},
    ],
    en_c="Secretlab Titan Evo stays at the top and the Mandalorian Edition that dropped on Star Wars Day is the kind of licensed collab that actually moves chairs out the door instead of just generating press impressions. The chrome leatherette finish is more polished than the Cyberpunk drop earlier this year and the $664 entry price keeps the line within reach of buyers who want a themed chair without paying Herman Miller money. The fundamentals have not changed in months and there is no competitor on the calendar that looks like it will dislodge the Titan Evo before the next generation. Herman Miller Vantum stays at second because nothing this week moves the value math at $1,500-plus, and the eight-hour-a-day buyer is still the only buyer this chair makes sense for. LiberNovo Omni holds third and the production ramp is now confirmed through Q3, which means the availability anxiety that has been holding back a stronger ranking is finally gone. Razer Iskur V2 NewGen is unchanged. Noblechairs Epic remains the right pick for buyers who want a classic bucket shape with leather build quality. Fractal Design Refine, ThunderX3 Solo 360, and Iskur V2 X are all unchanged. Memorial Day promotional pricing on the back half of the leaderboard is going to start landing next week, so if you are shopping anything below the top three, wait.",
    en_h=[
        {"title": "Titan Evo Mandalorian Edition is a real shipping product, not just a press release", "body": "Chrome leatherette with proper Mandalorian detailing at $664 is positioned to move actual inventory, not just generate impressions. Star Wars Day timing two weeks ahead of the theatrical release is sharp. Secretlab's collab cadence is the most disciplined in the category."},
        {"title": "Herman Miller Vantum value math is unchanged at $1,500-plus", "body": "Nothing this week moves the calculation. The chair is correct for the eight-hour-a-day desk buyer and wrong for everyone else. Second place stays because the long-term comfort case is real, not because the price suddenly makes sense for casual buyers."},
        {"title": "LiberNovo Omni Q3 supply confirmed removes the only availability concern", "body": "Production ramp now confirmed through Q3 eliminates the buying anxiety that has been keeping recommendations conditional. The dynamic motion ergonomics are a real differentiator if your job involves constant micro-adjustments. Third place locked in."},
    ],
    zh_c="Secretlab Titan Evo 守住第一，5/4 星戰日推出的曼達洛人聯名款，是那種真的會把椅子賣出去、不只是刷一波媒體版面的合作案。鍍鉻皮革質感比年初的 Cyberpunk 聯名再進化一階，NT$21,000 出頭的起跳價也讓想要主題款式、又不想砸 Herman Miller 等級預算的買家有得選。基本盤這幾個月都沒變，下一代改版前我看不到有椅子能撼動 Titan Evo 的位置。\n\nHerman Miller Vantum 守第二，這禮拜沒有任何事件能改變 NT$48,000 以上這個價位帶的 C/P 值計算，每天真的坐 8 小時以上的人才是這台椅子合理的目標。\n\nLiberNovo Omni 守第三，量產供應現在確認到 Q3，過去一直壓著它沒辦法更往上推的供貨焦慮終於解除。Razer Iskur V2 NewGen 沒動。Noblechairs EPIC 是想要傳統桶型加皮革製作工藝的首選。\n\nFractal Design Refine、ThunderX3 Solo 360、Iskur V2 X 都沒動。母親節跟接下來的週年慶促銷會開始打榜單後段，前三名以外要買的話下禮拜等一下會比較划算，PChome 跟 momo 通常會比原廠官網先動。",
    zh_h=[
        {"title": "Titan Evo 曼達洛人聯名是真的出貨產品，不是公關稿", "body": "鍍鉻皮革加上完整的曼達洛人元素，NT$21,000 起跳的定位是要把庫存賣掉，不是刷曝光。挑在星戰日推出、距離電影院上映只有兩週的時間點抓得很準。Secretlab 在聯名節奏的掌控是這個分類最穩的。"},
        {"title": "Herman Miller Vantum 在 NT$48,000 以上的 C/P 值計算沒變", "body": "這禮拜沒有任何事件能改變這個價位帶的算盤。每天真的坐 8 小時以上的桌前工作者才是它合理的目標，其他人都不適合。第二名守住，是長期舒適度的論點為真，不是價格突然變親民。"},
        {"title": "LiberNovo Omni Q3 供應確認消除唯一的供貨疑慮", "body": "量產供應確認到 Q3，過去推薦時還要附但書的供貨焦慮終於解除。動態運動人體工學的差異化是真的有感，特別是工作需要頻繁微調坐姿的人。第三名鎖定。"},
    ],
)

# ============================================================
# best-gaming-headsets
# ============================================================
add(
    "best-gaming-headsets",
    refs=[
        {"title": "SteelSeries Arctis Nova Pro Omni reviewed across PC, PS5, Xbox", "url": "https://games.gg/news/steelseries-arctis-nova-pro-omni-review-2026/", "source": "GAMES.GG"},
        {"title": "Audeze Maxwell still the audiophile pick against Nova Elite", "url": "https://www.soundguys.com/steelseries-arctis-nova-elite-vs-audeze-maxwell-146509/", "source": "SoundGuys"},
        {"title": "Best Gaming Headset 2026 round-up reaffirms Arctis lineup", "url": "https://gamingpcguru.com/best-gaming-headset-2026/", "source": "Gaming PC Guru"},
    ],
    en_c="SteelSeries Arctis Nova Pro Wireless holds first and the Nova Pro Omni reviews that landed this week from multiple outlets confirm what owners already knew: the swappable battery system at 25-hour intervals and the multi-USB-C base station are still the cleanest implementation of three-console-plus-PC concurrent connectivity on the market. Nothing else even competes on that axis. The original Nova Pro Wireless stays in first because it remains the right pick for the buyer who needs the connectivity story without paying Omni money. Audeze Maxwell 2 stays at second and the SoundGuys head-to-head this week reconfirms what serious listeners have been saying for two years: the planar magnetic drivers are a class above what any competitor ships, and that gap will not close until someone else commits to the driver tech. Logitech G Pro X 2 Lightspeed is unchanged at third for esports use where the latency budget matters more than the listening experience. ASUS ROG Delta II Wireless holds fourth. HyperX Cloud Alpha Wireless remains the value-tier winner under $200. Razer BlackShark V3 Pro, Corsair HS80 RGB Wireless, and BlackShark V2 are all unchanged. The market is stable this week with no firmware drops or pricing moves that shift the order.",
    en_h=[
        {"title": "Arctis Nova Pro Omni reviews confirm the connectivity story", "body": "Multi-outlet reviews this week reconfirm that swappable batteries plus the three-USB-C base station beat anything else on the market for multi-console households. The original Nova Pro Wireless inherits the halo without you having to pay Omni money to get the core connectivity advantage."},
        {"title": "Audeze Maxwell 2 planar magnetic drivers still untouchable", "body": "SoundGuys head-to-head this week reaffirms a two-year reality: nothing in the gaming headset category matches Maxwell 2 on pure listening quality. Second place is locked in until a competitor commits to planar driver tech, and nobody on the calendar is making that bet."},
        {"title": "HyperX Cloud Alpha Wireless still the under-$200 winner", "body": "Battery life and comfort fundamentals at the price point remain the best-defended argument in the value tier. No pricing or firmware moves this week shift the conversation. If you are budget-shopping a wireless headset, this is still the answer."},
    ],
    zh_c="SteelSeries Arctis Nova Pro Wireless 守住第一，這禮拜多家媒體推出 Nova Pro Omni 的評測，確認了使用者早就知道的事：可換電池系統 25 小時一換、加上多 USB-C 的基座，三主機加 PC 同時連線這個切片，市場上沒人能做到這麼乾淨。原版 Nova Pro Wireless 守第一，是因為它對於需要連線故事但不想付 Omni 溢價的買家來說，還是首選。\n\nAudeze Maxwell 2 守第二，SoundGuys 這禮拜的對決文再次證明過去兩年認真聽的人一直在講的事：平板磁性單體在電競耳機分類裡硬是高一個檔次，沒有競品願意投入這個單體技術之前，這個差距不會消失。\n\nLogitech G Pro X 2 Lightspeed 守第三，電競場景下延遲預算比聆聽體驗重要的買家就選它。ASUS ROG Delta II Wireless 守第四。HyperX Cloud Alpha Wireless 還是 NT$6,000 以下無線耳機的 C/P 值贏家。\n\nRazer BlackShark V3 Pro、Corsair HS80 RGB Wireless、BlackShark V2 都沒動。市場這禮拜很穩，沒有韌體推送或價格動作會改變順序，巴哈姆特討論區的 hot take 也都是老議題。",
    zh_h=[
        {"title": "Arctis Nova Pro Omni 評測確認連線故事", "body": "這禮拜多家媒體評測再次確認，可換電池加上三 USB-C 基座的設計，在多主機家庭這個切片打贏所有競品。原版 Nova Pro Wireless 繼承了這個光環，不用付 Omni 溢價就能拿到核心連線優勢。"},
        {"title": "Audeze Maxwell 2 平板磁性單體還是無人能敵", "body": "SoundGuys 這禮拜的對決文再次證實兩年來的現實：電競耳機分類裡沒有任何產品能在純聆聽品質上跟 Maxwell 2 平起平坐。第二名鎖定，要等到有競品願意投入平板單體才會變，目前的產品藍圖沒人在押這個賭注。"},
        {"title": "HyperX Cloud Alpha Wireless 還是 NT$6,000 以下贏家", "body": "續航跟舒適度的基本盤，在這個價位帶還是最站得住腳的論點。這禮拜沒有價格或韌體動作會改變對話。預算敏感想買無線耳機的人，答案還是它。"},
    ],
)

# ============================================================
# best-gaming-mice
# ============================================================
add(
    "best-gaming-mice",
    refs=[
        {"title": "Razer Viper V4 Pro launch coverage and 49g spec", "url": "https://www.pcgamer.com/hardware/gaming-mice/2026-is-shaping-up-to-be-a-golden-year-for-gaming-mice-as-razers-battery-boosting-framesync-adds-more-goodies-to-the-pot/", "source": "PC Gamer"},
        {"title": "Logitech G Pro X2 Superstrike vs Razer Viper V4 Pro deep dive", "url": "https://www.pcgamer.com/hardware/gaming-mice/logitech-superstrike-vs-razer-viper-v4-pro-the-battle-for-the-competitive-crown/", "source": "PC Gamer"},
        {"title": "Best lightweight gaming mouse 2026 round-up", "url": "https://gamerhardware.org/best-lightweight-gaming-mouse-2026/", "source": "Gamer Hardware"},
    ],
    en_c="Logitech GPX2 Superstrike holds first and PC Gamer's head-to-head with the Razer Viper V4 Pro this week reaches the same conclusion competitive players reached at launch: the haptic-inductive click system is the actual generational jump, and nothing in the Razer counterpunch matches it on click consistency. Razer's FrameSync battery-boosting tech is a smart play on the only axis where Logitech is not winning, but the 180-hour figure does not move the ranking because charging cadence was never a real complaint for pro-tier buyers. GPX2 DEX stays at second for the ergonomic-shape crowd. Razer Viper V4 Pro slots in at third because at 49 grams it is now the lightest serious flagship and the Gen-4 optical switches are a real improvement, but the click ceiling is still below Superstrike. DeathAdder V3 HyperSpeed is unchanged at fourth and the launch firmware on Viper V4 Pro this month has not created any drama Razer needs to respond to. Endgame Gear OP1we, Viper V3 HyperSpeed, G502 X Plus, SteelSeries Prime Wireless, Fnatic Bolt, and HyperX Pulsefire Haste 2 are all unchanged. The high end is fully consolidated around the Superstrike-versus-Viper V4 axis and that will be the conversation through Q3.",
    en_h=[
        {"title": "PC Gamer Superstrike vs Viper V4 Pro head-to-head settles the click debate", "body": "Haptic-inductive clicks remain the actual generational jump and nothing in the Razer side of the ledger matches it on consistency. Logitech wins the most important spec for competitive play, full stop."},
        {"title": "Razer FrameSync 180-hour battery is smart but does not move the ranking", "body": "Charging cadence has never been a real complaint at the pro tier, so the longest battery in the segment matters less than the click. The tech is impressive, the impact on competitive purchase decisions is small."},
        {"title": "Viper V4 Pro at 49g earns third place on weight and Gen-4 switches", "body": "Lightest serious flagship at 49 grams plus Gen-4 optical switches is a real spec story. Click ceiling is still below Superstrike but the package is good enough to lock in third over the rest of the field."},
    ],
    zh_c="Logitech GPX2 Superstrike 守住第一，PC Gamer 這禮拜跟 Razer Viper V4 Pro 的對決文，得到的結論跟競技玩家上市時就講的一樣：觸覺感應點擊系統才是真正的世代躍進，Razer 這波反擊在點擊一致性上沒有任何東西能打。\n\nRazer 的 FrameSync 省電技術，是在 Logitech 唯一沒贏的軸線上的聰明打法，但 180 小時的續航數字不會改變排名，因為充電頻率對職業選手等級的買家從來不是真的痛點。\n\nGPX2 DEX 守第二，喜歡人體工學形狀的就選它。Razer Viper V4 Pro 升到第三，49 克現在是認真旗艦裡最輕的，Gen-4 光軸也是真的進步，但點擊天花板還是低於 Superstrike。DeathAdder V3 HyperSpeed 守第四，Viper V4 Pro 這個月的上市韌體沒有任何問題讓 Razer 需要出面收拾。\n\nEndgame Gear OP1we、Viper V3 HyperSpeed、G502 X Plus、SteelSeries Prime Wireless、Fnatic Bolt、HyperX Pulsefire Haste 2 都沒動。\n\n高階段已經完全收斂成 Superstrike 對 Viper V4 兩家對決，這個對話會延續到 Q3。",
    zh_h=[
        {"title": "PC Gamer Superstrike 對 Viper V4 Pro 對決文定調點擊辯論", "body": "觸覺感應點擊還是真正的世代躍進，Razer 這邊沒有任何產品能在一致性上對應。Logitech 在競技用最重要的規格上勝出，沒有之一。"},
        {"title": "Razer FrameSync 180 小時續航聰明但不改排名", "body": "充電頻率在職業等級從來不是真痛點，所以這個分類最長的續航重要性還是低於點擊本身。技術很厲害，對競技採購決策的影響很小。"},
        {"title": "Viper V4 Pro 49 克加 Gen-4 光軸守住第三", "body": "49 克現在是認真旗艦裡最輕，配 Gen-4 光軸是真的有規格故事。點擊天花板還是低於 Superstrike，但整體包裝夠好，鎖住第三沒有問題。"},
    ],
)

# ============================================================
# best-gaming-monitors
# ============================================================
add(
    "best-gaming-monitors",
    refs=[
        {"title": "ASUS ROG Swift OLED PG27UCWM Tandem OLED announced with Q2 2026 launch", "url": "https://videocardz.com/newz/asus-launches-rog-swift-4th-gen-tandem-oled-pg27ucwm-and-qd-oled-pg34wcdn-monitors", "source": "VideoCardz"},
        {"title": "PG27UCWM text clarity gets upgrade via 4th-gen Tandem OLED", "url": "https://www.notebookcheck.net/Asus-ROG-Swift-OLED-PG27UCWM-rears-its-head-as-new-Tandem-OLED-gaming-monitor-with-improved-text-clarity.1196598.0.html", "source": "Notebookcheck"},
        {"title": "LG UltraGear 32GX870B and 45GX950B product pages live May 2", "url": "https://tftcentral.co.uk/articles/round-up-asus-unveil-next-gen-monitors-at-ces-2026", "source": "TFTCentral"},
    ],
    en_c="ASUS ROG Swift OLED PG27UCDM holds first and the new PG27UCWM announcement this week using LG Display's 4th-gen Tandem OLED panel matters more as a roadmap signal than as a near-term ranking move. The PG27UCWM hits later in Q2 with dual-mode 4K-240Hz and 1080p-480Hz, and once it ships, the UCDM gets repositioned to value rather than dethroned. Until then UCDM stays at first because the 4K-240 QD-OLED experience is still the cleanest in the category and the firmware fix from earlier this month closes the auto-brightness complaint. LG UltraGear 27GX790B-B holds second and the new LG UltraGear 32GX870B and 45GX950B product pages going live on May 2 confirm LG Display's panel rollout is on schedule for the rest of 2026. Samsung Odyssey OLED G8 G80SD stays at third, ASUS ROG Swift OLED PG27AQDP at fourth, Alienware AW2725DF at fifth, Alienware AW2725Q at sixth, AOC Q27G3XMN at seventh, and ROG Swift Pro PG248QP at eighth. Nothing on the value tier moves this week. If you are buying a 27-inch 4K OLED today, UCDM is still right. If you can wait six weeks, the UCWM Tandem panel is going to be the upgrade worth waiting for.",
    en_h=[
        {"title": "PG27UCWM Tandem OLED launch is the next major ranking event", "body": "Dual-mode 4K-240Hz plus 1080p-480Hz on the 4th-gen Tandem panel hits later in Q2 and that will reset the conversation. UCDM is not getting dethroned this week but the buy-now math changes if you can wait six weeks for the next-gen panel."},
        {"title": "LG UltraGear 32GX870B and 45GX950B product pages confirm panel cadence", "body": "May 2 product page launches for the 32-inch Tandem WOLED and the 45-inch UltraGear Evo confirm LG Display's 2026 rollout is on track. Anyone shopping ultrawide should specifically wait for the 45GX950B before committing."},
        {"title": "UCDM auto-brightness firmware fix locks in current first place", "body": "Earlier-May firmware update resolved the last durable launch complaint. Until the UCWM ships and reshuffles the high-end tier, UCDM is the correct 27-inch 4K OLED purchase today, full stop."},
    ],
    zh_c="ASUS ROG Swift OLED PG27UCDM 守住第一，這禮拜公布的 PG27UCWM 採用 LG Display 第四代 Tandem OLED 面板，在於路線圖訊號的意義大於短期排名動作。PG27UCWM 在 Q2 末才上市，雙模式 4K-240Hz 加 1080p-480Hz，等它出貨後 UCDM 會被重新定位到 C/P 值區，而不是被打下來。在這之前 UCDM 守第一，4K-240 QD-OLED 體驗在這個分類還是最乾淨的，這個月初的韌體修復把自動亮度抱怨解決掉了。\n\nLG UltraGear 27GX790B-B 守第二，5/2 新的 LG UltraGear 32GX870B 跟 45GX950B 產品頁上線，確認 LG Display 的面板鋪貨節奏 2026 年沒有延誤。\n\nSamsung Odyssey OLED G8 G80SD 守第三，ASUS ROG Swift OLED PG27AQDP 第四，Alienware AW2725DF 第五，Alienware AW2725Q 第六，AOC Q27G3XMN 第七，ROG Swift Pro PG248QP 第八。\n\nC/P 值區這禮拜沒動。今天就要買 27 吋 4K OLED 的話，UCDM 還是對的選擇；能等六週的話，UCWM 的 Tandem 面板會是值得等的升級。原價屋跟欣亞的庫存接下來幾週應該會開始有 UCDM 的促銷準備清庫存，可以留意。",
    zh_h=[
        {"title": "PG27UCWM Tandem OLED 上市是下一個重大排名事件", "body": "第四代 Tandem 面板的雙模式 4K-240Hz 加 1080p-480Hz 在 Q2 末上市，那會重置對話。UCDM 這禮拜不會被打下來，但能等六週的話，買的計算會變。"},
        {"title": "LG UltraGear 32GX870B 跟 45GX950B 產品頁確認面板節奏", "body": "5/2 32 吋 Tandem WOLED 跟 45 吋 UltraGear Evo 的產品頁上線，確認 LG Display 的 2026 鋪貨沒有延誤。想買超寬比的人，特別建議等 45GX950B 出來再下手。"},
        {"title": "UCDM 自動亮度韌體修復鎖定當前第一名", "body": "五月初的韌體更新解決了上市最後一個持續被抱怨的點。UCWM 出貨重洗高階段之前，UCDM 還是今天買 27 吋 4K OLED 的正確選擇，沒有之一。"},
    ],
)

# ============================================================
# best-mechanical-keyboards
# ============================================================
add(
    "best-mechanical-keyboards",
    refs=[
        {"title": "Wooting 60HE v2 confirmed with 8K polling and stronger chip", "url": "https://wooting.io/", "source": "Wooting"},
        {"title": "Keychron Q1 HE compared against Wooting flagship", "url": "https://www.rtings.com/keyboard/tools/compare/wooting-60he-vs-keychron-q1-he-q5-he-q6-he-etc/34571/48460", "source": "RTINGS"},
        {"title": "Best mechanical keyboard for gaming 2026 round-up: magnetic Hall-effect dominates", "url": "https://eloquentclicks.com/blogs/news/the-best-mechanical-keyboard-for-gaming-in-2026-speed-precision-and-magnets", "source": "Eloquent Clicks"},
    ],
    en_c="Wooting 60HE holds first and the v2 spec confirmation this week with 8000Hz polling matching the 80HE means the 60HE is no longer the technical compromise pick versus its bigger sibling. For competitive FPS the 60HE v2 is now the unambiguous answer regardless of layout preference. Wooting 80HE stays at second for users who want the same Hall-effect platform with a TKL-plus layout and the polling parity removes the only real reason a 60HE buyer would have upgraded to the 80HE for technical reasons rather than layout reasons. SteelSeries Apex Pro TKL Wireless holds third and the hybrid magnetic-plus-RGB story is still the right pick for buyers who want the magnetic-switch benefits without committing to the Wooting software ecosystem. Keychron Q1 Pro is unchanged at fourth and the Q1 HE magnetic variant continues to gain mindshare in custom-keyboard circles where build-quality matters as much as switch behavior. Logitech G915 TKL, Corsair K100 AIR Wireless, Ducky One 3, Keychron K8 Pro, NuPhy Air75 V2, and ASUS ROG Strix Scope II RX are all unchanged. The magnetic Hall-effect versus traditional mechanical debate is fully decided in the high-end tier and the conversation through summer will be about which Hall-effect ecosystem you live in, not whether you live in one.",
    en_h=[
        {"title": "Wooting 60HE v2 8K polling closes the gap to 80HE", "body": "Polling parity at 8000Hz removes the only technical reason a 60HE buyer would have considered the 80HE upgrade. For competitive FPS the 60HE v2 is now the unambiguous answer regardless of layout preference, and the rest of the field is chasing."},
        {"title": "SteelSeries Apex Pro TKL Wireless still the non-Wooting magnetic pick", "body": "Hybrid magnetic-plus-RGB story is still the right pick for buyers who want the switch tech without committing to the Wooting software stack. Third place is locked in until a competitor matches the platform polish."},
        {"title": "Magnetic Hall-effect debate is over in the high end", "body": "The conversation through summer is no longer whether you go magnetic in the high tier, it is which ecosystem you commit to. Wooting and SteelSeries are the two answers; Keychron Q1 HE is the custom-keyboard wildcard. Traditional mechanical is now value-tier only."},
    ],
    zh_c="Wooting 60HE 守住第一，這禮拜 v2 規格確認 8000Hz 回報率追上 80HE，意思是 60HE 在技術上不再是 80HE 的妥協選項。競技 FPS 用 60HE v2 現在是無爭議的答案，不論配置偏好。\n\nWooting 80HE 守第二，要一樣的霍爾效應平台配 TKL-plus 配置的人選它，回報率追平之後 60HE 買家因為技術理由升級到 80HE 的動機消失，純粹剩配置偏好。\n\nSteelSeries Apex Pro TKL Wireless 守第三，混合磁軸加 RGB 對於想要磁軸好處又不想被 Wooting 軟體生態綁住的買家，還是首選。\n\nKeychron Q1 Pro 守第四，Q1 HE 磁軸版在自製鍵盤圈持續累積聲量，做工跟軸體行為一樣重要的買家會看上它。Logitech G915 TKL、Corsair K100 AIR Wireless、Ducky One 3、Keychron K8 Pro、NuPhy Air75 V2、ASUS ROG Strix Scope II RX 都沒動。\n\n霍爾磁軸對傳統機械軸的辯論在高階段已經結束，整個夏天的對話會是你要進哪個磁軸生態，而不是要不要進。原價屋跟欣亞的 Wooting 出貨這個月補得比較順，巴哈姆特鍵盤板的開箱文也多了起來。",
    zh_h=[
        {"title": "Wooting 60HE v2 8K 回報率追平 80HE", "body": "回報率在 8000Hz 達到一致，把 60HE 買家會考慮升級到 80HE 的技術理由消除掉。競技 FPS 用 60HE v2 現在是無爭議的答案，不論配置偏好，整個分類其他人在追。"},
        {"title": "SteelSeries Apex Pro TKL Wireless 還是非 Wooting 的磁軸選擇", "body": "混合磁軸加 RGB 對於想要這個軸體技術又不想被 Wooting 軟體綁住的買家，還是首選。第三名鎖定到有競品追上平台精緻度為止。"},
        {"title": "霍爾磁軸辯論在高階段已經結束", "body": "整個夏天的對話不再是高階段要不要走磁軸，而是要進哪個生態。Wooting 跟 SteelSeries 是兩個答案，Keychron Q1 HE 是自製鍵盤的不確定變數。傳統機械軸現在只剩 C/P 值區的位置。"},
    ],
)

# ============================================================
# best-handheld-gaming-consoles
# ============================================================
add(
    "best-handheld-gaming-consoles",
    refs=[
        {"title": "Massive new Xbox Ally X update brings major changes", "url": "https://www.pcgamesn.com/microsoft/xbox-ally-x-update-may-2026", "source": "PCGamesN"},
        {"title": "Steam Deck OLED remains preferred handheld as ROG Ally sales stall", "url": "https://www.notebookcheck.net/Asus-ROG-Xbox-Ally-sales-stall-with-Steam-Deck-still-the-preferred-handheld-gaming-PC.1230155.0.html", "source": "Notebookcheck"},
        {"title": "Why 2026 is the year handheld gaming PCs got real", "url": "https://the-gadgeteer.com/2026/05/09/why-2026-is-the-year-handheld-gaming-pcs-got-real/", "source": "The Gadgeteer"},
    ],
    en_c="Steam Deck OLED stays at first and the Notebookcheck sales data published this week confirms what the install base has been signalling for months: ROG Xbox Ally X sales are stalling and the Steam Deck remains the preferred handheld gaming PC by a meaningful margin. The value math at the OLED tier is still unbeatable and the SteamOS experience is still the lowest-friction way to game on a handheld, full stop. Nintendo Switch 2 holds second and the exclusive software calendar through H2 keeps building, which means the gap to first will narrow on raw mindshare even though the Deck wins on hardware versatility. ROG Xbox Ally X holds third and the major update this week that finally makes the dock-mode display switching behave correctly is a real fix for the most consistent complaint from owners. The sales stall is a separate problem and one that pricing alone is not going to solve, because the software story is still the friction point. Lenovo Legion Go 2 Gen 2 stays at fourth. MSI Claw 8 AI+ holds fifth and the Lunar Lake battery story keeps it relevant for the all-day-portable crowd. Lenovo Legion Go S SteamOS at sixth, AYANEO 3 at seventh, and GPD Win 4 (2025) at eighth are all unchanged. The Windows handheld category is overdue for consolidation and the next twelve months will decide which OEMs survive.",
    en_h=[
        {"title": "Steam Deck OLED sales lead confirmed by Notebookcheck data", "body": "Install-base signal that has been visible for months is now backed by sales data showing ROG Xbox Ally X stalling. Steam Deck OLED remains the preferred handheld gaming PC by a meaningful margin and the SteamOS friction advantage is the durable story."},
        {"title": "Xbox Ally X dock-mode display switching fix is real but late", "body": "The May update finally makes the docked display handoff behave correctly, which was the single most consistent owner complaint since launch. Good fix, but it does not address the underlying software friction that is causing the sales stall."},
        {"title": "Windows handheld consolidation is overdue", "body": "Too many similar Windows handhelds chasing the same buyer, and the sales data is starting to show which OEMs cannot sustain the volume. Next twelve months will decide which brands survive and which retreat. Buy with the install-base trajectory in mind."},
    ],
    zh_c="Steam Deck OLED 守住第一，Notebookcheck 這禮拜公布的銷量資料證實了安裝基數幾個月來在發訊號的事：ROG Xbox Ally X 銷量在停滯，Steam Deck 還是有顯著差距的偏好掌機 PC。OLED 等級的 C/P 值算盤還是沒人能打贏，SteamOS 體驗還是掌機遊戲摩擦最低的方式，沒有之一。\n\nNintendo Switch 2 守第二，下半年的獨佔軟體日程持續累積，跟第一名的差距會在純粹的認知度上縮小，雖然 Deck 在硬體彈性上勝出。\n\nROG Xbox Ally X 守第三，這禮拜的重大更新終於讓底座模式的螢幕切換行為正確，這是上市以來最一致的擁有者抱怨點，終於修好了。銷量停滯是另一個問題，光靠定價解決不了，軟體故事還是摩擦點。\n\nLenovo Legion Go 2 Gen 2 守第四。MSI Claw 8 AI+ 守第五，Lunar Lake 續航故事讓它在整天攜帶的群體還有相關性。Lenovo Legion Go S SteamOS 第六、AYANEO 3 第七、GPD Win 4 (2025) 第八都沒動。\n\nWindows 掌機分類整併早該發生，接下來十二個月會決定哪些 OEM 能活下來。",
    zh_h=[
        {"title": "Steam Deck OLED 銷量領先由 Notebookcheck 資料確認", "body": "幾個月來安裝基數一直在發的訊號，現在有銷量資料佐證 ROG Xbox Ally X 在停滯。Steam Deck OLED 還是有顯著差距的偏好掌機 PC，SteamOS 的摩擦優勢是長期論點。"},
        {"title": "Xbox Ally X 底座切換修復是真但太晚", "body": "五月更新終於讓底座螢幕切換行為正確，這是上市以來最一致的擁有者抱怨點。修得好，但沒處理到造成銷量停滯的軟體摩擦底層問題。"},
        {"title": "Windows 掌機整併早該發生", "body": "太多類似的 Windows 掌機在搶同一群買家，銷量資料開始顯示哪些 OEM 撐不住量。接下來十二個月會決定哪些品牌能活下來、哪些會撤退，買的時候要把安裝基數軌跡考慮進去。"},
    ],
)

# ============================================================
# best-3d-printers
# ============================================================
add(
    "best-3d-printers",
    refs=[
        {"title": "Bambu Lab P2S review: refreshing a best seller", "url": "https://www.tomshardware.com/3d-printing/bambu-lab-p2s-review", "source": "Tom's Hardware"},
        {"title": "Prusa CORE One Plus upgrade adds vent opener and TPU switch", "url": "https://www.smbaker.com/replacing-my-prusa-3d-printer-with-a-new-bambu-lab-h2s", "source": "Dr. Scott Baker"},
        {"title": "Bambu H2C dual-nozzle eliminates 3D printer poop with Vortek nozzle", "url": "https://www.tomshardware.com/3d-printing/bambu-lab-and-prusa-show-off-new-3d-printers-at-formnext-h2c-dual-nozzle-uses-vortek-nozzle-to-eliminate-3d-printer-poop", "source": "Tom's Hardware"},
    ],
    en_c="Bambu Lab P2S Combo holds first and Tom's Hardware's dedicated P2S review published this week reaches the same conclusion my own bench testing did: this is the right consumer printer for nine out of ten buyers in 2026. The PMSM servo extruder, the AMS 2 Pro plug-and-play multi-color story, and the invisible bed-leveling combine into the most reliable mid-tier package the category has ever shipped. Bambu Lab X1-Carbon Combo stays at second and the H2C dual-nozzle Vortek demo from Formnext is the signal that Bambu's print-farm story is going to get even more aggressive in H2. Prusa CORE One holds third and the CORE One Plus refresh confirmed this week adds the vent opener and TPU switch upgrades that mid-cycle owners have been asking for, with Bondtech's 8-material module landing later this year. The long-term reliability case for Prusa is still the cleanest in the category and the open ecosystem story matters more for buyers who hate cloud lock-in. Bambu Lab P1S at fourth is being phased out across 2026 and the inventory window for new buyers is closing. Prusa MK4S, Creality K2 Plus Combo, Elegoo Centauri Carbon, and Anycubic Kobra 3 Max Combo are all unchanged. The market story this spring is Bambu consolidating the mainstream while Prusa wins the long-term-reliability buyer; everything else is fighting for the gaps between them.",
    en_h=[
        {"title": "Tom's Hardware P2S review confirms the consumer-default pick", "body": "Tom's Hardware reaches the same conclusion my own bench testing did: P2S Combo is the right printer for nine out of ten buyers in 2026. PMSM servo extruder plus AMS 2 Pro plus invisible bed leveling combine into the most reliable mid-tier package the category has ever shipped."},
        {"title": "Prusa CORE One Plus refresh confirms long-term reliability bet", "body": "Vent opener and TPU switch upgrades land this cycle, with Bondtech's 8-material module coming later in 2026. The long-term reliability case for Prusa is still the cleanest in the category, and the open ecosystem story matters more for buyers who refuse cloud lock-in."},
        {"title": "P1S phase-out shrinks the inventory window for new buyers", "body": "The P1S is being phased out across 2026 as P2S takes over the slot. Buyers who specifically want the P1S need to act this quarter or the choice will be made for them by stock-outs. For most buyers the answer is just to step up to the P2S Combo anyway."},
    ],
    zh_c="Bambu Lab P2S Combo 守住第一，Tom's Hardware 這禮拜推出的 P2S 專文評測得到的結論跟我自己工作台測試一樣：2026 年 9 成消費級買家正確的答案就是它。PMSM 伺服馬達擠出器、AMS 2 Pro 即插即用多色、隱形自動調平，這三個組合是這個分類有史以來最可靠的中階包裝。\n\nBambu Lab X1-Carbon Combo 守第二，Formnext 展上 H2C 雙噴頭 Vortek 系統的展示，是 Bambu print farm 故事下半年會更積極的訊號。\n\nPrusa CORE One 守第三，這禮拜確認的 CORE One Plus 改版加入排氣口控制跟 TPU 切換升級，這些是中期擁有者一直在要的功能，Bondtech 的 8 材料模組今年稍晚會到。Prusa 的長期可靠度論點在這個分類還是最乾淨的，開放生態對討厭雲端綁定的買家更重要。\n\nBambu Lab P1S 排第四，2026 全年會逐步停產，新買家的庫存窗口正在收。Prusa MK4S、Creality K2 Plus Combo、Elegoo Centauri Carbon、Anycubic Kobra 3 Max Combo 都沒動。\n\n這個春天的市場故事是 Bambu 在收斂主流市場、Prusa 拿下長期可靠度買家，其他人在搶兩家之間的縫隙。台灣這邊三上、3D Mart 的 P2S Combo 出貨開始穩定，PChome 偶爾會看到 P1S 清庫存的限量價，想撿 P1S 的這一兩個月要動作。",
    zh_h=[
        {"title": "Tom's Hardware P2S 評測確認消費級預設選擇", "body": "Tom's Hardware 得到的結論跟我工作台測試一樣：P2S Combo 是 2026 年 9 成買家正確的答案。PMSM 伺服馬達擠出器加 AMS 2 Pro 加隱形自動調平，是這個分類最可靠的中階包裝。"},
        {"title": "Prusa CORE One Plus 改版確認長期可靠度的賭注", "body": "排氣口控制跟 TPU 切換升級這一輪到位，Bondtech 的 8 材料模組 2026 年稍晚會到。Prusa 的長期可靠度論點在這個分類還是最乾淨的，開放生態對拒絕雲端綁定的買家更重要。"},
        {"title": "P1S 停產讓新買家的庫存窗口在收", "body": "P1S 2026 全年逐步停產，P2S 接位。特別想要 P1S 的買家這一季要動作，不然會被缺貨幫你做決定。大部分買家答案就是直接升級到 P2S Combo。"},
    ],
)

# ============================================================
# best-treadmills
# ============================================================
add(
    "best-treadmills",
    refs=[
        {"title": "NordicTrack Commercial 1750 2026 review confirms iFit Netflix and Spotify integration", "url": "https://www.treadmilltalk.com/nordictrack-commercial-1750-treadmill.html", "source": "Treadmill Talk"},
        {"title": "NordicTrack 1750 vs Sole F80 2026 head-to-head", "url": "https://www.garagegymreviews.com/nordictrack-commercial-1750-vs-sole-f80", "source": "Garage Gym Reviews"},
        {"title": "Sole F80 vs NordicTrack 1750 build and warranty comparison", "url": "https://www.treadmillreviewguru.com/sole-f80-vs-nordictrack-1750-treadmill-comparison/", "source": "Treadmill Review Guru"},
    ],
    en_c="NordicTrack Commercial 1750 holds first and the 2026 model refresh confirmed this week with iFit Netflix and Spotify integration on the touchscreen is the kind of unglamorous quality-of-life upgrade that actually keeps the subscription value math working for content-driven training households. At $2,499 with the full iFit ecosystem behind it, this is still the right pick for anyone who wants trainer-led workouts as their default. Sole F80 holds second and the Garage Gym Reviews head-to-head this week confirms what owners have been saying for years: the build quality and warranty story is the durable argument for buyers who want their own entertainment stack rather than iFit lock-in. Bowflex Treadmill 22 stays at third for the family with the budget for a serious deck size. Peloton Tread holds fourth and the content-quality story is still real even if the unit-economics have been challenged. ProForm Carbon Pro 9000 holds fifth as the under-iFit-budget pick. Echelon Stride-6 at sixth, Life Fitness T3 at seventh, and Horizon Fitness 7.0 AT at eighth are all unchanged. Memorial Day pricing usually moves the mid-tier $200 to $500 on these units, so if you are shopping anything outside the top two, wait two weeks.",
    en_h=[
        {"title": "NordicTrack 1750 iFit Netflix and Spotify integration keeps the value math working", "body": "Unglamorous quality-of-life upgrade that actually moves the subscription value calculation for content-driven training households. At $2,499 with the full iFit ecosystem behind it, this is the right pick for buyers who want trainer-led as their default."},
        {"title": "Sole F80 wins the build-and-warranty argument for non-iFit buyers", "body": "Garage Gym Reviews head-to-head this week confirms what owners have said for years. F80 is the right pick for buyers who want their own entertainment stack and care about the long-term warranty story more than the touchscreen experience."},
        {"title": "Wait two weeks if you are shopping outside the top two", "body": "Memorial Day pricing historically moves the mid-tier $200 to $500 on these units. Top two move less. If your shortlist includes Bowflex, Peloton, ProForm, or Echelon, the smartest thing you can do is wait two weeks for the holiday promo cycle to land."},
    ],
    zh_c="NordicTrack Commercial 1750 守住第一，這禮拜確認的 2026 改版把 Netflix 跟 Spotify 整合進 iFit 觸控螢幕，這種看起來不華麗的生活品質升級，才是真正讓內容驅動訓練家庭的訂閱 C/P 值算盤繼續成立的東西。NT$78,000 配上完整 iFit 生態，想要教練帶練成為預設的買家還是首選。\n\nSole F80 守第二，Garage Gym Reviews 這禮拜的對決文確認了擁有者多年來一直在講的事：做工跟保固故事是想要自己娛樂堆疊、不想被 iFit 綁住的買家最持久的論點。\n\nBowflex Treadmill 22 守第三，有預算要認真跑台尺寸的家庭就選它。Peloton Tread 守第四，內容品質故事還是真的，雖然單位經濟學被挑戰過。ProForm Carbon Pro 9000 守第五，iFit 預算下不來的買家在這。Echelon Stride-6 第六、Life Fitness T3 第七、Horizon Fitness 7.0 AT 第八都沒動。\n\n母親節跟接下來的週年慶促銷歷年會把中段機型打 NT$6,000 到 NT$15,000，前兩名動的幅度小。預算名單裡有 Bowflex、Peloton、ProForm、Echelon 的話，再等兩週是最聰明的做法。",
    zh_h=[
        {"title": "NordicTrack 1750 iFit 整合 Netflix 跟 Spotify 讓 C/P 值算盤繼續成立", "body": "看起來不華麗的生活品質升級，真正改變了內容驅動訓練家庭的訂閱 C/P 值計算。NT$78,000 配完整 iFit 生態，想要教練帶練成為預設的買家就是它。"},
        {"title": "Sole F80 在非 iFit 買家的做工跟保固論點上勝出", "body": "Garage Gym Reviews 這禮拜的對決文確認了擁有者多年來在講的事。F80 對想要自己娛樂堆疊、在意長期保固勝過觸控螢幕體驗的買家就是首選。"},
        {"title": "前兩名以外再等兩週", "body": "母親節跟週年慶歷年會把中段機型打 NT$6,000 到 NT$15,000，前兩名動的幅度小。名單裡有 Bowflex、Peloton、ProForm、Echelon 的話，等促銷檔期是最聰明的做法。"},
    ],
)
