# utils.py

import json
import os
from datetime import datetime

LOG_PATH = os.path.join("data", "news_log.json")

def get_timestamp():
    return datetime.utcnow().isoformat() + "Z"

def save_log_entry(entry, path=LOG_PATH):
    """
    Appends an entry (dict) to the news_log.json file.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)

    try:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        else:
            data = []

        data.append(entry)

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data[-100:], f, indent=2)  # Keep only last 100 entries

    except Exception as e:
        print(f"[ERROR] Failed to write to log file: {e}")

def print_signal_summary(result):
    """
    Utility to print clean console output for testing.
    """
    print(f"\n📊 Signal: {result['signal']}")
    print(f"🔍 Reason: {result['reason']}")
    print(f"   🔼 Bullish: {result['breakdown']['bullish']}")
    print(f"   🔽 Bearish: {result['breakdown']['bearish']}")
    print(f"   ⚪ Neutral: {result['breakdown']['neutral']}")
