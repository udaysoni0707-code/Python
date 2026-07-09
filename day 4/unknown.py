# num = int(input("Enter the number: "))
# sum = 0

# while num > 0:
#     digit = num % 10
#     sum = sum + digit
#     num = num // 10

# print("Sum of digits =", sum)

# #2. enter a number and print reverse of the number

# num = int(input("Enter a number: "))
# reverse = 0

# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10

# print("Reverse =", reverse)

# #3. enter a number and print its palindrome or not
# num = int(input("Enter a number : "))
# orignal = num
# reverse = 0

# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10

# if reverse == orignal:
#     print(reverse)
# else:
#     print(f"this is not a palindrome number {orignal}")

# #4. enter a number and print its Armstrong or not
# #example: 153  1**3 + 5**3 + 3**3 = 153

# num = int(input("Enter a number : "))
# original = num
# sum = 0
# while num>0:
#     digit = num%10
#     sum = sum+digit**3
#     num = num//10
# if sum == original:
#     print(original, "is an Armstrong Number")
# else:
#     print("not a Armstrong no.")
    
#5. enter and number and print its binary equivalent
num = int(input("Enter a number: "))

binary = 0
remainder=0

while num>0:
    remainder = num%2
    binary = ""
    num = num//2

print(binary)