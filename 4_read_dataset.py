import mysql.connector
import pandas as pd

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="iris",
    port = 3307
)

myCursor = db.cursor()

# drop_table_if_exist = ""

query = "SELECT * FROM iris_table"

myCursor.execute(query)

results = myCursor.fetchall()
for row in results:
    print(row)

db.commit()

myCursor.close()

db.close()