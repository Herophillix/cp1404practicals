"""
Check for repeated strings in a list
"""


def get_repeated_strings():
    """Ask user to input strings and check for repeated strings"""
    strings = []
    repeated_strings = []
    is_empty = False
    while not is_empty:
        string = input("Input a string(Empty to end): ")
        if string:
            if string in strings and string not in repeated_strings:
                repeated_strings.append(string)
            strings.append(string)
        else:
            is_empty = True
    return repeated_strings


def print_repeated_strings(repeated_strings):
    """Print repeated strings"""
    if len(repeated_strings) == 0:
        print("No strings are repeated")
    else:
        print("Strings repeated: ", end='')
        for string in repeated_strings:
            if string is repeated_strings[-1]:
                print(string)
            else:
                print("{0}, ".format(string), end='')


def main():
    """Print the repeated strings in what the user has inputted"""
    repeated_strings = get_repeated_strings()
    print_repeated_strings(repeated_strings)


if __name__ == "__main__":
    main()
