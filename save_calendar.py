import pandas as pd
from pathlib import Path
import plotly.io as pio
from visualization import create_visualization_figure  # Ensure this is correctly implemented


def ensure_directories_exist(path):
    """Ensure that the directory exists; if not, create it."""
    if not path.exists():
        path.mkdir(parents=True)


def save_calendar_files(df, month, visualization_dir='visualizations'):
    """Save the calendar data and visualizations in designated directories."""
    month_dir = Path(visualization_dir) / f"{month}_calendar"
    ensure_directories_exist(month_dir)

    csv_file_path = month_dir / f'{month}_calendar.csv'
    html_file_path = month_dir / f'{month}_calendar.html'

    if csv_file_path.exists():
        existing_df = pd.read_csv(csv_file_path, index_col=0)
        # Attempt to merge new events with existing ones without losing information
        for index, row in df.iterrows():
            for col in df.columns:
                if pd.isnull(existing_df.at[index, col]) and not pd.isnull(row[col]):
                    existing_df.at[index, col] = row[col]
                elif not pd.isnull(row[col]):
                    # If the slot is not empty but there's a new event, append the event.
                    existing_df.at[index, col] += f"; {row[col]}"
    else:
        existing_df = df

    existing_df.to_csv(csv_file_path)

    fig = create_visualization_figure(existing_df, month)
    pio.write_html(fig, file=html_file_path.as_posix())
