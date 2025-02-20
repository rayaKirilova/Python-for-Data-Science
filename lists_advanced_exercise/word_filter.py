text = [word for word in input().split()]

for word in text:
    if len(word) % 2 == 0:
        print(word)
