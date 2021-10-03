"""
4 5
1 5 5 2 4
2 1 4 14 3
3 7 11 2 8
4 8 12 16 4

Sum = 75
1 4 14
7 11 2
8 12 16
"""

rows, col = map(int, input().split(' '))
matrix = [[int(x) for x in input().split(' ')] for _ in range(rows)]
max_matrix = 0
final_result = []

for n in range(rows - 2):
    for m in range(col - 2):
        first_line = [matrix[n][m], matrix[n][m + 1], matrix[n][m + 2]]
        second_line = [matrix[n + 1][m], matrix[n + 1][m + 1], matrix[n + 1][m + 2]]
        third_line = [matrix[n + 2][m], matrix[n + 2][m + 1], matrix[n + 2][m + 2]]
        result = sum(first_line) + sum(second_line) + sum(third_line)

        if result >= max_matrix:
            max_matrix = result
            final_result = [result, first_line, second_line, third_line]

print(f'Sum = {final_result[0]}')
print(*final_result[1])
print(*final_result[2])
print(*final_result[3])
