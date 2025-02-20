substring_list = [substr for substr in input().split(', ')]
full_list = [str for str in input().split(', ')]

result_list = []

for substring in substring_list:
    for string in full_list:
        if substring in string:
            result_list.append(substring)
            break

print(result_list)


