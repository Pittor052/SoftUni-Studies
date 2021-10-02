"""
3 4
A B B D
E B B B
I J B B
"""
rows, cols = [int(x) for x in input().split()]
matrix = [[x for x in input().split(' ')] for _ in range(rows)]
final_result = []

for n in range(rows - 1):
    for m in range(cols - 1):
        result = [matrix[n][m],
                  matrix[n][m + 1],
                  matrix[n + 1][m],
                  matrix[n + 1][m + 1]]
        if matrix[n][m] == matrix[n][m + 1] == matrix[n + 1][m] == matrix[n + 1][m + 1]:
            final_result.append([result])
print(len(final_result))