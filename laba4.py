
def format_price(price):
    return f"ціна: {price:.2f} грн"



def check_availability(*items):

    store_items = ["яблуко", "банан", "хліб", "молоко", "яйця"]
    availability = {}
    for item in items:
        availability[item] = item in store_items
    return availability



def process_order(order):
    availability = check_availability(*order)

    if all(availability.values()):
        prices = {"яблуко": 15, "банан": 20, "хліб": 25, "молоко": 30, "яйця": 40}
        total = sum(prices[item] for item in order)
        return f"Ваше замовлення: {order}, {format_price(total)}"
    else:
        missing = [item for item, avail in availability.items() if not avail]
        return f"Деяких товарів немає в наявності: {missing}"


while True:
    action = input("Введіть 'купити' або 'переглянути ціну' (stop для виходу): ").lower()
    if action == "stop":
        break
    order_input = input("Введіть товари через кому: ").lower()
    order = [item.strip() for item in order_input.split(",")]

    if action == "купити":
        print(process_order(order))
    elif action == "переглянути ціну":
        availability = check_availability(*order)
        if all(availability.values()):
            prices = {"яблуко": 15, "банан": 20, "хліб": 25, "молоко": 30, "яйця": 40}
            total = sum(prices[item] for item in order)
            print(f"Загальна ціна замовлення: {format_price(total)}")
        else:
            missing = [item for item, avail in availability.items() if not avail]
            print(f"Деяких товарів немає в наявності: {missing}")
