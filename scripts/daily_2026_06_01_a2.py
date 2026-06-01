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


ENTRIES = {}

# ============================================================ 4K TVs
ENTRIES["best-4k-tvs.json"] = {
    "references": [
        {"title": "The 6 Best TVs of 2026", "url": "https://www.rtings.com/tv/reviews/best/tvs-on-the-market", "source": "RTINGS"},
        {"title": "Best OLED TVs in 2026 tested: Our top picks from LG, Samsung and more", "url": "https://www.tomsguide.com/tvs/oled-tvs/best-oled-tvs", "source": "Tom's Guide"},
        {"title": "Samsung S95H QD-OLED TV Review - Not Just a Pretty Frame", "url": "https://www.avsforum.com/threads/samsung-s95h-qd-oled-tv-review-not-just-a-pretty-frame.3343251/", "source": "AVS Forum"},
    ],
    "en": {
        "commentary": "I keep the LG C6 at the top this week, and the newest market move only reinforces that call. Samsung shipped the S95H in April with a QD-OLED panel rated around 2,700 nits in a 10 percent window, up from roughly 2,000 nits on the S95F, yet it arrived at a higher price and the gains do not translate into a meaningfully better picture in a normal living room. That is exactly why I still steer people to the S95F at rank two and keep the C6 in front. The C6 runs LG's Alpha 11 Gen 3 processor on the proven OLED EX panel, and the upscaling, shadow detail, and overall richness now justify its position over the brighter Samsung sets. The S95F remains the most complete TV you can actually buy, with elite gaming, the cleanest motion, and QD-OLED color, and at its current street price it is the smarter purchase than the S95H. Sony's Bravia 8 II holds third on the strength of its tone mapping and built-in audio, which still beat almost everything in this group for movie nights. Further down, the value tier is doing real work. The TCL QM8K and Hisense U8N deliver mini-LED brightness that embarrasses their price tags, and I would happily put either in a bright room where OLED struggles. My buying advice this week is simple. Buy the C6 if you want the best overall package, grab the S95F if you want maximum punch and gaming features, and skip the S95H until its price drops to where the small brightness bump makes sense. Panel prices are climbing across the board because of memory and component costs, so locking in a current-generation OLED now looks smart.",
        "highlights": [
            {"title": "S95H launches but does not unseat the S95F", "body": "Samsung's April S95H pushes peak brightness to about 2,700 nits in a 10 percent window, but the higher price means the S95F stays the better buy and keeps rank two."},
            {"title": "LG C6 earns the crown", "body": "The Alpha 11 Gen 3 processor on the OLED EX panel sharpens upscaling and shadow detail, giving the C6 the most balanced performance for the money."},
            {"title": "Bravia 8 II owns movie night", "body": "Sony's tone mapping and acoustic surface audio still set the bar for cinematic accuracy, holding third in a crowded OLED field."},
            {"title": "Value mini-LEDs punch up", "body": "The TCL QM8K and Hisense U8N bring brightness that suits sunlit rooms, making them my picks when budget and ambient light are the priority."},
            {"title": "Lock in OLED before prices climb", "body": "Memory and component costs are pushing panel prices up, so a current-gen OLED bought today looks like the value play."},
        ],
    },
    "zh-tw": {
        "commentary": "這週我還是把 LG C6 放在第一，而且最新的市場動態反而更證明這個判斷沒錯。Samsung 四月推出 S95H，QD-OLED 面板在 10% 視窗的峰值亮度衝到大約 2,700 nits，比 S95F 的大約 2,000 nits 高，但價格也跟著上去，實際擺在客廳看，那點亮度差幾乎感受不出來。講白了，這就是我繼續推 S95F 排第二、把 C6 放最前面的原因。C6 用 LG 的 Alpha 11 Gen 3 處理器搭配成熟的 OLED EX 面板，升頻、暗部細節跟整體層次都明顯進步，坐穩龍頭位置我覺得很合理。S95F 還是目前你真的買得到最全面的電視，遊戲體驗頂、動態最乾淨、QD-OLED 發色漂亮，以現在的通路價來看，它比 S95H 划算太多。Sony Bravia 8 II 守住第三，靠的是色調對應跟內建音效，在這群裡看電影的調性還是最舒服。往下看，性價比這一段很有戲。TCL QM8K 跟 Hisense U8N 的 mini-LED 亮度，以那個價位來說根本佛心，家裡採光好、開窗會反光的客廳，我會直接推這兩台。這週的建議很單純，想要最全面就買 C6，想要最猛跟最強遊戲功能就上 S95F，S95H 先觀望，等降到那點亮度加成划算再說。現在面板因為記憶體跟零件成本一路漲，趁這代 OLED 還在合理價先入手，我覺得是聰明做法。台灣這邊 C6 65 吋大概落在 NT$60,000 上下，會是甜蜜點。",
        "highlights": [
            {"title": "S95H 上市但動不了 S95F", "body": "Samsung 四月的 S95H 把峰值亮度推到約 2,700 nits，但價格更高，S95F 依然是比較划算的選擇，穩坐第二。"},
            {"title": "LG C6 拿下第一", "body": "Alpha 11 Gen 3 處理器搭 OLED EX 面板，升頻跟暗部細節都更銳利，C6 在同價位給出最均衡的表現。"},
            {"title": "Bravia 8 II 是看電影神器", "body": "Sony 的色調對應跟聲學表面音效還是標竿，在這群 OLED 裡看片調性最對味，守住第三。"},
            {"title": "性價比 mini-LED 很猛", "body": "TCL QM8K 跟 Hisense U8N 亮度夠強，採光好的客廳我會直接推，預算有限又怕反光就選這兩台。"},
            {"title": "趁漲價前先卡位 OLED", "body": "記憶體跟零件成本把面板價格往上推，現在入手這代 OLED 反而是划算的時間點。"},
        ],
    },
}

