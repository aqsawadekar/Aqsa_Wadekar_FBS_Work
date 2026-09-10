#take input
num = int(input('Enter three digit number:'))

#perform operation
d1 = num % 10
print('Digit 1 is:' , d1)
num = num // 10
print('Number is:' , num)

d2 = num % 10
print('Digit 2 is:' , d1)
num = num // 10
print('Number is:' , num)

d3 = num % 10
print('Digit 3 is:' , d1)
num = num // 10
print('Number is:' , num)

#perform reverse addition
reverse = d1 * 100 + d2 * 10 + d3
print('Sum of three digit number is:' , reverse)