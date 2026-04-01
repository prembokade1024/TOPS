# task_1...............
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

# task_2.................
# for i in range(1, 6):
#     print(" " * (6 - i) + " *" * i)

# task_3.............
# for i in range(1,6):
#     for j in range(1,6-i):
#         print("*")

# task_4.............
# for i in range(1,11):
#     print(i)
#     if(i==5):
#         break

# task_5.............
# for i in range(1,11):
#     if(i==5):
#         break
#     print(i)

# task_6..............
# for i in range(1,11):
#     if(i==5):
#         continue
#     print(i)

# task_7.................
# for i in range(1,11):
#     if(i==5):
#         pass
#     print(i)

# task_8.............
while True:
    
    menu = """
        Press 1 for Right angle traingle
        Press 2 for Factorial
        Press 3 for Prime number
        Press 4 for exit
    """
    print(menu)

    choice = int(input("Enter your choice : "))

    if choice == 1 :
        for i in range(1,6):
            for j in range(1,i+1):
                print("*",end="")
            print()

    elif choice == 2 :
        n = int(input("Enter a number : "))
        i = 1
        sum = 1
        while(i <= n):
            sum = sum*i
            i += 1
        print(f"Factorial of {n} : ", sum)
    
    elif choice == 3 :
        n = int(input("Enter a number: "))
        if n <= 1:
            print("Not a Prime Number")
        else:
            for i in range(2, n):
                if n % i == 0:
                    print("Not a Prime Number")
                    break
                else:
                    print("Prime Number")

    elif choice == 4 :
        print("Thank you........")
        break
    
    else:
        print("Invalid input")
        break

