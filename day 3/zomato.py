# ------------- Zomato delivery charges
# 3 km            40
# >3 upto 5       5/- km
# >5 upto 10      3/- km
# >10 upto 15     2/-

# 11 KM

distance = float(input("Enter the distance :-"))

if distance <=3:
    earning = 40
elif distance <=5:
    earning = 40 + (distance - 3)*5
elif distance <=10:
    earning = 40 + (2*5) + (distance -5)*3
else:
    earning = 40 + (2*5) + (5*3) + (distance -10)*2
    
print(f"distance is :- {distance}")
print(f"The total earning :- {earning}")