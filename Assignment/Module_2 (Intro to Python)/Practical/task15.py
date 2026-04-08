# 15.Given a number n, write a python program to make and print the list of Fibonacci series up to n. 
# Input : n=7 Hint : first 7 numbers in the series Expected output :
# First few Fibonacci numbers are 0, 1, 1, 2, 3, 5, 8, 13

def generate_fibonacci(n):
    series = [0, 1]
    
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    for i in range(2, n):
        next_val = series[-1] + series[-2]
        series.append(next_val)
        
    return series[:n]

n = int(input("Enter a value : "))
fib_series = generate_fibonacci(n)
print(f"First {n} Fibonacci numbers : {', '.join(map(str, fib_series))}")