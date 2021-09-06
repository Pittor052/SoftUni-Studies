# Most football fans love it for the goals and excitement. Well, this problem does not.
# You are up to handle the referee's little notebook and count the players who were sent off for fouls and misbehavior.
# The rules: Two teams, named "A" and "B" have 11 players each. The players on each team are numbered from 1 to 11.
# Any player may be sent off the field by being given a red card. If one of the teams has less than 7 players remaining,
# the game is stopped immediately by the referee, and the team with less than 7 players loses.
# A card is a string with the team's letter ('A' or 'B') followed by a single dash and player's number.
# e.g. the card 'B-7' means player #7 from team B received a card.
# The task: You will be given a sequence of cards (could be empty), separated by a single space.
# You should print the count of remaining players on each team at the end of the game in the format:
# "Team A - {players_count}; Team B - {players_count}". If the game was terminated by the referee,
# print an additional line: "Game was terminated".
# Note for the random tests: If a player that has already been sent off receives another card - ignore it.
# # 01 solution
# team_a = 11
# team_b = 11
# cards = input().split()
# while True:
#     found = True  # value for breaking the while loop
#     for i in range(len(cards)):  # loop the whole list (0, end of str)
#         test_digit = cards[i]  # take the element on the current position
#         for j in range(len(cards)):  # loop the whole list for the comparison with the element and the whole list
#             if test_digit == cards[j] and (not i == j):  # compare the element in test_digit with the current one
#                 cards.remove(test_digit)  # remove the match
#                 cards.append("")  # replace the removed element to keep the integrity of the list
#                 found = False
#                 break
#     if found:
#         break
# stop = False
# for i in cards:
#     x = "".join(i)
#     if "A" in x:
#         team_a -= 1
#     elif "B" in x:
#         team_b -= 1
#     if team_a < 7 or team_b < 7:
#         stop = True
#         break
# print(f"Team A - {team_a}; Team B - {team_b}")
# if stop:
#     print("Game was terminated")
# # 02 solution
team_a = 11
team_b = 11
cards = input().split()
card_list = set(cards)
stop = False
for i in cards:
    x = "".join(i)
    if "A" in x:
        team_a -= 1
    elif "B" in x:
        team_b -= 1
    if team_a < 7 or team_b < 7:
        stop = True
        break
print(f"Team A - {team_a}; Team B - {team_b}")
if stop:
    print("Game was terminated")
# # INPUT 1
# A-1 A-5 A-10 B-2
# # INPUT 2
# A-1 A-5 A-10 B-2 A-10 A-7 A-3
# # INPUT END
