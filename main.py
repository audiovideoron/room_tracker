# TODO: Integrate 'save_calendar.py' to persist event data when not using sample data.
# - Ensure that this saving mechanism is only triggered when 'use_sample_data' is False.
# - Decide on the format and storage method for saving the data (e.g., CSV, JSON, database).
# - Handle potential exceptions or errors during the save operation.
# - Provide feedback to the user that the data has been saved successfully or if an error occurred.

# TODO: Modify 'EventCalendar' class instantiation and DataFrame setting logic.
# - Adjust the EventCalendar class definition to accept and process user inputs as needed.
# - Set the DataFrame within the EventCalendar instance to either the sample data or user-created data.

# TODO: Write unit tests or prepare a manual testing plan to validate the input flow and visualization.
# - Confirm that the application can switch seamlessly between sample data and user input.
# - Test the entire user input flow for errors and correct data handling.
# - Verify that the visualization correctly represents the entered data.

# TODO: Consider edge cases and input validation in 'input.py' functions. - Ensure that user inputs are validated,
#  e.g., dates are within the valid range for the specified month, room names are valid, etc.

# TODO: Update documentation to reflect changes and guide the user through the input process.
# - Document how the user can enter data, what data is expected, and any format they should follow.

# TODO: Clean out debug print statements and implement logging

from event_calendar import EventCalendar
import visualization
from generate_sample_data import generate_sample_dataframe
from save_calendar import save_calendar_files
from input import get_user_input_without_rooms, get_room_input
import save_calendar
import display


def main():
    use_sample_data = False  # Toggle based on user input or other logic

    if use_sample_data:
        # Sample data scenario
        df, month = generate_sample_dataframe()
    else:
        # Real data scenario
        event_name, start_date, end_date, month = get_user_input_without_rooms()
        rooms = get_room_input(["v1", "v2", "v3", "v4"])

        # Initialize the calendar and update it with new event details
        calendar = EventCalendar(month)
        calendar.add_event(event_name, start_date, end_date, rooms)
        df = calendar.df  # Obtain updated DataFrame from the calendar

        # Save the calendar data if not using sample data
        save_calendar_files(df, month)

    # Generate and display the calendar visualization
    # fig = visualization.create_visualization_figure(df, month)

    # open newly created and modified calendars
    html_file_path = save_calendar.save_calendar_files(df, month)
    display.display_in_browser(html_file_path)


if __name__ == "__main__":
    main()
