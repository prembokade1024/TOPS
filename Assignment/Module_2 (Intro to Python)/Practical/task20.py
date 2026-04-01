# 20 Mini project :
# Problem Statement : Password Generator
# Make a program to generate a strong password using the input given by the user. 
# To generate a password, randomly take some words from the user input and then include numbers, special characters and capital letters to generate the password. 
# Also, keep a check that password length is more than 8 characters. 
# Note: Include Exception handling wherever required. 
#       Also, make a ‘User’ classand store the details like user id, name and password of each user as a tuple.
import random
import string
import secrets

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.password = None
        self.details = ()

    def set_password(self, password):
        if len(password) <= 8:
            raise ValueError("Password must be longer than 8 characters.")
        self.password = password
        # Storing details as a tuple: (user_id, name, password)
        self.details = (self.user_id, self.name, self.password)

def generate_password(user_input):
    try:
        words = user_input.split()
        if not words:
            raise ValueError("Input cannot be empty.")
        
        # Pick a random word from input
        base_word = random.choice(words)
        
        # Define character pools
        specials = "!@#$%^&*"
        numbers = string.digits
        caps = string.ascii_uppercase
        
        # Build password: base word + random additions
        password = base_word + ''.join(secrets.choice(specials + numbers + caps) for _ in range(6))
        
        if len(password) <= 8:
            password += "A1!" # Ensure minimum length if word was too short
            
        return password
    except Exception as e:
        return f"Error generating password: {e}"

try:
    user1 = User(101, "Alice")
    raw_input = "nature mountain adventure"
    
    generated_pwd = generate_password(raw_input)
    user1.set_password(generated_pwd)
    
    print(f"User Details: {user1.details}")
except ValueError as ve:
    print(ve)