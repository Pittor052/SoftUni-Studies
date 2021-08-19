from math import pi

figure = input()
a = str("square")
b = str("rectangle")
c = str("circle")
d = str("triangle")

if figure == a:

    side = float(input())
    print(side * side)

elif figure == b:

    side_a = float(input())
    side_b = float(input())
    print(side_a * side_b)

elif figure == c:

    rad = float(input())
    print(pi * rad * rad)

elif figure == d:

    side_a = float(input())
    side_b = float(input())
    print((side_a * side_b) / 2)
