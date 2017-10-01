import time
import calendar
import datetime
'''
print "Welcome."
print "Choices-->1)CALENDAR\n2)TIMER"
month=raw_input("enter the month")
year=raw_input("enter the year")

print calendar.month(int(year),int(month))
'''
eventime='07:15:00'
print "Year"
year=raw_input("-->")

print "Month"
month=raw_input("-->")

print "Day"
day=raw_input("-->")
eventdate=day+'/'+month+'/'+year
print eventdate
todaydate=time.strftime('%d/%m/%y')
print todaydate
today=time.strftime('%I:%M:%S')
print today
while(eventdate!=todaydate):
    todaydate=time.strftime('%d/%m/%y')
    #print todaydate
#print todaydate
if(eventdate==todaydate):    
    while(today!=eventime):
        today=time.strftime('%I:%M:%S')
        print today
    if(today==eventime):
        print "yead"
        
    
    
'''
d=datetime.strftime(s)
d = datetime.strptime(s, "%d/%m/%Y %H:%M:%S")
event=time.mktime(d.timetuple())
print event

'''
