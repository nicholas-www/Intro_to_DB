import mysql.connector

try:
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin',
        database='alx_book_store'
    )
except mysql.connector.Error:
    print('An error occured!')

cursor = db.cursor()

cursor.execute(
    """
    CREATE DATABASE IF NOT EXISTS alx_book_store
    """
)

print("Database 'alx_book_store' created successfully!")

cursor.close()
db.close()