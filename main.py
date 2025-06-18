from models.login import login_user
from models.registeration import register_user
from models.finance_manager import TransactionManager
from models.budget_manager import BudgetManager
from database.init_db import initialize_db
from models.backup_manager import BackupManager


def main():
    initialize_db()
    print("Welcome to Personal Finance Manager")

    while True:
        # Step 1: Login/Register
        username = None
        while not username:
            choice = input("\n1. Login\n2. Register\n\n Choose an option: ").strip()
            if choice == '1':
                username = login_user()
                if not username:
                    print("Login failed. Please try again.")
            elif choice == '2':
                register_user()
            else:
                print("Invalid choice. Please choose 1 or 2.")

        # Step 2: Initialize transaction manager
        tm = TransactionManager(username)

        # Initialize budget manager
        bm = BudgetManager(username)

        # Step 3: Main Menu for the logged-in user
        while True:
            print(f"\nLogged in as: {username}")
            print("------ MENU ------")
            print("1. Add Transaction")
            print("2. Update Transaction")
            print("3. Delete Transaction")
            print("4. View Transactions")
            print("5. Monthly Report")
            print("6. Yearly Report")
            print("7. Set Budget")
            print("8. Backup Data")
            print("9. Restore Data")
            print("10. Logout")

            option = input("Choose an option: ").strip()

            if option == '1':
                tm.add_transaction()
            elif option == '2':
                tm.update_transaction()
            elif option == '3':
                tm.delete_transaction()
            elif option == '4':
                tm.view_transactions()
            elif option == '5':
                tm.monthly_report()
            elif option == '6':
                tm.yearly_report()
            
            elif option == '7':
                bm.set_budget()
            
            elif option == '8':
                backup_manager = BackupManager()
                backup_manager.backup_database()
            elif option == '9':
                backup_manager = BackupManager()
                backup_manager.list_backups()
                backup_file = input("Enter the backup file name to restore: ")
                backup_manager.restore_database(backup_file)
            elif option == '10':
                print("Logging out...")
                break  
            else:
                print("Invalid option. Try again.")

if __name__ == '__main__':
    main()
