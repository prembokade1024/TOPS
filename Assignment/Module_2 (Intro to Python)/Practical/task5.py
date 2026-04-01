# 5. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead If thestring length of the given string is less than 3, leave it unchanged.
def modify_string(s):
    # Check if the string length is less than 3
    if len(s) < 3:
        return s
    
    # Check if the string already ends with 'ing'
    if s.endswith('ing'):
        return s + 'ly'
    
    # Otherwise, add 'ing' to the end
    else:
        return s + 'ing'

test_strings = ["go", "walk", "sing"]

for text in test_strings:
    print(f"Original: {text} -> Result: {modify_string(text)}")