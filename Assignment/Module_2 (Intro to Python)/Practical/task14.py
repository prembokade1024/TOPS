# 14.Write a Python program to find the highest 3 values in a dictionary.

def find_top_three_values(d):
    sorted_items = sorted(d.items(), key=lambda item: item[1], reverse=True)
    return sorted_items[:3]

my_dict = {
    'Apple': 50, 
    'Orange': 25, 
    'Banana': 80, 
    'Grapes': 65, 
    'Mango': 90
}

top_three = find_top_three_values(my_dict)

print(f"Top 3 values in dictionary: {top_three}")