training_fee = int(input())

price_sneakers = training_fee - training_fee * 0.4
price_team = price_sneakers - price_sneakers * 0.2
price_basketball = price_team / 4
price_accessories = price_basketball / 5

total_price_equipment = training_fee + price_sneakers + price_team + price_basketball + price_accessories
print(total_price_equipment)
