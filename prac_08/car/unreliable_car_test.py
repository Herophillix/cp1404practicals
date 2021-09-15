"""
Simulate movement of an unreliable car
"""
from unreliable_car import UnreliableCar


def main():
    """Simulate movement of an unreliable car"""
    current_car = UnreliableCar("Unreliable Car", 100, 50)
    current_car.drive(50)
    print(current_car)


if __name__ == "__main__":
    main()
