import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# 1. Load Data
df = pd.read_csv("salary_data (1).csv")
print("Dataset Overview:\n", df.head())

# 2. Features & Target Selection
X = df[['YearsExperience']]
y = df['Salary']

# 3. Train-Test Split (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Initialize & Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Model Parameters
print("\nModel Slope (m):", model.coef_[0])
print("Model Intercept (c):", model.intercept_)

# 6. Predictions
y_pred = model.predict(X_test)

# Comparison DataFrame
comparison = pd.DataFrame({
    'Actual Value': y_test.values,
    'Predicted Value': y_pred,
    'Difference (Error)': y_test.values - y_pred
})
print("\nComparison Table:\n", comparison)

# 7. Evaluation Metrics
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)  # Or root_mean_squared_error(y_test, y_pred) in newer sklearn
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n--- Evaluation Metrics (Test Set) ---")
print(f"Mean Squared Error (MSE)      : {mse:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"Mean Absolute Error (MAE)     : {mae:.2f}")
print(f"R² Score                      : {r2:.4f}")

# 8. Model Scoring (Train vs Test Score)
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)

print("\n--- Model Performance Scores ---")
print(f"Training Score (R²): {train_score:.4f}")
print(f"Testing Score (R²) : {test_score:.4f}")

# Check for Overfitting / Underfitting
if train_score > 0.85 and test_score > 0.85 and abs(train_score - test_score) < 0.1:
    print("Status: Good Fit (Model generalizes well)")
elif train_score > test_score and (train_score - test_score) > 0.1:
    print("Status: Overfitting (High train score, lower test score)")
else:
    print("Status: Underfitting (Both scores are relatively low)")

# 9. Single New Prediction
exper = [[7.5]]
predict_salary = model.predict(exper)
print(f"\nPredicted salary for 7.5 years experience: {predict_salary[0]:,.2f}")