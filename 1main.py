import tkinter as tk
from tkinter import TOP, BOTH
from ui_helper import *
from all_graph import *
from tools import *
from spiral import *
from constants import *


logger = setup_logger()
logger.info("coding starting....")
root = tk.Tk()
root.title("Menu of Lists")
root.geometry("800x600")
row1 = tk.Frame(root)
row1.grid(row=1,column=1)
row2 = tk.Frame(root)
row2.grid(row=1,column=2)

def show_selected_item(selected_item):
    logger.info(f"{selected_item} = is selected..")

    csv_file = find_json_value(INPUT_VALUES,"selected_file")
    data = read_csv(csv_file)
    if data is None:
        print("No data found")
        return

    angle_ = map_get_value('Angle',INPUT_VALUES,INPUT_BTN_LIST)

    if selected_item == "All":
        one_graph_all_param(file=csv_file)

    elif selected_item == "Generate_X_Rotate":
        spiral_data = x_axis_rrotat(angle=angle_)
        save_to_csv(spiral_data,SPIRAL_CSV_FILE)
    
    elif selected_item == "Generate_Y_Rotate":
        spiral_data = y_axis_rrotat(angle=angle_)
        save_to_csv(spiral_data,SPIRAL_CSV_FILE)

    elif selected_item == "Generate_XT_Rotate":
        spiral_data = xy_rotate(angle=angle_)
        save_to_csv(spiral_data,SPIRAL_CSV_FILE)
        #label.config(text=f"Successfully created file XY {SPIRAL_CSV_FILE}")

    elif selected_item == "Plot2":
        th_plot_data(file=csv_file)

    elif selected_item == "Plot3":
        plot_datoooa(data=data)

    elif selected_item == "Pillar 2D":
        plot_popodata(data=data)
    
    elif selected_item == "Spiral Graph 3D":
        t_file = [csv_file,csv_file]
        two_file_plot_data(two_files= t_file)
    
    elif selected_item == "Generate_3D_CSV":
        spiral_data = spiral()
        save_to_csv(spiral_data,SPIRAL_CSV_FILE)
        #label.config(text=f"Successfully created file {SPIRAL_CSV_FILE}")

    elif selected_item == "Choose csv file":
        open_file_dialog(row2)

    elif selected_item == "Plot CSV":
        plot_csv_file(SPIRAL_CSV_FILE)
        #label.config(text=f"Successfully plotted file {SPIRAL_CSV_FILE}")

    elif selected_item == "Exit":
        global root
        root.destroy()
    else:
        print(f"You selected: {selected_item}")
        #label.config(text="You selected: " + selected_item)


button_list_items = [
    "All", 
    "Generate_X_Rotate", 
    "Generate_Y_Rotate", 
    "Generate_XT_Rotate", 
    "Pillar 2D",
    "Choose csv file",
    "Plot2", 
    "Plot3", 
    "Spiral Graph 3D", 
    "Generate_3D_CSV", 
    "Plot CSV", 
    "Exit"
]

default_input_list = {
    "Resolution":"reso",
    "Angle":"anglr_",
    "Total_Steps":"steps",
    "Coil_radius":"coil_radius"
}

# Create buttons for each item
for item in button_list_items:
    button = tk.Button(row1, text=item, font=("Arial", 12), width=20, command=lambda item=item: show_selected_item(item))
    button.pack(pady=5)


# Create buttons for each item
inlist = read_json(INPUT_BTN_LIST)
print(inlist)
if inlist == []:
    save_as_json(default_input_list,INPUT_BTN_LIST)

input_list_items = read_json(INPUT_BTN_LIST)

for key in input_list_items:
    valu = input_list_items[key]
    create_labeled_entry(frame=row2, label_text=key, json_key=valu)
    
# Run the tkinter main loop
root.mainloop()
