a = [None for i in range(5)]
for i in range(len(a)):
  a[i] = int(input("Enter temp:"))

print("Anaheim forecast hi temps:")
print("Monday, June 20:", a[0])
print("Tuesday, June 21:", a[1])
print("Wednesday, June 22:", a[2])
print("Thursday, June 23:", a[3])
print("Friday, June 24:", a[4])
print("source: informed guessing...")

minTemp = a[0]
maxTemp = a[0]
for i in range(1, len(a)):
  if a[i] < minTemp: minTemp = a[i]
  if a[i] > maxTemp: maxTemp = a[i]

nMax,nMin = 0,0
for i in range(len(a)):
  if a[i] == minTemp: nMin += 1
  if a[i] == maxTemp: nMax += 1

print("Minimum is", minTemp, "occuring", nMin, "time(s)" \
  "\nMaximum is", maxTemp, "occuring", nMax, "time(s)")