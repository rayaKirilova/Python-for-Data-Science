cards = input().split()
number_of_shuffles = int(input())

for _ in range(number_of_shuffles):
    half = len(cards) // 2
    top_half = cards[:half]
    bottom_half = cards[half:]

    shuffled_cards = []

    for i in range(half):
        shuffled_cards.append(top_half[i])
        shuffled_cards.append(bottom_half[i])

    cards = shuffled_cards

print(cards)
