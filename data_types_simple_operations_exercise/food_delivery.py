chicken_menus = int(input())
fish_menus = int(input())
vegetarian_menus = int(input())

menu_price = chicken_menus * 10.35 + fish_menus * 12.40 + vegetarian_menus * 8.15
dessert_price = menu_price * 0.2
total_price = menu_price + dessert_price + 2.50

print(total_price)