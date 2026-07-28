# question 1 : ek file banai hai or usme kuch 
#            likha h then use print krwa diya 
with open("student.txt","w") as file:
    file.write("Name of student :- Uday")
    
with open("student.txt","r") as file:
    print(file.read())
    
# question 2 : ek file banai h or usme 3 line 
#              teen line likhni h , phir poori file
#              ko print karo 

print("Question :- 2")
with open("teacher.txt","w+") as file:
    file.write("Rahul\n")
    file.write("Aman\n")
    file.write("Uday\n")
    file.seek(0)
    print(file.readline())
    print(file.readline())
    print(file.readline())
    
# question 3 employee.txt naam ki file banao aur 
# usme ye data likho:

# 101 Rahul
# 102 Aman
# 103 Uday

# Phir:

# Pointer ko start par le jao.
# Sirf pehli line print karo.
# Uske baad baaki poora data print karo.

print("question 3")
with open("employee.txt","w+") as file:
    file.write("101 Rahul\n102 Aman\n103 Uday")
    file.seek(0)
    print(file.readline())
    print(file.read())
    
'''
question 4 
student.txt me ye data likho:

Rahul
Aman
Uday
Rohit
Mohit

Ab program aisa likho ki output sirf ye aaye:

Rahul
Uday
Mohit
'''
# question 4 
print("question 4.")
with open("student.txt","w+") as file:
    file.write("Rahul\nAman\nUday\nRohit\nMohit")
    file.seek(0)
    print(file.readline())
    file.readline()
    print(file.readline())
    file.readline()
    print(file.readline())
    
'''
Question 5
'''
print("question 5 ")
with open("result.txt","w+") as file:
    file.write("Rahul 90\nAman 75\nUday 88\nRohit 65\nMohit 92")
    file.seek(0)
    for line in file:
        line = line.split()
        