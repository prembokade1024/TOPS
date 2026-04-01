# task_1....................
# def even_odd():
#     n = int(input("Enter a number : "))
#     if(n % 2 == 0):
#         print("Even")
#     else:
#         print("Odd")

# even_odd()

# task_2................
# def factorial():
#     n = int(input("Enter a number : "))
#     i = 1
#     sum = 1
#     while(i <= n):
#         sum = sum*i
#         i += 1
#     print(f"Factorial of {n} : ", sum)

# factorial()

# task_3....................
# def prime_number():
#     n = int(input("Enter a number: "))
#     if n <= 1:
#         print("Not a Prime Number")
#     else:
#         for i in range(2, n):
#             if n % i == 0:
#                 print("Not a Prime Number")
#                 break
#             else:
#                 print("Prime Number")
#                 break

# prime_number()


# task_4...................
# def even_odd():
#     n = int(input("Enter a number : "))
#     if(n % 2 == 0):
#         print("Even")
#     else:
#         print("Odd")

# def factorial():
#     n = int(input("Enter a number : "))
#     i = 1
#     sum = 1
#     while(i <= n):
#         sum = sum*i
#         i += 1
#     print(f"Factorial of {n} : ", sum)

# def prime_number():
#     n = int(input("Enter a number: "))
#     if n <= 1:
#         print("Not a Prime Number")
#     else:
#         for i in range(2, n):
#             if n % i == 0:
#                 print("Not a Prime Number")
#                 break
#             else:
#                 print("Prime Number")
#                 break

# while True:
    
#     menu = """
#         Press 1 for Even or Odd
#         Press 2 for Factorial
#         Press 3 for Prime number
#         Press 4 for exit
#     """
#     print(menu)

#     choice = int(input("Enter your choice : "))

#     if choice == 1 :
#         even_odd()        

#     elif choice == 2 :
#         factorial()
    
#     elif choice == 3 :
#         prime_number()

#     elif choice == 4 :
#         print("Thank you........")
#         break
    
#     else:
#         print("Invalid input")
#         break

def even_odd():
    n = int(input("Enter a number : "))
    if(n % 2 == 0):
        print("Even")
    else:
        print("Odd")

def factorial():
    n = int(input("Enter a number : "))
    i = 1
    sum = 1
    while(i <= n):
        sum = sum*i
        i += 1
        print(f"Factorial of {n} : ",sum)

def prime_number():
    n = int(input("Enter a number : "))
    if(n <= 1):
        print(n, "Not a prime number")
    else:
        for i in range(2,n):
            if n % i == 0:
                print(n, "Not a prime number")
                break
            else:
                print(n,"Prime number")
                break

while True:

    menu = """ 
    
        Press 1 for Even or Odd
        Press 2 for Factorial
        Press 3 for Prime Number
        Press 4 for Exit
    
    """
    print(menu)

    choice = int(input("Enter your choice : "))
    if choice == 1:
        even_odd()

    elif choice == 2:
        factorial()

    elif choice == 3:
        prime_number()

    elif choice == 4:
        print("Thank you")
        break
    else:
        print("Invalid input")
        break
