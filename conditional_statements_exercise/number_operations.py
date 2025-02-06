first_number = int(input())
second_number = int(input())
operator =  input()

result = 0

if operator == '+':
    result = first_number + second_number
elif operator == '-':
    result = first_number - second_number
elif operator == '*':
    result = first_number * second_number
elif operator == '/':
    result = first_number / second_number

print(f"{first_number} {operator} {second_number} = {result:.2f}")