import numpy as np
import csv
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt

MAX_HEIGHT = 30
RADIUS_OF_COIL = 5
TURN = 3
POINTS_PER_TURN = 100

def save_t2o_csv(x_data, y_data, z_data,filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['x', 'y', 'z'])  # Header row
        writer.writerows(zip(x_data, y_data, z_data))

def save_to_csv(filename, data):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['x', 'y', 'z'])  # Header row
        writer.writerows(data)

def read_csv_data(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        data = [row for row in reader]
    x_data, y_data, z_data = zip(*data)
    return np.asarray(x_data, dtype=float), np.asarray(y_data, dtype=float), np.asarray(z_data, dtype=float)


def plot(filename):
    x_data, y_data, z_data = read_csv_data(filename)
    # Create a figure and 3D axes
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the 3D line
    ax.plot(x_data, y_data, z_data)

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

def spiral(start_angle=0, step_size=0.1):
    total_turns = 3  # Total number of complete 360-degree turns
    transition_turns = 2  # Number of turns with increasing radius
    constant_radius = 5  # Constant radius after transition

    x_data = []
    y_data = []
    z_data = []

    theta = 0
    total_steps = int(total_turns * 2 * math.pi / step_size)
    height_increment = MAX_HEIGHT / total_steps

    while theta < start_angle + total_turns * 2 * math.pi:
        if theta < transition_turns * 2 * math.pi:
            radius = RADIUS_OF_COIL * theta / (transition_turns * 2 * math.pi)
        else:
            radius = RADIUS_OF_COIL

        x = radius * math.cos(theta)
        y = radius * math.sin(theta)
        z = theta * height_increment

        x_data.append(x)
        y_data.append(y)
        z_data.append(z)

        theta += step_size

    return list(zip(x_data, y_data, z_data))



def generate_spiral_segment(height, num_coils):
    theta = np.linspace(0, 2 * np.pi * num_coils, POINTS_PER_TURN)
    # Calculate the radius for the first coil
    base_coil_radius = RADIUS_OF_COIL / 2 * theta[theta <= 2 * np.pi] / (2 * np.pi)
    # Calculate the radius for the rest of the coils
    rest_coil_radius = RADIUS_OF_COIL / 2
    # Combine the radii for all coils
    radius = np.concatenate((base_coil_radius, rest_coil_radius * np.ones(POINTS_PER_TURN - len(base_coil_radius))))
    spiral_z = height * (theta / (2 * np.pi * num_coils))
    spiral_x = radius * np.cos(theta)
    spiral_y = radius * np.sin(theta)
    return spiral_x, spiral_y, spiral_z

def generate_spiral_segment(height, num_coils):
    theta = np.linspace(0, 2 * np.pi * num_coils, POINTS_PER_TURN)
    radius = RADIUS_OF_COIL / 2 * theta / (2 * np.pi * num_coils)
    spiral_z = height * (theta / (2 * np.pi * num_coils))
    spiral_x = radius * np.cos(theta)
    spiral_y = radius * np.sin(theta)
    return spiral_x, spiral_y, spiral_z


