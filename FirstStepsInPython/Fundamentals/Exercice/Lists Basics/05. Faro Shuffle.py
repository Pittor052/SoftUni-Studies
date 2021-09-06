# # 01 solution 
line_input = input().split()
loop = int(input())
middle = int(len(line_input) / 2)

for _ in range(loop):
    left = line_input[:middle]
    right = line_input[middle:]
    shuffled = []
    for i in range(len(left)):
        shuffled.append(left[i])
        shuffled.append(right[i])
    line_input = shuffled
print(line_input)
# # INPUT 1
# a b c d e f g h
# 5
# # INPUT 2
# one two three four
# 3
# # INPUT END