# ============================================================ AI voice generators
ENTRIES["best-ai-voice-generators.json"] = {
    "references": [
        {"title": "Realtime TTS-2: A new frontier voice model", "url": "https://inworld.ai/blog/realtime-tts-2", "source": "Inworld AI"},
        {"title": "ElevenLabs Review 2026: The Most Realistic AI Voice Generator?", "url": "https://ucstrategies.com/news/elevenlabs-review-2026-the-most-realistic-ai-voice-generator/", "source": "UC Strategies"},
        {"title": "Best Text-to-Speech AI 2026: Top picks & In-depth reviews", "url": "https://aimlapi.com/blog/best-text-to-speech-ai", "source": "AI/ML API"},
    ],
    "en": {
        "commentary": "Inworld and ElevenLabs are sharing the top of my chart again this week, and both earned it for different reasons. Inworld's TTS-1.5 Max still sits at the top of the Artificial Analysis Speech Arena with an ELO around 1236, winning blind tests for naturalness and conversational flow, and its sub-250ms P90 latency on Max is what real-time agents actually need. The bigger story is that Inworld just previewed Realtime TTS-2, a model built specifically for live conversation. It hears the full audio of an exchange, picks up the user's tone and pacing, and takes voice direction in plain English the way you would prompt an LLM, all while holding one voice identity across more than 100 languages. That is a genuine step toward voice agents that feel like people, and it is why Inworld keeps the number one slot. ElevenLabs stays right beside it because nothing beats it for creator tooling and cloning fidelity. Eleven v3 now covers 70-plus languages, adds inline Audio Tags for emotional direction, and cuts errors on complex text by about 68 percent versus v2, which is exactly what audiobook and video producers want. On price, Inworld is the disruptor at roughly 5 dollars per million characters against ElevenLabs at 30 to 60, so budget-driven teams have an easy answer. I am holding the rest of the order steady. Hume's Octave 2 keeps third for its emotional range, MiniMax and Cartesia stay strong for multilingual and ultra-low latency work, and OpenAI's gpt-4o-mini-tts remains the value pick for developers already in that ecosystem. The takeaway this week is that real-time conversational quality has become the battleground, and Inworld is setting the pace.",
        "highlights": [
            {"title": "Inworld previews Realtime TTS-2", "body": "The new model listens to full-exchange audio, reads tone and pacing, and takes plain-English voice direction while holding one identity across 100-plus languages."},
            {"title": "TTS-1.5 Max still leads blind tests", "body": "Inworld holds the top Speech Arena ELO near 1236 with sub-250ms P90 latency, the combination real-time agents actually need."},
            {"title": "ElevenLabs v3 owns creator work", "body": "Eleven v3 covers 70-plus languages, adds inline Audio Tags for emotion, and cuts complex-text errors by about 68 percent over v2."},
            {"title": "Price gap is dramatic", "body": "Inworld runs near 5 dollars per million characters against 30 to 60 on ElevenLabs, giving budget-driven teams a clear default."},
            {"title": "Order below the top stays steady", "body": "Hume Octave 2 keeps its emotional-range edge at third, with MiniMax, Cartesia, and OpenAI holding their specialist roles."},
        ],
    },
    "zh-tw": {
        "commentary": "這週榜首一樣是 Inworld 跟 ElevenLabs 並列，兩家各有各的本事，都坐得很穩。Inworld 的 TTS-1.5 Max 還是穩居 Artificial Analysis Speech Arena 第一，ELO 大概落在 1236，盲測在自然度跟對話流暢度上都贏，Max 版 P90 延遲壓在 250ms 以內，這正是即時語音代理真正需要的東西。更值得講的是 Inworld 剛預告了 Realtime TTS-2，這款是專門為即時對話設計的。它會聽完整段對話的音訊，抓你的語氣跟節奏，還能像下 prompt 給 LLM 那樣，用白話英文去指揮聲音的演繹，而且同一個聲音身分可以橫跨超過 100 種語言。這已經是朝著「聽起來像真人」的語音代理邁出真正一步，Inworld 守第一我覺得實至名歸。ElevenLabs 緊貼在旁邊，創作者工具跟複製音色的擬真度目前還是無人能敵。Eleven v3 現在支援 70 多種語言，加了 inline Audio Tags 可以做情緒指揮，複雜文字的錯誤率比 v2 降了大約 68%，這正中有聲書跟影片製作者的需求。價格上 Inworld 是攪局者，每百萬字元大概 5 美元，ElevenLabs 要 30 到 60，預算吃緊的團隊答案很明顯。後段我維持不動，Hume Octave 2 靠情緒表現守第三，MiniMax 跟 Cartesia 在多語言跟超低延遲還是很猛，OpenAI 的 gpt-4o-mini-tts 對已經在那生態的開發者來說還是性價比首選。這週的重點很清楚，戰場已經轉到即時對話品質，而 Inworld 正在帶風向。",
        "highlights": [
            {"title": "Inworld 預告 Realtime TTS-2", "body": "新模型會聽完整段對話、讀語氣跟節奏，還能用白話英文指揮聲音演繹，同一聲音身分橫跨 100 多種語言。"},
            {"title": "TTS-1.5 Max 盲測仍領先", "body": "Inworld 在 Speech Arena 拿下約 1236 的最高 ELO，P90 延遲壓在 250ms 以內，這組合正是即時代理要的。"},
            {"title": "ElevenLabs v3 稱霸創作端", "body": "Eleven v3 支援 70 多種語言，加入 Audio Tags 做情緒指揮，複雜文字錯誤率比 v2 降約 68%。"},
            {"title": "價差非常明顯", "body": "Inworld 每百萬字元約 5 美元，ElevenLabs 要 30 到 60，預算導向的團隊有了很清楚的預設選擇。"},
            {"title": "前段以下維持不動", "body": "Hume Octave 2 靠情緒表現守第三，MiniMax、Cartesia、OpenAI 各自守住專長定位。"},
        ],
    },
}

