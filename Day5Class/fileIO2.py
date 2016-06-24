#file input formated

fin = open('input.txt')
aText = fin.readline().strip()
aFloat = float(fin.readline().strip())
aInt = float(fin.readline().strip())
#fin.close()

print(aText, aFloat, aInt)

while True:
    aText = fin.readline()
    if (aText == ''): break
    print(aText.strip())
fin.close()

fout = open("output.txt", 'a') # w is write over a ia append r is read only
fout.write('Hello\n')
fout.write('World\n')
fout.write(str(12345) + '\n')
fout.close()

fout = open("output.xls", 'w') # w is write over a ia append r is read only
fout.write('June 20\t111\n')
fout.write('June 21\t100\n')
fout.write('June 22\t99\n')
fout.write('June 23\t22\n')
fout.write('June 24\t63\n')

fout.close()