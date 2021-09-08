"""
Represent a tree that grows more quickly.
"""
from tree import Tree


class QuickTree(Tree):
    """Represent a tree that grows more quickly."""

    def grow(self, sunlight, water):
        """Grow a tree based on the sunlight and water parameters.
        Grow the trunk height by amount of water
        Increase the leaves by amount of sunlight."""
        self._trunk_height += water
        self._leaves += sunlight
