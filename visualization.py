import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def visualize_calendar(calendar_df, month):
    fig, ax = plt.subplots(figsize=(8, 10))  # Adjust as necessary for your display

    room_positions = np.arange(len(calendar_df.columns)) + 0.5
    ax.set_xticks(room_positions)
    ax.set_xticklabels(calendar_df.columns)

    # Adjust the room positions if necessary
    ax.set_xlim(0, len(calendar_df.columns))

    # Set the y-axis for the dates
    ax.set_yticks(np.arange(len(calendar_df.index)) + 0.5)
    ax.set_yticklabels(calendar_df.index[::-1])  # Reverse the order to have 1 at the top

    # Adjust the date positions if necessary
    ax.set_ylim(0, len(calendar_df.index))

    ax.set_axisbelow(True)
    ax.yaxis.grid(True)

    ax.xaxis.tick_top()
    ax.xaxis.set_label_position('top')

    # Plot room dividers
    for pos in room_positions - 0.5:
        ax.axvline(x=pos, color='black', linewidth=1)

    # Fill in the events
    # Fill in the events
    for room_index, room in enumerate(calendar_df.columns):
        for day, event in calendar_df[room].items():  # Iterate through each day and event
            if pd.notna(event):
                # Calculate the y position based on the day (index), since the y-ticks are reversed
                text_y_position = len(calendar_df.index) - day  # Subtract the day from the length to reverse
                ax.text(room_index + 0.5, text_y_position, event, ha='center', va='center', fontsize=8)

    ax.set_xlabel('Rooms')
    ax.set_ylabel('Dates')

    # Add the month in a larger font size at the bottom of the plot
    plt.text(0.5, -0.1, month, ha='center', va='center', fontsize=24, transform=ax.transAxes)

    plt.show()
