import collections

# # # SOLUTION 01 - 70/100
# dwarfs = []
# line_input = input()
# while "Once upon a time" not in line_input:
#     line_input = line_input.split(" <:> ")
#     name = line_input[0]
#     hat = line_input[1]
#     points = int(line_input[2])
#     if len(dwarfs) == 0:
#         dwarfs.append({"hat": hat, "name": name, "points": points})
#     else:
#         stop = False
#         new = True
#         for rec in dwarfs:
#             if (rec["name"], rec["hat"]) == (name, hat):
#                 new = False
#                 if rec["points"] < points:
#                     rec.update({"points": points})
#                     stop = True
#             if stop:
#                 break
#         if new:
#             dwarfs.append({"hat": hat, "name": name, "points": points})
#
#     line_input = input()
#
# result = sorted(dwarfs, key=lambda r: (-r["points"], r["hat"], -1 * r["name"]))
#
# for rec in result:
#     print(f"({rec['hat']}) {rec['name']} <-> {rec['points']}")
#
# # SOLUTION 02
line_input = input()
dwarfs = {}

while "Once upon a time" not in line_input:

    dwarf_name, hat, physics = line_input.split(" <:> ")
    physics = int(physics)

    if hat not in dwarfs:
        dwarfs[hat] = {dwarf_name: physics}

    elif dwarf_name in dwarfs[hat]:

        if dwarfs[hat][dwarf_name] < physics:
            dwarfs[hat][dwarf_name] = physics

    elif dwarf_name not in dwarfs[hat]:
        dwarfs[hat][dwarf_name] = physics

    line_input = input()

list_of_items = []

for k, v in dwarfs.items():
    for el in v:
        list_of_items.append((k, el, dwarfs[k][el], len(v)))

for i in sorted(list_of_items, key=lambda x: (-x[2], -x[3])):
    print(f"({i[0]}) {i[1]} <-> {i[2]}")

# dwarfs = collections.OrderedDict(sorted(dwarfs.items(), key=lambda r: (r[0][1], -len(r[0])), reverse=True))
# go = True
# for number in count_hats.values():
#     if number > 1:
#         dwarfs = {x: y for x, y in sorted(dwarfs.items(), key=lambda r: (r[0][1], -len(r[0])), reverse=True)}
#         go = False
#         break
# if go:
#     dwarfs = collections.OrderedDict(sorted(dwarfs.items(), key=lambda r: (r[0][1], -len(r[0]))))

# for hat, recs in dwarfs.items():
#     for name, strength in recs.items():
#         print(f"({hat}) {name} <-> {strength}")
# # TEST
# Pesho <:> Red <:> 2000
# Asd <:> Red <:> 2000
# Goble <:> Red <:> 2000
# Tosho <:> Blue <:> 1000
# Gosho <:> Green <:> 1000
# Sasho <:> Yellow <:> 4500
# Prakasho <:> Stamat <:> 1000
# Once upon a time


# # Solution by Petar Matev, expanded comprehension by Rumen Grozdanov
# dwarfs = {}
#
# while True:
#     command = input()
#     if command == "Once upon a time":
#         break
#     name, hatcolor, physics_ = command.split(" <:> ")
#     physics = int(physics_)
#
#     if hatcolor not in dwarfs:
#         dwarfs[hatcolor] = {name: physics}
#     else:
#         if name not in dwarfs[hatcolor]:
#             dwarfs[hatcolor].update({name: physics})
#         else:
#             if physics > dwarfs[hatcolor][name]:
#                 dwarfs[hatcolor][name] = physics
#
#
# # list_of_items = [(k, el, dwarfs[k][el], len(v)) for k, v in dwarfs.items() for el in v]
# list_of_items = []
# for k, v in dwarfs.items():
#     for el in v:
#         list_of_items.append((k, el, dwarfs[k][el], len(v)))
#
# for i in sorted(list_of_items, key=lambda x: (-x[2], -x[3])):
#     print(f"({i[0]}) {i[1]} <-> {i[2]}")
#
# # TEST
# Asd <:> Red <:> 2001
# Pesho <:> Red <:> 2000
# Tosho <:> Blue <:> 1000
# Gosho <:> Green <:> 1000
# Sasho <:> Yellow <:> 4500
# Prakasho <:> Stamat <:> 1000
# Once upon a time
#
# # TEST
# Pesho <:> Red <:> 5000
# Pesho <:> Blue <:> 10000
# Asd <:> Blue <:> 10000
# Pesho <:> Red <:> 10000
# Gosho <:> Blue <:> 10000
# Once upon a time
