import sys; sys.path.insert(0, "/Users/etrexkuo/toprankland/scripts")
from daily_helper import load, save, upsert, last_rankings, DATE

def do(name, refs, en, zh, rankings=None):
    d, p = load(name)
    entry = {
        "date": DATE,
        "rankings": rankings if rankings is not None else last_rankings(d),
        "references": refs,
        "i18n": {"en": en, "zh-tw": zh},
    }
    upsert(d, entry)
    save(p, d)
    print("updated", name)

# ---------------- best-robot-vacuums ----------------
do("best-robot-vacuums.json",
   [
     {"title": "Best (June 2026) Robot Vacuums", "url": "https://vacuumwars.com/best-monthly-2026-robot-vacuums/", "source": "Vacuum Wars"},
     {"title": "Ecovacs Deebot T90 Pro Omni Robot Vacuum Review", "url": "https://vacuumwars.com/ecovacs-deebot-t90-pro-omni-review/", "source": "Vacuum Wars"},
     {"title": "Ecovacs Deebot T90 Pro Omni Review: Mid-Range Mop King", "url": "https://www.bestrobovacuums.com/reviews/ecovacs-deebot-t90-pro-omni-review", "source": "Best Robovacuums"},
   ],
   {
     "commentary": "The big story in robot vacuums this June is the roller-mop takeover, and I want to be clear about what it does and does not change at the top. The new wave of roller-mop systems, led by the Ecovacs Deebot T90 Pro Omni that premiered at CES 2026 and the Eufy Omni C28, is genuinely better at lifting dried stains than the spinning-pad designs most robots still use, and that is reshaping the value tier fast. The T90 Pro Omni in particular has become the mid-range mop king and a deserved new value pick everywhere I look. That said, my number one does not move. The Dreame X60 Max Ultra Complete at 1,699.99 dollars still wins the overall crown because nothing beats its balance of 35,000 Pa suction, a slim 3.13-inch retractable-LiDAR body that actually clears low furniture, and the most complete dock and mopping package on the market. Roborock Saros 10R holds second as the navigation and thin-profile specialist, and the Dreame L50 Ultra stays third as the smartest value-to-performance buy in the lineup. The roller-mop momentum matters most below the podium, where Ecovacs and Eufy keep getting stronger, so I am holding ranks this week and letting the commentary flag the trend. If you are shopping the value tier, watch the roller-mop models closely. If you want the single best robot regardless of price, the X60 Max Ultra is still the answer.",
     "highlights": [
       {"title": "Dreame X60 Max Ultra is still the overall best", "body": "At 1,699.99 dollars it pairs 35,000 Pa suction with a slim 3.13-inch retractable-LiDAR body and the most complete dock package on the market. No rival matches that all-around balance, so it keeps number one."},
       {"title": "Roller-mop systems are reshaping the value tier", "body": "The CES 2026 Ecovacs Deebot T90 Pro Omni and the Eufy Omni C28 lift dried stains far better than spinning pads. That advantage is winning value categories and is the trend to watch this season."},
       {"title": "Roborock Saros 10R owns navigation", "body": "Its mapping and ultra-thin profile keep it the specialist for homes full of furniture legs and tight gaps. That precision holds it a clear second behind the Dreame."},
       {"title": "Dreame L50 Ultra is the smart-money pick", "body": "It delivers near-flagship cleaning and mopping at a price that undercuts the top two. For buyers who want most of the X60 experience for less, it stays the third-place value champion."},
     ],
   },
   {
     "commentary": "這個月掃地機器人最大的新聞，就是滾筒拖布全面崛起，我想把它對榜首到底有沒有影響講清楚。這一波滾筒拖布系統，由 CES 2026 亮相的 Ecovacs Deebot T90 Pro Omni 跟 Eufy Omni C28 領軍，清乾掉的污漬確實比多數機器還在用的旋轉拖盤強很多，這正在快速重塑性價比這一段。尤其 T90 Pro Omni 已經變成中階拖地王，我到處看到它被選為新的高性價比首選，實至名歸。話雖如此，我的第一名沒有動。Dreame X60 Max Ultra Complete 售價約台幣五萬出頭，整體冠軍還是它，因為沒有對手能贏過它那套平衡，35,000 Pa 吸力、3.13 吋薄機身配可伸縮 LiDAR 真的鑽得進低矮家具底下，加上市面上最完整的基座跟拖地配套。Roborock Saros 10R 守第二，是導航跟薄身專家，Dreame L50 Ultra 守第三，是整個陣容裡性價比最聰明的買法。滾筒拖布的氣勢主要影響的是頒獎台以下，Ecovacs 跟 Eufy 一直在變強，所以這週我守住排名，讓內文幫你標記趨勢。你如果在挑性價比這段，盯緊滾筒拖布機型。你如果不管預算就要最強那一台，答案還是 X60 Max Ultra。",
     "highlights": [
       {"title": "Dreame X60 Max Ultra 整體還是最強", "body": "售價約台幣五萬出頭，35,000 Pa 吸力配 3.13 吋薄身可伸縮 LiDAR，加上市面最完整的基座配套。沒有對手能在全面平衡上追上它，所以第一還是它。"},
       {"title": "滾筒拖布正在重塑性價比段", "body": "CES 2026 的 Ecovacs Deebot T90 Pro Omni 跟 Eufy Omni C28 清乾污漬遠勝旋轉拖盤。這個優勢正在拿下性價比類別獎，是本季要盯的趨勢。"},
       {"title": "Roborock Saros 10R 主宰導航", "body": "建圖能力跟超薄機身，讓它在桌椅腳多、縫隙窄的家裡是專家。這份精準守住它穩穩的第二，緊跟在 Dreame 後面。"},
       {"title": "Dreame L50 Ultra 是聰明錢之選", "body": "它用低於前兩名的價格，給你接近旗艦的清掃跟拖地。想用少一點錢拿到大部分 X60 體驗的人，它穩坐第三名性價比冠軍。"},
     ],
   })

