import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port = 3307
)

myCursor = db.cursor()

# drop_table_if_exist = ""

query = "CREATE DATABASE iris"

myCursor.execute(query)

print("Database Created")

db.commit()
myCursor.close()
db.close()