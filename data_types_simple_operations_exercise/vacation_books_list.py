number_of_pages = int(input())
pages_per_hour = int(input())
number_of_days = int(input())

reading_time = number_of_pages / pages_per_hour
hours_per_day = reading_time / number_of_days

print('{:.0f}'.format(hours_per_day))
