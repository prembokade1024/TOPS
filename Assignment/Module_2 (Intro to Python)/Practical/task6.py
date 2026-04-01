# 6. Write a Python program to find the first appearance of the substring 'not' and'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
def replace_not_poor(text):
    # Find the starting index of 'not' and 'poor'
    not_index = text.find('not')
    poor_index = text.find('poor')

    # Ensure both exist and 'not' comes before 'poor'
    if not_index != -1 and poor_index != -1 and not_index < poor_index:
        # Construct the string: 
        # Part before 'not' + 'good' + Part after 'poor'
        return text[:not_index] + 'good' + text[poor_index + 4:]
    
    return text

print(replace_not_poor("The lyrics are not that poor!"))
print(replace_not_poor("The lyrics are poor!"))
print(replace_not_poor("The lyrics are not good!"))