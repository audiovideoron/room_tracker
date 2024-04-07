from event_calendar import EventCalendar
from save_calendar import save_calendar_files
from input import get_user_input_without_rooms, get_room_input
from calendar_management import view_calendar, edit_calendar
import display

"""
main.py

This is the main execution file for the event calendar application. 
It interacts with the user, accepts inputs for event details, 
updates and displays the event calendar.
"""

# TODO: Minimally Viable Product (MVP) expedite development for minimum viable product
"""
During MVP use the CLI to creating new calendars and events, edit event names, dates, etc.
There's no webserver, or web forms. This is meant to expedite development of
calendar interface and features.

How are edits to existing values performed? Do we directly edit the csv, what's this flow

Rewrite TODOs to be more programmatically instructive
"""

# TODO: MVP:
# - open calendar and display in web browser
# - edit event_name
# - edit start_date, end_date
# - edit room_name,
# - multiple events within one room on the same day
# - flips there are three flip scenarios:
"""
    Flips might be moved into Long Term Roadmap.
    following day flips from first event to second event
        if same room on back-to-back days different events
    same day flip from first event to second event
        if same room & same day different events
    same day same event flip room sets
        if same day & same room and same event
"""


# TODO: date range must span across months

# TODO: Write unit tests to validate the input flow and
# - visualization.
# - Test the entire user input flow for errors and correct data handling
# - dates are within the valid range for the specified month,
# - room names are valid, etc.

def main():
    """
    Main Method

    This method is the entry point of the program.
    It offers an interactive loop for users to add events, view calendars, and edit them.
    After events are added, the calendar is saved and optionally displayed or edited.
    """
    directory_path = '/Users/rtp/PycharmProjects/room_schedule/visualizations'

    while True:
        # Offer choices to the user for different actions
        user_choice = input("Do you want to add a new event or view/edit calendars? (add/view/edit): ").lower()
        if user_choice == "add":
            event_name, start_date, end_date, month = get_user_input_without_rooms()
            rooms = get_room_input(["v1", "v2", "v3", "v4"])

            # Initialize the calendar and update it with new event details
            calendar = EventCalendar(month)
            calendar.add_event(event_name, start_date, end_date, rooms)

            # Save the updated calendar data to both CSV and HTML for persistence and visualization
            html_file_path = save_calendar_files(calendar.df, month, directory_path)
            print("Calendar updated and saved.")
            # Optionally display the updated calendar in the web browser
            display_choice = input("Would you like to view the updated calendar? (yes/no): ").lower()
            if display_choice == "yes":
                display.display_in_browser(html_file_path)
        elif user_choice in ["view", "edit"]:
            # Process for viewing or editing calendars
            month = view_calendar(directory_path)
            if user_choice == "edit" and month:
                # Transition to edit function if 'edit' was selected and a calendar was chosen
                edit_calendar(month, directory_path)
        else:
            print("Invalid option. Please choose 'add' to add a new event or 'view/edit' to manage calendars.")

        # Prompt to continue or exit
        continue_choice = input("Do you want to continue using the program? (yes/no): ").lower()
        if continue_choice != "yes":
            break

    print("Thank you for using the calendar management system.")


if __name__ == "__main__":
    main()
