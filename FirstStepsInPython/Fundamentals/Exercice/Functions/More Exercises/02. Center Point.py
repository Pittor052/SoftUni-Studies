import math

# 01 solution using lists
coordinates1 = []
coordinates2 = []
coordinates1.append((float(input())))
coordinates1.append((float(input())))
coordinates2.append((float(input())))
coordinates2.append((float(input())))

if abs(float(coordinates1[1])) <= abs(float(coordinates2[1])):
    print(f"({math.floor(coordinates1[0])}, {math.floor(coordinates1[1])})")
else:
    print(f"({math.floor(coordinates2[0])}, {math.floor(coordinates2[1])})")
#
# # 02 solution using function
# def closer_to_center(num1, num2):
#     if abs(num1) <= abs(num2):
#         return True
#
#
# x1 = (float(input()))
# x2 = (float(input()))
# x3 = (float(input()))
# x4 = (float(input()))
# if closer_to_center(x2, x4):
#     print(f"({math.floor(x1)}, {math.floor(x2)})")
# else:
#     print(f"({math.floor(x3)}, {math.floor(x4)})")
#
# # 03 solution basic
# x1 = (float(input()))
# x2 = (float(input()))
# x3 = (float(input()))
# x4 = (float(input()))
#
# if abs(x2) <= abs(x4):
#     print(f"({math.floor(x1)}, {math.floor(x2)})")
# else:
#     print(f"({math.floor(x3)}, {math.floor(x4)})")
