string_numbers = input().split()

numbers = [int(num) for num in string_numbers]
sorted_nums = list(sorted(numbers))

print(sorted_nums)