#  On the first line, you will receive the names of the robots and their processing times in the format
# &quot;robotName-processTime;robotName-processTime;robotName-processTime...&quot;
#  On the second line, you will get the starting time in format &quot;hh:mm:ss&quot;
#  Next, until the &quot;End&quot; command, you will get a product on each line.

# # !!!! UNFINISHED !!!!
line_input = input().split(';')
start_time = [int(x) for x in input().split(':')]
robot_name = []
robot_time = []
for ll in line_input:
    robot_name.append(ll.split('-')[0])
    robot_time.append(int(ll.split('-')[1]))
# robot_name ['ROB', 'SS2', 'NX8000']
# robot_time [15, 10, 3]
# start_time [8, 0, 0]




# ROB-15;SS2-10;NX8000-3
# 8:00:00
