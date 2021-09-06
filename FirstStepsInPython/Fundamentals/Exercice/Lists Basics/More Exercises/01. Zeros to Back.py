line_input = input().split(", ")
x = line_input.count("0")
while True:
    found = False
    for i in range(len(line_input)):
        element = "0"
        for j in range(len(line_input)):
            if element == line_input[j]:
                line_input.remove(element)
                found = True
                break
        if found:
            break
    if not found:
        break
for i in range(x):
    line_input.append("0")
for i in range(len(line_input)):
    line_input[i] = int(line_input[i])
print(line_input)
# # INPUT 1
# 1, 0, 1, 2, 0, 1, 3
