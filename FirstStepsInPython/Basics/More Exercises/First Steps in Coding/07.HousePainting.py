x = float(input())  # height of the house
y = float(input())  # width of the house
h = float(input())  # height of the side of the roof

door = 1.2 * 2
window = 1.5 * 1.5
front = (x * x) - door
back = x * x
side = (2 * (x * y)) - (2 * window)
triangle_roof = 2 * ((x * h) / 2)
rectangle_roof = 2 * (y * x)
paint_roof = (triangle_roof + rectangle_roof) / 4.3
paint_sides = (front + back + side) / 3.4
print(f"{paint_sides:.2f}")
print(f"{paint_roof:.2f}")
