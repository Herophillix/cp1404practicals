LOWER_ASCII = 33
UPPER_ASCII = 127
MIN_COLUMN = 1
MAX_COLUMN = 10


def char_to_ascii():
    character = input("Input a character: ")
    while len(character) > 1:
        print("Please only input 1 character")
        character = input("Input a character: ")
    print("The ASCII code for {0} is {1}".format(character, ord(character)))
    print()


def ascii_to_char():
    is_valid_number = False
    while not is_valid_number:
        try:
            number = int(input("Input a number between {0} and {1}: ".format(LOWER_ASCII, UPPER_ASCII)))
            while number < LOWER_ASCII or number > UPPER_ASCII:
                print("Please enter a number within the range")
                number = int(input("Input a number between {0} and {1}: ".format(LOWER_ASCII, UPPER_ASCII)))
            print("The character for ASCII code {0} is {1}".format(number, chr(number)))
            is_valid_number = True
        except ValueError:
            print("Please enter a valid number")
    print()


def ascii_table(column=1):
    row = (UPPER_ASCII - LOWER_ASCII) // column
    remainder = (UPPER_ASCII - LOWER_ASCII) % column
    code = LOWER_ASCII
    print('=' * (column * len("       |") + 1))
    for i in range(0, row + 1):
        max_range = column if i < row else remainder
        num_of_chars = 0
        for j in range(0, max_range):
            code += 1
            if j == 0:
                to_print = "| {0:>3} {1} |".format(code, chr(code))
            else:
                to_print = " {0:>3} {1} |".format(code, chr(code))
            num_of_chars += len(to_print)
            print(to_print, end="")
        print()
        print('=' * num_of_chars)

    # for i in range(LOWER_ASCII, UPPER_ASCII + 1):
    #     print("{0:>3} {1}".format(i, chr(i)))


def main():
    char_to_ascii()
    ascii_to_char()
    number_of_column = int(input("Input number of columns(1-10): "))
    while number_of_column < MIN_COLUMN or number_of_column > MAX_COLUMN:
        print("Please input the number of columns within the range")
        number_of_column = int(input("Input number of columns(1-10): "))
    ascii_table(number_of_column)


if __name__ == "__main__":
    main()
