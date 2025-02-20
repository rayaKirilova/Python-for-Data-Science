n = int(input())
word = input()

first_list = []
filtered_list = []

for _ in range(0, n):
    text = input()
    first_list.append(text)

print(first_list)
filtered_list = list(filter(lambda item: word in item, first_list))

print(filtered_list)