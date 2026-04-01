# 12.Write a Python program to convert a list of tuples into a dictionary
def convert_to_dict(list_of_tuples):
    # The dict() constructor automatically maps the first element 
    # of each tuple as the key and the second as the value.
    return dict(list_of_tuples)

data = [("a", 1), ("b", 2), ("c", 3)]
my_dict = convert_to_dict(data)

print(f"Original list of tuples: {data}")
print(f"Resulting dictionary: {my_dict}")