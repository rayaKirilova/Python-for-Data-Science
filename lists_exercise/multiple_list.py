factor = int(input())
count = int(input())

multiple_list = []

for index in range(1, count + 1):
    multiple_list.append(index * factor)

print(multiple_list)