line_input = input()
i = 0
test = ''
result = ''

while i < len(line_input):

    if not line_input[i].isdigit():
        test += line_input[i].upper()
    else:
        if (not i == len(line_input) - 1) and (line_input[i + 1].isdigit()):
            num = line_input[i] + line_input[i + 1]
            test *= int(num)
            result += test
            test = ''
            i += 1
        else:
            test *= int(line_input[i])
            result += test
            test = ''

    i += 1

print(f"Unique symbols used: {len(set(result))}")
print(result)

# a3a3
# aSd2&10s@1
