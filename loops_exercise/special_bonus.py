stop_number = int(input())
previous_number = 1

while True:
    current_number = int(input())

    if current_number == stop_number:
        bonus_number = previous_number * 1.2
        print(f"{bonus_number:.0f}")
        break
    else:
        previous_number = current_number

