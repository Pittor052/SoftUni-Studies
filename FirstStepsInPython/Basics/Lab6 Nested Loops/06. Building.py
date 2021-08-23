floors = int(input())
rooms_per_floor = int(input())
large = "L{0}{1}"
apartment = "A{0}{1}"
office = "O{0}{1}"
for i in range(floors, 0, -1):
    for j in range(0, rooms_per_floor):
        if i == floors:
            print(large.format(i, j), end=" ")
        elif i % 2:
            print(apartment.format(i, j), end=" ")
        elif i % 2 == 0:
            print(office.format(i, j), end=" ")
    print("")
