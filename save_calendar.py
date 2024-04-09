import pandas as pd
import plotly.io as pio
from visualization import create_visualization_figure  # Ensure this is correctly implemented
from config import VISUALIZATIONS_DIR  # Import the centralized path


def ensure_directories_exist(path):
    """
    Ensure that directories exist at the given path.
    """
    if not path.exists():
        path.mkdir(parents=True)


def save_calendar_files(df, month):
    """
    Save calendar events from a DataFrame to both a CSV file and an HTML visualization file.
    """
    month_dir = VISUALIZATIONS_DIR / f"{month}_calendar"
    ensure_directories_exist(month_dir)

    csv_file_path = month_dir / f'{month}_calendar.csv'
    html_file_path = month_dir / f'{month}_calendar.html'

    # Merge new events with existing ones or directly save the DataFrame if no file exists
    if csv_file_path.exists():
        existing_df = pd.read_csv(csv_file_path, index_col=0)
        for index, row in df.iterrows():
            for col in df.columns:
                if pd.isnull(existing_df.at[index, col]) and not pd.isnull(row[col]):
                    existing_df.at[index, col] = row[col]
                elif not pd.isnull(row[col]):
                    existing_df.at[index, col] += f"; {row[col]}"
    else:
        existing_df = df

    existing_df.to_csv(csv_file_path)

    # Generate and save the visualization HTML file
    fig = create_visualization_figure(existing_df, month)
    pio.write_html(fig, file=html_file_path.as_posix())

    return html_file_path
