n = int(input("Enter a number : "))
i =1
p=1
while i<=n:
    p = p*i
    i +=1
print(p)

# using for loop

n = int(input("Enter a number : "))
p=1
for i in range(1,n+1):
    p=p*i
print(p)