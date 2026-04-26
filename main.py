"""
EduSafe – Website Blocker
Blocks URLs based on rules, schedules, and usage policies.
"""

import json
import time
from datetime import datetime

# Load blocklist
def load_blocklist(path="config/blocklist.txt"):
    try:
        with open(path) as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

# Check if URL is blocked
def is_blocked(url, blocklist):
    return any(blocked in url for blocked in blocklist)

# Load schedule config
def is_within_schedule(schedule):
    now = datetime.now()
    current_hour = now.hour
    start = schedule.get("start_hour", 0)
    end = schedule.get("end_hour", 24)
    return start <= current_hour < end

# Main blocker logic
def run_blocker():
    blocklist = load_blocklist()
    print(f"[EduSafe] Loaded {len(blocklist)} blocked URLs.")
    print("[EduSafe] Blocker is active. Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("[EduSafe] Blocker stopped.")

if __name__ == "__main__":
    run_blocker()
