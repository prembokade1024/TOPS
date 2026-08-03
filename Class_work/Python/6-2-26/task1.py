# task_1................
# n = int(input("Enter a number : "))
# i = 1
# sum = 0
# while(i <= n):
#     print(i)
#     sum += i
#     i += 1

# print("Total : ", sum)

# task_2................
# n = int(input("Enter a number : "))
# i = 1
# sum = 1
# while(i <= n):
#     sum = sum*i
#     i += 1

# print(f"Factorial of {n} : ", sum)

# task_3..................
# n = int(input("Enter a number : "))
# rem = 0
# rev = 0

# while(n != 0 ):
#     rem = rem % 10
#     rev = rev * 10 + rem
#     n = n // 10
# print(rev)

# task_4....................
# n = int(input("Enter a number : "))
# rem = 0
# rev = 0

# while(n != 0 ):
#     rem = rem % 10
#     rev = rev * 10 + rem
#     n = n // 10
# # print(rev)

# if( n1 == rev ):
#     print("Palindrome")
# else:
#     print("Not a palindrome")

# task_5................
ev = 0
od = 0
evsum = 0
odsum = 0
total_sum = 0

for i in range(1, 6):
    n = int(input("Enter a number : "))
    
    if n % 2 == 0:
        print(n, "is even")
        ev += 1
        evsum += n
    else:
        print(n, "is odd")
        od += 1
        odsum += n

    total_sum += n

print("Even count :", ev)
print("Odd count :", od)

print("Even sum :", evsum)
print("Odd sum :", odsum)

print("Total sum :", total_sum)
