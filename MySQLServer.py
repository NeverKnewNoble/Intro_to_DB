import mysql.connector
from mysql.connector import errorcode

def create_database(cursor):
    try:
        # Check for the CREATE DATABASE statement
        cursor.execute("CREATE DATABASE alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_DB_CREATE_EXISTS:
            print("Database 'alx_book_store' already exists.")
        else:
            print(f"Failed creating database: {err}")

def main():
    try:
        # Check for the code to establish a connection to the MySQL server
        conn = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password"
        )
        cursor = conn.cursor()
        create_database(cursor)
    except mysql.connector.Error as err:
        # Check for the code to handle exceptions
        print(f"Error: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    # Check for the code to handle exceptions
    main()
