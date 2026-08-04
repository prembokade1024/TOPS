import pandas as pd
from pathlib import Path

# TASK 1: Load 'restaurants' data
print("--- TASK 1: Zomato Restaurants ---")
df_zomato = pd.read_csv('zomato_restaurants.tsv', sep='\t')
print(df_zomato.head())
print("\n")

# TASK 2: Filter data with a condition
print("--- TASK 2: Filtered IPL Matches ---")
df_ipl = pd.read_csv('ipl_matches.csv')
print(df_ipl.columns.tolist())
if 'win_by_runs' in df_ipl.columns:
    filtered_ipl = df_ipl[df_ipl['win_by_runs'] > 8]
    print(filtered_ipl[['team1', 'team2', 'win_by_runs']].head())
else:
    print(df_ipl.head())
print("\n")


# TASK 3: Read a JSON dataset
print("--- TASK 3: Trending Songs JSON ---")
df_songs = pd.read_json('trending_songs.json')

if 'title' in df_songs.columns:
    print(df_songs['title'])
else:
    print(df_songs.iloc[:, 0]) 
print("\n")


# TASK 4: Merge two CSV files using pathlib
print("--- TASK 4: Merged CSV Data ---")
flipkart_path = Path('flipkart_orders.csv')
paytm_path = Path('paytm_transactions.csv')

df_flipkart = pd.read_csv(flipkart_path)

df_paytm = pd.read_csv(paytm_path, sep=';')

merged_df = pd.merge(
    df_flipkart, 
    df_paytm, 
    left_on='order_id', 
    right_on='TransactionID',
    how='outer'
)

print(merged_df.head())
print("\n")

# TASK 5: Concatenate DataFrames and reset index

print("TASK_5: Concatenated DataFrames ---")

yesterday_orders = df_flipkart.iloc[:50]   # First 50 rows
today_orders = df_flipkart.iloc[50:100]    # Next 50 rows

combined_orders = pd.concat([yesterday_orders, today_orders], ignore_index=True)
print(combined_orders)