# WASTC 2016
# Sable Cantus
'''
sOrig = input("Please enter your message: ")
sNew = ""
for i in range(len(sOrig)):
	sNew += chr(ord(sOrig[i]) +1)
print (sNew)
'''

# Requirements. Write nsaEncoder1.py based on Exercise 9.2’s nsaEncoder0.py. Prompt the user to enter the name of an existing text file to be encoded, using the encoding algorithm from nsaEncoder0.py. Read the text from the input file and encode it a line at a time, and write each line of encoded text to an output file after it’s encoded. Name the output file secret.txt.

# prompt for the input file name
fileName = input("Enter the existing file: ")

# open the input file for input
fin = open(fileName)
# open secret.txt for output
fout = open("secret.txt", "w")

# start end-of-file loop
while True:
	# read a line from the input file
	sOld = fin.readline()
	if len(sOld) == 0: break
	sNew = ""
	# encode the line
	for i in range(len(sOld)):
		sNew += chr(ord(sOld[i]) +1)
	# write the line to the output file
	fout.write(sNew + '\n')
	
	# loop ends here

# close output file
fout.close()
# close input file
fin.close()