"""
Estimate electricity bills based on usage rate and tariff rate
"""


TARIFFS = {11: 0.244618, 21: 0.82341, 31: 0.136928, 41: 1.0, 51: 0.63342}


def main():
    """Estimate electricity bill"""
    current_tariff = None
    energy = 0
    day = 0

    print("Electricity bill estimator")
    print("Tariff Rate")
    for key, value in TARIFFS.items():
        print("Tariff {0}: ${1}".format(key,value))

    is_valid_input = False
    while not is_valid_input:
        try:
            tariff_choice = int(input("Tariff: "))
            while current_tariff is None:
                if tariff_choice in TARIFFS:
                    current_tariff = TARIFFS[tariff_choice]
                else:
                    print("Tariff not found")
                    tariff_choice = int(input("Tariff 11 or 31?: "))
            is_valid_input = True
        except ValueError:
            print("Invalid input")

    is_valid_input = False
    while not is_valid_input:
        try:
            energy = float(input("Energy used (kWh): "))
            while energy <= 0:
                print("Energy used must be greater than 0kWh")
                energy = float(input("Energy used (kWh): "))
            is_valid_input = True
        except ValueError:
            print("Invalid input")

    is_valid_input = False
    while not is_valid_input:
        try:
            day = int(input("Days used: "))
            while day <= 0:
                print("Days used must be greater than 0")
                day = int(input("Days used: "))
            is_valid_input = True
        except ValueError:
            print("Invalid input")

    estimated_price = current_tariff * energy * day
    print("Estimated price: $" + "{:.2f}".format(estimated_price))


if __name__ == '__main__':
    main()
