import plotly.graph_objects as go
import pandas as pd
import numpy as np


def create_visualization_figure(df, month):
    fig = go.Figure()

    # Define positions for each room based on their order
    room_positions = {room: i + 1 for i, room in enumerate(df.columns)}

    # Add events as markers, positioned according to their room and day
    for room, pos in room_positions.items():
        events_in_room = df[room].dropna()
        for day, event in events_in_room.items():
            fig.add_trace(go.Scatter(
                x=[pos],  # Position based on room order
                y=[day],
                text=[event],
                mode='markers+text',
                marker=dict(size=12),
                name=event,  # Use event name for the legend
                textposition="bottom center"
            ))

    # Customizing the layout to place room labels at the top and ensure grid appearance
    fig.update_layout(
        title=f'Event Schedule for {month}',
        xaxis=dict(
            tickmode='array',
            tickvals=list(room_positions.values()),
            ticktext=list(room_positions.keys()),
            showgrid=True,  # Show vertical gridlines
            gridwidth=1,
            gridcolor='lightgrey',
            side='top'  # Position room names at the top of the chart
        ),
        yaxis=dict(
            autorange='reversed',
            range=[0.5, 31.5],  # Adjust the range to include all days
            tickmode='array',
            tickvals=list(range(1, 32)),
            ticktext=[str(day) for day in range(1, 32)],
            showgrid=True,  # Show horizontal gridlines
            gridwidth=1,
            gridcolor='lightgrey'
        ),
        plot_bgcolor="white",
        hovermode='closest'
    )

    # Add a rectangle around the outer perimeter of the grid to emphasize boundary
    fig.add_shape(
        type="rect",
        x0=0.5,
        y0=0.5,
        x1=len(df.columns) + 0.5,
        y1=31.5,
        line=dict(
            color="Black",
            width=2,
        ),
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
