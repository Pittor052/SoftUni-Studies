# Judge statistics on the last Programming Fundamentals exam was not working correctly,
# so you have the task to take all the submissions and analyze them properly.
# You should collect all the submissions and print the final results and statistics about
# each language that the participants submitted their solutions in.
# You will be receiving lines in the format: "{username}-{language}-{points}" until you receive "exam finished".
# You should store each username and his submissions and points.
# You can receive a command to ban a user for cheating in the following format: "{username}-banned".
# In that case, you should remove the user from the contest,
# but preserve his submissions in the total count of submissions for each language.
# After receiving "exam finished" print each of the participants, ordered descending by their max points,
# then by username, in the following format:
# Results:
# {username} | {points}
# …
# After that print each language, used in the exam,
# ordered descending by total submission count and then by language name, in the following format:
# Submissions:
# {language} - {submissionsCount}
# …
# Input / Constraints
# Until you receive "exam finished" you will be receiving participant submissions in the following format:
# "{username}-{language}-{points}".
# You can receive a ban command -> "{username}-banned"
# The points of the participant will always be a valid integer in the range [0-100];
# Output
# Print the exam results for each participant, ordered descending by max points and then by username,
# in the following format:
# Results:
# {username} | {points}
# …
# After that print each language, ordered descending by total submissions and then by language name,
# in the following format:
# Submissions:
# {language} - {submissionsCount}
# …

from operator import itemgetter

line_input = input()
exams = []
banned = []
unique_records = []
res = {}
langs = {}

while "exam finished" not in line_input:

    if "banned" not in line_input:

        line_input = line_input.split("-")
        user = line_input[0]
        language = line_input[1]
        points = int(line_input[2])

        # create list of dicts from the input
        exams.append({"name": user, "language": language, "points": points})

        if language not in langs.keys():  # count the languages
            langs[language] = 1
        else:
            langs[language] += 1

    else:  # create list of banned names

        line_input = line_input.split("-")
        banned.append(line_input[0])

    line_input = input()

exams.sort(key=itemgetter("points"), reverse=True)

for rec in exams:
    if len(unique_records) == 0:
        res[rec["name"]] = 0
        res[rec["name"]] = (int(rec["points"]))
        unique_records.append({"name": rec["name"], "language": rec["language"], "points": rec["points"]})
    else:
        unique = True
        for rec2 in unique_records:
            if (rec["name"], rec["language"]) == (rec2["name"], rec2["language"]):
                unique = False
                break
        if unique:
            res[rec["name"]] = 0
            res[rec["name"]] = (int(rec["points"]))  # create dict with name and points
            #  append only unique records
            unique_records.append({"name": rec["name"], "language": rec["language"], "points": rec["points"]})

#                        sort res{name:points} by value(points) and then by key(name)
res1 = {k: v for k, v in sorted(res.items(), key=lambda item: (-item[1], item[0]))}

print("Results:")

for name, points in (res1.items()):
    if name not in banned:
        print(f"{name} | {points}")

print("Submissions:")

#                        sort langs{language:int} by value(int) and then by key(language)
res2 = {k: v for k, v in sorted(langs.items(), key=lambda item: (-item[1], item[0]))}

for lan, num in (res2.items()):
    print(f"{lan} - {num}")

# # Input 0
# Pesho-Java-84
# Gosho-C#-84
# Gosho-C#-70
# Kiro-C#-94
# exam finished
#
# Output 0
# Results:
# Kiro | 94
# Gosho | 84
# Pesho | 84
# Submissions:
# C# - 3
# Java - 1
#
# Comment 0
# We order the participant descending by max points and then by name, printing only the username and the max points.
# After that we print each language along with the count of submissions, ordered descending by submissions count,
# and then by language name.
# Input 1
# Pesho-Java-91
# Gosho-C#-84
# Kiro-Java-90
# Kiro-C#-50
# Kiro-banned
# exam finished
#
# Output 1
# Results:
# Pesho | 91
# Gosho | 84
# Submissions:
# C# - 2
# Java - 2
#
# Comment 1
# Kiro is banned so he is removed from the contest, but he`s submissions are still preserved in
# the languages submissions count.
# So although there are only 2 participants in the results, there are 4 submissions in total.
