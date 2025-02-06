number = int(input())
is_special = True

for digit in str(number):
    if number % int(digit) != 0:
        is_special = False

if is_special:
    print(f"{number} is special")
else:
    print(f"{number} is not special")
