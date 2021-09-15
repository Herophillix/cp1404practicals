"""
Represent a pine tree
"""
import random
from tree import Tree


class PineTree(Tree):
    """Represent a pine tree"""

    def __init__(self):
        super().__init__()
        self.row_leaves = 2

    def get_ascii_leaves(self):
        """Return a string representation of the tree's leaves."""
        result = ""
        leaves_per_row = 1
        for i in range(self.row_leaves):
            result += " " * (self.row_leaves - i - 1) + "#" * leaves_per_row
            result += '\n'
            leaves_per_row += 2
        return result

    def get_ascii_trunk(self):
        """Return a string representation of the tree's trunk."""
        result = ""
        # the _ (underscore) variable is a convention for an unused variable
        for _ in range(self._trunk_height):
            result += " " * (self.row_leaves - 1) + "| \n"
        return result

    def grow(self, sunlight, water):
        """Grow a tree based on the sunlight and water parameters.
        Randomly grow the trunk height by a number between 0 and water.
        Randomly increase the row of leaves if a random number between 0 and sunlight is greater than 2"""
        self._trunk_height += random.randint(0, water)
        self.row_leaves += 1 if random.randint(0, sunlight) > 2 else 0

