# 1. Write a python program to sum of the first n positive integers.
def sum_of_integers(n):

    return (n * (n + 1)) // 2

n = int(input("Enter a positive integer: "))
if n < 0:
    print("Please enter a positive integer.")
else:
    result = sum_of_integers(n)
    print(f"The sum of the first {n} positive integers is: {result}")