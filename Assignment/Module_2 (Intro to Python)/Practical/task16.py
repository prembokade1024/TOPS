# 16.Counting the frequencies in a list using a dictionary in Python. 
# Input : [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]
# Expected output : 1 : 5 , 2 : 4 , 3 : 3 , 4 : 3 , 5 : 2

def count_frequencies(input_list):
    frequencies = {}
    
    for item in input_list:
        if item in frequencies:
            frequencies[item] += 1
        else:
            frequencies[item] = 1
            
    return frequencies

data = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
result = count_frequencies(data)

for key, value in sorted(result.items()):
    print(f"{key} : {value}")