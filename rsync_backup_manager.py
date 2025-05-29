#!/usr/bin/env python3
import subprocess
from pathlib import Path
from datetime import datetime
import argparse

def run_rsync(source_folder, dest_folder, dry_run=False):
    source = str(Path(source_folder).resolve()) + '/'
    dest = str(Path(dest_folder).resolve())
    base_cmd = ["rsync", "-a", "--delete"]
    if dry_run:
        base_cmd.append("--dry-run")

    # Run the full command with progress on screen
    display_cmd = base_cmd + ["--progress", source, dest]
    print(f"🔄 Running rsync (display): {' '.join(display_cmd)}")
    try:
        subprocess.run(display_cmd, check=True)
        print("✅ Rsync (display) completed successfully." if not dry_run else "✅ Dry-run completed (no changes made).")
    except subprocess.CalledProcessError as e:
        print(f"❌ Rsync failed during display run: {e}")
        return False

    # Run a second time with --stats only, capturing output
    stats_cmd = base_cmd + ["--stats", source, dest]
    print(f"📊 Running rsync (stats): {' '.join(stats_cmd)}")
    try:
        result = subprocess.run(stats_cmd, check=True, capture_output=True, text=True)
        return result.stdout  # return stats output
    except subprocess.CalledProcessError as e:
        print(f"❌ Rsync failed during stats run: {e}")
        return False

def append_to_log(source, dest, stats_output):
    log_file = Path("/home/pafi/.config/backup_script/backup.log")
    log_file.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with log_file.open("a") as f:
        f.write(f"\n### Backup completed at {timestamp}\n")
        f.write(f"Source: {source}\n")
        f.write(f"Destination: {dest}\n")
        f.write("=== RSYNC STATS ===\n")
        f.write(stats_output)
        f.write("\n---\n")
    print(f"📝 Stats appended to: {log_file}")


def main():
    parser = argparse.ArgumentParser(description="Rsync backup script with stats logging.")
    parser.add_argument("source", help="Source folder to back up")
    parser.add_argument("dest", help="Destination folder")
    parser.add_argument("--dry-run", action="store_true", help="Perform a dry run (no changes made)")

    args = parser.parse_args()

    stats_output = run_rsync(args.source, args.dest, args.dry_run)
    if stats_output and isinstance(stats_output, str):
        append_to_log(args.source, args.dest, stats_output)

if __name__ == "__main__":
    main()
