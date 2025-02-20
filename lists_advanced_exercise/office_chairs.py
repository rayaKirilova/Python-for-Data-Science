num_rooms = int(input())
total_free_chairs = 0
is_game_on = True

for room_number in range (1, num_rooms + 1):
    input_str = input()
    chairs, visitors = input_str.split()

    count_chairs = len(chairs)
    count_visitors = int(visitors)

    diff = abs(count_chairs - count_visitors)

    if count_chairs < count_visitors:
        print(f'{diff} more chairs needed in room {room_number}')
        is_game_on = False
    else:
        total_free_chairs += diff

if is_game_on:
    print(f'Game On, {total_free_chairs} free chairs left')