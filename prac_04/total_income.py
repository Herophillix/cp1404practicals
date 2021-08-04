"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def print_report(incomes):
    """Display the report of the incomes"""
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes):
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month + 1, income, total))


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("Number of months: "))

    for month in range(1, number_of_months + 1):
        income = float(input("Enter income for month {0}: ".format(month)))
        incomes.append(income)

    print_report(incomes)


if __name__ == "__main__":
    main()
