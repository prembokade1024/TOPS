# Task 1

import numpy as np


# Task 2

followers = np.array([1200, 15000, 67000, 340000, 1250000])

print("Task 2")
print("Followers Array:", followers)
print("Shape:", followers.shape)
print("Number of Dimensions:", followers.ndim)
print("Data Type:", followers.dtype)


# Task 3

order_ids = np.arange(101, 111)

print("\nTask 3")
print("Order IDs:", order_ids)
print("Size:", order_ids.size)


# Task 4

identity_matrix = np.eye(3)

print("\nTask 4")
print(identity_matrix)

# The diagonal values (1s) represent that each playlist maps to itself,
# while the 0s indicate no relationship with other playlists.


# Task 5

cricket_scores = [45, 67, 120, 89, 54]

scores_array = np.array(cricket_scores)

print("\nTask 5")
print("Scores Array:", scores_array)
print("Memory used by each score (bytes):", scores_array.itemsize)