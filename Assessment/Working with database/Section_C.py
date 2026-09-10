import pandas as pd
import numpy as np
from sqlalchemy import create_engine, text
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Global variables to store our data across menu options
global_df = None
sql_result_1 = None
sql_result_2 = None

def setup_mysql_db():
    """Helper function to set up a simulated MySQL database for Option 2."""
    db_user = "root"
    db_password = "root"
    db_host = "localhost"
    db_name = "capstone_food_delivery"
    
    # 1. Connect to MySQL server to create the database if it doesn't exist
    server_engine = create_engine(f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}/")
    with server_engine.connect() as conn:
        conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {db_name}"))
    
    # 2. Connect to the specific database
    engine = create_engine(f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}/{db_name}")
    
    with engine.begin() as conn:
        # Drop existing to start fresh
        conn.execute(text("DROP TABLE IF EXISTS orders"))
        conn.execute(text("DROP TABLE IF EXISTS restaurants"))
        
        # Create Tables
        conn.execute(text('''CREATE TABLE restaurants (
                            restaurant_id INT PRIMARY KEY, name VARCHAR(255), city VARCHAR(100), category VARCHAR(100))'''))
        conn.execute(text('''CREATE TABLE orders (
                            order_id INT PRIMARY KEY, restaurant_id INT, order_value FLOAT, delivery_time_mins FLOAT)'''))
        
        # Insert Data
        restaurants = [
            (1, 'Spicy Bites', 'New York', 'Indian'), (2, 'Burger King', 'Los Angeles', 'Fast Food'),
            (3, 'Green Bowl', 'New York', 'Healthy'), (4, 'Sushi Hub', 'Los Angeles', 'Japanese')
        ]
        for r in restaurants:
            conn.execute(text("INSERT INTO restaurants VALUES (:1, :2, :3, :4)"), 
                         {"1": r[0], "2": r[1], "3": r[2], "4": r[3]})
        
        orders = [
            (101, 1, 45.5, 30), (102, 1, 22.0, 25), (103, 2, 15.0, 15),
            (104, 3, 35.0, 40), (105, 4, 60.5, 35), (106, 2, 12.5, 20),
            (107, 3, 28.0, 30), (108, 4, 90.0, 45)
        ]
        for o in orders:
            conn.execute(text("INSERT INTO orders VALUES (:1, :2, :3, :4)"), 
                         {"1": o[0], "2": o[1], "3": o[2], "4": o[3]})
            
    return engine

def option_1_load_clean():
    global global_df
    print("\n--- Option 1: Load & Clean Data ---")
    
    # 1. Load Simulated Data (including missing values and duplicates)
    data = {
        'order_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2],
        'restaurant_name': ['Spicy Bites', 'Burger King', 'Green Bowl', 'Sushi Hub', 'Spicy Bites'] * 2 + ['Spicy Bites', 'Burger King'],
        'city': ['New York', 'Los Angeles', 'New York', 'Los Angeles', 'New York'] * 2 + ['New York', 'Los Angeles'],
        'category': ['Indian', 'Fast Food', 'Healthy', 'Japanese', None] * 2 + ['Indian', 'Fast Food'], 
        'delivery_time_mins': [30, 20, np.nan, 45, 25, 35, 15, np.nan, 40, 22, 30, 20], 
        'order_value': [45.5, 15.0, 35.0, 60.5, 22.0, 18.0, 200.0, 40.0, np.nan, 25.0, 45.5, 15.0] 
    }
    df = pd.DataFrame(data)
    
    print("BEFORE CLEANING:")
    print(f"Shape: {df.shape}")
    print(f"Null Values:\n{df.isnull().sum()}\n")
    
    # 2. Imputation Strategies
    df['delivery_time_mins'] = df['delivery_time_mins'].fillna(df['delivery_time_mins'].median())
    df['order_value'] = df['order_value'].fillna(df['order_value'].median())
    df['category'] = df['category'].fillna(df['category'].mode()[0])
    
    # 3. Remove Duplicates
    df = df.drop_duplicates()
    
    # 4. Detect and Cap Outliers (IQR Method)
    Q1 = df['order_value'].quantile(0.25)
    Q3 = df['order_value'].quantile(0.75)
    IQR = Q3 - Q1
    upper_fence = Q3 + 1.5 * IQR
    df['order_value'] = df['order_value'].clip(upper=upper_fence)
    
    print("AFTER CLEANING:")
    print(f"Shape: {df.shape}")
    print(f"Null Values:\n{df.isnull().sum()}")
    print(f"Outliers capped at: ${upper_fence:.2f}\n")
    
    global_df = df 
    print("Data successfully loaded and cleaned!")

