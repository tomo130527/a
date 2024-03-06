import numpy as np
from scipy.linalg import solve

# Define the coefficients matrix A and the constants vector B in the system of equations Ax = B
A = np.array([[1, 1], [1, -1]])
B = np.array([3, 6])

# Solve the system of linear equations Ax = B
solution = solve(A, B)

# Display the solution
print("Solution for x and y:", solution)
