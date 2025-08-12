'''Level2:
Level 2: Taxable Income Calculation
Objective: Calculate taxable income after standard deductions.
Tasks:
• Deduct a Standard Deduction of ₹50,000 from the annual gross salary.
• Compute the Taxable Income and display all intermediate calculations.
Output: Display gross salary, standard deduction and taxable income.'''
import tax

standard_deduction = 50000
taxable_income = tax.Annual_Gross_Salary - standard_deduction
print(f"The standard deduction is {standard_deduction}")
print(f"The Gross salary is {tax.Gross_Monthly_Salary}")
print(f"The taxable income is{taxable_income}")

