"""
CP1404/CP5632 - Practical
Random word generator - based on format of words
Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"


def is_valid_format(word_format):
    """Check if the word format given is valid"""
    return all([characters in ['c', 'v'] for characters in word_format])


def main():
    """Generate a random word using a word format"""
    user_choice = int(input("Create word format(1)/Automatically generate word format(2): "))
    while user_choice < 1 or user_choice > 2:
        print("Please input within range")
        user_choice = int(input("Create word format(1)/Automatically generate word format(2): "))

    word_format = ""
    if user_choice == 1:
        word_format = input("Input a word format(c/v): ")
        while not is_valid_format(word_format):
            print("Invalid format")
            word_format = input("Input a word format(c/v): ")
    else:
        for i in range(0, random.randint(3,10)):
            # Higher probability for consonants
            word_format += 'c' if random.randint(0, 3) else 'v'
    word = ""
    for kind in word_format:
        if kind == 'c':
            word += random.choice(CONSONANTS)
        elif kind == 'v':
            word += random.choice(VOWELS)

    print(word)


if __name__ == "__main__":
    main()
