line_input = input()
result = ''
explosion = 0
i = 0
while i < len(line_input):

    if line_input[i] == ">":
        explosion += int(line_input[i + 1])
        result += ">"
    else:
        if explosion > 0:
            explosion -= 1
        else:
            result += line_input[i]
    i += 1
print(result)
# abv>1>1>2>2asdasd
# pesho>2sis>1a>2akarate>4hexmaster
