# WASTC 2016
# Sable Cantus
'''
sOrig = input("Please enter your message to decode: ")
sNew = ""
for i in range(len(sOrig)):
	sNew += chr(ord(sOrig[i]) -1)
print (sNew)
'''

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

fileName = "secret.txt"

# open the input file for input
fin = open(fileName)

# start end-of-file loop
while True:
	# read a line from the input file
	sOld = fin.readline()
	if len(sOld) == 0: break
	sNew = ""
	# decode the line
	for i in range(len(sOld)):
		sNew += chr(ord(sOld[i]) -1)
	# print the message
	print(sNew + '\n')
	
	# loop ends here

# close input file
fin.close()
