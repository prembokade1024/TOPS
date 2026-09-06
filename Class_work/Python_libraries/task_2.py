import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

df = pd.read_csv("data (1).csv")

df = df.drop(columns=['Unnamed: 32', 'id'], errors='ignore')
print("Missing values in dataset:\n", df.isnull().sum().max()) 

df['diagnosis'] = df['diagnosis'].map({'M': 1, 'B': 0})

X = df.drop('diagnosis', axis=1) 
y = df['diagnosis']              
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

importances = model.feature_importances_

plt.figure(figsize=(10, 8))

feat_importances = pd.Series(importances, index=X.columns)
feat_importances.nlargest(15).plot(kind='barh', color='teal')

plt.title('Top 15 Feature Importances - Random Forest')
plt.xlabel('Relative Importance')
plt.ylabel('Features')
plt.tight_layout()
plt.show()