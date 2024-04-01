import pandas as pd
from pathlib import Path
import plotly.io as pio
from visualization import create_visualization_figure  # Ensure this function is correctly implemented

def ensure_directories_exist(path):
    """Ensure that the specified directory exists; if not, it creates the directory."""
    path = Path(path)
    if not path.exists():
        path.mkdir(parents=True)

def save_calendar_files(df, month, visualization_dir='visualizations'):
    """Save the calendar data and visualizations in designated directories."""
    month_dir = Path(visualization_dir) / f"{month}_calendar"
    ensure_directories_exist(month_dir)

    # Define file paths
    csv_file_path = month_dir / f'{month}_calendar.csv'
    html_file_path = month_dir / f'{month}_calendar.html'

    # Load existing data if available and combine with new data
    if csv_file_path.exists():
        existing_df = pd.read_csv(csv_file_path, index_col=0)
        print("Existing DataFrame loaded:")
        print(existing_df)
        combined_df = pd.concat([existing_df, df], sort=False).drop_duplicates()
        print("Combined DataFrame after appending new data:")
        print(combined_df)
    else:
        combined_df = df
        print("New DataFrame, no existing data:")
        print(combined_df)

    # Save combined DataFrame to CSV (This part remains unchanged)
    combined_df.to_csv(csv_file_path)
    print(f"Saving data to: {csv_file_path}")  # Newly added print statement

    # Regenerate the visualization with combined data
    print("Creating visualization for new data...")
    fig = create_visualization_figure(combined_df, month)
    print("Visualization created.")

    # Save HTML visualization
    print(f"Saving HTML visualization to: {html_file_path}")  # Newly added print statement
    pio.write_html(fig, file=str(html_file_path))  # Ensure string path
    print("HTML visualization saved.")

    # print(f"Data saved as CSV: {csv_file_path}")
    # print(f"Visualization updated and saved as HTML: {html_file_path}")
