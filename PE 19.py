#jan,mar,may,july,august,oct,dec = 31
#april,june,september,november = 30
from time import time
t = time()

days = ["","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
values = [0,1,2,3,4,5,6,7]
noofdays = 0
leap = 0
years = 0
for i in range(1900,2001):
    years+=1
    print(i)
    j = str(i)
    if j[2]=='0' and j[3]=='0':
        if i%400==0:
            print("Leap year: ",i)
            noofdays+=366
            leap+=1
        else:
            noofdays+=365
    elif i%4==0:
        print("Leap year: ", i)
        noofdays+=366
        leap+=1
    else:
        noofdays+=365

print("Total number of days",noofdays)
print(leap," Leap years")
print(years-leap," Normal years")
print((leap*2 + (years - leap))%7)
print(time()-t)
print(2%7)