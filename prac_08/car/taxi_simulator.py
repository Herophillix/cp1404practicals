"""
Simulate movement of a taxi
"""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi
MENU = "q)uit, c)hoose taxi, d)rive"
TAXIS = (Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4))


def print_taxis_available():
    """Print all the taxis that are available"""
    for i, taxi in enumerate(TAXIS):
        print("{0} - {1}".format(i, taxi))


def choose_taxi():
    """Choose a taxi"""
    print_taxis_available()
    try:
        taxi_choice = int(input("Choose taxi: "))
        if 0 <= taxi_choice <= len(TAXIS) - 1:
            return TAXIS[taxi_choice]
        else:
            print("Invalid taxi choice")
    except ValueError:
        print("Invalid taxi choice")
    return None


def drive_taxi(current_taxi):
    """Drive a taxi for a certain amount of distance"""
    if current_taxi is None:
        print("You need to choose a taxi before you can drive")
    else:
        try:
            distance_to_travel = float(input("Drive how far? "))
            if distance_to_travel < 0:
                print("Distance must be > 0")
            else:
                current_taxi.start_fare()
                distance = current_taxi.drive(distance_to_travel)
                fare = current_taxi.get_fare()
                print("Your {0} trip cost you ${1:.2f}".format(current_taxi.name, fare))
                return distance, fare
        except ValueError:
            print("Invalid distance")
    return 0.0, 0.0


def main():
    """Simulate movement of a taxi"""
    is_program_ended = False
    total_distance = 0.0
    total_bill = 0.0
    current_taxi = None

    print("Let's drive!")
    while not is_program_ended:
        print(MENU)
        user_input = input(">>>").lower()
        if user_input == 'q':
            is_program_ended = True
        elif user_input == 'c':
            current_taxi = choose_taxi()
        elif user_input == 'd':
            distance, fare = drive_taxi(current_taxi)
            total_distance += distance
            total_bill += fare
        else:
            print("Invalid option")
        print("Bill to date: ${0:.2f}".format(total_bill))
        print("Total distance travelled: {0} km".format(total_distance))
    print("Taxis are now:")
    print_taxis_available()


if __name__ == "__main__":
    main()
