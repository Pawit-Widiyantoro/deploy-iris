import mysql.connector
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report

from joblib import dump

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  port=3307,
  database="iris"
)


def fetch_data():
    try:
        # Query to select data
        query = "SELECT * FROM iris_table"
        # Use pandas to read data into a DataFrame
        df = pd.read_sql(query, mydb)
    finally:
        mydb.close()
    
    return df

# Fetch the data
data = fetch_data()
print("Data fetched from the database:")
print(data.head())

# Separate features and target variable
X = data[['sepal_length' ,'sepal_width' ,'petal_length', 'petal_width']]
y = data['variety']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a model
model_rf = RandomForestClassifier()
model_svm = SVC()

model_rf.fit(X_train, y_train)
model_svm.fit(X_train, y_train)

# Make predictions on the test set
y_pred_rf = model_rf.predict(X_test)
y_pred_svm = model_svm.predict(X_test)

target_names = ['Setosa', 'Versicolor', 'Virginica']
# Evaluate the model
print("Random Forest", classification_report(y_test,y_pred_rf))
print("SVM", classification_report(y_test,y_pred_svm))

# Save the model to a file
model_filename_rf = 'trained_model_rf.pkl'
model_filename_svm = 'trained_model_svm.pkl'
dump(model_rf, model_filename_rf)
dump(model_svm, model_filename_svm)
print(f"Model saved to {model_filename_rf} and {model_filename_svm}")