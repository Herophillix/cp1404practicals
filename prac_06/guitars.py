"""
Describe the collection of my guitars
"""
from guitar import Guitar


def get_input_float(prompt):
    """Get user input as float"""
    is_input_valid = False
    user_input = 0
    while not is_input_valid:
        try:
            user_input = float(input(prompt))
            is_input_valid = True
        except ValueError:
            print("Error, please put a valid integer")
    return user_input


def get_input_int(prompt):
    """Get user input as integer"""
    is_input_valid = False
    user_input = 0
    while not is_input_valid:
        try:
            user_input = int(input(prompt))
            is_input_valid = True
        except ValueError:
            print("Error, please put a valid integer")
    return user_input


def main():
    """Describe the collection of my guitars"""
    guitars = []
    is_input_empty = False
    while not is_input_empty:
        name = input("Name: ")
        if name == "":
            is_input_empty = True
        else:
            year = get_input_int("Year: ")
            cost = get_input_float("Cost: $")
            new_guitar = Guitar(name, year, cost)
            guitars.append(new_guitar)
            print("{0} added".format(new_guitar))

    if len(guitars) > 0:
        print("These are my guitars:")
        for i, guitar in enumerate(guitars):
            print("Guitar {0}: {1:<20} ({2}), worth ${3:10,.2f} {4}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                                            "(vintage)" if guitar.is_vintage() else ""))


if __name__ == "__main__":
    main()
