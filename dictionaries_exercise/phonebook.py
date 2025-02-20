data = input()
phonebook = {}

while '-' in data:
    name, phone = data.split('-')
    phonebook[name] = phone

    data = input()

count = int(data)

for _ in range(count):
    search_name = input()
    if search_name in phonebook:
        print(f'{search_name} -> {phonebook[search_name]}')
    else:
        print(f'Contact {search_name} does not exist.')