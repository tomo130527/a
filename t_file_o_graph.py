import matplotlib.pyplot as plt
import pandas as pd
from ui_helper import double_backslashes

def plot_csv_data(file):
    # Read the CSV file
    df = pd.read_csv(file, index_col=0)  # Assume the first column is the index

    # Plot the data
    fig, ax = plt.subplots(figsize=(10, 6))
    df.plot(ax=ax)

    # Customize the plot
    ax.set_title(f'Data from {file}', fontsize=16)
    ax.set_xlabel('Index', fontsize=12)
    ax.set_ylabel('Values', fontsize=12)
    ax.legend(title='Columns')

    # Improve the appearance
    ax.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()




def plot_csv_data_two(file1, file2):
    # Read the CSV files
    df1 = pd.read_csv(file1, index_col=0)  # Assume the first column is the index
    df2 = pd.read_csv(file2, index_col=0)  # Assume the first column is the index

    # Create a new DataFrame to hold concatenated data
    concatenated_df = pd.concat([df1.add_suffix('_file1'), df2.add_suffix('_file2')], axis=1)
    concatenated_df = concatenated_df.reset_index(drop=True)  # Reset index to get rid of index issues

    # Plot the data
    fig, ax = plt.subplots(figsize=(10, 6))
    concatenated_df.plot(ax=ax)

    # Customize the plot
    ax.set_title('Data from both files', fontsize=16)
    ax.set_xlabel('Index', fontsize=12)
    ax.set_ylabel('Values', fontsize=12)
    ax.legend(title='Columns')

    # Improve the appearance
    ax.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()



file1 = double_backslashes(r"C:\Users\nares\Desktop\allout\240614\saa.csv")
file2 = double_backslashes(r"C:\Users\nares\Desktop\allout\240614\thh.csv")

# Plot both files
plot_csv_data_two(file1,file2)