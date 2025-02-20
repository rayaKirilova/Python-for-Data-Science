stock = {}
total_sold = 0

while True:
    command = input()

    if command == "Complete":
        break

    command_parts = command.split()
    action = command_parts[0]
    quantity = int(command_parts[1])
    food = command_parts[2]

    if action == "Receive":
        if quantity > 0:
            if food in stock:
                stock[food] += quantity
            else:
                stock[food] = quantity

    elif action == "Sell":
        if food not in stock:
            print(f"You do not have any {food}.")
        else:
            if stock[food] < quantity:
                sold_quantity = stock[food]
                stock.pop(food)
                print(f"There aren't enough {food}. You sold the last {sold_quantity} of them.")
                total_sold += sold_quantity
            else:
                stock[food] -= quantity
                total_sold += quantity
                print(f"You sold {quantity} {food}.")
                if stock[food] == 0:
                    stock.pop(food)

for food, quantity in stock.items():
    print(f"{food}: {quantity}")
print(f"All sold: {total_sold} goods")