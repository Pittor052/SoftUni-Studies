numbers = list(map(int, input().split(", ")))
even_indices = []

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_indices.append(i)

print(even_indices)
# 3, 2, 1, 5, 8
