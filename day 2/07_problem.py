# 7. enter marks of 5 subjects and print total and percentage

m1 = int(input("enter the marks of subject 1"))
m2 = int(input("enter the marks of subject 2"))
m3 = int(input("enter the marks of subject 3"))
m4 = int(input("enter the marks of subject 4"))
m5 = int(input("enter the marks of subject 5"))

total = m1+m2+m3+m4+m5
print(f"Total marks of 5 subject is :{total}")

percentage = (total/500)*100
print(f"precentage of student is: {percentage}")