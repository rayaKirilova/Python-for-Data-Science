square_meters = float(input())

total_cost = square_meters * 7.61
discount = total_cost * 0.18
final_price = total_cost - discount

print(f'The final price is: {final_price} lv.')
print(f'The discount is: {discount} lv.')