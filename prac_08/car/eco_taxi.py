"""
Class describing EcoTaxi and its functionality
"""
import math
from taxi import Taxi


class EcoTaxi(Taxi):
    """Class describing EcoTaxi and its functionality"""

    def __init__(self, name: str, fuel=0):
        """Constructor"""
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * 0.5
        self.fuel_usage_multiplier = 0.5
