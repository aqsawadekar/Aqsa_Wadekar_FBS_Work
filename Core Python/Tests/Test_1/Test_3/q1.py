
n = int(input("Enter n: "))

num = 2
count = 0

while(count < n):
    i = 2

    while(i < num):
        if num % i == 0:
            break
        i = i + 1

    if(i == num):
        print(num, end = " ")
        count = count + 1

    num = num + 1
