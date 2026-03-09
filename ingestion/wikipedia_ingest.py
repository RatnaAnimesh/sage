import os
import sys
import time
import random

# Add project root to sys.path
sys.path.append(os.path.dirname(os.getcwd()))

from ingestion.semantic_parser import SemanticToCategoricalParser, CausalSieve
from memory.storage_manager import StorageGuardian
from memory.offloader import OneDriveOffloader
from sage.memory.atomspace import AtomSpace

class MockWikipediaStream:
    """Simulates the Firehose of English Wikipedia."""
    def __init__(self):
        self.entities = ["Gravity", "Quantum", "History", "Economy", "Ecology", "Sociology", "Mathematics"]
        self.relations = ["orbits", "effects", "defines", "limits", "expands", "destabilizes"]

    def get_article(self):
        e1 = random.choice(self.entities)
        e2 = random.choice(self.entities)
        rel = random.choice(self.relations)
        return f"The {e1} {rel} the {e2}."

def run_wikipedia_ingestion():
    print("=== SAGE Phase 10: The Great Ingestion (Wikipedia Stream) ===")
    
    # 1. Setup Storage Infrastructure
    LOCAL_SNAP = "memory/local_snapshots"
    CLOUD_SNAP = "/Users/ashishmishra/Library/CloudStorage/OneDrive-BIRLAINSTITUTEOFTECHNOLOGYandSCIENCE/SAGE_Memory"
    
    guardian = StorageGuardian(local_path=LOCAL_SNAP, cloud_path=CLOUD_SNAP, threshold_gb=1000.0)
    offloader = OneDriveOffloader(local_storage=LOCAL_SNAP, onedrive_storage=CLOUD_SNAP)
    
    # 2. Setup SAGE Cognitive Bridge
    space = AtomSpace("Global_Wikipedia")
    parser = SemanticToCategoricalParser(space)
    stream = MockWikipediaStream()
    
    print(f"[SYSTEM] Monitoring Storage (Threshold: 1.0 TB)")
    print(f"[SYSTEM] OneDrive Bridge: ACTIVE\n")
    
    count = 0
    batch_size = 50000 
    
    try:
        while guardian.check_threshold():
            # Simulate a batch of ingestion
            for _ in range(batch_size):
                article = stream.get_article()
                parser.ingest_text(article)
            
            count += batch_size
            
            # Simulate Snapshot Creation (Dummy file for storage testing)
            snap_name = f"LTM_Snapshot_Batch_{count // batch_size}.bin"
            snap_path = os.path.join(LOCAL_SNAP, snap_name)
            
            # Create a 100MB dummy file to simulate memory growth
            with open(snap_path, "wb") as f:
                f.write(os.urandom(1024 * 1024 * 100)) # 100MB
                
            print(f"[BATCH] Ingested {count:,} facts. Created local snapshot: {snap_name}")
            
            # 3. Offload to OneDrive
            offloader.offload_snapshot(snap_name)
            
            # 4. Guardian Report
            guardian.report()
            
            # 5. Emit Telemetry for Monitor
            import json
            status = {
                "facts_ingested": count,
                "surge_rate": batch_size / 0.1, # Mock rate
                "avg_surprise": random.uniform(0.01, 0.05),
                "storage_gb": guardian.get_total_usage() / (1024**3),
                "cloud_snapshots": len(offloader.list_cloud_snapshots()),
                "guardian_status": "ACTIVE" if not guardian.paused else "PAUSED"
            }
            with open("ingestion_status.json", "w") as f:
                json.dump(status, f)
            
            # In a real scenario, this would loop until the internet is finished. 
            # For the PoC, we stop after a few batches to demonstrate the loop.
            if count >= 250000:
                print("\n[SYSTEM] Simulation Batch Complete.")
                break
                
    except KeyboardInterrupt:
        print("\n[SYSTEM] Ingestion manually paused.")

    print("\n--- INGESTION COMPLETE ---")
    print(f"Total Grounded Facts: {count:,}")
    print(f"Cloud Archive: {len(offloader.list_cloud_snapshots())} snapshots stored.")

if __name__ == "__main__":
    run_wikipedia_ingestion()
