"""
3, 6
7, 1, 3, 3, 2, 1
1, 3, 9, 8, 5, 6
4, 6, 7, 9, 1, 0

[
[7, 1, 3, 3, 2, 1], 
[1, 3, 9, 8, 5, 6], 
[4, 6, 7, 9, 1, 0]
]

[
[0 0, 0 1]
[1 0, 1 1]
[0 1, 0 2]
[1 1, 1,2]
]
"""

rows, col = map(int, input().split(', '))
matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]
result_matrix = []
result_sum = 0
m_cols = 2
while True:
    matrix_crop = []
    for n in range(rows):
        for m in range(m_cols):




