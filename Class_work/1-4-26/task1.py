class abc:

    def fun1(self):
        n = int(input("Enter a value : "))
        res = 0

        while n > 0:
            digit = n % 10
            res = res * 10 + digit
            n = n // 10

        print("Reversed number :", res)


    def fun2(self):
        l = list(map(int, input("Enter list elements: ").split()))
        l.sort()
        print("Ascending :", l)

        l.sort(reverse=True)
        print("Descending :", l)


    def fun3(self):
        l = [26, 42, 11, 24, 21, 11]
        uni = []
        dup = []

        for i in range(len(l)):
            j = l[i]
            if j not in uni:
                uni.append(j)
            else:
                dup.append(uni.index(j))
                dup.append(i)

        print("Duplicate index:", dup)


    def fun4(self):
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
                    print("Password mismatch!")

            elif choice == 2:
                email = input("Enter email: ")
                password = input("Enter password: ")

                if d.get('email') == email and d.get('password') == password:
                    print("Login successfully!!")
                else:
                    print("Invalid Credentials")

            elif choice == 3:
                mno = int(input("Enter mobile number: "))

                if d.get('mno') == mno:
                    otp = random.randint(1000, 9999)
                    print("OTP:", otp)

                    uotp = int(input("Enter OTP: "))
                    if uotp == otp:
                        new_password = input("Enter new password: ")
                        d['password'] = new_password
                        print("Password updated!!")
                    else:
                        print("Wrong OTP")
                else:
                    print("Invalid mobile number")

            elif choice == 4:
                print("Thank you!!")
                break

            else:
                print("Invalid choice")


# Object creation
obj = abc()

# obj.fun1()
# obj.fun2()
# obj.fun3()
obj.fun4() 