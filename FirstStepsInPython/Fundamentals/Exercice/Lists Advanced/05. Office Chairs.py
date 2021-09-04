rooms = int(input())
count = 0
free_chairs = 0
no_chairs = False
for i in range(rooms):
    count += 1
    command = input().split()
    if len(command[0]) < int(command[1]):
        print(f"{int(command[1]) - len(command[0])} more chairs needed in room {count}")
        no_chairs = True
    else:
        free_chairs += len(command[0]) - int(command[1])
if not no_chairs:
    print(f"Game On, {free_chairs} free chairs left")
# # INPUT 1
# 4
# XXXX 4
# XX 1
# XXXXXX 3
# XXX 3