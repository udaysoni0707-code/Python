#  input rd premium and print maturity 
#     Post office : small saving account (RD)
#     Criteria : Min of RD premium 5/- month
#     Time Period : 5 years
#     maturity : 364.27 on 5 rupees per month 
#     Note: Premium always 5x?
#     Time : fix for 5 years 
# Post Office RD Maturity Calculator

premium = int(input("Enter monthly RD premium: "))

maturity = (premium / 5) * 364.27

print("Monthly Premium =", premium)
print("Time Period = 5 Years")
print("Maturity Amount = ₹", round(maturity, 2))