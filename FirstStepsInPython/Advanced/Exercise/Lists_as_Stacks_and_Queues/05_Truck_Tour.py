pumps = int(input())
road = []
count = 0
while not count == pumps:
    road.append(list(map(lambda x: int(x), input().split())))
    count += 1
count = 0
index = 0
stop = False
while True:
    fuel = 0
    for pump in road:
        fuel += pump[0]
        if fuel - (pump[1]) >= 0:
            fuel -= pump[1]
            count += 1
            if count == pumps:
                stop = True
                break
        else:
            road.append(road.pop(0))
            index += 1
            count = 0
            break
    if stop:
        break
print(index)