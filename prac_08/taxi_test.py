"""
Simulate movement of a taxi
"""
from taxi import Taxi


def main():
    """Simulate movement of a taxi"""
    current_taxi = Taxi("Prius 1", 100)
    current_taxi.drive(40)
    print(current_taxi)
    current_taxi.start_fare()
    current_taxi.drive(100)
    print(current_taxi)


if __name__ == "__main__":
    main()
