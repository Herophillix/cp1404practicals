"""
Count the number of repeated words in a text
"""


def main():
    """Ask the user to input a text, and count the number of repeated words"""
    count_of_words = {}
    text = input("Input text: ")

    for word in text.split():
        word = word.lower()
        if word in count_of_words:
            count_of_words[word] += 1
        else:
            count_of_words[word] = 1

    longest_char_count = 0
    for key in count_of_words.keys():
        longest_char_count = longest_char_count if longest_char_count > len(key) else len(key)

    for key in sorted(count_of_words.keys()):
        print("{0:<{l}}: {1}".format(key, count_of_words[key], l=longest_char_count))


if __name__ == "__main__":
    main()