# ============================================================ Electric bikes
ENTRIES["best-electric-bikes.json"] = {
    "references": [
        {"title": "Here are the best electric bikes you can buy at every price level in May 2026", "url": "https://electrek.co/2026/05/03/here-are-the-best-electric-bikes-you-can-buy-at-every-price-level/", "source": "Electrek"},
        {"title": "Aventon Level.3 Review: A Massive Level Up for Commuting", "url": "https://electricbikereport.com/aventon-level-3-review/", "source": "Electric Bike Report"},
        {"title": "Lectric XP4 Review: Tested & Rated", "url": "https://www.outdoorgearlab.com/reviews/biking/electric-bike/lectric-xp4", "source": "OutdoorGearLab"},
    ],
    "en": {
        "commentary": "The Aventon Level 3 stays my number one commuter this week, and the reviews keep validating it. The integrated Aventon Control Unit gives you 4G connectivity, GPS tracking, remote motor lockout, and geofencing, a security suite that is genuinely unheard of at this price. Testers also beat Aventon's claimed 70-mile range, logging one of the longest commuter distances they have recorded, so the range number is real, not marketing. That combination of smart security and proven endurance is why it holds the top spot over flashier bikes. The Lectric XP4 750 keeps second as the value champion, and it earns it. It folds into a car trunk, carries a passenger, and packs more power and range than many full-size bikes for the money. The XP4 replaced the XP 3.0, which was the best-selling e-bike in the US, and it is clearly built to inherit that crown. If your budget is tight and you want maximum bang per dollar, this is the bike I point people to first. Velotric's Discover 3 holds third for riders who prioritize comfort and a polished ride feel, and the Segway Xyber and Aventon Aventure 3 round out the upper group for those who want extra power or fat-tire stability. Lower down, the Trek Verve Plus 4S is the premium comfort pick if money is no object, while the Tenways and Lectric XP Lite 2 cover the lightweight and ultra-budget ends. My guidance is steady this week. The Level 3 is the all-rounder to beat, and the XP4 is the smart-money play.",
        "highlights": [
            {"title": "Aventon Level 3 leads on smart security", "body": "The Aventon Control Unit adds 4G tracking, remote motor lockout, and geofencing, a security suite nearly unheard of at this price."},
            {"title": "Real range beats the spec", "body": "Testers exceeded Aventon's claimed 70 miles and logged one of the longest commuter ranges they have recorded, confirming the endurance is real."},
            {"title": "Lectric XP4 is the value champ", "body": "It folds into a trunk, carries a passenger, and packs more power and range than many full-size bikes, inheriting the best-seller crown from the XP 3.0."},
            {"title": "Comfort tier holds at third", "body": "Velotric's Discover 3 stays my pick for riders who want a smooth, polished ride over raw spec-sheet numbers."},
            {"title": "Buying advice stays simple", "body": "The Level 3 is the all-rounder to beat, and the XP4 750 is the smart-money choice for tight budgets."},
        ],
    },
    "zh-tw": {
        "commentary": "這週通勤電動車我還是把 Aventon Level 3 放第一，評測一直在幫它背書。內建的 Aventon Control Unit 給你 4G 連線、GPS 定位、遠端鎖馬達還有電子圍籬，這套防盜配置以這個價位來說真的很扯。實測還跑贏 Aventon 宣稱的 70 英里續航，創下評測單位記錄到最長的通勤里程之一，所以那個續航數字是真的，不是行銷話術。智慧防盜加上實打實的續航，這就是它能壓過那些看起來更炫的車款、守住榜首的原因。Lectric XP4 750 守第二，性價比之王當之無愧。它折一折就塞得進後車廂，還能載一個人，以這個價錢給的動力跟續航比很多全尺寸車還猛。XP4 接的是 XP 3.0 的棒子，那台是全美最暢銷的電動車，這台明顯就是衝著繼承王座來的。預算抓很緊、又想要每一塊錢都花在刀口上，我第一個就推這台。Velotric Discover 3 守第三，適合把舒適度跟順暢騎乘感擺第一的人，Segway Xyber 跟 Aventon Aventure 3 則撐起上半段，給想要更多動力或胖胎穩定性的人。再往下，Trek Verve Plus 4S 是預算無上限時的舒適首選，Tenways 跟 Lectric XP Lite 2 則包辦輕量跟超低預算這兩端。這週建議維持不變，Level 3 是最難打的全能車，XP4 是精打細算的聰明選擇。台灣這邊想找通勤車，這兩台的定位都很清楚。",
        "highlights": [
            {"title": "Aventon Level 3 靠智慧防盜領先", "body": "Aventon Control Unit 提供 4G 定位、遠端鎖馬達跟電子圍籬，這套防盜配置在這個價位幾乎找不到。"},
            {"title": "實測續航贏過規格", "body": "評測跑贏 Aventon 宣稱的 70 英里，創下記錄到最長的通勤里程之一，續航是真材實料。"},
            {"title": "Lectric XP4 是性價比之王", "body": "折疊塞後車廂、能載人，動力跟續航比很多全尺寸車還強，接下 XP 3.0 的暢銷棒子。"},
            {"title": "舒適段守第三", "body": "Velotric Discover 3 還是我推給重視順暢舒適騎乘、不那麼看規格表的人的選擇。"},
            {"title": "購買建議維持簡單", "body": "Level 3 是最難打的全能車，XP4 750 是預算吃緊時最精打細算的選擇。"},
        ],
    },
}

