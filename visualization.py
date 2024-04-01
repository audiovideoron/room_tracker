# TODO: Displaying Event Names: To ensure event names are visible,
# added alpha channel to colors and adjusted opacity

# TODO: Display Room Names: In what would be row 0 and centered in each column

import plotly.graph_objects as go
import pandas as pd
import numpy as np


def create_visualization_figure(df, month):
    fig = go.Figure()

    print("DataFrame to visualize:")
    print(df)

    room_positions = np.linspace(start=1, stop=4, num=4)

    event_colors = {
        event: f'rgba({np.random.randint(0, 255)}, {np.random.randint(0, 255)}, {np.random.randint(0, 255)}, 0.5)'
        for event in pd.unique(df.values.ravel()) if pd.notnull(event)}

    # Debugging: Print the event colors mapping
    print("Event colors mapping:")
    print(event_colors)

    # Add rectangles for the events
    for room, pos in zip(df.columns, room_positions):
        events_in_room = df[room].dropna()
        for day, event in events_in_room.items():
            fig.add_shape(
                type="rect",
                x0=pos - 0.5, y0=day,
                x1=pos + 0.5, y1=day + 1,
                line=dict(color=event_colors[event]),
                fillcolor=event_colors[event]
            )

            fig.add_trace(go.Scatter(
                x=[pos],
                y=[day + 0.5],
                text=[event],
                mode='text',
                textposition='middle center',
                showlegend=False
            ))
    # Debugging: Print a message indicating completion of adding events
    print("Completed adding all events to the figure.")

    # Customizing the layout to place room labels at the top and ensure grid appearance
    fig.update_layout(
        title=f'Ballroom Occupancy for {month}',
        xaxis=dict(
            tickmode='array',
            tickvals=[],  # Positions between the columns
            ticktext=[],  # No text for these ticks
            showgrid=True,  # Show grid lines
            gridwidth=1,
            gridcolor='lightgrey',
            zeroline=False,  # No line at x=0
            side='top'  # Position room names at the top of the chart
        ),
        yaxis=dict(
            autorange='reversed',  # Reverse the y-axis to have day 1 at the top
            tickmode='array',
            tickvals=list(range(1, 33)),  # Extend to include an extra tick for visual space
            ticktext=[str(day) if day <= 31 else "" for day in range(1, 33)],  # Leave the last tick label empty
            showgrid=True,
            gridcolor='lightgrey',
            gridwidth=1,
            range=[0.8, 31.5]  # Extend the range of y-axis to make room for new label
        ),
        plot_bgcolor="white",  # Set background color to white
        hovermode='closest',
        showlegend=True
    )

    # Add custom vertical grid lines
    for line_pos in np.linspace(start=1.5, stop=3.5, num=3):  # Adjust start and stop according to your columns position
        fig.add_shape(
            type='line',
            x0=line_pos, y0=0.5,
            x1=line_pos, y1=31.5,
            line=dict(color='lightgrey', width=2),
            layer='below'
        )

    # Add a rectangle around the outer perimeter of the grid to emphasize the boundary
    fig.add_shape(
        type="rect",
        x0=0.5, y0=-0,
        x1=4.5, y1=32,
        line=dict(color="Black", width=2),
        layer="below"
    )

    # Add a solid color background for row 0
    fig.add_shape(
        type="rect",
        x0=0.5, y0=-0.5,  # Adjust y0 to be just below row 0
        x1=4.5, y1=0.5,  # Adjust y1 to be just above row 1
        line=dict(color="Black", width=0),
        fillcolor="Black",  # Set the background color to black
        layer="above"
    )

    # Now, you would add the room name annotations with white text as previously described:
    room_names = ['Ballroom 4', 'Ballroom 3', 'Ballroom 2', 'Ballroom 1']  # Assuming these are the room names
    for name, pos in zip(room_names, room_positions):
        fig.add_annotation(
            x=pos,
            y=0,  # Position at the top, you might need to adjust this position
            text=name,
            showarrow=False,
            font=dict(size=18, color='white'),  # Set font size and color to white
            xanchor='center',  # Ensure the text is centered
            yanchor='middle',  # Anchor text at the bottom of the top margin
        )

        # Debugging: Print a message before returning the figure
        print("Returning the generated figure.")

    return fig


def display_figure(fig, filename='visualization.html'):
    """
    Saves the figure as an HTML file and automatically opens it in the default web browser.
    """
    fig.write_html(filename, auto_open=True)


# Sample usage
if __name__ == '__main__':
    from generate_sample_data import generate_sample_dataframe

    # Unpack the tuple returned by generate_sample_dataframe into df_sample and sample_month
    df_sample, sample_month = generate_sample_dataframe()

    # Now that df_sample is a DataFrame and sample_month is a string, pass them to create_visualization_figure
    fig = create_visualization_figure(df_sample, sample_month)

    # Use display_figure to display or save the generated figure
    display_figure(fig, filename='sample_month.html')
