sub1 = int(input("Enter the marks of 1st subject : "))
sub2 = int(input("Enter the marks of 2nd subject : "))
sub3 = int(input("Enter the marks of 3rd subject : "))
sub4 = int(input("Enter the marks of 4th subject : "))
sub5 = int(input("Enter the marks of 5th subject : "))

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total / 500) * 100

print(f"Total Marks : {total}")
print(f"Percentage : {percentage:.2f}%")

if sub1 < 33 or sub2 < 33 or sub3 < 33 or sub4 < 33 or sub5 < 33:
    print("Student Division : Fail")
elif total >= 480:
    print("Student Division : Merit")
elif total >= 450:
    print("Student Division : 1st")
elif total >= 400:
    print("Student Division : 2nd")
elif total >= 370:
    print("Student Division : 3rd")
else:
    print("Student Division : Fail")