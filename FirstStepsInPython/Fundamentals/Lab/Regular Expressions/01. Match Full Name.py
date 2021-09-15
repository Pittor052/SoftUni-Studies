import re

line_input = input()
pattern = r"\b[A-Z]{1}[a-z]+ [A-Z]{1}[a-z]+\b"

valid_names = re.findall(pattern, line_input)

print(*valid_names)