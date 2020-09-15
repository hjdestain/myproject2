# Week: 1
# Lesson: Python Dates and Times
# Date Started: 19 May 2020
# Date Finished: 19 May 2020


import datetime as dt
import time as tm

# show the current time since epoch
print(tm.time())

# convert the time to year/month/etc.
dtnow = dt.datetime.fromtimestamp(tm.time())
print(dtnow)

# print the values individually
print(dtnow.year)
print(dtnow.month)
print(dtnow.day)
print(dtnow.hour)
print(dtnow.minute)
print(dtnow.second)

# you can also use the date object to get today's date
today = dt.date.today()
print(today)

# time deltas allow for comparisons and establishment of time intervals
delta = dt.timedelta(days = 30)
print(today - delta)







