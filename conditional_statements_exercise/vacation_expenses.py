season = input()
accommodation_type = input()
count_of_days = int(input())

total_expenses = 0

if season == 'Spring':
    if accommodation_type == 'Hotel':
        price_accommodation = 30 * count_of_days
        total_expenses = price_accommodation - price_accommodation * 0.2
    elif accommodation_type == 'Camping':
        price_accommodation = 10 * count_of_days
        total_expenses = price_accommodation - price_accommodation * 0.2
elif season == 'Summer':
    if accommodation_type == 'Hotel':
        total_expenses = 50 * count_of_days
    elif accommodation_type == 'Camping':
        total_expenses = 30 * count_of_days
elif season == 'Winter':
    if accommodation_type == 'Hotel':
        price_accommodation = 40 * count_of_days
        total_expenses = price_accommodation - price_accommodation * 0.1
    elif accommodation_type == 'Camping':
        price_accommodation = 10 * count_of_days
        total_expenses = price_accommodation - price_accommodation * 0.1
elif season == 'Autumn':
    if accommodation_type == 'Hotel':
        price_accommodation = 20 * count_of_days
        total_expenses = price_accommodation - price_accommodation * 0.3
    elif accommodation_type == 'Camping':
        price_accommodation = 15 * count_of_days
        total_expenses = price_accommodation - price_accommodation * 0.3

print(f'{total_expenses:.2f}')
