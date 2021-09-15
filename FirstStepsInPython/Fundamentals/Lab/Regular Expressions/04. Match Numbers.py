import re

line_input = input()

regex = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))($|(?=\s))"

result = re.finditer(regex, line_input)

final = [item.group() for item in result]

print(*final)
# H|h?ow
# \s?H|h?ow(|!|.|,)?
# TEST ^T|t?here\W
