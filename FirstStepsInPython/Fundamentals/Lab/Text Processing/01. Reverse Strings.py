# while True:
#     command = input()
#     result = ""
#
#     if "end" in command:
#         break
#
#     for i in range(len(command) - 1, -1, -1):
#         result += command[i]
#
#     print(f"{command} = {result}")

command = input()
while not command == "end":
    print(f"{command} = {command[::-1]}")
    command = input()

# helLo
# Softuni
# bottle
# end
