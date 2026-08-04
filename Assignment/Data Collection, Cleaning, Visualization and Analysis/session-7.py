import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# TASK 1: Outliers in Zomato Ratings (IQR Method)
print("--- TASK 1: Zomato Outliers (IQR Method) ---")
df_zomato = pd.read_csv('zomato_restaurants.tsv')

# Zomato ratings often come as strings like '4.1/5'. 
# We must clean it into a numeric format first to calculate IQR.
if 'rate' in df_zomato.columns:
    df_zomato['rate_num'] = df_zomato['rate'].astype(str).str.replace('/5', '').str.strip()
    df_zomato['rate_num'] = pd.to_numeric(df_zomato['rate_num'], errors='coerce')
    
    # Calculate Q1, Q3, and IQR
    Q1 = df_zomato['rate_num'].quantile(0.25)
    Q3 = df_zomato['rate_num'].quantile(0.75)
    IQR = Q3 - Q1
    
    # Define bounds
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    # Filter for outliers
    outliers = df_zomato[(df_zomato['rate_num'] < lower_bound) | (df_zomato['rate_num'] > upper_bound)]
    
    print(f"Number of outliers detected: {len(outliers)}")
    print(f"Indices of first 10 outliers: {outliers.index.tolist()[:10]}")
else:
    print("Column 'rate' not found.")
print("\n")


# TASK 2: Boxplot for Order Amounts
print("--- TASK 2: Boxplot for Order Amounts ---")
df_flipkart = pd.read_csv('flipkart_orders.csv')

plt.figure(figsize=(8, 6))
plt.boxplot(df_flipkart['price'].dropna()) 
plt.title('Boxplot of Flipkart Order Prices (Outlier Detection)')
plt.ylabel('Order Amount (Price)')

plt.show() 
print("\n")


# TASK 3: Winsorization on Paytm Transactions

print("--- TASK 3: Winsorization on Paytm Transactions ---")
df_paytm = pd.read_csv('paytm_transactions.csv', sep=';')

# Ensuring the Amount column is numeric
df_paytm['Amount'] = pd.to_numeric(df_paytm['Amount'], errors='coerce')

# Calculate the 5th and 95th percentiles
lower_percentile = df_paytm['Amount'].quantile(0.05)
upper_percentile = df_paytm['Amount'].quantile(0.95)

# Apply winsorization using pandas .clip() method
df_paytm['Amount_winsorized'] = df_paytm['Amount'].clip(lower=lower_percentile, upper=upper_percentile)

print("Original 'Amount' Statistics:\n", df_paytm['Amount'].describe()[['min', 'max', 'mean']])
print("\nWinsorized 'Amount' Statistics:\n", df_paytm['Amount_winsorized'].describe()[['min', 'max', 'mean']])
print("\n")


# TASK 4: String to Numeric Conversion
print("--- TASK 4: String to Numeric Conversion ---")
# We use regex=True to replace anything that is NOT a digit (\d) or a decimal point (\.)
df_flipkart['cleaned_price'] = (
    df_flipkart['price']
    .astype(str)
    .str.replace(r'[^\d.]', '', regex=True) # Removes '₹', ',', spaces, etc.
    .astype(float)
)

print(df_flipkart[['price', 'cleaned_price']].head())
print("\n")


# TASK 5: Fix Boolean Conversion

print("--- TASK 5: Fix Boolean Conversion (Spotify Mock Data) ---")
df_spotify = pd.DataFrame({
    'user_id': [101, 102, 103, 104, 105],
    'is_premium': ['True', 0, 'yes', 1, 'False']
})
print("Original DataFrame:\n", df_spotify)

valid_true_values = ['True', 1, '1', 'yes', True]
df_spotify['is_premium'] = df_spotify['is_premium'].isin(valid_true_values)

print("\nFixed DataFrame (Strict Boolean):\n", df_spotify)