def get_month_input():
    """
    Prompt the user to input a month name and validate the input.

    :return: The entered month name if it is valid, otherwise keep prompting the user until a valid month name is entered.

    Example usage:
        month = get_month_input()
    """
    valid_months = ["January", "February", "March", "April", "May", "June",
                    "July", "August", "September", "October", "November", "December"]
    while True:
        month = input("What month is the event (e.g., January)? ").strip().capitalize()
        if month in valid_months:
            return month
        else:
            print(f"Invalid month. Please enter a valid month name.")


def get_user_input_without_rooms():
    """
    This method prompts the user to enter information about an event, including the event name, start date, end date, and month. It then calls the `get_month_input()` function to get the
    * month input from the user. The method returns a tuple containing the event name, start date, end date, and month.

    :return: A tuple containing the event name, start date, end date, and month.
    """
    event_name = input("What's the event name? ")
    start_date = int(input("What's the start date? "))
    end_date = int(input("What's the end date? "))
    month = get_month_input()  # Call the function to get the month input
    return event_name, start_date, end_date, month


def get_room_input(valid_rooms):
    """
    :param valid_rooms: a list of valid room names
    :return: a list of rooms entered by the user
    """
    while True:
        rooms_input = input("What rooms is the event in (comma separated, e.g., v1, v2)? ")
        rooms = [room.strip() for room in rooms_input.split(',')]
        if all(room in valid_rooms for room in rooms):
            return rooms
        else:
            print(f"Invalid room(s). Valid rooms are: {', '.join(valid_rooms)}. Please try again.")