# ---------------- best-cordless-vacuums ----------------
do("best-cordless-vacuums.json",
   [
     {"title": "Shark PowerDetect Cordless vs Dyson Gen5detect", "url": "https://www.techradar.com/home/vacuums/dyson-gen5detect-vs-shark-powerdetect-cordless-vacuum", "source": "TechRadar"},
     {"title": "Top 10 Best Cordless Vacuums of 2026", "url": "https://vacuumwars.com/vacuum-wars-best-cordless-vacuums/", "source": "Vacuum Wars"},
   ],
   {
     "commentary": "Heading into June 2026 my cordless ranking still leads with the Shark PowerDetect Clean & Empty, and the latest head-to-head testing only reinforces why. Against the mighty Dyson Gen5detect, the Shark is more maneuverable, better at cleaning edges and chunky spills, and its self-emptying base is a genuine effort-saver for allergy sufferers. It even picks up hair faster through high-pile carpet. Add a price that meaningfully undercuts Dyson and you get the best blend of performance and value on the board, which is exactly what a top pick should be. The Dyson Gen5detect holds second and remains the raw performance king: it beat almost every competitor in nearly every test, with the strongest suction, the best filtration and the most thoughtful toolset, including a bonus soft cleaner head that hard-floor homes will love. If money is no object and you want the absolute best cleaner, this is it. The Dyson V15 Detect stays third as the proven all-rounder, and the Tineco Pure One A90S holds fourth on the strength of long runtime and smart iLoop dust sensing. Samsung Bespoke Jet AI, the V12 Detect Slim, LG CordZero A9, Levoit LVAC-200 and the value-focused KARDV V06 all carry forward unchanged. Nothing this week reshuffled the order, so I held ranks and let the Shark-versus-Dyson value split frame the top two.",
     "highlights": [
       {"title": "Shark PowerDetect wins on value and versatility", "body": "Latest testing has it beating the Dyson Gen5detect on edges, chunky spills and high-pile hair pickup, with a self-empty base and a much lower price. That blend of performance and value keeps it number one."},
       {"title": "Dyson Gen5detect is the performance king", "body": "It topped almost every test with the strongest suction, best filtration and smartest toolset, plus a bonus soft head for hard floors. When budget is no object, it is the best cleaner, a deserved second."},
       {"title": "Dyson V15 Detect remains the safe all-rounder", "body": "Proven suction, laser dust detection and reliable filtration keep it the dependable middle choice. For buyers who want a trusted Dyson without the Gen5 price, it holds a solid third."},
       {"title": "Tineco Pure One A90S leads on runtime", "body": "Long battery life paired with iLoop smart dust sensing makes it the pick for big homes that need one charge to finish. That endurance keeps it firmly in fourth."},
     ],
   },
   {
     "commentary": "2026 年 6 月，我的無線吸塵器排名還是由 Shark PowerDetect Clean & Empty 領軍，最新的對決測試只是讓理由更紮實。對上猛獸 Dyson Gen5detect，Shark 更靈活、清邊角跟大塊掉屑更行，自動集塵基座對過敏的人是真的省事，在長毛地毯上抓頭髮甚至更快。再加上價格明顯比 Dyson 親民，你拿到的就是榜上性價比最好的組合，這正是首選該有的樣子。Dyson Gen5detect 守第二，純效能還是王者，它幾乎每項測試都贏過所有對手，吸力最強、過濾最好、配件設計最用心，還附一顆軟質地板刷頭，硬地板的家會很愛。如果預算無上限、就要最強，那就是它。Dyson V15 Detect 守第三，是身經百戰的全能型，Tineco Pure One A90S 守第四，靠長續航跟 iLoop 智慧偵塵。Samsung Bespoke Jet AI、V12 Detect Slim、LG CordZero A9、Levoit LVAC-200 跟主打性價比的 KARDV V06 全部照舊。這週沒事件洗牌，所以我守住排名，讓 Shark 對 Dyson 的性價比分界去框前兩名。",
     "highlights": [
       {"title": "Shark PowerDetect 贏在性價比與全能", "body": "最新測試裡它在邊角、大塊掉屑、長毛地毯抓髮都贏過 Dyson Gen5detect，還有自動集塵基座跟低很多的價格。這份效能加性價比讓它穩坐第一。"},
       {"title": "Dyson Gen5detect 是效能王", "body": "它幾乎每項測試都奪冠，吸力最強、過濾最好、配件最聰明，還附硬地板軟刷頭。預算無上限時它就是最強清潔機，第二實至名歸。"},
       {"title": "Dyson V15 Detect 仍是穩妥全能", "body": "成熟吸力、雷射偵塵、可靠過濾，讓它是可信賴的中間選擇。想要信得過的 Dyson 又不想花 Gen5 的錢，它穩穩第三。"},
       {"title": "Tineco Pure One A90S 續航最強", "body": "長電池續航配 iLoop 智慧偵塵，讓它成為大坪數、要一次充電掃完的首選。這份耐力守住它的第四。"},
     ],
   })

