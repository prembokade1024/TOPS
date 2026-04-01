# 7. Program to find Greatest Common Divisor of two numbers. For example, theGCD of 20 and 28 is 4 and the GCD of 98 and 56 is 14.
def find_gcd(a, b):
    """
    Computes the GCD using the Euclidean algorithm:
    While b is not 0, replace a with b and b with the remainder of a / b.
    """
    while b:
        a, b = b, a % b
    return a

num1 = 98
num2 = 56
result = find_gcd(num1, num2)

print(f"The GCD of {num1} and {num2} is: {result}")