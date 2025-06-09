import sqlite3
import bcrypt
import os

# Set the database path 
DB_PATH = os.path.join("data", "finance.db")

def register_user():
    print("\n=== User Registration ===")
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    try:
        # Connect to the database
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Insert new user
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        print("Registration successfull!")

    except sqlite3.IntegrityError:
        print("Username already exists. Try a different one.")

    finally:
        conn.close()

if __name__ == "__main__":
    register_user()
