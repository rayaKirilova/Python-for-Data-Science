n = int(input())
result = 0
result_str = '1'

for i in range(1, n):
    result = result + i
    result_str += f'+{i+1}'

print(f'{result_str}={result + n}')