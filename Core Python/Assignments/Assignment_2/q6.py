#take input
basic = float(input('Enter basic salary: '))

#calculate da
da = basic * 10 / 100

#calculate ta
ta = basic * 12 / 100

#calculate hra
hra = basic * 15 / 100

#calculate total salary
total_salary = basic + da + ta + hra

#display result
print('Total Salary of Employee is :' , total_salary)