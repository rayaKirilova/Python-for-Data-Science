numbers_list = input().split(", ")
beggars_count = int(input())

numbers = [int(num) for num in numbers_list]
beggars_sums = []

for beggar_index in range(beggars_count): # 0 1 2
    current_sum = 0

    for num in range(beggar_index, len(numbers), beggars_count):
        current_sum += numbers[num]

    beggars_sums.append(current_sum)

print(beggars_sums)
