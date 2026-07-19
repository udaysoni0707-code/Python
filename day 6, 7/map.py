def double_no(x):
    return x*2
print(double_no(2))

l = [1,2,3,4,5]
newl = list(map(double_no,l))
print(newl)

def mul_by_4(x):
    return x*4
print(mul_by_4(5))

l1 =[1,2,3,4,56,6]
newl1 = (map(lambda x:x*4,l1))
print(list(newl1))