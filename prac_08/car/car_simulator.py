"""
Simulate movement of different cars
"""
from car import Car
from taxi import  Taxi
from silver_service_taxi import SilverServiceTaxi
from eco_taxi import EcoTaxi
from gas_gussler import GasGussler
from bomb import Bomb
MENU = "q)uit, c)hoose car, d)rive, r)efuel"
CARS = (Car("Car", 100), Taxi("Taxi", 100), SilverServiceTaxi("Silver Taxi", 100, 2), EcoTaxi("Eco Taxi", 100),
        GasGussler("Gas Gussler", 100), Bomb("Bomb", 100))


def print_cars():
    for i, car in enumerate(CARS):
        print("{0} - {1}".format(i, car))


def choose_car():
    """Choose a car"""
    print("Cars available:")
    print_cars()

    is_car_chosen = False
    while not is_car_chosen:
        try:
            car_choice = int(input("Choose car: "))
            if 0 <= car_choice <= len(CARS) - 1:
                return CARS[car_choice]
            else:
                print("Invalid car choice")
        except ValueError:
            print("Invalid car choice")


def drive_car(current_car: Car):
    """Drive a car for a certain amount of distance"""
    if current_car is None:
        print("You need to choose a car before you can drive")
    else:
        is_car_driven = False
        while not is_car_driven:
            try:
                distance = float(input("Drive how far? "))
                if distance < 0:
                    print("Distance must be > 0")
                else:
                    if isinstance(current_car, Taxi):
                        current_car.start_fare()
                    distance_travelled = current_car.drive(distance)
                    print("{0} has travelled for {1}km".format(current_car.name, distance_travelled))
                    is_car_driven = True
            except ValueError:
                print("Invalid distance")


def refuel_car(current_car: Car):
    """Refuel a car"""
    if current_car is None:
        print("You need to choose a car before you can drive")
    else:
        is_car_refuelled = False
        while not is_car_refuelled:
            try:
                fuel = float(input("How much to refuel? "))
                if fuel < 0:
                    print("Fuel must be > 0")
                else:
                    current_car.add_fuel(fuel)
                    is_car_refuelled = True
            except ValueError:
                print("Invalid fuel")


def main():
    """Simulate movement of different cars"""
    is_program_ended = False
    current_car = None

    print("Let's drive!")
    while not is_program_ended:
        print(MENU)
        user_input = input(">>>").lower()
        if user_input == 'q':
            is_program_ended = True
        elif user_input == 'c':
            current_car = choose_car()
        elif user_input == 'd':
            drive_car(current_car)
        elif user_input == 'r':
            refuel_car(current_car)
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
