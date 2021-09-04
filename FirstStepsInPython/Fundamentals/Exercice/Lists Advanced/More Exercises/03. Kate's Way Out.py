# # 01 solution incomplete: depending on the initial position of Kate she must go up or down or left or right!
rows = int(input())
maze = []
moves = 0
top = 0
bottom = 0
initial_position = 0
initial_row = 0
left = False
right = False
side_exit = False
start_top = 0
stop_bottom = 0
move_side = 0
for i in range(rows):
    maze.append(input())
for row in range(len(maze)):
    for place in range(len(maze[row])):
        if maze[row][place] == 'k':
            initial_position = place
            initial_row = row
            break
    if (not initial_position == 0) and (not initial_row == 0):
        break
for test_row2 in range((len(maze) - 1), initial_row, -1):
    if maze[test_row2] == "######":
        bottom += test_row2
        stop_bottom = test_row2
for row in range(initial_row):
    if maze[row] == "######":
        top += 1
        start_top = row
for row in range(len(maze) - 1):
    if maze[row][0] == " " or maze[row][5] == " ":
        side_exit = True
if top > 0 and bottom > 0 and not side_exit:  # no exit
    print("Kate cannot get out")
elif top == 0 and not side_exit:  # calculate moves to top
    for place in range(stop_bottom, 1, -1):
        if place < 5 - 1 and not maze[place] == maze[place - 1][place + 1]:
            moves += 1
    for j in range(initial_row + 1):
        if j < initial_row - 1 and (not maze[j].count(" ") > maze[j + 1].count(" ")):
            moves += maze[j].count(" ") - maze[j + 1].count(" ")
        else:
            moves += maze[j].count(" ")
    print(f'Kate got out in {moves + 1} moves')
elif bottom == 0 and not side_exit:  # calculate moves to bottom
    for place in range(start_top, rows - 1):
        if place < 5 - 1 and not maze[place] == maze[place + 1][place + 1]:
            moves += 1
    for j in range(initial_row + 1):
        if j < initial_row - 1 and (not maze[j].count(" ") > maze[j + 1].count(" ")):
            moves += maze[j].count(" ") - maze[j + 1].count(" ")
        else:
            moves += maze[j].count(" ")
    print(f'Kate got out in {moves} moves')
elif (top > 0) and (bottom > 0) and side_exit:
    for i in range(start_top, stop_bottom + 1):  # calculate moves to side
        move_side += maze[i].count(" ")
    print(f'Kate got out in {move_side} moves')
# # INPUT 1
# 4
# ######
# #   k#
# ## ###
# ## ###
# # OUTPUT 1
# Kate got out in 5 moves
# # INPUT 2
# 5
# ######
# ##  k#
# ## ###
# ######
# ## ###
# # OUTPUT 2
# Kate cannot get out
# # TEST
# 5
# ######
# ##k###
# ## ###
# ##
# ######
# # TEST
# 5
# ## ###
# ## ###
# ## ###
# ##k###
# ######
#
# rows = int(input())
# maze = []
# for i in range(rows):
#     maze.append(input())
# moves = 0
# here = 0
# no_exit = False
# count = 1
# next_row = []
# position = 0
# initial_row = []
# for row in range(len(maze)):
#     for place in range(len(maze[row])):
#         if maze[row][place] == 'k':
#             position = place
#             initial_row = row
#             break
#     if not position == 0 and not initial_row == 0:
#         break
# # if initial_row == (rows - 2):
# #     maze.reverse()
# while True:
#     while True:
#         if maze[count] == "######":
#             count += 1
#         else:
#             break
#     maze_row = maze[count]
#     if not count == rows - 1:
#         next_row = list(maze[count + 1])
#     else:
#         break
#     for k in range(6, 0, -1):
#         if maze_row[k - 1] == " " and next_row[k - 1] == "#":
#             moves += 1
#             position = k - 1
#     if position == 5 or position == 0:
#         print(f'Kate got out in {moves} moves')
#         no_exit = True
#         break
#     if not next_row[position] == "#":
#         initial_position = here
#         moves += 1
#     else:
#         print("Kate cannot get out")
#         no_exit = True
#         break
#     count += 1
#
# if not no_exit:
#     print(f"Kate got out in {moves} moves")

