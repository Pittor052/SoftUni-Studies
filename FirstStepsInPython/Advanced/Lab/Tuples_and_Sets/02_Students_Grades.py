from collections import deque

# format: "{student's name} -> {grade1} {grade2} ... {gradeN} (avg: {average_grade})"

num_students = int(input())
students = {}

while num_students > 0:
    line_input = deque(input().split())
    name = line_input.popleft()

    if name not in students.keys():
        students[name] = []

    while line_input:
        students[name].append(float(line_input.popleft()))

    num_students -= 1

for name, grades in students.items():
    # grade = [' '.join(format(x, '.2f') for (x) in grades)]
    print(f"{name} -> {' '.join(format(x, '.2f') for (x) in grades)} (avg: {sum(grades) / len(grades):.2f})")

# 7
# Peter 5.20
# Mark 5.50
# Peter 3.20
# Mark 2.50
# Alex 2.00
# Mark 3.46
# Alex 3.00
