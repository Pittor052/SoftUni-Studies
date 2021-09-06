line_input = input().split(" ")
half = int(len(line_input) / 2)
car1 = line_input[:half]
car2 = line_input[half + 1:]
car2.reverse()
car1_result = 0
car2_result = 0
for i in car1:
    car1_result += int(i)
    if int(i) == 0:
        car1_result *= 0.8
for i in car2:
    car2_result += int(i)
    if int(i) == 0:
        car2_result *= 0.8
winner = ''
if min(car1_result, car2_result) == car1_result:
    winner = "left"
else:
    winner = "right"
print(f"The winner is {winner} with total time: {min(car1_result, car2_result):.1f}")
# # INPUT 1
# 29 13 9 0 13 0 21 0 14 82 12
# # INPUT END
