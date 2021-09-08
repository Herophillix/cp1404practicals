"""
CP1404/CP5632 Practical
Testing/example client code for trees classes
When you complete all the subclasses, you'll see that they behave differently.
"""
from tree import Tree
from even_tree import EvenTree
from upside_down_tree import UpsideDownTree
from wide_tree import WideTree
from quick_tree import QuickTree
from fruit_tree import FruitTree
from pine_tree import PineTree


def main():
    """Program to demonstrate trees of different types."""
    # Let's make some trees of different classes (subclasses)
    tree_list = [Tree(), EvenTree(), UpsideDownTree(), WideTree(), QuickTree(), FruitTree(), PineTree()]

    # display all the trees
    for tree in tree_list:
        print(tree.__class__)
        print(tree)

    print("Time to grow!")
    # grow them several times
    for _ in range(5):
        for tree in tree_list:
            tree.grow(5, 2)

    # display all the trees again
    for tree in tree_list:
        print(tree.__class__)
        print(tree)


if __name__ == "__main__":
    main()