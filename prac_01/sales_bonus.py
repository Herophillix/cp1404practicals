"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""


def main():
    sales = float(input("Input your sale: $"))
    while sales >= 0:
        bonus = 0
        if sales >= 1000:
            bonus = sales * 0.15
        else:
            bonus = sales * 0.1
        print("Your bonus is $" + "{:.2f}".format(bonus))
        sales = float(input("Input your sale: $"))
    else:
        print("End")


if __name__ == '__main__':
    main()
