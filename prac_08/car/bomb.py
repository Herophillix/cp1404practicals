"""
Class describing Bomb and its functionality
"""
from car import Car


class Bomb(Car):
    """Class describing Bomb and its functionality"""

    def __init__(self, name: str, fuel=0):
        """Constructor"""
        super().__init__(name, fuel)
        self.fuel_efficiency_multiplier = 0
