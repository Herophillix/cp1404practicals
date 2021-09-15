"""
Read a file containing list of guitars and display them
"""
GUITARS_FILE = "guitars.csv"


def main():
    """Read a file containing list of guitars and display them"""
    file = open(GUITARS_FILE, 'r')
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
            guitars.append((name, year, cost))

    for guitar in guitars:
        print("{0} ({1}) : ${2:10,.2f}".format(guitar[0], guitar[1], guitar[2]))


if __name__ == "__main__":
    main()
