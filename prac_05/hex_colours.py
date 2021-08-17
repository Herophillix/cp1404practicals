"""
Display hex color code based on its name
"""
COLOR = {"ALICEBLUE": "#f0f8ff", "BEIGE": "#f5f5dc", "BLACK": "#000000", "BLANCHEDALMOND": "#ffebcd",
         "CADETBLUE": "#5f9ea0", "CORAL": "#ff7f50", "DARKGOLDENROD": "#b8860b", "DARKKHAKI": "#bdb76b",
         "DARKORANGE": "#ff8c00", "DARKORCHID": "#9932cc"}


def main():
    """Ask user for a color name and display its hex color"""
    color_name = input("Color name: ").upper()
    while color_name not in COLOR:
        print("Color not found")
        color_name = input("Color name: ").upper()
    print("{0} has a code of {1}".format(color_name, COLOR[color_name]))


if __name__ == "__main__":
    main()
