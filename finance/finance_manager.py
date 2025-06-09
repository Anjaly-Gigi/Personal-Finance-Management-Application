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
    
    # Adds transaction to the database
    
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

    
    # update the transaction data

    def update_transaction(self):
        try:
            trans_id = input("Enter the transaction id to update:")

             # Prompt user for new values, leave blank to skip
            new_type = input("New type (leave blank to keep current):").strip()              
            new_category = input(" New category (leave blank to keep current): ").strip()
            new_description = input("New description (leave blank to keep current): ").strip()
            new_amount = float(input("New amount (₹) (leave blank to keep current): ")).strip()

            # Build dynamic query
            fields = []
            values = []

            if new_type:
                fields.append("type = ?")
                values.append(new_type)
            if new_category:
                fields.append("category = ?")
                values.append(new_category)
            if new_description:
                fields.append("description = ?")
                values.append(new_description)
            if new_amount:
                 try:
                     values.append(float(new_amount))
                     fields.append("amount = ?")
                 except ValueError:
                     print("Invalid amount.")
                     return

            if not fields:
                print("No fields to update.")
                return

             # Always update the date
            fields.append("date = ?")
            values.append(datetime.now())

            # Add transaction ID and user_id to the WHERE clause
            values.extend([trans_id, self.user_id])

            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()

            query = f'''
                UPDATE transactions
                SET {', '.join(fields)}
                WHERE id = ? AND user_id = ?
                ''' 
            cursor.execute(query, values)

            if cursor.rowcount == 0:
                 print("Transaction not found.")
            else:
                 print("Transaction updated.")

            conn.commit()
                 
        except Exception as e:
            print(f"Error: {e}")

        finally:
            conn.close()

    # delete a transaction 

    def delete_transaction(self):
        try:
            trans_id = input("Enter the transaction id to delete: ")

            conn = sqlite3.connect(db_path)
            cursor =conn.cursor()
            cursor.execute(
                '''
                   delete from transactions where id = ? and user_id = ?
                ''',(trans_id,self.user_id)
            )
            if cursor.rowcount == 0:
                print("Transaction not found.")
            else:
                print("Transaction deleted.")
            
            conn.commit()

        except Exception as e:
            print(f"Error: {e}")
        
        finally:
            conn.close()

        
    # view transactions data

            
    
