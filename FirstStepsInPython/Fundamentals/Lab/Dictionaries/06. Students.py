# # Updating existing element(s) in a dictionary: https://www.guru99.com/python-dictionary-append.html#6
# # Nested Dictionary: https://www.programiz.com/python-programming/nested-dictionary
# # Printing nested dictionaries line by line:
# https://thispointer.com/python-4-ways-to-print-items-of-a-dictionary-line-by-line/
# TASK:
# You will be receiving names of students, their ID and a course of programming they have taken in the format
#   "{name}:{ID}:{course}".
# On the last line you will receive a name of a course in snake case lowercase letters.
# You should print only the information of the students taken the corresponding course in the format:
#   "{name} - {ID}" on separate lines.
# Note: each student's ID will always be unique
line_input = input()
students = {}
while ":" in line_input:
    line_input = line_input.split(":")
    if " " in line_input[2]:
        line_input[2] = line_input[2].replace(" ", "_")
    name = line_input[0]
    num = line_input[1]
    if line_input[2] not in students:
        students[line_input[2]] = {name: num}
    else:
        students[line_input[2]].update({name: num})

    line_input = input()

for course, data in students.items():
    if course == line_input:
        for name, num in data.items():
            print(f"{name} - {num}")
# # INPUT 0
# Peter:123:programming basics
# John:5622:fundamentals
# Maya:89:fundamentals
# Lilly:633:fundamentals
# fundamentals
#
# # OUTPUT 0
# John - 5622
# Maya - 89
# Lilly - 633
#
# # INPUT 1
# Alex:6:programming basics
# Maria:7:programming basics
# Kaloyan:9:advanced
# Todor:10:fundamentals
# programming_basics
#
# # OUTPUT 1
# Alex - 6
# Maria - 7
