# 01 solution. The underscore is also used for ignoring the specific values. If you don’t need the specific values
# or the values are not used, just assign the values to underscore.
lines = int(input())
courses = []
for _ in range(lines):
    courses.append(input())
print(courses)
