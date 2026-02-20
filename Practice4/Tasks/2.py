from datetime import date
from datetime import datetime
#1
year = date.today().year
month = date.today().month
day = date.today().day
d = date(year, month, day + 5)
print(d)
#2
print(date(year, month, day-1), date(year, month, day),  date(year, month, day+1))
#3
hour = datetime.now().hour
minute = datetime.now().minute
second = datetime.now().second
dss = datetime(year, month, day,hour,minute,second,0)
print(dss)
#4
t1 = datetime.now()
t2 = datetime(2024, 12,14,15,13,12,12312)
dif = t1 - t2
print(dif)