import tkinter as tk

from helper import double_backslashes
from all_graph import one_graph_all_param, th_plot_data, three_plot_data, two_file_plot_data

def show_selected_item(event):
    global root  # Define root as global
    file = double_backslashes(r"C:\Users\nares\Desktop\Zikken\2024116\OneDrive-2024-01-16\20240116_1433_01top.csv")
    selected_item = listbox.get(tk.ACTIVE)
    
    if selected_item == "All":
        one_graph_all_param(file=file, x_column='SN', y_columns=['PZT volt', 'SD'], plot_type='line', title='CSV Data Plot', x_label='X-axis', y_label='Y-axis')

    elif selected_item == "Pillar 1D":
        three_plot_data(file=file,x_column='SN', y_columns=['Contrast','SD','PZT volt'], plot_type='line', title='CSV Data Plot', x_label='Time (s)', y_label='Y-axis', font_size=24)

    elif selected_item == "Pillar 2D":
        th_plot_data(file=file,x_column='SN', y_columns=['Contrast','SD','PZT volt'], plot_type='line', title='CSV Data Plot', x_label='Time (s)', y_label='Y-axis', font_size=24)
    
    elif selected_item == "Spiral Graph 3D":
        t_file = [file,file]
        two_file_plot_data(two_files= t_file,x_column='SN', plot_type='line', title='CSV Data Plot', x_label='Time (s)', font_size=12)

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
items = ["All", "Tools", "Pillar 1D", "Pillar 2D", "Spiral Graph 3D", "Exit"]
for item in items:
    listbox.insert(tk.END, item)

# Bind double click event to listbox
listbox.bind("<Double-Button-1>", show_selected_item)
# Create a label to display selected item
label = tk.Label(root, text="")
label.pack()
root.mainloop()
