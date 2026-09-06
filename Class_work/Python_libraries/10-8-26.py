import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

df = pd.read_csv("student_pass.csv")
print(df.head())

print(df.info())
missing_values=df.isnull().sum()
print(missing_values)

X = df[['StudyHours']]
y = df['Pass']

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

y_prob = model.predict_proba(X_test)

accuracy = accuracy_score(y_test,y_pred)
print("Accuracy : ",accuracy)

print("\nConfusion Matrix : ",confusion_matrix(y_test, y_pred))

print("\nClassification Report : ")
print(classification_report(y_test, y_pred))

print("\nPredicted Probabilities for the test set:")
print(y_prob)