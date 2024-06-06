import tkinter as tk

from tkinter import TOP, BOTH

from helper import *
from all_graph import *
from json_helper import *
from spiral import *
from constants import *
def show_selected_item(selected_item):
    global root 
    file = double_backslashes(PLOTTING_FILE)
    data = read_csv(file)
    if data is None:
        print("No data found")
        return
    #selected_item = listbox.get(tk.ACTIVE)
    
    if selected_item == "All":
        one_graph_all_param(data=data, x_column='SN', y_columns=['PZT volt', 'SD'], plot_type='line', title='CSV Data Plot', x_label='X-axis', y_label='Y-axis')

    elif selected_item == "Generate_X_Rotate":
        spiral_data = x_axis_rrotat(angle=45)
        save_to_csv(spiral_data,SPIRAL_CSV_FILE)
        #label.config(text=f"Successfully created file X {SPIRAL_CSV_FILE}")
    
    elif selected_item == "Generate_Y_Rotate":
        spiral_data = y_axis_rrotat(angle=45)
        save_to_csv(spiral_data,SPIRAL_CSV_FILE)
        #label.config(text=f"Successfully created file Y {SPIRAL_CSV_FILE}")

    elif selected_item == "Generate_XT_Rotate":
        spiral_data = xy_rotate(angle=45)
        save_to_csv(spiral_data,SPIRAL_CSV_FILE)
        #label.config(text=f"Successfully created file XY {SPIRAL_CSV_FILE}")

    elif selected_item == "Plot2":
        th_plot_data(data=data,x_column='SN', y_columns=['Contrast','SD','PZT volt'], plot_type='line', title='CSV Data Plot', x_label='Time (s)', y_label='Y-axis', font_size=24)

    elif selected_item == "Plot3":
        plot_datoooa(data=data,x_column='SN', y_columns=['Contrast','SD','PZT volt'], plot_type='line', title='CSV Data Plot', x_label='Time (s)', y_label='Y-axis', font_size=24)

    elif selected_item == "Pillar 2D":
        plot_popodata(data=data,x_column='SN', y_columns=['Contrast','SD','PZT volt'], plot_type='line', title='CSV Data Plot', x_label='Time (s)', y_label='Y-axis', font_size=24)
    
    elif selected_item == "Spiral Graph 3D":
        t_file = [file,file]
        two_file_plot_data(two_files= t_file,x_column='SN', plot_type='line', title='CSV Data Plot', x_label='Time (s)', font_size=12)
    
    elif selected_item == "Generate_3D_CSV":
        spiral_data = spiral()
        save_to_csv(spiral_data,SPIRAL_CSV_FILE)
        #label.config(text=f"Successfully created file {SPIRAL_CSV_FILE}")

    elif selected_item == "Plot CSV":
        plot_csv_file(SPIRAL_CSV_FILE)
        #label.config(text=f"Successfully plotted file {SPIRAL_CSV_FILE}")

    elif selected_item == "Exit":
        root.destroy()
    else:
        print(f"You selected: {selected_item}")
        #label.config(text="You selected: " + selected_item)


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



def create_labeled_entry(frame, label_text, padding=20):
    label = tk.Label(frame, text=label_text)
    label.pack(pady=padding)
    
    entry = tk.Entry(frame)
    entry.pack(pady=padding)

    btn = tk.Button(frame, text=label_text, font=("Arial", 12), width=20, command=lambda item=label_text: setting_save(label_text,entry.get()))
    btn.pack(pady=padding)
    
    return label, entry,btn

# Create the main tkinter window
root = tk.Tk()
root.title("Menu of Lists")
root.geometry("800x600")


row1 = tk.Frame(root)
row1.grid(row=1,column=1)
row2 = tk.Frame(root)
row2.grid(row=1,column=2)

button_list_items = [
    "All", 
    "Generate_X_Rotate", 
    "Generate_Y_Rotate", 
    "Generate_XT_Rotate", 
    "Pillar 2D", 
    "Plot2", 
    "Plot3", 
    "Spiral Graph 3D", 
    "Generate_3D_CSV", 
    "Plot CSV", 
    "Exit"
]
input_list_items = [
    "Angle", 
    "Resolution", 
    "Total steps", 
    "Maximum radius",
]

# Create buttons for each item
for item in button_list_items:
    button = tk.Button(row1, text=item, font=("Arial", 12), width=20, command=lambda item=item: show_selected_item(item))
    button.pack(pady=5)
# Create buttons for each item
for entrry in input_list_items:
    create_labeled_entry(frame=row2, label_text=entrry, padding=0)

# Run the tkinter main loop
root.mainloop()