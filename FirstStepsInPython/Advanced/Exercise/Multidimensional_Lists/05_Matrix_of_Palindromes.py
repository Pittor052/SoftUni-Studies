"""
4 6

aaa aba aca ada aea afa
bbb bcb bdb beb bfb bgb
ccc cdc cec cfc cgc chc
ddd ded dfd dgd dhd did

"""

rows, cols = map(int, input().split())
first_letter = 97
matrix = []
for n in range(rows):
    line_for_matrix = []
    for m in range(cols):
        line_for_matrix.append(chr(first_letter + n) + chr(first_letter + n + m) + chr(first_letter + n))
    matrix.append(line_for_matrix)
for idx in range(rows):
    print(*matrix[idx])
