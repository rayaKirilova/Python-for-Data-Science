input_names = input()

list_names = [name for name in input_names.split(', ')]
sorted_list = sorted(list_names, key=lambda x: (-len(x), x))

print(sorted_list)
# print(list_names)