list_words = input().split()

letter_count = {}

for word in list_words:
    for letter in word:
        if letter == " ":
            continue

        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1

letters = "\n".join(f"{key} -> {value}" for key, value in letter_count.items())

print(letters)