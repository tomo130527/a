import pandas as pd
import matplotlib.pyplot as plt

def double_backslashes(input_string):
    return input_string.replace('\\', '\\\\')

class CSVPlotter:
    def __init__(self, file_paths):
        self.file_paths = file_paths
        self.data = [None, None]

    def read_csv(self):
        for i, file_path in enumerate(self.file_paths):
            try:
                self.data[i] = pd.read_csv(file_path)
            except FileNotFoundError:
                print(f"File not found: {file_path}. Please provide a valid file path.")

    def plot_data(self, x_column, plot_type='line', title='', x_label='', font_size=24, max_frame=99999, truncate_frame=0):
        if any(data is None for data in self.data):
            self.read_csv()

        y_columns = set(column for data in self.data if data is not None for column in data.columns)
        y_columns.discard(x_column)

        if len(self.data) == 1:
            fig, axs = plt.subplots(len(y_columns), 1, figsize=(8, 6 * len(y_columns)), sharex=True, gridspec_kw={'hspace': 0})
        else:
            fig, axs = plt.subplots(len(self.data), len(y_columns), figsize=(15, 8), sharex=True)

        for j, (data, file_path) in enumerate(zip(self.data, self.file_paths)):
            if len(self.data) == 1:
                ax = axs[j]
            else:
                ax = axs[j, :]
                
            for i, col in enumerate(y_columns):
                if data is not None and col in data.columns:
                    ax[i].plot(data[x_column], data[col], label=f'{col}')
                    ax[i].set_title(col)
                    ax[i].set_xlabel(x_label)
                    if j == 0:  # Set y-axis label only for the first row
                        ax[i].set_ylabel(f'{col}')
                        #ax[i].set_ylabel(f'{col} - {file_path}')
                    
                    ax[i].legend()

        plt.tight_layout()
        plt.show()

# Example usage
converted_strings = [
    double_backslashes(r"C:\Users\nares\Desktop\Zikken\20231122\20231122_1032_33top.csv"),
    double_backslashes(r"C:\Users\nares\Desktop\Zikken\20231122\20231122_1032_33top.csv"),
]

csv_plotter = CSVPlotter(converted_strings)
csv_plotter.plot_data(x_column='No of frame', plot_type='line', title='CSV Data Plot', x_label='Time (s)', font_size=12)
