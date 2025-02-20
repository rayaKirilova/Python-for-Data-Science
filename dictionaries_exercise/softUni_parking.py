count = int(input())

parking = {}

for _ in range(count):
    command = input().split()

    if "register" in command:
        username = command[1]
        license_number = command[2]

        if username not in parking:
            parking[username] = license_number
            print(f'{username} registered {license_number} successfully')
        else:
            print(f"ERROR: already registered with plate number {license_number}")
    elif "unregister" in command:
        username = command[1]

        if username in parking:
            parking.pop(username)
            print(f"{username} unregistered successfully")
        else:
            print(f'ERROR: user {username} not found')

for username, license_number in parking.items():
    print(f'{username} => {license_number}')