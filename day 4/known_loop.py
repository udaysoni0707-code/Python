# # Print Row Number with Hello User

# i=1
# while i<=5:
#     print(f"{i}. hello word")
#     i=i+1
    
# # 2. print 1 to 10

# i = 1
# while i<=10:
#     print("number",i)
#     i=i+1
    
# # 3. Print 10 to 1 
# i = 10
# while i>1:
#     print(f"number : {i}")
#     i=i-1
    
# # 4. print table of 2 
# i = 1
# while i<=10:
#     print(f"The table of two 2*{i} = {2*i}")
#     i=i+1

# # 5. Print all even nos upto 100
# i = 1
# while i<=100:
#     if i%2==0:
#         print(f"The number is even : {i}")
#     i=i+1
    
# # 6. 50 se 1 tak even numbers print karo.

# i=50
# while i>1:
#     if i%2==0:
#         print(f"The even number is :- {i}")
#     i=i-1

# # 7. User se number lo aur check karo even hai ya odd (while + if use karke).

# num = int(input("Enter the number : "))
# i=1
# while i<=1:
#     if num%2==0:
#         print("even")
#     else:
#         print("odd")
#     i=i+1

# 8. Print sum of all nos upto 10
i=1
total=0
while i<=10:
    total = total+i
    i=i+1
print(total)

# 9. Print Product of all nos upto 5
i = 1
product = 1
while i<=5:
    product = product*i
    i=i+1
print(f"the product is : {product}")

# 10. enter a number and print its table

num = int(input("Enter a number : "))

i=1
while i<=10:
    print(f"The table is {num}*{i} = {num*i}")
    i=i+1
    
# 11. enter a number and print its factorial
# the outpu is : 5*4*3*2*1 = 120
num = int(input("Enter the number : "))

i = 1
factorial = 1

while i <= num:
    factorial = factorial * i
    i = i + 1

print("Factorial =", factorial)

# 11.enter 2 nos m and n print product of m , n times
# Example : m = 3, n = 4 Ans: 3 x 3 x 3 x 3 = 81
