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

def save_to_csv(data, filename):
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


def plot_csv_file(filename):
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

def spiral(step_size=0.001):
    x_data = []
    y_data = []
    z_data = []
    total_height = 30
    total_steps = 30
    base_height = 5
    segment2 = 5
    iin = 0
    base = base_height*(total_steps/total_height)
    spi = segment2*(total_steps/total_height)
    consr = (total_height-base_height-segment2)*(total_steps/total_height)

    nt = 1 

    while iin < total_steps:
        if iin < base:
            radius = 0
        elif iin < spi:
            radius = RADIUS_OF_COIL * ((iin - base) / (spi - base))
        elif iin < consr:
            radius = RADIUS_OF_COIL
        else:
            radius = 0

        x = radius * math.cos(nt*2*math.pi*iin/total_steps) + RADIUS_OF_COIL
        y = radius * math.sin(nt*2*math.pi*iin/total_steps) + RADIUS_OF_COIL
        z = iin * total_height / total_steps
        x_data.append(x)
        y_data.append(y)
        z_data.append(z)
        iin += step_size

    return list(zip(x_data, y_data, z_data))

