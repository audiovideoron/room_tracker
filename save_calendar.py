# save_calendar.py

import os
from pathlib import Path
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio


def ensure_directories_exist(path: Path):
    """Ensure that the specified directory exists; if not, it creates the directory."""
    if not path.exists():
        path.mkdir(parents=True)


def save_calendar_files(df, month, visualization_dir='visualizations'):
    """Save the calendar data and visualizations in designated directories."""
    month_dir = Path(visualization_dir) / f"{month}_calendar"
    ensure_directories_exist(month_dir)

    # Define file paths
    csv_file_path = month_dir / f'{month}_calendar.csv'
    html_file_path = month_dir / f'{month}_calendar.html'
    png_file_path = month_dir / f'{month}_calendar.png'

    # Save DataFrame to CSV
    df.to_csv(csv_file_path)

    # Assume 'fig' is your Plotly figure created from 'df'
    # You might need to adjust this part to create or pass 'fig' appropriately
    fig = go.Figure()  # Placeholder for actual figure creation logic

    # Save the figure as HTML and PNG
    fig.write_html(str(html_file_path))
    fig.write_image(str(png_file_path))

    print(f"Visualization saved as HTML: {html_file_path}")
    print(f"Visualization saved as PNG: {png_file_path}")
    print(f"Data saved as CSV: {csv_file_path}")
