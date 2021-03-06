"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""


CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory",
                "WA": "Western Australia", "ACT": "Australian Capital Territory", "VIC": "Victoria",
                "TAS": "Tasmania"}


def main():
    """Ask user for abbreviation of State name and display its full name"""
    # Reformat this file so the dictionary code follows PEP 8 convention
    for key, value in CODE_TO_NAME.items():
        print("{0:<3} is {1}".format(key,value))

    state_code = input("Enter short state: ").upper()
    while state_code != "":
        if state_code in CODE_TO_NAME:
            print(state_code, "is", CODE_TO_NAME[state_code])
        else:
            print("Invalid short state").upper()
        state_code = input("Enter short state: ")


if __name__ == "__main__":
    main()
