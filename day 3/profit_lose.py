#  enter sale price and cost price of a product and print profit or loss
cost_price = float(input("Enter the cost price pf item : "))
sale_price = float(input("Enter the sale price of item : "))

if cost_price < sale_price:
    profit = sale_price - cost_price
    print(f"The profit is :- {profit}")
else:
    lose = cost_price - sale_price
    print(f"The lose is :- {lose}")