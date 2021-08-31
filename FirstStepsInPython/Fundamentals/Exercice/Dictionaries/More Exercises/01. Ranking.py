from operator import itemgetter

exam_pass_input = input()
exam_pass_dict = {}
results = []

while not exam_pass_input == "end of contests":
    exam, password = exam_pass_input.split(":")
    exam_pass_dict[exam] = password
    exam_pass_input = input()

exam_pass_input = input()

while not exam_pass_input == "end of submissions":
    new = False
    contest, password, user, points = exam_pass_input.split("=>")

    if (contest in exam_pass_dict.keys()) and (password in exam_pass_dict.values()):
        if not results:
            results.append([user, contest, int(points)])
        else:
            for rec in results:
                if user == rec[0] and contest == rec[1]:
                    new = True
                    if int(points) > rec[2]:
                        rec.pop(2)
                        rec.append(int(points))

            if not new:
                results.append([user, contest, int(points)])

    exam_pass_input = input()

res_sort = sorted(results, key=itemgetter(0))
usr = res_sort[0][0]
top_res = {}
for rec in res_sort:
    if rec[0] == usr:
        if usr not in top_res.keys():
            top_res[usr] = 0

        top_res[usr] += rec[2]
    else:
        usr = rec[0]
        top_res[usr] = rec[2]
        continue

top_res = {x: y for x, y in sorted(top_res.items(), key=lambda item: -item[1])}

for name, points in top_res.items():
    print(f"Best candidate is {name} with total {points} points.")
    break
print("Ranking:")

res_sort = (sorted(res_sort, key=lambda x: (-x[2], x[1]), reverse=True))

for name, val in {x: y for x, y in sorted(top_res.items(), key=lambda item: item[0])}.items():
    print(name)
    for rec in range(len(res_sort) - 1, -1, -1):
        if name == res_sort[rec][0]:
            print(f"#  {res_sort[rec][1]} -> {res_sort[rec][2]}")
# # 01 Solution Polly Yankova
# contests = {}
# line_one = input()
# while not line_one == "end of contests":
#     line_info = line_one.split(":")
#     contest = line_info[0]
#     password = line_info[1]
#     contests[contest] = password
#     line_one = input()
# ranking = {}
# line_two = input()
# while not line_two == "end of submissions":
#     line_info = line_two.split("=>")
#     contest = line_info[0]
#     password = line_info[1]
#     username = line_info[2]
#     points = int(line_info[3])
#     if contest in contests and contests[contest] == password:
#         if username not in ranking:
#             ranking[username] = {contest: points}
#         else:
#             if contest in ranking[username]:
#                 if ranking[username][contest] < points:
#                     ranking[username][contest] = points
#             else:
#                 ranking[username][contest] = points
#     line_two = input()
#
# max_points = 0
# best_candidate = ' '
# for user, values in ranking.items():
#     current_points = 0
#     for name, point in values.items():
#         current_points += point
#     if current_points > max_points:
#         max_points = current_points
#         best_candidate = user
# print(f"Best candidate is {best_candidate} with total {max_points} points.")
# print("Ranking:")
# for user, value in sorted(ranking.items(), key=lambda kvp: kvp[0]):
#     print(f"{user}")
#     for contest, point in sorted(value.items(), key=lambda kvp: -kvp[1]):
#         print(f"#  {contest} -> {point}")
#
# # Input 0
# Part One Interview:success
# Js Fundamentals:Pesho
# C# Fundamentals:fundPass
# Algorithms:fun
# end of contests
# C# Fundamentals=>fundPass=>Tanya=>350
# Algorithms=>fun=>Tanya=>380
# Part One Interview=>success=>Nikola=>120
# Java Basics Exam=>pesho=>Petkan=>400
# Part One Interview=>success=>Tanya=>220
# OOP Advanced=>password123=>BaiIvan=>231
# C# Fundamentals=>fundPass=>Tanya=>250
# C# Fundamentals=>fundPass=>Nikola=>200
# Js Fundamentals=>Pesho=>Tanya=>400
# end of submissions
#
# # Output 0
# Best candidate is Tanya with total 1350 points.
# Ranking:
# Nikola
# #  C# Fundamentals -> 200
# #  Part One Interview -> 120
# Tanya
# #  Js Fundamentals -> 400
# #  Algorithms -> 380
# #  C# Fundamentals -> 350
# #  Part One Interview -> 220
# # TEST
# Part One Interview:success
# Js Fundamentals:Pesho
# C# Fundamentals:fundPass
# Algorithms:fun
# end of contests
# C# Fundamentals=>fundPass=>Tanya=>250
# C# Fundamentals=>fundPass=>Tanya=>350
# Algorithms=>fun=>Tanya=>380
# end of submissions
