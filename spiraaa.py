import math
from matplotlib import pyplot as plt
import numpy as np
import csv

class Plot3DLine:
    def __init__(self, height=10, num_coils=3, diameter=1):
        self.num_points = 1000
        self.diameter = diameter
        self.x_data, self.y_data, self.z_data = self.generate_spiral_segment(height, num_coils)
        self.height = height
        self.num_coils = num_coils

    def generate_spiral_segment(self, height, num_coils):
        theta = np.linspace(0, 2 * np.pi * num_coils, self.num_points)
        
        # Calculate the radius for the first coil
        base_coil_radius = self.diameter / 2 * theta[theta <= 2 * np.pi] / (2 * np.pi)
        
        # Calculate the radius for the rest of the coils
        rest_coil_radius = self.diameter / 2
        
        # Combine the radii for all coils
        radius = np.concatenate((base_coil_radius, rest_coil_radius * np.ones(self.num_points - len(base_coil_radius))))
        
        spiral_z = height * (theta / (2 * np.pi * num_coils))
        spiral_x = radius * np.cos(theta)
        spiral_y = radius * np.sin(theta)
        
        return spiral_x, spiral_y, spiral_z

    # def generate_spiral_segment(self, height, num_coils):
    #     theta = np.linspace(0, 2 * np.pi * num_coils, self.num_points)
    #     radius = self.diameter / 2 * theta / (2 * np.pi * num_coils)
    #     spiral_z = height * (theta / (2 * np.pi * num_coils))
    #     spiral_x = radius * np.cos(theta)
    #     spiral_y = radius * np.sin(theta)
    #     return spiral_x, spiral_y, spiral_z

    def generate_data(self):
        # Generate data without plotting
        self.x_data, self.y_data, self.z_data = self.generate_spiral_segment(self.height, self.num_coils)
        return self.x_data, self.y_data, self.z_data

    def save_to_csv(self, filename):
        # Save data to CSV file
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['x', 'y', 'z'])  # Header row
            writer.writerows(zip(self.x_data, self.y_data, self.z_data))

# Create an instance of the Plot3DLine class
plotter = Plot3DLine(height=35, num_coils=3, diameter=1)

# Generate data without plotting
x_data, y_data, z_data = plotter.generate_data()

# Save data to CSV file
plotter.save_to_csv("spiral_data.csv")
print("Data saved to spiral_data.csv")
def read_csv_data(filename):
  with open(filename, 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    data = [row for row in reader]
  x_data, y_data, z_data = zip(*data)
  return np.asarray(x_data, dtype=float), np.asarray(y_data, dtype=float), np.asarray(z_data, dtype=float)

class Plot3DLine:
  def __init__(self, filename):
    self.x_data, self.y_data, self.z_data = read_csv_data(filename)

  def plot(self):
    # Create a figure and 3D axes
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the 3D line
    ax.plot(self.x_data, self.y_data, self.z_data)

    # Set axis labels and title
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")
    ax.set_title("3D Spiral Plot from CSV")

    plt.show()

# Read data from CSV file
data_reader = Plot3DLine("spiral_data.csv")

# Plot the data
data_reader.plot()
