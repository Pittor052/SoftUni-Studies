grades = int(input())
name_exam = str(input())
grade = int(input())
poor_grade = 0
pas = True
average = 0
problems_solved = 0
last_name_exam = str()
while name_exam != "Enough":
    if int(grade) <= 4:
        poor_grade += 1
    if poor_grade == grades:
        pas = False
        break

    problems_solved += 1
    average += int(grade)
    last_name_exam = name_exam
    name_exam = str(input())
    grade = input()

if pas:
    print(f"Average score: {average / problems_solved:.2f}")
    print(f"Number of problems: {problems_solved}")
    print(f"Last problem: {last_name_exam}")
else:
    print(f"You need a break, {poor_grade} poor grades.")
