'''
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