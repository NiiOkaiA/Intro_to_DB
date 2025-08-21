import mysql.connector

db= mysql.connector.connect(
    host='localhost',
    user='root',
    password='newpassword',
    database='new_data')


cursor=db.cursor()

sql="CREATE DATABASE IF NOT EXISTS alx_book_store"
cursor.execute(sql)

print("Database 'alx_book_store' created successfully")
      
#Database 'alx_book_store' created successfully!
