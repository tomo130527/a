import numpy as np
import csv
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Plot3DLine:
    MAX_HEIGHT = 30
    RADIUS_OF_COIL = 5
    TURN = 3

    def save_to_csv(self, filename, data):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['x', 'y', 'z'])  # Header row
            writer.writerows(data)

    def read_csv_data(self, filename):
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header row
            data = [row for row in reader]
        x_data, y_data, z_data = zip(*data)
        return np.asarray(x_data, dtype=float), np.asarray(y_data, dtype=float), np.asarray(z_data, dtype=float)

    def plot(self, filename):
        self.x_data, self.y_data, self.z_data = self.read_csv_data(filename)

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

        # Set custom limits for the axes
        ax.set_xlim([0, 30])  # Example x-axis range
        ax.set_ylim([0, 30])  # Example y-axis range
        ax.set_zlim([0, 30])  # Example z-axis range

        plt.show()

    def spiral(self, start_angle=0, step_size=0.1):
        total_turns = 3  # Total number of complete 360-degree turns
        transition_turns = 2  # Number of turns with increasing radius
        constant_radius = 5  # Constant radius after transition

        x_data = []
        y_data = []
        z_data = []

        theta = 0
        total_steps = int(total_turns * 2 * math.pi / step_size)
        height_increment = self.MAX_HEIGHT / total_steps

        while theta < start_angle + total_turns * 2 * math.pi:
            if theta < transition_turns * 2 * math.pi:
                radius = self.RADIUS_OF_COIL * theta / (transition_turns * 2 * math.pi)
            else:
                radius = self.RADIUS_OF_COIL

            x = radius * math.cos(theta)
            y = radius * math.sin(theta)
            z = theta * height_increment

            x_data.append(x)
            y_data.append(y)
            z_data.append(z)

            theta += step_size

        return list(zip(x_data, y_data, z_data))

# Read data from CSV file
data_reader = Plot3DLine()
dd = data_reader.spiral()
data_reader.save_to_csv("ga.csv", dd)
# Plot the data
data_reader.plot("ga.csv")