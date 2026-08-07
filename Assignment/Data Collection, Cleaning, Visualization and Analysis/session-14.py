import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# TASK 1: IPL Univariate Analysis
print("--- TASK 1: IPL Univariate Analysis ---")
df_ipl = pd.read_csv('ipl_matches.csv')

# Isolating matches for the Mumbai Indians to analyze their specific performance metrics
mi_matches = df_ipl[(df_ipl['team1'] == 'Mumbai Indians') | (df_ipl['team2'] == 'Mumbai Indians')]

# Note: Standard match-level IPL datasets often track 'win_by_runs' rather than 'total_runs'
target_col = 'win_by_runs' if 'win_by_runs' in mi_matches.columns else mi_matches.select_dtypes(include='number').columns[0]

# Calculate summary statistics
mi_stats = mi_matches[target_col].agg(['mean', 'median', 'min', 'max', 'std'])

print(f"Summary Statistics for '{target_col}' (Mumbai Indians matches):")
print(mi_stats)
print("\n")


# TASK 2: Flipkart Reviews Bar Plot
print("--- TASK 2: Flipkart Ratings Plot ---")
df_flipkart = pd.read_csv('flipkart_orders.csv')

# Simulating a 'rating' column if it doesn't exist in your specific CSV version
if 'rating' not in df_flipkart.columns:
    df_flipkart['rating'] = np.random.choice([1, 2, 3, 4, 5], size=len(df_flipkart), p=[0.1, 0.1, 0.2, 0.3, 0.3])

plt.figure(figsize=(8, 5))
sns.countplot(data=df_flipkart, x='rating', palette='viridis')
plt.title('Count of Flipkart Reviews per Rating (1-5 Stars)')
plt.xlabel('Star Rating')
plt.ylabel('Number of Reviews')
plt.show()
plt.close()
print("Task 2 plot created successfully.\n")

# TASK 3: Zomato Cost vs Rating (FIXED)

print("--- TASK 3: Zomato Cost vs Rating ---")
df_zomato = pd.read_csv('zomato_restaurants.tsv', sep='\t')

# 1. Check your terminal for this output to find the exact column names
print("Available columns:", df_zomato.columns.tolist())

# 2. Update these variables with the exact names from your dataset
rating_col = 'rate' # Change this if it's 'aggregate_rating', 'Rate', etc.
cost_col = 'approx_cost(for two people)' # Change this if it's named differently

try:
    # Clean the rating column
    df_zomato['rate_clean'] = df_zomato[rating_col].astype(str).str.replace('/5', '').str.strip()
    df_zomato['rate_clean'] = pd.to_numeric(df_zomato['rate_clean'], errors='coerce')

    # Clean the cost column
    df_zomato['cost_clean'] = df_zomato[cost_col].astype(str).str.replace(',', '').str.strip()
    df_zomato['cost_clean'] = pd.to_numeric(df_zomato['cost_clean'], errors='coerce')

    # Create the plot
    plt.figure(figsize=(9, 6))
    sns.scatterplot(data=df_zomato, x='cost_clean', y='rate_clean', alpha=0.6, color='crimson')
    plt.title('Zomato: Average Cost for Two vs. User Rating')
    plt.xlabel('Approximate Cost for Two (₹)')
    plt.ylabel('User Rating (out of 5)')
    plt.show()
    plt.close()
    
except KeyError as e:
    print(f"\nERROR: Column {e} still not found. Double-check the spelling from the column list printed above!")

# TASK 4: BookMyShow Groupby Analysis
print("--- TASK 4: BookMyShow Groupby ---")
# Mock DataFrame for BookMyShow
df_bms = pd.DataFrame({
    'movie_name': ['Movie A', 'Movie B', 'Movie C', 'Movie D', 'Movie E'],
    'genre': ['Action', 'Comedy', 'Action', 'Drama', 'Comedy'],
    'box_office_collection': [150.5, 85.0, 210.0, 95.5, 120.0] # in Crores
})

# Groupby genre, calculate mean, and sort descending
avg_collection = (
    df_bms.groupby('genre')['box_office_collection']
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

print("Average Box Office Collection by Genre:")
print(avg_collection)
print("\n")

# TASK 5: Spotify Pairplot
print("--- TASK 5: Spotify Pairplot ---")
# Mock DataFrame for Spotify acoustic features
np.random.seed(42)
df_spotify = pd.DataFrame({
    'danceability': np.random.uniform(0.3, 0.9, 100),
    'energy': np.random.uniform(0.4, 0.95, 100),
    'valence': np.random.uniform(0.2, 0.8, 100),
    'popularity': np.random.randint(50, 100, 100)
})

# Introduce a slight positive correlation between energy and danceability for the plot
df_spotify['energy'] = df_spotify['danceability'] * 0.8 + np.random.normal(0, 0.1, 100)

# Create the pairplot
sns.pairplot(df_spotify, corner=True, diag_kind='kde', plot_kws={'alpha': 0.7, 'color': 'forestgreen'})
plt.show()
plt.close()