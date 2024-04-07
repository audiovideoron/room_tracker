import os
from display import display_in_browser


def list_files(directory_path, extension=None):
    """
    List all files in the directory, optionally filtering by extension.
    If 'extension' is None, directories are listed instead.
    """
    if extension:
        return [file for file in os.listdir(directory_path) if file.endswith(extension)]
    else:
        # List directories only
        return [d for d in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, d))]


def select_file(files):
    """
    Prompt the user to select a file from a list of files.
    """
    for index, file in enumerate(files, start=1):
        print(f"{index}. {file}")
    choice = int(input("Select a calendar to view: ")) - 1
    return files[choice]


def list_directories(directory_path):
    """
    List all subdirectories in the given directory.
    """
    return [d for d in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, d))]


def view_calendar(directory_path):
    """
    Allows the user to select a month and automatically opens the calendar for that month.
    Assumes each month directory contains only one .html calendar file.
    """
    months = list_directories(directory_path)
    if not months:
        print("No calendars available to view.")
        return

    print("Available Calendars:")
    for index, month in enumerate(months, start=1):
        print(f"{index}. {month}")
    choice = int(input("Select a month to view its calendar: ")) - 1

    selected_month = months[choice]
    month_dir = os.path.join(directory_path, selected_month)

    # Assuming only one .html file per month directory, automatically select it
    html_files = [file for file in os.listdir(month_dir) if file.endswith('.html')]
    if html_files:
        # Automatically select the first (and assumed only) HTML file
        selected_file = html_files[0]
        file_path = os.path.join(month_dir, selected_file)
        display_in_browser(file_path)
    else:
        print(f"No calendar available to view for {selected_month}.")


def edit_calendar(directory_path, month):
    """
    Placeholder function for editing calendar functionality.
    This function is intended to be developed to allow users to edit
    calendar events after viewing a calendar.

    :param directory_path: The path to the directory containing calendar files.
    :param month: The month of the calendar to edit, used to select the correct file.
    """
    # TODO: Implement the functionality to edit calendar events.
    print(f"Editing functionality for {month} calendar is not yet implemented.")
