

#array approach
a = [None for i in range(5)]
for i in range(5):
    a[i] = int(input("Enter Temp: "))

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

nMax, nMin = 0, 0
for i in range(len(a)):
    if a[i] == maxtemp: nMax += 1
    if a[i] == mintemp: nMin += 1

print("minimum is ", mintemp, "\nMaximum is ", maxtemp, \
      "\nMinimum occured", nMin, "times", "Maximum occured", nMax, "times")