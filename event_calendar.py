import pandas as pd


class EventCalendar:
    """

    The `EventCalendar` class represents a calendar for managing events in different rooms for a specific month.

    Attributes:
        - month (str): The month for which the calendar is created.
        - df (pandas.DataFrame): The calendar data frame that stores event information.

    Methods:
        - __init__(self, month)
            Initializes the EventCalendar object with the given month and initializes the calendar data frame.

        - initialize_calendar(self)
            Initializes the calendar data frame with dates and rooms.

        - add_event(self, event_name, start_date, end_date, rooms)
            Adds an event to the calendar for the specified date range and rooms.
            This method performs validation checks on the rooms and date range before adding the event to the calendar.

    Example usage:
        calendar = EventCalendar('January')
        calendar.add_event('Conference', 10, 12, ['v1', 'v2', 'v3'])
    """

    def __init__(self, month):
        self.month = month
        self.df = self.initialize_calendar()

    def initialize_calendar(self):
        """
        Initializes the calendar DataFrame with dates (1 to 31) and rooms ('v1', 'v2', 'v3', 'v4').

        Note: This implementation always generates a calendar with 31 days.

        :return: Initialized DataFrame representing the calendar.
        """
        # Dynamically set the range based on the month if needed
        dates = range(1, 32)  # Adjust if needed for months with different day counts
        rooms = ['v4', 'v3', 'v2', 'v1']
        return pd.DataFrame(index=dates, columns=rooms)

    def add_event(self, event_name, start_date, end_date, rooms):
        """
        Adds an event to the calendar for the specified date range and rooms. Before adding the event,
        it checks whether the provided rooms are valid, the start date is before the end date, and the
        room is already booked for the desired dates.

        :param event_name: Name of the event.
        :param start_date: Start day of the event.
        :param end_date: End day of the event.
        :param rooms: List of rooms for the event.

        :raise ValueError: If provided rooms are invalid or if the start date is after the end date.

        :return: None
        """
        # Validate room entries
        valid_rooms = ['v1', 'v2', 'v3', 'v4']
        invalid_rooms = set(rooms) - set(valid_rooms)
        if invalid_rooms:
            raise ValueError(f"Invalid room(s) provided: {', '.join(invalid_rooms)}. Please enter a valid room.")

        # Validate date range
        if start_date > end_date:
            raise ValueError("Start date must be before end date.")

        # Adding event to each room
        for room in rooms:
            for day in range(start_date, end_date + 1):
                if day in self.df.index:
                    if pd.isnull(self.df.at[day, room]):
                        print(f"Adding '{event_name}' to room '{room}' on day {day}")
                        self.df.at[day, room] = event_name
                    else:
                        print(
                            f"Cannot add '{event_name}' to room '{room}' on day {day} as it is already booked with '{self.df.at[day, room]}'")
                else:
                    print(f"Day {day} is out of range for the month of {self.month}. Skipping...")
