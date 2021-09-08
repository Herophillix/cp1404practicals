"""
Represent a tree that has fruit as well as leaves
"""
import random

from tree import Tree


class FruitTree(Tree):
    """Represent a tree that has fruit as well as leaves"""
    TREE_FRUITS_PER_ROW = 3

    def __init__(self):
        """Initialise a Tree with trunk_height of 1 and full row of leaves and a fruit."""
        super().__init__()
        self._fruits = 1

    def __str__(self):
        """Return a string representation of the full Tree"""
        return self.get_ascii_fruits() + super().__str__()

    def get_ascii_fruits(self):
        """Return a string representation of the tree's fruits."""
        result = ""
        if self._fruits % FruitTree.TREE_FRUITS_PER_ROW > 0:
            result += "." * (self._fruits % FruitTree.TREE_FRUITS_PER_ROW)
            result += "\n"
        for i in range(self._fruits // FruitTree.TREE_FRUITS_PER_ROW):
            result += "." * FruitTree.TREE_FRUITS_PER_ROW
            result += "\n"
        return result

    def grow(self, sunlight, water):
        """Grow a tree based on the sunlight and water parameters.
        Randomly increase the fruits by 1 in 2.
        Randomly decrease the fruits by 1 in 5."""
        super().grow(sunlight, water)
        self._fruits += random.randint(0, 1)
        self._fruits -= 1 if random.randint(0, 4) == 0 else 0
