"""
3, 6
7, 1, 3, 3, 2, 1
1, 3, 9, 8, 5, 6
4, 6, 7, 9, 1, 0
"""
# # 01 solution
# n_rows, m_column = [int(x) for x in input().split(', ')]
# matrix = [[int(y) for y in input().split(', ')] for x in range(n_rows)]
# print(sum(sum(row) for row in matrix))
# print(matrix)

# # 02 solution
n_rows, m_column = [int(x) for x in input().split(', ')]
matrix = []

for row in range(n_rows):
    lines = [int(x) for x in input().split(", ")]
    matrix.append(lines)

print(sum(sum(row) for row in matrix))
print(matrix)