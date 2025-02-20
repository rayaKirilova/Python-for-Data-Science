count = int(input())
synonyms = {}

for current_synonym in range(count):
    word = input()
    synonym = input()

    if word not in synonyms.keys():
        synonyms[word] = []
    synonyms[word].append(synonym)

for word, current_synonym in synonyms.items():
    print(f'{word} - {(", ").join(current_synonym)}')