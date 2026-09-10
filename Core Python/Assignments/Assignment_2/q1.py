#Take input
hh = int(input('Enter hours:'))
min = int(input('Enter minutes:'))
sec = int(input('Enter seconds:'))

#perform operation
total_seconds = hh * 3600 + min * 60 + sec

#Display result
print('Total Seconds is:' , total_seconds)
