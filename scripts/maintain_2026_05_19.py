#!/usr/bin/env python3
"""Maintain competitors data for VPN, gaming mice, smart watches — 2026-05-19."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RANKINGS = ROOT / "src" / "content" / "rankings"


def load(slug):
    return json.loads((RANKINGS / f"{slug}.json").read_text())


def save(slug, data):
    (RANKINGS / f"{slug}.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    )


def add_competitor(data, comp):
    if any(c["id"] == comp["id"] for c in data["competitors"]):
        return False
    data["competitors"].append(comp)
    return True


def add_ranking(data, date, ranking):
    for h in data["history"]:
        if h["date"] == date:
            if any(r["id"] == ranking["id"] for r in h["rankings"]):
                return False
            h["rankings"].append(ranking)
            return True
    return False


# ============================================================
# 1. VPN — add Obscura VPN
# ============================================================
vpn = load("best-vpn-services")
add_competitor(vpn, {
    "id": "obscuravpn",
    "name": "Obscura VPN",
    "brand": "Obscura",
    "url": "https://obscura.net/",
    "i18n": {
        "en": {
            "description": "Two-party multi-hop VPN that partners with Mullvad for the exit hop, audited in late 2025.",
            "priceRange": "$8"
        },
        "zh-tw": {
            "description": "雙方獨立的多跳 VPN，出口節點由 Mullvad 託管，2025 年底通過首次獨立稽核。",
            "priceRange": "約 NT$260"
        }
    }
})
add_ranking(vpn, "2026-05-19", {
    "id": "obscuravpn",
    "rank": 8,
    "score": 8.0,
    "scores": {"privacy": 9.5, "speed": 7.5, "network": 7.0, "usability": 7.5, "price": 7.5}
})
save("best-vpn-services", vpn)
print("VPN updated.")

# ============================================================
# 2. Gaming Mice — add Lamzu Maya X and Pulsar X2 CrazyLight
# ============================================================
mice = load("best-gaming-mice")
add_competitor(mice, {
    "id": "lamzu-maya-x",
    "name": "Lamzu Maya X",
    "brand": "Lamzu",
    "url": "https://lamzu.com/products/maya-x",
    "i18n": {
        "en": {
            "description": "Symmetrical 46g flagship with a PAW3950 sensor and 8K polling, a credible Viper V3 Pro alternative.",
            "priceRange": "$159"
        },
        "zh-tw": {
            "description": "46 公克對稱旗艦，PAW3950 感測器配 8K 回報率，被論壇拿來跟 Viper V3 Pro 直接對抽的款。",
            "priceRange": "約 NT$5,200"
        }
    }
})
add_competitor(mice, {
    "id": "pulsar-x2-cl",
    "name": "Pulsar X2 CrazyLight",
    "brand": "Pulsar",
    "url": "https://www.pulsar.gg/products/x2-crazylight-gaming-mouse",
    "i18n": {
        "en": {
            "description": "35g shell with the XS-1 sensor and 8K wireless polling, the lightest competitive mouse I would trust in 2026.",
            "priceRange": "$169"
        },
        "zh-tw": {
            "description": "35 公克外殼配 XS-1 感測器、8K 無線回報率，是我目前敢推給 FPS 玩家的最輕量旗艦。",
            "priceRange": "約 NT$5,500"
        }
    }
})
add_ranking(mice, "2026-05-19", {
    "id": "lamzu-maya-x",
    "rank": 13,
    "score": 8.9,
    "scores": {"sensor": 9.5, "latency": 9.5, "weight": 9.5, "build": 8.5, "value": 8.5}
})
add_ranking(mice, "2026-05-19", {
    "id": "pulsar-x2-cl",
    "rank": 14,
    "score": 9.0,
    "scores": {"sensor": 9.5, "latency": 9.5, "weight": 10.0, "build": 8.5, "value": 8.0}
})
save("best-gaming-mice", mice)
print("Gaming mice updated.")

# ============================================================
# 3. Smart Watches — add Apple Watch Ultra 3
# ============================================================
watches = load("best-smart-watches")
add_competitor(watches, {
    "id": "apple-ultra3",
    "name": "Apple Watch Ultra 3",
    "brand": "Apple",
    "url": "https://www.apple.com/apple-watch-ultra-3/",
    "i18n": {
        "en": {
            "description": "watchOS 26 paired with a brighter display, satellite messaging, and 42-hour battery makes this the best adventure smartwatch in the Apple ecosystem.",
            "priceRange": "$799"
        },
        "zh-tw": {
            "description": "watchOS 26 加上更亮的螢幕、衛星訊息、42 小時電池，老實說這就是 Apple 生態裡最強的戶外旗艦。",
            "priceRange": "NT$25,900"
        }
    }
})
add_ranking(watches, "2026-05-19", {
    "id": "apple-ultra3",
    "rank": 11,
    "score": 9.4,
    "scores": {"health": 9.5, "battery": 9.0, "display": 9.5, "ecosystem": 9.5, "value": 7.5}
})
save("best-smart-watches", watches)
print("Smart watches updated.")
