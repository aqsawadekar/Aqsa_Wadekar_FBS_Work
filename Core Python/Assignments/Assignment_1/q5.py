#Take inputs
P = int(input('Enter Principal:'))
T = float(input('Enter Time:'))
R = float(input('Enter Rate:'))

#Calculate Amount
A = P * (1 + R / 100) ** T

#Calculate Compound Interest
CI = A - P

#Display Result
print('Compound Interest:' , CI)