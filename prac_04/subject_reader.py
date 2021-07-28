"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data_list = get_data_list()
    print_data(data_list)


def print_data(data_list):
    for data in data_list:
        print("{0:<6} is taught by {1:<15} and has {2:<3} students".format(data[0], data[1], data[2]))


def get_data_list():
    """Read data from file formatted like: subject,lecturer,number of students."""
    return_value = []

    input_file = open(FILENAME)
    line_list = input_file.readlines()
    input_file.close()

    for line in line_list:
        line = line.strip()  # Remove the \n
        part_list = line.split(',')  # Separate the data into its parts
        for i in range(len(part_list)):
            if part_list[i].isdigit():
                part_list[i] = int(part_list[i])
        return_value.append(part_list)
    return return_value


if __name__ == "__main__":
    main()
