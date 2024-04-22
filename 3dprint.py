import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Plot3DLine:
  def __init__(self, height=10, num_coils=10, diameter=1):
    self.num_points = 1000
    self.diameter = diameter
    self.x_data, self.y_data, self.z_data = self.generate_spiral(height, num_coils)
    self.height = height
    self.num_coils = num_coils

  def generate_spiral(self, height, num_coils):
    theta = np.linspace(0, 2*np.pi * num_coils, self.num_points)
    radius = self.diameter / 2  # Radius is half the diameter
    z_data = height * theta / (2*np.pi * num_coils)  # Linear increase in z for each coil
    x_data = radius * np.cos(theta)
    y_data = radius * np.sin(theta)
    return x_data, y_data, z_data

  def plot(self):
    # Create a figure and 3D axes
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the 3D line
    ax.plot(self.x_data, self.y_data, self.z_data, marker='o')

    # Set axis labels and title
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")
    ax.set_title("3D Spiral Plot")

    plt.show()

# Create an instance of the Plot3DLine class and plot the spiral
plotter = Plot3DLine(height=35, num_coils=2, diameter=0.2)  # Adjust height, number of coils, and diameter here
plotter.plot()

