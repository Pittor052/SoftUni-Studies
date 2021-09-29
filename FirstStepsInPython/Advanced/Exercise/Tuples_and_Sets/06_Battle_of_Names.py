num_of_inputs = int(input())
odd, even = [], []

for num in range(1, num_of_inputs + 1):
    name = int(sum(ord(letter) for letter in input()) / num)
    if name % 2 == 0:
        even.append(name)
    else:
        odd.append(name)
odd = {x for x in odd}
even = {x for x in even}

if sum(odd) == sum(even):
    print(*odd.union(even), sep=", ")
elif sum(odd) > sum(even):
    result = odd.difference(even)
    print(*result, sep=", ")
else:
    result = even.symmetric_difference(odd)
    print(*result, sep=", ")

# 4
# Pesho
# Stefan
# Stamat
# Gosho