# ============================================================ Handheld gaming consoles
ENTRIES["best-handheld-gaming-consoles.json"] = {
    "references": [
        {"title": "Best gaming handhelds 2026 ranked: Steam Deck, Xbox Ally X, Switch 2, Legion Go 2, MSI Claw 8 AI+, and more", "url": "https://www.windowscentral.com/gaming-best-gaming-handhelds", "source": "Windows Central"},
        {"title": "The best gaming handhelds for 2026", "url": "https://tech.yahoo.com/gaming/article/the-best-gaming-handhelds-for-2026-180000267.html", "source": "Engadget"},
        {"title": "Which Gaming Handheld Should You Buy in 2026?", "url": "https://www.vice.com/en/article/which-gaming-handheld-should-you-buy-in-2026-price-power-and-battery-comparisons/", "source": "Vice"},
    ],
    "en": {
        "commentary": "Pricing turbulence is reshaping this category, and it is why I am holding my order steady rather than reacting. Valve raised the Steam Deck OLED price by 240 dollars in May, citing higher memory and storage costs, and Nintendo has confirmed a 50 dollar bump on the Switch 2 coming in September. The wider RAMageddon, the AI-driven spike in memory prices, is hitting every maker at once. Even with the increase, the Steam Deck OLED keeps my top spot. Its 7.4-inch HDR OLED at up to 90Hz still produces the bright color and deep blacks that define the handheld experience, and SteamOS remains the most polished portable platform with the deepest verified library. The Switch 2 holds second and is simply the best way to play Nintendo games in 2026, with its 7.9-inch 1080p 120Hz LCD, 256GB of storage, and 4K docked output via a custom Nvidia chip. If you can buy before September, do it and save the 50 dollars. The ROG Xbox Ally X stays third as the performance pick. Its Ryzen Z2 Extreme, 24GB of RAM, and fast 1TB SSD chew through demanding games that bring the Switch 2 and Steam Deck to their knees, and it wins by default if you want serious horsepower without a near-1,000-dollar Legion Go 2. Below that, the Legion Go 2 and MSI Claw 8 AI+ hold their spots for spec chasers, and the SteamOS Legion Go S remains a strong value entry. My advice this week is timing-driven. If you want a handheld, the smart move is to buy before the next round of price hikes lands.",
        "highlights": [
            {"title": "Steam Deck OLED holds despite a 240-dollar hike", "body": "Valve raised the price in May on memory and storage costs, but the 90Hz HDR OLED screen and the deepest verified library keep it number one."},
            {"title": "Switch 2 faces a September price bump", "body": "Nintendo confirmed a 50-dollar increase coming in September, so buying the 1080p 120Hz handheld now saves money."},
            {"title": "ROG Xbox Ally X is the power pick", "body": "The Ryzen Z2 Extreme, 24GB of RAM, and 1TB SSD handle demanding games that strain the Switch 2 and Steam Deck."},
            {"title": "RAMageddon is squeezing everyone", "body": "The AI-driven spike in memory prices is pushing costs up across every maker, making timing the key buying factor."},
            {"title": "Buy before the next hike", "body": "With prices climbing across the board, the smart move this week is to lock in a handheld before the next increase lands."},
        ],
    },
    "zh-tw": {
        "commentary": "價格亂流正在重塑這個品類，這也是我這週選擇維持排名、而不是急著反應的原因。Valve 五月把 Steam Deck OLED 漲了 240 美元，理由是記憶體跟儲存成本上升，而 Nintendo 也確認 Switch 2 九月要漲 50 美元。背後是更大範圍的 RAMageddon，也就是 AI 帶動的記憶體價格暴漲，這波每家廠商一起中招。就算漲了，Steam Deck OLED 還是守住我的第一。它那塊 7.4 吋、最高 90Hz 的 HDR OLED 依然能給出定義掌機體驗的鮮豔發色跟深邃黑位，SteamOS 仍是最成熟的掌機平台，認證遊戲庫也最深。Switch 2 守第二，2026 年要玩任天堂遊戲它就是最佳途徑，7.9 吋 1080p 120Hz LCD、256GB 儲存、靠客製 Nvidia 晶片還能 4K 接電視輸出。能在九月前入手就趕快，省那 50 美元。ROG Xbox Ally X 守第三，是效能首選。Ryzen Z2 Extreme、24GB RAM 加上快速 1TB SSD，那些把 Switch 2 跟 Steam Deck 逼到極限的大作它都吃得下，想要真正馬力又不想花近千美元上 Legion Go 2，它幾乎是預設答案。再往下，Legion Go 2 跟 MSI Claw 8 AI+ 守住規格控的位置，SteamOS 版 Legion Go S 仍是很強的性價比入門款。這週的建議跟時機綁在一起，想買掌機，聰明的做法就是趕在下一波漲價落地前先卡位。台灣水貨價也會跟著國際行情走，動作要快。",
        "highlights": [
            {"title": "Steam Deck OLED 漲 240 美元仍守第一", "body": "Valve 五月因記憶體跟儲存成本漲價，但 90Hz HDR OLED 螢幕加上最深的認證遊戲庫讓它穩坐第一。"},
            {"title": "Switch 2 九月要漲價", "body": "Nintendo 確認九月漲 50 美元，現在買這台 1080p 120Hz 掌機能省一筆。"},
            {"title": "ROG Xbox Ally X 是效能首選", "body": "Ryzen Z2 Extreme、24GB RAM 跟 1TB SSD，能扛起把 Switch 2 跟 Steam Deck 逼到極限的大作。"},
            {"title": "RAMageddon 壓著每家廠商", "body": "AI 帶動的記憶體價格暴漲讓所有廠商成本上揚，買進時機成了關鍵。"},
            {"title": "趕在下一波漲價前買", "body": "價格全面走高，這週聰明的做法就是趁下一輪漲價落地前先把掌機入手。"},
        ],
    },
}

