# # 01 solution using pop(), insert() nad append()
train_composition = [0] * int(input())
command = input().split()
while not command[0] == "End":
    if command[0] == "add":
        add_passengers = train_composition.pop(len(train_composition) - 1) + int(command[1])
        train_composition.append(add_passengers)
    elif command[0] == "insert":
        insert_passengers_in_wagon = train_composition.pop(int(command[1])) + int(command[2])
        train_composition.insert(int(command[1]), insert_passengers_in_wagon)
    elif command[0] == "leave":
        remaining_passengers_in_wagon = train_composition.pop(int(command[1])) - int(command[2])
        train_composition.insert(int(command[1]), remaining_passengers_in_wagon)
    command = input().split()
print(train_composition)

# # 02 solution optimized
# train_composition = [0] * int(input())
# command = input().split()
# while not command[0] == "End":
#     act = command[0]
#     if act == "add":
#         train_composition[-1] += int(command[1])
#     elif act == "insert":
#         train_composition[int(command[1])] += int(command[2])
#     elif act == "leave":
#         train_composition[int(command[1])] -= int(command[2])
#     command = input().split()
# print(train_composition)
# # INPUT 1
# 3
# add 20
# insert 0 15
# leave 0 5
# End
# # OUTPUT 1
# # [10, 0, 20]
