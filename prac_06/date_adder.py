"""
Add days into a date
"""
import math
from datetime import date
from my_date import MyDate


def get_input_int(prompt, min_range=-math.inf, max_range=math.inf):
    is_input_valid = False
    user_input = 0

    while not is_input_valid:
        try:
            user_input = int(input(prompt))
            if not min_range <= user_input <= max_range:
                print("Please put in value within range {0} - {1}".format(min_range, max_range))
            else:
                is_input_valid = True
        except ValueError:
            print("Please input a valid integer")

    return user_input


def main():
    """Add days into a date"""
    today = date.today()
    current_date = MyDate(today.day, today.month, today.year)
    current_date = MyDate(1, 1, 2021)

    print("The current date is {0}".format(current_date))
    day = get_input_int("How many days do you want to add?: ", min_range=0)

    while day != 0:
        current_date.add_day(day)
        print("The current date is {0}".format(current_date))
        day = get_input_int("How many days do you want to add?: ", min_range=0)


if __name__ == "__main__":
    main()
