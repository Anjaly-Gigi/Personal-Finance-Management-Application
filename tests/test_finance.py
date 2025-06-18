import unittest
import sqlite3
import os
from models.finance_manager import TransactionManager

DB_PATH = os.path.join("data", "finance.db")

class TestFinanceManager(unittest.TestCase):
    def setUp(self):
        self.username = "test_user"
        self.password = "test123"
        self.conn = sqlite3.connect(DB_PATH)
        self.cursor = self.conn.cursor()

        # Insert test user if not exists
        self.cursor.execute("SELECT id FROM users WHERE username = ?", (self.username,))
        user = self.cursor.fetchone()
        if not user:
            import bcrypt
            hashed = bcrypt.hashpw(self.password.encode(), bcrypt.gensalt())
            self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (self.username, hashed))
            self.conn.commit()

        self.tm = TransactionManager(self.username)

    def tearDown(self):
        # Clean up test data
        self.cursor.execute("DELETE FROM transactions WHERE user_id = ?", (self.tm.user_id,))
        self.cursor.execute("DELETE FROM users WHERE username = ?", (self.username,))
        self.conn.commit()
        self.conn.close()

    def test_methods_exist(self):
        self.assertTrue(callable(self.tm.add_transaction))
        self.assertTrue(callable(self.tm.update_transaction))
        self.assertTrue(callable(self.tm.delete_transaction))
        self.assertTrue(callable(self.tm.view_transactions))

if __name__ == '__main__':
    unittest.main()
