import os
import shutil
import time

class OneDriveOffloader:
    """
    Manages the 'Snapshot to Cloud' pipeline for SAGE's Long-Term Memory (LTM).
    """
    def __init__(self, local_storage: str, onedrive_storage: str):
        self.local_storage = local_storage
        self.onedrive_storage = onedrive_storage
        
        # Ensure cloud directory exists
        if not os.path.exists(self.onedrive_storage):
            os.makedirs(self.onedrive_storage, exist_ok=True)

    def offload_snapshot(self, snapshot_name: str) -> bool:
        """Moves a local memory snapshot to OneDrive."""
        local_file = os.path.join(self.local_storage, snapshot_name)
        cloud_file = os.path.join(self.onedrive_storage, snapshot_name)
        
        if not os.path.exists(local_file):
            print(f"[OFFLOADER ERROR] Local snapshot not found: {snapshot_name}")
            return False
            
        try:
            print(f"[OFFLOADER] Transferring {snapshot_name} to OneDrive...")
            shutil.move(local_file, cloud_file)
            print(f"[OFFLOADER SUCCESS] {snapshot_name} archived in cloud.")
            return True
        except Exception as e:
            print(f"[OFFLOADER ERROR] Transfer failed: {str(e)}")
            return False

    def list_cloud_snapshots(self):
        """Lists all snapshots currently stored in OneDrive."""
        if os.path.exists(self.onedrive_storage):
            return os.listdir(self.onedrive_storage)
        return []
