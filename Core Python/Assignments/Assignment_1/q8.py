#Take input
days = int(input('Enter total number of days:'))

#Calculate years
years = days // 365

#Calculate remaining days
remaining_days = days % 365

#Calculate weeks
weeks = remaining_days // 7

#Calculate days
days = remaining_days % 7

#Display result
print('Years:' , years)
print('Weeks:' , weeks)
print('Days:' , days)