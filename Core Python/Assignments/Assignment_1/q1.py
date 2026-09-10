#take input
s1 = int(input('Enter marks of subject 1:'))
s2 = int(input('Enter marks of subject 2:'))
s3 = int(input('Enter marks of subject 3:'))
s4 = int(input('Enter marks of subject 4:'))
s5 = int(input('Enter marks of subject 5:'))

#Calculate obtained marks
obt_marks = s1 + s2 + s3 + s4 + s5 

#calculate percentage
sum = (obt_marks / 500) * 100

#display result
print('Total percentage:' , sum)