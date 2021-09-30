"""
2
1, 2, 3
4, 5, 6
"""
# 01 solution
n = int(input())
matrix = [map(int, input().split(', ')) for _ in range(n)]
print([num for row in matrix for num in row])
