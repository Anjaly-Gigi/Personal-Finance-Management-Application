import sqlite3
import os 
from datetime import datetime
from models.budget_manager import BudgetManager  

db_path = os.path.join("data", "finance.db")

class TransactionManager:

    def __init__(self, username):
        self.username = username
        self.user_id = self.get_user_id()
        if self.user_id is None:
            raise ValueError("User not found. Please register first.")

    # Retrieves the user ID based on the username
    def get_user_id(self):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM users WHERE username = ?", (self.username,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None
    
    # Adds transaction to the database

    def add_transaction(self):
        try:
            transaction_type = input("Enter transaction type (income/expense): ").strip().lower()
            category = input("Enter category (e.g., Food, Transport, Rent, Salary): ").strip()
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))

            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute('''
                insert into transactions(user_id , type, category, description, amount,date)
                            values (?,?,?,?,?,?)''', (self.user_id,transaction_type,category, description, amount, datetime.now())
                             )
            conn.commit()
            print("Transaction added successfully")

             #  Budget check only for expense
            if transaction_type == 'expense':
                 BudgetManager(self.username).check_budget_alert(category)

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
            new_amount = input("New amount (₹) (leave blank to keep current): ").strip()

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
                    new_amount = float(new_amount)
                    fields.append("amount = ?")
                    values.append(new_amount)
                except ValueError:
                    print("Invalid amount entered.")
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

        
    # view transactions

    def view_transactions(self):
        
           conn = sqlite3.connect(db_path)
           cursor = conn.cursor()
           cursor.execute('''
            SELECT id, type, category, description, amount, date
            FROM transactions
            WHERE user_id = ?
            ORDER BY date DESC
            ''', (self.user_id,))
           rows = cursor.fetchall()
           conn.close()

           if not rows:
               print("No transactions found.")
           else:
               print("\n Your Transactions:")
               for row in rows:
                   print(f"ID: {row[0]} | {row[1]} [{row[2]}] - {row[3]} | {row[4]} | {row[5]}")


    def monthly_report(self):
        try:
            month = int(input("Enter month (1-12): "))
            year = int(input("Enter year (e.g., 2025): "))

            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute('''
                SELECT type, amount
                FROM transactions
                WHERE user_id = ? AND strftime('%m', date) = ? AND strftime('%Y', date) = ?
            ''', (self.user_id, f"{month:02}", str(year)))
            data = cursor.fetchall()
            conn.close()

            income = sum(amount for t_type, amount in data if t_type == 'income')
            expense = sum(amount for t_type, amount in data if t_type == 'expense')
            savings = income - expense

            print(f"\nMonthly Report - {month}/{year}")
            print(f"Total Income  : ₹{income:.2f}")
            print(f"Total Expense : ₹{expense:.2f}")
            print(f"Net Savings   : ₹{savings:.2f}")

        except Exception as e:
            print("Error generating monthly report:", e)

    def yearly_report(self):
        try:
            year = input("Enter year (e.g., 2025): ").strip()

            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute('''
                SELECT type, amount
                FROM transactions
                WHERE user_id = ? AND strftime('%Y', date) = ?
            ''', (self.user_id, year))
            data = cursor.fetchall()
            conn.close()

            income = sum(amount for t_type, amount in data if t_type == 'income')
            expense = sum(amount for t_type, amount in data if t_type == 'expense')
            savings = income - expense

            print(f"\n Yearly Report - {year}")
            print(f"Total Income  : ₹{income:.2f}")
            print(f"Total Expense : ₹{expense:.2f}")
            print(f"Net Savings   : ₹{savings:.2f}")

        except Exception as e:
            print("Error generating yearly report:", e)
