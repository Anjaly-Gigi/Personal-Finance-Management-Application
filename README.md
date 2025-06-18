# Personal Finance Management Application

A simple and secure **Command-Line Interface (CLI)** based application to manage personal finances — track your income, expenses, and generate reports.

<p align="center">
  <img src="https://img.freepik.com/premium-vector/online-mobile-payment-banking-service-concept-woman-pays-with-mobile-phone-successfully-safely-flat-vector-modern-illustration_566886-9730.jpg" width="220" height="220">
</p>

## Project Overview
 This Command-Line Interface (CLI) based Personal Finance Management application built using Python and SQLite helps users:  
 * Register and log in securely.
 * Track income and expenses.
 * Set budgets and get alerts when limits are exceeded.
 * Generate monthly and yearly reports.
 * Backup and restore financial data

##  Tech Stack

| Technology   | Purpose                    |
|-------------|-----------------------------|
| Python       | Core Programming Language   |
| SQLite3      | Lightweight Database        |
| CLI (Terminal)| User Interaction           |

## Installation Instructions

###  System Requirements
* Python 3.10 or higher
* pip (Python package manager)

### Running the Application
To start the app: `python main.py`

### User Manuel  
-  When you run `python main.py` , 2 options appear one is to register and other is to login.  
- If you're a new user, choose "Register" and provide a unique username and password.
- Existing users can log in using their credentials.
- Passwords are securely hashed using `bcrypt`.
- Once logged in, the app will show the main menu:
    `------- MENU ------`
`1. Add Transaction
2. Update Transaction
3. Delete Transaction
4. View Transactions
5. Monthly Report
6. Yearly Report
7. Set Budget
8. View Budgets
9. Backup Database
10. Restore Database
11. Logout`





###  Testing  
Run unit tests with:  `python -m unittest discover tests`





