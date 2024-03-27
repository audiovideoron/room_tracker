import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def visualize_calendar(calendar_df):
    # Set the figure size to accommodate the calendar layout
    fig, ax = plt.subplots(figsize=(8, 10))  # Adjust as necessary for your display

    # Set the number of rooms and create an array for their positions
    room_positions = np.arange(len(calendar_df.columns)) + 0.5

    # Set the room labels above each column, centered
    ax.set_xticks(room_positions)
    ax.set_xticklabels(calendar_df.columns)

    # Set the y-axis for the dates, reversed so 1 is at the top
    ax.set_yticks(np.arange(len(calendar_df.index)) + 0.5)
    ax.set_yticklabels(reversed(calendar_df.index))

    # Make sure the grid is drawn behind the plot elements
    ax.set_axisbelow(True)
    ax.yaxis.grid(True)

    # Plot room dividers and ensure they cover the entire y-range
    for pos in room_positions - 0.5:
        ax.axvline(x=pos, color='black', linewidth=1)

    # Configure x-axis labels to be at the top
    ax.xaxis.tick_top()
    ax.xaxis.set_label_position('top')

    # Adjust the limits to fit the grid exactly
    ax.set_xlim(0, len(calendar_df.columns))
    ax.set_ylim(0, len(calendar_df.index))

    # Fill in the events
    for room_index, room in enumerate(calendar_df.columns):
        for day_index, day in enumerate(calendar_df.index):  # The order is already from top to bottom
            event = calendar_df.at[day, room]
            if pd.notna(event):
                # Ensure the text is positioned according to the index of the DataFrame
                text_y_position = day_index + 0.5  # Adjusting this as needed
                ax.text(room_index + 0.5, text_y_position, event,
                        ha='center', va='center', fontsize=8)

    # Add labels for axes
    ax.set_xlabel('Rooms')
    ax.set_ylabel('Dates')

    plt.show()
