# WASTC 2016
# Sable Cantus
offset = [-5, 7, 9, 3, -2, 7, 12]

# prompt for the input file name
fileName = input("Enter file to encode: ")

# open the input and output files
fin = open(fileName)
fout = open("secret.txt", "w")

# start end-of-file loop
while True:
	# read a line from the input file
	sOld = fin.readline()
	if len(sOld) == 0: break
	counter = 0
	sNew = ""
	# encode the line
	for i in range(len(sOld)):
		index = counter % len(offset)
		sNew += chr(ord(sOld[i]) + offset[index])
		counter += 1
	# write the line to the output file
	fout.write(sNew + '\n')
	
	# loop ends here

# close input and output files
fout.close()
fin.close()