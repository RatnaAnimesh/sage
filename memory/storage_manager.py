import os
import shutil
import time
from typing import Optional

class StorageGuardian:
    """
    Monitors disk usage and enforces the 1TB safety threshold for SAGE.
    """
    ONE_TERABYTE = 1 * 1024 * 1024 * 1024 * 1024 # 1,099,511,627,776 bytes
    
    def __init__(self, local_path: str, cloud_path: str, threshold_gb: float = 1000.0):
        self.local_path = local_path
        self.cloud_path = cloud_path
        self.threshold_bytes = threshold_gb * 1024**3
        self.paused = False

    def get_total_usage(self) -> int:
        """Calculates total bytes consumed by SAGE across local and cloud storage."""
        total = 0
        for path in [self.local_path, self.cloud_path]:
            if os.path.exists(path):
                for dirpath, dirnames, filenames in os.walk(path):
                    for f in filenames:
                        fp = os.path.join(dirpath, f)
                        if not os.path.islink(fp):
                            total += os.path.getsize(fp)
        return total

    def check_threshold(self) -> bool:
        """Returns True if storage is below threshold, False otherwise."""
        usage = self.get_total_usage()
        usage_gb = usage / (1024**3)
        
        if usage >= self.threshold_bytes:
            if not self.paused:
                print(f"\n[GUARDIAN ALERT] Storage Threshold Reached: {usage_gb:.2f} GB / 1000 GB")
                print("[GUARDIAN] Ingestion PAUSED. Please check your OneDrive capacity.")
                self.paused = True
            return False
            
        self.paused = False
        return True

    def report(self):
        usage = self.get_total_usage()
        print(f"[STORAGE REPORT] Current SAGE Footprint: {usage/(1024**3):.2f} GB")
