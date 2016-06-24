'''
# formatted file input
fin = open("inputs.txt")
aText = fin.readline().strip() 	#usually pull out the \n or \r\n
aFloat =float(fin.readline().strip())
aInt = int(fin.readline().strip())
# set the file close right away and then work inside
fin.close()

print (aText)
print (aFloat)
print (aInt)
'''

'''
# file input, EOF, method #1
fin = open("emails.txt")
for line in fin:
	print(line.strip())
fin.close()
'''

'''
# file input, EOF, method #2
fin = open("emails.txt")
while True:
	aText = fin.readline()
	if (aText == ''): break		# test for no line to stop at end
	print(aText.strip())

fin.close()
'''

'''
# file output - create new file
# using variable "fout" for cross lang consistency
fout = open("output.txt", "w")		# the 'w' opens for writing
									# destroys existing file
fout.write("Hello\n")				# not an automatic \n
fout.write("world\n")
fout.write("12345\n")				#output must be a str
fout.close()
'''


# file output - append
# using variable "fout" for cross lang consistency
fout = open("output.txt", "a")		# the 'a' appends to a file
fout.write("Hello2\n")				# not an automatic \n
fout.write("world2\n")
fout.write(str(12345) +"\n")				#output must be a str
fout.close()


# to make an excel file, name file .xls and add \t for tab separation
# really just a tab delimited file
# look into excel read/write libraries
fout = open("output.xls", "a")
fout.write("June 20\t110\n")
fout.write("June 21\t105\n")
fout.write("June 22\t95\n")
fout.close()




