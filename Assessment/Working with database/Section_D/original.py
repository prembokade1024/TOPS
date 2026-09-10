import pandas as pd
from sqlalchemy import create_engine, text
import matplotlib.pyplot as plt

def run_ai_report():
    try:
        engine = create_engine("mysql+mysqlconnector://root:root@localhost/food_delivery")
        
        # BUG 1: HAVING before GROUP BY
        query = """
            SELECT restaurant_name, AVG(rating) as avg_rating, SUM(order_value) as total_revenue, COUNT(order_id) as order_count
            FROM orders
            HAVING COUNT(order_id) >= 5
            GROUP BY restaurant_name
            ORDER BY avg_rating DESC
            LIMIT 3
        """
        
        with engine.connect() as conn:
            df = pd.read_sql_query(text(query), conn)
            
        # BUG 2: Fails to handle empty DataFrame properly before plotting
        
        # BUG 3: Integer division for percentage calculation
        total_rev = df['total_revenue'].sum()
        df['revenue_share_pct'] = (df['total_revenue'] // total_rev) * 100
        
        # BUG 4: Chart axes unlabelled
        plt.barh(df['restaurant_name'], df['avg_rating'])
        
        for index, value in enumerate(df['revenue_share_pct']):
            plt.text(df['avg_rating'][index], index, str(value) + '%')
            
        plt.show()

    except Exception as e:
        print("Database connection or query failed.")

run_ai_report()