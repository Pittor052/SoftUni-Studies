"""
3
ABC
DEF
X!@
!
"""

num_rows = int(input())
matrix = [[s for s in input()] for n in range(num_rows)]
look_for = input()
found = False
for n in range(num_rows):
    for m in range(len(matrix[n])):
        result = 0
        this = matrix[n][m]
        if look_for == this:
            print(f'({n}, {m})')
            found = True
        if found:
            break
if not found:
    print(f'{look_for} does not occur in the matrix')

