"""
Simulate movement of car
"""
import math

from car import Car

MENU = "Menu:\nd) Drive\nr) Refuel\nq) Quit"


def get_input(prompt, valid_input=(), capitalize=False):
    is_input_valid = False
    user_input = ""

    while not is_input_valid:
        user_input = input(prompt)
        if user_input == "":
            print("Input cannot be empty")
        else:
            if capitalize:
                user_input = user_input.upper()
            if len(valid_input) > 0:
                if user_input not in valid_input:
                    print("Invalid input")
                else:
                    is_input_valid = True
            else:
                is_input_valid = True

    return user_input


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


def drive(current_car):
    if current_car.fuel == 0:
        print("You have no fuel left in your car!")
        return

    distance = get_input_int("How many km do you wish to drive?: ", min_range=0)
    actual_distance = current_car.drive(distance)
    print("The car drove for {0} km{1}".format(actual_distance,
                                               " and ran out of fuel." if current_car.fuel == 0 else "."))


def refuel(current_car):
    fuel = get_input_int("How many units of fuel do you want to add to the car?: ", min_range=0)
    current_car.add_fuel(fuel)
    print("Added {0} units of fuel".format(fuel))


def main():
    """Simulate movement of car"""
    print("Let's drive!")
    name = get_input("Name of car: ")
    current_car = Car(name, 100)

    is_program_running = True
    while is_program_running:
        print("Your current car is {0}".format(current_car))
        print(MENU)
        user_input = get_input("Input: ", valid_input=('D', 'R', 'Q'), capitalize=True)
        if user_input == 'D':
            drive(current_car)
        elif user_input == 'R':
            refuel(current_car)
        elif user_input == 'Q':
            is_program_running = False
            print("Good bye {0}'s driver".format(current_car.name))


if __name__ == "__main__":
    main()
