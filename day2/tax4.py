import tax3 as t3, tax as t1

net_annual_salary = t1.Gross_Monthly_Salary - t3.tax_amount
print(f'Annual Gross Salary = {t1.Gross_Monthly_Salary}')
print(f'Total Tax Amount = {t3.tax_amount}')
print(f'Net Annual Salary = {net_annual_salary}')