# task_1................
# a = int(input("Enter number A : "))
# b = int(input("Enter number B : "))

# using another variable
# temp = a
# a = b
# b = temp

# without using another variable
# a = a + b
# b = a - b
# a = a - b

# print("After swapping : ", a)
# print("After swapping : ", b)

# a,b = b,a (valid only in python)

#task_2.......................
# n = int(input("Enter your age : "))

# if (n > 100):
#     print(n, "not valid age.")
# elif (n >=  18):
#     print(n, "valid for vote.")
# else:
#     print("not valid for vote.")

# task_3
# n = int(input("Enter a number : "))

# if (n > 0):
#     print("Positive number")
# elif (n == 0):
#     print("you entered 0")
# else:
#     print("Negative number")

# task_4....................
# n = int(input("Enter a number : "))

# if (n % 2 == 0):
#     print("Even number")
# elif (n == 0):
#     print("you entered 0")
# else:
#     print("Odd number")

# task_4.................
# n = int(input("Enter a number : "))

# if (n >= 180):
#     print("Very long")
# elif (n >= 140 and n < 180):
#     print("Long")
# elif(n >= 80 and n <= 139):
#     print("Average")
# elif(n >= 10 and n <= 79):
#     print("Short")
# elif(n > 0 and n <= 9):
#     print("Too short")
# else:
#     print("not valid height")

# task_5........
n1 = int(input("Enter a number 1: "))
n2 = int(input("Enter a number 2: "))
n3 = int(input("Enter a number 3: "))

if(n1 > n2):
    if(n1 > n3):
        print(n1, "Largest")
    else:
        print(n3,"largest")
else:
    if(n2 > n3):
        print(n2,"Largest")
    else:
        print(n3,"Largest")