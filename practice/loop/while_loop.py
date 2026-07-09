# 1 program
i = 0
while i<=100:
    print(i)
    i+=1
    
# 2 program 

i = 100
while i>=1:
    print(i)
    i-=1
    
# 3th program of table
num = int(input("Enter a number : "))
i =1
while i<=10:
    print(f"The table of {num} X {i} = {num*i}")
    i+=1
    
# 4th program print a list using while loop
l1 = [1,2,3,4,5,6,7,8,9,10]
index = 0
while index<len(l1):
    print(l1[index])
    index +=1
    
# 5th program : find a number x in given tuple using the while loop
num = int(input("Enter a number : "))
l1 = (10,11,12,13,14,15,16,17,18)
index =0
while index<len(l1):
    if(l1[index] == num):
        print(f"User no is {num} are founded in {l1}")
    index +=1