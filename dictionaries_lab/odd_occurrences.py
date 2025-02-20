languages = [language.lower() for language in input().split()]
filtered_languages = {}

for element in languages:
    if element not in filtered_languages.keys():
        filtered_languages[element] = 0
    filtered_languages[element] += 1

odd_occurences = []
for language, occurences in filtered_languages.items():
    if occurences % 2 != 0:
        odd_occurences.append(language)

print(' '.join(odd_occurences))