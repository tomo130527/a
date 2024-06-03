import numpy as np
from scipy.linalg import solve
from sympy import symbols, Eq, solve


eq1 = [2, 4, 5]
eq2 = [-4, 5, 0]
def solve_system_of_linear_equations(line1, line2):
    # Define the coefficients matrix A and the constants vector B in the system of equations Ax = B
    A = np.array([[line1[0], line2[0]], [line1[1], -line2[1]]])
    B = np.array([line1[2], line2[2]])

    return solve(A, B)

# Display the solution

def quadratic_equation(a, b, c):
        # Define symbols
    x, y = symbols('x y')

    # Define an equation
    equation = Eq(x**2 + y**2, 25)

    # Solve the equation for x
    solution_x = solve(equation, x)

    # Display the solution for x
    print("Solution for x:", solution_x)

    # Substitute a specific value for y and solve for x
    equation_substituted = equation.subs(y, 3)
    solution_substituted = solve(equation_substituted, x)

    # Display the substituted solution for x
    print("Substituted solution for x:", solution_substituted)


print("Solution for x and y:", solve_system_of_linear_equations(line1=eq1, line2=eq2))