# ============================================================ Pickleball paddles
ENTRIES["best-pickleball-paddles.json"] = {
    "references": [
        {"title": "Best Pro Pickleball Paddles 2026", "url": "https://www.pickleheads.com/pickleball-gear/pro-pickleball-paddles", "source": "Pickleheads"},
        {"title": "JOOLA Perseus Pro V Pickleball Paddle", "url": "https://joola.com/products/joola-perseus-pro-v-pickleball-paddle-1", "source": "JOOLA"},
        {"title": "Top 10 Pickleball Paddles in 2026: Find Your Perfect Match", "url": "https://www.dupr.com/post/top-10-pickleball-paddles-in-2026-find-your-perfect-match", "source": "DUPR"},
    ],
    "en": {
        "commentary": "The JOOLA Perseus line stays my benchmark this week, and the newer Pro V release explains why I keep the Perseus Pro IV 16mm at number one. JOOLA's patent-pending KineticFrame, built into the throat, flexes to store momentum and release it on contact, the same kick-point idea used in hockey sticks and golf clubs, and it makes power feel genuinely effortless while spin stays top-tier. The Pro V refines that further with rounded top corners and an elongated profile that keeps the sweet spot centered while extending reach, and it costs 300 dollars. The key thing JOOLA finally got right is control. The new lineup delivers the same explosive power and spin but is far more controllable, which is why these paddles back more pros than anything else and why the Perseus holds the crown. It is USAP and UPA-A approved, so it is tournament-legal out of the box. Right behind it, the Honolulu J2CR keeps second as my value-meets-performance pick, balancing power and control with a wide sweet spot at a friendlier price. The Bread and Butter Loco hybrid holds third for players who want premium feel without the top-tier sticker. Further down, the Selkirk Labs Project Boomstik stays the raw-power specialist, the CRBN 1X leads on spin, and budget standouts like the Six Zero Double Black Diamond and Vatic Pro Prism Flash prove you do not need to spend 300 dollars to compete. My advice is steady. Buy the Perseus if you want the most refined power paddle in the game, and look to the Honolulu or a Vatic if value matters more than the badge.",
        "highlights": [
            {"title": "KineticFrame makes power effortless", "body": "JOOLA's throat-mounted frame flexes and recovers on contact like a hockey stick, delivering explosive drives while spin stays top-tier."},
            {"title": "Pro V refines control", "body": "Rounded top corners and an elongated profile center the sweet spot and extend reach, and the new lineup is far more controllable at 300 dollars."},
            {"title": "Perseus is tournament-legal", "body": "The paddle is USAP and UPA-A approved and backs more pros than anything else, which keeps it at number one."},
            {"title": "Honolulu J2CR is the value play", "body": "It balances power and control with a wide sweet spot at a friendlier price, holding second as my value-meets-performance pick."},
            {"title": "Budget paddles still compete", "body": "The Six Zero Double Black Diamond and Vatic Pro Prism Flash prove you can play seriously without spending 300 dollars."},
        ],
    },
    "zh-tw": {
        "commentary": "這週 JOOLA Perseus 系列還是我的標竿，而較新的 Pro V 也解釋了我為什麼把 Perseus Pro IV 16mm 放第一。JOOLA 那個正在申請專利的 KineticFrame 設計在拍頸，接觸瞬間會彎曲儲存動能再釋放，就是冰球桿跟高爾夫球桿用的 kick-point 概念，打起來力量真的來得很輕鬆，旋轉也維持頂尖水準。Pro V 再進一步優化，拍頭做圓角加上拉長的版型，把甜蜜點維持在中央同時延伸觸及範圍，售價 300 美元。JOOLA 這次終於搞懂的關鍵是控球。新一代一樣有爆發力跟旋轉，但好控太多，這也是為什麼背書這系列的職業選手比任何拍子都多，Perseus 穩坐王座。它通過 USAP 跟 UPA-A 認證，開箱就能打比賽。緊跟在後的 Honolulu J2CR 守第二，是我心中性價比兼顧性能的選擇，力量跟控球平衡、甜蜜點大，價格也親民。Bread and Butter Loco 混合款守第三，適合想要高階手感又不想付頂規價格的人。再往下，Selkirk Labs Project Boomstik 還是純爆發力的專家，CRBN 1X 旋轉領先，平價代表像 Six Zero Double Black Diamond 跟 Vatic Pro Prism Flash 則證明，不用花到 300 美元也能打得有競爭力。我的建議維持不變，想要場上最精緻的力量拍就買 Perseus，比較看重 CP 值而非品牌光環，就看 Honolulu 或 Vatic。台灣的話 Perseus 大概要 NT$9,000 以上，預算有限選 Vatic 我覺得很實在。",
        "highlights": [
            {"title": "KineticFrame 讓力量來得輕鬆", "body": "JOOLA 拍頸的框架接觸時會彎曲回彈，像冰球桿一樣，抽球爆發力十足，旋轉也維持頂尖。"},
            {"title": "Pro V 強化控球", "body": "拍頭圓角加拉長版型把甜蜜點維持在中央並延伸觸及，新一代在 300 美元價位好控太多。"},
            {"title": "Perseus 可直接打比賽", "body": "通過 USAP 跟 UPA-A 認證，背書的職業選手比任何拍子都多，穩坐第一。"},
            {"title": "Honolulu J2CR 是性價比之選", "body": "力量跟控球平衡、甜蜜點大、價格親民，守住第二，是兼顧性能的 CP 值選擇。"},
            {"title": "平價拍照樣有競爭力", "body": "Six Zero Double Black Diamond 跟 Vatic Pro Prism Flash 證明不用花到 300 美元也能認真打。"},
        ],
    },
}

