import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="iris",
    port = 3307
)

myCursor = db.cursor()

# drop_table_if_exist = ""

query = """CREATE TABLE iris_table (  
         id INT AUTO_INCREMENT primary key NOT NULL,
         sepal_length float(20) NOT NULL,  
         sepal_width float(20) NOT NULL,  
         petal_length float(20) NOT NULL,
         petal_width float(20) NOT NULL, 
         variety VARCHAR(64))"""

myCursor.execute(query)

print("table created")

db.commit()

myCursor.close()

db.close()