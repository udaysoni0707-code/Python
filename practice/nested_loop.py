for i in range (1,5):
    for j in range (1,4):
        print("*",end=" ")
        
    print()

'''
*
* *
* * *
* * * *
'''
for i in range (1,4):
    for j in range(1,i+1):
        print("$",end=" ")
        
    print()
    
'''
* * * * *
* * * *
* * * 
* * 
*
'''
for i in range (6,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
    
'''
1
1 2
1 2 3
1 2 3 4
'''
for i in range (1,5):
    for j in range (1,i+1):
        print(j,end=" ")
    print()
    
'''
4 3 2 1
3 2 1
2 1 
1
'''
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j , end=" ")
    print()