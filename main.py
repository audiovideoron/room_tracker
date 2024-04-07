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
    Users can add events, view, or edit calendars, and choose to quit when done.
    """
    directory_path = '/Users/rtp/PycharmProjects/room_schedule/visualizations'

    while True:
        user_choice = input(
            "Do you want to add a new event, view/edit calendars, or quit? (add/view/edit/quit): ").lower()

        if user_choice == "add":
            event_name, start_date, end_date, month = get_user_input_without_rooms()
            rooms = get_room_input(["v1", "v2", "v3", "v4"])

            calendar = EventCalendar(month)
            calendar.add_event(event_name, start_date, end_date, rooms)

            save_calendar_files(calendar.df, month, directory_path)
            print("Calendar updated and saved.")

            display_choice = input("Would you like to view the updated calendar? (yes/no): ").lower()
            if display_choice == "yes":
                # Assuming display_in_browser function takes the full path to the HTML file
                html_file_path = f"{directory_path}/{month}_calendar/{month}_calendar.html"
                display.display_in_browser(html_file_path)

        elif user_choice in ["view", "edit"]:
            month = view_calendar(directory_path)
            if user_choice == "edit" and month:
                edit_calendar(month, directory_path)

        elif user_choice == "quit":
            print("Thank you for using the calendar management system.")
            break

        else:
            print("Invalid option. Please choose 'add', 'view', 'edit', or 'quit'.")


if __name__ == "__main__":
    main()
