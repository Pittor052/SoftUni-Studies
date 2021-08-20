import math

year = str(input())
p = int(input())
h = int(input())

total_play_time = ((48 - h) * (3 / 4)) + (p * (2 / 3)) + h

if year == "leap":
    total_play_time += (total_play_time * 0.15)
    print(f"{math.floor(total_play_time)}")
else:
    print(f"{math.floor(total_play_time)}")
