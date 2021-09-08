"""
Represent an even tree, one that only grows leaves in full rows
"""
from tree import Tree


class EvenTree(Tree):
    """Represent an even tree, one that only grows leaves in full rows"""

    def grow(self, sunlight, water):
        """Grow like a normal tree, but fill out each row of leaves."""
        Tree.grow(self, sunlight, water)
        while self._leaves % 3 != 0:
            self._leaves += 1
