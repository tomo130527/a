import numpy as np
from scipy.linalg import solve

# Define the coefficients matrix A and the constants vector B in the system of equations Ax = B
A = np.array([[2, 1], [1, -3]])
B = np.array([8, 1])

# Solve the system of linear equations Ax = B
solution = solve(A, B)

# Display the solution
print("Solution for x and y:", solution)
