# 14.Write a Python program to find the highest 3 values in a dictionary.
import heapq

def find_top_three_values(d):
    # Method 1: Using sorting (Simple and readable)
    # Sort items by value (index 1) in descending order, then take the first 3
    sorted_items = sorted(d.items(), key=lambda item: item[1], reverse=True)
    return sorted_items[:3]

    # Method 2: Using heapq (Efficient for large dictionaries)
    # heapq.nlargest is faster (O(n log k) vs O(n log n)) for large datasets
    # return heapq.nlargest(3, d.items(), key=lambda item: item[1])

my_dict = {
    'Apple': 50, 
    'Orange': 25, 
    'Banana': 80, 
    'Grapes': 65, 
    'Mango': 90
}

top_three = find_top_three_values(my_dict)

print(f"Top 3 values in dictionary: {top_three}")