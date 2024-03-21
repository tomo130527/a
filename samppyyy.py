from sympy import symbols, Eq, solve

# Define symbols and equation
x, y = symbols('x y')
equation = x**2 + y**2 - 25

# Solve the equation for x
solution_x = solve(equation, x)

# Display the solution for x
print("Solution for x:", solution_x)

# Substitute a specific value for if y=3 and solve for x
solution_substituted = solve(equation.subs(y, 3), x)

# Display the substituted solution for x
print("Substituted solution for x:", solution_substituted)
