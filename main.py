from models.login import login_user
from models.registeration import register_user
from models.finance_manager import TransactionManager
from database.init_db import initialize_db

def main():
    initialize_db()
    print("Welcome to Personal Finance Manager")

    # Login/Register Loop
    while True:
        choice = input("\n1. Login\n2. Register\nChoose an option: ")
        if choice == '1':
            user_id = login_user()
            if user_id:
                break
        elif choice == '2':
            register_user()
        else:
            print("Invalid choice.")

    fm = TransactionManager()

    # Main Finance Menu
    while True:
        print("\n------ MENU ------")
        print("1. Add Transaction")
        print("2. Update Transaction")
        print("3. Delete Transaction")
        print("4. View Transactions")
        print("5. Monthly Report")
        print("6. Yearly Report")
        print("7. Exit")

        option = input("Choose an option: ")

        if option == '1':
            fm.add_transaction(user_id)
        elif option == '2':
            fm.update_transaction(user_id)
        elif option == '3':
            fm.delete_transaction(user_id)
        elif option == '4':
            fm.view_transactions(user_id)
        elif option == '5':
            fm.monthly_report(user_id)
        elif option == '6':
            fm.yearly_report(user_id)
        elif option == '7':
            print("👋 Exiting the app.")
            break
        else:
            print("Invalid option.")

if __name__ == '__main__':
    main()
