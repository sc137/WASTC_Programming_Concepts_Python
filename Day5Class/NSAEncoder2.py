# version 1.0


fin = open('input.txt')

sDecode = ""
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

for i in range(len(encoded)):
    print(encoded[i], end="")
    i += 1

print("\n")
for i in range(len(encoded)):
    sDecode = chr(ord(encoded[i]) + 1)
    decoded[len(decoded):] = [sDecode]  # Inserts at the end
    i += 1

for i in range(len(decoded)):
    print(decoded[i], end="")
    i += 1

