input_text = input().split()
bakery = {}

for index in range(0, len(input_text), 2):
    key = input_text[index]
    value = int(input_text[index +1])

    bakery[key] = value
print(bakery)
