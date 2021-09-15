"""
Simulate movement of a silver service taxi
"""
from silver_service_taxi import SilverServiceTaxi


def main():
    """Simulate movement of a silver service taxi"""
    current_taxi = SilverServiceTaxi("Prius 1", 100, 2)
    current_taxi.drive(18)
    print(current_taxi)
    print(current_taxi.get_fare())


if __name__ == "__main__":
    main()
