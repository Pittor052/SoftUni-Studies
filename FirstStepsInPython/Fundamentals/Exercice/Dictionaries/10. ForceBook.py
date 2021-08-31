# The force users are struggling to remember which side are the different forceUsers from,
# because they switch them too often. So you are tasked to create a web application to manage their profiles.
# You should store an information for every unique forceUser, registered in the application.
# You will receive several input lines in one of the following formats:
#   {forceSide} | {forceUser}
#   {forceUser} -> {forceSide}
# The forceUser and forceSide are strings, containing any character.
# If you receive forceSide | forceUser:
#   If there is no such forceUser and no such forceSide -> create new forceSide and add the forceUser
#       to the corresponding side.
#   Only if there is no such forceUser in any forceSide -> add the forceUser to the corresponding side.
#   If there is such forceUser already -> skip the command and continue to the next operation.
# If you receive a forceUser -> forceSide:
#   If there is such forceUser already -> change his/her side.
#   If there is no such forceUser in any forceSide -> add the forceUser to the corresponding forceSide.
#   If there is no such forceUser and no such forceSide -> create new forceSide and add the forceUser
#       to the corresponding side.
#   Then you should print on the console: "{forceUser} joins the {forceSide} side!" .
# You should end your program when you receive the command "Lumpawaroo".
# At that point you should print each force side, ordered descending by forceUsers count,
# than ordered by name. For each side print the forceUsers, ordered by name.
# In case there are no forceUsers in a side, you shouldn`t print the side information.
# Input / Constraints
#   The input comes in the form of commands in one of the formats specified above.
#   The input ends, when you receive the command "Lumpawaroo".
# Output
#   As output for each forceSide, ordered descending by forceUsers count, then by name,
#       you must print all the forceUsers, ordered by name alphabetically.
#   The output format is:
# Side: {forceSide}, Members: {forceUsers.Count}
# ! {forceUser}
# ! {forceUser}
# ! {forceUser}
# In case there are NO forceUsers, don`t print this side.
profiles = {}
command = input()


def user_existence(collection: {}, f_user):
    for users_ in collection.values():
        if f_user in users_:
            return True
    return False


def del_user(collection: {}, usr: str):
    for side, f_user in collection.items():
        if usr in f_user:
            collection[side].remove(usr)


def create_new(collection: {}, side: str, user: str):
    if (side not in collection.keys()) and (not user_existence(collection, user)):
        collection[side] = []  # create new forceSide
        collection[side].append(user)  # add the forceUser to the corresponding side.
    elif not user_existence(collection, user):
        collection[side].append(user)


def switch_side(collection: {}, side: str, user: str):
    if user_existence(collection, user):  # If there is such forceUser already
        del_user(collection, user)

        if side in collection.keys():
            collection[side].append(user)  # change his/her side
            print(f"{user} joins the {side} side!")
        else:
            collection[side] = []  # create new forceSide
            collection[side].append(user)  # add the forceUser to the corresponding side.
            print(f"{user} joins the {side} side!")

    elif side in collection.keys():
        profiles[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

    else:
        profiles[force_side] = []  # create new forceSide
        profiles[force_side].append(force_user)  # add the forceUser to the corresponding side.
        print(f"{force_user} joins the {force_side} side!")


while not command == "Lumpawaroo":

    if " | " in command:  # If you receive {forceSide} | {forceUser}:

        force_side, force_user = command.split(" | ")
        create_new(profiles, force_side, force_user)

    else:  # If you receive {forceUser} -> {forceSide}
        force_user, force_side = command.split(" -> ")
        switch_side(profiles, force_side, force_user)

    command = input()

profiles = dict((x, y) for x, y in sorted(profiles.items(), key=lambda r: (-len(r[1]), r[0])))

for current_side, users in profiles.items():
    if users:
        print(f"Side: {current_side}, Members: {len(users)}")
        for jedi in sorted(users):
            print(f"! {jedi}", end="\n")

# Side: {forceSide}, Members: {forceUsers.Count}
# ! {forceUser}
# ! {forceUser}
# ! {forceUser}
# In case there are NO forceUsers, don`t print this side.

# # Input 0
# Light | Gosho
# Dark | Pesho
# Lumpawaroo
#
# # Output 0
# Side: Dark, Members: 1
# ! Pesho
# Side: Light, Members: 1
# ! Gosho
#
# # Comments
# We register Gosho in the Light side and Pesho in the Dark side. After receiving "Lumpawaroo" we print both sides,
# ordered by membersCount and then by name.
#
# # Input 1
# Lighter | Royal
# Darker | DCay
# Ivan Ivanov -> Lighter
# DCay -> Lighter
# Lumpawaroo
#
# # Output 0
# Ivan Ivanov joins the Lighter side!
# DCay joins the Lighter side!
# Side: Lighter, Members: 3
# ! DCay
# ! Ivan Ivanov
# ! Royal
#
# # Comments
# Although Ivan Ivanov doesn't have profile, we register him and add him to the Lighter side.
# We remove DCay from Darker side and add him to Lighter side.
# We print only Lighter side because Darker side has no members.
#
# # TEST
# Lighter | Royal
# Darker | DCay
# Ivan Ivanov -> Darker
# DCay -> Darker
# Lumpawaroo
