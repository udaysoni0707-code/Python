# Q2. In your factory workers come to work on daily wage Your factory Rate Chart 
# Working Hour Wage 8 250/- >8 and <=10 50/- hr >10 and <=12 75/- hr >12 and <=14 
# 100/- hr other invalid working hour

emp_work_hr = float(input("Enter the working hour of worker : "))

if emp_work_hr <=8:
    earning = 250
elif emp_work_hr <=10:
    earning = 250 + (emp_work_hr - 8)*50
elif emp_work_hr <=12:
    earning = 250 + (2*50) + (emp_work_hr -10)*75
elif emp_work_hr <=14:
    earning = 250 + (2*50) + (2*75) + (emp_work_hr-12)*100
else:
    print("invaild hours")
    earning = 0
    
if earning is not None:
    print(f"The total eraning is :- {earning}")