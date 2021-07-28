"""
Check user password to be a minimum length
"""
MIN_PASSWORD_LENGTH = 8


def get_password():
    """Check if the password is greater than the MIN_PASSWORD_LENGTH"""
    user_input = input("Input a password: ")
    while len(user_input) < MIN_PASSWORD_LENGTH:
        print("Please input a password greater than {0} characters".format(MIN_PASSWORD_LENGTH))
        user_input = input("Input a password: ")
    return user_input


def main():
    """Get a valid user password and print it in * form"""
    password = get_password()
    print("Your password is: {0}".format('*' * len(password)))


if __name__ == "__main__":
    main()

