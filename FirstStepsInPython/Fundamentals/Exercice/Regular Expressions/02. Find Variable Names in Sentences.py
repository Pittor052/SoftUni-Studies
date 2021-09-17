import re

line_input = input()

print(*[item.group('name') for item in re.finditer(r"\b[_]{1}(?P<name>([A-Za-z]\d?)+)\b", line_input)], sep=",")
