"""
Test the functionality of guitar
"""
from guitar import Guitar


def main():
    """Test the functionality of guitar"""
    gibson = Guitar("Gibson L-5", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2014, 20)
    print("Gibson L-5 get_age() - Expected 99. Got {0}".format(gibson.get_age()))
    print("Another Guitar get_age() - Expected 7. Got {0}".format(another_guitar.get_age()))
    print("Gibson L-5 is_vintage() - Expected True. Got {0}".format(gibson.is_vintage()))
    print("Another Guitar is_vintage() - Expected False. Got {0}".format(another_guitar.is_vintage()))


if __name__ == "__main__":
    main()
