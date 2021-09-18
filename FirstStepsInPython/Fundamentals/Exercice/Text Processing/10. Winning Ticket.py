# # NOT SOLVED 30/100
ticket = input()
valid_symbols = ['@', '#', '$', '^']


for string in ticket.split(","):
    string = string.rstrip()
    string = string.lstrip()
    if len(string) == 20:
        left = string[:len(string) // 2]
        right = string[len(string) // 2:]
        if '@' in (left and right) or '#' in (left and right) or '$' in (left and right) or '^' in (left and right):
            left_symbol = ''
            right_symbol = ''
            for ch in range(len(left)):
                if left[ch] in valid_symbols:
                    left_symbol += left[ch]
                if right[ch] in valid_symbols:
                    right_symbol += right[ch]
            if not len(left_symbol) == len(right_symbol):
                print('invalid ticket')
                break
            max_count = max(left_symbol, right_symbol)
            min_count = min(left_symbol, right_symbol)

            if 6 <= len(min_count) < 10:
                print(f'ticket "{string}" - {len(min_count)}{min_count[0]}')
            elif len(max_count) == 10:
                print(f'ticket "{string}" - {len(max_count)}{max_count[0]} Jackpot!')
        else:
            print(f'ticket "{ticket}" - no match')
    else:
        print('invalid ticket')

# th@@@@@@eemo@@@@@@ey
