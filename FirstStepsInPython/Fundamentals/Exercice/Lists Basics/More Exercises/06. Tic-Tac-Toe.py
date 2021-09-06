line1_input = input().split()
line2_input = input().split()
line3_input = input().split()
winner = 0
found = False
while not found:
    if line1_input[0] == line2_input[0] == line3_input[0] != 0:  # 714
        winner = line1_input[0]
        found = True
    elif line1_input[1] == line2_input[1] == line3_input[1] != 0:  # 852
        winner = line1_input[1]
        found = True
        break
    elif line1_input[2] == line2_input[2] == line3_input[2] != 0:  # 963
        winner = line1_input[2]
        found = True
        break
    elif line1_input[0] == line1_input[1] == line1_input[2] != 0:  # 789
        winner = line1_input[0]
        found = True
        break
    elif line2_input[0] == line2_input[1] == line2_input[2] != 0:  # 456
        winner = line2_input[0]
        found = True
        break
    elif line3_input[0] == line3_input[1] == line3_input[2] != 0:  # 123
        winner = line3_input[0]
        found = True
        break
    elif line1_input[0] == line2_input[1] == line3_input[2] != 0:  # 753
        winner = line1_input[0]
        found = True
        break
    elif line1_input[2] == line2_input[1] == line3_input[0] != 0:  # 951
        winner = line1_input[2]
        found = True
        break
    found = True
if int(winner) == 0:
    print("Draw!")
elif int(winner) == 1:
    print("First player won")
else:
    print("Second player won")
# # INPUT 1
# 2 0 1
# 0 1 0
# 1 0 2
# # INPUT 2
# 0 1 0
# 2 2 2
# 1 0 0
# # INPUT 3
# 1 0 2
# 0 1 2
# 1 2 0
# # INPUT 4
# 0 1 0
# 2 2 2
# 1 0 0
# # INPUT END