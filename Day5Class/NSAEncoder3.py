# version 1.0


fin = open('input.txt')
fout = open('output.txt', 'w')
encoded = []
decoded = []

while True:
    sOld = fin.readline()
    sNew = ""
    if len(sOld) == 0:break
    for i in range(len(sOld)):
        sNew = chr(ord(sOld[i]) - 1)
        encoded[len(encoded):] = [sNew]  # Inserts at the end
        i += 1


i = 0
while True:                 # this section is wrong and incomplete
    if i == len(encoded): break
    fout.write(encoded[i] + '\n')
    i += 1

fout.close()
fin.close()


print("\n")
for i in range(len(encoded)):
    sDecode = chr(ord(encoded[i]) + 1)
    decoded[len(decoded):] = [sDecode]  # Inserts at the end
    i += 1

for i in range(len(decoded)):
    print(decoded[i], end="")
    i += 1

