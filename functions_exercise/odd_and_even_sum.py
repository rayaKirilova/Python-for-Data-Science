def sum_even_odd_digits(number: int):
    even_sum = 0
    odd_sum = 0

    for digit in str(number):
        if int(digit) % 2 == 0:
            even_sum += int(digit)

        else:
            odd_sum += int(digit)

            # return f"{even_sum} {odd_sum}"
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number = int(input())
result = sum_even_odd_digits(number)
print(result)