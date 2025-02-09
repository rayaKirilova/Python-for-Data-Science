count = int(input())
sum_left = 0
sum_right = 0

for _ in range(0, count):
    number = int(input())
    sum_left += number

for _ in range(count + 1, count * 2 + 1):
    number = int(input())
    sum_right += number

if sum_left == sum_right:
    print(f"Yes, sum = {sum_left}")
else:
    diff = abs(sum_left - sum_right)
    print(f"No, diff = {diff}")