# # 01 solution using sorted(
def by_int(item):
    command_split = item.split('-')
    first = int(command_split[0])
    return first


to_do_list = []
striped_result = []
while True:
    command = input()
    if command == "End":
        break
    to_do_list.append(command)
result = sorted(to_do_list, key=by_int)
for note in result:
    striped_result.append(note.split("-")[1])
print(striped_result)
# # 02 solution NOT completed 80 / 100
# notes = [0] * 10
# while True:
#     command = input()
#     if command == "End":
#         break
#     tokens = command.split("-")
#     priority = tokens[0]
#     note = tokens[1]
#     notes.insert(int(priority), note)
# result = []
# for item in notes:
#     if not str(item).isdigit():
#         result.append(item)
# print(result)
# 2-Walk the dog
# 1-Drink coffee
# 6-Dinner
# 10-Work
# End
# # TEST
# 2-Walk the dog
# 1-Drink coffee
# 6-Dinner
# 10-Work
# 2-Walk the dog
# 1-Drink coffee
# 6-Dinner
# 2-Walk the dog
# 1-Drink coffee
# 6-Dinner
# 2-Walk the dog
# 1-Drink coffee
# 6-Dinner
# End