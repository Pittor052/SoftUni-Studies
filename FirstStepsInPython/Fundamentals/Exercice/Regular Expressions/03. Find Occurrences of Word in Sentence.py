import re

text, word = input().lower(), input().lower()

print(len([item.group() for item in re.finditer('\\b'+word+'\\b', text)]))
