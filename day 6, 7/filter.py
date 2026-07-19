l = [9,8,7,6,5,4,3,2,1]
def filter_func(a):
    return a>6
newl = filter(filter_func,l)
print(list(newl))