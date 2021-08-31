# Write a program that keeps information about courses. Each course has a name and registered students.
# You will be receiving a course name and a student name, until you receive the command "end".
# Check if such course already exists, and if not, add the course. Register the user into the course.
# When you receive the command "end", print the courses with their names and total registered users,
# ordered by the count of registered users in descending order.
# For each contest print the registered users ordered by name in ascending order.
# Input
#   Until the "end" command is received, you will be receiving input in the format: "{courseName} : {studentName}".
#   The product data is always delimited by " : ".
# Output
#   Print the information about each course in the following the format:
#       "{courseName}: {registeredStudents}"
#   Print the information about each student, in the following the format:
#       "-- {studentName}"

line_input = input()
library = {}

while not line_input == "end":
    course, student = line_input.split(" : ")

    if course not in library:
        library[course] = [student]
    else:
        library[course].append(student)
    line_input = input()

for course_name, item2 in sorted(library.items(), key=lambda r: -len(r[1])):
    print(f"{course_name}: {len(item2)}")
    for students in sorted(item2):
        print(f"-- {students}")

# # INPUT 0
# Programming Fundamentals : John Smith
# Programming Fundamentals : Linda Johnson
# JS Core : Will Wilson
# Java Advanced : Harrison White
# end
#
# # OUTPUT 0
# Programming Fundamentals: 2
# -- John Smith
# -- Linda Johnson
# JS Core: 1
# -- Will Wilson
# Java Advanced: 1
# -- Harrison White
# # INPUT 1
# Algorithms : Jay Moore
# Programming Basics : Martin Taylor
# Python Fundamentals : John Anderson
# Python Fundamentals : Andrew Robinson
# Algorithms : Bob Jackson
# Python Fundamentals : Clark Lewis
# end
#
# # OUTPUT 1
# Python Fundamentals: 3
# -- Andrew Robinson
# -- Clark Lewis
# -- John Anderson
# Algorithms: 2
# -- Bob Jackson
# -- Jay Moore
# Programming Basics: 1
# -- Martin Taylor