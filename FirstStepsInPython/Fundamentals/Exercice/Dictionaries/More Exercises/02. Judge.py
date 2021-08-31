from operator import itemgetter

recs = []
line_input = input()
count_contest = {}
individual_high_score = {}
while "no more time" not in line_input:
    line_input = line_input.split(" -> ")
    name = line_input[0]
    contest = line_input[1]
    points = int(line_input[2])
    if contest not in count_contest:
        count_contest[contest] = 1
    else:
        count_contest[contest] += 1
    if name not in individual_high_score.keys():
        individual_high_score[name] = 0
    if len(recs) == 0:
        recs.append({"name": name, "contest": contest, "points": points})
    else:
        stop = False
        new = True
        for rec in recs:
            if (rec["name"], rec["contest"]) == (name, contest):
                new = False
                count_contest[contest] -= 1
                if rec["points"] <= points:
                    rec.update({"points": points})
                    stop = True
            if stop:
                break
        if new:
            recs.append({"name": name, "contest": contest, "points": points})

    line_input = input()

records = sorted(recs, key=itemgetter("points"), reverse=True)
name_points = {}
for key, value in count_contest.items():
    print(f"{key}: {value} participants")
    num_participant = 0
    name_points.clear()

    for stats in records:
        if key == stats["contest"]:
            individual_high_score[stats["name"]] += stats['points']
            name_points[stats["name"]] = stats["points"]
    for key_name, value_points in sorted(name_points.items(), key=lambda r: (-r[1], r[0])):
        num_participant += 1
        print(f"{num_participant}. {key_name} <::> {value_points}")


print("Individual standings:")
count = 0
for name, points in sorted(individual_high_score.items(), key=lambda r: (-r[1], r[0])):
    count += 1
    print(f"{count}. {name} -> {points}")
# Pesho -> OOP -> 350
# Gosho -> OOP -> 250
# Stamat -> Advanced -> 600
# Gosho -> OOP -> 300
# Prakash -> OOP -> 300
# Prakash -> Advanced -> 250
# Ani -> JSCore -> 400
# Pesho -> OOP -> 350
# Gosho -> OOP -> 250
# Stamat -> Advanced -> 600
# Gosho -> OOP -> 300
# Prakash -> OOP -> 300
# Prakash -> Advanced -> 250
# Ani -> JSCore -> 400
# no more time