# ============================================================ Robot vacuums
ENTRIES["best-robot-vacuums.json"] = {
    "references": [
        {"title": "Roborock Saros 20 vs Dreame X60 Max Ultra: Which 2026 Flagship Wins?", "url": "https://www.bestrobovacuums.com/comparisons/roborock-saros-20-vs-dreame-x60-max-ultra", "source": "Best Robovacuums"},
        {"title": "Best (May 2026) Robot Vacuums", "url": "https://vacuumwars.com/best-may-2026-robot-vacuums/", "source": "Vacuum Wars"},
        {"title": "I've seen most of 2026's new robot vacuums and these are the 2 models I can't wait to try", "url": "https://www.techradar.com/home/robot-vacuums/ive-seen-most-of-2026s-new-robot-vacuums-and-these-are-the-2-models-i-cant-wait-to-try", "source": "TechRadar"},
    ],
    "en": {
        "commentary": "The Dreame X60 Max Ultra stays my number one this week, and the latest testing keeps backing it. It holds a Vacuum Wars score of 4.11 and still delivers the most consistent all-around performance in the category. The slim 3.13-inch retractable-LiDAR body climbs 51mm thresholds, pushes 35,000Pa of suction, and scored 89 percent on carpet deep-clean and a perfect 100 percent on flattened pet-hair pickup in testing. At roughly 1,499 to 1,699 dollars it also delivers more cleaning performance per dollar than its closest rival, which is exactly why it keeps the crown. The big news is the Roborock Saros 20, the successor to the hugely popular Saros 10R. It keeps everything people loved about the 10R and adds an improved AdaptiLift system that climbs even taller thresholds, plus Matter support and Roborock's polished app. At around 1,599 dollars it justifies the premium if you specifically need maximum threshold crossing or the best app experience. I am keeping the Saros 10R at number two for now since the Saros 20 is still rolling out, but anyone shopping the top tier should put the 20 on their radar. The Dreame L50 Ultra holds third as the value flagship, pairing excellent mopping with a friendlier price. Roborock's Saros Z70 keeps its spot for the robotic arm novelty, and the Qrevo CurvX stays a strong mid-premium all-rounder. My guidance is consistent. The X60 Max Ultra is the best overall buy, and the Saros 20 is the one to watch if threshold climbing and Matter matter most to you.",
        "highlights": [
            {"title": "Dreame X60 Max Ultra stays on top", "body": "A 4.11 Vacuum Wars score, 35,000Pa suction, 51mm threshold climbing, and a perfect pet-hair pickup score keep it the best overall."},
            {"title": "Roborock Saros 20 arrives", "body": "The Saros 10R successor adds an improved AdaptiLift system for taller thresholds, plus Matter support and Roborock's polished app."},
            {"title": "Value still favors Dreame", "body": "At roughly 1,499 dollars the X60 Max Ultra delivers more cleaning per dollar than the 1,599-dollar Saros 20."},
            {"title": "Saros 20 justifies its premium for climbers", "body": "If you specifically need maximum threshold crossing, Matter, or the best app, the Saros 20 earns its higher price."},
            {"title": "Value flagship holds at third", "body": "The Dreame L50 Ultra pairs excellent mopping with a friendlier price, staying my pick for buyers who want flagship cleaning for less."},
        ],
    },
    "zh-tw": {
        "commentary": "這週掃地機器人我還是把 Dreame X60 Max Ultra 放第一，最新的測試一直在幫它撐腰。它在 Vacuum Wars 拿到 4.11 分，整體表現依然是這個品類裡最穩定的。機身薄到 3.13 吋、用可伸縮 LiDAR，能爬 51mm 門檻，吸力衝到 35,000Pa，測試裡地毯深層清潔拿 89%，壓平寵物毛清除更是滿分 100%。售價大約 1,499 到 1,699 美元，每一塊錢換到的清潔力也比最接近的對手高，這正是它守住王座的原因。最大的新聞是 Roborock Saros 20，超人氣 Saros 10R 的接班人。它保留了 10R 大家喜歡的一切，再加上升級的 AdaptiLift 系統，能爬更高的門檻，還支援 Matter，搭配 Roborock 那套打磨得很好的 App。大約 1,599 美元，如果你特別需要最強的越障能力或最好的 App 體驗，這個溢價就值得。我暫時把 Saros 10R 留在第二，因為 Saros 20 還在鋪貨，但要買高階機種的人都該把 20 放進雷達。Dreame L50 Ultra 守第三，是性價比旗艦，拖地很強、價格又比較親民。Roborock Saros Z70 靠機械手臂的新奇感守位，Qrevo CurvX 則是中高階很全面的選擇。我的建議一致，X60 Max Ultra 是整體最值得買的，Saros 20 則是越障跟 Matter 對你最重要時要盯緊的那台。台灣這邊旗艦機普遍落在 NT$40,000 以上，預算夠就直接上 X60。",
        "highlights": [
            {"title": "Dreame X60 Max Ultra 穩坐第一", "body": "Vacuum Wars 4.11 分、35,000Pa 吸力、能爬 51mm 門檻，寵物毛清除滿分，整體最值得買。"},
            {"title": "Roborock Saros 20 登場", "body": "Saros 10R 接班人加上升級的 AdaptiLift 能爬更高門檻，還支援 Matter 跟打磨精良的 App。"},
            {"title": "性價比仍偏向 Dreame", "body": "大約 1,499 美元的 X60 Max Ultra，每塊錢換到的清潔力比 1,599 美元的 Saros 20 高。"},
            {"title": "Saros 20 對越障需求者值回票價", "body": "如果你特別需要最強越障、Matter 或最好的 App，Saros 20 的較高售價就站得住腳。"},
            {"title": "性價比旗艦守第三", "body": "Dreame L50 Ultra 拖地強、價格親民，是想用較少預算拿到旗艦清潔力的首選。"},
        ],
    },
}

