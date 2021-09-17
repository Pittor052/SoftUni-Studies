import re

regex = r'([w]{3}\.)([A-Za-z0-9]([\-\.a-z0-9])*)\.[a-z]+'
result = []
while True:
    text = input()
    if not text:
        break
    match = re.finditer(regex, text)
    for stuff in match:
        result.append(stuff.group())

print(*result, sep="\n")
