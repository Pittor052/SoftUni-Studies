from math import floor
record_seconds = float(input())
distance_metres = float(input())
swim_seconds = float(input())

swim_time = distance_metres * swim_seconds
drag_time = floor(distance_metres / 15) * 12.5
swim_time += drag_time

if record_seconds > swim_time:
    print(f"Yes, he succeeded! The new world record is {swim_time:.2f} seconds.")
else:
    seconds_needed = swim_time - record_seconds
    print(f"No, he failed! He was {seconds_needed:.2f} seconds slower.")
