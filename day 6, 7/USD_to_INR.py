# let 1 USD = 100 INR
# THEN 100 USD = {100 INR} X {100}

def usd_inr(usd):
    inr = usd*100

    print(f"USD = {usd} in INR = {inr}")
    
usd_inr(10)