import mysql.connector

try:
    # Step 1: Connect to MySQL server (no database specified yet)
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Gabigabi@1"
    )

    if connection.is_connected():
        cursor = connection.cursor()

        # Step 2: Create database if it doesn’t exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error while connecting to MySQL: {err}")

finally:
    # Step 3: Properly close the cursor and connection
    try:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")
    except NameError:
        # Happens if connection was never established
        pass
