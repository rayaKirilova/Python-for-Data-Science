num_list = input().split()
count = int(input())

list_int_nums = [int(num) for num in num_list]

for i in range(count):
    min_element = min(list_int_nums)
    list_int_nums.remove(min_element)

print(", ".join(map(str, list_int_nums)))
