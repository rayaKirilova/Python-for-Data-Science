balance = 0.0

while True:
    transaction = input()

    if transaction.lower() == "end":
        break

    amount = float(transaction)
    if amount > 0:
        print(f"Increase: {amount:.2f}")
    else:
        print(f"Decrease: {abs(amount):.2f}")

    balance += amount

print(f"Balance: {balance:.2f}")
