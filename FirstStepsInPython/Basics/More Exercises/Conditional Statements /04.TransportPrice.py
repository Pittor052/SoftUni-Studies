kilometres = int(input())
time_of_day = str(input())

if kilometres < 20:
    if time_of_day == "day":
        print(f"{(kilometres * 0.79) + 0.70:.2f}")
    elif time_of_day == "night":
        print(f"{(kilometres * 0.9) + 0.70:.2f}")
elif 20 <= kilometres < 100:
    print(f"{kilometres * 0.09:.2f}")
else:
    print(f"{kilometres * 0.06:.2f}")
