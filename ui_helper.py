import os
import tkinter as tk
from tkinter import filedialog
import pandas as pd

from constants import *
from json_helper import *


def double_backslashes(input_string):
    return input_string.replace('\\', '\\\\')

def read_csv(file_path):
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    
    if not os.path.exists(file_path):
        print("File not found. Please provide a valid file path.")



def read_csv_two(file_paths):
    data = [None,None]
    data[0] = pd.read_csv(file_paths[0])
    data[1] = pd.read_csv(file_paths[1])
            
    return data

def read_all_settings(key):
    settings = read_json(SETTINGS_FILE)
    if settings is not None:
        data3 = settings[key]
    return data3


def open_file_dialog(master):
    file_path = filedialog.askopenfilename(
        title="Select a JSON File",
        filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
    )
    if file_path:
        print(f"Selected file: {file_path}")
        load_settings(master,file_path)


def load_settings(masster,file_path):
    my_set = read_json(file_path)
    for entrry in input_list_items:
        if entrry in my_set:
            pick_item = my_set[entrry]
            create_labeled_entry(frame=masster, label_text=entrry, jk=pick_item, padding=0)
        else:
            print(f"Warning: '{entrry}' not found in settings.")


def setting_save(json_key, json_value):
    # Read the current settings
    settings = read_json(SETTINGS_FILE)
    # Ensure the settings is a dictionary
    if not isinstance(settings, dict):
        settings = {}
    
    # Update or add the new key-value pair
    settings[json_key] = json_value
    # Save the updated settings back to the file
    save_as_json(settings, SETTINGS_FILE)
    print(f"Setting saved: {json_key} = {json_value}")


def create_labeled_entry(frame, label_text,json_key,json_value):
    r1 = tk.Frame(frame)
    
    entry_var = tk.StringVar(value=json_value)  # Create a StringVar with the default value
    entry = tk.Entry(master=r1,textvariable=entry_var)
    entry.grid(row=1,column=1, columnspan=2)

    btn = tk.Button(r1, text=label_text, font=("Arial", 12), width=20, command=lambda item=label_text: setting_save(json_key,entry.get()))
    btn.grid(row=1,column=3)
    
    r1.pack(pady=10)
    return r1

