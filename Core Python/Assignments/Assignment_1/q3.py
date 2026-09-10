#Take input
num1 = int(input('Enter the value for dividend:'))
num2 = int(input('Enter the value for divisor:'))

#Perform Operation for Quotient
Q = num1 // num2
print('Quotient is:', Q)

#Perform Operation for Remainder
R = num1 % num2
print('Remainder is:' , R)

#Display result
print(f'Quotient and Remainder of {num1} and {num2} is {Q} and {R}')