import pandas as pd
import numpy as np

# TASK 1: Convert Strings to Datetime
print("--- TASK 1: Convert Strings to Datetime ---")
timestamps = ['2024-06-01 14:30', '2024-06-02 09:15', '2024-06-03 20:45']

# Use pd.to_datetime to convert the list of strings to datetime objects
dt_objects = pd.to_datetime(timestamps)
print(dt_objects)
print("\n")

# TASK 2: Extract Year, Month, and Weekday
print("--- TASK 2: Extract Year, Month, Weekday ---")
df_flipkart = pd.read_csv('flipkart_orders.csv')

# Step 1: Ensure the 'order_date' column is actually a datetime object (crucial for .dt accessor)
df_flipkart['order_date'] = pd.to_datetime(df_flipkart['order_date'], errors='coerce')

# Step 2: Extract the features using the .dt accessor
df_flipkart['year'] = df_flipkart['order_date'].dt.year
df_flipkart['month'] = df_flipkart['order_date'].dt.month
df_flipkart['weekday'] = df_flipkart['order_date'].dt.day_name() # e.g., 'Monday', 'Tuesday'

# Displaying the results
print(df_flipkart[['order_date', 'year', 'month', 'weekday']].head())
print("\n")

# TASK 3: Resample to Calculate Weekly Orders
print("--- TASK 3: Weekly Order Resampling ---")
# To use resample(), the datetime column must be the index of the DataFrame
# We create a copy and drop rows where 'order_date' might be missing (NaT) to avoid index errors
df_time_indexed = df_flipkart.dropna(subset=['order_date']).copy()
df_time_indexed.set_index('order_date', inplace=True)

# Resample using 'W' (Weekly) and count the number of rows per week using .size()
weekly_orders = df_time_indexed.resample('W').size()

print("Total orders placed each week:")
print(weekly_orders.head())
print("\n")

# TASK 4: UTC to Asia/Kolkata Timezone Conversion
print("--- TASK 4: Timezone Conversion (Instagram Mock Data) ---")
# Creating a mock DataFrame for Instagram posts
df_insta = pd.DataFrame({
    'post_id': [101, 102, 103],
    'posted_at': ['2024-06-01 10:00:00', '2024-06-02 12:30:00', '2024-06-03 15:45:00']
})

# Convert string to datetime
df_insta['posted_at'] = pd.to_datetime(df_insta['posted_at'])
df_insta['posted_at_ist'] = df_insta['posted_at'].dt.tz_localize('UTC').dt.tz_convert('Asia/Kolkata')
print(df_insta[['posted_at', 'posted_at_ist']].head())
print("\n")

# TASK 5: Create 'is_weekend' Feature
print("--- TASK 5: Create 'is_weekend' Feature ---")
df_flipkart['is_weekend'] = np.where(df_flipkart['order_date'].dt.weekday >= 5, True, False)
print(df_flipkart[['order_date', 'weekday', 'is_weekend']].head(7))