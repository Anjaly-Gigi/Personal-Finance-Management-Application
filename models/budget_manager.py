import sqlite3
import os

DB_PATH = os.path.join("data", "finance.db")

class BudgetManager:
    def __init__(self, username):
        self.username = username
        self.user_id = self.get_user_id()

    def get_user_id(self):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM users WHERE username = ?", (self.username,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None

    def set_budget(self):
        category = input("Enter category for the budget: ").strip()
        try:
            amount = float(input("Enter monthly budget amount: "))
        except ValueError:
            print("Invalid amount.")
            return

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO budgets (user_id, category, amount)
            VALUES (?, ?, ?)
            ON CONFLICT(user_id, category) DO UPDATE SET amount = excluded.amount
        ''', (self.user_id, category, amount))

        conn.commit()
        conn.close()
        print(f"Budget of ₹{amount:.2f} set for '{category}'.")

    def check_budget_alert(self, category):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Get budgeted amount for this category
        cursor.execute("SELECT amount FROM budgets WHERE user_id = ? AND category = ?", (self.user_id, category))
        budget_result = cursor.fetchone()

        if not budget_result:
            conn.close()
            return  # No budget set for this category

        budget_limit = budget_result[0]

        # Calculate total expense in this category this month
        cursor.execute('''
            SELECT SUM(amount) FROM transactions
            WHERE user_id = ? AND category = ? AND type = 'expense' AND strftime('%Y-%m', date) = strftime('%Y-%m', 'now')
        ''', (self.user_id, category))

        total_spent = cursor.fetchone()[0] or 0
        conn.close()

        if total_spent > budget_limit:
            print(f"Budget Alert: You have exceeded the ₹{budget_limit:.2f} budget for '{category}'. Spent: ₹{total_spent:.2f}")
