from input import get_user_input_without_rooms, get_room_input
from event_calendar import EventCalendar
import visualization
import os


def main():
    valid_rooms = ["v1", "v2", "v3", "v4"]

    while True:
        event_name, start_date, end_date, month = get_user_input_without_rooms()
        rooms = get_room_input(valid_rooms)
        file_path = f"{month}_calendar.csv"

        # Initialize or load existing calendar
        calendar = EventCalendar(month)
        if os.path.exists(file_path):
            calendar.load_calendar(file_path)

        try:
            calendar.add_event(event_name, start_date, end_date, rooms)
        except ValueError as e:
            print(e)
            continue  # Go back to the start of the loop if there was an error
        else:
            calendar.save_calendar(file_path)
            visualization.visualize_calendar(calendar.df, month)

        # Ask the user if they want to add another event
        another = input("Would you like to add another event? (yes or no) ").strip().lower()
        if another != 'yes':
            break  # Exit the loop if the user does not want to add another event


if __name__ == "__main__":
    main()
