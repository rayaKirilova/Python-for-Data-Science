products = {}

while True:
    data = input()

    if data == 'buy':
        break

    name, price, quantity = data.split()
    price = float(price)
    quantity = int(quantity)

    if name not in products:
        products[name] = {"price": price, "quantity": quantity}
    else:
        products[name]["quantity"] += quantity
        products[name]["price"] = price

for name, info in products.items():
    total_price = info["price"] * info["quantity"]
    print(f'{name} -> {total_price:.2f}')