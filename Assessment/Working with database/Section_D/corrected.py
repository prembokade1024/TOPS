import pandas as pd
from sqlalchemy import create_engine, text
import matplotlib.pyplot as plt

def run_corrected_report():
    try:
        engine = create_engine("mysql+mysqlconnector://root:root@localhost/food_delivery")
        
        # FIX 1: Corrected SQL syntax (GROUP BY must come before HAVING)
        query = """
            SELECT restaurant_name, AVG(rating) as avg_rating, SUM(order_value) as total_revenue, COUNT(order_id) as order_count
            FROM orders
            GROUP BY restaurant_name
            HAVING COUNT(order_id) >= 5
            ORDER BY avg_rating DESC
            LIMIT 3
        """
        
        with engine.connect() as conn:
            df = pd.read_sql_query(text(query), conn)
            
        # FIX 2: Handle empty DataFrame explicitly to prevent crashes
        if df.empty:
            print("Notice: The query executed successfully, but returned no rows (e.g., no restaurants have >= 5 orders).")
            return
            
        # FIX 3: Fixed division for percentage (using true float division)
        total_rev = df['total_revenue'].sum()
        df['revenue_share_pct'] = (df['total_revenue'] / total_rev) * 100
        
        # Plotting
        plt.figure(figsize=(10, 6))
        bars = plt.barh(df['restaurant_name'], df['avg_rating'], color='teal')
        
        # FIX 4: Added title and axis labels
        plt.title('Top 3 Restaurants by Average Rating (Minimum 5 Orders)')
        plt.xlabel('Average Customer Rating (Out of 5.0)')
        plt.ylabel('Restaurant Name')
        
        # Add labels on bars
        for bar, pct in zip(bars, df['revenue_share_pct']):
            plt.text(bar.get_width() - 0.5, bar.get_y() + bar.get_height()/2, 
                     f'{pct:.1f}% Rev Share', 
                     va='center', ha='right', color='white', fontweight='bold')
            
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Error: Unable to complete the operation. Details: {e}")

run_corrected_report()
"""
Note:
I fixed four main issues in the original code. 
First, I moved the HAVING clause to immediately follow GROUP BY in the SQL query, as SQL syntax requires. 
Second, I added an if df.empty: check to gracefully exit and notify the user if no data matches the criteria, preventing a matplotlib crash. 
Third, I changed the integer division (//) to float division (/) to accurately calculate the percentage. 
Finally, I added a title and x/y labels to the chart to make it readable and interpretable.
"""