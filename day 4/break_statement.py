# print all prime numbers between 1 to 100
num = 2

while num <= 100:
    i = 2

    while i < num:
        if num % i == 0:
            break
        i += 1

    if i == num:
        print(num)

    num += 1