# WASTC 2016
# Sable Cantus
offset = [-5, 7, 9, 3, -2, 7, 12]
fileName = "secret.txt"

# open the input file for input
fin = open(fileName)

# start end-of-file loop
while True:
	# read a line from the input file
	sOld = fin.readline()
	if len(sOld) == 0: break
	counter = 0
	sNew = ""
	# decode the line
	for i in range(len(sOld)):
		index = counter % len(offset)
		sNew += chr(ord(sOld[i]) - offset[index])
		counter += 1
	# print the message
	print(sNew + '\n')
	
	# loop ends here

# close input file
fin.close()
