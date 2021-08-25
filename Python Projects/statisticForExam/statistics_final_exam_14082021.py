import re

line = input('Please input the data:\n')
results = []
scoredBelow100, scored100to200, scored200to300, scoredMax, countStudents = 0, 0, 0, 0, 0
regexFinalScore = r'(\d+$)'

while not line == "":
    countStudents += 1
    results.append([item.group() for item in re.finditer(regexFinalScore, line)])
    results[countStudents - 1] = (int(results[countStudents - 1][0]))
    line = input()

examType = input('Please input the exam name (example: Fundamentals Final Exam ): ')
examDate = input('Please input the exam date (example: 14/08/2021): ')
print(f'\n{examType}')
print(f'Exam date: {examDate} \n'
      f'Statistic for languages: '
      f'| JavaScript code (NodeJS) | Java code | PHP code (CLI) | Java zip file | Python code | C# code (.NET Core) |\n'
      f'Each student was given a random set of 3 problems from 18 available!\n'
      f'\nFrom {countStudents} participants:')

for score in set(results):

    if score < 100:
        scoredBelow100 += results.count(score)
    elif 100 <= score < 200:
        scored100to200 += results.count(score)
    elif 200 <= score < 300:
        scored200to300 += results.count(score)
    else:
        scoredMax += results.count(score)

print(f' * {(scoredBelow100 / countStudents) * 100:.2f}% ({scoredBelow100} students) got score '
      f'below 100 total points!\n'
      f' * {(scored100to200 / countStudents) * 100:.2f}% ({scored100to200} students) got score '
      f'between 100 and 200 total points!\n'
      f' * {(scored200to300 / countStudents) * 100:.2f}% ({scored200to300} students) got score '
      f'between 200 and 300 total points!\n'
      f' * {(scoredMax / countStudents) * 100:.2f}% ({scoredMax} students) got maximum total points!\n')
answer = input('Do you wish to view more details about the exam (Y/N)? ').upper().split()
if (len(answer) == 0) or (('Y' or 'YES') in answer):
    for i in set(results):
        print(f' * {results.count(i)} student/s got total score of {i}')

# # EXAMPLE FOR DATA INPUT
# 1	dasdsad123	Ivan Ivanov	100	-	-	-	-	100	-	-	-	-	-	-	-	-	-	100	-	-	90
# 2	Asds SAS	Ivan Ivanov	100	-	-	-	-	100	-	-	-	-	-	-	-	-	-	100	-	-	100
# 3	sadas	Ivan Ivanov	100	-	-	-	-	100	-	-	-	-	-	-	-	-	-	100	-	-	200
# 4	1233	Ivan Ivanov	100	-	-	-	-	100	-	-	-	-	-	-	-	-	-	100	-	-	300
# 5	asd_!123	Ivan Ivanov	100	-	-	-	-	100	-	-	-	-	-	-	-	-	-	100	-	-	300
