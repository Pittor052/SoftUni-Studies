# # 01 solution using bytearray() method returns a bytearray object (i.e. array of bytes) which is mutable
# # (can be modified) sequence of integers in the range 0 <= x < 256. Converts the string to bytes using str.encode()
# # Must also provide encoding and optionally errors
lines = int(input())
result = ""
while not lines == 0:
    command = input()
    result += command
    lines -= 1
print(f"The sum equals: {sum(bytearray(result, 'utf-8'))}")
