import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# TASK 1: Line Plot for Daily Steps
print("--- TASK 1: Generating Daily Steps Line Plot ---")
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
steps = [6500, 7200, 5800, 8100, 7500, 10200, 4300]

plt.figure(figsize=(8, 5))
plt.plot(days, steps, marker='o', linestyle='-', color='b')
plt.title('Daily Steps Over the Last 7 Days')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Steps')
plt.grid(True, linestyle='--', alpha=0.6)

# Save the plot as requested
plt.savefig('steps_lineplot.png')
plt.show() 
plt.close() 

# TASK 2: Scatter Plot for Zomato Restaurants
print("--- TASK 2: Generating Zomato Scatter Plot ---")
ratings = [3.5, 4.2, 4.8, 3.1, 4.0, 4.5, 2.9, 3.8, 4.9, 3.7]
prices = [350, 600, 1200, 200, 500, 800, 150, 400, 1500, 450]

plt.figure(figsize=(8, 5))
plt.scatter(ratings, prices, color='darkorange', s=100, alpha=0.7, edgecolors='black')
plt.title('Restaurant Ratings vs. Average Meal Price')
plt.xlabel('Zomato Rating (out of 5)')
plt.ylabel('Average Meal Price (₹)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
plt.close()

# TASK 3: Bar Chart for Food Orders
print("--- TASK 3: Generating Food Orders Bar Chart ---")
platforms = ['Swiggy', 'Zomato', 'Domino\'s']
orders = [12, 18, 5]
colors = ['orange', 'red', 'blue']

plt.figure(figsize=(7, 5))
# Creating the bar chart. To add a legend, we loop through and plot each bar individually
for i in range(len(platforms)):
    plt.bar(platforms[i], orders[i], color=colors[i], label=platforms[i])

plt.title('Food Delivery Orders in the Last Month')
plt.xlabel('Platform')
plt.ylabel('Number of Orders')
plt.legend(title="Platforms")
plt.show()
plt.close()

# TASK 4: Histogram of Spotify Listening Sessions
print("--- TASK 4: Generating Spotify Histogram ---")
spotify_durations = [15, 22, 45, 12, 60, 35, 28, 110, 18, 40, 
                     25, 30, 50, 10, 90, 42, 20, 55, 15, 33]

plt.figure(figsize=(8, 5))
plt.hist(spotify_durations, bins=5, color='mediumpurple', edgecolor='black')
plt.title('Distribution of Spotify Listening Session Durations')
plt.xlabel('Duration (Minutes)')
plt.ylabel('Frequency')
plt.show()
plt.close()

# TASK 5: Subplots for Instagram Usage
print("--- TASK 5: Generating Instagram Subplots ---")
ig_days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
screen_time = [45, 60, 40, 55, 90, 120, 110] # in minutes
posts_liked = [15, 25, 10, 20, 45, 60, 50]

# Create a figure with 2 subplots arranged horizontally (1 row, 2 columns)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Subplot 1: Line plot for screen time
ax1.plot(ig_days, screen_time, color='magenta', marker='o', linewidth=2)
ax1.set_title('Daily Instagram Screen Time')
ax1.set_xlabel('Day')
ax1.set_ylabel('Minutes')
ax1.grid(True, linestyle=':', alpha=0.6)

# Subplot 2: Bar chart for liked posts
ax2.bar(ig_days, posts_liked, color='cyan', edgecolor='black')
ax2.set_title('Number of Instagram Posts Liked')
ax2.set_xlabel('Day')
ax2.set_ylabel('Likes Count')

# Adjust overlap layout
plt.tight_layout()

# Save the figure as requested
plt.savefig('social_media_usage.png')
plt.show()
plt.close()
