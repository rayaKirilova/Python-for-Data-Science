n = int(input())
positive_nums_list = []
negative_nums_list = []

for i in range(0, n):
    number = int(input())

    if number >= 0:
        positive_nums_list.append(number)
    else:
        negative_nums_list.append(number)

print(positive_nums_list)
print(negative_nums_list)

count_positives = len(positive_nums_list)
sum_of_negatives = sum(negative_nums_list)

print(f'Count of positives: {count_positives}')
print(f'Sum of negatives: {sum_of_negatives}')
