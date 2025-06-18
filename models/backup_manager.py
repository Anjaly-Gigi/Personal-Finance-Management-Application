import os
import shutil
from datetime import datetime

DB_PATH = os.path.join("data", "finance.db")
BACKUP_DIR = os.path.join("data", "backups")

# Ensure backup folder exists
os.makedirs(BACKUP_DIR, exist_ok=True)

class BackupManager:
    def __init__(self):
        self.db_path = DB_PATH
        self.backup_dir = BACKUP_DIR

    def backup_database(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = f"finance_backup_{timestamp}.db"
        backup_path = os.path.join(self.backup_dir, backup_filename)

        try:
            shutil.copy2(self.db_path, backup_path)
            print(f"Backup successful! Saved to: {backup_path}")
        except Exception as e:
            print("Backup failed:", e)

    def restore_database(self, backup_filename):
        backup_path = os.path.join(self.backup_dir, backup_filename)

        if not os.path.exists(backup_path):
            print("Backup file not found.")
            return

        try:
            shutil.copy2(backup_path, self.db_path)
            print("Database restored successfully.")
        except Exception as e:
            print("Restore failed:", e)

    def list_backups(self):
        print("\nAvailable backups:")
        for file in os.listdir(self.backup_dir):
            if file.endswith(".db"):
                print(f" - {file}")
