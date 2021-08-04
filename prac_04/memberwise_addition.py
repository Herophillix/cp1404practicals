"""
Add numbers in a list by the members
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


def get_numbers(list_index):
    """Generate a number list and return it"""
    numbers = []
    count = get_input_int("Input count of numbers for list {0}: ".format(list_index), min_value=1)
    for i in range(count):
        number = get_input_int("Input a Number {0} for list {1}: ".format(i + 1, list_index))
        numbers.append(number)
    return numbers


def add_memberwise(numbers_1, numbers_2):
    new_numbers = []
    smaller_numbers = numbers_1 if len(numbers_1) < len(numbers_2) else numbers_2
    larger_numbers = numbers_1 if smaller_numbers is numbers_2 else numbers_2
    new_numbers = larger_numbers.copy()
    for i in range(len(smaller_numbers)):
        new_numbers[i] += smaller_numbers[i]
    return new_numbers


def main():
    """Ask user to input two list of numbers, and add them member wise"""
    numbers_1 = get_numbers(1)
    numbers_2 = get_numbers(2)
    numbers_sum = add_memberwise(numbers_1, numbers_2)
    print(numbers_sum)


if __name__ == "__main__":
    main()
