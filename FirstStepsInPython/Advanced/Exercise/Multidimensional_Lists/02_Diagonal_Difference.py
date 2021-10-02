"""
3
11 2 4
4 5 6
10 8 -12
"""
rows = int(input())
matrix = [[int(x) for x in input().split(' ')] for _ in range(rows)]
primary_diagonal = [matrix[x][x] for x in range(rows)]
secondary_diagonal = [matrix[x][rows - x - 1] for x in range(rows)]
print(f'{abs(sum(primary_diagonal) - sum(secondary_diagonal))}')
