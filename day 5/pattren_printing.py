# '''
# 1
# 12
# 123
# 1234
# 12345
# '''
# for i in range(5):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print( )
    
# '''
# 5
# 44
# 333
# 2222
# 11111
# '''
# for i in range(1,6):
#     for j in range(i+1,1,-1):
#         print(i,end=" ")
#     print()
    
# '''
# 3.
# 5
# 54
# 543
# 5432
# 54321
# '''
# for i in range (1,6):
#     for j in range(5,5-i,-1):
#         print(j,end=" ")
#     print()

# '''
# 5
# 45
# 345
# 2345
# 12345
# '''
# for i in range(1,6):
#     for j in range(6-i,6):
#         print(j,end=" ")
#     print()
    
# '''
# 1
# 23
# 456
# 78910
# '''
# # for i in range(1,5):
# #     for j in range():
# #         print(j,end=" ")
# #     print()

# '''
# *****
# ****
# ***
# **
# *
# *
# **
# ***
# ****
# *****
# '''
# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print("*",end=" ")
#     print()
# for i in range(0,6):
#     for j in range(0,i):
#         print("*",end=" ")
#     print()
    
# '''
# ----*
# ---*-*
# --*-*-*
# -*-*-*-*
# *-*-*-*-*
# '''
# '''
# logic 
# total row = 5
# space for first row = conti 4 _
# space for second row = conti 3 _ then one * then _
# space for third row = conti 2 _*_*_*
# space for fourth row = _*_*_*_*
# space for fivth row = *_*_*_*_*
# '''
# for i in range(1,6):
#     for j in range(5-i):
#         print(" ",end="")
#     for j in range(i):
#         print("*",end="")
#         if j != i-1:
#             print("_",end="")
    
#     print()
    
# '''
# ----1
# ---121
# --12321
# -1234321
# 123454321
# '''
# for i in range(0,5):
#     for j in range (4-i,0,-1):
#         print(" ",end=" ")
#     for j in range(1,i+2):
#         print(j,end=" ")
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print( )

# '''
# 54321
# 5432
# 543
# 54
# 5
# '''
# for i in range(1,6):
#     for j in range(5,i-1,-1):
#         print(j,end=" ")
        
#     print( )

'''
5
54
543
5432
54321
'''
for i in range(5,0,-1):
    for j in range(5,5-i):
        print(j,end=" ")
    print()
    
'''
1
22
333
4444
55555
'''
for i in range(1,6):
    for j in range(1,i+1,+1):
        print(i,end=" ")
    print()
    
'''
1
12
123
1234
12345
'''
for i in range(1,6,+1):
    for j in range(1,i+1,+1):
        print(j,end=" ")
    print()
    
'''
5
45
345
2345
12345
'''
for i in range(5,0,-1):
    for j in range(i,6):
        print(j,end=" ")
    print()
    
'''
1                  logic : total row 5
22                 outer loop : 1,6
333                inner loop : 1,i+1
4444               print : i in inner loop
55555              print: () in outer loop 
'''
# code :-
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
    
'''
12345           logic : total row : 5
1234            outer loop : 1,6
123             inner loop : 1,7-i
12              print j in inner loop
1               print() in  outer loop
'''
for i in range(1,6):
    for j in range(1,7-i):
        print(j,end=" ")
    print()
    
'''
55555           logic : total row : 5
4444            outer loop: 5,0,-1
333             inner loop: 1,i+1
22              print i in inner loop 
1
'''
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
    
    
'''
1               logic : total row :5
21              outer loop (1,6)
321             inner loop (i,0,-1)
4321            print(i)
54321
'''
for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
    
'''
5               logic : total row : 5
54              outer loop : (5,0,-1)
543             inner loop : (5,i-1,-1)
5432            print (j)
54321
'''
for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(j,end=" ")
    print()
    
'''
    1           logic total row : 5
   12           outer loop : 1,6,+1
  123           inner loop => space : (1, 6-i) print : " " , number : (1,i+1) print : j 
 1234
12345
'''
for i in range(1,6):
    for j in range(1,6-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    
'''
    1           logic : total row : 5
   121          outer loop : 1,6
  12321         inner loop : space: 1,6-i print " ", increasing no : 1,i+1 print j, decreasing no : i,0,-1 print j
 1234321
123454321
'''
for i in range(1,6):
    for j in range(1,6-i): # for spaces
        print(" ",end=" ")
    for j in range(1,i+1): # for increasing number
        print(j,end=" ")
    for j in range(i-1,0,-1): #for decreasing number  
        print(j,end=" ")
    print()
    
'''             logic : total row : 5
1               outer loop 1,6
23 2             inner loop : increasing with diff no : i,i*2 print j, decreasing no : 
345 43
4567 654
56789 8765
'''
for i in range(1,6):
    for j in range(i,i*2): # for increasing with diff number starting 
        print(j,end=" ")
    for j in range(2*i-2,i-1,-1):
        print(j, end=" ")
    print()
    
'''             logic : total row : 5
*****           outer loop : (1,6)
*   *           
*   *
*   *
*****
'''
for i in range(1,6):
    for j in range(1,6):
        if i==1 or j==1 or i==5 or j==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
'''
*****
   *
  *
 *
*****
'''
for i in range(1,6):
    for j in range(1,6):
        if i==1 or i==5 or i+j==6:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
'''
*
 *
  *
   *
    *
'''
for i in range(1,6):
    for j in range(1,6):
        if i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
'''
*       *
 *     *
  *   *
   * *
    *
'''
for i in range(1,6):
    for j in range(1,10):
        if i==j or i+j==10:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
