import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# 1. Load Dataset
df_students = pd.read_csv("student_marks_small.csv")
print("First 5 rows of dataset:")
print(df_students.head())

# Feature and Target
X_student = df_students[['StudyHours']]  # Feature matrix
y_student = df_students['Marks']         # Target vector

# 2. Split Data (80% Train, 20% Test)
X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(
    X_student, y_student, test_size=0.2, random_state=42
)

# 3. Train Model
model_student = LinearRegression()
model_student.fit(X_train_s, y_train_s)

# 4. Predictions on Test Data
y_pred_s = model_student.predict(X_test_s)

# 5. Evaluation Metrics
mse_s = mean_squared_error(y_test_s, y_pred_s)
rmse_s = np.sqrt(mse_s)
mae_s = mean_absolute_error(y_test_s, y_pred_s)
r2_s = r2_score(y_test_s, y_pred_s)

print("\n--- Student Marks Evaluation Metrics ---")
print(f"MSE  : {mse_s:.2f}")
print(f"RMSE : {rmse_s:.2f}")
print(f"MAE  : {mae_s:.2f}")
print(f"R²   : {r2_s:.4f}")

# 6. Train vs Test Scores
train_score_s = model_student.score(X_train_s, y_train_s)
test_score_s = model_student.score(X_test_s, y_test_s)

print("\n--- Student Model Performance ---")
print(f"Training Score (R²): {train_score_s:.4f}")
print(f"Testing Score (R²) : {test_score_s:.4f}")

# 7. Check Overfitting vs Underfitting
print("\n--- Overfitting vs. Underfitting Diagnosis ---")
gap = train_score_s - test_score_s

if train_score_s < 0.60 and test_score_s < 0.60:
    print("Status: UNDERFITTING")
    print("Reason: Both training and testing scores are low.")
elif train_score_s > 0.80 and gap > 0.15:
    print("Status: OVERFITTING")
    print("Reason: Training score is high, but testing score drops significantly.")
elif train_score_s >= 0.70 and test_score_s >= 0.70 and abs(gap) <= 0.10:
    print("Status: GOOD FIT")
    print("Reason: Strong performance across both train and test splits.")
else:
    print("Status: MODERATE FIT / CHECK WITH CROSS-VALIDATION")

# 8. Visualizing the Fit
plt.figure(figsize=(8, 5))
plt.scatter(X_train_s, y_train_s, color='blue', label='Train Data', alpha=0.7)
plt.scatter(X_test_s, y_test_s, color='green', label='Test Data', alpha=0.9)
plt.plot(X_student, model_student.predict(X_student), color='red', linewidth=2, label='Regression Line')
plt.title('Study Hours vs Marks (Model Fit)')
plt.xlabel('Study Hours')
plt.ylabel('Marks')
plt.legend()
plt.grid(True)
plt.show()