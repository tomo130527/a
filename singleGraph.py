import pandas as pd
import matplotlib.pyplot as plt
def double_backslashes(input_string):
    return input_string.replace('\\', '\\\\')

class CSVPlotter:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def read_csv(self):
        try:
            self.data = pd.read_csv(self.file_path)
        except FileNotFoundError:
            print("File not found. Please provide a valid file path.")
    
    def plot_data(self, x_column, y_columns, plot_type='line', title='', x_label='', y_label=''):
        if self.data is None:
            self.read_csv()
        self.data[x_column] = self.data[x_column]/10
        for i, col in enumerate(y_columns):
            plt.plot(self.data[x_column], self.data[col], label=col)
        
        plt.axhline(y=0.5, color='r', linestyle='--', label='y = 0.5')  # Add this line to plot the horizontal line at y=0.5
        plt.axvline(x=50, color='g', linestyle=':', label='x = 50')  # Vertical line at x=50 (customize x-value as needed)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.legend()
        plt.show()

converted_string = double_backslashes(
    r"C:\Users\nares\Desktop\Zikken\2024116\OneDrive-2024-01-16\20240116_1433_01top.csv"
)
csv_plotter = CSVPlotter(converted_string)

# Plot data from CSV
csv_plotter.plot_data(x_column='SN', y_columns=['PZT volt', 'SD'], plot_type='line', title='CSV Data Plot', x_label='X-axis', y_label='Y-axis')
