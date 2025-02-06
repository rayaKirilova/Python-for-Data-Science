balance = int(input())
withdraw = int(input())
limit = int(input())

if withdraw > limit:
    print('The limit was exceeded.')
else:
    if balance >= withdraw:
        print('The withdraw was successful.')
    else:
        print('Insufficient availability.')


