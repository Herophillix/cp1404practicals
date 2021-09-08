"""
Class describing GasGussler and its functionality
"""
from car import Car


class GasGussler(Car):
    """Class describing GasGussler and its functionality"""

    def __init__(self, name: str, fuel=0):
        """Constructor"""
        super().__init__(name, fuel)
        self.fuel_usage_multiplier = 2
