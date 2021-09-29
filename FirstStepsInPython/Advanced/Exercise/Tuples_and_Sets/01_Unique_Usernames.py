num_lines_input = int(input())
user_names = []
while num_lines_input > 0:
    user_names.append(input())
    num_lines_input -= 1

print(*{name for name in user_names}, sep='\n')
