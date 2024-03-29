import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd
import numpy as np


def visualize_calendar(calendar_df, month):
    fig, ax = plt.subplots(figsize=(10, 12))
    # Set the title at the top of the figure
    plt.title(f'Ballroom Occupancy for {month}', fontsize=20, pad=20)
    # Set room positions and labels
    room_positions = {room: index for index, room in enumerate(calendar_df.columns)}
    ax.set_xticks(np.arange(len(calendar_df.columns)) + 0.5)
    ax.set_xticklabels(calendar_df.columns)
    ax.set_xlim(0, len(calendar_df.columns))
    # Set y-ticks to show dates at the center of each row
    ax.set_yticks(np.arange(len(calendar_df.index)) + 0.5)
    ax.set_yticklabels(reversed(calendar_df.index))
    ax.set_ylim(0, len(calendar_df.index))
    # Grid and labels
    ax.set_axisbelow(True)
    ax.yaxis.grid(True)
    ax.xaxis.tick_top()
    ax.xaxis.set_label_position('top')
    ax.set_xlabel('Rooms')
    ax.set_ylabel('Dates')

    # Generate a color map for events
    unique_events = pd.unique(calendar_df.values.ravel())
    colors = plt.cm.get_cmap('tab20', len(unique_events))
    event_colors = {event: colors(i) for i, event in enumerate(unique_events) if pd.notna(event)}

# This is version 3
    # ... [unchanged parts of your code] ...

    # Draw colored backgrounds for events
    for room_index, room in enumerate(calendar_df.columns):
        for day in calendar_df.index:
            event = calendar_df.at[day, room]
            if pd.notna(event):
                # Adjust the y-coordinate by adding 0.5 to shift the event rectangle up to align with the grid
                rect_y = len(calendar_df.index) - day + 0.5
                color = event_colors.get(event, 'lightgrey')
                rect = patches.Rectangle((room_index, rect_y - 1), 1, 1, color=color, alpha=0.5)
                ax.add_patch(rect)
                # Center the text within the shifted rectangle
                ax.text(room_index + 0.5, rect_y - 0.5, event, ha='center', va='center', fontsize=10)

    # ...

    # ... [rest of the plotting code] ...
    # Month label
    # plt.text(0.5, -0.05, month, fontsize=20, transform=ax.transAxes, ha='center', va='center')
    plt.show()


# Create an example DataFrame structure with some events
calendar_df_example = pd.DataFrame({
    'v4': [np.nan] * 32,
    'v3': [np.nan] * 32,
    'v2': [np.nan] * 32,
    'v1': [np.nan] * 32
}, index=range(1, 33))
calendar_df_example.at[10, 'v2'] = 'Event2'
calendar_df_example.at[14, 'v1'] = 'Event3'
calendar_df_example.at[20, 'v4'] = 'Event4'
calendar_df_example.at[5, 'v1'] = 'Event5'
calendar_df_example.at[5, 'v2'] = 'Event5'
calendar_df_example.at[6, 'v1'] = 'Event5'
calendar_df_example.at[6, 'v2'] = 'Event5'
calendar_df_example.at[12, 'v3'] = 'Event6'
calendar_df_example.at[15, 'v2'] = 'Event7'
calendar_df_example.at[15, 'v3'] = 'Event7'
calendar_df_example.at[16, 'v2'] = 'Event7'
calendar_df_example.at[16, 'v3'] = 'Event7'
calendar_df_example.at[17, 'v2'] = 'Event7'
calendar_df_example.at[17, 'v3'] = 'Event7'
calendar_df_example.at[22, 'v1'] = 'Event8'
calendar_df_example.at[22, 'v4'] = 'Event8'
calendar_df_example.at[23, 'v4'] = 'Event8'
calendar_df_example.at[24, 'v4'] = 'Event8'
calendar_df_example.at[26, 'v1'] = 'Event9'
calendar_df_example.at[26, 'v2'] = 'Event9'
calendar_df_example.at[28, 'v3'] = 'Event10'
calendar_df_example.at[30, 'v2'] = 'Event11'
calendar_df_example.at[30, 'v3'] = 'Event11'
calendar_df_example.at[31, 'v2'] = 'Event12'
calendar_df_example.at[31, 'v3'] = 'Event12'
calendar_df_example.at[31, 'v4'] = 'Event12'

visualize_calendar(calendar_df_example, 'May')
