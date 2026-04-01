# 10.Write a Python program to get unique values from a list. 
def get_unique_ordered(numbers):
    unique_list = []
    for item in numbers:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

my_list = [1, 2, 2, 3, 4, 4, 5, 1]
print(f"Ordered Unique values: {get_unique_ordered(my_list)}")