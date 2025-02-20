current_version = list(map(int, input().split('.')))
new_version = []

for i in range(len(current_version) - 1, -1, -1):
    if current_version[i] < 9:
         current_version[i] += 1
         break
    else:
        current_version[i] = 0

new_version = '.'.join(map(str, current_version))

print(new_version)

