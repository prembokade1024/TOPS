import pandas as pd
import sweetviz as sv
import dtale

# TASK 1 & 4: Skipped due to Python 3.14 compatibility 
# (ydata-profiling requires Python < 3.14)
print("--- TASK 1 & 4: Skipped ---")
print("ydata-profiling is currently incompatible with Python 3.14.\n")

# TASK 2: Sweetviz Comparison Report
print("--- TASK 2: Zomato Sweetviz Comparison ---")
try:
    df_zomato = pd.read_csv('zomato_restaurants.tsv', sep='\t')
    
    midpoint = len(df_zomato) // 2
    df_zomato_part1 = df_zomato.iloc[:midpoint]
    df_zomato_part2 = df_zomato.iloc[midpoint:]

    # Create a comparison report between the two halves
    comparison_report = sv.compare(source=[df_zomato_part1, "Zomato First Half"], compare=[df_zomato_part2, "Zomato Second Half"])

    # Output the report to HTML
    comparison_report.show_html("zomato_comparison_report.html")
    print("Generated Sweetviz report. Check the browser to spot key differences.\n")
except FileNotFoundError:
    print("File 'zomato_restaurants.tsv' not found. Please ensure it exists.\n")

# TASK 3: D-Tale Interactive Exploration
print("--- TASK 3: Flipkart Data in D-Tale ---")
try:
    df_flipkart = pd.read_csv('flipkart_orders.csv')

    # Start the D-Tale server
    dtale_app = dtale.show(df_flipkart)

    # Print the URL so you can open it in your browser
    print(f"D-Tale server started! Click this link to explore: {dtale_app._main_url}")
    print("Instructions: Use the column header for 'price' to apply a filter (> 2000).\n")
except FileNotFoundError:
    print("File 'flipkart_orders.csv' not found.\n")

# TASK 5: Swiggy Summary Report (Sweetviz)
print("--- TASK 5: IPL Sweetviz Analysis ---")
try:
    # Adapting the Swiggy task to generate a summary report for your IPL dataset
    df_ipl = pd.read_csv('ipl_matches.csv')

    # Generate a single-file summary report using Sweetviz analyze()
    ipl_report = sv.analyze(df_ipl)

    # Output the report to HTML
    ipl_report.show_html("ipl_summary_report.html")
    print("Saved 'ipl_summary_report.html'.")
except FileNotFoundError:
    print("File 'ipl_matches.csv' not found.")