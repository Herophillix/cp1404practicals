TARIFF_11 = 0.244618
TARIFF_31 = 0.136928


def main():
    current_tariff = None

    print("Electricity bill estimator")
    tariff_choice = int(input("Tariff 11 or 31?: "))
    while current_tariff is None:
        if tariff_choice == 11:
            current_tariff = TARIFF_11
        elif tariff_choice == 31:
            current_tariff = TARIFF_31
        else:
            print("Tariff not found")
            tariff_choice = int(input("Tariff 11 or 31?: "))

    energy = float(input("Energy used (kWh): "))
    while energy <= 0:
        print("Energy used must be greater than 0kWh")
        energy = float(input("Energy used (kWh): "))

    day = int(input("Days used: "))
    while day <= 0:
        print("Days used must be greater than 0")
        day = int(input("Days used: "))

    estimated_price = current_tariff * energy * day
    print("Estimated price: $" + "{:.2f}".format(estimated_price))


if __name__ == '__main__':
    main()
