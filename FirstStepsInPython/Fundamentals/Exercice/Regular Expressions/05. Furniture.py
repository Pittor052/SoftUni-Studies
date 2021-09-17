import re

text = input()
regex = r'>>(?P<item>[A-za-z]*)<<(?P<price>\d+[\.\d]*)!(?P<quantity>\d+)'
items = []
total_price = 0
while not text == "Purchase":

    result = re.finditer(regex, text)
    for stuff in result:
        items.append(stuff.group('item'))
        total_price += (float(stuff.group('price'))*float(stuff.group('quantity')))
    text = input()

print('Bought furniture:')
for item in items:
    print(item)
print(f'Total money spend: {total_price:.2f}')
