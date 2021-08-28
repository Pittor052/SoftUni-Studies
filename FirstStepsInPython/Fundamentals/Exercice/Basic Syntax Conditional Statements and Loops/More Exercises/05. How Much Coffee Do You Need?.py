command = input()
compare_string_lower = {"coding", "dog", "cat", "movie"}
compare_string_upper = {"CODING", "DOG", "CAT", "MOVIE"}
coffee = 0
get_sleep = False
while not command == "END":
    if command.isupper() and command in compare_string_upper:
        coffee += 2
    if command.islower() and command in compare_string_lower:
        coffee += 1
    if coffee > 5:
        get_sleep = True
        print()
        print("You need extra sleep")
        break
    command = input()
if not get_sleep:
    print(f"{coffee}")

# dog
# CAT
# gaming
# END

# movie
# CODING
# MOVIE
# CLEANING
# cat
# END
