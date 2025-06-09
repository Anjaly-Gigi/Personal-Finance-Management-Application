from models.login import login_user
from models.registeration import register_user
from models.finance_manager import TransactionManager
from database.init_db import initialize_db

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
                break  
            elif choice == '2':
                register_user()
            else:
                print("Invalid choice. Please choose 1 or 2.")

        # Step 2: Initialize transaction manager
        tm = TransactionManager(username)

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
            print("7. Logout")
      

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
                print("Logging out...")
                break  
            else:
                print("Invalid option. Try again.")

if __name__ == '__main__':
    main()
