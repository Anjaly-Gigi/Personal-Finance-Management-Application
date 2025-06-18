import unittest
from models.backup_manager import BackupManager

class TestBackupManager(unittest.TestCase):
    def setUp(self):
        self.bm = BackupManager()

    def test_methods_exist(self):
        self.assertTrue(callable(self.bm.backup_database))
        self.assertTrue(callable(self.bm.list_backups))
        self.assertTrue(callable(self.bm.restore_database))

if __name__ == '__main__':
    unittest.main()
