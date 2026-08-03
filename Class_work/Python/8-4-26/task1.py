import random

class Bank:
    def __init__(self):
        self.bal = 0
        self.ac_no = random.randint(1001, 9999)

    def ac_register(self):
        print("--- Account Registration ---")
        name = input("Enter your name: ")
        email = input("Enter your Email : ")
        self.bal = 5000
        print("Registration Successful!!")
        print(f"Account Number : {self.ac_no}")
        print(f"Opening Balance: {self.bal}")

    def deposit(self):
        amount = int(input("Enter amount to deposit: "))
        if amount > 0:
            self.bal += amount
            print(f"Successfully deposited {amount}.")
            print(f"Current Balance: {self.bal}")
        else:
            print("Invalid amount. Please deposit a positive value.")

    def withdraw(self):
        amount = int(input("Enter amount to withdraw: "))
        if amount > self.bal:
            print("Transaction Denied: Insufficient Balance!")
        elif amount <= 0:
            print("Invalid amount. Please enter a value greater than 0.")
        else:
            self.bal -= amount
            print(f"Successfully withdrew {amount}.")
            print(f"Current Balance: {self.bal}")

    def check_bal(self):
        print(f"\n--- Account Statement ---")
        print(f"Account Number: {self.ac_no}")
        print(f"Current Available Balance: {self.bal}")
        print("--------------------------")

user_account = Bank()

print("1. Register Account")
print("2. Exit")
start_choice = input("Select an option: ")

if start_choice == "1":
    user_account.ac_register()
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")
        print("5. Returning to Main Menu")
        
        action = input("Choose an action (1-5): ")

        if action == "1":
            user_account.deposit()
        elif action == "2":
            user_account.withdraw()
        elif action == "3":
            user_account.check_bal()
        elif action == "4":
            print("Logged out successfully. Have a nice day!")
            break
        elif action == "5":
            break
        else:
            print("Invalid selection. Please try again.")
else:
    print("System Closed.")