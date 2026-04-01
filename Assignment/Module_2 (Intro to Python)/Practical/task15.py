# 15.Given a number n, write a python program to make and print the list of Fibonacci series up to n. 
# Input : n=7 Hint : first 7 numbers in the series Expected output :
# First few Fibonacci numbers are 0, 1, 1, 2, 3, 5, 8, 13

def generate_fibonacci(n):
    # Initialize the series with the first two numbers
    series = [0, 1]
    
    # Handle cases where n is 0 or 1
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    # Generate the series using a loop
    # We already have the first 2, so we need n-2 more
    for i in range(2, n):
        next_val = series[-1] + series[-2]
        series.append(next_val)
        
    return series[:n]

n = 7
fib_series = generate_fibonacci(n)
print(f"First {n} Fibonacci numbers are: {', '.join(map(str, fib_series))}")