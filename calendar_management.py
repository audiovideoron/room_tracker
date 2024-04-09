import pandas as pd
import plotly.io as pio
from visualization import create_visualization_figure
from config import VISUALIZATIONS_DIR
from display import display_in_browser


def select_month_for_action():
    """
    List available months and prompt the user to select one.
    """
    months = list_files(VISUALIZATIONS_DIR)
    if not months:
        print("No calendars available.")
        return None

    print("Available Calendars:")
    for index, month in enumerate(months, start=1):
        print(f"{index}. {month}")

    try:
        choice = int(input("Select a month: ")) - 1
        if 0 <= choice < len(months):
            selected_month = months[choice].replace('_calendar', '')  # Remove '_calendar' if present in the
            # directory names
            return selected_month
        else:
            print("Selection out of range.")
            return None
    except ValueError:
        print("Invalid selection.")
        return None


def list_files(directory_path, extension=None):
    """
    List all files in the directory, optionally filtering by extension.
    If 'extension' is None, directories are listed instead.
    """
    if extension:
        return [file.name for file in directory_path.glob(f'*{extension}')]
    else:
        return [d.name for d in directory_path.iterdir() if d.is_dir()]


def ensure_directories_exist(path):
    """Ensure that directories exist at the given path."""
    path.mkdir(parents=True, exist_ok=True)


def save_calendar_files(df, month):
    """
    Saves calendar events from a DataFrame to a CSV file and regenerates the HTML visualization.
    """
    month_dir = VISUALIZATIONS_DIR / f"{month}_calendar"
    ensure_directories_exist(month_dir)

    csv_file_path = month_dir / f'{month}_calendar.csv'
    html_file_path = month_dir / f'{month}_calendar.html'

    df.to_csv(csv_file_path, index=False)

    fig = create_visualization_figure(df, month)
    pio.write_html(fig, file=html_file_path)

    return html_file_path


def view_calendar(month):
    """
    Displays the calendar for the selected month.
    """
    html_file_path = VISUALIZATIONS_DIR / month / f"{month}.html"
    if not html_file_path.exists():
        print(f"No calendar available to view for {month}.")
        return

    display_in_browser(html_file_path)


def edit_calendar(month):
    csv_file_path = VISUALIZATIONS_DIR / f"{month}_calendar" / f"{month}_calendar.csv"
    if not csv_file_path.exists():
        print(f"No calendar found for {month}.")
        return

    # Load the DataFrame ensuring the first column is used as the index
    df = pd.read_csv(csv_file_path, index_col=0)

    print("DataFrame before any operations:")
    print(df)

    # Assuming events are repeated across the DataFrame and you want to capture distinct names
    unique_events = pd.unique(df.values.ravel())
    unique_events = [event for event in unique_events if pd.notna(event) and isinstance(event, str)]

    print("Unique events before filtering:", unique_events)

    print("Available events:")
    for i, event in enumerate(unique_events, start=1):
        print(f"{i}: Event '{event}'")

    try:
        choice = int(input("Select an event number to edit: ")) - 1
        if choice < 0 or choice >= len(unique_events):
            print("Invalid selection. Please choose a valid event number.")
            return
        selected_event_name = unique_events[choice]
        new_name = input("Enter the new name for the event: ")

        # Apply new name to all instances of the event
        for col in df.columns:
            df[col] = df[col].replace(selected_event_name, new_name)

        print("DataFrame after replacement:")
        print(df)

    except ValueError as e:
        print(f"Error: {e}")
        return

    # Save the updated DataFrame back to the CSV file ensuring index is preserved
    df.to_csv(csv_file_path, index=True)

    print(f"Event '{selected_event_name}' updated to '{new_name}'.")

    # Regenerate HTML visualization and display it
    # Make sure that save_calendar_files function is equipped to regenerate the HTML visualization
    save_calendar_files(df, month)

    # Use the path to the HTML file for displaying in the browser
    html_file_path = VISUALIZATIONS_DIR / f"{month}_calendar" / f"{month}_calendar.html"
    print(f"Event '{unique_events[choice]}' updated to '{new_name}'. Displaying the updated calendar...")
    display_in_browser(html_file_path)
