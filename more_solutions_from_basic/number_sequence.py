n = int(input())
first_number = int(input())

min_number = first_number
max_number = first_number

for i in range(1, n):
    number = int(input())

    if number < min_number:
        min_number = number
    if number > max_number:
        max_number = number

print(f'Max number: {max_number}')
print(f'Min number: {min_number}')