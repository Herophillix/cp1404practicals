"""CP1404/CP5632 Practical - Car class example."""


class Car:
    """Represent a Car object."""
    fuel_usage_multiplier = 1
    fuel_efficiency_multiplier = 1

    def __init__(self, name: str, fuel=0):
        """Initialise a Car instance.
        fuel: float, one unit of fuel drives one kilometre
        """
        self.name = name
        self.fuel = fuel
        self.fuel_usage_multiplier = Car.fuel_usage_multiplier
        self.fuel_efficiency_multiplier = Car.fuel_efficiency_multiplier
        self.odometer = 0

    def __str__(self):
        """Description of class"""
        return "{0}, fuel={1}, odometer={2}".format(self.name, self.fuel, self.odometer)

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance.
        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        fuel_usage = distance * self.fuel_usage_multiplier
        if fuel_usage > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= fuel_usage

        distance_travelled = distance * self.fuel_efficiency_multiplier
        self.odometer += distance_travelled
        return distance_travelled
