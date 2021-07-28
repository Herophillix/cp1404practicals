"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"
MIN_LENGTH = 2
MAX_LENGTH = 6
MIN_LOWERCASE_COUNT = 1
MIN_UPPERCASE_COUNT = 1
MIN_DIGIT_COUNT = 1
MIN_SPECIAL_COUNT = 1


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t{0} or more lowercase characters".format(MIN_LOWERCASE_COUNT))
    print("\t{0} or more uppercase characters".format(MIN_UPPERCASE_COUNT))
    print("\t{0} or more numbers".format(MIN_DIGIT_COUNT))
    if SPECIAL_CHARS_REQUIRED:
        print("\t{0} or more special characters:".format(MIN_SPECIAL_COUNT), SPECIAL_CHARACTERS)
    password = input("> ")
    is_password_valid, error_message = check_password_validity(password)
    while not is_password_valid:
        print("Invalid password!")
        print(error_message, end="")
        password = input("> ")
        is_password_valid, error_message = check_password_validity(password)
    print("Your {}-character password is valid: {}".format(len(password),
                                                           password))


def check_password_validity(password):
    """Determine if the provided password is valid."""
    invalid_message = ""
    # TODO: if length is wrong, return False
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        invalid_message = "Password length must be in between {0} and {1} characters!\n".format(MIN_LENGTH, MAX_LENGTH)
        return False, invalid_message

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        # TODO: count each kind of character (use str methods like isdigit)
        if char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif char.isdigit():
            count_digit += 1
        elif char in SPECIAL_CHARACTERS:
            count_special += 1
        pass

    is_valid = True

    # TODO: if any of the 'normal' counts are zero, return False
    if count_lower < MIN_LOWERCASE_COUNT:
        invalid_message += "Lowercase characters must be greater than or equals to {0} characters!\n".format(MIN_LOWERCASE_COUNT)
        is_valid = False
    if count_upper < MIN_UPPERCASE_COUNT:
        invalid_message += "Uppercase characters must be greater than or equals to {0} characters!\n".format(MIN_UPPERCASE_COUNT)
        is_valid = False
    if count_digit < MIN_DIGIT_COUNT:
        invalid_message += "Digits must be greater than or equals to {0} characters!\n".format(MIN_DIGIT_COUNT)
        is_valid = False

    # TODO: if special characters are required, then check the count of those
    # and return False if it's zero
    if SPECIAL_CHARS_REQUIRED and count_special < MIN_SPECIAL_COUNT:
        invalid_message += "Special characters must be greater than or equals to {0} characters!\n".format(MIN_SPECIAL_COUNT)
        is_valid = False

    # if we get here (without returning False), then the password must be valid
    return is_valid, invalid_message


if __name__ == "__main__":
    main()