# ---------------- best-air-purifiers ----------------
do("best-air-purifiers.json",
   [
     {"title": "8 Best Air Purifiers of 2026, Tested by Our Experts", "url": "https://www.consumerreports.org/appliances/air-purifiers/best-air-purifiers-of-the-year-a1197763201/", "source": "Consumer Reports"},
     {"title": "Best Air Purifiers 2026: 95 Models Objectively Tested", "url": "https://moderncastle.com/air-purifiers/best-air-purifier/", "source": "Modern Castle"},
   ],
   {
     "commentary": "Going into June 2026 my air-purifier ranking still rewards filtration depth above all, and the IQAir HealthPro Plus keeps number one because nothing matches it on the metric that matters most. Its medical-grade HyperHEPA pulls PM2.5 down to 0.1 microns and PM10 to 0.2 with no measurable ozone, and the three-stage activated-carbon-plus-HEPA system is simple and devastatingly effective. It is expensive and that is the only honest knock, but for anyone with asthma, allergies or a real air-quality problem, it is the one I tell them to buy. The Coway Airmega 400S holds a strong second as the best balance of clean-air delivery, quiet operation and value, the purifier I recommend to the most people because it does almost everything the IQAir does for far less. The Blueair HealthProtect 7470i stays third on the strength of the quietest operation in the group and continuous HEPASilent protection. Rabbit Air MinusA3 holds fourth as the wall-mountable design pick. The Coway Airmega ProX deserves a mention this month: recent large-room testing has it outperforming the 1,400-dollar IQAir Atem X and topping leaderboards for big residential spaces, which is exactly why it sits fifth and rising in my notes. The Atem Earth, Levoit Core 600S and Vital 200S, and the Alen BreatheSmart 45i all carry forward unchanged. No launch this week justified a reshuffle, so I held ranks and let filtration quality lead the verdicts.",
     "highlights": [
       {"title": "IQAir HealthPro Plus owns filtration", "body": "Its HyperHEPA captures particles down to 0.1 microns with no measurable ozone, the deepest filtration on the board. For asthma, allergies or a genuine air problem, it is the one I recommend, so it stays number one."},
       {"title": "Coway Airmega 400S is the best all-around buy", "body": "It pairs strong clean-air delivery with quiet running and real value, doing nearly everything the IQAir does for far less. That balance makes it the purifier I recommend to the most people, a clear second."},
       {"title": "Coway Airmega ProX is the large-room champion", "body": "Recent testing has it beating the 1,400-dollar IQAir Atem X and topping leaderboards for big residential spaces. That muscle in large rooms keeps it climbing and holds fifth this month."},
       {"title": "Blueair HealthProtect 7470i is the quiet pick", "body": "The quietest in the group with continuous HEPASilent protection, it is the choice for bedrooms and offices where noise matters most. That hush keeps it a deserved third."},
     ],
   },
   {
     "commentary": "2026 年 6 月，我的空氣清淨機排名還是把過濾深度擺第一，IQAir HealthPro Plus 守住榜首，因為在最關鍵的那個指標上沒有對手追得上。它的醫療級 HyperHEPA 能把 PM2.5 降到 0.1 微米、PM10 降到 0.2，臭氧低到測不出來，三段式活性碳加 HEPA 簡單又狠準。它貴，這是唯一誠實要講的缺點，但你如果有氣喘、過敏或真的空品問題，我就是叫你買它。Coway Airmega 400S 守住強勢第二，是潔淨空氣輸出、安靜運轉跟性價比最好的平衡，也是我推薦給最多人的那台，因為它用便宜很多的價格幾乎做到 IQAir 的一切。Blueair HealthProtect 7470i 守第三，靠的是這群裡最安靜的運轉跟持續的 HEPASilent 防護。Rabbit Air MinusA3 守第四，是可壁掛的設計之選。Coway Airmega ProX 這個月值得一提，最近的大坪數測試裡，它贏過要價約台幣四萬的 IQAir Atem X，在大住宅空間的排行榜居首，這正是它在我筆記裡排第五又持續往上的原因。Atem Earth、Levoit Core 600S 跟 Vital 200S，還有 Alen BreatheSmart 45i 全部照舊。這週沒有發布值得洗牌，所以我守住排名，讓過濾品質帶判斷。",
     "highlights": [
       {"title": "IQAir HealthPro Plus 主宰過濾", "body": "HyperHEPA 能抓到 0.1 微米的微粒、臭氧測不出來，是榜上最深的過濾。氣喘、過敏或真有空品問題，我就推它，所以第一是它。"},
       {"title": "Coway Airmega 400S 是最佳全能買法", "body": "潔淨空氣輸出、安靜運轉加上真性價比，用便宜很多的價格幾乎做到 IQAir 的一切。這份平衡讓它是我推薦給最多人的那台，穩穩第二。"},
       {"title": "Coway Airmega ProX 是大坪數冠軍", "body": "最近測試裡它贏過約台幣四萬的 IQAir Atem X，在大住宅空間排行榜居首。這份大空間實力讓它持續往上，本月守第五。"},
       {"title": "Blueair HealthProtect 7470i 是安靜之選", "body": "這群裡最安靜，又有持續的 HEPASilent 防護，是臥室跟辦公室最在意噪音時的選擇。這份安靜守住它應得的第三。"},
     ],
   })

