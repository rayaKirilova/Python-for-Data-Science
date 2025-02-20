def calculate_price(product: str, quantity: int) -> str:
    total_price = 0

    if product == "coffee":
        total_price = 1.50 * quantity
    elif product == "coke":
         total_price = 1.40 * quantity
    elif product == "water":
        total_price = 1.00 * quantity
    elif product == "snacks":
        total_price = 2.00 * quantity

    return f'{total_price:.2f}'

input_product = input()
input_quantity = int(input())
print(calculate_price(input_product, input_quantity))