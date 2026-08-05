import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# TASK 1: 2x2 Grid of Subplots
print("--- TASK 1: 2x2 Subplot Grid ---")
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Line Plot
axs[0, 0].plot(['A', 'B', 'C', 'D'], [10, 20, 15, 30], color='blue', marker='o')
axs[0, 0].set_title('Line Plot')

# Bar Chart
axs[0, 1].bar(['X', 'Y', 'Z'], [50, 30, 40], color='green')
axs[0, 1].set_title('Bar Chart')

# Scatter Plot
axs[1, 0].scatter([1, 2, 3, 4, 5], [5, 2, 8, 4, 6], color='red')
axs[1, 0].set_title('Scatter Plot')

# Pie Chart
axs[1, 1].pie([25, 35, 40], labels=['Part 1', 'Part 2', 'Part 3'], autopct='%1.1f%%')
axs[1, 1].set_title('Pie Chart')

plt.tight_layout()
plt.show()
plt.close()

# TASK 2: Styled Bar Chart for Delivery Apps
print("--- TASK 2: Styled Bar Chart ---")
platforms = ['Zomato', 'Swiggy', "Domino's"]
avg_times = [35, 42, 25]  # Delivery times in minutes
colors = ['lightcoral', 'orange', 'lightblue']

fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(platforms, avg_times, color=colors, edgecolor='black')

bars[0].set_linestyle('--')
bars[0].set_linewidth(2)

bars[1].set_linestyle('-.')
bars[1].set_linewidth(3)

bars[2].set_linestyle(':')
bars[2].set_linewidth(4)

ax.set_title('Average Delivery Times Comparison')
ax.set_ylabel('Time (Minutes)')
ax.set_xlabel('Platform')

plt.show()
plt.close()

# TASK 3: Multi-Axis Chart (Instagram)
print("--- TASK 3: Multi-Axis Chart ---")
influencers = ['User A', 'User B', 'User C', 'User D', 'User E']
followers = [10000, 45000, 20000, 80000, 35000]
daily_posts = [1.2, 3.5, 0.8, 4.0, 2.0]

fig, ax1 = plt.subplots(figsize=(9, 5))

# Plot Followers on left y-axis
ax1.plot(influencers, followers, color='blue', marker='o', label='Followers')
ax1.set_xlabel('Influencers')
ax1.set_ylabel('Number of Followers', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Create a second y-axis that shares the same x-axis
ax2 = ax1.twinx()

# Plot Daily Posts on right y-axis
ax2.plot(influencers, daily_posts, color='red', marker='s', linestyle='--', label='Avg Daily Posts')
ax2.set_ylabel('Average Daily Posts', color='red')
ax2.tick_params(axis='y', labelcolor='red')

plt.title('Instagram Influencers: Followers vs. Daily Posts')
fig.tight_layout()
plt.show()
plt.close()

# TASK 4: Scatter Plot with Annotations
print("--- TASK 4: Scatter Plot with Annotations ---")
movies = ['Pathaan', 'Jawan', 'Dangal', 'PK', 'Animal']
imdb_ratings = [5.9, 7.0, 8.3, 8.1, 6.2]
tickets_sold_millions = [3.2, 3.8, 4.5, 4.1, 3.0]

fig, ax = plt.subplots(figsize=(9, 6))
ax.scatter(imdb_ratings, tickets_sold_millions, color='purple', s=100)

# Loop through the data points to add the movie names as text
for i, txt in enumerate(movies):
    ax.annotate(
        txt, 
        (imdb_ratings[i], tickets_sold_millions[i]), 
        textcoords="offset points", 
        xytext=(0, 10), # Offset text by 10 points vertically
        ha='center',    # Center the text horizontally over the point
        fontsize=10
    )

ax.set_title('Bollywood Movies: IMDB Rating vs Tickets Sold')
ax.set_xlabel('IMDB Rating')
ax.set_ylabel('Tickets Sold (Millions)')
ax.grid(True, linestyle='--', alpha=0.5)

plt.show()
plt.close()

# TASK 5: Custom Text Annotation (Flipkart)
print("--- TASK 5: Custom Text Annotation ---")
months = ['Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [120, 135, 140, 450, 180, 210] # Huge spike in October

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(months, sales, marker='o', color='teal', linewidth=2)

# Find the peak value to annotate
max_sales = max(sales)
max_month = months[sales.index(max_sales)]

# Annotate the peak point
ax.annotate(
    'Big Billion Days', 
    xy=(max_month, max_sales),           # Point to annotate
    xytext=(max_month, max_sales + 50),  # Position of the text
    arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
    ha='center',
    fontsize=11,
    fontweight='bold',
    color='darkred'
)

# Adjust y-axis limit slightly higher to make room for the text
ax.set_ylim(0, max_sales + 100)
ax.set_title("Flipkart Monthly Sales (H2)")
ax.set_xlabel("Month")
ax.set_ylabel("Sales Volume")

plt.show()
plt.close()