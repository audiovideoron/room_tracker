# TODO add a method for removing or editing events
# TODO validate date range when adding events to ensure the start_date is before the
#  end_date, events can span across months
# TODO what happens if an event is already scheduled in a room on a given day, see flips
# TODO: in event spans only use event_name in beginning cell

import pandas as pd


class EventCalendar:
    def __init__(self, month):
        self.month = month
        self.df = self.initialize_calendar()

    def initialize_calendar(self):
        # Dynamically set the range based on the month if needed
        dates = range(1, 32)  # Adjust if needed for months with different day counts
        rooms = ['v4', 'v3', 'v2', 'v1']
        return pd.DataFrame(index=dates, columns=rooms)

    def add_event(self, event_name, start_date, end_date, rooms):

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
