import mysql.connector
from mysql.connector import errorcode

def create_database(cursor):
    try:
        # CREATE DATABASE IF NOT EXISTS statement
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")

def main():
    try:
        # Establishing a connection to the MySQL server
        conn = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password"
        )
        cursor = conn.cursor()
        create_database(cursor)
    except mysql.connector.Error as err:
        # Handling exceptions
        print(f"Error: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    main()
