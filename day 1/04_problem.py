# enter 2 no and print their value after swaping

# Enter 2 numbers and swap them

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

temp = a
a = b
b = temp

print("After swapping:")
print("a =", a)
print("b =", b)