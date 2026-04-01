# 2. Write a Python program to count occurrences of a substring in a string.
def count_substring(main_string, sub_string):
    
    return main_string.count(sub_string)

text = "banana"
substring = "ana"
result = count_substring(text, substring)

print(f"The substring '{substring}' appears {result} time in '{text}'.")