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
    
    def plot_data(self, x_column, y_columns, plot_type='line', title='', x_label='', y_label='', font_size=24):
        if self.data is None:
            self.read_csv()

        self.data[x_column] = (self.data[x_column]) / 10
        fig, axs = plt.subplots(len(y_columns), 1, figsize=(8, 6 * len(y_columns)), sharex=True, gridspec_kw={'hspace': 0})
        
        for i, col in enumerate(y_columns):
            axs[i].plot(self.data[x_column], self.data[col], label=col,linewidth=3)
            axs[i].set_title('')  # Clear subplot title
            axs[i].set_xlabel('')  # Clear x-label for all subplots
            axs[1].set_ylabel("Height", fontsize=font_size)  # Set ylabel to the column name with custom font size
            axs[0].set_ylabel("Brightness Difference", fontsize=font_size)  # Set ylabel to the column name with custom font size
            axs[i].tick_params(axis='y', labelsize=font_size)
            #axs[i].legend(fontsize=font_size)
            hori= 0.18
            axs[0].axhline(y=hori, color='g', linestyle=':', label=hori) 
            verticalline1 = 2.73
            verticalline2 = 4.73
            verticalline3 = 5.202
            axs[i].axvline(x=verticalline1, color='g', linestyle=':', label=verticalline1) 
            axs[i].axvline(x=verticalline2, color='b', linestyle=':', label=verticalline2) 
            axs[i].axvline(x=verticalline3, color='r', linestyle=':', label=verticalline3) 

            if i < len(y_columns) - 1:
                axs[i].get_xaxis().set_visible(False)  # Hide x-axis for all except the last subplot

        
        axs[-1].set_xlabel(x_label, fontsize=font_size)  # Set x-label only for the last subplot
        


        # Hide top and right spines and ticks for all subplots except the bottom one
        for ax in axs[:-1]:
            ax.spines['bottom'].set_visible(False)
            ax.xaxis.set_ticks_position('none')

        # Set font sizes for tick labels
        plt.xticks(fontsize=font_size)
        plt.yticks(fontsize=font_size)

        plt.tight_layout()
        plt.show()

# Example usage
converted_string = double_backslashes(
    r"C:\Users\nares\Downloads\240219\240219_182917.csv"

)
csv_plotter = CSVPlotter(converted_string)
csv_plotter.plot_data(x_column='time(s)', y_columns=['SD','PZT'], plot_type='line', title='CSV Data Plot', x_label='Time (s)', y_label='Y-axis', font_size=24)
#