# ---------------- best-portable-air-conditioners ----------------
do("best-portable-air-conditioners.json",
   [
     {"title": "The 4 Best Portable Air Conditioners of 2026", "url": "https://www.rtings.com/air-conditioner/reviews/best/portable", "source": "RTINGS"},
     {"title": "4 Of The Best Portable Air Conditioners In 2026", "url": "https://www.slashgear.com/2183453/best-portable-air-conditioners-in-2026/", "source": "SlashGear"},
   ],
   {
     "commentary": "With summer heat arriving, my portable-AC ranking holds firm, and the Midea Duo MAP14HS1TBL stays at number one for the clearest reason in the category: it cools faster and to lower temperatures than anything else on the market. It tops Forbes' 2026 list on the strength of greater seasonally adjusted cooling capacity than any rival portable unit, and its inverter compressor keeps noise down to a remarkable 42 to 49 dB while sipping energy. The hoseless-feeling Duo design also dodges the single-hose efficiency penalty that drags down cheaper units. When someone wants the best portable AC and is willing to pay for it, this is my answer. The Whynter NEX ARC-1230WN holds second and is genuinely the unit RTINGS rates highest overall, praised for strong cooling, easy setup and low noise, and it lands at better value than the Midea, so for many buyers it is the smarter spend. The LG LP1419IVSM Dual Inverter stays third as the quiet premium pick the New York Times keeps recommending for its low-volume operation and premium build. The Hisense HAP0824TWD, Whynter Elite ARC-122DS, DeLonghi Pinguino Arctic Whisper, Black+Decker BPACT14WT, KoolSiln 14,000 BTU and Frigidaire FHPC102AC1 all carry forward unchanged. No new launch this week moved the order, so I held ranks and let cooling power and efficiency lead the verdicts.",
     "highlights": [
       {"title": "Midea Duo is the cooling and efficiency leader", "body": "It cools faster and lower than any rival with greater seasonally adjusted capacity, an inverter compressor and a quiet 42 to 49 dB. That combination of power and efficiency keeps it number one."},
       {"title": "Whynter NEX ARC-1230WN is the value champion", "body": "RTINGS rates it the best portable AC tested for cooling, easy setup and low noise, and it costs less than the Midea. For most buyers that value makes it the smarter spend and a strong second."},
       {"title": "LG LP1419IVSM is the quiet premium pick", "body": "Its dual-inverter design delivers low-volume operation and premium build that keeps earning New York Times recommendations. For buyers who prize quiet above all, it holds a deserved third."},
       {"title": "Hisense HAP0824TWD balances efficiency and price", "body": "Strong energy efficiency and quiet running at a friendlier price make it the smart mid-tier choice. That balance keeps it solidly in fourth for value-minded shoppers."},
     ],
   },
   {
     "commentary": "夏天熱浪報到，我的移動式冷氣排名站得很穩，Midea Duo MAP14HS1TBL 守住第一，理由在這個類別最清楚，它冷得比市面上任何機器都快、能壓到更低的溫度。它登上 Forbes 2026 榜首，靠的是比所有對手移動機種都高的季節調整製冷量，變頻壓縮機又把噪音壓到驚人的 42 到 49 分貝，還很省電。它那套類似無管的 Duo 設計也避開了拖垮便宜機種的單管效率懲罰。有人要最強移動冷氣又願意花錢，我的答案就是它。Whynter NEX ARC-1230WN 守第二，平心而論是 RTINGS 整體評分最高的那台，製冷強、安裝簡單、噪音低，價格又比 Midea 更實惠，所以對很多人來說這是更聰明的花法。LG LP1419IVSM Dual Inverter 守第三，是安靜的高階之選，紐約時報一直推薦它的低噪運轉跟質感做工。Hisense HAP0824TWD、Whynter Elite ARC-122DS、DeLonghi Pinguino Arctic Whisper、Black+Decker BPACT14WT、KoolSiln 14,000 BTU 跟 Frigidaire FHPC102AC1 全部照舊。這週沒新發布動排名，所以我守住，讓製冷力跟效率帶判斷。",
     "highlights": [
       {"title": "Midea Duo 是製冷與效率領頭羊", "body": "它冷得比任何對手快、壓得更低，季節調整製冷量最高，變頻壓縮機又安靜在 42 到 49 分貝。這份力量加效率讓它穩坐第一。"},
       {"title": "Whynter NEX ARC-1230WN 是性價比冠軍", "body": "RTINGS 評它是測過最好的移動冷氣，製冷、安裝、低噪都強，價格還比 Midea 低。對多數人這份性價比是更聰明的花法，穩穩第二。"},
       {"title": "LG LP1419IVSM 是安靜的高階之選", "body": "雙變頻設計帶來低噪運轉跟質感做工，一直拿到紐約時報推薦。最看重安靜的人，它守住應得的第三。"},
       {"title": "Hisense HAP0824TWD 平衡效率與價格", "body": "強能效加安靜運轉，價格又更親民，讓它是聰明的中階選擇。這份平衡守住它在重性價比買家心中的第四。"},
     ],
   })

