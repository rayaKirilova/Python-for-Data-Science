n = int(input())
numbers = []
filtered_numbers = []

for i in range(n):
    number = int(input())
    numbers.append(number)

command = input()

if command == 'even':
    for element in numbers:
        if element % 2 == 0 or element == 0:
            filtered_numbers.append(element)
elif command == 'odd':
    for element in numbers:
        if element % 2 != 0:
            filtered_numbers.append(element)
elif command == 'negative':
    for element in numbers:
        if element < 0:
            filtered_numbers.append(element)
elif command == 'positive':
    for element in numbers:
        if element >= 0:
           filtered_numbers.append(element)

print(filtered_numbers)
