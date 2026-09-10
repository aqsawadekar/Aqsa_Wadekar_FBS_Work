#Take input
a = float(input('Enter the value of a:'))
b = float(input('Enter the value of b:'))
c = float(input('Enter the value of c:'))

#Perform operation
x1 = -b + (b ** 2 - 4 * a * c) / (2 * a)
x2 = -b - (b ** 2 - 4 * a * c) / (2 * a)

# Display result
print('Roots of Quadratic Euation are:' , x1 , x2)