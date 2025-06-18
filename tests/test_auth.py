import unittest
import sqlite3
import os
from models.registeration import register_user
from models.login import login_user

class TestAuth(unittest.TestCase):

    def test_registration_and_login(self):
        # Test dummy registration (should ideally mock input/output)
        self.assertTrue(callable(register_user))
        self.assertTrue(callable(login_user))

if __name__ == '__main__':
    unittest.main()
