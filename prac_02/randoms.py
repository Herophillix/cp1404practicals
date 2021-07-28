import random


def main():
    print(random.randint(5, 20))  # line 1
    # Smallest number: 5
    # Largest number: 20

    print(random.randrange(3, 10, 2))  # line 2
    # Smallest number: 3
    # Largest number: 9
    # Does not produce 4 as it is an even number, the code above only generates odd numbers

    print(random.uniform(2.5, 5.5))  # line 3
    # Smallest number: 2.5
    # Largest number: 5.5

    # TODO: Write code, not a comment, to produce a random number between 1 and 100 inclusive.
    print(random.randint(1, 100))


if __name__ == '__main__':
    main()
