import pandas as pd
import numpy as np

print("TASK 2: Pandas Data Cleaning")

# 1. Create DataFrame with missing values and duplicates
data = {
    'order_id': list(range(1, 21)) + [1, 2, 3],
    'customer_name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy',
                      'Mallory', 'Nina', 'Oscar', 'Peggy', 'Quentin', 'Romeo', 'Sybil', 'Trent', 'Victor', 'Walter'] + ['Alice', 'Bob', 'Charlie'],
    'restaurant_name': ['Rest_A', 'Rest_B', 'Rest_C', 'Rest_A', 'Rest_B'] * 4 + ['Rest_A', 'Rest_B', 'Rest_C'],
    'category': ['Fast Food', 'Healthy', 'Indian', 'Fast Food', None] * 4 + ['Fast Food', 'Healthy', 'Indian'], 
    'delivery_time_mins': [25, 30, np.nan, 45, 20, 35, 40, np.nan, 22, 28] * 2 + [25, 30, np.nan], 
    'order_value': [15.5, 22.0, 18.5, 120.0, np.nan, 14.0, 25.5, 33.0, np.nan, 19.0] * 2 + [15.5, 22.0, 18.5], 
    'rating': [4.5, 3.0, 4.0, np.nan, 5.0, 4.2, 3.8, np.nan, 4.7, 2.5] * 2 + [4.5, 3.0, 4.0]
}
df = pd.DataFrame(data)

# 2. Handle missing values
print("Missing values :")
print(df.isnull().sum())

df['delivery_time_mins'] = df['delivery_time_mins'].fillna(df['delivery_time_mins'].median())
df['order_value'] = df['order_value'].fillna(df['order_value'].median())
df['rating'] = df['rating'].fillna(round(df['rating'].mean(), 1))
df['category'] = df['category'].fillna(df['category'].mode()[0])

# 3. Remove duplicate rows
print(f"\nShape BEFORE deduplication: {df.shape}")
df = df.drop_duplicates()
print(f"Shape AFTER deduplication: {df.shape}")

# 4. Outlier Detection (IQR)
Q1 = df['order_value'].quantile(0.25)
Q3 = df['order_value'].quantile(0.75)
IQR = Q3 - Q1
upper_limit = Q3 + 1.5 * IQR
lower_limit = Q1 - 1.5 * IQR

outliers = df[(df['order_value'] > upper_limit) | (df['order_value'] < lower_limit)]
print(f"\nOutliers found:\n{outliers[['order_id', 'order_value']]}")

df['order_value'] = df['order_value'].clip(upper=upper_limit)
print(f"Capped upper limit value: {upper_limit:.2f}")