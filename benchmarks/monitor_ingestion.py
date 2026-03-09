import json
import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def run_monitor():
    status_file = "ingestion_status.json"
    
    while True:
        clear_screen()
        print("====================================================")
        print("          SAGE | INGESTION PULSE MONITOR            ")
        print("====================================================")
        
        if not os.path.exists(status_file):
            print("\n[WAITING] No active ingestion telemetry found.")
            print("Please ensure 'python3 ingestion/wikipedia_ingest.py' is running.")
        else:
            try:
                with open(status_file, "r") as f:
                    data = json.load(f)
                
                print(f"\n  INGESTION STATE:   {data['guardian_status']}")
                print(f"  FACTS GROUNDED:    {data['facts_ingested']:,}")
                print(f"  SURGE RATE:        {data['surge_rate']:,} facts/sec")
                print(f"  AVG SURPRISE (VFE): {data['avg_surprise']:.4f}")
                print(f"  STORAGE FOOTPRINT: {data['storage_gb']:.2f} GB / 1000 GB")
                print(f"  CLOUD ARCHIVE:     {data['cloud_snapshots']} Snapshots")
                
                if data['guardian_status'] == "PAUSED":
                    print("\n[!] WARNING: STORAGE THRESHOLD REACHED. Ingestion Paused.")
                else:
                    print("\n  Ingestion proceeding with structural certainty...")
                
            except Exception as e:
                print(f"\n[ERROR] Could not read telemetry: {e}")

        print("\n====================================================")
        print("  Press Ctrl+C to exit monitor. (Script keeps running)")
        time.sleep(2)

if __name__ == "__main__":
    try:
        run_monitor()
    except KeyboardInterrupt:
        print("\nMonitor terminated.")
