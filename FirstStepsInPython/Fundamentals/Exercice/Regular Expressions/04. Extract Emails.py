import re

text = input()
regex = r'\s(?P<mail>[A-Za-z0-9]+[A-Za-z0-9\-\.\_]*\@[A-Za-z]+[A-Za-z\-]*(\.[A-Za-z]+)+)\b'
print(*[match.group('mail') for match in re.finditer(regex, text)], sep="\n")
