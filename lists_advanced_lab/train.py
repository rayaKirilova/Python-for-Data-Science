count = int(input())

# train = [int(0) for x in range(count)]
train = [0] * count

command = input()

while command != 'End':
    instructions = command.split()

    if instructions[0] == 'add':
        train[count - 1] += int(instructions[1])
    if instructions[0] == 'insert':
        index = int(instructions[1])
        train[index] += int(instructions[2])
    if instructions[0] == 'leave':
        index = int(instructions[1])
        train[index] -= int(instructions[2])

    command = input()

print(train)
