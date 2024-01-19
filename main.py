import pandas as pd
import matplotlib.pyplot as plt

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

        fig, axs = plt.subplots(len(y_columns), 1, figsize=(8, 6 * len(y_columns)), sharex=True, gridspec_kw={'hspace': 0})

        for i, col in enumerate(y_columns):
            if plot_type == 'line':
                axs[i].plot(self.data[x_column], self.data[col], label=col)
            elif plot_type == 'scatter':
                axs[i].scatter(self.data[x_column], self.data[col], label=col)
            else:
                print("Invalid plot type. Please choose 'line' or 'scatter'.")

            axs[i].set_title('')  # Clear subplot title
            axs[i].set_xlabel('')  # Clear x-label for all subplots
            axs[i].set_ylabel(col, fontsize=font_size)  # Set ylabel to the column name with custom font size
            axs[i].tick_params(axis='y', labelsize=font_size)
            #axs[i].legend(fontsize=font_size)

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

# Example Usage:
csv_plotter = CSVPlotter('C:\\Users\\nares\\Desktop\\Zikken\\20231218\\OneDrive-2023-12-18\\20231218_1552_23top.csv')

csv_plotter.plot_data(x_column='No of frame', y_columns=['Contrast', 'PZT volt', 'SD'], plot_type='line', title='CSV Data Plot', x_label='X-axis', y_label='Y-axis', font_size=24)
