# # INCOMPLETE !!!
import re

racers = input().split(', ')
line = input()
races = []
regex = r'(?P<name>([A-Za-z])+)'
regex2 = r'(?P<length>.*)'
compare_race = {}

while not line == 'end of race':
    races.append(line)
    line = input()

for race in races:
    distance = len(race)
    result = re.finditer(regex, race)
    test = ''
    for name in result:

        if name.group('name') not in compare_race:
            compare_race[name.group('name')] = distance
        else:
            if distance > compare_race[name.group('name')]:
                compare_race[name.group()] += distance

print(racers)
print(compare_race)
print(races)
