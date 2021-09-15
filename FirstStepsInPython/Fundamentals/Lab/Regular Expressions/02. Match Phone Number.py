import re

line_input = input()

pattern = r"(\+359 2 \d{3} \d{4}\b)|(\+359-2-\d{3}-\d{4}\b)"

valid_phone_nums = re.finditer(pattern, line_input)
result = [item.group() for item in valid_phone_nums]
print(*result, sep=", ")