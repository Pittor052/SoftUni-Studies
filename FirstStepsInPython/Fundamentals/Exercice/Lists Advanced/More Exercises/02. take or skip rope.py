line_input = list(x for x in input())
num_list = list(int(x) for x in line_input if x.isnumeric())
words = list(x for x in line_input if not x.isnumeric())
take = list(num_list[x] for x in range(len(num_list)) if x % 2 == 0)
skip = list(num_list[y] for y in range(len(num_list)) if y % 2 == 1)
result = []
for i in range(len(take)):
    result.append(words[:take[i]])
    if skip[i] > 0:
        words = words[take[i] + skip[i]:]
for j in range(len(result)):
    for k in result[j]:
        print(k, end="")
# /home/master/PycharmProjects/pythonProjects/FirstStepsInPython/Fundamentals/Exercise /Lists Advanced/
# More Exercises