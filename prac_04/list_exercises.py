"""
Add numbers to a list and analyze the list
"""
import math


def get_input_int(prompt, min_value=-math.inf, max_value=math.inf):
    """Get an integer from input"""
    is_valid_input = False
    input_value = None
    while not is_valid_input:
        try:
            input_value = int(input(prompt))
            while input_value < min_value or input_value > max_value:
                if min_value == -math.inf:
                    print("Error, please input an integer lesser than {0}".format(max_value))
                elif max_value == math.inf:
                    print("Error, please input an integer greater than {0}".format(min_value))
                else:
                    print("Error, please put an integer within {0} and {1}".format(min_value, max_value))
                input_value = int(input(prompt))
            is_valid_input = True
        except ValueError:
            print("Error, please input a valid integer")
    return input_value


def populate_list(count):
    """Populate a list by asking user to input numbers in it"""
    number_list = []
    for i in range(count):
        number = get_input_int("Input number: ")
        number_list.append(number)
    return number_list


def populate_list_indefinite():
    """Populate a list by asking user to input numbers in it"""
    number_list = []
    index = 0
    is_negative_in_list = False
    while not is_negative_in_list:
        number = get_input_int("Input number {0}: ".format(index + 1))
        if number < 0:
            is_negative_in_list = True
        else:
            number_list.append(number)
            index += 1
    return number_list


def analyze_list(numbers):
    """Analyze the given list"""
    if len(numbers) == 0:
        print("List is not populated")
        print()
        return

    first_value = last_value = min_value = max_value = average_value = 0
    first_value = numbers[0]
    last_value = numbers[-1]
    min_value = min(numbers)
    max_value = max(numbers)
    average_value = sum(numbers) / len(numbers)
    print("First value: {0}".format(first_value))
    print("Last value: {0}".format(last_value))
    print("Min value: {0}".format(min_value))
    print("Max value: {0}".format(max_value))
    print("Average: {0}".format(average_value))
    print()


def check_username(usernames):
    username = input("Input username: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


def main():
    """Analyze list and check for usernames"""
    list_count = get_input_int("Input count of list: ", min_value=1)
    analyze_list(populate_list(list_count))

    print("Indefinite")
    analyze_list(populate_list_indefinite())

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    check_username(usernames)


if __name__ == "__main__":
    main()