#
# # 02 solution Иван_Георгиев
# n = int(input())
# maze = []
# for _ in range(n):
#     maze.append(list(input()))
# initial_position = []
# for row in range(len(maze)):  # finding the initial position of Kate
#     for place in range(len(maze[row])):
#         if maze[row][place] == 'k':
#             initial_position = [row, place]
#             break
#     if len(initial_position) == 2:
#         break
# position = initial_position
# previous_positions = []
# while True:
#     row = position[0]
#     place = position[1]
#     if maze[row][place] == '#':
#         print('Kate cannot get out')
#         break
#     if maze[row][place + 1] == ' ' and not [row, place + 1] in previous_positions:  # scan left
#         position = [row, place + 1]
#         previous_positions.append([row, place])
#     elif maze[row][place - 1] == ' ' and not [row, place - 1] in previous_positions:  # scan right
#         position = [row, place - 1]
#         previous_positions.append([row, place])
#     elif maze[row - 1][place] == ' ' and not [row - 1, place] in previous_positions:  # scan up
#         position = [row - 1, place]
#         previous_positions.append([row, place])
#     elif maze[row + 1][place] == ' ' and not [row + 1, place] in previous_positions:  # scan down
#         position = [row + 1, place]
#         previous_positions.append([row, place])
#     else:
#         maze[row][place] = '#'
#         previous_positions = []
#         position = initial_position
#
#     if position[0] == len(maze) - 1 or position[0] == 0 or position[1] == 0 or position[1] == len(maze[row]) - 1:
#         print(f'Kate got out in {len(previous_positions) + 1} moves')
#         break
# # 03 solution Радослав Георгиев
# rows = int(input())
# matrix = [list(input()) for i in range(rows)]
# k_row = sum([r for r in range(rows) if "k" in matrix[r]])
# k_col = sum([c for c in range(len(matrix[k_row])) if "k" == matrix[k_row][c]])
#
# r = k_row
# c = k_col
# visited_positions = [[k_row, k_col]]
# moves = 0
#
# while True:
#     moves += 1
#     if matrix[r][c + 1] == " " and c + 1 < len(matrix[r]) and not [r, c + 1] in visited_positions:
#         matrix[r][c], matrix[r][c + 1] = matrix[r][c + 1], matrix[r][c]
#         c += 1
#         visited_positions.append([r, c])
#     elif matrix[r][c - 1] == " " and c - 1 >= 0 and not [r, c - 1] in visited_positions:
#         matrix[r][c], matrix[r][c - 1] = matrix[r][c - 1], matrix[r][c]
#         c -= 1
#         visited_positions.append([r, c])
#     elif matrix[r - 1][c] == " " and r - 1 >= 0 and not [r - 1, c] in visited_positions:
#         matrix[r][c], matrix[r - 1][c] = matrix[r - 1][c], matrix[r][c]
#         r -= 1
#         visited_positions.append([r, c])
#     elif matrix[r + 1][c] == " " and r + 1 < rows and not [r + 1, c] in visited_positions:
#         matrix[r][c], matrix[r + 1][c] = matrix[r + 1][c], matrix[r][c]
#         r += 1
#         visited_positions.append([r, c])
#     else:
#         moves = 0
#         matrix[r][c] = "#"
#         r = k_row
#         c = k_col
#         matrix[r][c] = "k"
#         visited_positions = [[k_row, k_col]]
#     if r == 0 or r == rows - 1 or c == 0 or c == len(matrix[0]) - 1:
#         moves += 1
#         print(f"Kate got out in {moves} moves")
#         break
#     elif matrix[r][c + 1] == "#" and matrix[r][c - 1] == "#" and matrix[r - 1][c] == "#" and matrix[r + 1][c] == "#":
#         print("Kate cannot get out")
#         break
