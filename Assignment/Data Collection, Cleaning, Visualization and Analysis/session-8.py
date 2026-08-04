import pandas as pd

# TASK 1: Find Duplicates in Zomato Data
print("--- TASK 1: Zomato Duplicates ---")
# we will look for duplicate restaurant listings based on 'name' and 'address'.
df_zomato = pd.read_csv('zomato_restaurants.tsv')

if 'name' in df_zomato.columns and 'address' in df_zomato.columns:
    duplicates = df_zomato[df_zomato.duplicated(subset=['name', 'address'], keep=False)]
    print(f"Found {len(duplicates)} duplicate listings.")
    print(duplicates[['name', 'address']].head())
else:
    print("Columns 'name' and 'address' not found.")
print("\n")


# TASK 2: Top 3 Duplicate Flipkart Reviews
print("--- TASK 2: Top Duplicate Flipkart Reviews ---")
df_flipkart = pd.read_csv('flipkart_orders.csv')

if 'review' in df_flipkart.columns:
    top_reviews = df_flipkart['review'].value_counts().head(3)
    print("Top 3 most repeated reviews:")
    print(top_reviews)
else:
    print("Column 'review' not found in Flipkart dataset.")
print("\n")


# TASK 3: Remove Exact Duplicates (Adapted to JSON)
print("--- TASK 3: Clean Trending Songs JSON ---")
df_songs = pd.read_json('trending_songs.json')
print(f"Original song count: {len(df_songs)}")

df_songs_cleaned = df_songs.drop_duplicates()

print(f"Cleaned song count: {len(df_songs_cleaned)}")
print("\n")


# TASK 4: Standardize Strings (Adapted to IPL Data)
print("--- TASK 4: Standardize IPL Cities ---")
df_ipl = pd.read_csv('ipl_matches.csv')

if 'city' in df_ipl.columns:
    print("Unique cities before:", df_ipl['city'].unique()[:10])
    
    df_ipl['city'] = df_ipl['city'].replace(['Bangalore', 'bangalore'], 'Bengaluru')
    
    print("Unique cities after replacement:", df_ipl['city'].unique()[:10])
else:
    print("Column 'City' not found.")
print("\n")


# TASK 5: Unify Paytm Payment Statuses
print("--- TASK 5: Unify Paytm Payment Statuses ---")
df_paytm = pd.read_csv('paytm_transactions.csv', sep=';')

if 'Payment_Status' in df_paytm.columns:
    df_paytm['Payment_Status_Clean'] = df_paytm['Payment_Status'].astype(str).str.strip().str.lower()
    
    status_map = {
        'yes': 1, 'y': 1, 'success': 1, 'paid': 1,
        'no': 0, 'n': 0, 'failed': 0, 'pending': 0
    }
    
    df_paytm['Payment_Status_Unified'] = df_paytm['Payment_Status_Clean'].map(status_map)
    
    print(df_paytm[['Payment_Status', 'Payment_Status_Unified']].head())
else:
    print("Column 'Payment_Status' not found.")