# ITR
# 0-4 lac         0%
# >4 upto 8       5%
# >8 upto 12      10%
# >12 upto 16     15%
# >16 upto 20     20%
# >20 upto ...    25%

# 17 Lac

income = int(input("Enter the income in lac :- "))

if income <= 400000:
    tax = 0
elif income <= 800000:
    tax = (income-400000)*5/100
elif income <= 1200000:
    tax = (400000*5/100) + (income-8)*10
elif income <= 1600000:
    tax = (400000*5/100) + (400000*10/100) + (income-12)*15/100
else:
    tax = (400000*5/100) + (400000*10/100) + (400000*15/100) + (income-1600000)
    
print(f"income :- {income}")
print(f"Tax :- {tax}")