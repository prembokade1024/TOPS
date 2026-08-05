import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# TASK 1: Zomato Delivery Times (Histplot)
print("--- TASK 1: Zomato Delivery Times ---")
# Simulating delivery times (in minutes) for 50 orders using a normal distribution
delivery_times = np.random.normal(loc=35, scale=8, size=50)

plt.figure(figsize=(8, 5))
# kde=True adds the smooth curve over the bars
sns.histplot(delivery_times, bins=10, kde=True, color='tomato')
plt.title("Distribution of Zomato Delivery Times (50 Orders)")
plt.xlabel("Delivery Time (minutes)")
plt.ylabel("Frequency")
plt.show()
plt.close()


# TASK 2: Tips Dataset (Boxplot)
print("--- TASK 2: Tips Dataset by Weekday ---")
# Seaborn comes with built-in datasets; we load 'tips' directly
df_tips = sns.load_dataset('tips')

plt.figure(figsize=(8, 5))
# hue='day' is used in modern Seaborn alongside a palette to color the boxes
sns.boxplot(x='day', y='total_bill', data=df_tips, hue='day', palette='Set2', legend=False)
plt.title("Total Bill Amounts by Day of the Week")
plt.xlabel("Day of the Week")
plt.ylabel("Total Bill ($)")
plt.show()
plt.close()

# TASK 3: IPL Match Scores (Violinplot)
print("--- TASK 3: IPL Run Distributions ---")
# Apply the requested darkgrid theme
sns.set_theme(style="darkgrid")

try:
    # Using your local dataset instead of simulating from scratch
    df_ipl = pd.read_csv('ipl_matches.csv')
    
    # Filter for matches won by runs
    df_runs = df_ipl[df_ipl['win_by_runs'] > 0]
    
    # Identify the top 8 teams with the most wins by runs to keep the plot clean
    top_8_teams = df_runs['winner'].value_counts().head(8).index
    df_top_teams = df_runs[df_runs['winner'].isin(top_8_teams)]
    
    plt.figure(figsize=(12, 6))
    sns.violinplot(
        x='winner', 
        y='win_by_runs', 
        data=df_top_teams, 
        hue='winner', 
        palette='muted',
        legend=False
    )
    plt.xticks(rotation=45)
    plt.title("Distribution of Winning Margins (by Runs) for Top 8 IPL Teams")
    plt.xlabel("Team")
    plt.ylabel("Win Margin (Runs)")
    plt.tight_layout() # Ensures the labels don't get cut off
    
    plt.show()
    plt.close()
    
except FileNotFoundError:
    print("File 'ipl_matches.csv' not found. Ensure it is in the same directory.")
except Exception as e:
    print(f"An error occurred while plotting IPL data: {e}")


# TASK 4: Spotify Genres (Countplot)
print("--- TASK 4: Spotify Genres Countplot ---")
sns.set_theme(style="white") 

# Creating a mock dataset of 40 tracks across 4 distinct genres
genres_data = ['Pop']*15 + ['Hip Hop']*10 + ['Rock']*8 + ['Classical']*7
df_spotify = pd.DataFrame({'Genre': genres_data})

plt.figure(figsize=(8, 5))
sns.countplot(x='Genre', data=df_spotify, hue='Genre', palette='pastel', legend=False)
plt.title("Number of Spotify Songs per Genre (40 Tracks)")
plt.xlabel("Genre")
plt.ylabel("Song Count")
plt.show()
plt.close()

# TASK 5: Daily Step Counts (KDE Plot)
print("--- TASK 5: Daily Step Counts KDE ---")
# Apply the requested whitegrid theme
sns.set_theme(style="whitegrid")

# Simulating 7 days of step count data
step_counts = np.random.normal(loc=8500, scale=1200, size=7) 

plt.figure(figsize=(8, 5))
# fill=True shades the area under the density curve
sns.kdeplot(step_counts, fill=True, color='mediumseagreen', alpha=0.5)
plt.title("Density Distribution of Daily Step Counts (Past Week)")
plt.xlabel("Number of Steps")
plt.ylabel("Density")
plt.show()
plt.close()