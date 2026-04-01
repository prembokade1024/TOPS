s = "Python Programming"

print(len(s)) # finds the length of string including space
print(s.capitalize()) # capitilizes the first character of string
print(s.upper()) # capitalizes the whole string
print(s.lower()) # converts capitalized string into small character  
print(s.count("P")) # counts the character occurred how many times in string
print(s.center(30,"*")) # gives spacing or centre's string
print(s.find("r",8)) # finds character from given index
print(s.replace("P","A")) # replaces the character with given character
print(s.isalnum()) # finds the string is alphanumeric or not?
print(s.isalpha()) # finds the string is alpha or not?
print(s.swapcase()) # converts capitalized string into small character

s1 = "hellopython"
x = '-'.join(s) # it works like hyphon 
print(x)

