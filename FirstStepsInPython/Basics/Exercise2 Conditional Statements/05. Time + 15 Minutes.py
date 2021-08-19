hour = int(input())
minutes = int(input())
minutes += 15

if minutes > 59:
    hour += 1

if hour == 24:
    hour = 0

if minutes > 59:
    minutes -= 60

if minutes >= 10 and minutes <= 59:
    print(f"{hour}:{minutes}")
elif minutes >= 0 and minutes <= 9:
    print(f"{hour}:0{minutes}")
