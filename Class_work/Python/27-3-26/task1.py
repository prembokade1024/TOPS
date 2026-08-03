# def fac(n):
#     if n == 1 or n == 0: # base case
#         return 1

#     else:
#         return n * (n-1) # recursive case

# n = int(input("Enter a value : "))
# print(f"Factorial of {n} is ",fac(n))

# def prime(n, i = 2):
#     if n <= 1 or n % i == 0:
#         return False # base case
#     elif i * i > n:
#         return True # base case

#     return prime(n, i + 1)
# n = int(input("Enter a value : "))

# if prime(n):
#     print("Prime number")
# else:
#     print("Not a prime number")


def fibonacci(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter a value : "))

for i in range(n):
    print(fibonacci(i),end = " ")