# ============================================================ Smart watches
ENTRIES["best-smart-watches.json"] = {
    "references": [
        {"title": "Garmin Fenix 8 vs Apple Watch Ultra 3: here's which one I'd buy", "url": "https://www.techradar.com/health-fitness/smartwatches/garmin-fenix-8-vs-apple-watch-ultra-3-heres-which-one-id-buy-on-black-friday", "source": "TechRadar"},
        {"title": "I just ran a marathon with the Apple Watch Ultra 3 vs. Garmin Fenix 8 Pro", "url": "https://www.tomsguide.com/wellness/smartwatches/i-just-ran-a-marathon-with-the-apple-watch-ultra-3-vs-garmin-fenix-8-pro-heres-the-winner", "source": "Tom's Guide"},
        {"title": "Garmin Fenix 8 vs. Apple Watch Ultra 3: Which is the better smartwatch?", "url": "https://tech.sportskeeda.com/wearables/garmin-fenix-8-vs-apple-watch-ultra-3-which-better-smartwatch", "source": "Sportskeeda"},
    ],
    "en": {
        "commentary": "I am moving the Apple Watch Ultra 3 to the top this week, and the latest head-to-heads make the case. Across marathon testing and daily wear, the Ultra 3 delivers Apple's medical-grade heart alerts and sleep apnea detection, the kind of FDA-cleared health features Garmin still does not match. At 799 dollars it also undercuts the Fenix 8, which starts at 999, so the value math has shifted in Apple's favor for anyone living in the iPhone ecosystem. That combination of health depth, a brilliant display, and a sharper price is why it edges ahead. The Garmin Fenix 8 holds second and remains the choice for serious endurance athletes. Its standout battery life runs for weeks where the Ultra 3 measures in hours, it pairs with both iPhone and Android, and its training-readiness and endurance metrics tell you exactly when to push and when to rest. If multi-day expeditions or cross-platform freedom are your priority, the Fenix is still the watch. Samsung's Galaxy Watch 7 Ultra keeps third as the best Android-first flagship, with a bright display and a strong health stack for Samsung phone owners. Below the leaders, the Apple Series 11 and Series 10 remain the smart mainstream picks, the Garmin Forerunner 965 stays a runner's favorite, and the Pixel Watch 4 holds its value spot for Android users who want clean software. My advice this week is ecosystem-driven. Buy the Ultra 3 if you are on iPhone and want the best all-round health watch, and choose the Fenix 8 if battery life and cross-platform support outrank everything else.",
        "highlights": [
            {"title": "Apple Watch Ultra 3 takes the top spot", "body": "Medical-grade heart alerts, sleep apnea detection, and a 799-dollar price that undercuts the Fenix 8 push it ahead this week."},
            {"title": "Garmin Fenix 8 owns endurance", "body": "Battery life measured in weeks, iPhone and Android pairing, and training-readiness metrics keep it the athlete's choice at second."},
            {"title": "Price math favors Apple", "body": "At 799 dollars the Ultra 3 undercuts the Fenix 8's 999 starting price, shifting the value case for iPhone owners."},
            {"title": "Samsung leads the Android flagships", "body": "The Galaxy Watch 7 Ultra holds third with a bright display and strong health tracking for Samsung phone owners."},
            {"title": "Pick by ecosystem", "body": "Choose the Ultra 3 on iPhone for the best all-round health watch, or the Fenix 8 when battery and cross-platform support come first."},
        ],
    },
    "zh-tw": {
        "commentary": "這週我把 Apple Watch Ultra 3 移到第一，最新的對比評測幫我把這個判斷講清楚。不管是馬拉松實測還是日常配戴，Ultra 3 提供 Apple 醫療級的心律警示跟睡眠呼吸中止偵測，這類拿到 FDA 認證的健康功能 Garmin 到現在還追不上。售價 799 美元，也比起跳 999 美元的 Fenix 8 便宜，所以對活在 iPhone 生態裡的人來說，性價比的天平已經倒向 Apple。健康深度、漂亮螢幕加上更殺的價格，這組合就是它能往前一步的原因。Garmin Fenix 8 守第二，對認真的耐力運動員來說它還是首選。續航是招牌，Ultra 3 用小時算的時候它用週算，而且 iPhone 跟 Android 都能配對，訓練準備度跟耐力指標會明確告訴你什麼時候該衝、什麼時候該休。多日遠征或跨平台自由是你的重點，Fenix 還是那支錶。Samsung Galaxy Watch 7 Ultra 守第三，是 Android 陣營最強旗艦，螢幕亮、健康功能對 Samsung 手機用戶很完整。前段以下，Apple Series 11 跟 Series 10 還是主流聰明選擇，Garmin Forerunner 965 仍是跑者最愛，Pixel Watch 4 則守住想要乾淨軟體的 Android 用戶的性價比位置。這週建議跟生態系綁在一起，用 iPhone 又想要最全能的健康錶就買 Ultra 3，續航跟跨平台支援高於一切就選 Fenix 8。台灣 Ultra 3 大概 NT$28,900 起，以那套健康功能來看我覺得很值。",
        "highlights": [
            {"title": "Apple Watch Ultra 3 拿下第一", "body": "醫療級心律警示、睡眠呼吸中止偵測，加上 799 美元比 Fenix 8 便宜的價格，這週把它推上榜首。"},
            {"title": "Garmin Fenix 8 稱霸耐力", "body": "續航用週算、iPhone 跟 Android 都能配對、訓練準備度指標完整，守住運動員首選的第二。"},
            {"title": "價格天平偏向 Apple", "body": "Ultra 3 售價 799 美元，比 Fenix 8 的 999 起跳便宜，對 iPhone 用戶的性價比更有利。"},
            {"title": "Samsung 領銜 Android 旗艦", "body": "Galaxy Watch 7 Ultra 螢幕亮、健康功能完整，對 Samsung 手機用戶很有吸引力，守住第三。"},
            {"title": "依生態系挑選", "body": "用 iPhone 想要最全能健康錶就選 Ultra 3，續航跟跨平台優先就選 Fenix 8。"},
        ],
    },
}


