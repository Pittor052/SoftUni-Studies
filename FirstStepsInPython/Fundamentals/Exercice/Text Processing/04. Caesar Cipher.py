line_input1 = input()
result = ''

for ch in range(len(line_input1)):

    result += chr(ord(line_input1[ch]) + 3)

print(result)