import numpy as np

# 1. Create arrays with seed for reproducibility
np.random.seed(42)
orders = np.random.randint(100, 801, size=30)
revenue = np.random.uniform(5000, 50000, size=30)

# 2. Calculate general statistics
total_orders = np.sum(orders)
total_revenue = np.sum(revenue)
mean_orders = np.mean(orders)
std_orders = np.std(orders)
max_revenue_day = np.argmax(revenue)

print("TASK 1 : Analysis")
print(f"Total Orders: {total_orders}")
print(f"Total Revenue: ${total_revenue:,.2f}")
print(f"Mean Daily Orders: {mean_orders:.2f}")
print(f"Std Dev of Orders: {std_orders:.2f}")
print(f"Day with Highest Revenue: Day {max_revenue_day}")

# 3. Boolean Indexing for peak days (mean + 1 std)
threshold = mean_orders + std_orders
peak_days_mask = orders > threshold
peak_days_count = np.sum(peak_days_mask)
peak_days_revenue = np.sum(revenue[peak_days_mask])

print(f"\nPeak Days (> {threshold:.2f} orders): {peak_days_count}")
print(f"Total Revenue on Peak Days: ${peak_days_revenue:,.2f}")

# 4. Reshape to 5x6 matrix and sum axis=1
orders_matrix = orders.reshape(5, 6)
weekly_orders = np.sum(orders_matrix, axis=1)

print("\nTotal Orders per Weekly Block (5 blocks of 6 days):")
for i, block_total in enumerate(weekly_orders, 1):
    print(f"Block {i}: {block_total} orders")