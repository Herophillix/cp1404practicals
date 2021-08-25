"""
Describe a guitar and its features
"""
from datetime import date


class Guitar:
    """Describe a guitar and its features"""

    def __init__(self, name="", year=0, cost=0):
        """Constructor"""
        self.name = name
        current_year = date.today().year
        self.year = year if current_year - year > 0 else current_year
        self.cost = cost if cost > 0 else 0

    def __str__(self):
        """Description of the class"""
        return "{0} ({1}) : ${2:10,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Return the age of the guitar"""
        return date.today().year - self.year

    def is_vintage(self):
        """Check if the guitar is above 50 years old"""
        return self.get_age() > 50
