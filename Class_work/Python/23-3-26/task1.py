# file management
# file = open("task2.txt","w")
# file.write("write method")
# file.close()

# file = open("task2.txt","r")
# print(file.read())
# file.close()

# l = []

# for i in range(1,31):
#     l.append(i)
# file = open("task3.txt","w")
# file.write(str(l))
# file.close()

# import os

# os.rename("task2.txt","task.txt")
# os.remove("task2.txt")

# file = open("task.txt","w+")
# file.write("hello")
# print(file.tell())
# file.seek(0)
# print(file.read())
# file.close()

# import random

# file = "task.txt"

# while True:
#     menu = """
#     Press 1 for Sign-up
#     Press 2 for Login
#     Press 3 for Forgot Password
#     Press 4 for Exit
#     """
#     print(menu)

#     choice = int(input("Enter your choice: "))

#     # SIGN-UP (APPEND)
#     if choice == 1:
#         name = input("Enter your name: ")
#         email = input("Enter email: ")
#         mno = input("Enter mobile number: ")
#         password = input("Enter password: ")
#         c_password = input("Confirm password: ")

#         if password == c_password:
#             with open(file, "a") as f:   # append mode
#                 f.write(f"{name},{email},{mno},{password}\n")
#             print("Signed up successfully!!")
#         else:
#             print("Password mismatch")

#     # LOGIN (READ)
#     elif choice == 2:
#         email = input("Enter email: ")
#         password = input("Enter password: ")

#         found = False

#         with open(file, "r") as f:   # read mode
#             for line in f:
#                 data = line.strip().split(",")
#                 if data[1] == email and data[3] == password:
#                     print("Login successful!!")
#                     found = True
#                     break

#         if not found:
#             print("Invalid Credentials")

#     # FORGOT PASSWORD (READ + WRITE)
#     elif choice == 3:
#         mno = input("Enter mobile number: ")

#         lines = []
#         found = False

#         with open(file, "r") as f:
#             lines = f.readlines()

#         with open(file, "w") as f:   # overwrite file
#             for line in lines:
#                 data = line.strip().split(",")

#                 if data[2] == mno:
#                     otp = random.randint(1000, 9999)
#                     print("OTP:", otp)

#                     uotp = int(input("Enter OTP: "))

#                     if uotp == otp:
#                         new_password = input("Enter new password: ")
#                         data[3] = new_password
#                         found = True
#                         print("Password updated!!")

#                 f.write(",".join(data) + "\n")

#         if not found:
#             print("Mobile number not found")

#     elif choice == 4:
#         print("Thank you!!")
#         break

#     else:
#         print("Invalid choice")