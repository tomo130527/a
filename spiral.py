from matplotlib.figure import Figure
import numpy as np
import csv
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
from constants import *

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
    ax.plot(x_data, y_data, 6*z_data)
    # Set axis labels and title
    ax.set_xlabel("X-axis(um)")
    ax.set_ylabel("Y-axis(um)")
    ax.set_zlabel("Z-axis(um)")
    ax.set_title("3D Spiral Printing Simulation")
    # Set custom limits for the axes
    ax.set_xlim([0, 2.5*radius_of_coil])  
    ax.set_ylim([0, 2.5*radius_of_coil])  # Example y-axis range
    ax.set_zlim([0, 30])  # Example z-axis range
    plt.show() #return fig, ax

    

def spiral():
    x_data = []
    y_data = []
    z_data = []
    nt = 3
    iin = 0
    total_steps = 300
    base_height = 1
    segment2 = base_height + 1.5
    total_height = segment2 + 2.5
    slighted_height = total_height - base_height
    z_axix = 0
    base_steps = base_height * (total_steps / total_height)
    transition_steps = segment2 * (total_steps / total_height)

    while iin < total_steps:
        if iin < base_steps:
            radius = 0
        elif base_steps <= iin < transition_steps:
            radius = radius_of_coil * ((iin - base_steps) / (transition_steps - base_steps))
        else:
            radius = radius_of_coil

        x = round(radius * math.cos(nt * 2 * math.pi * iin / total_steps) + radius_of_coil, 4)
        y = round(radius * math.sin(nt * 2 * math.pi * iin / total_steps) + radius_of_coil, 4)
        z = round(iin * total_height / total_steps, 4)
        x_data.append(x)
        y_data.append(y)
        z_data.append(z)
        iin += RESOLUTION_POINTS

    return list(zip(x_data, y_data, z_data))


def y_axis_rrotat(angle):
    x_data = []
    y_data = []
    z_data = []
    iin = 0
    total_steps = 300
    base_height = 1
    segment2 = base_height + 1.5
    total_height = segment2 + 2.5
    slighted_height = total_height - base_height
    z_axix = 0
    base_steps = base_height * (total_steps / total_height)

    while iin < total_steps:
        if iin < base_steps:
            radius = 0
            z_axix = base_height * (iin / base_steps)
        else:
            radius = slighted_height * ( iin - base_steps)/(total_steps - base_steps) * math.sin(math.radians(angle))
            z_axix = base_height + slighted_height * ( iin - base_steps)/(total_steps - base_steps) * math.cos(math.radians(angle))

        x = round(radius_of_coil, 4)
        y = round(radius + radius_of_coil, 4)
        z = round(z_axix, 4)
        x_data.append(x)
        y_data.append(y)
        z_data.append(z)
        iin += RESOLUTION_POINTS

    return list(zip(x_data, y_data, z_data))

def x_axis_rrotat(angle):
    x_data = []
    y_data = []
    z_data = []
    iin = 0
    total_steps = 300
    base_height = 1
    segment2 = base_height + 1.5
    total_height = segment2 + 2.5
    slighted_height = total_height - base_height
    z_axix = 0
    base_steps = base_height * (total_steps / total_height)

    while iin < total_steps:
        if iin < base_steps:
            radius = 0
            z_axix = base_height * (iin / base_steps)
        else:
            radius = slighted_height * ( iin - base_steps)/(total_steps - base_steps) * math.sin(math.radians(angle))
            z_axix = base_height + slighted_height * ( iin - base_steps)/(total_steps - base_steps) * math.cos(math.radians(angle))

        x = round(radius + radius_of_coil, 4)
        y = round(radius_of_coil, 4)
        z = round(z_axix, 4)
        x_data.append(x)
        y_data.append(y)
        z_data.append(z)
        iin += RESOLUTION_POINTS

    return list(zip(x_data, y_data, z_data))


def xy_rotate(angle):
    x_data = []
    y_data = []
    z_data = []
    iin = 0
    radius_of_coil=2.5 
    total_steps = 300
    base_height = 1
    segment2 = base_height + 1.5
    total_height = segment2 + 2.5
    slighted_height = total_height - base_height
    z_axix = 0
    base_steps = base_height * (total_steps / total_height)

    while iin < total_steps:
        if iin < base_steps:
            radius = 0
            z_axix = base_height * (iin / base_steps)
        else:
            radius = slighted_height * ( iin - base_steps)/(total_steps - base_steps) * math.sin(math.radians(angle))
            z_axix = base_height + slighted_height * ( iin - base_steps)/(total_steps - base_steps) * math.cos(math.radians(angle))

        x = round(radius + radius_of_coil, 4)
        y = round(radius + radius_of_coil, 4)
        z = round(z_axix, 4)
        x_data.append(x)
        y_data.append(y)
        z_data.append(z)
        iin += RESOLUTION_POINTS

    return list(zip(x_data, y_data, z_data))

