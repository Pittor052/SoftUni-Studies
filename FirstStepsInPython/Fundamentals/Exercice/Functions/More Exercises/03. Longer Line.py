import math


def longer_line(point1, point2, point3, point4):
    result1 = abs(point1[0]) + abs(point1[1]) + abs(point2[0]) + abs(point2[1])
    result2 = abs(point3[0]) + abs(point3[1]) + abs(point4[0]) + abs(point4[1])
    if result1 >= result2:
        if (abs(point1[0]) + abs(point1[1])) > (abs(point2[0]) + abs(point2[1])):
            return f"({point2[0]}, {point2[1]})({point1[0]}, {point1[1]})"
        else:
            return f"({point1[0]}, {point1[1]})({point2[0]}, {point2[1]})"
    else:
        if (abs(point3[0]) + abs(point3[1])) > (abs(point4[0]) + abs(point4[1])):
            return f"({point4[0]}, {point4[1]})({point3[0]}, {point3[1]})"
        else:
            return f"({point3[0]}, {point3[1]})({point4[0]}, {point4[1]})"


coordinates1 = []
coordinates2 = []
coordinates3 = []
coordinates4 = []
coordinates1.append(math.floor((float(input()))))
coordinates1.append(math.floor((float(input()))))
coordinates2.append(math.floor((float(input()))))
coordinates2.append(math.floor((float(input()))))
coordinates3.append(math.floor((float(input()))))
coordinates3.append(math.floor((float(input()))))
coordinates4.append(math.floor((float(input()))))
coordinates4.append(math.floor((float(input()))))

print(longer_line(coordinates1, coordinates2, coordinates3, coordinates4))
