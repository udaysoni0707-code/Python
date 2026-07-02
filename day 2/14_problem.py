# enter basic salary of employee , calculate hra=10% of basic, da=55% of basic, pf=12% of basic and print gross salary
#     grosssalary=basic+hra+da-pf

basic_salary = int(input("Enter the basic salary : "))

hra = basic_salary*10/100
da = basic_salary*55/100
pf = basic_salary*12/100
gross_salary = basic_salary+hra+da-pf

print(f"hra of basic salary : {hra}")
print(f"da of basic salary : {da}")
print(f"pf of basic salary : {pf}")
print(f"Here the gross_salry : {gross_salary}")