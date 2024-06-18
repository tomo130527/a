import pandas as pd
import matplotlib.pyplot as plt
from constants import *
from ui_helper import *


def preprocess_data(data, x_column, y_columns, scale_x=10, sd_scale=40, pzt_scale=0.7):
    data[x_column] = data[x_column] / scale_x
    if 'SD' in y_columns:
        data['SD'] *= sd_scale
    if 'PZT volt' in y_columns:
        data['PZT volt'] *= pzt_scale
    return data

def truncate_data(data, truncate_frame):
    data = data.iloc[truncate_frame:].copy()
    data.iloc[:, 0] = (data.iloc[:, 0] - truncate_frame) / 10
    return data


def one_graph_all_param(data):
    data[x_column] = data[x_column]/10
    for i, col in enumerate(y_columns):
        plt.plot(data[x_column], data[col], label=col)
    
    plt.axhline(y=0.5, color='r', linestyle='--', label='y = 0.5')  # Add this line to plot the horizontal line at y=0.5
    plt.axvline(x=50, color='g', linestyle=':', label='x = 50')  # Vertical line at x=50 (customize x-value as needed)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.show()

def plot_datoooa(data):
    preprocess_data(data)
    fig, axs = plt.subplots(len(y_columns), 1, figsize=(8, 6 * len(y_columns)), sharex=True, gridspec_kw={'hspace': 0})
    hori= 0.15
    for i, col in enumerate(y_columns):
        axs[i].plot(data[x_column], data[col], label=col)
        axs[i].set_title('')  # Clear subplot title
        axs[i].set_xlabel('')  # Clear x-label for all subplots
        axs[i].set_ylabel(col, fontsize=font_size)  # Set ylabel to the column name with custom font size
        axs[i].tick_params(axis='y', labelsize=font_size)
        axs[i].legend(fontsize=font_size)
        axs[1].axhline(y=hori, color='g', linestyle=':', label=hori) 

        if i < len(y_columns) - 1:
            axs[i].get_xaxis().set_visible(False)  # Hide x-axis for all except the last subplot

    verticalline1 = 12
    verticalline2 = 2
    verticalline3 = 1
    axs[-1].set_xlabel(x_label, fontsize=font_size)  # Set x-label only for the last subplot
    #axs[-1].axvline(x=verticalline1, color='g', linestyle=':', label=verticalline1) 
    #axs[-1].axvline(x=verticalline2, color='b', linestyle=':', label=verticalline2) 
    #axs[-1].axvline(x=verticalline3, color='r', linestyle=':', label=verticalline3) 


    # Hide top and right spines and ticks for all subplots except the bottom one
    for ax in axs[:-1]:
        ax.spines['bottom'].set_visible(False)
        ax.xaxis.set_ticks_position('none')

    # Set font sizes for tick labels
    plt.xticks(fontsize=font_size)
    plt.yticks(fontsize=font_size)

    plt.tight_layout()
    plt.show()


def plot_popodata(data):
    x_column = data.columns[0]
    y_columns = data.columns[1:]
    max_frame=742
    truncate_frame=92
    data = data.iloc[truncate_frame:]
    data[x_column] = (data[x_column]-truncate_frame) / 10
    fig, axs = plt.subplots(len(y_columns), 1, figsize=(8, 6 * len(y_columns)), sharex=True, gridspec_kw={'hspace': 0})

    for i, col in enumerate(y_columns):
        if len(data[x_column]) > max_frame:
            data = data.iloc[:max_frame]
        if col != 'PZT volt':
            axs[i].plot(data[x_column], data[col], label=col)
            axs[i].set_title('')  # Clear subplot title
            axs[i].set_xlabel('')  # Clear x-label for all subplots
            axs[i].set_ylabel(col, fontsize=font_size)  # Set ylabel to the column name with custom font size
            axs[i].tick_params(axis='y', labelsize=font_size)

        if i < len(y_columns) - 1:
            axs[i].get_xaxis().set_visible(False)  # Hide x-axis for all except the last subplot

        if col == 'PZT volt':  # Check if it's the third subplot ('PZT volt')
            axs[i].plot(data[x_column], data[col] - 1.1, label=col + ' - 0.54')
    
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


