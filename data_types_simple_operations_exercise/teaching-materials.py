pen_packages = int(input())
markers_packages = int(input())
liters_board_cleaner = int(input())
discount_percent = int(input())

total_price_for_materials = pen_packages * 5.8 + markers_packages * 7.2 + liters_board_cleaner * 1.2
price_after_discount = total_price_for_materials - (total_price_for_materials * discount_percent / 100)

print(price_after_discount)