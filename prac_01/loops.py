def main():
    print("Loop 1: Example")
    for i in range(1, 21, 2):
        print(i, end=' ')
    print()
    print()

    print("Loop 2: 10s from 0 to 100")
    for i in range(0, 101, 10):
        print(i, end=' ')
    print()
    print()

    print("Loop 3: Count down from 20 to 1")
    for i in range(20, 0, -1):
        print(i, end=' ')
    print()
    print()

    print("Loop 4: Stars in a line")
    number_of_stars = int(input("Input number of star(s): "))
    while number_of_stars < 0:
        print("Stars can't be negative")
        number_of_stars = int(input("Input number of star(s): "))
    for i in range(0, number_of_stars + 1):
        print('*', end=' ')
    print()
    print()

    print("Loop 5: Stars")
    number_of_stars = int(input("Input number of star(s): "))
    while number_of_stars < 0:
        print("Stars can't be negative")
        number_of_stars = int(input("Input number of star(s): "))

    for i in range(0, number_of_stars):
        print('*' * (i + 1))


if __name__ == '__main__':
    main()
