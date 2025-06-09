import sqlite3
import os 
from datetime import datetime

db_path = os.path.join("data", "finance.db")

class FinanceManager:

    def __init__(self, username):
        self.username = username
        self.user_id = self.get_user_id()

    # Retrieves the user ID based on the username
    def get_user_id(self):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM users WHERE username = ?", (self.username,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None
    
    # Adds a transaction to the database
    def add_transaction(self, type, category, description, amount):
        try:
            transaction_type = input("Enter transaction type (income/expense): ").strip().lower()
            category = input("Enter category (e.g., Food, Transport, Rent): ").strip()
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))

            conn = sqlite3.connect("db_path")
            cursor = conn.cursor()
            cursor.execute('''
                insert into transactions("user_id","type", "category", "description", "amount","date")
                            values (?,?,?,?,?,?)",()''', (self.user_id,transaction_type,category, description, amount, datetime.now())
                             )
            conn.commit()
            print("Transaction added successfully")
        except Exception as e:
            print(f"Error: {e}")
            
        finally:
            conn.close()

    
