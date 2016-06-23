#analogue
a = 110
b = 90
c = 82
d = 75
e = 87

print("Anaheim forcast temps: ")
print("Monday June 20:", a)
print("Tuesday June 21:", b)
print("Wednesday June 22:", c)
print("Thursday June 23:", d)
print("Friday June 24:", e)
print("Source informed guessing...,")

#array approach
a = [110, 90, 82, 75, 87]

print("Anaheim forecast temps: ")
print("Monday June 20:", a[0])
print("Tuesday June 21:", a[1])
print("Wednesday June 22:", a[2])
print("Thursday June 23:", a[3])
print("Friday June 24:", a[4])
print("Source informed guessing...,")

#linear for loop
mintemp = a[0]
maxtemp = a[0]
for i in range(len(a)):
    if a[i] < mintemp: mintemp = a[i]
    if a[i] > maxtemp: maxtemp = a[i]

print("minimum is ", mintemp, "\nMaximum is ", maxtemp)