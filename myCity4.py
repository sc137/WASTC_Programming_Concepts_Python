# WASTC 2016
# Sable Cantus

a = [None for i in range(5)]
for i in range(len(a)):
	a[i] = int(input("Enter temp: "))
	
minTemp = a[0]
maxTemp = a[0]

for i in range(len(a)):
	if a[i] < minTemp: minTemp = a[i]
	if a[i] > maxTemp: maxTemp = a[i]
	
print ("Max temp is", maxTemp, \
		"\nMin temp is", minTemp)
		
nMax, nMin = 0, 0
for i in range(len(a)):
	if a[i] == maxTemp: nMax += 1
	if a[i] == minTemp: nMin += 1

print ("nMax occurrence:", nMax,\
		"\nnMin occurence:", nMin)