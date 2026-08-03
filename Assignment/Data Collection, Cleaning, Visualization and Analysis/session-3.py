import numpy as np

# Task 1
# Element-wise Operations

friend1 = np.array([8000, 7500, 9000, 10000, 8500, 9200, 11000])
friend2 = np.array([7000, 8000, 8800, 9500, 9000, 9100, 10500])

print("Task 1")

print("Friend 1 Steps:", friend1)
print("Friend 2 Steps:", friend2)

print("\nAddition:")
print(friend1 + friend2)

print("\nSubtraction:")
print(friend1 - friend2)

print("\nMultiplication:")
print(friend1 * friend2)

print("\nDivision:")
print(friend1 / friend2)


# Task 2
# dot() and matmul()

preferences = np.array([
    [5, 3, 4],
    [2, 5, 1],
    [4, 2, 5]
])

popularity = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("\nTask 2")

print("Using dot():")
print(np.dot(preferences, popularity))

print("\nUsing matmul():")
print(np.matmul(preferences, popularity))

print("\nBoth produce the same result for 2D matrices.")


# Task 3
# Transpose and Statistics

image = np.array([
    [120, 130, 140, 150],
    [110, 125, 135, 145],
    [100, 115, 125, 135],
    [90, 105, 115, 125]
])

transposed = image.T

print("\nTask 3")

print("Original Matrix:")
print(image)

print("\nTransposed Matrix:")
print(transposed)

print("\nMean:", np.mean(image))
print("Median:", np.median(image))
print("Standard Deviation:", np.std(image))
print("Variance:", np.var(image))


# Task 4
# Inverse, Determinant and Eigenvalues

matrix = np.array([
    [4, 2, 1],
    [0, 5, 3],
    [2, 1, 6]
])

print("\nTask 4")

print("Matrix:")
print(matrix)

print("\nInverse:")
print(np.linalg.inv(matrix))

print("\nDeterminant:")
print(np.linalg.det(matrix))

eigenvalues, eigenvectors = np.linalg.eig(matrix)

print("\nEigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)


# Task 5
# Reshape, Flatten, Split and Stack

orders = np.array([10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32])

print("\nTask 5")

reshaped = orders.reshape(4, 3)

part1, part2 = np.split(reshaped, 2)

print(part1)
print(part2)

stacked = np.vstack((part1, part2))
print(stacked)