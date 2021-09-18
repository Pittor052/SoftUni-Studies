line_input1, line_input2 = sorted(input().split(), key=lambda x: -len(x))
result = 0

for ch in range(len(line_input1)):
    if ch < len(line_input2):
        result += (ord(line_input1[ch]) * ord(line_input2[ch]))
    else:
        result += ord(line_input1[ch])

print(result)
