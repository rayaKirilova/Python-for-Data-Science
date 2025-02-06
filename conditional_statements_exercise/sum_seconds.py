first_player_seconds = int(input())
second_player_seconds = int(input())
third_player_seconds = int(input())

sum_seconds = first_player_seconds + second_player_seconds + third_player_seconds
reminder = sum_seconds % 60

if reminder >= 0 and reminder <= 9:
    print(f'{sum_seconds // 60}:0{reminder}')
else:
    print(f'{sum_seconds // 60}:{reminder}')


