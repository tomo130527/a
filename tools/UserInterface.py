import json
import os
import tkinter as tk

input_btn_togrther = INPUT_BUTTON_LIST_ALL = "tools/input_btn_togrther.json"
btn_list_all = BUTTON_LIST_ALL = "tools/btn_list_all.json"
input_v_save_all = INPUT_VALUE_SAVE_ALL = "tools/input_v_save_all.json"
default_input_btn = {"AppName": "app_key"}
PLOTTING_FILE = r"C:\Users\nares\Desktop\allout\240618\c.csv"
def double_backslashes(input_string):
    return input_string.replace('\\', '\\\\')


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
    
    # Create directory if it does not exist
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory '{directory}' created.")

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print("Data saved as JSON successfully.")


def save_field(write_file,json_key, json_value):
    input_btn = read_json(write_file)
    # Ensure the settings is a dictionary
    if not isinstance(input_btn, dict):
        input_btn = {}
    
    # Update or add the new key-value pair
    input_btn[json_key] = json_value
    # Save the updated settings back to the file
    save_as_json(input_btn, write_file)
    print(f"Setting saved: {json_key} = {json_value}")


def create_labeled_entry(frame1):
    sett = read_json(input_btn_togrther)
    gre = read_json(input_v_save_all)
    for key in sett:
        exval = None
        json_key = sett[key]
        
        # Check if the key exists in the secondary JSON and if its value is None
        if json_key in gre and gre[json_key] is None:
            exval = ""
        elif json_key in gre:
            exval = gre[json_key]
        else:
            exval = None
            
        r1 = tk.Frame(frame1)
        
        entry_var = tk.StringVar(value=exval)  # Create a StringVar with the default value
        entry = tk.Entry(master=r1,textvariable=entry_var)
        entry.grid(row=1,column=1, columnspan=2)

        btn = tk.Button(r1, text=json_key, font=("Arial", 12), width=20, command=lambda item=json_key: save_field(input_v_save_all,json_key,entry.get()))
        btn.grid(row=1,column=3)
        
        r1.pack(pady=10)
    return r1

def create_btn(frame1):
    sett = read_json(btn_list_all)
    for key in sett:
        json_key = sett[key]        
        r1 = tk.Frame(frame1)
#       btn = tk.Button(r1, text=key, font=("Arial", 12), width=20, command=lambda fn_name=json_key: globals()[fn_name]())
        btn = tk.Button(r1, text=key, font=("Arial", 12), width=20, command=lambda fn_name=json_key: show_selected_item(fn_name))
        btn.grid(row=1,column=3)
        
        r1.pack(pady=10)
    return r1

def Generate_X_Rotate():
    print("lala")

def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['x', 'y', 'z'])  # Header row
        writer.writerows(data)

def read_csv(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        data = [row for row in reader]
    x_data, y_data, z_data = zip(*data)
    return np.asarray(x_data, dtype=float), np.asarray(y_data, dtype=float), np.asarray(z_data, dtype=float)

def show_selected_item(selected_item):
    file = double_backslashes(PLOTTING_FILE)
    data = read_csv(file)
    if data is None:
        print("No data found")
        return
        
    if selected_item == "All":
        one_graph_all_param(data=data)

    elif selected_item == "Generate_X_Rotate":
        angle_ = int(read_all_settings('Angle'))
        spiral_data = x_axis_rrotat(angle=angle_)
        save_to_csv(spiral_data,SPIRAL_CSV_FILE)
    
    elif selected_item == "Generate_Y_Rotate":
        angle_ = int(read_all_settings('Angle'))
        spiral_data = y_axis_rrotat(angle=angle_)
        save_to_csv(spiral_data,SPIRAL_CSV_FILE)

    elif selected_item == "Generate_XT_Rotate":
        angle_ = int(read_all_settings('Angle'))
        spiral_data = xy_rotate(angle=angle_)
        save_to_csv(spiral_data,SPIRAL_CSV_FILE)

    elif selected_item == "Plot2":
        th_plot_data(data=data)

    elif selected_item == "Plot3":
        plot_datoooa(data=data)

    elif selected_item == "Pillar 2D":
        plot_popodata(data=data)
    
    elif selected_item == "Spiral Graph 3D":
        t_file = [file,file]
        two_file_plot_data(two_files= t_file)
    
    elif selected_item == "Generate_3D_CSV":
        spiral_data = spiral()
        save_to_csv(spiral_data,SPIRAL_CSV_FILE)

    elif selected_item == "Choose csv file":
        open_file_dialog(row2)

    elif selected_item == "Plot CSV":
        plot_csv_file(SPIRAL_CSV_FILE)

    elif selected_item == "Exit":
        root.destroy()
    else:
        print(f"You selected: {selected_item}")


def start():
    print("start")
    root = tk.Tk()
    root.title("Menu of Lists")
    root.geometry("800x600")
    row1 = tk.Frame(root)
    row1.grid(row=1,column=1)
    row2 = tk.Frame(root)
    row2.grid(row=1,column=2)
    if not os.path.exists(input_btn_togrther):
        data = {
            "AppName": "app_key",
        }
        save_as_json(data, input_btn_togrther)
        
    if not os.path.exists(btn_list_all):
        data = {
            "AppName": "app_key",
        }
        save_as_json(data, btn_list_all)
    
    create_labeled_entry(frame1=row1)
    create_btn(frame1=row2)
    root.mainloop()

start()
