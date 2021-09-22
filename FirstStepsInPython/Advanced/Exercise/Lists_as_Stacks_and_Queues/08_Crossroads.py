from collections import deque

green_light = int(input())
yellow_light = int(input())
cars_line = deque()
count_cars = 0
crash = False
output = []
text_input = input()

while 'END' not in text_input:
    if 'green' in text_input:
        seconds_remaining = 0
        count_green = 0
        count_yellow = 0

        if cars_line:
            current_car = cars_line[0]
            car = deque(cars_line.popleft())
            count_cars += 1

            for _ in range(green_light):
                if not car:
                    break
                car.popleft()
                count_green += 1

            if car:
                for _ in range(yellow_light):
                    if not car:
                        seconds_remaining = 0
                        break
                    car.popleft()
                if car:
                    seconds_remaining = 0
                    crash = True
                    output.append('A crash happened!')
                    output.append(f'{current_car} was hit at {car.popleft()}.')
            else:
                seconds_remaining = green_light - count_green

                while seconds_remaining > 0:
                    count_seconds = 0

                    if not car and cars_line:
                        current_car = cars_line[0]
                        car = deque(cars_line.popleft())
                        count_cars += 1
                    for _ in range((yellow_light + seconds_remaining)):
                        if not car:
                            seconds_remaining -= abs(count_seconds)
                            break
                        car.popleft()
                        count_seconds -= 1
                    if car:
                        seconds_remaining = 0
                        crash = True
                        output.append('A crash happened!')
                        output.append(f'{current_car} was hit at {car.popleft()}.')
                    if not cars_line:
                        break
    else:
        cars_line.append(text_input)
    if crash:
        break
    text_input = input()

if not crash:
    print('Everyone is safe.')
    print(f'{count_cars} total cars passed the crossroads.')
else:
    print()
    print(*output, sep='\n')

# #
# 10
# 5
# Merce0es
# green
# Merce1es
# BMW
# Skoda
# green
# END
# #
# 20
# 11
# Merce0es
# green
# Merce1es
# BMW
# Skoda
# opel
# green
# END

# #
# 9
# 3
# Mercedes
# Hummer
# green
# Hummer
# Mercedes
# green
# END