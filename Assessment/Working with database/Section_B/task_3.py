import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

data = {
    'order_id': list(range(1, 21)) + [1, 2, 3],
    'customer_name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy',
                      'Mallory', 'Nina', 'Oscar', 'Peggy', 'Quentin', 'Romeo', 'Sybil', 'Trent', 'Victor', 'Walter'] + ['Alice', 'Bob', 'Charlie'],
    'restaurant_name': ['Rest_A', 'Rest_B', 'Rest_C', 'Rest_A', 'Rest_B'] * 4 + ['Rest_A', 'Rest_B', 'Rest_C'],
    'category': ['Fast Food', 'Healthy', 'Indian', 'Fast Food', None] * 4 + ['Fast Food', 'Healthy', 'Indian'], 
    'delivery_time_mins': [25, 30, np.nan, 45, 20, 35, 40, np.nan, 22, 28] * 2 + [25, 30, np.nan], 
    'order_value': [15.5, 22.0, 18.5, 120.0, np.nan, 14.0, 25.5, 33.0, np.nan, 19.0] * 2 + [15.5, 22.0, 18.5], 
    'rating': [4.5, 3.0, 4.0, np.nan, 5.0, 4.2, 3.8, np.nan, 4.7, 2.5] * 2 + [4.5, 3.0, 4.0]
}
df = pd.DataFrame(data)


print("TASK 3: Matplotlib & Seaborn Visualisation")

# 1. Setup figure
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1 (top-left): Countplot
sns.countplot(data=df, x='category',hue='category', ax=axes[0, 0], palette='viridis',legend=False)
axes[0, 0].set_title('Order Count per Category')
axes[0, 0].set_xlabel('Category')
axes[0, 0].set_ylabel('Order Count')

# Plot 2 (top-right): Boxplot
sns.boxplot(data=df, x='category', y='delivery_time_mins', hue='category',ax=axes[0, 1], palette='Set2',legend=False)
axes[0, 1].set_title('Delivery Time Distribution by Category')
axes[0, 1].set_xlabel('Category')
axes[0, 1].set_ylabel('Delivery Time (mins)')

# Plot 3 (bottom-left): Horizontal Bar Chart (Matplotlib)
avg_order_value = df.groupby('restaurant_name')['order_value'].mean().sort_values()
axes[1, 0].barh(avg_order_value.index, avg_order_value.values, color='skyblue')
axes[1, 0].set_title('Average Order Value per Restaurant')
axes[1, 0].set_xlabel('Avg Order Value ($)')
axes[1, 0].set_ylabel('Restaurant Name')

# Plot 4 (bottom-right): Heatmap of correlation matrix
numeric_cols = df.select_dtypes(include=[np.number])
corr_matrix = numeric_cols.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=axes[1, 1], fmt=".2f")
axes[1, 1].set_title('Correlation Matrix of Numeric Columns')

# Layout and Save
plt.tight_layout()
file_name = 'food_delivery_dashboard.png'
plt.savefig(file_name, dpi=150, bbox_inches='tight')
print(f"Visualisation dashboard successfully saved as '{file_name}'.")