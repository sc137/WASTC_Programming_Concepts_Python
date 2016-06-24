#version 0.0

print("Type in something to encrypt: ", end="")
sOld = input()
sNew = ""
sDecode = ""
encoded = []
decoded = []
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

