import numpy as np

# ---------------------------------
# Task 1
# Create a 2D NumPy array of ratings

ratings = np.array([
    [5, 4, 3, 5, 2],
    [4, 5, 5, 3, 4],
    [3, 4, 5, 4, 5],
    [5, 3, 4, 5, 4]
])

print("Task 1")
print("Original Ratings:\n", ratings)

selected_users = ratings[1:3]

print("\nRatings of 2nd and 3rd Users:")
print(selected_users)


# ---------------------------------
# Task 2
# Boolean Indexing

steps = np.array([7500, 8200, 9000, 6500, 10000,
                  7800, 9500, 8700, 7200, 11000])

print("\nTask 2")
print("Steps greater than 8000:")
print(steps[steps > 8000])


# ---------------------------------
# Task 3
# Fancy Indexing

ipl_scores = np.array([180, 195, 210, 175, 225, 200, 240, 190])

print("\nTask 3")
print("Scores from Matches 2, 5, and 7:")
print(ipl_scores[[1, 4, 6]])


# ---------------------------------
# Task 4
# Broadcasting

prices = np.array([500, 1200, 2500, 800, 1500])

discounted_prices = prices * 0.90

print("\nTask 4")
print("Original Prices:", prices)
print("Prices after 10% Discount:", discounted_prices)

# Task 5
# Boolean Masking

ratings = np.array([5, -2, 3, 0, -1, 4, -5, 2])

ratings[ratings < 0] = 0

print("\nTask 5")
print("Updated Ratings:")
print(ratings)