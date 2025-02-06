hour = int(input())
week_day = input()

if week_day == "Monday" or week_day == "Tuesday" or week_day == "Wednesday" or week_day == "Thursday" or week_day == "Friday" or week_day == "Saturday":
    if (hour >= 1 and hour <= 6) or (hour >= 10 and hour <= 12):
        print('open')
    else:
        print('closed')
else:
    print('closed')