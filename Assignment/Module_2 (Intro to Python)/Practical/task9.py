# 9. Write a Python program to find the second smallest number in a list.
def find_second_smallest_efficient(numbers):
    if len(numbers) < 2:
        return None
        
    smallest = float('inf')
    second_smallest = float('inf')
    
    for num in numbers:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
            
    return second_smallest if second_smallest != float('inf') else None

nums = [12, 5, 1, 8, 1, 10]
print(f"The second smallest number is: {find_second_smallest_efficient(nums)}")
