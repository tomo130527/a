import csv
import subprocess
import sys
import json

import numpy as np

from constants import INPUT_BTN_LIST, INPUT_VALUES

def install_package(package_name):
    try:
        __import__(package_name)
        print(f"The package '{package_name}' is already installed.")
    except ImportError:
        print(f"The package '{package_name}' is not installed. Installing now...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        print(f"The package '{package_name}' has been installed successfully.")

# Example usage
# install_package('matplotlib')

def read_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        # If the file doesn't exist, create it and return an empty dictionary
        save_as_json([],file_path)
        return []

def save_as_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print("Data saved as JSON successfully.")


def find_json_value(json_data, key):
    if isinstance(json_data, dict):
        return json_data.get(key)
    print("Error: JSON data is not a dictionary.")
    return None


def map_get_value(key, input_values_path, input_btn_list_path):
    pref_data = read_json(input_values_path)
    input_j_data = read_json(input_btn_list_path)
    
    try:
        angle_ = int(find_json_value(pref_data, input_j_data[key]))
    except (ValueError, TypeError) as e:
        print(f"Error: {e}. Could not convert value to int.")
        angle_ = None  # or set to a default value like 0 or -1

    return angle_


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

