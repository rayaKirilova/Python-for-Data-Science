input_nums = input().split(', ')
numbers = [int(num) for num in input_nums]

positive_nums = [number for number in numbers if number >= 0]
positive_nums_str = (', ').join([str(num) for num in positive_nums])

negative_nums = [number for number in numbers if number < 0]
negative_nums_str = (', ').join([str(num) for num in negative_nums])

even_nums = [number for number in numbers if number % 2 == 0]
even_nums_str = (', ').join([str(num) for num in even_nums])

odd_nums = [number for number in numbers if number % 2 != 0]
odd_nums_str = (', ').join([str(num) for num in odd_nums])


print(f'Positive: {positive_nums_str}')
print(f'Negative: {negative_nums_str}')
print(f'Even: {even_nums_str}')
print(f'Odd: {odd_nums_str}')