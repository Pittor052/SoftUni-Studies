line_input = input().split()
total_sum = 0

for string in line_input:
    result = 0
    first_ch, last_ch = string[0], string[-1]
    number = int(string[1: len(string) - 1])

    if first_ch.isupper():
        ch = ord(first_ch) - 64
        result += (number / ch)

    if first_ch.islower():
        ch = ord(first_ch.upper()) - 64
        result += (number * ch)

    number = result
    result = 0

    if last_ch.isupper():
        ch = ord(last_ch) - 64
        result += (number - ch)

    if last_ch.islower():
        ch = ord(last_ch.upper()) - 64
        result += (number + ch)

    total_sum += result

print(f'{total_sum:.2f}')