# ---------------- best-smart-thermostats ----------------
do("best-smart-thermostats.json",
   [
     {"title": "Google Nest Learning Thermostat 4th gen vs Ecobee Premium", "url": "https://www.tomsguide.com/home/smart-home/google-nest-learning-thermostat-4th-gen-vs-ecobee-premium-how-they-compare", "source": "Tom's Guide"},
     {"title": "Ecobee vs Nest Thermostat (2026): Which Is Right for You?", "url": "https://www.smarthomeexplorer.com/guides/ecobee-vs-nest-thermostat-2026", "source": "Smart Home Explorer"},
   ],
   {
     "commentary": "Going into June 2026 my smart-thermostat ranking still puts the Ecobee Smart Thermostat Premium at number one, and the latest head-to-head with the Nest only confirms it. Both sell for 249 dollars, but Ecobee wins seven of twelve direct categories, and the reasons are practical: an included room sensor for true multi-room comfort, built-in air-quality monitoring, a built-in smart speaker, and compatibility with every major ecosystem including Alexa, Google, Siri and HomeKit with no subscription required. For the widest range of homes it is simply the most capable box you can buy. The Google Nest Learning Thermostat 4th gen holds a very close second and remains the most beautiful and most automated option: its OLED display with Farsight and self-learning algorithm dial in a schedule within seven to ten days with zero manual input. If you live in Google Home and want hands-free scheduling, it is the better pick, and the gap is small. The Honeywell Home T9 stays third on the strength of best-in-class multi-room sensor coverage. The Eve Thermostat holds fourth as the HomeKit-native Matter choice, and the Aqara W200 fifth for Thread and broad ecosystem support. Emerson Sensi Touch 2, Ecobee Enhanced, Nest 2020, Honeywell T6 Pro and the budget Amazon Smart Thermostat all carry forward unchanged. No launch this week reshuffled the order, so I held ranks and let the Ecobee-versus-Nest split frame the top two.",
     "highlights": [
       {"title": "Ecobee Premium wins on capability", "body": "It takes seven of twelve head-to-head categories with an included room sensor, air-quality monitoring, a built-in speaker and no-subscription support for every ecosystem. That breadth keeps it number one."},
       {"title": "Nest 4th gen owns automation and design", "body": "Its OLED Farsight display and self-learning algorithm dial in a schedule in seven to ten days with no manual input. For Google Home households wanting hands-free comfort, it is a very close second."},
       {"title": "Honeywell Home T9 leads on multi-room", "body": "Its sensor coverage is the best in class for balancing temperature across many rooms. For larger or multi-zone homes that need even comfort everywhere, it holds a deserved third."},
       {"title": "Eve Thermostat is the HomeKit purist's pick", "body": "Native HomeKit with Matter and Thread support makes it the cleanest choice for an Apple-centric smart home. That focus keeps it solidly in fourth."},
     ],
   },
   {
     "commentary": "2026 年 6 月，我的智慧溫控器排名還是把 Ecobee Smart Thermostat Premium 放第一，最新跟 Nest 的對決只是再次確認。兩台都賣約台幣七千五，但 Ecobee 在十二項直接對比贏了七項，理由都很實在，內附房間感測器做到真正的多房舒適、內建空品監測、內建智慧喇叭，還相容所有主流生態系，Alexa、Google、Siri、HomeKit 全包又不用訂閱。論能涵蓋最多種家庭，它就是你買得到最全能的那一台。Google Nest Learning Thermostat 4th gen 守住非常貼近的第二，依然是最漂亮、最自動化的選擇，OLED 螢幕配 Farsight 跟自學演算法，七到十天就把排程調到位、完全不用手動。你如果整個家都在 Google Home 又想要免動手排程，它是更好的選擇，而且差距很小。Honeywell Home T9 守第三，靠的是同級最強的多房感測覆蓋。Eve Thermostat 守第四，是 HomeKit 原生的 Matter 之選，Aqara W200 第五，主打 Thread 跟廣泛生態系支援。Emerson Sensi Touch 2、Ecobee Enhanced、Nest 2020、Honeywell T6 Pro 跟入門的 Amazon Smart Thermostat 全部照舊。這週沒發布洗牌，所以我守住，讓 Ecobee 對 Nest 的分界去框前兩名。",
     "highlights": [
       {"title": "Ecobee Premium 贏在全能", "body": "它在十二項對比拿下七項，內附房間感測器、空品監測、內建喇叭，又免訂閱支援所有生態系。這份廣度讓它穩坐第一。"},
       {"title": "Nest 4th gen 主宰自動化與設計", "body": "OLED Farsight 螢幕配自學演算法，七到十天就把排程調好、不用手動。整個家在 Google Home、想要免動手舒適的人，它是非常貼近的第二。"},
       {"title": "Honeywell Home T9 多房最強", "body": "它的感測覆蓋是同級最佳，能把溫度平均分到很多房間。較大或多區的家想要處處舒適，它守住應得的第三。"},
       {"title": "Eve Thermostat 是 HomeKit 純粹派之選", "body": "原生 HomeKit 加 Matter 跟 Thread 支援，是 Apple 為主智慧家庭最乾淨的選擇。這份專注守住它穩穩的第四。"},
     ],
   })

