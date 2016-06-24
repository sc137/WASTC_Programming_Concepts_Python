# version 2.0

offset = [-1, 8, 9, 12, 6, 1]
fin = open('input.txt')
fout = open('secret.txt', 'w')
encoded = []
decoded = []
counter = 0
while True:
    sOld = fin.readline()
    sNew = ""
    if len(sOld) == 0:break
    for i in range(len(sOld)):
        index = counter % len(offset)
        sNew = chr(ord(sOld[i]) + offset[index])
        counter += 1
        i += 1
        encoded[len(encoded):] = [sNew]  # Inserts at the end


i = 0
while True:                 # this section is wrong and incomplete
    if i == len(encoded): break
    fout.write(encoded[i] )
    i += 1

fout.close()
fin.close()