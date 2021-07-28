import math

CHOICES = "1)Even Numbers \n2)Odd Numbers \n3)Squares \n4)Quit"


def get_user_choice():
    print(CHOICES)
    return int(input("Input: "))


def print_even_numbers(start, end):
    start = start if start % 2 == 0 else start + 1
    for i in range(start, end + 1, 2):
        print(i, end=' ')
    print()


def print_odd_numbers(start, end):
    start = start if start % 2 != 0 else start + 1
    for i in range(start, end + 1, 2):
        print(i, end=' ')
    print()


def print_square_numbers(start, end):
    start = start if start > 0 else 0
    for i in range(start, end + 1):
        root = math.sqrt(i)
        if root.__ceil__() == root:
            print(i, end=' ')
    print()


def main():
    start_number = int(input("Input starting number: "))
    end_number = int(input("Input ending number: "))
    while end_number < start_number:
        print("Ending number must be greater than " + str(start_number))
        end_number = int(input("Input ending number: "))
    user_choice = get_user_choice()
    while user_choice != 4:
        if user_choice == 1:
            print_even_numbers(start_number, end_number)
        elif user_choice == 2:
            print_odd_numbers(start_number, end_number)
        elif user_choice == 3:
            print_square_numbers(start_number, end_number)
        else:
            print("Invalid input")
        user_choice = get_user_choice()
    else:
        print("Goodbye")


if __name__ == '__main__':
    main()
