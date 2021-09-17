to_remove = input()
line_input = input()

while to_remove in line_input:
    line_input = line_input.replace(to_remove, "")
print(line_input)
