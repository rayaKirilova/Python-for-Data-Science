number_of_electrons = int(input())
shell = []

n = 1

while number_of_electrons > 0:
    max_electrons = 2 * (n ** 2)
    electrons_to_add = min(number_of_electrons, max_electrons)
    shell.append(electrons_to_add)

    number_of_electrons -= electrons_to_add

    n += 1

print(shell)