# Import SymPy
from sympy import symbols, Eq, solve

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
