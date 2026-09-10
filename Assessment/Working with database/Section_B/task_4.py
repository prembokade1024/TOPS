import pandas as pd
import numpy as np
from sqlalchemy import create_engine, text

print("TASK 4: SQL & Python Performance Report : ")

# 1. Configure MySQL Connection using SQLAlchemy
db_user = "root"
db_password = "root" 
db_host = "localhost"
db_name = "food_delivery"

# Initial connection to create the database (if it doesn't exist)
server_engine = create_engine(f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}/")
with server_engine.connect() as conn:
    conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {db_name}"))

# Connect to the newly created
engine = create_engine(f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}/{db_name}")

# 2. Create Tables and Insert Data
with engine.begin() as conn: # .begin() auto-commits the transactions
    # Drop tables if they exist to start fresh
    conn.execute(text("DROP TABLE IF EXISTS orders"))
    conn.execute(text("DROP TABLE IF EXISTS restaurants"))

    # Create Tables
    conn.execute(text('''
        CREATE TABLE restaurants (
            restaurant_id INT PRIMARY KEY,
            name VARCHAR(255),
            category VARCHAR(100),
            city VARCHAR(100)
        )
    '''))

    conn.execute(text('''
        CREATE TABLE orders (
            order_id INT PRIMARY KEY,
            restaurant_id INT,
            order_value FLOAT,
            delivery_time_mins FLOAT,
            rating FLOAT,
            FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id)
        )
    '''))

    # Insert Restaurant Data
    rest_data = [
        (1, 'Spicy Bites', 'Indian', 'NY'), (2, 'Burger King', 'Fast Food', 'LA'),
        (3, 'Green Bowl', 'Healthy', 'NY'), (4, 'Sushi Hub', 'Japanese', 'LA'),
        (5, 'Pizza Point', 'Italian', 'NY'), (6, 'Taco Fiesta', 'Mexican', 'LA'),
        (7, 'Wok Way', 'Chinese', 'NY'), (8, 'Sweet Treats', 'Dessert', 'LA')
    ]
    for row in rest_data:
        conn.execute(text("INSERT INTO restaurants VALUES (:1, :2, :3, :4)"), 
                     {"1": row[0], "2": row[1], "3": row[2], "4": row[3]})

    # Generate and Insert 25 Sample Orders
    np.random.seed(1)
    orders_data = [
        (i, int(np.random.randint(1, 9)), float(round(np.random.uniform(10, 50), 2)), 
         float(np.random.randint(15, 45)), float(round(np.random.uniform(3.5, 5.0), 1))) 
        for i in range(1, 26)
    ]
    for row in orders_data:
         conn.execute(text("INSERT INTO orders VALUES (:1, :2, :3, :4, :5)"),
                      {"1": row[0], "2": row[1], "3": row[2], "4": row[3], "5": row[4]})


# 3. SQL Query using Pandas read_sql_query
query = """
SELECT 
    r.name,
    COUNT(o.order_id) as total_orders,
    SUM(o.order_value) as total_revenue,
    ROUND(AVG(o.rating), 2) as avg_rating
FROM restaurants r
LEFT JOIN orders o ON r.restaurant_id = o.restaurant_id
GROUP BY r.restaurant_id, r.name
"""

# Pandas requires the query to be wrapped in text() and passed with an active connection
with engine.connect() as conn:
    sql_df = pd.read_sql_query(text(query), conn)

# 4. Add Rank Column and Sort
sql_df['total_revenue'] = sql_df['total_revenue'].fillna(0) 
sql_df['revenue_rank'] = sql_df['total_revenue'].rank(ascending=False, method='min').astype(int)
sql_df = sql_df.sort_values(by='revenue_rank', ascending=True)

print("Full Restaurant Performance Table:")
print(sql_df.to_string(index=False))

# 5. Print Top 5 and Export
top_5 = sql_df.head(5)
print("\nTop 5 Restaurants by Total Revenue:")
print(top_5.to_string(index=False))

csv_filename = 'restaurant_performance_report_mysql.csv'
sql_df.to_csv(csv_filename, index=False)
print(f"\nReport exported successfully to {csv_filename}")