line_input1 = input()

for ch in range(len(line_input1)):
    if line_input1[ch] == ":":
        print(line_input1[ch] + line_input1[ch + 1])


