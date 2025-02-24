import math

count_cans_paint = int(input())
count_wallpaper_rolls = int(input())
price_gloves = float(input())
price_brushes = float(input())

total_price_paint = count_cans_paint * 21.50
total_price_wallpapers = count_wallpaper_rolls * 5.20
needed_gloves = math.ceil(count_wallpaper_rolls * 0.35)
#rint(needed_gloves)

needed_brushes = math.floor(count_cans_paint * 0.48)
#print(needed_brushes)

total_price_gloves = price_gloves * needed_gloves
#print(total_price_gloves)

total_price_brushes = price_brushes * needed_brushes
#print(total_price_brushes)

total_price_all_products = total_price_paint + total_price_wallpapers + total_price_brushes + total_price_gloves
#print(total_price_all_products)

delivery_price = total_price_all_products / 15
print(f'This delivery will cost {delivery_price:.2f} lv.')
