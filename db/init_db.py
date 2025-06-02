import sqlite3

def initialize_db():

    # Define connection and cursor
    
    connection = sqlite3.connect('data/finance.db')
    cursor = connection.cursor()

    # Create the table if it doesn't exist
    cursor.execute('''
          CREATE TABLE IF NOT EXISTS users (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          username TEXT NOT NULL UNIQUE,
          password TEXT NOT NULL
     )
       ''')

    # Commit the changes and close the connection
    connection.commit()
    connection.close()

if __name__ == "__main__":
    initialize_db()
    print("Database initialized successfully.")
