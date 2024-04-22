import csv
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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
