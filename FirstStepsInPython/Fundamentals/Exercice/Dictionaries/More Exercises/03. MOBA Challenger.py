line_input = input()
moba, player_skill = {}, {}

while not line_input == "Season end":
    if "->" in line_input:
        player, position, skill = line_input.split(" -> ")
        skill = int(skill)

        if player not in moba:
            moba[player] = {position: skill}
            player_skill[player] = skill

        elif position not in moba[player]:
            moba[player][position] = skill
            player_skill[player] += skill
    else:
        player1, player2 = line_input.split(" vs ")
        player1_recs = ''
        player2_recs = ''
        stop = False

        if (player1 in moba) and (player2 in moba):
            for chosen_one in moba:

                if player1 == chosen_one:
                    player1_recs = moba[chosen_one].copy()

                elif player2 == chosen_one:
                    player2_recs = moba[chosen_one].copy()

            for key_record1, value_record1 in player1_recs.items():
                for key_record2, value_record2 in player2_recs.items():

                    if key_record1 == key_record2:

                        if value_record1 < value_record2:
                            moba.pop(player1)
                            player_skill.pop(player1)
                            stop = True

                        elif value_record1 > value_record2:
                            moba.pop(player2)
                            player_skill.pop(player2)
                            stop = True
                if stop:
                    break

    line_input = input()

for player_name, player_points in sorted(player_skill.items(), key=lambda r: (-r[1], r[0])):
    print(f"{player_name}: {player_points} skill")
    for chosen_one, skills in moba.items():
        if chosen_one == player_name:
            for position, power in sorted(skills.items(), key=lambda x: (-x[1], x[0])):
                print(f"- {position} <::> {power}")

# Pesho -> Adc -> 400
# Gosho -> Jungle -> 300
# Stamat -> Mid -> 200
# Stamat -> Mid -> 250
# Season end