# 16.Counting the frequencies in a list using a dictionary in Python. 
# Input : [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]
# Expected output : 1 : 5 , 2 : 4 , 3 : 3 , 4 : 3 , 5 : 2

def count_frequencies(input_list):
    # Initialize an empty dictionary to store counts
    frequencies = {}
    
    for item in input_list:
        # Check if item exists in dictionary
        if item in frequencies:
            frequencies[item] += 1
        else:
            # If new item, initialize count to 1
            frequencies[item] = 1
            
    return frequencies

data = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
result = count_frequencies(data)

# Printing the output
for key, value in sorted(result.items()):
    print(f"{key} : {value}")