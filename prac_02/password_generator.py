import math
import random


MIN_LOWER_ASCII = 97
MAX_LOWER_ASCII = 122
MIN_UPPER_ASCII = 65
MAX_UPPER_ASCII = 90
MIN_DIGIT_ASCII = 48
MAX_DIGIT_ASCII = 57
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def get_user_input(prompt, min_value=-math.inf, max_value=math.inf):
    is_input_valid = False
    return_value = None
    while not is_input_valid:
        try:
            return_value = int(input(prompt))
            while return_value < min_value or return_value > max_value:
                print("Please input a value within the range({0} - {1})".format(min_value, max_value))
                return_value = int(input(prompt))
            is_input_valid = True
        except ValueError:
            print("Please input a valid value")
    return return_value


def create_password(min_length, max_length, lower, upper, digit, special):
    requirements_length = lower + upper + digit + special
    min_length = min_length if min_length > requirements_length else requirements_length
    password_length = random.randint(min_length, max_length)
    leftover_length = password_length - requirements_length
    
    password_requirement = lower * 'L' + upper * 'U' + digit * 'D' + special * 'S' + leftover_length * 'N'
    password_requirement = ''.join(random.sample(password_requirement, len(password_requirement)))
    password = ""

    for requirement in password_requirement:
        if requirement == 'L':
            password += chr(random.randint(MIN_LOWER_ASCII, MAX_LOWER_ASCII))
        elif requirement == 'U':
            password += chr(random.randint(MIN_UPPER_ASCII, MAX_UPPER_ASCII))
        elif requirement == 'D':
            password += chr(random.randint(MIN_DIGIT_ASCII, MAX_DIGIT_ASCII))
        elif requirement == 'S':
            password += random.choice(SPECIAL_CHARACTERS)
        else:
            random_number = random.randint(1, 4)
            if random_number == 1:
                password += chr(random.randint(MIN_LOWER_ASCII, MAX_LOWER_ASCII))
            elif random_number == 2:
                password += chr(random.randint(MIN_UPPER_ASCII, MAX_UPPER_ASCII))
            elif random_number == 3:
                password += chr(random.randint(MIN_DIGIT_ASCII, MAX_DIGIT_ASCII))
            else:
                password += random.choice(SPECIAL_CHARACTERS)
    return password


def main():
    min_length = get_user_input("Input minimum length for password({0} - {1}): ".format(1, 30), min_value=1, max_value=30)
    max_length = get_user_input("Input maximum length for password({0} - {1}): ".format(min_length, 30), min_value=min_length, max_value=30)
    available_length = max_length

    min_lower = get_user_input("Input minimum number of lowercase characters({0} - {1}): ".format(0, available_length), min_value=0, max_value=available_length)
    available_length -= min_lower

    min_upper = get_user_input("Input minimum number of uppercase characters({0} - {1}): ".format(0, available_length), min_value=0, max_value=available_length)
    available_length -= min_upper

    min_digit = get_user_input("Input minimum number of digits ({0} - {1}): ".format(0, available_length), min_value=0, max_value=available_length)
    available_length -= min_digit

    min_special = get_user_input("Input minimum number of special characters({0} - {1}): ".format(0, available_length), min_value=0, max_value=available_length)
    available_length -= min_special

    password = create_password(min_length, max_length, min_lower, min_upper, min_digit, min_special)
    print("Your password is: {0}".format(password))


if __name__ == "__main__":
    main()
