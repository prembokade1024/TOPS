# 17.Write a python program using function to find the sum of odd and even series
# Odd series: 12/ 1! +32/ 3! + 52/ 5!+……n
# Even series: 22/ 2! + 42/ 4! + 62/ 6!+……n
import math

def calculate_odd_series(n):
    """
    Calculates the sum of: 1^2/1! + 3^2/3! + 5^2/5! + ... + n^2/n!
    Where n is the number of terms.
    """
    total_sum = 0
    for i in range(n):
        # The i-th odd number is (2*i + 1)
        term_num = 2 * i + 1
        term = (term_num**2) / math.factorial(term_num)
        total_sum += term
    return total_sum

def calculate_even_series(n):
    """
    Calculates the sum of: 2^2/2! + 4^2/4! + 6^2/6! + ... + n^2/n!
    Where n is the number of terms.
    """
    total_sum = 0
    for i in range(1, n + 1):
        # The i-th even number is (2*i)
        term_num = 2 * i
        term = (term_num**2) / math.factorial(term_num)
        total_sum += term
    return total_sum

n_terms = 5
print(f"Sum of the first {n_terms} terms of Odd series: {calculate_odd_series(n_terms):.4f}")
print(f"Sum of the first {n_terms} terms of Even series: {calculate_even_series(n_terms):.4f}")