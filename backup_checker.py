#!/usr/bin/env python3
import argparse
from pathlib import Path
from datetime import datetime

def parse_log_timestamp(line):
    try:
        timestamp_str = line.split("at", 1)[1].strip()
        return datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
    except Exception:
        return None

def main():
    parser = argparse.ArgumentParser(description="Check the last backup timestamp.")
    parser.add_argument("-x", "--max-age", type=int, help="Warn if last backup was X or more days ago")
    args = parser.parse_args()

    log_file = Path.home() / ".config/backup_script/backup.log"
    if not log_file.exists():
        print("❌ No backup log found.")
        return

    with log_file.open() as f:
        lines = [line.strip() for line in f if line.startswith("### Backup completed at")]

    if not lines:
        print("❌ No backups recorded.")
        return

    last_line = lines[-1]
    last_backup = parse_log_timestamp(last_line)

    if not last_backup:
        print("❌ Failed to parse timestamp from log.")
        return

    now = datetime.now()
    delta_days = (now - last_backup).days

    if args.max_age is not None and delta_days >= args.max_age:
        print(f"⚠️ Backup overdue! It's been {delta_days} days")
    else:
        print(f"🕒 Last backup: {last_backup} ({delta_days} days ago)")

if __name__ == "__main__":
    main()
