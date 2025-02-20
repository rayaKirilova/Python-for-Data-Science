list_numbers = [int(num) for num in input().split()]
start_index = int(input())
end_index = int(input())

filtered_list = []

for index in range(start_index, end_index + 1):
    filtered_list.append(list_numbers[index])

sum_min_max_element = max(filtered_list) + min(filtered_list)

print(sum_min_max_element)