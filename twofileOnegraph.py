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

    def plot_data(self, x_column, y_columns, plot_type='line', title='', x_label='', y_label='', font_size=24, max_frame=99999, truncate_frame=0):
        if any(data is None for data in self.data):
            self.read_csv()

        fig, axs = plt.subplots(len(self.data), len(y_columns), figsize=(15, 8), sharex=True)

        for j, data in enumerate(self.data):
            for i, col in enumerate(y_columns):
                if data is not None and col in data.columns:
                    data[x_column] = (data[x_column] - truncate_frame) / 10
                    if len(data[x_column]) > max_frame:
                        data = data.iloc[:max_frame]

                    axs[j, i].plot(data[x_column], data[col], label=f'File {j + 1}')

                    axs[j, i].set_title(col)
                    axs[j, i].set_xlabel(x_label)
                    axs[j, i].set_ylabel(y_label)

                    axs[j, i].legend()

        plt.tight_layout()
        plt.show()

# Example usage
converted_strings = [
    double_backslashes(
        r"C:\Users\nares\Desktop\allout\20240117\20240117_1813_51top.csv"
        ),
    double_backslashes(
        r"C:\Users\nares\Desktop\allout\20240117\20240117_1813_51top.csv"
        )
]

csv_plotter = CSVPlotter(converted_strings)
csv_plotter.plot_data(x_column='SN', y_columns=['PZT volt', 'Contrast', 'SD'], plot_type='line', title='CSV Data Plot', x_label='Time (s)', y_label='Y-axis', font_size=12)
