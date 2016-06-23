import random

a = [None for i in range(100)]
n = 0 #size counter
fin = open("songs.txt") #f in file in but this is optional what your name is


for lineFromFile in fin: #end of loop
    aSong = lineFromFile.strip() # strips control characters
    if n < len(a):
        a[n] = aSong
        n += 1
fin.close() #no consequece to not closing it will close when program ends but not accessible while py has it


while True:
    print("Play Song: [Y/N]", end="")
    y = input()
    if not y.lower() == 'y': break
    s = random.randint(0, len(a[:n-1]))
    print(a[s], "\n")

