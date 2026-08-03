# 2) function with parameter's without return type 
# task_1......................
# def rev(n, rev1 = 0, rem = 0): # parameter's
#     while(n != 0):
#         rem = n % 10
#         rev1 = rev1*10+rem
#         n = n // 10

#     print(rev1)

# n1 = int(input("Enter a number : "))
# rev(n1) # arguments

# task_2.......................
# def pattern_1(n):
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print("*",end="")
#         print()

# n = int(input("Enter a row : "))
# pattern_1(n)

# task_3..................
# def pattern_2(n):
#     for i in range(1, n+1):
#         for j in range(1, n-i+1):
#             print(" ", end = "")
#         for j in range(1, i+1):
#             print("*",end = "")
#         print()    

# n = int(input("Enter a row : "))
# pattern_2(n)

# # task_4..................
# def pattern_3(n):
#     for i in range(1, n+1):
#         for j in range(1, n-i+1):
#             print(" ", end = "")
#         for j in range(1, i+1):
#             print(" *",end = "")
#         print()    

# n = int(input("Enter a row : "))
# pattern_3(n)


# # pattern_1...................
# def pattern_1(n):
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print("*",end="")
#         print()

# # pattern_2..................
# def pattern_2(n):
#     for i in range(1, n+1):
#         for j in range(1, n-i+1):
#             print(" ", end = "")
#         for j in range(1, i+1):
#             print("*",end = "")
#         print()    

# # pattern_3..................
# def pattern_3(n):
#     for i in range(1, n+1):
#         for j in range(1, n-i+1):
#             print(" ", end = "")
#         for j in range(1, i+1):
#             print(" *",end = "")
#         print()    

#     while True: 
#         """
#         Press 1 for right-angle triangle.
#         Press 2 for left-angle triangle.
#         Press 3 for triangle.
#     """
#     print(menu)

#     choice = int(input("Enter your choice : "))

#     if choice == 1 :
#         n = int(input("Enter a row : "))
#         pattern_1(n)

#     elif choice == 2:
#         n = int(input("Enter a row : "))
#         pattern_1(n)

#     elif choice == 3:
#         n = int(input("Enter a row : "))
#         pattern_1(n)
#     elif choice == 4:
#         print("Thank you!!!!")
#         break
#     else:
#         print("Invalid input")
#         break

# 3) function without parameter's with return type
# def hello():
#     a = 20
#     b = 50

#     return a + b

# result = hello()
# print(result)

# def factorial():
#     n = 1
#     for i in range(1,6):
#         n = n * i
    
#     return n

# print(factorial())

# 4) function with parameter's with return type
# def add(a, b):      
#     return a + b    

# result = add(20, 50)
# print(result)

def factorial(n):   
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact     
print(factorial(5))
