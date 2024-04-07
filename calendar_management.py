from pathlib import Path
from display import display_in_browser
import config
from config import VISUALIZATIONS_DIR  # Import the centralized path


# In calendar_management.py

def select_month_for_action():
    """List available months and prompt the user to select one."""
    months = list_files(config.VISUALIZATIONS_DIR)  # Assuming this function lists directories
    if not months:
        print("No calendars available.")
        return None

    print("Available Calendars:")
    for index, month in enumerate(months, start=1):
        print(f"{index}. {month}")

    try:
        choice = int(input("Select a month: ")) - 1
    except ValueError:
        print("Invalid selection.")
        return None

    if 0 <= choice < len(months):
        return months[choice]
    else:
        print("Selection out of range.")
        return None


def list_files(directory_path, extension=None):
    """
    List all files in the directory, optionally filtering by extension.
    If 'extension' is None, directories are listed instead.
    """
    directory_path = Path(directory_path)  # Ensure directory_path is a Path object
    if extension:
        return [file.name for file in directory_path.glob(f'*{extension}')]
    else:
        # List directories only
        return [d.name for d in directory_path.iterdir() if d.is_dir()]


def select_file(files):
    """
    Prompt the user to select a file from a list of files.
    """
    for index, file in enumerate(files, start=1):
        print(f"{index}. {file}")
    choice = int(input("Select a calendar to view: ")) - 1
    return files[choice]


def view_calendar():
    """
    Allows the user to select a month and automatically opens the calendar for that month.
    Assumes each month directory contains only one .html calendar file.
    Uses the centralized VISUALIZATIONS_DIR path.
    """
    months = list_files(VISUALIZATIONS_DIR)
    if not months:
        print("No calendars available to view.")
        return

    print("Available Calendars:")
    for index, month in enumerate(months, start=1):
        print(f"{index}. {month}")
    choice = int(input("Select a month to view its calendar: ")) - 1

    if 0 <= choice < len(months):
        selected_month = months[choice]
        month_dir = VISUALIZATIONS_DIR / selected_month

        html_files = list_files(month_dir, '.html')
        if html_files:
            selected_file = html_files[0]  # Assuming only one HTML file exists
            file_path = month_dir / selected_file
            display_in_browser(str(file_path))
        else:
            print(f"No calendar available to view for {selected_month}.")
    else:
        print("Invalid selection.")


def edit_calendar(month):
    """
    Placeholder function for editing calendar functionality.
    This function will be developed to allow users to edit calendar events.

    :param month: The month of the calendar to edit, used to select the correct file.
    """
    # Implementation will use VISUALIZATIONS_DIR to locate the specific month's calendar file.
    print(f"Editing functionality for {month} calendar is not yet implemented.")
