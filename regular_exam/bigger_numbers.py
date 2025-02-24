numbers_list = [int(number) for number in input().split()]
number = int(input())
filtered_list = []

for current_number in numbers_list:
    if current_number > number:
        filtered_list.append(str(current_number))

result = " ".join(filtered_list)
print(result)