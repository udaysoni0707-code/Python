# biggest between 3 nos using ternary operator

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter thrid number: "))

# expr1 if condition else expr2

biggest=a if a>b  and a>c else b if b>a and b>c else c

print(f"Biggest number is {biggest}")

