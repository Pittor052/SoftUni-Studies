electrons = int(input())
result = []
count = 0
while not electrons <= 0:
    count += 1
    max_electrons = 2 * (count * count)
    if max_electrons > electrons:
        result.append(electrons)
        break
    else:
        result.append(max_electrons)
        electrons -= max_electrons

print(result)
