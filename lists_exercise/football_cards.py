team_a = []
team_b = []

for number in range(1, 12):
    team_a.append(f'A-{number}')
    team_b.append(f'B-{number}')

team_cards = input().split()
end_game = False

for element in range(len(team_cards)):
    if team_cards[element] in team_a:
        team_a.remove(team_cards[element])
    elif team_cards[element] in team_b:
        team_b.remove(team_cards[element])

    if len(team_a) < 7 or len(team_b) < 7:
        end_game = True
        break

print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')

if end_game:
    print('Game was terminated')
