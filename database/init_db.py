import sqlite3

def initialize_db():

    # Define connection and cursor
    
    connection = sqlite3.connect('data/finance.db')
    cursor = connection.cursor()

    # Create the table users if it doesn't exist
    cursor.execute('''
          CREATE TABLE IF NOT EXISTS users (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          username TEXT NOT NULL UNIQUE,
          password TEXT NOT NULL
     )
       ''')
    


    # Create table for transactions
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,           
            type TEXT CHECK(type IN ('income', 'expense')) NOT NULL,
            category TEXT NOT NULL,
            description TEXT,
            amount REAL NOT NULL,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    ''')
    

    # Commit the changes and close the connection
    connection.commit()
    connection.close()

if __name__ == "__main__":
    initialize_db()
    print("Database initialized successfully.")