def reorder(rankings, new_order_ids):
    by_id = {r["id"]: r for r in rankings}
    out = []
    for rank, rid in enumerate(new_order_ids, start=1):
        r = dict(by_id[rid])
        r["rank"] = rank
        out.append(r)
    # append any ids not listed, preserving their data
    for r in rankings:
        if r["id"] not in new_order_ids:
            out.append(dict(r))
    return out


def main():
    for name, payload in ENTRIES.items():
        data, p = load(name)
        rankings = [dict(r) for r in last_rankings(data)]

        # Smart watches: move Apple Ultra 3 to #1 (conservative reorder justified by news)
        if name == "best-smart-watches.json":
            ids = [r["id"] for r in rankings]
            new_order = ["apple-ultra3"] + [i for i in ids if i != "apple-ultra3"]
            rankings = reorder(rankings, new_order)

        entry = {
            "date": DATE,
            "rankings": rankings,
            "references": payload["references"],
            "i18n": {
                "en": {
                    "commentary": payload["en"]["commentary"],
                    "highlights": payload["en"]["highlights"],
                },
                "zh-tw": {
                    "commentary": payload["zh-tw"]["commentary"],
                    "highlights": payload["zh-tw"]["highlights"],
                },
            },
        }
        upsert(data, entry)
        save(p, data)
        print("updated", name)


if __name__ == "__main__":
    main()
