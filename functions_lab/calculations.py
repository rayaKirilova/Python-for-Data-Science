def calculations(operator: str, first_num:int, second_num:int) -> int:
    result = 0

    if operator == 'add':
        result = first_num + second_num
    elif operator == 'subtract':
        result = first_num - second_num
    elif operator == 'multiply':
        result = first_num * second_num
    elif operator == 'divide':
        result = first_num // second_num

    return result

input_operator = input()
first_number = int(input())
second_number = int(input())
print(calculations(input_operator, first_number, second_number))