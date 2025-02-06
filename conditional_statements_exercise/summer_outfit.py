temperature = int(input())
time_of_day = input()

clothing = ''
shoes = ''

if time_of_day == "Morning":
    if temperature >= 10 and temperature <= 18:
        clothing = 'Sweatshirt'
        shoes = 'Sneakers'
    elif temperature > 18 and temperature <= 24:
        clothing = 'Shirt'
        shoes = 'Moccasins'
    else:
        clothing = 'T-Shirt'
        shoes = 'Sandals'
elif time_of_day == "Afternoon":
    if temperature >= 10 and temperature <= 18:
        clothing = 'Shirt'
        shoes = 'Moccasins'
    elif temperature > 18 and temperature <= 24:
        clothing = 'T-Shirt'
        shoes = 'Sandals'
    else:
        clothing = 'Swim Suit'
        shoes = 'Barefoot'
elif time_of_day == "Evening":
        clothing = 'Shirt'
        shoes = 'Moccasins'

print(f'It\'s {temperature} degrees, get your {clothing} and {shoes}.')
