"""
Dictionary of list of friends with its name and addresses
"""
FRIENDS_DIRECTORY = "friends_list.txt"
OPTION = "1. Add a friend\n2. Remove a friend\n3. Change friend's address\n4. View friend's address\n5. End"


def read_file(friends: dict):
    """Read a file and add it into the dictionary"""
    lines = None
    try:
        file = open(FRIENDS_DIRECTORY, 'r')
        lines = file.readlines()
        file.close()
    except FileNotFoundError:
        return

    for line in lines:
        friend_information = line.split(',', 1)
        if len(friend_information) == 2:
            friends[friend_information[0]] = friend_information[1]


def write_file(friends: dict):
    """Write the dictionary into a file"""
    file = open(FRIENDS_DIRECTORY, 'w')
    for name, address in friends.items():
        file.write("{0},{1}".format(name, address))
    file.close()


def get_user_choice():
    """Get the user choice and return it"""
    print(OPTION)
    is_valid_input = False
    while not is_valid_input:
        try:
            user_choice = int(input("Choice: "))
            return user_choice
        except ValueError:
            print("Invalid input")


def is_dictionary_populated(friends: dict):
    """Check whether a dictionary is populated or not"""
    return len(friends.keys()) > 0


def get_friend_in_dictionary(friends: dict):
    """Get a friend in the dictionary"""
    is_friend = False
    name = ""
    while not is_friend:
        name = input("Name: ")
        if name not in friends:
            print("Friend not found")
        elif name == "":
            print("No name is inputted")
        else:
            is_friend = True
    return name


def add_friend(friends: dict):
    """Add a friend to dictionary"""
    is_new_friend = False
    name = ""
    while not is_new_friend:
        name = input("Name: ")
        if name in friends:
            print("Friend has already been added")
        elif name == "":
            print("No name is inputted")
        else:
            is_new_friend = True

    address = input("Address: ")
    friends[name] = address
    print("{0} added as a friend".format(name))


def remove_friend(friends: dict):
    """Remove a friend"""
    if not is_dictionary_populated(friends):
        print("No friend in dictionary")
        return

    name = get_friend_in_dictionary(friends)

    friends.pop(name)
    print("{0} is no longer your friend".format(name))


def change_address(friends: dict):
    """Change the address of a friend"""
    if not is_dictionary_populated(friends):
        print("No friend in dictionary")
        return

    name = get_friend_in_dictionary(friends)

    address = input("Address: ")
    friends[name] = address
    print("Address of {0} has been changed".format(name))


def view_address(friends: dict):
    """View the address of a friend"""
    if not is_dictionary_populated(friends):
        print("No friend in dictionary")
        return

    name = get_friend_in_dictionary(friends)

    print("Address of {0}: {1}".format(name, friends[name]))


def main():
    """Dictionary of list of friends with its name and addresses"""
    friends = {}
    read_file(friends)
    user_choice = get_user_choice()
    while user_choice != 5:
        if user_choice == 1:
            add_friend(friends)
        elif user_choice == 2:
            remove_friend(friends)
        elif user_choice == 3:
            change_address(friends)
        elif user_choice == 4:
            view_address(friends)
        else:
            print("Invalid input")
        user_choice = get_user_choice()
    else:
        print("Goodbye")
    write_file(friends)


if __name__ == "__main__":
    main()
