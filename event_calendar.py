import pandas as pd


class EventCalendar:
    def __init__(self, month):
        self.month = month
        self.df = self.initialize_calendar()

    def initialize_calendar(self):
        dates = range(1, 33)
        rooms = ['v4', 'v3', 'v2', 'v1']
        df = pd.DataFrame(index=dates, columns=rooms)
        return df

    def add_event(self, event_name, start_date, end_date, rooms):
        # List of valid rooms
        valid_rooms = ['v1', 'v2', 'v3', 'v4']

        # Check if any of the provided rooms are invalid
        invalid_rooms = set(rooms) - set(valid_rooms)
        if invalid_rooms:
            raise ValueError(f"Invalid room(s) provided: {', '.join(invalid_rooms)}. Please enter a valid room.")

        # Proceed with adding the event if all rooms are valid
        for date in range(start_date, end_date + 1):
            for room in rooms:
                self.df.at[date, room.strip()] = event_name

    def load_calendar(self, file_path):
        self.df = pd.read_csv(file_path, index_col=0)

    def save_calendar(self, file_path):
        self.df.to_csv(file_path)
