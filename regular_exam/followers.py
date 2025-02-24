command = input()
followers_book = {}

while command != 'Log out':
    followers_info = command.split(': ')
    status = followers_info[0]
    username = followers_info[1]

    if status == 'New follower':
        if username not in followers_book:
            followers_book[username] = 0
    elif status == 'Like':
        if username not in followers_book:
            followers_book[username] = 0
        like_count = int(followers_info[2])
        followers_book[username] += like_count
    elif status == 'Comment':
        if username not in followers_book:
            followers_book[username] = 1
        else:
            followers_book[username] += 1
    elif status == 'Blocked':
        if username not in followers_book:
            print(f"{username} doesn't exist.")
        else:
            followers_book.pop(username)

    command = input()

print(f'{len(followers_book)} followers')

for follower, count in followers_book.items():
    print(f'{follower}: {count}')
