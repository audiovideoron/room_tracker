import pandas as pd
from pathlib import Path
import plotly.io as pio
from visualization import create_visualization_figure  # Ensure this is correctly implemented


def ensure_directories_exist(path):
    """
    Ensure that directories exist at the given path.

    :param path: The path to check and create directories if they don't exist.
    :return: None
    """
    if not path.exists():
        path.mkdir(parents=True)


def save_calendar_files(df, month, visualization_dir='visualizations'):
    """
    Save calendar events from a DataFrame to both a CSV file and an HTML visualization file.

    :param df: The DataFrame that contains the calendar events to be saved. The dataframe should have columns
    representing time slots/events and rows representing days. Non-empty cells should contain event details. :param
    month: The month for which the calendar events are saved. :param visualization_dir: The directory where the
    visualization files will be saved. Defaults to 'visualizations'.

    :return: The path of the saved HTML file.

    Note: If a CSV file already exists for the specified month, the function attempts to merge new events with
    existing ones without losing any information. If any potential conflicts arise (i.e., in case of already booked
    rooms), the new event is appended beside existing events in a semicolon-separated list.
    """
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

    return html_file_path
