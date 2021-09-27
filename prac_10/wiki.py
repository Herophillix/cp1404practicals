"""
Wikipedia Tutorial
"""
import wikipedia


def main():
    """Wikipedia Tutorial"""
    is_input_empty = False
    while not is_input_empty:
        user_input = input("What do you want to search? ")
        if user_input != "":
            try:
                page = wikipedia.page(user_input, auto_suggest=False)
                print(page.title)
                print(page.summary)
                print(page.url)
            except wikipedia.exceptions.DisambiguationError as e:
                print(e.options)
        else:
            is_input_empty = True


if __name__ == "__main__":
    main()
