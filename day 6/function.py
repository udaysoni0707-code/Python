# function defintion
def calcu_sum(a,b,c): # paramenters
    prod = a*b*c
    print(prod)
    return prod

calcu_sum(1,2,1987)    # function call; arguments

def print_hello():
    print("Hello ji :-)")
    
print_hello()

# average of 3 numbers ?
def avg(x,y,z):
    avg = (x+y+z)/3
    print(avg)
    return avg

avg(9,9,9)

# default parameters

def mul(a=10,b=12): 
    mul=a*b
    print(mul)
    return mul
mul()
