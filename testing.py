import tkinter as tk

from json_helper import *
from ui_helper import create_labeled_entry

root = tk.Tk()
root.title("Menu of Lists")
root.geometry("800x600")
row1 = tk.Frame(root)
row1.grid(row=1,column=1)
row2 = tk.Frame(root)
row2.grid(row=1,column=2)

create_labeled_entry(frame=row1, reading_file="ui_setting.json",saving_file="settings.json")

root.mainloop()