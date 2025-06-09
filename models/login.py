import sqlite3
import bcrypt
import os

# Set the database path
DB_PATH = os.path.join("data", "finance.db")

def login_user():
    print("\n=== User Login ===")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if not username or not password:
        print("⚠️ Username and password cannot be empty.")
        return None

    try:
        # Connect to the database
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Fetch the user by username
        cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()

        if result:
            stored_hashed_password = result[0]

            # Verify password
            if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password):
                print("Login successful!")
                return username
            else:
                print("Incorrect password.")
        else:
            print("Username not found.")

    except Exception as e:
        print("Error:", e)

    finally:
        conn.close()

    

