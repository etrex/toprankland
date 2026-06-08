import sys; sys.path.insert(0, "/Users/etrexkuo/toprankland/scripts")
from daily_helper import load, save, DATE

# prose replacements per file, applied recursively to today's entry strings
FIXES = {
    "best-ai-coding-assistants.json": [
        ("完整 fork VS Code，AI 是原生一等公民不是外掛，Composer", "完整 fork VS Code，AI 從骨子裡就是原生一等公民，Composer"),
        ("你不是二選一，你是看哪個給你施力點。", "你是看哪個給你施力點來搭配兩者。"),
        ("贏家組合是兩個工具不是一個", "贏家組合是兩個工具一起用"),
        ("The winning setup is two tools, not one", "The winning setup is two tools working together"),
        ("You do not pick one, you pick where each gives you leverage.", "You pick where each gives you leverage."),
        ("你不是二選一，你是照各自的施力點來搭配。", "你是照各自的施力點來搭配兩者。"),
    ],
    "best-ai-meeting-assistants.json": [
        ("，而不是當看得見的參與者加入通話，", "，全程不需要一隻機器人加入通話，"),
    ],
    "best-gaming-mice.json": [
        ("這不是行銷，是 LAN 賽事桌上手底下真的出現的東西。", "這是 LAN 賽事桌上手底下真的會出現的東西。"),
    ],
    "best-handheld-gaming-consoles.json": [
        ("因為掌機的問題從來不是純規格，是你真的能玩什麼，", "因為掌機真正的問題是你真的能玩什麼，"),
    ],
    "best-mechanical-keyboards.json": [
        ("是真的競技優勢，不是行銷。", "是真的競技優勢。"),
    ],
    "best-smart-glasses.json": [
        ("，用來看影音跟工作，不是日常 AI 助手。就這個", "，用來看影音跟工作。就這個"),
    ],
    "best-smart-thermostats.json": [
        ("智慧恆溫器的問題不再是值不值得，而是你偏好跟哪個介面一起生活。", "智慧恆溫器現在的問題是你偏好跟哪個介面一起生活。"),
    ],
    "best-smartphones.json": [
        ("我把它放第三是看整體均衡，不是它有什麼弱點。", "我把它放第三是看整體均衡。"),
        ("我放它第三是看整體均衡，不是它有弱點。", "我放它第三是看整體均衡。"),
    ],
}

DASHES = [" — ", " — ", " – ", " – ", "—", "—", "–"]


def fix_strings(o, repls):
    if isinstance(o, dict):
        return {k: fix_strings(v, repls) for k, v in o.items()}
    if isinstance(o, list):
        return [fix_strings(v, repls) for v in o]
    if isinstance(o, str):
        s = o
        for a, b in repls:
            s = s.replace(a, b)
        return s
    return o


def normalize_ref_dashes(refs):
    out = []
    for r in refs:
        t = r.get("title", "")
        for dsh in DASHES:
            t = t.replace(dsh, ": " if dsh.strip() else ": ")
        # collapse accidental double colons/spaces
        t = t.replace("::", ":").replace("  ", " ").strip()
        r = dict(r); r["title"] = t
        out.append(r)
    return out


import glob, os
for fp in sorted(glob.glob("/Users/etrexkuo/toprankland/src/content/rankings/*.json")):
    name = os.path.basename(fp)
    d, p = load(name)
    entry = [h for h in d["history"] if h["date"] == DATE][0]
    changed = False
    if name in FIXES:
        before = repr(entry["i18n"])
        entry["i18n"] = fix_strings(entry["i18n"], FIXES[name])
        if repr(entry["i18n"]) != before:
            changed = True
    if "references" in entry:
        newrefs = normalize_ref_dashes(entry["references"])
        if newrefs != entry["references"]:
            entry["references"] = newrefs; changed = True
    if changed:
        save(p, d)
        print("fixed", name)

print("stylefix done")
