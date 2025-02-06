number = int(input())

count_divisible_by_two = 0
count_divisible_by_three = 0
count_divisible_by_four = 0

for i in range(number):
    input_number = int(input())

    if input_number % 2 == 0:
        count_divisible_by_two += 1
    if input_number % 3 == 0:
        count_divisible_by_three += 1
    if input_number % 4 == 0:
        count_divisible_by_four += 1

print(f"{(count_divisible_by_two / number) * 100:.2f}%")
print(f"{(count_divisible_by_three / number) * 100:.2f}%")
print(f"{(count_divisible_by_four / number) * 100:.2f}%")
