import mysql.connector
try:
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="freepalestine710",
)
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;") 
    print("Database 'alx_book_store' created successfully!")

    mycursor.close()
    mydb.close()
except mysql.connector.Error as e:
    print("Error: Could not connect to MySQL Server", e)
    