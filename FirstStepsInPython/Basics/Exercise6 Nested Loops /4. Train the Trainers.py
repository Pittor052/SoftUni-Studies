jury = int(input())
subject = input()
sum_grades = 0.0
total_grades = 0.0
count_grades = 0
print()
while not subject == "Finish":
    command = input()
    try:
        sum_grades += float(command)
        count_grades += 1
    except:
        print(f"{subject} - {sum_grades / jury:.2f}.")
        subject = command
        total_grades += sum_grades
        sum_grades = 0.0
    continue

print(f"Student's final assessment is {total_grades/count_grades:.2f}.")

# 2
# While-Loop
# 6.00
# 5.50
# For-Loop
# 5.84
# 5.66
# Finish
