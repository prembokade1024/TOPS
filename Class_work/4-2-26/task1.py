# task_1.....................
# n1 = int(input("Enter number 1 : "))
# n2 = int(input("Enter number 2 : "))
# n3 = int(input("Enter number 3 : "))
# n4 = int(input("Enter number 4 : "))

# if(n1 > n2 and n1 > n3 and n1 > n4):
#     print(n1, "Greater")
# elif(n2 > n3 and n2 > n4):
#     print(n2, "Greater")
# elif(n3 > n4):
#     print(n3, "Greater")
# else:
#     print(n4, "Greater")

# task_2.....................
# n1 = int(input("Enter number 1 : "))
# n2 = int(input("Enter number 2 : "))
# n3 = int(input("Enter number 3 : "))
# n4 = int(input("Enter number 4 : "))

# if(n1 > n2 or n1 > n3 or n1 > n4):
#     print(n1, "Greater")
# elif(n2 > n3 or n2 > n4):
#     print(n2, "Greater")
# elif(n3 > n4):
#     print(n3, "Greater")
# else:
#     print(n4, "Greater")

# task_3..................
# i = 1
# while(i <= 10):
#     print(i)
#     i = i+1

# task_4..................
# n = int(input("Enter a number"))
# i = 1
# while(i <= n):
#     print(i)
#     i = i+1

# task_5.............
# n = int(input("Enter a number"))
# i = n
# while(i >= 1):
#     print(i)
#     i = i-1

# task_6...............
# n = int(input("Enter a number : "))
# i = 1
# while(i <= 10):
#     print(n,"x",i," = ", n * i)
#     i = i+1

# task_7.............
i = 1
ev = 0
od = 0
evsum = 0
odsum = 0
sum = 0

while( i <= 5 ):
    n = int(input("Enter a number : "))
    
    if( n%2 == 0):
        print(n, "is even")
        ev += 1
        evsum = evsum + n
    else:
        print(n, "is odd")
        od += 1
        odsum = odsum + n
    sum += n
    i += 1
    
print("Even count : ", ev)
print("Odd count : ", od)

print("Even sum : ", evsum)
print("Odd sum : ", odsum)

print("Total sum : ", sum)
