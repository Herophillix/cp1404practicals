"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os
import re


def main():
    """Demo os module functions."""
    os.chdir('Lyrics')

    for directory_name, subdirectories, filenames in os.walk('..'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        # add a loop to rename the files
        for filename in filenames:
            old_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(old_name, new_name)


def get_fixed_filename(filename: str):
    """Return a 'fixed' version of filename."""
    filename = filename.replace(".TXT", ".txt")

    # Split all the names by the whitespace
    split_names = filename.replace("_", " ").split(" ")
    fixed_names = []
    for split_name in split_names:
        # Capitalize the first letter of the name
        for i, character in enumerate(split_name):
            if character.isalpha():
                split_name = split_name[0:i] + split_name[i].upper() + split_name[i + 1:]
                break

        # Split all the capitalized names within the split_name
        capitalized_names = []
        capitalized_name = ""
        is_word_found = False
        for character in split_name:
            if character.isalpha() and character.isupper():
                if not is_word_found:
                    is_word_found = True
                else:
                    capitalized_names.append(capitalized_name)
                    capitalized_name = ""
            capitalized_name = capitalized_name + character
        capitalized_names.append(capitalized_name)

        for capitalized_name in capitalized_names:
            fixed_names.append(capitalized_name)

    return '_'.join(fixed_names)


if __name__ == "__main__":
    main()
