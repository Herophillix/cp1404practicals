"""
Class describing SilverServiceTaxi and its functionality
"""
import math
from taxi import Taxi


def clamp(value: float, min_value: float, max_value: float):
    """Clamp a number within a range"""
    max_value = max_value if min_value < max_value else max_value
    if value < min_value:
        value = min_value
    elif value > max_value:
        value = max_value
    return value


class SilverServiceTaxi(Taxi):
    """Class describing SilverServiceTaxi and its functionality"""
    flagfall = 4.50

    def __init__(self, name: str, fuel=0, fanciness=1):
        """Constructor"""
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * clamp(fanciness, 1, math.inf)

    def __str__(self):
        """Description of the class"""
        return super().__str__() + " plus flagfall of ${0:.2f}".format(SilverServiceTaxi.flagfall)

    def get_fare(self):
        """Get the price of the taxi ride"""
        return super().get_fare() + SilverServiceTaxi.flagfall
