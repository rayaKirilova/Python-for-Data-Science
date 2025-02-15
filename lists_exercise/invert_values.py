num_list = input().split()

opposite_list = []

for number in num_list:
    number = -int(number)
    opposite_list.append(number)

print(opposite_list)
