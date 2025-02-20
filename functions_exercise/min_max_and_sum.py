numbers_input = input().split()
numbers = [int(num) for num in numbers_input]

print(f'The minimum number is {min(numbers)}')
print(f'The maximum number is {max(numbers)}')
print(f'The sum number is: {sum(numbers)}')