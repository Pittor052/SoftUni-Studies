import re

line_input = input()

regex = r"\b(?P<day>\d{2})(?P<separator>[-.\/])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})\b"

result = re.finditer(regex, line_input)

for match in result:
    print(f"Day: {match.group('day')}, Month: {match.group('month')}, Year: {match.group('year')}")