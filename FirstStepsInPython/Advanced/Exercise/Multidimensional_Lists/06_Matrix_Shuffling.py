rows, cols = map(int, input().split())
matrix = [[x for x in input().split(' ')] for _ in range(rows)]

while True:
    command = input()
    if 'END' in command:
        break
    elif ('swap' not in command) or (not len(command.split()) == 5):
        print('Invalid input!')
        continue

    match = command.split()
    idx_1, idx_2, idx_3, idx_4 = [int(match[x]) for x in range(1, 5)]
    if (0 <= idx_1 < rows) and (0 <= idx_2 < cols) and (0 <= idx_3 < rows) and (0 <= idx_4 < cols):
        matrix[idx_1][idx_2], matrix[idx_3][idx_4] = matrix[idx_3][idx_4], matrix[idx_1][idx_2]
        for r in range(rows):
            print(*matrix[r])
    else:
        print('Invalid input!')
        continue
