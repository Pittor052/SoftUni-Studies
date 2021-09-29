num_lines_input = int(input())
found = set()
while num_lines_input:
    ranges = input().split('-')
    start = int(ranges[0].split(',')[0])
    stop = int(ranges[1].split(',')[1]) + 1
    result = set(range(start, stop))
    if len(result) > len(found):
        found = result.copy()
    num_lines_input -= 1

print(f'Longest intersection is [{", ".join(str(x) for x in found)}] with length {len(found)}')

# 3
# 0,3-1,2
# 2,10-3,5
# 6,15-3,10

# # TEST
# 1
# 1,3-3,4
