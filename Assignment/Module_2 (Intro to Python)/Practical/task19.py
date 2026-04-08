# 19.Write a Python function that takes a list and returns a new list with unique elements of the first list.
def get_unique_list(input_list):
    return list(set(input_list))

my_list = [10, 20, 10, 30, 40, 30, 50]
unique_list = get_unique_list(my_list)

print(f"Original list: {my_list}")
print(f"Unique list:   {unique_list}")
