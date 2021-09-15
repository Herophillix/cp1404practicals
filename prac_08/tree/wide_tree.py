"""
Represent a wide tree: grows twice as wide as a normal tree
"""
from tree import Tree


class WideTree(Tree):
    """Represent a wide tree: grows twice as wide as a normal tree"""

    def get_ascii_leaves(self):
        """Return a string representation of the tree's leaves."""
        result = ""
        if self._leaves % Tree.TREE_LEAVES_PER_ROW > 0:
            result += "##" * (self._leaves % Tree.TREE_LEAVES_PER_ROW)
            result += "\n"
        for i in range(self._leaves // Tree.TREE_LEAVES_PER_ROW):
            result += "##" * Tree.TREE_LEAVES_PER_ROW
            result += "\n"
        return result

    def get_ascii_trunk(self):
        """Return a string representation of the tree's trunk."""
        result = ""
        for _ in range(self._trunk_height * 2):
            result += "  || \n"
        return result
