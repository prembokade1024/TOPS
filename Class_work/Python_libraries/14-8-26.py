import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("student_pass (1).csv")
print(df.head())

df['Result'] = df['Result'].astype(str).str.strip().str.lower()
df['Result'] = df['Result'].replace({'fail': 0, 'pass': 1})
df['Result'] = df['Result'].astype(int)

# Features and target
X = df[['Study_Hours', 'Attendance']]
y = df['Result']


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)
scaler = StandardScaler()

X_train_scale = scaler.fit_transform(X_train)
X_test_scale = scaler.transform(X_test)


model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train_scale, y_train)
y_pred = model.predict(X_test_scale)

print("Prediction:", y_pred)
prob = model.predict_proba(X_test_scale)

print("Probability:")
print(prob)
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy * 100, "%")

new_student = pd.DataFrame([[1.2, 40]], columns=['Study_Hours','Attendance'])
new_student_scale = scaler.transform(new_student)
prediction = model.predict(new_student_scale)
probability = model.predict_proba(new_student_scale)


print("New Student Prediction:", prediction)
print("New Student Probability:", probability)

if prediction[0] == 1:
    print("Result: pass")
else:
    print("Result: fail")