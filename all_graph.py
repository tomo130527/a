import pandas as pd
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from helper import read_csv, read_csv_two

def one_graph_all_param(data, x_column, y_columns, plot_type='line', title='', x_label='', y_label=''):
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

def one_graph_all_paramii(data, x_column, y_columns, plot_type='line', title='', x_label='', y_label=''):
    data[x_column] = data[x_column] / 10
    fig = Figure()
    ax = fig.add_subplot(111)
    
    for col in y_columns:
        if plot_type == 'line':
            ax.plot(data[x_column], data[col], label=col)
    
    ax.axhline(y=0.5, color='r', linestyle='--', label='y = 0.5')
    ax.axvline(x=50, color='g', linestyle=':', label='x = 50')
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.legend()
    
    return fig, ax


def plot_datoooa(data, x_column, y_columns, plot_type='line', title='', x_label='', y_label='', font_size=24):
    data[x_column] = (data[x_column]) / 10    
    # Multiply the "SD" column by 15
    if 'SD' in y_columns:
        data['SD'] *= 40
    if 'PZT volt' in y_columns:
        data['PZT volt'] *= 0.7

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


def plot_popodata(data, x_column, y_columns, plot_type='line', title='', x_label='', y_label='', font_size=24,max_frame=742,truncate_frame=92):
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


def th_plot_data(data, x_column, y_columns, plot_type='line', title='', x_label='', y_label='', font_size=24,max_frame=742,truncate_frame=180):
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



def two_file_plot_data(two_files, x_column, plot_type='line', title='', x_label='', font_size=24, max_frame=99999, truncate_frame=0):
    data = read_csv_two(two_files)
    if any(data is None for data in data):
        data = read_csv_two(two_files)

    y_columns = set(column for data in data if data is not None for column in data.columns)
    y_columns.discard(x_column)

    if len(data) == 1:
        fig, axs = plt.subplots(len(y_columns), 1, figsize=(8, 6 * len(y_columns)), sharex=True, gridspec_kw={'hspace': 0})
    else:
        fig, axs = plt.subplots(len(data), len(y_columns), figsize=(15, 8), sharex=True)

    for j, (data, file_path) in enumerate(zip(data, two_files)):
        if len(data) == 1:
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
