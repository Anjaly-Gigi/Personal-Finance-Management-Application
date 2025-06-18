import unittest
from models.budget_manager import BudgetManager

class TestBudgetManager(unittest.TestCase):
    def setUp(self):
        self.bm = BudgetManager("test_user")

    def test_methods_exist(self):
        self.assertTrue(callable(self.bm.set_budget))
        self.assertTrue(callable(self.bm.check_budget_alert))

if __name__ == '__main__':
    unittest.main()
