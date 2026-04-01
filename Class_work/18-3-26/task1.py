import random

original = random.randint(1,51)

print("******Enter number between 1 to 50**********")
while True:
    choice = int(input("Enter a number between 1 to 50 : "))
    if choice > 50:
        print("Invalid number!!")
    elif choice == original:
        print("Win!!")
    elif choice > original:
        print("Original number is lesser than Entered number")
    else:
        print("Original number is greater than entered number")