import pandas as pd

# TASK 1: Load IPL Data & Count Missing Values
print("--- TASK 1: Missing Values Count ---")
# Loading your local IPL matches dataset
df_ipl = pd.read_csv('ipl_matches.csv')

# Checking missing and present values across the whole dataset
missing_counts = df_ipl.isnull().sum()
present_counts = df_ipl.notnull().sum()

print("Missing values per column:\n", missing_counts)
print("\nPresent values per column:\n", present_counts)
print("\n")


# TASK 2: Dropping Missing Data
print("--- TASK 2: Dropping Missing Data ---")
shape_before = df_ipl.shape
print(f"Shape before dropping: {shape_before}")

df_ipl_dropped = df_ipl.dropna(axis=0, how='any')

shape_after = df_ipl_dropped.shape
print(f"Shape after dropping: {shape_after}")
print("\n")


# TASK 3: Mean Imputation
print("--- TASK 3: Mean Imputation ---")

numeric_col = 'win_by_runs' 

if numeric_col in df_ipl.columns:
    col_mean = df_ipl[numeric_col].mean()
    print(f"Calculated mean of {numeric_col}: {col_mean:.2f}")

    df_ipl[numeric_col] = df_ipl[numeric_col].fillna(col_mean)
    print(f"Missing values in '{numeric_col}' filled successfully.")
else:
    print(f"Column '{numeric_col}' not found. Please update the column name.")
print("\n")

# TASK 4 :
print("--- TASK 4: Forward and Backward Fill ---")
# Reading the CSV without the tab separator
df_zomato = pd.read_csv('zomato_restaurants.tsv')

rating_col = 'rate' 

if rating_col not in df_zomato.columns:
    print("Columns found by pandas:", df_zomato.columns.tolist())
else:
    missing_before = df_zomato[rating_col].isnull().sum()
    print(f"Missing values in '{rating_col}' before fill: {missing_before}")

    df_zomato[rating_col] = df_zomato[rating_col].ffill()
    df_zomato[rating_col] = df_zomato[rating_col].bfill()

    missing_after = df_zomato[rating_col].isnull().sum()
    print(f"Missing values in '{rating_col}' after fill: {missing_after}")
print("\n")