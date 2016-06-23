import random

a = [None for i in range(100)]
n = 0                                           #size counter
r = [None for p in range(3)]
fin = open("songs.txt")                         #f in file in but this is optional what your name is
o = 0

for lineFromFile in fin:                        #end of loop
    aSong = lineFromFile.strip()                # strips control characters
    if n < len(a):
        a[n] = aSong
        n += 1
fin.close()                                     #no consequece to not closing it will close when program ends but
                                                # not accessible while py has it

while True:
    print("Play Song: [Y/N]", end="")
    y = input()
    if not y.lower() == 'y': break
    while True:                            # not sure how this while loop works
        s = random.randint(0, len(a[:n - 1]))
        for j in range(len(r)):                  # loops through r array to compare to the currently chosen song
            if not a[s] == r[j]:
                j += 1
            else: break                          # if the songs are the same, demands a new random number
        if j == len(r): break
    if o < len(r):
        r[o] = a[s]
        o += 1
    else:
        o = 0
        r[o] = a[s]
        o += 1
    print(a[s], "\n")
    print(r)

