# 4. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
def swap_first_two_chars(str1, str2):
    if len(str1) < 2 or len(str2) < 2:
        return "Strings must be at least 2 characters long."
    

    str1_prefix = str1[:2]
    str2_prefix = str2[:2]
    

    new_str1 = str2_prefix + str1[2:]
    new_str2 = str1_prefix + str2[2:]
    
    return f"{new_str1} {new_str2}"

a = input("Enter a string : ")
b = input("Enter a string : ")

result = swap_first_two_chars(a, b)
print(f"Original: {a}, {b}")
print(f"Swapped:  {result}")

