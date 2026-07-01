# enter marks of 5 subjects and print total and percetage
sub1 = int(input("Enter the marks of subject 1 "))
sub2 = int(input("Enter the marks of subject 2 "))
sub3 = int(input("Enter the marks of subject 3 "))
sub4 = int(input("Enter the marks of subject 4 "))
sub5 = int(input("Enter the marks of subject 5 "))

total = sub1+sub2+sub3+sub4+sub5
print(f"tha total number of 5 five subject are :{total}")

perctage = (total/500)*100
print(f"The percentage is:{perctage}")