# 18. Python Program to Find Factorial of Number Using Recursion
def factorial(n):
    # Base case: Factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive step: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)


num = 5
print(f"The factorial of {num} is: {factorial(num)}")
