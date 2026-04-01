# 13.Write a Python program to sort a dictionary (ascending /descending) by value.
def sort_dict_by_value(d, descending=False):
    """
    Sorts a dictionary by value.
    'reverse=descending' determines if the sort order is descending.
    """
    # d.items() gives us (key, value) pairs
    # key=lambda item: item[1] tells sorted() to look at the value (index 1)
    sorted_items = sorted(d.items(), key=lambda item: item[1], reverse=descending)
    
    # Convert back to a dictionary
    return dict(sorted_items)

my_dict = {'Apple': 10, 'Orange': 5, 'Banana': 20, 'Grapes': 15}

ascending = sort_dict_by_value(my_dict, descending=False)
descending = sort_dict_by_value(my_dict, descending=True)

print(f"Original: {my_dict}")
print(f"Ascending:  {ascending}")
print(f"Descending: {descending}")