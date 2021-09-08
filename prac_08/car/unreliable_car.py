"""
Class describing UnreliableCar and its functionality
"""
import random

from car import Car


def clamp(value: float, min_value: float, max_value: float):
    """Clamp a number within a range"""
    max_value = max_value if min_value < max_value else max_value
    if value < min_value:
        value = min_value
    elif value > max_value:
        value = max_value
    return value


class UnreliableCar(Car):
    """Class describing UnreliableCar and its functionality"""

    def __init__(self, name: str, fuel=0, reliability=100):
        """Constructor"""
        super().__init__(name, fuel)
        self.reliability = clamp(reliability, 0, 100)

    def __str__(self):
        """Description of class"""
        return super().__str__() + ", reliability={0}".format(self.reliability)

    def drive(self, distance):
        """Drive the car a given distance.
        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        if self.reliability < random.randint(0, 100):
            super().drive(distance)
        else:
            return 0
