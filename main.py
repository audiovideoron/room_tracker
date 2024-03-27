from event_calendar import EventCalendar
import visualization
import os


def get_user_input():
    print("Enter the details for the new event.")
    event_name = input("Event name: ")
    start_date = int(input("Start date (1-32): "))
    end_date = int(input("End date (1-32): "))
    rooms = input("Rooms (comma separated, e.g., v1, v2): ").split(',')
    month = input("Month of the event: ")
    return event_name, start_date, end_date, rooms, month


def main():
    event_name, start_date, end_date, rooms, month = get_user_input()
    file_path = f"{month}_calendar.csv"

    # Initialize or load existing calendar
    calendar = EventCalendar(month)
    if os.path.exists(file_path):
        calendar.load_calendar(file_path)

    calendar.add_event(event_name, start_date, end_date, [room.strip() for room in rooms])
    calendar.save_calendar(file_path)

    visualization.visualize_calendar(calendar.df)


if __name__ == "__main__":
    main()
