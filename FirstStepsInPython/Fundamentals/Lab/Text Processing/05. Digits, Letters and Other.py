line_input = input()
nums = ""
letters = ""
chars = ""

for char in line_input:

    if char.isdigit():
        nums += char

    elif char.isalpha():
        letters += char

    else:
        chars += char

print(*(nums, letters, chars), sep="\n")
