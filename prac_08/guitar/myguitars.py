"""
Read a file containing list of guitars and display them
"""
from guitar import Guitar
GUITARS_FILE = "myguitars.csv"


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


def read_file(file_name: str):
    """Read a file and add the guitars into the list"""
    file = open(file_name, 'r')
    lines = file.readlines()
    file.close()

    guitars = []
    for line in lines:
        parts = line.strip().split(',')
        if len(parts) == 3:
            name = parts[0]
            try:
                year = int(parts[1])
            except ValueError:
                year = 0
            try:
                cost = float(parts[2])
            except ValueError:
                cost = 0.0
            guitars.append(Guitar(name, year, cost))
    return guitars


def save_file(file_name: str, guitars: list[Guitar]):
    file = open(file_name, 'w')
    for guitar in guitars:
        file.write("{0},{1},{2}\n".format(guitar.name, guitar.year, guitar.cost))


def main():
    """Read a file containing list of guitars and display them"""
    guitars = read_file(GUITARS_FILE)
    guitars.sort(reverse=True)

    if len(guitars) > 0:
        print("These are my guitars:")
        for i, guitar in enumerate(guitars):
            print(
                "Guitar {0}: {1:<20} ({2}), worth ${3:10,.2f} {4}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                                          "(vintage)" if guitar.is_vintage() else ""))

    is_input_empty = False
    while not is_input_empty:
        print("Add a new guitar(Empty name to quit)")
        name = input("Name: ")
        if name == "":
            is_input_empty = True
        else:
            year = get_input_int("Year: ")
            cost = get_input_float("Cost: $")
            new_guitar = Guitar(name, year, cost)
            guitars.append(new_guitar)
            print("{0} added".format(new_guitar))

    guitars.sort(reverse=True)
    save_file(GUITARS_FILE, guitars)


if __name__ == "__main__":
    main()
