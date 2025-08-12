'''Level 1: Basic Input and Salary Calculation
Objective: Capture employee details and calculate the gross salary.
Tasks:
• Accept the following inputs for an employee:
o Name
o EmpID
o Basic Monthly Salary
o Special Allowances (Monthly)
o Bonus Percentage (Annual Bonus as % of Gross Salary)
• Calculate:
o Gross Monthly Salary = Basic Salary + Special Allowances
o Annual Gross Salary = (Gross Monthly Salary × 12) + Bonus
• Output:
o Display the employee details, gross monthly salary, and annual gross salary.
'''
print("Basic Input and Salary Calculation")

name=input("Enter your Name: ")
EmpID=int(input("Enter your Employee ID: "))
monthly_salary=int(input("Enter your Basic Monthly Salary: "))
s_allowances=int(input("Enter your any special allowances (Monthly): "))
bonus_percentage = float(input("Enter your bonus in percentage: "))
bonus_amount = (bonus_percentage / 100) * (monthly_salary * 12)
Gross_Monthly_Salary = monthly_salary + s_allowances
Annual_Gross_Salary = (Gross_Monthly_Salary * 12) + bonus_amount

print(name)
print(EmpID)
print(monthly_salary)
print(s_allowances)
print(bonus_percentage)
print(f" The Gross Monthly Salary is {Gross_Monthly_Salary}")
print(f" The Annual Gross Salary is {Annual_Gross_Salary}")