def th_plot_data(data):
    # Extract column names for x and y columns from the first row
    x_column = data.columns[0]
    y_columns = data.columns[1:]

    # Define the parameters
    max_frame = 742
    truncate_frame = 180
    font_size = 12
    x_label = x_column

    # Truncate the data
     # Truncate the data
    data = data.iloc[truncate_frame:].copy()
    data[x_column] = data[x_column].astype(float)  # Explicitly cast to float
    data.loc[:, x_column] = (data[x_column] - truncate_frame) / 10
    
    # Create subplots
    fig, axs = plt.subplots(len(y_columns), 1, figsize=(10, len(y_columns) * 2), sharex=True, gridspec_kw={'hspace': 0})

    # Plot each y_column
    for i, col in enumerate(y_columns):
        axs[i].plot(data[x_column], data[col], label=col)
        axs[i].set_ylabel(col, fontsize=font_size)
        axs[i].tick_params(axis='y', labelsize=font_size)
        
        # Hide x-axis for all except the last subplot
        if i < len(y_columns) - 1:
            axs[i].get_xaxis().set_visible(False)

    # Set x-label for the last subplot
    axs[-1].set_xlabel(x_label, fontsize=font_size)

    # Customize the plots
    for ax in axs[:-1]:
        ax.spines['bottom'].set_visible(False)
        ax.xaxis.set_ticks_position('none')

    # Add horizontal lines
    plt.axhline(y=0.020, color='r', linestyle='--', label='y = 0.5')
    plt.axhline(y=0.013, color='b', linestyle='--', label='y = 0.5')

    plt.xticks(fontsize=font_size)
    plt.yticks(fontsize=font_size)
    plt.tight_layout()
    plt.show()


def th_plot_datatt(data):
    x_column = data.columns[0]
    y_columns = data.columns[1:]
    max_frame=742
    truncate_frame=180
    data = data.iloc[truncate_frame:]
    data[x_column] = (data[x_column]-truncate_frame) / 10
    fig, axs = plt.subplots(len(y_columns), 1, figsize=(len(x_column),len(y_columns)), sharex=True, gridspec_kw={'hspace': 0})

    for i, col in enumerate(y_columns):
        axs[i].plot(data[x_column], data[col], label=col)
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


def two_file_plot_data(two_files, x_column="sn", x_label="B"):
    data = [None, None]
    data[0] = pd.read_csv(two_files[0])
    data[1] = pd.read_csv(two_files[1])

    # Collect all y_columns from both dataframes, excluding unnamed columns
    y_columns = set()
    for df in data:
        if df is not None:
            y_columns.update(col for col in df.columns if not col.startswith('Unnamed'))
    y_columns.discard(x_column)

    # Determine the number of subplots needed
    num_y_columns = len(y_columns)
    num_files = len(data)

    if num_y_columns == 0:
        print("No y-columns found.")
        return

    if num_files == 1:
        fig, axs = plt.subplots(num_y_columns, 1, figsize=(8, 6 * num_y_columns), sharex=True, gridspec_kw={'hspace': 0})
        if num_y_columns == 1:
            axs = [axs]  # Make axs iterable
    else:
        fig, axs = plt.subplots(num_files, num_y_columns, figsize=(15, 8), sharex=True)
        if num_files == 1:
            axs = [axs]  # Make axs iterable
        elif num_y_columns == 1:
            axs = [[ax] for ax in axs]  # Make axs 2D iterable

    for j, (df, file_path) in enumerate(zip(data, two_files)):
        if df is None:
            continue

        for i, col in enumerate(y_columns):
            if col in df.columns:
                if num_files == 1:
                    ax = axs[i]
                else:
                    ax = axs[j][i]

                ax.plot(df[x_column], df[col], label=f'{col}')
                ax.set_title(col)
                ax.set_xlabel(x_label)
                if j == 0:  # Set y-axis label only for the first row
                    ax.set_ylabel(f'{col}')
                ax.legend()

    plt.tight_layout()
    plt.show()