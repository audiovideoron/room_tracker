from event_calendar import EventCalendar
from save_calendar import save_calendar_files
from input import get_user_input_without_rooms, get_room_input
import save_calendar
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
    It provides an interactive loop for users to input event details such
    as event name, start date, end date and the rooms in which the events
    are to be held.
    These details are then used to update an event calendar.
    The updated calendar is saved using the save_calendar_files method
    from the save_calendar module and then displayed in the web browser.

    :return: None
    """

    while True:
        # Real data scenario
        event_name, start_date, end_date, month = get_user_input_without_rooms()
        rooms = get_room_input(["v1", "v2", "v3", "v4"])

        # Initialize the calendar and update it with new event details
        calendar = EventCalendar(month)
        calendar.add_event(event_name, start_date, end_date, rooms)
        # Get a reference to the calendar's DataFrame, which contains the updated
        # event and room details, to be written to the file system in the following steps.
        df = calendar.df

        # Ask the user if they want to add another event
        add_another = input("Would you like to add another event? (Yes/No) ")
        if add_another.lower() != "yes":
            break

    # Save the calendar data if not using sample data
    save_calendar_files(df, month)

    # open newly created and modified calendars
    html_file_path = save_calendar.save_calendar_files(df, month)
    display.display_in_browser(html_file_path)


if __name__ == "__main__":
    main()
