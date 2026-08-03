import pandas as pd
import io
import pandas as pd

# Task_1

print("Task 1 :")
# Load the IPL matches dataset
df_ipl = pd.read_csv('ipl_matches.csv')

# Display the first 5 rows
print("First 5 rows of IPL Match Scores:")
print(df_ipl.head())

#Task_2
print("Task 2 :")
# Load JSON dataset of trending songs
df_songs = pd.read_json('trending_songs.json')

# Display column names, non-null counts, and data types
print("Trending Songs DataFrame Info:")
df_songs.info()

# Task_3

print("Task 3 :")
# Load TSV file using '\t' as the delimiter/separator
df_zomato = pd.read_csv('zomato_restaurants.tsv', sep='\t')

# Generate summary statistics including categorical and numerical columns
print("Summary Statistics for Zomato Data:")
print(df_zomato.describe(include='all'))

# Task_4
print("Task 4 :")
chunk_size = 2000

# (Using CSV format as pd.read_csv natively supports chunksize iterator)
chunk_iterator = pd.read_csv('flipkart_orders.csv', chunksize=chunk_size)

for i, chunk in enumerate(chunk_iterator, start=1):
    print(f"Chunk {i}: {len(chunk)} rows loaded.")

# Task_5

print("Task 5 :")
# Load semicolon-separated CSV
df_paytm = pd.read_csv("paytm_transactions.csv", sep=';')
print(df_paytm.head())
# Detect missing (null) values per column
missing_values = df_paytm.isnull().sum()

# Filter and print columns that contain at least one null value
columns_with_nulls = missing_values[missing_values > 0]

print("Columns containing missing values and their null counts:")
if not columns_with_nulls.empty:
    print(columns_with_nulls)
else:
    print("No missing values found!")