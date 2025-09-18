# EG 2nd Booleans Notes!

import time
import datetime as date

over = False

print(over)

name = "Emma"

print(bool(name))


current_time = time.time()
readable_time = time.ctime(current_time)

print(f"Current Time in seconds since January 1, 1970(epoch time): {current_time}")
print(f"Current Time: {readable_time}")

now= date.datetime.today()
hour = now.strftime("%H")
# Month = %m ( %b, %B )
# Day = %d
# Year = %Y, %y
# Hour = %H
# minutes = %M
# seconds = %S

print(f"Current time according to datetime: {now}")
print(f"Hour: {hour}")
print(f"My hour variable is a String: {isinstance(hour, str)}")
print(f"My hour variable is a Integer: {isinstance(hour, int)}")
print(f"My hour variable is a Float: {isinstance(hour, float)}")