# ---------------- best-robotic-pool-cleaners ----------------
do("best-robotic-pool-cleaners.json",
   [
     {"title": "Best Robotic Pool Cleaners of 2026. Over 30+ Tested & Reviewed", "url": "https://www.thepoolnerd.com/best-robotic-pool-cleaners", "source": "The Pool Nerd"},
     {"title": "Best Robotic Pool Cleaners 2026: Top Picks by Pool Type", "url": "https://beatbot.com/blogs/robotic-pool-cleaner/best-robotic-pool-cleaners-2026", "source": "Beatbot"},
   ],
   {
     "commentary": "As pool season opens, my ranking holds a stance some buyers find surprising: corded still wins overall, and the Dolphin Premier stays at number one. After 30-plus models tested, the reason is consistency. The Premier pairs commercial-grade twin motors, Multi-Media filtration with a Media-Alert full-bin indicator, and the kind of long-term reliability that has made roughly nine in ten owners who ask for a recommendation end up happier with a corded Dolphin. It just cleans, every cycle, for years. The Beatbot AquaSense 2 Ultra holds a strong second as the best cordless robot money can buy: AI mapping, surface skimming and the longest runtime in any cordless pool cleaner, with a 13,400 mAh battery good for up to five hours of floor cleaning. The honest caveat is real though. Cordless means daily maintenance, fishing a heavy robot out, emptying the filter and recharging, and at around 3,000 dollars it could not keep pace with corded Dolphins at a fraction of the price in head-to-head testing. That trade-off is exactly why it sits second. The Dolphin Nautilus CC Plus Wi-Fi stays third as the value workhorse, and the Aiper Scuba S1 fourth as the best-value cordless. Beatbot AquaSense 2 Pro, Wybot C2 Vision, Polaris 9650iQ Sport, Pentair Prowler 930W, Dolphin Active 30, Aiper Scuba SE and Wybot C1 all carry forward unchanged. No launch this week moved the order, so I held ranks.",
     "highlights": [
       {"title": "Dolphin Premier is the overall best", "body": "Commercial twin motors, Multi-Media filtration and Media-Alert reliability make roughly nine in ten owners happier with a corded Dolphin. It cleans flawlessly every cycle for years, so it keeps number one."},
       {"title": "Beatbot AquaSense 2 Ultra is the best cordless", "body": "AI mapping, surface skimming and a 13,400 mAh battery good for up to five hours give it the longest runtime of any cordless robot. For wire-free convenience it is the clear second."},
       {"title": "Cordless convenience has a real cost", "body": "Cordless means daily maintenance and a 3,000-dollar price that still could not match corded Dolphins in testing. I keep the verdict honest so the ranking matches how these robots actually perform."},
       {"title": "Dolphin Nautilus CC Plus is the value workhorse", "body": "It delivers reliable corded cleaning and Wi-Fi control at a far friendlier price than the Premier. For most residential pools that want dependable value, it holds a strong third."},
     ],
   },
   {
     "commentary": "泳池季開跑，我的排名守住一個有些買家會意外的立場，有線整體還是贏，Dolphin Premier 守住第一。測過三十幾台之後，理由是穩定。Premier 配的是商用級雙馬達、Multi-Media 過濾加 Media-Alert 集塵滿格指示，還有那種長期可靠度，這也是為什麼大約十個來問推薦的池主裡，有九個最後是用有線 Dolphin 用得更開心。它就是每一輪都把池子掃乾淨，一掃好幾年。Beatbot AquaSense 2 Ultra 守住強勢第二，是錢買得到最好的無線機，AI 建圖、水面撇沫，還有所有無線池底機裡最長的續航，13,400 mAh 電池能撐到五小時池底清掃。但誠實的但書是真的。無線代表每天要維護，把沉重的機器撈出來、清濾網、再充電，而且在約台幣九萬的價位，對決測試裡它跟不上價格只有零頭的有線 Dolphin。這個取捨正是它排第二的原因。Dolphin Nautilus CC Plus Wi-Fi 守第三，是性價比主力，Aiper Scuba S1 守第四，是最划算的無線機。Beatbot AquaSense 2 Pro、Wybot C2 Vision、Polaris 9650iQ Sport、Pentair Prowler 930W、Dolphin Active 30、Aiper Scuba SE 跟 Wybot C1 全部照舊。這週沒發布動排名，所以我守住。",
     "highlights": [
       {"title": "Dolphin Premier 是整體最強", "body": "商用雙馬達、Multi-Media 過濾跟 Media-Alert 可靠度，讓大約十個池主有九個用有線 Dolphin 更開心。每輪都掃得乾淨、撐好幾年，所以第一是它。"},
       {"title": "Beatbot AquaSense 2 Ultra 是最強無線", "body": "AI 建圖、水面撇沫，加上 13,400 mAh 電池撐到五小時，是所有無線機裡續航最長的。要無線的便利，它是明確的第二。"},
       {"title": "無線的便利是有代價的", "body": "無線代表每天維護，加上約台幣九萬的價格在測試裡還是追不上有線 Dolphin。我把判斷講白，讓排名對得上這些機器真實的表現。"},
       {"title": "Dolphin Nautilus CC Plus 是性價比主力", "body": "它用比 Premier 親民很多的價格，給你可靠的有線清掃跟 Wi-Fi 控制。多數住宅泳池想要可靠又划算，它守住強勢第三。"},
     ],
   })

