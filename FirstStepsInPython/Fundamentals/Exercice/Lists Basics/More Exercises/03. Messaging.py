# # 01 solution NOPE
num = input().split(" ")
line_input = input()
message = ""

for i in num:
    s = 0
    test = list(i)
    for j in test:
        s += int(j)
    if s > len(line_input):
        for j in range(1, 2):
            message += line_input[j]
            char = line_input[j]
            for k in range(len(line_input)):
                if line_input[k] == char:
                    line_input = line_input[:k] + line_input[k + 1:]
                    break
    else:
        message += line_input[s]
        char = line_input[s]
        line_input = line_input[:s] + line_input[s + 1:]

print(message)

# # INPUT 1
# 9992 562 8933
# This is some message for you
# # INPUT END
