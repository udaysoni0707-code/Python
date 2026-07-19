# without lambda 

def square(x):
    return x*x
print(square(2))

# with the help of lambda 

sq = lambda y: y*y
print(f"The square is {sq(3)}")