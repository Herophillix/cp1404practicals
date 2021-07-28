"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
MENU = "C - Convert Celsius to Fahrenheit \nF - Convert Fahrenheit to Celsius \nQ - Quit"


def fahrenheit_to_celsius(temperature):
    """Convert fahrenheit to celsius"""
    return 5 / 9 * (temperature - 32)


def celsius_to_fahrenheit(temperature):
    """Convert celsius to fahrenheit"""
    return temperature * 9.0 / 5 + 32


def main():
    """Ask user for a temperature and converts it to another unit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


if __name__ == '__main__':
    main()
