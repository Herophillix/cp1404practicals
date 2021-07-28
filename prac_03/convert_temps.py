"""
Convert temperatures from .txt file and output to a .txt file
"""
INPUT_FILE_DIRECTORY = "temps_input.txt"
OUTPUT_FILE_DIRECTORY = "temps_output.txt"


def fahrenheit_to_celsius(temperature):
    """Convert fahrenheit to celsius"""
    return 5 / 9 * (temperature - 32)


def celsius_to_fahrenheit(temperature):
    """Convert celsius to fahrenheit"""
    return temperature * 9.0 / 5 + 32


def main():
    """Read a .txt file and save it to a .txt file"""
    in_file = open(INPUT_FILE_DIRECTORY, 'r')
    temperature_list = in_file.readlines()
    in_file.close()

    out_file = open(OUTPUT_FILE_DIRECTORY, 'w')
    for value in temperature_list:
        try:
            temperature = float(value)
            out_file.write("{0}\n".format(celsius_to_fahrenheit(temperature)))
        except ValueError:
            print("{0} is not a float".format(value))
    out_file.close()


if __name__ == "__main__":
    main()
