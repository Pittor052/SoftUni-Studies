goal = 10000
num_steps = 0
pas = True
goal_reached = False
while not goal_reached:
    steps = input()
    try:
        num_steps += int(steps)
        pas = True
    except:
        steps = int(input())
        num_steps += steps
        pas = False
        if num_steps >= goal:
            goal_reached = True
            break
    if pas:
        if num_steps >= goal:
            goal_reached = True
            break
    else:
        break

if goal_reached:
    print("Goal reached! Good job!")
    print(f"{abs(goal - num_steps )} steps over the goal!")
else:
    print(f"{abs(num_steps - goal)} more steps to reach goal.")
