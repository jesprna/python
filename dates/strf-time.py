import datetime

x= datetime.datetime.now()
y = datetime.datetime(2020, 3, 18)


print(x.year)
print(x.month)
print(x.day)
print(x.hour)
print(x.minute)
print(x.second)

print("__________________")

print(x.strftime("%B"))
print(x.strftime("%A"))
print(x.strftime("%a"))

print(x.strftime("%A, %d %B %Y"))


print("__________________")
print(y)
print(y.month)

# %b: Returns the first three characters of the month name. In our example, it returned "Sep"
# %d: Returns day of the month, from 1 to 31. In our example, it returned "15".
# %Y: Returns the year in four-digit format. In our example, it returned "2018".
# %H: Returns the hour. In our example, it returned "00".
# %M: Returns the minute, from 00 to 59. In our example, it returned "00".
# %S: Returns the second, from 00 to 59. In our example, it returned "00".


# %a: Returns the first three characters of the weekday, e.g. Wed.
# %A: Returns the full name of the weekday, e.g. Wednesday.
# %B: Returns the full name of the month, e.g. September.
# %w: Returns the weekday as a number, from 0 to 6, with Sunday being 0.
# %m: Returns the month as a number, from 01 to 12.
# %p: Returns AM/PM for time.
# %y: Returns the year in two-digit format, that is, without the century. For example, "18" instead of "2018".
# %f: Returns microsecond from 000000 to 999999.
# %Z: Returns the timezone.
# %z: Returns UTC offset.
# %j: Returns the number of the day in the year, from 001 to 366.
# %W: Returns the week number of the year, from 00 to 53, with Monday being counted as the first day of the week.
# %U: Returns the week number of the year, from 00 to 53, with Sunday counted as the first day of each week.
# %c: Returns the local date and time version.
# %x: Returns the local version of date.
# %X: Returns the local version of time.

