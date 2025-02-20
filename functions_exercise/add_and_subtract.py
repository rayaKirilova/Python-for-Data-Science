def sum_numbers(num1: int, num2: int) -> int:
    return num1 + num2

def subtract(sum_nums: int, num3: int) -> int:
    sum_nums = sum_numbers(input_first_num, input_second_num)
    return sum_nums - num3

def add_and_subtract(num1: int, num2: int, num3: int) -> int:
    result_subtract = subtract(sum_numbers(input_first_num, input_second_num), input_third_num)
    return result_subtract

input_first_num = int(input())
input_second_num = int(input())
input_third_num = int(input())

print(add_and_subtract(input_first_num, input_second_num, input_third_num))