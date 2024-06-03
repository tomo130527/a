import pandas as pd


def double_backslashes(input_string):
    return input_string.replace('\\', '\\\\')

def read_csv(file_path):
    try:
        return pd.read_csv(file_path)
    
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")

def read_csv_two(file_paths):
    data = [None,None]
    data[0] = pd.read_csv(file_paths[0])
    data[1] = pd.read_csv(file_paths[1])
            
    return data
