text = input()

vowels = "aeiouAEIOU"
new_text = "".join([char for char in text if char not in vowels])

print(new_text)
