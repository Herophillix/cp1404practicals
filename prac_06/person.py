"""
Describe a person
"""


class Person:
    """Describe a person"""

    def __init__(self, first_name: str, last_name: str, age: int):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age if age > 0 else 0