def option_2_sql_analysis():
    global sql_result_1, sql_result_2
    print("\n--- Option 2: Run SQL Analysis ---")
    
    engine = setup_mysql_db()
    
    query1 = """
        SELECT restaurant_id, COUNT(order_id) as total_orders, SUM(order_value) as total_revenue, AVG(delivery_time_mins) as avg_delivery_time
        FROM orders
        GROUP BY restaurant_id
    """
    
    query2 = """
        SELECT r.name, r.city, o.order_id, o.order_value
        FROM restaurants r
        JOIN orders o ON r.restaurant_id = o.restaurant_id
    """
    
    # Pandas requires the query to be wrapped in text() with SQLAlchemy
    with engine.connect() as conn:
        sql_result_1 = pd.read_sql_query(text(query1), conn)
        sql_result_2 = pd.read_sql_query(text(query2), conn)
    
    print("\nQUERY 1 RESULTS (Aggregate metrics per restaurant):")
    print(sql_result_1.to_string(index=False))
    
    print("\nQUERY 2 RESULTS (Joined Order Details):")
    print(sql_result_2.to_string(index=False))

def option_3_view_charts():
    if global_df is None:
        print("\nError: Please run Option 1 (Load & Clean Data) first.")
        return
        
    print("\n--- Option 3: View Charts ---")
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    sns.countplot(data=global_df, x='category', hue='category', palette='pastel', ax=axes[0], legend=False)
    axes[0].set_title('Total Orders by Category')
    axes[0].set_xlabel('Restaurant Category')
    axes[0].set_ylabel('Number of Orders')
    
    sns.barplot(data=global_df, x='city', y='delivery_time_mins', hue='city', palette='muted', errorbar=None, ax=axes[1], legend=False)
    axes[1].set_title('Average Delivery Time by City')
    axes[1].set_xlabel('City')
    axes[1].set_ylabel('Avg Delivery Time (mins)')
    
    plt.tight_layout()
    plt.show()

def option_4_export_report():
    if global_df is None or sql_result_1 is None or sql_result_2 is None:
        print("\nError: Please run both Option 1 and Option 2 before exporting.")
        return
        
    print("\n--- Option 4: Export Report ---")
    file_path = 'food_delivery_report.xlsx'
    
    try:
        with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
            global_df.to_excel(writer, sheet_name='Cleaned Data', index=False)
            sql_result_1.to_excel(writer, sheet_name='SQL Aggregates', index=False)
            sql_result_2.to_excel(writer, sheet_name='SQL Joins', index=False)
            
        print(f"Success! Report saved to: {os.path.abspath(file_path)}")
    except Exception as e:
        print(f"Failed to export report. Error: {e}")

def main_menu():
    while True:
        print("\n" + "="*45)
        print(" FOOD DELIVERY ANALYTICS CONSOLE APPLICATION")
        print("="*45)
        print("1. Load & Clean Data")
        print("2. Run SQL Analysis")
        print("3. View Charts")
        print("4. Export Report")
        print("0. Exit")
        print("="*45)
        
        choice = input("Enter your choice (0-4): ")
        
        if choice == '1':
            option_1_load_clean()
        elif choice == '2':
            option_2_sql_analysis()
        elif choice == '3':
            option_3_view_charts()
        elif choice == '4':
            option_4_export_report()
        elif choice == '0':
            print("\nExiting application. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 0 and 4.")

if __name__ == "__main__":
    main_menu()