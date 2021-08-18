book_pages = int(input())
pages_read_per_hour = int(input())
number_of_days = int(input())
total_time = book_pages / pages_read_per_hour
daily_hours_needed = total_time / number_of_days
print(daily_hours_needed)