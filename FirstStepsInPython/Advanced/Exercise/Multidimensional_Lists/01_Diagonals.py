"""
3
1, 2, 3
4, 5, 6
7, 8, 9

Primary diagonal: 1, 5, 9. Sum: 15
Secondary diagonal: 3, 5, 7. Sum: 15
n = 0, rows - 1
n = 1, rows - 2
n = 2, rows - 3
"""
# # 01 solution
rows = int(input())
matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]
primary_diagonal = [matrix[x][x] for x in range(rows)]
secondary_diagonal = [matrix[x][rows - x - 1] for x in range(rows)]
print(f'Primary diagonal: {", ".join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}')
print(f'Secondary diagonal: {", ".join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}')

# # 02 solution
# rows = int(input())
# matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]
# primary_diagonal = []
# secondary_diagonal = []
# for x in range(rows):
#     primary_diagonal.append(matrix[x][x])
# for x in range(rows):
#     secondary_diagonal.append(matrix[x][rows - x - 1])
#
# print(f'Primary diagonal: {", ".join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}')
# print(f'Secondary diagonal: {", ".join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}')
