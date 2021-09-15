"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Demo os module functions."""
    os.chdir('Lyrics')

    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        # add a loop to rename the files
        for filename in filenames:
            old_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(old_name, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    split_names = filename.split(' ')
    print(split_names)
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


if __name__ == "__main__":
    # main()
    get_fixed_filename("Amazing Grace")
