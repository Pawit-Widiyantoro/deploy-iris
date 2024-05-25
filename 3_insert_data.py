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

query = """INSERT INTO iris_table (sepal_length ,sepal_width ,petal_length, petal_width, variety) 
          VALUES (%s, %s,%s,%s,%s)"""

data = pd.read_csv("iris.csv")
print(f"dataset load {data}")

for index, row in data.iterrows():
    myCursor.execute(query, (row['SepalLengthCm'],row['SepalWidthCm'],row['PetalLengthCm'],row['PetalWidthCm'],row['Species']))

db.commit()

myCursor.close()

db.close()