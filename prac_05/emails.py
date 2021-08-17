"""
Dictionary of emails and their names
"""


def main():
    """Ask user for an email, and confirm their names"""
    emails = {}
    email = input("Email: ")
    while email != "":
        if email.count('@') == 1:
            email_components = email.split('@')

            name_component = email_components[0].replace('_', '.')
            split_names = name_component.split('.')
            possible_name = ""

            for name in split_names:
                possible_name += name.title() + ' '
            possible_name = possible_name[:-1]

            is_name_correct = False
            user_name = ""
            check_name = input("Is your name {0}?(y/n): ".format(possible_name))

            while not is_name_correct:
                if check_name == "" or check_name.lower() == 'y':
                    user_name = possible_name
                    is_name_correct = True
                elif check_name.lower() == 'n':
                    user_name = input("Name: ")
                    is_name_correct = True
                else:
                    print("Invalid input")
                    check_name = input("Is your name {0}?(y/n): ")

            emails[email] = user_name
            email = input("Email: ")
        else:
            print("Invalid email format")
            email = input("Email: ")
    else:
        for key, value in emails.items():
            print("{0}({1})".format(value, key))


if __name__ == "__main__":
    main()
