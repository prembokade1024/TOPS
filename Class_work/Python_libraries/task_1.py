import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC 
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("Churn_Modelling (1).csv")
print(df.head())

# missing_values=df.isnull().sum()
# print(missing_values)

df['Gender'] = df['Gender'].map({'Female': 0, 'Male': 1}).astype(int)

df = pd.get_dummies(df, columns=['Geography'], drop_first=True)
df = df.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1)

X = df.drop('Exited', axis=1)
y = df['Exited']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = SVC(kernel="rbf")
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:",accuracy * 100, "%")

new_customer = [[600, 1, 40, 3, 60000.00, 2, 1, 1, 50000.00, 0, 2]]

new_customer_scaled = scaler.fit_transform(new_customer)

prediction = model.predict(new_customer_scaled)

print("Customer Prediction:", prediction)

if prediction[0] == 1:
    print("Result: Exited")
else:
    print("Result: Stayed")