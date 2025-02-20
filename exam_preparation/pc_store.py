cpu_price = float(input())
video_card_price = float(input())
ram_price = float(input())
ram_count = int(input())
percent_discount = float(input())

cpu_price_in_lv = cpu_price * 1.57
video_card_in_lv = video_card_price * 1.57
ram_price_in_lv = ram_price * 1.57
total_ram_price = ram_price_in_lv * ram_count

cpu_price_after_discount = cpu_price_in_lv - cpu_price_in_lv * percent_discount
video_card_price_after_discount = video_card_in_lv - video_card_in_lv * percent_discount

total_sum_parts = cpu_price_after_discount + total_ram_price + video_card_price_after_discount

print(f'Money needed - {total_sum_parts:.2f} leva.')