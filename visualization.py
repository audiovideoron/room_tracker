# TODO: Evenly Spaced Columns for each room: We can adjust the x-axis tick positions
# to correctly place the room labels over the evenly spaced columns they must be centered.

# TODO: Grid Lines: The addition of the gridlines can be done by specifying
# showgrid=True in the layout update for both the x-axis and y-axis.
# These lines will help define the spreadsheet-like structure.

# TODO: Displaying Event Names: To ensure event names are visible,
# we can adjust the text font size and color to make sure
# it stands out over the event color.

import plotly.graph_objects as go
import pandas as pd
import numpy as np


def create_visualization_figure(df, month):
    fig = go.Figure()

    # Define evenly spaced positions for the four room columns
    room_positions = np.linspace(start=1, stop=4, num=4)

    # Define a dictionary to assign each room a unique color
    event_colors = {event: f'rgb({np.random.randint(0, 255)}, {np.random.randint(0, 255)}, {np.random.randint(0, 255)})'
                    for event in pd.unique(df.values.ravel()) if pd.notnull(event)}

    # Add rectangles for the events
    for room, pos in zip(df.columns, room_positions):
        events_in_room = df[room].dropna()
        for day, event in events_in_room.items():
            fig.add_shape(
                type="rect",
                x0=pos - 0.5, y0=day - 0.5,
                x1=pos + 0.5, y1=day + 0.5,
                line=dict(color=event_colors[event]),
                fillcolor=event_colors[event]
            )
            # Add the event name text in the center of the rectangle
            fig.add_trace(go.Scatter(
                x=[pos],
                y=[day],
                text=[event],
                mode='text',
                textposition='middle center',
                showlegend=False
            ))

    # Customizing the layout to place room labels at the top and ensure grid appearance
    fig.update_layout(
        title=f'Event Schedule for {month}',
        xaxis=dict(
            tickmode='array',
            tickvals=list(room_positions),
            ticktext=df.columns,
            showgrid=True,  # Show vertical gridlines for rooms
            gridwidth=1,
            gridcolor='lightgrey',
            side='top'  # Position room names at the top of the chart
        ),
        yaxis=dict(
            autorange='reversed',  # Reverse the y-axis to have day 1 at the top
            tickmode='array',
            tickvals=list(range(1, 32)),
            ticktext=[str(day) for day in range(1, 32)],
            showgrid=True,  # Show horizontal gridlines for days
            gridwidth=1,
            gridcolor='lightgrey'
        ),
        plot_bgcolor="white",  # Set background color to white
        hovermode='closest',
        showlegend=True
    )

    # Add a rectangle around the outer perimeter of the grid to emphasize the boundary
    fig.add_shape(
        type="rect",
        x0=0.5, y0=0.5,
        x1=4.5, y1=31.5,
        line=dict(color="Black", width=2),
        fillcolor="lightgrey",
        layer="below"
    )

    return fig


def display_figure(fig, filename='visualization.html'):
    """
    Saves the figure as an HTML file and automatically opens it in the default web browser.
    """
    fig.write_html(filename, auto_open=True)


# Sample usage
if __name__ == '__main__':
    # Create a sample DataFrame for demonstration purposes
    sample_data = {
        'v4': [None] * 31, 'v3': [None] * 31, 'v2': [None] * 31, 'v1': [None] * 31,
    }
    df_sample = pd.DataFrame(sample_data, index=np.arange(1, 32))
    df_sample.at[10, 'v2'] = 'Event1'
    df_sample.at[20, 'v4'] = 'Event2'

    # Create and display the figure
    fig = create_visualization_figure(df_sample, 'Sample Month')
    display_figure(fig)
