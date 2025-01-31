number = int(input())
is_valid = (number >= 100 and number <= 200) or number == 0

if not is_valid:
    print('invalid')