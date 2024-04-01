import pandas as pd

#
"""
# class EventCalendar:
#     def __init__(self, month):
#         self.month = month
#         self.df = self.initialize_calendar()
#
#     def initialize_calendar(self):
#         dates = range(1, 33)  # Adjust this if the range should be 1 to 31
#         rooms = ['v4', 'v3', 'v2', 'v1']
#         df = pd.DataFrame(index=dates, columns=rooms)
#         return df
#
#     def add_event(self, event_name, start_date, end_date, rooms):
#         valid_rooms = ['v1', 'v2', 'v3', 'v4']
#         invalid_rooms = set(rooms) - set(valid_rooms)
#         if invalid_rooms:
#             raise ValueError(f"Invalid room(s) provided: {', '.join(invalid_rooms)}. Please enter a valid room.")
#         for room in rooms:
#             for day in range(start_date, end_date + 1):
#                 self.df.at[day, room.strip()] = event_name
#                 print(f"Added event '{event_name}' to room '{room.strip()}' for day {day}")
#                 print("Current DataFrame:")
#                 print(self.df)
#             for day in range(start_date, end_date + 1):
#                 # This checks if the day is within the DataFrame's index range
#                 if day in self.df.index:
#                     self.df.at[day, room.strip()] = event_name
#                 else:
#                     print(f"Day {day} is out of range for the month.")
#
#     def update_calendar_dataframe(self, event_name, start_date, end_date, rooms):
#         for room in rooms:
#             for day in range(start_date, end_date + 1):
#                 self.df.at[day, room] = event_name
#
#
# def load_calendar(self, file_path):
#     # file_path is received as parameter, no need to redefine it
#     try:
#         self.df = pd.read_csv(file_path, index_col=0)
#     except FileNotFoundError:
#         print(f'File {file_path} not found.')
#     else:
#         print(f"Loading event calendar from {file_path}")
#
#     def save_calendar(self, file_path):
#         self.df.to_csv(file_path)
"""


class EventCalendar:
    def __init__(self, month):
        self.month = month
        self.df = self.initialize_calendar()

    def initialize_calendar(self):
        # Consider dynamically setting the range based on the month
        dates = range(1, 32)
        rooms = ['v4', 'v3', 'v2', 'v1']
        return pd.DataFrame(index=dates, columns=rooms)

    def add_event(self, event_name, start_date, end_date, rooms):
        valid_rooms = ['v1', 'v2', 'v3', 'v4']
        if invalid_rooms := set(rooms) - set(valid_rooms):
            raise ValueError(f"Invalid room(s) provided: {', '.join(invalid_rooms)}. Please enter a valid room.")
        for room in rooms:
            for day in range(start_date, end_date + 1):
                if day in self.df.index:
                    self.df.at[day, room.strip()] = event_name
                else:
                    print(f"Day {day} is out of range for the month.")

    def load_calendar(self, file_path):
        try:
            self.df = pd.read_csv(file_path, index_col=0)
            print(f"Loading event calendar from {file_path}")
        except FileNotFoundError:
            print(f'File {file_path} not found.')

    def save_calendar(self, file_path):
        self.df.to_csv(file_path)
        print(f"Calendar saved to {file_path}")
