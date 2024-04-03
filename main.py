# TODO: expedite development for minimum viable product
# - feasibility of flip logic without database
# - when do we start unit testing?
# - do we refactor for ease of testing?

# TODO: MVP add open_calendar.py

# TODO: MVP add edit_calendar.py

# TODO: date range must span across months
# - how to do this?

# TODO: Write unit tests or prepare a manual testing plan to validate the input flow and
#  visualization.
# - Test the entire user input flow for errors and correct data handling.

# TODO: Long Term Considerations
# - for long term considerations switch to postgresql, multiple users, fastapi

# TODO: redesign application for FastAPI and postgresql
# - Convert format and storage method for saving the data to postgresql.

# TODO: Modify 'EventCalendar' class instantiation and DataFrame setting logic.
# - Adjust the EventCalendar class definition to accept and process user inputs as needed.
# - Set the DataFrame within the EventCalendar instance to either the sample data or user-created data.

# TODO: Consider edge cases and input validation in 'input.py' functions. - Ensure that user inputs are validated,
#  e.g., dates are within the valid range for the specified month, room names are valid, etc.

# TODO: there are three flip scenarios
"""
Flips are opportunities for efficiency and profit. Event labor is sold by total time required
for setup. When two events share the same setup less time is required to flip which
lowers the labor expense. We watch for back-to-back events where the same equipment has
been sold or can be substituted.
"""
# - following day flips from first event to second event
#       if same room on back-to-back days
# - same day flip from first event to second event
#       if same room & same day different events
# - same day same event flip room sets
#       if same day & same room and same event

# TODO: narrow the room column display to accommodate a detail pane
# - click on event and open it in the pane
# - click on shared room date cell and open start end for each event
# - calculate labor requirements

# TODO: auto generate room calendar from sales records
# - use sales form to collect data
# - auto populate calendars from sales records

# TODO: design site customization
# - every hotel has different rooms
# - room_name list based on site_id

from event_calendar import EventCalendar
from save_calendar import save_calendar_files
from input import get_user_input_without_rooms, get_room_input
import save_calendar
import display


def main():
    while True:
        # Real data scenario
        event_name, start_date, end_date, month = get_user_input_without_rooms()
        rooms = get_room_input(["v1", "v2", "v3", "v4"])

        # Initialize the calendar and update it with new event details
        calendar = EventCalendar(month)
        calendar.add_event(event_name, start_date, end_date, rooms)
        df = calendar.df  # Obtain updated DataFrame from the calendar

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
