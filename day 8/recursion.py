def print_num(n):
    if n > 5:      # Base Case
        return

    print(n)

    print_num(n + 1)   # Recursive Call

print_num(1)

def fun(n):
    if n == 0:
        return

    print(n)
    fun(n-1)
    print(n)

fun(2)

# print number 1 to N 
def num(n):
    if n==0:
        return
    
    num(n-1)
    print(n)
    
fun(10)

# print N to 1
def num(n):
    if n==0:
        return
    
    print(n)
    num(n-1)
    
num(10)

# Program 3: Sum of N Numbers
def sum(n):
    if n==0:
        return 0
    else:
        return n+sum(n-1)  
    

    
print(f"The sum of n :- {sum(3)}")

# factorial of N

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
print(f"Thr factorial is :- {fact(6)}")

# 2^5
def power_n(n):
    if n==0:
        return 1
    else:
        return n**5
print(power_n(2))