# ---------------- best-robot-lawn-mowers ----------------
do("best-robot-lawn-mowers.json",
   [
     {"title": "Best Robot Lawn Mower 2026", "url": "https://us.mammotion.com/blogs/news/best-robot-lawn-mower-2026", "source": "Mammotion"},
     {"title": "9 Best Robot Lawn Mowers of 2026", "url": "https://www.reviewed.com/home-outdoors/best-right-now/best-robot-lawn-mowers", "source": "Reviewed"},
   ],
   {
     "commentary": "Mowing season is in full swing and my ranking holds firm, with the Mammotion LUBA 3 AWD 5000 keeping number one. It earned a CES 2026 Innovation Award on the strength of the world's first Tri-Fusion positioning system, combining 360-degree LiDAR, NetRTK satellite correction and dual-camera AI vision, and that hybrid approach is exactly why it dominates. All-wheel drive lets it climb slopes and chew through terrain that stops every rival, and for big or complicated yards it is simply the most capable robot mower made. The ECOVACS GOAT A3000 LiDAR Pro holds second as the automation leader, with its HoloScope 360 dual-LiDAR navigation cutting setup to under a minute and handling edge trimming that reduces manual work. The standard GOAT A3000 LiDAR stays third and the A2000 LiDAR Pro fourth, giving ECOVACS a deep, value-graded run of wire-free LiDAR mowers that suit most suburban lawns beautifully. The Segway Navimow X315 holds fifth as the coverage specialist, and the drop-and-go Navimow i2 LiDAR sixth as the easiest first-time setup for flatter yards. Husqvarna Automower 450X EPOS, Worx Landroid Vision M600, Yarbo Lawn Mower Pro, EcoFlow BLADE and the compact Mammotion YUKA Mini 700H all carry forward unchanged. No new launch this week reshuffled the order, so I held ranks and let terrain and navigation lead the verdicts.",
     "highlights": [
       {"title": "Mammotion LUBA 3 AWD is the terrain king", "body": "Its CES 2026 award-winning Tri-Fusion system fuses LiDAR, NetRTK and dual-camera vision, and all-wheel drive climbs slopes that stop rivals. For big or complex yards it is the most capable mower made, so it stays number one."},
       {"title": "ECOVACS GOAT A3000 LiDAR Pro leads automation", "body": "HoloScope 360 dual-LiDAR cuts setup to under a minute and automates edge trimming that others leave to you. That hands-off polish keeps it a clear second."},
       {"title": "ECOVACS owns the value-graded middle", "body": "The A3000 LiDAR and A2000 LiDAR Pro give a deep, price-laddered run of wire-free LiDAR mowers that fit most suburban lawns. That lineup depth holds third and fourth comfortably."},
       {"title": "Navimow i2 LiDAR is the easiest setup", "body": "Its drop-and-go convenience needs no wires, antennas or complex calibration, ideal for flatter yards and first-time buyers. That simplicity keeps it a worthy sixth."},
     ],
   },
   {
     "commentary": "除草季全面開打，我的排名站得很穩，Mammotion LUBA 3 AWD 5000 守住第一。它拿下 CES 2026 創新獎，靠的是全球首創的 Tri-Fusion 定位系統，結合 360 度 LiDAR、NetRTK 衛星校正跟雙鏡頭 AI 視覺，這套混合方案正是它稱霸的原因。四輪驅動讓它爬上所有對手都會卡住的斜坡跟地形，論大坪數或複雜庭院，它就是做得出來最強的割草機器人。ECOVACS GOAT A3000 LiDAR Pro 守第二，是自動化領頭羊，HoloScope 360 雙 LiDAR 導航把安裝壓到一分鐘內，邊緣修剪也能自動處理、省下人工。標準版 GOAT A3000 LiDAR 守第三，A2000 LiDAR Pro 守第四，讓 ECOVACS 有一整排價格分級的無線 LiDAR 割草機，很適合多數市郊草坪。Segway Navimow X315 守第五，是覆蓋專家，drop-and-go 的 Navimow i2 LiDAR 守第六，是平坦庭院最容易上手的首次安裝。Husqvarna Automower 450X EPOS、Worx Landroid Vision M600、Yarbo Lawn Mower Pro、EcoFlow BLADE 跟小巧的 Mammotion YUKA Mini 700H 全部照舊。這週沒新發布洗牌，所以我守住，讓地形跟導航帶判斷。",
     "highlights": [
       {"title": "Mammotion LUBA 3 AWD 是地形之王", "body": "它拿 CES 2026 大獎的 Tri-Fusion 系統融合 LiDAR、NetRTK 跟雙鏡頭視覺，四輪驅動爬上對手會卡的斜坡。大或複雜的庭院它最強，所以第一是它。"},
       {"title": "ECOVACS GOAT A3000 LiDAR Pro 自動化最強", "body": "HoloScope 360 雙 LiDAR 把安裝壓到一分鐘內，還自動修剪別人留給你做的邊緣。這份免動手的細膩守住它明確的第二。"},
       {"title": "ECOVACS 主宰價格分級的中段", "body": "A3000 LiDAR 跟 A2000 LiDAR Pro 給出一整排價格階梯的無線 LiDAR 割草機，適合多數市郊草坪。這份陣容深度穩穩守住第三第四。"},
       {"title": "Navimow i2 LiDAR 最好安裝", "body": "drop-and-go 的便利不用拉線、不用天線、不用複雜校正，平坦庭院跟首購族最適合。這份簡單守住它值得的第六。"},
     ],
   })

