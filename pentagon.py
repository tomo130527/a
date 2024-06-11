import matplotlib.pyplot as plt
import numpy as np

# Define parameters for the plot
center_x = 0
center_y = 0
radius = 1  # The arm extends 1 unit from the center

# Define a line segment along x-axis
x_line = np.linspace(center_x - radius, center_x + radius, 100)
y_line = np.zeros_like(x_line)

# Define a line segment along y-axis
y_line_vertical = np.linspace(center_y - radius, center_y + radius, 100)
x_line_vertical = np.zeros_like(y_line_vertical)

# Plot horizontal and vertical lines
plt.figure(figsize=(6, 6))
plt.plot(x_line, y_line, 'b-', lw=2)  # Horizontal line
plt.plot(x_line_vertical, y_line_vertical, 'b-', lw=2)  # Vertical line

plt.title("Plus Sign Using Versatile Equation Approach")
plt.xlim(-2, 2)  # Adjust limits to view the whole shape
plt.ylim(-2, 2)
plt.gca().set_aspect('equal', adjustable='box')  # Ensure aspect ratio is equal
plt.grid(True)
plt.show()
