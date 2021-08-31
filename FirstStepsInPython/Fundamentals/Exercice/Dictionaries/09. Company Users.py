# Write a program that keeps information about companies and their employees.
# You will be receiving a company name and an employee's id, until you receive the command "End" command.
# Add each employee to the given company. Keep in mind that a company cannot have two employees with the same id.
# When you finish reading the data, order the companies by the name in ascending order.
# Print the company name and each employee's id in the following format:
# {companyName}
# -- {id1}
# -- {id2}
# -- {idN}
# Input / Constraints
# Until you receive the "End" command, you will be receiving input in the format: "{companyName} -> {employeeId}".
# The input always will be valid.

line_input = input()
companies = {}

while not line_input == 'End':
    company_name, employee_id = line_input.split(" -> ")

    if company_name not in companies:
        companies[company_name] = []
        companies[company_name].append(employee_id)
    else:
        if employee_id not in companies[company_name]:
            companies[company_name].append(employee_id)

    line_input = input()

for company_name, employee_id in sorted(companies.items(), key=lambda r: (r[0])):
    print(f"{company_name}")
    for number in employee_id:
        print(f"-- {number}")

# # input 0
# SoftUni -> AA12345
# SoftUni -> BB12345
# Microsoft -> CC12345
# HP -> BB12345
# End
#
# # output 0
# HP
# -- BB12345
# Microsoft
# -- CC12345
# SoftUni
# -- AA12345
# -- BB12345
#
# # input 1
# SoftUni -> AA12345
# SoftUni -> CC12344
# Lenovo -> XX23456
# SoftUni -> AA12345
# Movement -> DD11111
# SoftUni -> AA12345
# SoftUni -> CC12344
# Lenovo -> XX23456
# SoftUni -> AA12345
# Movement -> DD11111
# End