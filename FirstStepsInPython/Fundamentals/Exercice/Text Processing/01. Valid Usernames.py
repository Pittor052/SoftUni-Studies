usernames = input().split(", ")
allowed_symbols = ["-", "_"]
for user in usernames:
    valid = True
    if 3 <= len(user) <= 16:
        for char in user:
            if not char.isalnum():
                if char not in allowed_symbols:
                    valid = False
                    break
    else:
        valid = False
    if valid:
        print(user)

# # Solution Georgi Ivanov
# string = input().split(", ")
#
# for i in string:
#     if 3 < len(i) < 16:
#         if "_" in i or "-" in i or i.isalnum():
#             print(i)
# # INPUT
# sh, too_long_username, !lleg@l ch@rs, jeffbutt
# Jeff, john45, ab, cd, peter-ivanov, @smith
