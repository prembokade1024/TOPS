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
        self.details = (self.user_id, self.name, self.password)

def generate_password(user_input):
    try:
        words = user_input.split()
        if not words:
            raise ValueError("Input cannot be empty.")

        base_word = random.choice(words)

        specials = "!@#$%^&*"
        numbers = string.digits
        caps = string.ascii_uppercase

        password = base_word + ''.join(secrets.choice(specials + numbers + caps) for _ in range(6))

        if len(password) <= 8:
            password += "A1!"

        return password
    except Exception as e:
        return f"Error generating password : {e}"

try:
    user_id = int(input("Enter User_id : "))
    name = input("Enter Name : ")
    raw_input_text = input("Enter words for password generation : ")

    user1 = User(user_id, name)

    generated_pwd = generate_password(raw_input_text)
    user1.set_password(generated_pwd)

    print("\nGenerated Password : ", generated_pwd)
    print("User Details : ", user1.details)

except ValueError as ve:
    print("Error : ", ve)
except Exception as e:
    print("Unexpected Error:", e)