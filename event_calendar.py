# TODO add a method for removing or editing events
# TODO validate date range when adding events to ensuring the start_date is before the
#  end_date and both are within the month in question
# TODO what happens if an event is already scheduled in a room on a given day

import pandas as pd


# class EventCalendar:
#     def __init__(self, month):
#         self.month = month
#         self.df = self.initialize_calendar()
#
#     def initialize_calendar(self):
#         # Consider dynamically setting the range based on the month
#         dates = range(1, 32)
#         rooms = ['v4', 'v3', 'v2', 'v1']
#         return pd.DataFrame(index=dates, columns=rooms)
#
#         #     def add_event(self, event_name, start_date, end_date, rooms):
#         #         valid_rooms = ['v1', 'v2', 'v3', 'v4']
#         #         if invalid_rooms := set(rooms) - set(valid_rooms):
#         #             raise ValueError(f"Invalid room(s) provided: {', '.join(invalid_rooms)}. Please enter a valid room.")
#         #         for room in rooms:
#         #             for day in range(start_date, end_date + 1):
#         #                 if day in self.df.index:
#         #                     self.df.at[day, room.strip()] = event_name
#         #                 else:
#         #                     print(f"Day {day} is out of range for the month.")
#
#     def add_event(self, event_name, start_date, end_date, rooms):
#         valid_rooms = ['v1', 'v2', 'v3', 'v4']
#
#         if invalid_rooms := set(rooms) - set(valid_rooms):
#             raise ValueError(f"Invalid room(s) provided: {', '.join(invalid_rooms)}. Please enter a valid room.")
#
#         # Validate the date range
#         if start_date > end_date:
#             raise ValueError(f"Start date must be before end date. Got start_date: {start_date}, end_date: {end_date}")
#
#         # Check if the dates are within the month range
#         if not all(date in self.df.index for date in range(start_date, end_date + 1)):
#             raise ValueError(f"Date range must be within the month. Got start_date: {start_date}, end_date: {end_date}")
#
#         for room in rooms:
#             if self.df[room][start_date:end_date + 1].notnull().any():
#                 raise ValueError(f"Room {room} is already booked on one of the days in the given range.")
#
#             for day in range(start_date, end_date + 1):
#                 self.df.at[day, room.strip()] = event_name
#
#         print(f"Event '{event_name}' added from day {start_date} to {end_date} in rooms {', '.join(rooms)}.")

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
        print(f"Attempting to add event '{event_name}' from {start_date} to {end_date} in rooms: {rooms}")

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
            print(f"Adding event to room: {room}")
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

            # Logging the DataFrame state after adding events to each room
            print(f"DataFrame after attempting to add event '{event_name}' to room '{room}':")
            print(self.df)

        print(f"Finished adding event '{event_name}'.")
