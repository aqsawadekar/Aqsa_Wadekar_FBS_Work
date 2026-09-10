#take input
feet = float(input('Enter distance in feet:'))
inches = float(input('Enter distance in inches'))

#convert feet into inches
total_inches = feet * 12 + inches

#convert inches into cm
cm = total_inches * 2.54

#convert cm into meters
m = cm / 100

#display result
print('Distance in meters is:' , m)
print('Distance in centimeters is:' , cm)