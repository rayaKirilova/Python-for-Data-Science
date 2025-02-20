def is_even(numbers_as_string: list[str]) -> list[int]:
    numbers = [int(num) for num in numbers_as_string]
    return list(filter(lambda x: x % 2 == 0, numbers))

string_numbers = input().split()
print(is_even(string_numbers))