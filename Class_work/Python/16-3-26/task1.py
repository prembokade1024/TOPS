import random
d = {}

while True:
    menu = """
    Press 1 for Sign-up
    Press 2 for Login
    Press 3 for Forgot Password
    Press 4 for Exit
    """
    print(menu)

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter your name: ")
        email = input("Enter email: ")
        mno = int(input("Enter mobile number: "))
        password = input("Enter password: ")
        c_password = input("Confirm password: ")

        if password == c_password:
            d['name'] = name
            d['email'] = email
            d['mno'] = mno
            d['password'] = password
            print("Signed up successfully!!")
        else:
            print("Password and Confirm Password do not match.")

    elif choice == 2:
        email = input("Enter email: ")
        password = input("Enter password: ")

        if d['email'] == email and d['password'] == password:
            print("Login successfully!!")
        else:
            print("Invalid Credentials")

    elif choice == 3:
        mno = int(input("Enter mobile number: "))

        if d['mno'] == mno:
            otp = int(random.randint(1000,9999))
            print(otp)
            uotp = int(input("Enter Otp: "))
            if uotp == otp:
                new_password = input("Enter new password: ")
                d['password'] = new_password
            print("Password updated!!")
        else:
            print("Invalid input")

    elif choice == 4:
        print("Thank you!!")
        break

    else:
        print("Invalid choice")