# ---------------- best-treadmills ----------------
do("best-treadmills.json",
   [
     {"title": "NordicTrack Commercial 1750 Vs. Sole F80 (2026)", "url": "https://barbend.com/nordictrack-commercial-1750-vs-sole-f80/", "source": "BarBend"},
     {"title": "NordicTrack 1750 Review (2026): Our Expert's In-Depth Tests", "url": "https://www.treadmillreviews.net/nordictrack-commercial-1750/", "source": "Treadmill Reviews"},
   ],
   {
     "commentary": "Heading into June 2026 my treadmill ranking holds, and the NordicTrack Commercial 1750 stays at number one as the best all-around home treadmill you can buy. A strong 4.25 CHP motor, a roomy 22-by-60-inch deck, decline as well as incline training, and deep iFIT integration make it the rare machine that satisfies serious runners and class-takers alike. For the widest range of households it does the most things well, which is exactly what a top pick should do. The NordicTrack X24 Incline Trainer holds second for anyone whose focus is steep incline and hill work, where its extended range outclasses standard treadmills. The Sole F80 stays a close third and is the one I recommend for buyers who prize build over screens: a rock-solid frame, an industry-leading warranty, cushioning Sole claims cuts joint impact up to 40 percent, and the freedom to stream Netflix or your own apps with no required subscription. If you want durability and bring-your-own entertainment, this is the smart pick. The Bowflex Treadmill 22 holds fourth as the JRNY-driven tech alternative, and the Peloton Tread fifth for class addicts. ProForm Carbon Pro 9000, Echelon Stride-6, Life Fitness T3, Horizon 7.0 AT and the Aviron Victory all carry forward unchanged. No launch this week reshuffled the order, so I held ranks and let all-around versatility lead the verdicts.",
     "highlights": [
       {"title": "NordicTrack Commercial 1750 is the best all-rounder", "body": "A 4.25 CHP motor, 22-by-60-inch deck, decline and incline training, and deep iFIT make it satisfy runners and class-takers alike. It does the most things well, so it stays number one."},
       {"title": "NordicTrack X24 owns incline training", "body": "Its extended incline range outclasses standard treadmills for serious hill and climb work. For buyers whose whole focus is incline, it holds a deserved second."},
       {"title": "Sole F80 wins on build and freedom", "body": "A rock-solid frame, industry-leading warranty, up-to-40-percent impact cushioning and subscription-free streaming make it the durability pick. For bring-your-own-entertainment buyers it is a close third."},
       {"title": "Bowflex Treadmill 22 is the tech alternative", "body": "Its large screen and JRNY platform give an engaging guided experience without locking into iFIT. For households in the Bowflex ecosystem it holds a solid fourth."},
     ],
   },
   {
     "commentary": "2026 年 6 月，我的跑步機排名守住，NordicTrack Commercial 1750 守住第一，是你買得到最全能的家用跑步機。強悍的 4.25 CHP 馬達、寬敞的 22 乘 60 吋跑帶、能下坡也能上坡訓練，加上深度 iFIT 整合，讓它是少見能同時滿足認真跑者跟上課派的機器。論能涵蓋最多種家庭，它把最多事情都做得好，這正是首選該做到的。NordicTrack X24 Incline Trainer 守第二，給那些主攻陡坡跟爬坡訓練的人，它的延伸坡度範圍勝過一般跑步機。Sole F80 守住貼近的第三，是我推薦給重做工勝過螢幕那群人的選擇，堅固機架、業界最強保固、Sole 宣稱可減少關節衝擊達四成的避震，還能自由串流 Netflix 或自己的 App、不用強制訂閱。想要耐用加自帶娛樂，它是聰明之選。Bowflex Treadmill 22 守第四，是 JRNY 驅動的科技替代方案，Peloton Tread 守第五，給課程成癮者。ProForm Carbon Pro 9000、Echelon Stride-6、Life Fitness T3、Horizon 7.0 AT 跟 Aviron Victory 全部照舊。這週沒發布洗牌，所以我守住，讓全能多功能帶判斷。",
     "highlights": [
       {"title": "NordicTrack Commercial 1750 是最強全能", "body": "4.25 CHP 馬達、22 乘 60 吋跑帶、能上坡下坡，加上深度 iFIT，同時滿足跑者跟上課派。它把最多事情都做得好，所以第一是它。"},
       {"title": "NordicTrack X24 主宰坡度訓練", "body": "它延伸的坡度範圍在認真爬坡訓練上勝過一般跑步機。整個重點就在坡度的買家，它守住應得的第二。"},
       {"title": "Sole F80 贏在做工與自由", "body": "堅固機架、業界最強保固、最高減四成衝擊的避震，加上免訂閱串流，讓它是耐用之選。自帶娛樂的買家，它是貼近的第三。"},
       {"title": "Bowflex Treadmill 22 是科技替代方案", "body": "大螢幕配 JRNY 平台，給你投入感十足的引導體驗，又不用綁死在 iFIT。在 Bowflex 生態系裡的家庭，它守住穩穩的第四。"},
     ],
   })

print("ALL DONE")
