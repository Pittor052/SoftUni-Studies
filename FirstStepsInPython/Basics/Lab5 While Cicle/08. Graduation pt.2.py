name = input()
year = 1
sum_grades = 0.0
repeat = 0

while year <= 12:
    grade = float(input())
    if grade < 4:
        repeat += 1
        if repeat > 1:
            print(f"{name} has been excluded at {year} grade")
            break
        else:
            continue
    sum_grades += grade
    year += 1

average = sum_grades / 12

if average >= 4 and repeat < 2:
    print(f"{name} graduated. Average grade: {average:.2f}")

# решение без принт в цикъл!
# Solution by Sichanov Dimitur
# name = input()
# year = 1
# sum_grades = 0.0
# repeat = 0
# is_expelled = False
# while year <= 12:
#     grade = float(input())
#     if grade < 4:
#         repeat += 1
#         if repeat > 1:
#             is_expelled = True
#             break
#         continue
#     sum_grades += grade
#     year += 1
# if is_expelled:
#     print(f"{name} has been excluded at {year} grade")
# else:
#     average = sum_grades / 12
#     print(f"{name} graduated. Average grade: {average:.2f}")

# input for check

# Gosho
# 5
# 5.5
# 6
# 5.43
# 5.5
# 6
# 5.55
# 5
# 6
# 6
# 5.43
# 5

# Mimi
# 5
# 6
# 5
# 6
# 5
# 6
# 6
# 2
# 3

# Mimi
# 5
# 6
# 5
# 6
# 5
# 6
# 6
# 2
# 5
# 5
# 5
# 5
# 5

# Mimi
# 6
# 6
# 6
# 6
# 6
# 6
# 6
# 6
# 6
# 6
# 2
# 2

