def main():
    # Discount
    min_discount_price = 100
    discount = 0.1

    total_price = 0

    print("Welcome to the shop!")
    number_of_items = int(input("Input number of items: "))
    while number_of_items <= 0:
        print("You need to buy at least an item here!")
        number_of_items = int(input("Input number of items: "))

    for i in range(number_of_items):
        item_index = str(i + 1)
        input_price = float(input("Price of item " + item_index + ": $"))
        while input_price <= 0:
            print("Price can't be less than $0")
            input_price = float(input("Price of item " + item_index + ": $"))
        total_price += input_price

    if total_price > min_discount_price:
        print("Total price is over $" + str(min_discount_price) + ", applying a " + str(discount * 100) + "% discount")
        total_price *= 1 - discount
    print("Total price for " + str(number_of_items) + " item(s): $" + "{:.2f}".format(total_price))


if __name__ == '__main__':
    main()
