NAME_FILE_DIRECTORY = "names.txt"
NUMBER_FILE_DIRECTORY = "numbers.txt"


def write_name():
    name_to_add = input("Input your name: ")
    file = open(NAME_FILE_DIRECTORY, 'a')
    file.write("{}\n".format(name_to_add))
    file.close()

    print()


def read_name():
    file = open(NAME_FILE_DIRECTORY, 'r')
    for name in file:
        print("Your name is {0}".format(name.strip()))
    file.close()

    print()


def read_number(number_of_lines=0):
    file = open(NUMBER_FILE_DIRECTORY, 'r')
    number_list = file.readlines()
    file.close()

    count = len(number_list)
    if number_of_lines > 0:
        # Ensure that the number of lines read is <= the count of lines in the file
        count = count if count < number_of_lines else number_of_lines
    sum_of_numbers = 0
    valid_number_count = 0

    for i in range(0, count):
        number = number_list[i]
        try:
            sum_of_numbers += int(number)
            valid_number_count += 1
        except ValueError:
            print("Error, line {0} of {1} is not a valid integer({2})".format(i, NUMBER_FILE_DIRECTORY, number.strip("\n")))

    print("Sum of {0} numbers in {1} is {2}".format(valid_number_count, NUMBER_FILE_DIRECTORY, sum_of_numbers), "\n")


def main():
    write_name()
    read_name()
    read_number(2)
    read_number()


if __name__ == "__main__":
    main()
