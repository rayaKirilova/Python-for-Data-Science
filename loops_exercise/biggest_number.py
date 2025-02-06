number = int(input())
max_number = 0

for i in range(number):
    input_number = int(input())

    if input_number >= max_number:
        max_number = input_number

print(max_number)