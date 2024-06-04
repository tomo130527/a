import tkinter as tk

from helper import double_backslashes, read_csv
from all_graph import one_graph_all_param, plot_datoooa, plot_popodata, plotooo_data, th_plot_data, three_plot_data, two_file_plot_data
from spiral import plot_csv_file, save_to_csv, spiral

SPIRAL_CSV_FILE = 'spiral_data.csv'




def show_selected_item(event):
    global root  # Define root as global
    file = double_backslashes(r"C:\Users\nares\Desktop\Zikken\2024116\OneDrive-2024-01-16\20240116_1433_01top.csv")
    data = read_csv(file)
    if data is None:
        print("No data found")
        return
    selected_item = listbox.get(tk.ACTIVE)
    
    if selected_item == "All":
        one_graph_all_param(data=data, x_column='SN', y_columns=['PZT volt', 'SD'], plot_type='line', title='CSV Data Plot', x_label='X-axis', y_label='Y-axis')

    elif selected_item == "Plot1":
        three_plot_data(data=data,x_column='SN', y_columns=['Contrast','SD','PZT volt'], plot_type='line', title='CSV Data Plot', x_label='Time (s)', y_label='Y-axis', font_size=24)

    elif selected_item == "Plot2":
        th_plot_data(data=data,x_column='SN', y_columns=['Contrast','SD','PZT volt'], plot_type='line', title='CSV Data Plot', x_label='Time (s)', y_label='Y-axis', font_size=24)

    elif selected_item == "Plot3":
        plot_datoooa(data=data,x_column='SN', y_columns=['Contrast','SD','PZT volt'], plot_type='line', title='CSV Data Plot', x_label='Time (s)', y_label='Y-axis', font_size=24)
    
    elif selected_item == "Pillar 1D":
        plotooo_data(data=data,x_column='SN', y_columns=['Contrast','SD','PZT volt'], plot_type='line', title='CSV Data Plot', x_label='Time (s)', y_label='Y-axis', font_size=24)

    elif selected_item == "Pillar 2D":
        plot_popodata(data=data,x_column='SN', y_columns=['Contrast','SD','PZT volt'], plot_type='line', title='CSV Data Plot', x_label='Time (s)', y_label='Y-axis', font_size=24)
    
    elif selected_item == "Spiral Graph 3D":
        t_file = [file,file]
        two_file_plot_data(two_files= t_file,x_column='SN', plot_type='line', title='CSV Data Plot', x_label='Time (s)', font_size=12)
    
    elif selected_item == "Gererate CSV":
        spiral_data = spiral()
        save_to_csv(spiral_data,SPIRAL_CSV_FILE)
        label.config(text=f"Successfully created file {SPIRAL_CSV_FILE}")

    elif selected_item == "Plot CSV":
        plot_csv_file(SPIRAL_CSV_FILE)
        label.config(text=f"Successfully plotted file {SPIRAL_CSV_FILE}")

    elif selected_item == "Exit":
        root.destroy()
    else:
        label.config(text="You selected: " + selected_item)


root = tk.Tk()
root.title("Menu of Lists")
# Create a listbox
listbox = tk.Listbox(root)
listbox.pack(pady=10)
# Add items to the listbox
items = ["All", "Plot1","Plot2","Plot3", "Pillar 1D", "Pillar 2D", "Spiral Graph 3D","Gererate CSV","Plot CSV", "Exit"]
for item in items:
    listbox.insert(tk.END, item)

# Bind double click event to listbox
listbox.bind("<Double-Button-1>", show_selected_item)
# Create a label to display selected item
label = tk.Label(root, text="")
label.pack()
root.mainloop()
