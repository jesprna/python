c = input("Enter the temperature in celcius: ")
c = int(c) 
f = (9/5) + c + 32

f = int(f)
print(f)

m = input("Enter the number of minutes")
m = int(m)
mHour = m/60

seconds = input("Enter a number in seconds");
seconds = int(seconds)
sHour = seconds/3600

hour = mHour +  sHour
print(hour)