# 15. enter 2 nos and print there value after swaping - using 3rd variable

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

print(f"The numbers before the swaping a = {a} , b = {b}")

temp = a 
a = b
b = temp 
print(f"The numbers after the swaping a = {a} , b = {b}")
