"""
Class describing Taxi and its functionality
"""
from car import Car


class Taxi(Car):
    """Class describing Taxi and its functionality"""
    price_per_km = 1.23

    def __init__(self, name: str, fuel=0):
        """Constructor"""
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km
        self.is_fare_started = True
        self.current_fare_distance = 0

    def __str__(self):
        """Description of class"""
        return super().__str__() + ", {0}km on current fare, ${1:.2f}/km".format(
            self.current_fare_distance, self.price_per_km)

    def drive(self, distance):
        """Drive the car a given distance.
        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        distance_travelled = super().drive(distance)
        if self.is_fare_started:
            self.current_fare_distance = distance_travelled
            self.is_fare_started = False
        return distance_travelled

    def get_fare(self):
        """Get the price of the taxi ride"""
        return round(self.price_per_km * self.current_fare_distance, 1)

    def start_fare(self):
        """Start the fare"""
        self.is_fare_started = True
        self.current_fare_distance = 0
