n = int(input())
total_sum = 0

if n <= 0:
    print(0)

for _ in range(n):
    number = int(input())
    total_sum += number

    if total_sum != 0:
        print(total_sum)
    else:
        print(total_sum)
