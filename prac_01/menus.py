CHOICES = "(H)ello \n(G)oodbye \n(Q)uit"


def get_user_choice():
    print(CHOICES)
    return input(">>>").upper()


def main():
    name = input("Enter your name: ")
    user_choice = get_user_choice()
    while user_choice != 'Q':
        if user_choice == 'H':
            print("Hello " + name)
        elif user_choice == 'G':
            print("Goodbye " + name)
        else:
            print("Invalid input")
        user_choice = get_user_choice()
    else:
        print("End")


if __name__ == '__main__':
    main()
