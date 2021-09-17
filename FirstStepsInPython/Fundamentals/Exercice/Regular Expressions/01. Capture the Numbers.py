import re

regex = r"\d+"
result = []
line_input = input()

while line_input:

    temp = re.findall(regex, line_input)

    for item in temp:
        result.append(item)

    line_input = input()

print(*result)