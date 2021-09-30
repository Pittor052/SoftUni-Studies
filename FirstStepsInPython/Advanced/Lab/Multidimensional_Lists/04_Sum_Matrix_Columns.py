"""
3, 6
7 1 3 3 2 1
1 3 9 8 5 6
4 6 7 9 1 0
"""
row, columns = map(int, input().split(', '))
matrix = [[int(x) for x in input().split()] for num in range(row)]
for m in range(columns):
    result = 0
    for n in range(row):
        result += matrix[n][m]
    print(result)
