"""
Generate random temperature and output into a .txt file
"""
import random

FILE_DIRECTORY = "temps_input.txt"
MIN_TEMPERATURE = -200
MAX_TEMPERATURE = 200


def main():
    """Generate random temperature and output into a .txt file"""
    file = open(FILE_DIRECTORY, 'w')
    for i in range(0, 15):
        file.write("{0}\n".format(random.uniform(-200, 200)))
    file.close()


if __name__ == "__main__":
    main()
