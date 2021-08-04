"""
Ask user for a number of lines and generates random numbers in each line
"""
import random
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


def generate_random_numbers(count_of_number, min_value, max_value):
    # ensure that range of random numbers is within count, to prevent repeated numbers
    difference = max_value - min_value
    if difference < count_of_number:
        max_value += count_of_number - difference

    random_numbers = []
    for i in range(count_of_number):
        number = random.randint(min_value, max_value)
        while number in random_numbers:
            number = random.randint(min_value, max_value)
        random_numbers.append(number)
    return random_numbers


def print_quick_pick(count):
    for i in range(count):
        random_numbers = generate_random_numbers(6, 1, 45)
        random_numbers.sort()
        for number in random_numbers:
            print(number, end=' ')
        print()


def main():
    """Ask user for a number of lines and generates random numbers in each line"""
    quick_pick_number = get_input_int("Number of quick pick: ", min_value=1)
    print_quick_pick(quick_pick_number)


if __name__ == "__main__":
    main()
