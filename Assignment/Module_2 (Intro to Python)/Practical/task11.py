# 11.Write a Python program to unzip a list of tuples into individual lists.
def unzip_tuples(list_of_tuples):
    # The '*' operator unpacks the list of tuples into separate arguments for zip()
    # zip() then pairs the first elements together, the second elements together, etc.
    return list(zip(*list_of_tuples))

data = [(1, 'a'), (2, 'b'), (3, 'c')]

# Unzipping
result = unzip_tuples(data)

# Converting result (which is a list of tuples) into two separate lists
list1, list2 = result

print(f"Original: {data}")
print(f"List 1: {list1}")
print(f"List 2: {list2}")