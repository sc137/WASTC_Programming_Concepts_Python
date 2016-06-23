# WASTC 2016
# Sable Cantus

a = [None for i in range(5)]
n = 0 # array size (vs capacity)

while True:
	aScore = int(input("Enter a score [1-100]: "))
	
	if aScore < 0 or aScore > 100: print ("Invalid")
	else:	
		# add to the list (if there is room)
		if n < len(a):
			a[n] = aScore
			n += 1
	if n == len(a): break

print (a)