# Write a program that keeps information about students and their grades.
# You will receive n pair of rows. First you will receive the student's name,
# after that you will receive his grade. Check if the student already exists and if not, add him.
# Keep track of all grades for each student.
# When you finish reading the data, keep the students with average grade higher than or equal to 4.50.
# Order the filtered students by average grade in descending order.
# Print the students and their average grade in the following format:
#   {name} -> {averageGrade}
# Format the average grade to the 2nd decimal place.

n = int(input())
data = {}

while not n == 0:
    name = input()
    grade = float(input())
    if name not in data:
        data[name] = [grade]
    else:
        data[name].append(grade)
    n -= 1

for name, grades in data.items():
    data[name] = sum(grades) / len(grades)

data = dict((y, x) for x, y in data.items())

for grade, student in sorted(data.items(), reverse=True):
    if grade >= 4.50:
        print(f"{student} -> {grade:.2f}")
# # Input 0
# 5
# John
# 5.5
# John
# 4.5
# Alice
# 6
# Alice
# 3
# George
# 5
#
# # Output 0
# John -> 5.00
# George -> 5.00
# Alice -> 4.50
