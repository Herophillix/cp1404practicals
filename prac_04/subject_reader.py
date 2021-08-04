"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Get a data from a text file and print it"""
    datas = get_datas()
    print_data(datas)


def print_data(datas):
    """Print the information from a list of data"""
    for data in datas:
        print("{0:<6} is taught by {1:<15} and has {2:<3} students".format(data[0], data[1], data[2]))


def get_datas():
    """Read data from file formatted like: subject,lecturer,number of students."""
    datas = []

    input_file = open(FILENAME)
    lines = input_file.readlines()
    input_file.close()

    for line in lines:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        for i in range(len(parts)):
            if parts[i].isdigit():
                parts[i] = int(parts[i])
        datas.append(parts)
    return datas


if __name__ == "__main__":
    main()
