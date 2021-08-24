# workspace dimensions width = 120 / height = 70
import math

width = float(input()) * 100    # conversion from metres to centimeters
height = float(input()) * 100   # conversion from metres to centimeters

desks_width = math.floor(width / 120)               # number of desks on width
desks_height = math.floor((height - 100) / 70)      # number of desks on height


number_of_desks = (desks_width * desks_height) - 3
# number of desks in the grid minus corridor and 3 desks for door and podium

print(f'{number_of_desks}')
