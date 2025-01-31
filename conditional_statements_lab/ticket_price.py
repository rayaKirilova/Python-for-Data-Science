ticket_type = input()

if ticket_type == 'student':
    print('$1.00')
elif ticket_type == 'regular':
    print('$1.60')
else:
    print('Invalid ticket type!')