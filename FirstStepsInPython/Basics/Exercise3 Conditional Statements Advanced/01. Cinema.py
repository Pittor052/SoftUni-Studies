screen_type = str(input())
roll = int(input())
column = int(input())

room_capacity = roll * column
total_price = 0

if screen_type == "Premiere":
    total_price = room_capacity * 12
    print(f"{total_price:.2f} leva")
elif screen_type == "Normal":
    total_price = room_capacity * 7.5
    print(f"{total_price:.2f} leva")
elif screen_type == "Discount":
    total_price = room_capacity * 5
    print(f"{total_price:.2f} leva")
