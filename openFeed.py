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
    
    def plot_data(self, x_column, y_columns, plot_type='line', title='', x_label='', y_label='', font_size=24,max_frame=742,truncate_frame=180):
        if self.data is None:
            self.read_csv()

        self.data = self.data.iloc[truncate_frame:]
        self.data[x_column] = (self.data[x_column]-truncate_frame) / 10
        fig, axs = plt.subplots(len(y_columns), 1, figsize=(len(x_column),len(y_columns)), sharex=True, gridspec_kw={'hspace': 0})

        for i, col in enumerate(y_columns):
            axs[i].plot(self.data[x_column], self.data[col], label=col)
            axs[i].set_title('')  # Clear subplot title
            axs[i].set_xlabel('')  # Clear x-label for all subplots
            axs[i].set_ylabel(col, fontsize=font_size)  # Set ylabel to the column name with custom font size
            axs[i].tick_params(axis='y', labelsize=font_size)
            # axs[i].legend(fontsize=font_size)
            #axs[i].axvline(x=14.5, color='g', linestyle=':', label='x = 50') 

            if i < len(y_columns) - 1:
                axs[i].get_xaxis().set_visible(False)  # Hide x-axis for all except the last subplot

        axs[-1].set_xlabel(x_label, fontsize=font_size)  # Set x-label only for the last subplot

        # Hide top and right spines and ticks for all subplots except the bottom one
        for ax in axs[:-1]:
            ax.spines['bottom'].set_visible(False)
            ax.xaxis.set_ticks_position('none')

        
        plt.axhline(y=0.020, color='r', linestyle='--', label='y = 0.5')
        plt.axhline(y=0.013, color='b', linestyle='--', label='y = 0.5')
        
        plt.xticks(fontsize=font_size)
        plt.yticks(fontsize=font_size)
        plt.tight_layout()
        plt.show()

# Example usage
converted_string = double_backslashes(
    r"C:\Users\nares\Desktop\Zikken\20231124\20231124_1104_09top.csv"
    #r"C:\Users\nares\Desktop\Zikken\20231124\20231124_1111_04sd.csv"
)
csv_plotter = CSVPlotter(converted_string)
csv_plotter.plot_data(x_column='No of frame', y_columns=['Contrast','SD'], plot_type='line', title='CSV Data Plot', x_label='Time (s)', y_label='Y-axis', font_size=24)
