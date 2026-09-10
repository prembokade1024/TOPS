"""
Write a Python program that connects to a MySQL database named 'food_delivery' using SQLAlchemy. 
The database has an 'orders' table with columns: order_id, restaurant_name, category, order_value, rating, delivery_time_mins. 
Write a SQL query to find the top 3 restaurants by average customer rating, but filter out any restaurant that has fewer than 5 orders. 
Load the result into a Pandas DataFrame. Add a new column calculating each restaurant's revenue share as a percentage of the total revenue across ONLY these top 3 restaurants. 
Finally, plot a horizontal bar chart of the top 3 restaurants by average rating, and display the revenue share percentage as a label on each bar. 
Include error handling to print a user-friendly message if the connection fails or if the query returns an empty DataFrame, rather than crashing.
"""