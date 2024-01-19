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
    
    def plot_data(self, x_column, y_columns, plot_type='line', title='', x_label='', y_label='', font_size=24,max_frame=742,truncate_frame=92):
        if self.data is None:
            self.read_csv()
        self.data = self.data.iloc[truncate_frame:]
        self.data[x_column] = (self.data[x_column]-truncate_frame) / 10
        #fig, axs = plt.subplots(len(y_columns), 1, figsize=(8, 6 * len(y_columns)), sharex=True, gridspec_kw={'hspace': 0})
        fig, axs = plt.subplots(len(y_columns), 1, figsize=(len(x_column), len(y_columns)), sharex=True, gridspec_kw={'hspace': 0})

        for i, col in enumerate(y_columns):
            if len(self.data[x_column]) > max_frame:
                self.data = self.data.iloc[:max_frame]
            if col != 'PZT volt':
                axs[i].plot(self.data[x_column], self.data[col], label=col)
                axs[i].set_title('')  # Clear subplot title
                axs[i].set_xlabel('')  # Clear x-label for all subplots
                axs[i].set_ylabel(col, fontsize=font_size)  # Set ylabel to the column name with custom font size
                axs[i].tick_params(axis='y', labelsize=font_size)

            if i < len(y_columns) - 1:
                axs[i].get_xaxis().set_visible(False)  # Hide x-axis for all except the last subplot

            if col == 'PZT volt':  # Check if it's the third subplot ('PZT volt')
                axs[i].plot(self.data[x_column], self.data[col] - 1.1, label=col + ' - 0.54')
                axs[i].set_ylabel(col, fontsize=font_size)
        
        axs[1].axhline(y=0.020, color='r', linestyle='--', label='Upper Th = 0.020')
        axs[1].axhline(y=0.013, color='b', linestyle='--', label='Lower Th = 0.013')

        axs[-1].set_xlabel(x_label, fontsize=font_size)  # Set x-label only for the last subplot

        # Hide top and right spines and ticks for all subplots except the bottom one
        for ax in axs[:-1]:
            ax.spines['bottom'].set_visible(False)
            ax.xaxis.set_ticks_position('none')
        
        plt.xticks(fontsize=font_size)
        plt.yticks(fontsize=font_size)
        plt.tight_layout()
        plt.show()

# Example usage
converted_string = double_backslashes(
    #r"C:\Users\nares\Desktop\Zikken\20231124\20231124_1104_09top.csv"
    #r"C:\Users\nares\Desktop\Zikken\20231124\20231124_1111_04sd.csv"
    #r"C:\Users\nares\Desktop\Zikken\20231124\20231124_1123_25sd.csv"
    r"C:\Users\nares\Desktop\Zikken\2024116\OneDrive-2024-01-16\20240116_1433_01top.csv"
)
csv_plotter = CSVPlotter(converted_string)
csv_plotter.plot_data(x_column='SN', y_columns=['Contrast','SD','PZT volt'], plot_type='line', title='CSV Data Plot', x_label='Time (s)', y_label='Y-axis', font_size=24)
