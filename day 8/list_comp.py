double_marks = []
for i in range(10,21):
    double_marks.append(i)
print(double_marks)

# using list comprehension 

numbers = [i for i in range(1,6)]
print(numbers)

# Syntax 
# new_list = [expression for item in iterable]      
# expression    -> kya store karna hai
# for item      -> loop
# iterable      -> range(), list, tuple, string etc.

square = [i**2 for i in range(1,7)]
print(square)

# cube of all element in list , without using list

cube = []     # without list comperhension
for i in range(1,10):
    cube.append(i**3)
print(cube)
                # using list comperhension 
cube = [i**3 for i in range(1,10)]
print(cube)

even = [i for i in range(1,17) if i%2==0]
print(even)

odd = [j for j in range(1,17) if i%2!=0]
print(f"odd number list :- {odd}")

square_even = [i**2 for i in range(1,10) if i%2==0]
print(f"The square of even number :- {square_even}")

names = ["uday","aman","rahul"]
upper = [name.upper() for name in names]
print(upper)

# syntax with if else condition in list comprehension 
# [expression_if_true if condition else expression_if_false for item in iterable]

result = ["even" if i%2==0 else "odd" for i in range(1,7)]
print(result)

# nested list comprehension
# normal 
l1 = []
for i in range (1,5):
    for j in range (1,5):
        l1.append((i,j))
print(l1)
# using list comperhension 
pairs = [(i,j) for i in range (1,4) for j in range (1,4)]
print(pairs)