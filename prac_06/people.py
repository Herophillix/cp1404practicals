"""
Describe many people in a table
"""
import math
from person import Person
from table import *


def get_input(prompt):
    """Get user input as raw value"""
    user_input = input(prompt)
    while user_input == "":
        print("Input cannot be empty")
        user_input = input(prompt)
    return user_input


def get_input_int(prompt, min_range=-math.inf, max_range=math.inf):
    """Get user input as integer"""
    is_input_valid = False
    user_input = 0

    while not is_input_valid:
        try:
            user_input = int(input(prompt))
            if not min_range <= user_input <= max_range:
                print("Please put in value within range {0} - {1}".format(min_range, max_range))
            else:
                is_input_valid = True
        except ValueError:
            print("Please input a valid integer")

    return user_input


def print_people_table(people: [Person]):
    """Print the list of people in a table"""
    table = Table()
    header_rows = [Cell("First Name"), Cell("Last Name"), Cell("Age")]
    table.add_row(header_rows)
    table.add_buffer()

    for person in people:
        row = [Cell(person.first_name), Cell(person.last_name), Cell(str(person.age), '>')]
        table.add_row(row)
        table.add_buffer()

    table.print_table()


def main():
    """Describe many people in a table"""
    num_of_times = get_input_int("Number of people: ")
    while num_of_times <= 0:
        print("Please input a value > 0")
        num_of_times = get_input_int("Number of people: ")

    people = []

    for i in range(num_of_times):
        print("Person {0}".format(i + 1))
        first_name = get_input("First Name: ")
        last_name = get_input("Last Name: ")
        age = get_input_int("Age: ", min_range=0)
        new_person = Person(first_name, last_name, age)
        people.append(new_person)

    people.sort(key=lambda person: person.age)
    print_people_table(people)


if __name__ == "__main__":
    main()
