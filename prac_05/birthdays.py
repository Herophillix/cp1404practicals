"""
Dictionary to display user name and age
"""
from datetime import date


def add_person(people: dict):
    """Add a person to dictionary"""
    is_valid_name = False
    while not is_valid_name:
        name = input("Name: ")
        if name == "":
            print("Name can't be empty")
        elif name in people.keys():
            print("Name has already existed")
        else:
            is_valid_name = True

    is_valid_birthday = False
    while not is_valid_birthday:
        birthday = input("Birthday(DD/MM/YYYY): ")
        if birthday == "":
            print("Birthday can't be empty")
        else:
            birthday_details = birthday.split('/')
            if len(birthday_details) != 3:
                print("Invalid birthday format")
            else:
                try:
                    birth_date = int(birthday_details[0])
                    birth_month = int(birthday_details[1])
                    birth_year = int(birthday_details[2])
                except ValueError:
                    print("Invalid birthday format")
                    continue

                today = date.today().strftime("%d-%m-%Y").split('-')
                current_date = int(today[0])
                current_month = int(today[1])
                current_year = int(today[2])

                if 0 < birth_year <= current_year:
                    month_limit = 12 if birth_year != current_year else current_month
                    if 0 < birth_month <= month_limit:
                        if birth_month == 2:
                            date_limit = 28 + (1 if birth_year % 4 == 0 else 0)
                        elif birth_month in [1, 3, 5, 7, 8, 10, 12]:
                            date_limit = 31
                        else:
                            date_limit = 30
                        date_limit = date_limit if birth_year != current_year and birth_month != current_month else current_date
                        if 0 < birth_date <= date_limit:
                            people[name] = (birth_date, birth_month, birth_year)
                            is_valid_birthday = True
                        else:
                            print("Invalid date")
                    else:
                        print("Invalid month")
                else:
                    print("Invalid year")


def main():
    """Ask user to add users, and then display their name and age"""
    people = {}

    for i in range(5):
        add_person(people)

    today = date.today().strftime("%d-%m-%Y").split('-')
    current_date = int(today[0])
    current_month = int(today[1])
    current_year = int(today[2])

    for name, birthday in people.items():
        birth_date = birthday[0]
        birth_month = birthday[1]
        birth_year = birthday[2]

        age = current_year - birth_year - 1
        if birth_month < current_month:
            age += 1
        elif birth_month == current_month:
            if birth_date < current_date:
                age += 1

        print("{0} is {1} years old".format(name,age))


if __name__ == "__main__":
    main()
