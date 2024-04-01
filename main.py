# TODO: Refactor 'main' to allow switching between sample data and user input.

# TODO: If use_sample_data is False, implement the data input flow.
# - Call 'get_month_input()' to get the month of the event.
# - Call 'get_user_input_without_rooms()' to get the basic event details (name, start date, end date).
# - Call 'get_room_input()' to get the rooms where the event will take place.
# - Construct or update the DataFrame with the provided event details and room assignments.

# TODO: Integrate 'save_calendar.py' to persist event data when not using sample data.
# - After gathering user inputs and updating the DataFrame in 'main',
#   call a function from 'save_calendar.py' to save the event details persistently.
# - Ensure that this saving mechanism is only triggered when 'use_sample_data' is False.
# - Decide on the format and storage method for saving the data (e.g., CSV, JSON, database).
# - Handle potential exceptions or errors during the save operation.
# - Provide feedback to the user that the data has been saved successfully or if an error occurred.

# TODO: Ensure that 'month' variable is set dynamically based on the user input.
# - Do not hardcode the month name; it should reflect the actual event month as entered by the user.

# TODO: Modify 'EventCalendar' class instantiation and DataFrame setting logic.
# - Adjust the EventCalendar class definition to accept and process user inputs as needed.
# - Set the DataFrame within the EventCalendar instance to either the sample data or user-created data.

# TODO: Implement 'display_figure()' in 'visualization.py'. - Ensure it can handle figure display or save the figure
#  file with an appropriate name reflecting the month or other event details.

# TODO: Write unit tests or prepare a manual testing plan to validate the input flow and visualization.
# - Confirm that the application can switch seamlessly between sample data and user input.
# - Test the entire user input flow for errors and correct data handling.
# - Verify that the visualization correctly represents the entered data.

# TODO: Consider edge cases and input validation in 'input.py' functions. - Ensure that user inputs are validated,
#  e.g., dates are within the valid range for the specified month, room names are valid, etc.

# TODO: Update documentation to reflect changes and guide the user through the input process.
# - Document how the user can enter data, what data is expected, and any format they should follow.

# After updating 'main.py' with these TODO comments, you can proceed with implementing each task one by one. This
#  structured approach will help maintain clarity and focus throughout the development process.


from event_calendar import EventCalendar
import visualization
from generate_sample_data import generate_sample_dataframe
from save_calendar import save_calendar_files
from input import get_user_input_without_rooms, get_room_input


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
        print(calendar)

        # Save the calendar data if not using sample data
        save_calendar_files(df, month)

    # Generate and display the calendar visualization
    fig = visualization.create_visualization_figure(df, month)
    visualization.display_figure(fig, month)


if __name__ == "__main__":
    main()
