#take input
a = int(input('Enter the value of first number :'))
b = int(input('Enter the value of second number :'))

#store a in temporary variable
temp = a


a = b

b = temp

#display result
print('After swapping first number :' , a)
print('After swapping second number :' , b)
